# 私密地图维护

## 架构与公开边界

本仓库当前使用 Astro 4.16.19、React、pnpm 和 Pagefind，博客仍由 Astro 静态生成。仓库的定时工作流调用 Vercel Deploy Hook；实际 HTTP 检查也确认线上托管于 Vercel。没有改动博客的布局、内容集合、导航或 Astro 路由。

`pnpm build` 在原有构建、类型检查和 Pagefind 后，通过 Vercel Build Output API 打包：

- `dist/` 和 `.vercel/output/static/`：原有公开博客；没有地图 HTML、数据或资源。
- `.vercel/output/functions/japan.func/`：独立 Node.js 22 函数和通用 Leaflet 程序，无真实行程和运行时 Secret。
- `/japan` 及子路径先进入函数，再查会话、读取数据或资源。不会先命中静态文件。
- Pagefind 只扫描 `dist/`。地图没有 Astro 页面或 content entry，不进入首页、导航、RSS、sitemap、相关推荐或搜索。地图 HTML 还设置 `data-pagefind-ignore`、`noindex,noarchive,nosnippet`。
- `vercel.json` 的 `framework: null` 用于采用现有 Astro 静态输出加显式函数产物；没有将博客改为 SSR。不要在 Vercel 项目中另行指定覆盖此构建的 Output Directory。

官方实现依据：[Vercel Build Output API](https://vercel.com/docs/build-output-api)、[运行时与函数目录](https://vercel.com/docs/build-output-api/primitives)、[路由顺序与 host 条件](https://vercel.com/docs/build-output-api/configuration)。

## 地图、来源与许可

使用锁定版本的 Leaflet 1.9.4（BSD-2-Clause），JS/CSS 随构建打包，不使用 CDN 脚本。完整 Leaflet 许可证保存在函数的 `assets/Leaflet-LICENSE.txt`。地图默认使用国土地理院标准地图：

```text
https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png
```

标准地图的具体覆盖与最高精度以[官方瓦片目录](https://maps.gsi.go.jp/development/ichiran.html#std)为准；实现限制为 z2–18，不请求超过服务范围的层级。日本外部区域及低缩放层的原始资料与署名要求也见该目录。地图保留“出典：国土地理院”和官方链接，遵守[国土地理院内容利用条款](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)。

仅请求当前视窗瓦片，`keepBuffer: 0`，没有预抓取、离线 PWA、公共行程瓦片或 Service Worker。网络失败时明确标记详细底图不可用，可重试或切换“仅点线示意”；日程继续可读。没有自托管 PMTiles，Range/206 不适用。

已核对官方 [Q1-12](https://www.gsi.go.jp/LAW/2930-qa.html)：实时读取地理院服务器上的瓦片，采用本实现的署名与目录链接方式即可使用，无需另行提交利用申请。此说明针对当前在线加载方式。

坐标存储为 WGS84：原 `routes.coords` 保持 `[纬度, 经度]`；GeoJSON/KML 导出转换为 `[经度, 纬度]`。原 Bokeh 派生字段从运行时数据移除，并在私有原件中完整保留。地点是参考点，连线是走廊示意；摄影方向独立成层。没有依据线路长度估算公交时间，也没有重新查询机票。

## 私有数据与更新

以下目录被 Git、Prettier 和 Vercel CLI 源码上传忽略：

```text
.private/japan/import/       原始 ZIP 解包、HTML、PDF、CSV、KML、来源程序及许可证
.private/japan/trip.json     校验后的运行时数据
.private/japan/ui.json       从原页面迁移的地区范围及成组方案展示覆盖
.private/japan/secrets.env   本机 Secret 文件，权限 0600
.private/japan/qa/           导入校验、截图、测试日志与网络证据
.private/japan/backups/      维护时保存的旧基准版本
```

实际生产基准存在私有 Redis 的 `<prefix>:baseline`；新增地点在 `<prefix>:collaboration`，修订在 `<prefix>:history`。这些值不参与网站构建，也不进入客户端 bundle。不要放入 `public/`、Git LFS、GitHub 附件、公开 CI artifact 或公共对象存储。原 ZIP 留在当前目录并被忽略；建议维护时继续在私有目录保存原件。

更新现有私有 JSON 后运行以下命令，参数使用你保存的真实私有文件路径：

```sh
node scripts/japan/import.mjs PRIVATE_TRIP_JSON PRIVATE_UI_JSON
node --env-file=.private/japan/secrets.env scripts/japan/publish-data.mjs
```

导入脚本不执行原始 `build_data.py`；保留所有非投影字段、ID、日期、精度说明、可选状态和来源索引，校验原投影与 WGS84 的一致性。地区范围和两个完整方案的标题、住宿、focus 与时间说明在私有 UI 文件中维护；基准日期不自动前移。导入报告记录输入／输出 SHA-256 和展示覆盖。生产更新会保存旧基准，并以原子比较更新避免覆盖另一位维护者的修改；不会清空协作记录。

已规范化的行程修订可直接发布：`node --env-file=.private/japan/secrets.env scripts/japan/publish-data.mjs .private/japan/updates/REVISED_TRIP.json`。先保存当前基准、协作及历史的私有快照，核对日期、住宿晚数，以及每个方案的 focus 点在对应日期可见。发布后回读核对，将同一版本同步到本机 `trip.json` 和 `ui.json`，再验证正式页面；无需重新部署博客。保留原导入报告及 `backups/` 中对应摘要的原始基准，测试会分别检查原始导入保全和当前行程有效性。修订数据、差异记录及截图均留在 `.private/`，不提交 Git。

## Secret 与会话

必需的运行时变量见根目录 `.env.example`，仅配置在 Vercel **Production**，不配置到 Preview：

| 变量                     | 用途                                     |
| ------------------------ | ---------------------------------------- |
| `JAPAN_PASSWORD_HASH`    | 带随机盐的 scrypt 摘要                   |
| `JAPAN_SESSION_KEY`      | 独立 256-bit 随机会话签名密钥，base64url |
| `JAPAN_REDIS_REST_URL`   | 已有私有 Redis 的 HTTPS REST 入口        |
| `JAPAN_REDIS_REST_TOKEN` | 该 Redis 的读写服务端凭证                |
| `JAPAN_REDIS_PREFIX`     | 此功能专用键前缀                         |

初始化：`pnpm japan:init`，两次隐藏输入共享密码。也支持从安全输入管道读取：`node scripts/japan/init-secrets.mjs --stdin`。不要把密码写入 shell 命令、命令参数或历史。脚本只写私有文件，不输出变量值；禁止将该文件粘贴到公共文档或构建日志。本次本机已初始化指定共享密码对应的摘要和独立会话密钥，并经用户授权保存到 Vercel Production 的 Secret 类型变量，未保存明文密码。

使用 Node 原生 scrypt，N=131072、r=8、p=1、16-byte 盐、32-byte 输出，符合 [OWASP 的 scrypt 最低建议](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)。使用 JOSE HS256 签名并验证 issuer、audience、签名与过期时间。Redis 内会话存储只使用随机会话 ID 的摘要。

Cookie 名 `__Secure-japan`，host-only、Path `/japan`、Secure、HttpOnly、SameSite=Strict，12 小时有效。登录前使用短时签名 CSRF Cookie 与表单令牌；退出与写入还要求当前会话 CSRF。所有写入检查精确 Origin。`Referrer-Policy: same-origin` 让原生表单可校验来源，并且不向第三方发送本站 Referer。

每个可信 Vercel 客户端 IP 15 分钟最多 10 次登录尝试，全局 15 分钟最多 120 次；由 Redis 原子 INCR/EXPIRE 实际执行。IP 只作为带密钥摘要保存。协作写入每会话每小时最多 60 次。存储不可达、Secret 缺失或未初始化时拒绝访问，绝不退回进程内计数或前端鉴权。

退出删除 Redis 会话，所以复制的旧 Cookie、旧标签页及后续接口请求失效。页面通过 BroadcastChannel、聚焦检查、30 秒会话复核、pagehide 清空和 pageshow 重载处理多标签与浏览器返回缓存；恢复后台标签前先校验会话。网络断开时无法保证服务端已收到退出，会明确提示。

换密：使用 `JAPAN_SECRET_OUTPUT=.private/japan/rotated.env pnpm japan:init` 生成新文件，将新摘要和新会话密钥一并更新到 Vercel Production 并部署。摘要变化会使所有旧令牌立即不匹配当前配置，旧 Redis 会话在 TTL 后删除；若更换 session key，旧签名也失效。不要只改本机文件就认为生产已换密。[OWASP 会话原则](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)。

## 多人协作

所有登录者可通过“共同补充目的地”添加候选地点（中日文名称、经纬度／点选、日期、地区、所属方案、到达方式、备注和来源）。新增地点默认可选、未核实。所有原始地点、线路和日期保持只读。

新增地点保存后返回独立编辑凭证，仅存当前标签页的 `sessionStorage`，退出时清除。服务端只保存该凭证摘要。可编辑自己持有凭证的新增地点，不把昵称当作真实身份或授权。丢失凭证后由维护者处理；重新用共享密码登录不会自动获得其他人的编辑权限。需要编辑自己的地点时，在搜索结果中打开详情即可。

原子 compare-and-set 同时更新内容与历史，冲突返回 409 并要求刷新；不静默覆盖。每次添加、修改和恢复保留时间、昵称、旧／新内容。历史只由登录后的 `/japan/history` 返回，移除内部凭证摘要。维护者恢复某条新增地点的历史版本：

```sh
node --env-file=.private/japan/secrets.env scripts/japan/restore-addition.mjs ADDED_ID HISTORICAL_REVISION
```

恢复作为新修订保存，不覆盖其他人新增的目的地。共享密码不提供可审计的个人实名身份。

## 部署与裸域名

2026-09-16 已完成正式页面 `https://phymani.me/japan` 的上线验收。验收部署为 Vercel `website` 项目的 `2Lnu9WN1FEGzuVhJSiYzpFvPsmzr`（代码提交 `30c9541`，状态 Ready）。实际资源包含一个 `/japan` Node.js 22 函数（IAD1）和原有静态博客。修复了 CI 中 `.pnpm-store` 导致隐私扫描文件列表超出缓冲区的问题：忽略包缓存并流式读取 Git 文件列表，扫描失败不打印子进程输出。

经用户确认，已将 `phymani.me` 连接到同一 Production 项目，没有修改 DNS。实测首页、文章、RSS、sitemap 与 `/japanese` 仍 307 到原 www 路径；`/japan/` 为 308 到 `/japan`，www 地图入口为 308 到正式裸域名。正式入口未登录返回最小密码页（200），数据接口返回 401；登录后地图和数据均为 200，所有这些响应均带 `private, no-store`。原始项目托管域名的地图、数据和导出均返回 404；具体部署域名另有 Vercel 登录保护。

系统环境变量开关已开启。已获用户授权安装免费 Upstash 数据库 `website-japan-private`，地域 IAD1，每月 500,000 条命令，未启用额外读取地域或自动驱逐。五个应用变量均仅配置到 Production，其中摘要、会话密钥、REST URL 和 Token 使用 Secret 类型。启用这些变量的部署 `2Lnu9WN1FEGzuVhJSiYzpFvPsmzr` 已 Ready。

Upstash 集成另行管理五个 `JAPAN_REDIS_KV_*` / `JAPAN_REDIS_REDIS_URL` 变量，也均仅限 Production。应用使用上表的明确变量名；以后轮换数据库 Token 时，同步更新本机私有配置与 Production 的 `JAPAN_REDIS_REST_TOKEN`，然后重新部署。

经用户确认，完整私有行程已由本机直接上传到此数据库，未经过公共 CI。生产数据与私有基准逐字段一致。真实 Upstash HTTPS/REST、Lua 原子计数、并发冲突和历史记录测试通过；两个独立登录客户端完成新增、读取与修改测试。临时新增地点已清理，原始行程和其他协作记录保留。

平台初始化已完成，无需额外手动配置。后续维护：

1. 数据库和五个 Production 变量已配置。维持免费方案和当前环境范围，不把私有变量同步到 Preview 或 Development。超出免费额度或服务不可达时会拒绝访问，不自动升级付费方案。
2. 更新行程时从本机执行上述导入、上传命令，不要经公共 CI 转存行程。数据由运行时读取，单独更新数据不需要重新构建网站。
3. 代码或 Secret 变更后在现有 Vercel 项目重新部署。仓库 `vercel.json` 的 `framework: null` 和 `buildCommand: pnpm build` 覆盖控制台默认值；控制台目前仍显示 Astro，没有 Output Directory 覆盖。已经实际验证 `.vercel/output` 作为静态博客和函数产物成功部署，不需要重复修改控制台 Framework Preset。
4. 域名接入已完成；后续保持当前绑定。代码继续将其他裸域名路径以原有 307 跳转到 `www`，只让 `/japan` 进入函数。回滚到不含这些规则的旧版本时，需同时恢复原整域跳转。

`/japan/` 308 到 `/japan`；`www` 的地图 GET/HEAD 308 到正式入口，POST 拒绝。预览／原始 `*.vercel.app` 及其他 host 拒绝地图，即便误继承 Secret。畸形、编码、重复斜杠路径不能返回数据；未知内部路径需要先鉴权，仍无对应文件。`/japanese` 不属于本功能。额外的 13 项生产路径探测覆盖编码、重复斜杠、静态别名、旧 HTML 与私有文件地址，未发现鉴权绕过。

私密响应设置 `Cache-Control: private, no-store`、`CDN-Cache-Control: no-store`、`Vercel-CDN-Cache-Control: no-store`。不要在 Vercel/CDN 外层设置覆盖这些响应的公共缓存。没有 Cache API 或预渲染地图产物。

通常的本机部署命令（需先通过已有项目登录／关联，不能新建另一个公开站点）：

```sh
pnpm install --frozen-lockfile
pnpm japan:lint
pnpm build
pnpm japan:test
vercel link
vercel build --prod
vercel deploy --prebuilt --prod
```

也可以使用现有 Git 集成发布通用代码。不要运行 `git add .`；提交前运行产物检查并检查 staged diff。CLI 源码上传由 `.vercelignore` 排除私有目录，`--prebuilt` 仅上传不含真实数据的构建产物。

回滚：在现有项目执行 `vercel rollback PREVIOUS_DEPLOYMENT_URL`，或在 Vercel 控制台选择先前部署。若旧部署不包含裸域名分流规则，同时恢复原来的平台整域跳转；地图将变成不可用，私有 Redis 数据不会变公开。数据回滚使用 `.private/japan/backups/` 中选定版本经 `publish-data.mjs` 重新上传，保留协作记录。

## 测试与验收范围

单元测试用独立合成行程和测试密码。真实行程校验只在本机私有输入存在时运行，公共 CI 自动跳过。

首次测试先运行 `pnpm build`；部署产物测试会核对该次构建的实际路由和静态文件。

```sh
pnpm japan:test
# 真实 Redis 已有本机实例时：
JAPAN_TEST_REDIS_URL=redis://127.0.0.1:6397 pnpm japan:test
# 本次临时 Redis 测试运行时保存在 gitignored testing 目录，未安装到系统：
.private/japan/testing/redis-8.2.1/src/redis-server --bind 127.0.0.1 --port 6397 --appendonly yes --dir .private/japan/testing/redis-data
pnpm japan:e2e
JAPAN_TEST_REAL=1 pnpm japan:e2e --project=desktop real-network
# 私有真实行程预览，仅监听本机；使用独立测试密码：
JAPAN_TEST_REAL=1 node scripts/japan/dev.mjs
```

`pnpm japan:e2e` 使用持久 Redis，UI 测试 mock 瓦片；`real-network` 单独运行真实国土地理院瓦片检查，每个区域只看一个正常街区视窗，截图不进入 Git。Node 22 及以上支持维护命令的 `--env-file`。本机测试浏览器使用已安装的 Chrome；其他环境可运行 `pnpm exec playwright install chromium`。

测试覆盖口令摘要、篡改／过期会话、限速、注销撤销、CSRF、备用域名拒绝、路径边界、坐标转换、数据保全、互斥方案、协作并发、文字转义与桌面／手机布局。`scripts/japan/scan-public.mjs` 检查实际输出、索引与受跟踪文件，发现私密标记即失败，只报告文件数量，不输出内容。原有 `pnpm lint` 会全仓库改写格式，因此新增 `japan:lint` 做本功能限定的只读检查。

**生产验收已完成**：52 项真实 HTTP 检查通过，包括指定密码登录、篡改／过期 Cookie、实际限速、协作权限与冲突、注销撤销，以及已登录访问后全新无 Cookie 客户端仍无法读取同一私密地址。Chrome 在正式域名首次登录即加载 z14 详细底图；八个指定区域均验证了真实 z15 瓦片解码。两个方案的两天切换与跨标签退出清理通过。博客首页、文章、RSS、sitemap 和 Pagefind 的抽查正常，详见 [验收记录](VALIDATION.md)。

生产浏览器验收使用桌面 Chrome；手机布局与触控验收使用本地 Playwright，包括独立的真实瓦片网络测试。生产缓存探测来自当前网络出口，没有声称遍历全球 CDN 节点。真实截图和完整验收证据仅保存在本机私有目录。
