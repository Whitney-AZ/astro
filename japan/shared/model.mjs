// Generic program only. Actual names, dates, coordinates and variant overrides are private input.
export const categoryNames = {
  station: '车站／换乘',
  airport: '机场',
  sight: '观光',
  photo: '摄影',
  stay: '住宿片区',
  event: '赛事／活动',
  reference: '景物参照',
}
export const modeNames = {
  rail: 'JR／铁路',
  metro: '地铁',
  bus: '巴士',
  guide: '预约车辆／向导',
  walk: '步行',
  air: '航空',
  cable: '缆车',
  view: '摄影视线',
}
export const modeStyles = {
  rail: ['#315f9b', ''],
  metro: ['#277ab3', '10 3 2 3'],
  bus: ['#ba601c', '9 5'],
  guide: ['#9252a1', '10 3 3 3'],
  walk: ['#258466', '2 5'],
  air: ['#bd4e59', '14 8'],
  cable: ['#53636a', '5 3'],
  view: ['#a57b17', '2 7'],
}
export function safeUrl(value) {
  try {
    const u = new URL(value)
    return ['https:', 'http:'].includes(u.protocol) && !u.username && !u.password ? u.href : null
  } catch {
    return null
  }
}
export function visibleVariant(record, state) {
  return (
    record.variant === 'all' ||
    record.variant === state.lake ||
    (record.variant === 'airport_alt' && state.optional)
  )
}
export function selectRecords(data, state) {
  const matches = (r) =>
    (!state.day || r.days.includes(state.day)) &&
    visibleVariant(r, state) &&
    (state.optional || !r.optional)
  const q = state.search.trim().toLocaleLowerCase()
  return {
    points: data.points.filter(
      (p) =>
        matches(p) &&
        state.categories.includes(p.category) &&
        (!q || [p.name, p.jp, p.note, p.access].join(' ').toLocaleLowerCase().includes(q)),
    ),
    routes: data.routes.filter((r) => matches(r) && state.modes.includes(r.mode)),
  }
}
export function selectedDay(data, day, lake) {
  const d = data.days.find((d) => d.day === Number(day))
  return d ? { ...d, ...data.ui?.variants?.[lake]?.days?.[d.day] } : null
}
export function assertTrip(data) {
  const fail = (message) => {
    throw new Error(`Invalid trip: ${message}`)
  }
  if (
    !data ||
    data.meta?.timezone !== 'Asia/Tokyo' ||
    !Array.isArray(data.days) ||
    !data.days.length
  )
    fail('timezone or days')
  if (!Array.isArray(data.points) || !Array.isArray(data.routes) || !data.sources)
    fail('collections')
  const ids = new Set(),
    days = new Set(data.days.map((d) => d.day))
  const coord = ([lat, lon]) =>
    Number.isFinite(lat) &&
    Number.isFinite(lon) &&
    lat >= 20 &&
    lat <= 50 &&
    lon >= 120 &&
    lon <= 155
  data.days.forEach((d, i) => {
    if (d.day !== i + 1 || !/^\d{4}-\d{2}-\d{2}$/.test(d.date)) fail('day numbering')
    const t = Date.parse(`${d.date}T00:00:00+09:00`)
    if (
      !Number.isFinite(t) ||
      (i && t - Date.parse(`${data.days[i - 1].date}T00:00:00+09:00`) !== 86400000)
    )
      fail('date continuity')
  })
  for (const record of [...data.points, ...data.routes]) {
    if (typeof record.id !== 'string' || ids.has(record.id)) fail('duplicate or missing id')
    ids.add(record.id)
    if (!Array.isArray(record.days) || !record.days.length || record.days.some((d) => !days.has(d)))
      fail('day reference')
    if (!Array.isArray(record.sources) || record.sources.some((s) => !data.sources[s]))
      fail('source reference')
    if (typeof record.optional !== 'boolean' || typeof record.variant !== 'string') fail('variant')
  }
  for (const p of data.points)
    if (!coord([p.lat, p.lon]) || !categoryNames[p.category]) fail('point WGS84 or category')
  for (const r of data.routes)
    if (
      !Array.isArray(r.coords) ||
      r.coords.length < 2 ||
      !r.coords.every(coord) ||
      !modeNames[r.mode]
    )
      fail('route WGS84 or mode')
  for (const d of data.days)
    if (!Array.isArray(d.focus) || d.focus.some((id) => !ids.has(id))) fail('focus reference')
  for (const source of Object.values(data.sources)) if (!safeUrl(source.url)) fail('source URL')
  return data
}
export function geojson(data) {
  return {
    type: 'FeatureCollection',
    tripMetadata: {
      meta: data.meta,
      days: data.days,
      sources: data.sources,
      variants: data.ui?.variants,
    },
    features: [
      ...data.points.map(({ lat, lon, ...properties }) => ({
        type: 'Feature',
        id: properties.id,
        geometry: { type: 'Point', coordinates: [lon, lat] },
        properties,
      })),
      ...data.routes.map(({ coords, ...properties }) => ({
        type: 'Feature',
        id: properties.id,
        geometry: { type: 'LineString', coordinates: coords.map(([lat, lon]) => [lon, lat]) },
        properties,
      })),
    ],
  }
}
export const escapeXml = (value) =>
  String(value ?? '').replace(
    /[&<>"']/g,
    (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;' })[c],
  )
export function kml(data) {
  return `<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><description>${escapeXml(JSON.stringify({ meta: data.meta, days: data.days, sources: data.sources }))}</description>${geojson(
    data,
  )
    .features.map((f) => {
      const coordinates =
        f.geometry.type === 'Point'
          ? f.geometry.coordinates.join(',')
          : f.geometry.coordinates.map((c) => c.join(',')).join(' ')
      const geometry = f.geometry.type === 'Point' ? 'Point' : 'LineString'
      return `<Placemark id="${escapeXml(f.id)}"><name>${escapeXml(f.properties.name || f.properties.title)}</name><description>${escapeXml(JSON.stringify(f.properties))}</description><${geometry}><coordinates>${coordinates}</coordinates></${geometry}></Placemark>`
    })
    .join('')}</Document></kml>`
}
