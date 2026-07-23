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
- The direct orientation answers what can realistically be done today and what
  should wait. It is not a page of investing philosophy or disclaimers.
- The dated field guide covers the relevant market segments and instruments,
  and names verified representative examples. If the user asks for current
  sectors, leading companies, securities, or fund codes, the response supplies
  current, sourced analysis or clearly states which requested item could not be
  verified.
- The action kit names and compares the actual applications, broker or
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

- no concrete recommendation → `orientation.recommendations` validation error;
- no named segments or representative objects → `field_guide.entries`
  validation error;
- no first-session workflow → `action_kit.first_session` validation error;
- no cadence-matched resource route → `resource_tracks` validation error.

## Case B: low-stakes physical skill with a weekend deadline

### Prompt

> I want to learn enough pottery in two weekends to make one usable mug. I
> prefer demonstrations over books, live in a city, and do not own any tools.

### Acceptance checks

- The direct orientation distinguishes hand-building from wheel throwing and
  recommends one based on the two-weekend outcome.
- The field guide names representative clay bodies, forming methods, studio
  options, firing stages, and tool categories, with selection rules.
- The action kit names the minimum tools or recommends a studio/class setup,
  then gives an exact first-session sequence and dust, glaze, food-safety, and
  kiln checks that change behavior.
- The core resource track is demonstration-first and broken into session-sized
  units. A book or reference site may be optional, but is not used as the
  default merely because it is authoritative.
- The roadmap ends with an inspectable mug and completion criteria covering
  form, handle attachment, drying, firing, and usability.

## Pass condition

A case passes only when the output is both structurally valid and a reviewer
can answer these questions without hunting:

1. What should this user do or conclude?
2. What concrete options exist, and how do they differ?
3. What must the user set up and do first?
4. Which exact resources fit the user's cadence and format preference?
5. What evidence, assumptions, and limitations support the recommendations?

