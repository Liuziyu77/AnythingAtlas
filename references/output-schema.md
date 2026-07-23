# Output Schema

Use one JSON model as the source for Markdown and HTML. Schema `0.3` separates
internal research checks from the compact information architecture shown to
the user.

## Top-level fields

| Field | Type | Purpose |
| --- | --- | --- |
| `meta` | object | Schema version, title, topic, slug, language, date, summary, total time, HTML theme |
| `brief` | object | Confirmed goal, background, preferences, constraints, assumptions |
| `guide` | object | Direct answer, concrete recommendations, task-specific guide subsections, immediate action |
| `resource_tracks` | array | Alternative resource sequences matched to cadence, format, and depth |
| `resources` | array | Verified curated resources with canonical URLs and recognizable channels |
| `roadmap` | array | Ordered executable stages that reference resources by stable ID |
| `source_directory` | object | Final, channel-grouped directory of linked resources |

These fields render as five visible sections:

1. confirmed brief;
2. core guide;
3. curated resources, including resource tracks;
4. detailed roadmap;
5. source directory.

## Guide object

Include:

```json
{
  "bottom_line": "The direct answer to the user's real question.",
  "key_points": ["Only points that change understanding, action, or a decision."],
  "recommendations": [
    {
      "choice": "A concrete option, method, tool, work, or position",
      "best_for": "The condition or user it fits",
      "why": "The decisive reason",
      "tradeoffs": "The material limitation or alternative"
    }
  ],
  "sections": [
    {
      "title": "A user-facing subsection such as How to Look, Historical Arc, Tool Setup, or Market Landscape",
      "purpose": "What distinct question this subsection answers",
      "items": [
        {
          "name": "Exact concept, method, tool, person, work, product, or action",
          "explanation": "Why it matters and how the user should use it",
          "examples": ["Specific representative examples"]
        }
      ]
    }
  ],
  "next_action": {
    "action": "One concrete action",
    "when": "When and for how long",
    "output": "Inspectable result"
  }
}
```

Use only guide subsections that add distinct value. The internal field map,
action setup, and knowledge dependencies do not each require a visible
subsection. Merge or omit them when they would repeat the same content.

## Resource-track object

Include:

```json
{
  "title": "Quick, balanced, deep, or another user-relevant route",
  "best_for": "Who and what cadence it fits",
  "cadence": "For example, 20 minutes per weekday",
  "resource_ids": ["stable-id"],
  "sequence": ["Exact order and portions to consume"]
}
```

Create at least one track. When format preference is unknown, provide two
meaningfully different tracks rather than one mixed list. Render every
resource ID as a clickable title, not plain text.

## Resource object

Include:

```json
{
  "id": "stable-id",
  "title": "Canonical title",
  "creator": "Author or institution",
  "url": "https://canonical.example/resource",
  "channel": "Official documentation, YouTube, Bilibili, book, podcast, repository, or another recognizable channel",
  "type": "course",
  "role": "Core foundation",
  "level": "Beginner",
  "format": "Video and exercises",
  "time": "12 hours",
  "best_for": "Short guided sessions with immediate practice",
  "access": "Free; web; available in the user's region",
  "why": "Reason for inclusion",
  "focus": "Exact sections to use",
  "limitations": "Relevant caveat",
  "verified_on": "YYYY-MM-DD"
}
```

## Roadmap stage object

Include:

```json
{
  "stage": 1,
  "title": "Build the foundation",
  "duration": "2 weeks",
  "weekly_effort": "6 hours",
  "objectives": ["Observable outcome"],
  "prerequisites": ["None"],
  "resource_ids": ["stable-id"],
  "tasks": ["Concrete task"],
  "deliverable": "Inspectible output",
  "completion_criteria": ["Observable check"],
  "optional": ["Optional branch"]
}
```

Every assigned resource must render as a clickable link to its canonical URL
inside the roadmap stage.

## Source-directory object

Include:

```json
{
  "selection_note": "How the sources were selected and what the grouping means.",
  "groups": [
    {
      "name": "Official institutions",
      "description": "What this channel contributes and how to use it.",
      "resource_ids": ["stable-id"]
    },
    {
      "name": "YouTube",
      "description": "Verified video explainers or lectures.",
      "resource_ids": ["another-stable-id"]
    }
  ]
}
```

Use channel names the user recognizes, such as official museum sites,
university courses, books, YouTube, Bilibili, podcasts, GitHub, newsletters,
or practitioner communities. Every curated resource must appear in at least
one source-directory group.

## Consistency rules

- Set `meta.schema_version` to `0.3`.
- Set `meta.theme` to `atlas`, `scholar`, `archive`, `signal`, or `workshop`.
- Use `atlas` for mixed topics, `scholar` for academic study, `archive` for source-led historical work, `signal` for fast-moving technology, and `workshop` for practical projects unless the user chooses a theme.
- Preserve the five-section presentation order: brief, guide, resources,
  roadmap, source directory.
- Do not expose source methodology, source notes, an action kit, field map, or
  knowledge map as separate top-level sections.
- Include specific examples in every guide item.
- Make every recommendation conditional enough to reveal who or what it fits.
- Use stable resource IDs in resource tracks, roadmap assignments, and source
  groups.
- Keep every resource clickable in tracks, roadmap stages, cards, and the
  source directory.
- Keep all URLs canonical and absolute.
- Use ISO dates when exact dates are known.
- Use arrays even when a field currently has one item.
- Do not put essential content only in presentation-specific fields.
- Ensure all user-facing text is already in the requested language before rendering.
- Prefer precise facts, selections, and actions over generic explanatory prose.

See `examples/sample-atlas.json` for a complete buildable example.
