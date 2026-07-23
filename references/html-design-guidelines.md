# HTML Design Guidelines

Render the atlas as a designed standalone document.

## Required properties

- Use semantic HTML5.
- Embed CSS and the logo so the file works offline.
- Use no required JavaScript.
- Support mobile and desktop layouts.
- Include useful print styles.
- Preserve every section, source note, citation, and roadmap stage from Markdown.
- Escape all user- and research-supplied text.

## Visual hierarchy

Include:

- a branded hero with title and executive summary;
- a compact confirmed-brief panel;
- easy section navigation;
- knowledge-map cards with dependencies;
- source-plan callouts;
- resource cards showing role, level, format, time, reason, focus, and limitations;
- a roadmap timeline with stages, tasks, deliverables, and completion checks;
- visually distinct caution and next-action panels.

## Accessibility

- Set the document language.
- Use one `h1` and ordered heading levels.
- Give the logo meaningful alt text.
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

Use a calm atlas aesthetic: deep navy, clear blue, cyan accents, generous white space, subtle contour or grid motifs, and restrained shadows. Prioritize legibility over decoration.

## Validation

Check:

1. standalone opening without network access;
2. section and resource parity with Markdown;
3. heading and landmark structure;
4. internal anchors;
5. external URL schemes;
6. mobile and print readability;
7. absence of raw template placeholders.
