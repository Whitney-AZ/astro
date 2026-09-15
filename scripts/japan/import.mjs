import { readFile, writeFile, mkdir } from 'node:fs/promises'
import { resolve } from 'node:path'
import { assertTrip } from '../../japan/shared/model.mjs'
import { digest } from '../../japan/server/security.mjs'

const input = process.argv[2],
  overrides = process.argv[3]
if (!input || !overrides)
  throw new Error('Usage: node scripts/japan/import.mjs PRIVATE_TRIP_JSON PRIVATE_UI_JSON')
for (const path of [input, overrides])
  if (!resolve(path).startsWith(resolve('.private/japan') + '/'))
    throw new Error('Input must be in .private/japan')
const original = await readFile(input, 'utf8'),
  source = JSON.parse(original),
  ui = JSON.parse(await readFile(overrides, 'utf8'))
assertTrip(source)
let maxProjectionError = 0
const projected = (lat, lon) => [
  (6378137 * lon * Math.PI) / 180,
  6378137 * Math.log(Math.tan(Math.PI / 4 + (lat * Math.PI) / 360)),
]
for (const p of source.points) {
  const expected = projected(p.lat, p.lon)
  if (p.x !== undefined)
    maxProjectionError = Math.max(
      maxProjectionError,
      Math.abs(p.x - expected[0]),
      Math.abs(p.y - expected[1]),
    )
}
for (const r of source.routes)
  if (r.xs)
    r.coords.forEach(([lat, lon], i) => {
      const p = projected(lat, lon)
      maxProjectionError = Math.max(
        maxProjectionError,
        Math.abs(r.xs[i] - p[0]),
        Math.abs(r.ys[i] - p[1]),
      )
    })
if (maxProjectionError > 0.01) throw new Error('Projected and geographic coordinates disagree')
const normalized = {
  ...source,
  points: source.points.map(({ x, y, ...p }) => p),
  routes: source.routes.map(({ xs, ys, angle, arrowx, arrowy, ...r }) => r),
  ui,
}
assertTrip(normalized)
for (const variant of Object.values(ui.variants))
  for (const [day, override] of Object.entries(variant.days || {})) {
    if (!source.days.some((d) => d.day === Number(day))) throw new Error('Variant day missing')
    if (override.focus?.some((id) => !source.points.some((p) => p.id === id)))
      throw new Error('Variant point missing')
  }
await mkdir('.private/japan/qa', { recursive: true, mode: 0o700 })
await writeFile('.private/japan/trip.json', JSON.stringify(normalized), { mode: 0o600 })
await writeFile(
  '.private/japan/qa/import.json',
  JSON.stringify(
    {
      inputSha256: digest(original),
      inputPath: input,
      outputSha256: digest(JSON.stringify(normalized)),
      counts: {
        points: source.points.length,
        routes: source.routes.length,
        days: source.days.length,
      },
      pointIds: source.points.map((p) => p.id),
      routeIds: source.routes.map((r) => r.id),
      maxProjectionError,
      originalPreserved: true,
      derivedFieldsRemoved: ['x', 'y', 'xs', 'ys', 'angle', 'arrowx', 'arrowy'],
      uiOverrides: ui.variants,
      importedAt: new Date().toISOString(),
    },
    null,
    2,
  ),
  { mode: 0o600 },
)
console.log(
  `Imported ${source.points.length} points, ${source.routes.length} routes and ${source.days.length} days; WGS84 and source references verified. Private report written.`,
)
