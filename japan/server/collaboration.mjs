import { randomUUID } from 'node:crypto'
import { random, digest, equal } from './security.mjs'
import { categoryNames, safeUrl } from '../shared/model.mjs'

export function validateAddition(input, data) {
  const point = {}
  for (const [key, max] of Object.entries({
    name: 120,
    jp: 120,
    author: 60,
    time: 300,
    stay: 200,
    access: 1500,
    note: 3000,
    source_url: 1000,
  })) {
    if (typeof input[key] !== 'string' || input[key].length > max) throw new Error('Invalid field')
    point[key] = input[key].trim()
  }
  if (!point.name || !point.author) throw new Error('Name and nickname required')
  point.lat = Number(input.lat)
  point.lon = Number(input.lon)
  if (
    !Number.isFinite(point.lat) ||
    !Number.isFinite(point.lon) ||
    point.lat < 20 ||
    point.lat > 50 ||
    point.lon < 120 ||
    point.lon > 155 ||
    input.lat === '' ||
    input.lon === ''
  )
    throw new Error('WGS84 coordinates required')
  if (
    !Array.isArray(input.days) ||
    !input.days.length ||
    input.days.length > data.days.length ||
    input.days.some((d) => !Number.isInteger(d) || !data.days.some((day) => day.day === d))
  )
    throw new Error('Date required')
  point.days = [...new Set(input.days)]
  if (!categoryNames[input.category] || !Object.hasOwn(data.ui.regions, input.region))
    throw new Error('Category or region')
  if (!['all', ...Object.keys(data.ui.variants)].includes(input.variant)) throw new Error('Variant')
  if (point.source_url && !safeUrl(point.source_url)) throw new Error('Source URL')
  Object.assign(point, {
    category: input.category,
    region: input.region,
    variant: input.variant,
    optional: true,
    sources: [],
    coordinate_note: '协作添加的参考点，未经核实；不是精确入口或站台',
    collaboration: true,
  })
  return point
}
export async function editAddition(store, input, data, sessionId) {
  const raw = await store.get('collaboration')
  if (!raw) throw new Error('Storage not initialized')
  const current = JSON.parse(raw)
  if (input.revision !== current.revision)
    return { status: 409, body: { error: '其他人已更新，请刷新后再保存。' } }
  const point = validateAddition(input.point, data)
  let editToken
  if (input.id) {
    const existing = current.points.find((p) => p.id === input.id)
    if (!existing || !equal(existing.editHash, digest(String(input.editToken || ''))))
      return { status: 403, body: { error: '需要此新增地点的编辑凭证。' } }
    Object.assign(point, {
      id: existing.id,
      editHash: existing.editHash,
      createdAt: existing.createdAt,
    })
  } else {
    if (current.points.length >= 500)
      return { status: 400, body: { error: '新增地点数量已达上限。' } }
    editToken = random()
    Object.assign(point, {
      id: `added-${randomUUID()}`,
      editHash: digest(editToken),
      createdAt: new Date().toISOString(),
    })
  }
  point.updatedAt = new Date().toISOString()
  const next = {
    revision: current.revision + 1,
    points: [...current.points.filter((p) => p.id !== point.id), point],
  }
  const audit = {
    revision: next.revision,
    action: input.id ? 'update' : 'add',
    point,
    previous: current.points.find((p) => p.id === point.id) || null,
    session: digest(sessionId),
    at: point.updatedAt,
  }
  const ok = await store.cas('collaboration', raw, JSON.stringify(next), audit)
  return ok
    ? {
        status: 200,
        body: { id: point.id, revision: next.revision, ...(editToken ? { editToken } : {}) },
      }
    : { status: 409, body: { error: '其他人已更新，请刷新后再保存。' } }
}
export function publicCollaboration(value) {
  return { revision: value.revision, points: value.points.map(({ editHash, ...p }) => p) }
}
