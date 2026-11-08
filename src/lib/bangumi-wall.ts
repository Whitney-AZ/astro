// Adapted from Wangs-official/bangumi_wall (MIT).
// See public/licenses/bangumi-wall.txt for the upstream license.
export const SUBJECT_TYPES = [
  { id: 2, label: '动画' },
  { id: 1, label: '书籍' },
  { id: 4, label: '游戏' },
  { id: 3, label: '音乐' },
  { id: 6, label: '三次元' },
] as const

export const COLLECTION_TYPES = [
  { id: 1, label: '想看' },
  { id: 2, label: '看过' },
  { id: 3, label: '在看' },
  { id: 4, label: '搁置' },
  { id: 5, label: '抛弃' },
] as const

export const SUBJECT_TYPE_LABEL: Record<number, string> = Object.fromEntries(
  SUBJECT_TYPES.map((type) => [type.id, type.label]),
)
export const COLLECTION_TYPE_LABEL: Record<number, string> = Object.fromEntries(
  COLLECTION_TYPES.map((type) => [type.id, type.label]),
)

export interface WallItem {
  id: number
  subjectType: number
  status: number
  name: string
  originalName: string
  cover: string | null
  date: string | null
  score: number | null
  rate: number | null
  epStatus: number
  eps: number
  comment: string
  updatedAt: string
  rank: number | null
}

function positive(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) && value > 0 ? value : null
}

export function toWallItem(collection: any): WallItem | null {
  const subject = collection?.subject
  if (
    !subject ||
    collection.private ||
    !Number.isSafeInteger(collection.subject_id) ||
    collection.subject_id <= 0 ||
    !SUBJECT_TYPES.some((type) => type.id === collection.subject_type) ||
    !COLLECTION_TYPES.some((type) => type.id === collection.type)
  )
    return null
  const cover = subject.images?.common ?? subject.images?.medium ?? subject.images?.large
  return {
    id: collection.subject_id,
    subjectType: collection.subject_type,
    status: collection.type,
    name: subject.name_cn || subject.name || `条目 ${collection.subject_id}`,
    originalName: subject.name || '',
    cover: typeof cover === 'string' && /^https:\/\//i.test(cover) ? cover : null,
    date: typeof subject.date === 'string' ? subject.date : null,
    score: positive(subject.score),
    rate: positive(collection.rate),
    epStatus: positive(collection.ep_status) ?? 0,
    eps: positive(subject.eps) ?? 0,
    comment: typeof collection.comment === 'string' ? collection.comment : '',
    updatedAt: typeof collection.updated_at === 'string' ? collection.updated_at : '',
    rank: positive(subject.rank),
  }
}

/** Only public collections: no OAuth, cookies, tokens, or third-party mirror. */
export async function fetchPublicCollections(
  username: string,
  request: typeof fetch = fetch,
): Promise<WallItem[]> {
  const signal = AbortSignal.timeout(30000)
  async function page(offset: number) {
    const query = new URLSearchParams({ limit: '50', offset: String(offset) })
    const response = await request(
      `https://api.bgm.tv/v0/users/${encodeURIComponent(username)}/collections?${query}`,
      {
        credentials: 'omit',
        headers: {
          Accept: 'application/json',
          ...(typeof window === 'undefined'
            ? { 'User-Agent': 'Whitney-AZ/astro (https://github.com/Whitney-AZ/astro)' }
            : {}),
        },
        signal,
      },
    )
    if (!response.ok) throw new Error(`Bangumi API ${response.status}`)
    const result = await response.json()
    if (
      !Array.isArray(result.data) ||
      !Number.isSafeInteger(result.total) ||
      result.total < 0 ||
      !Number.isSafeInteger(result.limit) ||
      result.limit < 1
    ) {
      throw new Error('Invalid Bangumi collection response')
    }
    if (offset < result.total && result.data.length === 0) {
      throw new Error('Incomplete Bangumi collection response')
    }
    return result as { data: unknown[]; total: number; limit: number }
  }
  const first = await page(0)
  const raw = [...first.data]
  // Bounded batches keep requests modest; all pages must succeed before replacing a snapshot.
  for (let offset = first.limit; offset < first.total; offset += first.limit * 3) {
    const offsets = [offset, offset + first.limit, offset + first.limit * 2].filter(
      (value) => value < first.total,
    )
    const pages = await Promise.all(offsets.map(page))
    pages.forEach((result) => raw.push(...result.data))
  }
  const unique = new Map<number, WallItem>()
  for (const collection of raw) {
    const item = toWallItem(collection)
    if (item) unique.set(item.id, item)
  }
  return [...unique.values()]
}

export const SORTS = [
  { id: 'updatedAt', label: '收藏时间' },
  { id: 'rate', label: '我的评分' },
  { id: 'score', label: 'Bangumi 评分' },
  { id: 'rank', label: '排名' },
  { id: 'date', label: '发行日期' },
  { id: 'name', label: '名称' },
] as const
export type SortId = (typeof SORTS)[number]['id']

export function selectItems(
  items: WallItem[],
  options: {
    types: number[]
    statuses: number[]
    query: string
    sort: SortId
    ascending: boolean
  },
): WallItem[] {
  const query = options.query.trim().toLocaleLowerCase()
  return items
    .filter(
      (item) =>
        (!options.types.length || options.types.includes(item.subjectType)) &&
        (!options.statuses.length || options.statuses.includes(item.status)) &&
        (!query || `${item.name} ${item.originalName}`.toLocaleLowerCase().includes(query)),
    )
    .sort((a, b) => {
      const left = a[options.sort],
        right = b[options.sort]
      // Unrated / unknown values remain last in either direction.
      if (left === null || left === '') return right === null || right === '' ? a.id - b.id : 1
      if (right === null || right === '') return -1
      const comparison =
        typeof left === 'number' && typeof right === 'number'
          ? left - right
          : options.sort === 'updatedAt'
            ? Date.parse(String(left)) - Date.parse(String(right))
            : String(left).localeCompare(String(right), 'zh-CN')
      return (options.ascending ? comparison : -comparison) || a.id - b.id
    })
}
