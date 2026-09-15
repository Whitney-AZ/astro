import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFile, readdir, access } from 'node:fs/promises'

test('built routing protects the entire boundary before filesystem and retains the public domain redirect', async () => {
  const { routes } = JSON.parse(await readFile('.vercel/output/config.json', 'utf8'))
  const privateRoute = routes.findIndex((r) => r.dest === '/japan')
  const filesystem = routes.findIndex((r) => r.handle === 'filesystem')
  assert.ok(privateRoute >= 0 && privateRoute < filesystem)
  const match = new RegExp(routes[privateRoute].src)
  for (const path of [
    '/japan',
    '/japan/',
    '/japan/data',
    '/japan/assets/app.js',
    '/japan/export/kml',
    '/japan/collaboration',
    '/japan/index.html',
  ])
    assert.ok(match.test(path))
  assert.equal(match.test('/japanese'), false)
  const publicRedirect = routes.find((r) =>
    r.has?.some((h) => h.type === 'host' && h.value === 'phymani.me'),
  )
  assert.equal(publicRedirect.status, 307)
  assert.equal(publicRedirect.headers.Location, 'https://www.phymani.me/$1')
  assert.ok(routes.indexOf(publicRedirect) > privateRoute)
})
test('static artifacts contain no Japan page and blog entrypoints remain present', async () => {
  for (const name of [
    'index.html',
    'archives/index.html',
    'bangumi/index.html',
    'srednicki/index.html',
    'rss.xml',
    'sitemap-index.xml',
    'pagefind/pagefind.js',
  ])
    await access(`.vercel/output/static/${name}`)
  for (const name of ['japan', 'japan.html', 'japan/index.html'])
    await assert.rejects(access(`.vercel/output/static/${name}`))
  const func = '.vercel/output/functions/japan.func'
  const cfg = JSON.parse(await readFile(`${func}/.vc-config.json`, 'utf8'))
  assert.equal(cfg.runtime, 'nodejs22.x')
  assert.equal(cfg.launcherType, 'Nodejs')
  const assets = await readdir(`${func}/assets`)
  assert.ok(assets.includes('app.js') && assets.includes('app.css'))
  assert.ok(!assets.some((name) => /json|map$|kml|csv|pdf/.test(name)))
  const rss = await readFile('dist/rss.xml', 'utf8')
  assert.ok(!rss.includes('/japan'))
})
