---
marp: true
mermaid: true
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Probability and Statistics"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Probability and Statistics

---
hideInToc: true
layout: quote
---

# In science, we never measure the *true* value—we collect **samples**, estimate **parameters**, and quantify **uncertainty**. Probability gives us the language; statistics gives us the tools.

---
hideInToc: true
---

# Motivation

- ## All measurements have **uncertainty**

- ## We need to **distinguish signal from noise**

- ## Models require **parameter estimation**

- ## Results must be **statistically significant**

- ## Predictions come with **confidence intervals**

#### This lecture builds the foundation for data fitting, hypothesis testing, and inference

---
layout: section
hideInToc: true
---

# Foundations of **Probability**

---
hideInToc: true
---

# What is Probability?

<div class="card card-info pad-tight">

## 🎲 **Definition**

**Probability** is a numerical measure of the likelihood of an event occurring, constrained to the interval $[0, 1]$:

- 🚫 $P(A) = 0$ means event $A$ is **impossible**
- ✅ $P(A) = 1$ means event $A$ is **certain**
- 🤔 $0 < P(A) < 1$ means event $A$ is **uncertain**

</div>

<div class="card card-primary pad-tight mt-md">

## 🎯 **Purpose**

📊 Quantify uncertainty • 🔮 Make predictions • 📈 Update beliefs with evidence • 🌍 Model random phenomena in nature

</div>

---
hideInToc: true
---

# Two Interpretations of Probability

<div class="grid-2 gap-md">

<div class="card card-primary pad-tight">

## 📊 **Frequentist**

**Probability = long-run relative frequency**

$$P(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

where $n_A$ = occurrences of $A$ in $n$ trials

💡 **Example:** Flip coin 10,000 times → ~50% heads

**Used for:** Repeated experiments, physical processes

</div>

<div class="card card-secondary pad-tight">

## 🧠 **Bayesian**

**Probability = degree of belief**

Subjective confidence updated with evidence

💡 **Example:** "70% chance of rain tomorrow"

**Used for:** One-time events, updating knowledge

</div>

</div>

<div class="card card-accent pad-tight mt-md">

⚖️ **Both valid!** • ⚛️ Physics: mostly frequentist • 🤖 ML: increasingly Bayesian

</div>

---
hideInToc: true
---

# Basic Concepts

<div class="grid-2 mt-md gap-tight">

<div class="card card-primary pad-tight">

### 🔬 **Experiment**

<div class="note-text mt-xs">Repeatable process producing an outcome</div>

</div>

<div class="card card-secondary pad-tight">

### 🌐 **Sample Space (Ω)**

<div class="note-text mt-xs">All possible outcomes</div>

</div>

<div class="card card-accent pad-tight">

### 🎯 **Event**

<div class="note-text mt-xs">Subset of Ω satisfying a condition</div>

</div>

<div class="card card-info pad-tight">

### 📊 **Probability P(A)**

<div class="note-text mt-xs">Number in [0,1] quantifying likelihood</div>

</div>

</div>

---
hideInToc: true
---

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#0f1f3d', 'primaryBorderColor': '#60a5fa', 'primaryTextColor': '#e2e8f0', 'secondaryColor': '#102b4c', 'lineColor': '#5eead4', 'fontFamily': 'Inter, system-ui, sans-serif'}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 40, 'rankSpacing': 45}}}%%
flowchart TD
    Exp["🎲 Experiment<br/><b>Roll a die</b>"]:::hub
    Exp --> SS["🌐 Sample Space Ω<br/><i>{1, 2, 3, 4, 5, 6}</i>"]:::category

    SS --> E1["📊 Event A: Even<br/>{2, 4, 6}<br/>P(A) = 1/2"]:::event
    SS --> E2["📈 Event B: > 4<br/>{5, 6}<br/>P(B) = 1/3"]:::event
    SS --> E3["🎯 Intersection A∩B<br/>{6}<br/>P(A∩B) = 1/6"]:::intersection
    SS --> E4["➕ Union A∪B<br/>{2, 4, 5, 6}<br/>P(A∪B) = 2/3"]:::union

    classDef hub fill:#0b2540,stroke:#60a5fa,stroke-width:3px,color:#f8fafc,rx:16px,ry:16px
    classDef category fill:#133661,stroke:#5eead4,stroke-width:2.5px,color:#e2e8f0,rx:14px,ry:14px
    classDef event fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e0f2fe,rx:12px,ry:12px
    classDef intersection fill:#155e75,stroke:#34d399,stroke-width:2px,color:#d1fae5,rx:12px,ry:12px
    classDef union fill:#1e3a5f,stroke:#fbbf24,stroke-width:2px,color:#fef3c7,rx:12px,ry:12px
```

<div class="card card-info pad-tight mermaid-note">

<div class="note-text">

**Key:** Sample space Ω contains all outcomes • Events are subsets • Intersection (∩) = both occur • Union (∪) = at least one occurs

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

<div class="card card-success pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event A (even):</strong>
<span class="mono-strong">{2, 4, 6}</span>
</div>
</div>

<div class="card card-warning pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event B (&gt; 4):</strong>
<span class="mono-strong">{5, 6}</span>
</div>
</div>

<div class="card card-info pad-snug">
<div class="flex-between">
<strong class="text-subhead">Event C (exact):</strong>
<span class="mono-strong">{3}</span>
</div>
</div>

<div class="card card-accent pad-snug">
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

<div class="card card-info pad-tight mt-md">

## **Axiomatic Foundation**

Given a sample space $\Omega$ and a collection of events, a probability function $P$ assigns to each event $A$ a real number $P(A)$ satisfying three axioms:

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### ✅ **Axiom 1**

**Non-negativity**

$$P(A) \geq 0$$

for any event $A$

<div class="meta-caption mt-xs">
Probabilities cannot be negative
</div>

</div>

<div class="card card-secondary pad-tight">

### 🌍 **Axiom 2**

**Normalization**

$$P(\Omega) = 1$$

<div class="meta-caption mt-xs">
The entire sample space has probability 1
</div>

</div>

<div class="card card-accent pad-tight">

### ➕ **Axiom 3**

**Countable Additivity**

If $A$ and $B$ are mutually exclusive $(A \cap B = \emptyset)$:

$$P(A \cup B) = P(A) + P(B)$$

<div class="meta-caption mt-xs">
Disjoint events add
</div>

</div>

</div>

---
hideInToc: true
---

# Useful Rules from the Axioms

<div class="card card-info pad-tight mt-md">

## **Derived Properties**

From the three axioms, we can derive important rules that make probability calculations tractable.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning pad-tight">

### 🔄 **Complement Rule**

$$P(A^c) = 1 - P(A)$$

where $A^c$ is the complement of $A$

<div class="meta-caption mt-xs">
Follows from $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$
</div>

</div>

<div class="card card-info pad-tight">

### ➕ **General Addition Rule**

For any events $A$ and $B$:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

<div class="meta-caption mt-xs">
Avoids double-counting the intersection
</div>

</div>

<div class="card card-success pad-tight">

### ✖️ **Multiplication Rule**

For independent events:

$$P(A \cap B) = P(A) \times P(B)$$

<div class="meta-caption mt-xs">
Only if $A$ and $B$ are independent
</div>

</div>

</div>

---
hideInToc: true
---

# Conditional Probability

<div class="card card-info pad-tight">

## 🎯 **Definition**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

Probability of $A$ given that $B$ has occurred • Restricts sample space to $B$

</div>

<div class="grid-2 mt-md gap-tight">

<div class="card card-primary pad-tight">

## 📐 **Properties**

$0 \leq P(A \mid B) \leq 1$ • $P(\Omega \mid B) = 1$ • Additive for mutually exclusive events

</div>

<div class="card card-accent pad-tight">

## 🎲 **Example: Two dice**

$A$: sum is 8, $P(A) = 5/36$ • $B$: first die shows 3, $P(B) = 1/6$

$A \cap B = \{(3,5)\}$ → $P(A \mid B) = \frac{1/36}{1/6} = \frac{1}{6}$

</div>

</div>

---
hideInToc: true
---

# Conditional Probability Visualization

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#0f1f3d', 'primaryBorderColor': '#60a5fa', 'primaryTextColor': '#e2e8f0', 'secondaryColor': '#102b4c', 'lineColor': '#5eead4', 'fontFamily': 'Inter, system-ui, sans-serif'}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 45, 'rankSpacing': 50}}}%%
flowchart LR
    Start["🌐 Sample Space Ω"]:::hub
    Start --> Condition["🔍 Given: B occurs"]:::process
    Condition --> NewSpace["📦 Reduced space: B"]:::category
    NewSpace --> Question["❓ Check A ∩ B"]:::process
    Question --> Answer["🎯 P(A|B) = P(A∩B)/P(B)"]:::result

    classDef hub fill:#0b2540,stroke:#60a5fa,stroke-width:2.5px,color:#f8fafc,rx:14px,ry:14px
    classDef process fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef category fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef result fill:#155e75,stroke:#5eead4,stroke-width:2.5px,color:#e0f2fe,rx:14px,ry:14px
```

<div class="card card-info pad-tight mermaid-note">

<div class="note-text">

**Flow:** Start with Ω → Given B occurs → Restrict to B → Find A∩B → Calculate ratio P(A∩B)/P(B)

</div>

</div>

---
hideInToc: true
---

# Independence

<div class="card card-info pad-tight">

## 🔀 **Definition**

Events $A$ and $B$ are **independent** if:

$$P(A \cap B) = P(A) \cdot P(B) \quad \text{or equivalently} \quad P(A \mid B) = P(A)$$

Knowing $B$ occurred provides **no information** about $A$

</div>

<div class="grid-2 mt-md gap-tight">

<div class="card card-primary pad-tight">

## ✅ **Independent**

- Flipping two coins
- Rolling two dice
- Drawing cards **with** replacement

</div>

<div class="card card-warning pad-tight">

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

<div class="card card-primary pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📊 **Prior**
### $P(A)$

<div class="note-text mt-xs">Initial belief</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">×</div>

<div class="card card-secondary pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📈 **Likelihood**
### $P(B|A)$

<div class="note-text mt-xs">Data probability</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">÷</div>

<div class="card card-info pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 📐 **Evidence**
### $P(B)$

<div class="note-text mt-xs">Normalization</div>

</div>

<div style="font-size: 2.5em; color: #5eead4; font-weight: 700;">=</div>

<div class="card card-accent pad-tight" style="flex: 0 0 auto; min-width: 140px; text-align: center;">

### 🎯 **Posterior**
### $P(A|B)$

<div class="note-text mt-xs">Updated belief</div>

</div>

</div>

<div class="card card-success pad-tight" style="margin-top: 1.5rem; text-align: center;">

**The Bayesian Update:** Multiply prior by likelihood, then normalize by evidence to get updated belief

</div>

---
hideInToc: true
---

# Bayes' Theorem

<div class="card card-info pad-tight">

## 🔄 **Formula**

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

**Terminology:** Prior $P(A)$ • Likelihood $P(B \mid A)$ • Evidence $P(B)$ • Posterior $P(A \mid B)$

</div>

<div class="grid-2 mt-md gap-tight">

<div class="card card-primary pad-tight">

## 💡 **Key Idea**

Reverses conditionals: $P(B \mid A) \to P(A \mid B)$

Update beliefs with new data

</div>

<div class="card card-accent pad-tight">

## 🎯 **Applications**

Medical diagnosis • Spam filters • Parameter estimation • Hypothesis testing • ML

</div>

</div>

---
hideInToc: true
---

# Example: Medical Test

<div class="card card-warning pad-tight">

## 🏥 **Scenario**

Disease: 1% prevalence • Test: 95% sensitivity, 90% specificity

**Question:** Probability of disease if test is positive?

</div>

<div class="grid-2 mt-md gap-tight">

<div class="card card-primary pad-tight">

## 📊 **Calculation**

$$P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+)}$$

$P(+) = 0.95(0.01) + 0.10(0.99) = 0.1085$

$$P(D \mid +) = \frac{0.0095}{0.1085} \approx \textbf{8.8%}$$

</div>

<div class="card card-accent pad-tight">

## 💡 **Insight**

Only **8.8%** chance despite positive test!

**Why?** Rare disease → false positives (990) >> true positives (95)

</div>

</div>


---
hideInToc: true
---

# Visualizing the Medical Test

```mermaid {scale: .725}
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'secondaryColor': '#102b4c',
  'tertiaryColor': '#0ea5e9',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 45, 'rankSpacing': 60}}%%
flowchart TB
    Pop["👥 Population<br/><span class='text-sm'>10,000 people</span>"]:::hub
    Pop --> Disease["🦠 Disease<br/><span class='mono-strong'>1% → 100</span>"]:::branch
    Pop --> Healthy["💪 No disease<br/><span class='mono-strong'>99% → 9,900</span>"]:::branch

    Disease --> TP["Test +<br/>TP: 95"]:::positive
    Disease --> FN["Test -<br/>FN: 5"]:::negative

    Healthy --> FP["Test +<br/>FP: 990"]:::alert
    Healthy --> TN["Test -<br/>TN: 8,910"]:::positive

    TP --> TotalPos["Total positives<br/><span class='mono-strong'>95 + 990 = 1,085</span>"]:::summary
    FP --> TotalPos

    classDef hub fill:#0b2540,stroke:#60a5fa,stroke-width:2px,color:#e2e8f0,rx:14px,ry:14px;
    classDef branch fill:#132f5d,stroke:#38bdf8,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef positive fill:#0f4c81,stroke:#5eead4,stroke-width:2px,color:#e0f2fe,rx:12px,ry:12px;
    classDef alert fill:#b45309,stroke:#ffb74d,stroke-width:2px,color:#fff7ed,rx:12px,ry:12px;
    classDef negative fill:#8b2f39,stroke:#f87171,stroke-width:2px,color:#fee2e2,rx:12px,ry:12px;
    classDef summary fill:#10223f,stroke:#fbbf24,stroke-width:2px,color:#fde68a,rx:16px,ry:16px;
```

<div class="card card-info pad-tight mermaid-note">

<div class="note-text">

Total positive: 95 + 990 = **1,085** • **P(Disease | +) = 95/1,085 = 8.8%** • False positives dominate when disease is rare

</div>

</div>

---
layout: section
hideInToc: true
---

# Random Variables and Distributions

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **Formal Definition**

A **random variable** $X$ is a function that maps each outcome $\omega$ in the sample space $\Omega$ to a real number:

$$X: \Omega \rightarrow \mathbb{R}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Purpose**

Random variables allow us to:
- Work with numbers instead of abstract outcomes
- Use calculus and algebra
- Define probability distributions
- Calculate expected values and variances

</div>

<div class="card card-secondary pad-tight">

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

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'secondaryColor': '#102b4c',
  'tertiaryColor': '#143860',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 45, 'rankSpacing': 55}}}%%
flowchart TB
    RV["🎲 Random variable X<br/><span class='text-sm'>Maps outcomes → numbers</span>"]:::hub
    RV --> Disc["🔢 Discrete<br/><i>countable outcomes</i>"]:::category
    RV --> Cont["📈 Continuous<br/><i>real-valued range</i>"]:::category

    Disc --> PMF["PMF<br/>P(X = x)"]:::detail
    Disc --> DiscSupport["Support<br/><span class='text-sm'>0, 1, 2, ...</span>"]:::support
    PMF --> DiscEx["Examples<br/><span class='text-sm'>dice · Bernoulli · counts</span>"]:::example

    Cont --> PDF["PDF<br/>f(x)"]:::detail
    Cont --> ContSupport["Support<br/><span class='text-sm'>intervals</span>"]:::support
    PDF --> ContEx["Examples<br/><span class='text-sm'>time · energy · lengths</span>"]:::example

    classDef hub fill:#0b2540,stroke:#60a5fa,stroke-width:2px,color:#f8fafc,rx:14px,ry:14px;
    classDef category fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef detail fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef support fill:#0f2b4c,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:14px,ry:14px;
    classDef example fill:#1d3a64,stroke:#38bdf8,stroke-width:1.5px,color:#e2e8f0,rx:12px,ry:12px;
```


---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="stack-tight" style="margin-top: 0;">

<div class="card card-info pad-tight">

## **Definition**

A random variable $X$ is **discrete** if it can only take countable values (e.g., $0, 1, 2, \ldots$ or a finite set).

</div>

<div class="card card-primary pad-tight">

## **Probability Mass Function**

The PMF $p_X(x)$ or $P(X = x)$ gives the probability that $X$ takes the value $x$.

**Properties:**
1. $P(X = x) \geq 0$ for all $x$
2. $\sum_{\text{all } x} P(X = x) = 1$

**Example:** Number of heads in 3 coin flips

</div>

</div>

<div class="card card-accent pad-tight">

## **Example PMF**

$X$ = number of heads in 3 flips

<div class="text-sm mono-strong mt-sm">

| $x$ | $P(X = x)$ | Calculation |
|-----|------------|-------------|
| 0   | 1/8        | $\binom{3}{0}(0.5)^3$ |
| 1   | 3/8        | $\binom{3}{1}(0.5)^3$ |
| 2   | 3/8        | $\binom{3}{2}(0.5)^3$ |
| 3   | 1/8        | $\binom{3}{3}(0.5)^3$ |

</div>

<div class="meta-caption mt-sm">

$$\sum_{x=0}^{3} P(X = x) = \frac{1+3+3+1}{8} = 1 \quad \checkmark$$

</div>

</div>

</div>

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **Definition**

A random variable $X$ is **continuous** if it can take any value in an interval or union of intervals (uncountably many values).

**Key Insight:** For continuous $X$, $P(X = x) = 0$ for any specific $x$. Only intervals have non-zero probability.

</div>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Probability Density Function (PDF)**

The PDF $f(x)$ is **not** a probability, but a density. Probabilities are computed as:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

**Properties:**
1. $f(x) \geq 0$ for all $x$
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$
3. $P(X = c) = 0$ for any specific $c$

</div>

<div class="card card-accent pad-tight">

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

<div class="card card-info pad-tight mt-md">

## **Definition**

For any random variable $X$ (discrete or continuous), the CDF is:

$$F(x) = P(X \leq x)$$

The CDF gives the probability that $X$ takes a value **at most** $x$.

</div>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Properties**

1. **Non-decreasing:** If $x_1 < x_2$, then $F(x_1) \leq F(x_2)$
2. **Limits:** $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$
3. **Right-continuous:** $\lim_{h \to 0^+} F(x+h) = F(x)$
4. **For continuous $X$:** $F'(x) = f(x)$ (PDF is derivative of CDF)

</div>

<div class="card card-accent pad-tight">

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

<div class="card card-primary pad-tight">

## **Mean (Average)**

- Formula: $\mu = \frac{\sum x_i}{n}$
- Uses every value
- Most familiar summary
- **Sensitive** to outliers

</div>

<div class="card card-secondary pad-tight">

## **Median**

- Middle value after sorting
- Splits data into two halves
- Robust to skew/outliers

</div>

<div class="card card-info pad-tight">

## **Mode**

- Most frequent value(s)
- Good for categorical data
- Can have multiple modes

</div>

</div>

<div class="card card-accent pad-tight mt-md">

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

<div class="grid-3 mt-md gap-tight">

<div class="card card-warning pad-tight">

### 📏 **Range**

$$\text{Range} = \max - \min$$

<div class="meta-caption">Simple but not robust</div>

</div>

<div class="card card-accent pad-tight">

### 📊 **Variance**

$$\sigma^2 = \frac{\sum(x_i - \mu)^2}{n}$$

<div class="meta-caption">Average squared deviation</div>

</div>

<div class="card card-info pad-tight">

### 📈 **Standard Deviation**

$$\sigma = \sqrt{\text{variance}}$$

<div class="meta-caption">Same units as data</div>

</div>

</div>

---
hideInToc: true
---

# Why Variance?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Why square deviations?**

<div class="card-content text-base">
Squaring removes sign, magnifies large misses, and yields smooth functions that work well with calculus/optimization.
</div>

</div>

<div class="card card-info pad-tight">

## **Population vs Sample**

<div class="card-content text-base">
$$
\sigma^2 = \frac{1}{n}\sum (x_i-\mu)^2, \qquad

$$

$$
s^2 = \frac{1}{n-1}\sum (x_i-\bar{x})^2
$$
Bessel’s correction ($n-1$) keeps $s^2$ unbiased.
</div>

</div>


</div>

---
hideInToc: true
---

# Expectation and Variance

<div class="card card-info pad-tight mt-md">

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

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">


## **Variance**

Measures spread around the mean:

$$\text{Var}(X) = E[(X - \mu)^2]$$

**Computational formula:**

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

**Standard deviation:**

$$\sigma = \sqrt{\text{Var}(X)}$$

</div>

<div class="card card-accent pad-tight">

## **Key Properties**

**Linearity of Expectation:**
- $E[aX + b] = aE[X] + b$
- $E[X + Y] = E[X] + E[Y]$ (always!)

**Variance Properties:**
- $\text{Var}(aX + b) = a^2\text{Var}(X)$
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

  (only if $X$ and $Y$ are independent)

</div>

</div>

---
layout: section
hideInToc: true
---

# Common Probability Distributions

---
hideInToc: true
---

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'secondaryColor': '#102b4c',
  'tertiaryColor': '#143860',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 35, 'rankSpacing': 40}}%%
flowchart TB
    Root["Probability distributions"]:::hub
    Root --> Disc["Discrete<br/>countable"]:::category
    Root --> Cont["Continuous<br/>real-valued"]:::category

    Disc --> Bern["Bernoulli<br/>P(X=1)=p"]:::discrete
    Disc --> Binom["Binomial<br/>n trials"]:::discrete
    Disc --> Pois["Poisson<br/>rare events"]:::discrete

    Cont --> Unif["Uniform<br/>[a,b]"]:::continuous
    Cont --> Exp["Exponential<br/>wait time"]:::continuous
    Cont --> Norm["Normal<br/>μ, σ"]:::continuous

    classDef hub fill:#0b2540,stroke:#60a5fa,stroke-width:2px,color:#f8fafc,rx:14px,ry:14px;
    classDef category fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef discrete fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e0f2fe,rx:12px,ry:12px;
    classDef continuous fill:#155e75,stroke:#5eead4,stroke-width:2px,color:#e0f2fe,rx:12px,ry:12px;
```

---
hideInToc: true
---

# Discrete Distributions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Bernoulli (1 trial)**

- Outcome: success (1) or failure (0)
- Parameter: $p = P(X = 1)$
- Mean $= p$, variance $= p(1-p)$
- Building block for discrete models

</div>

<div class="card card-secondary pad-tight">

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

<div class="card card-primary pad-tight">

## **When to use**

- Counting rare events in fixed interval
- Events occur independently
- Constant average rate $\lambda$

## **PMF**
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

<div class="meta-caption mt-sm">Parameter $\lambda$ = expected count.</div>

</div>

<div class="card card-info pad-tight">

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

<div class="card card-primary pad-tight">

## **Uniform Distribution**

- Support: $[a,b]$
- $f(x) = \tfrac{1}{b-a}$ (flat)
- $E[X] = \tfrac{a+b}{2}$
- $\text{Var}(X) = \tfrac{(b-a)^2}{12}$

</div>

<div class="card card-secondary pad-tight">

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

<div class="card card-primary pad-compact">
<div class="emoji-xl">🏆</div>
<div class="meta-strong">Most Important</div>
</div>

<div class="card card-secondary pad-compact">
<div class="emoji-xl">🌿</div>
<div class="meta-strong">Arises Naturally</div>
</div>

<div class="card card-info pad-compact">
<div class="emoji-xl">🎯</div>
<div class="meta-strong">CLT Foundation</div>
</div>

<div class="card card-success pad-compact">
<div class="emoji-xl">🔬</div>
<div class="meta-strong">Measurement Errors</div>
</div>

<div class="card card-warning pad-compact">
<div class="emoji-xl">🧪</div>
<div class="meta-strong">Statistical Tests</div>
</div>

<div class="card card-accent pad-compact">
<div class="emoji-xl">⚙️</div>
<div class="meta-strong">Two Parameters: μ, σ²</div>
</div>

</div>

<div style="text-align: center; font-size: 1.1em; font-weight: bold; margin-top: 1.5rem;">

🌟 **"The normal distribution is the pattern of patterns"**

</div>

---
hideInToc: true
---

# Normal Distribution

<div class="card card-info pad-tight mt-md">

## **Probability Density Function**

A random variable $X$ follows a **normal (Gaussian) distribution** with parameters $\mu$ (mean) and $\sigma^2$ (variance), written $X \sim N(\mu, \sigma^2)$, if:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad -\infty < x < \infty$$

</div>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Key Properties**

1. **Symmetric** about $\mu$
2. **Bell-shaped** (unimodal)
3. **Mean = Median = Mode = $\mu$**
4. **Inflection points** at $x = \mu \pm \sigma$
5. **Area under curve = 1**
6. **Asymptotic**: tails approach (but never reach) zero

</div>

<div class="card card-accent pad-tight">

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



<div class="grid-3 gap-tight">

<div class="card card-success pad-balanced text-center">
<div class="text-xl-strong">📊 68%</div>
<div class="note-text mt-xs">$\mu \pm \sigma$</div>
</div>

<div class="card card-info pad-balanced text-center">
<div class="text-xl-strong">📈 95%</div>
<div class="note-text mt-xs">$\mu \pm 2\sigma$</div>
</div>

<div class="card card-primary pad-balanced text-center">
<div class="text-xl-strong">🎯 99.7%</div>
<div class="note-text mt-xs">$\mu \pm 3\sigma$</div>
</div>

</div>

<div class="card card-warning pad-balanced" style="margin-top: 1.2rem;">

### 💡 **Practical Implication**

<div class="note-text mt-xs">

$3\sigma$ measurement = extremely rare (0.3%)

⚛️ **Physics**: $5\sigma$ = gold standard (1 in 3.5M)

</div>

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

<div class="card card-info pad-tight mt-md">

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

<div class="card card-info pad-tight mt-md">

Or equivalently, the standardized sum converges in distribution to $N(0,1)$:

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

</div>


<div class="card card-primary pad-tight mt-md">

## **Key Insights**

- Works for **any** underlying distribution (not just normal!)
- Larger $n$ → better approximation
- Standard error: $SE = \sigma/\sqrt{n}$ decreases with $\sqrt{n}$
- Rule of thumb: $n \geq 30$ often sufficient for good approximation

</div>

---
hideInToc: true
---

# Why CLT Matters

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Why we rely on it**

- Measurement errors = many tiny effects → approximate normal
- Sampling distributions of means trend toward normal even if raw data are skewed
- Confidence intervals & hypothesis tests assume normality via CLT

</div>

<div class="card card-secondary pad-tight">

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

<div class="grid-3 mt-md gap-tight">

<div class="card card-primary pad-balanced">

### 📐 **Definition**

$$SE = \frac{\sigma}{\sqrt{n}}$$

<div class="meta-caption">Std dev of sample mean</div>

</div>

<div class="card card-warning pad-balanced">

### 🔍 **Interpretation**

<div class="text-tight">

📊 Uncertainty in $\mu$

📉 Decreases as $\sqrt{n}$

🔢 Halve error: $4\times$ data

</div>

</div>

<div class="card card-success pad-balanced">

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

# Estimation

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Point Estimation**

- Single best guess for a parameter
- $\bar{x}$ estimates $\mu$
- $s^2$ estimates $\sigma^2$
- Deterministic function of the data

</div>

<div class="card card-secondary pad-tight">

## **Interval Estimation**

- Range of plausible parameter values
- Confidence interval (CI) contains true value with chosen probability (e.g., 95%)
- Communicates both estimate and uncertainty

</div>

<div class="card card-info pad-tight">

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

<div class="card card-primary pad-tight">

## **Idea**

Pick parameter values $\theta$ that make the observed data most probable.

</div>

<div class="card card-secondary pad-tight">

## **Likelihood Function**

$L(\theta \mid \text{data}) = P(\text{data} \mid \theta)$

- Independent observations: $L(\theta) = \prod f(x_i; \theta)$
- Often easier to work with $\log L(\theta)$ (turns products into sums)

</div>

<div class="card card-info pad-tight">

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

<div class="card card-primary pad-tight">

## **Setup**

- Observations $x_1, \ldots, x_n$
- Model: $X_i \sim N(\mu, \sigma^2)$ with known $\sigma$
- Likelihood: $L(\mu) = \prod \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x_i-\mu)^2}{2\sigma^2}\right)$

## **Result**

$\hat{\mu} = \bar{x}$ (sample mean) maximizes $L(\mu)$.

</div>

<div class="card card-info pad-tight">

## **Why this matters**

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

# Connecting to Data Fitting

---
hideInToc: true
---

# Data Fitting Workflow

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'secondaryColor': '#102b4c',
  'tertiaryColor': '#143860',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 28, 'rankSpacing': 32}}%%
flowchart LR
    Data["Data<br/>(xᵢ, yᵢ)"]:::input --> Model["Model<br/>y = f(x; θ) + ε"]:::process
    Model --> Method{"Method?"}:::decision
    Method --> LS["Least sq"]:::option
    Method --> MLE["MLE"]:::option
    Method --> Chi["χ²"]:::option

    LS --> Fit
    MLE --> Fit
    Chi --> Fit
    Fit["Fit<br/>θ̂"]:::process --> Uncertainty["Uncertainty<br/>SEs, CIs"]:::process
    Uncertainty --> Diagnostics["Diagnostics<br/>χ², residuals"]:::process
    Diagnostics --> Decision{"Good?"}:::decision
    Decision -->|Yes| Report["Report<br/>θ̂ ± error"]:::output
    Decision -->|No| Model
    Report --> Predict["Predict<br/>f(x_new; θ̂)"]:::output

    classDef input fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef process fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px;
    classDef decision fill:#0b2540,stroke:#fcd34d,stroke-width:2px,color:#fef3c7,rx:14px,ry:14px;
    classDef option fill:#155e75,stroke:#5eead4,stroke-width:2px,color:#e0f2fe,rx:10px,ry:10px;
    classDef output fill:#1c3d5a,stroke:#5eead4,stroke-width:2px,color:#e0f2fe,rx:12px,ry:12px;
```

---
hideInToc: true
---

# From Probability to Fitting

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Data fitting problem**

- Observations $(x_i, y_i)$
- Model relationship $y = f(x; \theta) + \varepsilon$
- Goal: pick $\theta$ that best explains the data

</div>

<div class="card card-secondary pad-tight">

## **Statistical foundation**

- Errors modeled as random (often normal)
- Estimate $\theta$ via least squares / MLE
- Quantify uncertainty (SEs, CIs, $\chi^2$)
- Diagnose fit quality before trusting results

<div class="meta-caption mt-sm">Next: apply these ideas to concrete fitting workflows.</div>

</div>

</div>

---
hideInToc: true
---

# Least Squares = MLE (for normal errors)

<div class="card card-primary pad-tight mt-md">

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

<div class="card card-info pad-tight mt-md">

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

# Common Mistakes and Pitfalls

<div class="grid-2 mt-md gap-md">

<div class="stack-tight" style="margin-top: 0;">

<div class="card card-primary pad-tight">

## **Probability vs Statistics**

<div class="card-content text-base">
Probability starts with a model and reasons forward to the data, while statistics starts with data and works backward to infer or validate a model. Treating them as the same step often leads to incorrect intuition.
</div>

</div>

<div class="card card-warning pad-tight">

## **p-hacking**

<div class="card-content text-base">
Running many tests until one looks “significant” inflates false positives. Pre-register analyses and adjust for multiple comparisons to keep results honest.
</div>

</div>

</div>

<div class="stack-tight" style="margin-top: 0;">

<div class="card card-secondary pad-tight">

## **Misreading Confidence Intervals**

<div class="card-content text-base">
A 95% confidence interval does not mean “95% chance the parameter lies here.” It means that, across repeated experiments, the method produces intervals that contain the true value about 95% of the time.
</div>

</div>

<div class="card card-accent pad-tight">

## **Extrapolation**

<div class="card-content text-base">
Models are trustworthy only within the range where they were calibrated. Predictions far outside that range should be treated with caution (or new data).
</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Practical Advice

<div class="grid-3 mt-lg">

<div class="card card-primary pad-tight">

## 📊 **Visualize**

<div class="card-content text-base">

Visualize data first

</div>

</div>

<div class="card card-secondary pad-tight">

## ✓ **Check**

<div class="card-content text-base">

Verify assumptions

</div>

</div>

<div class="card card-info pad-tight">

## 📏 **Report**

<div class="card-content text-base">

Include uncertainties

</div>

</div>

<div class="card card-success pad-tight">

## 🎯 **Understand**

<div class="card-content text-base">

Know p-values

</div>

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Caution**

<div class="card-content text-base">

Small sample limits

</div>

</div>

<div class="card card-accent pad-tight">

## 🔬 **Simulate**

<div class="card-content text-base">

When unclear

</div>

</div>

<div class="card card-primary pad-tight" style="grid-column: 1 / -1;">

## 📝 **Document for Reproducibility**

</div>

</div>
