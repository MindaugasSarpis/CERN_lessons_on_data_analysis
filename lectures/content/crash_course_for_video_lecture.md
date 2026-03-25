---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

addons:
  - slidev-addon-python-runner
mermaid: true

---

# Dr. Mindaugas Šarpis
# Data Analysis and Artificial Intelligence

## From breakthroughs in fundamental science to applied business and industry knowledge

---
layout: quote
---

# In God we trust, all others must bring data.
Edwards Deming

---
---

<VideoPlayer src="VU_VM_Zoom_New.mp4" autoplay />

---
---

<VideoPlayer src="Voyage_in_to_the_world_of_atoms.mp4" autoplay />

---
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight" v-click>

## 🏛️ **The Organisation**

- **European Organization for Nuclear Research**
- Founded in **1954** by 12 European states
- Today: **24 member states**, thousands of visiting scientists
- Located at the **French-Swiss border** near Geneva

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 🎯 **The Mission**

- Probe the **fundamental structure** of matter
- Build and operate the world's most powerful **particle accelerators**
- Push the boundaries of **technology and engineering**
- Train the **next generation** of scientists

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md" v-click>

## 🌍 **By the Numbers**

🔬 World's **largest** particle physics laboratory · 👩‍🔬 **17,000+** scientists from **110+ nations** · 🧪 Home to the **Large Hadron Collider**

</div>


---
---

<VideoPlayer src="CERN_Overview_Short.mp4" autoplay />

---
---

<div class="card card-info card-glass pad-tight" v-click>

## ⚙️ **The Machine**

- A **27 km** circumference ring situated **100 m** underground
- Accelerates protons to **99.9999991%** the speed of light
- Collides particles **~1 billion times per second**
- Operating temperature: **1.9 K** (~ -271.1°C) — colder than outer space

</div>

<div class="card card-warning card-glass pad-compact mt-md" v-click>

## 🏆 **Key Achievement**

Discovery of the **Higgs boson** in **2012** — confirmed the mechanism that gives particles their mass (Nobel Prize in Physics 2013)

</div>

---
---

<VideoPlayer src="ATLAS-FOOTAGE-2022-004-002-1080p_Shaft.mp4" autoplay />

---
---

<VideoPlayer src="QGP_Formation.mp4" autoplay />

---
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight" v-click>

## 📊 **The Data Challenge**

- LHC produces **~1 PB of data per second** of raw detector output
- Only **~1 in a billion** collisions contains interesting physics
- Must filter, reconstruct, and analyse in near real-time

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 🔍 **Needle in a Haystack**

- Signal events look almost identical to background noise
- Statistical methods decide if a discovery is **real or a fluctuation**
- The 5-sigma standard: less than **1 in 3.5 million** chance of being wrong

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md" v-click>

💡 Finding the Higgs required sifting through **trillions** of events. Not with AI — with **rigorous data analysis.** The same rigour applies far beyond physics.

</div>

---
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
/* Base card: compact padding, smooth transitions on everything */
.anim-card.card {
  padding: 0.4rem 0.8rem !important;
  overflow: hidden;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              padding 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Expanded state: more padding when examples are visible */
.anim-card.card:has(.anim-ex:not(.slidev-vclick-hidden)) {
  padding: 0.5rem 1rem 0.6rem !important;
}

/* Hidden card: slide in from left */
.anim-card.slidev-vclick-hidden {
  transform: translateX(-40px);
  opacity: 0 !important;
  visibility: visible !important;
  pointer-events: none;
}

/* Heading: large when collapsed, smaller when expanded */
.anim-card h2 {
  font-size: 1.3em;
  line-height: 1.2;
  margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) h2 {
  font-size: 1em;
}

/* Subtitle text */
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

/* Example rows: animated collapse */
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
.anim-ex ul {
  margin: 0;
  padding-left: 1.4em;
}
.anim-ex li {
  margin: 0.15em 0;
}
</style>

---
---

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

.flow-label {
  font-weight: 700;
  font-size: 1.15em;
  white-space: nowrap;
  min-width: 9rem;
}

.flow-text {
  font-size: 1.05em;
  opacity: 0.9;
}
.flow-text code {
  background: rgba(255, 255, 255, 0.1);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.95em;
}

.flow-arrow {
  font-size: 1.4em;
  opacity: 0.4;
  margin: 0.3rem 0;
  transition: opacity 0.5s ease;
}
.flow-arrow.slidev-vclick-hidden {
  opacity: 0 !important;
  visibility: visible !important;
}
</style>

---
---

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight" v-click>

## ⚛️ **Particle Physics**

- Detector signals
- Event reconstruction
- Statistical tests
- **Discovery**

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 💼 **Business**

- Customer clicks
- Behaviour patterns
- Predictive models
- **Decisions**

</div>

<div class="card card-accent card-glass pad-tight" v-click>

## 🏥 **Medicine**

- Patient records
- Clinical patterns
- Diagnostic models
- **Treatment plans**

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md" v-click>

## 🔑 **Key Insight**

The **methods** are universal. The **domain** changes, the **thinking** doesn't.

**Collect → Clean → Explore → Model → Decide → Communicate**

</div>

---
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
/* Card entrance: slide in from left + fade */
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

/* Heading: large when collapsed, smaller when expanded */
.anim-card h2 {
  font-size: 1.3em;
  line-height: 1.2;
  margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) h2 {
  font-size: 1em;
}

/* Subtitle */
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

/* Example rows: animated collapse */
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
.anim-ex ul {
  margin: 0;
  padding-left: 1.4em;
}
.anim-ex li {
  margin: 0.15em 0;
}

/* Card padding */
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
---

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
<div v-click class="card card-warning card-glass pad-tight" style="position: absolute; bottom: 0; left: 0; right: 0;">

## ⚠️ **The Marketing Label**

Most of what companies call "AI" lives in the first three boxes. Understanding **where your problem sits** on this spectrum is the real skill.

</div>

</div>

</div>

---
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight" v-click>

## 🧠 **Think**

Ask the right question. Understand the domain. Know what "good enough" looks like.

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 🔍 **Explore**

Look at the data before modelling it. Distributions, outliers, missing values — they tell a story.

</div>

<div class="card card-accent card-glass pad-tight" v-click>

## 🛠️ **Choose**

Pick the simplest method that solves the problem. A good scatter plot beats a bad neural network.

</div>

<div class="card card-success card-glass pad-tight" v-click>

## 📢 **Communicate**

Results that nobody understands have zero impact. Visualisation and storytelling are part of analysis.

</div>

</div>

---
---

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
---

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact" v-click>

## 📊 **"AI-Powered" Dashboard**

<div class="note-text">Reality: SQL queries + conditional formatting · Tool: Spreadsheet or BI tool</div>

</div>

<div class="card card-primary card-glass pad-compact" v-click>

## 🔔 **"Smart" Anomaly Detection**

<div class="note-text">Reality: Statistical control charts (invented 1924) · Tool: Basic statistics</div>

</div>

<div class="card card-secondary card-glass pad-compact" v-click>

## 🎯 **"Predictive" Analytics**

<div class="note-text">Reality: Linear regression on historical trends · Tool: A few lines of Python</div>

</div>

<div class="card card-accent card-glass pad-compact" v-click>

## 🤖 **Actual ML Use Case**

<div class="note-text">Reality: Image classification with millions of samples · Tool: Deep learning frameworks, GPUs</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md" v-click>

💡 **3 out of 4** need data analysis skills, not AI expertise. Know the difference.

</div>

---
---

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight" v-click>

## 📊 **Statistics**

<div class="note-text">Underpins inference, uncertainty, and experimental design</div>

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 🔧 **Data Engineering**

<div class="note-text">Ensures data are collected, stored, and discoverable</div>

</div>

<div class="card card-accent card-glass pad-tight" v-click>

## 🔍 **Data Analysis**

<div class="note-text">Explores, explains, and communicates what the data say</div>

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-tight" v-click>

## 🧪 **Data Science**

<div class="note-text">Fuses engineering, analysis, and machine learning</div>

</div>

<div class="card card-success card-glass pad-tight" v-click>

## 🤖 **AI / ML**

<div class="note-text">Automates pattern recognition at scale — one tool among many</div>

</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md" v-click>

🎯 **AI is a tool in the toolbox, not the toolbox itself.** Data analysis is the foundation everything else builds on.

</div>

---
---

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-tight" v-click>

## ⚠️ Jumping to complex models before understanding the data

</div>

<div class="card card-warning card-glass pad-tight" v-click>

## ⚠️ Confusing correlation with causation

</div>

<div class="card card-warning card-glass pad-tight" v-click>

## ⚠️ Overfitting pretty charts to noisy data

</div>

<div class="card card-warning card-glass pad-tight" v-click>

## ⚠️ Calling everything "AI" to sound impressive

</div>

<div class="card card-warning card-glass pad-tight" v-click>

## ⚠️ Shipping insights without reproducibility

</div>

</div>

---
---

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight" v-click>

## 🧠 **Data literacy > tool literacy**

Understanding your data matters more than knowing the latest framework

</div>

<div class="card card-secondary card-glass pad-tight" v-click>

## 🎯 **The thinking matters more than the label**

Good analysis is good analysis — whether you call it statistics, data science, or AI

</div>

<div class="card card-accent card-glass pad-tight" v-click>

## 🔬 **CERN-grade rigour is learnable**

The same methods that found the Higgs apply to your business, your research, your career

</div>

<div class="card card-success card-glass pad-tight" v-click>

## 🚀 **These skills transfer everywhere**

From particle physics to finance, from genomics to marketing — data is the common language

</div>

</div>

---
---

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact" v-click>

## 🖥️ **Computing Foundations**

How computers actually work, command line, file management

</div>

<div class="card card-secondary card-glass pad-compact" v-click>

## 🐍 **Python Programming**

From zero to data analysis — the most in-demand language in science and industry

</div>

<div class="card card-accent card-glass pad-compact" v-click>

## 📊 **Data Analysis**

Statistics, probability, visualisation, fitting, and real-world case studies

</div>

<div class="card card-info card-glass pad-compact" v-click>

## 🔄 **Reproducibility**

Version control, workflows, and practices used at CERN and in industry

</div>

<div class="card card-success card-glass pad-compact" v-click>

## 🤖 **AI & Machine Learning**

Understand what it is, when to use it, and when not to

</div>

<div class="card card-warning card-glass pad-compact" v-click>

## 🎯 **Your Own Project**

Apply everything to a real project in your field

</div>

</div>

---
layout: quote
---

# The best thing about being a scientist is that you never stop being a **student**.

---
layout: fact
---

# Thank you.

Dr. Mindaugas Šarpis

Data Analysis and Artificial Intelligence
