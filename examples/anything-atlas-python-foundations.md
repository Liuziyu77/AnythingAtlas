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

## 2. Topic Brief

### Overview

Python is a general-purpose programming language with readable syntax and a large standard library. A strong beginner path combines language fundamentals, frequent coding practice, debugging, and one useful project.

### Why it matters

Python can automate everyday tasks and provides a foundation for later study in web development, data, scientific computing, and artificial intelligence.

### Expected outcomes

- Read and write small Python programs
- Use control flow, functions, collections, files, and exceptions
- Debug common errors
- Complete and explain a small automation project

## 3. Knowledge Map

### Execution and basic syntax

Running Python, expressions, variables, strings, numbers, and basic input and output.

### Control flow and functions

Conditions, loops, reusable functions, arguments, return values, and scope.

**Depends on:** Execution and basic syntax

### Data and files

Lists, dictionaries, sets, text processing, files, and structured data.

**Depends on:** Control flow and functions

### Reliable small programs

Errors, debugging, tests, decomposition, and an end-to-end automation script.

**Depends on:** Data and files

## 4. Source and Channel Plan

- **Topic type:** Practical skill with a mature technical foundation
- **Required materials:**
  - Official language tutorial
  - Beginner-friendly project book
  - Automated coding exercises

### Priority channels

- **Official Python documentation (Primary):** Canonical language explanations and current syntax
- **Author-maintained open book (Primary):** Guided practical projects with a beginner orientation
- **Exercise platform (Complementary):** Repeated practice, automated checks, and optional mentoring

- **Credibility policy:**
  - Prefer official documentation for language behavior
  - Use current author-maintained material for projects
  - Use exercises as practice rather than as the sole explanation
- **Recency rule:** Check documentation version and platform availability at the time of use.
- **Channel cautions:**
  - The official tutorial assumes some general programming familiarity
  - Exercise catalogs and access features can change

## 5. Recommended Starting Point

- **Action:** Run the first examples in Python and modify each one.
- **Resource:** The Python Tutorial, sections 1–3
- **Why this first:** It establishes the canonical vocabulary and gives immediate hands-on feedback.

## 6. Curated Resource Atlas

### [The Python Tutorial](https://docs.python.org/3/tutorial/)

- **Creator:** Python Software Foundation
- **Type:** Official tutorial
- **Role:** Core foundation
- **Level:** Beginner with some general programming familiarity
- **Format:** Web documentation with examples
- **Time:** 12–16 hours for selected sections
- **Verified:** 2026-07-23

**Why included:** It is the canonical introduction to Python language concepts and current standard behavior.

**Focus:** Sections 1–8 first; use later sections as references when the roadmap calls for them.

**Limitations:** It explicitly expects basic programming understanding and is less project-driven than a beginner course.

### [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

- **Creator:** Al Sweigart
- **Type:** Open web book
- **Role:** Guided learning
- **Level:** Complete beginner
- **Format:** Book chapters and practical projects
- **Time:** 14–18 hours for selected chapters and one project
- **Verified:** 2026-07-23

**Why included:** It connects fundamentals to concrete automation tasks and is available to read online.

**Focus:** Chapters 1–12, then choose one automation chapter that matches the learner’s interests.

**Limitations:** The project breadth is wider than this six-week path, so most later chapters should be treated as optional.

### [Python on Exercism](https://exercism.org/tracks/python)

- **Creator:** Exercism
- **Type:** Exercise track
- **Role:** Practice
- **Level:** Beginner to advanced
- **Format:** Coding exercises, automated analysis, and mentoring
- **Time:** 8–10 hours for selected beginner exercises
- **Verified:** 2026-07-23

**Why included:** It provides deliberate practice and fast feedback that complements reading and projects.

**Focus:** Complete the tutorial exercise and selected concept exercises on basics, conditions, loops, strings, lists, and dictionaries.

**Limitations:** The catalog and mentoring availability can change, and an account may be needed for the full workflow.

## 7. Detailed Learning or Exploration Roadmap

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

- The Python Tutorial
- Automate the Boring Stuff with Python

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

- The Python Tutorial
- Automate the Boring Stuff with Python
- Python on Exercism

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

- Automate the Boring Stuff with Python
- Python on Exercism

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

## 8. Source Notes

- **Official tutorial audience (caution):** The Python Tutorial says it is designed for programmers new to Python rather than people entirely new to programming, so the project book supplies extra beginner scaffolding.
- **Changing platforms (note):** Exercise counts, mentoring features, and access workflows may change; verify the current track before assigning exact exercises.
- **Scope (note):** This roadmap intentionally postpones classes, packaging, web frameworks, data science, and advanced testing.

## 9. Next Action

- **Action:** Open The Python Tutorial and run the examples in sections 1–3, changing at least one value in every example.
- **When:** Today, for 45 minutes
- **Expected output:** A saved Python file containing three modified examples and one sentence about what each demonstrates.

---

*AnythingAtlas · Map the best way into any topic.*
