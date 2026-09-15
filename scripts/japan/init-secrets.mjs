import { password } from '@inquirer/prompts'
import { mkdir, writeFile, chmod } from 'node:fs/promises'
import { passwordHash, random } from '../../japan/server/security.mjs'

process.umask(0o077)
let value
if (process.argv.includes('--stdin')) {
  if (process.stdin.isTTY)
    throw new Error('Use a secure pipe with --stdin; otherwise use the hidden interactive prompt.')
  const chunks = []
  let bytes = 0
  for await (const chunk of process.stdin) {
    bytes += chunk.length
    if (bytes > 512) throw new Error('Input too long')
    chunks.push(chunk)
  }
  value = Buffer.concat(chunks)
    .toString('utf8')
    .replace(/\r?\n$/, '')
} else {
  value = await password({ message: '共享密码（隐藏输入，不会记录到输出）' })
  const confirm = await password({ message: '再次输入' })
  if (confirm !== value) throw new Error('Passwords do not match')
}
const hash = await passwordHash(value)
value = undefined
await mkdir('.private/japan', { recursive: true, mode: 0o700 })
// Exclusive create prevents accidental overwriting; rotate by choosing a new private output file.
const output = process.env.JAPAN_SECRET_OUTPUT || '.private/japan/secrets.env'
if (!output.startsWith('.private/japan/') || output.includes('..'))
  throw new Error('Output must be inside .private/japan')
await writeFile(
  output,
  `JAPAN_PASSWORD_HASH='${hash}'\nJAPAN_SESSION_KEY='${random()}'\nJAPAN_REDIS_PREFIX='japan-v1'\nJAPAN_REDIS_REST_URL=''\nJAPAN_REDIS_REST_TOKEN=''\n`,
  { flag: 'wx', mode: 0o600 },
)
await chmod(output, 0o600)
console.log(
  'Secret file created in the private directory. No values printed. Set these variables in Vercel Production only.',
)
