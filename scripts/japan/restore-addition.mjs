import { RedisStore } from '../../japan/server/store.mjs'
// Admin maintenance only; takes no credentials on the command line.
const [id, revisionText] = process.argv.slice(2)
if (!/^added-[\w-]+$/.test(id || '') || !/^\d+$/.test(revisionText || ''))
  throw new Error('Usage: restore-addition.mjs ADDED_ID HISTORICAL_REVISION')
const store = new RedisStore()
const raw = await store.get('collaboration'),
  current = JSON.parse(raw)
const history = (await store.command('LRANGE', store.key('history'), 0, -1)).map((row) =>
  JSON.parse(row),
)
const record = history.find((row) => row.revision === Number(revisionText) && row.point.id === id)
if (!record) throw new Error('Requested historical revision not found')
const point = { ...record.point, updatedAt: new Date().toISOString() }
const next = {
  revision: current.revision + 1,
  points: [...current.points.filter((p) => p.id !== id), point],
}
const previous = current.points.find((p) => p.id === id) || null
if (
  !(await store.cas('collaboration', raw, JSON.stringify(next), {
    revision: next.revision,
    action: 'restore',
    at: point.updatedAt,
    point,
    previous,
    restoredFrom: Number(revisionText),
  }))
)
  throw new Error('Concurrent update; refresh and retry')
console.log(
  'Historical candidate restored as a new revision; other candidates and the baseline were retained.',
)
