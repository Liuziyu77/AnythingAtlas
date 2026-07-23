# AnythingAtlas Qualitative Regression Cases

Use these cases when changing the skill instructions, schema, or renderers.
They test content quality that cannot be established by structural validation
alone. Facts and recommendations must still be researched at test time.

## Case A: urgent, high-stakes, short-session learning

### Prompt

> I am a salaried worker in mainland China earning CNY 200,000–300,000 per
> year. I want to understand stock investing in one day, start today with CNY
> 50,000, and then study for 30 minutes a day for one week.

### Acceptance checks

- The clarification batch asks only for variables that could materially change
  an actionable plan, such as liquidity horizon, emergency fund, debt, loss
  tolerance, existing account or holdings, and whether the goal is long-term
  investing or active trading.
- A 30-minute daily cadence is treated as a strong short-form preference. The
  agent either confirms that preference compactly or supplies a short-session
  core track plus a deeper alternative.
- The core guide answers what can realistically be done today and what
  should wait. It is not a page of investing philosophy or disclaimers.
- The guide covers the relevant market segments and instruments,
  and names verified representative examples. If the user asks for current
  sectors, leading companies, securities, or fund codes, the response supplies
  current, sourced analysis or clearly states which requested item could not be
  verified.
- A compact practical subsection names and compares the actual applications, broker or
  official portals, data or disclosure sources, and order workflow the user
  will encounter. Examples may include official exchange and disclosure sites
  and widely used market-data applications, but every named option must be
  verified and assessed for fit and incentives.
- The plan does not substitute simulation or generic caution for all requested
  action. If current facts and the user's profile support only a conditional
  small first action, it states that action, its limit, and the stop conditions.
- When the user requests personalized decision support, the agent does not
  refuse merely because the answer is specific. It gathers the material
  variables, uses current evidence, and provides conditional options, sizing or
  decision rules, risks, and assumptions without implying guaranteed returns or
  professional status.
- Core resources include exact short videos, concise pages, or modular lessons
  that fit 30-minute sessions. Longer books or courses appear in a separate
  deep/reference track with exact assigned portions.

### Automatic gates expected to catch weak output

- no concrete recommendation → `guide.recommendations` validation error;
- no named segments or representative objects → `guide.sections[].items`
  validation error;
- no immediate workflow → `guide.next_action` validation error;
- no cadence-matched resource route → `resource_tracks` validation error.

## Case B: low-stakes physical skill with a weekend deadline

### Prompt

> I want to learn enough pottery in two weekends to make one usable mug. I
> prefer demonstrations over books, live in a city, and do not own any tools.

### Acceptance checks

- The core guide distinguishes hand-building from wheel throwing and
  recommends one based on the two-weekend outcome.
- Its task-specific subsections name representative clay bodies, forming methods, studio
  options, firing stages, and tool categories, with selection rules.
- Its practical subsection names the minimum tools or recommends a studio/class setup,
  then gives an exact first-session sequence and dust, glaze, food-safety, and
  kiln checks that change behavior.
- The core resource track is demonstration-first and broken into session-sized
  units. A book or reference site may be optional, but is not used as the
  default merely because it is authoritative.
- The roadmap ends with an inspectable mug and completion criteria covering
  form, handle attachment, drying, firing, and usability.

## Case C: museum-going introduction to Impressionism

### Prompt

> I want a systematic introduction to Impressionist painting for museum
> visits, not professional art-history research. I know little Western art
> history, can read Chinese and watch English video, and want to understand the
> context, core traits, major artists and works, ways to look at color, light,
> brushwork, subject, and composition, and the relationship to Academic art
> and Post-Impressionism.

### Acceptance checks

- The visible atlas uses five top-level sections by default. It does not expose
  separate field-map, action-kit, knowledge-map, source-plan, or source-note
  chapters.
- The core guide synthesizes historical context, looking skills, representative
  artists and works, and movement relationships into only the distinct
  subsections needed by this user.
- Resource tracks distinguish a short video-led route from a more systematic
  reading or museum-source route, or ask one compact preference question before
  choosing.
- Every assigned museum page, YouTube or Bilibili video, book page, course, or
  other resource is a clickable link in both its resource track and roadmap
  stage, not a plain-text title.
- The final source directory groups the same clickable resources by
  recognizable channels such as museum websites, YouTube, Bilibili, and books.
- Generic sections about methodology, source credibility, or abstract learning
  philosophy are omitted unless they change how this user studies or looks at
  a painting.

## Pass condition

A case passes only when the output is both structurally valid and a reviewer
can answer these questions without hunting:

1. What should this user do or conclude?
2. What concrete options exist, and how do they differ?
3. What must the user set up and do first?
4. Which exact resources fit the user's cadence and format preference?
5. What evidence, assumptions, and limitations support the recommendations?
