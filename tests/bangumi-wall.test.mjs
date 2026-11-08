import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { transform } from 'esbuild'

// Exercise the actual TypeScript module without adding a runtime dependency.
const source = await readFile(new URL('../src/lib/bangumi-wall.ts', import.meta.url), 'utf8')
const { code } = await transform(source, { loader: 'ts', format: 'esm' })
const { fetchPublicCollections, toWallItem, selectItems } = await import(
  `data:text/javascript;base64,${Buffer.from(code).toString('base64')}`
)

function collection(id, overrides = {}) {
  return {
    subject_id: id, subject_type: 2, type: 3, private: false,
    subject: { name: `Original ${id}`, name_cn: `作品 ${id}`, images: { common: 'https://lain.bgm.tv/test.jpg' }, score: 7.5 },
    updated_at: '2026-11-08T10:00:00+08:00', ...overrides,
  }
}

test('fetches every page, bounds concurrency, and never sends credentials', async () => {
  const offsets = []
  let inFlight = 0, maximum = 0
  const request = async (url, options) => {
    const parsed = new URL(url)
    assert.equal(parsed.origin, 'https://api.bgm.tv')
    assert.equal(options.credentials, 'omit')
    assert.equal(options.headers.Authorization, undefined)
    const offset = Number(parsed.searchParams.get('offset'))
    offsets.push(offset)
    inFlight++; maximum = Math.max(maximum, inFlight)
    await new Promise((resolve) => setTimeout(resolve, 2))
    inFlight--
    return Response.json({ total: 202, limit: 50, data: Array.from({ length: Math.min(50, 202 - offset) }, (_, i) => collection(offset + i + 1)) })
  }
  const result = await fetchPublicCollections('857721', request)
  assert.equal(result.length, 202)
  assert.deepEqual(offsets, [0, 50, 100, 150, 200])
  assert.ok(maximum <= 3)
})

test('rejects failed or malformed pages instead of publishing partial collections', async () => {
  await assert.rejects(fetchPublicCollections('857721', async (url) => {
    const offset = Number(new URL(url).searchParams.get('offset'))
    return offset ? new Response('unavailable', { status: 503 })
      : Response.json({ total: 51, limit: 50, data: Array.from({ length: 50 }, (_, i) => collection(i + 1)) })
  }), /503/)
  await assert.rejects(fetchPublicCollections('857721', async () => Response.json({ total: 5, limit: 50, data: [] })), /Incomplete/)
  await assert.rejects(fetchPublicCollections('857721', async () => Response.json({ total: '5', data: [] })), /Invalid/)
  assert.deepEqual(await fetchPublicCollections('857721', async () => Response.json({ total: 0, limit: 50, data: [] })), [])
})

test('excludes private and invalid entries, sanitizes covers, and deduplicates IDs', async () => {
  assert.equal(toWallItem(collection(1, { private: true })), null)
  assert.equal(toWallItem(collection(-1)), null)
  assert.equal(toWallItem(collection(1, { subject: null })), null)
  const unsafe = toWallItem(collection(1, { subject: { name: 'Missing', images: { common: 'javascript:alert(1)' } } }))
  assert.equal(unsafe.cover, null)
  assert.equal(unsafe.rate, null)
  const result = await fetchPublicCollections('857721', async () => Response.json({ total: 3, limit: 50, data: [collection(1), collection(1), collection(2, { private: true })] }))
  assert.equal(result.length, 1)
})

const defaults = { types: [], statuses: [], query: '', sort: 'updatedAt', ascending: false }
test('combines category, state and multilingual search without mutating the snapshot', () => {
  const items = [toWallItem(collection(1)), toWallItem(collection(2, { subject_type: 1, type: 2 }))]
  assert.deepEqual(selectItems(items, { ...defaults, types: [1], statuses: [2], query: ' ORIGINAL 2 ' }).map((item) => item.id), [2])
  assert.equal(selectItems(items, { ...defaults, types: [1], statuses: [3] }).length, 0)
  assert.deepEqual(selectItems(items, { ...defaults, query: '作品 1' }).map((item) => item.id), [1])
  assert.deepEqual(items.map((item) => item.id), [1, 2])
})

test('sorts ratings and ranks with missing values last in both directions', () => {
  const items = [toWallItem(collection(1, { rate: 0 })), toWallItem(collection(2, { rate: 9 })), toWallItem(collection(3, { rate: 7 }))]
  assert.deepEqual(selectItems(items, { ...defaults, sort: 'rate' }).map((item) => item.id), [2, 3, 1])
  assert.deepEqual(selectItems(items, { ...defaults, sort: 'rate', ascending: true }).map((item) => item.id), [3, 2, 1])
  items[1].rank = 10; items[2].rank = 100
  assert.deepEqual(selectItems(items, { ...defaults, sort: 'rank', ascending: true }).map((item) => item.id), [2, 3, 1])
})

test('sorts collection timestamps chronologically across time zones', () => {
  const items = [toWallItem(collection(1, { updated_at: '2026-11-08T10:00:00+08:00' })), toWallItem(collection(2, { updated_at: '2026-11-08T03:00:00Z' }))]
  assert.deepEqual(selectItems(items, defaults).map((item) => item.id), [2, 1])
})
