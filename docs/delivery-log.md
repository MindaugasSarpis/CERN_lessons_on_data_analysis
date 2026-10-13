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

## 2026-10-11 · Lecture 04, Seminar 4 and the editor slides of Lectures 02 and 03

Not a session: a rework asked for by the lecturer before 13 October.

**What the lecturer asked for**

- Lecture 04 and Seminar 4 self-contained: no reliance on what an earlier
  seminar did or did not do, and the seminar after the lecture, in its order.
- What the seminars do in Markdown, in the editor and in the terminal laid
  out in the lectures first (Lectures 01 to 04).
- Lecture 04 checked for coherence, and package managers and environments
  introduced thoroughly.

**Changed in response** (11 October)

- Lecture 04 names the terminal, the shell and the prompt from zero; the
  nine references to Seminar 3 as a terminal session are gone, and so are
  the room-state notes ("most Windows laptops have no Python yet").
- Lecture 04 has a seventh section, *Tools & Environments*, 11 slides between
  *Programs Someone Else Wrote* and *Checksums & Backups*: where a program
  comes from, the `PATH` list (which explains `Python was not found` by the
  stand-in in `WindowsApps`), a package manager and its five jobs, PowerShell
  7 installed by `winget`, pip, `pip install numpy` measured (16.7 MB wheel,
  43 MB unpacked), one shared Python breaking a project (`np.float_` removed
  in NumPy 2.0), a virtual environment measured (14 MB, 891 files), the
  empty environment filled, and `requirements.txt`. The README's *How to
  rebuild* names the Python and the three environment lines. Two quizzes
  were added. Lecture 13 keeps its deeper treatment and was not changed.
- Five slides left Lecture 04 for `parked/`: *A Path That Fails*, *One
  Pattern, Two Shells*, *Wildcards Are Not Regular Expressions*, *A Pattern
  on Another Laptop* and *A Checksum by Hand* (which Lecture 03 has). The
  deck estimates 156 min, over the 145 band; the lecture page's 90-minute
  plan skips most of the new section's detail and keeps `PATH`, the virtual
  environment and `requirements.txt`.
- Lecture 02 has three slides on VS Code before *Markdown*: the editor and
  opening the folder, the five regions of the window and the Command
  Palette, files and saving in the Side Bar. Lecture 03 has one slide on
  installing an extension, the Hex Editor, before *Reading a Hexdump*. Both
  were the gaps between Seminars 1 and 3 and the lectures before them.
- Seminar 4 follows the lecture's order: tools, the shell named, the data
  file by command, then a program, a checksum, a new section 13 that makes
  the project's environment (`python -m venv .venv`, `pip install numpy`,
  `pip freeze`), and the README with the environment lines. The bytes
  exercise of the old Part 3 is optional section 16. Links from Seminars 3,
  7 and 15 were renumbered.
- Lecture 01's hours are 52 h contact and 78 h self-study (13 sessions of
  4 h; 130 h for the 5-credit elective), from the lecturer's note.

**Open**

- Not run on a Mac or on a Windows laptop: the `which python3` and
  `Get-Command` paths, the `PATH` listings and the `winget` output of the new
  slides are the installers' defaults and winget's documented lines. Run
  them once before 13 October and correct the slides. The pip and venv
  outputs were measured on Linux with Python 3.14.8 (pip 26.2.1, numpy
  2.5.4); a python.org Python may bundle another pip.
- Seminar 4 leaves `.venv/` and `requirements.txt` in every project folder.
  Seminar 5's `.gitignore` and Seminar 7's `pip install numpy` (global) do
  not know about them yet.
- The spec's Lecture 04 paragraph still says Git Bash and does not mention
  the tools section; an amendment line was added below it.


## 2026-10-12 · Lectures 01 to 04 and Seminars 1, 3 and 4, for teaching

Not a session: a rework asked for by the lecturer the day before Lecture 04.

**What the lecturer asked for**

- Lecture 04 introduces the command line thoroughly, one step at a time,
  including getting zsh on a Mac and the newest PowerShell on Windows.
- The pendulum table and the LHCb file were never introduced in class, and
  the D⁰ file adds overhead and makes the course look particle-physics
  specific: generic examples instead, with clear storytelling and flow.
- "I like the content but if I present it as is it will be very confusing
  and complicated": there is a lot of text to orient in quickly.
- Seminar 4 starts again from scratch: the room has seen a little Markdown
  and four commands (`pwd`, `ls`, `cd`, `clear`). The seminar's ideas are
  introduced in the lecture, but not its files or data. Up to 2 h, runnable
  from the page without much preparation.
- The same for Lectures 01 to 03 and Seminars 1 and 3. The lecturer asked
  whether the flow VS Code → Markdown → simple command line with files →
  advanced command line → Git → Python is reasonable; it is the order of
  Lectures and Seminars 02, 03, 04, 05 and 06.

**Changed in response** (12 October)

- **One generic example for Lectures 01 to 04**: a made-up weather station,
  generated by `weather_files.py` and labelled as generated: an hourly log
  of 2016 to 2025 (87 672 rows, `time,temp_c,humidity_pct,wind_ms`, the
  thermometer down for 120 hours in July 2019 and written as `-999`) and a
  spreadsheet export of nine daily means (`;`, decimal comma, a column `nr`,
  a mean line). The coldest hour of ten years, −999 °C, is the turn of
  Lecture 04; counted as a number it moves the ten-year mean from 7.16 to
  5.78 °C.
- **Seminars use files of their own**, each generated by a seeded script:
  Seminar 1 a reading list and a library's loans log (`books_*`), Seminar 3
  a folder of seven short files (`inbox_*`), Seminar 4 two bicycle
  counters, 2024–2025 (`bikes_*`, the mark `9999` for one broken week).
- **Slides for teaching**: one step per slide, about 40 words of prose at
  most, the detail moved into the speaker notes, and every note in one form:
  **Do**, **Say**, **Ask**, **If asked**, minutes.
- **Lecture 04** was rewritten: a section *Set Up the Shell* (terminal,
  shell and program; `echo $SHELL` and `chsh -s /bin/zsh` on macOS; the two
  PowerShells, `winget install --id Microsoft.PowerShell`, 7.6.6 of
  8 September 2026; the terminal of VS Code and its default profile), then
  *First Commands* one per slide (`echo`, `pwd`, `ls`, `cd`, paths, the
  parts of a command, spaces, `Tab`, history, help, errors), then the
  sections it had. The notes on Windows PowerShell 5.1 went. 86 lecture
  slides and 10 quizzes, 151 min estimated; the lecture page's plan takes
  91 min and keeps every idea the core of Seminar 4 uses.
- **Seminar 4** was rewritten from scratch in the lecture's order:
  installs, the terminal of VS Code, a project folder built with `mkdir`,
  the files read and counted, `9999` found at an end of a sorted column,
  168 marked rows, a clean copy, `clean_export.py` and `column_stats.py`,
  one checksum in the room, the README, `git config`. Core 1 h 42 min;
  bytes, regular expressions, a virtual environment, a checksum list and a
  test of the README are optional.
- **Lecture 01** opens on the weather log (two people, two means of the
  same file, seven numbers) instead of the pendulum, and its course map
  follows the flow above. Three slides were parked.
- **Lecture 02** asks its five questions of the weather log, has the export
  repaired by hand in the editor (180 bytes to 148), keeps CERN as two
  short real examples (record 401, the trigger), and parks the experiment
  slides and their clips. **Seminar 1** repairs its own reading list and
  reads a library's loans log; core 1 h 41 min.
- **Lecture 03** keeps its topics and derivations on weather values (9.4 as
  a float32, −16.3 as text and as binary, a row as 29 bytes of text or 16
  of binary, the 148 bytes of the cleaned table counted in the hexdump) and
  gains a section on the terminal, slides 76–87: terminal and shell, the
  terminal of VS Code, the prompt, `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`,
  `rm`, a file's size and its bytes, in forms that run in zsh and in both
  Windows PowerShells. 142 min estimated. **Seminar 3** is rewritten as
  "Files and Bytes from the Terminal": a folder of seven generated files
  (`inbox_*`), each hiding one thing (a space in a name, CRLF, Windows-1257,
  a picture under a `.txt` name, two files of equal size and different
  checksum); core about 105 min.
- The handed-out scripts are generic: `clean_export.py` cleans any such
  export, `column_stats.py` takes any file and column.
- After a further note ("S4 such that it rigorously introduces (revisits
  the concepts) from S1-S3 … so now maybe the files should be minimal"),
  Seminar 4 opens with a 42-minute warm-up from an empty folder while the
  installs run: VS Code region by region, terminal, shell and prompt, the
  project folder by `mkdir`, a README in Markdown, the switch to PowerShell
  7, and `counts.csv` typed from the page (three lines, 35 characters, 39
  bytes with LF, 42 with CRLF, `ž` as `c5 be`). The core needs two
  downloads, `bikes.csv` and `column_stats.py`; the cleaning of the export
  is optional. Core 1 h 43 min. Handing out files by `git clone` and
  `git pull` fits from Seminar 5 on, from a small repository of its own:
  this repository is 328 MB packed.
- After a further note ("I will follow the slides during lecture, not
  showcase a file, I will showcase something during seminar"; "the slides
  should be self contained and not mention a specific file, the seminars
  can mention specific files"): the "made up / generated for the course"
  labels left the slides, the lecture pages and the handed-out READMEs,
  and no slide or note of Lectures 01 to 04 asks to open, type or install
  anything beside the deck. Example names and paths stay where the slide
  shows everything; the provenance of the weather log is told in the
  story (the station's operator, by e-mail, CC0). Lecture 04 gains three
  slides on the shell's own settings (an alias and a prompt, `~/.zshrc`
  and `$PROFILE`, Oh My Zsh with Oh My Posh and Starship), 73 to 75, in the
  90-minute skip list. Seminar 4 gains, in section 7, a two-line script
  that runs on a Mac with LF and stops with `bad interpreter:
  /bin/zsh^M` once saved with CRLF (warm-up now 49 min, core 1 h 50 min),
  and an optional section 23 that writes the same settings into the
  start-up files and shows Oh My Zsh or Oh My Posh.
- After "we want to rigorously introduce what conda environments are and no
  venv" (and the choice "Miniforge only"): Python on the students' laptops
  comes from Miniforge 26.7.2 (conda plus Python, conda-forge only), not
  python.org. Lecture 04's Tools & Environments section is rebuilt: the
  shell-settings slides come first, then what `conda init` wrote, conda as
  package and environment manager, one shared Python against one
  environment per project, an environment as a folder (`conda create`,
  `conda env list`), activation as a change of `PATH`, `conda install
  numpy` measured, and `environment.yml` from `conda env export
  --from-history`. The pip, venv and `requirements.txt` slides left.
  Seminar 4 installs Miniforge in sections 1 and 13 (the macOS installer's
  "Proceed with initialization?" defaults to no; Windows needs `conda init
  powershell` in the Miniforge Prompt; winget's Miniforge3 package is from
  2022) and builds a conda environment `bikes` in optional section 20. A
  prompt line of one's own hides conda's environment name unless it keeps
  `$env:CONDA_PROMPT_MODIFIER` (PowerShell loads conda's `profile.ps1`
  before `$PROFILE`).
- After "carefully check for readability, clarity, flow … implement":
  Lectures 01 to 04, their pages and Seminars 1, 3 and 4 were read slide by
  slide and section by section, and fixed in place (notes, bridges,
  arithmetic, run-sheet sums, Watch-for rows).

- **Slide text, at the lecturer's request (12 October, evening).** "One
  Row, Four Values" and "Three Questions" were called empty slogans that add
  no meaning; "Terminal, Shell, Program" over the cards Terminal, Shell and
  Program was called repeated; "This course uses PowerShell 7. The next
  slide installs it…" was called something said in words; "don't need to
  say what's on the next slides". Section slides stay, as pauses for
  questions, and titles that state the step ("Read the Prompt", "Where Am I:
  `pwd`") stay. In Lecture 04 every slogan title was rewritten or removed
  (three slides now have no title), every forward reference and narration
  line went from slides and notes, and section subtitles no longer list the
  next slides. Seminar 4's headings say what each section does, with the
  same anchors. The rule is CLAUDE.md convention 15 and the project skill
  `.claude/skills/writing-lecture-slides`.
- **Lecture 04 content (12 October, evening).** Reviewed for coherence: a
  first shell script, which the course spec lists after Lecture 04, was
  missing, and the checksum section opened on 148 against 158 bytes from
  sixteen slides earlier. Now: the five install slides are two (macOS: check
  the shell, with what a variable is; Windows: install PowerShell 7);
  slide 8 defines terminal, shell and program precisely; *Checksums &
  Backups* comes before *Tools & Environments*; two slides on a first shell
  script close the README section (`#!/bin/zsh`, `chmod +x`, `./`, and
  stopping at the first error: `set -e`, and in PowerShell both
  `$ErrorActionPreference = 'Stop'` and
  `$PSNativeCommandUseErrorActionPreference = $true`, because `Stop` alone
  does not stop at a failing `python`); one quiz on `$?`. Slide 4 links
  `weather_project.zip`. Five slides have a `**Live:**` moment (Tab and
  history, the line count, line 5000, the pipe built filter by filter, the
  rebuild script; the checksum check optional), listed with setup on the
  lecture page. The deck is 101 slides, 158 min by the timing model, 177 by
  the notes; the 90-minute plan ends at 1:31.

**Open**

- The script outputs of Lecture 04 slides 85 and 86 ran in zsh 5.9.2 and
  PowerShell 7.6.6 on Linux; the Windows paths in them are shortened by
  hand. Every deck, 01 to 16, was then swept the same way with the
  skill (slogan titles rewritten, titles that repeated their boxes removed,
  "By the end of this lecture" lead-ins, narration and forward references
  gone; no slide added or removed). Seminar pages other than Seminar 4 are
  not swept yet.
- Not run on a Mac or a Windows laptop: in Lecture 04 the `chsh` dialogue,
  the `winget` output, PowerShell's `ls` table, the `which` and
  `Get-Command` paths and the `PATH` listings; macOS formats of `wc` and
  `uniq -c` and the Windows CRLF sizes were written from the rules. All
  other outputs were run in zsh 5.9 and PowerShell 7.6.6 on Linux. The
  same holds for Seminars 1, 3 and 4 (listed on their pages' worker notes:
  VS Code counters and keys not tried on real laptops).
- Not run on a Mac or Windows either: the Oh My Zsh install and
  `uninstall_oh_my_zsh`, Oh My Posh by `winget` and its profile line, and
  the `$PROFILE` path on Windows. The zsh and PowerShell lines of Seminar 4
  section 23 and the `bad interpreter` message ran in zsh 5.9.2 and
  PowerShell 7.6.6 on Linux.
- Not run on a Mac or Windows: the Miniforge installers' screens, every
  macOS and Windows path in the conda outputs (`/Users/ada/miniforge3/…`,
  `C:\Users\ada\miniforge3\…`), `conda init powershell` writing
  `profile.ps1` for both PowerShells (read from conda's source). The conda
  commands, versions, sizes and package counts ran with Miniforge 26.7.2 on
  Linux.
- Later seminars still install packages with pip into whichever Python is
  active, which is now conda's `base`: Seminar 7 (numpy), 10 (scipy), 11
  (matplotlib), 12 (pandas, pyarrow), 16 (scikit-learn); Seminars 7 and 12
  also point to python.org in a Watch-for row. Lecture and Seminar 13 and
  lines of 14 and 15 use venv and `requirements.txt`, and `overview.md`
  lists `requirements.txt` in the project layout. Each becomes a conda
  environment with `environment.yml` at its rework.
- Lectures 05 to 16 and Seminars 5 to 16 still use the pendulum table and
  the LHCb file, and some assume files that Seminar 4 no longer makes
  (Seminar 5: checksums of `D0_KPi.csv`; Seminar 6 and Lecture 6:
  `scripts/clean_pendulum.py`; Seminar 7: `D0_valid.csv`). Rework each the
  same way before its week, Seminar 5 first (20 October).

## 2026-10-13 · Seminar 4, before its session

**Lecturer's notes**

- "The S4 doesn't make much sense"; "have some steps, some tasks to
  actually do"; "if we need to have something installed for the seminar
  we will do it at the start of that seminar. They are a bit tricky to
  read."

**Changed in response** (13 October)

- Seminar 4 is one story with one file: how many bicycles pass in an hour?
  Part 1 installs PowerShell 7, Git and Miniforge first, in the system's
  terminal with VS Code closed, so VS Code finds them when it starts (no
  restart mid-session); then the prompt, the project folder, the README's
  start. Part 2 gets the file and checks it (checksum first, then lines,
  bytes, a hex view of the first 80 bytes). Part 3 finds the `9999` week
  and writes `bikes_valid.csv`. Part 4 gives the answer (86.3 against
  38.6). Part 5 writes `rebuild.sh` / `rebuild.ps1`, breaks a CRLF copy on
  a Mac, and finishes the README. Every part ends with a **Task** for the
  room alone, the answer folded under it (two paths; line ends and the
  file size; a line number and the empty hours; each counter's mean, 49.6
  and 27.4; the script extended to make those files).
- Out: `counts.csv` and its two "places", the backup drill, `hello.sh`,
  `git config` (Seminar 5, section 1 sets it). Optional section 22 is now
  *Stop the script at the first error* (`set -e`, the two PowerShell
  lines). `bikes_files.py` writes the new README and a zip with both
  scripts and `results/bikes_stats.txt`.

**Open**

- The other seminar pages still install or assume things mid-session;
  lay each out the same way (installs at its start, one question, tasks)
  when it is reworked.

## 2026-10-13 · End of Lecture 3, Lecture 4 and Seminar 4

**Planned**

- The rest of Lecture 03 (numbers in computers), Lecture 04 on its plan,
  then Seminar 4 as rewritten the same morning.

**What happened** (lecturer's notes of 13 October)

- "Started from L3 how numbers work in computers, it was not bad but then
  towards the end, the mathematical computations with binary, the hex I
  just skipped through."
- "Then L4 was more like a seminar, not a bad thing, but wasn't very
  coherent. Towards the end content got too complicated and we ended up
  finishing quicker."
- "Then tried following the seminar, but it wasn't great. Too much text, the
  steps are not clear, too many boxes 'what to skip'. Would like a really
  coherent step by step seminar. But filling the 2 hours. Now the content
  just wasn't there."
- The file download did not work from the long workbook link; a TinyURL was
  used.
- Later the same day: "the seminars should be very neatly laid out and the
  steps should be short and coherent, I don't have the time to read long
  descriptions between the steps and orient myself"; "The seminars I want
  to have up on iPad and show on my Mac live, even without too much
  preparation. One step at a time"; "I have a problem with Mac and Windows
  PS diverging in what they can do in CLI"; "we want to introduce how
  packages and package managers work in terminal".

**Decided** (13 October, by the lecturer)

- One project for lectures and seminars, the weather station.
- From Seminar 5 on, files come by Git: the room clones a small public
  repository, not the course repository.
- One family of shell for the course: zsh on macOS, Git Bash on Windows,
  with the same Unix commands (first chosen as PowerShell 7 on both by a
  misread question, converted the same evening).
- Lecture 05 runs one straight line; pull requests, review, SSH, stash and
  line endings are parked.
- Seminar steps are typed in the terminal while the Source Control view
  shows them (no click-then-type doubling).

**Changed in response** (13 October)

- `docs/seminar-page-recipe.md` rewritten: one question, installs first,
  short steps (instruction, typed line, output), one **Check:** line per
  section, one Task per part, almost no boxes; Seminar 5 is the model.
- The workbook has a **▶ Steps** button on seminar pages
  (`javascripts/steps.js`): one step at a time, full screen, arrows or
  swipe, the place remembered; it also draws the pages' Mermaid diagrams.
- `misc/weather_repo/build.sh` builds
  [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project),
  published the same day: the weather project with seven commits by Smiltė
  and Tomas, about 0.5 MB to clone. Tomas's commit `2cca38a` makes the mean
  read the raw file and writes 5.78 into the README.
- Seminar 5 rewritten as "Who changed the mean?": clone, `git log`,
  `git blame`, `git show`, `git revert`, the rebuild, `.gitignore`, a commit
  of one's own, GitHub, push and pull; branch, conflict and tag optional.
  Every output from a run in zsh 5.9 and bash with Git 2.56 on Linux.

- **Lecture 03** (143 to 132 min): six drill slides of the numbers part
  parked (conversions, bitwise operations, 5.75 and 0.1 as float32); hex
  now arrives as the short way to write the first bytes of `weather.csv`,
  binary addition is an hour count 7 + 1, and −16.3 is worked out as a
  float32 (`C1 82 66 66`). Two's complement unchanged. The terminal section
  is in zsh and Git Bash.
- **Lecture 02** (112 to 109 min): `weather.csv` is on the screen from
  slide 1 and read from slide 13 (was 34); text cards became tables; the
  CERN example is now an ATLAS open-data file (record 328) set beside
  `weather.csv`, with its own `-999` marks counted from the real file.
- **Lecture 01**: wording only (slogans and narration out, notes in the
  one form).
- **Lecture 04** (158 to 128 min): one question, "is 7.16 right?", in
  eight steps, each section ending on a number or a file; zsh and Git
  Bash, one line for both; the commands Lecture 03 taught are one recap slide; a full section
  on programs, packages and package managers (Homebrew, `winget`, conda
  environments, `environment.yml`); the shell-settings slides (aliases,
  start-up files, Oh My Zsh, `conda init`) and 40 more parked; the quizzes
  at the end.
- **Lecture 05** (142 to 136 min): the weather project put under Git by
  Smiltė and cloned by Tomas; one straight line from two copies of the
  export to a tag; Mermaid diagrams of a commit's objects, the graph, the
  three areas and merges; new VS Code screenshots; pull requests, review,
  SSH, stash and line endings parked; the quizzes at the end.
- **Seminars 1, 3, 4 and 6 to 16** rewritten in the layout of Seminar 5,
  each one question about the weather project. Seminar 4 installs Git
  (with Git Bash) and Miniforge with Homebrew or `winget` and shows `grep`
  and `find` in depth. Seminars 1 to 4 hand out
  zips from the Releases page of `weather-project`
  (`weather_seminar_files.py`); later seminars pull course commits
  (`misc/weather_repo/files/`, `STAGE=N` in `build.sh`). The install page,
  the overview, the nav and the paired-seminar paragraphs of the lecture
  pages follow.

**Open**

- Not run on a Mac or Windows: VS Code's Publish Branch and sign-in
  dialogs, the Source Control Graph, Homebrew's and `winget`'s screens,
  conda paths under Homebrew, timings of Seminar 15 (measured on a
  128-core Linux node).
- Push the course commit of each later seminar after the one before it
  ran (`STAGE=6 bash misc/weather_repo/build.sh`, then a normal push),
  never before Seminar 5: its page prints the seven commits.
- Lecture 02 now uses an ATLAS file of simulated events (record 328) for
  its CERN example: to be confirmed by the lecturer.
- Lecture 01 says 64 h in class (16 sessions of 4 h); the schedule slide
  lists 13 Tuesdays.
- Lectures 06 to 16 still use the pendulum and the LHCb file, and some of
  their pages (13) still describe venv; their seminars already use the
  weather project. Rework each deck before its week.

## 2026-10-13 · Weeks 5 and 6 swapped: Python before Git

**Lecturer's notes**

- "Section 8 of L4 also got complicated, we didn't take python yet so I am
  trying to avoid examples with python. Do you think the flow would be
  better if we at least introduce the fundamentals of python sooner?";
  then "Can still do this, I didn't give L5".
- "It's difficult to give a lecture on python... it all looks like a 4h
  seminar doesn't it? The same goes for CLI."

**Changed in response** (13 October)

- Lecture and Seminar 5 are now **Python Foundations** (20 Oct), Lecture
  and Seminar 6 **Version Control with Git** (27 Oct): files, slugs
  (`05-python-foundations`, `06-version-control`), `decks.json` (both in
  block A), the lecture and seminar pages, nav, overview, home page and
  every cross-reference.
- The Python deck is reworked onto the weather project as a lecture, not a
  typing tutorial: short pieces, the room predicts each output before it is
  shown, and how the interpreter works underneath.
- Seminar 5 (Python) starts from the folder of Seminar 4, without Git; its
  buggy `coldest_hour.py` and a catch-up `weather-project-s4.zip` are on the
  Releases page (`misc/weather_repo/release_files.py`). Seminar 6 (Git) keeps
  that folder as `weather-project-s5`, copies its scripts into the clone and
  commits them, and adds the `course` remote for later seminars. The course
  commit of Seminar 6 in `build.sh` is gone; `STAGE` now defaults to 6.

**Open**

- The Git deck's story is dated 13 to 20 October; it is now given on 27
  October.
- For the next run: Lecture 04 can end shell-only (the mean by `awk`), with
  conda moved to Lecture 05.
