import test from 'node:test'
import assert from 'node:assert/strict'
import { mkdtemp, writeFile, rm, mkdir, readFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { execFileSync } from 'node:child_process'
import { repositoryFiles } from '../../scripts/japan/repository-files.mjs'

test('repository inventory streams more than 1 MiB and excludes the CI package cache', async () => {
  const cwd = await mkdtemp(join(tmpdir(), 'japan-inventory-'))
  try {
    execFileSync('git', ['init', '-q', cwd])
    await writeFile(join(cwd, '.gitignore'), await readFile('.gitignore'))
    await mkdir(join(cwd, '.pnpm-store'))
    await writeFile(join(cwd, '.pnpm-store', 'ignored-package'), 'cached dependency')
    await writeFile(join(cwd, 'untracked-source.mjs'), 'export {}')
    await writeFile(join(cwd, 'tracked-source.mjs'), 'export {}')
    execFileSync('git', ['add', 'tracked-source.mjs'], { cwd })
    const object = execFileSync('git', ['hash-object', '-w', '--stdin'], {
      cwd,
      input: '',
      encoding: 'utf8',
    }).trim()
    const names = Array.from({ length: 12000 }, (_, i) => `${'x'.repeat(100)}/${i}.mjs`)
    execFileSync('git', ['update-index', '--index-info'], {
      cwd,
      input: names.map((name) => `100644 ${object}\t${name}\n`).join(''),
    })
    assert.ok(Buffer.byteLength(names.join('\0')) > 1024 * 1024)
    const found = []
    for await (const file of repositoryFiles(cwd)) found.push(file)
    assert.equal(found.length, names.length + 3)
    assert.ok(found.includes('tracked-source.mjs'))
    assert.ok(found.includes('untracked-source.mjs'))
    assert.ok(!found.some((name) => name.startsWith('.pnpm-store/')))
    assert.ok(names.every((name) => found.includes(name)))
  } finally {
    await rm(cwd, { recursive: true, force: true })
  }
})

test('repository inventory errors do not print child output or paths', async () => {
  const cwd = await mkdtemp(join(tmpdir(), 'japan-inventory-error-'))
  try {
    await assert.rejects(
      async () => {
        for await (const file of repositoryFiles(cwd)) assert.fail(file)
      },
      { message: 'Repository privacy inventory failed.' },
    )
  } finally {
    await rm(cwd, { recursive: true, force: true })
  }
})
