# Delivery log

One entry per session, written after it from the lecturer's notes: what was
planned, what happened, where the flow broke, where the room got stuck, and
what was changed in response. Read the entries of a lecture before reworking
it. No student names in this file: the repository is public.

Each entry has the same four parts.

- **Planned:** the deck, the seminar page and the plan that was meant to run.
- **What happened:** the lecturer's notes, as given.
- **Changed in response:** what was edited, with the date.
- **Open:** what is known to be wrong and not yet fixed.

## 2026-09-29 · Lecture 2 and Seminar 1

**Planned**

- Lecture 02 Introduction to Data on its 90-minute plan.
- Seminar 1 as a follow-along page: install VS Code, build the project
  folder, write the README in Markdown, look at `D0_KPi.csv`, record its
  provenance.

**What happened** (lecturer's notes of 4 October)

- The seminar left the page. Markdown and the project structure were taught
  off-hand, and as taught they did not make much sense. The flow was not good.
- Multi-line editing was shown without prepared examples or exercises.
- The lecture was a bit dry and sloppy.
- The multiple-choice slides felt out of place.
- The folder built on the projector differs from the page: `Project/` with
  `Data`, `Results`, `figures` and `scripts`, a `README.md`, a `report.md`
  with headings, lists, a table, a link and a picture, a Marp deck exported
  to PDF, a `plot.py`, and a hand-typed `data.csv`.
- Not recorded: how far the data-file and provenance part of the seminar got.

**Changed in response** (4 October)

- Lecture 02 has a closing section, Markdown & Text Editing, 17 slides: the
  project folder and its names, Markdown as source and preview, and one small
  table repaired in the editor with Find and Replace, whole-line keys, a
  cursor on every line and selected matches. Every key was checked against
  the VS Code key sheets for Windows, macOS and Linux.
- Slide 8 of Lecture 02 gives the ISO/IEC 2382 definition of data.
- Seminar 1 has a new Part 3, Edit many lines at once, with the same table as
  the slides, and its example files in `lectures/workbook/docs/data/`.
- The quiz slides left the flow of Lecture 02. Their questions are also on
  the workbook page of the lecture under *Check yourself*.
- Eight other slides of Lecture 02, all from the skip list of its 90-minute
  plan, are parked in `lectures/content/parked/`. The deck went from 59
  slides and 122 min to 62 lecture slides and 120 min.
- Lecture 03 uses Lithuanian letters for its encoding examples, has a slide
  on the encoding and line ending in the Status Bar of VS Code, shows the
  hexdump of the table from Lecture 02, and no longer points to seminars or
  to other lectures.
- Seminar 3 is rewritten as a follow-along page: three terminal commands,
  then files measured and opened as bytes. The old brief needed `hexdump`,
  `tr`, `wc` and `git commit`.
- The workbook pages of Lectures 2 and 3 have a 90-minute plan with the
  current slide numbers.
- After a second note from the lecturer (the in-line quizzes are skipped
  through; they could stand at the end for self-reflection; fill the time
  with coherent, textbook-like content): Lectures 1 to 3 close with a
  self-check section that holds their quiz slides, and no quiz interrupts a
  lecture. Lecture 03 got eight derivation slides in the freed time: bits
  and counts, converting between bases, two's complement by weights, why 0.1
  is not exact, the steps between floats, how UTF-8 packs a code point, one
  number as text and as binary, a checksum by hand.

**Open**

- Lecture 02 is still mostly text cards. It shows no real data before its
  last third, and the CERN case study stands apart from the example file.
- Lecture 03 has titles in the older style.

## 2026-10-04 · The rest of the course reworked

Not a session: a rework asked for by the lecturer after the notes above.

**What the lecturer asked for**

- Start from the very basics, then build rigorously: data fitting from first
  principles, a perceptron built step by step.
- Some of the content came from a simple language model: expand, restructure,
  add.
- Too much material is better than too little.
- Get each lecture right now, so that later weeks need fewer iterations.

**Changed in response**

- The decks are renumbered into the order they are given: 04 command line,
  05 Git, 06 Python foundations, 07 Python for data and NumPy,
  08 visualisation, 09 probability and statistics, 10 fitting from first
  principles, 11 the perceptron (new), 12 Pandas and data cleaning,
  13 reproducible workflows. 14 to 16 are further topics. The former
  Lecture 05 on Markdown and VS Code is parked: week 2 teaches it.
- Lectures 04 to 16, their seminar pages and their lecture pages were
  reworked to one brief,
  `docs/superpowers/specs/2026-10-04-course-rework-first-principles-design.md`.
- Two examples run through the course: the pendulum table (cleaned by hand in
  week 2, read as bytes in week 3, plotted, fitted for g, cleaned by script)
  and the LHCb file.
- On Windows the terminal from Lecture 04 on is Git Bash inside VS Code.

**Open**

- Nothing was run on a Windows laptop. Before each lecture from 04 on, try
  its seminar page once in Git Bash: the terminal profile, `python` against
  `py`, line endings in scripts, checksums, `sort -n` under a Lithuanian
  locale.
- Runnable code slides of Lectures 09, 10, 13 and 16 ran in ordinary Python,
  not all of them in the browser runner.
- Lecture 15's timings with 8 and 12 workers were taken on a loaded machine.
- Every reworked deck sits at 126 to 144 min. Each needs the skip list on its
  lecture page for a 90-minute slot.
- Lecture 02's first two thirds are still mostly text cards.

## 2026-10-06 · Lecture 2 (closing section), Lecture 3 and Seminar 3

**Planned**

- Lecture 02, slides 45 to 61, shown live in VS Code, then Part 3 of
  Seminar 1 with the room.
- Lecture 03 on its 90-minute plan.
- Seminar 3, as far as time allows. Part 1 and Part 2 come first.
- The room's folders are renamed to the layout of the slides before Part 3:
  `Data` to `data` with `raw` and `processed` inside, `Results` to `results`.

**What happened**

**Changed in response**

**Open**
