<!--
Parked slides from slides/02_Introduction_to_Data.md, taken out on 2026-10-04.

They left the deck when the section "Markdown & Text Editing" was added, so that
the lecture stays inside the 105-145 min band. All of them were on the skip list
of the 90-minute plan. The quiz slides are not here: they close the deck as its
self-check section. This file is not in decks.json: it is not built, not
gated and not deployed. To put a slide back, move it into the lecture file.

Where they stood: "What Each Flavour Is Used For" after "One Table, Three
Files"; the two "Data at Work" slides and "Common Threads" after the thought
exercise; "Working with the Data" and the section "Beyond Physics" (three slides) after
"Why It Has to Be Real-Time".
-->

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

<div class="note-text mt-md">Nothing to memorise. Most datasets mix flavours: the weather table two slides back holds numbers, text and timestamps.</div>

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

---
hideInToc: true
---

# Common **Threads** Across Every Domain

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **A decision comes first**

Which therapy, which trade, which collision to keep: the analysis is built around a decision someone has to make.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Uncertainty is stated**

A forecast gives a range, a risk model a probability, a mass measurement a ± error.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔄 **The analysis gets rerun**

New data keeps arriving, so the work has to be a pipeline that runs again, not a calculation done once by hand.

</div>

<div class="card card-info card-glass pad-compact">

## 🤝 **The work is shared**

Domain expert, analyst, engineer, decision-maker: each sees one part of the problem.

</div>

<div class="card card-success card-glass pad-compact">

## ⚖️ **Rules grow with the stakes**

Data on health, policy and money comes with consent, audits and regulation.

</div>

<div class="card card-warning card-glass pad-compact">

## 📖 **It has to be explained**

A number changes a decision only once the person deciding understands what it says.

</div>

</div>

<div class="note-text mt-md">🔍 Which of the five domains is closest to your own field?</div>

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

# Beyond **Physics**

Built at CERN to handle its own data, now used everywhere: the Web, the computing grid, open data, open publishing.

<!--
Speaker: section break. Everything so far was about the experiments; this section
is about what CERN had to build to run them and that others now use. Ask which
CERN invention they used today — the answer is the Web, every one of them. (~1 min)
-->

---
hideInToc: true
---

# CERN's Impact Beyond **Physics**

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact">

## 🌐 **The World Wide Web**

Invented at CERN by **Tim Berners-Lee** in **1989** to share data between scientists. Now used by **5+ billion** people.

</div>

<div class="card card-success card-glass pad-compact">

## 🖥️ **Computing Grid (WLCG)**

The **Worldwide LHC Computing Grid** connects **170+ centres** in **40+ countries** and stores **hundreds of petabytes** of new data every year

</div>

<div class="card card-warning card-glass pad-compact">

## 🏥 **Medical Applications**

Accelerator technology is used in **hadron therapy** for cancer, which is more precise than conventional radiotherapy

</div>

<div class="card card-accent card-glass pad-compact">

## 📂 **Open Science**

The CERN **Open Data Portal** publishes real collision data for teaching and independent research

</div>

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

📖 **Open publishing:** CERN co-founded **SCOAP3**, which makes almost all particle-physics journal articles free to read. Preprints appear on **arXiv** before any journal sees them.

</div>

---
hideInToc: true
---

# The LHC Computing <span class="gradient-text">Grid</span>

<div class="card card-info card-glass pad-compact mt-sm">

🌍 No single data centre can process the LHC's output. The work is spread over a **tiered global grid** *(as of 2026: 170+ sites, 42 countries, ~1.4 million CPU cores)*.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🏛️ **Tier 0 — CERN** · the custodial copy of all raw data on tape, first-pass reconstruction

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

🏢 **Tier 1 — ~15 national labs** · second copies, large-scale reprocessing, round-the-clock links to CERN

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🏫 **Tier 2 — ~150 universities** · simulation and the everyday analyses of individual physicists

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

💡 A physicist who starts an analysis usually does not know **in which country** the jobs run. The same idea at your scale: compute where convenient, keep the data organised and portable.

🔭 What comes next: the **Future Circular Collider (FCC)** feasibility study, reported in **2025**, proposes a 91 km ring, more than three times the LHC's 27 km.

</div>


<!--
Parked from slides/02_Introduction_to_Data.md on 2026-10-06, in the storytelling
rework (the deck now opens on four lines of D0_KPi.csv, "A File With No Note").

Where they stood:
- "A Day in Data — Morning", "A Day in Data — Afternoon to Lights-Out" and
  "Every One of These Is a Dataset": after the section "Data in Your Life"
  (now "Data and Information"), before "What Is Data?".
- "Measurement vs Metadata": after "Kinds of Variables". Merged into the new
  "Anatomy of a Table" (the unit in the column name is metadata).
- "Anatomy of a Table" with the invented weather table: after "Measurement vs
  Metadata". Replaced by the same slide on pendulum_raw.csv.
- "Thought Exercise — Data in Your Field": after "One Table, Three Files".
  Merged into "The Five Questions, Your Dataset".
- "Why Data Analysis Matters at CERN": first slide after the section "Data at
  the LHC" (now "From Collision to Row"). Its 5-sigma bullet used statistics
  not yet taught; 1 PB/s is on "From Collision to Dataset".
- "Recap — You Can Now…": the last lecture slide, before "Check Yourself".
  Replaced by "The File, Annotated" and a four-line Recap.
- Two quiz slides of the self-check (a day of data analysis; 5 sigma): first
  and third quiz after "Check Yourself".
-->

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

<!--
Parked 2026-10-12, when the deck changed its example file to the weather station
(no particle-physics data thread any more). These slides stood in the sections
"How One Row Was Made" (ATLAS and CMS, ALICE, LHCb, with their fly-in clips and
the quark-gluon plasma clip) and "From Collision to Row" (From Collision to
Dataset, From Events to Petabytes, What the Trigger Kept), and "147 Columns, 4
Filled" stood in "Reading the File". The deck keeps one CERN slide on the
trigger and the data-flow clip. Several of these slides refer to D0_KPi.csv.
-->

# Parked **2026-10-12**
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



<!-- Parked 2026-10-13 from Lecture 02, after 'What the File Does Not Say', before the section 'Data and Information'. Text-card slide taken out when the deck moved its look at the data forward and tied the CERN examples to the same five questions. -->

---
hideInToc: true
---

# Learning **Objectives**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🔣 Say what turns symbols into **data**: a rule that lets someone else read them back

</div>

<div class="card card-secondary card-glass pad-compact">

📋 Read a **table**: one row per observation, one variable per column, and which columns can be averaged

</div>

<div class="card card-accent card-glass pad-compact">

🌐 Write down where a file came from, its **provenance**, and what one row is

</div>

<div class="card card-success card-glass pad-compact">

📝 Work out **units** and **missing** values from the numbers, and write them into a **README** in VS Code

</div>

</div>

<!--
**Say:** one objective per group of the five questions, and the last one is the tool for writing the answers down.
(~1 min)
-->


<!-- Parked 2026-10-13 from Lecture 02, first slide of the section 'Reading the File'; slide 'Data Is Symbols Plus a Rule' reads the same row as a sentence. Text-card slide taken out when the deck moved its look at the data forward and tied the CERN examples to the same five questions. -->

---
hideInToc: true
---

# Read a Row **Aloud**

<div class="card card-primary card-glass pad-compact mt-md">

```text
2016-01-01T00:00,-4.4,93,2.5
```

</div>

<div class="card card-accent card-glass pad-compact mt-md">

🗣️ "At 00:00 on 1 January 2016 the station measured `temp_c` −4.4, `humidity_pct` 93 and `wind_ms` 2.5."

</div>

<div class="note-text mt-md">The sentence still lacks the units, and says nothing about the other 87 671 rows.</div>

<!--
**Do:** read row 1 aloud as a sentence, then ask a student to read row 2 the same way.
**Say:** `T` separates the date from the hour. This way of writing a time is the standard ISO 8601.
(~2 min)
-->


<!-- Parked 2026-10-13 from Lecture 02, first slide of the section 'Kinds of Data'. Text-card slide taken out when the deck moved its look at the data forward and tied the CERN examples to the same five questions. -->

---
hideInToc: true
---

# Structured vs **Unstructured**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Structured**

Rows and columns: a table, a spreadsheet, a database. Each column has one meaning.

- Sensor logs, survey answers, sales
- `weather.csv` is structured

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌀 **Unstructured**

Free form: text, images, sound, video.

- E-mails, photos, recordings
- A step is needed to turn it into numbers or labels

</div>

</div>

<!--
**Ask:** which kind is a folder of holiday photos? A list of exam marks?
(~2 min)
-->


<!-- Parked 2026-10-13 from Lecture 02, after 'Provenance, Written Down', section 'Where the File Came From'. Text-card slide taken out when the deck moved its look at the data forward and tied the CERN examples to the same five questions. -->

---
hideInToc: true
---

# Your Own **Dataset**

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

## 🎒 **The provenance note**

- Where it came from: a web address, an instrument, a colleague
- The terms of use
- The file exactly as received, and the date

</div>

<div class="card card-warning card-glass pad-compact">

## 🔒 **Personal data**

- Anonymise before it enters the project folder
- Never e-mail or upload raw personal data

</div>

</div>

<!--
**Ask:** what would the source line be for data you collected yourself?
(~2 min)
-->
