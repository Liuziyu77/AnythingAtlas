<p align="center">
  <img src="assets/logo/logo.png" alt="AnythingAtlas 标志" width="1080">
</p>

<h1 align="center">AnythingAtlas</h1>

<p align="center"><strong>Map the best way into any topic</strong></p>

<p align="center"><strong>规划任何主题的最佳学习路径</strong></p>

<p align="center">
  <a href="https://agentskills.io/"><img src="https://img.shields.io/badge/Agent_Skills-Compatible-0B1F3A?style=flat-square" alt="兼容 Agent Skills"></a>
  <a href="https://learn.chatgpt.com/docs/build-skills"><img src="https://img.shields.io/badge/Codex-Supported-10A37F?style=flat-square" alt="支持 Codex"></a>
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Claude_Code-Supported-D97757?style=flat-square" alt="支持 Claude Code"></a>
  <img src="https://img.shields.io/badge/Output-Markdown_%2B_HTML-167B94?style=flat-square" alt="输出 Markdown 和 HTML">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-075FC8?style=flat-square" alt="Apache 2.0 许可证"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · 简体中文
</p>

## 🧭 AnythingAtlas 是什么？

AnythingAtlas 是一项为“踏入陌生领域的第一步”而生的 Agent skill，你可以将其用于 Claude Code、Codex，以及其他兼容 Agent Skills 的 Agent 框架中。

当你想要学习一个全新领域或者面对一个陌生课题的时候，最难的往往不是找不到资料，而是面对海量资料不知道什么是真正重要的、哪些是有价值学习的、或者应该从哪里开始学习。

无论你想进入量化金融、研究 AI 智能体、理解一个历史事件，还是掌握一项实践技能，AnythingAtlas 都会把散落在书籍、课程、论文、专家、档案、代码仓库与网络噪声中的信息，整理成一张清晰的领域地图：领域最基础的是什么、有哪些资料可以学习，如何使用这些资料，并帮你指定由浅入深的学习计划。

## 🚀 使用方法

**你只需要做：告诉 AnythingAtlas 想学的主题是什么？想花多少时间学习？之后，AnythingAtlas 将主动引导提问，全网为你寻找精心筛选的学习资料，制定定制化的个人学习计划。**

### 🖼️ 案例 Gallery

三个不同领域、三种学习目标、三套视觉主题。点击封面查看完整的自包含 HTML 图谱。

<table>
  <tr>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/anything-atlas-classical-music-from-scratch.html">
        <img src="assets/gallery/music.svg" alt="从零开始听懂古典音乐案例封面" width="100%">
      </a>
      <br>
      <strong>🎼 从零开始听懂古典音乐</strong>
      <br>
      <sub><code>Scholar</code> · 24 周 · 聆听优先</sub>
      <br><br>
      从音乐语言、历史时期和代表作品，逐步练到比较不同演绎。
      <br><br>
      <a href="examples/anything-atlas-classical-music-from-scratch.html"><strong>查看完整图谱 →</strong></a>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/anything-atlas-impressionism-for-museum-visitors.html">
        <img src="assets/gallery/museum.svg" alt="印象派绘画看展案例封面" width="100%">
      </a>
      <br>
      <strong>🖼️ 从“看不懂”到会看印象派</strong>
      <br>
      <sub><code>Archive</code> · 8 周 · 看展导向</sub>
      <br><br>
      用光线、色彩、笔触、题材与构图建立真正可用的观展方法。
      <br><br>
      <a href="examples/anything-atlas-impressionism-for-museum-visitors.html"><strong>查看完整图谱 →</strong></a>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/anything-atlas-portrait-photography-8-week-portfolio.html">
        <img src="assets/gallery/portrait.svg" alt="八周人像摄影作品集案例封面" width="100%">
      </a>
      <br>
      <strong>📷 八周人像摄影作品集</strong>
      <br>
      <sub><code>Workshop</code> · 8 周 · 成片导向</sub>
      <br><br>
      从曝光、对焦和自然光，推进到一组统一的 8–12 张人像作品。
      <br><br>
      <a href="examples/anything-atlas-portrait-photography-8-week-portfolio.html"><strong>查看完整图谱 →</strong></a>
    </td>
  </tr>
</table>

## 🗺️ 工作流程

```text
用户的初步请求：想学习的主题和规划的时间
   ↓
聚焦澄清并确认需求：AnythingAtlas 主动引导与提问，深入了解用户水平与需求
   ↓
紧凑核心指南：回答真正的问题、展示具体选项并给出第一次行动
   ↓
主题分类，以及资源发现、验证、排序与筛选
   ↓
带可点击链接、适合用户节奏的资源路线与详细个性化学习计划
   ↓
按渠道分组的资源出处：官网、书籍、YouTube、B站、代码仓库及其他相关渠道
   ↓
输出：Markdown 文件 + 精美、自包含的 HTML 文件
```

AnythingAtlas 会根据课题类型，切换资料选择、信息渠道与验证重点：

| 课题类型 | 优先资料 | 主要信息渠道 | 核心判断标准 |
| --- | --- | --- | --- |
| 成熟学术领域 | 教材、综述论文、大学课程、专业标准 | 图书馆目录、学术索引、大学课程页面、专业学会 | 经典性、学术共识、体系完整性 |
| 快速发展的技术 | 近期论文、技术说明、源代码、基准测试 | 预印本平台、会议论文集、官方仓库、研究实验室、专家简报 | 时效性、可复现性、维护活跃度 |
| 历史事件 | 一手文献、档案、口述历史、学术专著 | 国家与地方档案馆、图书馆馆藏、博物馆、学术数据库 | 史料出处、时代语境、事实与阐释的区分 |
| 人物或组织 | 访谈、演讲、机构记录、传记、可信报道 | 官方网站、机构档案、访谈合集、新闻数据库 | 第一方记录与外部验证、时间线、利益关系 |
| 行业研究 | 官方统计、监管文件、企业披露、研究报告 | 监管数据库、统计门户、公司申报文件、行业协会、专业出版物 | 数据口径、利益冲突、信息时效性 |
| 实践技能 | 官方文档、操作演示、结构化课程、练习项目 | 官方文档站、课程平台、项目仓库、实践者社区 | 可操作性、难度递进、练习与反馈质量 |
| 社会议题 | 官方数据、系统性研究、政策文件、多方观点 | 公共机构、综述数据库、研究中心、方法透明的社会组织 | 研究方法、样本代表性、观点与证据的区分 |
| 时事事件 | 第一方声明、公开记录、时间线、可信报道 | 政府与机构网站、司法或立法记录、通讯社、实时数据源 | 时间顺序、多源交叉验证、信息更新状态 |

## 📦 输出约定

每次完整运行都会创建：

1. `anything-atlas-<主题标识>.md`——规范、便于携带和编辑的图谱。
2. `anything-atlas-<主题标识>.html`——使用精心设计的独立页面呈现。

两份文件统一采用紧凑的五章顺序：需求简报、核心指南、包含适配路线的
精选资源、详细路线图，以及最后按渠道分组的资源出处。资源路线和路线图
中的指定资源在 Markdown 与 HTML 中都必须可以点击。

## 🎨 HTML 主题

AnythingAtlas 会根据课题自动选择视觉主题，也可以由用户指定。五套主题共用同一份内容与语义结构，均支持移动端、打印和离线打开。

| 主题 | 适合的课题 | 视觉方向 |
| --- | --- | --- |
| `atlas` | 跨领域、综合型或未明确分类的主题 | 清晰的地图式层级，蓝色信息卡片；默认主题 |
| `scholar` | 成熟学科、理论学习、学术综述 | 温暖的编辑排版与纸张质感，适合长文阅读 |
| `archive` | 历史、人物、组织、一手材料研究 | 档案卷宗感、克制的棕褐色与文献线索 |
| `signal` | AI、软件、前沿技术与快速变化的研究 | 深色高对比界面，突出版本、证据与技术信号 |
| `workshop` | 实践技能、项目制学习、动手训练 | 醒目的模块与检查点，强调任务、产出和进度 |

生成的 HTML 不使用图片 Logo，只在页脚以文字标记 `AnythingAtlas`。

## 🚀 快速开始

AnythingAtlas 采用开放的 [Agent Skills](https://agentskills.io/) 结构。同一份 `SKILL.md` 可以在 Codex、Claude Code 以及其他兼容 Agent Skills 的客户端中使用，无需为每个平台重写工作流程。

仓库名是 `AnythingAtlas`；`anything-atlas` 是 `SKILL.md` 中的 skill 标识，也是推荐的安装目录名。

| Agent | 用户级安装目录 | 项目级安装目录 | 显式调用 |
| --- | --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/anything-atlas` | `<项目根目录>/.agents/skills/anything-atlas` | `$anything-atlas` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/anything-atlas` | `<项目根目录>/.claude/skills/anything-atlas` | `/anything-atlas` |
| 其他兼容 Agent Skills 的客户端 | 以客户端文档为准 | 以客户端文档为准 | 以客户端为准 |

安装到 Codex：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Liuziyu77/AnythingAtlas.git ~/.agents/skills/anything-atlas
```

安装到 Claude Code：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Liuziyu77/AnythingAtlas.git ~/.claude/skills/anything-atlas
```

如果已经克隆了 `AnythingAtlas`，也可以将现有仓库复制或软链接到表中的目录。随后使用对应命令调用，也可以直接用自然语言描述需求，让 Agent 根据 skill 的 `description` 自动匹配：

```text
Codex: $anything-atlas
Claude Code: /anything-atlas

我希望充分理解现代 AI 智能体，以便提出一个研究项目。我掌握基础
Python 和大语言模型知识，每周可以学习八小时，持续十二周；我偏好
论文、代码和中文解释。
```

如果缺少会影响结果的重要信息，AnythingAtlas 会先集中提出一组后续问题，再开始研究。

使用仓库内示例直接生成双格式文件：

```bash
python3 scripts/build_atlas.py \
  --input examples/sample-atlas.json \
  --output-dir /tmp/anything-atlas-output \
  --theme workshop
```

可选主题为 `atlas`、`scholar`、`archive`、`signal` 和 `workshop`。命令行的 `--theme` 优先于 JSON 中的 `meta.theme`；两者都未设置时使用 `atlas`。

运行结构化回归测试：

```bash
python3 -m unittest discover -s tests -v
```

## 🗂️ 仓库结构

```text
AnythingAtlas/
├── SKILL.md                         智能体核心工作流程
├── agents/openai.yaml               OpenAI/Codex 专属界面与依赖元数据
├── references/                      按需读取的研究与输出规范
├── scripts/                         Markdown/HTML 渲染与验证
├── assets/
│   ├── gallery/                     README 案例封面
│   ├── logo/logo.png                README 项目 Logo
│   └── html-template/
│       ├── atlas.html               独立图谱语义模板
│       ├── atlas.css                五套主题共用的基础样式
│       └── themes/                  五套视觉主题与打印样式
├── examples/
│   ├── sample-atlas.json            可直接构建的规范示例
│   ├── anything-atlas-*.md          生成的 Markdown 示例
│   └── anything-atlas-*.html        生成的独立 HTML 示例
├── tests/                           结构化测试与定性回归案例
├── Design.md                        双语产品设计
├── README.md                        英文说明
├── README.zh-CN.md                  简体中文说明
└── LICENSE                          Apache-2.0
```

## 📚 文档

- [Skill 指令](SKILL.md)
- [产品设计](Design.md)
- [需求澄清策略](references/clarification-policy.md)
- [具体性与资源适配策略](references/specificity-and-resource-fit.md)
- [主题分类体系](references/topic-taxonomy.md)
- [来源与渠道策略](references/source-and-channel-policies.md)
- [可信度标准](references/credibility-criteria.md)
- [路线图模式](references/roadmap-schema.md)
- [输出模式](references/output-schema.md)
- [HTML 设计规范](references/html-design-guidelines.md)
- [定性回归案例](tests/quality-cases.md)

## 🚧 当前状态

AnythingAtlas 目前是一个早期功能原型。核心 skill 工作流程、主题感知型策略、规范内容模型、双格式渲染器、五套独立 HTML 主题、统一打印样式和内容一致性验证器均已实现。资源研究能力仍取决于运行该 skill 的智能体可以使用哪些工具。

如果您对于 AnythingAtlas 有任何**功能改进**或**体验改善**的建议，欢迎提出 issue 和 PR，我们将在24小时之内进行改善。也欢迎给本项目点一个Star，感谢支持。

## ⚖️ 许可证

本项目使用 [Apache License 2.0](LICENSE)。
