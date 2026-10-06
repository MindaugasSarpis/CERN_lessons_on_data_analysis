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

**What happened** (lecturer's notes of 6 October)

- The order was Lecture 03 first, then the closing section of Lecture 02,
  then Seminar 3.
- Lecture 03 went fine. It filled the time and was not too easy. It stopped
  a couple of slides before the end.
- The closing section of Lecture 02, slides 45 to 61, was shown. Part 3 of
  Seminar 1, the editing exercise, was not done with the room.
- Seminar 3 was hectic again. The page had a lot of material, and on opening
  it it was not clear at once what to do. The session became four terminal
  commands, `pwd`, `ls`, `cd` and `clear`, for two hours. None of the byte
  part was done, and the README got no **File anatomy** section.
- It could have been more coherent: the terminal, the shell and the prompt
  had not been introduced properly before the room used them.
- Students do not do homework. Anything set for home does not happen.

**Changed in response** (6 and 7 October)

- **Seminar pages, all of them.** A page opens on a **run sheet**: the goal,
  then one row per section with what is shown on the projector and what the
  room ends with. How to use the page, what to prepare and the files sit in
  collapsed boxes below it. Every line the room types stands in its own
  block, macOS and Windows variants are in tabs (macOS first), and a rule
  separates the sections. The layout is written down in
  `docs/seminar-page-recipe.md`, with Seminar 3 as the example.
- **No homework anywhere.** Every "at home" step is gone. What did not fit is
  an optional section done in class if the room is fast, or a stretch goal.
  Installing Python, Git and PowerShell 7 moved into Part 1 of Seminar 4; the
  install page is now its in-class reference. Seminars 5 to 16 were checked
  for anything they assumed from homework.
- **No Git Bash.** The terminal is `zsh` on macOS and PowerShell 7 on
  Windows. Lecture 04 shows every command in both, side by side, each output
  taken from a real run in both shells (Windows PowerShell 7.6.6 on a Windows
  laptop). The Unix-only text chain of Lecture 04 (the `cut | tr | uniq`
  histogram, the cleaning in one line, the `bash` loops) is parked in
  `lectures/content/parked/04_Command_Line_and_Files.md`. The cleaning is now
  a handed-out program, `scripts/clean_pendulum.py`, which writes the same
  97 bytes on every system. Lectures 05 to 16 and their seminar pages follow
  the same convention.
- **Lecture 04** names what Seminar 3 typed without naming: a new slide
  *Read the Prompt* (PowerShell 5.1, PowerShell 7, zsh, Python's `>>>`). It
  opens on four copies of the cleaned table (96, 97, 105, 107 bytes) and
  closes by naming the right one in the README by size and SHA-256. It also
  rebuilds a checksum by hand, in case the end of Lecture 03 was not seen.
  141 min.
- **Seminar 3** works in VS Code and the Hex Editor alone: no terminal before
  Lecture 04 has named its parts. Its byte part, which did not happen this
  year, is Part 3 of Seminar 4, measured by command.
- **Seminar 4** is rewritten around Lecture 04: tools installed, the shell
  named, a file as bytes, the data file by command, the program, its
  checksum and the README.
- **Storytelling, after the note that Lecture 03 works and Lectures 01–02 do
  not as well.** An audit took a rubric from Lecture 03 (an object first,
  small steps, every rule worked out with real numbers, one surprise per
  section, the end answering the start) and checked Lectures 01 to 13
  against it. A second review corrected the audit. In response:
  - Lecture 01 opens on the pendulum table: two people, 9.80 and 9.84, and
    "I send you only 9.84; how do you check it?". The four aims answer it,
    and the closing slide answers it again. The reel and the clips are
    unchanged.
  - Lecture 02 opens on four lines of `D0_KPi.csv` with no note and five
    questions the file does not answer; the lecture answers them and closes
    on the file, annotated. The clips are unchanged, and the Markdown section
    stays as it was.
  - Lecture 03: small fixes only (the source of 1880.649, `1` = 0x31 against
    `2` = 0x32 on the ASCII table, the real hash of `pendulum.csv`, no
    terminal before Lecture 04).
  - Lectures 05 to 13 open on what the week before really delivered and
    close on an answered result; every section slide carries one line that
    links back. Lecture 05's Git outputs were regenerated from a folder in
    the state Seminar 4 leaves (`misc/l05_scratch_repo/build.sh`).
- `docs/superpowers/specs/2026-10-04-course-rework-first-principles-design.md`
  and `CLAUDE.md` record the terminal convention and the no-homework rule.

**Open**

- Which slides at the end of Lecture 03 were not reached.
- Part 3 of Seminar 1 (edit many lines at once) has not been done with the
  room. Seminar 4 starts by bringing every folder up to date, including the
  README line about the four edits.
- Nothing was run on a real Mac: the macOS outputs were made on Linux and
  adapted (for example the padding of `wc`). Try Lecture 04 and Seminar 4 on
  a Mac once before 13 October.
- `winget install Microsoft.PowerShell` and the python.org installers were
  not run on a student laptop. How VS Code names the PowerShell 7 profile was
  read from its code, not seen.
- The VS Code screenshots of Lecture 05 (`git_vscode_*.png`) show the folder
  before Seminar 4 and need to be taken again.
- The L01 figures for contact and self-study hours (64 h, 196 h) are for a
  10-credit course; the physics course has about 76 h of self-study. To be
  set from the course description.
- Lecture 01 has no entry in this log for 8 September.
