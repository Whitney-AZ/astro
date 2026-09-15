import { test } from 'node:test'
import assert from 'node:assert/strict'
import { createClient } from '@redis/client'
import { LocalRedisStore } from './local-store.mjs'
import { editAddition } from '../server/collaboration.mjs'
import { fixture, addition } from './fixture.mjs'

test(
  'REAL Redis: parallel limit increments, TTL, CAS conflict and shared state between independent clients',
  { skip: !process.env.JAPAN_TEST_REDIS_URL },
  async () => {
    const a = createClient({ url: process.env.JAPAN_TEST_REDIS_URL }),
      b = createClient({ url: process.env.JAPAN_TEST_REDIS_URL })
    await Promise.all([a.connect(), b.connect()])
    const prefix = `test-${Date.now()}`,
      first = new LocalRedisStore(a, prefix),
      second = new LocalRedisStore(b, prefix)
    try {
      const hits = await Promise.all(
        Array.from({ length: 30 }, (_, i) => (i % 2 ? first : second).hit('concurrent', 900)),
      )
      assert.equal(new Set(hits).size, 30)
      assert.equal(Math.max(...hits), 30)
      assert.ok((await a.ttl(first.key('limit:concurrent'))) > 0)
      await first.set('collaboration', JSON.stringify({ revision: 0, points: [] }))
      const results = await Promise.all([
        editAddition(first, { revision: 0, point: addition() }, fixture(), 'test-session-a'),
        editAddition(second, { revision: 0, point: addition() }, fixture(), 'test-session-b'),
      ])
      assert.deepEqual(results.map((r) => r.status).sort(), [200, 409])
      assert.equal(JSON.parse(await second.get('collaboration')).points.length, 1)
      assert.equal((await first.history()).length, 1)
      await first.set('session-test', 'active', 43200)
      assert.equal(await second.get('session-test'), 'active')
      await second.del('session-test')
      assert.equal(await first.get('session-test'), null)
    } finally {
      const keys = await a.keys(`${prefix}:*`)
      if (keys.length) await a.del(keys)
      await Promise.all([a.quit(), b.quit()])
    }
  },
)
