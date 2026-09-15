import { build } from 'esbuild'
import { mkdir, rm, cp, writeFile, readFile } from 'node:fs/promises'

const output = '.vercel/output'
await mkdir('.japan-build', { recursive: true })
await build({
  entryPoints: ['japan/client/app.mjs'],
  outdir: '.japan-build',
  entryNames: 'app',
  bundle: true,
  minify: true,
  sourcemap: false,
  format: 'esm',
  platform: 'browser',
  target: ['es2022'],
  loader: { '.png': 'dataurl' },
  legalComments: 'none',
})
await rm(output, { recursive: true, force: true })
await mkdir(`${output}/functions/japan.func/assets`, { recursive: true })
await cp('dist', `${output}/static`, { recursive: true })
await cp('.japan-build/app.js', `${output}/functions/japan.func/assets/app.js`)
await cp('.japan-build/app.css', `${output}/functions/japan.func/assets/app.css`)
await cp(
  'node_modules/leaflet/LICENSE',
  `${output}/functions/japan.func/assets/Leaflet-LICENSE.txt`,
)
await build({
  entryPoints: ['japan/server/entry.mjs'],
  outfile: `${output}/functions/japan.func/index.mjs`,
  bundle: true,
  platform: 'node',
  target: 'node22',
  format: 'esm',
  sourcemap: false,
  legalComments: 'none',
})
await writeFile(
  `${output}/functions/japan.func/.vc-config.json`,
  JSON.stringify(
    {
      runtime: 'nodejs22.x',
      handler: 'index.mjs',
      launcherType: 'Nodejs',
      shouldAddHelpers: false,
    },
    null,
    2,
  ),
)
// All protected paths resolve to the function BEFORE the static filesystem.
// Other naked-domain URLs retain the existing 307 -> www behavior after the dashboard redirect is removed.
await writeFile(
  `${output}/config.json`,
  JSON.stringify(
    {
      version: 3,
      routes: [
        { src: '^/japan(?:/.*)?$', dest: '/japan', caseSensitive: true },
        {
          src: '^/(?:japan\\.html|japan\\.json|api/japan(?:/.*)?)$',
          status: 404,
          headers: {
            'Cache-Control': 'private, no-store',
            'X-Robots-Tag': 'noindex, noarchive, nosnippet',
          },
        },
        {
          src: '^/(.*)$',
          has: [{ type: 'host', value: 'phymani.me' }],
          status: 307,
          headers: { Location: 'https://www.phymani.me/$1' },
        },
        { handle: 'filesystem' },
        { src: '^/(.*)/$', dest: '/$1/index.html', check: true },
        { src: '^/(.*)$', dest: '/$1/index.html', check: true },
        { src: '^/.*$', dest: '/404.html', status: 404 },
      ],
    },
    null,
    2,
  ),
)
// Read back the generated config so malformed output fails the build.
JSON.parse(await readFile(`${output}/config.json`, 'utf8'))
console.log(
  'Japan function and static blog packaged; no private data or runtime secrets read during build.',
)
