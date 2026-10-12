# 2: Introduction to Data

Lecture 2 opens on a file that arrived with no note: the first four lines of
`weather.csv`, the hourly log of a weather station, 87 673 lines and
2 515 215 bytes. The room lists what the file does not say, and the lecture
answers those five questions one section at a time. It ends with the tools
for writing the answers down: VS Code, a README in Markdown, and edits made on
many lines at once.

## What the lecture covers

1. **A file with no note**: four lines of `weather.csv`; the five questions
   they leave open; data as symbols plus the rule that lets someone else
   read them back; the lifecycle.
2. **Kinds of data**: structured and unstructured; everything as numbers;
   kinds of variables; the anatomy of a table on the nine-day spreadsheet
   export `weather_daily_export.csv`; which columns can be averaged, and why
   a mean line left in does not move the mean; measured, derived and
   bookkeeping columns; CSV, spreadsheet and binary; the decimal comma; the
   same file opened in a spreadsheet; one row as text and as binary numbers.
3. **Where the file came from**: portals, the anatomy of a record (with CERN
   Open Data record 401 as the real example), licences, the provenance note
   for `weather.csv`, your own dataset, from record to project folder.
4. **How one row was made**: one hour, one row at the station; at CERN, the
   trigger that decides which collisions become rows; the data-flow clip.
5. **Reading the file**: one row read aloud; the rows counted with
   `Ctrl+End` in a text editor and checked against 10 years of hours; line 5000 found with
   `Ctrl+G` and checked against its time; the units worked out from the
   numbers; `-999` found with `Ctrl+F`, below absolute zero, and what it does
   to a mean; the five questions answered, then asked of the student's own
   dataset.
6. **The editor**: the project folder and names that travel; VS Code, the
   five regions of its window, three keys, files in the Side Bar, saving.
7. **Markdown**: source and preview, headings, lists, links and images,
   tables, five usual mistakes.
8. **Editing many lines**: the daily export repaired in the editor with
   whole-line keys, Find and Replace, a cursor on every line and selected
   matches; turned into a Markdown table; the four edits written into the
   README and checked by size; text commands and the key sheet. The lecture
   closes on the four lines of `weather.csv`, annotated.

## The definition of data

Slide 7 gives the definition of ISO/IEC 2382, *Information technology,
Vocabulary*:

> Data is a reinterpretable representation of information in a formalized
> manner suitable for communication, interpretation, or processing.

Three words carry it. A **representation**: the symbols `-4.4` are not a
temperature, they may stand for one. **Formalized**: the symbols follow a
fixed rule. **Reinterpretable**: someone else, or a program, can get the
information back. The lecture's thesis is one sentence, on slide 8: *a number
is data only together with the rule that lets someone else read it back.*
Each section adds one part of the rule for `weather.csv`, and slide 68 shows
them all on the file's first four lines.

## The numbers on the slides

All were computed on the files in `lectures/workbook/docs/data/`.

- `weather.csv`: 87 673 lines (87 672 rows and a header), 2 515 215 bytes,
  28.7 bytes per row. Row 1, `2016-01-01T00:00,-4.4,93,2.5`, is 28
  characters and a line end. As four 4-byte numbers per row the file would be
  87 672 × 16 = 1 402 752 bytes; the text is 1.8× larger.
- Rows: 10 × 365 × 24 = 87 600, plus 3 leap days × 24 = 72, gives 87 672: one
  row per hour from 2016 to 2025. Line 5000 is
  `2016-07-27T06:00,18.2,71,1.1`, 4 998 = 208 × 24 + 6 hours after the first.
- `temp_c` from −16.3 to 32.4, median 6.7; `humidity_pct` from 34 to 100;
  `wind_ms` from 0.0 to 12.0, median 3.5 (all without the marked rows).
- `-999` in `temp_c`: 120 rows, `2019-07-22T00:00` to `2019-07-26T23:00`,
  5 × 24 = 120. Mean temperature without them 7.16 °C, with them 5.78 °C;
  120 × (−999) / 87 672 = −1.37 °C.
- `weather_daily_export.csv`: 180 bytes, nine days of October 2025. Sums 45
  (`nr`) and 71.7 (`temp_c`); 71.7 / 9 = 7.967, the `7,97` of its mean line;
  (71.7 + 7.97) / 10 = 7.967 again. 1 October: 24 hourly values of
  `weather.csv` sum to 151.1, and 151.1 / 24 = 6.30. Repaired by hand it is
  148 bytes: the mean line is 11 bytes, column `nr` 3 + 9 × 2 = 21, and
  180 − 11 − 21 = 148.

## The lecture in 90 minutes

The lecture is slides 1–69 and estimates about 113 min; with the pauses for
the room it runs longer. Slides 70–78 are the self-check quizzes and take no
lecture time. For a 90-minute slot, skip the slides in the second table;
that leaves about 92 min. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–5 | Four lines of `weather.csv`, the five questions, objectives |
| 0:08 | 7–8 | The definition of data, symbols plus a rule |
| 0:13 | 13–16 | Kinds of variables, the daily table, which columns can be averaged, the mean line left in |
| 0:23 | 19 | The decimal comma |
| 0:25 | 22, 24, 26, 28 | A record, the provenance note, the project folder |
| 0:32 | 29–31 | One hour, one row; the trigger at CERN |
| 0:38 | 33, 35, 37–40 | The rows counted, the units, `-999`, what it does to a mean, the five answers |
| 0:53 | 42–43, 45–46, 48–49 | The project folder and VS Code |
| 1:05 | 50–53, 55 | Markdown: the source and its preview |
| 1:13 | 57–62, 64 | The daily export repaired, then made a Markdown table |
| 1:29 | 68–69 | The file, annotated; Recap |
| 1:32 | | End |

| Skip | Slides | Saves |
|--|--|--|
| The lifecycle | 9 | 2 min |
| Structured and unstructured; everything as numbers | 11–12 | 4 min |
| Measured or derived; three files; the spreadsheet; two sizes | 17–18, 20–21 | 8 min |
| Portals, licences, your own dataset | 23, 25, 27 | 6 min |
| The data-flow clip | 32 | 3 min |
| One row read aloud, a line in the middle, your dataset | 34, 36, 41 | 10 min |
| Names that travel, three keys | 44, 47 | 4 min |
| Links and images, five mistakes | 54, 56 | 4 min |
| The same word everywhere, the size check, text commands, the key sheet | 63, 65–67 | 8 min |

- **Do not cut** slides 3–4 (the questions), 8 (the thesis), 14–16 (the
  table and its mean), 38–40 (`-999` and the answers) and 68 (The File,
  Annotated): together they carry the story.
- **The slides carry everything.** Each step in VS Code is shown on its
  slide with its result, so nothing is opened beside the deck. Ask the room
  for each unit before showing its card.
- **Slides 42–64 are what Seminar 1 practises** with its own files, by hand.
- **The speaker notes** of every slide have the same short form: **Do**,
  **Say**, **Ask**, **If asked**, and the minutes.

To show the slides offline: `node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/02-intro-to-data/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 70–78: eight quiz slides for students to try afterwards. The same
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
42–67 with files of its own, a reading list and a library's loans log, not
the weather files: install VS Code and build a project folder; write the
README in Markdown; repair the reading list in the editor and turn it into a
report; count a long file, read its units and its missing-value mark `NA`,
open it in a spreadsheet, and write where the data came from. All of it is
done in class.

## Parked slides

Slides that left the deck are kept in
`lectures/content/parked/02_Introduction_to_Data.md`. On 12 October 2026, when
the deck changed its example to the weather station, the CERN detector slides
left it: ATLAS and CMS, ALICE, LHCb, their fly-in clips and the quark-gluon
plasma clip, From Collision to Dataset, From Events to Petabytes, What the
Trigger Kept and 147 Columns, 4 Filled. One CERN slide on the trigger and the
data-flow clip stay. Earlier parked slides: What Each Flavour Is Used For,
Data at Work, Common Threads, Working with the Data, the section Beyond
Physics, A Day in Data, Every One of These Is a Dataset, Measurement vs
Metadata, the thought exercise, Why Data Analysis Matters at CERN, the old
Recap and two quiz slides. The file is not built. To put a slide back, move it
into the lecture file.

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
  number it moves a ten-year mean by more than a degree.
- A file in `data/raw` is never edited. It is cleaned on a copy, and the
  README lists what was changed.
- An edit that is the same on every line is made once: Find and Replace for
  the same text everywhere, a cursor on every line for the same place on
  every line.
