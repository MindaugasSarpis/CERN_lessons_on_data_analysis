---
layout: cover
title: "Introduction to Data"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Introduction to Data

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
Speaker: last time was the why — the films and CERN. Today is the what: data
itself. Start from their own day, then kinds of data, tables and files, then how
to find and document a dataset. CERN comes after that, as the case study, with
its example file. The lecture ends with the tools for text files: the project
folder, Markdown, and changing many lines at once. (~2 min)
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

🗂️ Spot the **datasets** in an ordinary day and sort them into the **four flavours**

</div>

<div class="card card-secondary card-glass pad-compact">

🔄 Walk a dataset through its **lifecycle** — collect, store, clean, analyse, decide, share — and say where it silently goes wrong

</div>

<div class="card card-accent card-glass pad-compact">

📋 Read a **table** — rows as observations, columns as variables — and say which **kind of variable** each column holds

</div>

<div class="card card-success card-glass pad-compact">

🌐 Find an **open dataset** and document it — portal, record, **DOI**, licence, provenance

</div>

<div class="card card-warning card-glass pad-compact">

⚛️ Trace how a **collision becomes a dataset** at CERN — detector, trigger, storage

</div>

<div class="card card-info card-glass pad-compact">

📄 Read a real data file — **rows, columns, units, metadata** — before writing a line of code

</div>

<div class="card card-primary card-glass pad-compact">

✍️ Write a README in **Markdown** and change **many lines** of a text file with one edit

</div>

</div>

<!--
Speaker: read these as promises. By the end they should know what a dataset
*is*, how a table is built, where to get one and how to write down where it came
from. (~1 min)
-->

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

# What **Is** Data?

<div class="card card-info card-glass pad-tight mt-sm glow">

**Data** is a *reinterpretable representation of information in a formalized manner suitable for communication, interpretation, or processing.*

<div class="note-text mt-sm">ISO/IEC 2382, <em>Information technology — Vocabulary</em></div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔣 **A representation**

Symbols that stand for something: digits, letters, pixels. `11.2` is not a temperature. It stands for one.

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

In this course: **data is recorded observation**, written down consistently enough to count, sort and compare. One value says little. Thousands of them, organised, show a trend, a spread, a peak.

</div>

<div class="note-text mt-sm"><code>11.2</code> is data. "Vilnius, 29 September, 08:00: 11.2 °C" is information: the data together with what it means.</div>

<!--
Speaker: read the definition once, then take its three words one at a time. A
representation: the symbols are not the thing. Formalized: there is a rule.
Reinterpretable: the rule lets someone else read it back. Ask what is missing
when a colleague sends a file of numbers with no column names. (~2 min)
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

The loop from two slides ago. The figure names the stages differently; the cycle is the same. Every project — yours, a bank's, a physics collaboration's — walks it, and each answer raises fresh questions that restart it.

</div>

<div class="note-text mt-md">Most problems in practice come from skipping a stage: analysing before cleaning, or deciding before storing where the data came from.</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Kinds of **Data**

<!--
Speaker: from "data is everywhere" to telling one kind from another. Three new
ideas: the kind of variable, the shape of a table, the format of a file. (~1 min)
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

Describing a thing by a set of numbers. Everything in a dataset can be expressed as numbers: a colour is 3 numbers, a place on Earth is 2 (latitude, longitude), a collision ends as one mass, 1864.8 MeV. Written as a number is not the same as behaving like one — next slide.

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

<div class="note-text mt-md">Postcodes, phone numbers and ID numbers look like numbers and are not: the average of two postcodes means nothing. The kind of variable decides which plot and which statistic make sense.</div>

<!--
Speaker: ask the Excel users which kind each column of a spreadsheet they know is.
The kind of variable decides the summary, the plot and the distribution. (~2 min)
-->

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

## ⚠️ **Metadata is not optional** 📁 ♻️

A momentum with no units, a reading with no timestamp, a file with no source — that's a number you can neither trust nor reproduce. Much of data work is keeping the metadata attached to the numbers.

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

# One Table, Three **Files**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **CSV — plain text**

- One line per row, values separated by commas
- Opens in any program, on any system
- Stores no types and no units: `11.2` is just four characters

</div>

<div class="card card-secondary card-glass pad-compact">

## 📗 **Spreadsheet — .xlsx**

- The table plus formatting, formulas, several sheets
- The program decides how a value is shown and stored
- Excel turned gene names such as `SEPT2` into dates so often that geneticists renamed the genes in 2020

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **Binary — ROOT, HDF5**

- Compact and fast, with a type for every column
- Readable only by a program that knows the format
- What large experiments and data services use

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
layout: section
hideInToc: true
---

# The LHC **Experiments**

The case study. One accelerator, four detectors: ATLAS, CMS, ALICE, LHCb.

<!--
Speaker: the CERN case study starts here; everything before it was general.
ATLAS and CMS share one slide; ALICE and LHCb get one each. ATLAS, CMS and ALICE
have a silent 3D fly-in from the ring to the detector — talk over the clips.
LHCb has a 0:47 clip instead; today's example file comes from LHCb. (~1 min)
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

LHCb observed **CP violation in charm**, in decays of the **D⁰ meson**: the particle in today's example file.

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

# Data at the **LHC**

<!--
Speaker: from the detectors to what they produce: 1 PB/s of raw output, of which
almost nothing is signal. The rest of the section is how that becomes a dataset
someone can analyse. (~1 min)
-->

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

<VideoPlayer src="cern_video_2015_024_001.mp4" />

<!-- The whole data flow in one clip (2:51, music): accelerator chain, detectors, trigger levels, data centre, the grid. -->

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
layout: section
hideInToc: true
---

# A Dataset **Up Close**

<!--
Speaker: now open the example file, conceptually — no code yet. Apply the table
and variable slides from earlier to it. (Pass 2 of the reel adds a 2:28 LHCb
decay animation as the opener of this section.) (~1 min)
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
layout: section
hideInToc: true
---

# Markdown & **Text Editing**

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

# **Recap** — You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Spot the **datasets** in an ordinary day and sort them into the **four flavours**

</div>

<div class="card card-success card-glass pad-compact">

✅ Walk a dataset through its **lifecycle** — collect to share — and name the step where it silently goes wrong

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **table** — observations in rows, variables in columns — and name the **kind of variable** in each column

</div>

<div class="card card-success card-glass pad-compact">

✅ Find an **open dataset**, read its **record** (title, DOI, licence) and write down its **provenance**

</div>

<div class="card card-success card-glass pad-compact">

✅ Trace a **collision** from detector through trigger to stored dataset

</div>

<div class="card card-success card-glass pad-compact">

✅ Open a data file and read **rows, columns, units and metadata** before touching code

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a README in **Markdown** and change **many lines** of a text file with one edit

</div>

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each. (~1 min)
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
