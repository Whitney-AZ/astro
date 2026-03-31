import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const configPath = path.join(__dirname, '../src/config.json')

async function archive() {
  const config = JSON.parse(fs.readFileSync(configPath, 'utf8'))
  const username = config.bangumi?.username || 'whitney'

  console.log(`Fetching completed anime for user: ${username}...`)

  // type=2 is completed (看过), limit=100 ensures we don't miss any recent ones
  const res = await fetch(
    `https://api.bgm.tv/v0/users/${username}/collections?subject_type=2&type=2&limit=100`,
    {
      headers: { 'User-Agent': 'PhyMAnime-Blog-Archiver/1.0' },
    },
  )

  if (!res.ok) {
    console.error('Failed to fetch from Bangumi API:', res.statusText)
    return
  }

  const data = await res.json()
  const collections = data.data || []

  if (collections.length === 0) {
    console.log('No completed anime found.')
    return
  }

  // Generate markdown content
  const date = new Date()
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const season = month >= 10 ? '秋' : month >= 7 ? '夏' : month >= 4 ? '春' : '冬'

  const slug = `bangumi-archive-${year}-${season === '秋' ? 'autumn' : season === '夏' ? 'summer' : season === '春' ? 'spring' : 'winter'}`
  const filename = `${slug}.md`

  let md = `---
title: ${year}年${season}季 补番与追番总结
date: ${date.toISOString().split('T')[0]}
summary: 这个季度的追番记录存档。
category: 追番
tags: [追番, 归档]
---

这是基于 Bangumi.tv 数据自动生成的季度追番总结报告。共包含 ${collections.length} 部最近看过的番剧记录：

`

  collections.forEach((item) => {
    const subject = item.subject
    const title = subject.name_cn || subject.name
    const cover = subject.images?.large || subject.images?.common || ''
    const myScore = item.rate || '无'
    const epStatus = item.ep_status

    md += `### [${title}](https://bgm.tv/subject/${subject.id})
<img src="${cover}" alt="${title}" width="150" referrerpolicy="no-referrer" style="border-radius: 8px; float: right; margin-left: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

- **我的评分**：${myScore} / 10
- **总观看集数**：${epStatus}
- **BGM 评分**：${subject.score || '暂无'}

${item.comment ? `> ${item.comment}` : '> 暂无简评'}

<div style="clear: both; margin-bottom: 2rem;"></div>

---

`
  })

  // Add the script to package.json if the user wants to run it.
  const outputPath = path.join(__dirname, '../src/content/posts', filename)
  fs.writeFileSync(outputPath, md, 'utf8')
  console.log(`Successfully generated archive at: ${outputPath}`)
}

archive().catch(console.error)
