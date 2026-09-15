# Srednicki 网站文章补全：完成

已补入第2–97节，共96篇；连同原有第1节，网站章节地图为97/97。96篇均完成对中译PDF的内容、公式及语言复读，记录及当前文章哈希全部有效。

## 内容与访问

- 正文位于 src/content/posts/Srednicki-02.md 至 Srednicki-97.md。
- 逐节补入必要的详细推导、实际习题内容及跨节依赖；数学适用条件、历史示例数据和未进行的高阶计算保留明确范围。
- 元数据为 draft: false、hideFromHome: true。最终产物确认新增文章不出现在首页及分页，在章节地图和RSS中均可访问。
- 原第1节、chapters目录及中译PDF未编辑。96份输入章节与原清单哈希相同；PDF SHA-256为91eead3d237b8e750dc8e0b3b778d39809a087a9336c4eac3b930a98d434425b。
- 共95个独立SVG，包含第9节补图及第97节质子衰变双图。图源与全部SVG哈希核对通过；原PDF不放入public。

## 最终检查

- pnpm build：退出0。构建日志为 build-final.log。
- python3 scripts/srednicki/audit.py：退出0，97页、27,176处渲染数学、96篇有效复读哈希，问题列表为空。
- 审计覆盖数学错误及未定义命令、重复锚点、本地链接、图像资产、章节映射、陈旧HTML和来源变动。
- git diff --check通过。acceptance.json记录地图、两页首页过滤、RSS、元数据及图像哈希检查。
- AI式模板语言与防御性写法已逐篇处理并作全书扫描；具体依据、保留的物理条件及现有文章对照见 STYLE_REVIEW.md。
- 桌面及390px代表页已经实际截图查看，包括长矩阵、积分、图组及表格。各节记录注明实际抽查范围；没有声称逐屏检查所有正文。

## 可追溯记录

- source-manifest.json：输入章节、PDF页码、补充来源及最终文章哈希。末节页码已校正为407–412。
- reviews/02.md 至 reviews/97.md：96份逐篇内容与语言复读记录。
- build-audit.json、acceptance.json：最终机器检查结果。
- figures.json、figure-render.json：95幅SVG的来源与结果。
- scripts/srednicki/check\_\*.py及相应JSON：实际独立计算；最后三节分别完成593、234、226项检查。
- progress-history.md保留阶段状态。editorial-candidates.json和conversion-references.json为初始转换候选资料，不代表尚有待办事项。

构建中的既有Bangumi请求仍遇到api.bgm.tv DNS失败并使用回退；不影响Srednicki页面构建。Pagefind成功索引211个页面。工作保留在本地，未提交、推送或部署。

请勿重跑scripts/srednicki/prepare.py，以免覆盖人工复读后的正文。
