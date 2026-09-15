import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'
import { createClient } from '@redis/client'
import { createApp } from '../../japan/server/app.mjs'
import { passwordHash, random } from '../../japan/server/security.mjs'
import { fixture, testPassword } from '../../japan/tests/fixture.mjs'
import { LocalRedisStore } from '../../japan/tests/local-store.mjs'

if (process.env.VERCEL || process.env.NODE_ENV === 'production')
  throw new Error('Local test runner cannot run in production')
const port = Number(process.env.JAPAN_TEST_PORT || 8788),
  origin = `http://localhost:${port}`
const client = createClient({ url: process.env.JAPAN_TEST_REDIS_URL || 'redis://127.0.0.1:6397' })
client.on('error', () => {})
await client.connect()
const store = new LocalRedisStore(client, process.env.JAPAN_TEST_PREFIX || 'japan-local-qa')
const data =
  process.env.JAPAN_TEST_REAL === '1'
    ? JSON.parse(await readFile('.private/japan/trip.json', 'utf8'))
    : fixture()
await store.set('baseline', JSON.stringify(data))
if (!(await store.get('collaboration')))
  await store.set('collaboration', JSON.stringify({ revision: 0, points: [] }))
const env = {
  JAPAN_PASSWORD_HASH: await passwordHash(testPassword),
  JAPAN_SESSION_KEY: random(),
  JAPAN_REDIS_PREFIX: 'local',
  NODE_ENV: 'development',
}
const app = createApp({
  env,
  store,
  localOrigin: origin,
  assets: new URL('../../.japan-build/', import.meta.url),
})
const server = createServer(async (req, res) => {
  try {
    const headers = new Headers()
    for (const [key, value] of Object.entries(req.headers))
      if (value) headers.set(key, Array.isArray(value) ? value.join(', ') : value)
    const request = new Request(`${origin}${req.url}`, {
      method: req.method,
      headers,
      ...(['GET', 'HEAD'].includes(req.method) ? {} : { body: req, duplex: 'half' }),
    })
    const result = await app(request, { ip: req.socket.remoteAddress || '127.0.0.1' })
    res.statusCode = result.status
    for (const [key, value] of result.headers) if (key !== 'set-cookie') res.setHeader(key, value)
    const cookies = result.headers.getSetCookie()
    if (cookies.length) res.setHeader('Set-Cookie', cookies)
    res.end(Buffer.from(await result.arrayBuffer()))
  } catch {
    res.writeHead(503)
    res.end('Local server unavailable')
  }
})
server.listen(port, '127.0.0.1', () =>
  console.log(
    `Local private map test server: ${origin}/japan (independent test password; Redis persistence enabled)`,
  ),
)
process.on('SIGTERM', () =>
  server.close(async () => {
    await client.quit()
    process.exit(0)
  }),
)
