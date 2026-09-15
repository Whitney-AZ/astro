// All state is durable. No serverless process-local rate limit or session fallback.
export const RATE_SCRIPT = `local n=redis.call('INCR',KEYS[1]); if n==1 then redis.call('EXPIRE',KEYS[1],ARGV[1]) end; return n`
export const CAS_SCRIPT = `local old=redis.call('GET',KEYS[1]); if old~=ARGV[1] then return 0 end; redis.call('SET',KEYS[1],ARGV[2]); redis.call('RPUSH',KEYS[2],ARGV[3]); return 1`
export class RedisStore {
  constructor(env = process.env) {
    if (
      !/^https:\/\/[\w.-]+(?::443)?\/?$/.test(env.JAPAN_REDIS_REST_URL || '') ||
      !env.JAPAN_REDIS_REST_TOKEN
    )
      throw new Error('Storage unavailable')
    this.url = env.JAPAN_REDIS_REST_URL
    this.token = env.JAPAN_REDIS_REST_TOKEN
    this.prefix = env.JAPAN_REDIS_PREFIX
  }
  key(name) {
    return `${this.prefix}:${name}`
  }
  async command(...args) {
    const res = await fetch(this.url, {
      method: 'POST',
      headers: { Authorization: `Bearer ${this.token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(args),
      signal: AbortSignal.timeout(8000),
      cache: 'no-store',
    })
    if (!res.ok) throw new Error('Storage unavailable')
    const body = await res.json()
    if (body.error || !Object.hasOwn(body, 'result')) throw new Error('Storage unavailable')
    return body.result
  }
  get(name) {
    return this.command('GET', this.key(name))
  }
  set(name, value, seconds) {
    return this.command('SET', this.key(name), value, ...(seconds ? ['EX', seconds] : []))
  }
  del(name) {
    return this.command('DEL', this.key(name))
  }
  hit(name, seconds) {
    return this.command('EVAL', RATE_SCRIPT, 1, this.key(`limit:${name}`), seconds)
  }
  cas(name, old, next, audit) {
    return this.command(
      'EVAL',
      CAS_SCRIPT,
      2,
      this.key(name),
      this.key('history'),
      old,
      next,
      JSON.stringify(audit),
    )
  }
  history() {
    return this.command('LRANGE', this.key('history'), -100, -1)
  }
}
