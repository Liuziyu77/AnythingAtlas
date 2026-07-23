---
name: anything-atlas
description: Research and curate a trustworthy, action-first entry into any unfamiliar topic. Use when a user asks for practical orientation, concrete tools or options, a field map, a reading list, learning resources, books, videos, courses, papers, experts or accounts to follow, a topic research plan, or a personalized curriculum or roadmap. Clarify only material gaps, match resources to format and session-length preferences, verify and rank sources, build an executable first-session kit and staged roadmap, and always deliver synchronized Markdown and polished self-contained HTML files.
---

# AnythingAtlas

Turn an unfamiliar topic into a verified knowledge atlas and an executable learning or exploration roadmap.

## Non-negotiable requirements

- Clarify the user’s real goal before doing expensive research.
- Adapt the evidence standard, resource types, and discovery channels to the topic.
- Verify that recommended resources exist and that titles, authors, URLs, dates, and access conditions are accurate.
- Prefer the smallest sufficient set of complementary resources over a long undifferentiated list.
- Explain why every resource is included, who it suits, what to focus on, and what its limitations are.
- Answer first: put the direct conclusion, concrete options, and decisive
  trade-offs before background, methodology, and the learning plan.
- Include a field guide with exact, representative tools, platforms, products,
  works, people, institutions, methods, or players appropriate to the topic.
- Match resources to the user's preferred format and normal session length;
  provide distinct quick, balanced, or deep tracks when useful.
- For action-oriented requests, name the actual setup and give an executable
  first-session workflow.
- Write compactly: prioritize decisions, evidence, exact resource assignments, and actions over generic explanation.
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
- preferred language, formats, normal session length, and practice modes;
- depth, budget, geography, and access;
- sources or viewpoints to include or avoid.

Summarize the interpreted brief and consequential assumptions. Ask for confirmation only when unresolved ambiguity remains. If the user delegates the choices, proceed with reasonable defaults and record them in the deliverables.

Do not present the final atlas until the brief is sufficiently clear.

When the user wants to act immediately and learn afterward, treat those as two
linked horizons: a minimum viable first-session outcome and a follow-on
learning cadence. Infer a short-form preference when the user only has short
daily sessions; do not ask again unless the choice remains consequential.

### 2. Classify and map the topic

Read [references/topic-taxonomy.md](references/topic-taxonomy.md) and
[references/specificity-and-resource-fit.md](references/specificity-and-resource-fit.md).
Classify the request by domain type, maturity, rate of change, evidentiary
burden, controversy, geographic scope, theory–practice balance, user mode,
urgency, and consumption pattern.

Build a dependency-aware knowledge map containing:

- foundational concepts;
- prerequisites;
- major branches;
- representative questions;
- important people and institutions;
- common misconceptions;
- optional deeper directions.

Separately build a field guide that names the concrete landscape the user will
encounter: major segments, representative choices or actors, what each is
known for, and how to select among them. Date-stamp it when the field changes.

### 3. Design the source and channel plan

Read [references/source-and-channel-policies.md](references/source-and-channel-policies.md) and [references/credibility-criteria.md](references/credibility-criteria.md).

Specify before searching:

- required evidence and material types;
- primary discovery channels and why they fit;
- primary-versus-secondary source balance;
- recency, language, geography, budget, and access rules;
- excluded or low-trust channels;
- credibility and conflict-handling criteria;
- format and session-length fit;
- channels for actual tools, platforms, practitioners, creators, accounts,
  communities, products, or official portals relevant to the task.

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
- never invent a citation, account, course, paper, archive, or URL;
- verify concrete field-guide entries, tools, platforms, representative
  examples, and ongoing-update accounts when included.

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

Organize the selected resources into one or more user-fit tracks. Every track
must state who it fits, the cadence, exact resource order, and exact portions
to consume. Do not mix books, videos, sites, and accounts indiscriminately.

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

For urgent practical requests, create the concrete setup and minimum viable
first-session path before the longer roadmap. Do not replace requested action
with theory, simulation, or warnings alone unless a specific safety, legal,
access, or feasibility constraint requires it.

### 7. Build the shared content model

Read [references/output-schema.md](references/output-schema.md). Create one UTF-8 JSON content model that contains every section, resource, citation, assumption, and roadmap stage.

Treat the JSON as an intermediate build artifact, not as a required user deliverable. Store it in a temporary location unless the user requests the source data.

The model must carry the direct orientation, field guide, action kit, resource
tracks, curated resources, roadmap, and evidence notes. Do not bury essential
recommendations in prose that the renderers cannot preserve.

### 8. Render and validate both files

Read [references/html-design-guidelines.md](references/html-design-guidelines.md).

Choose the HTML theme from the user’s preference and topic classification:

- `atlas` for broad, interdisciplinary, or mixed topics, and as the default;
- `scholar` for mature academic fields and theory-heavy study;
- `archive` for history, people, organizations, and source-led investigation;
- `signal` for fast-moving technology, AI, software, and research frontiers;
- `workshop` for practical skills, projects, and learn-by-doing paths.

Set the choice in `meta.theme`, or pass it explicitly with `--theme`. User preference overrides the automatic mapping when it does not reduce readability.

Run:

```bash
python3 scripts/build_atlas.py \
  --input /path/to/atlas.json \
  --output-dir /path/to/output \
  --theme <atlas|scholar|archive|signal|workshop>
```

Create:

```text
anything-atlas-<topic-slug>.md
anything-atlas-<topic-slug>.html
```

Keep this answer-first order in both deliverables:

1. confirmed brief;
2. direct orientation;
3. field guide;
4. practical action kit;
5. knowledge map;
6. resource tracks;
7. curated resources;
8. detailed roadmap;
9. source and channel plan;
10. source notes;
11. next action.

Keep the HTML self-contained by embedding its CSS. Do not place the AnythingAtlas logo, a brand banner, or a brand block in the generated atlas. Credit AnythingAtlas once, as text, in the footer.

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
- Read `specificity-and-resource-fit.md` before mapping, curating, or writing
  any atlas.
- Read `topic-taxonomy.md` and `source-and-channel-policies.md` before research.
- Read `credibility-criteria.md` while verifying and ranking resources.
- Read `roadmap-schema.md` before writing the roadmap.
- Read `output-schema.md` before creating the shared JSON model.
- Read `html-design-guidelines.md` before rendering or reviewing HTML.

## Safety and uncertainty

- Preserve disagreement between reliable sources instead of manufacturing consensus.
- Separate facts, interpretations, and recommendations.
- State important omissions and inaccessible sources.
- For medical, legal, financial, or other high-stakes topics, prioritize
  current authoritative sources and clearly separate facts, analysis, and
  recommendations. Give specific conditional or scenario-based options when
  the user asks for decision support and the material variables are known.
  Never imply licensure, a fiduciary relationship, a diagnosis, guaranteed
  outcomes, or unsupported certainty.
- Do not use a disclaimer as a substitute for answering the user's question.
- Avoid using popularity as a substitute for expertise.
