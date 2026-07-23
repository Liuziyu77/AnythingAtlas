<p align="center">
  <img src="assets/logo/logo.png" alt="AnythingAtlas logo" width="1080">
</p>

<h1 align="center">AnythingAtlas</h1>

<p align="center"><strong>Map the best way into any topic</strong></p>

<p align="center"><strong>规划学习任何主题的最佳路径</strong></p>

<p align="center">
  <a href="https://agentskills.io/"><img src="https://img.shields.io/badge/Agent_Skills-Compatible-0B1F3A?style=flat-square" alt="Agent Skills compatible"></a>
  <a href="https://learn.chatgpt.com/docs/build-skills"><img src="https://img.shields.io/badge/Codex-Supported-10A37F?style=flat-square" alt="Codex supported"></a>
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Claude_Code-Supported-D97757?style=flat-square" alt="Claude Code supported"></a>
  <img src="https://img.shields.io/badge/Output-Markdown_%2B_HTML-167B94?style=flat-square" alt="Markdown and HTML output">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-075FC8?style=flat-square" alt="Apache 2.0 license"></a>
</p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

## 🧭 What is AnythingAtlas?

AnythingAtlas is an Agent Skill built for the first step into unfamiliar territory. You can use it with Claude Code, Codex, and other Agent Skills-compatible frameworks.

When you begin learning a new field or confronting an unfamiliar subject, the hardest part is often not finding information. It is working out what truly matters, which resources are worth your time, and where to begin.

Whether you want to enter quantitative finance, research AI agents, understand a historical event, or master a practical skill, AnythingAtlas turns scattered books, courses, papers, experts, archives, repositories, and online noise into a clear map of the field: its foundations, the resources worth learning from, how to use them, and a step-by-step plan that takes you from beginner to advanced.

**All you need to do is tell AnythingAtlas what you want to learn and how much time you have. It will guide you through a focused set of questions, search broadly for carefully selected learning resources, and build a personalized study plan around your needs.**

## ✨ Features

- **Proactive clarification:** AnythingAtlas asks about the details that shape what and how you want to learn, including scope, goals, background, time, language, content format, and desired depth.
- **Topic-aware discovery:** It distinguishes between knowledge domains, academic questions, new skills, events, and other topic types, then applies a suitable discovery strategy and chooses sources accordingly.
- **Broad research:** It searches the information channels that fit the topic, including academic indexes, archives, official documentation, code repositories, professional institutions, expert accounts, and practitioner communities.
- **Information verification:** It checks the authority and reliability of resources and information.
- **Learning design:** It builds a roadmap with explicit resource assignments, tasks, time estimates, milestones, stage deliverables, and completion criteria.
- **Easy reading:** It produces synchronized Markdown alongside responsive, accessible, print-friendly HTML.

## 🗺️ How it works

```text
Initial request: the topic and the time available
   ↓
Focused clarification and confirmed brief: guided questions to understand the learner and their needs
   ↓
Topic classification and knowledge map: a discovery strategy suited to the field, skill, and timeframe
   ↓
Source and information-channel plan: define how information quality will be verified
   ↓
Discovery, verification, ranking, and curation
   ↓
Detailed personalized roadmap: carefully selected resources and a tailored study plan
   ↓
Output: Markdown file + polished, self-contained HTML file
```

AnythingAtlas changes its resource selection, information channels, and verification priorities to match the type of topic:

| Topic type | Priority resources | Main information channels | Core evaluation criteria |
| --- | --- | --- | --- |
| Mature academic field | Textbooks, review papers, university courses, professional standards | Library catalogs, academic indexes, university course pages, professional societies | Canonical status, academic consensus, systematic coverage |
| Fast-moving technology | Recent papers, technical reports, source code, benchmarks | Preprint servers, conference proceedings, official repositories, research labs, expert briefings | Recency, reproducibility, maintenance activity |
| Historical event | Primary documents, archives, oral histories, scholarly monographs | National and local archives, library collections, museums, academic databases | Provenance, historical context, separation of fact from interpretation |
| Person or organization | Interviews, speeches, institutional records, biographies, credible reporting | Official websites, institutional archives, interview collections, news databases | First-party records and external verification, chronology, conflicts of interest |
| Industry research | Official statistics, regulatory filings, corporate disclosures, research reports | Regulatory databases, statistics portals, company filings, industry associations, professional publications | Data definitions, conflicts of interest, timeliness |
| Practical skill | Official documentation, demonstrations, structured courses, practice projects | Official documentation sites, course platforms, project repositories, practitioner communities | Practicality, progression of difficulty, quality of practice and feedback |
| Social issue | Official data, systematic research, policy documents, multiple perspectives | Public institutions, review databases, research centers, methodologically transparent civil-society organizations | Research methods, sample representativeness, separation of evidence from opinion |
| Current event | First-party statements, public records, timelines, credible reporting | Government and institutional websites, judicial or legislative records, news agencies, real-time data sources | Chronology, cross-source verification, update status |

## 📦 Output contract

Every completed run creates:

1. `anything-atlas-<topic-slug>.md` — a structured, portable, editable atlas.
2. `anything-atlas-<topic-slug>.html` — a thoughtfully designed standalone presentation.

## 🚀 Quick start

AnythingAtlas follows the open [Agent Skills](https://agentskills.io/) format. The same `SKILL.md` works with Codex, Claude Code, and other Agent Skills-compatible clients; the core workflow does not need to be rewritten for each platform.

The repository is named `AnythingAtlas`; `anything-atlas` is the skill identifier in `SKILL.md` and the recommended installation-directory name.

| Agent | User-level location | Project-level location | Explicit invocation |
| --- | --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/anything-atlas` | `<project-root>/.agents/skills/anything-atlas` | `$anything-atlas` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/anything-atlas` | `<project-root>/.claude/skills/anything-atlas` | `/anything-atlas` |
| Other Agent Skills-compatible clients | Follow the client documentation | Follow the client documentation | Client-specific |

Install for Codex:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Liuziyu77/AnythingAtlas.git ~/.agents/skills/anything-atlas
```

Install for Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Liuziyu77/AnythingAtlas.git ~/.claude/skills/anything-atlas
```

If you have already cloned `AnythingAtlas`, copy or symlink that checkout into the relevant directory instead. Then invoke it explicitly, or describe your goal naturally and let the agent match the skill from its `description`:

```text
Codex: $anything-atlas
Claude Code: /anything-atlas

I want to understand modern AI agents well enough to propose a research
project. I know basic Python and language models, can study eight hours
per week for twelve weeks, and prefer papers, code, and explanations in
Chinese.
```

If important information is missing, AnythingAtlas asks a compact set of follow-up questions before researching.

## 🗂️ Repository structure

```text
AnythingAtlas/
├── SKILL.md                         Core agent workflow
├── agents/openai.yaml               OpenAI/Codex UI and dependency metadata
├── references/                      On-demand research and output policies
├── scripts/                         Markdown/HTML rendering and validation
├── assets/
│   ├── logo/logo.png                Project logo
│   └── html-template/               Standalone atlas template and styles
├── examples/
│   ├── sample-atlas.json            Buildable canonical example
│   ├── anything-atlas-*.md          Generated Markdown example
│   └── anything-atlas-*.html        Generated standalone HTML example
├── Design.md                        Bilingual product design
├── README.md                        English documentation
├── README.zh-CN.md                  Simplified Chinese documentation
└── LICENSE                          Apache-2.0
```

## 🎯 Design principles

- Clarify before research.
- Trust before volume.
- Map before path.
- Plan channels before discovery.
- Explain every recommendation.
- Separate evidence from commentary.
- Adapt to the topic and the user.
- Preserve uncertainty.
- Make the roadmap executable.
- Use one content model for both deliverables.

## 📚 Documentation

- [Skill instructions](SKILL.md)
- [Product design](Design.md)
- [Clarification policy](references/clarification-policy.md)
- [Topic taxonomy](references/topic-taxonomy.md)
- [Source and channel policies](references/source-and-channel-policies.md)
- [Credibility criteria](references/credibility-criteria.md)
- [Roadmap schema](references/roadmap-schema.md)
- [Output schema](references/output-schema.md)
- [HTML design guidelines](references/html-design-guidelines.md)

## 🚧 Status

AnythingAtlas is an early functional prototype. The core skill workflow, topic-aware policies, canonical content model, dual renderers, standalone HTML design, and parity validator are implemented. Resource research still depends on the tools available to the agent running the skill.

If you have ideas for **feature improvements** or a better **user experience**, please open an issue or PR. We will work on improvements within 24 hours. If you find AnythingAtlas useful, please consider giving the project a Star—thank you for your support.

## ⚖️ License

Licensed under the [Apache License 2.0](LICENSE).
