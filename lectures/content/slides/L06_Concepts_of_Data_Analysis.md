---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false
mermaid: true

transition: fade

title: "Concepts of Data Analysis"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Concepts of Data Analysis

---
layout: section
hideInToc: true
---

# What is **Data Analysis**?

---
hideInToc: true
layout: quote
---

## **Data analysis** is a process of inspecting, cleaning, transforming, and modeling **data** with the goal of discovering useful **information**, informing conclusions, and supporting decision-making

###### Wikipedia

---
hideInToc: true
layout: fact
---

# What is **Data Science**?

---
hideInToc: true
layout: quote
---

## **Data science** is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processing, scientific visualization, algorithms and systems to extract or extrapolate **knowledge and insights** from potentially noisy, structured, or unstructured data

###### Wikipedia

---
hideInToc: true
layout: fact
---

# What is **Data**?

---
hideInToc: true
layout: quote
---

## **Data** are a collection of discrete or continuous values that convey information, describing the quantity, quality, fact, statistics, other basic **units of meaning**, or simply sequences of symbols that may be further interpreted formally. **A datum** is an individual value in a collection of data.

###### Wikipedia

---
hideInToc: true
---

# Why Learn This Now?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧭 **Framework Before Tools**

You have learned Python. Before diving into libraries and datasets, you need a conceptual framework for *thinking* about data — what it is, how to handle it, and what can go wrong.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔬 **From CERN to Industry**

These concepts — lifecycle, quality, ethics, FAIR principles — apply identically whether you are analysing collision data at CERN or customer behaviour at a startup.

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 🎯 **This Lecture**

We build the mental model: data types, quality, the analysis lifecycle, FAIR principles, tools, hygiene, ethics, and key pitfalls to avoid.

</div>

---
layout: section
hideInToc: true
---

# From Data to **Wisdom**

---
hideInToc: true
---

<div style="display: flex; flex-direction: column; gap: 0.4rem; height: 100%; justify-content: center;">

<div class="card card-primary card-glass anim-card" v-click="1">

## 📋 **Data**

<span class="anim-sub">Capture observations — numbers, text, images, signals</span>

<div v-click="[1, 2]" class="anim-ex">

- `[72, 68, 75, 80, 71]` — heart-rate readings
- `"sunny, 12 °C, wind NW"` — weather log entry

</div>

</div>

<div class="card card-secondary card-glass anim-card" v-click="2">

## 💡 **Information**

<span class="anim-sub">Emerges when data gain context, structure, and purpose</span>

<div v-click="[2, 3]" class="anim-ex">

- Resting heart rate **averaged 73 bpm** last week
- Store B weekend revenue is **2.3× higher** than weekdays

</div>

</div>

<div class="card card-accent card-glass anim-card" v-click="3">

## 🧠 **Knowledge**

<span class="anim-sub">Blends information with experience and domain expertise</span>

<div v-click="[3, 4]" class="anim-ex">

- Rising heart rate **predicts flu onset** 48 h early
- Weekend spike driven by **nearby Saturday market**

</div>

</div>

<div class="card card-success card-glass anim-card" v-click="4">

## 🎯 **Wisdom**

<span class="anim-sub">Guides decisions with judgement and responsibility</span>

<div v-click="[4, 5]" class="anim-ex">

- Send a **rest advisory** when heart rate trends up
- **Extend Saturday hours** and stock accordingly

</div>

</div>

</div>

<style>
.anim-card.card {
  padding: 0.4rem 0.8rem !important;
  overflow: hidden;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              padding 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card.card:has(.anim-ex:not(.slidev-vclick-hidden)) {
  padding: 0.5rem 1rem 0.6rem !important;
}
.anim-card.slidev-vclick-hidden {
  transform: translateX(-40px);
  opacity: 0 !important;
  visibility: visible !important;
  pointer-events: none;
}
.anim-card h2 {
  font-size: 1.3em;
  line-height: 1.2;
  margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) h2 {
  font-size: 1em;
}
.anim-sub {
  display: block;
  font-size: 0.75em;
  opacity: 0.85;
  margin-top: 0.15em;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) .anim-sub {
  font-size: 0.7em;
}
.anim-ex {
  max-height: 200px;
  opacity: 0.7;
  overflow: hidden;
  font-size: 0.7em;
  margin-top: 0.2rem;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease,
              margin-top 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-ex.slidev-vclick-hidden {
  max-height: 0 !important;
  opacity: 0 !important;
  visibility: visible !important;
  margin-top: 0 !important;
  pointer-events: none;
}
.anim-ex ul { margin: 0; padding-left: 1.4em; }
.anim-ex li { margin: 0.15em 0; }
</style>

---
hideInToc: true
---

# Example — a lab thermometer

<div class="flow-container">

<div class="card card-primary card-glass flow-row" v-click="1">
  <div class="flow-label">📋 Data</div>
  <div class="flow-text"><code>2025-10-24, 22.3°C</code></div>
</div>

<div class="flow-arrow" v-click="2">↓</div>

<div class="card card-secondary card-glass flow-row" v-click="2">
  <div class="flow-label">💡 Information</div>
  <div class="flow-text">Lab A was <strong>22.3 °C</strong> at 10:24 on Oct 24, 2025</div>
</div>

<div class="flow-arrow" v-click="3">↓</div>

<div class="card card-accent card-glass flow-row" v-click="3">
  <div class="flow-label">🧠 Knowledge</div>
  <div class="flow-text">Lab A runs <strong>1.5 °C hotter</strong> on Fridays due to compute load</div>
</div>

<div class="flow-arrow" v-click="4">↓</div>

<div class="card card-success card-glass flow-row" v-click="4">
  <div class="flow-label">🎯 Wisdom</div>
  <div class="flow-text">Shift Friday calibration <strong>earlier</strong> to reduce thermal drift</div>
</div>

</div>

<style>
.flow-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  gap: 0;
}
.flow-row {
  display: flex !important;
  align-items: center;
  gap: 1rem;
  width: 90%;
  padding: 1rem 1.5rem !important;
}
.flow-row.slidev-vclick-hidden {
  transform: translateX(-30px);
  opacity: 0 !important;
  visibility: visible !important;
}
.flow-label { font-weight: 700; font-size: 1.15em; white-space: nowrap; min-width: 9rem; }
.flow-text { font-size: 1.05em; opacity: 0.9; }
.flow-text code { background: rgba(255, 255, 255, 0.1); padding: 0.15em 0.4em; border-radius: 4px; font-size: 0.95em; }
.flow-arrow { font-size: 1.4em; opacity: 0.4; margin: 0.3rem 0; transition: opacity 0.5s ease; }
.flow-arrow.slidev-vclick-hidden { opacity: 0 !important; visibility: visible !important; }
</style>

---
hideInToc: true
---

# How disciplines overlap

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## 📊 **Statistics**

<div class="note-text">Underpins inference, uncertainty, and experimental design</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔧 **Data Engineering**

<div class="note-text">Ensures data are collected, stored, and discoverable</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 🔍 **Data Analysis**

<div class="note-text">Explores, explains, and communicates what the data say</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight">

## 🧪 **Data Science**

<div class="note-text">Fuses engineering, analysis, and machine learning</div>

</div>

<div class="card card-success card-glass pad-tight">

## 🎯 **Decision Science**

<div class="note-text">Closes the loop with impact tracking and action</div>

</div>

<div class="card card-warning card-glass pad-tight">

## 🤖 **AI / ML**

<div class="note-text">Automates pattern recognition at scale — one tool among many</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Why data analysis matters **now**

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **Data explosion**

Volume, velocity, variety rising everywhere

</div>

<div class="card card-secondary card-glass pad-compact">

## 🏆 **Evidence wins**

Edge comes from data-driven decisions

</div>

<div class="card card-accent card-glass pad-compact">

## 📜 **Regulation**

Traceability, privacy, explainability

</div>

<div class="card card-info card-glass pad-compact">

## 🗣️ **Shared language**

Aligns science, engineering, business

</div>

<div class="card card-success card-glass pad-compact">

## 📖 **Data narratives**

Audiences expect evidence-backed stories

</div>

<div class="card card-warning card-glass pad-compact">

## ⚛️ **CERN angle**

High-throughput, rigorous, reproducible

</div>

</div>

---
hideInToc: true
---

# Key Ideas

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🧪 **Universal scope**

Every scientific study has a data analysis component

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Publications**

Results of analysis become **scientific publications**

</div>

<div class="card card-accent card-glass pad-compact">

## 💼 **Business impact**

Imperative for real-world **decision making**

</div>

<div class="card card-info card-glass pad-compact">

## 🔄 **Multi-disciplinary**

A **multi-step** process spanning many fields

</div>

<div class="card card-warning card-glass pad-compact">

## 🔁 **Iterative**

Insight rarely arrives in a single pass

</div>

<div class="card card-success card-glass pad-compact">

## 🤝 **Trust**

Earned via transparency, reproducibility, storytelling

</div>

</div>

---
layout: section
hideInToc: true
---

# Data Analysis in the **Wild** — examples across fields

---
hideInToc: true
---

# **Biomedicine and Genomics**

<div class="card card-primary card-glass pad-tight mt-md">

<div class="stack-tight">

- ## 🧬 Genome sequencing → identifying variants & gene expression patterns
- ## 💊 Clinical trials → monitoring safety, efficacy, adaptive designs
- ## 📊 Population health dashboards & personalised medicine
- ## 🎯 Decisions: targeted therapies, drug discovery, diagnostics

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

### 🧪 **23andMe** or **Ancestry.com**? Comparing against *reference populations*

</div>

---
hideInToc: true
---

# **Environmental Sciences**

<div class="card card-accent card-glass pad-tight mt-md">

<div class="stack-tight">

- ## 🌍 Climate models integrating satellite, sensor, and historical data
- ## 🏭 Pollution monitoring at city/block resolution
- ## 🌿 Biodiversity studies combining field notes + remote sensing
- ## 📜 Supports policy making, disaster response, conservation funding

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

<div class="note-text">

#### 🔄 Living analysis → data feeds update models continuously

</div>

</div>

---
hideInToc: true
---

# **Social Sciences**

<div class="card card-secondary card-glass pad-tight mt-md">

<div class="stack-tight">

- ## 📈 Economic forecasting blending macro indicators & behavioural data
- ## 🧑‍🤝‍🧑 Social behaviour studies using surveys, logs, ethnography
- ## 💬 Text analysis for sentiment, misinformation, community wellbeing
- ## 🏛️ Informs policy, marketing, product design, civic planning

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

<div class="note-text">

#### 🔗 Qualitative + quantitative insights reinforce each other

</div>

</div>

---
hideInToc: true
---

# **Astronomy**

<div class="card card-primary card-glass pad-tight mt-md">

<div class="stack-tight">

- ## 🔭 Observational data from telescopes, satellites, detectors
- ## 🌊 Gravitational wave detection via signal processing & ML
- ## 🌟 Cataloguing millions of celestial objects, anomaly detection
- ## 💻 Requires high-throughput computing, reproducible pipelines

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

<div class="note-text">

#### 🤖 Fun fact: many ML innovations came from sky surveys

</div>

</div>

---
hideInToc: true
---

# **Particle Physics (CERN)**

<div class="card card-accent card-glass pad-tight mt-md">

<div class="stack-tight">

- ## ⚛️ Petabytes of collision data → reconstruct events, filter noise
- ## 📊 Multivariate analysis to isolate rare signals (e.g. Higgs boson)
- ## 🤝 Collaboration across detectors, theory, computing teams
- ## 🌐 Drives advances in distributed computing & open data practices

</div>

</div>

---
hideInToc: true
---

# **Engineering** & **Healthcare Operations**

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-tight">

## 🔧 **Engineering**

- Predictive maintenance on turbines, trains, manufacturing lines
- Quality control with computer vision & statistical process control
- Structural health monitoring via sensors + physics-informed models
- Outcomes: less downtime, safer infrastructure, cost optimisation

</div>

<div class="card card-warning card-glass pad-tight">

## 🏥 **Healthcare Operations**

- Epidemiology tracking outbreaks & transmission dynamics
- Health policy simulation for capacity & funding
- Hospital operations: patient flow, staffing, supply chain
- Ethical considerations: privacy, bias, explainability

</div>

</div>

---
hideInToc: true
---

# **Finance** & **Sports Analytics**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 💰 **Finance**

- Stock market analysis + algorithmic trading with latency constraints
- Risk management using stress tests, scenario analysis, VaR
- Fraud detection & compliance monitoring with streaming data
- Balances profitability with regulation and transparency

</div>

<div class="card card-success card-glass pad-tight">

## 🏃 **Sports Analytics**

- Performance analysis combining tracking sensors & video
- Strategy optimisation: playbooks, opponent scouting
- Fan engagement via personalised content & ticket pricing
- Data informs coaching, recruitment, business growth

</div>

</div>

---
hideInToc: true
---

# **Product / Business** & **Public Policy**

<div class="grid-2 gap-md mt-md">

<div class="card card-accent card-glass pad-tight">

## 📊 **Product & Business**

- Growth funnels: acquisition, activation, retention, revenue, referral
- Experimentation: A/B tests, feature flagging, causal inference
- Customer segmentation & lifetime value in subscription models
- Guides product roadmaps, marketing spend, customer success

</div>

<div class="card card-info card-glass pad-tight">

## 🏙️ **Public Policy & Urban Planning**

- Smart city sensors for transport, energy, waste
- Open data portals enabling transparency & civic innovation
- Geospatial analysis for zoning, emergency response, sustainability
- Stakeholder engagement & ethical data sharing are crucial

</div>

</div>

---
hideInToc: true
---

# **Education & Learning Analytics**

<div class="card card-secondary card-glass pad-tight mt-md">

<div class="stack-tight">

- ## 📚 Learning management system logs reveal engagement patterns
- ## 🚨 Early warning systems for student support
- ## 📝 Curriculum design using assessment data & qualitative feedback
- ## ⚖️ Balances personalisation with fairness and privacy

</div>

</div>

---
hideInToc: true
---

# Reflection — which example resonates?

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔍 Where could similar data exist in your context?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 What decisions would better data unlock?

</div>

<div class="card card-accent card-glass pad-tight">

## 🚧 What obstacles — technical, ethical, organisational — stand in the way?

</div>

</div>

---
layout: section
hideInToc: true
---

# Four **Flavours** of Analytics

---
hideInToc: true
---

<div style="display: flex; flex-direction: column; gap: 0.4rem; height: 100%; justify-content: center;">

<div class="card card-primary card-glass pad-compact anim-card" v-click="1">

## 📋 **Descriptive Analysis**

<span class="anim-sub">What happened?</span>

<div v-click="[1, 2]" class="anim-ex">

- Event rate rose **12 %** last run
- Sales dropped **8 %** in Q3
- Average delivery time was **3.2 days**

</div>

</div>

<div class="card card-secondary card-glass pad-compact anim-card" v-click="2">

## 🔍 **Diagnostic Analysis**

<span class="anim-sub">Why did it happen?</span>

<div v-click="[2, 3]" class="anim-ex">

- Rate rose due to **trigger threshold** change
- Drop correlates with **pricing** change
- Delivery slowed because of **warehouse relocation**

</div>

</div>

<div class="card card-accent card-glass pad-compact anim-card" v-click="3">

## 🔮 **Predictive Analysis**

<span class="anim-sub">What is likely next?</span>

<div v-click="[3, 4]" class="anim-ex">

- Projected **8 % rate increase** next fill
- Model forecasts **recovery in Q1**
- Delivery times will **normalise by March**

</div>

</div>

<div class="card card-success card-glass pad-compact anim-card" v-click="4">

## 🎯 **Prescriptive Analysis**

<span class="anim-sub">What should we do?</span>

<div v-click="[4, 5]" class="anim-ex">

- Raise threshold by **0.3** to maintain buffer
- Revert price, **A/B test** alternatives
- Add a **temporary depot** until the move completes

</div>

</div>

</div>

<style>
.anim-card {
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card.slidev-vclick-hidden {
  transform: translateX(-40px);
  opacity: 0 !important;
  visibility: visible !important;
  pointer-events: none;
}
.anim-card h2 {
  font-size: 1.3em;
  line-height: 1.2;
  margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) h2 {
  font-size: 1em;
}
.anim-sub {
  display: block;
  font-size: 0.75em;
  opacity: 0.6;
  font-style: italic;
  margin-top: 0.1em;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) .anim-sub {
  font-size: 0.7em;
}
.anim-ex {
  max-height: 200px;
  opacity: 0.7;
  overflow: hidden;
  font-size: 0.7em;
  margin-top: 0.2rem;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease,
              margin-top 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-ex.slidev-vclick-hidden {
  max-height: 0 !important;
  opacity: 0 !important;
  visibility: visible !important;
  margin-top: 0 !important;
  pointer-events: none;
}
.anim-ex ul { margin: 0; padding-left: 1.4em; }
.anim-ex li { margin: 0.15em 0; }
.anim-card.card {
  padding: 0.4rem 0.8rem !important;
  overflow: hidden;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              padding 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card.card:has(.anim-ex:not(.slidev-vclick-hidden)) {
  padding: 0.5rem 1rem 0.6rem !important;
}
</style>

---
hideInToc: true
---

# Each layer builds on the previous

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 **Descriptive** — establishes baseline facts

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Diagnostic** — uncovers root causes

</div>

<div class="card card-accent card-glass pad-tight">

## 🔮 **Predictive** — forecasts future states

</div>

<div class="card card-success card-glass pad-tight">

## 🎯 **Prescriptive** — recommends optimal actions

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="A hospital model predicts patient readmission risk using age, diagnosis, and length of stay. What type of analytics is this?"
  :options="[
    'Descriptive — it summarises past admissions',
    'Diagnostic — it explains why patients were readmitted',
    'Predictive — it forecasts a future outcome',
    'Prescriptive — it recommends a treatment plan'
  ]"
  :correct="2"
  explanation="The model uses historical features to estimate a future probability (readmission risk). That is predictive analytics. It does not yet recommend what to do about it — that would be prescriptive."
/>

---
layout: section
hideInToc: true
---

# Data **Fundamentals**

---
hideInToc: true
---

# Data comes in many shapes

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Tabular** — rows × columns (experiments, business metrics)

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌳 **Hierarchical** — JSON/XML, nested logs, documents

</div>

<div class="card card-accent card-glass pad-tight">

## 🕸️ **Graph** — networks, relationships, supply chains

</div>

<div class="card card-info card-glass pad-tight">

## 🗺️ **Spatial & temporal** — GIS layers, time series, event streams

</div>

<div class="card card-warning card-glass pad-tight">

## 🖼️ **Multimedia** — images, audio, video, sensor waveforms

</div>

</div>

---
hideInToc: true
---

# Structured vs semi- vs unstructured

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **Structured**

Predefined schema, SQL-friendly (lab results)

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔖 **Semi-structured**

Consistent markers, flexible fields (JSON, HL7)

</div>

<div class="card card-accent card-glass pad-tight">

## 📝 **Unstructured**

Natural language, images, free-form signals

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

<div class="note-text">

#### Choose storage, tooling, and cleaning strategies accordingly

</div>

</div>

---
hideInToc: true
---

<img src="/figures/data_types.svg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain;" />

---
hideInToc: true
---

# Granularity & unit of analysis

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔬 Define the entity: person, transaction, collision event, sensor ping

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 Aggregation level affects signal vs noise

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Misaligned granularity introduces bias & misleading conclusions

</div>

<div class="card card-info card-glass pad-tight">

## 📝 Document transformations between granularities

</div>

</div>

---
hideInToc: true
---

# Mind the **time** dimension

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📊 Cross-sectional vs time series vs panel data

</div>

<div class="card card-secondary card-glass pad-tight">

## ⏱️ Sampling frequency and latency influence what you can see

</div>

<div class="card card-accent card-glass pad-tight">

## 📈 Seasonality, trends, and lag effects require tailored methods

</div>

<div class="card card-info card-glass pad-tight">

## 🕐 Align timestamps, time zones, and calendars early

</div>

</div>

---
hideInToc: true
---

# **Metadata** keeps data alive

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 👤 Who collected it, when, where, how, and why?

</div>

<div class="card card-secondary card-glass pad-tight">

## 📐 Variable definitions, units, encoding schemes

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 Data lineage: transformations, assumptions, scripts, owners

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Without metadata the data become a liability, not an asset

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Quality** & Uncertainty

---
hideInToc: true
---

# Data quality checklist

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## ✅ **Completeness**

<div class="note-text">Missingness patterns and mechanisms</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔗 **Consistency**

<div class="note-text">Units, schemas, timezones</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 📐 **Validity**

<div class="note-text">Ranges, constraints, outliers (legit vs error)</div>

</div>

<div class="card card-primary card-glass pad-tight">

## 🎯 **Accuracy**

<div class="note-text">Reflects reality — guards against sensor drift & transcription error</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight">

## ⏱️ **Timeliness**

<div class="note-text">Latency, freshness</div>

</div>

<div class="card card-warning card-glass pad-tight">

## 🔄 **Lineage**

<div class="note-text">Provenance, versioning, reproducibility</div>

</div>

<div class="card card-success card-glass pad-tight">

## 🔢 **Uniqueness**

<div class="note-text">Deduplication when merging feeds</div>

</div>

<div class="card card-success card-glass pad-tight">

## ⚖️ **Ethics**

<div class="note-text">Consent, privacy, bias, fairness</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Common data issues & biases

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-tight">

## ❓ Missing data mechanisms (MCAR, MAR, MNAR)

</div>

<div class="card card-warning card-glass pad-tight">

## 📊 Outliers: true phenomena or collection errors?

</div>

<div class="card card-warning card-glass pad-tight">

## 🎯 Sampling bias & survivorship bias

</div>

<div class="card card-warning card-glass pad-tight">

## 🧠 Confirmation bias, p-hacking, and multiple testing

</div>

<div class="card card-warning card-glass pad-tight">

## ⚖️ Ethical blind spots: representation, consent, accessibility

</div>

</div>

---
hideInToc: true
---

# Uncertainty and inference

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📊 Always report uncertainty: CIs, credible intervals, SEs

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Beware p-hacking (selectively analyzing data for significant results); **pre-register** your analysis plan when possible

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔢 Power matters: effect size, N, variance

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 Distinguish correlation from causation

</div>

<div class="card card-info card-glass pad-tight">

## 🧪 Sensitivity analyses: robustness to assumptions

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="You fit a model with 50 parameters to 60 data points and get 99.9 % accuracy on your training set. Should you celebrate?"
  :options="[
    'Yes — high accuracy means the model works',
    'No — the model is likely overfitting',
    'It depends on the test set performance'
  ]"
  :correct="1"
  explanation="With almost as many parameters as data points, the model is memorising the training data rather than learning patterns. This is classic overfitting — it will likely perform poorly on new data. Always evaluate on a held-out test set."
/>

---
hideInToc: true
---

# Exercise · Audit your data sources

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 Pick one dataset you rely on

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔬 Classify type, granularity, measurement levels, quality risks

</div>

<div class="card card-accent card-glass pad-tight">

## 📝 Note missing metadata you would need before analysis

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Lifecycle** & Workflow

---
hideInToc: true
---

# Thought Exercise — Your Data World

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🤔 **Think** (1 min)

Pick a project, hobby, or job you know well. What data gets generated there? Who uses it, and for what decisions?

</div>

<div class="card card-secondary card-glass pad-tight">

## 💬 **Discuss** (3 min)

Share with a neighbour: What is one decision that could be improved if the data were better collected, stored, or analysed?

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🎯 **Goal**

Connect the abstract lifecycle ideas to your own experience before we see the full framework.

</div>

---
hideInToc: true
---

# Lifecycle recap — six key phases

<div class="card card-info card-glass pad-compact mt-sm">

<div class="note-text">

A concise six-phase view — easy to remember day-to-day. Detailed sub-stages nest inside each phase.

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🎯 **Plan**

</div>

<div class="card card-secondary card-glass pad-compact">

📥 **Acquire**

</div>

<div class="card card-accent card-glass pad-compact">

💾 **Store**

</div>

<div class="card card-info card-glass pad-compact">

🔧 **Process**

</div>

<div class="card card-success card-glass pad-compact">

📊 **Analyse**

</div>

<div class="card card-warning card-glass pad-compact">

📢 **Share**

</div>

</div>

---
hideInToc: true
---

# End-to-end lifecycle (1/2)

<div class="note-text mt-sm">

The detailed nine-stage view of the analysis lifecycle.

</div>

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

### 🎯 **Problem Framing**
Hypotheses & success metrics

</div>

<div class="card card-secondary card-glass pad-compact">

### 🔍 **Data Discovery**
Access & quality assessment

</div>

<div class="card card-accent card-glass pad-compact">

### 🧹 **Preparation**
Cleaning, joining, feature selection

</div>

<div class="card card-info card-glass pad-compact">

### 📊 **Exploration**
Profiling, visualization, sanity checks

</div>

<div class="card card-success card-glass pad-compact">

### 🧪 **Modeling/Inference**
Statistical tests & machine learning

</div>

</div>

---
hideInToc: true
---

# End-to-end lifecycle (2/2)

<div class="grid-3 gap-md mt-md">

<div class="card card-warning card-glass pad-compact">

### ✅ **Evaluation**
Validation, uncertainty, sensitivity

</div>

<div class="card card-primary card-glass pad-compact">

### 📢 **Communication**
Narrative, visuals, decisions

</div>

<div class="card card-secondary card-glass pad-compact">

### ⚙️ **Operationalization**
Notebooks, scripts, pipelines

</div>

<div class="card card-accent card-glass pad-compact">

### 📡 **Monitoring**
Drift, quality, impact

</div>

</div>

---
hideInToc: true
---

# Governance overlays every stage

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔒 Security, privacy, compliance, and ethics checks

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 Documentation and lineage updates

</div>

<div class="card card-accent card-glass pad-tight">

## ✅ Quality gates and automated tests

</div>

<div class="card card-info card-glass pad-tight">

## 🔄 Feedback loops from stakeholders and end users

</div>

</div>

---
hideInToc: true
---

# Analysis is **iterative**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔄 Expect to loop between question ↔ data ↔ analysis ↔ insight

</div>

<div class="card card-secondary card-glass pad-tight">

## 🚧 Dead ends reveal where data, methods, or framing must change

</div>

<div class="card card-accent card-glass pad-tight">

## 🗂️ Maintain versioned checkpoints to compare approaches

</div>

<div class="card card-info card-glass pad-tight">

## 📢 Communicate progress, uncertainty, and trade-offs early

</div>

</div>

---
hideInToc: true
---

# Spotting opportunities

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🗺️ Map stakeholders → decisions → supporting data

</div>

<div class="card card-secondary card-glass pad-tight">

## 📏 Ask how outcomes are measured today

</div>

<div class="card card-accent card-glass pad-tight">

## 🔎 Identify gaps between available data and needed insight

</div>

<div class="card card-info card-glass pad-tight">

## ✅ Check feasibility: access, quality, ethics, skills, time

</div>

</div>

---
layout: section
hideInToc: true
---

# Steps of Data **Analysis**

The lifecycle phases zoomed into the practical "how"

---
hideInToc: true
---

# 1. **Define the Problem or Research Question**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 Formulate the question with stakeholders and context

<div class="note-text">This steers the choices in every subsequent step</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 📐 Translate goals into measurable metrics & hypotheses

</div>

<div class="card card-accent card-glass pad-tight">

## 🗺️ Map constraints: data access, time, ethics, skills

</div>

<div class="card card-info card-glass pad-tight">

## 🧪 Plan the experimental or observational design

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

<div class="note-text">

#### 💡 Interactive exercise · Draft a SMART question for your project

</div>

</div>

---
hideInToc: true
---

# 2. **Collect Data** — key questions

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📊 How much data do you need?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🏷️ What sort of data do you need?

</div>

<div class="card card-accent card-glass pad-tight">

## 📁 What data formats should you choose?

</div>

<div class="card card-info card-glass pad-tight">

## 🔍 Can you trust the data?

</div>

</div>

---
hideInToc: true
---

# 2. **Collect Data** — best practices

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-tight">

## ⚙️ Can you collect the data? Assess feasibility early

</div>

<div class="card card-success card-glass pad-tight">

## 📝 Document permissions, consent, and provenance

</div>

<div class="card card-primary card-glass pad-tight">

## ✅ Automate validation checks at ingestion

</div>

</div>

---
hideInToc: true
---

# 3. **Clean Data**

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## 🔍 **Data Selection**

</div>

<div class="card card-secondary card-glass pad-tight">

## ✂️ **Data Stripping**

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 **Data Skimming**

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight">

## 🔧 **Data Wrangling**

</div>

<div class="card card-warning card-glass pad-tight">

## ❓ Handle missing values, outliers, inconsistent categories

</div>

<div class="card card-success card-glass pad-tight">

## 📝 Record transformations for reproducibility

</div>

</div>

</div>

---
hideInToc: true
---

# 4. **Analyse Data**

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## 🔍 **Data Exploration**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **Statistical Analysis**

</div>

<div class="card card-accent card-glass pad-tight">

## 🧪 **Model Building**

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight">

## 🤖 **Machine Learning**

</div>

<div class="card card-warning card-glass pad-tight">

## 🧠 **Classification (...AI...)**

</div>

<div class="card card-success card-glass pad-tight">

## 📐 Evaluate assumptions, uncertainty, and sensitivity

</div>

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

<div class="note-text">

#### Compare baseline vs advanced methods — a good scatter plot beats a bad neural network

</div>

</div>

---
hideInToc: true
---

# 5. **Visualise the Data**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 👥 What's your target audience?

</div>

<div class="card card-secondary card-glass pad-tight">

## 💬 What is the message you want to convey?

</div>

<div class="card card-accent card-glass pad-tight">

## 🎨 Choose encodings that emphasise the core insight

</div>

<div class="card card-info card-glass pad-tight">

## ✏️ Iterate quickly with sketches before polishing

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

<div class="note-text">

#### 📌 Visualisation principles are covered in the **Data Visualisation** lecture (L7); practical matplotlib skills come later

</div>

</div>

---
hideInToc: true
---

# Visualisation principles (preview)

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🎨 Choose encodings that match the variable type

</div>

<div class="card card-secondary card-glass pad-tight">

## 📏 Show context: baselines, denominators, time windows

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Avoid deceit: truncated axes, cherry-picked ranges

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 Use small multiples for comparisons

</div>

<div class="card card-success card-glass pad-tight">

## 📖 Tell the story: title as takeaway, caption as why

</div>

</div>

---
hideInToc: true
---

# 6. **Interpret and Report the Results**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 Draw conclusions from data

</div>

<div class="card card-secondary card-glass pad-tight">

## 📄 Report findings

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 Connect to decisions, risks, next steps

</div>

<div class="card card-info card-glass pad-tight">

## ❓ Capture limitations and open questions

</div>

<div class="card card-success card-glass pad-tight">

## 📦 Package reproducible assets (code, dashboards, docs)

</div>

</div>

---
hideInToc: true
---

# Validation & monitoring

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📊 Split data wisely, guard against leakage

</div>

<div class="card card-secondary card-glass pad-tight">

## 📐 Assess error bars, confidence intervals, effect sizes

</div>

<div class="card card-accent card-glass pad-tight">

## 🧪 Stress test with scenario analysis & sensitivity checks

</div>

<div class="card card-info card-glass pad-tight">

## 📡 Plan post-deployment monitoring for drift and quality

</div>

</div>

---
hideInToc: true
---

# Team checkpoints per phase

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🚀 **Kickoff** → align on question, scope, success metrics

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **Midpoint** → share exploratory findings, data quality flags

</div>

<div class="card card-accent card-glass pad-tight">

## 🎤 **Pre-delivery** → rehearse narrative, anticipate objections

</div>

<div class="card card-info card-glass pad-tight">

## 📝 **Retrospective** → document lessons, update playbooks

</div>

</div>

---
hideInToc: true
---

# Communication toolkit

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📄 Executive summary (one-pager)

</div>

<div class="card card-secondary card-glass pad-tight">

## 📓 Notebook or reproducible analysis package

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 Dashboard / data app for continued monitoring

</div>

<div class="card card-info card-glass pad-tight">

## 📋 Decision memo outlining options & trade-offs

</div>

<div class="card card-success card-glass pad-tight">

## 🔬 Technical appendix for peers to audit

</div>

</div>

---
hideInToc: true
---

# From data to decisions

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 💡 Translate insights into recommendations & actions

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 Align with organisational objectives and constraints

</div>

<div class="card card-accent card-glass pad-tight">

## 📏 Plan how outcomes will be measured post-decision

</div>

<div class="card card-info card-glass pad-tight">

## 📝 Capture learnings to refine future analyses

</div>

</div>

---
layout: section
hideInToc: true
---

# Tools & **Collaboration**

---
hideInToc: true
---

# Modern analytics stack

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📡 **Data sources** — sensors, APIs, files, databases, experiments

</div>

<div class="card card-secondary card-glass pad-tight">

## 📥 **Ingestion** — ETL/ELT tools, streaming pipelines, notebooks

</div>

<div class="card card-accent card-glass pad-tight">

## 💾 **Storage** — data lakes, warehouses, object stores, feature stores

</div>

<div class="card card-info card-glass pad-tight">

## 💻 **Compute** — notebooks, scripts, distributed clusters, cloud services

</div>

<div class="card card-success card-glass pad-tight">

## 📢 **Delivery** — dashboards, apps, reports, APIs, alerts

</div>

</div>

---
hideInToc: true
---

# Roles and collaboration

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## 🧑‍🔬 **Domain expert**

<div class="note-text">Frames problems, validates insights</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **Analyst / Scientist**

<div class="note-text">Explores, models, communicates</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 🔧 **Data Engineer**

<div class="note-text">Access, reliability, pipelines</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight">

## 📋 **PM / Lead**

<div class="note-text">Scope, impact, trade-offs</div>

</div>

<div class="card card-warning card-glass pad-tight">

## 🎨 **Visualisation designer**

<div class="note-text">Crafts compelling stories</div>

</div>

<div class="card card-success card-glass pad-tight">

## 🤝 **Shared artefacts**

<div class="note-text">Glossary, metrics, dashboards</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Collaboration rituals

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 Shared backlog with clear owners & due dates

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔄 Version control (git) for notebooks, SQL, scripts

</div>

<div class="card card-accent card-glass pad-tight">

## 👁️ Code & analysis reviews to raise quality and share knowledge

</div>

<div class="card card-info card-glass pad-tight">

## 🤝 Pair sessions for tricky modelling or cleaning tasks

</div>

<div class="card card-success card-glass pad-tight">

## 📦 Reproducible environments (conda, containers, Poetry, Nix)

</div>

</div>

---
hideInToc: true
---

# Choosing the right artefact

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📓 **Notebooks** for exploration, teaching, storytelling

</div>

<div class="card card-secondary card-glass pad-tight">

## 📜 **Scripts & packages** for automation and reuse

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 **Dashboards & apps** for ongoing monitoring

</div>

<div class="card card-info card-glass pad-tight">

## 🧪 **Experiments** for causal claims and product decisions

</div>

<div class="card card-success card-glass pad-tight">

<div class="note-text">

#### Mix intentionally; document the purpose of each asset

</div>

</div>

</div>

---
hideInToc: true
---

# Languages of data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🗄️ **SQL** remains foundational for structured data

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐍 **Python** ecosystem (pandas, Polars, PySpark, SciPy, scikit-learn)

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 **R** for statistics, visualisation, reproducible reports

</div>

<div class="card card-info card-glass pad-tight">

## 🚀 **Julia, Scala, Rust** for performance-critical workloads

</div>

<div class="card card-warning card-glass pad-tight">

## 🔬 **Domain-specific** tools (ROOT at CERN, SAS, MATLAB, SPSS)

</div>

</div>

---
hideInToc: true
---

# Proprietary tools vs programming languages

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

## 🏢 **Proprietary** (Tableau, Origin, Excel)

**⚠️ Drawbacks:** expensive, limited in scope, compatibility & flexibility gaps

**✅ Benefits:** easy to learn via GUI, great for rapid stakeholder demos & quick wins

</div>

<div class="card card-success card-glass pad-tight">

## 💻 **Languages** (Python, R, Julia)

**✅ Benefits:** open source, free, powerful, scale from exploration to production

**⚠️ Drawbacks:** steeper learning curve (CLI, programming literacy)

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

### 💡 **Tip** — mix surface-level ease with depth and reproducibility

</div>

---
hideInToc: true
---

# DataOps & automation

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## ⏱️ Schedule data pipelines with orchestration tools

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔄 Leverage CI/CD for tests, linting, deployment

</div>

<div class="card card-accent card-glass pad-tight">

## 📐 Parameterise workflows for reproducibility

</div>

<div class="card card-info card-glass pad-tight">

## 📡 Monitor pipelines for latency, failures, data drift

</div>

</div>

---
hideInToc: true
---

# Testing your analysis

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🧪 Unit tests for data transforms & calculations

</div>

<div class="card card-secondary card-glass pad-tight">

## ✅ Data validation (great expectations, pydantic, pandera)

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 Statistical tests to confirm assumptions

</div>

<div class="card card-info card-glass pad-tight">

## 📂 Golden datasets & regression tests for dashboards

</div>

<div class="card card-success card-glass pad-tight">

## 👁️ Peer review before results leave the team

</div>

</div>

---
hideInToc: true
---

# Documentation & knowledge sharing

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📖 Analyst runbooks and playbooks

</div>

<div class="card card-secondary card-glass pad-tight">

## 📋 Data dictionaries & catalogs

</div>

<div class="card card-accent card-glass pad-tight">

## 📝 Decision logs capturing context and rationale

</div>

<div class="card card-info card-glass pad-tight">

## 🎤 Internal demos & show-and-tell sessions

</div>

<div class="card card-success card-glass pad-tight">

## 🤝 Mentoring to spread tooling fluency

</div>

</div>

---
hideInToc: true
---

# **Discussion**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🤔 When to use proprietary tools?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔧 What should you be using?

</div>

<div class="card card-accent card-glass pad-tight">

## 📈 Saturation of achieved proficiency

</div>

<div class="card card-info card-glass pad-tight">

## 🔄 How do we ensure reproducibility when collaborating?

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Hygiene** & Ethics

---
hideInToc: true
---

# Why data hygiene matters

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-tight">

## 🚫 Prevent costly errors & embarrassing corrections

</div>

<div class="card card-primary card-glass pad-tight">

## 🤝 Build trust with stakeholders & regulators

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔄 Accelerate future analyses with reusable assets

</div>

<div class="card card-accent card-glass pad-tight">

## 🔒 Protect sensitive data and maintain compliance

</div>

<div class="card card-success card-glass pad-tight">

## 📦 Enable others to replicate or extend your work

</div>

</div>

---
hideInToc: true
---

# Hygiene habits to cultivate

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔄 Source control for data definitions and transformations

</div>

<div class="card card-secondary card-glass pad-tight">

## ✅ Automated linting & formatting for notebooks / scripts

</div>

<div class="card card-accent card-glass pad-tight">

## 📁 Clear folder structures & naming conventions

</div>

<div class="card card-info card-glass pad-tight">

## 🗂️ Versioned datasets or snapshotting

</div>

<div class="card card-success card-glass pad-tight">

## 🧹 Regular housekeeping: archive, deprecate, document

</div>

</div>

---
hideInToc: true
---

# Reproducibility practices

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📓 Keep code with results (notebook discipline)

</div>

<div class="card card-secondary card-glass pad-tight">

## 📦 Parameterise and record environment (env.yaml)

</div>

<div class="card card-accent card-glass pad-tight">

## 🗂️ Version data / queries or capture snapshots

</div>

<div class="card card-info card-glass pad-tight">

## 🎲 Seed randomness; log configs and hashes

</div>

<div class="card card-success card-glass pad-tight">

## ⚙️ Automate critical paths (Makefile / CI)

</div>

</div>

---
hideInToc: true
---

# Ethics & responsible analytics

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🛡️ **Minimise harm** — privacy, consent, security

</div>

<div class="card card-secondary card-glass pad-tight">

## ⚖️ **Fairness** — monitor for disparate impact across groups

</div>

<div class="card card-accent card-glass pad-tight">

## 🔍 **Transparency** — explain methods, assumptions, limitations

</div>

<div class="card card-info card-glass pad-tight">

## 👤 **Accountability** — define owners and escalation paths

</div>

<div class="card card-success card-glass pad-tight">

## 🌍 **Sustainability** — consider computational & environmental cost

</div>

</div>

---
hideInToc: true
---

# Data governance essentials

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔐 Policies for access control and approvals

</div>

<div class="card card-secondary card-glass pad-tight">

## 📋 Data catalogues & stewardship roles

</div>

<div class="card card-accent card-glass pad-tight">

## 📜 Compliance frameworks (GDPR, HIPAA, CERN policies)

</div>

<div class="card card-info card-glass pad-tight">

## 🚨 Incident response plans for data breaches or quality issues

</div>

<div class="card card-success card-glass pad-tight">

## 📚 Training & audits to keep teams aligned

</div>

</div>

---
layout: section
hideInToc: true
---

# **FAIR** Principles

---
layout: quote
hideInToc: true
---

## The first step in **(re)using data** is to find them. **Metadata** and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services — a core component of the FAIRification process.

---
hideInToc: true
---

# What is **Metadata**?

<div class="card card-warning card-glass pad-tight mt-md">

## 📋 **Metadata** = data about data

Metadata describes the who, what, when, where, how, and why of a dataset. Examples: column names and types, units, collection date, author, license, provenance, and schema version.

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 🔍 **Why it matters for FAIR**

Without rich metadata, datasets cannot be found, understood, or reused. Machine-readable metadata enables automated discovery and integration across systems.

</div>

---
hideInToc: true
---

# **Findable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🏷️ **F1.** (Meta)data are assigned a globally **unique** and persistent **identifier**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **F2.** Data are described with **rich metadata**

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 **F3.** Metadata explicitly **include the identifier** of the data they describe

</div>

<div class="card card-info card-glass pad-tight">

## 🔍 **F4.** (Meta)data are registered or indexed in a **searchable resource**

</div>

</div>

---
hideInToc: true
---

# **Accessible** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🌐 **A1.** (Meta)data are retrievable by their identifier using a standardised communications protocol

</div>

<div class="card card-secondary card-glass pad-tight">

### 📖 **A1.1** The protocol is **open**, free, and universally implementable

</div>

<div class="card card-accent card-glass pad-tight">

### 🔐 **A1.2** The protocol allows for **authentication** and **authorisation** where necessary

</div>

<div class="card card-info card-glass pad-tight">

## 📂 **A2.** Metadata are accessible even when the data are no longer available

</div>

</div>

---
hideInToc: true
---

# **Interoperable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🗣️ **I1.** (Meta)data use a formal, accessible, shared, and broadly applicable **language for knowledge representation**

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔗 **I2.** (Meta)data use vocabularies that follow **FAIR principles**

</div>

<div class="card card-accent card-glass pad-tight">

## 📎 **I3.** (Meta)data include **qualified references** to other (meta)data

</div>

</div>

---
hideInToc: true
---

# **Reusable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 **R1.** (Meta)data are **richly described** with a plurality of accurate and relevant attributes

</div>

<div class="card card-secondary card-glass pad-tight">

### 📜 **R1.1.** (Meta)data are released with a clear and **accessible** data usage **license**

</div>

<div class="card card-accent card-glass pad-tight">

### 🔗 **R1.2.** (Meta)data are associated with detailed **provenance**

</div>

<div class="card card-info card-glass pad-tight">

### 🏛️ **R1.3.** (Meta)data meet **domain-relevant community standards**

</div>

</div>

---
hideInToc: true
---

# FAIR in practice

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🏷️ Assign DOIs or persistent IDs through catalogues

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 Publish rich metadata schemas (DCAT, schema.org, Invenio)

</div>

<div class="card card-accent card-glass pad-tight">

## 🌐 Provide API/documentation for programmatic access

</div>

<div class="card card-info card-glass pad-tight">

## 📖 Reuse domain ontologies and controlled vocabularies

</div>

<div class="card card-success card-glass pad-tight">

## 🔄 Capture provenance with tools like REANA, DVC, Quilt

</div>

</div>

---
layout: section
hideInToc: true
---

# Case Study · CERN **Open Data**

---
hideInToc: true
---

# Context

<div class="card card-primary card-glass pad-tight mt-md">

- ## 🌐 CERN releases proton-proton collision datasets via the Open Data portal
- ## 🎯 Goal: enable students & researchers to reproduce landmark analyses
- ## 📁 Data formats: ROOT files, CSV summaries, metadata packages
- ## 🔧 Tooling: ROOT, Python, R, Jupyter, cloud notebooks

</div>

---
hideInToc: true
---

# Collaboration model

<div class="card card-secondary card-glass pad-tight mt-md">

- ## 👥 Physicists, statisticians, software engineers, detector experts
- ## 🔄 Shared code repositories with rigorous review (ROOT macros, Python)
- ## 🧪 Simulation teams provide synthetic data for validation
- ## 📄 Publication committees ensure rigour & messaging

</div>

---
hideInToc: true
---

# Risks & mitigations

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **Detector anomalies**

<div class="note-text">Continuous monitoring & calibration</div>

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ **Bias in selection cuts**

<div class="note-text">Blind analyses & control regions</div>

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **Reproducibility**

<div class="note-text">Containerised environments, notebooks, docs</div>

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **Communication**

<div class="note-text">Translate particle jargon for broader audiences</div>

</div>

</div>

---
hideInToc: true
---

# Mini case study · detector night-shift spikes

<div class="card card-info card-glass pad-tight mt-md">

## 📡 **Scenario**
Detector shows intermittent spike counts on night shifts.

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 📋 **Plan**

- Define metric (spike rate/hour), segment by shift.
- Pull two weeks of logs; check missingness.
- Visualize rates; annotate configuration changes.
- Test difference-in-means with bootstrap CI (resampling-based confidence intervals).
- Prescribe mitigation if the effect is robust.

</div>

---
hideInToc: true
---

# Exercise · Plan your own analysis

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 Pick a dataset (CERN or your organisation)

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔧 Draft a 6-step workflow referencing today's framework

</div>

<div class="card card-accent card-glass pad-tight">

## 👥 Identify stakeholders, success metrics, and key risks

</div>

<div class="card card-info card-glass pad-tight">

## 📦 Decide what artefact you would deliver

</div>

</div>

---
hideInToc: true
---

# Lessons from CERN for everyone else

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📝 Document everything — you never know who will re-run it

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔧 Invest in shared tooling and platforms early

</div>

<div class="card card-accent card-glass pad-tight">

## 🌐 Open data accelerates innovation beyond your organisation

</div>

<div class="card card-info card-glass pad-tight">

## 👁️ Rigorous peer review can coexist with fast iteration

</div>

<div class="card card-success card-glass pad-tight">

## 🎉 Celebrate small wins: incremental insights build trust

</div>

</div>

---
layout: section
hideInToc: true
---

# Pitfalls, Patterns & **Takeaways**

---
hideInToc: true
---

# Common pitfalls

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ Jumping to complex models before understanding the data

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Confusing correlation with causation

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Overfitting pretty charts to noisy data

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Confusing proxy metrics with outcomes

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Ignoring units / timezones and data joins

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Confirmation bias; not seeking disconfirming evidence

</div>

<div class="card card-warning card-glass pad-tight">

## ⚠️ Shipping insights without reproducibility

</div>

</div>

---
hideInToc: true
---

# Useful patterns

<div class="stack-tight mt-md">

<div class="card card-success card-glass pad-tight">

## ✅ Start with a checklist (quality, ethics, uncertainty)

</div>

<div class="card card-success card-glass pad-tight">

## ✅ Write the "results" slide first; work backward

</div>

<div class="card card-success card-glass pad-tight">

## ✅ Keep a decisions log with assumptions

</div>

<div class="card card-success card-glass pad-tight">

## ✅ Pair-review visuals and statistical claims

</div>

<div class="card card-success card-glass pad-tight">

## ✅ Maintain a lightweight data dictionary

</div>

</div>

---
hideInToc: true
---

# Practitioner habits

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧠 **Think**

Ask the right question. Understand the domain. Know what "good enough" looks like.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Explore**

Look at the data before modelling it. Distributions, outliers, missing values — they tell a story.

</div>

<div class="card card-accent card-glass pad-tight">

## 🛠️ **Choose**

Pick the simplest method that solves the problem. A good scatter plot beats a bad neural network.

</div>

<div class="card card-success card-glass pad-tight">

## 📢 **Communicate**

Results that nobody understands have zero impact. Visualisation and storytelling are part of analysis.

</div>

</div>

---
hideInToc: true
---

# Takeaways

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Decisions first**

Define metrics and success criteria early

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **Quality & uncertainty**

Treat as first-class, not footnotes

</div>

<div class="card card-accent card-glass pad-compact">

## 📢 **Communicate clearly**

With integrity and empathy for the audience

</div>

<div class="card card-success card-glass pad-compact">

## 🔄 **Reproducible & useful**

Easy to re-run, easy to act on

</div>

<div class="card card-info card-glass pad-compact">

## 🧹 **Hygiene & governance**

Underpin every trustworthy insight

</div>

<div class="card card-warning card-glass pad-compact">

## 🔧 **Tools intentionally**

Balance speed, scale, and rigour

</div>

</div>
