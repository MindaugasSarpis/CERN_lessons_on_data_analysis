---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false
mermaid: true


title: "Concepts of Data Analysis"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Concepts of Data Analysis

##### <span class="aims-badge">♻️ reproducibility · 📁 data & files</span>

<!--
Speaker: open by naming the two aims this lecture serves — reproducibility and
efficient work with data. Frame today as the mental model that must come BEFORE
tools: what data is, how to judge it, and what goes wrong. (~1 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🎯 Frame every analysis around the **decision** it must support

</div>

<div class="card card-secondary card-glass pad-compact">

🔍 Tell apart **descriptive, diagnostic, predictive, and prescriptive** analysis

</div>

<div class="card card-accent card-glass pad-compact">

✅ Audit data against a **quality checklist** and read missing-data mechanisms

</div>

<div class="card card-success card-glass pad-compact">

🔄 Walk data through the full **analysis lifecycle** — plan to share

</div>

<div class="card card-warning card-glass pad-compact">

♻️ Make results **reproducible** — ready for the FAIR practices of Lecture 14

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Stress the through-line —
"start from the decision" — and tell them Seminar 9 is where they audit their
own dataset's quality. (~1 min)
-->

---
hideInToc: true
---

<div class="def-stack">

<div class="card card-primary card-glass def-card">

## 📋 **Data**

<div v-click="[1, 2]" class="def-ex">

<span class="def-sub">Units of meaning — values that describe or measure</span>

Discrete or continuous values that convey information — quantities, qualities, facts, or symbols to be interpreted. *A datum is one such value.* <span class="def-src">— Wikipedia</span>

</div>

</div>

<div class="card card-secondary card-glass def-card">

## 🔍 **Data Analysis**

<div v-click="[2, 3]" class="def-ex">

<span class="def-sub">Turning data into conclusions and decisions</span>

The process of **inspecting, cleaning, transforming, and modelling** data to discover useful information, inform conclusions, and support decision-making. <span class="def-src">— Wikipedia</span>

</div>

</div>

<div class="card card-accent card-glass def-card">

## 🧪 **Data Science**

<div v-click="[3, 4]" class="def-ex">

<span class="def-sub">Analysis + computing + algorithms at scale</span>

An interdisciplinary field combining statistics, scientific computing, visualisation, and algorithms to extract **knowledge and insights** from noisy, structured, or unstructured data. <span class="def-src">— Wikipedia</span>

</div>

</div>

</div>

<style>
.def-stack {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-top: 0.5rem;
}
.def-card.card {
  padding: 0.7rem 1.2rem !important;
  overflow: hidden;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              padding 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.def-card.card:has(.def-ex:not(.slidev-vclick-hidden)) {
  padding: 0.45rem 1.1rem 0.55rem !important;
}
.def-card.slidev-vclick-hidden {
  transform: translateX(-40px);
  opacity: 0 !important;
  visibility: visible !important;
  pointer-events: none;
}
.def-card h2 {
  font-size: 1.4em;
  line-height: 1.15;
  margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.def-card:has(.def-ex:not(.slidev-vclick-hidden)) h2 {
  font-size: 1em;
}
.def-sub {
  display: block;
  font-size: 0.92em;
  opacity: 0.85;
  margin-top: 0.05em;
  font-style: italic;
}
.def-ex {
  max-height: 300px;
  opacity: 0.9;
  overflow: hidden;
  font-size: 0.82em;
  margin-top: 0.2rem;
  line-height: 1.3;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease,
              margin-top 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.def-ex.slidev-vclick-hidden {
  max-height: 0 !important;
  opacity: 0 !important;
  visibility: visible !important;
  margin-top: 0 !important;
  pointer-events: none;
}
.def-src {
  opacity: 0.6;
  font-style: italic;
  font-size: 0.9em;
  margin-left: 0.3em;
}
</style>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧭 **Framework Before Tools**

You have learned Python. Before diving into libraries and datasets, you need a conceptual framework for *thinking* about data — what it is, how to handle it, and what can go wrong.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔬 **From CERN to Industry**

These concepts — lifecycle, quality, ethics, governance — apply identically whether you are analysing collision data at CERN or customer behaviour at a startup.

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 🎯 **This Lecture**

We build the mental model: data types, quality, the analysis lifecycle, tools, hygiene, ethics, and key pitfalls to avoid.

</div>

---
hideInToc: true
---

# One principle above all · **Decisions first**

<span class="def-sub">Every technique in this lecture is in service of this single idea. Keep it in mind as each concept lands.</span>

<div class="grid-2 gap-md mt-md tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Start from the decision, not the data**

Who will act on the result? On what timeline? What changes if the answer flips? If no one acts, it is not analysis — it is decoration.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Define success before you touch a row**

Pick the metric, the threshold, and the acceptance criterion up front. Otherwise every plot looks interesting and none is conclusive.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Without a decision, rigour is theatre**

Quality checks, documentation, reproducibility — they matter *because* a decision depends on the output. Strip the decision and the discipline collapses.

</div>

<div class="card card-success card-glass pad-compact">

## 🔁 **Re-ask at every step**

"What decision am I supporting?" is the single best prompt against scope creep, p-hacking, and lost weekends of modelling for its own sake.

</div>

</div>

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
  <div class="flow-text"><code>2025-10-24 10:24, 22.3°C</code></div>
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
  height: calc(100% - 4rem); /* leave room for the slide title */
  gap: 0;
}
.flow-row {
  display: flex !important;
  align-items: center;
  gap: 1rem;
  width: 90%;
  padding: 0.85rem 1.5rem !important;
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

# Analysis bridges **data → decisions**

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 📈 **Raw data**

- Sensors, logs, experiments, surveys, the web
- Volume, velocity, variety keep rising
- Too much to read, too messy to trust
- Value is locked inside noise

</div>

<div class="card card-accent card-glass pad-tight">

## 🌉 **Analysis**

- **Inspect** — what's really in the data?
- **Clean** — fix errors, gaps, units
- **Model** — find structure and patterns
- **Explain** — communicate with uncertainty

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 **Decisions**

- Publish a result, approve a treatment
- Ship a product, set a policy
- Every stakeholder now asks: *what does the data say?*
- Without analysis, decisions are just opinion

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

<div class="note-text">

*Some questions preview ideas you'll formalise later — focus on the reasoning behind each answer.*

</div>

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

<style>
/* The MCQ fills 100% height for standalone use; with the preamble above it
   this slide would overflow by exactly the preamble's height. */
.mcq-container { height: calc(100% - 5rem) !important; }
</style>

---
hideInToc: true
---

<MCQ
  question="A plot shows a histogram of the K-pi invariant mass for 60,000 LHCb events. What type of analytics is this?"
  :options="[
    'Descriptive — it summarises what the data look like',
    'Diagnostic — it explains why the mass takes these values',
    'Predictive — it forecasts the mass of the next event',
    'Prescriptive — it recommends a selection cut'
  ]"
  :correct="0"
  explanation="Plotting the distribution of a measured quantity — no explanation, forecast, or recommendation attached — is the textbook example of descriptive analytics: what the data look like, nothing more."
/>

---
hideInToc: true
---

<MCQ
  question="The K-pi mass histogram shows a clear peak near 1865 MeV. An analyst investigates and attributes it to real D0 -> K- pi+ decays rather than combinatorial background. What type of analytics is this?"
  :options="[
    'Descriptive — it reports where the peak sits',
    'Diagnostic — it explains why the peak is there',
    'Predictive — it forecasts future peaks',
    'Prescriptive — it recommends a physics decision'
  ]"
  :correct="1"
  explanation="Going beyond 'there is a peak' to 'here is the physical reason the peak appears' is diagnostic analytics — explaining the cause of an observed pattern, one step past description but short of forecasting or recommending action."
/>

---
hideInToc: true
---

<MCQ
  question="A logistics system suggests the optimal truck-routing plan each morning under current traffic and fuel prices. What type of analytics is this?"
  :options="[
    'Descriptive — it reports yesterday\'s routes',
    'Diagnostic — it explains past delays',
    'Predictive — it forecasts traffic',
    'Prescriptive — it recommends the best action'
  ]"
  :correct="3"
  explanation="The system goes past forecasting and actually recommends the action to take (the route). That is prescriptive analytics — it may use predictive models internally, but its output is a decision."
/>

---
hideInToc: true
---

<MCQ
  question="A team trains a model that forecasts equipment failure AND outputs the maintenance schedule that minimises downtime cost. Best classification?"
  :options="[
    'Purely predictive — it only estimates failure probability',
    'Purely diagnostic — it explains failures',
    'Prescriptive — the end product is an optimal action plan',
    'Descriptive — it summarises failure history'
  ]"
  :correct="2"
  explanation="Predictive analytics is a *component* here, but the deliverable is a recommended schedule optimising a cost objective. Whenever the output is an action or decision, the pipeline as a whole is prescriptive."
/>

---
hideInToc: true
---

<MCQ
  question="A researcher fits a causal model to estimate how a new teaching method would change exam scores if rolled out. Which label fits best, and why is it subtle?"
  :options="[
    'Descriptive — it uses historical exam data',
    'Diagnostic — it explains past score variation',
    'Predictive — it forecasts future scores',
    'Prescriptive / causal — it estimates the effect of an intervention'
  ]"
  :correct="3"
  explanation="A pure predictive model answers 'what score will I see?' under the status quo. A causal / interventional model answers 'what would happen if we changed something?' — the basis for prescriptive recommendations. The subtlety: both use historical data and both output numbers, but only the causal one supports decisions about actions."
/>

---
hideInToc: true
---

# Miniature end-to-end · **Do students prefer coffee A or B?**

<span class="def-sub">Before we dive into concepts, here is the entire arc in one toy example — so every slide that follows has a concrete thing to hang on.</span>

<div class="grid-3 gap-md mt-md tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **Define**

*"Should the café stock A or B?"* — decision: which beans to order next month. Metric: preference rate. Threshold: call a winner if the gap > 10 pp.

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Collect**

Blind taste test, 100 volunteers, randomised cup order. Log preference + year-of-study as covariate.

</div>

<div class="card card-accent card-glass pad-compact">

## 3️⃣ **Explore**

Tabulate counts: 65 prefer A, 35 prefer B. Sanity check: no year-of-study bias; no dropouts.

</div>

<div class="card card-info card-glass pad-compact">

## 4️⃣ **Model**

Binomial test on 65/100 vs 50/50 null. *p* ≈ 0.003. 95 % CI for A's preference: 55–74 %.

</div>

<div class="card card-success card-glass pad-compact">

## 5️⃣ **Communicate**

*"A wins 65 % vs 35 %, CI 55–74 %. Gap exceeds threshold — order A."* One sentence, one number, one decision.

</div>

<div class="card card-warning card-glass pad-compact">

## 6️⃣ **What could still go wrong?**

Sample of 100 ≠ all students. Taste may vary by time of day. Next iteration: repeat across shifts before locking in.

</div>

</div>

*The formal statistical test behind step 4 — and what a p-value and confidence interval actually mean — is covered in the Probability & Statistics lecture. Focus here on the logic: is the difference big enough to trust?*

---
hideInToc: true
---

# Data comes in many shapes

<span class="def-sub">The *shape* of your data decides which tools, file formats, and mental models apply. Pick the wrong shape and every later step fights you. Click a card to expand.</span>

<div class="grid-2 gap-sm dd-stack shapes-stack mt-md">

<details name="shapes" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">📊 <strong>Tabular</strong> — rows × columns</span></summary>
<div class="dd-body">

**Each row is an observation, each column a variable.** The workhorse shape: experimental results, business metrics, surveys, most CSVs you will ever meet.

- *Typical formats:* CSV, TSV, Parquet, Feather, SQL tables, Excel sheets, pandas / Polars / R dataframes
- *Ecosystem:* SQL, pandas, Polars, DuckDB, Arrow; dashboards (Tableau, Looker, Metabase); almost every ML library ingests a 2-D array
- *Strengths:* joins, group-by aggregations, vectorised maths, columnar compression, decades of battle-tested tooling
- *Variable types:* numeric (int, float), categorical, ordinal, boolean, datetime, text — each needs its own cleaning strategy
- *Gotchas:* mixed units across rows; columns silently changing type on import; `NaN` vs empty string vs `"NA"`; wide-vs-long confusion; silent integer overflow in aggregations
- *Wide vs long:* wide = one row per subject, many measurement columns; long = one row per measurement. Plotting and modelling usually want long; reporting usually wants wide
- *CERN example:* per-event summary tables with columns like `event_id`, `energy_gev`, `pt`, `eta`, `phi`, `trigger_flag` — one file per run, millions of rows

</div>
</details>

<details name="shapes" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">🌳 <strong>Hierarchical</strong> — nested trees</span></summary>
<div class="dd-body">

**Records contain sub-records, sometimes recursively.** One event has many tracks; one patient has many visits, each with many measurements, each with many lab values.

- *Typical formats:* JSON, XML, YAML, HDF5 groups, ROOT TTrees / RNTuples, Protobuf messages, Avro
- *Ecosystem:* jq and XPath for querying; uproot / awkward-array for ROOT in Python; HDF5 for scientific blobs; document databases (MongoDB, Couchbase)
- *Strengths:* faithful to real-world structure; schema can evolve per branch; variable-length arrays are first-class; self-describing (schema lives with data)
- *Variable-length vs fixed:* a key distinction — an event with *N* tracks (where *N* varies) cannot be flattened to a rectangular table without either repetition or loss
- *Gotchas:* hard to flatten without data loss; joins become awkward; deep nesting kills readability; schema evolution is a minefield when older consumers read newer data
- *Access patterns:* selective branch reads (ROOT, Parquet nested columns) let you touch only the fields you need — critical at petabyte scale
- *CERN example:* a ROOT event record holding variable-length arrays of tracks, each track carrying `pt`, `eta`, `phi`, `hits[]`, plus event-level metadata (run, lumi, vertices)

</div>
</details>

<details name="shapes" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">🕸️ <strong>Graph</strong> — nodes and edges</span></summary>
<div class="dd-body">

**The relationships *are* the data.** A table of "who follows whom" loses the structure the moment you query it; a graph keeps paths, cycles, and neighbourhoods first-class.

- *Typical formats:* edge lists (CSV), GraphML, Neo4j, RDF/SPARQL
- *Strengths:* shortest-path, centrality, community detection, provenance chains
- *Gotchas:* no single canonical layout; visualisations mislead at scale
- *CERN example:* detector-geometry dependency graphs; collaboration/author networks

</div>
</details>

<details name="shapes" class="dd-card card card-info card-glass">
<summary><span class="dd-title">🗺️ <strong>Spatial & temporal</strong> — coordinates and time</span></summary>
<div class="dd-body">

**Order and proximity matter.** Shuffling rows in a tabular dataset is fine; shuffling time stamps destroys the signal.

- *Typical formats:* GeoJSON, Shapefile, NetCDF, Parquet partitioned by date, event streams (Kafka)
- *Strengths:* windowing, rolling stats, spatial joins, trajectory analysis
- *Gotchas:* timezones, daylight saving, coordinate reference systems, irregular sampling
- *CERN example:* beam-intensity time series; detector-hit spatial coordinates

</div>
</details>

<details name="shapes" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">🖼️ <strong>Multimedia</strong> — images, audio, waveforms</span></summary>
<div class="dd-body">

**Dense, high-dimensional signals.** A 4 K image is ~8 million pixels — about 25 million numbers in RGB; a 1 s audio waveform is tens of thousands of samples. Analysis usually means *feature extraction* first.

- *Typical formats:* PNG/JPEG, WAV/FLAC, MP4, raw tensors, HDF5
- *Strengths:* convolutional models, signal processing, transfer learning from pretrained nets
- *Gotchas:* storage costs, labelling effort, leakage through metadata (EXIF, filename patterns)
- *CERN example:* calorimeter "images" for jet classification; detector scan videos

</div>
</details>

<details name="shapes" class="dd-card card card-success card-glass">
<summary><span class="dd-title">📝 <strong>Text</strong> — free-form language</span></summary>
<div class="dd-body">

**Unstructured on the surface, richly structured inside** (tokens, syntax, semantics). Often mixed with tabular metadata (author, timestamp).

- *Typical formats:* plain text, Markdown, PDF, HTML, log files
- *Strengths:* embeddings, topic models, entity extraction, RAG pipelines
- *Gotchas:* encoding issues, boilerplate, deduplication, PII leakage
- *CERN example:* elog entries; beam operator run comments; detector alarm logs

</div>
</details>

</div>

<div class="card card-info card-glass pad-compact mt-sm">

## 💡 **Choose the shape, then the tool**

Many datasets *can* be coerced into a table, but not always *should* be. Forcing a graph into rows loses the relationships; flattening a ROOT TTree into a DataFrame loses the per-event structure. **Match the shape to the question.**

</div>

<style scoped>
.shapes-stack { position: relative; }
.shapes-stack .dd-card { position: relative; }
.shapes-stack .dd-card[open] { z-index: 20; }
.shapes-stack .dd-card[open] > .dd-body {
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  margin-top: 0.35rem;
  max-height: 300px;
  overflow-y: auto;
  padding: 0.75rem 1rem;
  background: linear-gradient(140deg, rgba(2,6,23,0.97), rgba(15,23,42,0.95));
  border: 1px solid rgba(148,163,184,0.45);
  border-radius: 0.6rem;
  box-shadow: 0 16px 40px rgba(0,0,0,0.55);
  font-size: 0.82em;
  line-height: 1.35;
  backdrop-filter: blur(8px);
}
.shapes-stack .dd-card:nth-last-child(-n+2)[open] > .dd-body {
  top: auto;
  bottom: 100%;
  margin-top: 0;
  margin-bottom: 0.35rem;
  max-height: 200px;
}
.shapes-stack .dd-body ul { margin: 0.3rem 0 0; padding-left: 1.1rem; }
.shapes-stack .dd-body li { margin: 0.15rem 0; }
.shapes-stack .dd-title { font-size: 0.95em; }
</style>

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
hideInToc: true
---

# Data quality checklist

<span class="def-sub">You know *what* data looks like. Now: can you trust it? Every downstream decision rests on that answer — start by auditing these eight dimensions.</span>

<div class="grid-2 gap-md mt-md tidy-cards">

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

# What the checklist catches · **a documented case**

<span class="def-sub">In 2010 an influential economics paper (Reinhart & Rogoff) linked high public debt to negative growth. A 2013 re-analysis found the result rested on a **spreadsheet error and selective data** — each gap below maps back to a checklist dimension. *(Details simplified; see Herndon, Ash & Pollin 2013.)*</span>

<div class="grid-2 gap-md mt-md tidy-cards">

<div class="card card-warning card-glass pad-compact">

## ❓ **Completeness missed**

Several countries' high-debt, high-growth years were **left out of the average** — the visible spreadsheet looked complete, but rows were silently excluded.

</div>

<div class="card card-warning card-glass pad-compact">

## 🔗 **Consistency missed**

Countries were weighted inconsistently, so one country's single bad year counted as much as another's two decades of data.

</div>

<div class="card card-warning card-glass pad-compact">

## 📐 **Validity missed**

A formula that was supposed to average a column of countries only spanned **part of the range** — the classic off-by-a-few spreadsheet slip.

</div>

<div class="card card-warning card-glass pad-compact">

## 🔄 **Lineage missed**

The cleaning steps lived in a one-off notebook. When a reviewer asked "why were these rows excluded?", no one could answer.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 💡 **The lesson**

No single failure was exotic. Each one is on the checklist we just reviewed. **Data quality is not a vibe — it is a list you run.**

</div>

---
hideInToc: true
---

# Common data issues & biases

<div class="stack-tight mt-md tidy-cards">

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

# Missing-data mechanisms — **why** values are missing

<span class="def-sub">The *reason* data are missing dictates which imputation and analysis methods are valid: **test** whether they're missing completely at random (MCAR), **assume** missing-at-random (MAR) when justified, and **reason carefully** about missing-not-at-random (MNAR) using domain knowledge.</span>

<div class="miss-row mt-md">

<div class="card card-success card-glass miss-card">

## 🎲 **MCAR**

<span class="def-sub">Missing Completely At Random</span>

<div class="miss-ex">

Independent of everything — observed or not.

- *Ex.:* flaky cable drops sensor readings
- Dropping rows is **unbiased** (just weaker)
- Testable (Little's test)

</div>

</div>

<div class="card card-warning card-glass miss-card">

## 📊 **MAR**

<span class="def-sub">Missing At Random</span>

<div class="miss-ex">

Depends on *observed* vars, not the missing value.

- *Ex.:* men skip "weight" more; random given gender
- Dropping rows is **biased**
- Fix: multiple imputation on covariates
- Assumed — justify it

</div>

</div>

<div class="card card-accent card-glass miss-card">

## 🚨 **MNAR**

<span class="def-sub">Missing Not At Random</span>

<div class="miss-ex">

Depends on the *unobserved* value itself.

- *Ex.:* high earners hide income
- **No fix from data alone**
- Needs a missingness model or sensitivity analysis
- Reason from domain knowledge

</div>

</div>

</div>

---
hideInToc: true
---

# Uncertainty and inference

<span class="def-sub">🌡️ `22.3 °C` means nothing without `± 0.2 °C`. Every reported number deserves the same treatment.</span>

<div class="grid-3 gap-sm mt-sm tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 📊 **Report uncertainty**

CIs, credible intervals, SEs — never a bare point estimate.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Guard against p-hacking**

Pre-register the plan. Don't fish for significance.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Power matters**

Effect size, N, variance — know what you can detect *before* testing.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔗 **Correlation ≠ causation**

An association alone doesn't prove A causes B; establishing causation needs careful experimental design or dedicated statistical methods (see the Probability & Statistics lecture).

</div>

<div class="card card-info card-glass pad-compact">

## 🧪 **Sensitivity analyses**

Perturb assumptions — does the conclusion survive?

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **Replicate**

One result is a hint; many are evidence.

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="You fit a model with 50 parameters to 60 data points and get 99.9 % accuracy on your TRAINING set. What should you conclude from that number alone?"
  :options="[
    'The model works — high training accuracy proves it',
    'Almost nothing — with so many parameters, memorising the training data is expected; only held-out data can tell you if it generalises',
    'The model must be underfitting',
    'Training accuracy is the only metric that matters'
  ]"
  :correct="1"
  explanation="With nearly as many parameters as data points, a model can memorise the training set and score ~100 % without learning anything generalisable — classic overfitting. Training accuracy alone is uninformative; you must evaluate on a held-out test set (or via cross-validation)."
/>

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

<div class="grid-3 gap-sm mt-sm stage-grid">

<details name="stage" class="card card-primary card-glass stage-card">
<summary>
<span class="stage-title"><strong>🎯 Plan</strong> · Problem Framing</span>
<span class="stage-sub">hypotheses & success metrics</span>
</summary>
<div class="stage-ex">

Translate a vague question into a precise one. Define the decision the analysis must support, the success metric, and what would falsify your hypothesis **before** touching data.

</div>
</details>

<details name="stage" class="card card-secondary card-glass stage-card">
<summary>
<span class="stage-title"><strong>🔍 Acquire</strong> · Data Discovery</span>
<span class="stage-sub">access & quality assessment</span>
</summary>
<div class="stage-ex">

Find sources, negotiate access, document provenance, and check coverage, freshness, and completeness against the question you framed.

</div>
</details>

<details name="stage" class="card card-accent card-glass stage-card">
<summary>
<span class="stage-title"><strong>🧹 Process</strong> · Preparation</span>
<span class="stage-sub">cleaning, joining, features</span>
</summary>
<div class="stage-ex">

Fix types, units, duplicates, missing values; join tables on stable keys; engineer features that encode domain knowledge. Usually the biggest chunk of work.

</div>
</details>

<details name="stage" class="card card-info card-glass stage-card">
<summary>
<span class="stage-title"><strong>📊 Analyse</strong> · Exploration</span>
<span class="stage-sub">profiling, viz, sanity checks</span>
</summary>
<div class="stage-ex">

Plot distributions, scan outliers, check expected relationships. Build intuition and catch data problems *before* modelling, not after.

</div>
</details>

<details name="stage" class="card card-success card-glass stage-card">
<summary>
<span class="stage-title"><strong>🧪 Analyse</strong> · Modeling</span>
<span class="stage-sub">statistical tests & ML</span>
</summary>
<div class="stage-ex">

Match the model to the question (descriptive / predictive / causal). Start simple; add complexity only when it earns its keep. Cross-validate honestly.

</div>
</details>

<details name="stage" class="card card-warning card-glass stage-card">
<summary>
<span class="stage-title"><strong>✅ Analyse</strong> · Evaluation</span>
<span class="stage-sub">validation, uncertainty</span>
</summary>
<div class="stage-ex">

Quantify uncertainty (CIs, bootstraps), run sensitivity analyses, compare against a baseline. A model that can't beat a trivial baseline isn't a finding.

</div>
</details>

<details name="stage" class="card card-primary card-glass stage-card">
<summary>
<span class="stage-title"><strong>📢 Share</strong> · Communication</span>
<span class="stage-sub">narrative, visuals, decisions</span>
</summary>
<div class="stage-ex">

Lead with the decision, not the method. Visuals carry the argument; technical detail goes in the appendix. Audience first, rigour always.

</div>
</details>

<details name="stage" class="card card-secondary card-glass stage-card">
<summary>
<span class="stage-title"><strong>⚙️ Share</strong> · Operationalisation</span>
<span class="stage-sub">notebooks, scripts, pipelines</span>
</summary>
<div class="stage-ex">

Turn a one-off into something reproducible: versioned code, pinned environments, scheduled pipelines. Future you must be able to re-run it.

</div>
</details>

<details name="stage" class="card card-accent card-glass stage-card">
<summary>
<span class="stage-title"><strong>📡 Share</strong> · Monitoring</span>
<span class="stage-sub">drift, quality, impact</span>
</summary>
<div class="stage-ex">

Data and the world change. Watch for input drift, model decay, and whether the decisions the analysis informs actually produce the expected impact.

</div>
</details>

</div>

<style scoped>
.stage-grid {
  align-items: start;
  grid-auto-rows: min-content;
}
.stage-grid .stage-card.card {
  padding: 0.45rem 0.8rem !important;
  font-size: 0.85em;
  line-height: 1.3;
  cursor: pointer;
  user-select: none;
  transition: box-shadow 0.25s ease, transform 0.25s ease, background-color 0.25s ease;
}
.stage-grid .stage-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0,0,0,0.3);
  filter: brightness(1.08);
}
.stage-grid .stage-card > summary {
  list-style: none;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.stage-grid .stage-card > summary::-webkit-details-marker { display: none; }
.stage-grid .stage-card > summary::after {
  content: "▸";
  font-size: 0.85em;
  opacity: 0.7;
  flex: 0 0 auto;
  transition: transform 0.25s ease;
  align-self: center;
}
.stage-grid .stage-card[open] > summary::after {
  transform: rotate(90deg);
  opacity: 1;
}
.stage-grid .stage-card[open] {
  box-shadow: 0 0 0 2px rgba(255,255,255,0.55), 0 8px 24px rgba(0,0,0,0.35);
  transform: translateY(-2px);
  z-index: 2;
}
.stage-grid .stage-title {
  display: inline;
  flex: 1 1 auto;
}
.stage-grid .stage-sub {
  display: block;
  flex: 1 0 100%;
  font-size: 0.88em;
  opacity: 0.7;
  margin-top: 0.1rem;
}
.stage-grid .stage-ex {
  font-size: 0.92em;
  line-height: 1.35;
  margin-top: 0.35rem;
  padding-top: 0.35rem;
  border-top: 1px solid rgba(255,255,255,0.15);
}
</style>

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

# Where each phase tends to **break**

<span class="def-sub">Every phase has a signature failure mode. Name them now, before we zoom into the analytical steps — that way, each later concept slots into the phase it protects.</span>

<div class="grid-3 gap-md mt-md tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 📋 **Plan**

**Risk:** wrong question. Fluent answer to a question no one asked. *Symptom:* no clear decision downstream.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📥 **Acquire**

**Risk:** sampling & selection bias. *Symptom:* the sample silently excludes the people your conclusion is about.

</div>

<div class="card card-accent card-glass pad-compact">

## 🗄️ **Store**

**Risk:** silent schema drift. *Symptom:* a column changes meaning mid-pipeline and no one notices for months.

</div>

<div class="card card-info card-glass pad-compact">

## 🛠️ **Process**

**Risk:** data leakage. *Symptom:* information from the test set sneaks into training via scaling, joins, or time-travel bugs.

</div>

<div class="card card-warning card-glass pad-compact">

## 📊 **Analyse**

**Risks:** overfitting & p-hacking. *Symptoms:* perfect training accuracy; the "significant" finding vanishes on replication.

</div>

<div class="card card-success card-glass pad-compact">

## 📢 **Share**

**Risk:** misinterpretation. *Symptom:* a confidence interval becomes a headline number; caveats disappear downstream.

</div>

</div>

---
layout: section
hideInToc: true
---

# Steps of Data **Analysis**

<!--
Speaker: transition — we've built the mental model; now zoom into the analytical
loop itself. Six concrete steps: Define, Collect, Clean, Analyse, Visualise,
Interpret. "Define" is where most analyses are won or lost. (~1 min)
-->

---
hideInToc: true
---

# The Six-Step Loop at a Glance

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#0f1f3d', 'primaryBorderColor': '#60a5fa', 'primaryTextColor': '#e2e8f0', 'secondaryColor': '#102b4c', 'lineColor': '#5eead4', 'fontFamily': 'Inter, system-ui, sans-serif'}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 35, 'rankSpacing': 40}}}%%
flowchart LR
    Def["1 Define"]:::input --> Col["2 Collect"]:::process
    Col --> Cln["3 Clean"]:::process
    Cln --> Ana["4 Analyse"]:::process
    Ana --> Vis["5 Visualise"]:::output
    Vis --> Int["6 Interpret"]:::output
    Int -.dead end?.-> Def

    classDef input fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef process fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef output fill:#155e75,stroke:#5eead4,stroke-width:2.5px,color:#e0f2fe,rx:14px,ry:14px
```

<div class="card card-accent card-glass pad-tight mt-md">

**Not a line — a loop.** A dead end at any step sends you back to **Define**, not forward. The six steps in detail follow.

</div>

---
hideInToc: true
---

# 1. **Define** — turn a goal into an answerable question

<span class="def-sub">Now we zoom into the **Analyse** phase from the lifecycle above and break the analytical work itself — the loop that turns a raw dataset into an answered question — into six concrete steps. (Note: *Analyse* names both a lifecycle phase above and one of these six steps.)</span>

<div class="stack-tight dd-stack mt-md">

<details name="s1" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🎯 Name the <strong>decision</strong> the analysis must support</span></summary>
<div class="dd-body">

Who will act on the result, on what timeline, and what changes if the answer flips? An analysis with no downstream decision is a hobby, not work.

</div>
</details>

<details name="s1" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">📐 Make it <strong>SMART</strong> — specific, measurable, achievable, relevant, time-bound</span></summary>
<div class="dd-body">

"Is it getting better?" → "Did mean API latency drop by ≥ 10% in Q1 vs Q4, for EU users?" A good question names the metric, the population, and the comparison.

</div>
</details>

<details name="s1" class="dd-card card card-info card-glass">
<summary><span class="dd-title">🧪 Pre-commit to a success threshold, null hypothesis, stopping rule</span></summary>
<div class="dd-body">

Decide what "success" means *before* you see the data. Otherwise the threshold quietly slides to wherever the result happens to land — and you've written fiction.

</div>
</details>

<details name="s1" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">⚠️ Feasibility check — can data that exists (or could exist) actually answer this?</span></summary>
<div class="dd-body">

The most expensive mistake is solving the wrong problem faster. If the data to answer the question doesn't exist and can't be collected, reframe the question before writing a line of code.

</div>
</details>

</div>

---
hideInToc: true
---

# 2. **Collect** — sourcing, not just downloading

<div class="grid-2 gap-md dd-stack mt-md">

<details name="s2" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🧭 Primary vs secondary · observational vs experimental</span></summary>
<div class="dd-body">

Experimental data (you control the treatment) lets you claim *causation*. Observational data can usually only support *association*. Know which you have before you write the conclusion.

</div>
</details>

<details name="s2" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">🎲 Sampling strategy defines what you can generalise to</span></summary>
<div class="dd-body">

Random, stratified, cluster, convenience — each yields a different inference scope. A convenience sample of engineers doesn't tell you about all users, no matter how large.

</div>
</details>

<details name="s2" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">📜 Provenance — who produced it, when, how, under what licence</span></summary>
<div class="dd-body">

A dataset without lineage is a liability, not an asset. Record source, retrieval date, version, licence, and any pre-processing done upstream before it reaches you.

</div>
</details>

<details name="s2" class="dd-card card card-info card-glass">
<summary><span class="dd-title">✅ Validate at ingestion — schema, ranges, freshness, row counts</span></summary>
<div class="dd-body">

Catch breakage at the door, not three notebooks deep. A short contract (expected columns, dtypes, min/max, row-count bounds) that fails loudly saves hours of detective work later.

</div>
</details>

<details name="s2" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">⚠️ Selection & survivorship bias enter <strong>here</strong></span></summary>
<div class="dd-body">

No cleaning step downstream can undo a biased sample. If the data-generating process systematically omits cases, your model inherits that blind spot — often invisibly.

</div>
</details>

</div>

---
hideInToc: true
---

# 3. **Clean** — often the biggest time sink

<div class="grid-2 gap-md dd-stack mt-md">

<details name="s3" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🔧 Structural fixes — types, units, encodings, duplicates, timezones</span></summary>
<div class="dd-body">

Silent coercions are the enemy: `"NA"` parsed as a string, floats truncated to ints, timestamps silently shifted by a timezone. Assert your assumptions; don't trust the reader.

</div>
</details>

<details name="s3" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">❓ Missing values — MCAR / MAR / MNAR → drop, impute, or flag</span></summary>
<div class="dd-body">

The *mechanism* dictates the treatment. Missing at random → imputation is usually fine. Missing because of the value itself (MNAR) → imputation can bias results; often better to flag and model explicitly.

</div>
</details>

<details name="s3" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">🎯 Outliers — error or signal?</span></summary>
<div class="dd-body">

Never auto-delete. An outlier might be the most informative row in the table (a fraud case, a rare event, a sensor miscalibration). Investigate, then decide — and document the decision.

</div>
</details>

<details name="s3" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">🔗 Joins — check key quality, cardinality, and orphan rows</span></summary>
<div class="dd-body">

A silent many-to-many join can inflate counts by 10×. Always verify expected cardinality (1:1, 1:N, N:1) and count orphans on both sides before and after joining.

</div>
</details>

<details name="s3" class="dd-card card card-success card-glass">
<summary><span class="dd-title">📝 Record every transformation — script it, don't click it</span></summary>
<div class="dd-body">

If a cleaning step only lives in your head (or in Excel history), it isn't reproducible. A versioned script is the only artefact that lets future-you — or anyone else — rerun the analysis.

</div>
</details>

</div>

---
hideInToc: true
---

# 4. **Analyse** — start simple, earn complexity

<div class="grid-2 gap-md dd-stack mt-md">

<details name="s4" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🔍 Exploratory Data Analysis (EDA) first — distributions, pairwise relationships, drift over time</span></summary>
<div class="dd-body">

Before any model: look. **Exploratory Data Analysis (EDA)** means profiling the data with summary stats and plots to build intuition and spot problems. Most "surprising" model results are data problems in disguise — a leaking feature, a timezone bug, a duplicated cohort. EDA catches these before they embarrass you. (Choosing and reading those plots is the focus of the Data Visualisation lecture; here the point is simply to look before you model.)

</div>
</details>

<details name="s4" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">🎯 Match the method to the question</span></summary>
<div class="dd-body">

Descriptive, inferential, predictive, and causal questions each need different tools. A hypothesis test is not a forecast; a random-forest accuracy is not a causal effect. Pick the right family first.

</div>
</details>

<details name="s4" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">📊 Always fit a <strong>baseline</strong> before anything clever</span></summary>
<div class="dd-body">

Mean, last-value, logistic regression. If a deep model can't beat a trivial baseline by a meaningful margin, it's not ready to ship — and the gap itself tells you where the signal actually lives.

</div>
</details>

<details name="s4" class="dd-card card card-info card-glass">
<summary><span class="dd-title">📐 Quantify uncertainty — CIs, bootstraps, sensitivity runs</span></summary>
<div class="dd-body">

A point estimate without a range is half an answer. Report intervals, re-run under plausible perturbations of assumptions, and tell the reader how stable the conclusion is.

</div>
</details>

<details name="s4" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">⚠️ Watch for leakage, p-hacking, overfitting</span></summary>
<div class="dd-body">

Leakage: future information sneaking into training. P-hacking: testing until something is "significant". Overfitting: memorising the training set. Hold-out sets, cross-validation, and pre-registered analyses are your defence.

</div>
</details>

</div>

---
hideInToc: true
---

# 5. **Visualise** — design for the decision, not the data

<span class="def-sub">Chart design is the focus of the Data Visualisation lecture; the principle here is to choose the chart *after* you know your audience and message.</span>

<div class="stack-tight dd-stack mt-md">

<details name="s5" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">👥 Audience → 💬 Message → 🎨 Encoding (in that order)</span></summary>
<div class="dd-body">

Pick the chart last; it's a consequence of the first two choices. A chart built around "what does pandas plot by default?" is almost never the right one.

</div>
</details>

<details name="s5" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">1️⃣ One chart, one idea — annotate the takeaway on the figure</span></summary>
<div class="dd-body">

If the reader needs the caption to understand the point, redesign. Title as takeaway ("Latency dropped 14% after the rollout"), caption as why and how.

</div>
</details>

<details name="s5" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">✂️ Remove everything that doesn't support the message</span></summary>
<div class="dd-body">

Truncated axes, rainbow palettes, 3D effects, excess gridlines, redundant legends — default to less. Honest design is usually minimal design.

</div>
</details>

<details name="s5" class="dd-card card card-info card-glass">
<summary><span class="dd-title">♿ Accessibility — colour-safe, readable at projector resolution</span></summary>
<div class="dd-body">

Test in greyscale; test from the back row. Use colour-blind-safe palettes (viridis, Okabe-Ito), 14pt+ axis labels, and never rely on colour alone to encode meaning.

</div>
</details>

</div>


---
hideInToc: true
---

# 6. **Interpret & Report** — land the decision

<div class="grid-2 gap-md dd-stack mt-md">

<details name="s6" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🎯 Conclude honestly — no more than the data supports</span></summary>
<div class="dd-body">

State the finding, the effect size, and the uncertainty. Resist the temptation to round a nuanced result into a bold headline; overclaiming is how trust dies.

</div>
</details>

<details name="s6" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">🔗 Tie to decisions — findings → actions → risks</span></summary>
<div class="dd-body">

Every finding should end with "…therefore we should". Name the action, who owns it, and what could go wrong if the analysis is partially right or fully wrong.

</div>
</details>

<details name="s6" class="dd-card card card-info card-glass">
<summary><span class="dd-title">❓ Name the limitations — prominently, not buried</span></summary>
<div class="dd-body">

Sample scope, missing confounders (unmeasured variables that influence both the predictor and the outcome), assumptions that could fail. Put them where the reader will see them; a caveat in the appendix doesn't count.

</div>
</details>

<details name="s6" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">📏 Plan measurement — how will we know we were right?</span></summary>
<div class="dd-body">

Define the follow-up metric and cadence *before* the decision is made. "We'll review the launch impact on DAU at T+30 days against this baseline" — not "we'll see how it goes".

</div>
</details>

<details name="s6" class="dd-card card card-success card-glass">
<summary><span class="dd-title">📦 Package for reuse — others must be able to rerun tomorrow</span></summary>
<div class="dd-body">

Versioned code, pinned environment, seeded randomness, a README naming inputs and outputs. Reproducibility is the minimum bar; reuse is the bonus.

</div>
</details>

</div>

---
hideInToc: true
---

# Communication artefacts — pick the right one

<div class="grid-2 gap-md dd-stack mt-md">

<details name="artefact" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">📄 Executive summary</span></summary>
<div class="dd-body">

One page for busy stakeholders: the question, the answer, the confidence, the recommended action. No methods, no caveats-by-weight — just the decision they need to make.

</div>
</details>

<details name="artefact" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">📋 Decision memo</span></summary>
<div class="dd-body">

Options considered, trade-offs, recommendation. Written for a reader who must *choose*, not just be informed. Structure: context → options → recommendation → risks.

</div>
</details>

<details name="artefact" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">📊 Dashboard</span></summary>
<div class="dd-body">

For ongoing monitoring and self-service. Works when the question repeats and the metric is stable. Bad fit for one-off decisions — a dashboard built for a single question becomes stale on day two.

</div>
</details>

<details name="artefact" class="dd-card card card-info card-glass">
<summary><span class="dd-title">📓 Reproducible notebook</span></summary>
<div class="dd-body">

End-to-end analysis for peers who will read, re-run, and critique the work. Narrative + code + output interleaved. The right artefact when the *how* matters as much as the *what*.

</div>
</details>

<details name="artefact" class="dd-card card card-success card-glass">
<summary><span class="dd-title">🔬 Technical appendix</span></summary>
<div class="dd-body">

Methods, assumptions, derivations, audit trail. Attached to a summary or memo, read by the few who need to verify. It's where nuance lives without cluttering the headline.

</div>
</details>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

<div class="note-text">

#### 💡 Match the artefact to the **audience** and the **decision horizon** — not to what's easiest to produce

</div>

</div>

---
hideInToc: true
---

# Flavours × Steps · **which step produces which insight**

<span class="def-sub">The four analytics flavours aren't independent paths — they are what the same six-step loop *yields* when the Define step points at a different kind of decision.</span>

<div class="grid-2 gap-md mt-md tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 📊 **Descriptive** — "what happened?"

The work lives in **Explore** (summary stats, plots) and **Communicate** (dashboards). Modelling is minimal. *Output:* a faithful rear-view mirror.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Diagnostic** — "why did it happen?"

Most of the effort goes into **Explore** (segmentation, cohort comparison) and **Model** (regression on drivers). *Output:* named contributors to the outcome.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔮 **Predictive** — "what happens next?"

Quality hinges on **Collect** (the right features, honest splits) and **Model** (out-of-sample validation). *Output:* a forecast with an uncertainty band — never a single number.

</div>

<div class="card card-warning card-glass pad-compact">

## 🎛️ **Prescriptive / causal** — "what should we do?"

The decisive steps are **Define** (intervention + counterfactual) and **Model** (causal identification). *Output:* an action with an expected effect size.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 💡 **The takeaway**

Same six steps, four different centres of gravity. "What kind of analysis is this?" is really asking "**which step is doing the work?**"

</div>

---
layout: section
hideInToc: true
---

# Tools & **Collaboration**

<!--
Speaker: pivot from the how-to to the ecosystem — the stack, the roles, the
rituals. Emphasise tool-agnosticism: the concepts outlive any single tool, and
no single role sees the whole pipeline. (~1 min)
-->

---
hideInToc: true
---

# Modern analytics stack

<div class="stack-loop mt-md">

<div class="pipe-step card card-primary card-glass">
<div class="pipe-head">📡 <strong>1. Sources</strong></div>
<div class="pipe-sub">where the raw data originates</div>
<ul class="pipe-list">
<li>sensors & instruments</li>
<li>web / app APIs</li>
<li>operational databases</li>
<li>files & uploads</li>
<li>experiments, surveys</li>
</ul>
</div>

<div class="pipe-step card card-secondary card-glass">
<div class="pipe-head">📥 <strong>2. Ingestion</strong></div>
<div class="pipe-sub">move, schedule, validate</div>
<ul class="pipe-list">
<li>ETL / ELT pipelines</li>
<li>streaming (Kafka, Kinesis)</li>
<li>batch schedulers (Airflow)</li>
<li>schema & freshness checks</li>
</ul>
</div>

<div class="pipe-step card card-accent card-glass">
<div class="pipe-head">💾 <strong>3. Storage</strong></div>
<div class="pipe-sub">durable, queryable, governed</div>
<ul class="pipe-list">
<li>data lakes (S3, GCS)</li>
<li>warehouses (BigQuery, Snowflake)</li>
<li>feature stores</li>
<li>lineage & access control</li>
</ul>
</div>

<div class="pipe-step card card-info card-glass">
<div class="pipe-head">💻 <strong>4. Compute</strong></div>
<div class="pipe-sub">where analysis actually runs</div>
<ul class="pipe-list">
<li>notebooks & scripts</li>
<li>SQL engines</li>
<li>distributed clusters (Spark)</li>
<li>cloud / HPC jobs</li>
</ul>
</div>

<div class="pipe-step card card-success card-glass">
<div class="pipe-head">📢 <strong>5. Delivery</strong></div>
<div class="pipe-sub">results in decision-makers' hands</div>
<ul class="pipe-list">
<li>dashboards (Grafana, Superset)</li>
<li>reports & memos</li>
<li>APIs & embedded models</li>
<li>alerts & notifications</li>
</ul>
</div>

</div>

<style scoped>
.stack-loop {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.7rem;
  margin-top: 1rem;
}
.stack-loop .pipe-step {
  padding: 0.7rem 0.9rem !important;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  min-height: 8rem;
}
.stack-loop .pipe-head {
  font-size: 1.05em;
  line-height: 1.2;
  text-align: center;
}
.stack-loop .pipe-sub {
  font-size: 0.78em;
  opacity: 0.75;
  line-height: 1.3;
  text-align: center;
  font-style: italic;
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding-bottom: 0.4rem;
}
.stack-loop .pipe-list {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.82em;
  line-height: 1.45;
  opacity: 0.92;
}
.stack-loop .pipe-list li { margin: 0.12rem 0; }
.loop-back {
  text-align: center;
  margin-top: 0.9rem;
  font-size: 0.88em;
  opacity: 0.75;
  letter-spacing: 0.02em;
}
.loop-back em { font-style: italic; }
</style>

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

<!--
Speaker: this is where reproducibility becomes a habit, not a slogan. Hygiene =
future-you can re-run it; ethics = you can be trusted with the data. Land the
rule of thumb: re-runnable in under an hour, six months later. (~1 min)
-->

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

# Hygiene & reproducibility habits

<div class="grid-2 gap-md dd-stack mt-md">

<details name="hygiene" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🔄 Source-control everything</span></summary>
<div class="dd-body">

Code, SQL, data definitions, transformations, configs — all in git. If it drives a result, it lives under version control; otherwise silent edits quietly invalidate past analyses.

</div>
</details>

<details name="hygiene" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">📁 Clear structure & naming conventions</span></summary>
<div class="dd-body">

`raw/`, `interim/`, `processed/`, `reports/`; dated, snake_case filenames; one project per repo. Conventions beat creativity — future-you wants predictability, not cleverness.

</div>
</details>

<details name="hygiene" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">🧹 Housekeeping as you go</span></summary>
<div class="dd-body">

Archive dead branches, deprecate unused scripts, update READMEs in the same PR as the change. Debt compounds; a five-minute cleanup today saves an hour of confusion next quarter.

</div>
</details>

<details name="hygiene" class="dd-card card card-info card-glass">
<summary><span class="dd-title">📦 Record the environment</span></summary>
<div class="dd-body">

`env.yaml`, `requirements.txt` with pinned versions, lockfiles, or a container. "Works on my machine" is not reproducible — the exact library versions are part of the result.

</div>
</details>

<details name="hygiene" class="dd-card card card-success card-glass">
<summary><span class="dd-title">🎲 Seeds, hashes, snapshots</span></summary>
<div class="dd-body">

Fix the random seed, hash input files, snapshot the dataset version. Same inputs + same code → same results — not "almost the same results with a different train/test split".

</div>
</details>

<details name="hygiene" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">⚙️ Automate the critical path</span></summary>
<div class="dd-body">

A `Makefile`, `make.py`, or CI job that rebuilds the whole analysis with one command. If the steps live only in your memory and terminal history, they'll break silently the first time anyone else tries.

</div>
</details>

</div>

<div class="card card-info card-glass pad-compact mt-md">

<div class="note-text">

#### 🎯 Rule of thumb — if you cannot re-run an analysis six months later in under an hour, it isn't finished

</div>

</div>

---
hideInToc: true
---

# Ethics, governance & accountability

<div class="grid-2 gap-md dd-stack mt-md">

<details name="ethics" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🛡️ Minimise harm — privacy, consent, security by design</span></summary>
<div class="dd-body">

Collect the minimum you need, anonymise where possible, encrypt at rest and in transit. Ask "could this dataset hurt someone if it leaked?" — if yes, treat it accordingly from day one.

</div>
</details>

<details name="ethics" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">⚖️ Fairness — monitor for disparate impact across groups</span></summary>
<div class="dd-body">

A model can be accurate overall and still systematically wrong for a subgroup. Slice key metrics by demographic, geography, or cohort and watch the gaps, not just the averages.

</div>
</details>

<details name="ethics" class="dd-card card card-accent card-glass">
<summary><span class="dd-title">🔍 Transparency — methods, assumptions, limitations visible</span></summary>
<div class="dd-body">

Publish what you did, what you assumed, and what you don't know. A result that can't be inspected can't be trusted — and won't be, once it matters.

</div>
</details>

<details name="ethics" class="dd-card card card-success card-glass">
<summary><span class="dd-title">🌍 Sustainability — compute and environmental cost</span></summary>
<div class="dd-body">

Large models and always-on pipelines carry real energy and carbon costs. Scale effort to the question: a 10-hour GPU run to answer something a SQL query could solve is a design failure, not a feature.

</div>
</details>

<details name="ethics" class="dd-card card card-info card-glass">
<summary><span class="dd-title">👤 Accountability — named owners, escalation paths</span></summary>
<div class="dd-body">

Every dataset, model, and dashboard should have a human owner. Anonymous artefacts rot: no one notices when they break, and no one is responsible when they mislead.

</div>
</details>

<details name="ethics" class="dd-card card card-warning card-glass">
<summary><span class="dd-title">📜 Compliance frameworks — know which apply</span></summary>
<div class="dd-body">

GDPR (EU personal data), HIPAA (US health), CERN data-classification policies, institutional ethics approvals. Don't discover the rule after you've broken it — check at project kickoff.

</div>
</details>

<details name="ethics" class="dd-card card card-primary card-glass">
<summary><span class="dd-title">🚨 Incident response — breaches and quality failures</span></summary>
<div class="dd-body">

Have a written plan: who is notified, how results are withdrawn or corrected, how affected users are informed. Designing this in calm is vastly easier than improvising in crisis.

</div>
</details>

<details name="ethics" class="dd-card card card-secondary card-glass">
<summary><span class="dd-title">📚 Training & audits — keep practices aligned over time</span></summary>
<div class="dd-body">

Periodic reviews of access, models in production, and privacy controls. Good practices decay silently; regular audits surface drift before it becomes a headline.

</div>
</details>

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

<span class="def-sub">Open, reusable data is a principle until someone actually ships a dataset under it. CERN's Open Data portal is that proof: a petabyte-scale demonstration that every concept in this lecture works at real-world scale.</span>

<div class="card card-primary card-glass pad-tight mt-md">

- 🌐 CERN releases proton-proton collision datasets via the Open Data portal
- 🎯 Goal: enable students & researchers to reproduce landmark analyses
- 📁 Data formats: ROOT files, CSV summaries, metadata packages
- 🔧 Tooling: ROOT, Python, R, Jupyter, cloud notebooks

</div>

---
hideInToc: true
---

# Collaboration model

<div class="card card-secondary card-glass pad-tight mt-md">

- 👥 Physicists, statisticians, software engineers, detector experts
- 🔄 Shared code repositories with rigorous review (ROOT macros, Python)
- 🧪 Simulation teams provide synthetic data for validation
- 📄 Publication committees ensure rigour & messaging

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

<div class="note-text">Blind analyses (analysing without looking at the signal region, to avoid biasing the result) & control regions</div>

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

Pick the simplest method that solves the problem. Reach for complexity only when the simple thing has clearly failed.

</div>

<div class="card card-success card-glass pad-tight">

## 📢 **Communicate**

Results that nobody understands have zero impact. Visualisation and storytelling are part of analysis.

</div>

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Frame an analysis around the **decision** it serves

</div>

<div class="card card-success card-glass pad-compact">

✅ Classify work as **descriptive, diagnostic, predictive, or prescriptive**

</div>

<div class="card card-success card-glass pad-compact">

✅ Run a **data-quality checklist** and read missing-data mechanisms

</div>

<div class="card card-success card-glass pad-compact">

✅ Hand results to the next analyst — documented and reproducible

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 9 tie-in**

run a data-quality audit on your dataset — find missing, duplicate, and physically impossible values before analysing.

</div>

<!--
Speaker: the "you can now" beat — have them nod to each capability. The seminar
tie-in makes it concrete: next session they audit their own dataset for missing,
duplicate, and impossible values before touching analysis. (~1 min)
-->

---
hideInToc: true
---

# Further **Reading**

<div class="card card-info card-glass pad-compact mt-sm">

📚 This lecture draws on these — several are free online:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">📗 **Wilson et al.** — *Good Enough Practices in Scientific Computing* (2017) · free</div>

<div class="card card-secondary card-glass pad-compact">🔗 **Wilkinson et al.** — *The FAIR Guiding Principles* (2016), *Scientific Data* · GO FAIR</div>

<div class="card card-accent card-glass pad-compact">🔄 **CRISP-DM** — the cross-industry standard process for data mining</div>

<div class="card card-info card-glass pad-compact">📘 **Kelleher & Tierney** — *Data Science* (MIT Press, Essential Knowledge)</div>

</div>

---
hideInToc: true
---

# Takeaways

<div class="card card-info card-glass pad-compact mt-sm">

<div class="note-text">

Remember the lab thermometer — a single reading (`22.3 °C`) travelled all the way to an operational decision (shift Friday calibration). That journey is what this lecture is really about.

</div>

</div>

<div class="grid-3 gap-md mt-md tidy-cards">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Decisions first**

The reading mattered because someone had to act on it — define metrics and success criteria early

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **Quality & uncertainty**

No value is trustworthy without its error bar — treat both as first-class, not footnotes

</div>

<div class="card card-accent card-glass pad-compact">

## 🔄 **Lifecycle, not event**

Plan → Acquire → Store → Process → Analyse → Share, with governance on every step

</div>

<div class="card card-info card-glass pad-compact">

## ♻️ **Reproducible & reusable**

Documented and versioned so the next analyst can pick up where you stopped — formalised as **FAIR** in Lecture 14

</div>

<div class="card card-success card-glass pad-compact">

## 📢 **Story over numbers**

Inspect → clean → transform → model → communicate: Wikipedia's definition, lived end-to-end

</div>

<div class="card card-warning card-glass pad-compact">

## ⚖️ **Responsible by default**

Hygiene, ethics, accountability — the price of being trusted with data

</div>

</div>
