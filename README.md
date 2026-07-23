<p align="center">
  <img src="assets/logo/logo.png" alt="AnythingAtlas logo" width="1080">
</p>

<h1 align="center">AnythingAtlas</h1>

<p align="center"><strong>Map the best way into any topic.</strong></p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

AnythingAtlas is a Codex skill for entering unfamiliar fields with a trustworthy knowledge map, a carefully verified resource set, and a detailed learning or exploration roadmap.

It does more than return a reading list. AnythingAtlas first clarifies what the user actually wants, determines which evidence and information channels fit the topic, verifies the resources, and then produces two synchronized deliverables: an editable Markdown atlas and a polished, self-contained HTML atlas.

## What it does

- Proactively clarifies scope, goals, background, time, language, formats, depth, and access constraints.
- Classifies the topic before choosing sources.
- Adapts its discovery policy to academic fields, fast-moving technology, history, people, industries, practical skills, social issues, and current events.
- Searches topic-appropriate channels such as academic indexes, archives, official documentation, repositories, institutions, expert accounts, and professional communities.
- Verifies titles, creators, URLs, dates, access conditions, relevance, authority, and limitations.
- Curates a small complementary core instead of a long undifferentiated list.
- Builds a staged roadmap with exact assignments, tasks, time estimates, milestones, deliverables, and completion criteria.
- Generates synchronized Markdown and responsive, accessible, print-friendly HTML.

## How it works

```text
Initial request
   ↓
Focused clarification and confirmed brief
   ↓
Topic classification and knowledge map
   ↓
Source and information-channel plan
   ↓
Discovery, verification, ranking, and curation
   ↓
Detailed personalized roadmap
   ↓
Markdown file + polished self-contained HTML file
```

Different topics use different evidence policies. A history atlas should prioritize primary records and archives; a fast-moving AI atlas should emphasize current papers, repositories, benchmarks, and active researchers; a practical-skill atlas should emphasize official documentation, demonstrations, projects, and feedback.

## Output contract

Every completed run creates:

1. `anything-atlas-<topic-slug>.md` — the canonical, portable, editable atlas.
2. `anything-atlas-<topic-slug>.html` — the same content presented as a designed standalone document.

Both files contain:

- the confirmed user brief and assumptions;
- a topic brief and dependency-aware knowledge map;
- the source and channel plan;
- a recommended starting point;
- verified resource cards with rationale, focus, level, time, and limitations;
- a detailed staged roadmap;
- source notes, disagreements, and caveats;
- one immediate next action.

The HTML file embeds its CSS and logo, requires no build step or network connection, and includes responsive and print layouts.

## Quick start

Place or symlink this repository at:

```text
$CODEX_HOME/skills/anything-atlas
```

When `CODEX_HOME` is not set, use:

```text
~/.codex/skills/anything-atlas
```

Then invoke the skill with a topic:

```text
$anything-atlas

I want to understand modern AI agents well enough to propose a research
project. I know basic Python and language models, can study eight hours
per week for twelve weeks, and prefer papers, code, and explanations in
Chinese.
```

If important information is missing, AnythingAtlas asks a compact set of follow-up questions before researching.

## Build the included example

The renderer uses one JSON content model to create both deliverables:

```bash
python3 scripts/build_atlas.py \
  --input examples/sample-atlas.json \
  --output-dir /tmp/anything-atlas-output
```

Validate an existing pair:

```bash
python3 scripts/validate_deliverables.py \
  --input examples/sample-atlas.json \
  --markdown /tmp/anything-atlas-output/anything-atlas-python-foundations.md \
  --html /tmp/anything-atlas-output/anything-atlas-python-foundations.html
```

The scripts use only the Python standard library.

## Repository structure

```text
anything-atlas/
├── SKILL.md                         Core agent workflow
├── agents/openai.yaml               Codex UI metadata
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

## Design principles

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

## Documentation

- [Skill instructions](SKILL.md)
- [Product design](Design.md)
- [Clarification policy](references/clarification-policy.md)
- [Topic taxonomy](references/topic-taxonomy.md)
- [Source and channel policies](references/source-and-channel-policies.md)
- [Credibility criteria](references/credibility-criteria.md)
- [Roadmap schema](references/roadmap-schema.md)
- [Output schema](references/output-schema.md)
- [HTML design guidelines](references/html-design-guidelines.md)

## Status

AnythingAtlas is an early functional prototype. The core skill workflow, topic-aware policies, canonical content model, dual renderers, standalone HTML design, and parity validator are implemented. Resource research still depends on the tools available to the agent running the skill.

## License

Licensed under the [Apache License 2.0](LICENSE).
