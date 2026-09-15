# Gyoza

Gyoza is a static blog template built with Astro and React.

![astro version](https://img.shields.io/badge/astro-4.6-red)
![node version](https://img.shields.io/badge/node-18.18-green)

Demo Site:

- [gyoza.lxchapu.com](https://gyoza.lxchapu.com)
- [www.lxchapu.com](https://www.lxchapu.com)

Enjoy it!

## 📷 Screenshots

![Preview](https://s2.loli.net/2024/05/06/A9rzC3Uym7RwdQc.webp)

## 🎉 Features

- ✅ 有着规范的 URL 和 OpenGraph 信息，对 SEO 友好
- ✅ 支持站点地图
- ✅ 支持 RSS 订阅
- ✅ 支持夜间模式
- ✅ 特殊日期变灰
- ✅ 简单干净的配色和主题
- ✅ 支持评论系统
- ✅ 支持代码高亮

## 🔧 Tech Stack

- [Astro](https://astro.build/)
- [React](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Framer Motion](https://www.framer.com/motion/)
- [Jotai](https://jotai.org/)

## 📖 Documentation

前往：[Documentation](https://gyoza.lxchapu.com/posts/guide)

### Srednicki 笔记与首页显示

笔记放在 `src/content/posts/`，使用 Markdown 格式。以下 frontmatter 将笔记关联到 Srednicki 第 1 节，并从首页及其分页文章列表中隐藏：

```yaml
---
title: 'Srednicki §1 阅读笔记'
date: 2026-09-09
category: 笔记
series: 'Srednicki QFT'
srednickiSections: [1]
hideFromHome: true
draft: false
---
```

`hideFromHome` 默认为 `false`。设为 `true` 后，文章仍正常发布，可从 Srednicki 地图、分类、标签、搜索及直接链接访问，也仍包含在 RSS 中。它不影响 `draft` 的发布规则。`srednickiSections` 可以填写多个章节编号（1–97）。

## 🚀 Project Structure

```text
├── public/
├── src/
│   ├── components/
│   ├── content/
│   ├── layouts/
│   ├── pages/
│   ├── plugins/
│   ├── store/
│   ├── styles/
│   ├── utils/
│   └── config.json
├── astro.config.mjs
├── README.md
├── package.json
└── tsconfig.json
```

网站配置保存在 `config.json` 文件。

## 🧞 Commands

| Command        | Action                                       |
| :------------- | :------------------------------------------- |
| `pnpm i`       | Installs dependencies                        |
| `pnpm dev`     | Starts local dev server at `localhost:4321`  |
| `pnpm build`   | Build your production site to `./dist/`      |
| `pnpm preview` | Preview your build locally, before deploying |
| `pnpm format`  | Format code using Prettier                   |
