import { readFile, mkdir, writeFile } from 'node:fs/promises'
import { RedisStore } from '../../japan/server/store.mjs'
import { assertTrip } from '../../japan/shared/model.mjs'
import { digest } from '../../japan/server/security.mjs'

// Run only locally with a private environment file. Never run in public CI.
const input = process.argv[2] || '.private/japan/trip.json'
if (!input.startsWith('.private/japan/') || input.includes('..'))
  throw new Error('Private input required')
const raw = await readFile(input, 'utf8')
assertTrip(JSON.parse(raw))
const store = new RedisStore()
const existing = await store.get('baseline')
await mkdir('.private/japan/backups', { recursive: true, mode: 0o700 })
if (existing) {
  const oldHash = digest(existing)
  await writeFile(`.private/japan/backups/${oldHash}.json`, existing, { mode: 0o600 })
  // Compare-and-set prevents another maintenance update from being silently overwritten.
  const updated = await store.command(
    'EVAL',
    "if redis.call('GET',KEYS[1])~=ARGV[1] then return 0 end; redis.call('SET',KEYS[2],ARGV[1]); redis.call('SET',KEYS[1],ARGV[2]); return 1",
    2,
    store.key('baseline'),
    store.key(`baseline-history:${oldHash}`),
    existing,
    raw,
  )
  if (!updated)
    throw new Error('Baseline changed concurrently; retry after reviewing current input')
} else {
  if (!(await store.command('SET', store.key('baseline'), raw, 'NX')))
    throw new Error('Baseline was initialized concurrently')
}
await store.command(
  'SET',
  store.key('collaboration'),
  JSON.stringify({ revision: 0, points: [] }),
  'NX',
)
console.log(
  'Private baseline uploaded; collaboration records retained. No itinerary or credentials printed.',
)
