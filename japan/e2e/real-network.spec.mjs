import { test, expect } from '@playwright/test'
import { readFile, mkdir, writeFile } from 'node:fs/promises'
import { testPassword } from '../tests/fixture.mjs'

test('REAL network: original private data, eight street-level GSI viewports and whole-variant switch', async ({
  page,
}, info) => {
  test.skip(
    process.env.JAPAN_TEST_REAL !== '1',
    'Opt-in real data and network test; private input is never stored in Git',
  )
  test.setTimeout(150000)
  const data = JSON.parse(await readFile('.private/japan/trip.json', 'utf8'))
  const evidence = [],
    errors = []
  page.on('pageerror', (error) => errors.push(error.message))
  await page.goto('/japan')
  expect(await page.content()).not.toContain(data.points[0].name)
  await page.getByLabel('共享密码').fill(testPassword)
  await page.getByRole('button', { name: '进入地图' }).click()
  await expect(page.locator('#count')).toContainText('个地点')
  await expect(page.locator('#base-status')).toContainText('国土地理院标准地图', { timeout: 30000 })
  await expect(page.locator('#day option')).toHaveCount(data.days.length + 1)
  const loaded = await page.request.get('/japan/data')
  const payload = await loaded.json()
  expect(payload.points.filter((p) => !p.collaboration)).toEqual(data.points)
  expect(payload.routes).toEqual(data.routes)
  const initialZooms = await page
    .locator('img.leaflet-tile-loaded')
    .evaluateAll((images) => images.map((i) => Number(i.src.split('/std/')[1]?.split('/')[0])))
  expect(initialZooms.some((z) => z >= 14)).toBe(true)
  const root = `.private/japan/qa/real-${info.project.name}`
  await mkdir(root, { recursive: true })
  for (const [i, id] of data.ui.verificationPoints.entries()) {
    const point = data.points.find((p) => p.id === id)
    if (point.variant !== 'all' && point.variant !== 'airport_alt')
      await page.locator('#lake').selectOption(point.variant)
    await page.locator('#search').fill(point.name)
    await page.locator('#list').getByRole('button').filter({ hasText: point.name }).first().click()
    await expect(page.locator('#detail h2')).toHaveText(point.name)
    await expect(page.locator('#base-status')).toContainText('国土地理院标准地图', {
      timeout: 30000,
    })
    const tiles = await page.locator('img.leaflet-tile').evaluateAll((images) =>
      images.map((i) => ({
        loaded: i.complete && i.naturalWidth === 256,
        zoom: Number(i.src.split('/std/')[1]?.split('/')[0]),
      })),
    )
    expect(tiles.length).toBeGreaterThan(0)
    expect(tiles.every((t) => t.loaded && t.zoom === 15)).toBe(true)
    await page.screenshot({ path: `${root}/region-${i + 1}.png` })
    evidence.push({ pointId: id, tileCount: tiles.length, zoom: 15, allImagesDecoded: true })
  }
  for (const [lake, variant] of Object.entries(data.ui.variants)) {
    await page.locator('#lake').selectOption(lake)
    for (const day of Object.keys(variant.days || {})) {
      await page.locator('#day').selectOption(day)
      await expect(page.locator('#summary')).toContainText(variant.days[day].title)
    }
  }
  expect(errors).toEqual([])
  await writeFile(
    `${root}/evidence.json`,
    JSON.stringify(
      {
        checkedAt: new Date().toISOString(),
        realNetwork: true,
        viewports: evidence,
        pageErrors: errors,
      },
      null,
      2,
    ),
    { mode: 0o600 },
  )
})
