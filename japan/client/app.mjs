import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import './app.css'
import {
  categoryNames,
  modeNames,
  modeStyles,
  safeUrl,
  selectRecords,
  selectedDay,
} from '../shared/model.mjs'

const $ = (selector) => document.querySelector(selector)
const root = $('#japan-app')
const lifecycle = new AbortController()
const csrf = $('meta[name="japan-csrf"]').content
const listen = (node, type, fn) => node.addEventListener(type, fn, { signal: lifecycle.signal })
const text = (tag, content, className) => {
  const node = document.createElement(tag)
  node.textContent = content
  if (className) node.className = className
  return node
}
const button = (content, fn) => {
  const node = text('button', content)
  node.type = 'button'
  node.addEventListener('click', fn)
  return node
}
const link = (label, value) => {
  const href = safeUrl(value)
  const node = text(href ? 'a' : 'span', label)
  if (href) {
    node.href = href
    node.target = '_blank'
    node.rel = 'noopener noreferrer'
  }
  return node
}
const addText = (parent, label, value) => {
  if (value) {
    parent.append(text('dt', label), text('dd', value))
  }
}
const state = {
  day: 0,
  lake: '',
  optional: true,
  labels: true,
  search: '',
  categories: Object.keys(categoryNames),
  modes: Object.keys(modeNames),
}
let data,
  map,
  layers,
  sightlines,
  tiles,
  poll,
  expired = false,
  pick = false,
  editing = false,
  fallback = false,
  tilesTimer
let channel
try {
  channel = new BroadcastChannel('japan-session')
} catch {
  /* Focus checks also cover unsupported browsers. */
}
function editTokens() {
  try {
    return JSON.parse(sessionStorage.getItem('japan-edit-tokens') || '{}')
  } catch {
    return {}
  }
}
function lock(broadcast = false) {
  if (expired) return
  expired = true
  if (broadcast) channel?.postMessage('logout')
  clearInterval(poll)
  clearTimeout(tilesTimer)
  lifecycle.abort()
  try {
    map?.remove()
    sessionStorage.removeItem('japan-edit-tokens')
  } catch {
    /* Best effort UI cleanup. */
  }
  data = null
  root.replaceChildren(
    text('p', '会话已结束，请重新登录。'),
    link('重新登录', `${location.origin}/japan`),
  )
  root.style.visibility = 'visible'
}
async function api(path, options = {}) {
  const result = await fetch(path, {
    credentials: 'same-origin',
    cache: 'no-store',
    signal: lifecycle.signal,
    ...options,
  })
  if (expired) throw new Error('会话已结束。')
  if ([401, 403].includes(result.status) && path !== '/japan/collaboration') {
    lock()
    throw new Error('请重新登录。')
  }
  const value = await result.json().catch(() => ({}))
  if (!result.ok)
    throw Object.assign(new Error(value.error || '请求失败，请稍后重试。'), {
      status: result.status,
    })
  return value
}
async function sessionCheck() {
  try {
    const session = await api('/japan/session')
    if (Date.now() >= session.expires) lock()
    else if (!expired) root.style.visibility = 'visible'
  } catch {
    lock()
  }
}
function fragment() {
  history.replaceState(
    null,
    '',
    `/japan#${new URLSearchParams({ day: String(state.day), lake: state.lake })}`,
  )
}
function fitRegion(key) {
  const region = data.ui.regions[key]
  if (!region) return
  map.fitBounds(
    [
      [region.bounds[0], region.bounds[1]],
      [region.bounds[2], region.bounds[3]],
    ],
    { padding: [25, 25], maxZoom: region.zoom || 14, animate: false },
  )
}
function fitDay() {
  const d = selectedDay(data, state.day, state.lake)
  const visible = selectRecords(data, state).points
  let points = visible.filter((p) => d?.focus.includes(p.id))
  if (!points.length) points = visible
  if (points.length)
    map.fitBounds(
      points.map((p) => [p.lat, p.lon]),
      { padding: [35, 35], maxZoom: 14, animate: false },
    )
}
function setDay(day) {
  state.day = Math.max(0, Math.min(data.days.length, Number(day)))
  $('#day').value = String(state.day)
  $('#detail').replaceChildren()
  render()
  if (state.day) fitDay()
  else fitRegion(data.ui.overviewRegion)
  fragment()
}
function dates(record) {
  return record.days
    .map((n) => data.days.find((d) => d.day === n)?.label)
    .filter(Boolean)
    .join('、')
}
function sources(record, parent) {
  const div = text('div', '', 'j-links')
  for (const key of record.sources) {
    const source = data.sources[key]
    if (source) div.append(link(source.title, source.url))
  }
  if (record.source_url) div.append(link('贡献者提供的来源（待核实）', record.source_url))
  parent.append(div)
}
function revealDetails() {
  $('#panel').classList.remove('j-collapsed')
  $('#toggle-panel').setAttribute('aria-expanded', 'true')
  $('#panel').scrollTo({ top: Math.max(0, $('#detail').offsetTop - 8), behavior: 'smooth' })
}
function showPoint(point, zoom = true) {
  const card = text('article', '', 'j-card j-detail')
  card.append(
    button('关闭详情', () => $('#detail').replaceChildren()),
    text('h2', point.name),
    text('p', point.jp, 'j-jp'),
  )
  const info = document.createElement('dl')
  addText(info, '日期', dates(point))
  addText(info, '建议时间', point.time)
  addText(info, '停留长度', point.stay)
  addText(info, '到达方式', point.access)
  addText(info, '备注', point.note)
  addText(info, '坐标精度', point.coordinate_note)
  addText(info, 'WGS84', `${point.lat.toFixed(5)}, ${point.lon.toFixed(5)}`)
  addText(info, '状态', point.optional ? '可选候选，不是必到项目' : '基准方案参考点')
  if (point.collaboration)
    addText(
      info,
      '协作贡献',
      `${point.author} · ${new Date(point.updatedAt).toLocaleString('zh-CN', { timeZone: 'Asia/Tokyo' })}（日本时间）`,
    )
  card.append(info)
  sources(point, card)
  card.append(
    link('主动打开地理院地图核对道路 ↗', `https://maps.gsi.go.jp/#16/${point.lat}/${point.lon}/`),
  )
  if (point.collaboration && editTokens()[point.id])
    card.append(button('编辑这个新增地点', () => startEdit(point)))
  $('#detail').replaceChildren(card)
  if (zoom) map.setView([point.lat, point.lon], 15, { animate: false })
  revealDetails()
}
function showRoute(route) {
  const card = text('article', '', 'j-card j-detail'),
    info = document.createElement('dl')
  card.append(
    button('关闭详情', () => $('#detail').replaceChildren()),
    text('h2', route.title),
  )
  addText(info, '方式', modeNames[route.mode])
  addText(info, '日期', dates(route))
  addText(info, '车程／活动长度（原始参考）', route.duration)
  addText(info, '时间窗口与状态', route.time)
  addText(info, '换乘、等待与风险提示（原文）', route.note)
  addText(
    info,
    '独立等待与风险余量',
    '原资料未单列的分钟数不作推算；以上车程不自动包含候车、换乘或风险余量。',
  )
  addText(info, '几何精度', route.geometry_status)
  if (route.mode === 'view')
    card.append(text('p', '仅摄影方向，非步行路线。不得据此跨湖、上冰或进入农田。', 'j-notice'))
  card.append(info)
  sources(route, card)
  $('#detail').replaceChildren(card)
  revealDetails()
}
function draw() {
  layers.clearLayers()
  sightlines.clearLayers()
  const selected = selectRecords(data, state)
  for (const route of selected.routes) {
    const [color, dashArray] = modeStyles[route.mode]
    const group = route.mode === 'view' ? sightlines : layers
    const line = L.polyline(route.coords, {
      color,
      dashArray,
      weight: route.mode === 'view' ? 2 : 3,
      opacity: route.optional ? 0.55 : 0.85,
    }).addTo(group)
    line
      .bindTooltip(
        text('span', `${route.title}${route.mode === 'view' ? ' · 仅摄影方向，非步行路线' : ''}`),
      )
      .on('click', () => showRoute(route))
    const path = line.getElement()
    if (path) {
      path.setAttribute('tabindex', '0')
      path.setAttribute('role', 'button')
      path.setAttribute('aria-label', route.title)
      path.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault()
          showRoute(route)
        }
      })
    }
    if (state.day && route.mode !== 'view') {
      const a = route.coords.at(-2),
        b = route.coords.at(-1)
      const pa = map.latLngToLayerPoint(a),
        pb = map.latLngToLayerPoint(b)
      const angle = (Math.atan2(pb.y - pa.y, pb.x - pa.x) * 180) / Math.PI
      const arrow = text('span', '➤', 'j-route-arrow')
      arrow.style.color = color
      arrow.style.transform = `rotate(${angle}deg)`
      L.marker([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], {
        interactive: false,
        icon: L.divIcon({ html: arrow, className: 'j-arrow-icon', iconSize: [18, 18] }),
      }).addTo(group)
    }
  }
  for (const point of selected.points) {
    const markerElement = text(
      'span',
      { station: '▲', airport: '◆', photo: '★', stay: '■', event: '⬢', sight: '●', reference: '△' }[
        point.category
      ],
      'j-marker',
    )
    markerElement.style.color = data.colors[point.category]
    const marker = L.marker([point.lat, point.lon], {
      title: point.name,
      alt: point.name,
      keyboard: true,
      icon: L.divIcon({
        html: markerElement,
        className: `j-marker-icon${point.optional ? ' j-optional' : ''}`,
        iconSize: [26, 26],
        iconAnchor: [13, 13],
      }),
    }).addTo(layers)
    marker.on('click', () => showPoint(point, false))
    marker.getElement()?.setAttribute('aria-label', point.name)
    if (state.labels)
      marker.bindTooltip(text('span', point.name), {
        permanent: map.getZoom() >= 13,
        direction: 'top',
        offset: [0, -8],
      })
  }
  $('#count').textContent = `${selected.points.length} 个地点 · ${selected.routes.length} 段连接`
  return selected
}
function render() {
  if (!data || expired) return
  const selected = draw(),
    d = selectedDay(data, state.day, state.lake)
  $('#map-title').textContent = d ? `${d.label} · ${d.title}` : '全程概览'
  $('#previous').disabled = state.day === 0
  $('#next').disabled = state.day === data.days.length
  $('#summary').replaceChildren()
  if (d) {
    const card = text('article', '', 'j-card')
    card.append(
      text('small', `${d.date} · 住：${d.hotel}`),
      text('h2', d.title),
      text('p', d.description),
      text('p', d.when, 'j-notice'),
    )
    card.append(
      text('p', '时间是建议、候选或参考，不代表活动确认、天气保证或已出票班次。', 'j-muted'),
    )
    $('#summary').append(card)
  } else {
    $('#summary').append(
      text(
        'p',
        `${data.days.length} 天 · ${data.meta.nights} 晚 · ${data.meta.people} 人 · 日本时间`,
        'j-notice',
      ),
      text('p', data.meta.limitations, 'j-muted'),
    )
  }
  $('#list').replaceChildren()
  if (!state.day && !state.search)
    for (const source of data.days) {
      const day = selectedDay(data, source.day, state.lake)
      const card = button('', () => setDay(day.day))
      card.className = 'j-card j-day-card'
      card.append(
        text('small', day.label),
        text('h3', day.title),
        text('p', day.when),
        text('span', `住：${day.hotel}`),
      )
      $('#list').append(card)
    }
  else {
    $('#list').append(text('h3', '地点与选项'))
    for (const point of selected.points) {
      const b = button(`${point.optional ? '◇' : '●'} ${point.name}`, () => showPoint(point))
      b.className = 'j-list-button'
      $('#list').append(b)
    }
    $('#list').append(text('h3', '交通与摄影视线'))
    for (const route of selected.routes) {
      const b = button(`${modeNames[route.mode]} · ${route.title}`, () => showRoute(route))
      b.className = 'j-list-button'
      $('#list').append(b)
    }
  }
  for (const option of $('#day').options)
    if (Number(option.value)) {
      const day = selectedDay(data, Number(option.value), state.lake)
      option.textContent = `${day.label} ${day.title}`
    }
}
function option(select, value, label) {
  const o = text('option', label)
  o.value = value
  select.append(o)
}
function checks(target, names, chosen, onChange) {
  for (const [key, name] of Object.entries(names)) {
    const label = document.createElement('label'),
      input = document.createElement('input')
    input.type = 'checkbox'
    input.value = key
    input.checked = true
    label.append(input, text('span', name))
    if (modeStyles[key]) {
      const swatch = text('span', '', 'j-swatch')
      swatch.style.borderColor = modeStyles[key][0]
      swatch.style.borderTopStyle = modeStyles[key][1] ? 'dashed' : 'solid'
      label.append(swatch)
    }
    target.append(label)
    listen(input, 'change', () => {
      onChange([...target.querySelectorAll('input:checked')].map((el) => el.value))
      render()
    })
  }
}
function tileStatus(message, failed = false) {
  $('#base-status').textContent = message
  $('#retry-tiles').hidden = !failed
  $('#fallback').hidden = !failed || fallback
}
function initTiles() {
  tiles = L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png', {
    minZoom: 2,
    maxZoom: 18,
    maxNativeZoom: 18,
    attribution:
      '<a href="https://maps.gsi.go.jp/development/ichiran.html" target="_blank" rel="noopener noreferrer">出典：国土地理院</a>',
    keepBuffer: 0,
    updateWhenIdle: true,
    updateWhenZooming: false,
    crossOrigin: true,
  })
  let failed = 0,
    loaded = 0
  tiles.on('loading', () => {
    failed = 0
    loaded = 0
    tileStatus('正在加载详细底图…')
    clearTimeout(tilesTimer)
    tilesTimer = setTimeout(() => tileStatus('详细底图连接超时；日程仍可查看。', true), 12000)
  })
  tiles.on('tileerror', () => {
    failed++
    tileStatus('部分或全部详细瓦片加载失败；可重试或使用点线示意。', true)
  })
  tiles.on('tileload', () => loaded++)
  tiles.on('load', () => {
    clearTimeout(tilesTimer)
    if (!fallback)
      tileStatus(
        failed || !loaded
          ? '详细底图未完整加载；日程仍可查看。'
          : '国土地理院标准地图 · 道路与地名底图',
        failed > 0 || !loaded,
      )
  })
  tiles.addTo(map)
  listen($('#retry-tiles'), 'click', () => {
    fallback = false
    if (!map.hasLayer(tiles)) tiles.addTo(map)
    else tiles.redraw()
  })
  listen($('#fallback'), 'click', () => {
    fallback = true
    map.removeLayer(tiles)
    clearTimeout(tilesTimer)
    tileStatus('降级：仅点线示意，无详细道路底图；不可用于导航。', true)
  })
  listen(window, 'offline', () =>
    tileStatus('网络已断开；详细底图不可用，已加载日程仍可查看。', true),
  )
}
function startEdit(point) {
  const form = $('#add-point')
  editing = true
  for (const key of [
    'id',
    'author',
    'name',
    'jp',
    'lat',
    'lon',
    'time',
    'stay',
    'access',
    'note',
    'source_url',
    'region',
    'category',
    'variant',
  ])
    form.elements.namedItem(key).value = point[key] || ''
  form.elements.namedItem('day').value = point.days[0]
  $('#collaboration').open = true
  $('#cancel-edit').hidden = false
  $('#save-status').textContent = '正在编辑新增地点。'
  form.scrollIntoView({ block: 'nearest' })
}
async function refreshData() {
  data = await api('/japan/data')
  $('#updated').textContent =
    `资料更新 ${data.meta.updated} · 协作版本 ${data.collaborationRevision}`
  render()
}
async function init() {
  data = await api('/japan/data')
  const params = new URLSearchParams(location.hash.slice(1))
  state.lake = Object.hasOwn(data.ui.variants, params.get('lake'))
    ? params.get('lake')
    : data.ui.defaultVariant
  state.day = /^\d+$/.test(params.get('day') || '')
    ? Math.min(data.days.length, Number(params.get('day')))
    : 0
  $('#trip-title').textContent = data.meta.title
  $('#updated').textContent =
    `资料更新 ${data.meta.updated} · 协作版本 ${data.collaborationRevision}`
  for (const d of data.days) option($('#day'), d.day, d.label)
  $('#day').value = state.day
  for (const [key, variant] of Object.entries(data.ui.variants))
    option($('#lake'), key, variant.name)
  $('#lake').value = state.lake
  for (const [key, region] of Object.entries(data.ui.regions))
    $('#regions').append(button(region.name, () => fitRegion(key)))
  checks($('#categories'), categoryNames, state.categories, (value) => (state.categories = value))
  checks($('#modes'), modeNames, state.modes, (value) => (state.modes = value))
  map = L.map('map', {
    zoomControl: true,
    minZoom: 2,
    maxZoom: 18,
    attributionControl: true,
    zoomAnimation: false,
  })
  layers = L.layerGroup().addTo(map)
  sightlines = L.layerGroup().addTo(map)
  const initial = data.points.find((point) => point.id === data.ui.initialView?.pointId)
  if (initial) map.setView([initial.lat, initial.lon], data.ui.initialView.zoom, { animate: false })
  else fitRegion(data.ui.initialRegion)
  initTiles()
  map.on('zoomend', () => draw())
  map.on('click', (event) => {
    if (!pick) return
    $('#add-point').elements.namedItem('lat').value = event.latlng.lat.toFixed(6)
    $('#add-point').elements.namedItem('lon').value = event.latlng.lng.toFixed(6)
    pick = false
    $('#pick').textContent = '在地图上点选位置'
    $('#panel').classList.remove('j-collapsed')
    $('#toggle-panel').setAttribute('aria-expanded', 'true')
  })
  listen($('#day'), 'change', (e) => setDay(e.target.value))
  listen($('#previous'), 'click', () => setDay(state.day - 1))
  listen($('#next'), 'click', () => setDay(state.day + 1))
  listen($('#lake'), 'change', (e) => {
    state.lake = e.target.value
    $('#detail').replaceChildren()
    render()
    if (state.day) fitDay()
    else fitRegion(data.ui.variantRegion)
    fragment()
  })
  listen($('#search'), 'input', (e) => {
    state.search = e.target.value
    render()
  })
  listen($('#optional'), 'change', (e) => {
    state.optional = e.target.checked
    render()
  })
  listen($('#labels'), 'change', (e) => {
    state.labels = e.target.checked
    draw()
  })
  listen($('#toggle-panel'), 'click', () => {
    const collapsed = $('#panel').classList.toggle('j-collapsed')
    $('#toggle-panel').setAttribute('aria-expanded', String(!collapsed))
    setTimeout(() => map.invalidateSize(), 200)
  })
  for (const source of Object.values(data.sources))
    $('#source-list').append(link(source.title, source.url))
  const form = $('#add-point')
  for (const d of data.days) option(form.elements.namedItem('day'), d.day, d.label)
  for (const [k, v] of Object.entries(categoryNames))
    option(form.elements.namedItem('category'), k, v)
  form.elements.namedItem('category').value = 'sight'
  for (const [k, v] of Object.entries(data.ui.regions))
    option(form.elements.namedItem('region'), k, v.name)
  option(form.elements.namedItem('variant'), 'all', '全部方案共同候选')
  for (const [k, v] of Object.entries(data.ui.variants))
    option(form.elements.namedItem('variant'), k, v.name)
  listen($('#pick'), 'click', () => {
    pick = true
    $('#pick').textContent = '请在地图上点一下'
    if (matchMedia('(max-width: 760px)').matches) {
      $('#panel').classList.add('j-collapsed')
      $('#toggle-panel').setAttribute('aria-expanded', 'false')
    }
  })
  listen($('#cancel-edit'), 'click', () => {
    editing = false
    form.reset()
    form.elements.namedItem('id').value = ''
    $('#cancel-edit').hidden = true
    $('#save-status').textContent = ''
  })
  listen($('#refresh'), 'click', async () => {
    try {
      await refreshData()
      $('#save-status').textContent = '已刷新其他人的更新。'
    } catch (e) {
      $('#save-status').textContent = e.message
    }
  })
  listen(form, 'submit', async (event) => {
    event.preventDefault()
    const values = Object.fromEntries(new FormData(form))
    const id = values.id
    const submit = form.querySelector('[type="submit"]')
    submit.disabled = true
    try {
      const result = await api('/japan/collaboration', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': csrf },
        body: JSON.stringify({
          revision: data.collaborationRevision,
          ...(editing ? { id, editToken: editTokens()[id] } : {}),
          point: { ...values, days: [Number(values.day)] },
        }),
      })
      if (result.editToken) {
        const tokens = editTokens()
        tokens[result.id] = result.editToken
        sessionStorage.setItem('japan-edit-tokens', JSON.stringify(tokens))
      }
      await refreshData()
      $('#save-status').textContent =
        '已保存，其他人刷新后可见。此标签页保留新增地点的编辑凭证，退出后清除。'
      form.reset()
      form.elements.namedItem('id').value = ''
      editing = false
      $('#cancel-edit').hidden = true
    } catch (e) {
      if (!expired) $('#save-status').textContent = e.message
    } finally {
      if (!expired) submit.disabled = false
    }
  })
  listen($('#logout'), 'submit', async (event) => {
    event.preventDefault()
    const postBody = new URLSearchParams({ csrf })
    lock(true)
    try {
      const result = await fetch('/japan/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: postBody,
        credentials: 'same-origin',
        cache: 'no-store',
      })
      if (!result.ok) throw new Error('Logout not confirmed')
      location.replace('/japan')
    } catch {
      root.append(text('p', '网络中断，服务端退出尚未确认。请恢复网络后重新打开并退出。'))
    }
  })
  channel?.addEventListener('message', () => lock())
  listen(document, 'visibilitychange', () => {
    if (document.hidden) root.style.visibility = 'hidden'
    else void sessionCheck()
  })
  listen(window, 'focus', () => void sessionCheck())
  window.addEventListener('pagehide', () => lock(), { once: true })
  window.addEventListener('pageshow', (event) => {
    if (event.persisted) location.replace('/japan')
  })
  poll = setInterval(() => {
    if (!document.hidden) void sessionCheck()
  }, 30000)
  render()
  if (state.day) fitDay()
}
init().catch((error) => {
  if (!expired) {
    $('#fatal').textContent = error.message || '地图暂不可用。'
    $('#base-status').textContent = '行程尚未加载，请稍后刷新。'
  }
})
