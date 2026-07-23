# Output Schema

Use one JSON model as the source for Markdown and HTML.

## Top-level fields

| Field | Type | Purpose |
| --- | --- | --- |
| `meta` | object | Schema version, title, topic, slug, language, date, summary, total time, HTML theme |
| `brief` | object | Confirmed goal, background, preferences, constraints, assumptions |
| `orientation` | object | Direct bottom line, decision-relevant points, concrete recommendations, trade-offs |
| `field_guide` | object | Dated map of relevant segments, options, actors, tools, works, or approaches |
| `action_kit` | object | Setup, first-session workflow, decision rules, and safety or quality checks |
| `knowledge_map` | array | Concepts or branches with descriptions and dependencies |
| `resource_tracks` | array | Alternative resource sequences matched to cadence, format, and depth |
| `resources` | array | Verified curated resources |
| `roadmap` | array | Ordered executable stages |
| `source_plan` | object | Topic type, materials, channels, credibility, recency, cautions |
| `source_notes` | array | Credibility, recency, bias, controversy, and evidence notes |
| `next_action` | object | Immediate action, timing, and expected output |

## Orientation object

Include:

```json
{
  "bottom_line": "The direct answer to the user's real question.",
  "key_points": ["Only points that change a decision or action."],
  "recommendations": [
    {
      "choice": "A concrete option, method, tool, work, or position",
      "best_for": "The condition or user it fits",
      "why": "The decisive reason",
      "tradeoffs": "The material limitation or alternative"
    }
  ],
  "tradeoffs": ["Cross-cutting conditions or uncertainties."]
}
```

## Field-guide object

Include:

```json
{
  "as_of": "YYYY-MM-DD or a stable-period description",
  "scope": "What the guide includes and excludes",
  "entries": [
    {
      "name": "Exact segment, approach, organization, product, tool, person, or work",
      "category": "Its role in the field",
      "why_it_matters": "Why the user should notice it",
      "representative_examples": ["Specific examples, not category placeholders"],
      "selection_note": "When to choose, follow, compare, or ignore it"
    }
  ]
}
```

For changing topics, use a real `as_of` date and verify current names,
availability, and status. For stable topics, the field guide may map canonical
schools, works, methods, or sources.

## Action-kit object

Include:

```json
{
  "setup": [
    {
      "item": "Tool, account, environment, template, or source",
      "recommendation": "Exact setup choice",
      "why": "Why this choice fits the brief"
    }
  ],
  "first_session": ["Ordered, concrete actions"],
  "decision_rules": ["If/then rules or quality criteria"],
  "safety_checks": ["Only checks that change behavior"],
  "failure_modes": ["Likely mistakes and their corrections"]
}
```

Use an empty `setup` or `safety_checks` array when genuinely irrelevant; never
fill them with generic prose.

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
meaningfully different tracks rather than one mixed list.

The `source_plan` must include `topic_type`, `materials`, `channels`,
`credibility_policy`, `recency`, `format_fit`, and `cautions`. `format_fit`
records why the chosen media and unit lengths match the user's normal cadence.

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

## Consistency rules

- Set `meta.schema_version` to `0.2`.
- Set `meta.theme` to `atlas`, `scholar`, `archive`, `signal`, or `workshop`.
- Use `atlas` for mixed topics, `scholar` for academic study, `archive` for source-led historical work, `signal` for fast-moving technology, and `workshop` for practical projects unless the user chooses a theme.
- Preserve top-level presentation order: brief, orientation, field guide,
  action kit, knowledge map, resource tracks, resources, roadmap, source plan,
  source notes, next action.
- Put the direct answer before definitions and methodology.
- Include representative examples in every field-guide entry.
- Make every recommendation conditional enough to reveal who or what it fits.
- Use stable resource IDs in roadmap assignments.
- Use stable resource IDs in resource-track assignments.
- Keep all URLs canonical and absolute.
- Use ISO dates when exact dates are known.
- Use arrays even when a field currently has one item.
- Write empty optional arrays instead of filler text.
- Do not put essential content only in presentation-specific fields.
- Ensure all user-facing text is already in the requested language before rendering.
- Prefer precise facts, selections, and actions over generic explanatory prose.
- Put source methodology after the practical and learning sections; do not
  force the user through it before the answer.

See `examples/sample-atlas.json` for a complete buildable example.
