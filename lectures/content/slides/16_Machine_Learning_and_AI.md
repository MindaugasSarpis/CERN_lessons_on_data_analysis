---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

mermaid: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Machine Learning & AI

---
hideInToc: true
layout: quote
---

# Machine learning is not magic — it is **the four aims applied at scale**. The thinking you have built all course long matters more than the label on the model.

---
hideInToc: true
---

# Motivation

<div class="card card-info card-glass pad-tight mt-md">

## 🤖 **The capstone, not the point**

Every earlier lecture built a practice. Machine learning is where they **pay off together** — it is only as trustworthy as the data, code, and evaluation beneath it.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

🔧 **Tool-agnostic** — the ideas (features, loss, generalisation) outlive any framework

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

♻️ **Reproducible** — a model no one can retrain is not a result

</div>

<div class="card card-accent card-glass pad-compact reveal-scale">

⚙️ **Automated** — training and evaluation belong in your pipeline, not your memory

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

📁 **Data first** — a model is only as good as the data you feed it

</div>

</div>

<div class="note-text mt-md">

*This is an optional, advanced lecture — everything before it stands on its own.*

</div>

---
layout: section
hideInToc: true
---

# What ML **Is** (and Isn't)

---
hideInToc: true
---

# What Is <span class="gradient-text">Machine Learning</span>?

<div class="card card-info card-glass pad-tight mt-sm">

## 💡 **Learning patterns from data**

Instead of writing the rules by hand, you give a model **examples** and it learns a function that maps inputs to outputs — then applies it to data it has never seen.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight reveal-left">

## ✍️ **Traditional programming**

`rules + data → answers`

*You* encode the logic: "if energy > 100 GeV then …"

</div>

<div class="card card-success card-glass pad-tight reveal-left">

## 🤖 **Machine learning**

`data + answers → rules`

The model *infers* the logic from labelled examples.

</div>

</div>

<div class="note-text mt-md">

💡 It's the same modelling mindset as **curve fitting** (Lecture 12) — just with many more parameters and far less hand-crafting.

</div>

---
hideInToc: true
---

# Three Flavours of Learning

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🎯 **Supervised** — labelled examples

Predict a label (classification) or number (regression). *"Is this collision signal or background?"* — most of what we'll do here.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 🔍 **Unsupervised** — no labels

Find structure: clusters, anomalies, lower-dimensional views. *"Which events look unusual?"*

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

## 🕹️ **Reinforcement** — learn by reward

An agent takes actions and learns from feedback. Powerful, but rarely the first tool for data analysis.

</div>

</div>

---
hideInToc: true
---

# Where ML Sits Among the Fields

<div class="card card-info card-glass pad-compact mt-sm">

🧭 "Data science", "AI", "analytics" overlap constantly. The **thinking** is shared; the labels are marketing.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📊 **Statistics**

Inference, uncertainty, significance — the foundation (Lecture 11).

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔧 **Data engineering**

Moving, storing, cleaning data at scale — pipelines (Lectures 13–14).

</div>

<div class="card card-info card-glass pad-compact">

## 🔍 **Data analysis**

Asking questions, exploring, visualising, deciding (Lectures 9–10).

</div>

<div class="card card-accent card-glass pad-compact">

## 🧪 **Data science**

The blend of the three above, applied to a real problem.

</div>

<div class="card card-success card-glass pad-compact">

## 🤖 **AI / ML**

Models that *learn* the mapping — one tool in the box, not the whole box.

</div>

<div class="card card-warning card-glass pad-compact">

## 🎯 **The point**

Good analysis is good analysis — **whatever you call it**.

</div>

</div>

---
hideInToc: true
---

# What Is <span class="gradient-text">Not</span> AI

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ "AI-powered" is often a label on decades-old, perfectly good statistics. Knowing the difference is a superpower.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact" v-click>

## 📊 **"AI-Powered" dashboard**

*Reality:* SQL queries + conditional formatting.

</div>

<div class="card card-primary card-glass pad-compact" v-click>

## 🔔 **"Smart" anomaly detection**

*Reality:* statistical control charts (invented **1924**).

</div>

<div class="card card-secondary card-glass pad-compact" v-click>

## 🎯 **"Predictive" analytics**

*Reality:* linear regression on a trend — a few lines of Python.

</div>

<div class="card card-accent card-glass pad-compact" v-click>

## 🤖 **Actual ML**

*Reality:* image classification from millions of labelled samples.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md" v-click>

💡 **3 of these 4** need solid **data-analysis** skills, not AI expertise. Reach for ML when simpler tools genuinely can't do the job.

</div>

---
layout: section
hideInToc: true
---

# The ML **Workflow**

---
hideInToc: true
---

# The Workflow — Same Shape as Fitting

<div class="card card-info card-glass pad-compact mt-sm">

⚙️ You already know this loop from **data fitting** (Lecture 12). ML just scales it up.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

1️⃣ **Features** — turn raw data into numeric inputs `X` (📁 the data work pays off here)

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

2️⃣ **Model** — choose a family (linear, tree, network) with parameters to learn

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

3️⃣ **Train** — fit parameters by minimising a **loss** on training data

</div>

<div class="card card-success card-glass pad-compact reveal-left">

4️⃣ **Evaluate** — measure performance on **held-out** data, honestly

</div>

<div class="card card-warning card-glass pad-compact reveal-left">

5️⃣ **Iterate or ship** — good enough → deploy; not → back to features/model

</div>

</div>

---
hideInToc: true
---

# The Golden Rule: Split Your Data

<div class="card card-warning card-glass pad-tight mt-sm glow">

## 🔒 **Never evaluate on data you trained on**

A model that has *seen* the answers can memorise them. The only honest question is: **how does it do on data it has never seen?**

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

## 🏋️ **Train** (~60%)

Fit the model's parameters.

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

## 🎚️ **Validation** (~20%)

Tune choices (which model, how complex).

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

## 🎓 **Test** (~20%)

Touched **once**, at the end — your honest estimate.

</div>

</div>

<div class="note-text mt-md">

💡 When data is scarce, **cross-validation** rotates the split so every point is tested once.

</div>

---
hideInToc: true
---

# Overfitting — the Central Danger

<div class="card card-info card-glass pad-compact mt-sm">

📉 You met this in **Concepts of Data Analysis** (the 99.9%-accuracy trap) and in **fitting** (too many parameters). It is the defining failure mode of ML.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight reveal-left">

## 🐛 **Overfitting**

Model memorises noise → **great** on train, **poor** on test. Too complex for the data.

</div>

<div class="card card-primary card-glass pad-tight reveal-left">

## 🥱 **Underfitting**

Model too simple → poor on **both**. Missing real structure.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

🎯 The sweet spot is **generalisation**: the model captures the signal, ignores the noise. You find it by watching the **train-vs-test gap**, not the training score.

</div>

---
layout: section
hideInToc: true
---

# A First **Classifier**

---
hideInToc: true
---

# Signal vs Background — the Setup

<div class="card card-info card-glass pad-compact mt-sm">

🎯 A classic physics task and the course's running example: given event features (energy, momentum, …), decide **signal** or **background** — the trigger problem from Lecture 2, now learned from data.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📥 **Inputs `X`**

A table (Pandas!) — one row per event, columns of numeric features.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🏷️ **Labels `y`**

`1` = signal, `0` = background — from simulation or hand-labelled data.

</div>

</div>

<div class="note-text mt-md">

🔧 We'll use **scikit-learn** — but the workflow is identical in any ML library.

</div>

---
hideInToc: true
---

# A First Classifier in scikit-learn

```python {*}{maxHeight:'340px'}
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# X: features (n_events × n_features), y: 1=signal, 0=background
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 1. choose a model   2. train   3. predict on UNSEEN data
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 4. evaluate honestly
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<div class="note-text mt-sm">

Same four steps every time — swap `RandomForestClassifier` for any other model and nothing else changes. 🔧

</div>

---
hideInToc: true
---

# Reading the Result: the Confusion Matrix

<div class="card card-info card-glass pad-compact mt-sm">

🔢 Accuracy alone hides *how* a model is wrong. The **confusion matrix** shows every kind of mistake.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

|  | pred bg | pred signal |
|---|---|---|
| **actual bg** | ✅ TN | ❌ FP |
| **actual signal** | ❌ FN | ✅ TP |

</div>

<div class="card card-secondary card-glass pad-tight">

- **Precision** — of predicted signal, how much *is* signal?
- **Recall** — of real signal, how much did we *catch*?
- **False positives** flood you with fake discoveries; **false negatives** miss the real one.

</div>

</div>

<div class="note-text mt-md">

💡 In physics, a false "discovery" is expensive — recall the **5-sigma** standard from Lecture 2.

</div>

---
hideInToc: true
---

# Why Accuracy Can Lie

<div class="card card-warning card-glass pad-tight mt-sm glow">

## ⚠️ **The imbalanced-class trap**

If 1 event in 10,000 is signal, a model that predicts **"background, always"** is **99.99% accurate** — and completely useless.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 📏 **Use the right metric**

Precision, recall, F1, ROC-AUC — chosen for what the mistake *costs*.

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

## ⚖️ **Know your baseline**

Always compare against "predict the majority" and a simple model.

</div>

</div>

<div class="note-text mt-md">

📊 This is just the **data-analysis judgement** from earlier lectures, pointed at a model's output.

</div>

---
layout: section
hideInToc: true
---

# Modern **AI** & LLMs

---
hideInToc: true
---

# Large Language Models, Briefly

<div class="card card-info card-glass pad-tight mt-sm">

## 🧠 **What they are**

Models trained to predict the next token over vast text. That simple objective yields tools that draft, summarise, translate, and **write code** — including analysis code.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-tight reveal-left">

## ✅ **Great for**

- Boilerplate & first drafts of code
- Explaining errors, unfamiliar APIs
- Summarising, rephrasing, brainstorming

</div>

<div class="card card-warning card-glass pad-tight reveal-left">

## ⚠️ **Watch out for**

- Confident **wrong** answers (hallucination)
- No guarantee of reproducibility
- Data privacy — what you paste, you share

</div>

</div>

---
hideInToc: true
---

# Using AI Tools <span class="gradient-text">Responsibly</span>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🧠 **You own the output** — this course's project lets you use AI, but you must **understand and explain every line**.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

♻️ **Reproducibility still applies** — pin versions, script the steps, don't rely on a chat you can't rerun.

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🔍 **Verify, don't trust** — run it, test it, check it against what you know. AI is a fast junior, not an oracle.

</div>

<div class="card card-success card-glass pad-compact reveal-left">

🔧 **Tool, not crutch** — it accelerates people who understand the problem; it hides the gap for those who don't.

</div>

</div>

---
layout: section
hideInToc: true
---

# The **Thesis**

---
hideInToc: true
---

# Data Literacy <span class="gradient-text">></span> Tool Literacy

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight reveal-scale">

## 🧠 **Understanding beats frameworks**

Knowing *your data* and *your question* matters more than the latest library. Tools change every year; the thinking doesn't.

</div>

<div class="card card-secondary card-glass pad-tight reveal-scale">

## 🎯 **The thinking, not the label**

Statistics, data science, AI — good analysis is good analysis, whatever the name on the slide.

</div>

<div class="card card-accent card-glass pad-tight reveal-scale">

## 🔬 **CERN-grade rigour is learnable**

The methods that found the Higgs are the ones you've practised — applied honestly, at your scale.

</div>

<div class="card card-success card-glass pad-tight reveal-scale">

## 🚀 **These skills transfer everywhere**

Physics, finance, genomics, marketing — data is the common language.

</div>

</div>

---
hideInToc: true
---

# Classic Ways ML Goes Wrong

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-compact reveal-up">

🏃 **Jumping to complex models** before understanding the data — a linear baseline first, always.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

🔀 **Confusing correlation with causation** — a predictor is not a cause (Lecture 11).

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

💧 **Data leakage** — test information sneaking into training → fake-great scores.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

🏷️ **Calling everything "AI"** to sound impressive — name the actual method.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

♻️ **Shipping a model no one can retrain** — an unreproducible result is not a result.

</div>

</div>

---
hideInToc: true
---

# Key <span class="gradient-text">Takeaways</span>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact reveal-up">

🤖 **ML learns rules from examples** — the same modelling loop as fitting, at scale.

</div>

<div class="card card-secondary card-glass pad-compact reveal-up">

🔒 **Split your data** — train / validation / test; the test set is touched once.

</div>

<div class="card card-accent card-glass pad-compact reveal-up">

📉 **Watch overfitting** — trust the train-vs-test gap, never the training score.

</div>

<div class="card card-info card-glass pad-compact reveal-up">

📏 **Pick the right metric** — accuracy lies on imbalanced data; know what a mistake costs.

</div>

<div class="card card-success card-glass pad-compact reveal-up">

🧭 **Data literacy > tool literacy** — the four aims are what make ML trustworthy.

</div>

</div>

---
layout: quote
hideInToc: true
---

# You now have the whole toolkit: **organise** your data, **automate** your analysis, make it **reproducible**, and stay **tool-agnostic**. Machine learning is just the newest tool — the practices are what last.

---
hideInToc: true
layout: fact
---

# Thank you.

### Dr. Mindaugas Šarpis
