# 2: Introduction to Data

Lecture 1 ended its reel at LHCb and said the seminars use the same events
physicists used. Lecture 2 opens on that file: the first four lines of
`D0_KPi.csv`, 91 584 lines and 3 926 142 bytes, with no note. The room lists
what the file does not say, and the lecture answers those five questions one
section at a time. It ends on the same four lines, annotated, and on the tools
for writing the answers down: a README in Markdown and a text editor.

## What the lecture covers

1. **A file with no note** — four lines of `D0_KPi.csv`; the five questions
   they leave open; data as symbols plus the rule that lets someone else read
   them back; the lifecycle, and where the file stands in it.
2. **Kinds of data** — structured vs unstructured; numbers, text, images and
   events as numbers; kinds of variables; the anatomy of a table on
   `pendulum_raw.csv` as received; which columns can be averaged, worked out
   on it; the same table as CSV, spreadsheet and binary file, and the LHCb
   table measured as 3 926 142 bytes of text against 1 289 541 bytes of ROOT.
3. **Where the file came from** — portals, the anatomy of record 401,
   licences (CC0 / CC BY / share-alike), the minimal provenance note, your own
   dataset, from record to project folder.
4. **How one row was made** — the four LHC experiments, LHCb and the D⁰; from
   collision to stored event; one row of the file against one stored event;
   what the trigger kept, and the two columns, `TAU` and `IPCHI2`, that
   measure it.
5. **Reading the file** — one row read aloud; three questions answered with
   `Ctrl+End`, `Ctrl+G` and `Ctrl+F`; 147 columns declared and 4 filled; the
   units worked out from the numbers; the five questions answered, then asked
   of a dataset from the student's own field.
6. **Markdown & text editing** — the project folder and its names; Markdown
   as source and preview: headings, lists, links, images, tables, the usual
   mistakes; the pendulum table repaired in the editor with Find and Replace,
   whole-line keys, a cursor on every line and selected matches; the four
   edits written into the README. The lecture closes on the four lines of
   `D0_KPi.csv`, annotated.

## The definition of data

Slide 7 gives the definition of ISO/IEC 2382, *Information technology —
Vocabulary*:

> Data is a reinterpretable representation of information in a formalized
> manner suitable for communication, interpretation, or processing.

Three words carry it. A **representation**: the symbols `1880.649` are not a
mass, they may stand for one. **Formalized**: the symbols follow a fixed rule,
and a file format and a column name carry part of that rule.
**Reinterpretable**: someone else, or a program, can get the information back.
The lecture's thesis is one sentence: *a number is data only together with the
rule that lets someone else read it back.* Each section ends by adding one part
of the rule for `D0_KPi.csv`: the kind of each column (slide 14), the record
and its checksum (slide 21), the selection that made a row (slide 37), the
units (slide 42). The last slide, 63, shows them all on the file's first four
lines.

## The numbers on the slides

All were computed on the files in `lectures/workbook/docs/data/`.

- `D0_KPi.csv`: 91 584 lines (91 583 rows and a header), 3 926 142 bytes,
  42.9 bytes per row. `MasterclassData.root`: 1 289 541 bytes, 14.1 bytes per
  row, 147 columns declared and 4 filled; the CSV is 3.0× larger.
- Record 401 says "about 60k events" and lists 53 948; the file has 91 583
  rows, 1.7 per event.
- Line 5000: `1868.8636,5537.248,0.0007151779,10.399748`. `-100` occurs 49
  times, each one `-100.0` in `TAU`.
- Medians: `M` 1864.08 (D⁰ mass 1864.84 MeV/c²), `PT` 3 049, `TAU` 0.000272
  (D⁰ lifetime 0.41 ps; ln 2 × 0.41 = 0.28 ps). The busiest 5-unit bin of `M`
  is 1860–1865, with 8 931 candidates.
- `pendulum_raw.csv`: 130 bytes. Sums 45, 540 and 136.25; means 5.0, 60 cm and
  15.139 s; with the mean line left in, 151.39 / 10 = 15.139 s again. The
  cleaned `pendulum.csv` is 97 bytes: the mean line is 12 bytes, column `nr`
  21 bytes, and 130 − 97 = 33.

## The lecture in 90 minutes

The lecture is slides 1–64 and estimates about 126 min. Slides 65–73 are the
self-check quizzes and take no lecture time. In a 2-hour slot nothing is
skipped. For a 90-minute slot, skip the slides in the second table. The hook
of slide 3 is answered on slide 43, at about 1:00. To jump, type the slide
number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–5 | Four lines of `D0_KPi.csv`, the five questions, objectives |
| 0:08 | 6–8 | Data and information, the lifecycle |
| 0:14 | 9, 12–16 | Kinds of variables, the pendulum table, which columns can be averaged, three files, two sizes |
| 0:27 | 17, 19, 21, 23 | Record 401, provenance, the project folder |
| 0:35 | 24, 31–35, 37 | LHCb and its clip, from collision to dataset, the data-flow clip, what the trigger kept |
| 0:48 | 38–40, 42–43 | One row read aloud, three questions clicked, units by reasoning, the five questions answered |
| 1:02 | 44 | The five questions on the student's own dataset (5 min) |
| 1:08 | 45–52 | The project folder and Markdown |
| 1:23 | 63–64 | The file, annotated; Recap |
| 1:26 | | Move to the seminar. Slides 53–62 open it |

| Skip | Slides | Saves |
|--|--|--|
| Structured vs unstructured; numbers, text, images, events | 10–11 | 5 min |
| Portals, licences, your own dataset | 18, 20, 22 | 6 min |
| ATLAS and CMS, ALICE, their fly-ins, the quark–gluon plasma clip | 25–30 | 12 min |
| From Events to Petabytes | 36 | 3 min |
| 147 Columns, 4 Filled | 41 | 2 min |
| Editing many lines and writing the edits down, shown at the start of the seminar instead | 53–62 | 22 min |

- **Do not cut** slide 63 (The File, Annotated): it closes the lecture by
  answering slide 3. Slides 3–4 (the hook), 7 (the thesis), 13–16 (the
  pendulum table and the two sizes), 37 and 39–43 (the file read and
  answered) carry the story.
- **The LHCb clip stays in** (slide 32, 0:47): it is the detector the file
  comes from.
- **The data-flow clip stays in** (slide 35, 2:51, with music): accelerator
  chain, detectors, trigger, data centre, grid.
- **Slide 14** (which columns can be averaged): let the room add up `t10_s`
  and guess what the mean line does to the mean before showing it.
- **Slides 40 and 42 are shown live.** Open `D0_KPi.csv` in VS Code on the
  projector: `Ctrl+End`, `Ctrl+G` 5000, `Ctrl+F` `-100`. Ask the room for
  each unit before showing the card.
- **Slide 44** (5 min): students answer the five questions for a dataset of
  their own field, on paper. The answers are the first lines of their README
  in the seminar.
- **Slides 45–62 are shown live.** Keep VS Code open beside the slides and do
  each step on the projector: type the six lines of slide 47 and open the
  preview, make the mistakes of slide 52, repair the file of slide 53 with
  the keys of slides 54–59, and type the README lines of slide 60. Slide 62
  is the key sheet. It stays on the projector while the room works through
  Part 3 of the seminar.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/02-intro-to-data/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 65–73: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A colleague sends a file of numbers with no header and no note. By the
   definition of data, what is missing?
   *The rule that lets someone else read the numbers back: what each one is,
   in which unit, from where.*
2. You downloaded a CSV file six months ago and want a reader to get exactly
   the same data. What must you have recorded?
   *The record's DOI or stable URL, the version or the date you fetched it, and
   the checksum of the file.*
3. The detector electronics put out about 1 PB of raw signal per second. Why is
   it not all recorded?
   *No system can write 1 PB/s to disk. The trigger reduces it to the few
   thousand events per second that computing can absorb.*
4. CERN publishes its collision data years after recording it. Which stage of
   the lifecycle is that, and what makes it possible?
   *Sharing, the last stage. It works only because provenance, formats and
   software were kept at every stage before it.*
5. What is one row of the LHCb example file?
   *One K⁻π⁺ candidate from one collision.*
6. A candidate has `TAU` = 0.0003 and no unit is written. Which unit fits?
   *Nanoseconds: 0.0003 ns = 0.3 ps, the size of the D⁰ lifetime of 0.41 ps.
   In seconds it would be hundreds of millions of times too long.*
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
write into the README where it came from. All of it is done in class. Python,
Git and PowerShell 7 are installed in class at the start of
[Seminar 4](../seminars/seminar_04.md).

## Parked slides

Slides that left the deck are kept in
`lectures/content/parked/02_Introduction_to_Data.md`: What Each Flavour Is Used
For, Data at Work (two slides), Common Threads, Working with the Data, the
section Beyond Physics, and from the rework of 6 October: A Day in Data (two
slides), Every One of These Is a Dataset, Measurement vs Metadata, the weather
version of Anatomy of a Table, the thought exercise, Why Data Analysis Matters
at CERN, the old Recap and two quiz slides. The file is not built. To put a
slide back, move it into the lecture file.

## Take-aways

- Data is a representation of information by a fixed rule, which someone else
  can read back. A number without its rule is not yet data anyone can use:
  `1880.649` became information once its kind, source, row and unit were
  found.
- Parametrisation: every flavour of data is written as a set of numbers before
  it is analysed. Written as a number is not the same as behaving like one: a
  row number has a mean of 5.0 that says nothing.
- A row is one observation, a column is one variable of one kind, a cell is
  one value. A mean line in a table breaks the first rule, and the mean cannot
  show it: only the count can.
- The same table is 3.0× larger as text than as ROOT. Neither one stores its
  units.
- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum. A converted copy says how it was converted.
- The trigger decides what becomes a row. `TAU` and `IPCHI2` measure the
  flight it looks for.
- Units are metadata. When the file does not say, work them out from the
  numbers against a value you know, check them against any note that came
  with the file (here `root_to_csv.py`), and write them into the README.
- A file in `data/raw` is never edited. It is cleaned on a copy, and the
  README lists what was changed.
- An edit that is the same on every line is made once: Find and Replace for
  the same text everywhere, a cursor on every line for the same place on every
  line.
