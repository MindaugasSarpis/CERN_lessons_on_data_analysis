<!--
Parked slides from slides/02_Introduction_to_Data.md, taken out on 2026-10-04.

They left the deck when the section "Markdown & Text Editing" was added, so that
the lecture stays inside the 105-145 min band. All of them were on the skip list
of the 90-minute plan. This file is not in decks.json: it is not built, not
gated and not deployed. To put a slide back, move it into the lecture file.

Where they stood: "What Each Flavour Is Used For" after "One Table, Three
Files"; the two "Data at Work" slides and "Common Threads" after the thought
exercise; "Working with the Data", the section "Beyond Physics" (three slides) and the
quiz on publishing open data, all after the quiz on the trigger.
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

<!--
The five quiz slides below also left the deck on 2026-10-04, after the lecturer's
note that the multiple-choice slides were out of place in this lecture. The same
questions are on the workbook page lectures/lecture_2.md under "Check yourself".
In deck order they stood after: Data Has a Lifecycle; From Record to Your Project
Folder; Why Data Analysis Matters at CERN; Why It Has to Be Real-Time; Same
Questions, Your Dataset.
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

