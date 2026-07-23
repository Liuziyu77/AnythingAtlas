# Output Schema

Use one JSON model as the source for Markdown and HTML.

## Top-level fields

| Field | Type | Purpose |
| --- | --- | --- |
| `meta` | object | Title, topic, slug, language, date, summary, total time, HTML theme |
| `brief` | object | Confirmed goal, background, preferences, constraints, assumptions |
| `topic_brief` | object | Overview, importance, expected outcomes |
| `knowledge_map` | array | Concepts or branches with descriptions and dependencies |
| `source_plan` | object | Topic type, materials, channels, credibility, recency, cautions |
| `starting_point` | object | Best first action or resource and rationale |
| `resources` | array | Verified curated resources |
| `roadmap` | array | Ordered executable stages |
| `source_notes` | array | Credibility, recency, bias, controversy, and evidence notes |
| `next_action` | object | Immediate action, timing, and expected output |

## Resource object

Include:

```json
{
  "id": "stable-id",
  "title": "Canonical title",
  "creator": "Author or institution",
  "url": "https://canonical.example/resource",
  "type": "course",
  "role": "Core foundation",
  "level": "Beginner",
  "format": "Video and exercises",
  "time": "12 hours",
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

## Consistency rules

- Set `meta.theme` to `atlas`, `scholar`, `archive`, `signal`, or `workshop`.
- Use `atlas` for mixed topics, `scholar` for academic study, `archive` for source-led historical work, `signal` for fast-moving technology, and `workshop` for practical projects unless the user chooses a theme.
- Preserve top-level presentation order: brief, topic brief, knowledge map, source plan, starting point, resources, roadmap, source notes, next action.
- Use stable resource IDs in roadmap assignments.
- Keep all URLs canonical and absolute.
- Use ISO dates when exact dates are known.
- Use arrays even when a field currently has one item.
- Write empty optional arrays instead of filler text.
- Do not put essential content only in presentation-specific fields.
- Ensure all user-facing text is already in the requested language before rendering.
- Prefer precise facts, selections, and actions over generic explanatory prose.

See `examples/sample-atlas.json` for a complete buildable example.
