---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Introduction to CERN"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Introduction to CERN

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
Speaker: welcome them to the course proper. Frame the hour — this is the "why":
what CERN is, why it drowns in data, and why that makes it the perfect backdrop
for the skills we build. Set an exploratory, big-picture tone. (~2 min)
-->

---
hideInToc: true
layout: quote
---

# Not only is the Universe stranger than we think, it is stranger than we **can** think. 
Werner Heisenberg

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🏛️ Describe **what CERN is** — the laboratory, the **LHC**, and its four main experiments

</div>

<div class="card card-secondary card-glass pad-compact">

🔬 Trace how a collision becomes **data** — the accelerator chain, detector layers, and the **trigger**

</div>

<div class="card card-accent card-glass pad-compact">

📊 Explain why **data analysis** is central — petabytes per second and the needle-in-a-haystack problem

</div>

<div class="card card-success card-glass pad-compact">

🌐 Recognise CERN's impact beyond physics — the **Web**, the computing **grid**, and **open data**

</div>

<div class="card card-warning card-glass pad-compact">

🎯 Connect these challenges to the **skills** this course builds

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Stress that today is context and
motivation — the hands-on skills start next lecture at the command line. The paired
Seminar 2 is where they go find the running-project dataset. (~1 min)
-->

---
hideInToc: true
---

# Today's Journey

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🏛️ **What CERN is** — the laboratory, the LHC, and its impact beyond physics

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

📊 **Why data analysis is central there** — petabytes of collisions, and needles in haystacks

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🎬 **A film tour across scales** — from the cosmos down to the quantum

</div>

<div class="card card-info card-glass pad-compact reveal-left">

🎯 **Why these skills matter to you** — the same toolkit this course builds

</div>

</div>

---
layout: section
hideInToc: true
---

# What is **CERN**?

<img src="/figures/logo_CERN_white.svg" alt="CERN" class="mx-auto mt-12 h-64" />

<!--
Speaker: section break. Ask who has heard of CERN and what for — most will say
"the Higgs" or "the Web". Use that to preview the next few slides: the org, the
machine, and how a detector actually sees a collision. (~1 min)
-->

---
hideInToc: true
---

# CERN at a Glance

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🏛️ **The Organisation**

- **European Organization for Nuclear Research**
- Founded in **1954** by 12 European states
- Today: **25 member states** *(as of 2026)*, thousands of visiting scientists
- Located at the **French-Swiss border** near Geneva

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 **The Mission**

- Probe the **fundamental structure** of matter
- Build and operate the world's most powerful **particle accelerators**
- Push the boundaries of **technology and engineering**
- Train the **next generation** of scientists

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🌍 **By the Numbers**

🔬 World's **largest** particle physics laboratory · 👩‍🔬 **17,000+** scientists from **110+ nations** · 🏗️ Operating since **1954** · 🧪 Home to the **Large Hadron Collider**

</div>

---
hideInToc: true
---

# The Large Hadron Collider (LHC)

<div class="card card-info card-glass pad-tight">

## ⚙️ **The Machine**

- A **27 km** circumference ring situated **100 m** underground
- Accelerates protons to **99.9999991%** the speed of light
- Collides particles **~1 billion times per second**
- Operating temperature: **1.9 K** (~ -271.3°C — colder than outer space)

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔭 **Main Experiments**

- **ATLAS** — general-purpose detector
- **CMS** — general-purpose detector
- **ALICE** — heavy-ion collisions
- **LHCb** — matter-antimatter asymmetry

</div>

<div class="card card-warning card-glass pad-compact">

## 🏆 **Key Achievement**

Discovery of the **Higgs boson** in **2012** — confirmed the mechanism that gives particles their mass

Nobel Prize in Physics 2013

*Precisely: this gives mass to fundamental particles (**fermions**, **W/Z** bosons) — most of the mass around you (e.g. the proton's) is **QCD binding energy**, not the Higgs.*

</div>

</div>

---
hideInToc: true
---

# The Accelerator <span class="gradient-text">Chain</span>

<div class="card card-info card-glass pad-compact mt-sm">

🔗 No single machine takes protons from a hydrogen bottle to near light speed — the LHC is only the **last link in a chain**, each accelerator handing faster particles to the next.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

1️⃣ **LINAC4** — a linear accelerator kicks things off: **160 MeV**

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

2️⃣ **PS Booster → Proton Synchrotron** — first rings: **2 GeV → 26 GeV**

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

3️⃣ **Super Proton Synchrotron (SPS)** — 7 km ring: **450 GeV**

</div>

<div class="card card-success card-glass pad-compact reveal-left">

4️⃣ **LHC** — 27 km ring: **6.8 TeV per beam** *(Run 3)* — then the beams are made to cross inside the detectors

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

💡 Each machine was once CERN's frontier — today's record-holder is tomorrow's injector.

</div>

---
hideInToc: true
---

# How a Detector <span class="gradient-text">Sees</span> a Collision

<div class="card card-info card-glass pad-compact mt-sm">

🧅 Detectors like ATLAS are built as **layers of an onion** around the collision point — each layer measures a different property of the particles flying out.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

## 🌀 **Tracker** *(innermost)*

Charged particles bend in a magnetic field — the curvature of each track gives its **momentum**

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

## ⚡ **EM Calorimeter**

Stops **electrons and photons**, measuring the **energy** they deposit

</div>

<div class="card card-accent card-glass pad-compact reveal-scale">

## 🔨 **Hadronic Calorimeter**

Stops heavier particles made of quarks (protons, neutrons, pions) — again measuring **energy**

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

## 🧲 **Muon System** *(outermost)*

**Muons** punch through everything else — dedicated outer chambers catch them

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

💾 One collision → **millions of electronic signals** across these layers. Software reassembles them into particles — those are the "detector readings" every analysis starts from.

</div>

---
layout: section
hideInToc: true
---

# Four **Eyes** on the Ring

The LHC is one machine — but four giant detectors watch its collisions, each built to ask a different question of the same beams.

<!--
Speaker: quick tour of the four experiments. The framing to plant: one accelerator,
four different questions — the machine is shared, the science is not. LHCb gets the
longest stop because the course's running dataset comes from it. (~1 min)
-->

---
hideInToc: true
---

# The Generalists: <span class="gradient-text">ATLAS</span> & <span class="gradient-text">CMS</span>

<div class="card card-info card-glass pad-compact mt-sm">

🔭 Two **general-purpose** detectors ask the broadest question — *what is matter made of, and what holds it together?* — with deliberately **different designs**, so neither can fool the other.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🏟️ **ATLAS**

- The **largest** collider detector ever built
- **46 m** long, **25 m** tall — half a cathedral, 100 m underground
- ~**7,000 tonnes**, ~100 million readout channels

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧲 **CMS**

- Built around one colossal superconducting **solenoid** magnet
- **14,000 tonnes** — heavier than the Eiffel Tower
- Same physics goals as ATLAS, opposite design philosophy

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🤝 On **4 July 2012** both announced the Higgs **independently, on the same day** — replication was designed into the LHC from the start. Cross-checking isn't a courtesy; it's architecture.

</div>

---
hideInToc: true
---

# <span class="gradient-text">ALICE</span> — Rewinding the Big Bang

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💥 **The Question**

What was matter like in the first **millionths of a second** after the Big Bang — before protons and neutrons even existed?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌡️ **The Method**

Collide **lead nuclei** instead of protons → a fleeting droplet of **quark–gluon plasma**, over **100,000×** hotter than the core of the Sun

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

📈 A single lead–lead collision can spray out **tens of thousands** of particle tracks — untangling them is a **data problem** before it is a physics problem.

</div>

---
hideInToc: true
---

# <span class="gradient-text">LHCb</span> — Where Did the Antimatter Go?

<div class="card card-primary card-glass pad-tight mt-sm">

## ⚖️ **The Question**

The Big Bang should have created matter and antimatter in **equal amounts** — yet everything you see is matter. LHCb hunts the tiny **asymmetries** (*CP violation*) that let matter win.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔬 **The Method**

Precision-measure decays of **beauty** and **charm** quarks in a forward detector whose sensors sit **millimetres** from the beam

</div>

<div class="card card-warning card-glass pad-compact">

## 🏆 **A 2019 First**

LHCb discovered **CP violation in charm** — in decays of the **D⁰ meson**. Remember that name.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧭 The asymmetries found so far are **far too small** to explain the surviving universe — one of the great open problems in physics.

</div>

---
hideInToc: true
---

# Meet the Particle You'll <span class="gradient-text">Analyse</span>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⚛️ **The D⁰ meson**

- A **charm quark** bound to an up antiquark
- Lives **~0.4 trillionths of a second**, then decays — e.g. **D⁰ → K⁻π⁺**
- Compute the **invariant mass** of each K⁻π⁺ pair, and a peak rises near **1865 MeV**
- That peak is the particle's **fingerprint** in the data

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **Your running project**

<img src="/figures/lhcb_d0_spectrum.png" style="display:block;margin:0.4rem auto 0.6rem;max-height:185px;background:#fff;border-radius:8px;">

Real **LHCb open data** — you'll locate it in Seminar 2 and, by the fitting lecture, produce and fit this exact peak yourself.

</div>

</div>

<!--
Speaker: the seed slide — this exact peak returns in the Python, visualisation, and
fitting lectures. Students should leave knowing one particle by name: the D0, mass
about 1865 MeV, seen as a bump in the K-pi invariant-mass spectrum. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Why **Data**?

<!--
Speaker: pivot from hardware to the real subject of the course. The LHC is only
interesting because of what pours out of it — 1 PB/s, of which almost nothing is
signal. This is where the course's toolkit earns its keep. (~1 min)
-->

---
hideInToc: true
---

# Why <span class="gradient-text">Data Analysis</span> Matters at CERN

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-scale">

## 📊 **The Data Challenge**

- The LHC produces **~1 PB per second** of raw detector output
- Only **~1 in a billion** collisions contains interesting physics
- Must filter, reconstruct, and analyse in near real-time
- Finding the Higgs required sifting through **trillions** of events

</div>

<div class="card card-secondary card-glass pad-tight reveal-scale">

## 🔍 **Needle in a Haystack**

- Collision events produce **detector readings** (energy, momentum, position)
- Signal events look almost identical to background noise
- Statistical methods decide if a discovery is **real or a fluctuation**
- The 5-sigma standard: if there were **no new particle**, a background fluctuation this strong would appear in fewer than **1 in 3.5 million** experiments *(made precise in the Probability & Statistics lecture)*

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md glow">

💾 **Data Pipeline:** Raw detector signals &#8594; Trigger selection (real-time filtering) &#8594; Event reconstruction &#8594; Physics analysis &#8594; Statistical inference &#8594; Publication

<div class="mt-sm" style="font-size: 0.85em; opacity: 0.85;">

Don't worry about the details yet — every stage here is a skill you'll build over this course, from handling files to statistical inference.

</div>

</div>

---
hideInToc: true
---

# From Collision to <span class="gradient-text">Dataset</span>

<div class="card card-info card-glass pad-compact mt-sm">

🚦 Storing 1 PB **every second** is impossible — the experiments decide **in real time** which collisions are worth keeping. This selection is called the **trigger**.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

💥 **~40 million** bunch crossings per second inside each detector

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

⚡ **Level-1 trigger** — custom electronics decide in **microseconds** → ~**100,000** events/s survive

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🖥️ **High-Level Trigger** — a computing farm inspects the full event → a few **thousand** events/s written to storage

</div>

<div class="card card-success card-glass pad-compact reveal-left">

💾 Only these survivors become the **datasets** physicists analyse

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

⚠️ A trigger decision is **final** — discarded collisions are gone forever. Deciding what to keep is itself a data-analysis problem.

</div>

---
hideInToc: true
---

# From Events to <span class="gradient-text">Petabytes</span>

<div class="card card-info card-glass pad-compact mt-sm">

🧮 Put real units on the cascade you just saw — from a single **event** to a **year** of recorded data.

</div>

<div class="mt-md" style="text-align: center;">

```mermaid {scale: 0.85}
graph LR
    A[Collision 40 MHz] --> B[L1 Trigger 100 kHz]
    B --> C[HLT few kHz]
    C --> D[Storage 10 GB/s]

    classDef stage fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    class A,B,C,D stage;
```

</div>

<div class="card card-accent card-glass pad-compact mt-md">

📦 Each surviving event weighs **~1–2 MB** raw. A few thousand of them every second is already **~10 GB/s** written to disk and tape — hundreds of petabytes of brand-new data, every year.

</div>

---
hideInToc: true
---

# What Doesn't Make the **Cut**

<div class="card card-info card-glass pad-compact mt-sm">

🗑️ The trigger's real job isn't finding physics — it's **throwing almost everything away**, correctly, in microseconds.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🔥 Roughly **999,999,999 of every billion** collisions are discarded before any human ever looks at them

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

💽 What survives is still **hundreds of petabytes a year** — dwarfing most of the world's other data-generating projects

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🧮 Even that ruthless cut is generous: any one physicist's actual analysis sample is a sliver of a sliver

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

🎯 So why not just build bigger disks and keep it all?

</div>

---
hideInToc: true
---

# Why It Has to Be <span class="gradient-text">Real-Time</span>

<div class="card card-info card-glass pad-compact mt-sm">

⏱️ Bigger disks wouldn't even be the bottleneck — the real constraint is **time itself**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔁 **No Do-Overs**

Bunches cross every **25 nanoseconds** — the next collision arrives long before software finishes judging the last one

</div>

<div class="card card-secondary card-glass pad-tight">

## ⏳ **No Buffering, Later**

Unlike a slow video stream, there's no "buffering" option — the trigger commits **in microseconds**, or the data is gone

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="Given ~1 PB/s of raw collision data, why can't the LHC experiments simply record every collision?"
  :options="[
    'There is no scientific reason to — only a handful of processes matter',
    'No real-time system can write ~1 PB/s to disk, even before counting the cost',
    'Data-protection rules cap how much CERN is legally allowed to store',
    'Only high-luminosity runs need a trigger — earlier runs recorded everything'
  ]"
  :correct="1"
  explanation="No I/O system can sustain ~1 PB/s to permanent storage. The trigger compresses that firehose down to the few thousand events/s (~10 GB/s) that computing can actually absorb — before anyone judges what's interesting."
/>

---
hideInToc: true
---

<div class="note-text">

*Check your reading of the previous slides — this one trips up professionals too.*

</div>

<MCQ
  question="The Higgs discovery met the '5-sigma' standard. What does that actually mean?"
  :options="[
    'There is less than a 1-in-3.5-million chance the discovery is wrong',
    'If there were no new particle, a background fluctuation this strong would occur in fewer than 1 in 3.5 million experiments',
    'The Higgs mass was measured to 5 decimal places',
    'Five independent experiments confirmed the signal'
  ]"
  :correct="1"
  explanation="5 sigma limits how often pure background fakes a signal this strong — not the chance the discovery is wrong (option one's misreading). Lecture 11 makes this precise."
/>

<style>
.mcq-container { height: calc(100% - 3.5rem) !important; }
</style>

---
hideInToc: true
---

# CERN's Impact Beyond Physics

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

## 🌐 **The World Wide Web**

Invented at CERN by **Tim Berners-Lee** in **1989** to share data between scientists — now used by **5+ billion** people worldwide

</div>

<div class="card card-success card-glass pad-tight">

## 🖥️ **Computing Grid (WLCG)**

The **Worldwide LHC Computing Grid** connects **170+ centres** in **40+ countries** — storing **hundreds of petabytes** of new data every year

</div>

<div class="card card-warning card-glass pad-tight">

## 🏥 **Medical Applications**

Particle accelerator technology enables **hadron therapy** for cancer treatment — more precise than conventional radiotherapy

</div>

<div class="card card-accent card-glass pad-tight">

## 📂 **Open Science**

CERN **Open Data Portal** makes real collision data publicly available — enabling education and independent research worldwide

</div>

</div>

---
hideInToc: true
---

# A Planet-Sized <span class="gradient-text">Computer</span>

<div class="card card-info card-glass pad-compact mt-sm">

🌍 No single data centre can process the LHC's output — the work is spread across a **tiered global grid** *(as of 2026: 170+ sites, 42 countries, ~1.4 million CPU cores)*.

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

💡 A physicist launching an analysis rarely knows — or cares — **which country** their jobs run in. You'll meet the same idea at your own scale: compute where convenient, keep data organised and portable.

🔭 The pattern repeats at the frontier: in **2025** the CERN Council backed the **Future Circular Collider (FCC)** feasibility study — today's frontier is tomorrow's injector.

</div>

---
hideInToc: true
---

# CERN's Data, <span class="gradient-text">Openly</span>

<div class="card card-primary card-glass pad-tight mt-sm">

## 📂 **The Open Data Portal**

CERN releases real collision data publicly — including the **LHCb D⁰ → K⁻π⁺** sample this course's seminars use. Anyone, anywhere can download it and analyse it themselves, no CERN credentials required.

</div>

<div class="card card-success card-glass pad-compact mt-md">

🎓 That's not hypothetical for you: **Seminar 2** has you locate this exact dataset and record its provenance before you ever open it in Python.

</div>

---
hideInToc: true
---

# Why the <span class="gradient-text">DOI</span> Matters

<div class="card card-warning card-glass pad-compact mt-sm">

🔖 "Open" only helps the next person if they can find the **exact version** you used — that's what a dataset's **DOI** and **licence** are for.

</div>

<div class="card card-success card-glass pad-tight mt-md">

## 📌 **Provenance, Not Just Access**

Every CERN Open Data release carries a **DOI**, a **licence**, and full provenance — the same FAIR-data habits **Lecture 14** builds out in full, applied here to the dataset you'll use all course.

</div>

---
hideInToc: true
---

# Open Access, and the <span class="gradient-text">Grid</span> Behind It

<div class="card card-secondary card-glass pad-tight mt-sm">

## 📖 **Publishing, Openly Too**

CERN co-founded **SCOAP3**, making almost all particle-physics journal articles free to read worldwide — and preprints on **arXiv** circulate long before any journal sees them.

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔭 The tiered grid that stores and moves all this data — jobs, storage trade-offs, ~170 sites — is **Lecture 15**'s subject in full; today was just its shape.

</div>

---
layout: section
hideInToc: true
---

# From the **Cosmos** to the **Quantum**

The next short films sweep across the scales of nature — from mountains and deep space down to individual atoms and particle tracks.

Watch for the **change in scale**: the same urge to observe, measure, and understand connects a telescope pointed at distant galaxies with a detector watching protons collide.

<!--
Speaker: dim the lights. Let the films run — don't narrate over them. The one cue
to plant beforehand: every scene ends as data someone must turn into understanding.
That thread carries into the next section. (~1 min setup)
-->

---

<VideoPlayer src="Skylapse.mp4" autoplay loop   />

---

<VideoPlayer src="Drone_Climbing_Mountain.mp4" autoplay   />

---

<VideoPlayer src="VU_VM.mp4" autoplay   />

---

<VideoPlayer src="NASA_Mars_Mariner_4_Pan_Audio.mp4" autoplay   />

---

<VideoPlayer src="Perseverance_Rover_Landing_NASA.mp4" autoplay   />

---


<VideoPlayer src="Cassini_Grand_Finale_NO_VO.mp4" autoplay   />

---

<VideoPlayer src="Stars_Pan_Audio.mp4" autoplay   />

---

<VideoPlayer src="Telescope.mp4" autoplay   />

---

<VideoPlayer src="Hubble.mp4" autoplay   />

---

<VideoPlayer src="Webb_Reel.mp4" autoplay   />

---

<VideoPlayer src="Milky_Way_Sim_Audio.mp4" autoplay   />

---

<VideoPlayer src="Expansion_Funnel_H264_1080p.webm" autoplay   />


---
hideInToc: true
layout: fact
---

# Half-time

## Every scene so far ends as data someone must turn into understanding — which one would *you* analyse first?

---

<VideoPlayer src="QGP_Formation.mp4" autoplay   />

---

<VideoPlayer src="Voyage_in_to_the_world_of_atoms.mp4" autoplay   />

---

<VideoPlayer src="Cloud_Chamber_Audio.mp4" autoplay   />

---
layout: section
hideInToc: true
---

# Inside **CERN**

Now we descend from the universe at large into the laboratory itself — the accelerators, detectors, and people who turn these big questions into concrete measurements.

<!--
Speaker: shift from cosmos to lab. These clips show the real machines behind the
diagrams — ATLAS, LHCb, the tunnels. Point out the human scale next to the
detectors before rolling. (~1 min setup)
-->

---

<VideoPlayer src="CERN_Overview_Short.mp4" autoplay   />

---

<VideoPlayer src="ATLAS-VIDEO-2021-001-001-1080p.mp4" autoplay   />

---


<VideoPlayer src="ATLAS-FOOTAGE-2022-004-002-1080p_Shaft.mp4" autoplay   />


---

<VideoPlayer src="LHCb.mp4" autoplay   />

---



<VideoPlayer src="CERN-FOOTAGE-2023-019-001-2160p.mp4" autoplay   />

---

<VideoPlayer src="CERN-VIDEO-2020-064-001-2160p.mp4" autoplay   />


---

<VideoPlayer src="CERN-FOOTAGE-2024-006-001.mp4" autoplay   />

---

<VideoPlayer src="CERN-FOOTAGE-2024-010-002.mp4" autoplay   />


---

<VideoPlayer src="GTC_2020_1080p.mp4" autoplay   />

---
layout: section
hideInToc: true
---

# From Films to **Skills**

Every scene you just watched ends the same way — as data that someone has to turn into understanding.

---
hideInToc: true
---

# Careers at <span class="gradient-text">CERN</span>

CERN employs far more than physicists — a glimpse of who turns 40 million collisions a second into discoveries.

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔬 **Physicists**

Design analyses, hunt signals in noise — statistics and Python, at full scale.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🛠️ **Engineers**

Build and maintain accelerators, magnets, cryogenics, and detectors under extreme conditions.

</div>

<div class="card card-accent card-glass pad-tight">

## 💻 **Computing Specialists**

Keep 170+ grid sites, trigger farms, and petabyte storage running around the clock.

</div>

</div>

---
hideInToc: true
---

# Your Skills, <span class="gradient-text">Their</span> Jobs

<div class="card card-info card-glass pad-compact mt-sm">

🌐 The **Web** and **hadron therapy** — from the impact slide earlier — didn't appear from nowhere: they're this course's toolkit solving problems outside physics.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-tight">

## 🐍 **In an Analysis Group**

Reproducible Python, version control, and statistics are the daily tools of every physicist reading out the detector.

</div>

<div class="card card-warning card-glass pad-tight">

## 🖥️ **In a Computing Team**

Disciplined file handling and automation scale the same habits from a laptop to 170+ sites and a million cores.

</div>

</div>

---
hideInToc: true
---

# A Day in the <span class="gradient-text">Data</span>

<div class="card card-accent card-glass pad-tight mt-sm">

## 🔎 **One Analyst's Morning**

Pull last night's triggered events, check the D⁰ peak hasn't drifted, flag anything strange for the shift crew, push a fix to the shared analysis code — before lunch, on a laptop, anywhere in the world.

</div>

<div class="card card-info card-glass pad-compact mt-md">

🌍 None of that requires standing next to the detector — it requires exactly the skills this course builds.

</div>

---
hideInToc: true
---

# Why <span class="gradient-text">You</span> Need These Skills

CERN turns raw collisions into discoveries with exactly the toolkit this course builds:

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-up">

## 📁 **Handling Massive Data**

Petabytes of detector output demand disciplined file handling, data formats, and organisation.

</div>

<div class="card card-secondary card-glass pad-tight reveal-up">

## 🔀 **Working Together**

Thousands of scientists share one codebase — impossible without version control.

</div>

<div class="card card-accent card-glass pad-tight reveal-up">

## 🐍 **Turning Signal into Insight**

Python and data-analysis tools transform readings into physics.

</div>

<div class="card card-warning card-glass pad-tight reveal-up">

## 🎲 **Real or a Fluke?**

Statistics decide whether a bump in the data is a discovery — or noise.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md" style="text-align: center;">

You don't need a particle accelerator to use any of this. **Next, we start building these skills ourselves — beginning at the command line.**

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Describe **CERN**, the **LHC**, and its four main experiments

</div>

<div class="card card-success card-glass pad-compact">

✅ Trace a collision from **beam** to stored **dataset** via the **trigger**

</div>

<div class="card card-success card-glass pad-compact">

✅ Explain why **data analysis** is central — and what **5-sigma** means

</div>

<div class="card card-success card-glass pad-compact">

✅ Connect CERN's challenges to the **skills** this course builds

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 2 tie-in**

find and document the running-project dataset — LHCb's D⁰ → K⁻π⁺ open data on the CERN Open Data Portal — recording its provenance (title, DOI, licence).

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each. The tie-in makes the
payoff concrete: in the seminar they hunt down the actual dataset the whole course
will analyse, and practise recording its provenance. (~1 min)
-->

