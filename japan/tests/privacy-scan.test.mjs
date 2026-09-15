import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, mkdir, writeFile, rm } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { randomUUID } from 'node:crypto'
import { execFileSync, spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

test('public audit rejects a Redis credential without printing its value', async () => {
  const cwd = await mkdtemp(join(tmpdir(), 'japan-privacy-scan-'))
  const token = `independent-test-token-${randomUUID()}`
  const script = fileURLToPath(new URL('../../scripts/japan/scan-public.mjs', import.meta.url))
  const scan = () => spawnSync(process.execPath, [script], { cwd, encoding: 'utf8' })
  try {
    execFileSync('git', ['init', '-q', cwd])
    for (const name of ['public', 'dist', '.vercel/output', '.private/japan'])
      await mkdir(join(cwd, name), { recursive: true })
    await writeFile(join(cwd, '.gitignore'), '.private/\n')
    await writeFile(join(cwd, '.private/japan/secrets.env'), `JAPAN_REDIS_REST_TOKEN='${token}'\n`)
    assert.equal(scan().status, 0)
    await writeFile(join(cwd, 'public/accidental-config.js'), `const value = '${token}'`)
    const result = scan()
    assert.equal(result.status, 1)
    assert.match(result.stderr, /Private artifact audit failed/)
    assert.ok(!(result.stdout + result.stderr).includes(token))
  } finally {
    await rm(cwd, { recursive: true, force: true })
  }
})
