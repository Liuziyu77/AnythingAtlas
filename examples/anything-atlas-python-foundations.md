# Python Programming Foundations

> A practical six-week path from Python syntax to a small automation project.

**Generated:** 2026-07-23
**Estimated total time:** 6 weeks · 5 hours per week

---

## 1. Confirmed User Brief

- **Goal:** Write small, useful Python programs and become ready for a project-focused intermediate course.
- **Starting point:** No Python experience and only limited prior programming exposure.
- **Available time:** 5 hours per week for 6 weeks
- **Language:** English
- **Preferred formats:**
  - Written tutorials
  - Hands-on exercises
  - Small projects
- **Desired depth:** Beginner foundation with practical application
- **Constraints:**
  - Prefer free web-accessible resources
  - Keep the core set to three resources
- **Assumptions:**
  - The learner can install Python or use a browser-based environment
  - The learner wants general automation rather than data science specialization

## 2. Core Guide

### Bottom line

Start with the official Python runtime and a plain code editor, learn only the syntax needed to automate one real file or text task, and use short exercises for feedback. Do not begin with frameworks, data-science stacks, or a long survey course.

### What matters

- Typing and modifying working examples builds useful fluency faster than passive watching.
- Functions, collections, files, and error handling cover most beginner automation tasks.
- One small end-to-end script is a better six-week checkpoint than broad but shallow topic coverage.

### Recommendations

#### Official tutorial plus a local Python installation

- **Best for:** Learning canonical behavior and becoming comfortable running real files
- **Why:** It keeps the environment close to how Python is actually used and provides authoritative syntax explanations.
- **Trade-offs:** The tutorial assumes some general programming familiarity, so a complete beginner needs a gentler project resource alongside it.

#### Automate the Boring Stuff as the project spine

- **Best for:** A complete beginner motivated by useful office or file automation
- **Why:** Its examples turn syntax into recognizable tasks instead of treating Python as abstract theory.
- **Trade-offs:** The book is much broader than this plan; only the assigned chapters and one project should be core.


### Use one simple toolchain

> **What this section answers:** Choose where to run, write, and practice Python without wasting the first week on tooling.

#### Runtime

Install the current stable Python 3 release and run files locally. Use a browser notebook only when installation is blocked.

**Examples:** Python from python.org; Google Colab as a temporary fallback

#### Editor

Use one editor with syntax highlighting and a visible terminal for the full six-week path.

**Examples:** Visual Studio Code with the Microsoft Python extension; IDLE for the smallest setup

#### Practice loop

End every session with code that runs or a documented error you can explain; passive watching does not count as practice.

**Examples:** Modify one working example; Complete one Exercism concept task; Record and fix one traceback


### Learn capabilities in dependency order

> **What this section answers:** Focus on the smallest concept sequence that leads to a useful automation script.

#### Run and read code

Start with expressions, variables, strings, input, output, and reading simple tracebacks.

**Examples:** A greeting script; A deliberate SyntaxError and NameError

#### Control and reuse

Add conditions, loops, and functions so a script can make decisions and avoid repeated code.

**Examples:** A text game; A function that validates input

#### Process data and files

Use lists, dictionaries, text processing, and files to solve realistic automation tasks.

**Examples:** Summarize a text file; Read and write JSON

#### Make the script reliable

Handle empty and invalid inputs, break work into functions, and document how another person can run the program.

**Examples:** Failure-case checklist; Short usage guide; Reusable command-line script


### Next Action

- **Action:** Open The Python Tutorial and run the examples in sections 1–3, changing at least one value in every example.
- **When:** Today, for 45 minutes
- **Expected output:** A saved Python file containing three modified examples and one sentence about what each demonstrates.

## 3. Curated Resource Atlas

### Choose a route

#### Short-session practical track

- **Best for:** A beginner learning in 30–45 minute sessions who wants visible progress every day
- **Cadence:** Five 30–45 minute sessions per week
- **Assigned resources:** [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/), [Python on Exercism](https://exercism.org/tracks/python), [The Python Tutorial](https://docs.python.org/3/tutorial/)

**Sequence**

- Read one assigned Automate the Boring Stuff section for no more than 15 minutes.
- Type and alter the example for 15 minutes.
- Use the remaining time for one small Exercism task or one debugging note.
- Consult the matching Python Tutorial section only when a concept needs a canonical explanation.

#### Reference-first track

- **Best for:** A learner who prefers precise written explanations and can sustain 60–90 minute sessions
- **Cadence:** Three 60–90 minute sessions per week
- **Assigned resources:** [The Python Tutorial](https://docs.python.org/3/tutorial/), [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/), [Python on Exercism](https://exercism.org/tracks/python)

**Sequence**

- Study the assigned Python Tutorial section and run every example.
- Complete the matching project-book chapter.
- Finish one or two concept exercises and record any errors that required documentation.

### Resource details

#### [The Python Tutorial](https://docs.python.org/3/tutorial/)

- **Creator:** Python Software Foundation
- **Channel:** Official documentation
- **Type:** Official tutorial
- **Role:** Core foundation
- **Level:** Beginner with some general programming familiarity
- **Format:** Web documentation with examples
- **Time:** 12–16 hours for selected sections
- **Best for:** Learners who want precise, canonical explanations and do not mind dense reading
- **Access:** Free web access; no account required
- **Verified:** 2026-07-23

**Why included:** It is the canonical introduction to Python language concepts and current standard behavior.

**Focus:** Sections 1–8 first; use later sections as references when the roadmap calls for them.

**Limitations:** It explicitly expects basic programming understanding and is less project-driven than a beginner course.

#### [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

- **Creator:** Al Sweigart
- **Channel:** Author-maintained open book
- **Type:** Open web book
- **Role:** Guided learning
- **Level:** Complete beginner
- **Format:** Book chapters and practical projects
- **Time:** 14–18 hours for selected chapters and one project
- **Best for:** Complete beginners motivated by short, useful automation projects
- **Access:** Free to read on the web; optional paid editions and courses
- **Verified:** 2026-07-23

**Why included:** It connects fundamentals to concrete automation tasks and is available to read online.

**Focus:** Chapters 1–12, then choose one automation chapter that matches the learner’s interests.

**Limitations:** The project breadth is wider than this six-week path, so most later chapters should be treated as optional.

#### [Python on Exercism](https://exercism.org/tracks/python)

- **Creator:** Exercism
- **Channel:** Practice platform
- **Type:** Exercise track
- **Role:** Practice
- **Level:** Beginner to advanced
- **Format:** Coding exercises, automated analysis, and mentoring
- **Time:** 8–10 hours for selected beginner exercises
- **Best for:** Short practice sessions with immediate automated feedback
- **Access:** Free account-based web platform
- **Verified:** 2026-07-23

**Why included:** It provides deliberate practice and fast feedback that complements reading and projects.

**Focus:** Complete the tutorial exercise and selected concept exercises on basics, conditions, loops, strings, lists, and dictionaries.

**Limitations:** The catalog and mentoring availability can change, and an account may be needed for the full workflow.

## 4. Detailed Learning or Exploration Roadmap

### Stage 1: Learn to read and run Python

- **Duration:** 2 weeks
- **Weekly effort:** 5 hours

**Objectives**

- Run Python programs
- Use values, variables, strings, conditions, loops, and functions
- Explain a traceback at a basic level

**Prerequisites**

- None

**Assigned resources**

- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

**Tasks**

- Work through Python Tutorial sections 1–4
- Complete Automate the Boring Stuff chapters 1–5
- Rewrite five examples from memory and deliberately trigger three errors

**Deliverable:** A command-line number or text game using at least one function and one loop.

**Completion criteria**

- Explain variables, conditions, loops, functions, and exceptions without notes
- Fix a syntax error and a simple runtime error
- Run the deliverable from a clean terminal session

**Optional branches**

- Add input validation to the game

### Stage 2: Work with data and files

- **Duration:** 2 weeks
- **Weekly effort:** 5 hours

**Objectives**

- Use lists and dictionaries
- Process text and files
- Break a problem into small functions

**Prerequisites**

- Complete Stage 1

**Assigned resources**

- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python on Exercism](https://exercism.org/tracks/python)

**Tasks**

- Study Python Tutorial sections 5, 7, and 8
- Complete Automate the Boring Stuff chapters 6–10
- Solve six selected Exercism concept exercises
- Write a script that reads a text file and produces a summary

**Deliverable:** A tested text-processing utility with a short usage guide.

**Completion criteria**

- Choose an appropriate list or dictionary for a new problem
- Read and write a UTF-8 text file safely
- Explain the program’s function boundaries and error handling

**Optional branches**

- Add JSON input or output

### Stage 3: Build a useful automation project

- **Duration:** 2 weeks
- **Weekly effort:** 5 hours

**Objectives**

- Plan a small program
- Use documentation independently
- Test and explain an end-to-end script

**Prerequisites**

- Complete Stage 2

**Assigned resources**

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python on Exercism](https://exercism.org/tracks/python)

**Tasks**

- Choose one automation problem involving files, text, or structured data
- Write a one-page plan before coding
- Implement the project in small functions
- Test normal, empty, and invalid inputs
- Write a concise retrospective

**Deliverable:** A reusable automation script, tests or a verification checklist, and a one-page project note.

**Completion criteria**

- A new user can run the script from the usage instructions
- The script handles at least two failure cases
- The learner can explain every function and identify the next improvement

**Optional branches**

- Package the script as a command-line tool
- Request feedback on one Exercism solution


## 5. Source Directory

**How these sources were selected:** The core set combines one canonical language source, one beginner project source, and one feedback-oriented practice source. Each resource is free on the web and assigned in exact portions.

### Official documentation

Use for canonical Python behavior, terminology, and version-current explanations.

- [The Python Tutorial](https://docs.python.org/3/tutorial/) — Python Software Foundation; Sections 1–8 first; use later sections as references when the roadmap calls for them.

### Open book

Use for complete-beginner explanations and practical automation projects.

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — Al Sweigart; Chapters 1–12, then choose one automation chapter that matches the learner’s interests.

### Practice platform

Use for short exercises, automated feedback, and optional mentoring.

- [Python on Exercism](https://exercism.org/tracks/python) — Exercism; Complete the tutorial exercise and selected concept exercises on basics, conditions, loops, strings, lists, and dictionaries.


---

*AnythingAtlas · Map the best way into any topic*
