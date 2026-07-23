# HTML Design Guidelines

Render the atlas as a designed standalone document.

## Required properties

- Use semantic HTML5.
- Embed CSS so the file works offline.
- Use no required JavaScript.
- Support mobile and desktop layouts.
- Include useful print styles.
- Preserve every section, source note, citation, and roadmap stage from Markdown.
- Escape all user- and research-supplied text.
- Use no AnythingAtlas image logo in generated HTML.
- Credit AnythingAtlas once, as text, in the footer.

## Visual hierarchy

Include:

- a focused hero with the atlas title and executive summary;
- a compact confirmed-brief panel;
- easy section navigation;
- knowledge-map cards with dependencies;
- source-plan callouts;
- resource cards showing role, level, format, time, reason, focus, and limitations;
- a roadmap timeline with stages, tasks, deliverables, and completion checks;
- visually distinct caution and next-action panels.

Present the atlas in this sequence:

1. confirmed brief;
2. topic brief;
3. knowledge map;
4. source and channel plan;
5. recommended starting point;
6. curated resources;
7. detailed roadmap;
8. source notes;
9. next action.

The first six sections establish what the field contains, which evidence matters, and which resources were selected. Only then should the page present the learning roadmap.

## Accessibility

- Set the document language.
- Use one `h1` and ordered heading levels.
- Preserve visible keyboard focus.
- Maintain readable contrast.
- Do not encode meaning by color alone.
- Use descriptive link text.
- Allow text zoom without clipping.
- Respect `prefers-reduced-motion`.

## Responsive and print behavior

- Collapse the sidebar into normal flow on narrow screens.
- Avoid fixed content widths that overflow.
- Allow long URLs to wrap.
- Keep cards and roadmap stages from splitting awkwardly in print.
- Hide navigation controls that are useless on paper.
- Preserve source URLs in printable form.

## Style direction

Choose one built-in theme from the topic and the user’s preference:

| Theme | Best fit | Direction |
| --- | --- | --- |
| `atlas` | Broad or interdisciplinary topics | Cartographic blue, clear hierarchy, balanced cards |
| `scholar` | Mature academic and theory-heavy fields | Warm editorial typography, paper-like reading flow |
| `archive` | History, people, organizations, primary-source work | Archival dossier, restrained sepia, document cues |
| `signal` | Fast-moving technology and research frontiers | Dark high-contrast interface, technical signal accents |
| `workshop` | Practical skills and project-based learning | Bold modules, visible checkpoints, energetic color |

Use `atlas` when no stronger match exists. A user’s explicit theme choice wins unless it would materially harm legibility. All themes must preserve the same content, semantics, responsive behavior, print behavior, and text-only footer credit. Prioritize legibility and information density over decoration.

## Validation

Check:

1. standalone opening without network access;
2. section and resource parity with Markdown;
3. research sections appear before the roadmap;
4. heading and landmark structure;
5. internal anchors;
6. external URL schemes;
7. mobile and print readability;
8. the selected `theme-*` body class;
9. a text-only AnythingAtlas footer credit and no brand image;
10. absence of raw template placeholders.
