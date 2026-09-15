import { readFile, readdir, stat } from 'node:fs/promises'
import { execFileSync } from 'node:child_process'

const forbiddenNames =
  /(?:trip_data\.json|points\.geojson|routes_schematic\.geojson|日本.*(?:地图|行程).*(?:zip|html|pdf|csv|kml)|secrets\.env)/i
let markers = []
try {
  const data = JSON.parse(await readFile('.private/japan/trip.json', 'utf8'))
  markers = [
    ...data.points.map((p) => p.name).filter((n) => n.length >= 8),
    ...data.routes.map((r) => JSON.stringify(r.coords)),
    data.meta.dates,
    data.meta.plan,
  ].filter(Boolean)
} catch {
  /* Public CI has no real input; structural checks still run. */
}
let secretValues = []
try {
  const env = await readFile('.private/japan/secrets.env', 'utf8')
  secretValues = [...env.matchAll(/(?:PASSWORD_HASH|SESSION_KEY)='([^']+)'/g)].map((m) => m[1])
} catch {
  /* No production secrets required for builds. */
}
const failures = []
async function files(root) {
  const all = []
  for (const entry of await readdir(root, { withFileTypes: true })) {
    const p = `${root}/${entry.name}`
    if (entry.isDirectory()) all.push(...(await files(p)))
    else all.push(p)
  }
  return all
}
for (const root of ['public', 'dist', '.vercel/output']) {
  for (const file of await files(root)) {
    if (forbiddenNames.test(file)) failures.push(file)
    if ((await stat(file)).size > 15000000) continue
    const content = await readFile(file, 'utf8')
    if ([...markers, ...secretValues].some((m) => content.includes(m))) failures.push(file)
  }
}
const tracked = execFileSync(
  'git',
  ['ls-files', '--cached', '--others', '--exclude-standard', '-z'],
  { encoding: 'utf8' },
)
  .split('\0')
  .filter(Boolean)
for (const file of tracked) {
  if (file.startsWith('.private/') || forbiddenNames.test(file)) failures.push(file)
  const content = await readFile(file, 'utf8').catch(() => '')
  if (
    secretValues.some((value) => content.includes(value)) ||
    /\b[jJ]apan(?:19|20)\d{2}\b/.test(content) ||
    /scrypt\$131072\$8\$1\$[\w-]{22}\$[\w-]{43}/.test(content)
  )
    failures.push(file)
}
for (const file of (await files('dist')).filter((f) =>
  /(?:sitemap.*\.xml|rss\.xml|pagefind.*\.json|index\.html)$/.test(f),
)) {
  const content = await readFile(file, 'utf8')
  if (
    /(?:href|url)=["'][^"']*\/japan(?:["'/#?])|https:\/\/phymani\.me\/japan(?:[<"'/#?])/.test(
      content,
    )
  )
    failures.push(file)
}
if (failures.length)
  throw new Error(
    `Private artifact audit failed for ${new Set(failures).size} file(s). Inspect locally; contents are not logged.`,
  )
console.log(
  `Public output, routing indexes and tracked files passed privacy checks${markers.length ? ' against real private markers' : ' (real private input unavailable)'}.`,
)
