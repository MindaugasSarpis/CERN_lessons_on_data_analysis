# 2: Introduction to Data

Lecture 1 was the *why* — the course, the four aims, and the motivation reel
from the cosmos down to CERN. Lecture 2 is the *what*: what a dataset is, where
one comes from, how you write down where it came from, and the two tools for
doing so, Markdown and a text editor.

## What the lecture covers

1. **Data in your life** — a day's worth of datasets; the definition of data;
   its lifecycle from collecting to sharing.
2. **Kinds of data** — structured vs unstructured; the four flavours (numbers,
   text, images, events) and their parametrisation — how each one is written
   as numbers; kinds of variables (continuous, discrete, nominal, ordinal);
   measurement vs metadata; the anatomy of a table; the same table as CSV,
   spreadsheet and binary file.
3. **Open data & provenance** — portals, the anatomy of a record, licences
   (CC0 / CC BY / share-alike), the minimal provenance note, data you bring
   yourself, from record to your project folder.
4. **Case study: CERN** — the four LHC experiments; from collision to dataset
   and why the trigger works in real time.
5. **A dataset up close** — the LHCb example as a file: rows are candidates,
   four computed columns, units are metadata, five questions to ask any file
   before writing code.
6. **Markdown & text editing** — the project folder and its names; Markdown
   as source and preview: headings, lists, links, images, tables, the usual
   mistakes; then one small table that arrives in the wrong format and is
   repaired in the editor with Find and Replace, whole-line keys, a cursor on
   every line and selected matches.

## The definition of data

Slide 8 gives the definition of ISO/IEC 2382, *Information technology —
Vocabulary*:

> Data is a reinterpretable representation of information in a formalized
> manner suitable for communication, interpretation, or processing.

Three words carry it. A **representation**: the symbols `11.2` are not a
temperature, they stand for one. **Formalized**: the symbols follow a fixed
rule, and a file format and a column name carry that rule. **Reinterpretable**:
someone else, or a program, can get the information back. The rest of the
lecture returns to each word: variables and tables are the rule, metadata and
provenance are what makes a file reinterpretable, and Lecture 3 goes down to
the lowest level of representation, the bit.

## The lecture in 90 minutes

The lecture is slides 1–62 and estimates about 120 min. Slides 63–71 are the
self-check quizzes and take no lecture time. In a 2-hour slot nothing is
skipped. For a 90-minute slot, skip the slides in the second table. To
jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–9 | Data in your life, the definition of data, the lifecycle |
| 0:15 | 10–17 | Kinds of data, variables, tables, files, thought exercise |
| 0:34 | 18–24 | Open data and provenance |
| 0:48 | 32–37 | LHCb, why analysis matters, from collision to dataset |
| 0:59 | 40–44 | The example file up close |
| 1:08 | 45–52 | The project folder and Markdown |
| 1:23 | 62 | Recap |
| 1:25 | | Move to the seminar. Slides 53–61 open it |

| Skip | Slides | Saves |
|--|--|--|
| ATLAS and CMS, ALICE, their fly-ins, the quark–gluon plasma clip | 26–31 | 12 min |
| From Events to Petabytes, Why It Has to Be Real-Time | 38–39 | 5 min |
| Editing many lines, shown at the start of the seminar instead | 53–61 | 19 min |

- **Do not cut** slides 10–16 (kinds of data, tables, files), 18–24 (open data
  and provenance) or 40–44 (the example file). The seminar uses every one of
  them.
- **The LHCb clip stays in** (slide 33, 0:47): it is the detector the example
  file comes from.
- **The data-flow clip stays in** (slide 37, 2:51, with music): accelerator
  chain, detectors, trigger, data centre, grid.
- **Slide 16** (One Table, Three Files) introduces the decimal comma. The file
  on slide 53 and the seminar's comparison in a spreadsheet both build on it.
  Do not rush it.
- **Slide 17** (thought exercise, 5 min): ask students to keep their answer.
  They write it into their README in the seminar.
- **Slides 45–61 are shown live.** Keep VS Code open beside the slides and do
  each step on the projector: type the six lines of slide 47 and open the
  preview, make the mistakes of slide 52, and repair the file of slide 53 with
  the keys of slides 54–59. Slide 61 is the key sheet. It stays on the
  projector while the room works through Part 3 of the seminar.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/02-intro-to-data/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 63–71: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. Alarm, transit card, recommendations, fraud checks: what do they have in
   common as data analysis?
   *Each runs the same loop: collect, store, clean, analyse, decide, then share
   or archive.*
2. You downloaded a CSV file six months ago and want a reader to get exactly
   the same data. What must you have recorded?
   *The record's DOI or stable URL, the version or the date you fetched it, and
   the checksum of the file.*
3. What does the 5-sigma standard of a discovery mean?
   *With no new particle, background alone produces a signal this strong in
   fewer than 1 in 3.5 million experiments. It is not the chance that the
   discovery is wrong.*
4. The detector electronics put out about 1 PB of raw signal per second. Why is
   it not all recorded?
   *No system can write 1 PB/s to disk. The trigger reduces it to the few
   thousand events per second that computing can absorb.*
5. CERN publishes its collision data years after recording it. Which stage of
   the lifecycle is that, and what makes it possible?
   *Sharing, the last stage. It works only because provenance, formats and
   software were kept at every stage before it.*
6. What is one row of the LHCb example file?
   *One K⁻π⁺ candidate from one collision.*
7. A file has lines like `1;20;9,02` and must become `1,20,9.02`. Which
   replacement comes first?
   *The decimal comma, `,` to `.`, while it is the only comma in the file. In
   the other order the line becomes `1,20,9,02` and the decimal comma cannot
   be told from the others.*
8. A list of lines `100,…`, `20,…`, `30,…` is sorted by the editor. Why does
   `100` come first?
   *The editor sorts text. The character `1` comes before `2`.*

## Paired seminar

[Seminar 1 — Get Started with VS Code and Markdown](../seminars/seminar_01.md)
is the first session in class and starts from zero. It has four parts: install
VS Code and build a project folder; write the README in Markdown; clean a small
table with Find and Replace and a cursor on every line, and turn it into a
table in a short report; put the lecture's example file into `data/raw/` and
write into the README where it came from. At home students choose a dataset
from their own field and
[install Python and Git](../seminars/install_python_git.md).

## Parked slides

Slides that left the deck are kept in
`lectures/content/parked/02_Introduction_to_Data.md`: What Each Flavour Is Used
For, Data at Work (two slides), Common Threads, Working with the Data, and the
section Beyond Physics. The file is not built. To put a
slide back, move it into the lecture file.

## Take-aways

- Data is a representation of information by a fixed rule, which someone else
  can read back. A number without its rule is not yet data anyone can use.
- Parametrisation: every flavour of data is written as a set of numbers before
  it is analysed — a character as a code, a pixel as three values 0–255, an
  event as a time plus what was measured. Written as a number is not the same
  as behaving like one: a postcode has no average.
- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum.
- Read the record before the data: what is one row, how was it selected, what
  may you publish.
- Units are metadata — if the file does not say, your README must.
- A row is one observation, a column is one variable of one kind, a cell is
  one value.
- A CSV file is plain text; a spreadsheet shows its own interpretation of it.
- A file that is too large, or not yours to share, stays out of the folder you
  pass on. The README says how to fetch it.
- A file in `data/raw` is never edited. It is cleaned on a copy, and the
  README lists what was changed.
- An edit that is the same on every line is made once: Find and Replace for
  the same text everywhere, a cursor on every line for the same place on every
  line.
