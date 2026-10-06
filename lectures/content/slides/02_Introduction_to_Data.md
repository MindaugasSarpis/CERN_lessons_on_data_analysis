---
layout: cover
title: "Introduction to Data"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Introduction to Data

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
Speaker: Lecture 1 ended its reel at LHCb and said the seminars use the same
events physicists used. Today opens on that file, four lines of it, and asks
what can be said about it. Every section answers one of the questions it
raises. (~1 min)
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

# A File With No **Note**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **`D0_KPi.csv`, the first four lines**

```text
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
1913.8755,2542.169,0.00018464602,17.386473
```

**91 584 lines, 3 926 142 bytes.** Nothing else came with it: no note, no units, no word on where it was made.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **What the file shows**

A header line with four names. Then lines of four numbers, separated by commas. Every line has the same shape.

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **What is in it?**

Is `1880.649` a mass, a price, a distance? In which unit? Is one line one person, one second, one collision?

</div>

</div>

<div class="note-text mt-sm">Lecture 1 promised real data, the same events physicists used. This is that file, opened in a text editor.</div>

<!--
Speaker: leave the four lines up and ask "what is in this file?" Collect what the
room can say (a header, commas, four numbers per line, about 91 583 rows) and
what it cannot (what a number stands for, its unit, where the file came from,
what one line is). Write the second list on the board: it becomes the next
slide. (~4 min)
-->

---
hideInToc: true
---

# What the File Does **Not** Say

<div class="card card-info card-glass pad-compact mt-sm">

Five questions the four lines cannot answer. The sections of this lecture answer them in this order, and the closing slide writes the answers onto the same four lines.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

1️⃣ What **kind** of variable is each column, and which ones can be **averaged**?

</div>

<div class="card card-secondary card-glass pad-compact">

2️⃣ Where did the file **come from**, and may we publish what we make from it?

</div>

<div class="card card-accent card-glass pad-compact">

3️⃣ What is **one row**: a person, an hour, a collision?

</div>

<div class="card card-success card-glass pad-compact">

4️⃣ In which **unit** is each column?

</div>

<div class="card card-warning card-glass pad-compact">

5️⃣ How are **missing** values marked? Some lines have `-100.0` in `TAU`.

</div>

</div>

<!--
Speaker: these are the room's own questions from the last slide, in the order
the lecture answers them. Point at the part of the four lines each one is about:
the columns, the file as a whole, one line, the numbers, the -100.0. (~2 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🔣 Say what turns symbols into **data**: a rule that lets someone else read them back

</div>

<div class="card card-secondary card-glass pad-compact">

📋 Read a **table**: rows as observations, columns as variables, the **kind** of each, and which can be averaged

</div>

<div class="card card-accent card-glass pad-compact">

🌐 Find a dataset's **record** and write down its **provenance**, and trace how a **collision** became one row

</div>

<div class="card card-success card-glass pad-compact">

📄 Work out a file's **units** from its numbers, and write them into a **README** in Markdown

</div>

</div>

<!--
Speaker: four objectives, one per question group of the last slide. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Data and **Information**

The file holds a header and four numbers per line. The symbols arrived; what they stand for did not.

---
hideInToc: true
---

# What **Is** Data?

<div class="card card-info card-glass pad-tight mt-sm glow">

**Data** is a *reinterpretable representation of information in a formalized manner suitable for communication, interpretation, or processing.*

<div class="note-text mt-sm">ISO/IEC 2382, <em>Information technology — Vocabulary</em></div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔣 **A representation**

Symbols that stand for something: digits, letters, pixels. `1880.649` is not a mass. It may stand for one.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Formalized**

Written by a fixed rule: which symbols, in which order, in which unit. A file format and a column name carry that rule.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔁 **Reinterpretable**

Another person, or a program, gets the information back from the symbols. Without the rule nobody can.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🧭 **A number is data only together with the rule that lets someone else read it back.** The four lines of `D0_KPi.csv` came with the symbols and almost none of the rule.

</div>

<div class="note-text mt-sm"><code>1880.649</code> is data. "One K⁻π⁺ pair recorded by LHCb has the mass 1880.649 MeV/c²" would be information: the data together with its rule. Each part of that sentence is found in this lecture.</div>

<!--
Speaker: read the definition once, then take its three words one at a time. A
representation: the symbols are not the thing. Formalized: there is a rule.
Reinterpretable: the rule lets someone else read it back. Then point back at the
four lines: which of the three does the file have? The representation and part
of the format (commas, a header); the rest of the rule is missing. The sentence
at the bottom is what the lecture builds up, one part per section. (~3 min)
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

📥 Collect → 💾 Store → 🧹 Clean → 📊 Analyse → ✅ Decide → 🌐 Share / archive

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every project passes these stages, from the first measurement to the archive. `D0_KPi.csv` stands after the second stage: stored, not yet cleaned.

</div>

<div class="note-text mt-md">Most problems in practice come from skipping a stage: analysing before cleaning, or deciding before storing where the data came from. The rule of a file is written at the first two stages, or it is lost.</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Kinds of **Data**

A file needs a rule to be read back. The first part of that rule is what kind of thing each column holds, and that shows only in a table laid out by fixed rules.

<!--
Speaker: question 1 of the hook. Three ideas: the kind of variable, the shape of
a table, the format of a file. They are worked on a second, smaller file first,
a pendulum table from a lab, and then carried back to D0_KPi.csv. (~1 min)
-->

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
- `D0_KPi.csv` is structured: a header, then four values on every line

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

# Numbers, Text, Images, **Events**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Numbers**

Measurements you can add, average, and plot. The core of statistics and fitting.

**As numbers:** already there — 21.4 °C, 1864.8 MeV/c².

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

Describing a thing by a set of numbers. Everything in a dataset can be expressed as numbers: a colour is 3 numbers, a place on Earth is 2 (latitude, longitude), a collision ends as one mass, 1864.8 MeV/c². Written as a number is not the same as behaving like one — next slide.

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
hideInToc: true
---

# Kinds of **Variables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Quantitative — continuous**

Any value in a range: a temperature of 21.4 °C, a mass of 1864.8 MeV/c². You can average it.

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

<div class="note-text mt-md">Postcodes, phone numbers and ID numbers look like numbers and are not: the average of two postcodes means nothing. The kind of variable decides which plot and which statistic make sense.</div>

<!--
Speaker: ask the Excel users which kind each column of a spreadsheet they know is.
The kind of variable decides the summary, the plot and the distribution. (~2 min)
-->

---
hideInToc: true
---

# Anatomy of a **Table**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`pendulum_raw.csv`, as received**

```text
nr;length_cm;t10_s
1;20;9,02
2;30;11,05
3;40;12,61
4;50;14,23
5;60;15,49
6;70;16,84
7;80;17,90
8;90;19,10
9;100;20,01
;mean;15,14
```

130 bytes from a lab partner: the time of 10 swings of a pendulum for nine lengths.

</div>

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

## ➡️ **A row**

One observation: one length, timed. Everything in the row belongs to it.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬇️ **A column**

One variable, of one kind, in one unit. The unit sits in the name, `_cm` and `_s`, because a CSV file has nowhere else for it. That is **metadata**: data about the measurement.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔲 **A cell**

One value. `9,02` is one value, written with a decimal comma.

</div>

</div>

</div>

<div class="note-text mt-sm">A table that keeps these three rules is called <strong>tidy</strong>. The last line, <code>;mean;15,14</code>, breaks the first one: a mean is not an observation.</div>

<!--
Speaker: a second file, small enough to read whole. Ask what one row is (one
length), which column is set by the experimenter (length_cm), which is measured
(t10_s), and which is only a counter (nr). Then ask which line does not belong.
(~3 min)
-->

---
hideInToc: true
---

# Which Columns Can Be **Averaged**?

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **`nr`**

1 + 2 + … + 9 = 45, and 45 / 9 = **5.0**. A label for the row, like a postcode: its mean says nothing.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **`length_cm`**

20 + 30 + … + 100 = 540, and 540 / 9 = **60 cm**. Continuous, but chosen by the experimenter, not measured.

</div>

<div class="card card-accent card-glass pad-compact">

## ⏱️ **`t10_s`**

9.02 + 11.05 + … + 20.01 = 136.25, and 136.25 / 9 = **15.139 s**. The file's own last line says `15,14`: the check closes.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 😮 **Leave the mean line in**

(136.25 + 15.14) / 10 = 151.39 / 10 = **15.139 s**: the same mean. A value equal to the mean does not move the mean, so the mean cannot show that the line is there. The count can: 10 rows for 9 lengths.

</div>

<div class="note-text mt-sm">Question 1 of the hook, answered for <code>D0_KPi.csv</code>: its four columns are continuous, and each one can be averaged.</div>

<!--
Speaker: let the room add up t10_s before showing it (136.25). Then ask what
happens to the mean if the mean line is left in. Most will expect it to change.
It does not: adding a value equal to the mean keeps the mean. That is why a mean
line in a table is dangerous, and why one row has to be one observation. (~4 min)
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
- Stores no types and no units: `9.02` is just four characters

</div>

<div class="card card-secondary card-glass pad-compact">

## 📗 **Spreadsheet — .xlsx**

- The table plus formatting, formulas, several sheets
- The program decides how a value is shown and stored
- The file itself is a zip archive of XML text files

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **Binary — ROOT, HDF5**

- Compact and fast, with a type for every column
- Readable only by a program that knows the format
- What large experiments and data services use

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ **Decimal comma or decimal point?** `1,5` and `1.5` are the same number written in two countries. A CSV file does not say which one it uses. A spreadsheet decides from the computer's regional settings, so the same file can open differently on two computers. `pendulum_raw.csv` uses the comma.

</div>

<!--
Speaker: the point is the comparison: the same table as plain text, as a
spreadsheet and as a binary file. The next slide measures it on the LHCb file.
(~2 min)
-->

---
hideInToc: true
---

# One Table, Two **Sizes**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`D0_KPi.csv`, text**

**3 926 142 bytes** for 91 583 rows. 3 926 142 / 91 583 = **42.9 bytes per row**. Row 1, `1880.649,3000.9534,0.00041271152,1299.1675`, is 42 characters and a line end, one byte each.

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **`MasterclassData.root`, binary**

**1 289 541 bytes** for the same rows. 1 289 541 / 91 583 = **14.1 bytes per row**. Four numbers of 4 bytes each make 16, and ROOT compresses them below that.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 😮 **147 columns, and still 3× smaller**

The ROOT file declares **147 columns**. Only 4 are filled, and the CSV keeps those 4. Yet the text copy is 3 926 142 / 1 289 541 = **3.0×** larger: the empty columns cost almost nothing, and a number written as text takes about 10 characters.

</div>

<div class="note-text mt-sm">Neither file says what the numbers are. The ROOT file stores a type for each column, the CSV not even that. The rest of the rule has to be written down somewhere else.</div>

<!--
Speaker: the CSV in the workbook is a converted copy of the ROOT file in the
record. Count the first row together: 8 + 1 + 9 + 1 + 13 + 1 + 9 = 42
characters, plus the line end. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Where the File **Came From**

Column names and commas are only part of a file's rule. Who recorded the file, and on what terms it may be used, is written in the record it was published with.

<!--
Speaker: question 2 of the hook. From what the numbers are to where the file
came from, and how to write that down so someone else can fetch the same
bytes. (~1 min)
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
- One **ROOT** file, 1 289 541 bytes — particle decays recorded by LHCb at CERN
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

# Licences: CC0, CC BY, **Share-Alike**

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

♻️ Someone else, or you in six months, must be able to fetch the **same bytes**; the checksum is how you prove it. It belongs to the record's ROOT file. `D0_KPi.csv` has other bytes, so the note says how it was made: by `root_to_csv.py`.

</div>

---
hideInToc: true
---

# Your Own **Dataset**

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

♻️ Lecture 1 kept `data/raw/` out of every rebuild because it cannot be regenerated. A file too large, or not yours to share, stays out of the folder you pass on, and the README says how to fetch it again. The README is where the file's rule is written down.

</div>

---
layout: section
hideInToc: true
---

# How One Row Was **Made**

Record 401 names the experiment that recorded the file: LHCb. It is one of four detectors on the LHC ring, and each of them asks a different question.

<!--
Speaker: question 3 of the hook, what one row is, starts here. ATLAS and CMS
share one slide; ALICE and LHCb get one each. ATLAS, CMS and ALICE have a silent
3D fly-in from the ring to the detector: talk over the clips. LHCb has a 0:47
clip instead; the file comes from LHCb. (~1 min)
-->

---
hideInToc: true
---

# <span class="gradient-text">ATLAS</span> & <span class="gradient-text">CMS</span>

<div class="card card-info card-glass pad-compact mt-sm">

🔭 Two **general-purpose** detectors. Same physics programme: the Higgs boson, searches for new particles. **Different designs**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🏟️ **ATLAS**

- The **largest** collider detector ever built
- **46 m** long, **25 m** in diameter, 100 m underground
- ~**7,000 tonnes**, ~100 million readout channels

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧲 **CMS**

- One superconducting **solenoid** magnet, **3.8 T**
- **21 m** long, **15 m** in diameter
- **14,000 tonnes**: half the size of ATLAS, twice the weight

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🤝 On **4 July 2012** both announced the Higgs **independently, on the same day**. The LHC was built with two general-purpose detectors so that each result can be checked by the other.

</div>

---
hideInToc: true
---

<VideoPlayer src="cern_footage_2022_042_003.mp4" />

<!-- ATLAS — 3D fly-in from the LHC ring to the detector (0:38, silent). -->

---
hideInToc: true
---

<VideoPlayer src="cern_footage_2022_042_002.mp4" />

<!-- CMS — 3D fly-in from the LHC ring to the detector (0:39, silent). -->

---
hideInToc: true
---

# <span class="gradient-text">ALICE</span> — Quark–Gluon Plasma

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💥 **The Question**

What was matter like in the first **millionths of a second** after the Big Bang, before protons and neutrons existed?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌡️ **The Method**

Collide **lead nuclei** instead of protons. For an instant the collision forms **quark–gluon plasma**, over **100,000×** hotter than the core of the Sun.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

📈 One lead–lead collision can produce **tens of thousands** of particle tracks. Software has to reconstruct every one of them before any physics is done.

</div>

---
hideInToc: true
---

<VideoPlayer src="QGP_Formation.mp4" />

<!-- Quark–gluon plasma forming (0:33) — ALICE's physics. -->

---
hideInToc: true
---

<VideoPlayer src="cern_footage_2022_042_004.mp4" />

<!-- ALICE — 3D fly-in from the LHC ring to the detector (1:10, silent). -->

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

LHCb observed **CP violation in charm**, in decays of the **D⁰ meson**. Each row of `D0_KPi.csv` is a K⁻π⁺ pair that may come from one.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧭 The asymmetries measured so far are **far too small** to account for the matter in the universe. The question is open.

</div>

---
hideInToc: true
---

<VideoPlayer src="LHCb.mp4" />

<!-- LHCb reel (0:47) — where the example file comes from. -->

---
layout: section
hideInToc: true
---

# From Collision to **Row**

Each of the four detectors, LHCb among them, sees the bunches cross 40 million times a second. Almost every collision is thrown away within microseconds, and what is kept becomes rows.

<!--
Speaker: from the detectors to what they keep. The section ends on one row of
the file and the two columns that come from the selection. (~1 min)
-->

---
hideInToc: true
---

# From Collision to <span class="gradient-text">Dataset</span>

<div class="card card-info card-glass pad-compact mt-sm">

🚦 The raw signal comes to about 1 PB **every second**. Nothing can store that, so the experiments decide **in real time** which collisions to keep. This selection is the **trigger**. It discards almost everything, within microseconds.

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

<VideoPlayer src="cern_video_2015_024_001.mp4" />

<!-- The whole data flow in one clip (2:51, music): accelerator chain, detectors, trigger levels, data centre, the grid. -->

---
hideInToc: true
---

# From Events to <span class="gradient-text">Petabytes</span>

<div class="card card-info card-glass pad-compact mt-sm">

🧮 The same chain in numbers, from one **event** to one **year** of data, and back down to one **row** of the file.

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

**~1–2 MB** per event × a few **thousand** events/s ≈ **10 GB/s** to disk and tape; × ~**10⁷ s** of beam per year ≈ **100+ PB per year**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **One Row of the File**

1 289 541 bytes / 91 583 rows = **14 bytes** per candidate in the ROOT file. A stored event is 1–2 MB, about **100 000×** more. The row keeps four numbers computed from two of the event's tracks.

</div>

</div>

---
hideInToc: true
---

# What the Trigger **Kept**

<div class="card card-info card-glass pad-compact mt-sm">

⏱️ Bunches cross every **25 ns**: 1 s / 40 000 000 crossings. The electronics hold an event for a few **microseconds**, and a collision not kept by then is overwritten. The keep or discard decision is code, written before anyone sees the data.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **What it looks for in charm**

A D⁰ flies a few millimetres before it decays, so its kaon and pion tracks **do not point back** to the collision. The trigger keeps such pairs.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **LHCb, Since Run 3**

No hardware trigger at all: every crossing, **30 million per second**, is read out in full and judged by a **software trigger**, its first stage on GPUs.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

📄 Two columns of the file measure that flight. `TAU` is the time the candidate flew before it decayed. `IPCHI2` says how well the pair, taken together, points back to the collision: row 2's `0.34182164` points back well, row 1's `1299.1675` does not.

</div>

<div class="note-text mt-sm">Question 3 of the hook, answered: one row is one K⁻π⁺ pair that the selection kept from one collision. The selection is part of the file's rule.</div>

<!--
Speaker: point at rows 1 and 2 of the hook. Ask which of the two pairs looks
more like a D⁰ made in the collision itself (row 2: it points back). (~3 min)
-->

---
layout: section
hideInToc: true
---

# Reading the **File**

The record and the trigger say how a row was made. How many rows there are, and in which units, only the file itself can show.

<!--
Speaker: back to the four lines of the hook, now in VS Code on the projector.
Questions 4 and 5 are answered here, by clicking and by reasoning. (~1 min)
-->

---
hideInToc: true
---

# One Row, **Read Aloud**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The file as a table**

- One **header line** naming the four columns
- Each **row** = one **candidate**: a K⁻π⁺ pair from one collision that might be a D⁰
- Each **column** = one quantity computed for that pair

</div>

<div class="card card-accent card-glass pad-compact">

## 🧮 **What row 1 says**

"In one collision LHCb found a kaon and a pion that may have come from one D⁰. Their combined mass is `M` = 1880.649, the pair's transverse momentum `PT` = 3000.9534, it flew for `TAU` = 0.00041271152 before decaying, and `IPCHI2` = 1299.1675 says it points back badly."

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💾 Every number in that sentence still lacks its unit, and the sentence says nothing yet about the other 91 582 rows.

</div>

<!--
Speaker: read row 1 aloud as a sentence, then ask a student to read row 2 the
same way. (~2 min)
-->

---
hideInToc: true
---

# Three Questions, **Clicked**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⬇️ **How many rows?**

`Ctrl+End` jumps to line **91 585**, and it is empty: the file ends with a line end. 91 584 lines minus the header = **91 583 rows**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **And in the middle?**

`Ctrl+G`, then `5000`:

`1868.8636,5537.248,`<br>`0.0007151779,10.399748`

Four numbers again, the shape of row 1.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔎 **Where are the gaps?**

`Ctrl+F`, then `-100`: **49** matches, each one `-100.0` in `TAU`. No decay lasts −100 of anything. It marks "no valid time", as the converter's notes say.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

😮 **The record says "about 60k events" and lists 53 948. The file has 91 583 rows.** 91 583 / 53 948 = 1.7 rows per event: a row is a candidate, not a collision, and one collision can hold more than one K⁻π⁺ pair. Which rows share a collision the file cannot say; its event-number column is empty.

</div>

<div class="note-text mt-sm">macOS: <code>Cmd+↓</code>, <code>Ctrl+G</code>, <code>Cmd+F</code>. Question 5 of the hook, answered: <code>-100.0</code> marks a missing time, in 49 rows.</div>

<!--
Speaker: do the three on the projector with D0_KPi.csv open in VS Code. Before
Ctrl+End, ask the room to guess the row count from the record. (~4 min)
-->

---
hideInToc: true
---

# 147 Columns, **4 Filled**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Measured**

Track momenta, charges, particle-ID scores: what the detector recorded. The ROOT file names these columns but ships them **empty**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Derived**

Computed from the tracks: invariant mass `M`, transverse momentum `PT`, decay time `TAU`, `IPCHI2`. The **four columns that are filled**.

</div>

<div class="card card-accent card-glass pad-compact">

## 🗂️ **Bookkeeping**

Event and run numbers: which collision, which data-taking period. Emptied here too; keep them in your own data.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ **Units are metadata, and here they are missing.** Neither the file nor the record says which unit a column is in. The numbers themselves carry enough to work it out.

</div>

---
hideInToc: true
---

# Units by **Reasoning**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚖️ **`M`**

Median of the 91 583 values: **1864.08**. A D⁰ weighs **1864.84 MeV/c²**. In GeV/c² it would be more than ten times the heaviest elementary particle, the top quark at 173 GeV/c². So **MeV/c²**.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⏱️ **`TAU`**

Median: **0.000272**. A D⁰ lives on average **0.41 ps = 0.00041 ns**. Read in ns, the median is 0.27 ps, the same size. In seconds it would be 660 million times too long. So **ns**.

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **`PT`, `IPCHI2`**

`PT` comes from the same tracks as `M`, in the same units: median 3 049, so **MeV/c**, about 3 GeV/c. `IPCHI2` is a distance divided by its uncertainty, squared: **no unit**.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ **Two checks.** The busiest 5-unit bin of `M` is 1860 to 1865, with 8 931 candidates: the D⁰ peak, where MeV/c² puts it. Half of all decays come within ln 2 × 0.41 = 0.28 ps; the file's median is 0.27.

</div>

<div class="note-text mt-sm">Question 4 of the hook, answered, and checked: the notes of <code>root_to_csv.py</code>, which made the CSV, list the same four units.</div>

<!--
Speaker: ask the room for each unit before showing the card. For TAU, let them
try seconds first: 0.27 ms is a lifetime 660 million times the D0's. The
medians were computed with pandas on the whole file. (~5 min)
-->

---
hideInToc: true
---

# The Five Questions, **Answered**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| | **Question** | **`D0_KPi.csv`** |
| --- | --- | --- |
| 1 | Kind of each column | Four continuous columns; each one can be averaged |
| 2 | Where it came from | Record 401, DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR`, CC0; converted from `MasterclassData.root` |
| 3 | One row | One K⁻π⁺ pair, kept by the trigger from one collision |
| 4 | Units | `M` MeV/c², `PT` MeV/c, `TAU` ns, `IPCHI2` none |
| 5 | Missing values | `-100.0` in `TAU`, 49 rows |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Five answers, and none of them was in the four lines. Each one is part of the file's rule, found on the record, in the trigger or in the numbers themselves.

</div>

<!--
Speaker: the hook, answered. Go back to the four lines of slide 3 for a moment
and read row 1 with its units. (~2 min)
-->

---
hideInToc: true
---

# The Five Questions, **Your Dataset**

| | 🌦️ **Weather station** | 📋 **Survey** | 🖼️ **Image collection** |
| --- | --- | --- | --- |
| **Kind** | Continuous | Ordinal, 1 to 5 | Pixels 0–255; a label |
| **Source** | A weather portal | Your questionnaire | An image archive |
| **Row** | One hour at one station | One respondent | One image file |
| **Units** | °C, hPa, % | Listed in the codebook | Bytes for the file size |
| **Missing** | A gap in the hours, or `-999` | A blank answer | A file that does not open |

<div class="card card-accent card-glass pad-compact mt-md">

## 🤔 **Your turn** (5 min)

Pick a dataset from your own field and answer the five questions for it with a neighbour, on paper, before any code. Keep the answers: they are the first lines of your project README.

</div>

<!--
Speaker: give the room five minutes. Walk round and ask two or three people
for their answer to question 2: where does the data come from, and may they
publish what they make from it? (~6 min)
-->

---
layout: section
hideInToc: true
---

# Markdown & **Text Editing**

The five answers are not in the file, so they are written next to it in a README. A README is plain text like the data, and so is the pendulum table, which still needs its repair.

<!--
Speaker: the example file was plain text, and so is the README that describes
it. This section is the tools for text files: where they go, how the notes are
written, and how many lines are changed at once. Show each slide live in VS Code
as you go. (~1 min)
-->

---
hideInToc: true
---

# The **Project Folder**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **One project, one folder**

- Everything that belongs to one piece of work sits in one folder
- The subfolders are the same in every project: `data/raw`, `data/processed`, `scripts`, `results`
- A file in `data/raw` is never edited. Changes are made on a copy in `data/processed`
- `README.md` at the top says what is where

</div>

<div class="card card-secondary card-glass pad-compact">

## 🏷️ **Names**

- Lowercase and without spaces: `pendulum_run2.csv`, not `Pendulum Run 2.csv`
- Only `a` to `z`, digits, `-` and `_`. No `ą`, `č`, `š`, `ž`
- Dates as `2026-09-29`, so that the names sort by date
- The name says what is inside: `pendulum.csv`, not `data.csv`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📝 A data file and a README are both **plain text**. One program opens both: a **text editor**. This course uses **VS Code**. It is free and works the same on Windows, macOS and Linux. Every step shown here exists in other editors too.

</div>

<!--
Speaker: the tree itself was on the slide "From Record to Your Project Folder".
Here the rules: one folder, the same subfolders, raw is never edited, and names
that survive every system. Open the folder in VS Code and show it. (~2 min)
-->

---
hideInToc: true
---

# **Markdown**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **You type**, in `README.md`

```md
# Pendulum

Time of 10 swings for **nine** lengths.

- Data: `data/raw/pendulum.csv`
- Measured: 2026-09-29
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **The preview shows**

<div class="rendered-md">
<p class="rendered-title">Pendulum</p>
<p>Time of 10 swings for <strong>nine</strong> lengths.</p>
<ul>
<li>Data: <code>data/raw/pendulum.csv</code></li>
<li>Measured: 2026-09-29</li>
</ul>
</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📝 Markdown is plain text with a few signs for structure. The file name ends in `.md`. Any editor opens it, and it can be read without the preview. In VS Code the preview opens beside the text with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

</div>

<div class="note-text mt-sm">The same file can become a web page, a PDF or a set of slides. These slides are written in Markdown.</div>

<!--
Speaker: type these six lines live and open the preview beside them. The point
is that the left side is already readable. Nothing is hidden in the file. (~2 min)
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

<div class="card card-info card-glass pad-compact mt-md">

A space follows the `#`. A page has one title with a single `#`. More `#` signs make a smaller heading. The headings are the outline of the page: VS Code lists them under **Outline** in the Explorer.

</div>

---
hideInToc: true
---

# Paragraphs & **Lists**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
A paragraph is one or more lines.
A single line break does not show.

An empty line starts a new paragraph.

- an item
- another item
  - indented by two spaces

1. first step
2. second step
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p>A paragraph is one or more lines. A single line break does not show.</p>
<p>An empty line starts a new paragraph.</p>
<ul>
<li>an item</li>
<li>another item
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

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Leave an **empty line** between blocks: before a list, a table or a heading. The preview in VS Code forgives a missing one. Other programs that read Markdown do not.

</div>

---
hideInToc: true
---

# Links, Images & **File Names**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**, in `results/report.md`

```md
[CERN Open Data](https://opendata.cern.ch)

![Time against length](pendulum_plot.png)

The plot is made by `scripts/plot.py`.
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p><a href="https://opendata.cern.ch">CERN Open Data</a></p>
<p><img src="/figures/pendulum_plot.png" alt="Time against length"></p>
<p>The plot is made by <code>scripts/plot.py</code>.</p>
</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`[text](address)` is a link. `![description](file)` shows a picture; the file is looked for starting from the folder of the `.md` file. Backticks mark a file name or a piece of code.

</div>

---
hideInToc: true
---

# **Tables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
| length_cm | t10_s |
|--|--|
| 20 | 9.02 |
| 30 | 11.05 |
| 40 | 12.61 |
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<table>
<thead>
<tr><th>length_cm</th><th>t10_s</th></tr>
</thead>
<tbody>
<tr><td>20</td><td>9.02</td></tr>
<tr><td>30</td><td>11.05</td></tr>
<tr><td>40</td><td>12.61</td></tr>
</tbody>
</table>
</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`|` separates the cells. The second line, `|--|--|`, makes the first line the header: without it there is no table. The cells need not line up in the source. `|--:|` aligns a column to the right, which suits numbers.

</div>

---
hideInToc: true
---

# Markdown — **Usual Mistakes**

| **You type** | **The preview shows** | **Reason** |
| --- | --- | --- |
| `#Title` | `#Title` as plain text | The space after `#` is missing |
| Two lines, one line break between | One line | Only an empty line ends a paragraph |
| A table without `\|--\|--\|` | Text with `\|` signs | The second line makes the table |
| `**bold **` | The asterisks, and no bold | A space stands before the closing `**` |
| `![plot](plot.png)` | A broken picture | The file is in another folder |

<div class="note-text mt-md">The preview is the test. Keep it open and read it after every block you type.</div>

<!--
Speaker: make each mistake live and let the room say what is wrong. (~2 min)
-->

---
hideInToc: true
---

# One Edit, **Many Lines**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **The file as received**

```text
nr;length_cm;t10_s
1;20;9,02
2;30;11,05
3;40;12,61
…
9;100;20,01
;mean;15,14
```

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **The file as needed**

```text
length_cm,t10_s
20,9.02
30,11.05
40,12.61
…
100,20.01
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A lab partner saved this table from a spreadsheet on a computer set to Lithuanian: `;` between the values, `,` as the decimal sign, a row number, a line with the mean. Each fix is the same on every line. By hand that is about 40 edits. The editor makes each fix once.

</div>

<div class="note-text mt-sm">Example values: the time of 10 swings of a pendulum for nine lengths.</div>

<!--
Speaker: this is the decimal-comma card from "One Table, Three Files", now as a
file someone sent. Ask the room to list what has to change before showing the
right-hand side. The original stays in data/raw; the work is done on a copy in
data/processed. (~2 min)
-->

---
hideInToc: true
---

# Find & **Replace**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **The tool**

- `Ctrl+H` opens Find and Replace (macOS `Cmd+Option+F`)
- The counter shows how many places match. Read it before you replace: 9 commas for nine rows, 20 semicolons for ten lines
- **Replace All** changes every match at once
- `Ctrl+Z` takes it back

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **Two replacements, in this order**

```text
Find    Replace    Matches
,       .          9
;       ,          20
```

The decimal comma goes first, while it is the only comma in the file. In the other order `1;20;9,02` becomes `1,20,9,02`, and nothing tells the decimal comma from the others.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

⚙️ Find and Replace changes the same **text** wherever it stands. It cannot put something at the start of every line, and it cannot delete a column. For that the editor has more than one cursor.

</div>

<!--
Speaker: delete the mean line first, then open Find and Replace and read the
counter aloud. Before the second replacement ask the room which one has to come
first, and try the wrong order once: Ctrl+Z takes it back. (~3 min)
-->

---
hideInToc: true
---

# Whole **Lines**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ↕️ **The line the cursor is in**

- `Alt+↑` and `Alt+↓` move it
- `Shift+Alt+↓` copies it below
- `Ctrl+Shift+K` deletes it
- `Ctrl+Enter` opens an empty line below it
- `Ctrl+C` and `Ctrl+X` take the whole line when nothing is selected

</div>

<div class="card card-secondary card-glass pad-compact">

## ↔️ **Along the line**

- `Home` and `End` go to its start and its end
- `Ctrl+←` and `Ctrl+→` go one word at a time
- `Shift` with any of these selects on the way
- `Ctrl+Z` undoes one step, `Ctrl+Y` redoes it

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Nothing has to be selected first. The line with the mean goes with one key, `Ctrl+Shift+K`: one row is one observation, and a mean is not an observation.

</div>

<div class="note-text mt-sm">macOS: <code>Option</code> for <code>Alt</code>, <code>Cmd</code> for <code>Ctrl</code>. Three exceptions: one word is <code>Option+←</code> and <code>Option+→</code>, the start and end of the line are <code>Cmd+←</code> and <code>Cmd+→</code>, redo is <code>Cmd+Shift+Z</code>.</div>

---
hideInToc: true
---

# A Cursor on **Every Line**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖱️ **Three ways to place them**

- Select the lines, then `Shift+Alt+I`: a cursor at the end of each line
- `Ctrl+Alt+↓`: one more cursor on the line below
- `Alt`+click: one more cursor where you click
- `Esc` goes back to one cursor

</div>

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Type once**

```text
Alytus           - Alytus
Kaunas      →    - Kaunas
Vilnius          - Vilnius
```

Three cursors, `Home`, then `-` and a space. Whatever is typed, deleted or pasted happens at every cursor.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The Status Bar counts the cursors: `3 selections`. Read the number before you type.

</div>

<div class="note-text mt-sm">macOS: <code>Shift+Option+I</code>, <code>Cmd+Option+↓</code>, <code>Option</code>+click.</div>

---
hideInToc: true
---

# Lines of **Different Length**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧭 **Delete the first column**

1. `Ctrl+A`, then `Shift+Alt+I`: a cursor at the end of every line
2. `Home`: every cursor at the start of its line
3. `Ctrl+Shift+→`: the first word is selected, `nr` or `1`
4. `Shift+→`: the comma as well
5. `Delete`

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Before and after**

```text
nr,length_cm,t10_s        length_cm,t10_s
1,20,9.02            →    20,9.02
2,30,11.05                30,11.05
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The cursors move together. `→` moves each one by a character, and `nr` is one character longer than `1`. `Home`, `End` and the word keys land in the right place on every line, whatever its length.

</div>

<div class="note-text mt-sm">macOS: <code>Cmd+A</code>, <code>Shift+Option+I</code>, <code>Cmd+←</code>, <code>Option+Shift+→</code>, <code>Shift+→</code>, <code>Delete</code>.</div>

---
hideInToc: true
---

# The Same Word, **Everywhere**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Select the matches**

- Double-click a word to select it
- `Ctrl+D` adds the next place with the same text
- `Ctrl+Shift+L` adds all of them at once
- Type the new word. It replaces every match

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **Rename a column**

```md
| length_cm | t10_s |

The period is t10_s divided by 10.

- `t10_s`: time of 10 swings, in s
```

`t10_s` stands in three places. Selected together and typed once, all three become `time10_s`.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`Ctrl+D` is for the next few matches, `Ctrl+Shift+L` for all of them. Unlike Replace All, every place that is about to change shows a cursor before anything is typed.

</div>

<div class="note-text mt-sm">macOS: <code>Cmd+D</code>, <code>Cmd+Shift+L</code>.</div>

---
hideInToc: true
---

# CSV to **Markdown Table**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **The commas**

Select one comma. `Ctrl+Shift+L`. Type a space, `|` and a space.

```text
length_cm | t10_s
20 | 9.02
30 | 11.05
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **The line ends**

`Ctrl+A`, `Shift+Alt+I`, a space and `|`. Then `Home`, `|` and a space.

```text
| length_cm | t10_s |
| 20 | 9.02 |
| 30 | 11.05 |
```

</div>

<div class="card card-accent card-glass pad-compact">

## 3️⃣ **The header**

`Ctrl+Enter` in line 1.<br>Then type `|--|--|`.

```text
| length_cm | t10_s |
|--|--|
| 20 | 9.02 |
| 30 | 11.05 |
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

⚙️ The steps are the same for 10 lines and for 10 000. This is automation at its smallest: say the change once, and it is made on every line.

</div>

<div class="note-text mt-sm">macOS: <code>Cmd+Shift+L</code>, <code>Cmd+A</code>, <code>Shift+Option+I</code>, <code>Cmd+←</code>, <code>Cmd+Enter</code>.</div>

<!--
Speaker: do this live in an empty report.md with the preview open. The table
appears in the preview at step 3. (~3 min)
-->

---
hideInToc: true
---

# Write Down What You **Changed**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **In `README.md`, under Data**

```md
- **File:** `data/raw/pendulum.csv`,
  from a lab partner, 2026-09-29
- **Cleaned copy:** `data/processed/pendulum.csv`.
  Mean line deleted, `,` replaced by `.`,
  `;` replaced by `,`, column `nr` deleted
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **130 bytes became 97**

- The mean line, `;mean;15,14` and its line end: **12** bytes
- Column `nr`: `nr;` and `1;` to `9;`, 3 + 9 × 2 = **21** bytes
- The two replacements swap one character for one: **0**

12 + 21 = 33 = 130 − 97. The check closes.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

✍️ Four edits, made by hand and listed in words. The next file from the lab partner needs all four again. Without the list nobody can tell that these 97 bytes came from those 130: the list is part of the cleaned file's rule.

</div>

<!--
Speaker: type the two lines into the README on the projector. Then check the
byte count together: right-click the file, Properties on Windows or Get Info on
macOS, shows the size in bytes. (~3 min)
-->

---
hideInToc: true
---

# Text Commands in the **Command Palette**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **`Ctrl+Shift+P`, then part of the name**

- **Sort Lines Ascending**: the selected lines in alphabetical order
- **Transform to Uppercase**, **to Lowercase**: the selected text
- **Delete Duplicate Lines**
- **Trim Trailing Whitespace**: spaces at the ends of lines
- **Toggle Word Wrap**: long lines fold at the edge of the window

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Sorting sorts text**

```text
100,20.01
20,9.02
30,11.05
```

`100` comes before `20`, because the character `1` comes before `2`. The editor sees characters, not numbers.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔧 No key has to be remembered for these. The Command Palette finds every command from a few letters of its name. macOS: `Cmd+Shift+P`.

</div>

---
hideInToc: true
---

# Keys — **Windows & macOS**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ↕️ **Lines and cursors**

| | Windows | macOS |
| --- | --- | --- |
| Move the line | `Alt+↑` `Alt+↓` | `Option+↑` `Option+↓` |
| Copy the line down | `Shift+Alt+↓` | `Shift+Option+↓` |
| Delete the line | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Cursor at each line end | `Shift+Alt+I` | `Shift+Option+I` |
| Cursor on the line below | `Ctrl+Alt+↓` | `Cmd+Option+↓` |
| Cursor at a click | `Alt`+click | `Option`+click |

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔎 **Find, select, move**

| | Windows | macOS |
| --- | --- | --- |
| Find and Replace | `Ctrl+H` | `Cmd+Option+F` |
| Add the next match | `Ctrl+D` | `Cmd+D` |
| Add all matches | `Ctrl+Shift+L` | `Cmd+Shift+L` |
| One word left, right | `Ctrl+←` `Ctrl+→` | `Option+←` `Option+→` |
| Line start, line end | `Home` `End` | `Cmd+←` `Cmd+→` |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |

</div>

</div>

<div class="note-text mt-sm">Linux has the Windows keys, with two exceptions: a cursor on the line below is <code>Shift+Alt+↓</code>, and copying the line down is <code>Ctrl+Shift+Alt+↓</code>.</div>

<!--
Speaker: leave this slide up while the room works. Nobody needs all twelve:
the three that pay off first are Shift+Alt+I, Ctrl+D and Alt+arrow. (~1 min)
-->

---
hideInToc: true
---

# The File, **Annotated**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
M,PT,TAU,IPCHI2                               ← column names; no units
1880.649,3000.9534,0.00041271152,1299.1675    ← one K⁻π⁺ pair from one collision
1860.6599,2803.4126,0.0001864154,0.34182164   ← this pair points back well
1913.8755,2542.169,0.00018464602,17.386473    ← 91 580 more rows like these
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| **Column** | `M` | `PT` | `TAU` | `IPCHI2` |
| --- | --- | --- | --- | --- |
| **Unit** | MeV/c² | MeV/c | ns | none |
| **Seen in the file** | peak at 1860–1865 | median 3 049 | `-100.0` = missing, 49 rows | small = points back |

</div>

<div class="card card-success card-glass pad-compact mt-md">

🧭 Record 401, DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR`, CC0, converted from 1 289 541 bytes of ROOT. **A number is data only together with the rule that lets someone else read it back.** Before computing on a file, write its rule into the README.

</div>

<!--
Speaker: the four lines of slide 3, with every question answered. Read row 1
aloud once more, now with its units: a K-pi+ pair of mass 1880.649 MeV/c2 that
flew 0.41 ps and does not point back to the collision. Do not cut this slide.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Data is symbols plus a rule. `1880.649` became information when its kind, source, row and unit were found

</div>

<div class="card card-success card-glass pad-compact">

✅ A table: one row per observation, one variable per column, one value per cell; a mean line breaks the first rule and the mean cannot show it

</div>

<div class="card card-success card-glass pad-compact">

✅ The record gives source, DOI, licence and checksum; the trigger decides what becomes a row

</div>

<div class="card card-success card-glass pad-compact">

✅ Units come from the numbers when the file is silent; the README holds them, with every edit made to the data

</div>

</div>

<!--
Speaker: one line per objective of slide 5. (~1 min)
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
  explanation="Data is a representation by a fixed rule that someone else can read back. The symbols arrived; the rule did not. 1880.649 says nothing until its column, unit and source are known."
/>

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

<MCQ
  question="CERN publishes its collision data on the Open Data Portal years after recording it. Which stage of the data lifecycle is that, and what makes it possible?"
  :options="[
    'Collecting — the detector writes each stored event straight to the public portal',
    'Cleaning — the trigger decides at run time which events are fit for publication',
    'Sharing — the last stage, possible only because provenance, formats and software were kept',
    'Analysing — physicists publish their plots, and the plots are the open data'
  ]"
  :correct="2"
  explanation="Publication is the share stage at the end of the lifecycle. It only works because every earlier stage kept the metadata: how events were selected, which software version processed them, what the columns mean. Skip that in your own project and the last stage becomes impossible."
/>

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

<MCQ
  question="A candidate in the LHCb file has `TAU` = 0.0003, and no unit is written anywhere. Which unit fits, and why?"
  :options="[
    'Seconds, because SI units are the default in a CSV file',
    'Nanoseconds: 0.0003 ns = 0.3 ps, the size of a D⁰ lifetime of 0.41 ps',
    'Picoseconds, because a D⁰ lives for picoseconds',
    'Millimetres, because TAU is a flight distance'
  ]"
  :correct="1"
  explanation="Read in ns, 0.0003 is 0.3 ps, the same size as the D⁰ lifetime of 0.41 ps. In seconds it would be hundreds of millions of times too long, in ps about a thousand times too short."
/>

---
hideInToc: true
---

<MCQ
  question="A file has lines like `1;20;9,02`. They must become `1,20,9.02`. Which two Replace All steps do that?"
  :options="[
    'First <code>;</code> to <code>,</code> and then <code>,</code> to <code>.</code>',
    'First <code>,</code> to <code>.</code> and then <code>;</code> to <code>,</code>',
    'Either order, because the result is the same',
    'Neither: the decimal commas have to be retyped by hand'
  ]"
  :correct="1"
  explanation="Replace the decimal comma while it is still the only comma in the file. In the other order the line first becomes 1,20,9,02: three commas, and nothing tells the decimal one from the others. The second step then gives 1.20.9.02."
/>

---
hideInToc: true
---

<MCQ
  question="An editor sorts three lines as text: `100,20.01`, `20,9.02` and `30,11.05`. Which line comes first?"
  :options="[
    'The line with 20, because 20 is the smallest number',
    'The line with 100, because the character 1 comes before 2 and 3',
    'The line with 30, because it has the most digits',
    'None: lines that hold numbers cannot be sorted'
  ]"
  :correct="1"
  explanation="Sorting text compares characters from the left, and 1 comes before 2. To sort by value the column has to be read as numbers, which a text editor does not do."
/>
