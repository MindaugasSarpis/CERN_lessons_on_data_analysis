# Lecture 2 — Introduction to Data

!!! abstract "Overview"
    **Time:** 15:00–17:00, 110 min of teaching and a break of 10 min

    **Questions**

    - What makes a number a measurement?
    - What is a table, and what is wrong with most tables?
    - What is in a data file, and why does it open differently on two
      computers?
    - Where does a data file come from, and how do I write that down?

    **After this lecture, students can**

    - write a measurement with its unit and uncertainty
    - read a table and name the kind of variable in each column
    - find what breaks the rules of a table: units, dates, missing values
    - read a CSV file character by character
    - find an open dataset and record its provenance
    - say where a row of the example file comes from

    **Needs:** the slides `02-intro-to-data`. VS Code with `D0_KPi.csv`, if
    at hand.

One real file, `D0_KPi.csv`, runs through the lecture. The slides add one
thing at a time. There are no film clips.

| Block | Clock | Min | Slides |
|--|--|--|--|
| [1. The example file](#example) | 15:00 | 9 | 1–6 |
| [2. From a number to a measurement](#number) | 15:09 | 8 | 7–13 |
| [3. The table](#table) | 15:17 | 19 | 14–20 |
| [4. Kinds of data](#kinds) | 15:36 | 5 | 21–23 |
| [5. A table as a file](#file) | 15:41 | 17 | 24–30 |
| Break | 15:58 | 10 | |
| [6. Open data and provenance](#provenance) | 16:08 | 17 | 31–38 |
| [7. How the example file was made](#made) | 16:25 | 22 | 39–47 |
| [8. The file up close](#close) | 16:47 | 18 | 48–56 |
| Break, then [Seminar 1](../seminars/seminar_01.md) | 17:05 | 10 | |

??? note "Before the session"
    - Start the slides: `node scripts/serve-local.mjs 8123`, then open
      `http://localhost:8123/02-intro-to-data/`.
    - To jump to a slide, type its number and press Enter.
    - Slides 57 to 65 are extra material: data in everyday life and in
      other fields. They are not part of the lecture.
    - The film clips of the detectors and of the data flow are in the
      extra material of Lecture 1.

## 1. The example file { #example }

<p class="block-meta">15:00 · 9 min · slides 1–6</p>

**Say.** Last time was the why. Today is the what: data itself. One file
runs through the whole lecture.

**Show slide 4,** or the real file in VS Code.

```text title="D0_KPi.csv, lines 1–5"
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
1913.8755,2542.169,0.00018464602,17.386473
1888.7571,4453.104,0.00056827645,56.79793
```

**Ask:** what can you tell from five lines? Four names, commas, decimal
points, no units.

**Say.** Four questions for today: what is one row, what kind of value is
in each column, where did the file come from, and what is wrong with it?

!!! success "Key points"
    - Data is recorded observation, in a form a machine can store and read
      again.
    - Every project walks the same cycle: collect, store, clean, analyse,
      decide, share.

## 2. From a number to a measurement { #number }

<p class="block-meta">15:09 · 8 min · slides 7–13</p>

**Say.** The next slides add one thing at a time to a single number.

| Slide | Shows | It is |
|--|--|--|
| 8 | `1864.84` | A number |
| 9 | `1864.84 MeV/c²` | A number with a unit |
| 10 | `1864.84 ± 0.05 MeV/c²` | A measurement |
| 13 | `1880.649, 3000.9534, 0.00041271152, 1299.1675` | One observation |

**Ask at each slide:** what is still missing?

!!! question "Ask the room · slide 12"
    The file writes the mass as `1880.649`. How many of these digits were
    measured?

??? success "Solution"
    About three. LHCb measures the mass of one pair to about 8 MeV/c². The
    other digits come from the way the computer stores a number: 32 bits
    hold about seven decimal digits, and the file prints all of them.

!!! success "Key points"
    - A measurement is a value, a unit and an uncertainty.
    - The uncertainty sets the number of digits to write.
    - The number of digits in a file is a property of the software that
      wrote it. Do not round the raw file. Round when you report.

## 3. The table { #table }

<p class="block-meta">15:17 · 19 min · slides 14–20</p>

**Say.** Values that belong together make a row. Rows of the same kind make
a table. A row is one observation, a column is one variable, a cell is one
value.

!!! question "Exercise · slide 17 · 5 min, with a neighbour"
    Find seven problems in this table. What would a program make of each
    cell?

    | Station | 29/09 | 30/09 | Notes |
    |--|--|--|--|
    | Vilnius | 11,2 °C | 12.0 | |
    | | 12.4 | -999 | sensor replaced |
    | Kaunas | 11.9 (approx.) | n/a | |
    | **Mean** | **11.8** | **12.0** | |

??? success "Solution"
    1. Dates are used as column names.
    2. `29/09`: day and month in an order that depends on the country, and
       no year.
    3. A unit inside a cell: `11,2 °C`.
    4. Decimal comma and decimal point in one column.
    5. An empty cell that means "same as above".
    6. Three signs for a missing value: `-999`, `n/a`, empty.
    7. A comment inside a value: `11.9 (approx.)`.
    8. A computed row, **Mean**, among the data.
    9. Nothing tells the two Vilnius readings of one day apart.

    Slide 18 shows the same data tidy.

**Then slides 19 and 20:** `03/04/2026` is the 3rd of April in London and
the 4th of March in New York. `2026-04-03` cannot be misread, and it sorts
by time.

!!! success "Key points"
    - Every cell is filled, one thing in a cell, only data in the table.
    - Dates are written as `2026-09-29`.
    - A missing value has one sign, and the README names it. Missing is not
      zero.
    - The kind of variable decides which statistic makes sense: a postcode
      has no average.

## 4. Kinds of data { #kinds }

<p class="block-meta">15:36 · 5 min · slides 21–23</p>

**Say.** A table is structured data. Text, images and sound are
unstructured: a computer cannot average them until they are written as
numbers.

**Ask at slide 23:** how does each of these become numbers? A colour is
three numbers, a place on Earth is two, one second of CD sound is 44 100.

!!! success "Key points"
    - Every kind of data is written as numbers before it is analysed.
    - Written as a number is not the same as behaving like one.

## 5. A table as a file { #file }

<p class="block-meta">15:41 · 17 min · slides 24–30</p>

**Say.** A table is an idea. On disk it is a row of characters.

| Character | Its job | What can go wrong |
|--|--|--|
| `,` | Ends a value | A value that contains a comma |
| `.` | Decimal point | Half of Europe writes `1880,649` |
| Line break | Ends a row | Windows writes two characters, macOS and Linux one |
| Line 1 | Names the columns | Nothing marks it as a header |

!!! question "Ask the room · slide 27"
    The same file is opened in Excel on a laptop with English settings and
    on one with Lithuanian settings. What does each show?

??? success "Solution"
    English settings: four columns of numbers. Lithuanian settings: one
    column of text, because the spreadsheet expects `;` between values and
    `,` inside a number. The file is the same, byte for byte.

!!! question "Ask the room · slide 28"
    Before showing each case, ask for a guess: how many COVID-19 cases can
    be lost because of a file format?

??? success "Solution"
    15 841, at Public Health England in 2020: the old `.xls` format holds
    65 536 rows. The other two cases: a cell range that left out 5 of 20
    countries (Reinhart and Rogoff), and gene names turned into dates in
    about one paper in five.

**Slide 30, thought exercise, 5 min.** Ask students to keep their answer.
They write it into their README in the seminar.

!!! success "Key points"
    - A CSV file holds characters only: no types, no units.
    - A spreadsheet shows its own reading of the file, and saving writes
      that reading back.
    - What the file cannot say goes into a data dictionary: name, meaning,
      unit, kind, sign for a missing value.

## 6. Open data and provenance { #provenance }

<p class="block-meta">16:08 · 17 min · slides 31–38</p>

**Say.** A portal is a catalogue. Every dataset on it is a record with a
stable address. You cite the record, not the file you happened to download.

```text title="The provenance note, slide 35"
Source:   CERN Open Data Portal, record 401
DOI:      10.7483/OPENDATA.LHCb.E7EJ.JUWR
Licence:  CC0
Fetched:  2026-09-29
Files:    MasterclassData.root  sha256 8694…039b
Changes:  none — D0_KPi.csv is a converted copy
```

!!! question "Exercise · slide 38 · 3 min"
    You downloaded a CSV file from a portal six months ago. What must you
    have recorded, so that a reader can get exactly the same data?

??? success "Solution"
    The DOI or stable address of the record, the version or the date you
    fetched it, and the checksum of the file. A file name and a size can
    be the same for two different files.

!!! success "Key points"
    - Cite the record: DOI, version or date, checksum.
    - Read the record before the data: what is one row, what may you
      publish.
    - Open to read is not open to pass on. Check the licence.

## 7. How the example file was made { #made }

<p class="block-meta">16:25 · 22 min · slides 39–47</p>

**Say.** The case study answers one question: where does a row of the
example file come from?

| Stage | Rate |
|--|--|
| Bunch crossings in the detector | 40 million per second |
| After the first trigger level | 100 000 per second |
| After the high-level trigger, written to storage | A few thousand per second |

!!! question "Exercise · slide 42 · 4 min"
    The Higgs discovery met the 5-sigma standard. What does that mean?

??? success "Solution"
    If there were no new particle, a fluctuation of the background this
    strong would appear in fewer than 1 in 3.5 million experiments. It is
    not the chance that the discovery is wrong.

!!! question "Exercise · slide 46 · 3 min"
    Why can the experiments not record everything?

??? success "Solution"
    Nothing can write about 1 PB per second to disk. The trigger reduces
    the output to what storage can take, before anyone judges what is
    interesting.

!!! success "Key points"
    - Fewer than one collision in a hundred thousand is stored.
    - A trigger decision is final. Deciding what to keep is data analysis.
    - The selection is code, written before anyone sees the data.

## 8. The file up close { #close }

<p class="block-meta">16:47 · 18 min · slides 48–56</p>

**Say.** Back to the file from the start, with everything from today.

!!! question "Ask the room · slide 52"
    What is the average decay time in the file? Ask for a guess, then show
    the table.

??? success "Solution"
    | | Rows | Mean | Median |
    |--|--|--|--|
    | All rows | 91 583 | −0.0525 ns | 0.00027 ns |
    | Without the rows marked `-100` | 91 534 | +0.00098 ns | 0.00027 ns |

    49 rows, 0.05% of the file, change the sign of the mean.

!!! question "Exercise · slide 55 · 3 min"
    What does one row of the example file represent?

??? success "Solution"
    One candidate pair of a kaon and a pion from one collision. The file
    cannot say which rows are a D⁰ and which are background. Only the whole
    column does, as a peak.

**Slide 53, five questions for any data file:**

1. How many rows and columns?
2. What is one row?
3. Which columns are measured, derived, bookkeeping?
4. What are the units, and where is that written?
5. How is a missing value marked?

!!! success "Key points"
    - Look at the smallest and the largest value of every column before
      computing anything.
    - Units are metadata. If the file does not say, the README must.
    - Answer the five questions before the first line of code.

## If time runs short

| Cut, in this order | Slides | Saves |
|--|--|--|
| The exercise on 5 sigma | 42 | 4 min |
| The exercise on recording everything | 46 | 3 min |
| From Events to Petabytes | 44 | 3 min |
| The exercise on provenance | 38 | 3 min |

Do not cut slides 17–20 (the broken table, dates, missing values), 25–29
(the file) or 49–53 (the example file). The seminars use them.

## For students to read

- K. Broman and K. Woo, *Data Organization in Spreadsheets*, The American
  Statistician, 2018
- G. Wilson and others, *Good Enough Practices in Scientific Computing*,
  PLOS Computational Biology, 2017
