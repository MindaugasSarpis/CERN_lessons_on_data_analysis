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

# Why Learn This Now?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🧭 **Framework Before Tools**

You have learned Python. Before diving into libraries and datasets, you need a conceptual framework for *thinking* about data — what it is, how to handle it, and what can go wrong.

</div>

<div class="card card-secondary pad-tight">

## 🔬 **From CERN to Industry**

These concepts — lifecycle, quality, ethics, FAIR principles — apply identically whether you are analysing collision data at CERN or customer behaviour at a startup.

</div>

</div>

<div class="card card-info pad-tight mt-md">

## 🎯 **This Lecture**

We will build the mental model: data types, quality, the analysis lifecycle, and key pitfalls to avoid.

</div>

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

📌 Visualization principles are covered in the next lecture (**Data Visualization**). Practical tools (matplotlib, Pandas) come later in the course.

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

<div class="card card-info pad-tight mt-md">

## 📚 **Deep-dive topics** — data fundamentals, FAIR principles, tools & collaboration, data hygiene, and field-by-field examples are covered in a dedicated extended session

</div>
