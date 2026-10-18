# 2: Introduction to Data

Lecture 2 opens on a file that arrived with no note: the first four lines of
`weather.csv`, the hourly log of a weather station, 87 673 lines and
2 515 215 bytes. The room lists what the file does not say, and the lecture
answers those five questions one section at a time, each on the file itself.
A CERN file is asked the same questions: what becomes a row at the LHC, how
the ATLAS file of CERN Open Data record 328 marks a value that cannot exist
(`-999.0`, as the station does), and what its record says that the station's
e-mail did not. The lecture ends with the tools for writing the answers down:
VS Code, a README in Markdown, and edits made on many lines at once.

## What the lecture covers

1. **A file with no note**: four lines of `weather.csv`; the five questions
   they leave open, each next to the part of the file it is about; data as
   symbols plus the rule that lets someone else read them back; the
   lifecycle.
2. **How one row was made**: one line per hour at the station; the same
   question at the LHC, where the trigger keeps a few thousand collisions a
   second; the data-flow clip.
3. **Reading the file**: the rows counted with `Ctrl+End` and checked against
   10 years of hours; line 5000 found with `Ctrl+G` and checked against its
   time; the units worked out from the numbers; `-999` found with `Ctrl+F`,
   below absolute zero, and what it does to a mean; `-999.0` in a CERN file,
   580 253 of 818 238 rows, where a value cannot exist.
4. **Kinds of data**: everything as numbers; the four kinds of variables and
   the columns of `weather.csv`; the anatomy of a table on the nine-day
   spreadsheet export `daily_export.csv`; which columns can be averaged, and
   why a mean line left in does not move the mean; the 24 hourly values of
   1 October behind the export's `6,3`; CSV, spreadsheet and binary with the
   size of the log in each; the decimal comma; the same file opened in a
   spreadsheet; one row as text and as binary numbers.
5. **Where the file came from**: portals; the anatomy of a record, CERN Open
   Data record 328 next to `weather.csv`; licences; the provenance note for
   `weather.csv`; from record to project folder; the five questions answered
   for both files, then asked of other datasets and of the student's own.
6. **The editor**: the project folder and rules for file names; VS Code, the
   five regions of its window, first keys, files in the Side Bar, saving.
7. **Markdown**: source and preview, headings, lists, links and images,
   tables, usual mistakes.
8. **Editing many lines**: the daily export repaired in the editor with
   whole-line keys, Find and Replace, a cursor on every line and selected
   matches; turned into a Markdown table; the four edits written into the
   README and checked by size; text commands and the key sheet. The lecture
   closes on the four lines of `weather.csv`, annotated.

## The definition of data

Slide 6 gives the definition of ISO/IEC 2382, *Information technology,
Vocabulary*:

> Data is a reinterpretable representation of information in a formalized
> manner suitable for communication, interpretation, or processing.

Three words carry it. A **representation**: the symbols `-4.4` are not a
temperature, they may stand for one. **Formalized**: the symbols follow a
fixed rule. **Reinterpretable**: someone else, or a program, can get the
information back. The lecture's thesis is one sentence, on slide 7: *a number
is data only together with the rule that lets someone else read it back.*
Each section adds one part of the rule for `weather.csv`, and slide 65 shows
them all on the file's first four lines.

## The numbers on the slides

The weather numbers were computed on the files in `lectures/workbook/docs/data/`.

- `weather.csv`: 87 673 lines (87 672 rows and a header), 2 515 215 bytes,
  28.7 bytes per row. Row 1, `2016-01-01T00:00,-4.4,93,2.5`, is 28
  characters and a line end. As four 4-byte numbers per row the file would be
  87 672 × 16 = 1 402 752 bytes; the text is 1.8× larger. Saved as `.xlsx`
  with `openpyxl` 3.1.5 it is 1 922 248 bytes.
- Rows: 10 × 365 × 24 = 87 600, plus 3 leap days × 24 = 72, gives 87 672: one
  row per hour from 2016 to 2025. Line 5000 is
  `2016-07-27T06:00,18.2,71,1.1`, 4 998 = 208 × 24 + 6 hours after the first.
- `temp_c` from −16.3 to 32.4, median 6.7; `humidity_pct` from 34 to 100;
  `wind_ms` from 0.0 to 12.0, median 3.5 (all without the marked rows).
- `-999` in `temp_c`: 120 rows, `2019-07-22T00:00` to `2019-07-26T23:00`,
  5 × 24 = 120. Mean temperature without them 7.16 °C, with them 5.78 °C;
  120 × (−999) / 87 672 = −1.37 °C.
- 1 October 2025 in `weather.csv`: 24 hourly values from 2.7 (02:00) to 10.1
  (14:00), sum 151.1, and 151.1 / 24 = 6.30, the `6,3` of the export.
- `daily_export.csv` (in the workbook `weather_daily_export.csv`): 180 bytes,
  nine days of October 2025. Sums 45 (`nr`) and 71.7 (`temp_c`);
  71.7 / 9 = 7.967, the `7,97` of its mean line; (71.7 + 7.97) / 10 = 7.967
  again. Repaired by hand it is 148 bytes: the mean line is 11 bytes, column
  `nr` 3 + 9 × 2 = 21, and 180 − 11 − 21 = 148.
- CERN Open Data record 328, *Dataset from the ATLAS Higgs Boson Machine
  Learning Challenge 2014*, DOI `10.7483/OPENDATA.ATLAS.ZBP2.M5T8`, CC0: one
  file, `atlas-higgs-challenge-2014-v2.csv.gz`, 65 630 848 bytes, 818 238 rows
  of simulated collisions and 35 columns. Counted on the file (13 October
  2026): `PRI_jet_num` is 0 in 327 371 rows and 1 in 252 882;
  `DER_deltaeta_jet_jet` is `-999.0` in exactly those 580 253 rows (71 %);
  `DER_mass_MMC` is `-999.0` in 124 602 rows. Rows 100000 to 100002 are
  shown on slide 19, 4 of their 35 columns. The record describes every
  column (`DER_deltaeta_jet_jet`: "undefined if PRI_jet_num ≤ 1") but gives
  no units; the mass columns, near the Higgs mass of 125 GeV, point to GeV.

## The lecture, part by part

The lecture is slides 1–66; when time is short, skip the slides of the
second table. Slides 67–75 are the self-check quizzes and take no lecture
time. To jump, type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–4 | Four lines of `weather.csv` and the five questions |
| 6–7 | The definition of data, symbols plus a rule |
| 9–12 | One line per hour; one row at the LHC; the data-flow clip |
| 13–14, 16–19 | The rows counted, the units, `-999` and the mean, `-999.0` in a CERN file |
| 21–26 | Numbers, kinds of variables, the daily export, which columns can be averaged, measured or derived |
| 28 | The decimal comma |
| 31, 33, 35–37 | The record next to `weather.csv`, the provenance note, the project folder, the five answers |
| 39–40, 42–43, 45–46 | The project folder and VS Code |
| 47–50, 52 | Markdown: the source and its preview |
| 54–59, 61 | The daily export repaired, then made a Markdown table |
| 65–66 | The file, annotated; Recap |

| Skip | Slides |
|--|--|
| The lifecycle | 8 |
| A line in the middle | 15 |
| File formats; the spreadsheet; a row as text and as binary | 27, 29–30 |
| Portals, licences | 32, 34 |
| The five questions for other datasets | 38 |
| Rules for file names, first keys | 41, 44 |
| Links and images, usual mistakes | 51, 53 |
| Every match of a word, the size check, text commands, the key sheet | 60, 62–64 |

- **Do not cut** slides 3–4 (the questions), 7 (the thesis), 17–19 (`-999`,
  its effect on the mean, the CERN file), 23–25 (the table and its mean), 37
  (the answers) and 65 (The File, Annotated): together they carry the story.
- **The slides carry everything.** Each step in VS Code is shown on its
  slide with its result, so nothing is opened beside the deck. Ask the room
  for each unit before showing its card.
- **Slides 39–64 are what Seminar 1 practises** by hand.
- **The speaker notes** of every slide have the same short form: **Do**,
  **Say**, **Ask**, **If asked**, and the minutes.

To show the slides offline: `node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/02-intro-to-data/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 67–75: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A colleague sends a file of numbers with no header and no note. By the
   definition of data, what is missing?
   *The rule that lets someone else read the numbers back: what each one is,
   in which unit, from where.*
2. You downloaded a CSV file six months ago and want a reader to get exactly
   the same data. What must you have recorded?
   *The record's DOI or stable URL, the version or the date you fetched it,
   and the checksum of the file.*
3. The detectors of the LHC see about 40 million bunch crossings a second.
   Why is not every collision stored?
   *No system can write the raw signal, about 1 PB a second, to disk. The
   trigger keeps the few thousand collisions a second that computing can
   absorb.*
4. A weather service publishes its station logs on an open portal years
   after recording them. Which stage of the lifecycle is that, and what makes
   it possible?
   *Sharing, the last stage. It works only because the rule of the data was
   kept at every stage before it.*
5. In `weather.csv`, what does one row represent?
   *One hour at one station.*
6. A column is named `wind_ms` and holds values from 0.0 to 12.0, median 3.5.
   Which unit fits?
   *Metres per second: 3.5 m/s is a breeze and 12 m/s a strong wind. A wind
   in milliseconds makes no sense.*
7. A file has lines like `1;2025-10-01;6,3` and must become
   `1,2025-10-01,6.3`. Which replacement comes first?
   *The decimal comma, `,` to `.`, while it is the only comma in the file. In
   the other order it cannot be told from the separators.*
8. An editor sorts `10.4`, `5.0` and `9.8` as text. Which comes first?
   *`10.4`: the character `1` comes before `5` and `9`.*

## Paired seminar

[Seminar 1, VS Code and Markdown](../seminars/seminar_01.md) is the first
session in class and starts from zero. It practises the ideas of slides
39–64 by hand: VS Code and a project folder, a README in Markdown, and a
table repaired in the editor. All of it is done in class.

## Parked slides

Slides that left the deck are kept in
`lectures/content/parked/02_Introduction_to_Data.md`. On 13 October 2026,
when the look at the file moved to the first third of the deck and the CERN
examples were tied to the same five questions, four text-card slides left
it: Learning Objectives, Read a Row Aloud (slide 7 reads the same row),
Structured vs Unstructured and Your Own Dataset. On 12 October 2026, when the
deck changed its example to the weather station, the CERN detector slides
left it: ATLAS and CMS, ALICE, LHCb, their fly-in clips and the quark-gluon
plasma clip, From Collision to Dataset, From Events to Petabytes, What the
Trigger Kept and 147 Columns, 4 Filled. Earlier parked slides: What Each
Flavour Is Used For, Data at Work, Common Threads, Working with the Data, the
section Beyond Physics, A Day in Data, Every One of These Is a Dataset,
Measurement vs Metadata, the thought exercise, Why Data Analysis Matters at
CERN, the old Recap and two quiz slides. The file is not built. To put a
slide back, move it into the lecture file.

## Take-aways

- Data is a representation of information by a fixed rule, which someone
  else can read back. `-4.4` became information once its kind, source, row
  and unit were found.
- A row is one observation, a column is one variable of one kind, a cell is
  one value. A mean line in a table breaks the first rule, and the mean
  cannot show it: only the count can.
- A derived column is checkable only if the README says how it was computed.
- A spreadsheet shows an interpretation of a CSV file that depends on the
  computer; a text editor shows its characters.
- Write provenance down: source, licence, date, files, changes. Cite the
  record, not the file.
- A row is a decision: one hour at a station, one kept collision at CERN.
- Units and missing-value marks come from the numbers when the file is
  silent: −999 °C is below absolute zero, so it is a mark, and counted as a
  number it moves a ten-year mean by more than a degree. A CERN file uses
  the same mark for a value that cannot exist for a collision.
- A file in `data/raw` is never edited. It is cleaned on a copy, and the
  README lists what was changed.
- An edit that is the same on every line is made once: Find and Replace for
  the same text everywhere, a cursor on every line for the same place on
  every line.
