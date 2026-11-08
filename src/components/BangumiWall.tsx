import { useMemo, useState } from 'react'
import {
  COLLECTION_TYPES,
  SUBJECT_TYPES,
  SUBJECT_TYPE_LABEL,
  SORTS,
  fetchPublicCollections,
  selectItems,
  type SortId,
  type WallItem,
} from '@/lib/bangumi-wall'
import {
  DEFAULT_DISPLAY,
  SUBTITLE_FIELDS,
  renderTitle,
  renderSubtitle,
  type DisplayConfig,
  type TitleMode,
} from '@/lib/bangumi-wall-display'

interface Props {
  username: string
  initialItems: WallItem[]
  syncedAt: string | null
  syncFailed: boolean
}

function Cover({ item }: { item: WallItem }) {
  const [failed, setFailed] = useState(false)
  return item.cover && !failed ? (
    <img
      src={item.cover}
      alt=""
      loading="lazy"
      decoding="async"
      referrerPolicy="no-referrer"
      onError={() => setFailed(true)}
    />
  ) : (
    <span className="wall-cover-placeholder">{item.name}</span>
  )
}

export default function BangumiWall({ username, initialItems, syncedAt, syncFailed }: Props) {
  const [items, setItems] = useState(initialItems)
  const [lastSync, setLastSync] = useState(syncedAt)
  const [error, setError] = useState(syncFailed)
  const [loading, setLoading] = useState(false)
  const [types, setTypes] = useState<number[]>([])
  const [statuses, setStatuses] = useState<number[]>([])
  const [query, setQuery] = useState('')
  const [sort, setSort] = useState<SortId>('updatedAt')
  const [ascending, setAscending] = useState(false)
  const [display, setDisplay] = useState<DisplayConfig>({
    ...DEFAULT_DISPLAY,
    subtitleFields: ['year', 'myRate'],
  })
  const [limit, setLimit] = useState(60)
  const [beforeCoverOnly, setBeforeCoverOnly] = useState<DisplayConfig | null>(null)

  const visible = useMemo(
    () => selectItems(items, { types, statuses, query, sort, ascending }),
    [items, types, statuses, query, sort, ascending],
  )
  const mixedTypes = new Set(visible.map((item) => item.subjectType)).size > 1
  const coverOnly =
    display.titleMode === 'hidden' && display.subtitleFields.length === 0 && !display.showComment
  const countByType = (id: number) => items.filter((item) => item.subjectType === id).length
  const countByStatus = (id: number) =>
    items.filter(
      (item) => item.status === id && (!types.length || types.includes(item.subjectType)),
    ).length

  function resetFilters() {
    setTypes([])
    setStatuses([])
    setQuery('')
    setLimit(60)
  }
  async function refresh() {
    if (loading) return
    setLoading(true)
    try {
      const next = await fetchPublicCollections(username)
      setItems(next)
      setLastSync(new Date().toISOString())
      setError(false)
    } catch {
      setError(true)
    } finally {
      setLoading(false)
    }
  }
  function toggleCoverOnly() {
    if (coverOnly) {
      setDisplay(beforeCoverOnly ?? DEFAULT_DISPLAY)
    } else {
      setBeforeCoverOnly(display)
      setDisplay({ ...display, titleMode: 'hidden', subtitleFields: [], showComment: false })
    }
  }

  return (
    <div className="collection-wall">
      <header className="bangumi-masthead wall-masthead">
        <div className="bangumi-heading">
          <p className="bangumi-eyebrow">
            <span aria-hidden="true">✦</span>Bangumi Collection
          </p>
          <h1>
            收藏封面墙<span aria-hidden="true">✧</span>
          </h1>
          <p className="bangumi-intro">看过的故事，听过的旋律，还有下一份期待。</p>
          <a className="wall-back" href="/bangumi">
            ← 正在追番
          </a>
        </div>
        <div className="bangumi-edition">
          <span className="bangumi-edition-label">公开收藏</span>
          <p className="bangumi-count">
            {lastSync ? String(items.length).padStart(2, '0') : '—'}
            <span>项</span>
          </p>
          <a
            href={`https://bgm.tv/user/${encodeURIComponent(username)}`}
            target="_blank"
            rel="noopener noreferrer"
          >
            我的 Bangumi <span aria-hidden="true">↗</span>
          </a>
        </div>
      </header>

      <section className="wall-controls" aria-label="筛选收藏">
        <div className="wall-filter-row" role="group" aria-label="作品类别，可多选">
          <span className="wall-filter-label">类别</span>
          <button
            type="button"
            aria-pressed={!types.length}
            onClick={() => {
              setTypes([])
              setLimit(60)
            }}
          >
            全部 <small>{items.length}</small>
          </button>
          {SUBJECT_TYPES.map((type) => (
            <button
              type="button"
              key={type.id}
              aria-pressed={types.includes(type.id)}
              onClick={() => {
                setTypes(
                  types.includes(type.id)
                    ? types.filter((id) => id !== type.id)
                    : [...types, type.id],
                )
                setLimit(60)
              }}
            >
              {type.label} <small>{countByType(type.id)}</small>
            </button>
          ))}
        </div>
        <div className="wall-filter-row" role="group" aria-label="收藏状态，可多选">
          <span className="wall-filter-label">状态</span>
          <button
            type="button"
            aria-pressed={!statuses.length}
            onClick={() => {
              setStatuses([])
              setLimit(60)
            }}
          >
            全部
          </button>
          {COLLECTION_TYPES.map((status) => (
            <button
              type="button"
              key={status.id}
              aria-pressed={statuses.includes(status.id)}
              onClick={() => {
                setStatuses(
                  statuses.includes(status.id)
                    ? statuses.filter((id) => id !== status.id)
                    : [...statuses, status.id],
                )
                setLimit(60)
              }}
            >
              {status.label} <small>{countByStatus(status.id)}</small>
            </button>
          ))}
        </div>
        <div className="wall-search-row">
          <label className="wall-search">
            <span aria-hidden="true">⌕</span>
            <input
              type="search"
              aria-label="搜索收藏"
              placeholder="搜索中文名或原名…"
              value={query}
              onChange={(event) => {
                setQuery(event.target.value)
                setLimit(60)
              }}
            />
          </label>
          <label className="wall-sort">
            排序
            <select
              value={sort}
              onChange={(event) => {
                const next = event.target.value as SortId
                setSort(next)
                setAscending(next === 'rank' || next === 'name')
                setLimit(60)
              }}
            >
              {SORTS.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.label}
                </option>
              ))}
            </select>
          </label>
          <button
            type="button"
            className="wall-direction"
            aria-label={ascending ? '切换为降序' : '切换为升序'}
            onClick={() => setAscending(!ascending)}
          >
            {ascending ? '↑ 升序' : '↓ 降序'}
          </button>
          <div className="wall-views" role="group" aria-label="显示视图">
            <button
              type="button"
              aria-pressed={display.view === 'grid'}
              onClick={() => setDisplay({ ...display, view: 'grid' })}
            >
              封面墙
            </button>
            <button
              type="button"
              aria-pressed={display.view === 'list'}
              onClick={() => setDisplay({ ...display, view: 'list' })}
            >
              列表
            </button>
          </div>
        </div>
        <details className="wall-display">
          <summary>显示设置</summary>
          <div className="wall-display-options">
            <label>
              标题
              <select
                value={display.titleMode}
                onChange={(event) =>
                  setDisplay({ ...display, titleMode: event.target.value as TitleMode })
                }
              >
                <option value="cn">中文名</option>
                <option value="original">原名</option>
                <option value="hidden">隐藏</option>
              </select>
            </label>
            <label>
              封面尺寸
              <select
                value={display.size}
                onChange={(event) =>
                  setDisplay({ ...display, size: event.target.value as DisplayConfig['size'] })
                }
              >
                <option value="sm">小</option>
                <option value="md">中</option>
                <option value="lg">大</option>
              </select>
            </label>
            <label>
              <input
                type="checkbox"
                checked={display.showComment}
                onChange={(event) => setDisplay({ ...display, showComment: event.target.checked })}
              />
              显示短评
            </label>
            <label>
              <input
                type="checkbox"
                checked={display.showTypeIcon}
                onChange={(event) => setDisplay({ ...display, showTypeIcon: event.target.checked })}
              />
              类别标记
            </label>
            <button type="button" aria-pressed={coverOnly} onClick={toggleCoverOnly}>
              只显示封面
            </button>
          </div>
          <fieldset className="wall-subtitles">
            <legend>
              封面信息 <span>可多选，按点选顺序显示</span>
            </legend>
            {SUBTITLE_FIELDS.map((field) => (
              <label key={field.id}>
                <input
                  type="checkbox"
                  checked={display.subtitleFields.includes(field.id)}
                  onChange={() =>
                    setDisplay({
                      ...display,
                      subtitleFields: display.subtitleFields.includes(field.id)
                        ? display.subtitleFields.filter((id) => id !== field.id)
                        : [...display.subtitleFields, field.id],
                    })
                  }
                />
                {field.label}
              </label>
            ))}
          </fieldset>
        </details>
      </section>

      <div className="wall-results-heading">
        <p role="status" aria-live="polite">
          {lastSync ? (
            <>
              共 <strong>{visible.length}</strong> 项
              {visible.length !== items.length && ` / ${items.length} 项收藏`}
            </>
          ) : (
            '收藏暂未同步'
          )}
        </p>
        <button type="button" onClick={refresh} disabled={loading}>
          {loading ? '正在同步…' : '刷新收藏 ↻'}
        </button>
      </div>
      {error && (
        <div className="wall-notice" role="alert">
          <p>
            暂时无法连接 Bangumi。
            {lastSync
              ? '以下保留上次同步的收藏，可以稍后重试。'
              : '可以重试，或前往 Bangumi 查看收藏。'}
          </p>
          <button type="button" onClick={refresh} disabled={loading}>
            重新同步
          </button>
        </div>
      )}
      {visible.length ? (
        <ul
          className={`wall-items wall-${display.view} wall-size-${display.size}${coverOnly ? ' wall-covers-only' : ''}`}
          aria-label="收藏列表"
          aria-busy={loading}
        >
          {visible.slice(0, limit).map((item) => {
            const title = renderTitle(item, display.titleMode)
            const subtitle = renderSubtitle(item, display.subtitleFields)
            const comment = display.showComment && item.comment
            return (
              <li key={item.id} className="wall-item">
                <a
                  href={`https://bgm.tv/subject/${item.id}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`${item.name}，在 Bangumi 打开`}
                  title={item.comment ? `${item.name}\n${item.comment}` : item.name}
                >
                  <div className="wall-cover">
                    <Cover key={item.cover} item={item} />
                    {display.showTypeIcon && mixedTypes && (
                      <span className="wall-type">{SUBJECT_TYPE_LABEL[item.subjectType]}</span>
                    )}
                    <span className="wall-open" aria-hidden="true">
                      ↗
                    </span>
                  </div>
                  {(title || subtitle || comment) && (
                    <div className="wall-card-copy">
                      {title && <h2>{title}</h2>}
                      {subtitle && <p className="wall-metadata">{subtitle}</p>}
                      {comment && <p className="wall-comment">{comment}</p>}
                    </div>
                  )}
                </a>
              </li>
            )
          })}
        </ul>
      ) : (
        !loading &&
        !(!lastSync && error) && (
          <div className="wall-empty">
            <span aria-hidden="true">✧</span>
            <h2>{items.length ? '没有符合条件的收藏' : '还没有公开收藏'}</h2>
            <p>
              {items.length
                ? '试试其他类别、收藏状态或关键词。'
                : '在 Bangumi 标记作品后，就能在这里看到它们。'}
            </p>
            {!!items.length && (
              <button type="button" onClick={resetFilters}>
                清除筛选
              </button>
            )}
          </div>
        )
      )}
      {visible.length > limit && (
        <div className="wall-load-more">
          <button type="button" onClick={() => setLimit(limit + 60)}>
            加载更多（剩余 {visible.length - limit} 项）
          </button>
        </div>
      )}
      <footer className="bangumi-footnote wall-footnote">
        <span>
          数据来自 Bangumi · 仅展示公开收藏
          {lastSync && (
            <>
              {' '}
              · 同步于{' '}
              <time dateTime={lastSync}>
                {new Date(lastSync).toLocaleString('zh-CN', {
                  timeZone: 'Asia/Shanghai',
                  hour12: false,
                })}
              </time>
            </>
          )}
        </span>
        <span>
          基于{' '}
          <a
            href="https://github.com/Wangs-official/bangumi_wall"
            target="_blank"
            rel="noopener noreferrer"
          >
            bangumi_wall ↗
          </a>{' '}
          · <a href="/licenses/bangumi-wall.txt">MIT</a>
        </span>
      </footer>
    </div>
  )
}
