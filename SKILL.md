---
name: anything-atlas
description: Research and curate a trustworthy entry into any unfamiliar topic. Use when a user asks for a reading list, learning resources, books, courses, papers, experts or accounts to follow, a knowledge map, a topic research plan, or a personalized curriculum or roadmap. Proactively clarify goals and constraints, classify the topic, select topic-appropriate materials and information channels, verify and rank resources, build a detailed staged roadmap, and always deliver synchronized Markdown and polished self-contained HTML files.
---

# AnythingAtlas

Turn an unfamiliar topic into a verified knowledge atlas and an executable learning or exploration roadmap.

## Non-negotiable requirements

- Clarify the user’s real goal before doing expensive research.
- Adapt the evidence standard, resource types, and discovery channels to the topic.
- Verify that recommended resources exist and that titles, authors, URLs, dates, and access conditions are accurate.
- Prefer the smallest sufficient set of complementary resources over a long undifferentiated list.
- Explain why every resource is included, who it suits, what to focus on, and what its limitations are.
- Make every roadmap stage executable with tasks, time, milestones, deliverables, and completion criteria.
- Produce both a complete Markdown file and a polished, self-contained HTML file.
- Generate both files from the same structured content and validate their parity before delivery.

## Workflow

### 1. Clarify and confirm the brief

Inspect the information already supplied. Do not ask questions whose answers can be safely inferred.

Read [references/clarification-policy.md](references/clarification-policy.md). Ask one compact batch of high-impact questions when missing answers could materially change the atlas. Cover only relevant gaps in:

- scope and boundaries;
- desired outcome;
- current knowledge and prerequisites;
- available time, target date, and intensity;
- preferred language, formats, and practice modes;
- depth, budget, geography, and access;
- sources or viewpoints to include or avoid.

Summarize the interpreted brief and consequential assumptions. Ask for confirmation only when unresolved ambiguity remains. If the user delegates the choices, proceed with reasonable defaults and record them in the deliverables.

Do not present the final atlas until the brief is sufficiently clear.

### 2. Classify and map the topic

Read [references/topic-taxonomy.md](references/topic-taxonomy.md). Classify the request by domain type, maturity, rate of change, evidentiary burden, controversy, geographic scope, and theory–practice balance.

Build a dependency-aware knowledge map containing:

- foundational concepts;
- prerequisites;
- major branches;
- representative questions;
- important people and institutions;
- common misconceptions;
- optional deeper directions.

### 3. Design the source and channel plan

Read [references/source-and-channel-policies.md](references/source-and-channel-policies.md) and [references/credibility-criteria.md](references/credibility-criteria.md).

Specify before searching:

- required evidence and material types;
- primary discovery channels and why they fit;
- primary-versus-secondary source balance;
- recency, language, geography, budget, and access rules;
- excluded or low-trust channels;
- credibility and conflict-handling criteria.

Do not apply the same policy to a mature academic field, fast-moving technology, historical event, public figure, industry, practical skill, and current event.

### 4. Discover and verify resources

Search the selected channels broadly enough to avoid one-platform bias. Prefer primary and authoritative sources when available.

Verify every recommended resource:

- confirm existence, canonical title, creator or institution, and working URL;
- confirm relevance to the exact topic and user level;
- check publication date, edition, maintenance status, and access conditions;
- distinguish original evidence, expert interpretation, educational summary, and opinion;
- note ideological, commercial, geographic, or methodological limitations;
- use current web research whenever recency can affect the answer;
- never invent a citation, account, course, paper, archive, or URL.

If a claim or resource cannot be verified, omit it or label the uncertainty explicitly.

### 5. Rank and curate

Rank candidates by authority, relevance, accessibility, timeliness, depth, practicality, reliability, and complementarity.

Assign each selected resource a role:

- Start here
- Core foundation
- Primary evidence
- Guided learning
- Deep dive
- Practice
- Stay updated

Keep the core set deliberately small. Move useful but nonessential materials into optional branches.

### 6. Build the detailed roadmap

Read [references/roadmap-schema.md](references/roadmap-schema.md).

For every stage, provide:

- objective and prerequisite dependencies;
- exact chapters, lectures, sections, papers, episodes, or projects;
- concrete study, research, or practice tasks;
- duration and suggested weekly effort;
- a tangible deliverable or checkpoint;
- completion criteria and a self-check method;
- core and optional materials;
- the condition for advancing to the next stage.

Fit the roadmap to the confirmed time budget. End with one action the user can take immediately.

### 7. Build the shared content model

Read [references/output-schema.md](references/output-schema.md). Create one UTF-8 JSON content model that contains every section, resource, citation, assumption, and roadmap stage.

Treat the JSON as an intermediate build artifact, not as a required user deliverable. Store it in a temporary location unless the user requests the source data.

### 8. Render and validate both files

Read [references/html-design-guidelines.md](references/html-design-guidelines.md).

Run:

```bash
python3 scripts/build_atlas.py \
  --input /path/to/atlas.json \
  --output-dir /path/to/output
```

Create:

```text
anything-atlas-<topic-slug>.md
anything-atlas-<topic-slug>.html
```

Use the bundled logo by default. Keep the HTML self-contained by embedding its CSS and logo.

Run validation separately when reviewing existing output:

```bash
python3 scripts/validate_deliverables.py \
  --input /path/to/atlas.json \
  --markdown /path/to/atlas.md \
  --html /path/to/atlas.html
```

Fix all validation errors before delivery.

### 9. Deliver

Link both output files in the final response. Summarize the confirmed goal, the source strategy, and the recommended first action.

Do not paste the entire atlas into chat unless the user requests it. Do not claim completion when either file is missing.

## Reference routing

- Read `clarification-policy.md` whenever the request is underspecified.
- Read `topic-taxonomy.md` and `source-and-channel-policies.md` before research.
- Read `credibility-criteria.md` while verifying and ranking resources.
- Read `roadmap-schema.md` before writing the roadmap.
- Read `output-schema.md` before creating the shared JSON model.
- Read `html-design-guidelines.md` before rendering or reviewing HTML.

## Safety and uncertainty

- Preserve disagreement between reliable sources instead of manufacturing consensus.
- Separate facts, interpretations, and recommendations.
- State important omissions and inaccessible sources.
- For medical, legal, financial, or other high-stakes topics, provide educational orientation rather than professional advice and prioritize current authoritative sources.
- Avoid using popularity as a substitute for expertise.
