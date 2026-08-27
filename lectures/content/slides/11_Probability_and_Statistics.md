---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Probability and Statistics"
layout: cover

addons:
  - slidev-addon-python-runner

python:
  installs: ["numpy", "matplotlib", "scipy"]
  prelude: |
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import binom, norm
    import warnings
    warnings.filterwarnings('ignore')
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Probability and Statistics

##### <span class="aims-badge">🔧 tool-agnostic</span>

<!--
Speaker: this is the one "theory" lecture of the course. Frame it as the language for everything that follows — fitting, uncertainty, honest reporting. Reassure them: intuition over proofs. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# In science, we never measure the *true* value — we collect **samples**, estimate **parameters**, and quantify **uncertainty**. Probability gives us the language; statistics gives us the tools.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🎲 Reason with **probability** — axioms, conditional probability, and Bayes' theorem

</div>

<div class="card card-secondary card-glass pad-compact">

📈 Describe data with **distributions** and summaries — mean, variance, SD

</div>

<div class="card card-accent card-glass pad-compact">

🔔 Apply the **Central Limit Theorem** and the standard error of the mean

</div>

<div class="card card-success card-glass pad-compact">

🎯 Distinguish a **standard deviation** from a **standard error**

</div>

<div class="card card-warning card-glass pad-compact">

🔗 Connect statistics to **data fitting** — least squares, MLE, and χ²

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Stress the SD-vs-SE and CLT items — those change how they report results. Seminar 11 is where they apply this to the D⁰ sample. (~1 min)
-->

---
hideInToc: true
---

# Motivation

- ## All measurements have **uncertainty**

- ## We need to **distinguish signal from noise**

- ## Models require **parameter estimation**

- ## Claims need **quantified confidence** — how sure are we?

- ## Predictions come with **confidence intervals**

#### This lecture builds the foundation for data fitting, estimation, and quantifying uncertainty

---
layout: section
hideInToc: true
---

# Foundations of **Probability**

<!--
Speaker: this first block is the grammar — axioms, conditional probability, Bayes. Keep it brisk; the die and medical-test examples do the real teaching. (~1 min)
-->

---
hideInToc: true
---

# What is **Probability**?

<div class="card card-info card-glass pad-tight">

## 🎲 **Definition**

**Probability** is a numerical measure of the likelihood of an event occurring, constrained to the interval $[0, 1]$:

- 🚫 $P(A) = 0$ means event $A$ is **impossible**
- ✅ $P(A) = 1$ means event $A$ is **certain**
- 🤔 $0 < P(A) < 1$ means event $A$ is **uncertain**

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 🎯 **Purpose**

📊 Quantify uncertainty • 🔮 Make predictions • 📈 Update beliefs with evidence • 🌍 Model random phenomena in nature

</div>

---
hideInToc: true
---

# Two **Interpretations** of Probability

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Frequentist**

**Probability = long-run relative frequency**

$$P(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

where $n_A$ = occurrences of $A$ in $n$ trials

💡 **Example:** Flip coin 10,000 times → ~50% heads

**Used for:** Repeated experiments, physical processes

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧠 **Bayesian**

**Probability = degree of belief**

Subjective confidence updated with evidence

💡 **Example:** "70% chance of rain tomorrow"

**Used for:** One-time events, updating knowledge

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

⚖️ **Both valid!** • ⚛️ Physics: mostly frequentist • 🤖 ML: increasingly Bayesian

</div>

---
hideInToc: true
---

# Basic **Concepts**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔬 **Experiment**

<div class="note-text mt-xs">

Repeatable process producing an outcome

</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌐 **Sample Space (Ω)**

<div class="note-text mt-xs">

All possible outcomes

</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **Event**

<div class="note-text mt-xs">

Subset of Ω satisfying a condition

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 📊 **Probability P(A)**

<div class="note-text mt-xs">

Number in [0,1] quantifying likelihood

</div>

</div>

<div class="card card-warning card-glass pad-tight">

## 🚫 **Mutually exclusive (disjoint)**

<div class="note-text mt-xs">

Two events that can't both happen: $A \cap B = \emptyset$. E.g. a single die roll being both even and odd.

</div>

</div>

</div>

---
hideInToc: true
---

# Sample Space & Events · **Roll a die**

<div class="card card-info card-glass pad-tight mt-sm">

## 🎲 **Experiment** → Sample space $\Omega = \{1, 2, 3, 4, 5, 6\}$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Event A — Even**

$A = \{2, 4, 6\}$ • $P(A) = \tfrac{1}{2}$

</div>

<div class="card card-secondary card-glass pad-tight">

## 📈 **Event B — Greater than 4**

$B = \{5, 6\}$ • $P(B) = \tfrac{1}{3}$

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **Intersection $A \cap B$**

$\{6\}$ • $P(A \cap B) = \tfrac{1}{6}$

</div>

<div class="card card-success card-glass pad-tight">

## ➕ **Union $A \cup B$**

$\{2, 4, 5, 6\}$ • $P(A \cup B) = \tfrac{2}{3}$

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

<div class="note-text">

**Key:** Sample space Ω contains all outcomes • events are subsets • ∩ = both occur • ∪ = at least one occurs

</div>

</div>

---
hideInToc: true
---

# Axioms of Probability (**Kolmogorov**)

<div class="card card-info card-glass pad-compact mt-sm">

## 📜 **Axiomatic Foundation**

Given a sample space $\Omega$ and a collection of events, a probability function $P$ assigns to each event $A$ a real number $P(A)$ satisfying three axioms:

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✅ **1 — Non-negativity**

$$P(A) \geq 0$$

<div class="meta-caption mt-xs">

for any event $A$ — probabilities cannot be negative

</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌍 **2 — Normalization**

$$P(\Omega) = 1$$

<div class="meta-caption mt-xs">

the entire sample space has probability 1

</div>

</div>

<div class="card card-accent card-glass pad-tight">

## ➕ **3 — Additivity**

$$P(A \cup B) = P(A) + P(B)$$

<div class="meta-caption mt-xs">

for **mutually exclusive** $A, B$ — extends to countably many disjoint events

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 💡 **Why these axioms matter** — every rule of probability (complement, addition, conditional probability, Bayes' theorem…) can be derived from just these three

</div>

---
hideInToc: true
---

# Useful **Rules** from the Axioms

<div class="card card-info card-glass pad-compact mt-md">

## 🧰 **Derived Properties**

From the three axioms, we can derive important rules that make probability calculations tractable.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 🔄 **Complement Rule**

$$P(A^c) = 1 - P(A)$$

where $A^c$ is the complement of $A$

<div class="meta-caption mt-xs">

Follows from $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$

</div>

</div>

<div class="card card-info card-glass pad-tight">

## ➕ **General Addition Rule**

For any events $A$ and $B$:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

<div class="meta-caption mt-xs">

Avoids double-counting the intersection

</div>

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

## ✖️ **Multiplication Rule** — For **independent** events (where knowing one tells you nothing about the other): $P(A \cap B) = P(A) \times P(B)$

</div>

---
hideInToc: true
---

# Conditional **Probability**

<div class="card card-info card-glass pad-tight">

## 🎯 **Definition**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

Probability of $A$ given that $B$ has occurred • Restricts sample space to $B$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **Properties**

$0 \leq P(A \mid B) \leq 1$ • $P(\Omega \mid B) = 1$ • Additive for mutually exclusive events

</div>

<div class="card card-accent card-glass pad-tight">

## 🎲 **Example: Two dice**

$A$: sum is 8, $P(A) = 5/36$ • $B$: first die shows 3, $P(B) = 1/6$

$A \cap B = \{(3,5)\}$: of the 36 equally likely outcomes, only $(3,5)$ has the first die = 3 **and** the sum = 8, so $P(A \cap B) = 1/36$ → $P(A \mid B) = \frac{1/36}{1/6} = \frac{1}{6}$

</div>

</div>

---
hideInToc: true
---

# Conditional Probability — **Step by Step**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🌐 **1. Start** — sample space $\Omega$

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **2. Given** — event $B$ occurs

</div>

<div class="card card-accent card-glass pad-tight">

## 📦 **3. Restrict** — reduced sample space is $B$

</div>

<div class="card card-info card-glass pad-tight">

## ❓ **4. Check** — find $A \cap B$ inside the restricted space

</div>

<div class="card card-success card-glass pad-tight">

## 🎯 **5. Compute** — $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

<div class="note-text">

**Flow:** Start with Ω → given $B$ → restrict to $B$ → find $A \cap B$ → divide by $P(B)$

</div>

</div>

---
hideInToc: true
---

# **Independence**

<div class="card card-info card-glass pad-tight">

## 🔀 **Definition**

Events $A$ and $B$ are **independent** if:

$$P(A \cap B) = P(A) \cdot P(B) \quad \text{or equivalently} \quad P(A \mid B) = P(A)$$

Knowing $B$ occurred provides **no information** about $A$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✅ **Independent**

- Flipping two coins
- Rolling two dice
- Drawing cards **with** replacement

</div>

<div class="card card-warning card-glass pad-tight">

## ❌ **Not Independent**

- Drawing cards **without** replacement
- Height and weight
- Temperature and ice cream sales

</div>

</div>

---
hideInToc: true
---

# Bayes' **Theorem**

<div class="card card-info card-glass pad-tight">

## 🔄 **Formula**

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

**Terminology:** Prior $P(A)$ • Likelihood $P(B \mid A)$ • Evidence $P(B)$ • Posterior $P(A \mid B)$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💡 **Key Idea**

Reverses conditionals: $P(B \mid A) \to P(A \mid B)$

Update beliefs with new data

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **Applications**

Medical diagnosis • Spam filters • Parameter estimation • Hypothesis testing • ML

</div>

</div>

---
hideInToc: true
---

# Bayes' Theorem **Components**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight text-center">

## 📊 **Prior** — $P(A)$

Initial belief, before seeing the data

</div>

<div class="card card-secondary card-glass pad-tight text-center">

## 📈 **Likelihood** — $P(B \mid A)$

How probable the data is, if $A$ is true

</div>

<div class="card card-info card-glass pad-tight text-center">

## 📐 **Evidence** — $P(B)$

Normalization: how probable the data is overall

</div>

<div class="card card-accent card-glass pad-tight text-center">

## 🎯 **Posterior** — $P(A \mid B)$

Updated belief, after seeing the data

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md text-center">

## 🔄 **The Bayesian update** — Posterior = Prior × Likelihood ÷ Evidence

$$\underbrace{P(A \mid B)}_{\text{posterior}} = \frac{\overbrace{P(B \mid A)}^{\text{likelihood}} \cdot \overbrace{P(A)}^{\text{prior}}}{\underbrace{P(B)}_{\text{evidence}}}$$

Multiply the prior by the likelihood, then normalize — that is all "learning from data" means here.

</div>

---
hideInToc: true
---

# Example: **Medical Test**

<div class="card card-warning card-glass pad-compact mt-sm">

## 🏥 **Scenario** — disease: 1% prevalence • test: 95% sensitivity, 90% specificity

**sensitivity** = P(test + | has disease); **specificity** = P(test − | no disease). **Question:** probability of disease if the test is positive? Think in a population of **10,000** people → 100 diseased, 9,900 healthy

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🦠 **Diseased** — 100 people

- ✅ **True positive (TP):** 95
- ❌ **False negative (FN):** 5

</div>

<div class="card card-accent card-glass pad-tight">

## 💪 **Healthy** — 9,900 people

- ⚠️ **False positive (FP):** 990
- ✅ **True negative (TN):** 8,910

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

## 📊 **Total positives: $95 + 990 = 1{,}085$** → $P(\text{Disease} \mid +) = \dfrac{95}{1{,}085} \approx 8.8\%$

False positives dominate when the disease is rare.

</div>

---
hideInToc: true
---

# Medical Test — **Bayes' calculation**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Calculation**

$$P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+)}$$

$P(+) = P(+ \mid D)\,P(D) + P(+ \mid D^c)\,P(D^c)$

$\phantom{P(+)} = 0.95(0.01) + 0.10(0.99) = 0.1085$

$$P(D \mid +) = \frac{0.0095}{0.1085} \approx \textbf{8.8\%}$$

</div>

<div class="card card-accent card-glass pad-tight">

## 💡 **Insight**

Only **8.8%** chance despite a positive test — the same $95 / 1{,}085$ as the head-count.

**Why?** Rare disease → false positives (990) ≫ true positives (95).

Sensitivity is $P(+ \mid D)$; the patient wants $P(D \mid +)$ — Bayes' theorem reverses the conditional.

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="A disease has 1% prevalence; the test is 95% sensitive and 90% specific. A patient tests positive. Why is P(disease | positive) only 8.8%, not 95%?"
  :options="[
    'The test is unreliable and should not be used',
    'The disease is rare, so false positives from the large healthy population outnumber the true positives from the small diseased population',
    'Sensitivity and specificity were entered into the formula backwards',
    'P(disease | positive) always equals the test sensitivity'
  ]"
  :correct="1"
  explanation="With only 1% prevalence, healthy people vastly outnumber diseased people — so even a 10% false-positive rate among the healthy produces more false positives (990) than true positives (95). Sensitivity and specificity describe P(test | disease); confusing that with P(disease | test) is the classic base-rate fallacy."
/>

<!--
Speaker: let them vote before revealing — most pick "95%" instinctively. The point is the base rate: 990 false positives vs 95 true. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Random Variables and **Distributions**

<!--
Speaker: the shift from events to numbers. PMF for discrete, PDF for continuous, CDF for both — that trio is the mental model to leave with. Expectation and variance close the block. (~1 min)
-->

---
hideInToc: true
---

# Random **Variables**

<div class="card card-info card-glass pad-tight mt-md">

## 📐 **Formal Definition**

A **random variable** $X:\Omega\to\mathbb{R}$ assigns a number to each possible outcome $\omega$ (an element of the sample space $\Omega$). E.g. for a die, $X$ could be "the number shown".

$$X: \Omega \rightarrow \mathbb{R}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 **Purpose**

Random variables allow us to:
- Work with numbers instead of abstract outcomes
- Use calculus and algebra
- Define probability distributions
- Calculate expected values and variances

</div>

<div class="card card-secondary card-glass pad-tight">

## ✍️ **Notation**

- **Random Variable:** $X, Y, Z$ (uppercase)
- **Specific Value:** $x, y, z$ (lowercase)
- **Probability:** $P(X = x)$ or $P(X \leq x)$

**Example:**
- Coin flip: $X = \begin{cases} 1 & \text{if heads} \\ 0 & \text{if tails} \end{cases}$

</div>

</div>

---
hideInToc: true
---

# Discrete Random **Variables**

<div class="card card-info card-glass pad-tight mt-md">

## 🔢 **Definition**

A random variable $X$ is **discrete** if it can only take countable values (e.g., $0, 1, 2, \ldots$ or a finite set).

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 📊 **Probability Mass Function (PMF)**

The PMF $p_X(x)$ or $P(X = x)$ gives the probability that $X$ takes the value $x$.

**Properties:**
1. $P(X = x) \geq 0$ for all $x$
2. $\sum_{\text{all } x} P(X = x) = 1$

</div>

---
hideInToc: true
---

# PMF Example: **Coin Flips**

<div class="card card-accent card-glass pad-tight mt-md">

## 🎯 **Example PMF**

$X$ = number of heads in 3 fair coin flips

<div class="text-sm mono-strong mt-sm">

| $x$ | 0 | 1 | 2 | 3 |
|-----|---|---|---|---|
| $P(X = x)$ | 1/8 | 3/8 | 3/8 | 1/8 |

</div>

<div class="meta-caption mt-sm">

Each probability is $\binom{3}{x}(0.5)^3$ — and they sum to 1: $\frac{1+3+3+1}{8} = 1 \;\checkmark$

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 💡 **Reading the PMF**

- The most likely outcomes are $x=1$ and $x=2$ (each with probability 3/8)
- The extreme outcomes $x=0$ and $x=3$ are equally unlikely (each 1/8)
- Every valid PMF must sum to exactly 1

</div>

---
hideInToc: true
---

# Continuous Random **Variables**

<div class="card card-info card-glass pad-tight mt-md">

## 📈 **Definition**

A random variable $X$ is **continuous** if it can take any value in an interval or union of intervals (uncountably many values).

**Key Insight:** For continuous $X$, $P(X = x) = 0$ for any specific $x$. Only intervals have non-zero probability.

With infinitely many possible values packed into any interval, no single exact value carries probability weight — so for continuous variables probability lives in *intervals*, $P(a \le X \le b)$, which is why we use a probability **density** (PDF) rather than a mass function.

</div>

---
hideInToc: true
---

# Probability **Density** Function (PDF)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **Definition**

The PDF $f(x)$ is **not** a probability, but a density. Probabilities are computed as:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

**Properties:**
1. $f(x) \geq 0$ for all $x$
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$
3. $P(X = c) = 0$ for any specific $c$

</div>

<div class="card card-accent card-glass pad-tight">

## 📏 **Example: Uniform on [0,1]**

$$f(x) = \begin{cases} 1 & \text{if } 0 \leq x \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

**Verification:**

$$\int_0^1 1 \, dx = 1 \quad \checkmark$$

**Probability calculation:**

$$P(0.2 \leq X \leq 0.5) = \int_{0.2}^{0.5} 1 \, dx = 0.3$$

</div>

</div>

---
hideInToc: true
---

# Cumulative Distribution Function (**CDF**)

<div class="card card-info card-glass pad-compact mt-sm">

## 📈 **Definition** — for any random variable $X$, discrete or continuous

$$F(x) = P(X \leq x)$$

the probability that $X$ takes a value **at most** $x$.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **Properties**

1. **Non-decreasing:** $x_1 < x_2 \Rightarrow F(x_1) \leq F(x_2)$
2. **Limits:** $F(x) \to 0$ as $x \to -\infty$ and $F(x) \to 1$ as $x \to \infty$
3. **For continuous $X$:** $F'(x) = f(x)$ — the PDF is the derivative of the CDF

</div>

<div class="card card-accent card-glass pad-tight">

## 💡 **Why CDFs are useful**

- Works for **both** discrete and continuous RVs
- Interval probabilities: $P(a < X \leq b) = F(b) - F(a)$
- Quantiles: find $x$ such that $F(x) = p$
- Foundation for statistical inference

</div>

</div>

---
hideInToc: true
---

# Expectation and **Variance**

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

## 🎯 **Expected Value (Mean)**

The **expectation** $E[X]$ (also written $\mu$) is the average of $X$ weighted by probabilities:

**Discrete:**

$$E[X] = \sum_{\text{all } x} x \cdot P(X = x)$$

**Continuous:**

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x)\,dx$$

</div>

<div class="card card-primary card-glass pad-tight">

## 📐 **Variance**

Measures spread around the mean:

$$\text{Var}(X) = E[(X - \mu)^2]$$

**Computational formula:**

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

**Standard deviation:** $\sigma = \sqrt{\text{Var}(X)}$ — same units as $X$

</div>

</div>

---
hideInToc: true
---

# **Properties** of Expectation and Variance

<div class="card card-accent card-glass pad-tight mt-md">

## 📏 **Linearity of Expectation**

- $E[aX + b] = aE[X] + b$
- $E[X + Y] = E[X] + E[Y]$ (always — even for dependent variables!)

</div>

<div class="card card-warning card-glass pad-tight mt-md">

## 📊 **Variance Properties**

- $\text{Var}(aX + b) = a^2\text{Var}(X)$ — adding a constant does not change variance
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ — only if $X$ and $Y$ are **independent**
- For dependent variables: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$

</div>

---
layout: section
hideInToc: true
---

# Descriptive **Statistics**

<!--
Speaker: how we summarise a sample — centre and spread. Flag the sample-vs-population bridge here; it sets up the standard error later. (~1 min)
-->

---
hideInToc: true
---

# Measures of **Central Tendency**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Mean (Average)**

- Formula: $\bar{x} = \frac{1}{n}\sum x_i$
- Uses every value
- Most familiar summary
- **Sensitive** to outliers

</div>

<div class="card card-secondary card-glass pad-tight">

## 📍 **Median**

- Middle value after sorting
- Splits data into two halves
- Robust to skew/outliers

</div>

<div class="card card-info card-glass pad-tight">

## 🔁 **Mode**

- Most frequent value(s)
- Good for categorical data
- Can have multiple modes

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🧮 **Example**

Data: [1, 2, 2, 3, 10]

- Mean = **3.6**
- Median = **2**
- Mode = **2**

<div class="meta-caption mt-sm">

Outlier 10 pulls the mean upward, but median/mode stay near the bulk.

</div>

</div>

---
hideInToc: true
---

# Measures of **Spread**

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 📏 **Range**

$$\text{Range} = \max - \min$$

<div class="meta-caption">

Simple but not robust

</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 **Sample Variance**

$$s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$$

<div class="meta-caption">

Average squared deviation from $\bar{x}$

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 📈 **Standard Deviation**

$$s = \sqrt{s^2}$$

<div class="meta-caption">

Same units as the data

</div>

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

📦 **Quartiles & the IQR** — sort the data and split it into quarters: **Q1** (25th percentile), the **median** (Q2, 50th), and **Q3** (75th). The **interquartile range** $\text{IQR} = Q_3 - Q_1$ spans the middle 50% — the robust spread measure a **boxplot** draws.

</div>

---
hideInToc: true
---

# Why **Variance**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ❓ **Why square deviations?**

<div class="card-content text-base">

Squaring removes sign, magnifies large misses, and yields smooth functions that work well with calculus/optimization.

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 🔬 **Population vs Sample**

<div class="card-content text-base">

$$
\sigma^2 = \frac{1}{n}\sum (x_i-\mu)^2
$$

$$
s^2 = \frac{1}{n-1}\sum (x_i-\bar{x})^2
$$

Bessel's correction ($n-1$) keeps $s^2$ unbiased.

**NumPy:** `np.std(x, ddof=1)` — the default `ddof=0` is the population formula.

</div>

</div>

</div>

---
hideInToc: true
---

# Sample Statistics and Population **Parameters**

<div class="card card-info card-glass pad-tight mt-md">

## 🔗 **The Bridge**

Every descriptive statistic we compute from data is a **sample estimate** of a true **population parameter**. The sample is what we observe; the population is what we want to learn about.

A **parameter** is a fixed but unknown number describing the whole population (e.g. the true mean $\mu$); a **statistic** is something we compute from our sample (e.g. $\bar{x}$). We use statistics to estimate parameters.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Key Correspondences**

- Sample mean $\bar{x}$ estimates population mean $\mu$
- Sample variance $s^2$ estimates population variance $\sigma^2$
- Sample proportion $\hat{p}$ estimates population proportion $p$

</div>

<div class="card card-accent card-glass pad-tight">

## 💡 **Why it matters**

- More data → estimates converge to true values (consistency)
- Unbiased estimators are correct "on average" over repeated samples
- The **standard error** quantifies how far the estimate might be from the truth
- This is the foundation for confidence intervals and hypothesis tests

</div>

</div>

---
layout: section
hideInToc: true
---

# Common Probability **Distributions**

<!--
Speaker: a quick zoo — Bernoulli/Binomial/Poisson (discrete), Uniform/Exponential/Normal (continuous). Poisson gives the √N counting error; the Normal is what measurement errors look like. (~1 min)
-->

---
hideInToc: true
---

# Distribution **Overview**

<div class="card card-info card-glass pad-tight mt-sm">

## 🎲 **Probability distributions** — how values of a random variable are distributed

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔢 **Discrete** — countable outcomes

- **Bernoulli** — $P(X=1) = p$
- **Binomial** — $n$ independent trials
- **Poisson** — rare events per interval

</div>

<div class="card card-secondary card-glass pad-tight">

## 📈 **Continuous** — real-valued range

- **Uniform** — flat on $[a, b]$
- **Exponential** — wait times
- **Normal** — $\mu, \sigma$

</div>

</div>

---
hideInToc: true
---

# **Discrete** Distributions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪙 **Bernoulli (1 trial)**

- Outcome: success (1) or failure (0)
- Parameter: $p = P(X = 1)$
- Mean $= p$, variance $= p(1-p)$
- Building block for discrete models

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 **Binomial (n trials)**

- $n$ independent Bernoulli trials
- $X =$ number of successes
- $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- Mean $= np$, variance $= np(1-p)$

</div>

</div>

---
hideInToc: true
---

# **Poisson** Distribution

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⏱️ **When to use**

- Counting rare events in a fixed interval
- Events occur independently
- Constant average rate $\lambda$

## 📐 **PMF**

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

<div class="meta-caption mt-sm">

Parameter $\lambda$ = expected count.

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 📊 **Properties & Examples**

- Mean = variance = $\lambda$
- **SD = √λ** → a count of $N$ events carries uncertainty ≈ **√N** (the "counting error")
- $P(X=0) = e^{-\lambda}$ (no events)
- Additive: sum of independent Poissons → Poisson
- Radioactive decays • photon arrivals • events in a mass window

<div class="meta-caption mt-sm">

Counting uncertainty √N ≠ SE on a mean — different questions.

</div>

</div>

</div>

---
hideInToc: true
---

# **Continuous** Distributions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📏 **Uniform Distribution**

- Support: $[a,b]$
- $f(x) = \tfrac{1}{b-a}$ (flat)
- $E[X] = \tfrac{a+b}{2}$
- $\text{Var}(X) = \tfrac{(b-a)^2}{12}$

</div>

<div class="card card-secondary card-glass pad-tight">

## ⏳ **Exponential Distribution**

- Time to first event
- $f(x) = \lambda e^{-\lambda x}$, $x \ge 0$
- $E[X] = 1/\lambda$, $\text{Var}(X) = 1/\lambda^2$
- **Memoryless:** $P(X > s+t \mid X > s) = P(X > t)$

</div>

</div>

---
hideInToc: true
---

# Why the Normal Distribution is **Special**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">
<div class="emoji-xl">🏆</div>
<div class="meta-strong">Most Important</div>
<div class="note-text mt-xs">The distribution you meet most often across science and statistics</div>
</div>

<div class="card card-secondary card-glass pad-compact">
<div class="emoji-xl">🌿</div>
<div class="meta-strong">Arises Naturally</div>
<div class="note-text mt-xs">Sums and averages of many small random effects tend toward it</div>
</div>

<div class="card card-info card-glass pad-compact">
<div class="emoji-xl">🎯</div>
<div class="meta-strong">CLT Foundation</div>
<div class="note-text mt-xs">The Central Limit Theorem explains why it appears so widely</div>
</div>

<div class="card card-success card-glass pad-compact">
<div class="emoji-xl">🔬</div>
<div class="meta-strong">Measurement Errors</div>
<div class="note-text mt-xs">Random errors are usually symmetric around the true value</div>
</div>

<div class="card card-warning card-glass pad-compact">
<div class="emoji-xl">🧪</div>
<div class="meta-strong">Statistical Tests</div>
<div class="note-text mt-xs">Many standard tests assume approximately normal data</div>
</div>

<div class="card card-accent card-glass pad-compact">
<div class="emoji-xl">⚙️</div>
<div class="meta-strong">Two Parameters: μ, σ²</div>
<div class="note-text mt-xs">Mean μ and variance σ² pin it down completely</div>
</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md text-center">

🌟 The normal distribution is, in a sense, the **pattern of patterns** — average enough independent things and normality emerges.

</div>

---
hideInToc: true
---

# **Normal** Distribution

<div class="card card-info card-glass pad-compact mt-sm">

## 🔔 **Probability Density Function** — $X \sim N(\mu, \sigma^2)$ with mean $\mu$ and variance $\sigma^2$

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad -\infty < x < \infty$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📐 **Key Properties**

- **Symmetric**, **bell-shaped** about $\mu$: mean = median = mode = $\mu$
- **Inflection points** at $x = \mu \pm \sigma$
- Area under the curve = 1; tails approach (but never reach) zero

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **Standard Normal**

$Z \sim N(0, 1)$ with density

$$\phi(z) = \frac{1}{\sqrt{2\pi}}\, e^{-z^2/2}$$

**Standardization:** $Z = \dfrac{X - \mu}{\sigma}$ — if $X \sim N(\mu, \sigma^2)$ then $Z \sim N(0,1)$, so one table (or software routine) serves every normal.

</div>

</div>

---
hideInToc: true
---

# The **68-95-99.7** Rule

For $X \sim N(\mu, \sigma^2)$:

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-balanced text-center">

<div class="text-xl-strong">📊 68%</div>

<div class="note-text mt-xs">

$\mu \pm \sigma$

</div>

</div>

<div class="card card-info card-glass pad-balanced text-center">

<div class="text-xl-strong">📈 95%</div>

<div class="note-text mt-xs">

$\mu \pm 2\sigma$

</div>

</div>

<div class="card card-primary card-glass pad-balanced text-center">

<div class="text-xl-strong">🎯 99.7%</div>

<div class="note-text mt-xs">

$\mu \pm 3\sigma$

</div>

</div>

</div>

<div class="card card-warning card-glass pad-balanced mt-md">

## 💡 **Practical Implication**

<div class="note-text mt-xs">

A $3\sigma$ measurement is extremely rare — 0.3% (both tails)

⚛️ **Physics**: $5\sigma$ = gold standard for a discovery — 1 in 3.5 M (one tail — the HEP convention)

</div>

</div>

---
layout: section
hideInToc: true
---

# Sampling & **Estimation**

<!--
Speaker: from describing a distribution to estimating its parameters from a sample. The CLT is the hinge — it turns any measurement into a normal error bar and gives us the standard error; MLE tells us how to pick the estimate. (~1 min)
-->

---
layout: fact
hideInToc: true
---

# **Central Limit Theorem (CLT)**

### The cornerstone of statistical inference

---
hideInToc: true
---

# CLT **Statement**

<div class="card card-info card-glass pad-tight mt-md">

## 📜 **Theorem Statement**

Let $X_1, X_2, \ldots, X_n$ be independent and identically distributed (i.i.d.) random variables with:
- Mean: $E[X_i] = \mu$
- Variance: $\text{Var}(X_i) = \sigma^2 < \infty$

Define the sample mean:

$$\bar{X} = \frac{X_1 + X_2 + \cdots + X_n}{n} = \frac{1}{n}\sum_{i=1}^{n} X_i$$

Then for large $n$, **approximately**:

$$\bar{X} \;\overset{\text{approx.}}{\sim}\; N\!\left(\mu, \frac{\sigma^2}{n}\right)$$

</div>

---
hideInToc: true
---

# CLT — **Equivalent** Form

<div class="card card-info card-glass pad-tight mt-md">

Or equivalently, the standardized sum converges in distribution to $N(0,1)$:

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

</div>


<div class="card card-primary card-glass pad-tight mt-md">

## 🔑 **Key Insights**

- Works for **any** underlying distribution (not just normal!)
- Larger $n$ → better approximation
- Standard error: $SE = \sigma/\sqrt{n}$ decreases with $\sqrt{n}$
- Rule of thumb: $n \geq 30$ often sufficient for good approximation

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔗 **Connection to Fitting**

This justifies the normal-error assumption used in fitting: measurement errors typically arise from many small independent effects, so by the CLT they are approximately normally distributed.

</div>

---
hideInToc: true
---

# Why CLT **Matters**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧭 **Why we rely on it**

- Measurement errors = many tiny effects → approximate normal
- Sampling distributions of means trend toward normal even if raw data are skewed
- Confidence intervals & hypothesis tests assume normality via CLT

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎲 **Die-rolling intuition**

- Roll a die $n$ times and average:
  - $n=1$: uniform
  - $n=2$: slightly peaked
  - $n=10$: bell-shaped
  - $n=100$: tightly normal
- More samples $\Rightarrow$ distribution of $\bar{X}$ smooths out.

<div class="meta-caption mt-sm">

CLT magic: sum/average of many independent pieces → normal.

</div>

</div>

</div>

---
hideInToc: true
---

# Interactive: **Binomial → Normal**

<div class="note-text mt-sm">

Watch the Binomial PMF for growing $n$ collapse onto the Normal curve the CLT predicts — $\mu = np$, $\sigma = \sqrt{np(1-p)}$.

</div>

```python {monaco-run} {autorun:false}
p = 0.5
fig, axes = plt.subplots(1, 3, figsize=(9, 2.7), sharey=True)
for ax, n in zip(axes, [5, 20, 80]):
    k = np.arange(0, n + 1)
    ax.bar(k, binom.pmf(k, n, p), color="#56B4E9", width=0.8)
    mu, sig = n * p, np.sqrt(n * p * (1 - p))
    xs = np.linspace(0, n, 300)
    ax.plot(xs, norm.pdf(xs, mu, sig), color="#D55E00", linewidth=2)
    ax.set(title=f"n={n}", xlabel="k")
plt.tight_layout(); plt.show()
```

---
hideInToc: true
---

# Two Different Promises: **LLN vs CLT**

<div class="card card-info card-glass pad-compact mt-sm">

🎲 As $n$ grows, two distinct things happen to the sample mean $\bar{x}$ — students often blur them, but they answer different questions.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 **Law of Large Numbers**

*Where does $\bar{x}$ go?*

- The sample mean **converges to the true mean** $\mu$
- Justifies "collect more data → estimate gets closer to the truth"
- Says nothing about the *shape* of the uncertainty

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔔 **Central Limit Theorem**

*What shape is $\bar{x}$'s uncertainty?*

- The distribution of $\bar{x}$ becomes **normal**, with spread $\sigma/\sqrt{n}$
- Holds **whatever** the original distribution's shape
- Justifies error bars, confidence intervals, and $\pm 2\,\text{SE}$

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 LLN says the estimate **lands on the truth**; CLT says **how it wobbles** on the way there.

</div>

---
hideInToc: true
---

<MCQ
  question="As n grows, the LLN and the CLT both describe what happens to the sample mean — but they answer different questions. Which pairing is correct?"
  :options="[
    'LLN describes the shape of the uncertainty; CLT describes where the mean converges',
    'LLN describes where the mean converges; CLT describes the shape of its uncertainty',
    'They are two names for the same statement',
    'CLT only applies if the original data is already Normally distributed'
  ]"
  :correct="1"
  explanation="LLN says the sample mean converges to the true mean μ as n grows — it answers where does it land. CLT says the distribution of that mean becomes Normal with spread σ/√n, whatever the shape of the original data — it answers how it wobbles on the way there."
/>

<!--
Speaker: quick vote. The trap is the last option — the CLT needs no normality in the raw data; that is the whole point. (~3 min)
-->

---
hideInToc: true
---

# Standard **Error**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-balanced">

## 📐 **Definition**

$$SE = \frac{\sigma}{\sqrt{n}}$$

<div class="meta-caption">

Std dev of the sample mean

</div>

</div>

<div class="card card-warning card-glass pad-balanced">

## 🔍 **Interpretation**

<div class="text-tight">

📊 Uncertainty of $\bar{x}$ as an estimate of $\mu$

📉 Decreases as $\sqrt{n}$

🔢 Halve error: $4\times$ data

</div>

</div>

<div class="card card-success card-glass pad-balanced">

## 📝 **Usage**

<div class="text-tight">

**mean $\pm$ SE** → ~68% confidence

**mean $\pm 2 \times$ SE** → ~95% confidence

</div>

</div>

</div>

---
hideInToc: true
---

# Standard Deviation **vs** Standard Error

<div class="card card-info card-glass pad-compact mt-sm">

⚠️ The most-confused pair in statistics. They answer **different questions** — and only one shrinks as you collect more data.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Standard deviation (σ)**

- Spread of the **individual data points**
- "How variable is one measurement?"
- **Does not** shrink with more data — it converges to the true spread of the population

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎯 **Standard error (SE = σ/√n)**

- Spread of the **estimate of the mean**
- "How well do I know the average?"
- **Shrinks as √n** — more data pins the mean down tighter

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Rule: describe your **data** with σ; state the uncertainty of a **result** with SE. Error bars on a mean should almost always be SE (or a CI), not σ.

</div>

---
hideInToc: true
---

# Interactive: **Bootstrap** — Resampling for Free

<div class="note-text mt-sm">

No formula needed: resample your own data **with replacement** many times and look at how much the statistic wobbles. *(Seminar 11 stretch goal.)*

</div>

```python {monaco-run} {autorun:false}
rng = np.random.default_rng(0)                      # seeded → reproducible
data = rng.normal(10, 2, 50)                        # 50 "measurements"
boot_means = [np.mean(rng.choice(data, len(data), replace=True))
              for _ in range(1000)]

print(f"SE (bootstrap) = {np.std(boot_means):.3f}")
print(f"SE (formula)   = {np.std(data, ddof=1) / np.sqrt(len(data)):.3f}")
```

---
hideInToc: true
---

# **Estimation**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 **Point Estimation**

- Single best guess for a parameter
- $\bar{x}$ estimates $\mu$
- $s^2$ estimates $\sigma^2$
- Deterministic function of the data

</div>

<div class="card card-secondary card-glass pad-tight">

## 📏 **Interval Estimation**

- Range of plausible parameter values
- Confidence interval (CI): over many repeats, the chosen fraction (e.g. 95%) of such intervals bracket the true value
- Communicates both estimate and uncertainty

</div>

<div class="card card-info card-glass pad-tight">

## ⭐ **Desirable Properties**

- **Unbiased:** $E[\hat{\theta}] = \theta$
- **Consistent:** converges to truth as $n$ grows
- **Efficient:** minimal variance among unbiased estimators

</div>

</div>


---
hideInToc: true
---

# Maximum Likelihood **Estimation** (MLE)

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💡 **Idea**

Pick parameter values $\theta$ that make the observed data most probable.

</div>

<div class="card card-secondary card-glass pad-tight">

## 📐 **Likelihood Function**

$L(\theta \mid \text{data}) = P(\text{data} \mid \theta)$

- Independent observations: $L(\theta) = \prod f(x_i; \theta)$
- Often easier to work with $\log L(\theta)$ (turns products into sums)

</div>

<div class="card card-info card-glass pad-tight">

## 🎯 **Maximum Likelihood Estimator**

- $\hat{\theta} = \arg\max_\theta L(\theta)$
- Many estimators have closed forms (e.g., mean of normals)
- Provides asymptotically efficient, normal estimators

</div>

</div>

---
hideInToc: true
---

# MLE Example: **Normal Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⚙️ **Setup**

- Observations $x_1, \ldots, x_n$
- Model: $X_i \sim N(\mu, \sigma^2)$ with known $\sigma$
- Likelihood: $L(\mu) = \prod \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x_i-\mu)^2}{2\sigma^2}\right)$

## ✅ **Result**

$\hat{\mu} = \bar{x}$ (sample mean) maximizes $L(\mu)$.

</div>

<div class="card card-info card-glass pad-tight">

## 💡 **Why this matters**

- MLE gives a principled estimator derived from probability
- Extends to any distribution by swapping in the appropriate pdf/pmf
- Asymptotically optimal (minimum variance, normal errors)
- Foundation for many fitting algorithms

</div>

</div>

---
layout: section
hideInToc: true
---

# Connecting to Data **Fitting**

<!--
Speaker: the payoff — everything above is the vocabulary Lecture 12 uses. Walk the 7-step workflow once, show why least squares is MLE in disguise, and introduce χ²; the hands-on fitting is next week. (~1 min)
-->

---
hideInToc: true
---

# From Probability to **Fitting**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📥 **The data fitting problem**

- Observations $(x_i, y_i)$
- Model relationship $y = f(x; \theta) + \varepsilon$
- Goal: pick $\theta$ that best explains the data

</div>

<div class="card card-accent card-glass pad-tight">

## ➡️ **Where this goes**

**Lecture 12** turns these ideas into concrete fitting workflows:

- least-squares and $\chi^2$ fits of a model to data
- an MLE fit of the D⁰ peak
- uncertainties and goodness-of-fit read off the fit

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Nothing new is needed: errors are random variables (normal, by the CLT), the estimate comes from MLE, and its uncertainty is a standard error.

</div>

---
hideInToc: true
---

# Data Fitting **Workflow**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📥 **1. Data** — observations $(x_i, y_i)$

</div>

<div class="card card-secondary card-glass pad-tight">

## 📐 **2. Model** — $y = f(x; \theta) + \varepsilon$

</div>

<div class="card card-accent card-glass pad-tight">

## 🎯 **3. Method** — least squares · MLE · $\chi^2$

</div>

<div class="card card-info card-glass pad-tight">

## ✨ **4. Fit** — estimate parameters $\hat{\theta}$

</div>

<div class="card card-success card-glass pad-tight">

## 📏 **5. Uncertainty** — standard errors, confidence intervals

</div>

<div class="card card-warning card-glass pad-tight">

## 🔍 **6. Diagnose** — $\chi^2$, residuals, goodness-of-fit

</div>

<div class="card card-primary card-glass pad-tight">

## 🔁 **7. Report or revisit** — bad fit → return to step 2 • good fit → report $\hat{\theta} \pm \text{error}$ and predict $f(x_{\text{new}}; \hat{\theta})$

</div>

</div>

---
hideInToc: true
---

# Least Squares **= MLE** (for normal errors)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🎯 **The identity**

If errors are independent and normally distributed:

$$y_i = f(x_i; \theta) + \varepsilon_i, \quad \varepsilon_i \sim N(0, \sigma^2)$$

then minimizing the sum of squared errors

$$S(\theta) = \sum \left(y_i - f(x_i; \theta)\right)^2$$

is mathematically identical to maximizing the likelihood.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧱 **Statistical foundation**

- Errors modeled as random (often normal — the CLT again)
- Estimate $\theta$ via least squares / MLE
- Quantify uncertainty (SEs, CIs, $\chi^2$)
- Diagnose fit quality before trusting results

<div class="meta-caption mt-sm">

Least squares = MLE under Gaussian noise → explains its ubiquity.

</div>

</div>

</div>

---
hideInToc: true
---

# Chi-Squared (**χ²**) Statistic

<div class="card card-info card-glass pad-tight mt-md">

## 📐 **Definition**

$$\chi^2 = \sum \frac{(\text{observed} - \text{expected})^2}{\text{variance}}$$

For weighted fits with known uncertainties $\sigma_i$:

$$\chi^2 = \sum \left[\frac{y_i - f(x_i; \theta)}{\sigma_i}\right]^2$$

## 🔍 **Interpretation**

- Measures "badness of fit"
- Expectation: $\chi^2 \approx n - p$ (dof)
- Good fit: $\chi^2/(n-p) \approx 1$
- $\gg 1$: model misses structure; $\ll 1$: uncertainties inflated

</div>

---
hideInToc: true
---

# Common Mistakes and **Pitfalls**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔀 **Probability vs Statistics**

<div class="card-content text-base">

Probability starts with a model and reasons forward to the data; statistics starts with data and works backward to infer or validate a model. Treating them as the same step leads to wrong intuition.

</div>

</div>

<div class="card card-warning card-glass pad-tight">

## 🎣 **p-hacking**

<div class="card-content text-base">

Running many tests until one looks "significant" inflates false positives (a p-value measures how surprising the data would be under a null model — Lecture 12 shows the one you'll use). Pre-register analyses and adjust for multiple comparisons.

</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 📏 **Misreading Confidence Intervals**

<div class="card-content text-base">

A 95% CI does not mean "95% chance the parameter lies here." It means: across repeated experiments, the method produces intervals that contain the true value about 95% of the time.

</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 🚀 **Extrapolation**

<div class="card-content text-base">

Models are trustworthy only within the range where they were calibrated. Predictions far outside that range deserve caution (or new data).

</div>

</div>

</div>

---
hideInToc: true
---

# Correlation **≠** Causation

<div class="card card-warning card-glass pad-compact mt-sm glow">

⚠️ A statistical association between two variables does **not** mean one causes the other. This is the single most abused idea in data analysis.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🍦 **The classic example**

Ice-cream sales and drowning deaths are strongly correlated across the year.

Neither causes the other — **summer heat** drives both. A hidden **confounder** creates the association.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧭 **What can produce a correlation?**

- **Causation** (X → Y) — what we usually hope for
- **Reverse causation** (Y → X)
- A **confounder** driving both
- **Selection bias** in how data was collected
- Pure **coincidence** (especially with many variables)

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 To claim causation you need more than correlation — a **controlled experiment** (A/B test) or careful causal-inference methods. Observational correlation only flags *where to look*.

</div>

---
hideInToc: true
---

# Practical **Advice** (1/2)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Visualize First**

<div class="card-content text-base">

Always plot your data before running any analysis. Patterns, outliers, and unexpected structure are often obvious visually.

</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## ✓ **Check Assumptions**

<div class="card-content text-base">

Verify that the assumptions behind your statistical method actually hold for your data (normality, independence, constant variance).

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 📏 **Report Uncertainties**

<div class="card-content text-base">

A result without an uncertainty is incomplete. Always include error bars, confidence intervals, or standard errors.

</div>

</div>

<div class="card card-success card-glass pad-tight">

## 🎯 **Hypothesis testing & p-values**

<div class="card-content text-base">

Formal hypothesis testing is beyond this course — but you'll meet one specific p-value in Lecture 12: the χ² goodness-of-fit p-value, used purely as a fit-quality diagnostic, not as a "significant/not significant" verdict.

</div>

</div>

</div>

---
hideInToc: true
---

# Practical **Advice** (2/2)

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **Respect Small Samples**

<div class="card-content text-base">

Small samples give noisy estimates. Be cautious about drawing strong conclusions with limited data.

</div>

</div>

<div class="card card-accent card-glass pad-tight">

## 🔬 **Simulate When Unclear**

<div class="card-content text-base">

When analytical solutions are hard, Monte Carlo simulation can reveal the expected behavior of your estimator or test.

</div>

</div>

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 📝 **Document for Reproducibility**

Record every step of your analysis — data source, cleaning, model choices, software versions — so others (and future you) can reproduce the results.

</div>

---
layout: section
hideInToc: true
---

# Bringing It **Together**

<!--
Speaker: one MCQ to check that the SD-vs-SE message landed, then the recap and the seminar tie-in. (~1 min)
-->

---
hideInToc: true
---

<MCQ
  question="You measure a quantity 100 times and want to report how precisely you know its average. What should the error bar on the mean show?"
  :options="[
    'The standard deviation σ of the individual measurements',
    'The standard error σ/√n of the mean',
    'The full range (max − min) of the data',
    'The variance σ² of the measurements'
  ]"
  :correct="1"
  explanation="The standard error σ/√n measures the uncertainty in the estimated mean and shrinks as you collect more data; the standard deviation describes the spread of individual points and does not."
/>

<!--
Speaker: this is the seminar's crux. If they pick σ, send them back to the SD-vs-SE slide — the seminar asks for exactly this distinction. (~3 min)
-->

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Reason about **uncertainty** with probability axioms and Bayes' theorem

</div>

<div class="card card-success card-glass pad-compact">

✅ Work with **random variables** — PMF, PDF, CDF, and key distributions

</div>

<div class="card card-success card-glass pad-compact">

✅ Apply the **CLT** and report a **standard error** on a mean

</div>

<div class="card card-success card-glass pad-compact">

✅ Tell a **standard deviation** from a **standard error** apart

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Connect statistics to **data fitting** — least squares, MLE, χ² — closing the loop: load → explore & visualise → model → quantify uncertainty → report honestly

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 11 tie-in**

Measure the D⁰ peak mass from the shared LHCb sample and report it as mean ± SE — stating which number is the SD (spread of events) and which is the SE (how well you know the average), plus the √N counting uncertainty on the event count.

</div>

<!--
Speaker: have them nod along to each ✅. The seminar tie-in makes it concrete — they compute a mean on the D⁰ sample and report it with an honest ± SE, and separately the √N on the count. (~1 min)
-->

---
hideInToc: true
---

# Further **Reading**

<div class="card card-info card-glass pad-compact mt-sm">

📚 To go deeper — the first two are free and superb:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📗 **Diez, Çetinkaya-Rundel & Barr** — *OpenIntro Statistics* · free at openintro.org

</div>

<div class="card card-secondary card-glass pad-compact">

🎲 **Blitzstein & Hwang** — *Introduction to Probability* · free (Harvard Stat 110)

</div>

<div class="card card-accent card-glass pad-compact">

📘 **Wasserman** — *All of Statistics* — a fast, rigorous reference

</div>

<div class="card card-info card-glass pad-compact">

🔬 **Barlow** — *Statistics: A Guide to the Use of Statistical Methods in the Physical Sciences*

</div>

</div>
