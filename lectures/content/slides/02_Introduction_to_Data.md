---
layout: cover
title: "Introduction to Data"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Introduction to Data

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
**Say:** a file arrives with no note. The lecture finds out what is in it, then writes the answers down.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# It is a capital mistake to theorize before one has **data**. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
Sherlock Holmes, Arthur Conan Doyle, *A Scandal in Bohemia*

---
hideInToc: true
---

# A File With No **Note**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **`weather.csv`, the first four lines**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
2016-01-01T02:00,-5.5,95,2.7
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **What the file shows**

A header with four names. Then lines of four values, with commas between them.

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **What it does not say**

Where it came from, what one line is, the units, and what is missing.

</div>

</div>

<div class="note-text mt-sm">87 673 lines, 2 515 215 bytes. Nothing else came with it.</div>

<!--
**Ask:** what can you say about this file? What can you not say?
**Do:** write the second list on the board.
(~4 min)
-->

---
hideInToc: true
---

# What the File Does **Not** Say

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | **Question** | **Where to look in the four lines** |
| --- | --- | --- |
| 1 | What **kind** is each column, and which can be **averaged**? | `time,temp_c,humidity_pct,wind_ms` |
| 2 | Where did the file **come from**, and may we use it? | Nowhere: 2 515 215 bytes and no note |
| 3 | What is **one row**? | `2016-01-01T00:00,-4.4,93,2.5` |
| 4 | In which **unit** is each column? | `-4.4`, `93`, `2.5` |
| 5 | How are **missing** values marked? | Not in these lines: 87 669 rows more to read |

</div>

<!--
**Say:** these are the room's own questions, each next to the part of the file it is about.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Data and **Information**

The file brought the symbols. The rule for reading them back did not come with it.

<!--
(~1 min)
-->

---
hideInToc: true
---

# What **Is** Data?

<div class="card card-info card-glass pad-tight mt-sm">

**Data** is a *reinterpretable representation of information in a formalized manner suitable for communication, interpretation, or processing.*

<div class="note-text mt-sm">ISO/IEC 2382, <em>Information technology, Vocabulary</em></div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔣 **Representation**

Symbols that stand for something. `-4.4` is not a temperature. It may stand for one.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Formalized**

Written by a fixed rule: which symbols, in which order, in which unit.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔁 **Reinterpretable**

Someone else, or a program, gets the information back. Without the rule, nobody can.

</div>

</div>

<!--
**Do:** read the definition once, then take the three words one at a time.
**Ask:** which of the three does `weather.csv` have? The symbols and part of the format: commas and a header. The rest of the rule is missing.
(~3 min)
-->

---
hideInToc: true
---

# Data Is Symbols Plus a **Rule**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔣 **The symbols**

```text
2016-01-01T00:00,-4.4,93,2.5
```

Data, as it arrived.

</div>

<div class="card card-success card-glass pad-compact">

## 📖 **With the rule**

At midnight on 1 January 2016, one weather station measured −4.4 °C, 93 % humidity and a wind of 2.5 m/s.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧭 **A number is data only together with the rule that lets someone else read it back.**

</div>

<!--
**Say:** the right card is information. Nobody can write it from the left card alone: the station, the units and what one line is are not in the file.
(~2 min)
-->

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

📥 Collect, 💾 Store, 🧹 Clean, 📊 Analyse, ✅ Decide, 🌐 Share and archive

</div>

<div class="card card-info card-glass pad-compact mt-md">

`weather.csv` stands after the second stage: stored, not yet cleaned. Its rule should have been written at the first two stages.

</div>

</div>

</div>

<!--
**Say:** every project passes these stages. Most trouble comes from a skipped stage: analysing before cleaning, or deciding before writing down where the data came from.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# How One Row Was **Made**

A row is a decision: what was measured, how often, and what was kept.

<!--
**Say:** question 3, what one row is.
(~1 min)
-->

---
hideInToc: true
---

# The Station Writes One Line per **Hour**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **The station**

Its sensors read many times an hour. It writes **one line per hour**: the time and the hour's values.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **How many lines**

24 a day. 365 × 24 = **8 760** a year, and **8 784** in a leap year.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

✂️ The readings inside each hour are not in the file. Someone decided that one hour is one row, and that decision is part of the file's rule.

</div>

<!--
**Ask:** what would one row be if the station wrote every minute? How many rows a year? (525 600)
(~2 min)
-->

---
hideInToc: true
---

# One Row at the Station and at the **LHC**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | 🌡️ **Weather station** | 💥 **A detector of the LHC** |
| --- | --- | --- |
| What happens | Sensors read many times an hour | **40 million** bunch crossings a second, dozens of collisions in each |
| What is kept | One line per hour | A few **thousand** collisions a second, chosen in microseconds by the **trigger** |
| One row | One hour | One kept collision |
| What is lost | The readings inside each hour | Every collision not kept |

</div>

<div class="note-text mt-md">Deciding what becomes a row is part of the analysis, and at the LHC it is written as code before anyone sees the data.</div>

<!--
**Say:** question 3 at the largest scale there is. The raw signal is about 1 PB a second; nothing can store it.
**If asked:** the trigger is electronics and a computer farm. Fewer than one collision in a hundred thousand is stored.
(~3 min)
-->

---
hideInToc: true
---

<VideoPlayer src="cern_video_2015_024_001.mp4" />

<!--
**Do:** let it run: the whole chain, 2:51, with music.
**Say:** accelerator chain, detectors, trigger, data centre, grid. Talk over it only at the trigger.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Reading the **File**

How many rows, in which units, and where the gaps are: the file itself shows it.

<!--
**Say:** questions 4 and 5 are answered from the file itself, by reading and by reasoning.
(~1 min)
-->

---
hideInToc: true
---

# How Many **Rows**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⬇️ **In a text editor**

`Ctrl+End` (macOS `Cmd+↓`) jumps to line **87 674**, and it is empty: the file ends with a line end.

87 673 lines − 1 header = **87 672 rows**.

</div>

<div class="card card-success card-glass pad-compact">

## 🧮 **By arithmetic**

2016 to 2025 is 10 years, 3 of them leap years:

```text
10 × 365 × 24 =  87 600
 3 ×   1 × 24 =      72
                 87 672
```

</div>

</div>

<!--
**Ask:** before showing the cards: how many rows should ten years of hours have?
**If asked:** any text editor has these keys.
**Say:** the count closes, so every hour has its row. That says nothing yet about the values in it.
(~3 min)
-->

---
hideInToc: true
---

# A Line in the **Middle**

<div class="card card-primary card-glass pad-compact mt-md">

## 🎯 **Go to line 5000: `Ctrl+G`**

```text
2016-07-27T06:00,18.2,71,1.1
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

🧮 Line 5000 is row 4 999: **4 998 hours** after the first one. 4 998 = 208 × 24 + 6: day 208 after 1 January, at 06:00. In the leap year 2016 that is **27 July**.

</div>

<!--
**If asked:** `Ctrl+G` is the same key on macOS.
**Say:** the line has the shape of row 1, and its time fits the count. The file is in order.
(~2 min)
-->

---
hideInToc: true
---

# Units by **Reasoning**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **`temp_c`**

From −16.3 to 32.4, median 6.7. In kelvin the median would be near 280. So **°C**, as `_c` says.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💧 **`humidity_pct`**

From 34 to 100, never above. **Percent**, as `_pct` says.

</div>

<div class="card card-accent card-glass pad-compact">

## 🌬️ **`wind_ms`**

`ms` reads as milliseconds or as metres per second. Median 3.5, at most 12.0: a breeze, a strong wind. So **m/s**.

</div>

</div>

<div class="note-text mt-md">A unit in a column name is a hint. The numbers have to agree with it.</div>

<!--
**Ask:** for each column, which unit fits, before showing its card. For `wind_ms` let the room argue: milliseconds of wind makes no sense.
**If asked:** the medians and ranges were computed on the whole file, without the 120 rows marked `-999`.
(~4 min)
-->

---
hideInToc: true
---

# How Missing Values Are **Marked**

<div class="card card-warning card-glass pad-compact mt-md">

## 🔎 **`Ctrl+F` (macOS `Cmd+F`), then `-999`**

**120 matches**, all in `temp_c`, from `2019-07-22T00:00` to `2019-07-26T23:00`: 5 days × 24 hours = 120.

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ −999 °C is below absolute zero, −273.15 °C. It is not a temperature. It is a **mark** for "no value": the sensor was down for five days.

</div>

<div class="note-text mt-md">Other files mark a missing value with an empty cell, <code>NA</code>, <code>-1</code> or <code>9999</code>.</div>

<!--
**Say:** question 5. The mark is a number, so every program that reads the file counts it as one.
(~3 min)
-->

---
hideInToc: true
---

# What a Mark Does to a **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Without the 120 marks**

Mean temperature over ten years: **7.16 °C**

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **With them, as numbers**

Mean temperature over ten years: **5.78 °C**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 120 × (−999) = −119 880 added to the sum. Spread over 87 672 rows: −119 880 / 87 672 = **−1.37 °C**. Five lost days move a ten-year mean by more than a degree.

</div>

<!--
**Say:** both means were computed on the file. Their difference is 1.38, the 1.37 of the arithmetic plus the five summer days that are missing.
**Say:** this is why the question how missing values are marked is asked before any number is computed.
(~2 min)
-->

---
hideInToc: true
---

# −999 in a **CERN File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **Simulated ATLAS collisions, CERN Open Data record 328: 4 of 35 columns**

```text
EventId,DER_mass_MMC,DER_deltaeta_jet_jet,PRI_jet_num
100000,138.47,0.91,2
100001,160.937,-999.0,1
100002,-999.0,-999.0,1
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Counted**

`DER_deltaeta_jet_jet` is the separation between the two jets of a collision. 327&nbsp;371 rows with no jet and 252&nbsp;882 with one: **580&nbsp;253** of 818&nbsp;238 hold −999.0.

</div>

<div class="card card-warning card-glass pad-compact">

## 📖 **What the mark means here**

A value that cannot exist for that row: one jet has no second one. The record's description says when each column is undefined.

</div>

</div>

<!--
**Say:** the same mark as at the station, with another meaning: there the sensor was down, here the quantity does not exist. A mean with the marks in it would be mostly marks: 71 % of the rows.
**If asked:** a jet is a narrow spray of particles. The file was made for a machine-learning challenge in 2014 and is CC0.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Kinds of **Data**

The first part of the rule: what kind of thing each column holds, and what may be computed from it.

<!--
**Say:** question 1.
(~1 min)
-->

---
hideInToc: true
---

# Everything as **Numbers**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| **Thing** | **As numbers** |
| --- | --- |
| A temperature | `-4.4` |
| An hour of the log | `2016-01-01T00:00` is hour 0, and `2025-12-31T23:00` hour 87 671 |
| A letter | `A` = 65 |
| A place on Earth | two numbers: latitude and longitude |
| One pixel of a photo | three numbers from 0 to 255: red, green, blue |
| A 12-megapixel photo | 12 million pixels × 3 = 36 million numbers |

</div>

<div class="note-text mt-md">Describing a thing by a set of numbers is called <strong>parametrisation</strong>. A computer stores and computes only numbers.</div>

<!--
**Say:** written as a number is not the same as behaving like one. A pixel value of 255 is a brightness; the 65 of `A` only names a letter.
(~2 min)
-->

---
hideInToc: true
---

# Kinds of **Variables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📋 **Four kinds**

| Kind | For example | Mean? |
| --- | --- | --- |
| 📏 Continuous | −4.4 °C, 2.5 m/s | yes |
| 🧮 Discrete | visitors, goals | yes |
| 🏷️ Nominal | city, station name | no: counted |
| 📶 Ordinal | grades, low to high | no: ranked |

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🌡️ **The columns of `weather.csv`**

| Column | Range | Kind |
| --- | --- | --- |
| `time` | 2016 to 2025, hourly | a time, in order |
| `temp_c` | −16.3 to 32.4 | continuous |
| `humidity_pct` | 34 to 100 | continuous |
| `wind_ms` | 0.0 to 12.0 | continuous |

</div>

</div>

<div class="note-text mt-md">Postcodes and ID numbers are written in digits and are labels: the mean of two postcodes means nothing.</div>

<!--
**Ask:** which kind is each column of a spreadsheet you know?
**Say:** the kind decides which summary and which plot make sense. A discrete count has no half visitor, and an ordinal step has no size.
(~3 min)
-->

---
hideInToc: true
---

# Anatomy of a **Table**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`daily_export.csv`**

```text
nr;date;temp_c
1;2025-10-01;6,3
2;2025-10-02;5,0
3;2025-10-03;5,6
4;2025-10-04;7,0
5;2025-10-05;9,4
6;2025-10-06;10,4
7;2025-10-07;9,2
8;2025-10-08;9,0
9;2025-10-09;9,8
;mean;7,97
```

</div>

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

## ➡️ **A row**

One observation: one day.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬇️ **A column**

One variable, of one kind, in one unit. `_c` in the name is the unit.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔲 **A cell**

One value. `6,3` is written with a decimal comma.

</div>

</div>

</div>

<div class="note-text mt-sm">Nine daily mean temperatures, exported from a spreadsheet. The last line is not a day.</div>

<!--
**Say:** a second file from the same station, small enough to read whole. 180 bytes.
**Ask:** what is one row? Which column is only a counter? Which line does not belong?
**Say:** a table with one observation per row, one variable per column and one value per cell is called tidy.
(~3 min)
-->

---
hideInToc: true
---

# Which Columns Can Be **Averaged**?

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **`nr`**

1 + 2 + … + 9 = 45, and 45 / 9 = **5.0**. A label for the row: its mean says nothing.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📅 **`date`**

The days are in order, and the middle one is 2025-10-05. A label for the day, not a measurement.

</div>

<div class="card card-accent card-glass pad-compact">

## 🌡️ **`temp_c`**

6.3 + 5.0 + … + 9.8 = 71.7, and 71.7 / 9 = **7.967**. The file's last line says `7,97`.

</div>

</div>

<!--
**Do:** let the room add up `temp_c` before you show the card: 6.3, 5.0, 5.6, 7.0, 9.4, 10.4, 9.2, 9.0, 9.8.
**Say:** the check closes: 7.967 rounds to the 7,97 of the last line.
(~3 min)
-->

---
hideInToc: true
---

# The Mean Line, **Left In**

<div class="card card-warning card-glass pad-compact mt-md">

## 😮 **Ten values instead of nine**

```text
(71.7 + 7.97) / 10 = 79.67 / 10 = 7.967
```

The same mean. A value equal to the mean does not move the mean.

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The mean cannot show that the line is there. The count can: **10 rows for 9 days**. One row is one observation, and a mean is not one.

</div>

<!--
**Ask:** before showing the card: what happens to the mean if the mean line is counted as a day? Most expect it to change.
(~2 min)
-->

---
hideInToc: true
---

# Measured or **Derived**?

<div class="card card-primary card-glass pad-compact mt-sm">

## 📏 **Measured: `temp_c` of `weather.csv`, 1 October 2025, 00:00 to 23:00**

```text
 3.9  3.9  2.7  2.8  3.1  3.5  3.8  4.8  5.9  6.9  7.5  8.2
 9.3  9.6 10.1  9.7  9.7  9.4  8.4  7.5  6.8  5.9  4.4  3.3
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Derived: the export's `6,3`**

The 24 values sum to 151.1, and 151.1 / 24 = 6.30: the line `1;2025-10-01;6,3`.

</div>

<div class="card card-accent card-glass pad-compact">

## 🗂️ **Bookkeeping**

`time`, `date`, `nr`: which hour, which day, which row.

</div>

</div>

<div class="note-text mt-md">A derived value is checkable only if the README says how it was computed.</div>

<!--
**Ask:** is the mean line of the export measured or derived?
**If asked:** the coldest hour of that day is 2.7 °C at 02:00, the warmest 10.1 °C at 14:00.
(~2 min)
-->

---
hideInToc: true
---

# File Formats for a **Table**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | **Format** | **`weather.csv`, 87 672 rows** | **Read by** |
| --- | --- | --- | --- |
| 📄 | CSV: plain text, one line per row | 2 515 215 bytes | any program, and a person |
| 📗 | Spreadsheet, `.xlsx`: a zip of XML files | 1 922 248 bytes | a program that knows the format |
| 📦 | Binary: four 4-byte numbers per row | 87 672 × 16 = 1 402 752 bytes | a program told the types and their order |

</div>

<div class="note-text mt-md">HDF5 and ROOT are binary formats that write the types into the file. CERN stores its collision data in ROOT files.</div>

<!--
**Say:** the same table in three formats. CSV is the largest, and the only one a person can read.
**If asked:** the .xlsx was written with Python's openpyxl 3.1.5; Excel writes another byte count. An .xlsx file is a zip archive of XML text files.
(~2 min)
-->

---
hideInToc: true
---

# Decimal Comma or **Point**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🇬🇧 **Point**

```text
2025-10-01,6.3
```

The comma separates the values.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🇱🇹 **Comma**

```text
2025-10-01;6,3
```

The comma is the decimal sign, so `;` separates the values.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A CSV file does not say which one it uses. A spreadsheet decides from the computer's regional settings, so one file opens differently on two computers.

</div>

<!--
**Say:** `daily_export.csv` came from a spreadsheet set to Lithuanian, so it has `;` and the decimal comma.
**Ask:** whose spreadsheet uses a decimal comma?
(~2 min)
-->

---
hideInToc: true
---

# Opened in a **Spreadsheet**

<div class="note-text mt-sm"><code>weather.csv</code>, with <code>,</code> between the values and <code>.</code> as the decimal sign, opened on three computers:</div>

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| On the screen | Reason |
| --- | --- |
| Every line in column A, as one text | The spreadsheet expects `;` between values |
| Columns, but numbers turned into text or dates | It expects `,` as the decimal sign |
| The right columns | The computer's settings match the file |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The file is the same on every laptop. The spreadsheet shows an **interpretation** of it, and saving writes that interpretation back. A file in `data/raw` is never saved from a spreadsheet.

</div>

<!--
**Say:** VS Code shows the same characters on every laptop. That is why data files are opened in a text editor.
(~2 min)
-->

---
hideInToc: true
---

# A Row as Text and as **Binary**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **As text**

`2016-01-01T00:00,-4.4,93,2.5` is 28 characters and a line end: **29 bytes**. The file: **2 515 215 bytes**, 28.7 per row.

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **As binary numbers**

Four numbers of 4 bytes each: **16 bytes** per row. 87 672 × 16 = **1 402 752 bytes**.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📏 The text copy is 2 515 215 / 1 402 752 = **1.8×** larger. Neither copy says what the numbers mean: that rule is written somewhere else.

</div>

<!--
**Say:** in text every digit is one byte; in binary a number has a fixed size, whatever its digits.
**If asked:** the time fits in 4 bytes as a count of hours from the first row.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Where the File **Came From**

Who made a file, and on what terms it may be used, is written where it was published.

<!--
**Say:** question 2.
(~1 min)
-->

---
hideInToc: true
---

# Open-Data **Portals**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| **Portal** | **Holds** | **For example** |
| --- | --- | --- |
| 🌍 Copernicus Climate Data Store | weather and climate | ERA5: hourly temperature on a grid, from 1940 |
| 📊 Eurostat, data.gov.lt | statistics of the EU and of Lithuania | prices, population, transport |
| ⚛️ CERN Open Data | particle physics | record 328: 818 238 simulated ATLAS collisions |
| 📚 Zenodo | any field | the data of a paper, with a DOI |

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔗 A portal is a **catalogue**. Each dataset on it is a **record** with a stable address. Cite the record, not the file you happened to download.

</div>

<!--
**Ask:** has anyone downloaded data from one of these? From where?
(~2 min)
-->

---
hideInToc: true
---

# Anatomy of a **Record**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| **A record carries** | ⚛️ **CERN Open Data, record 328** | 🌡️ **`weather.csv`** |
| --- | --- | --- |
| Title | ATLAS Higgs Boson Machine Learning Challenge 2014 | none |
| Identifier | DOI `10.7483/OPENDATA.ATLAS.ZBP2.M5T8` | none: an e-mail |
| Licence | **CC0** | CC0, stated in the e-mail |
| Files | one, 65 630 848 bytes, with its checksum | one, 2 515 215 bytes |
| Description | how the collisions were simulated; when a column is undefined | asked for by e-mail |

</div>

<div class="note-text mt-md">A DOI keeps working when the portal moves: <code>doi.org/</code> followed by the DOI leads to the record.</div>

<!--
**Say:** read the record before the data. Everything in the right column had to be asked for.
**If asked:** the file of record 328 is a compressed CSV, 818 238 rows and 35 columns.
(~2 min)
-->

---
hideInToc: true
---

# Open-Data **Licences**

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🆓 **CC0**

No conditions. Reuse, change, republish.

</div>

<div class="card card-primary card-glass pad-compact">

## 🏷️ **CC BY**

Anything, as long as the source is **credited**.

</div>

<div class="card card-warning card-glass pad-compact">

## 🔁 **CC BY-SA, ODbL**

Share-alike: what is made from it stays **equally open**. OpenStreetMap is an example.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

⚠️ Some portals allow a download and forbid putting the file online again. Check the licence before sharing data or a table made from it.

</div>

<!--
**Say:** CERN Open Data is CC0. Most open data portals state the licence on every record.
(~2 min)
-->

---
hideInToc: true
---

# Provenance, **Written Down**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **The minimal note**

- Source: portal and record, or who sent it
- **Licence**
- **Date** it was fetched or received
- File names, sizes, checksums
- What was done to it: "nothing" is an answer

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **For `weather.csv`**

```text
Source:   e-mail from the station's
          operator
Licence:  CC0, stated in the e-mail
Received: 2026-09-29
File:     data/raw/weather.csv,
          2 515 215 bytes
Changes:  none
```

</div>

</div>

<!--
**Say:** the file came with no note, but its sender is known. Ask once, then write the answers down.
**Say:** someone else, or you in six months, must be able to get the same bytes. A checksum, a fingerprint of the bytes, proves it.
(~2 min)
-->

---
hideInToc: true
---

# From Record to **Project Folder**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧭 **Six steps**

1. **Find** the record
2. **Read** it: DOI, licence, description
3. **Download** into `data/raw/`, name unchanged
4. **Look** at it, never edit it
5. **Write** the note into `README.md`
6. **Test**: a neighbour finds the data from the README alone

</div>

<div class="card card-secondary card-glass pad-compact">

## 📁 **One folder per project**

```text
weather-project/
├─ README.md
├─ data/
│  ├─ raw/
│  └─ processed/
├─ scripts/
└─ results/
```

</div>

</div>

<!--
**Say:** `data/raw` holds files exactly as received. Everything made from them goes elsewhere.
(~2 min)
-->

---
hideInToc: true
---

# The Five Questions, **Answered**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| | **Question** | 🌡️ **`weather.csv`** | ⚛️ **ATLAS file, record 328** |
| --- | --- | --- | --- |
| 1 | Kind of each column | A time, three continuous columns | Masses, momenta, angles; a count of jets; a label `s` or `b` |
| 2 | Where it came from | The station's operator, by e-mail; CC0 | CERN Open Data, with a DOI; CC0 |
| 3 | One row | One hour at one station | One simulated collision |
| 4 | Units | °C, %, m/s | Not stated; masses near 125, the Higgs mass in GeV, point to GeV |
| 5 | Missing values | `-999` in `temp_c`, 120 rows | `-999.0` where a value cannot exist |

</div>

<div class="note-text mt-md">None of the answers for <code>weather.csv</code> was in its four lines. Each one is part of the file's rule.</div>

<!--
**Do:** go back to the four lines of slide 3 for a moment and read row 1 with its units.
(~2 min)
-->

---
hideInToc: true
---

# The Five Questions for Other **Datasets**

<div class="table-compact">

| | 📋 **Survey** | 🖼️ **Image collection** | 🛒 **Online shop orders** |
| --- | --- | --- | --- |
| **Kind** | Ordinal, 1 to 5 | Pixels 0 to 255; a label | Counts, prices, a category |
| **Source** | Your questionnaire | An image archive | The shop's export |
| **Row** | One respondent | One image file | One order |
| **Units** | In the codebook | Pixels, bytes | Pieces, euros |
| **Missing** | A blank answer | A file that does not open | An empty delivery date |

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🤔 **Your turn**, 5 min

Pick a dataset from your own field and answer the five questions with a neighbour, on paper.

</div>

<!--
**Do:** give the room five minutes. Walk round and ask two or three people for question 2: where does the data come from, and may they publish what they make from it?
(~6 min)
-->

---
layout: section
hideInToc: true
---

# The **Editor**

The five answers are not in the file, so they are written next to it, in a README. Both are plain text, and one editor opens both.

<!--
**Say:** answers that stay in this room are lost.
(~1 min)
-->

---
hideInToc: true
---

# The Project **Folder**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **One project, one folder**

- Everything for one piece of work in one folder
- The same subfolders every time: `data/raw`, `data/processed`, `scripts`, `results`
- `README.md` at the top says what is where

</div>

<div class="card card-warning card-glass pad-compact">

## 🔒 **The rule for `data/raw`**

A file in `data/raw` is never edited. Changes are made on a copy in `data/processed`.

</div>

</div>

<!--
**Say:** a file in `data/raw` cannot be made again. Everything else can.
(~2 min)
-->

---
hideInToc: true
---

# Rules for File **Names**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Rule | Good | Not |
| --- | --- | --- |
| Small letters, no spaces | `daily_export.csv` | `Daily Export.csv` |
| Only `a` to `z`, digits, `-`, `_` | `zemaitija.csv` | `žemaitija.csv` |
| Dates as year, month, day | `2025-10-01.csv` | `1.10.2025.csv` |
| The name says what is inside | `weather.csv` | `data.csv` |

</div>

<div class="note-text mt-md">These names work on every system, in every program, and they sort by date.</div>

<!--
**Ask:** why does `2025-10-01` sort right and `1.10.2025` not? Text is sorted from the left, character by character.
**If asked:** `Data` and `data` are two folders on Linux and one on Windows and macOS: small letters avoid the question.
(~2 min)
-->

---
hideInToc: true
---

# The Editor: **VS Code**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧰 **What it is**

- A text editor: it shows the characters of a file and writes them back, nothing added
- Free, from `code.visualstudio.com`
- The same window on Windows, macOS and Linux

</div>

<div class="card card-secondary card-glass pad-compact">

## 📂 **Open a folder**

- **File**, **Open Folder…**, then the project folder
- **Do you trust the authors?** Yes, once
- The folder's name appears at the top of the Side Bar

</div>

</div>

<div class="note-text mt-md">VS Code works on a folder, not on one file. Every file of the project is then one click away.</div>

<!--
**If asked:** Windows: the User Installer needs no administrator password. macOS: drag the app into Applications.
(~2 min)
-->

---
hideInToc: true
---

# The Window: **Five Regions**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```text
+---+---------+----------------------+
|   |         |                      |
| 1 |    2    |          3           |
|   |         |                      |
|   |         +----------------------+
|   |         |          4           |
+---+---------+----------------------+
|                  5                 |
+------------------------------------+
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

| | Region | Holds |
| --- | --- | --- |
| 1 | **Activity Bar** | Icons that switch the Side Bar |
| 2 | **Side Bar** | The files: the **Explorer** |
| 3 | **Editor** | Open files, one tab each |
| 4 | **Panel** | Hidden at first; the terminal |
| 5 | **Status Bar** | Line, encoding, line ending |

</div>

</div>

<!--
**Do:** name the regions in order, 1 to 5.
(~2 min)
-->

---
hideInToc: true
---

# First Keys in **VS Code**

<div class="grid-3 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

## 🔍 **Command Palette**

`Ctrl+Shift+P`<br>(macOS `Cmd+Shift+P`)

Finds every command by part of its name.

</div>

<div class="card card-info card-glass pad-compact">

## ↔️ **Side Bar**

`Ctrl+B`<br>(macOS `Cmd+B`)

Hides it and brings it back.

</div>

<div class="card card-success card-glass pad-compact">

## 🔎 **Zoom**

`Ctrl+=` and `Ctrl+-`<br>(macOS `Cmd`)

Sets the size for the projector.

</div>

</div>

<div class="note-text mt-md">The Command Palette is the one key worth remembering: every other command can be found through it.</div>

<!--
**Say:** on macOS `Cmd` stands where Windows and Linux have `Ctrl`.
(~2 min)
-->

---
hideInToc: true
---

# Files in the **Side Bar**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🗂️ **Make and name**

- Mouse over the Side Bar: **New File** and **New Folder** appear
- A new item lands **inside the selected folder**
- `data/raw` as a name makes both folders
- `F2` (macOS `Enter`) renames

</div>

<div class="card card-secondary card-glass pad-compact">

## 📥 **Bring a file in**

- Drag it from **Downloads** onto a folder: it is copied there
- Right-click, **Reveal in File Explorer** (macOS **Reveal in Finder**) shows it in the file manager

</div>

</div>

<!--
**Say:** a new item lands inside the selected folder. That is the usual slip.
(~3 min)
-->

---
hideInToc: true
---

# Is the File **Saved**?

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚪ **A dot on the tab**

The file on disk still holds the old text. `Ctrl+S` (macOS `Cmd+S`) writes the new one.

</div>

<div class="card card-success card-glass pad-compact">

## 💾 **Auto Save**

**File**, **Auto Save**: every change is written at once.

</div>

</div>

<div class="note-text mt-md">The right end of the Status Bar names the file's encoding and line ending: <code>UTF-8</code>, <code>LF</code> or <code>CRLF</code>.</div>

<!--
**Say:** a program that reads the file reads the disk, not the tab. Unsaved text does not exist for it.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Markdown**

The README is written in Markdown: plain text with a few signs for structure.

<!--
(~1 min)
-->

---
hideInToc: true
---

# Source and **Preview**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **You type**, in `README.md`

```md
# Weather Station

Hourly log of one station, **2016 to 2025**.

- Data: `data/raw/weather.csv`
- Received: 2026-09-29
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **The preview shows**

<div class="rendered-md">
<p class="rendered-title">Weather Station</p>
<p>Hourly log of one station, <strong>2016 to 2025</strong>.</p>
<ul>
<li>Data: <code>data/raw/weather.csv</code></li>
<li>Received: 2026-09-29</li>
</ul>
</div>

</div>

</div>

<div class="note-text mt-md">The preview opens beside the text with <code>Ctrl+K</code>, then <code>V</code> (macOS <code>Cmd+K</code>, then <code>V</code>).</div>

<!--
**Say:** the left side is already readable. Nothing is hidden in the file. These slides are written in Markdown too.
(~2 min)
-->

---
hideInToc: true
---

# Headings & **Emphasis**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
# Title of the page
## Section
### Subsection

*italic*, **bold**, ~~struck out~~
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p class="rendered-title">Title of the page</p>
<p class="rendered-section">Section</p>
<p class="rendered-sub">Subsection</p>
<p><em>italic</em>, <strong>bold</strong>, <s>struck out</s></p>
</div>

</div>

</div>

<div class="note-text mt-md">A space follows the <code>#</code>. One title per page. The headings appear under <strong>Outline</strong> in the Explorer.</div>

<!--
(~1 min)
-->

---
hideInToc: true
---

# Paragraphs & **Lists**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
A single line break
does not show.

An empty line starts a paragraph.

- an item
  - indented by two spaces

1. first step
2. second step
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p>A single line break does not show.</p>
<p>An empty line starts a paragraph.</p>
<ul>
<li>an item
<ul>
<li>indented by two spaces</li>
</ul>
</li>
</ul>
<ol>
<li>first step</li>
<li>second step</li>
</ol>
</div>

</div>

</div>

<!--
**Say:** leave an empty line before a list, a table or a heading. The VS Code preview forgives a missing one; other programs do not.
(~2 min)
-->

---
hideInToc: true
---

# Links & **Images**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
[Copernicus](https://climate.copernicus.eu)

![The lifecycle](lifecycle.png)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p><a href="https://climate.copernicus.eu">Copernicus</a></p>
<p><img src="/figures/RDM_Lifecycle.png" alt="The lifecycle" style="width:150px;"></p>
</div>

</div>

</div>

<div class="note-text mt-md">An image file is looked for from the folder of the <code>.md</code> file. Backticks mark a file name: <code>`data/raw`</code>.</div>

<!--
**Say:** `[text](address)` is a link, `![description](file)` a picture.
(~2 min)
-->

---
hideInToc: true
---

# **Tables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
| date | temp_c |
|--|--|
| 2025-10-01 | 6.3 |
| 2025-10-02 | 5.0 |
| 2025-10-03 | 5.6 |
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<table>
<thead>
<tr><th>date</th><th>temp_c</th></tr>
</thead>
<tbody>
<tr><td>2025-10-01</td><td>6.3</td></tr>
<tr><td>2025-10-02</td><td>5.0</td></tr>
<tr><td>2025-10-03</td><td>5.6</td></tr>
</tbody>
</table>
</div>

</div>

</div>

<div class="note-text mt-md"><code>|</code> separates the cells. The second line, <code>|--|--|</code>, makes the first line the header.</div>

<!--
**Say:** without the second line there is no table. The cells need not line up in the source.
(~2 min)
-->

---
hideInToc: true
---

# Usual Markdown **Mistakes**

<div class="table-compact">

| **You type** | **The preview shows** | **Reason** |
| --- | --- | --- |
| `#Title` | `#Title` as text | No space after `#` |
| Two lines, one line break | One line | Only an empty line ends a paragraph |
| A table without `\|--\|--\|` | Text with `\|` signs | The second line makes the table |
| `**bold **` | The asterisks | A space before the closing `**` |
| `![plot](plot.png)` | A broken picture | The file is in another folder |

</div>

<!--
**Ask:** for each row, what goes wrong? Let the room answer before reading the reason.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Editing **Many Lines**

The daily table arrived in a spreadsheet's format. Each fix is the same on every line, and the editor makes it once.

<!--
**Say:** back to the nine-day table of slide 23. It is repaired here by hand, on a copy.
(~1 min)
-->

---
hideInToc: true
---

# What the Daily Table **Needs**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **As received**

```text
nr;date;temp_c
1;2025-10-01;6,3
2;2025-10-02;5,0
…
9;2025-10-09;9,8
;mean;7,97
```

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **As needed**

```text
date,temp_c
2025-10-01,6.3
2025-10-02,5.0
…
2025-10-09,9.8
```

</div>

</div>

<div class="note-text mt-md">Four fixes: the mean line out, the decimal comma to a point, <code>;</code> to <code>,</code>, the column <code>nr</code> out.</div>

<!--
**Ask:** what has to change? Let the room list the four fixes before showing the right card.
**Say:** the fixes are made on a copy, `data/processed/daily.csv`. The file in `data/raw` stays as it arrived.
(~2 min)
-->

---
hideInToc: true
---

# Keys for Whole **Lines**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Key | Does |
| --- | --- |
| `Ctrl+Shift+K` | Deletes the line |
| `Alt+↑` `Alt+↓` | Moves it |
| `Shift+Alt+↓` | Copies it below |
| `Ctrl+Z` | Undoes one step |

</div>

<div class="card card-success card-glass pad-compact">

## ✂️ **Fix 1**

Cursor in the line `;mean;7,97`, then `Ctrl+Shift+K`. Nothing has to be selected first.

</div>

</div>

<div class="note-text mt-md">macOS: <code>Cmd</code> for <code>Ctrl</code>, <code>Option</code> for <code>Alt</code>.</div>

<!--
**Say:** one row is one observation, and the mean line was not one.
(~2 min)
-->

---
hideInToc: true
---

# Find & **Replace**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **The tool**

- `Ctrl+H` (macOS `Cmd+Option+F`)
- The counter shows the matches: read it first
- **Replace All** changes every match

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **Fixes 2 and 3, in this order**

```text
Find   Replace   Matches
,      .          9
;      ,         20
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ In the other order, `1;2025-10-01;6,3` becomes `1,2025-10-01,6,3`, and the decimal comma can no longer be told from the others.

</div>

<!--
**Say:** 9 commas for nine rows, 20 semicolons for ten lines. The counter is read before Replace All.
(~3 min)
-->

---
hideInToc: true
---

# A Cursor on **Every Line**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Key | Does |
| --- | --- |
| Select lines, `Shift+Alt+I` | A cursor at each line end |
| `Ctrl+Alt+↓` | One more cursor below |
| `Alt`+click | One more cursor there |
| `Esc` | Back to one cursor |

</div>

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Type once**

```text
Alytus      →   - Alytus
Kaunas      →   - Kaunas
Vilnius     →   - Vilnius
```

Three cursors, `Home`, then `-` and a space.

</div>

</div>

<div class="note-text mt-md">macOS: <code>Shift+Option+I</code>, <code>Cmd+Option+↓</code>, <code>Option</code>+click. The Status Bar counts the cursors.</div>

<!--
**Say:** whatever is typed, deleted or pasted happens at every cursor.
(~2 min)
-->

---
hideInToc: true
---

# Lines of Different **Length**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧭 **Fix 4: the column `nr`**

1. `Ctrl+A`, then `Shift+Alt+I`
2. `Home`: all cursors to the line start
3. `Ctrl+Shift+→`: the first word
4. `Shift+→`: the comma too
5. `Delete`

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Before and after**

```text
nr,date,temp_c
1,2025-10-01,6.3
```

```text
date,temp_c
2025-10-01,6.3
```

</div>

</div>

<div class="note-text mt-md">macOS: <code>Cmd+A</code>, <code>Shift+Option+I</code>, <code>Cmd+←</code>, <code>Option+Shift+→</code>. <code>nr</code> is one character longer than <code>1</code>: the word key lands right on every line.</div>

<!--
**Say:** `→` moves each cursor by one character, so cursors on lines of different length drift apart. `Home`, `End` and the word keys do not.
(~3 min)
-->

---
hideInToc: true
---

# Select Every Match of a **Word**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Key | Does |
| --- | --- |
| Double-click | Selects a word |
| `Ctrl+D` | Adds the next match |
| `Ctrl+Shift+L` | Adds all matches |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **Rename a column**

```md
| date | temp_c |

- `temp_c`: daily mean, in °C
```

Both `temp_c` selected, then `t_mean_c` typed once.

</div>

</div>

<div class="note-text mt-md">macOS: <code>Cmd+D</code>, <code>Cmd+Shift+L</code>. Every place about to change shows a cursor before anything is typed.</div>

<!--
**Say:** unlike Replace All, you see every match before the change.
(~2 min)
-->

---
hideInToc: true
---

# CSV to Markdown **Table**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **The commas**

Select one comma, `Ctrl+Shift+L`, type ` | `.

```text
date | temp_c
2025-10-01 | 6.3
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **The line ends**

`Ctrl+A`, `Shift+Alt+I`, type ` |`. `Home`, type `| `.

```text
| date | temp_c |
| 2025-10-01 | 6.3 |
```

</div>

<div class="card card-accent card-glass pad-compact">

## 3️⃣ **The header**

`Ctrl+Enter` in line 1, then type `|--|--|`.

```text
| date | temp_c |
|--|--|
| 2025-10-01 | 6.3 |
```

</div>

</div>

<!--
**Say:** the preview shows a table only after step 3: the second line makes it.
**If asked:** a cursor on an empty last line gets a lone `|`; delete that line.
(~3 min)
-->

---
hideInToc: true
---

# Write Down What You **Changed**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **In `README.md`**

```md
- **Cleaned copy:**
  `data/processed/daily.csv`.
  Mean line deleted, `,` to `.`,
  `;` to `,`, column `nr` deleted
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **180 bytes became 148**

- `;mean;7,97` and its line end: **11**
- `nr;` and `1;` to `9;`: 3 + 9 × 2 = **21**
- The replacements: one character for one, **0**

180 − 11 − 21 = 148.

</div>

</div>

<div class="note-text mt-md">The next file needs all four fixes again. Without the list, nobody can tell that these 148 bytes came from those 180.</div>

<!--
**If asked:** the size is in the file manager: right-click, Properties on Windows, Get Info on macOS.
(~3 min)
-->

---
hideInToc: true
---

# Text Commands in the **Command Palette**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **`Ctrl+Shift+P`, then part of the name**

- **Sort Lines Ascending**
- **Transform to Uppercase**
- **Delete Duplicate Lines**
- **Toggle Word Wrap**

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Sorting sorts text**

```text
10.4
5.0
9.8
```

`10.4` comes first: the character `1` comes before `5`.

</div>

</div>

<div class="note-text mt-md">Dates written as <code>2025-10-01</code> sort right as text. Numbers of different length do not.</div>

<!--
**Say:** the editor sees characters, not numbers.
(~2 min)
-->

---
hideInToc: true
---

# The Keys on **One Page**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ↕️ **Lines and cursors**

| | Windows | macOS |
| --- | --- | --- |
| Delete the line | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Move the line | `Alt+↑` `Alt+↓` | `Option+↑` `Option+↓` |
| Copy the line down | `Shift+Alt+↓` | `Shift+Option+↓` |
| Cursor at each line end | `Shift+Alt+I` | `Shift+Option+I` |
| Cursor on the line below | `Ctrl+Alt+↓` | `Cmd+Option+↓` |

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔎 **Find and select**

| | Windows | macOS |
| --- | --- | --- |
| Find and Replace | `Ctrl+H` | `Cmd+Option+F` |
| Add the next match | `Ctrl+D` | `Cmd+D` |
| Add all matches | `Ctrl+Shift+L` | `Cmd+Shift+L` |
| One word | `Ctrl+←` `Ctrl+→` | `Option+←` `Option+→` |
| Line start, end | `Home` `End` | `Cmd+←` `Cmd+→` |

</div>

</div>

<div class="note-text mt-sm">Linux has the Windows keys, except a cursor below, <code>Shift+Alt+↓</code>, and copy down, <code>Ctrl+Shift+Alt+↓</code>.</div>

<!--
**Say:** nobody needs all ten. The three that pay off first: `Shift+Alt+I`, `Ctrl+D`, `Alt+↑`.
(~1 min)
-->

---
hideInToc: true
---

# The File, **Annotated**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
time,temp_c,humidity_pct,wind_ms     ← names; units only as hints
2016-01-01T00:00,-4.4,93,2.5         ← one hour at one station
2016-01-01T01:00,-4.8,95,2.6         ← 87 670 more rows like these
2019-07-22T00:00,-999,…              ← a mark: 120 hours with no value
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| **Column** | `time` | `temp_c` | `humidity_pct` | `wind_ms` |
| --- | --- | --- | --- | --- |
| **Unit** | ISO 8601, hourly | °C | % | m/s |
| **Seen in the file** | 87 672 hours, none missing | `-999` = no value | 34 to 100 | median 3.5 |

</div>

<div class="card card-success card-glass pad-compact mt-md">

🧭 **A number is data only together with the rule that lets someone else read it back.** Before computing on a file, write its rule into the README.

</div>

<!--
**Do:** read row 1 aloud once more, now with its units. Do not cut this slide: it closes the questions of slide 4.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Data is symbols plus a rule. `-4.4` became information when its kind, source, row and unit were found

</div>

<div class="card card-success card-glass pad-compact">

✅ A table: one row per observation, one variable per column. A mean line breaks the first rule, and only the count shows it

</div>

<div class="card card-success card-glass pad-compact">

✅ Provenance: source, licence, date, files. A row is a decision: one hour at a station, one kept collision at CERN

</div>

<div class="card card-success card-glass pad-compact">

✅ Units and missing marks come from the numbers when the file is silent. The README holds them, with every edit made to the data

</div>

</div>

<!--
**Say:** one line for each part of the rule.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="A colleague sends a file of numbers with no header and no note. By the definition of data, what is missing?"
  :options="[
    'Nothing: the numbers are the data, and the rest is decoration',
    'The rule that lets someone else read the numbers back: what each one is, in which unit, from where',
    'A larger sample: one file of numbers is too little to count as data',
    'A binary format, because plain text cannot hold data'
  ]"
  :correct="1"
  explanation="Data is a representation by a fixed rule that someone else can read back. The symbols arrived; the rule did not. -4.4 says nothing until its column, unit and source are known."
/>

---
hideInToc: true
---

<MCQ
  question="You downloaded a CSV from a data portal six months ago and want a reader to get exactly the same data. What must you have recorded?"
  :options="[
    'The record\'s DOI or stable URL, the version or fetch date, and the file\'s checksum',
    'The file name, its size in bytes, and the folder you saved it into on your laptop',
    'The portal\'s homepage URL, the dataset\'s title, and the name of its authors',
    'The name and e-mail of the colleague who first told you about the dataset'
  ]"
  :correct="0"
  explanation="A DOI or stable record URL identifies the dataset wherever the file sits today; the version or fetch date pins which release you used; the checksum proves the bytes are unchanged. Names and sizes can collide, and a homepage and a title can change."
/>

---
hideInToc: true
---

<MCQ
  question="The detectors of the LHC see about 40 million bunch crossings a second. Why is not every collision stored?"
  :options="[
    'There is no scientific reason to: only a handful of processes matter',
    'No system can write the raw signal, about 1 PB a second, to disk',
    'Data-protection rules cap how much CERN may store',
    'Only some runs need a trigger: the others record everything'
  ]"
  :correct="1"
  explanation="No storage system can take about 1 PB a second. The trigger keeps the few thousand collisions a second that computing can absorb, and decides before anyone sees the data."
/>

---
hideInToc: true
---

<MCQ
  question="A weather service publishes its station logs on an open portal, years after recording them. Which stage of the data lifecycle is that, and what makes it possible?"
  :options="[
    'Collecting: the stations write each reading straight to the portal',
    'Cleaning: the portal removes the readings that are not fit for publication',
    'Sharing: the last stage, possible only because provenance and formats were kept',
    'Analysing: the plots on the portal are the open data'
  ]"
  :correct="2"
  explanation="Publication is the share stage at the end of the lifecycle. It only works because the earlier stages kept the rule of the data: what a row is, the units, how values were marked."
/>

---
hideInToc: true
---

<MCQ
  question="In `weather.csv`, what does one row represent?"
  :options="[
    'One day at one station',
    'One hour at one station',
    'One reading of one sensor',
    'One station, with all its readings'
  ]"
  :correct="1"
  explanation="The station writes one line per hour: 24 rows a day, 8 760 a year, 87 672 for 2016 to 2025. The readings inside an hour are not in the file."
/>

---
hideInToc: true
---

<MCQ
  question="A column is named `wind_ms` and holds values from 0.0 to 12.0, median 3.5. Which unit fits?"
  :options="[
    'Milliseconds, because ms is the symbol for them',
    'Metres per second: 3.5 m/s is a breeze and 12 m/s a strong wind',
    'Kilometres per hour, because weather reports use them',
    'None: wind has no unit'
  ]"
  :correct="1"
  explanation="A unit in a name is a hint, and ms reads two ways. Wind is a speed; 3.5 m/s is a breeze and 12 m/s a strong wind. A wind of milliseconds makes no sense."
/>

---
hideInToc: true
---

<MCQ
  question="A file has lines like `1;2025-10-01;6,3`. They must become `1,2025-10-01,6.3`. Which two Replace All steps do that?"
  :options="[
    'First <code>;</code> to <code>,</code> and then <code>,</code> to <code>.</code>',
    'First <code>,</code> to <code>.</code> and then <code>;</code> to <code>,</code>',
    'Either order, because the result is the same',
    'Neither: the decimal commas have to be retyped by hand'
  ]"
  :correct="1"
  explanation="Replace the decimal comma while it is still the only comma in the file. In the other order the line first becomes 1,2025-10-01,6,3, and nothing tells the decimal comma from the others."
/>

---
hideInToc: true
---

<MCQ
  question="An editor sorts three lines as text: `10.4`, `5.0` and `9.8`. Which line comes first?"
  :options="[
    'The line 5.0, because 5.0 is the smallest number',
    'The line 10.4, because the character 1 comes before 5 and 9',
    'The line 9.8, because it is the last one typed',
    'None: lines that hold numbers cannot be sorted'
  ]"
  :correct="1"
  explanation="Sorting text compares characters from the left, and 1 comes before 5. To sort by value the column has to be read as numbers, which a text editor does not do."
/>
