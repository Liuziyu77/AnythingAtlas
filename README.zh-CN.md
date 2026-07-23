<p align="center">
  <img src="assets/logo/logo.png" alt="AnythingAtlas 标志" width="1080">
</p>

<h1 align="center">AnythingAtlas</h1>

<p align="center"><strong>绘制进入任何主题的最佳路径。</strong></p>

<p align="center">
  <a href="README.md">English</a> · 简体中文
</p>

AnythingAtlas 是一项帮助用户进入陌生领域的 Codex skill。它会构建可信的知识图谱、筛选并验证资源，再给出一份详细的学习或探索路线图。

它不只是返回一份书单。AnythingAtlas 会先澄清用户真正想要什么，判断该课题适合哪些证据与信息渠道，验证候选资源，最终生成两份内容同步的交付物：一份便于编辑的 Markdown 图谱和一份精美、自包含的 HTML 图谱。

## 功能

- 主动澄清范围、目标、背景、时间、语言、内容形式、期望深度与访问限制。
- 先对课题进行分类，再选择资料来源。
- 针对学术领域、快速发展的技术、历史、人物、行业、实践技能、社会议题与时事采用不同的发现策略。
- 搜索适合课题的信息渠道，例如学术索引、档案、官方文档、代码仓库、专业机构、专家账号和实践者社区。
- 验证标题、作者、链接、日期、访问条件、相关性、权威性与局限。
- 筛选一组规模较小但彼此互补的核心资源，而不是生成冗长且未经区分的清单。
- 构建包含明确资源安排、任务、时间估算、里程碑、阶段产出与完成标准的路线图。
- 同时生成内容同步的 Markdown，以及响应式、无障碍、适合打印的 HTML。

## 工作流程

```text
用户的初步请求
   ↓
聚焦澄清并确认需求简报
   ↓
主题分类与知识图谱
   ↓
来源与信息渠道方案
   ↓
资源发现、验证、排序与筛选
   ↓
详细的个性化路线图
   ↓
Markdown 文件 + 精美、自包含的 HTML 文件
```

不同课题采用不同的证据策略。历史主题应优先考虑一手记录与档案；快速发展的 AI 主题应重视近期论文、代码仓库、基准测试与活跃研究者；实践技能则应重视官方文档、演示、项目与反馈。

## 输出约定

每次完整运行都会创建：

1. `anything-atlas-<主题标识>.md`——规范、便于携带和编辑的图谱。
2. `anything-atlas-<主题标识>.html`——使用精心设计的独立页面呈现相同内容。

两份文件都包含：

- 已确认的用户需求简报与假设；
- 主题简介与包含依赖关系的知识图谱；
- 来源与渠道方案；
- 推荐起点；
- 包含推荐理由、重点、级别、时间与局限的已验证资源卡片；
- 详细的分阶段路线图；
- 来源说明、分歧与注意事项；
- 一项可以立即执行的下一步行动。

HTML 文件会内嵌 CSS 与 logo，无需构建步骤或网络连接，并提供响应式与打印布局。

## 快速开始

将本仓库放置或链接到：

```text
$CODEX_HOME/skills/anything-atlas
```

如果没有设置 `CODEX_HOME`，请使用：

```text
~/.codex/skills/anything-atlas
```

然后通过一个主题调用该 skill：

```text
$anything-atlas

我希望充分理解现代 AI 智能体，以便提出一个研究项目。我掌握基础
Python 和大语言模型知识，每周可以学习八小时，持续十二周；我偏好
论文、代码和中文解释。
```

如果缺少会影响结果的重要信息，AnythingAtlas 会先集中提出一组后续问题，再开始研究。

## 构建仓库内的示例

渲染器使用同一份 JSON 内容模型生成两种交付文件：

```bash
python3 scripts/build_atlas.py \
  --input examples/sample-atlas.json \
  --output-dir /tmp/anything-atlas-output
```

验证一组已有文件：

```bash
python3 scripts/validate_deliverables.py \
  --input examples/sample-atlas.json \
  --markdown /tmp/anything-atlas-output/anything-atlas-python-foundations.md \
  --html /tmp/anything-atlas-output/anything-atlas-python-foundations.html
```

这些脚本仅使用 Python 标准库。

## 仓库结构

```text
anything-atlas/
├── SKILL.md                         智能体核心工作流程
├── agents/openai.yaml               Codex 界面元数据
├── references/                      按需读取的研究与输出规范
├── scripts/                         Markdown/HTML 渲染与验证
├── assets/
│   ├── logo/logo.png                项目 logo
│   └── html-template/               独立图谱模板与样式
├── examples/
│   ├── sample-atlas.json            可直接构建的规范示例
│   ├── anything-atlas-*.md          生成的 Markdown 示例
│   └── anything-atlas-*.html        生成的独立 HTML 示例
├── Design.md                        双语产品设计
├── README.md                        英文说明
├── README.zh-CN.md                  简体中文说明
└── LICENSE                          Apache-2.0
```

## 设计原则

- 先澄清，再研究。
- 可信优先于数量。
- 先有图谱，再定路径。
- 先规划渠道，再发现资源。
- 解释每一项推荐。
- 区分证据与评论。
- 适应课题与用户。
- 保留不确定性。
- 让路线图可以直接执行。
- 两份交付文件共用一份内容模型。

## 文档

- [Skill 指令](SKILL.md)
- [产品设计](Design.md)
- [需求澄清策略](references/clarification-policy.md)
- [主题分类体系](references/topic-taxonomy.md)
- [来源与渠道策略](references/source-and-channel-policies.md)
- [可信度标准](references/credibility-criteria.md)
- [路线图模式](references/roadmap-schema.md)
- [输出模式](references/output-schema.md)
- [HTML 设计规范](references/html-design-guidelines.md)

## 当前状态

AnythingAtlas 目前是一个早期功能原型。核心 skill 工作流程、主题感知型策略、规范内容模型、双格式渲染器、独立 HTML 设计和内容一致性验证器均已实现。资源研究能力仍取决于运行该 skill 的智能体可以使用哪些工具。

## 许可证

本项目使用 [Apache License 2.0](LICENSE)。
