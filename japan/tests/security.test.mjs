import { test, before } from 'node:test'
import assert from 'node:assert/strict'
import { createApp } from '../server/app.mjs'
import {
  passwordHash,
  verifyPassword,
  random,
  config,
  sign,
  verify,
  cookie,
  COOKIE,
  CSRF_COOKIE,
  readCookie,
  SESSION_SECONDS,
} from '../server/security.mjs'
import { fixture, MemoryStore, testPassword, addition } from './fixture.mjs'

let env
before(async () => {
  env = {
    VERCEL: '1',
    VERCEL_ENV: 'production',
    JAPAN_PASSWORD_HASH: await passwordHash(testPassword),
    JAPAN_SESSION_KEY: random(),
    JAPAN_REDIS_PREFIX: 'unit',
  }
})
async function setup() {
  const store = new MemoryStore()
  await store.set('baseline', JSON.stringify(fixture()))
  await store.set('collaboration', JSON.stringify({ revision: 0, points: [] }))
  return { store, app: createApp({ env, store }) }
}
const request = (path, options = {}, host = 'phymani.me') =>
  new Request(`https://${host}${path}`, options)
async function login(app, password = testPassword, ip = '192.0.2.1') {
  const page = await app(request('/japan'))
  const csrf = (await page.text()).match(/name="csrf" value="([^"]+)"/)[1]
  const result = await app(
    request('/japan/auth', {
      method: 'POST',
      headers: {
        origin: 'https://phymani.me',
        'content-type': 'application/x-www-form-urlencoded',
        cookie: `${CSRF_COOKIE}=${csrf}`,
        'x-vercel-forwarded-for': ip,
      },
      body: new URLSearchParams({ csrf, password }),
    }),
  )
  return {
    result,
    sessionCookie: result.headers
      .getSetCookie()
      .find((c) => c.startsWith(`${COOKIE}=`))
      ?.split(';')[0],
    csrf,
  }
}
test('scrypt uses random salt; valid password only; secret configuration rejects empty values', async () => {
  assert.match(env.JAPAN_PASSWORD_HASH, /^scrypt\$131072\$8\$1/)
  assert.equal(await verifyPassword(testPassword, env.JAPAN_PASSWORD_HASH), true)
  assert.equal(await verifyPassword('wrong-test-password', env.JAPAN_PASSWORD_HASH), false)
  assert.notEqual(await passwordHash(testPassword), env.JAPAN_PASSWORD_HASH)
  assert.throws(() => config({}))
})
test('JWT checks signature, expiry and audience without exposing password fingerprints; cookie is path-compatible', async () => {
  const cfg = config(env),
    token = await sign({ jti: random() }, cfg, 'session', 1, Date.now() - 5000)
  assert.equal(await verify(token, cfg, 'session'), null)
  const fresh = await sign({ jti: random() }, cfg, 'session', SESSION_SECONDS)
  assert.ok(await verify(fresh, cfg, 'session'))
  assert.equal(await verify(fresh + 'x', cfg, 'session'), null)
  assert.equal(await verify(fresh, cfg, 'csrf'), null)
  const decoded = JSON.parse(Buffer.from(fresh.split('.')[1], 'base64url').toString())
  assert.equal(decoded.version, undefined)
  assert.ok(!JSON.stringify(decoded).includes(cfg.version))
  const value = cookie(COOKIE, 'test', SESSION_SECONDS)
  for (const field of ['Secure', 'HttpOnly', 'SameSite=Strict', 'Path=/japan', 'Max-Age=43200'])
    assert.ok(value.includes(field))
  assert.ok(!value.includes('Domain='))
  assert.equal(readCookie(`${COOKIE}=a; ${COOKIE}=b`, COOKIE), '')
})
test('unauthorized HTML has only login; every private route and asset rejects missing credentials', async () => {
  const { app } = await setup()
  const page = await app(request('/japan'))
  const content = await page.text()
  assert.equal(page.status, 200)
  assert.match(content, /type="password"/)
  assert.ok(!content.includes('SYNTHETIC_SECRET'))
  assert.ok(!content.includes('<script'))
  for (const path of [
    '/japan/data',
    '/japan/export/geojson',
    '/japan/export/kml',
    '/japan/assets/app.js',
    '/japan/assets/app.css',
    '/japan/collaboration',
    '/japan/history',
    '/japan/index.html',
    '/japan/trip_data.json',
  ]) {
    const result = await app(request(path))
    assert.equal(result.status, 401, path)
    assert.match(result.headers.get('cache-control'), /private, no-store/)
  }
})
test('canonical host, aliases, encoded paths and previews cannot bypass protection', async () => {
  const { app, store } = await setup()
  assert.equal((await app(request('/japan/'))).headers.get('location'), '/japan')
  assert.equal(
    (await app(request('/japan', {}, 'www.phymani.me'))).headers.get('location'),
    'https://phymani.me/japan',
  )
  for (const path of [
    '/japan.html',
    '/api/japan',
    '/japanese',
    '/japan//data',
    '/japan/%64ata',
    '/%6aapan/data',
    '/japan?password=test',
  ])
    assert.ok([400, 404].includes((await app(request(path))).status), path)
  for (const host of ['example.vercel.app', 'preview.example.com', 'phymani.me.attacker.test'])
    assert.equal((await app(request('/japan/data', {}, host))).status, 404)
  const preview = createApp({ env: { ...env, VERCEL_ENV: 'preview' }, store })
  assert.equal((await preview(request('/japan'))).status, 404)
})
test('origin and CSRF are mandatory on auth, logout and edits', async () => {
  const { app } = await setup()
  for (const origin of ['', 'https://evil.test', 'null']) {
    const result = await app(
      request('/japan/auth', {
        method: 'POST',
        headers: { origin, 'content-type': 'application/x-www-form-urlencoded' },
        body: 'password=test',
      }),
    )
    assert.equal(result.status, 403)
  }
  const { result, sessionCookie } = await login(app)
  assert.equal(result.status, 303)
  const badLogout = await app(
    request('/japan/logout', {
      method: 'POST',
      headers: {
        origin: 'https://phymani.me',
        cookie: sessionCookie,
        'content-type': 'application/x-www-form-urlencoded',
      },
      body: 'csrf=bad',
    }),
  )
  assert.equal(badLogout.status, 403)
  const badEdit = await app(
    request('/japan/collaboration', {
      method: 'POST',
      headers: {
        origin: 'https://phymani.me',
        cookie: sessionCookie,
        'content-type': 'application/json',
      },
      body: '{}',
    }),
  )
  assert.equal(badEdit.status, 403)
})
test('wrong passwords are uniformly rejected, and the store-backed rate limiter blocks the eleventh attempt', async () => {
  const { app, store } = await setup()
  const failed = await login(app, 'wrong-test-password')
  assert.equal(failed.result.status, 401)
  assert.match(await failed.result.text(), /密码不正确或登录失败/)
  const { ipKey } = await import('../server/security.mjs')
  await store.set(`limit:ip:${ipKey('192.0.2.1', config(env))}`, 10, 900)
  const limited = await login(app)
  assert.equal(limited.result.status, 429)
  assert.equal(limited.result.headers.get('retry-after'), '900')
})
test('authenticated reads are never reusable by a fresh client; logout revokes captured tokens', async () => {
  const { app } = await setup(),
    { sessionCookie } = await login(app)
  for (const path of ['/japan', '/japan/data', '/japan/export/geojson', '/japan/export/kml']) {
    const result = await app(request(path, { headers: { cookie: sessionCookie } }))
    assert.equal(result.status, 200)
    assert.equal(result.headers.get('cache-control'), 'private, no-store')
    assert.equal(result.headers.get('vercel-cdn-cache-control'), 'no-store')
    const fresh = await app(request(path))
    assert.ok(!(await fresh.text()).includes('SYNTHETIC_SECRET'))
  }
  const page = await app(request('/japan', { headers: { cookie: sessionCookie } }))
  const csrf = (await page.text()).match(/name="japan-csrf" content="([^"]+)"/)[1]
  const logout = await app(
    request('/japan/logout', {
      method: 'POST',
      headers: {
        cookie: sessionCookie,
        origin: 'https://phymani.me',
        'content-type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({ csrf }),
    }),
  )
  assert.equal(logout.status, 303)
  assert.equal(
    (await app(request('/japan/data', { headers: { cookie: sessionCookie } }))).status,
    401,
  )
})
test('missing secrets and failed persistent store fail closed', async () => {
  const { store } = await setup()
  for (const key of ['JAPAN_PASSWORD_HASH', 'JAPAN_SESSION_KEY', 'JAPAN_REDIS_PREFIX']) {
    const app = createApp({ env: { ...env, [key]: '' }, store })
    assert.equal((await app(request('/japan/data'))).status, 503)
  }
  const app = createApp({
    env,
    store: {
      get: () => {
        throw new Error('offline')
      },
    },
  })
  const result = await app(request('/japan'))
  assert.equal(result.status, 503)
  assert.ok(!(await result.text()).includes('offline'))
})
test('HTTP private reads reject tampered, expired and password-rotated sessions', async () => {
  const { app, store } = await setup()
  const { sessionCookie } = await login(app)
  assert.equal(
    (await app(request('/japan/data', { headers: { cookie: sessionCookie + 'tampered' } }))).status,
    401,
  )
  const expired = await sign({ jti: random() }, config(env), 'session', 1, Date.now() - 10000)
  assert.equal(
    (await app(request('/japan/data', { headers: { cookie: `${COOKIE}=${expired}` } }))).status,
    401,
  )
  const rotatedEnv = {
    ...env,
    JAPAN_PASSWORD_HASH: await passwordHash('different-independent-test-passphrase!'),
  }
  const rotated = createApp({ env: rotatedEnv, store })
  assert.equal(
    (await rotated(request('/japan/data', { headers: { cookie: sessionCookie } }))).status,
    401,
  )
})
test('collaboration supports safe additions, owner credentials, revision conflicts and private history', async () => {
  const { app } = await setup(),
    { sessionCookie } = await login(app)
  const page = await app(request('/japan', { headers: { cookie: sessionCookie } }))
  const csrf = (await page.text()).match(/name="japan-csrf" content="([^"]+)"/)[1]
  const post = (value) =>
    app(
      request('/japan/collaboration', {
        method: 'POST',
        headers: {
          cookie: sessionCookie,
          origin: 'https://phymani.me',
          'content-type': 'application/json',
          'x-csrf-token': csrf,
        },
        body: JSON.stringify(value),
      }),
    )
  const result = await post({ revision: 0, point: addition() })
  assert.equal(result.status, 200)
  const saved = await result.json()
  assert.equal((await post({ revision: 0, point: addition() })).status, 409)
  assert.equal(
    (await post({ revision: 1, id: saved.id, editToken: 'wrong', point: addition() })).status,
    403,
  )
  assert.equal(
    (await post({ revision: 1, id: 'a', editToken: saved.editToken, point: addition() })).status,
    403,
  )
  assert.equal(
    (
      await post({
        revision: 1,
        id: saved.id,
        editToken: saved.editToken,
        point: { ...addition(), name: 'Updated synthetic place' },
      })
    ).status,
    200,
  )
  assert.equal(
    (await post({ revision: 2, point: { ...addition(), source_url: 'javascript:alert(1)' } }))
      .status,
    400,
  )
  const data = await (
    await app(request('/japan/data', { headers: { cookie: sessionCookie } }))
  ).json()
  assert.equal(data.points.length, 4)
  assert.equal(data.collaborationRevision, 2)
  assert.ok(!JSON.stringify(data).includes('editHash'))
  const history = await (
    await app(request('/japan/history', { headers: { cookie: sessionCookie } }))
  ).json()
  assert.equal(history.length, 2)
  assert.ok(!JSON.stringify(history).includes('editHash'))
})
