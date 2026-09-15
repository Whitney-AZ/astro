import { readFile } from 'node:fs/promises'
import { isIP } from 'node:net'
import {
  config,
  cookie,
  COOKIE,
  CSRF_COOKIE,
  readCookie,
  sign,
  verify,
  random,
  digest,
  equal,
  verifyPassword,
  SESSION_SECONDS,
  ipKey,
} from './security.mjs'
import { RedisStore } from './store.mjs'
import { loginPage, mapPage } from './pages.mjs'
import { assertTrip, geojson, kml } from '../shared/model.mjs'
import { editAddition, publicCollaboration } from './collaboration.mjs'

const canonical = 'https://phymani.me'
const baseHeaders = {
  'Cache-Control': 'private, no-store',
  'CDN-Cache-Control': 'no-store',
  'Vercel-CDN-Cache-Control': 'no-store',
  'X-Robots-Tag': 'noindex, noarchive, nosnippet',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'same-origin',
  'X-Frame-Options': 'DENY',
  'Content-Security-Policy':
    "default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://cyberjapandata.gsi.go.jp; connect-src 'self'; font-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'; object-src 'none'",
  'Permissions-Policy': 'geolocation=(), camera=(), microphone=()',
  Vary: 'Cookie, Host',
}
function response(body, status = 200, headers = {}) {
  return new Response(body, { status, headers: { ...baseHeaders, ...headers } })
}
const json = (body, status = 200) =>
  response(JSON.stringify(body), status, { 'Content-Type': 'application/json; charset=utf-8' })
const html = (body, status = 200) =>
  response(body, status, { 'Content-Type': 'text/html; charset=utf-8' })
const redirect = (path, status = 303) => response(null, status, { Location: path })
async function body(request) {
  if (Number(request.headers.get('content-length') || 0) > 16000) throw new Error('Body too large')
  const reader = request.body?.getReader()
  if (!reader) return ''
  let size = 0
  const chunks = []
  for (;;) {
    const { done, value } = await reader.read()
    if (done) break
    size += value.length
    if (size > 16000) {
      await reader.cancel()
      throw new Error('Body too large')
    }
    chunks.push(value)
  }
  return Buffer.concat(chunks).toString('utf8')
}
export function createApp({
  env = process.env,
  store: suppliedStore,
  assets = new URL('../../.japan-build/', import.meta.url),
  localOrigin,
} = {}) {
  return async function handle(request, connection = {}) {
    try {
      const url = new URL(request.url)
      const local =
        env.VERCEL !== '1' &&
        env.NODE_ENV !== 'production' &&
        localOrigin &&
        url.origin === localOrigin
      // Preview and raw deployment hosts are denied even if production secrets are inherited.
      if (
        !local &&
        (env.VERCEL_ENV !== 'production' || !['phymani.me', 'www.phymani.me'].includes(url.host))
      )
        return response('Not found', 404)
      const rawPath = url.pathname
      if (/%|\\|\/\/|[\u0000-\u0020]/.test(rawPath)) return response('Not found', 404)
      if (rawPath !== '/japan' && !rawPath.startsWith('/japan/')) return response('Not found', 404)
      if (url.host === 'www.phymani.me')
        return request.method === 'GET' || request.method === 'HEAD'
          ? redirect(`${canonical}/japan`, 308)
          : response('Not found', 404)
      if (rawPath === '/japan/')
        return request.method === 'GET' || request.method === 'HEAD'
          ? redirect('/japan', 308)
          : response('Not found', 404)
      if (!local && url.protocol !== 'https:') return response('HTTPS required', 400)
      if (url.search) return response('Query strings are not accepted', 400)
      if (!['GET', 'POST', 'HEAD'].includes(request.method))
        return response('Method not allowed', 405, { Allow: 'GET, HEAD, POST' })
      let cfg, store
      try {
        cfg = config(env)
        store = suppliedStore || new RedisStore(env)
      } catch {
        return rawPath === '/japan'
          ? html(loginPage(null), 503)
          : json({ error: '服务暂不可用。' }, 503)
      }
      const now = Date.now()
      const sessionToken = readCookie(request.headers.get('cookie'), COOKIE)
      const payload = await verify(sessionToken, cfg, 'session', now)
      let session = null
      if (payload?.jti && /^[\w-]{43}$/.test(payload.jti)) {
        const stored = await store.get(`session:${digest(payload.jti)}`)
        if (stored) {
          const candidate = JSON.parse(stored)
          if (candidate.version === cfg.version && candidate.expires > now) session = candidate
        }
      }
      if (request.method === 'POST') {
        if (
          request.headers.get('origin') !== (local ? localOrigin : canonical) ||
          request.headers.get('sec-fetch-site') === 'cross-site'
        )
          return json({ error: '请求来源无效。' }, 403)
      }
      if (rawPath === '/japan' && ['GET', 'HEAD'].includes(request.method)) {
        if (session) return html(request.method === 'HEAD' ? null : mapPage(session.csrf))
        // Storage must be reachable before showing a usable login form.
        if (!(await store.get('baseline'))) return html(loginPage(null), 503)
        const token = await sign({ nonce: random() }, cfg, 'csrf', 600)
        const res = html(request.method === 'HEAD' ? null : loginPage(token))
        res.headers.append('Set-Cookie', cookie(CSRF_COOKIE, token, 600))
        return res
      }
      if (rawPath === '/japan/auth' && request.method === 'POST') {
        if (!request.headers.get('content-type')?.startsWith('application/x-www-form-urlencoded'))
          return json({ error: '表单无效。' }, 400)
        const form = new URLSearchParams(await body(request))
        const csrf = form.get('csrf')
        if (
          form.getAll('csrf').length !== 1 ||
          form.getAll('password').length !== 1 ||
          !equal(csrf, readCookie(request.headers.get('cookie'), CSRF_COOKIE)) ||
          !(await verify(csrf, cfg, 'csrf'))
        )
          return json({ error: '表单已失效，请重新打开登录页。' }, 403)
        const ip = local
          ? connection.ip || '127.0.0.1'
          : request.headers.get('x-vercel-forwarded-for')?.trim()
        if (!ip || !isIP(ip)) return json({ error: '服务暂不可用。' }, 503)
        const attempts = await store.hit(`ip:${ipKey(ip, cfg)}`, 900)
        const globalAttempts = await store.hit('global', 900)
        if (attempts > 10 || globalAttempts > 120)
          return response('尝试过多，请 15 分钟后重试。', 429, { 'Retry-After': '900' })
        if (!(await verifyPassword(form.get('password'), cfg.hash)))
          return html(loginPage(csrf, '密码不正确或登录失败。'), 401)
        if (!(await store.get('baseline')) || !(await store.get('collaboration')))
          return html(loginPage(null), 503)
        // Remove the old login's server-side session if the browser signs in again.
        if (session && payload?.jti) await store.del(`session:${digest(payload.jti)}`)
        const id = random()
        const sessionData = {
          csrf: random(),
          version: cfg.version,
          expires: now + SESSION_SECONDS * 1000,
        }
        await store.set(`session:${digest(id)}`, JSON.stringify(sessionData), SESSION_SECONDS)
        const token = await sign({ jti: id }, cfg, 'session', SESSION_SECONDS)
        const res = redirect('/japan')
        res.headers.append('Set-Cookie', cookie(COOKIE, token, SESSION_SECONDS))
        res.headers.append('Set-Cookie', cookie(CSRF_COOKIE, '', 0))
        return res
      }
      if (!session) return json({ error: '请重新登录。' }, 401)
      if (rawPath === '/japan/logout' && request.method === 'POST') {
        if (!request.headers.get('content-type')?.startsWith('application/x-www-form-urlencoded'))
          return json({ error: '表单无效。' }, 400)
        const form = new URLSearchParams(await body(request))
        if (form.getAll('csrf').length !== 1 || !equal(form.get('csrf'), session.csrf))
          return json({ error: '表单无效。' }, 403)
        await store.del(`session:${digest(payload.jti)}`)
        const res = redirect('/japan')
        res.headers.append('Set-Cookie', cookie(COOKIE, '', 0))
        res.headers.append('Set-Cookie', cookie(CSRF_COOKIE, '', 0))
        return res
      }
      if (rawPath === '/japan/session' && request.method === 'GET')
        return json({ expires: session.expires })
      const assetName = {
        '/japan/assets/app.js': ['app.js', 'text/javascript'],
        '/japan/assets/app.css': ['app.css', 'text/css'],
      }[rawPath]
      if (assetName && request.method === 'GET')
        return response(await readFile(new URL(assetName[0], assets)), 200, {
          'Content-Type': `${assetName[1]}; charset=utf-8`,
        })
      if (
        [
          '/japan/data',
          '/japan/export/geojson',
          '/japan/export/kml',
          '/japan/collaboration',
          '/japan/history',
        ].includes(rawPath)
      ) {
        if (rawPath === '/japan/collaboration' && request.method === 'POST') {
          if (!equal(request.headers.get('x-csrf-token'), session.csrf))
            return json({ error: '请求无效。' }, 403)
          if (!request.headers.get('content-type')?.startsWith('application/json'))
            return json({ error: '请求格式无效。' }, 400)
          if ((await store.hit(`edit:${digest(payload.jti)}`, 3600)) > 60)
            return response('更新过于频繁。', 429, { 'Retry-After': '3600' })
          const data = assertTrip(JSON.parse(await store.get('baseline')))
          let input
          try {
            input = JSON.parse(await body(request))
            validateInputObject(input)
          } catch {
            return json({ error: '请求格式无效。' }, 400)
          }
          let result
          try {
            result = await editAddition(store, input, data, payload.jti)
          } catch (e) {
            if (
              [
                'Invalid field',
                'Name and nickname required',
                'WGS84 coordinates required',
                'Date required',
                'Category or region',
                'Variant',
                'Source URL',
              ].includes(e.message)
            )
              return json({ error: '请核对必填项、日期、经纬度及来源网址。' }, 400)
            throw e
          }
          return json(result.body, result.status)
        }
        if (request.method !== 'GET') return response('Method not allowed', 405)
        if (rawPath === '/japan/history') {
          const history = (await store.history())
            .map((v) => JSON.parse(v))
            .map(({ session: ignored, point, previous, ...h }) => ({
              ...h,
              point: publicCollaboration({ revision: 0, points: [point] }).points[0],
              previous: previous
                ? publicCollaboration({ revision: 0, points: [previous] }).points[0]
                : null,
            }))
          return json(history)
        }
        const data = assertTrip(JSON.parse(await store.get('baseline')))
        const additions = publicCollaboration(JSON.parse(await store.get('collaboration')))
        if (rawPath === '/japan/collaboration') return json(additions)
        const combined = {
          ...data,
          points: [...data.points, ...additions.points],
          collaborationRevision: additions.revision,
        }
        if (rawPath === '/japan/data') return json(combined)
        const isGeo = rawPath.endsWith('geojson')
        return response(isGeo ? JSON.stringify(geojson(combined)) : kml(combined), 200, {
          'Content-Type': isGeo
            ? 'application/geo+json; charset=utf-8'
            : 'application/vnd.google-earth.kml+xml; charset=utf-8',
          'Content-Disposition': `attachment; filename="trip.${isGeo ? 'geojson' : 'kml'}"`,
        })
      }
      return response('Not found', 404)
    } catch {
      return json({ error: '服务暂不可用，请稍后重试。' }, 503)
    }
  }
}
function validateInputObject(input) {
  if (
    !input ||
    !Number.isSafeInteger(input.revision) ||
    !input.point ||
    typeof input.point !== 'object'
  )
    throw new Error('Input')
}
