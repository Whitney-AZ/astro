import { RedisStore } from '../server/store.mjs'
// Test-only TCP adapter; production uses the same commands through authenticated HTTPS REST.
export class LocalRedisStore extends RedisStore {
  constructor(client, prefix) {
    super({
      JAPAN_REDIS_REST_URL: 'https://example.invalid',
      JAPAN_REDIS_REST_TOKEN: 'local-test-only',
      JAPAN_REDIS_PREFIX: prefix,
    })
    this.client = client
  }
  command(...args) {
    return this.client.sendCommand(args.map(String))
  }
}
