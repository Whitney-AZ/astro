// Entirely synthetic. Never replace this file with an actual itinerary.
export const testPassword = 'independent-test-passphrase!'
export function fixture() {
  const point = (id, name, lat, lon, variant = 'all') => ({
    id,
    name,
    jp: `テスト ${name}`,
    lat,
    lon,
    category: 'sight',
    region: 'test',
    days: [1, 2],
    time: '建议窗口',
    stay: '待核',
    access: '测试到达方式',
    note: '测试备注，未预订',
    sources: ['example'],
    optional: false,
    variant,
    coordinate_note: '测试参考坐标',
  })
  return {
    meta: {
      title: 'Synthetic private test trip',
      timezone: 'Asia/Tokyo',
      updated: '2000-01-01',
      nights: 1,
      people: 2,
      limitations: 'Synthetic fixture only',
    },
    sources: { example: { title: 'Example', url: 'https://example.com/' } },
    points: [
      point('a', 'SYNTHETIC_SECRET_POINT_A', 35.7, 139.7),
      point('b', 'SYNTHETIC_SECRET_POINT_B', 35.71, 139.71, 'one'),
      point('c', 'SYNTHETIC_SECRET_POINT_C', 35.72, 139.72, 'two'),
    ],
    routes: [
      {
        id: 'ab',
        title: 'Synthetic A to B',
        mode: 'rail',
        days: [1],
        coords: [
          [35.7, 139.7],
          [35.71, 139.71],
        ],
        time: '待核',
        duration: '参考',
        note: '换乘未核实',
        sources: ['example'],
        optional: false,
        variant: 'one',
        geometry_status: '示意',
      },
    ],
    days: [
      {
        day: 1,
        date: '2000-01-01',
        label: 'Day 1',
        title: 'Synthetic first day',
        hotel: 'Test region',
        description: 'Test only',
        focus: ['a', 'b'],
        when: '待核',
      },
      {
        day: 2,
        date: '2000-01-02',
        label: 'Day 2',
        title: 'Synthetic second day',
        hotel: '—',
        description: 'Test only',
        focus: ['a', 'b'],
        when: '待核',
      },
    ],
    colors: { sight: '#257f79' },
    ui: {
      defaultVariant: 'one',
      initialRegion: 'test',
      overviewRegion: 'test',
      variantRegion: 'test',
      regions: { test: { name: 'Test region', bounds: [35.69, 139.69, 35.73, 139.73] } },
      variants: {
        one: { name: 'Variant one', days: {} },
        two: {
          name: 'Variant two',
          days: {
            1: {
              title: 'Alternative synthetic first day',
              hotel: 'Other test region',
              focus: ['a', 'c'],
            },
            2: { title: 'Alternative synthetic second day', focus: ['a', 'c'] },
          },
        },
      },
    },
  }
}
export class MemoryStore {
  constructor() {
    this.values = new Map()
    this.audit = []
  }
  async get(key) {
    const value = this.values.get(key)
    if (!value || value.expires <= Date.now()) return null
    return value.value
  }
  async set(key, value, seconds = Infinity) {
    this.values.set(key, { value, expires: Date.now() + seconds * 1000 })
    return 'OK'
  }
  async del(key) {
    return this.values.delete(key)
  }
  async hit(key, seconds) {
    const n = Number((await this.get(`limit:${key}`)) || 0) + 1
    await this.set(`limit:${key}`, n, seconds)
    return n
  }
  async cas(key, old, next, audit) {
    if ((this.values.get(key)?.value ?? null) !== old) return 0
    this.values.set(key, { value: next, expires: Infinity })
    this.audit.push(JSON.stringify(audit))
    return 1
  }
  async history() {
    return this.audit
  }
}
export function addition() {
  return {
    name: 'Synthetic contributed place',
    jp: 'テスト',
    author: 'Test contributor',
    lat: 35.73,
    lon: 139.73,
    days: [1],
    region: 'test',
    category: 'sight',
    variant: 'all',
    time: '',
    stay: '',
    access: '',
    note: '',
    source_url: '',
  }
}
