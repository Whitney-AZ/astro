import { createApp } from './app.mjs'
const app = createApp({ assets: new URL('./assets/', import.meta.url) })
export default async function handler(req, res) {
  try {
    const host = req.headers.host || ''
    if (!/^(phymani\.me|www\.phymani\.me)$/.test(host)) {
      res.writeHead(404, {
        'Cache-Control': 'private, no-store',
        'X-Robots-Tag': 'noindex, noarchive, nosnippet',
      })
      res.end('Not found')
      return
    }
    const headers = new Headers()
    for (const [name, value] of Object.entries(req.headers))
      if (value !== undefined) headers.set(name, Array.isArray(value) ? value.join(', ') : value)
    const request = new Request(`https://${host}${req.url}`, {
      method: req.method,
      headers,
      ...(['GET', 'HEAD'].includes(req.method) ? {} : { body: req, duplex: 'half' }),
    })
    const result = await app(request)
    res.statusCode = result.status
    for (const [name, value] of result.headers)
      if (name !== 'set-cookie') res.setHeader(name, value)
    const cookies = result.headers.getSetCookie()
    if (cookies.length) res.setHeader('Set-Cookie', cookies)
    res.end(Buffer.from(await result.arrayBuffer()))
  } catch {
    res.writeHead(503, {
      'Cache-Control': 'private, no-store',
      'X-Robots-Tag': 'noindex, noarchive, nosnippet',
    })
    res.end('Unavailable')
  }
}
