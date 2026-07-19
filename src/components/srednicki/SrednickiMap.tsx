import { useEffect, useMemo, useRef, useState } from 'react'
import {
  srednickiChildren,
  srednickiPartNames,
  srednickiSectionById,
  srednickiSections,
} from '@/data/srednicki'
import type { SrednickiNoteLink } from '@/utils/srednicki'

type Props = {
  notesBySection: Record<string, SrednickiNoteLink[]>
}

type Point = { x: number; y: number }
type NoteFilter = 'all' | 'done' | 'todo'

const edges = srednickiSections.flatMap((section) =>
  section.prereqs.map((from) => ({ from, to: section.id })),
)

function collectRelated(start: number, next: (id: number) => number[]) {
  const found = new Set<number>()
  const pending = [...next(start)]

  while (pending.length) {
    const id = pending.pop()!
    if (found.has(id)) continue
    found.add(id)
    pending.push(...next(id))
  }

  return found
}

function buildLayout(width: number) {
  const safeWidth = Math.max(320, Math.round(width))
  const leftPad = safeWidth < 560 ? 42 : 60
  const rightPad = 14
  const usableWidth = safeWidth - leftPad - rightPad
  const maxAcross = Math.max(7, Math.floor(usableWidth / 42))
  const levels = new Map<number, typeof srednickiSections>()

  for (const section of srednickiSections) {
    const group = levels.get(section.depth) ?? []
    group.push(section)
    levels.set(section.depth, group)
  }

  const positions = new Map<number, Point>()
  const bandTops = new Map<number, number>()
  let cursorY = 34

  for (const depth of [...levels.keys()].sort((a, b) => a - b)) {
    const items = levels.get(depth)!.sort((a, b) => a.id - b.id)
    const rows = Math.ceil(items.length / maxAcross)
    bandTops.set(depth, cursorY)

    items.forEach((section, index) => {
      const row = Math.floor(index / maxAcross)
      const rowStart = row * maxAcross
      const count = Math.min(maxAcross, items.length - rowStart)
      const column = index - rowStart
      positions.set(section.id, {
        x: leftPad + (usableWidth * (column + 0.5)) / count,
        y: cursorY + row * 50,
      })
    })

    cursorY += rows * 50 + 24
  }

  return {
    width: safeWidth,
    height: cursorY + 4,
    positions,
    bandTops,
    levels: [...levels.keys()].sort((a, b) => a - b),
    leftPad,
    rightPad,
  }
}

function pathBetween(from: Point, to: Point) {
  const delta = Math.max(20, (to.y - from.y) * 0.42)
  return `M ${from.x} ${from.y + 15} C ${from.x} ${from.y + delta}, ${to.x} ${
    to.y - delta
  }, ${to.x} ${to.y - 16}`
}

export function SrednickiMap({ notesBySection }: Props) {
  const graphWrapRef = useRef<HTMLDivElement>(null)
  const [graphWidth, setGraphWidth] = useState(1100)
  const [selectedId, setSelectedId] = useState<number | null>(null)
  const [noteFilter, setNoteFilter] = useState<NoteFilter>('all')
  const [query, setQuery] = useState('')
  const [nodeTooltip, setNodeTooltip] = useState<{
    id: number
    left: number
    top: number
    placement: 'above' | 'below'
  } | null>(null)

  useEffect(() => {
    const element = graphWrapRef.current
    if (!element) return

    const updateWidth = () => setGraphWidth(element.getBoundingClientRect().width)
    updateWidth()
    const observer = new ResizeObserver(updateWidth)
    observer.observe(element)
    return () => observer.disconnect()
  }, [])

  const layout = useMemo(() => buildLayout(graphWidth), [graphWidth])
  const ancestors = useMemo(
    () =>
      selectedId
        ? collectRelated(selectedId, (id) => srednickiSectionById.get(id)?.prereqs ?? [])
        : new Set<number>(),
    [selectedId],
  )
  const descendants = useMemo(
    () =>
      selectedId
        ? collectRelated(selectedId, (id) => srednickiChildren.get(id) ?? [])
        : new Set<number>(),
    [selectedId],
  )
  const selectedSection = selectedId ? srednickiSectionById.get(selectedId) : undefined
  const completedCount = Object.values(notesBySection).filter((notes) => notes.length > 0).length
  const normalizedQuery = query.trim().toLocaleLowerCase()
  const visibleSections = srednickiSections.filter((section) => {
    const hasNote = Boolean(notesBySection[String(section.id)]?.length)
    const matchesFilter = noteFilter === 'all' || (noteFilter === 'done' ? hasNote : !hasNote)
    const matchesQuery =
      !normalizedQuery ||
      String(section.id) === normalizedQuery ||
      section.title.toLocaleLowerCase().includes(normalizedQuery)
    return matchesFilter && matchesQuery
  })

  const showNodeTooltip = (element: SVGGElement, id: number) => {
    const graphWrap = graphWrapRef.current
    if (!graphWrap) return

    const wrapRect = graphWrap.getBoundingClientRect()
    const nodeRect = element.getBoundingClientRect()
    const center = nodeRect.left - wrapRect.left + nodeRect.width / 2
    const horizontalPadding = Math.min(wrapRect.width / 2, wrapRect.width < 480 ? 118 : 188)
    const left = Math.max(horizontalPadding, Math.min(center, wrapRect.width - horizontalPadding))
    const nodeTop = nodeRect.top - wrapRect.top
    const placement = nodeTop < 82 ? 'below' : 'above'
    const top = placement === 'above' ? nodeTop - 10 : nodeRect.bottom - wrapRect.top + 10

    setNodeTooltip({ id, left, top, placement })
  }

  const sectionHref = (id: number) =>
    notesBySection[String(id)]?.[0]?.href ?? `/srednicki/sections/${id}`

  return (
    <div className="srednicki-app">
      <header className="srednicki-hero">
        <div>
          <p className="srednicki-eyebrow">Quantum Field Theory · Mark Srednicki</p>
          <h1>章节依赖与笔记</h1>
        </div>
        <dl className="srednicki-stats" aria-label="地图概况">
          <div>
            <dt>章节</dt>
            <dd>{srednickiSections.length}</dd>
          </div>
          <div>
            <dt>直接依赖</dt>
            <dd>{edges.length}</dd>
          </div>
          <div>
            <dt>已有笔记</dt>
            <dd>{completedCount}</dd>
          </div>
        </dl>
      </header>

      <section className="srednicki-map-shell" aria-labelledby="dependency-map-heading">
        <div className="srednicki-toolbar">
          <div>
            <p className="srednicki-kicker">Interactive map</p>
            <h2 id="dependency-map-heading">依赖网络</h2>
          </div>
          <label className="srednicki-picker">
            <span>聚焦章节</span>
            <select
              value={selectedId ?? ''}
              onChange={(event) =>
                setSelectedId(event.target.value ? Number(event.target.value) : null)
              }
            >
              <option value="">显示全书</option>
              {srednickiSections.map((section) => (
                <option key={section.id} value={section.id}>
                  {section.id}. {section.title}
                </option>
              ))}
            </select>
          </label>
        </div>

        <div className="srednicki-selection" aria-live="polite">
          {selectedSection ? (
            <>
              <div className="srednicki-selection-heading">
                <div>
                  <p>{srednickiPartNames[selectedSection.part]}</p>
                  <h3>
                    {selectedSection.id}. {selectedSection.title}
                  </h3>
                </div>
                <button type="button" onClick={() => setSelectedId(null)}>
                  清除聚焦
                </button>
              </div>
              <div className="srednicki-selection-grid">
                <div>
                  <span>笔记状态</span>
                  <a
                    className={`srednicki-note-link ${
                      notesBySection[String(selectedSection.id)]?.length ? 'is-done' : 'is-todo'
                    }`}
                    href={sectionHref(selectedSection.id)}
                  >
                    {notesBySection[String(selectedSection.id)]?.length
                      ? `阅读：${notesBySection[String(selectedSection.id)][0].title}`
                      : '尚未做笔记 · 查看章节页'}
                  </a>
                </div>
                <div>
                  <span>直接前置</span>
                  <div className="srednicki-section-links">
                    {selectedSection.prereqs.length ? (
                      selectedSection.prereqs.map((id) => (
                        <button key={id} type="button" onClick={() => setSelectedId(id)}>
                          {id}. {srednickiSectionById.get(id)?.title}
                        </button>
                      ))
                    ) : (
                      <strong>无</strong>
                    )}
                  </div>
                </div>
                <div>
                  <span>完整前置链</span>
                  <strong>{ancestors.size} 节</strong>
                </div>
                <div>
                  <span>直接后续 / 完整后续链</span>
                  <strong>
                    {srednickiChildren.get(selectedSection.id)?.length ?? 0} / {descendants.size} 节
                  </strong>
                </div>
              </div>
            </>
          ) : (
            <p>
              点击节点可高亮完整前置链与后续链；章节笔记链接见下方索引。
            </p>
          )}
        </div>

        <div className="srednicki-legend" aria-label="图例">
          <span>
            <i className="part-dot part-1" />I · Spin Zero
          </span>
          <span>
            <i className="part-dot part-2" />
            II · Spin One Half
          </span>
          <span>
            <i className="part-dot part-3" />
            III · Spin One
          </span>
          <span>
            <i className="note-dot is-done" />
            已有笔记
          </span>
          <span>
            <i className="note-dot is-todo" />
            尚未笔记
          </span>
          <span>
            <i className="line-key upstream" />
            前置链
          </span>
          <span>
            <i className="line-key downstream" />
            后续链
          </span>
        </div>

        <div className="srednicki-graph-wrap" ref={graphWrapRef}>
          <svg
            className="srednicki-graph"
            viewBox={`0 0 ${layout.width} ${layout.height}`}
            role="img"
            aria-labelledby="srednicki-graph-title srednicki-graph-description"
          >
            <title id="srednicki-graph-title">Srednicki Quantum Field Theory 章节依赖图</title>
            <desc id="srednicki-graph-description">
              箭头从前置章节指向依赖它的章节。实线外环表示已有笔记，虚线外环表示尚未做笔记。
            </desc>
            <defs>
              <marker
                id="srednicki-arrow"
                viewBox="0 0 8 8"
                refX="7"
                refY="4"
                markerWidth="6"
                markerHeight="6"
                orient="auto"
              >
                <path d="M 0 0 L 8 4 L 0 8 z" className="arrow-neutral" />
              </marker>
              <marker
                id="srednicki-arrow-upstream"
                viewBox="0 0 8 8"
                refX="7"
                refY="4"
                markerWidth="6"
                markerHeight="6"
                orient="auto"
              >
                <path d="M 0 0 L 8 4 L 0 8 z" className="arrow-upstream" />
              </marker>
              <marker
                id="srednicki-arrow-downstream"
                viewBox="0 0 8 8"
                refX="7"
                refY="4"
                markerWidth="6"
                markerHeight="6"
                orient="auto"
              >
                <path d="M 0 0 L 8 4 L 0 8 z" className="arrow-downstream" />
              </marker>
            </defs>

            {layout.levels.map((depth) => {
              const y = layout.bandTops.get(depth)! - 24
              return (
                <g key={`level-${depth}`}>
                  <line
                    className="level-guide"
                    x1={layout.leftPad}
                    y1={y + 10}
                    x2={layout.width - layout.rightPad}
                    y2={y + 10}
                  />
                  <text className="level-label" x="2" y={y + 14}>
                    层 {depth}
                  </text>
                </g>
              )
            })}

            {edges.map((edge) => {
              const from = layout.positions.get(edge.from)!
              const to = layout.positions.get(edge.to)!
              const isUpstream = Boolean(
                selectedId &&
                  ancestors.has(edge.from) &&
                  (ancestors.has(edge.to) || edge.to === selectedId),
              )
              const isDownstream = Boolean(
                selectedId &&
                  (edge.from === selectedId || descendants.has(edge.from)) &&
                  descendants.has(edge.to),
              )
              const isFaded = Boolean(selectedId && !isUpstream && !isDownstream)
              const marker = isUpstream
                ? 'url(#srednicki-arrow-upstream)'
                : isDownstream
                  ? 'url(#srednicki-arrow-downstream)'
                  : 'url(#srednicki-arrow)'

              return (
                <path
                  key={`${edge.from}-${edge.to}`}
                  className={[
                    'edge',
                    isUpstream && 'is-upstream',
                    isDownstream && 'is-downstream',
                    isFaded && 'is-faded',
                  ]
                    .filter(Boolean)
                    .join(' ')}
                  d={pathBetween(from, to)}
                  markerEnd={marker}
                />
              )
            })}

            {srednickiSections.map((section) => {
              const point = layout.positions.get(section.id)!
              const isSelected = section.id === selectedId
              const isUpstream = ancestors.has(section.id)
              const isDownstream = descendants.has(section.id)
              const isFaded = Boolean(selectedId && !isSelected && !isUpstream && !isDownstream)
              const hasNote = Boolean(notesBySection[String(section.id)]?.length)
              const label = `${section.id}. ${section.title}。${
                hasNote ? '已有笔记' : '尚未做笔记'
              }。直接前置：${section.prereqs.length ? section.prereqs.join('、') : '无'}`

              return (
                <g
                  key={section.id}
                  className={[
                    'node',
                    `part-${section.part}`,
                    hasNote ? 'has-note' : 'needs-note',
                    isSelected && 'is-selected',
                    isUpstream && 'is-upstream',
                    isDownstream && 'is-downstream',
                    isFaded && 'is-faded',
                  ]
                    .filter(Boolean)
                    .join(' ')}
                  transform={`translate(${point.x} ${point.y})`}
                  role="button"
                  tabIndex={0}
                  aria-label={label}
                  aria-pressed={isSelected}
                  aria-describedby={
                    nodeTooltip?.id === section.id ? 'srednicki-node-tooltip' : undefined
                  }
                  onClick={() =>
                    setSelectedId((current) => (current === section.id ? null : section.id))
                  }
                  onMouseEnter={(event) => showNodeTooltip(event.currentTarget, section.id)}
                  onMouseLeave={() => setNodeTooltip(null)}
                  onFocus={(event) => showNodeTooltip(event.currentTarget, section.id)}
                  onBlur={() => setNodeTooltip(null)}
                  onKeyDown={(event) => {
                    if (event.key === 'Enter' || event.key === ' ') {
                      event.preventDefault()
                      setSelectedId((current) => (current === section.id ? null : section.id))
                    }
                  }}
                >
                  <circle className="note-ring" r={isSelected ? 20 : 17} />
                  <circle className="node-body" r={isSelected ? 16 : 14} />
                  <text>{section.id}</text>
                </g>
              )
            })}
          </svg>

          {nodeTooltip && (
            <div
              id="srednicki-node-tooltip"
              className={`srednicki-tooltip is-${nodeTooltip.placement}`}
              role="tooltip"
              style={{ left: nodeTooltip.left, top: nodeTooltip.top }}
            >
              <span>
                第 {nodeTooltip.id} 节 ·{' '}
                {notesBySection[String(nodeTooltip.id)]?.length ? '已有笔记' : '尚未做笔记'}
              </span>
              <strong>{srednickiSectionById.get(nodeTooltip.id)?.title}</strong>
            </div>
          )}
        </div>
      </section>

      <section className="srednicki-index" aria-labelledby="section-index-heading">
        <div className="srednicki-index-heading">
          <div>
            <p className="srednicki-kicker">Notes index</p>
            <h2 id="section-index-heading">章节笔记索引</h2>
          </div>
          <div className="srednicki-index-controls">
            <label>
              <span className="sr-only">搜索章节</span>
              <input
                type="search"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="搜索序号或标题"
              />
            </label>
            <div className="srednicki-filter" aria-label="按笔记状态筛选">
              {(
                [
                  ['all', '全部'],
                  ['done', '已有笔记'],
                  ['todo', '尚未笔记'],
                ] as const
              ).map(([value, label]) => (
                <button
                  key={value}
                  type="button"
                  className={noteFilter === value ? 'is-active' : ''}
                  aria-pressed={noteFilter === value}
                  onClick={() => setNoteFilter(value)}
                >
                  {label}
                </button>
              ))}
            </div>
          </div>
        </div>

        <p className="srednicki-result-count" aria-live="polite">
          显示 {visibleSections.length} / {srednickiSections.length} 节
        </p>

        <div className="srednicki-section-grid">
          {visibleSections.map((section) => {
            const notes = notesBySection[String(section.id)] ?? []
            const hasNote = notes.length > 0
            return (
              <a
                id={`section-${section.id}`}
                key={section.id}
                className={`srednicki-section-card ${hasNote ? 'is-done' : 'is-todo'}`}
                href={sectionHref(section.id)}
              >
                <span className="srednicki-section-number">§{section.id}</span>
                <span className="srednicki-section-copy">
                  <strong>{section.title}</strong>
                  <small>{hasNote ? `已有笔记 · ${notes[0].title}` : '尚未做笔记'}</small>
                </span>
                <span className="srednicki-card-arrow" aria-hidden="true">
                  →
                </span>
              </a>
            )
          })}
        </div>

        {!visibleSections.length && <p className="srednicki-empty">没有符合条件的章节。</p>}
      </section>

      <footer className="srednicki-source-note">
        <p>
          数据依据：Srednicki, <cite>Quantum Field Theory</cite>（2006 版）目录中作者列出的
          immediate prerequisites。
        </p>
        <p>纵向层级表示最长前置链深度，并非原书页码或篇章顺序。</p>
      </footer>
    </div>
  )
}
