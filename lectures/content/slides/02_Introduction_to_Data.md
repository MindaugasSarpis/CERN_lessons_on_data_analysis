---
layout: cover
title: "Introduction to Data"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Introduction to Data

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
Speaker: last time was the why. Today is the what: data itself. One file runs
through the lecture. First a table is built from a single number, then the
table becomes a file, then where a file comes from and how to write that down.
The case study is how the example file was made at LHCb, and the file itself
closes the lecture. No film clips today. (~2 min)
-->
---
hideInToc: true
layout: quote
---

# It is a capital mistake to theorize before one has **data**. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
Sherlock Holmes — Arthur Conan Doyle, *A Scandal in Bohemia*
---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📏 Write down a measurement completely: **value, unit, uncertainty**, and no more digits than are known

</div>

<div class="card card-secondary card-glass pad-compact">

📋 Read a **table**: observations in rows, variables in columns, and the **kind of variable** in each column

</div>

<div class="card card-accent card-glass pad-compact">

🧹 Find what is wrong with a table: mixed units, dates in two orders, a code in place of a missing value

</div>

<div class="card card-info card-glass pad-compact">

📄 Read a **CSV file** character by character, and say why it opens differently on two computers

</div>

<div class="card card-success card-glass pad-compact">

🌐 Find an **open dataset** and document it: portal, record, **DOI**, licence, provenance

</div>

<div class="card card-warning card-glass pad-compact">

⚛️ Trace how a **collision becomes a row** of the example file: detector, trigger, storage

</div>

</div>

<!--
Speaker: one file runs through the whole lecture. The first half builds a
table from a single number, step by step. The second half asks where a file
comes from and how the example file was made. (~1 min)
-->

---
hideInToc: true
---

# Today's **Example File**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`D0_KPi.csv`, lines 1–5**

```text
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
1913.8755,2542.169,0.00018464602,17.386473
1888.7571,4453.104,0.00056827645,56.79793
```

91 579 more lines follow. 3.9 MB of text.

</div>

<div class="card card-accent card-glass pad-compact">

## 📈 **Column `M`, all rows**

<img src="/figures/viz_example_d0_mass.svg" style="display:block;margin:0 auto;max-height:190px;">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

⚛️ Particle decays recorded by the **LHCb** experiment at CERN, published as open data. Four questions for today: what is **one row**, what **kind of value** is in each column, **where** did the file come from, and what is **wrong** with it?

</div>

<!--
Speaker: show the file before any definition. Ask what they can tell from five
lines: four names, commas, decimal points, no units. Then the plot: one column,
91 583 values, a peak. Do not explain the physics yet; the CERN section does.
Every section of the lecture comes back to this file. If VS Code is open, show
the real file instead of the slide. (~4 min)
-->
---
hideInToc: true
---

# What **Is** Data?

<div class="card card-info card-glass pad-tight mt-sm">

A working definition for this course: **data is recorded observation** — facts captured in a form a machine can store and re-read. The moment something is written down consistently enough to count, sort, or compare, it becomes data.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **It starts as a measurement**

A temperature, a timestamp, a momentum, a yes/no. On its own, one value says little.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📚 **It becomes useful in bulk**

Thousands of those values, organised, show what one reading cannot: a trend, a spread, a peak.

</div>

</div>
---
hideInToc: true
---

# Data Has a **Lifecycle**

<div class="grid-2 mt-sm gap-md">

<div>

<a href="https://datamanagement.hms.harvard.edu/" target="_blank"><img src="/figures/RDM_Lifecycle.png" style="display:block;margin:0 auto;width:350px;height:350px;"></a>

<div class="note-text" style="text-align:center;">Figure: Harvard Medical School</div>

</div>

<div>

<div class="card card-primary card-glass pad-compact">

## 🔁 **Six stages**

📥 Collect → 💾 Store → 🧹 Clean → 📊 Analyse → ✅ Decide → 🌐 Share / archive

</div>

<div class="card card-info card-glass pad-compact mt-md">

The figure names the stages differently; the cycle is the same. Every project — yours, a bank's, a physics collaboration's — walks it, and each answer raises fresh questions that restart it.

</div>

<div class="note-text mt-md">Most problems in practice come from skipping a stage: analysing before cleaning, or deciding before storing where the data came from.</div>

</div>

</div>
---
layout: section
hideInToc: true
---

# From a Number to a **Table**

<!--
Speaker: the next slides add one thing at a time to a single number, until it
is a table. Go fast through the large slides and ask at each: what is still
missing? (~1 min)
-->

---
layout: fact
hideInToc: true
---

# 1864.84

## <v-click> A number. It says nothing yet. </v-click>

---
layout: fact
hideInToc: true
---

# 1864.84 MeV/c²

## <v-click> A number with a **unit**: a mass </v-click>

---
layout: fact
hideInToc: true
---

# 1864.84 ± 0.05 MeV/c²

## <v-click> With an **uncertainty**: a measurement </v-click>

---
hideInToc: true
---

# What the Uncertainty **Says**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **1864.84 ± 0.05 MeV/c²**

The mass of the D⁰ meson, the average of many experiments. The true value lies between 1864.79 and 1864.89 with a probability of about 68%.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✂️ **It sets the number of digits**

The uncertainty is in the second decimal place, so the value is written to the second decimal place. `1864.8400000` claims seven digits that nobody measured.

</div>

</div>

| **Written** | **Reads as** |
| --- | --- |
| `1865` | Known to about 1 MeV/c² |
| `1864.84` | Known to about 0.01 MeV/c² |
| `1864.84 ± 0.05` | Known, and how well |
| `1864.8400000` | Copied from a calculator |

<!--
Speaker: the value is from the Particle Data Group. Ask for a measurement
from their own field and its uncertainty: a body temperature, a price, a
distance on a map. (~3 min)
-->

---
hideInToc: true
---

# Digits Written, Digits **Known**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **In the example file**

```text
M          TAU
1880.649   0.00041271152
1860.6599  0.0001864154
```

Up to eight digits for each value.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔬 **In the detector**

LHCb measures the mass of one K⁻π⁺ pair to about **8 MeV/c²**. Of `1880.649`, the first three digits are measured.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💾 The other digits come from the way the computer stores a number: 32 bits hold about seven decimal digits, and the file prints all of them. A file stores digits. Whether they mean anything is written in the metadata, or nowhere.

</div>

<div class="note-text mt-sm">Do not round the raw file. Round when you report: the digits cost nothing to keep and rounding cannot be undone.</div>

<!--
Speaker: 8 MeV is the width of the peak in the file itself, from a fit. The
point is not to distrust the file. It is that the number of digits in a file
is a property of the software that wrote it. (~3 min)
-->

---
layout: fact
hideInToc: true
---

# 1880.649, 3000.9534, 0.00041271152, 1299.1675

## <v-click> Four values that belong together: one **observation** </v-click>

<style>
h1 { font-size: 2.6rem; }
</style>

---
hideInToc: true
---

# Measurement vs **Metadata**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **The measurement**

The number you care about — the temperature, the price, the particle's momentum. The reason the record exists at all.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🏷️ **The metadata**

Data *about* the measurement — when, where, by which instrument, in what units, under what settings.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 🛰️ **Mars Climate Orbiter, 1999** 📁 ♻️

One team's software wrote the thruster impulse in **pound-force seconds**. The navigation software read the same numbers as **newton seconds**, a factor of 4.45. The specification asked for newton seconds, and nobody checked the file against it. The spacecraft entered the atmosphere of Mars too low and was lost.

</div>
---
hideInToc: true
---

# Anatomy of a **Table**

| **station** | **time** | **temp_C** | **pressure_hPa** | **sky** |
| --- | --- | --- | --- | --- |
| Vilnius | 2026-09-29 08:00 | 11.2 | 1018.4 | cloudy |
| Vilnius | 2026-09-29 09:00 | 12.0 | 1018.1 | cloudy |
| Kaunas | 2026-09-29 08:00 | 11.9 | 1017.6 | rain |

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➡️ **A row**

One observation: one station at one hour. Everything in the row belongs to that observation.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬇️ **A column**

One variable, of one kind, in one unit. `temp_C` is continuous; `sky` is nominal.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔲 **A cell**

One value. Not "11.2 °C (approx.)", not two readings, not a colour that carries meaning.

</div>

</div>

<div class="note-text mt-sm">Illustrative values. A table that keeps these three rules is called <strong>tidy</strong>, and every tool in this course expects it.</div>

<!--
Speaker: the table is made up for the slide. Point out that the unit sits in the
column name because a CSV file has nowhere else to put it. Ask: what is one row
in a spreadsheet you use? (~2 min)
-->
---
hideInToc: true
---

# Kinds of **Variables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Quantitative — continuous**

Any value in a range: a temperature of 21.4 °C, a mass of 1864.8 MeV. You can average it.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Quantitative — discrete**

Counts: goals scored, tracks in a collision. Whole numbers; you can still average them.

</div>

<div class="card card-accent card-glass pad-compact">

## 🏷️ **Categorical — nominal**

Labels with no order: city, blood group, particle type. You can count them, not average them.

</div>

<div class="card card-info card-glass pad-compact">

## 📶 **Categorical — ordinal**

Labels with an order: exam grades, low / medium / high. You can rank them; the size of a step is not defined.

</div>

</div>

<div class="note-text mt-md">Postcodes, phone numbers and ID numbers look like numbers and are not: the average of two postcodes means nothing. In the example file all four columns are continuous. A run number or a particle type would not be.</div>

<!--
Speaker: ask the Excel users which kind each column of a spreadsheet they know is.
The kind of variable decides the summary, the plot and the distribution. (~2 min)
-->
---
hideInToc: true
demo: 3
---

# A Table That **Breaks** the Rules

| **Station** | **29/09** | **30/09** | **Notes** |
| --- | --- | --- | --- |
| Vilnius | 11,2 °C | 12.0 | |
| | 12.4 | -999 | sensor replaced |
| Kaunas | 11.9 (approx.) | n/a | |
| **Mean** | **11.8** | **12.0** | |

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **Find seven problems** (2 min, with a neighbour)

What would a program make of each cell? It reads characters, and it cannot ask what was meant.

</div>

<div class="card card-info card-glass pad-compact">

## 🧑‍💻 **A person can read this table**

That is why such tables get made. Every problem in it is a decision that someone must take again, by hand, each time the table is used.

</div>

</div>

<!--
Speaker: give two minutes, then collect. The seven: dates as column names;
day and month in an order that depends on the country; a unit inside a cell;
decimal comma and decimal point mixed; an empty cell that means "same as
above"; three different signs for a missing value (-999, n/a, empty); a
comment inside a value; and a computed row (Mean) among the data, which makes
eight. A ninth: nothing tells the two Vilnius readings of one day apart. The
tidy table on the next slide needs a column for the hour. (~5 min)
-->

---
hideInToc: true
---

# The Same Data, **Tidy**

| **station** | **date** | **hour** | **temp_C** | **note** |
| --- | --- | --- | --- | --- |
| Vilnius | 2026-09-29 | 08 | 11.2 | |
| Vilnius | 2026-09-29 | 14 | 12.4 | |
| Kaunas | 2026-09-29 | 08 | 11.9 | reading approximate |
| Vilnius | 2026-09-30 | 14 | NA | sensor replaced |
| Kaunas | 2026-09-30 | 08 | NA | |

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**Every cell is filled.** A name is repeated in each row. A missing value has one sign, `NA`.

</div>

<div class="card card-secondary card-glass pad-compact">

**One thing in a cell.** The unit is in the column name, the comment in a column of its own.

</div>

<div class="card card-accent card-glass pad-compact">

**Only data.** The mean is computed from the table. It is not stored in it.

</div>

</div>

<div class="note-text mt-sm">Rules from K. Broman and K. Woo, <em>Data Organization in Spreadsheets</em>, The American Statistician, 2018.</div>

---
hideInToc: true
---

# 03/04/2026

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🇬🇧 **In London**

The 3rd of April.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🇺🇸 **In New York**

The 4th of March.

</div>

</div>

| **Written as** | **Sorted as text** | |
| --- | --- | --- |
| `03/04/2026`, `15/01/2026`, `20/12/2025` | `03/04/2026`, `15/01/2026`, `20/12/2025` | April, January, December |
| `2026-04-03`, `2026-01-15`, `2025-12-20` | `2025-12-20`, `2026-01-15`, `2026-04-03` | In the order of time |

<div class="card card-success card-glass pad-compact mt-md">

📅 **ISO 8601:** year, month, day, each with a fixed number of digits: `2026-04-03`. It cannot be misread, and sorting it as text sorts it by time. It is also how Lithuania writes a date.

</div>

---
hideInToc: true
---

# Missing Is Not **Zero**

| **In the cell** | **A program reads** | **Risk** |
| --- | --- | --- |
| empty | Missing, or an empty text, or 0 | Depends on the program |
| `0` | The number 0 | A temperature of 0 °C is a measurement |
| `-999`, `-100` | A number | It enters every sum and every mean |
| `n/a`, `-`, `?` | A text | The whole column is read as text |
| `NA`, `NaN` | Missing | Understood by most programs |

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The example file writes `-100` where a decay time could not be computed. Neither the file nor its record says so. The closing section shows what that does to the mean.

</div>

<div class="note-text mt-sm">Choose one sign for a missing value, use it in the whole table, and write it into the README.</div>

---
layout: section
hideInToc: true
---

# Kinds of **Data**

---
hideInToc: true
---

# Structured vs **Unstructured**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Structured**

Lives in neat rows and columns — a table, a spreadsheet, a database. Each column has a meaning and a type.

- Sensor logs, transaction records, survey answers
- Easy to sort, filter, and compute on directly
- **Most of this course lives here** — the tidy table

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌀 **Unstructured**

Free-form — text, images, audio, video. Rich, but a computer can't average it until you extract structure first.

- Emails, photos, recordings, PDFs
- Needs a step to turn it into numbers or labels
- Most machine learning works on this kind of data

</div>

</div>

<div class="note-text mt-md">The first real job of many projects is turning the second kind into the first.</div>
---
hideInToc: true
---

# Four **Flavours** of Data

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Numbers**

Measurements you can add, average, and plot. The core of statistics and fitting.

**As numbers:** already there — 21.4 °C, 1864.8 MeV.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔤 **Text**

Labels, categories, free comments. Countable once you decide what to count.

**As numbers:** one code per character (`A` = 65), or one count per category.

</div>

<div class="card card-accent card-glass pad-compact">

## 🖼️ **Images**

Grids of pixels. Most image analysis today is machine learning.

**As numbers:** a 12-megapixel photo = 12 million pixels × 3 colours, each value 0–255.

</div>

<div class="card card-info card-glass pad-compact">

## ⚡ **Events**

Timestamped things that happened — a click, a tap, a particle collision.

**As numbers:** a time, plus what was measured at that moment.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

## 🎛️ **Parametrisation**

Describing a thing by a set of numbers. Everything in a dataset can be expressed as numbers: a colour is 3 numbers, a place on Earth is 2 (latitude, longitude), a collision ends as one mass, 1864.8 MeV. Written as a number is not the same as behaving like one: a postcode has no average.

</div>

<!--
Speaker: parametrisation = choosing the set of numbers that describes a thing. A
computer stores and computes only numbers, so every flavour is written as numbers
before it is analysed. Walk the four cards and ask how each one becomes numbers.
More examples to say aloud: one second of CD sound is 44 100 samples; a particle
track in LHCb is five numbers. Bridge to the next slide: a postcode is written
in digits and still has no average. (~3 min)
-->
---
layout: section
hideInToc: true
---

# A Table as a **File**

<!--
Speaker: a table is an idea. On disk it is a row of characters. This section
is about what is lost and what is guessed on the way between the two. (~1 min)
-->

---
hideInToc: true
---

# A CSV File, Character by **Character**

```text
M,PT,TAU,IPCHI2⏎
1880.649,3000.9534,0.00041271152,1299.1675⏎
1860.6599,2803.4126,0.0001864154,0.34182164⏎
```

| **Character** | **Its job** | **What can go wrong** |
| --- | --- | --- |
| `,` | Ends a value | A value that contains a comma: `Vilnius, LT` |
| `.` | Decimal point | Half of Europe writes `1880,649` |
| `⏎` | Ends a row | Windows writes two characters here, macOS and Linux one |
| Line 1 | Names the columns | Nothing marks it as a header. It is a convention |
| `"` | Wraps a value that contains `,` | `"Vilnius, LT"` is one value |

<div class="note-text mt-sm">CSV stands for comma-separated values. The file holds characters only: no types, no units, no formatting. What is a number is decided by the program that reads it.</div>

<!--
Speaker: the file has no notion of a column. Count the commas in a line: three
commas, four values. A line with four commas would shift every value after the
extra one. (~3 min)
-->

---
hideInToc: true
---

# One Table, Three **Files**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **CSV — plain text**

- One line per row, values separated by commas
- Opens in any program, on any system
- Stores no types and no units: `11.2` is just four characters
- The example file: 91 583 rows, **3.9 MB**

</div>

<div class="card card-secondary card-glass pad-compact">

## 📗 **Spreadsheet — .xlsx**

- The table plus formatting, formulas, several sheets
- The program decides how a value is shown and stored
- It changes what it recognises: `SEPT2` becomes a date, `00123` becomes 123

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **Binary — ROOT, HDF5**

- Compact and fast, with a type for every column
- Readable only by a program that knows the format
- The same 91 583 rows as ROOT: **1.3 MB**

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ **Decimal comma or decimal point?** `1,5` and `1.5` are the same number written in two countries. A CSV file does not say which one it uses. A spreadsheet decides from the computer's regional settings, so the same file can open differently on two computers.

</div>

<!--
Speaker: the point is the comparison — the same table as plain text and as a
spreadsheet. Do not rush it. (~2 min)
-->
---
hideInToc: true
---

# The Same File on a **Lithuanian** Laptop

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🇬🇧 **English settings**

| A | B | C | D |
| --- | --- | --- | --- |
| M | PT | TAU | IPCHI2 |
| 1880.649 | 3000.9534 | 0.000412712 | 1299.1675 |

Four columns of numbers.

</div>

<div class="card card-warning card-glass pad-compact">

## 🇱🇹 **Lithuanian settings**

| A |
| --- |
| M,PT,TAU,IPCHI2 |
| 1880.649,3000.9534,0.00041271152,1299.1675 |

One column of text.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🌍 With Lithuanian settings a spreadsheet expects `;` between values and `,` inside a number. It finds no `;`, so each line is one value. The file is the same, byte for byte. A text editor shows the same characters on both laptops.

</div>

<div class="note-text mt-sm">Saving from the spreadsheet writes its reading back into the file. A file in <code>data/raw/</code> is opened in a spreadsheet to look at, and never saved from one.</div>

---
hideInToc: true
---

# Three Failures, None in the **Statistics**

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📉 **A cell range, 2010**

Reinhart and Rogoff's paper on public debt and growth was cited in budget debates worldwide. In 2013 a student who re-ran their spreadsheet found that the average left out **5 of 20 countries**: the formula stopped five rows early.

</div>

<div class="card card-warning card-glass pad-compact">

## 🦠 **A row limit, 2020**

Public Health England passed test results through the old `.xls` format, which holds **65 536 rows**. Rows beyond the limit were dropped without a message. **15 841** positive COVID-19 cases reached contact tracing up to a week late.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧬 **A cell format, 2016**

A check of 3 597 genetics papers with supplementary Excel files found gene names turned into dates, `SEPT2` into `2-Sep`, in about **one paper in five**.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔍 Each analysis used correct methods. Each failure happened while a table was stored, moved or opened. Which of the three could happen in your own field?

</div>

<!--
Speaker: three cases, one minute each. Sources: Herndon, Ash and Pollin (2013)
on Reinhart and Rogoff; the Public Health England statement of October 2020;
Ziemann, Eren and El-Osta (2016), Genome Biology. The point for the next
section: all three are caught by keeping the raw file untouched and writing
down what was done to it. (~4 min)
-->
---
hideInToc: true
---

# The Data **Dictionary**

<div class="note-text mt-sm">What the file cannot say is written next to it. For the example file:</div>

| **Column** | **Meaning** | **Unit** | **Kind** | **Missing** |
| --- | --- | --- | --- | --- |
| `M` | Mass of the kaon and the pion together | MeV/c² | continuous | none |
| `PT` | Momentum of the pair across the beam | MeV/c | continuous | none |
| `TAU` | Decay time of the candidate | ns | continuous | `-100` |
| `IPCHI2` | How well the pair points back to the collision | none | continuous | none |

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📖 **One row per column**

Name, meaning, unit, kind of variable, sign for a missing value. Five facts that the file does not hold.

</div>

<div class="card card-success card-glass pad-compact">

## 📁 **Where it lives**

In the README of the project, or in a file next to the data. It is written once and saves every later reader the same five questions.

</div>

</div>

---
hideInToc: true
demo: 3
---

# Thought Exercise — Data in **Your Field**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🤔 **Think** (2 min)

Pick a project, hobby, or job you know well.

- What data gets generated?
- Who collects it, and how?
- What decisions does it inform?

</div>

<div class="card card-secondary card-glass pad-tight">

## 💬 **Discuss** (3 min)

Share with a neighbour:

- What is one decision that could be improved if the data were better collected, stored, or analysed?
- What would "good enough" data analysis look like in your context?

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🎯 **Takeaway**

Keep your answer. The data you just described is a candidate for your semester project.

</div>
---
layout: section
hideInToc: true
---

# Open Data & **Provenance**

<!--
Speaker: shift gears — from *what data is* to *where you get it and how you prove
where it came from*. (~1 min)
-->
---
hideInToc: true
---

# Open-Data **Portals**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔬 **Physics & space**

- **CERN Open Data Portal** — LHC collision data, masterclass samples
- **NASA** open data & the Planetary Data System
- **ESA** archives — Gaia, Euclid, Webb

</div>

<div class="card card-secondary card-glass pad-compact">

## 🌍 **Society & environment**

- **Eurostat** and national statistics offices
- **Copernicus / ECMWF** — weather and climate
- **World Bank, OECD, WHO** indicators

</div>

<div class="card card-accent card-glass pad-compact">

## 📚 **Any field**

- **Zenodo** — upload anything, get a DOI
- **Kaggle**, **Hugging Face** datasets
- Your university's research repository

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔗 A portal is a **catalogue**: every dataset on it is a **record** with a stable address. You cite the record, not the file you happened to download.

</div>
---
hideInToc: true
---

# Anatomy of a **Record**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧾 **What every record carries**

- **Title** and authors / collaboration
- A **persistent identifier** — the DOI resolves forever, even if the portal moves
- **Licence** — what you may do with it
- **Files** with sizes and **checksums**
- **Description** — how the data was produced and selected
- **Version** and date

</div>

<div class="card card-accent card-glass pad-compact">

## ⚛️ **Record 401 — today's example**

- *LHCb event file for real measurement*
- DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR`
- Licence **CC0** — no conditions
- One **ROOT** file, 1.3 MB — particle decays recorded by LHCb at CERN
- Downloadable by anyone — no CERN account needed
- The workbook keeps a **CSV converted from it** — a derived file, and documented as one

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Reading the record *before* the data answers the questions you would otherwise ask the file: what is one row, which selection was applied, what am I allowed to publish.

</div>
---
hideInToc: true
---

# Licences — What “Open” **Actually Permits**

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🆓 **CC0**

No conditions at all — reuse, remix, republish. *CERN Open Data; NASA imagery is public domain, which amounts to the same.*

</div>

<div class="card card-primary card-glass pad-compact">

## 🏷️ **CC BY**

Do anything, but **credit the source**. *ESO and NOIRLab material.*

</div>

<div class="card card-warning card-glass pad-compact">

## 🔁 **ODbL, CC BY-SA**

Share-alike: derived datasets must stay **equally open**. *OpenStreetMap; most ESA imagery (CC BY-SA IGO).*

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

⚠️ **Open to read ≠ open to redistribute.** Some portals let you download but not re-host. Check the licence *before* you put the dataset online or pass it on — and before you publish a table derived from it.

</div>
---
hideInToc: true
---

# Provenance — **Write Down Where It Came From**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **The minimal provenance note**

- Portal + **record ID** and **DOI**
- **Licence**
- **Date** you fetched it (and record version)
- File names and their **checksums**
- What you did to it so far — *nothing* is a valid answer

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **As it looks in a README**

```text
Source:   CERN Open Data Portal, record 401
DOI:      10.7483/OPENDATA.LHCb.E7EJ.JUWR
Licence:  CC0
Fetched:  2026-09-29
Files:    MasterclassData.root  sha256 8694…039b
Changes:  none — D0_KPi.csv is a converted copy
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

♻️ Reproducibility starts **before** the analysis: someone else — or you in six months — must be able to fetch the **same bytes**. The checksum is how you prove it.

</div>
---
hideInToc: true
---

# Data You **Bring Yourself**

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

## 🎒 **Same discipline, your dataset**

- Where it came from — URL, instrument, survey, colleague
- Under what terms you may use and publish it
- A **snapshot**: the file exactly as received, plus its checksum
- The date — web data changes under you

</div>

<div class="card card-warning card-glass pad-compact">

## 🔒 **Personal or sensitive data**

- Anonymise before the file enters your project folder
- Never upload or e-mail raw personal data
- If in doubt: describe the data in the project, keep the file out of it

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🎯 Your semester project is on data of **your** choice — this checklist is what makes that choice safe to build on.

</div>
---
hideInToc: true
---

# From Record to **Your Project Folder**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧭 **Six steps**

1. **Find** the dataset's record on its portal
2. **Read** the record — DOI, licence, description
3. **Download** the file into `data/raw/`, without renaming
4. **Look** at it in a text editor — never edit or re-save it
5. **Write** the provenance note into `README.md`
6. **Test** — a neighbour finds it from your README alone

</div>

<div class="card card-secondary card-glass pad-compact">

## 📁 **An ordinary folder on your laptop**

```text
analysis-project/
├─ README.md        # where the data came from
├─ data/
│  ├─ raw/          # files exactly as downloaded
│  └─ processed/    # cleaned copies
├─ scripts/         # code
└─ results/         # plots and tables
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

♻️ File too large, or not yours to share? Pass on the README: it says exactly how to fetch the data again. That is the difference between "I have the data" and "the analysis is reproducible".

</div>
---
hideInToc: true
---

<MCQ
  question="You downloaded a CSV from a data portal six months ago and now want to cite it in your project so that a reader can get exactly the same data. What must you have recorded?"
  :options="[
    'The record\'s DOI or stable URL, the version or fetch date, and the file\'s checksum',
    'The file name, its size in bytes, and the folder you saved it into on your laptop',
    'The portal\'s homepage URL, the dataset\'s title, and the name of the collaboration',
    'The name and e-mail of the colleague who first told you about the dataset'
  ]"
  :correct="0"
  explanation="A DOI or stable record URL identifies the dataset independently of where the file sits today; the version or fetch date pins which release you used; the checksum proves the bytes are unchanged. Name and size can collide; a homepage plus a title can move or change silently, and a person's memory cannot be resolved to exact bytes."
/>
---
layout: section
hideInToc: true
---

# How the Example File Was **Made**

The case study. From a collision in the LHCb detector to a row in `D0_KPi.csv`.

<!--
Speaker: the case study. It answers one question: where does a row of the
example file come from? No tour of CERN; that was Lecture 1. (~1 min)
-->

---
hideInToc: true
---

# <span class="gradient-text">LHCb</span> — Matter and Antimatter

<div class="card card-primary card-glass pad-tight mt-sm">

## ⚖️ **The Question**

The Big Bang should have produced matter and antimatter in **equal amounts**, yet the universe is made of matter. LHCb measures the small **asymmetries** between the two (*CP violation*).

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔬 **The Method**

Precision measurements of **beauty** and **charm** quark decays, in a forward detector with sensors **millimetres** from the beam.

</div>

<div class="card card-warning card-glass pad-compact">

## 🏆 **A 2019 First**

LHCb observed **CP violation in charm**, in decays of the **D⁰ meson**: the particle in today's example file.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧭 The asymmetries measured so far are **far too small** to account for the matter in the universe. The question is open.

</div>
---
hideInToc: true
---

# Why <span class="gradient-text">Data Analysis</span> Matters at CERN

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-scale">

## 📊 **The Scale**

- The LHC produces **~1 PB per second** of raw detector output
- Only **~1 in a billion** collisions contains interesting physics
- Must filter, reconstruct, and analyse in near real time
- Finding the Higgs required sifting through **trillions** of events

</div>

<div class="card card-secondary card-glass pad-tight reveal-scale">

## 🔍 **Signal vs Background**

- Collision events produce **detector readings** (energy, momentum, position)
- Signal events look almost identical to background noise
- Statistical methods decide if a discovery is **real or a fluctuation**
- The 5-sigma standard: if there were **no new particle**, a background fluctuation this strong would appear in fewer than **1 in 3.5 million** experiments

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md glow">

💾 **Data Pipeline:** Raw detector signals &#8594; Trigger selection (real-time filtering) &#8594; Event reconstruction &#8594; Physics analysis &#8594; Statistical inference &#8594; Publication

<div class="mt-sm">

Each stage is a skill from this course, from handling files to statistical inference.

</div>

</div>
---
hideInToc: true
---

<div class="note-text">

*A check on the previous slide. Professionals get this one wrong too.*

</div>

<MCQ
  question="The Higgs discovery met the '5-sigma' standard. What does that actually mean?"
  :options="[
    'There is less than a one-in-3.5-million chance that the discovery itself is wrong',
    'With no new particle, a background fluke this strong shows up in fewer than 1 in 3.5 million experiments',
    'The Higgs mass was pinned down to five decimal places by combining ATLAS and CMS',
    'Five independent detectors each confirmed the signal at the same mass on the same day'
  ]"
  :correct="1"
  explanation="5 sigma limits how often pure background fakes a signal this strong — not the chance the discovery is wrong (option one's misreading)."
/>

<style>
.mcq-container { height: calc(100% - 3.5rem) !important; }
</style>
---
hideInToc: true
---

# From Collision to <span class="gradient-text">Dataset</span>

<div class="card card-info card-glass pad-compact mt-sm">

🚦 Nothing can store 1 PB **every second**, so the experiments decide **in real time** which collisions to keep. This selection is the **trigger**. It discards almost everything, within microseconds.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

💥 **~40 million bunch crossings** per second inside each detector — and a crossing is not a collision: each packs **dozens of overlapping proton–proton collisions**, about **1 billion collisions per second** in all

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

⚡ **Level-1 Trigger** — custom electronics decide in **microseconds** → ~**100,000** events/s survive

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🖥️ **High-Level Trigger** — a computing farm inspects the full event → a few **thousand** events/s written to storage

</div>

<div class="card card-success card-glass pad-compact reveal-left">

💾 Only these events become the **datasets** physicists analyse: fewer than **one collision in a hundred thousand** is stored

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

⚠️ A trigger decision is **final**: a discarded collision cannot be recovered. Deciding what to keep is itself data analysis.

</div>
---
hideInToc: true
---

# From Events to <span class="gradient-text">Petabytes</span>

<div class="card card-info card-glass pad-compact mt-sm">

🧮 The same chain in numbers, from one **event** to one **year** of data.

</div>

<div class="mt-md" style="text-align: center;">

```mermaid {scale: 0.85}
graph LR
    A[Crossings 40 MHz] --> B[L1 Trigger 100 kHz]
    B --> C[HLT few kHz]
    C --> D[Storage 10 GB/s]

    classDef stage fill:#0a1f3f,stroke:#38bdf8,color:#e8f1ff;
    class A,B,C,D stage;
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

## 📦 **The Arithmetic**

**~1–2 MB** per event × a few **thousand** events/s ≈ **10 GB/s** to disk and tape; × ~**10⁷ s** of beam per year ≈ **100+ PB per year**. One analysis uses a tiny part of that: today's example file is 1.3 MB.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **LHCb, Since Run 3**

No hardware trigger at all: every crossing — **30 million per second** — is read out in full and judged by a **software trigger** (its first stage on GPUs). That is the detector behind today's example dataset.

</div>

</div>
---
hideInToc: true
---

# Why It Has to Be <span class="gradient-text">Real-Time</span>

<div class="card card-info card-glass pad-compact mt-sm">

🎯 **Why not store everything?** Nothing can *write* 1 PB every second, and the detector cannot wait: the keep/discard decision has to be made in **microseconds**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⏱️ **25 ns Between Crossings**

Bunches cross every **25 nanoseconds**. The next collisions arrive long before any software has finished judging the last ones.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **A Few Microseconds of Memory**

The detector electronics can hold an event for only a few **microseconds**. If the first trigger level has not said "keep" by then, it is overwritten.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🔍 **What the trigger looks for:** a few high-energy leptons or jets, missing energy — or, at LHCb, tracks that **don't point back** to the collision, because a D⁰ flies a few millimetres before it decays. The selection is code, written before anyone sees the data.

</div>
---
hideInToc: true
---

<MCQ
  question="The detector electronics put out ~1 PB of raw signal per second, before any selection. Why can't the experiments simply record it all?"
  :options="[
    'There is no scientific reason to — only a handful of processes matter',
    'No real-time system can write ~1 PB/s to disk, even before counting the cost',
    'Data-protection rules cap how much CERN is legally allowed to store',
    'Only high-luminosity runs need a trigger — earlier runs recorded everything'
  ]"
  :correct="1"
  explanation="No storage system can sustain ~1 PB/s of writes. The trigger reduces the raw output to the few thousand events/s (~10 GB/s) that computing can absorb, before anyone judges what is interesting."
/>
---
hideInToc: true
---

# Working with the <span class="gradient-text">Data</span>

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-tight">

## 🔎 **The Analyst**

Takes last night's events, plots the mass of the D⁰ candidates and checks that it has not shifted, reports anything odd to the shift crew, corrects the shared analysis code. All on a laptop, anywhere in the world.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌙 **The Shift Crew**

Watches the same plot live in the control room. If a sub-detector or the trigger farm fails, the plot shows it, and the night's data is marked good or bad for everyone who uses it later.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🌍 Neither job is done next to the detector. Both need the skills of this course: files, code, version control, statistics.

</div>
---
layout: section
hideInToc: true
---

# A Dataset **Up Close**

<!--
Speaker: now open the example file, conceptually — no code yet. Apply the table
and variable slides from earlier to it. (~1 min)
-->
---
hideInToc: true
---

# From File to **Table**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The LHCb sample as a CSV file**

- One **header line** naming the columns
- **91 583** lines after it — the record says "about 60k events"; count for yourself
- Each **row** = one **candidate**: a K⁻π⁺ pair from one collision that might be a D⁰
- Each **column** = one quantity computed for that pair — four in all

</div>

<div class="card card-accent card-glass pad-compact">

## 🧮 **What a row says**

"In this collision we found a kaon and a pion that may have come from one D⁰: their combined mass is *M*, the pair's transverse momentum *PT*, it flew for a time *TAU* before decaying, and *IPCHI2* says how well it points back to the collision."

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💾 The CSV file is plain text. Today we read what it **means**.

</div>
---
hideInToc: true
---

# Columns, Units and **Meaning**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Measured**

Track momenta, charges, particle-ID scores — what the detector recorded. The ROOT file names these columns but ships them **empty**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Derived**

Computed from the tracks: invariant mass `M`, transverse momentum `PT`, decay time `TAU`, `IPCHI2` — the **four columns that are filled**.

</div>

<div class="card card-accent card-glass pad-compact">

## 🗂️ **Bookkeeping**

Event and run numbers — which collision, which data-taking period. Emptied here too; keep them in your own data.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ **Units are metadata.** A column named `M` means nothing until you know it is in MeV/c². Here neither the file nor the record says — you work it out (a D⁰ weighs 1865 MeV/c²) and write it into your README.

</div>
---
hideInToc: true
---

# What Column `M` **Shows**

<div class="grid-2 mt-sm gap-md">

<div>

<img src="/figures/viz_example_d0_mass.svg" style="display:block;margin:0 auto;max-height:300px;">

</div>

<div>

<div class="card card-primary card-glass pad-compact">

## ⛰️ **The peak**

Pairs that did come from a D⁰. Their mass is the same within the resolution of the detector, so they pile up at **1865 MeV/c²**.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 〰️ **The flat part**

A kaon and a pion that met by chance. Their combined mass can be anything, so they spread evenly.

</div>

<div class="card card-warning card-glass pad-compact mt-md">

No row says which of the two it is. Only the whole column does.

</div>

</div>

</div>

<!--
Speaker: the plot from the start of the lecture, now readable. One row is a
candidate, not a D0: the file cannot tell signal from background row by row.
This is also how the unit of M is found: the peak sits at the known D0 mass in
MeV. (~3 min)
-->
---
hideInToc: true
---

# 49 Rows Change the **Mean**

| **Decay time `TAU`** | **Rows** | **Mean** | **Median** |
| --- | --- | --- | --- |
| All rows | 91 583 | **−0.0525 ns** | 0.00027 ns |
| Without the rows marked `-100` | 91 534 | **+0.00098 ns** | 0.00027 ns |

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **A code, not a measurement**

In 49 rows the decay time could not be computed, and the file writes `-100` there. A program that does not know this averages them in. The result is a negative time.

</div>

<div class="card card-success card-glass pad-compact">

## 🔎 **How to find it**

Look at the smallest and the largest value of every column before computing anything. Here the smallest `TAU` is `-100`, in a column of values near 0.0003.

</div>

</div>

<div class="note-text mt-sm">49 rows are 0.05% of the file. The median does not move. The mean changes sign.</div>

<!--
Speaker: computed from the real file. Ask first: what is the average decay
time? Then show the table. Neither the file nor the record mentions -100; the
conversion script's comment does. Three more rows hold small negative times,
which are measurements, not codes. (~3 min)
-->
---
hideInToc: true
---

# Read Before You **Compute**

<div class="card card-primary card-glass pad-compact mt-sm">

## ❓ **Five questions for any data file**

1. How many **rows** and **columns** — and does the size make sense for that?
2. What is **one row** — an event, a person, an hour, a pixel?
3. Which columns are **measured**, which **derived**, which **bookkeeping**?
4. What are the **units** — and where is that written down?
5. How are **missing** or invalid values marked — blank, `NaN`, `-999`? *(This file: `TAU = -100`.)*

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Answer these on paper before the first line of code.

</div>
---
hideInToc: true
---

# Same Questions, **Your** Dataset

| | 🌦️ **Weather station** | 📋 **Survey** | 🖼️ **Image collection** |
| --- | --- | --- | --- |
| **One row** | One hour at one station | One respondent | One image file |
| **Measured** | Temperature, pressure, humidity | Answers, stored as codes | Pixels, in the image files |
| **Derived** | Daily mean | Total score | Label |
| **Bookkeeping** | Station, time | Respondent number | File name, size, time taken |
| **Units** | °C, hPa, % | Listed in the codebook | Bytes for the file size |

<div class="card card-info card-glass pad-compact mt-md">

🔁 Where the example file has the mass `M`, read *your own numeric variable*. Where it has a D⁰ candidate, read *one row of your data*.

</div>
---
hideInToc: true
---

<MCQ
  question="In the LHCb example sample, what does one row of the CSV file represent?"
  :options="[
    'One sub-detector of LHCb, with its readings for the run',
    'One column of momentum values, one per particle',
    'One reconstructed particle track through the detector',
    'One K⁻π⁺ candidate from one collision event'
  ]"
  :correct="3"
  explanation="Each row is one candidate pair found in one event: its invariant mass, transverse momentum, decay time and impact-parameter score. Columns are the quantities; rows are the things measured. Knowing what one row is comes before any statistics."
/>
---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Write a measurement with its **unit** and **uncertainty**, and with the digits that are known

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **table**, name the **kind of variable** in each column, and find what breaks its rules

</div>

<div class="card card-success card-glass pad-compact">

✅ Write dates as `2026-09-29` and a missing value with one sign

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **CSV file** character by character, and say why a spreadsheet may show it differently

</div>

<div class="card card-success card-glass pad-compact">

✅ Find an **open dataset**, read its **record** and write down its **provenance**

</div>

<div class="card card-success card-glass pad-compact">

✅ Say where a row of the example file comes from, and what is wrong with 49 of them

</div>

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each. (~1 min)
-->

---
layout: section
hideInToc: true
extra: true
---

# Extra **Material**

Data in everyday life and in other fields. Not part of the lecture.

---
layout: section
hideInToc: true
---

# Data in **Your Life**

---
hideInToc: true
---

# A Day in Data — **Morning**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⏰ **Before breakfast**

- Your phone logs the exact second the alarm went off
- A wearable scores how you slept — from heart rate and motion all night
- A weather app pushes a forecast computed from millions of sensor readings
- The battery graph has logged every charge and discharge of the past week

Ten minutes awake and you have already generated — and consumed — several datasets. None of it felt like "data".

</div>

<div class="card card-secondary card-glass pad-tight">

## 🚌 **The commute**

- A transit card taps in — a timestamp and a location, stored for years
- Maps reroutes you around traffic it inferred from other phones moving slowly
- Dozens of cameras log the same walk from different angles
- A playlist auto-queues songs a model predicts you'll keep

Each tap, ping, and skip is a row in someone's table — and the routing that helped you was itself built from yesterday's data.

</div>

</div>

---
hideInToc: true
---

# A Day in Data — **Afternoon to Lights-Out**

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-tight">

## 💻 **Work & screens**

- Every click, scroll, and pause feeds product-analytics dashboards
- A shop's "customers also bought" is a live recommendation model
- Each card payment is scored for fraud in under a second
- Spam filters classify every message before you see it

Most of this analysis runs with no person in the loop: the ⚙️ automation and ♻️ reproducibility this course teaches. You notice it only when it fails.

</div>

<div class="card card-info card-glass pad-tight">

## 🌙 **Evening**

- A streaming service picks your thumbnail from thousands of A/B tests
- A run is logged as a GPS track, then compared to last month's pace
- A smart meter reports the day's electricity in fine-grained slices
- The cycle closes as the wearable starts scoring tonight's sleep

From alarm to lights-out you moved through hundreds of small analyses — almost all of them made by someone else, about you.

</div>

</div>

---
hideInToc: true
---

# Every One of These Is a **Dataset**

<div class="card card-success card-glass pad-tight mt-sm">

Behind each convenience is the same loop you'll learn to run in this course: **collect → store → clean → analyse → decide → share**. The recommendation, the forecast, the fraud alert — all of it is somebody's pipeline running on somebody's table.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **Three questions for any app**

What does it **record**? In what **table** does that end up? Which **decision** does the result feed? Later today you ask the same of your own field.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎓 **What carries over**

The forecast, the playlist and the fraud check need the same four skills: organising files, writing code, statistics, reproducibility. Those are this course.

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="Across a whole day — alarm, transit card, recommendations, fraud checks — what makes all of it 'data analysis' rather than magic?"
  :options="[
    'Each one runs the same loop: collect, store, clean, analyse, decide — then share or archive',
    'Collecting and storing the readings is itself the analysis — once data is saved, the work is done',
    'Behind each service, analysts review your raw activity streams and decide case by case',
    'Each device analyses its own data locally, so nothing needs to be stored or cleaned first'
  ]"
  :correct="0"
  explanation="However different the domains look, they share one pipeline — collect, store, clean, analyse, decide, share. Recognising that shared shape is the whole point of these opening lectures: the skills transfer because the loop is always the same."
/>

---
hideInToc: true
---

# What Each Flavour Is **Used For**

| **Flavour** | **What is done with it** | **Example** |
| --- | --- | --- |
| 🔢 Numbers | Summarise, visualise, fit, report ± an error | Temperature, mass |
| 🔤 Text | Parse a line; code and count categories | Survey answers |
| 🖼️ Images | Pixels as arrays, then a classifier | Galaxy photographs |
| ⚡ Events | Turn one collision into a number (a mass) | Particle collisions |
| 📁 …and their files | Read, name, and organise safely | CSV, .xlsx, ROOT |

<div class="note-text mt-md">Nothing to memorise. Most datasets mix flavours: the weather table of the lecture holds numbers, text and timestamps.</div>

---
hideInToc: true
---

# Data at Work — **Biomedicine, Environment, Finance**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧬 **Biomedicine**

- Genome sequencing → variants, gene expression
- Clinical trials → safety, efficacy, adaptive designs
- Decisions: diagnostics, targeted therapies

🧪 <strong>23andMe</strong> went bankrupt in 2025 and its genetic database changed hands in the proceedings. The customers' consent went with it.

</div>

<div class="card card-accent card-glass pad-compact">

## 🌍 **Environment**

- Climate models fed by satellites, sensors, archives
- Pollution monitored at city-block resolution
- Decisions: policy, disaster response, conservation

🔄 Data feeds update the models continuously. The result is a pipeline that keeps running, not one final number.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💰 **Finance**

- Algorithmic trading under latency constraints
- Risk: stress tests, scenario analysis
- Fraud detection on streaming transactions

📉 Every participant models the other participants. A pattern found in past data stops working once people trade on it.

</div>

</div>

---
hideInToc: true
---

# Data at Work — **Astronomy & Particle Physics**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔭 **Astronomy**

- Observational data from telescopes, satellites, detectors
- Gravitational wave detection via signal processing & machine learning
- Cataloguing millions of celestial objects, anomaly detection
- Requires high-throughput computing, reproducible pipelines

🤖 <strong>Galaxy Zoo</strong> crowdsourced classifications of ~1M galaxies from SDSS images — the labelled set used to train today's automatic galaxy classifiers.

</div>

<div class="card card-accent card-glass pad-tight">

## ⚛️ **Particle physics (CERN)**

- Petabytes of collision data → reconstruct events, filter noise
- Multivariate analysis to isolate rare signals (e.g. Higgs boson)
- Collaboration across detectors, theory, computing teams
- Drives advances in distributed computing & open data practices

🔬 <strong>The lectures' example comes from here</strong>: open LHCb collision data, published by the collaboration itself.

</div>

</div>
