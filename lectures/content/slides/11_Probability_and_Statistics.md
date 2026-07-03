---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Probability and Statistics"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Probability and Statistics

---
hideInToc: true
layout: quote
---

# In science, we never measure the *true* value — we collect **samples**, estimate **parameters**, and quantify **uncertainty**. Probability gives us the language; statistics gives us the tools.

---
hideInToc: true
---

# Motivation

- ## All measurements have **uncertainty**

- ## We need to **distinguish signal from noise**

- ## Models require **parameter estimation**

- ## Results must be **statistically significant** *(a term we'll make precise later in this lecture)*

- ## Predictions come with **confidence intervals**

#### This lecture builds the foundation for data fitting, estimation, and quantifying uncertainty

---
layout: section
hideInToc: true
---

# Foundations of **Probability**

---
hideInToc: true
---

# What is Probability?

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

# Two Interpretations of Probability

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

# Basic Concepts

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### 🔬 **Experiment**

<div class="note-text mt-xs">Repeatable process producing an outcome</div>

</div>

<div class="card card-secondary card-glass pad-tight">

### 🌐 **Sample Space (Ω)**

<div class="note-text mt-xs">All possible outcomes</div>

</div>

<div class="card card-accent card-glass pad-tight">

### 🎯 **Event**

<div class="note-text mt-xs">Subset of Ω satisfying a condition</div>

</div>

<div class="card card-info card-glass pad-tight">

### 📊 **Probability P(A)**

<div class="note-text mt-xs">Number in [0,1] quantifying likelihood</div>

</div>

<div class="card card-warning card-glass pad-tight">

### 🚫 **Mutually exclusive (disjoint)**

<div class="note-text mt-xs">Two events that can't both happen: $A \cap B = \emptyset$. E.g. a single die roll being both even and odd.</div>

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

# Visualizing Sample Space & Events

<div class="grid-2-large">

<div>

## 🎲 Sample Space <br>
## Ω = {1, 2, 3, 4, 5, 6}

<div class="dice-grid">

<div class="dice-box dice-box-primary">1</div>
<div class="dice-box dice-box-success">2</div>
<div class="dice-box dice-box-info">3</div>
<div class="dice-box dice-box-success">4</div>
<div class="dice-box dice-box-warning">5</div>
<div class="dice-box dice-box-accent">6</div>

</div>

<div class="caption-text">
All outcomes are equally likely: P(each) = 1/6
</div>

</div>

<div>

## 📍 **Events (Subsets of Ω)**

<div class="stack-tight">

<div class="card card-success card-glass pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event A (even):</strong>
<span class="mono-strong">{2, 4, 6}</span>
</div>
</div>

<div class="card card-warning card-glass pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event B (&gt; 4):</strong>
<span class="mono-strong">{5, 6}</span>
</div>
</div>

<div class="card card-info card-glass pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event C (exact):</strong>
<span class="mono-strong">{3}</span>
</div>
</div>

<div class="card card-accent card-glass pad-snug">
<div class="flex-between">
<strong class="text-subhead">A ∩ B (even &amp; &gt; 4):</strong>
<span class="mono-strong">{6}</span>
</div>
</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Axioms of Probability (Kolmogorov)

<div class="card card-info card-glass pad-tight mt-md">

## **Axiomatic Foundation**

Given a sample space $\Omega$ and a collection of events, a probability function $P$ assigns to each event $A$ a real number $P(A)$ satisfying three axioms:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### ✅ **Axiom 1 — Non-negativity**

$$P(A) \geq 0$$

for any event $A$

<div class="meta-caption mt-xs">
Probabilities cannot be negative
</div>

</div>

<div class="card card-secondary card-glass pad-tight">

### 🌍 **Axiom 2 — Normalization**

$$P(\Omega) = 1$$

<div class="meta-caption mt-xs">
The entire sample space has probability 1
</div>

</div>

</div>

---
hideInToc: true
---

# Axiom 3 — Countable Additivity

<div class="card card-accent card-glass pad-tight mt-md">

### ➕ **Axiom 3**

If $A$ and $B$ are **mutually exclusive** $(A \cap B = \emptyset)$:

$$P(A \cup B) = P(A) + P(B)$$

More generally, for any countable collection of pairwise disjoint events $A_1, A_2, \ldots$:

$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

<div class="meta-caption mt-xs">
Disjoint events add — this is the foundation for all probability calculations
</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 💡 **Why these axioms matter**

From just these three axioms, every rule of probability can be derived: complement rule, addition rule, conditional probability, Bayes' theorem, and more.

</div>

---
hideInToc: true
---

# Useful Rules from the Axioms

<div class="card card-info card-glass pad-compact mt-md">

## **Derived Properties**

From the three axioms, we can derive important rules that make probability calculations tractable.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### 🔄 **Complement Rule**

$$P(A^c) = 1 - P(A)$$

where $A^c$ is the complement of $A$

<div class="meta-caption mt-xs">
Follows from $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$
</div>

</div>

<div class="card card-info card-glass pad-tight">

### ➕ **General Addition Rule**

For any events $A$ and $B$:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

<div class="meta-caption mt-xs">
Avoids double-counting the intersection
</div>

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

### ✖️ **Multiplication Rule** — For **independent** events (where knowing one tells you nothing about the other): $P(A \cap B) = P(A) \times P(B)$

</div>

---
hideInToc: true
---

# Conditional Probability

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

# Conditional Probability Visualization

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

# Independence

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

# Bayes' Theorem Components

<div style="display: flex; align-items: center; gap: 1.2rem; margin-top: 2rem; justify-content: center;">

<div class="card card-primary card-glass pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📊 **Prior**
### $P(A)$

<div class="note-text mt-xs">Initial belief</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">×</div>

<div class="card card-secondary card-glass pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📈 **Likelihood**
### $P(B|A)$

<div class="note-text mt-xs">Data probability</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">÷</div>

<div class="card card-info card-glass pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📐 **Evidence**
### $P(B)$

<div class="note-text mt-xs">Normalization</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">=</div>

<div class="card card-accent card-glass pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 🎯 **Posterior**
### $P(A|B)$

<div class="note-text mt-xs">Updated belief</div>

</div>

</div>

<div class="card card-success card-glass pad-tight" style="margin-top: 1.5rem; text-align: center;">

**The Bayesian Update:** Multiply prior by likelihood, then normalize by evidence to get updated belief

</div>

---
hideInToc: true
---

# Bayes' Theorem

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

# Example: Medical Test

<div class="card card-warning card-glass pad-tight">

## 🏥 **Scenario**

Disease: 1% prevalence • Test: 95% sensitivity, 90% specificity

**sensitivity** = P(test + | has disease); **specificity** = P(test − | no disease)

**Question:** Probability of disease if test is positive?

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Calculation**

$$P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+)}$$

$P(+) = 0.95(0.01) + 0.10(0.99) = 0.1085$

$$P(D \mid +) = \frac{0.0095}{0.1085} \approx \textbf{8.8%}$$

</div>

<div class="card card-accent card-glass pad-tight">

## 💡 **Insight**

Only **8.8%** chance despite positive test!

**Why?** Rare disease → false positives (990) >> true positives (95)

</div>

</div>


---
hideInToc: true
---

# Visualizing the Medical Test

<div class="card card-info card-glass pad-compact mt-sm">

## 👥 **Population: 10,000** — Disease prevalence **1%** → 100 diseased, 9,900 healthy

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

<div class="card card-warning card-glass pad-tight mt-md">

## 📊 **Total positives: $95 + 990 = 1{,}085$**

$$P(\text{Disease} \mid +) = \frac{95}{1{,}085} \approx \textbf{8.8\%}$$

False positives dominate when disease is rare.

</div>

---
layout: section
hideInToc: true
---

# Random Variables and Distributions

---
hideInToc: true
---

# Random Variables

<div class="card card-info card-glass pad-tight mt-md">

## **Formal Definition**

A **random variable** $X:\Omega\to\mathbb{R}$ assigns a number to each possible outcome $\omega$ (an element of the sample space $\Omega$). E.g. for a die, $X$ could be "the number shown".

$$X: \Omega \rightarrow \mathbb{R}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Purpose**

Random variables allow us to:
- Work with numbers instead of abstract outcomes
- Use calculus and algebra
- Define probability distributions
- Calculate expected values and variances

</div>

<div class="card card-secondary card-glass pad-tight">

## **Notation**

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

# Types of Random Variables

<div class="card card-info card-glass pad-tight mt-sm">

## 🎲 **Random variable $X$** — maps outcomes $\omega \in \Omega$ to real numbers

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔢 **Discrete** — countable outcomes

- **PMF:** $P(X = x)$
- **Support:** $\{0, 1, 2, \ldots\}$
- **Examples:** dice · Bernoulli · counts

</div>

<div class="card card-secondary card-glass pad-tight">

## 📈 **Continuous** — real-valued range

- **PDF:** $f(x)$
- **Support:** intervals of $\mathbb{R}$
- **Examples:** time · energy · lengths

</div>

</div>


---
hideInToc: true
---

# Discrete Random Variables

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

# PMF Example: Coin Flips

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

# Continuous Random Variables

<div class="card card-info card-glass pad-tight mt-md">

## **Definition**

A random variable $X$ is **continuous** if it can take any value in an interval or union of intervals (uncountably many values).

**Key Insight:** For continuous $X$, $P(X = x) = 0$ for any specific $x$. Only intervals have non-zero probability.

With infinitely many possible values packed into any interval, no single exact value carries probability weight — so for continuous variables probability lives in *intervals*, $P(a \le X \le b)$, which is why we use a probability **density** (PDF) rather than a mass function.

</div>

---
hideInToc: true
---

# Probability Density Function (PDF)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Definition**

The PDF $f(x)$ is **not** a probability, but a density. Probabilities are computed as:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

**Properties:**
1. $f(x) \geq 0$ for all $x$
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$
3. $P(X = c) = 0$ for any specific $c$

</div>

<div class="card card-accent card-glass pad-tight">

## **Example: Uniform on [0,1]**

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

# Cumulative Distribution Function (CDF)

<div class="card card-info card-glass pad-tight mt-md">

## **Definition**

For any random variable $X$ (discrete or continuous), the CDF is:

$$F(x) = P(X \leq x)$$

The CDF gives the probability that $X$ takes a value **at most** $x$.

</div>

---
hideInToc: true
---

# CDF Properties and Uses

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Properties**

1. **Non-decreasing:** If $x_1 < x_2$, then $F(x_1) \leq F(x_2)$
2. **Limits:** $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$
3. **Right-continuous:** $\lim_{h \to 0^+} F(x+h) = F(x)$
4. **For continuous $X$:** $F'(x) = f(x)$ (PDF is derivative of CDF)

</div>

<div class="card card-accent card-glass pad-tight">

## **Why CDFs are useful**

- Works for **both** discrete and continuous RVs
- Probability of intervals:

$$P(a < X \leq b) = F(b) - F(a)$$

- Quantiles: Find $x$ such that $F(x) = p$
- Easy to visualize cumulative behavior
- Foundation for statistical inference

</div>

</div>

---
layout: section
hideInToc: true
---

# Descriptive Statistics

---
hideInToc: true
---

# Measures of Central Tendency

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Mean (Average)**

- Formula: $\mu = \frac{\sum x_i}{n}$
- Uses every value
- Most familiar summary
- **Sensitive** to outliers

</div>

<div class="card card-secondary card-glass pad-tight">

## **Median**

- Middle value after sorting
- Splits data into two halves
- Robust to skew/outliers

</div>

<div class="card card-info card-glass pad-tight">

## **Mode**

- Most frequent value(s)
- Good for categorical data
- Can have multiple modes

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## **Example**

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

# Measures of Spread

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### 📏 **Range**

$$\text{Range} = \max - \min$$

<div class="meta-caption">Simple but not robust</div>

</div>

<div class="card card-accent card-glass pad-tight">

### 📊 **Variance**

$$\sigma^2 = \frac{\sum(x_i - \mu)^2}{n}$$

<div class="meta-caption">Average squared deviation</div>

</div>

<div class="card card-info card-glass pad-tight">

### 📈 **Standard Deviation**

$$\sigma = \sqrt{\text{variance}}$$

<div class="meta-caption">Same units as data</div>

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

📦 **Quartiles & the IQR** — sort the data and split it into quarters: **Q1** (25th percentile), the **median** (Q2, 50th), and **Q3** (75th). The **interquartile range** $\text{IQR} = Q_3 - Q_1$ spans the middle 50% — the robust spread measure a **boxplot** draws.

</div>

---
hideInToc: true
---

# Why Variance?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Why square deviations?**

<div class="card-content text-base">
Squaring removes sign, magnifies large misses, and yields smooth functions that work well with calculus/optimization.
</div>

</div>

<div class="card card-info card-glass pad-tight">

## **Population vs Sample**

<div class="card-content text-base">
$$
\sigma^2 = \frac{1}{n}\sum (x_i-\mu)^2, \qquad

$$

$$
s^2 = \frac{1}{n-1}\sum (x_i-\bar{x})^2
$$
Bessel's correction ($n-1$) keeps $s^2$ unbiased.
</div>

</div>


</div>

---
hideInToc: true
---

# Sample Statistics and Population Parameters

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
hideInToc: true
---

# Expectation and Variance

<div class="card card-info card-glass pad-tight mt-md">

## **Expected Value (Mean)**

The **expectation** or **expected value** $E[X]$ (also written $\mu$) is the "average" value of $X$ weighted by probabilities:

**Discrete:**

$$E[X] = \sum_{\text{all } x} x \cdot P(X = x)$$

**Continuous:**

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x)\,dx$$

</div>

---
hideInToc: true
---

# Variance

<div class="card card-primary card-glass pad-tight mt-md">

## 📐 **Definition**

Measures spread around the mean:

$$\text{Var}(X) = E[(X - \mu)^2]$$

**Computational formula:**

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

**Standard deviation:**

$$\sigma = \sqrt{\text{Var}(X)}$$

</div>

---
hideInToc: true
---

# Properties of Expectation and Variance

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

# Common Probability Distributions

---
hideInToc: true
---

# Distribution Overview

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

# Discrete Distributions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Bernoulli (1 trial)**

- Outcome: success (1) or failure (0)
- Parameter: $p = P(X = 1)$
- Mean $= p$, variance $= p(1-p)$
- Building block for discrete models

</div>

<div class="card card-secondary card-glass pad-tight">

## **Binomial (n trials)**

- $n$ independent Bernoulli trials
- $X =$ number of successes
- $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- Mean $= np$, variance $= np(1-p)$

</div>

</div>

---
hideInToc: true
---

# Poisson Distribution

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **When to use**

- Counting rare events in fixed interval
- Events occur independently
- Constant average rate $\lambda$

## **PMF**
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

<div class="meta-caption mt-sm">Parameter $\lambda$ = expected count.</div>

</div>

<div class="card card-info card-glass pad-tight">

## **Properties & Examples**

- Mean = variance = $\lambda$
- $P(X=0) = e^{-\lambda}$ (no events)
- Additive: sum of independent Poissons → Poisson

- Radioactive decays • photon arrivals
- Network packet counts • DNA mutations

<div class="meta-caption mt-sm">Use Poisson to answer: "How many events per interval?"</div>

</div>

</div>

---
hideInToc: true
---

# Continuous Distributions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Uniform Distribution**

- Support: $[a,b]$
- $f(x) = \tfrac{1}{b-a}$ (flat)
- $E[X] = \tfrac{a+b}{2}$
- $\text{Var}(X) = \tfrac{(b-a)^2}{12}$

</div>

<div class="card card-secondary card-glass pad-tight">

## **Exponential Distribution**

- Time to first event
- $f(x) = \lambda e^{-\lambda x}$, $x \ge 0$
- $E[X] = 1/\lambda$, $\text{Var}(X) = 1/\lambda^2$
- **Memoryless:** $P(X > s+t \mid X > s) = P(X > t)$

</div>

</div>

---
hideInToc: true
---

# Why the Normal Distribution is Special

<div class="grid-3" style="gap: 0.8rem; margin-top: 1.5rem;">

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

<div style="text-align: center; font-size: 1.1em; font-weight: bold; margin-top: 1.5rem;">

🌟 The normal distribution is, in a sense, the **pattern of patterns** — average enough independent things and normality emerges.

</div>

---
hideInToc: true
---

# Normal Distribution

<div class="card card-info card-glass pad-tight mt-md">

## **Probability Density Function**

A random variable $X$ follows a **normal (Gaussian) distribution** with parameters $\mu$ (mean) and $\sigma^2$ (variance), written $X \sim N(\mu, \sigma^2)$, if:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad -\infty < x < \infty$$

</div>

---
hideInToc: true
---

# Normal Distribution Properties

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Key Properties**

1. **Symmetric** about $\mu$
2. **Bell-shaped** (unimodal)
3. **Mean = Median = Mode = $\mu$**
4. **Inflection points** at $x = \mu \pm \sigma$
5. **Area under curve = 1**
6. **Asymptotic**: tails approach (but never reach) zero

</div>

<div class="card card-accent card-glass pad-tight">

## **Standard Normal**

The **standard normal** $Z \sim N(0, 1)$ has:

$$\phi(z) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{z^2}{2}\right)$$

**Z-transformation (standardization):**

$$Z = \frac{X - \mu}{\sigma}$$

If $X \sim N(\mu, \sigma^2)$, then $Z \sim N(0, 1)$

This allows us to use standard tables/software for any normal distribution.

</div>

</div>

---
hideInToc: true
---

# The 68-95-99.7 Rule



For $X \sim N(\mu, \sigma^2)$:



<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-balanced text-center">
<div class="text-xl-strong">📊 68%</div>
<div class="note-text mt-xs">$\mu \pm \sigma$</div>
</div>

<div class="card card-info card-glass pad-balanced text-center">
<div class="text-xl-strong">📈 95%</div>
<div class="note-text mt-xs">$\mu \pm 2\sigma$</div>
</div>

<div class="card card-primary card-glass pad-balanced text-center">
<div class="text-xl-strong">🎯 99.7%</div>
<div class="note-text mt-xs">$\mu \pm 3\sigma$</div>
</div>

</div>

<div class="card card-warning card-glass pad-balanced" style="margin-top: 1.2rem;">

### 💡 **Practical Implication**

<div class="note-text mt-xs">

$3\sigma$ measurement = extremely rare (0.3%)

⚛️ **Physics**: $5\sigma$ = gold standard (1 in 3.5M)

</div>

</div>

---
hideInToc: true
---

# Two Different Promises: LLN vs CLT

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
layout: fact
hideInToc: true
---

# **Central Limit Theorem (CLT)**

### The cornerstone of statistical inference

---
hideInToc: true
---

# CLT Statement

<div class="card card-info card-glass pad-tight mt-md">

## **Theorem Statement**

Let $X_1, X_2, \ldots, X_n$ be independent and identically distributed (i.i.d.) random variables with:
- Mean: $E[X_i] = \mu$
- Variance: $\text{Var}(X_i) = \sigma^2 < \infty$

Define the sample mean:

$$\bar{X} = \frac{X_1 + X_2 + \cdots + X_n}{n} = \frac{1}{n}\sum_{i=1}^{n} X_i$$

Then as $n \to \infty$:

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

</div>

---
hideInToc: true
---

# CLT — Equivalent Form

<div class="card card-info card-glass pad-tight mt-md">

Or equivalently, the standardized sum converges in distribution to $N(0,1)$:

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

</div>


<div class="card card-primary card-glass pad-tight mt-md">

## **Key Insights**

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

# Why CLT Matters

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Why we rely on it**

- Measurement errors = many tiny effects → approximate normal
- Sampling distributions of means trend toward normal even if raw data are skewed
- Confidence intervals & hypothesis tests assume normality via CLT

</div>

<div class="card card-secondary card-glass pad-tight">

## **Die-rolling intuition**

- Roll a die $n$ times and average:
  - $n=1$: uniform
  - $n=2$: slightly peaked
  - $n=10$: bell-shaped
  - $n=100$: tightly normal
- More samples $\Rightarrow$ distribution of $\bar{X}$ smooths out.

<div class="meta-caption mt-sm">CLT magic: sum/average of many independent pieces → normal.</div>

</div>

</div>

---
hideInToc: true
---

# Standard Error

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-balanced">

### 📐 **Definition**

$$SE = \frac{\sigma}{\sqrt{n}}$$

<div class="meta-caption">Std dev of sample mean</div>

</div>

<div class="card card-warning card-glass pad-balanced">

### 🔍 **Interpretation**

<div class="text-tight">

📊 Uncertainty in $\mu$

📉 Decreases as $\sqrt{n}$

🔢 Halve error: $4\times$ data

</div>

</div>

<div class="card card-success card-glass pad-balanced">

### 📝 **Usage**

<div class="text-tight">

**mean $\pm$ SE**

or **mean $\pm 2 \times$ SE**

for ~95% confidence

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

# Estimation

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Point Estimation**

- Single best guess for a parameter
- $\bar{x}$ estimates $\mu$
- $s^2$ estimates $\sigma^2$
- Deterministic function of the data

</div>

<div class="card card-secondary card-glass pad-tight">

## **Interval Estimation**

- Range of plausible parameter values
- Confidence interval (CI) contains true value with chosen probability (e.g., 95%)
- Communicates both estimate and uncertainty

</div>

<div class="card card-info card-glass pad-tight">

## **Desirable Properties**

- **Unbiased:** $E[\hat{\theta}] = \theta$
- **Consistent:** converges to truth as $n$ grows
- **Efficient:** minimal variance among unbiased estimators

</div>

</div>


---
hideInToc: true
---

# Maximum Likelihood Estimation (MLE)

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Idea**

Pick parameter values $\theta$ that make the observed data most probable.

</div>

<div class="card card-secondary card-glass pad-tight">

## **Likelihood Function**

$L(\theta \mid \text{data}) = P(\text{data} \mid \theta)$

- Independent observations: $L(\theta) = \prod f(x_i; \theta)$
- Often easier to work with $\log L(\theta)$ (turns products into sums)

</div>

<div class="card card-info card-glass pad-tight">

## **Maximum Likelihood Estimator**

- $\hat{\theta} = \arg\max_\theta L(\theta)$
- Many estimators have closed forms (e.g., mean of normals)
- Provides asymptotically efficient, normal estimators

</div>

</div>

---
hideInToc: true
---

# MLE Example: Normal Mean

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Setup**

- Observations $x_1, \ldots, x_n$
- Model: $X_i \sim N(\mu, \sigma^2)$ with known $\sigma$
- Likelihood: $L(\mu) = \prod \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x_i-\mu)^2}{2\sigma^2}\right)$

## **Result**

$\hat{\mu} = \bar{x}$ (sample mean) maximizes $L(\mu)$.

</div>

<div class="card card-info card-glass pad-tight">

## **Why this matters**

- MLE gives a principled estimator derived from probability
- Extends to any distribution by swapping in the appropriate pdf/pmf
- Asymptotically optimal (minimum variance, normal errors)
- Foundation for many fitting algorithms

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
layout: section
hideInToc: true
---

# Connecting to Data Fitting

---
hideInToc: true
---

# Data Fitting Workflow

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

# From Probability to Fitting

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Data fitting problem**

- Observations $(x_i, y_i)$
- Model relationship $y = f(x; \theta) + \varepsilon$
- Goal: pick $\theta$ that best explains the data

</div>

<div class="card card-secondary card-glass pad-tight">

## **Statistical foundation**

- Errors modeled as random (often normal)
- Estimate $\theta$ via least squares / MLE
- Quantify uncertainty (SEs, CIs, $\chi^2$)
- Diagnose fit quality before trusting results

<div class="meta-caption mt-sm">The rest of this section applies these ideas to concrete fitting workflows.</div>

</div>

</div>

---
hideInToc: true
---

# Least Squares = MLE (for normal errors)

<div class="card card-primary card-glass pad-tight mt-md">

<div class="text-tight">
If errors are independent and normally distributed:

$$y_i = f(x_i; \theta) + \varepsilon_i, \quad \varepsilon_i \sim N(0, \sigma^2)$$

Then minimizing the sum of squared errors

$$S(\theta) = \sum \left(y_i - f(x_i; \theta)\right)^2$$

is mathematically identical to maximizing the likelihood.
</div>

<div class="meta-caption mt-sm">
Least squares = MLE under Gaussian noise → explains its ubiquity.
</div>

</div>

---
hideInToc: true
---

# Chi-Squared (χ²) Statistic

<div class="card card-info card-glass pad-tight mt-md">

## **Definition**

$$\chi^2 = \sum \frac{(\text{observed} - \text{expected})^2}{\text{variance}}$$

For weighted fits with known uncertainties $\sigma_i$:

$$\chi^2 = \sum \left[\frac{y_i - f(x_i; \theta)}{\sigma_i}\right]^2$$

## **Interpretation**

- Measures "badness of fit"
- Expectation: $\chi^2 \approx n - p$ (dof)
- Good fit: $\chi^2/(n-p) \approx 1$
- $\gg 1$: model misses structure; $\ll 1$: uncertainties inflated

</div>

---
hideInToc: true
---

# Common Mistakes and Pitfalls (1/2)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Probability vs Statistics**

<div class="card-content text-base">
Probability starts with a model and reasons forward to the data, while statistics starts with data and works backward to infer or validate a model. Treating them as the same step often leads to incorrect intuition.
</div>

</div>

<div class="card card-warning card-glass pad-tight">

## **p-hacking**

<div class="card-content text-base">
Running many tests until one looks "significant" inflates false positives. Pre-register analyses and adjust for multiple comparisons to keep results honest.
</div>

</div>

</div>

---
hideInToc: true
---

# Common Mistakes and Pitfalls (2/2)

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-tight">

## **Misreading Confidence Intervals**

<div class="card-content text-base">
A 95% confidence interval does not mean "95% chance the parameter lies here." It means that, across repeated experiments, the method produces intervals that contain the true value about 95% of the time.
</div>

</div>

<div class="card card-accent card-glass pad-tight">

## **Extrapolation**

<div class="card-content text-base">
Models are trustworthy only within the range where they were calibrated. Predictions far outside that range should be treated with caution (or new data).
</div>

</div>

</div>

---
hideInToc: true
---

# Practical Advice (1/2)

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
The natural next step beyond this course: a p-value measures how surprising your data would be if nothing interesting were going on. Learn it before drawing "significant/not significant" conclusions.
</div>

</div>

</div>

---
hideInToc: true
---

# Practical Advice (2/2)

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

<div class="card card-primary card-glass pad-tight mt-md" style="grid-column: 1 / -1;">

## 📝 **Document for Reproducibility**

Record every step of your analysis — data source, cleaning, model choices, software versions — so others (and future you) can reproduce the results.

</div>

---
layout: section
hideInToc: true
---

# Bringing It **Together**

---
hideInToc: true
---

# **The Journey So Far**

From a blank terminal to statistical inference:

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🧰 **The Craft**

Command line, files, version control, and Python — the tools to *do* the work reliably.

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **The Analysis**

Concepts of data analysis, visualisation, and now probability & statistics — the tools to *make sense* of data.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md" style="text-align: center;">

You now have an end-to-end toolkit: **load data → explore & visualise → model it → quantify uncertainty → report honestly.** Keep practising it on your own projects — that's where it becomes yours.

</div>
