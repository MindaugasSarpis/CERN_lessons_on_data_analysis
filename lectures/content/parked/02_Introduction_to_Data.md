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
