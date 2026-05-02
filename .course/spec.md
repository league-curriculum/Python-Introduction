# Curik Course Specification

## Course Concept

**Course title:** Introduction to Programming with Python

**Audience:** Middle school students (grades 6–8) at the League of Amazing Programmers, a non-profit programming school serving 5th–12th graders in San Diego. No prior programming experience is assumed; this is intended as a first programming course.

**Framing:** Originally an "Hour of Code" activity (created in collaboration with Trinket.io), now expanded into a multi-week introductory course while retaining the Hour-of-Code spirit: zero installation friction, immediate visual feedback, low-stakes exploration with reset buttons.

**Scope:** 25 lessons across four modules plus a capstone final project.

- Module 0 — Turtles (8 lessons): meeting the turtle, movement, color, text, pen state, circles, the coordinate grid, advanced turtle methods.
- Module 1 — Remembering and Repeating (7 lessons): variables, `for` loops with `range`, function definitions, loop-driven shape drawing, lists, `if/elif/else`.
- Module 2 — Function Practice (4 lessons): parameters, an interactive "happy pet" program, turtle commands as functions, drawing complex shapes.
- Module 3 — Lists, Strings, and Iterables (2 lessons): list methods, advanced list manipulation, strings as iterables.
- Final Project: open-ended capstone requiring lists, tuples, `zip`, `range` loops, conditionals, and `input()`.

**Learner outcome:** By the end of the course, a student can read and modify Python programs that use variables, loops, conditionals, lists, and functions to produce graphical and interactive turtle programs, and can plan and complete a small original program of their own.

**Engagement hook:** Every lesson presents code that runs in the browser via Trinket — students see their changes draw on screen within seconds, which keeps young learners motivated through the abstraction-heavy middle of the course (variables, loops, functions).

**Runtime:** Trinket.io embedded Python. No local Python install, no IDE setup, no command line. Students need only a browser and (optionally) a free Trinket account to save work.

**Pedagogical orientation:** Project-based with a strong turtle/visual-graphics focus. New concepts are introduced when they are needed to make a more interesting drawing or program, rather than systematically by language feature.

## Pedagogical Model

**Approach:** Constructivist, project-based learning anchored in turtle graphics. Students build and modify working programs from lesson one; abstract concepts (variables, loops, functions) are introduced when they enable a more interesting drawing or interactive behavior.

**Why turtle-first:**
- Immediate, visible feedback turns code into a drawing — young learners stay engaged through the unavoidable abstraction-heavy stretches.
- Errors are visible (the turtle goes the wrong way) and recoverable (reset button), which lowers the cost of experimentation.
- The same turtle metaphor carries from `forward()` (Module 0) through `for` loops (Module 1) and reusable functions (Module 2) into open-ended composition (final project), so each new concept extends a familiar object instead of starting from scratch.

**Concept progression:**
1. **Concrete commands** (Module 0): one-off turtle methods. Students build muscle memory for syntax and learn that programs are sequences of instructions.
2. **Naming and repetition** (Module 1): variables let you remember a value, loops let you repeat without copy-paste, functions let you name a behavior, conditionals let you choose between behaviors. Each concept is introduced via a turtle drawing that becomes tedious without it.
3. **Composition** (Module 2): students write functions that take parameters and call other functions, building larger programs out of small pieces.
4. **Data** (Module 3): lists and strings as containers and as iterables. Sets up the final project, which requires combining data structures with control flow.
5. **Capstone**: open-ended project with a required-techniques checklist, not a prescribed output. Students choose what to build.

**Cognitive-load practices:**
- One new concept per lesson; the rest of the lesson reinforces with variations.
- Live, runnable code embedded in every lesson — students never read code they cannot also run and edit.
- Reset button on every embed: experimentation is encouraged because mistakes are one click from undone.
- Worked examples precede free exercises within a lesson.

**Differentiation:**
- Tier 3 student-facing content with optional "advanced" extensions in some lessons (e.g., Module 0 lesson 8 reads the official Python turtle docs).
- Instructor-guide section (per lesson) supplies pacing notes, common mistakes, and discussion prompts for the teacher to differentiate live.

**Assessment philosophy:** Assessment-for-learning, not high-stakes testing. Each lesson's exercises are formative; the final project is a portfolio piece judged against a checklist of required techniques rather than a rubric score.

## Research Summary

**Why Python for first programming:**
- Python's syntax minimizes ceremony — no semicolons, no type declarations, no `public static void main`. Beginners write meaningful programs on day one.
- Industry relevance is strong (data science, web, ML, scripting), so the language students learn first is also one they will see again, which sustains motivation.
- Exceptionally large beginner-resource ecosystem; students who get stuck have many places to look.

**Why turtle graphics for first Python:**
- Originating in Logo (Papert, 1980), turtle graphics is the most-studied visual-programming primitive for novices. The "body-syntonic" mental model (you are the turtle) gives students a way to debug by mentally walking through code.
- Output is graphical and immediate — the dominant alternative for first programs (`print()` of arithmetic) produces text output that intermediate-grade students often experience as boring.
- Errors fail visibly (the drawing is wrong) rather than silently (a wrong number printed), so debugging is naturally motivated.

**Why Trinket for runtime:**
- Zero install, zero configuration. Critical for a school setting where students may be on Chromebooks, school-managed laptops, or home computers without admin rights.
- Embeds run inline in each lesson — students never context-switch between "reading the lesson" and "running the code." The decision cost of trying something is near zero.
- Reset button restores the canonical example, so students who break their copy can recover without losing the lesson.
- Trade-off accepted: no debugger, no file system, no third-party packages. For an introductory course these absences are simplifying, not limiting.

**Why middle school:**
- Grades 6–8 is the empirically observed window where students form long-term attitudes toward computing. Positive early experience predicts later CS course-taking, especially for under-represented students.
- Cognitive readiness for variables and loops is generally established by grade 6; functions and lists are within reach by grade 8 with appropriate scaffolding.
- The League of Amazing Programmers' existing student population centers on this age range, so the course slots into an established pipeline.

**Comparable courses surveyed:**
- Code.org CS Discoveries — middle-school CS, but block-based for most of the year. We pick up where Code.org leaves off, transitioning students to text-based code.
- Trinket's own "Hour of Python" — the seed of this course; we extend its 1-hour scope into a full intro sequence while preserving its Trinket-embedded format.
- CMU CS Academy — Python with graphics, but desktop-installed and high-school targeted. Our course is browser-only and pitched younger.

**Gaps this course fills:** A browser-only, turtle-first, Trinket-embedded Python introduction that is long enough (25 lessons + capstone) to take a complete novice to writing original programs, without ever requiring local installation.

## Alignment Decision

**League of Amazing Programmers curriculum alignment:**
This course is the on-ramp to the League's Python track. It precedes any course that assumes students can already write a `for` loop or define a function, and it feeds directly into the League's intermediate Python offerings (data structures, OOP, simple games beyond turtle).

**Standards alignment (CSTA K-12 Computer Science Standards, grades 6–8 band, 2017):**
- **2-AP-10 — Use flowcharts and/or pseudocode to address complex problems as algorithms.** Lessons 030 (loops) and 070 (if/else) explicitly contrast "do this in your head" with "tell the computer."
- **2-AP-11 — Create clearly named variables that represent different data types and perform operations on their values.** Module 1 lesson 020 (variables) and Module 3 lessons (lists, strings).
- **2-AP-12 — Design and iteratively develop programs that combine control structures, including nested loops and compound conditionals.** Module 1 lessons 030–070; final project requires combining loops, conditionals, and lists.
- **2-AP-13 — Decompose problems and subproblems into parts to facilitate the design, implementation, and review of programs.** Module 2 (function practice) is built around decomposition.
- **2-AP-14 — Create procedures with parameters to organize code and make it easier to reuse.** Module 1 lesson 040 and all of Module 2.
- **2-AP-16 — Incorporate existing code, media, and libraries into original programs, and give attribution.** Module 0 lesson 080 has students reading the official Python turtle docs and using methods we did not teach directly.
- **2-AP-17 — Systematically test and refine programs using a range of test cases.** Embedded throughout via the Trinket reset/edit/run cycle; explicit in the final project rubric.

**Out of scope by design:**
- Object-oriented programming (no `class` definitions). Defers to follow-on League courses.
- File I/O, networking, third-party packages. Trinket's sandbox doesn't support these and they would be a distraction at this level.
- Algorithm analysis, big-O. Premature for grade 6–8 first exposure.
- Software engineering practices (version control, testing frameworks, packaging). Defer to follow-on courses.

**Decision: proceed with the existing 25-lesson scope as the canonical Python introduction for the League middle-school track.** Convert the existing Sphinx course to Hugo without resequencing or rewriting lessons; the conversion's job is to change the publishing format and modernize the embed mechanism, not to redesign the curriculum, which is already field-proven.

## Course Structure Outline
## Course Structure Outline

**Total: 25 lessons + 1 final project, organized into 5 modules.**

### Module 0 — Turtles (8 lessons)
Goal: students can issue Python turtle commands and produce intentional drawings.

1. Meet Tina — the turtle object, `Turtle()`, `write()`
2. Moving — `forward`, `backward`, `left`, `right`, `penup`, `pendown`
3. Color — `color()`, named colors, RGB
4. Saying Hello — text output with `write()`, font arguments
5. Tina's Pen — pen size, pen state
6. Going in Circles — `circle()`, partial circles, dot
7. Tina's Grid — coordinates, `goto()`, `setheading()`
8. Tina's Secrets — reading the official turtle documentation, applying unfamiliar methods

### Module 1 — Remembering and Repeating (7 lessons)
Goal: students replace repetition with loops and name values with variables.

1. Variables, Loops, Lists overview — preview of the module
2. Variables — assignment, naming, reuse
3. Loops — `for x in range(...)`
4. Functions — `def`, parameters, calling
5. Crazy Shapes — loops driving turtle to draw geometric patterns
6. First Look at Lists — list literals, indexing, `len`
7. If and Else — `if`/`elif`/`else`, comparisons

### Module 2 — Function Practice (4 lessons)
Goal: students compose programs from small named pieces.

1. More Functions — parameters, return values, scope
2. Happy Pet — interactive program combining functions, loops, state
3. Obedient Turtle — wrapping turtle commands in user-defined functions
4. Houses — drawing complex composite shapes via function decomposition

### Module 3 — Lists, Strings, and Iterables (2 lessons)
Goal: students manipulate sequences and iterate over them.

1. More Lists — list methods (`append`, `pop`, slicing)
2. Yet More Lists — strings as iterables, `for letter in word`, combining lists and loops

### Final Project (open-ended capstone)
Required techniques: lists, tuples, `zip()` loops, `range()` loops, `if/else`, `input()`. Three example projects provided (Crazy Turtle Walk, Flaming Ninja Star, Yin Yang) but students may propose their own.

### Module-to-module dependencies
Strict linear order. Each module assumes everything in the previous module. The final project assumes all four modules.

### Per-lesson Hugo structure (Tier 3)
Every lesson page contains:
- Frontmatter: `title`, `weight`, `uid` (assigned by `curik scaffold`).
- Student content (rendered to site and extracted to README via `{{< readme-shared >}}` where applicable):
  - Brief motivating context (1–2 sentences).
  - Worked example as an embedded `{{< trinket >}}` runnable code block.
  - One or more "your turn" exercises, each with a `{{< trinket >}}` starter program.
  - Optional `{{< callout >}}` admonitions for tips and common mistakes.
- Instructor guide (hidden behind toggle, extracted to instructor README): pacing notes, expected pitfalls, discussion prompts, assessment cues. **Authoring of instructor-guide content is a follow-up task; the porter emits empty stubs.**

### Module landing pages
Each module's `_index.md` has a short overview paragraph, the module's learning goal, and Hugo automatically lists child lessons.

## Assessment Plan
## Assessment Plan

**Philosophy:** Assessment-for-learning, not high-stakes testing. Middle-school first-programming students need low-stakes, frequent feedback that supports motivation; ranked grading at this stage suppresses the experimentation the curriculum depends on.

### Formative (per lesson)
- **Embedded "your turn" exercises.** Every lesson has at least one exercise where the student modifies a working starter program. The Trinket embed is the assessment instrument: if the program runs and produces the requested change, the student has demonstrated the lesson objective. Self-check, no instructor grading required.
- **Instructor walkaround.** During in-person delivery, the instructor circulates and reviews student screens. The lesson's instructor-guide section lists what to look for (correct output, idiomatic code) and common mistakes to coach.
- **Reset button as safety net.** Students are explicitly encouraged to break the example, observe the error, and reset. Failing is a normal part of the loop, not a graded event.

### Summative (final project)
- **Required-techniques checklist** rather than a numeric rubric:
  - Uses at least one list.
  - Uses at least one tuple.
  - Uses at least one `range()` loop.
  - Uses at least one `zip()` loop or equivalent multi-sequence iteration.
  - Uses `if`/`else`.
  - Uses `input()` to take user input.
  - Produces a turtle drawing or interactive output of the student's design.
- **Demo-and-explain.** Student demonstrates the program to the instructor or class and explains one design choice ("why I used a list here"). This catches programs that meet the checklist mechanically but the student doesn't understand.
- **Portfolio piece.** The completed project is saved (Trinket account or screenshot + code paste) so the student leaves the course with something they can show.

### Non-graded indicators the instructor monitors
- Engagement: are students experimenting beyond the prompt?
- Recovery: when something breaks, do students try to debug before asking?
- Vocabulary: are students using terms (`function`, `loop`, `variable`, `argument`) correctly when they ask questions?

### What we deliberately do not assess
- Speed or memorization of syntax. Students may consult the lesson page or Python turtle docs at any time.
- Code style, beyond "your variable names should mean something."
- Algorithmic efficiency. Out of scope at this level.

### Reporting
At end of course, instructor produces a one-paragraph narrative per student covering: what they built, what concepts they demonstrated mastery of, and what to focus on in the follow-on intermediate course. No letter grade.

## Technical Decisions
## Technical Decisions

### Publishing platform
- **Hugo static site** with the `curriculum-hugo-theme` (managed by Curik, lives in `themes/`, treated as read-only).
- Site output is plain HTML/CSS/JS — no server-side runtime, deployable to any static host.
- Markdown dialect: Goldmark with `unsafe = true` (required so the Trinket shortcode can emit raw `<iframe>` HTML).

### Runtime
- **Trinket.io** embedded Python via iframe (`https://trinket.io/tools/1.0/jekyll/embed/python#code=<urlencoded>`).
- No local Python required for students.
- Optional free Trinket account if students want to save modified programs across sessions.
- Trade-off: Trinket runs Skulpt-based Python, which is mostly Python 3 but missing some standard-library modules. Acceptable for the scope of this course (turtle, basic builtins, lists, strings).

### Trinket embed mechanism (project-level shortcode)
- New file: `layouts/shortcodes/trinket.html` (project-level; **does not modify the theme**).
- Mirrors the iframe-generation logic in `docs/source/preprocess.py`:
  - Default width: 700px.
  - Default height: `(line_count * 17) + 110` if not specified.
  - URL-encodes the inner code with Hugo's `urlquery`.
  - Wraps iframe in `<div class="iframe-container">`.
- May be upstreamed to the curik theme package later; project-level placement lets us ship now without an upstream release.

### Markdown source format
- Each lesson is a Hugo content file at `content/<NN-module>/<NN-lesson>.md`.
- Frontmatter: `title`, `weight`, `uid` (Curik-assigned).
- Body uses standard Goldmark Markdown plus theme/project shortcodes:
  - `{{< trinket >}}` for runnable Python (project shortcode).
  - `{{< callout type="info|warning|tip" >}}` for admonitions (theme shortcode).
  - `{{< instructor-guide >}}` for instructor-only content (theme shortcode).
  - `{{< readme-shared >}}` / `{{< readme-only >}}` for README extraction (theme shortcodes).

### Sphinx → Hugo migration tooling
- One-shot script: `scripts/port_sphinx_to_hugo.py`.
- Reads `docs/source/**/*.md` (Sphinx + MyST) and writes the body region of the corresponding scaffolded Hugo lesson.
- Conversions: ` ```python.run ` fences → `{{< trinket >}}`; MyST `:::{note|warning|tip}` admonitions → `{{< callout >}}`; MyST `{toctree}` directives stripped (Hugo handles section indexes); image references rewritten to `/images/...`.
- Idempotent: bounded by `<!-- curik:body:start -->` / `<!-- curik:body:end -->` sentinels so re-running preserves manually authored instructor-guide content.
- Disposable: not part of the deployed site, lives in `scripts/` for one-time use plus occasional re-runs while migrating.

### Assets
- Images: copy `docs/source/images/*` → `static/images/` so they are served at `/images/...`.
- No JavaScript or CSS customizations beyond the theme.

### Hugo build & deploy
- `curik hugo build` produces `public/`.
- Deploy target: TBD (likely League's existing static-site host); not blocking for this conversion.
- Versioning: `curik hugo bump-version` updates the curriculum version stamp in `hugo.toml` for releases.

### Validation
- `curik validate course` — schema/structure checks on Hugo content.
- `curik syllabus validate` — checks `course.yml` lesson list matches `content/`.
- Manual: spot-check at least one Trinket-heavy lesson in `hugo server` and confirm the embedded program runs.

### Things deliberately out of scope for the conversion
- No theme modifications. The theme is upstream-managed; project-level shortcodes only.
- No content rewrites. The existing 25 lessons are field-proven; the porter preserves their text.
- No new lessons. Adding lessons is a separate Phase 2+ concern.
- No instructor-guide authoring. Stubs only; content authoring is a follow-up project.
