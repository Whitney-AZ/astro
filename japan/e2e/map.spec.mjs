import { test, expect } from '@playwright/test'
import { testPassword } from '../tests/fixture.mjs'

const tile = Buffer.from(
  'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=',
  'base64',
)
async function login(page) {
  await page.goto('/japan')
  await page.getByLabel('共享密码').fill(testPassword)
  await page.getByRole('button', { name: '进入地图' }).click()
  await expect(page.locator('#count')).toContainText('个地点')
}
test.beforeEach(async ({ page }) => {
  // Mock-only UI tests. Real GSI network verification is a separate opt-in spec.
  await page.route('https://cyberjapandata.gsi.go.jp/**', (route) =>
    route.fulfill({ contentType: 'image/png', body: tile }),
  )
})
test('login protects data with JavaScript disabled and private response stays private across clients', async ({
  browser,
  page,
}) => {
  const noJs = await browser.newContext({ javaScriptEnabled: false })
  const bare = await noJs.newPage()
  await bare.goto('http://localhost:8789/japan')
  await expect(bare.getByLabel('共享密码')).toBeVisible()
  expect(await bare.content()).not.toContain('SYNTHETIC_SECRET')
  await login(page)
  const authorized = await page.request.get('/japan/data')
  expect(authorized.status()).toBe(200)
  expect(authorized.headers()['cache-control']).toBe('private, no-store')
  const unauthorized = await noJs.request.get('http://localhost:8789/japan/data')
  expect(unauthorized.status()).toBe(401)
  expect(await unauthorized.text()).not.toContain('SYNTHETIC_SECRET')
  await noJs.close()
})
test('date, search, categories, transport, alternatives and mobile panel', async ({
  page,
  isMobile,
}) => {
  await login(page)
  await expect(page.locator('#base-status')).toContainText('国土地理院标准地图')
  await page.locator('#day').selectOption('1')
  await expect(page.locator('#summary')).toContainText('Synthetic first day')
  await page.locator('#next').click()
  await expect(page.locator('#summary')).toContainText('Synthetic second day')
  await page.locator('#previous').click()
  await page.locator('#lake').selectOption('two')
  await expect(page.locator('#summary')).toContainText('Alternative synthetic first day')
  await expect(page.locator('#summary')).toContainText('Other test region')
  await expect(page.locator('#count')).toContainText('0 段连接')
  await page.locator('#search').fill('テスト')
  await expect(page.locator('#count')).toContainText('2 个地点')
  await page.locator('#search').fill('no-such-place')
  await expect(page.locator('#count')).toContainText('0 个地点')
  await page.locator('#search').fill('')
  await page.getByText('图层与图例', { exact: true }).click()
  await page.locator('#categories input[value=sight]').uncheck()
  await expect(page.locator('#count')).toContainText('0 个地点')
  await page.locator('#categories input[value=sight]').check()
  await page.locator('#lake').selectOption('one')
  await page.locator('#modes input[value=rail]').uncheck()
  await expect(page.locator('#count')).toContainText('0 段连接')
  if (isMobile) {
    await page.locator('#toggle-panel').click()
    await expect(page.locator('#panel')).toBeHidden()
    await page.locator('#toggle-panel').click()
    await expect(page.locator('#panel')).toBeVisible()
  }
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true)
})
test('failed tiles offer explicit fallback and retry', async ({ page }) => {
  await page.unroute('https://cyberjapandata.gsi.go.jp/**')
  await page.route('https://cyberjapandata.gsi.go.jp/**', (route) => route.abort())
  await login(page)
  await expect(page.locator('#retry-tiles')).toBeVisible()
  await page.locator('#fallback').click()
  await expect(page.locator('#base-status')).toContainText('仅点线示意')
  await expect(page.locator('#list')).toContainText('Synthetic first day')
})
test('collaborators add and edit owned candidates; rendering stays text-only', async ({ page }) => {
  await login(page)
  await page.getByText('共同补充目的地', { exact: true }).click()
  const form = page.locator('#add-point')
  await form.locator('[name=author]').fill('Browser test')
  await form.locator('[name=name]').fill('<img src=x onerror=alert(1)>')
  await form.locator('[name=lat]').fill('35.735')
  await form.locator('[name=lon]').fill('139.735')
  await form.getByRole('button', { name: '保存候选地点' }).click()
  await expect(page.locator('#save-status')).toContainText('已保存')
  await page.locator('#search').fill('onerror')
  await page.locator('#list').getByRole('button').first().click()
  await expect(page.locator('#detail h2')).toHaveText('<img src=x onerror=alert(1)>')
  await expect(page.locator('#detail h2')).toBeInViewport()
  await expect(page.locator('#detail img')).toHaveCount(0)
  await page.getByRole('button', { name: '编辑这个新增地点' }).click()
  await form.locator('[name=name]').fill('Updated browser candidate')
  await form.getByRole('button', { name: '保存候选地点' }).click()
  await expect(page.locator('#save-status')).toContainText('已保存')
})
test('logout clears pending resize, other tabs, stale requests and browser-back content', async ({
  page,
  context,
}) => {
  const errors = []
  page.on('pageerror', (error) => errors.push(error.message))
  await login(page)
  const other = await context.newPage()
  await other.route('https://cyberjapandata.gsi.go.jp/**', (route) =>
    route.fulfill({ contentType: 'image/png', body: tile }),
  )
  await other.goto('/japan')
  await expect(other.locator('#count')).toContainText('个地点')
  // Keep the cleared page alive beyond the resize timer to cover slow networks.
  await page.route('**/japan/logout', async (route) => {
    await new Promise((resolve) => setTimeout(resolve, 500))
    await route.continue()
  })
  await page.evaluate(() => {
    document.querySelector('#toggle-panel').click()
    document.querySelector('#logout').requestSubmit()
  })
  await expect(page.getByLabel('共享密码')).toBeVisible()
  await expect(other.locator('#japan-app')).toContainText('会话已结束')
  expect((await other.request.get('/japan/data')).status()).toBe(401)
  expect(errors).toEqual([])
  await page.goBack()
  await expect(page.locator('body')).not.toContainText('SYNTHETIC_SECRET')
})
