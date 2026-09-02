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

##### <span class="aims-badge">🔧 ♻️ ⚙️ 📁 — applies all four aims</span>

<!--
Speaker: this is the capstone lecture — everything the course built now pays off
together. Set the tone: ML is not magic, it is the four aims applied at scale. It is
optional and advanced, so keep it conceptual over code. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Machine learning is not magic — it is **the four aims applied at scale**. The thinking you have built all course long matters more than the label on the model.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🤖 Frame ML as **learning rules from data** — the fitting loop at scale

</div>

<div class="card card-secondary card-glass pad-compact">

🔒 **Split** data into train / validation / test and evaluate only on unseen data

</div>

<div class="card card-accent card-glass pad-compact">

📉 Diagnose **overfitting** by watching the train-vs-test gap

</div>

<div class="card card-success card-glass pad-compact">

📊 Read a **confusion matrix** and prefer precision / recall to raw accuracy

</div>

<div class="card card-info card-glass pad-compact">

📈 Read a **ROC curve** and use cross-validation to get a mean *and* a spread

</div>

<div class="card card-warning card-glass pad-compact">

🧠 Use **LLMs and AI tools** responsibly — verify, reproduce, own the output

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Remind them this is the optional
capstone — the payoff is watching the four aims converge. Seminar 16 is where they
train and honestly evaluate a classifier on the D⁰ sample (or their own-field dataset). (~1 min)
-->

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

<!--
Speaker: the job of this block is to demystify ML and inoculate against hype — half of
what's sold as "AI" is decades-old statistics. Name the actual method. (~1 min)
-->

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

⚠️ "AI-powered" is often a label on decades-old, perfectly good statistics.

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

<!--
Speaker: anchor everything to the fitting loop from Lecture 12 — same shape, more
parameters. The golden rule, splitting your data, is the beat that matters most. (~1 min)
-->

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

📉 You met this in **Lecture 9** (50 parameters for 60 points) and in **fitting** (too many parameters). It is the defining failure mode of ML.

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
hideInToc: true
---

# Model Complexity — the Polynomial **Dial**

<div class="card card-info card-glass pad-compact mt-sm">

📉 The clearest way to *see* overfitting: fit the same 15 noisy points with polynomials of rising degree and watch train error and test error part ways. Degree is a **complexity dial** — the honest setting minimises error on **held-out** data, never on the training points.

</div>

<img class="fig" src="/figures/viz_ml_polynomial_dial.svg" style="display:block;margin:0.6rem auto 0;max-height:215px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact reveal-scale">

## 1️⃣ **Degree 1**

Too stiff — misses the curve. **Underfit**: poor on train *and* test.

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

## 3️⃣ **Degree 3**

Captures the shape, ignores the wiggles. **Just right**.

</div>

<div class="card card-primary card-glass pad-compact reveal-scale">

## 🔟 **Degree 10**

Threads every point — train error near zero, test error explodes. **Overfit**.

</div>

</div>

---
layout: section
hideInToc: true
---

# Regression — Fitting, **Rebranded**

<!--
Speaker: the friendliest on-ramp to ML — it is literally Lecture 12 with new
vocabulary. Land the translation table hard; everything else follows. (~1 min)
-->

---
hideInToc: true
---

# Linear Regression = Lecture 12, Rebranded

<div class="card card-info card-glass pad-tight mt-sm">

## 🔁 **You have already done this**

Fitting a straight line by **least squares** (Lecture 12) *is* machine learning's simplest model. Only the vocabulary changes — the mathematics is identical.

</div>

<div class="card card-primary card-glass pad-compact mt-sm">

| Fitting (Lecture 12) | Machine learning (today) |
|---|---|
| fit the model | **train** the model |
| parameters | **weights** |
| minimise χ² | minimise the **loss** |
| residuals | prediction **errors** |

</div>

<div class="note-text mt-md">

💡 And *goodness of fit* becomes **evaluation metrics** — where the next slides go.

</div>

---
hideInToc: true
---

# Least Squares Is a **Loss Function**

<div class="card card-info card-glass pad-tight mt-sm">

## 🎯 **The number training drives down**

The model is a line, `y = w·x + b`. A **loss** scores how wrong a prediction is; training searches for the `w`, `b` that make it smallest. Least squares — the **sum of squared residuals**, χ² from Lecture 12 with equal uncertainties — is one choice of loss. Choosing the loss chooses *what "wrong" means*: a modelling decision, not a detail.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 📐 **Squared error**

Punishes big misses hard — the least-squares loss you minimised in Lecture 12. Sensitive to outliers.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 📏 **Absolute error**

Treats every miss in proportion — robust when a few points go wild.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

🔧 `curve_fit(f, x, y)` in Lecture 12, `LinearRegression().fit(X, y)` today — same optimisation, different packaging. That uniform `fit` / `predict` API is what lets you swap models without rewriting your analysis.

</div>

<div class="note-text mt-md">

💡 Classifiers minimise a *different* loss (cross-entropy), but the idea is identical: name the mistake, then minimise it. ⚙️

</div>

---
hideInToc: true
---

# A First Regressor in scikit-learn

```python {*}{maxHeight:'320px'}
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Toy physics data: pT is (roughly) inversely proportional to curvature
rng = np.random.default_rng(42)
curvature = rng.uniform(0.5, 5.0, 500)
pt = 3.0 / curvature + rng.normal(0.0, 0.1, 500)

X = (1.0 / curvature).reshape(-1, 1)          # feature engineering!
X_train, X_test, y_train, y_test = train_test_split(
    X, pt, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
print(model.coef_[0], model.intercept_)       # ~3.0  ~0.0
```

<div class="note-text mt-sm">

🎯 The physics knowledge — `pt ∝ 1/curvature` — went into the **feature**, not the model. And the golden rule is unchanged: judge it on `X_test` only, data the fit never saw.

</div>

---
hideInToc: true
---

# Judging a Regression: MAE and RMSE

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-left">

## 📏 **MAE — mean absolute error**

The average of `|prediction − truth|`. Robust to outliers, and reads directly as *"typically off by 0.1 GeV"*.

</div>

<div class="card card-secondary card-glass pad-tight reveal-left">

## 📐 **RMSE — root mean squared error**

The square root of the mean squared error. Punishes **large** misses hard — the square root of the least-squares loss you minimised.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

⚠️ **Report both.** RMSE ≫ MAE means a few events are badly wrong — a tail the average hides. Both carry the **units of `y`**, so they mean something physical.

</div>

<div class="note-text mt-md">

💡 No "accuracy" here: regression quality is *how far off*, not *right or wrong*.

</div>

---
hideInToc: true
---

# Residual Plots — Your Old Friend

<div class="card card-info card-glass pad-compact mt-sm">

🔍 Lecture 12's habit transfers unchanged: plot **prediction − truth** against the prediction. Structure in the residuals = structure your model missed. A single score never shows this.

</div>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg" style="display:block;margin:0.6rem auto 0;max-height:290px;">

<div class="note-text mt-sm">

📊 **Anscombe's quartet**: four datasets, one identical fitted line and R² — only *plotting the data and residuals* reveals which fit is honest.

</div>

---
hideInToc: true
---

# From One Feature to Many

<div class="card card-info card-glass pad-compact mt-sm">

📊 Real problems have many features: `y = w₁x₁ + w₂x₂ + … + b`. Still least squares, still one line of scikit-learn — but three new habits matter.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

⚖️ **Scale your features** — a weight on "energy in MeV" is not comparable to one on "angle in radians" until you standardise them.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

🔍 **Weights are interpretable** — sign and size tell you *what the model believes*; nonsense weights are an early bug alarm.

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

📉 **More features = more ways to overfit** — regularisation (ridge, lasso) is the "fewer parameters" discipline from fitting, turned into an automatic penalty.

</div>

</div>

---
layout: section
hideInToc: true
---

# A First **Classifier**

<!--
Speaker: make it concrete with signal-vs-background in scikit-learn. Emphasise the same
four steps fit any model, and read the confusion matrix — not just accuracy. (~2 min)
-->

---
hideInToc: true
---

# Signal vs Background — the Setup

<div class="card card-info card-glass pad-compact mt-sm">

🎯 A classic physics task — and Seminar 16's exercise on the D⁰ sample: given event features (momenta, pT, …), decide **signal** or **background** — the trigger problem from Lecture 2, now learned from data.

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

# X, y = the D⁰ feature table and its peak/sideband label
# (X: n_events × n_features, y: 1 = signal, 0 = background)
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

Same four steps every time — swap `RandomForestClassifier` for any other model and nothing else changes. 🔧 The Random Forest is **classical ML** — great on tabular data; **deep learning** swaps in a many-layer neural network that learns its own features from raw data (images, text, audio).

</div>

---
hideInToc: true
---

# Try It: a Classifier in Pure NumPy

```py {monaco-run} {autorun:false}
import numpy as np
rng = np.random.default_rng(7)
# one feature; label 1 = signal, 0 = background (overlapping distributions)
X = np.r_[rng.normal(1.0, 1.0, 400), rng.normal(-1.0, 1.0, 400)]
y = np.r_[np.ones(400), np.zeros(400)]
i = rng.permutation(800); X, y = X[i], y[i]              # shuffle
Xtr, ytr, Xte, yte = X[:600], y[:600], X[600:], y[600:]  # split

# "train": one centroid per class.  "predict": nearest centroid
m1, m0 = Xtr[ytr == 1].mean(), Xtr[ytr == 0].mean()
pred = (np.abs(Xte - m1) < np.abs(Xte - m0)).astype(int)
print(f"test accuracy on unseen data: {(pred == yte).mean():.2f}")
```

<div class="note-text mt-sm">

🎯 No sklearn — just the **four steps**: build a feature, train (find the centroids), predict on **held-out** data, evaluate. The library only automates this. ▶️ **Run it**, then shrink the gap between the two means and watch accuracy fall toward 0.5.

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

# Trusting the **Score**

<!--
Speaker: a classifier hands you a probability, not a verdict. This block turns that
into an honest number you can defend — sweep the threshold, then rotate the split so
the estimate itself is reproducible. (~1 min)
-->

---
hideInToc: true
---

# A Classifier Outputs a **Probability**

<div class="card card-info card-glass pad-tight mt-sm">

## 🎚️ **`predict` hides a decision**

`model.predict` looks binary, but underneath sits `predict_proba` — a score from 0 to 1. The **cut** that turns 0.83 into "signal" is *your* choice, not the model's.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🔽 **Low threshold**

Catch almost all signal — but let background through. High recall, low precision.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 🔼 **High threshold**

Only the surest events pass — purer, but you miss real signal. High precision, low recall.

</div>

</div>

<div class="note-text mt-md">

💡 There is no single "accuracy" — there is a **whole curve** of trade-offs behind one model.

</div>

---
hideInToc: true
---

# Precision or Recall? Ask What It Costs

<div class="card card-info card-glass pad-compact mt-sm">

⚖️ You rarely maximise both — moving the threshold trades one for the other. Which you favour depends entirely on the **cost of each mistake**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🔬 **Favour precision**

When a false alarm is expensive — a claimed "discovery" that isn't. Physics leans here: the 5-sigma standard (Lecture 2).

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 🕸️ **Favour recall**

When a miss is expensive — a rare signal you can't discard, or a first-pass filter feeding a later cut.

</div>

</div>

<div class="note-text mt-md">

💡 **F1** blends the two into one number when you genuinely need a single score to compare models.

</div>

---
hideInToc: true
---

# The ROC Curve — Sweep Every Threshold

<div class="card card-info card-glass pad-compact mt-sm">

📈 Slide the cut from 1 down to 0 and plot **true-positive rate** against **false-positive rate**. Each point is one threshold; the curve is the model's entire behaviour.

</div>

<img class="fig" src="/figures/viz_ml_roc_curve.svg" style="display:block;margin:0.6rem auto 0;max-height:235px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 📐 **AUC — area under the curve**

`0.5` = coin flip (the diagonal), `1.0` = perfect: the chance a random signal event outranks a random background one. Above `0.8` is usually genuinely useful.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## ⚖️ **Why it beats accuracy**

**Threshold-free** and barely moved by class imbalance. For very rare signal, pair it with a **precision–recall curve**.

</div>

</div>

---
hideInToc: true
---

# Try It: a Threshold Sweep in NumPy

```py {monaco-run} {autorun:false}
import numpy as np
rng = np.random.default_rng(0)
# model scores: background peaks low, signal peaks high — but they overlap
bkg = rng.normal(0.35, 0.15, 2000).clip(0, 1)
sig = rng.normal(0.65, 0.15, 200).clip(0, 1)      # rare signal: ~1 in 11

for cut in (0.3, 0.5, 0.7):
    tpr = (sig >= cut).mean()          # recall: signal we keep
    fpr = (bkg >= cut).mean()          # background leaking through
    print(f"cut={cut}:  TPR={tpr:.2f}  FPR={fpr:.3f}")

# AUC ≈ P(random signal scored above random background)
auc = (sig[:, None] > bkg[None, :]).mean()
print(f"\nAUC = {auc:.3f}")
```

<div class="note-text mt-sm">

🎯 Raise the cut and both rates fall together — that trade-off *is* the ROC curve. The AUC never asked you to pick a threshold. ▶️ **Run it**, then widen the signal spread and watch AUC drop.

</div>

---
hideInToc: true
---

<MCQ
  question="Two classifiers are compared on the same imbalanced signal-vs-background sample. Model A has higher accuracy; Model B has higher ROC-AUC. Which is the safer basis for choosing?"
  :options="[
    'Accuracy — it is always the most honest single number',
    'Neither, unless both models use exactly the same threshold',
    'ROC-AUC — it is threshold-free and barely affected by class imbalance',
    'Whichever model is more complex — more complexity means better performance'
  ]"
  :correct="2"
  explanation="On imbalanced data accuracy is dominated by the majority class, so a lazy model can look strong. AUC summarises ranking ability across every threshold and is largely insensitive to the imbalance, so it reflects real separation power rather than the majority class."
/>

---
hideInToc: true
---

# Cross-Validation — Every Point Tested Once

<div class="card card-info card-glass pad-compact mt-sm">

♻️ One train/test split is a single random draw — get lucky and the score flatters you. **k-fold cross-validation** removes the luck: split into `k` parts, train on `k−1`, test on the held-out one, rotate.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🔁 **How it works**

Every point lands in the test set exactly once. Average the `k` scores → a **mean and a spread**, not one fragile number.

</div>

<div class="card card-success card-glass pad-compact reveal-left">

## ♻️ **The spread tells gain from noise**

The spread tells you whether a gain is real or noise — and a scripted CV run is a **reproducible** estimate, not a lucky screenshot.

</div>

</div>

<div class="note-text mt-md">

💡 `cross_val_score(model, X, y, cv=5)` — five honest numbers for one line of code. CV replaces the validation split for tuning — the final **test set** still stays untouched.

</div>

---
hideInToc: true
---

<MCQ
  question="Your Random Forest scores 100% on the training set and 71% on the test set. What is the most likely diagnosis — and the first fix?"
  :options="[
    'Data leakage — drop the feature that encodes the label',
    'Under-training — train longer or add more trees',
    'The test set is too small — the 71% is just noise',
    'Overfitting — simplify or regularise, then compare on held-out data'
  ]"
  :correct="3"
  explanation="A large train-vs-test gap is the signature of overfitting: the model memorised the training noise. Reduce its complexity (shallower trees, fewer features, regularisation) and judge every change on held-out data or with cross-validation. Leakage would inflate the test score too; more training would only widen the gap."
/>

---
layout: section
hideInToc: true
---

# Features — Where the **Physics** Lives

<!--
Speaker: the honest secret of applied ML — the model matters less than the features.
This is where the course's domain and data skills cash in, and where the most
dangerous, invisible bug lives: leakage. (~1 min)
-->

---
hideInToc: true
---

# Good Features Beat Fancy Models

<div class="card card-info card-glass pad-tight mt-sm">

## 🛠️ **The 80% nobody photographs**

Real analyses are won on **features**, not exotic models. A linear model on well-chosen inputs routinely beats a deep net on raw ones — and this is exactly where your physics and 📁 data skills pay off.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## ➗ **Encode what you know**

`pT ∝ 1/curvature`, an angle's `cos`, a ratio, a log — put the physics into `X` so the model needn't rediscover it.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## ⚖️ **Standardise & clean**

One scale, missing values handled, outliers understood — the Lecture 13 data work, pointed at a model.

</div>

</div>

---
hideInToc: true
---

# Building Features from the D⁰ Sample

<div class="card card-info card-glass pad-compact mt-sm">

🎯 At LHCb, three families of features separate a real D⁰ from a random track pairing — and the seminar sample lets you build the first from the daughter momenta alone.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏃 **Kinematics** — yours

Daughter `p`, `pT`, opening angle, momentum asymmetry — all computable from the two momentum vectors you already have.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📍 **Vertex quality**

Fit χ², flight distance — a genuine D⁰ flies, then decays at a clean displaced vertex.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎯 **Impact parameter**

Daughter tracks miss the primary vertex; combinatorial background often points back to it.

</div>

</div>

<div class="note-text mt-md">

💡 Vertex and impact-parameter features are what **full LHCb reconstruction** adds — use them if your file has those columns. And notice what is **not** on this list: the invariant **mass**. Hold that thought — the next slide is why.

</div>

---
hideInToc: true
---

# Data Leakage — the Silent Killer

<div class="card card-warning card-glass pad-tight mt-sm glow">

## 💧 **When the answer hides in the features**

Leakage is any information in `X` that won't exist at prediction time — or that secretly encodes `y`. The model scores brilliantly in testing and **collapses** in the real world.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🎯 **The physics trap**

Feed the **mass** in to classify the mass peak, and the model "learns" to read the answer. 100% — and worthless.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 🔧 **How to avoid it**

Fit every transform (scaling, imputing) on **train only**, then apply to test. Ask of each feature: *would I know this before the label?*

</div>

</div>

<div class="note-text mt-md">

⚠️ Leakage is why a "too-good-to-be-true" score usually is. Suspect it first.

</div>

---
hideInToc: true
---

<MCQ
  question="You classify D⁰ signal vs background, and one input feature is the reconstructed invariant mass. Cross-validated accuracy is 99.99%. What has most likely happened?"
  :options="[
    'The model is genuinely excellent and ready to deploy',
    'Data leakage — the mass you label on is also an input',
    'The dataset is too small for any score to be trusted',
    'Random Forests always overfit and should never be used'
  ]"
  :correct="1"
  explanation="The label was defined from a mass window, so the mass feature lets the model read the answer instead of learning physics. Drop it, keep only variables known independently of the mass, and the honest score falls to something believable."
/>

---
layout: section
hideInToc: true
---

# Learning **Without Labels**

<!--
Speaker: everything so far needed a y. Unsupervised learning gives that up and asks a
different question — what structure is already here? Keep k-means concrete: assign,
update, repeat. (~1 min)
-->

---
hideInToc: true
---

# When You Have No Labels

<div class="card card-info card-glass pad-tight mt-sm">

## 🔍 **A different question**

Supervised learning asks *"predict `y`"*. Unsupervised learning has **no `y`** at all — it asks *"what structure is already in `X`?"* You explore instead of predict.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **Clustering**

Group similar points — event types, particle categories.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📉 **Dimensionality reduction**

Compress many features to a few (PCA) for plotting and speed.

</div>

<div class="card card-accent card-glass pad-compact">

## 🚨 **Anomaly detection**

Flag points that fit no pattern — a new-physics search in spirit.

</div>

</div>

---
hideInToc: true
---

# k-means — Assign, Update, Repeat

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Pick `k`, the number of groups. Then loop two steps until nothing moves:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-left">

## 1️⃣ **Assign**

Attach every point to its **nearest centre**.

</div>

<div class="card card-secondary card-glass pad-tight reveal-left">

## 2️⃣ **Update**

Move each centre to the **mean** of its points.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

⚠️ You must **choose `k`**, and it assumes round, similar-sized blobs. It always returns clusters — whether or not real ones exist. Scale your features first, or the largest-numbered column hijacks the distance.

</div>

---
hideInToc: true
---

# Try It: k-means from Scratch

```py {monaco-run} {autorun:false}
import numpy as np
rng = np.random.default_rng(1)
# two true blobs of "events" in a 2-D feature space
A = rng.normal([0, 0], 0.5, (150, 2))
B = rng.normal([3, 3], 0.5, (150, 2))
X = np.vstack([A, B])

c = X[rng.choice(len(X), 2, replace=False)]        # random initial centres
for _ in range(10):
    d = ((X[:, None] - c) ** 2).sum(2)             # distance to each centre
    lab = d.argmin(1)                              # assign
    c = np.array([X[lab == k].mean(0) for k in range(2)])   # update

print("recovered centres:\n", c.round(2))
```

<div class="note-text mt-sm">

🎯 Ten lines, no library — the same *assign/update* loop scikit-learn runs. ▶️ **Run it**: the centres land near `(0,0)` and `(3,3)`, the blobs it was never told about.

</div>

---
hideInToc: true
---

# Clustering in Physics — Honest Expectations

<img class="fig" src="/figures/viz_ml_kmeans.svg" style="display:block;margin:0.6rem auto 0;max-height:235px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact reveal-left">

## ✅ **Where it helps**

Grouping detector hits into track candidates, sorting events by topology, a first pass over an unlabelled sample.

</div>

<div class="card card-warning card-glass pad-compact reveal-left">

## ⚠️ **Where it misleads**

Clusters are not physics categories. They shift with `k`, scaling, and the distance metric — always validate against something you understand.

</div>

</div>

<div class="note-text mt-md">

💡 Unsupervised methods **generate hypotheses**; they do not confirm them. That remains the analyst's job.

</div>

---
layout: section
hideInToc: true
---

# ML at the **Experiment**

<!--
Speaker: make it real — this is not a toy. The trigger is a classifier running at 40 MHz,
and flavour tagging decides what CP-violation measurements even mean. Two vivid stories. (~1 min)
-->

---
hideInToc: true
---

# The Trigger — Classification at 40 MHz

<div class="card card-info card-glass pad-tight mt-sm">

## ⚡ **The hardest deadline in computing**

The LHC collides bunches **40 million times a second**. Storing it all is impossible — physics you will never analyse must be dropped in **microseconds**. That keep-or-drop decision is a **classifier** (Lecture 2, now named).

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🎯 **The task**

Signal (interesting) vs background (routine) — the exact problem from this lecture, under a real-time budget.

</div>

<div class="card card-warning card-glass pad-compact reveal-left">

## 💸 **The stakes**

A wrong "drop" is data gone **forever**. Recall over raw accuracy — you cannot re-run the collision.

</div>

</div>

<div class="note-text mt-md">

♻️ LHCb now runs ML inside a fully software trigger — versioned, monitored, reproducible — at the ~30 MHz of crossings that actually produce a visible collision in LHCb.

</div>

---
hideInToc: true
---

# Flavour Tagging — Classification with Stakes

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ To measure matter–antimatter differences, LHCb must know whether a `B` meson was **born** as matter or antimatter. Nothing labels it — the answer is *inferred* from the rest of the event.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🤖 **A classifier's job**

Read the other tracks — their charges, their kinematics — and predict the initial flavour with a calibrated **probability**.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 📏 **Why calibration matters**

A mis-stated confidence biases the physics result. The **probability**, not just the label, is the deliverable.

</div>

</div>

<div class="note-text mt-md">

💡 This is why we cared about `predict_proba` and thresholds — real measurements ride on the number, not the verdict.

</div>

---
hideInToc: true
---

# ML Across the Experiment

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔬 **Particle ID**

Combine detector responses into one "is this a kaon?" probability.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📈 **Calibration**

Regression to correct measured energies back towards the truth.

</div>

<div class="card card-accent card-glass pad-compact">

## 🚨 **Anomaly searches**

Unsupervised hunts for events no model predicted — new physics.

</div>

</div>

<div class="note-text mt-md">

🔧 Every one of these is a tool you have now met — classification, regression, clustering — wearing an experiment's badge.

</div>

---
layout: section
hideInToc: true
---

# Modern AI, **Responsibly**

<!--
Speaker: LLMs are the tool of the moment — great for drafts, dangerous when trusted.
Land the responsible-use rules: you own the output, verify it, keep it reproducible.
Then the ethics beat, made concrete and technical rather than preachy: bias is a data
property; a model card is reproducibility for models; and the mark of maturity is
knowing when NOT to reach for ML at all. (~2 min)
-->

---
hideInToc: true
---

# Large Language Models, Briefly

<div class="card card-info card-glass pad-tight mt-sm">

## 🧠 **What they are**

Models trained to predict the next token over vast text. That simple objective yields tools that draft, summarise, translate, and **write code** — including analysis code. Under the hood: **neural networks** trained with the same loop you just learned — data, model, loss, train, evaluate — with the "features" learned from raw tokens, at vastly larger scale.

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

<div class="note-text mt-md">

⚙️ The frontier: LLMs increasingly act as **agents** — calling tools, editing files, and running code in a loop — the fastest-emerging category of automation.

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
hideInToc: true
---

# Bias In, Bias Out

<div class="card card-warning card-glass pad-tight mt-sm">

## ⚖️ **A model inherits its data**

ML learns the world you show it — **including its skews**. Under-represent a case in training and the model is worst exactly where you looked least. This is a **data** property before it is an algorithm one.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 🔀 **Spurious correlation**

The model latches onto whatever predicts `y` in *your* sample — a detector artefact, a run period — not the physics you meant.

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

## 🔍 **The defence**

Know your dataset (Lecture 13), check performance **per subgroup**, and be suspicious of any feature that works "too well".

</div>

</div>

---
hideInToc: true
---

# Model Cards — Reproducibility for Models

<div class="card card-info card-glass pad-tight mt-sm">

## ♻️ **Document the model like a dataset**

A trained model is a **research artefact**. A *model card* is its README: what it does, on what data, how well, and where it breaks — so a future reader (often you) can trust or retire it.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-left">

## 📇 **What to record**

Training data & date, the features, the metric **with its test set**, known limits, model + library versions.

</div>

<div class="card card-success card-glass pad-compact reveal-left">

## ⚙️ **Make it automatic**

Emit the card from the training script (Lecture 14) — a model no one can retrain or explain is not a result.

</div>

</div>

---
hideInToc: true
---

# When *Not* to Use ML

<div class="card card-info card-glass pad-compact mt-sm">

🧠 The most senior move in the room is often *"we don't need ML for this."* Reach for it only when simpler tools genuinely fall short.

</div>

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-compact reveal-up">

📏 **A formula or a cut already works** — don't trade a clear rule for an opaque model.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

🔍 **You must explain every decision** — a simple, inspectable model can beat an accurate black box.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

📉 **Data is scarce or unrepresentative** — ML amplifies the gaps, it does not fill them.

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

⚖️ **A confident error is expensive** — and you cannot audit why it was made.

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

💧 **Data leakage** — the answer (or test data) sneaking into the inputs → fake-great scores.

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

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Frame a task as **supervised learning** — features and labels

</div>

<div class="card card-success card-glass pad-compact">

✅ **Split** the data and train a classifier in scikit-learn

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **confusion matrix** — precision, recall, F1

</div>

<div class="card card-success card-glass pad-compact">

✅ Spot **overfitting**, data leakage, and the accuracy trap

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 16 tie-in — the four aims converge**

Train and honestly evaluate a signal-vs-background classifier on the D⁰ sample: label peak vs sidebands, stratified split, Random Forest or logistic regression, confusion matrix + precision/recall/F1 against the majority baseline, ROC/AUC, the train-vs-test gap — all in one seeded script. *Stretch: leak the mass in and watch 100% appear.*

🔧 swap the model, nothing else changes · ♻️ ⚙️ one seeded script reproduces the whole run · 📁 clean features, no leaked mass

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each card. The seminar makes
it concrete: the D⁰ sample (or their own-field dataset) goes through a real train/test
evaluation with the same metrics. (~1 min)
-->

---
hideInToc: true
---

# Further **Reading**

<div class="card card-info card-glass pad-compact mt-sm">

📚 Where to learn ML properly — the first is free and the best starting point:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📗 **James, Witten, Hastie, Tibshirani & Taylor** — *An Introduction to Statistical Learning with Applications in Python* (ISLP, 2023) · free at statlearning.com

</div>

<div class="card card-secondary card-glass pad-compact">

🛠️ **Géron** — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*

</div>

<div class="card card-accent card-glass pad-compact">

🐍 **scikit-learn user guide** — excellent, example-driven documentation

</div>

<div class="card card-info card-glass pad-compact">

🧠 **Google** — *Machine Learning Crash Course* · free, hands-on

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
