import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { dirname, join } from 'node:path'
import { assertTrip, geojson, kml, selectedDay, selectRecords, safeUrl } from '../shared/model.mjs'
import { fixture } from './fixture.mjs'

test('coordinate order and date continuity are enforced, exports use standard lon-lat', () => {
  const data = fixture()
  assertTrip(data)
  assert.deepEqual(geojson(data).features[0].geometry.coordinates, [139.7, 35.7])
  assert.match(kml(data), /139\.7,35\.7/)
  const bad = structuredClone(data)
  ;[bad.points[0].lat, bad.points[0].lon] = [bad.points[0].lon, bad.points[0].lat]
  assert.throws(() => assertTrip(bad))
  const routeBad = structuredClone(data)
  routeBad.routes[0].coords[0].reverse()
  assert.throws(() => assertTrip(routeBad))
  const dateBad = structuredClone(data)
  dateBad.days[1].date = '2000-01-04'
  assert.throws(() => assertTrip(dateBad))
  assert.equal(safeUrl('javascript:alert(1)'), null)
  assert.equal(safeUrl('data:text/html,bad'), null)
})
test('variant replaces both days, focus and lodging; hidden variants leave no orphan route', () => {
  const data = fixture(),
    state = {
      day: 1,
      lake: 'two',
      optional: true,
      search: '',
      categories: ['sight'],
      modes: ['rail'],
    }
  assert.deepEqual(
    selectRecords(data, state).points.map((p) => p.id),
    ['a', 'c'],
  )
  assert.equal(selectRecords(data, state).routes.length, 0)
  assert.match(selectedDay(data, 1, 'two').title, /Alternative/)
  assert.match(selectedDay(data, 2, 'two').title, /Alternative/)
  assert.equal(selectedDay(data, 1, 'two').hotel, 'Other test region')
  assert.equal(selectRecords(data, { ...state, search: 'テスト' }).points.length, 2)
  assert.equal(selectRecords(data, { ...state, categories: [] }).points.length, 0)
})
test('real private import: counts, original IDs, all non-projection fields, sources, lodging and alternate focus', async (t) => {
  let data, audit, original
  try {
    data = JSON.parse(await readFile('.private/japan/trip.json', 'utf8'))
    audit = JSON.parse(await readFile('.private/japan/qa/import.json', 'utf8'))
  } catch {
    t.skip('Real private input is intentionally absent in public CI')
    return
  }
  assertTrip(data)
  assert.deepEqual(
    [data.points.length, data.routes.length, data.days.length, data.meta.nights],
    [60, 47, 15, 14],
  )
  assert.deepEqual(
    data.points.map((p) => p.id),
    audit.pointIds,
  )
  assert.deepEqual(
    data.routes.map((r) => r.id),
    audit.routeIds,
  )
  original = JSON.parse(await readFile(audit.inputPath, 'utf8'))
  const exported = geojson(data)
  for (const name of ['points.geojson', 'routes_schematic.geojson']) {
    const source = JSON.parse(await readFile(join(dirname(audit.inputPath), name), 'utf8'))
    for (const feature of source.features) {
      assert.deepEqual(
        exported.features.find((f) => f.id === feature.properties.id).geometry,
        feature.geometry,
      )
    }
  }
  assert.deepEqual(
    data.points,
    original.points.map(({ x, y, ...point }) => point),
  )
  assert.deepEqual(
    data.routes,
    original.routes.map(({ xs, ys, angle, arrowx, arrowy, ...route }) => route),
  )
  for (const key of ['days', 'sources', 'meta', 'lakes', 'colors', 'modeColors', 'symbols'])
    assert.deepEqual(data[key], original[key])
  assert.ok(audit.maxProjectionError < 0.01)
  assert.equal(data.days.filter((d) => d.hotel && d.hotel !== '—').length, 14)
  assert.equal(new Set(data.days.map((d) => d.date)).size, 15)
  for (const lake of Object.keys(data.ui.variants))
    for (const day of data.days) {
      const current = selectedDay(data, day.day, lake)
      for (const id of current.focus) {
        const point = data.points.find((p) => p.id === id)
        assert.ok(point && (point.variant === 'all' || point.variant === lake || point.optional))
      }
    }
})
