import {
  scrypt as nodeScrypt,
  randomBytes,
  createHash,
  timingSafeEqual,
  createHmac,
} from 'node:crypto'
import { promisify } from 'node:util'
import { SignJWT, jwtVerify } from 'jose'

const scrypt = promisify(nodeScrypt)
export const SESSION_SECONDS = 12 * 60 * 60
export const COOKIE = '__Secure-japan'
export const CSRF_COOKIE = '__Secure-japan-csrf'
export const random = () => randomBytes(32).toString('base64url')
export const digest = (value) => createHash('sha256').update(value).digest('hex')
export function equal(a, b) {
  return (
    typeof a === 'string' &&
    typeof b === 'string' &&
    a.length < 4096 &&
    b.length < 4096 &&
    Buffer.byteLength(a) === Buffer.byteLength(b) &&
    timingSafeEqual(Buffer.from(a), Buffer.from(b))
  )
}
export async function passwordHash(password) {
  if (!password || Buffer.byteLength(password) > 256) throw new Error('Password length')
  const salt = randomBytes(16)
  const key = await scrypt(password, salt, 32, { N: 131072, r: 8, p: 1, maxmem: 256 * 1024 * 1024 })
  return `scrypt$131072$8$1$${salt.toString('base64url')}$${key.toString('base64url')}`
}
export function validHash(hash) {
  return /^scrypt\$131072\$8\$1\$[\w-]{22}\$[\w-]{43}$/.test(hash || '')
}
export async function verifyPassword(password, hash) {
  if (
    !validHash(hash) ||
    typeof password !== 'string' ||
    !password ||
    Buffer.byteLength(password) > 256
  )
    return false
  const [, , , , salt, expected] = hash.split('$')
  const actual = await scrypt(password, Buffer.from(salt, 'base64url'), 32, {
    N: 131072,
    r: 8,
    p: 1,
    maxmem: 256 * 1024 * 1024,
  })
  return equal(actual.toString('base64url'), expected)
}
export function config(env = process.env) {
  if (
    !validHash(env.JAPAN_PASSWORD_HASH) ||
    !/^[\w-]{43}$/.test(env.JAPAN_SESSION_KEY || '') ||
    !/^[a-zA-Z0-9:_-]{1,80}$/.test(env.JAPAN_REDIS_PREFIX || '')
  )
    throw new Error('Configuration unavailable')
  return {
    hash: env.JAPAN_PASSWORD_HASH,
    key: Buffer.from(env.JAPAN_SESSION_KEY, 'base64url'),
    version: digest(env.JAPAN_PASSWORD_HASH),
    prefix: env.JAPAN_REDIS_PREFIX,
  }
}
export function cookie(name, value, seconds) {
  return `${name}=${value}; Path=/japan; Max-Age=${seconds}; Secure; HttpOnly; SameSite=Strict`
}
export function readCookie(header, name) {
  const values = (header || '')
    .split(';')
    .map((s) => s.trim())
    .filter((s) => s.startsWith(`${name}=`))
  return values.length === 1 ? values[0].slice(name.length + 1) : ''
}
export async function sign(payload, cfg, audience, seconds, now = Date.now()) {
  // Password-version fingerprints stay only in the server-side session record.
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256', typ: 'JWT' })
    .setIssuer('japan')
    .setAudience(audience)
    .setIssuedAt(Math.floor(now / 1000))
    .setExpirationTime(Math.floor(now / 1000) + seconds)
    .sign(cfg.key)
}
export async function verify(token, cfg, audience, now = Date.now()) {
  try {
    const { payload } = await jwtVerify(token, cfg.key, {
      algorithms: ['HS256'],
      issuer: 'japan',
      audience,
      currentDate: new Date(now),
    })
    return payload
  } catch {
    return null
  }
}
export function ipKey(ip, cfg) {
  return createHmac('sha256', cfg.key).update(ip).digest('hex')
}
