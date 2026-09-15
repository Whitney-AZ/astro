import { spawn } from 'node:child_process'

// Stream NUL-delimited paths: CI dependency caches can exceed execFileSync's
// buffer limit. Never attach command output to errors printed by public CI.
export async function* repositoryFiles(cwd = process.cwd()) {
  const child = spawn('git', ['ls-files', '--cached', '--others', '--exclude-standard', '-z'], {
    cwd,
    stdio: ['ignore', 'pipe', 'ignore'],
  })
  const completed = new Promise((resolve) => {
    child.once('error', () => resolve(false))
    child.once('close', (code) => resolve(code === 0))
  })
  child.stdout.setEncoding('utf8')
  let pending = ''
  try {
    for await (const chunk of child.stdout) {
      pending += chunk
      let end
      while ((end = pending.indexOf('\0')) !== -1) {
        const file = pending.slice(0, end)
        pending = pending.slice(end + 1)
        if (file) yield file
      }
    }
    if (!(await completed) || pending) throw new Error('Repository privacy inventory failed.')
  } finally {
    if (child.exitCode === null) child.kill()
  }
}
