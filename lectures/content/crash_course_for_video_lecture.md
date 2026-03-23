---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade
hideInToc: true

addons:
  - slidev-addon-python-runner
mermaid: true

---

# Dr. Mindaugas Šarpis
# Data Analysis and Artificial Intelligence

## From CERN to Your Data

---
hideInToc: true
layout: quote
---

# Not only is the Universe stranger than we think, it is stranger than we **can** think.
Werner Heisenberg

---
layout: section
hideInToc: true
---

# Our place in the Universe

---
hideInToc: true
---

<VideoPlayer src="VU_VM_Zoom.mp4" autoplay />

---
hideInToc: true
---

<VideoPlayer src="Voyage_in_to_the_world_of_atoms.mp4" autoplay />

---
layout: section
hideInToc: true
---

# Exploring the **Fundamental**

---
hideInToc: true
---

# What is CERN?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🏛️ **The Organisation**

- **European Organization for Nuclear Research**
- Founded in **1954** by 12 European states
- Today: **24 member states**, thousands of visiting scientists
- Located at the **French-Swiss border** near Geneva

</div>

<div class="card card-secondary pad-tight">

## 🎯 **The Mission**

- Probe the **fundamental structure** of matter
- Build and operate the world's most powerful **particle accelerators**
- Push the boundaries of **technology and engineering**
- Train the **next generation** of scientists

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## 🌍 **By the Numbers**

🔬 World's **largest** particle physics laboratory · 👩‍🔬 **17,000+** scientists from **110+ nations** · 🧪 Home to the **Large Hadron Collider**

</div>

---
hideInToc: true
---

# The Large Hadron Collider (LHC)

<div class="card card-info pad-tight">

## ⚙️ **The Machine**

<v-clicks>

- A **27 km** circumference ring situated **100 m** underground
- Accelerates protons to **99.9999991%** the speed of light
- Collides particles **~1 billion times per second**
- Operating temperature: **1.9 K** (~ -271.1°C) — colder than outer space

</v-clicks>

</div>

<div class="card card-warning pad-compact mt-md" v-click>

## 🏆 **Key Achievement**

Discovery of the **Higgs boson** in **2012** — confirmed the mechanism that gives particles their mass (Nobel Prize in Physics 2013)

</div>

---
layout: section
hideInToc: true
---

# Inside the **Machine**

---
hideInToc: true
---

<VideoPlayer src="CERN_Overview_Short.mp4" autoplay />

---
hideInToc: true
---

<VideoPlayer src="ATLAS-FOOTAGE-2022-004-002-1080p_Shaft.mp4" autoplay />

---
hideInToc: true
---

<VideoPlayer src="QGP_Formation.mp4" autoplay />

---
hideInToc: true
---

# From Collisions to Discovery

```mermaid {scale: 1.0}
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 40, 'rankSpacing': 45}}}%%
flowchart LR
  C["🔬 Collisions<br/>1 billion/sec"] --> T["⚡ Trigger<br/>Filter 99.999%"]
  T --> R["🔧 Reconstruct<br/>Build events"]
  R --> A["📊 Analyse<br/>Statistical tests"]
  A --> D{"🎯 5σ?"}
  D -->|Yes| P["📢 Publish"]
  D -->|No| M["🔄 More data"]
  M --> C

  classDef stage fill:#0b2236,stroke:#60a5fa,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
  classDef decision fill:#0b2540,stroke:#fcd34d,stroke-width:2px,color:#fef3c7,rx:14px,ry:14px;
  classDef output fill:#063c34,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
  classDef loop fill:#3b1f09,stroke:#f59e0b,stroke-width:2px,color:#ffe7c7,rx:12px,ry:12px;
  class C,T,R,A stage;
  class D decision;
  class P output;
  class M loop;
```

<div class="card card-info pad-compact mt-md" v-click>

💡 No neural networks were needed to discover the Higgs. **Careful experimental design, statistics, and reproducible analysis** — the same skills you can learn.

</div>

---
hideInToc: true
---

# Why Data Analysis Matters at CERN

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📊 **The Data Challenge**

- LHC produces **~1 PB of data per second** of raw detector output
- Only **~1 in a billion** collisions contains interesting physics
- Must filter, reconstruct, and analyse in near real-time

</div>

<div class="card card-secondary pad-tight">

## 🔍 **Needle in a Haystack**

- Signal events look almost identical to background noise
- Statistical methods decide if a discovery is **real or a fluctuation**
- The 5-sigma standard: less than **1 in 3.5 million** chance of being wrong

</div>

</div>

<div class="card card-accent pad-compact mt-md" v-click>

💡 Finding the Higgs required sifting through **trillions** of events. Not with AI. With **rigorous data analysis.**

</div>

---
layout: section
hideInToc: true
---

# What is **Data Analysis?**

---
hideInToc: true
---

# Data → Information → Knowledge → Wisdom

<div class="stack-tight mt-sm">

<div
  class="card card-primary pad-tight"
  v-motion
  :initial="{ opacity: 0, x: -60 }"
  :enter="{ opacity: 1, x: 0, transition: { delay: 200 } }"
>

## 📋 **Data**
Capture observations — numbers, text, images, signals

</div>

<div
  class="card card-secondary pad-tight"
  v-motion
  :initial="{ opacity: 0, x: -60 }"
  :enter="{ opacity: 1, x: 0, transition: { delay: 500 } }"
>

## 💡 **Information**
Emerges when data gain context, structure, and purpose

</div>

<div
  class="card card-accent pad-tight"
  v-motion
  :initial="{ opacity: 0, x: -60 }"
  :enter="{ opacity: 1, x: 0, transition: { delay: 800 } }"
>

## 🧠 **Knowledge**
Blends information with experience and domain expertise

</div>

<div
  class="card card-success pad-tight"
  v-motion
  :initial="{ opacity: 0, x: -60 }"
  :enter="{ opacity: 1, x: 0, transition: { delay: 1100 } }"
>

## 🎯 **Wisdom**
The responsibility to act on knowledge with judgement

</div>

</div>

---
hideInToc: true
---

# A Concrete Example

<div class="grid-2 gap-md mt-md">

<div class="card card-info pad-tight" v-click>

## 📋 **Raw Data**

### `2025-10-24, 22.3°C`

</div>

<div class="card card-primary pad-tight" v-click>

## 💡 **Information**

### `Lab A was 22.3°C at 10:24 on Oct 24, 2025.`

</div>

<div class="card card-accent pad-tight" v-click>

## 🧠 **Knowledge**

### `Lab A runs 1.5°C hotter on Fridays due to load.`

</div>

<div class="card card-success pad-tight" v-click>

## 🎯 **Wisdom**

### `Shift calibration earlier on Fridays to reduce drift.`

</div>

</div>

---
hideInToc: true
---

# The Same Process, Everywhere

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-compact" v-click>

## ⚛️ **Particle Physics**

Detector signals → event reconstruction → statistical tests → discovery

</div>

<div class="card card-secondary pad-compact" v-click>

## 💼 **Business**

Customer clicks → behaviour patterns → predictive models → decisions

</div>

<div class="card card-accent pad-compact" v-click>

## 🏥 **Medicine**

Patient records → clinical patterns → diagnostic models → treatment plans

</div>

</div>

<div class="card card-info pad-tight mt-md" v-click>

## 🔑 **Key Insight**

The **methods** are universal. The **domain** changes, the **thinking** doesn't.
Collect → Clean → Explore → Model → Decide → Communicate

</div>

---
hideInToc: true
---

# Four Flavours of Analytics

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight" v-click>

## 📋 **Descriptive** — What happened?

<div class="note-text">Event rate rose 12% last run · Sales dropped 8% in Q3</div>

</div>

<div class="card card-secondary pad-tight" v-click>

## 🔍 **Diagnostic** — Why did it happen?

<div class="note-text">Rate rose due to trigger threshold change · Drop correlates with pricing change</div>

</div>

<div class="card card-accent pad-tight" v-click>

## 🔮 **Predictive** — What is likely next?

<div class="note-text">Projected 8% rate increase next fill · Model forecasts recovery in Q1</div>

</div>

<div class="card card-success pad-tight" v-click>

## 🎯 **Prescriptive** — What should we do?

<div class="note-text">Raise threshold by 0.3 to maintain buffer · Revert price, A/B test alternatives</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Navigating the **Buzzword** Landscape

---
hideInToc: true
---

# What People Call "AI"

<div class="mt-md">

<div style="position: relative; height: 320px; margin-top: 1rem;">

<!-- The spectrum bar -->
<div style="
  position: absolute; top: 0; left: 0; right: 0; height: 50px;
  border-radius: 14px; overflow: hidden;
  display: flex;
">
  <div v-click style="flex: 2; background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light)); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.85em; border-right: 1px solid rgba(255,255,255,0.1);">
    Spreadsheets & Rules
  </div>
  <div v-click style="flex: 2; background: linear-gradient(135deg, var(--color-secondary), var(--color-secondary-light)); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.85em; border-right: 1px solid rgba(255,255,255,0.1);">
    Statistics
  </div>
  <div v-click style="flex: 2; background: linear-gradient(135deg, var(--color-accent), var(--color-accent-light)); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.85em; border-right: 1px solid rgba(255,255,255,0.1);">
    Machine Learning
  </div>
  <div v-click style="flex: 2; background: linear-gradient(135deg, var(--color-success), var(--color-success-light)); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.85em; border-right: 1px solid rgba(255,255,255,0.1);">
    Deep Learning
  </div>
  <div v-click style="flex: 2; background: linear-gradient(135deg, var(--color-warning), var(--color-warning-light)); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.85em;">
    LLMs / GenAI
  </div>
</div>

<!-- Labels below -->
<div style="position: absolute; top: 70px; left: 0; right: 0; display: flex; font-size: 0.8em; opacity: 0.7;">
  <div v-click="1" style="flex: 2; text-align: center;">IF/ELSE, pivot tables</div>
  <div v-click="2" style="flex: 2; text-align: center;">regression, hypothesis tests</div>
  <div v-click="3" style="flex: 2; text-align: center;">decision trees, clustering</div>
  <div v-click="4" style="flex: 2; text-align: center;">neural networks, CNNs</div>
  <div v-click="5" style="flex: 2; text-align: center;">ChatGPT, image generation</div>
</div>

<!-- The punchline -->
<div v-click class="card card-warning pad-tight" style="position: absolute; bottom: 0; left: 0; right: 0;">

## ⚠️ **The Marketing Label**

Most of what companies call "AI" lives in the first three boxes. Understanding **where your problem sits** on this spectrum is the real skill.

</div>

</div>

</div>

---
hideInToc: true
---

# The Real Skill Stack

<div class="grid-2 mt-md gap-md">

<div
  class="card card-primary pad-tight"
  v-motion
  :initial="{ opacity: 0, y: 40 }"
  :enter="{ opacity: 1, y: 0, transition: { delay: 200 } }"
>

## 🧠 **Think**

Ask the right question. Understand the domain. Know what "good enough" looks like.

</div>

<div
  class="card card-secondary pad-tight"
  v-motion
  :initial="{ opacity: 0, y: 40 }"
  :enter="{ opacity: 1, y: 0, transition: { delay: 500 } }"
>

## 🔍 **Explore**

Look at the data before modelling it. Distributions, outliers, missing values — they tell a story.

</div>

<div
  class="card card-accent pad-tight"
  v-motion
  :initial="{ opacity: 0, y: 40 }"
  :enter="{ opacity: 1, y: 0, transition: { delay: 800 } }"
>

## 🛠️ **Choose**

Pick the simplest method that solves the problem. A good scatter plot beats a bad neural network.

</div>

<div
  class="card card-success pad-tight"
  v-motion
  :initial="{ opacity: 0, y: 40 }"
  :enter="{ opacity: 1, y: 0, transition: { delay: 1100 } }"
>

## 📢 **Communicate**

Results that nobody understands have zero impact. Visualisation and storytelling are part of analysis.

</div>

</div>

---
hideInToc: true
---

# Quiz: Which of These is "AI"?

<MCQ
  question="A company uses a dashboard that flags when monthly sales drop below the 12-month rolling average. Is this AI?"
  :options="[
    'Yes — it automatically detects anomalies',
    'No — it is a simple statistical rule',
    'It depends on how they market it'
  ]"
  :correct="1"
  explanation="This is a straightforward threshold comparison against a moving average — a statistical rule, not machine learning. But it is effective data analysis! The label matters less than whether it solves the problem."
/>

---
hideInToc: true
---

# When "AI" is Just Good Data Analysis

<div class="grid-2 mt-md gap-md">

<div class="card card-info pad-compact" v-click>

## 📊 **"AI-Powered" Dashboard**

<div class="note-text">Reality: SQL queries + conditional formatting · Tool: Spreadsheet or BI tool</div>

</div>

<div class="card card-primary pad-compact" v-click>

## 🔔 **"Smart" Anomaly Detection**

<div class="note-text">Reality: Statistical control charts (invented 1924) · Tool: Basic statistics</div>

</div>

<div class="card card-secondary pad-compact" v-click>

## 🎯 **"Predictive" Analytics**

<div class="note-text">Reality: Linear regression on historical trends · Tool: A few lines of Python</div>

</div>

<div class="card card-accent pad-compact" v-click>

## 🤖 **Actual ML Use Case**

<div class="note-text">Reality: Image classification with millions of samples · Tool: Deep learning frameworks, GPUs</div>

</div>

</div>

<div class="card card-warning pad-compact mt-md" v-click>

💡 **3 out of 4** need data analysis skills, not AI expertise. Know the difference.

</div>

---
hideInToc: true
---

# How the Disciplines Overlap

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

## 🤖 **AI / ML**

<div class="note-text">Automates pattern recognition at scale — one tool among many</div>

</div>

</div>

</div>

<div class="card card-warning pad-compact mt-md" v-click>

🎯 **AI is a tool in the toolbox, not the toolbox itself.** Data analysis is the foundation everything else builds on.

</div>

---
hideInToc: true
---

# Common Pitfalls

<div class="stack-tight mt-md">

<div class="card card-warning pad-tight" v-click>

## ⚠️ Jumping to complex models before understanding the data

</div>

<div class="card card-warning pad-tight" v-click>

## ⚠️ Confusing correlation with causation

</div>

<div class="card card-warning pad-tight" v-click>

## ⚠️ Overfitting pretty charts to noisy data

</div>

<div class="card card-warning pad-tight" v-click>

## ⚠️ Calling everything "AI" to sound impressive

</div>

<div class="card card-warning pad-tight" v-click>

## ⚠️ Shipping insights without reproducibility

</div>

</div>

---
layout: section
hideInToc: true
---

# **Takeaways**

---
hideInToc: true
---

# What To Take Away

<div class="grid-2 gap-md mt-md">

<div
  class="card card-primary pad-tight"
  v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { delay: 200 } }"
>

## 🧠 **Data literacy > tool literacy**

Understanding your data matters more than knowing the latest framework

</div>

<div
  class="card card-secondary pad-tight"
  v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { delay: 500 } }"
>

## 🎯 **The thinking matters more than the label**

Good analysis is good analysis — whether you call it statistics, data science, or AI

</div>

<div
  class="card card-accent pad-tight"
  v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { delay: 800 } }"
>

## 🔬 **CERN-grade rigour is learnable**

The same methods that found the Higgs apply to your business, your research, your career

</div>

<div
  class="card card-success pad-tight"
  v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { delay: 1100 } }"
>

## 🚀 **These skills transfer everywhere**

From particle physics to finance, from genomics to marketing — data is the common language

</div>

</div>

---
hideInToc: true
---

# What This Course Teaches

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-compact">

## 🖥️ **Computing Foundations**

How computers actually work, command line, file management

</div>

<div class="card card-secondary pad-compact">

## 🐍 **Python Programming**

From zero to data analysis — the most in-demand language in science and industry

</div>

<div class="card card-accent pad-compact">

## 📊 **Data Analysis**

Statistics, probability, visualisation, fitting, and real-world case studies

</div>

<div class="card card-info pad-compact">

## 🔄 **Reproducibility**

Version control, workflows, and practices used at CERN and in industry

</div>

<div class="card card-success pad-compact">

## 🤖 **AI & Machine Learning**

Understand what it is, when to use it, and when not to

</div>

<div class="card card-warning pad-compact">

## 🎯 **Your Own Project**

Apply everything to a real project in your field

</div>

</div>

---
hideInToc: true
layout: quote
---

# The best thing about being a scientist is that you never stop being a **student**.

---
hideInToc: true
layout: fact
---

# Thank you.

Dr. Mindaugas Šarpis

Data Analysis and Artificial Intelligence
