# 2: Introduction to Data

Lecture 1 was the *why* — the course, the four aims, and the motivation reel
from the cosmos down to CERN. Lecture 2 is the *what*: what a dataset is, where
one comes from, and how you write down where it came from.

## What the lecture covers

1. **Data in your life** — a day's worth of datasets; what data even is; its
   lifecycle from collecting to sharing.
2. **Kinds of data** — structured vs unstructured; the four flavours (numbers,
   text, images, events); kinds of variables (continuous, discrete, nominal,
   ordinal); measurement vs metadata; the anatomy of a table; the same table
   as CSV, spreadsheet and binary file; data at work in other fields.
3. **Open data & provenance** — portals, the anatomy of a record, licences
   (CC0 / CC BY / share-alike), the minimal provenance note, data you bring
   yourself, from record to your repo.
4. **Case study: CERN** — the four LHC experiments; the D⁰ meson and its K⁻π⁺
   invariant-mass peak near 1865 MeV; the 5-sigma standard; from collision to
   dataset and why the trigger works in real time; the Web, the computing grid
   and open data.
5. **A dataset up close** — the LHCb example as a file: rows are candidates,
   four computed columns, units are metadata, five questions to ask any file
   before writing code.

## The lecture in 90 minutes

The deck has 63 slides and is sized for a 2-hour slot, about 131 min as
written. For a 90-minute slot, skip the slides in the second table. To jump,
type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–9 | Data in your life, what data is, the lifecycle |
| 0:16 | 11–19 | Kinds of data, variables, tables, files, thought exercise |
| 0:33 | 23–30 | Open data and provenance |
| 0:50 | 31–49 | CERN case study: the four detectors, the D⁰, the data flow, the trigger |
| 1:14 | 57–63 | The example file up close, recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Quiz: the lifecycle | 10 | 3 min |
| Where Each Flavour Shows Up Later | 18 | 2 min |
| Data at Work (two slides), Common Threads | 20–22 | 7 min |
| ATLAS film clip, ALICE, quark–gluon plasma clip | 35–37 | 6 min |
| LHCb film clip | 41 | 2 min |
| Quiz: what does 5 sigma mean? | 45 | 4 min |
| Quiz: why not record it all? | 50 | 3 min |
| Careers at CERN, Working with the Data | 51–52 | 4 min |
| Beyond Physics, the whole section with its quiz | 53–56 | 9 min |

- **Running late:** skip From Events to Petabytes (slide 48) next. The
  data-flow clip before it shows the same chain.
- **Do not cut** slides 11–17 (kinds of data, tables, files), 23–30 (open data
  and provenance) or 57–62 (the example file). The seminar uses every one of
  them.
- **The four detector fly-ins stay in:** ATLAS (33), CMS (34), ALICE (38),
  LHCb (40), three and a half minutes together. They are silent, so talk over
  them. The ALICE slide is skipped, so say what ALICE studies while its
  fly-in plays.
- **The data-flow clip stays in** (slide 47, 2:51, with music): accelerator
  chain, detectors, trigger, data centre, grid. It stands in for the skipped
  Beyond Physics section, where the grid is otherwise introduced.
- **Slide 17** (One Table, Three Files) sets up the seminar's comparison of
  the same CSV file in VS Code and in a spreadsheet. Do not rush it.
- **Slide 19** (thought exercise, 5 min): ask students to keep their answer.
  They write it into their README in the seminar.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/02-intro-to-data/`.

## Paired seminar

[Seminar 1 — Get Started with VS Code and Markdown](../seminars/seminar_01.md)
is the first session in class and starts from zero: install VS Code, build a
project folder, write its README in Markdown, put the lecture's example file
into `data/raw/`, and write into the README where it came from. At home
students choose a dataset from their own field and
[install Python and Git](../seminars/install_python_git.md).

## Take-aways

- Cite the **record**, not the file: DOI or stable URL, version or fetch date,
  checksum.
- Read the record before the data: what is one row, how was it selected, what
  may you publish.
- Units are metadata — if the file does not say, your README must.
- A row is one observation, a column is one variable of one kind, a cell is
  one value.
- A CSV file is plain text; a spreadsheet shows its own interpretation of it.
- Large or restricted data stays out of git; the README says how to fetch it.
