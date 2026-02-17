---
background: /background_intro.jpg

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

# Data analysis and Artificial Intelligence

## Concepts of Data Analysis

---
hideInToc: true
layout: fact
---

# What is **Data Analysis**?

---
hideInToc: true
layout: quote
---

## **Data analysis** is a process of inspecting, cleaning, transforming, and modeling **data** with the goal of discovering useful **information**, informing conclusions, and supporting decision-making

# Wikipedia

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

# Wikipedia

---
hideInToc: true
layout: fact
---

# What is Data?

---
hideInToc: true
layout: quote
---

## **Data** are a collection of discrete or continuous values that convey information, describing the quantity, quality, fact, statistics, other basic **units of meaning**, or simply sequences of symbols that may be further interpreted formally. **A datum** is an individual value in a collection of data.

# Wikipedia

---
hideInToc: true
---

# Data → Information → Knowledge

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 **Data**
Capture observations (numbers, text, images, signals)

</div>

<div class="card card-secondary pad-tight">

## 💡 **Information**
Emerges when data gain context, structure, and purpose

</div>

<div class="card card-accent pad-tight">

## 🧠 **Knowledge**
Blends information with experience and domain expertise

</div>

<div class="card card-success pad-tight">

## 🎯 **Wisdom**
The responsibility to act on knowledge with judgement

</div>

</div>

---
hideInToc: true
---

# Example

<div class="grid-2 gap-md mt-md">

<div class="card card-info pad-tight">

## 📋 **Raw Data**

###  `2025-10-24, 22.3°C`

</div>

<div class="card card-primary pad-tight">

## 💡 **Information**

### `Lab A was 22.3°C at 10:24 on Oct 24, 2025.`

</div>

<div class="card card-accent pad-tight">

## 🧠 **Knowledge**

### `Lab A runs 1.5°C hotter on Fridays due to load.`

</div>

<div class="card card-success pad-tight">

## 🎯 **Wisdom**

### `Shift calibration earlier on Fridays to reduce drift.`

</div>

</div>

---
hideInToc: true
---

# How disciplines overlap

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary pad-tight">

## 📊 **Statistics**

<div class="note-text">Underpins inference, uncertainty, and experimental design</div>

</div>

<div class="card card-secondary pad-tight">

## 🔧 **Data Engineering**

<div class="note-text">Ensures data are collected, stored, and discoverable</div>

</div>

<div class="card card-accent pad-tight">

## 🔍 **Data Analysis**

<div class="note-text">Explores, explains, and communicates what the data say</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info pad-tight">

## 🧪 **Data Science**

<div class="note-text">Fuses engineering, analysis, and machine learning</div>

</div>

<div class="card card-success pad-tight">

## 🎯 **Decision Science**

<div class="note-text">Closes the loop with impact tracking and action</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Why data analysis matters now

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📈 **Exploding volume, velocity, and variety** of data in every industry

</div>

<div class="card card-secondary pad-tight">

## 🏆 **Competitive edge** comes from **evidence-based** decisions

</div>

</div>

<div class="stack-tight mt-md">

<div class="card card-accent pad-tight">

## 📜 Regulations demand **traceability**, **privacy**, and **explainability**

</div>

<div class="card card-info pad-tight">

## 🗣️ Teams need a **shared language** across disciplines

</div>

<div class="card card-success pad-tight">

## 📖 Audiences expect stories backed by **data narratives**

</div>

</div>

<div class="card card-warning pad-tight mt-md">

### ⚛️ **CERN angle** — High-throughput pipelines, reproducible workflows, and rigorous uncertainty quantification are non-negotiable.

</div>

---
hideInToc: true
---

# Four flavours of analytics

<div class="card card-info pad-tight mt-md">

<div style="font-size: 1.25em;">

| **Flavour** | **Question** | **Example** |
|:------------|:-------------|:------------|
| **Descriptive** | What happened? | Event rate rose 12% last run |
| **Diagnostic** | Why did it happen? | Rate rose due to trigger threshold change |
| **Predictive** | What is likely next? | Projected 8% rate increase next fill |
| **Prescriptive** | What should we do? | Raise threshold by 0.3 to maintain buffer |

</div>

</div>

---
hideInToc: true
---

# Each layer builds on the previous one

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 **Descriptive** — establishes baseline facts

</div>

<div class="card card-secondary pad-tight">

## 🔍 **Diagnostic** — uncovers root causes

</div>

<div class="card card-accent pad-tight">

## 🔮 **Predictive** — forecasts future states

</div>

<div class="card card-success pad-tight">

## 🎯 **Prescriptive** — recommends optimal actions

</div>

</div>

---
hideInToc: true
---

# Key Ideas

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🧪 **Universal Scope**
Any experiment (study or analysis) in any field of science will have a data analysis component

</div>

<div class="card card-secondary pad-tight">

## 📄 **Publications**
Normally, the **results of data analysis** appear in scientific **publications**

</div>

<div class="card card-accent pad-tight">

## 💼 **Business Impact**
In business data analysis is imperative for **decision making**

</div>

<div class="card card-info pad-tight">

## 🔄 **Multi-step & Multi-disciplinary**
Data analysis is a **multi-step** process spanning **multiple disciplines**

</div>

<div class="card card-warning pad-tight">

## 🔁 **Iterative**
Expect to **iterate** — insight rarely appears in a single pass

</div>

<div class="card card-success pad-tight">

## 🤝 **Trust**
Trust is earned through **transparency**, **reproducibility**, and **storytelling**

</div>

</div>

---
hideInToc: true
---

# Thought Exercise — Your Data World

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🤔 **Think** (1 min)

Pick a project, hobby, or job you know well. What data gets generated there? Who uses it, and for what decisions?

</div>

<div class="card card-secondary pad-tight">

## 💬 **Discuss** (3 min)

Share with a neighbour: What is one decision that could be improved if the data were better collected, stored, or analysed?

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## 🎯 **Goal**

Connect the abstract lifecycle ideas to your own experience before we see the full framework.

</div>

---
hideInToc: true
---

# End-to-end Lifecycle (1/2)

<div class="note-text mt-sm">

Here is the detailed nine-stage view of the analysis lifecycle. A simplified six-phase version appears later in this lecture.

</div>

<div class="grid-3 gap-md mt-md">

<div class="card card-primary pad-compact">

### 🎯 **Problem Framing**
Hypotheses & success metrics

</div>

<div class="card card-secondary pad-compact">

### 🔍 **Data Discovery**
Access & quality assessment

</div>

<div class="card card-accent pad-compact">

### 🧹 **Preparation**
Cleaning, joining, feature selection

</div>

<div class="card card-info pad-compact">

### 📊 **Exploration**
Profiling, visualization, sanity checks

</div>

<div class="card card-success pad-compact">

### 🧪 **Modeling/Inference**
Statistical tests & machine learning

</div>

</div>

---
hideInToc: true
---

# End-to-end Lifecycle (2/2)

<div class="grid-3 gap-md mt-md">

<div class="card card-warning pad-compact">

### ✅ **Evaluation**
Validation, uncertainty, sensitivity

</div>

<div class="card card-primary pad-compact">

### 📢 **Communication**
Narrative, visuals, decisions

</div>

<div class="card card-secondary pad-compact">

### ⚙️ **Operationalization**
Notebooks, scripts, pipelines

</div>

<div class="card card-accent pad-compact">

### 📡 **Monitoring**
Drift, quality, impact

</div>

</div>


---
hideInToc: true
class: text-center
---

# Lifecycle blueprint
<div style="display: flex; justify-content: center; align-items: center;">

<Transform :scale="0.8">
```mermaid
flowchart TB
  P[Plan & Frame] --> D[Discover Data]
  D --> Prep[Prepare & Clean]
  Prep --> Exp[Explore & Profile]
  Exp --> Mod[Model & Test]
  Mod --> Eval[Evaluate & Stress Test]
  Eval --> Share[Communicate & Decide]
  Share --> Prod[Operationalize]
  Prod --> Mon[Monitor & Iterate]
  Mon -.-> P

  G[Governance · Ethics · Quality] -.-> P
  G -.-> D
  G -.-> Prep
  G -.-> Mod
  G -.-> Prod

  classDef stage fill:#0b2236,stroke:#44c0f5,stroke-width:2px,color:#e5f6ff;
  classDef overlay fill:none,stroke:#f5a623,stroke-dasharray:6 4,color:#ffe7c7;
  class P,D,Prep,Exp,Mod,Eval,Share,Prod,Mon stage;
  class G overlay;
```
</Transform>

</div>

---
hideInToc: true
---

# Spotting opportunities

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🗺️ Map stakeholders → decisions → supporting data

</div>

<div class="card card-secondary pad-tight">

## 📏 Ask how outcomes are measured today

</div>

<div class="card card-accent pad-tight">

## 🔎 Identify gaps between available data and needed insight

</div>

<div class="card card-info pad-tight">

## ✅ Check feasibility: access, quality, ethics, skills, time

</div>

</div>

---
hideInToc: true
---

# Data quality checklist

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary pad-tight">

## ✅ **Completeness**

<div class="note-text">Missingness patterns and mechanisms</div>

</div>

<div class="card card-secondary pad-tight">

## 🔗 **Consistency**

<div class="note-text">Units, schemas, timezones</div>

</div>

<div class="card card-accent pad-tight">

## 📐 **Validity**

<div class="note-text">Ranges, constraints, outliers (legit vs error)</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info pad-tight">

## ⏱️ **Timeliness**

<div class="note-text">Latency, freshness</div>

</div>

<div class="card card-warning pad-tight">

## 🔄 **Lineage**

<div class="note-text">Provenance, versioning, reproducibility</div>

</div>

<div class="card card-success pad-tight">

## ⚖️ **Ethics**

<div class="note-text">Consent, privacy, bias, fairness</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Uncertainty and inference

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📊 Always report uncertainty: CIs, credible intervals, SEs

</div>

<div class="card card-warning pad-tight">

## ⚠️ Beware p-hacking (selectively analyzing data to get significant results); pre-register (publicly declare your analysis plan before seeing results) when possible

</div>

<div class="card card-secondary pad-tight">

## 🔢 Power matters: effect size, N, variance

</div>

<div class="card card-accent pad-tight">

## 🔗 Distinguish correlation from causation

</div>

<div class="card card-info pad-tight">

## 🧪 Sensitivity analyses: robustness to assumptions

</div>

</div>

---
hideInToc: true
---

# Visualization principles

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🎨 Choose encodings that match the variable type

</div>

<div class="card card-secondary pad-tight">

## 📏 Show context: baselines, denominators, time windows

</div>

<div class="card card-warning pad-tight">

## ⚠️ Avoid deceit: truncated axes, cherry-picked ranges

</div>

<div class="card card-accent pad-tight">

## 📊 Use small multiples for comparisons

</div>

<div class="card card-success pad-tight">

## 📖 Tell the story: title as takeaway, caption as why

</div>

</div>

<div class="note-text mt-sm">

📌 Visualization is covered in much greater depth in **Lecture 7**.

</div>

---
hideInToc: true
---

# Reproducibility practices

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📓 Keep code with results (notebook discipline)

</div>

<div class="card card-secondary pad-tight">

## 📦 Parameterize and record environment (env.yaml)

</div>

<div class="card card-accent pad-tight">

## 🗂️ Version data/queries or capture snapshots

</div>

<div class="card card-info pad-tight">

## 🎲 Seed randomness; log configs and hashes

</div>

<div class="card card-success pad-tight">

## ⚙️ Automate critical paths (Makefile/CI)

</div>

</div>

---
hideInToc: true
---

# Roles and collaboration

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary pad-tight">

## 🧑‍🔬 **Domain expert**

<div class="note-text">Frames problems, validates insights</div>

</div>

<div class="card card-secondary pad-tight">

## 📊 **Analyst/Scientist**

<div class="note-text">Explores, models, communicates</div>

</div>

<div class="card card-accent pad-tight">

## 🔧 **Engineer**

<div class="note-text">Data access, reliability, pipelines</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info pad-tight">

## 📋 **PM/Lead**

<div class="note-text">Scope, impact, trade-offs</div>

</div>

<div class="card card-success pad-tight">

## 🤝 **Shared artifacts**

<div class="note-text">Glossary, metrics, dashboards</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Mini case study

<div class="card card-info pad-tight mt-md">

## 📡 **Scenario**
Detector shows intermittent spike counts on night shifts.

</div>

<div class="card card-primary pad-tight mt-md">

## 📋 **Plan**

- Define metric (spike rate/hour), segment by shift.
- Pull two weeks of logs; check missingness.
- Visualize rates; annotate configuration changes.
- Test difference-in-means with bootstrap CI (resampling-based confidence intervals).
- Prescribe mitigation if effect is robust.

</div>

---
hideInToc: true
---

# Common pitfalls

<div class="stack-tight mt-md">

<div class="card card-warning pad-tight">

## ⚠️ Overfitting pretty charts to noisy data

</div>

<div class="card card-warning pad-tight">

## ⚠️ Confusing proxy metrics with outcomes

</div>

<div class="card card-warning pad-tight">

## ⚠️ Ignoring units/timezones and data joins

</div>

<div class="card card-warning pad-tight">

## ⚠️ Confirmation bias; not seeking disconfirming evidence

</div>

<div class="card card-warning pad-tight">

## ⚠️ Shipping insights without reproducibility

</div>

</div>

---
hideInToc: true
---

# Useful patterns

<div class="stack-tight mt-md">

<div class="card card-success pad-tight">

## ✅ Start with a checklist (quality, ethics, uncertainty)

</div>

<div class="card card-success pad-tight">

## ✅ Write the "results" slide first; work backward

</div>

<div class="card card-success pad-tight">

## ✅ Keep a decisions log with assumptions

</div>

<div class="card card-success pad-tight">

## ✅ Pair-review visuals and statistical claims

</div>

<div class="card card-success pad-tight">

## ✅ Maintain a lightweight data dictionary

</div>

</div>

---
hideInToc: true
---

# Takeaways

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🎯 Define decisions and metrics early

</div>

<div class="card card-secondary pad-tight">

## 📊 Treat data quality and uncertainty as first-class

</div>

<div class="card card-accent pad-tight">

## 📢 Communicate with clarity and integrity

</div>

<div class="card card-success pad-tight">

## 🔄 Make it reproducible; make it useful

</div>

</div>

---
layout: section
hideInToc: true
---

# Examples of **data analysis** in different fields of science and industry

---
hideInToc: true
---

# **Bio medicine and Genomics**

<div class="card card-primary pad-tight mt-md">

<div class="stack-tight">

- ## 🧬 Genome Sequencing → identifying variants & gene expression patterns

- ## 💊 Clinical Trials → monitoring safety, efficacy, adaptive designs

- ## 📊 Population health dashboards & personalised medicine

- ## 🎯 Decisions: targeted therapies, drug discovery, diagnostics

</div>

</div>

<div class="card card-info pad-tight mt-md">

### 🧪 **23andMe** or **Ancestry.com** (ancestry services)? Comparing against *reference populations*

</div>

---
hideInToc: true
---

# **Environmental Sciences**

<div class="card card-accent pad-tight mt-md">

<div class="stack-tight">

- ## 🌍 Climate models integrating satellite, sensor, and historical data

- ## 🏭 Pollution monitoring at city/block resolution

- ## 🌿 Biodiversity studies combining field notes + remote sensing

- ## 📜 Supports policy making, disaster response, conservation funding

</div>

</div>

<div class="card card-info pad-tight mt-md">

<div class="note-text">

#### 🔄 Living analysis → data feeds update models continuously

</div>

</div>

---
hideInToc: true
---

# **Social Sciences**

<div class="card card-secondary pad-tight mt-md">

<div class="stack-tight">

- ## 📈 Economic forecasting blending macro indicators & behavioural data

- ## 🧑‍🤝‍🧑 Social behaviour studies using surveys, logs, ethnography

- ## 💬 Text analysis for sentiment, misinformation, community wellbeing

- ## 🏛️ Informs policy, marketing, product design, civic planning

</div>

</div>

<div class="card card-info pad-tight mt-md">

<div class="note-text">

#### 🔗 Qualitative + quantitative insights reinforce each other

</div>

</div>

---
hideInToc: true
---

# **Astronomy**

<div class="card card-primary pad-tight mt-md">

<div class="stack-tight">

- ## 🔭 Observational data analysis from telescopes, satellites, detectors

- ## 🌊 Gravitational wave detection via signal processing & ML

- ## 🌟 Cataloguing millions of celestial objects, anomaly detection

- ## 💻 Requires high-throughput computing, reproducible pipelines

</div>

</div>

<div class="card card-info pad-tight mt-md">

<div class="note-text">

#### 🤖 Fun fact: many ML innovations came from sky surveys

</div>

</div>

---
hideInToc: true
---

# **Particle Physics (CERN)**

<div class="card card-accent pad-tight mt-md">

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

# **Engineering**

<div class="card card-secondary pad-tight mt-md">

<div class="stack-tight">

- ## 🔧 Predictive maintenance on turbines, trains, manufacturing lines

- ## 👁️ Quality control with computer vision & statistical process control

- ## 📡 Structural health monitoring via sensors + physics-informed models

- ## 🎯 Outcomes: less downtime, safer infrastructure, cost optimisation

</div>

</div>

---
hideInToc: true
---

# **Healthcare Operations**

<div class="card card-warning pad-tight mt-md">

<div class="stack-tight">

- ## 🦠 Epidemiology tracking outbreaks & transmission dynamics

- ## 🏥 Health policy simulation for capacity planning & funding

- ## 🏗️ Hospital operations: patient flow, staffing, supply chain analytics

- ## ⚖️ Ethical considerations: privacy, bias, explainability

</div>

</div>

---
hideInToc: true
---

# **Finance**

<div class="card card-primary pad-tight mt-md">

<div class="stack-tight">

- ## 📈 Stock market analysis + algorithmic trading with latency constraints

- ## 🛡️ Risk management using stress tests, scenario analysis, VaR

- ## 🔍 Fraud detection & compliance monitoring with streaming data

- ## ⚖️ Balances profitability with regulation and transparency

</div>

</div>

---
hideInToc: true
---

# **Sports Analytics**

<div class="card card-success pad-tight mt-md">

<div class="stack-tight">

- ## 🏃 Performance analysis combining tracking sensors & video

- ## 🎮 Strategy optimisation: playbooks, opponent scouting

- ## 🎟️ Fan engagement through personalised content & ticket pricing

- ## 📊 Data informs coaching, recruitment, business growth

</div>

</div>

---
hideInToc: true
---

# **Product & Business Analytics**

<div class="card card-accent pad-tight mt-md">

<div class="stack-tight">

- ## 📊 Growth funnels: acquisition, activation, retention, revenue, referral

- ## 🧪 Experimentation: A/B tests, feature flagging, causal inference

- ## 👥 Customer segmentation & lifetime value in subscription models

- ## 🗺️ Guides product roadmaps, marketing spend, customer success

</div>

</div>

---
hideInToc: true
---

# **Public Policy & Urban Planning**

<div class="card card-info pad-tight mt-md">

<div class="stack-tight">

- ## 🏙️ Smart city sensors to manage transport, energy, waste

- ## 📂 Open data portals enabling transparency & civic innovation

- ## 🗺️ Geospatial analysis for zoning, emergency response, sustainability

- ## 🤝 Stakeholder engagement & ethical data sharing are crucial

</div>

</div>

---
hideInToc: true
---

# **Education & Learning Analytics**

<div class="card card-secondary pad-tight mt-md">

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

# Reflection — Which example resonates?

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔍 Where could similar data exist in your context?

</div>

<div class="card card-secondary pad-tight">

## 🎯 What decisions would better data unlock?

</div>

<div class="card card-accent pad-tight">

## 🚧 What obstacles — technical, ethical, organisational — stand in the way?

</div>

</div>

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

<div class="card card-primary pad-tight">

## 📊 **Tabular** — rows × columns (experiments, business metrics)

</div>

<div class="card card-secondary pad-tight">

## 🌳 **Hierarchical** — JSON/XML, nested logs, documents

</div>

<div class="card card-accent pad-tight">

## 🕸️ **Graph** — networks, relationships, supply chains

</div>

<div class="card card-info pad-tight">

## 🗺️ **Spatial & temporal** — GIS layers, time series, event streams

</div>

<div class="card card-warning pad-tight">

## 🖼️ **Multimedia** — images, audio, video, sensor waveforms

</div>

</div>

---
hideInToc: true
---

# Structured vs unstructured

<div class="grid-3 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📐 **Structured**

Predefined schema, SQL-friendly (lab results)

</div>

<div class="card card-secondary pad-tight">

## 🔖 **Semi-structured**

Consistent markers, flexible fields (JSON, HL7)

</div>

<div class="card card-accent pad-tight">

## 📝 **Unstructured**

Natural language, images, free-form signals

</div>

</div>

<div class="card card-info pad-tight mt-md">

<div class="note-text">

#### Choose storage, tooling, and cleaning strategies accordingly

</div>

</div>

---
hideInToc: true
---

# Levels of measurement

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🏷️ **Nominal** — categories without order (blood type, product ID)

</div>

<div class="card card-secondary pad-tight">

## 📶 **Ordinal** — ranked categories (survey Likert scales)

</div>

<div class="card card-accent pad-tight">

## 📏 **Interval** — consistent differences, no true zero (°C, calendar dates)

</div>

<div class="card card-info pad-tight">

## ⚖️ **Ratio** — meaningful zero & ratios (mass, revenue, counts)

</div>

</div>

<div class="card card-warning pad-tight mt-md">

<div class="note-text">

#### Measurement level dictates valid summaries & visualisations

</div>

</div>

---
hideInToc: true
---

# Granularity & unit of analysis

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔬 Define the entity: person, transaction, collision event, sensor ping

</div>

<div class="card card-secondary pad-tight">

## 📊 Aggregation level affects signal vs noise

</div>

<div class="card card-warning pad-tight">

## ⚠️ Misaligned granularity introduces bias & misleading conclusions

</div>

<div class="card card-info pad-tight">

## 📝 Document transformations between granularities

</div>

</div>

---
hideInToc: true
---

# Mind the time dimension

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📊 Cross-sectional vs time series vs panel data

</div>

<div class="card card-secondary pad-tight">

## ⏱️ Sampling frequency and latency influence what you can see

</div>

<div class="card card-accent pad-tight">

## 📈 Seasonality, trends, and lag effects require tailored methods

</div>

<div class="card card-info pad-tight">

## 🕐 Align timestamps, time zones, and calendars early

</div>

</div>

---
hideInToc: true
---

# Metadata keeps data alive

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 👤 Who collected it, when, where, how, and why?

</div>

<div class="card card-secondary pad-tight">

## 📐 Variable definitions, units, encoding schemes

</div>

<div class="card card-accent pad-tight">

## 🔗 Data lineage: transformations, assumptions, scripts, owners

</div>

<div class="card card-warning pad-tight">

## ⚠️ Without metadata the data become a liability, not an asset

</div>

</div>

---
hideInToc: true
---

# Data quality recap + two more dimensions

<div class="card card-info pad-compact mt-md">

**Recall the quality checklist** — completeness, consistency, validity, timeliness, lineage, ethics. Two extra dimensions worth highlighting:

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🎯 **Accuracy**

Does the recorded value reflect reality? Measurement error, transcription mistakes, and sensor drift all erode accuracy.

</div>

<div class="card card-success pad-tight">

## 🔢 **Uniqueness**

Are there unintended duplicates? Deduplication is critical when merging datasets or ingesting repeated feeds.

</div>

</div>

---
hideInToc: true
---

# Common data issues & biases

<div class="stack-tight mt-md">

<div class="card card-warning pad-tight">

## ❓ Missing data mechanisms (MCAR, MAR, MNAR)

</div>

<div class="card card-warning pad-tight">

## 📊 Outliers: true phenomena or collection errors?

</div>

<div class="card card-warning pad-tight">

## 🎯 Sampling bias & survivorship bias

</div>

<div class="card card-warning pad-tight">

## 🧠 Confirmation bias, p-hacking (see earlier definition), and multiple testing

</div>

<div class="card card-warning pad-tight">

## ⚖️ Ethical blind spots: representation, consent, accessibility

</div>

</div>

---
hideInToc: true
---

# **Continuous** and **Discrete** Data

<div class="grid-3 gap-md mt-md">

<div class="card card-primary pad-compact">

### 🔢 Quantitative / Numerical Data

</div>

<div class="card card-secondary pad-compact">

### 🏷️ Qualitative / Categorical Data

</div>

<div class="card card-accent pad-compact">

### 📅 Date and Time

</div>

</div>

<div style="text-align: center;" class="mt-md">

```mermaid
graph TD;
    A[Data] --> B[ **Qualitative**        ]
    A -->       C[ **Quantitative**       ]
    B -->       B1[**Hair color**         ]
    B -->       B2[**Customer Feedback**  ]
    C -->       D[ **Discrete**           ]
    C -->       E[ **Continuous**         ]
    D -->       D2[**Number of children** ]
    D -->       D3[**Counts of cattle**   ]
    E -->       E2[**Heights of patients**]
    E -->       E3[**Length of a snake**  ]

classDef node fill:none,stroke:white,stroke-width:3px,font-size:30px;
```
</div>

---
hideInToc: true
---

# Exercise · Audit your data sources

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 Pick one dataset you rely on

</div>

<div class="card card-secondary pad-tight">

## 🔬 Classify type, granularity, measurement levels, quality risks

</div>

<div class="card card-accent pad-tight">

## 📝 Note missing metadata you would need before analysis

</div>

</div>

---
layout: section
hideInToc: true
---

# Data Lifecycle & **Workflow**

---
hideInToc: true
---

# Lifecycle Recap — Six Key Phases

<div class="card card-info pad-compact mt-sm">

<div class="note-text">

Earlier we saw a detailed 9-stage lifecycle. Here is the same idea distilled into 6 high-level phases — easier to remember and apply day-to-day. The detailed stages nest inside these phases.

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-compact">

🎯 **Plan**

</div>

<div class="card card-secondary pad-compact">

📥 **Acquire**

</div>

<div class="card card-accent pad-compact">

💾 **Store**

</div>

<div class="card card-info pad-compact">

🔧 **Process**

</div>

<div class="card card-success pad-compact">

📊 **Analyse**

</div>

<div class="card card-warning pad-compact">

📢 **Share**

</div>

</div>

---
hideInToc: true
---

# Governance overlays every stage

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔒 Security, privacy, compliance, and ethics checks

</div>

<div class="card card-secondary pad-tight">

## 📝 Documentation and lineage updates

</div>

<div class="card card-accent pad-tight">

## ✅ Quality gates and automated tests

</div>

<div class="card card-info pad-tight">

## 🔄 Feedback loops from stakeholders and end users

</div>

</div>

---
hideInToc: true
---

# Analysis is iterative

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔄 Expect to loop between question ↔ data ↔ analysis ↔ insight

</div>

<div class="card card-secondary pad-tight">

## 🚧 Dead ends reveal where data, methods, or framing must change

</div>

<div class="card card-accent pad-tight">

## 🗂️ Maintain versioned checkpoints to compare approaches

</div>

<div class="card card-info pad-tight">

## 📢 Communicate progress, uncertainty, and trade-offs early

</div>

</div>

---
hideInToc: true
---

# From data to decisions

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 💡 Translate insights into recommendations & actions

</div>

<div class="card card-secondary pad-tight">

## 🎯 Align with organisational objectives and constraints

</div>

<div class="card card-accent pad-tight">

## 📏 Plan how outcomes will be measured post-decision

</div>

<div class="card card-info pad-tight">

## 📝 Capture learnings to refine future analyses

</div>

</div>

---
layout: section
hideInToc: true
---

# Steps of Data **Analysis**

Now we walk through each step in detail — these map onto the lifecycle phases above, but focus on the practical "how"

---
hideInToc: true
---

# 1. **Define the Problem or Research Question**

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🎯 Formulate the question with stakeholders and context

<div class="note-text">This might steer the choices in the following steps</div>

</div>

<div class="card card-secondary pad-tight">

## 📐 Translate goals into measurable metrics & hypotheses

</div>

<div class="card card-accent pad-tight">

## 🗺️ Map constraints: data access, time, ethics, skills

</div>

<div class="card card-info pad-tight">

## 🧪 Plan the experimental or observational design

</div>

</div>

<div class="card card-success pad-tight mt-md">

<div class="note-text">

#### Interactive exercise · Draft a SMART question for your project

</div>

</div>

---
hideInToc: true
---

# 2. **Collect Data** — Key Questions

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📊 How much data do you need?

</div>

<div class="card card-secondary pad-tight">

## 🏷️ What sort of data do you need?

</div>

<div class="card card-accent pad-tight">

## 📁 What data formats should you choose?

</div>

<div class="card card-info pad-tight">

## 🔍 Can you trust the data?

</div>

</div>

---
hideInToc: true
---

# 2. **Collect Data** — Best Practices

<div class="stack-tight mt-md">

<div class="card card-warning pad-tight">

## ⚙️ Can you collect the data? Assess feasibility early

</div>

<div class="card card-success pad-tight">

## 📝 Document permissions, consent, and provenance

</div>

<div class="card card-primary pad-tight">

## ✅ Automate validation checks at ingestion

</div>

</div>

---
hideInToc: true
---

# 3. **Clean Data**

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary pad-tight">

## 🔍 **Data Selection**

</div>

<div class="card card-secondary pad-tight">

## ✂️ **Data Stripping**

</div>

<div class="card card-accent pad-tight">

## 📊 **Data Skimming**

</div>

</div>

<div class="stack-tight">

<div class="card card-info pad-tight">

## 🔧 **Data Wrangling**

</div>

<div class="card card-warning pad-tight">

## ❓ Handle missing values, outliers, inconsistent categories

</div>

<div class="card card-success pad-tight">

## 📝 Record transformations for reproducibility

</div>

</div>

</div>

---
hideInToc: true
---

# 4. **Analyze Data**

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary pad-tight">

## 🔍 **Data Exploration**

</div>

<div class="card card-secondary pad-tight">

## 📊 **Statistical Analysis**

</div>

<div class="card card-accent pad-tight">

## 🧪 **Model Building**

</div>

</div>

<div class="stack-tight">

<div class="card card-info pad-tight">

## 🤖 **Machine Learning**

</div>

<div class="card card-warning pad-tight">

## 🧠 **Classification (...AI...)**

</div>

<div class="card card-success pad-tight">

## 📐 Evaluate assumptions, uncertainty, and sensitivity

</div>

</div>

</div>

<div class="card card-accent pad-tight mt-md">

<div class="note-text">

#### Compare baseline vs advanced methods

</div>

</div>

---
hideInToc: true
---

# 5. **Visualize the data**

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 👥 What's your target audience?

</div>

<div class="card card-secondary pad-tight">

## 💬 What is the message you want to convey?

</div>

<div class="card card-accent pad-tight">

## 🎨 Choose encodings that emphasise the core insight

</div>

<div class="card card-info pad-tight">

## ✏️ Iterate quickly with sketches before polishing

</div>

</div>

<div class="card card-warning pad-compact mt-md">

<div class="note-text">

#### 📌 We'll dive deep into visualization techniques, chart types, and storytelling with data in **Lecture 7**

</div>

</div>

---
hideInToc: true
---

# 6. **Interpret and report the results**

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🎯 Draw Conclusions from Data

</div>

<div class="card card-secondary pad-tight">

## 📄 Report Findings

</div>

<div class="card card-accent pad-tight">

## 🔗 Connect to decisions, risks, next steps

</div>

<div class="card card-info pad-tight">

## ❓ Capture limitations and open questions

</div>

<div class="card card-success pad-tight">

## 📦 Package reproducible assets (code, dashboards, docs)

</div>

</div>

---
hideInToc: true
---

# Validation & monitoring

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📊 Split data wisely, guard against leakage

</div>

<div class="card card-secondary pad-tight">

## 📐 Assess error bars, confidence intervals, effect sizes

</div>

<div class="card card-accent pad-tight">

## 🧪 Stress test with scenario analysis & sensitivity checks

</div>

<div class="card card-info pad-tight">

## 📡 Plan post-deployment monitoring for drift and quality

</div>

</div>

---
hideInToc: true
---

# Team checkpoints per phase

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🚀 **Kickoff** → align on question, scope, success metrics

</div>

<div class="card card-secondary pad-tight">

## 📊 **Midpoint** → share exploratory findings, data quality flags

</div>

<div class="card card-accent pad-tight">

## 🎤 **Pre-delivery** → rehearse narrative, anticipate objections

</div>

<div class="card card-info pad-tight">

## 📝 **Retrospective** → document lessons, update playbooks

</div>

</div>

---
hideInToc: true
---

# Communication toolkit

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📄 Executive summary (one-pager)

</div>

<div class="card card-secondary pad-tight">

## 📓 Notebook or reproducible analysis package

</div>

<div class="card card-accent pad-tight">

## 📊 Dashboard / data app for continued monitoring

</div>

<div class="card card-info pad-tight">

## 📋 Decision memo outlining options & trade-offs

</div>

<div class="card card-success pad-tight">

## 🔬 Technical appendix for peers to audit

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

<div class="card card-primary pad-tight">

## 📡 **Data sources** — sensors, APIs, files, databases, experiments

</div>

<div class="card card-secondary pad-tight">

## 📥 **Ingestion** — ETL/ELT tools, streaming pipelines, notebooks

</div>

<div class="card card-accent pad-tight">

## 💾 **Storage** — data lakes, warehouses, object stores, feature stores

</div>

<div class="card card-info pad-tight">

## 💻 **Compute** — notebooks, scripts, distributed clusters, cloud services

</div>

<div class="card card-success pad-tight">

## 📢 **Delivery** — dashboards, apps, reports, APIs, alerts

</div>

</div>

---
hideInToc: true
---

# People & roles

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🧑‍🔬 **Domain experts** anchor context and define value

</div>

<div class="card card-secondary pad-tight">

## 🔧 **Data engineers** ensure reliable, scalable pipelines

</div>

<div class="card card-accent pad-tight">

## 📊 **Analysts & scientists** explore, model, and interpret

</div>

<div class="card card-info pad-tight">

## 🎨 **Visualisation designers** craft compelling stories

</div>

<div class="card card-success pad-tight">

## ⚙️ **Product & ops teams** translate insight into action

</div>

</div>

---
hideInToc: true
---

# Collaboration rituals

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 Shared backlog with clear owners & due dates

</div>

<div class="card card-secondary pad-tight">

## 🔄 Version control (git) for notebooks, SQL, scripts

</div>

<div class="card card-accent pad-tight">

## 👁️ Code & analysis reviews to raise quality and share knowledge

</div>

<div class="card card-info pad-tight">

## 🤝 Pair sessions for tricky modelling or cleaning tasks

</div>

<div class="card card-success pad-tight">

## 📦 Reproducible environments (conda, containers, Poetry, Nix)

</div>

</div>

---
hideInToc: true
---

# Choosing the right artefact

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📓 **Notebooks** for exploration, teaching, storytelling

</div>

<div class="card card-secondary pad-tight">

## 📜 **Scripts & packages** for automation and reuse

</div>

<div class="card card-accent pad-tight">

## 📊 **Dashboards & apps** for ongoing monitoring

</div>

<div class="card card-info pad-tight">

## 🧪 **Experiments** for causal claims and product decisions

</div>

<div class="card card-success pad-tight">

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

<div class="card card-primary pad-tight">

## 🗄️ **SQL** remains foundational for structured data

</div>

<div class="card card-secondary pad-tight">

## 🐍 **Python** ecosystem (pandas, Polars, PySpark, SciPy, scikit-learn)

</div>

<div class="card card-accent pad-tight">

## 📊 **R** for statistics, visualisation, reproducible reports

</div>

<div class="card card-info pad-tight">

## 🚀 **Julia, Scala, Rust** for performance-critical workloads

</div>

<div class="card card-warning pad-tight">

## 🔬 **Domain-specific** tools (ROOT at CERN, SAS, MATLAB, SPSS)

</div>

</div>

---
hideInToc: true
---

# Tool snapshots

<div class="grid-3 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🏢 **Proprietary**
Tableau, Origin, Excel

</div>

<div class="card card-secondary pad-tight">

## 💻 **Languages**
Python, R, Julia

</div>

<div class="card card-accent pad-tight">

## 💡 **Tip**
Mix surface-level ease with depth and reproducibility

</div>

</div>

---
hideInToc: true
---

# **Proprietary** Tools

<div class="grid-2 gap-md mt-md">

<div class="card card-warning pad-tight">

## ⚠️ **Drawbacks**

- Expensive
- Limited in scope
- Lack compatibility
- Lack flexibility

</div>

<div class="card card-success pad-tight">

## ✅ **Benefits**

- Easy to learn / use (GUI)
- Great for rapid stakeholder demos & quick wins

</div>

</div>

---
hideInToc: true
---

# **Programming** Languages

<div class="grid-2 gap-md mt-md">

<div class="card card-success pad-tight">

## ✅ **Benefits**

- Open Source
- Free
- Powerful
- Scales from exploration to production

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Drawbacks**

- Steep learning curve (CLI)

</div>

</div>

---
hideInToc: true
---

# DataOps & automation

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## ⏱️ Schedule data pipelines with orchestration tools

</div>

<div class="card card-secondary pad-tight">

## 🔄 Leverage CI/CD for tests, linting, deployment

</div>

<div class="card card-accent pad-tight">

## 📐 Parameterise workflows for reproducibility

</div>

<div class="card card-info pad-tight">

## 📡 Monitor pipelines for latency, failures, data drift

</div>

</div>

---
hideInToc: true
---

# Testing your analysis

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🧪 Unit tests for data transforms & calculations

</div>

<div class="card card-secondary pad-tight">

## ✅ Data validation (great expectations, pydantic, pandera)

</div>

<div class="card card-accent pad-tight">

## 📊 Statistical tests to confirm assumptions

</div>

<div class="card card-info pad-tight">

## 📂 Golden datasets & regression tests for dashboards

</div>

<div class="card card-success pad-tight">

## 👁️ Peer review before results leave the team

</div>

</div>

---
hideInToc: true
---

# Documentation & knowledge sharing

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📖 Analyst runbooks and playbooks

</div>

<div class="card card-secondary pad-tight">

## 📋 Data dictionaries & catalogs

</div>

<div class="card card-accent pad-tight">

## 📝 Decision logs capturing context and rationale

</div>

<div class="card card-info pad-tight">

## 🎤 Internal demos & show-and-tell sessions

</div>

<div class="card card-success pad-tight">

## 🤝 Mentoring to spread tooling fluency

</div>

</div>

---
hideInToc: true
---

# **Discussion**

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🤔 When to use proprietary tools?

</div>

<div class="card card-secondary pad-tight">

## 🔧 What should you be using?

</div>

<div class="card card-accent pad-tight">

## 📈 Saturation of achieved proficiency

</div>

<div class="card card-info pad-tight">

## 🔄 How do we ensure reproducibility when collaborating?

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Hygiene**

---
hideInToc: true
---

# Why data hygiene matters

<div class="stack-tight mt-md">

<div class="card card-warning pad-tight">

## 🚫 Prevent costly errors & embarrassing corrections

</div>

<div class="card card-primary pad-tight">

## 🤝 Build trust with stakeholders & regulators

</div>

<div class="card card-secondary pad-tight">

## 🔄 Accelerate future analyses with reusable assets

</div>

<div class="card card-accent pad-tight">

## 🔒 Protect sensitive data and maintain compliance

</div>

<div class="card card-success pad-tight">

## 📦 Enable others to replicate or extend your work

</div>

</div>

---
hideInToc: true
---

# Hygiene habits to cultivate

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔄 Source control for data definitions and transformations

</div>

<div class="card card-secondary pad-tight">

## ✅ Automated linting & formatting for notebooks/scripts

</div>

<div class="card card-accent pad-tight">

## 📁 Clear folder structures & naming conventions

</div>

<div class="card card-info pad-tight">

## 🗂️ Versioned datasets or snapshotting

</div>

<div class="card card-success pad-tight">

## 🧹 Regular housekeeping: archive, deprecate, document

</div>

</div>

---
hideInToc: true
---

# Ethics & responsible analytics

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🛡️ Minimise harm: privacy, consent, security

</div>

<div class="card card-secondary pad-tight">

## ⚖️ Fairness: monitor for disparate impact across groups

</div>

<div class="card card-accent pad-tight">

## 🔍 Transparency: explain methods, assumptions, limitations

</div>

<div class="card card-info pad-tight">

## 👤 Accountability: define owners and escalation paths

</div>

<div class="card card-success pad-tight">

## 🌍 Sustainability: consider computational & environmental cost

</div>

</div>

---
hideInToc: true
---

# Data governance essentials

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🔐 Policies for access control and approvals

</div>

<div class="card card-secondary pad-tight">

## 📋 Data catalogues & stewardship roles

</div>

<div class="card card-accent pad-tight">

## 📜 Compliance frameworks (GDPR, HIPAA, CERN policies)

</div>

<div class="card card-info pad-tight">

## 🚨 Incident response plans for data breaches or quality issues

</div>

<div class="card card-success pad-tight">

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

## The first step in **(re)using data** is to find them. **Metadata** and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services, so this is an essential component of the FAIRification process.

---
hideInToc: true
---

# **Findable** data

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🏷️ **F1.** (Meta)data are assigned a globally **unique** and persistent **identifier**

</div>

<div class="card card-secondary pad-tight">

## 📝 **F2.** Data are described with **rich metadata**

</div>

<div class="card card-accent pad-tight">

## 🔗 **F3.** Metadata explicitly **include the identifier** of the data they describe

</div>

<div class="card card-info pad-tight">

## 🔍 **F4.** (Meta)data are registered or indexed in a **searchable resource**

</div>

</div>

---
hideInToc: true
---

# What is **Metadata**?

<div class="card card-warning pad-tight mt-md">

## 📋 **Metadata** = data about data

Metadata describes the who, what, when, where, how, and why of a dataset. Examples: column names and types, units, collection date, author, license, provenance, and schema version.

</div>

<div class="card card-info pad-tight mt-md">

## 🔍 **Why it matters for FAIR**

Without rich metadata, datasets cannot be found, understood, or reused. Machine-readable metadata enables automated discovery and integration across systems.

</div>

---
hideInToc: true
---

# **Accessible** data

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🌐 **A1.** **(Meta)data** are retrievable by their **identifier** using a standardised communications protocol

</div>

<div class="card card-secondary pad-tight">

### 📖 **A1.1** The protocol is **open**, free, and universally implementable

</div>

<div class="card card-accent pad-tight">

### 🔐 **A1.2** The protocol allows for an **authentication** and **authorisation** procedure, where necessary

</div>

<div class="card card-info pad-tight">

## 📂 **A2.** Metadata are accessible, even when the data are no longer available

</div>

</div>

---
hideInToc: true
---

# **Interoperable** data

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🗣️ **I1.** (Meta)data use a formal, accessible, shared, and broadly applicable **language for knowledge representation**

</div>

<div class="card card-secondary pad-tight">

## 🔗 **I2.** (Meta)data use vocabularies that follow **FAIR principles**

</div>

<div class="card card-accent pad-tight">

## 📎 **I3.** (Meta)data include **qualified references** to other (meta)data

</div>

</div>

---
hideInToc: true
---

# **Reusable** data

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 **R1.** (Meta)data are **richly described** with a plurality of accurate and relevant attributes

</div>

<div class="card card-secondary pad-tight">

### 📜 **R1.1.** (Meta)data are released with a clear and **accessible** data usage **license**

</div>

<div class="card card-accent pad-tight">

### 🔗 **R1.2.** (Meta)data are associated with detailed **provenance**

</div>

<div class="card card-info pad-tight">

### 🏛️ **R1.3.** (Meta)data meet **domain-relevant community standards**

</div>

</div>

---
hideInToc: true
---

# FAIR in practice

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🏷️ Assign DOIs or persistent IDs through catalogues

</div>

<div class="card card-secondary pad-tight">

## 📝 Publish rich metadata schemas (DCAT, schema.org, Invenio)

</div>

<div class="card card-accent pad-tight">

## 🌐 Provide API/documentation for programmatic access

</div>

<div class="card card-info pad-tight">

## 📖 Reuse domain ontologies and controlled vocabularies

</div>

<div class="card card-success pad-tight">

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

<div class="card card-primary pad-tight mt-md">

- ## 🌐 CERN releases proton-proton collision datasets via the Open Data portal

- ## 🎯 Goal: enable students & researchers to reproduce landmark analyses

- ## 📁 Data formats: ROOT files, CSV summaries, metadata packages

- ## 🔧 Tooling: ROOT, python, R, Jupyter, cloud notebooks

</div>

---
hideInToc: true
---

# Collaboration model

<div class="card card-secondary pad-tight mt-md">

- ## 👥 Physicists, statisticians, software engineers, detector experts

- ## 🔄 Shared code repositories with rigorous review (ROOT macros, python)

- ## 🧪 Simulation teams provide synthetic data for validation

- ## 📄 Publication committees ensure rigour & messaging

</div>

---
hideInToc: true
---

# Risks & mitigations

<div class="grid-2 gap-md mt-md">

<div class="card card-warning pad-tight">

## ⚠️ **Detector anomalies**

<div class="note-text">Continuous monitoring & calibration</div>

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Bias in selection cuts**

<div class="note-text">Blind analyses & control regions</div>

</div>

<div class="card card-success pad-tight">

## ✅ **Reproducibility**

<div class="note-text">Containerised environments, notebooks, docs</div>

</div>

<div class="card card-success pad-tight">

## ✅ **Communication**

<div class="note-text">Translate particle jargon for broader audiences</div>

</div>

</div>

---
hideInToc: true
---

# Exercise · Plan your own analysis

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📋 Pick a dataset (CERN or your organisation)

</div>

<div class="card card-secondary pad-tight">

## 🔧 Draft a 6-step workflow referencing today's framework

</div>

<div class="card card-accent pad-tight">

## 👥 Identify stakeholders, success metrics, and key risks

</div>

<div class="card card-info pad-tight">

## 📦 Decide what artefact you would deliver

</div>

</div>

---
hideInToc: true
---

# Lessons from CERN for everyone else

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📝 Document everything — you never know who will re-run it

</div>

<div class="card card-secondary pad-tight">

## 🔧 Invest in shared tooling and platforms early

</div>

<div class="card card-accent pad-tight">

## 🌐 Open data accelerates innovation beyond your organisation

</div>

<div class="card card-info pad-tight">

## 👁️ Rigorous peer review can coexist with fast iteration

</div>

<div class="card card-success pad-tight">

## 🎉 Celebrate small wins: incremental insights build trust

</div>

</div>

---
layout: section
hideInToc: true
---

# Wrap-up & **Next Steps**

---
hideInToc: true
---

# Key takeaways

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🎯 Start with the decision, not the data

</div>

<div class="card card-secondary pad-tight">

## 🔄 Treat data analysis as an iterative, collaborative lifecycle

</div>

<div class="card card-accent pad-tight">

## 🧹 Healthy data hygiene & governance underpin trustworthy insights

</div>

<div class="card card-info pad-tight">

## 🔧 Choose tools intentionally to balance speed, scale, and rigour

</div>

</div>

<div class="card card-success pad-tight mt-md">

## 📢 Communicate clearly, ethically, and with empathy for your audience

</div>
