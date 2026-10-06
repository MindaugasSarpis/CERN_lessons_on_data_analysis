---
layout: cover
title: "Probability & Statistics"
# slidev-addon-python-runner reads this block from slide 1 = this cover (see CLAUDE.md)
python:
  installs: ["numpy"]
  prelude: |
    import numpy as np
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Probability and Statistics

##### <span class="aims-badge">🔧 tool-agnostic · ♻️ reproducibility</span>

<!--
Speaker: the lecture is one chain of derivations. Each result is used by the
next one: the rules of probability give the binomial, its limit gives the
Poisson, sums give the Gaussian, the variance of a sum gives the standard
error and error propagation, and the Gaussian gives the likelihood of a mean.
Keep a pen and the board ready. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The main goal of this lecture is to derive how a quantity that comes out differently every time is described: by **probability**, by a **distribution**, by the **uncertainty** of a mean and of a computed result, and by the **likelihood**

---
hideInToc: true
---

# One Quantity, **91 583 Values**

<img class="fig" src="/figures/viz_handson_mass_errorbars.svg" style="display:block;margin:0 auto;max-height:250px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The figure of Lecture 08**

Column `M` of `D0_KPi.csv`, one K⁻π⁺ candidate per row, in bins of 1 MeV/c². Every bin carries a bar of ± √N: 1916 ± 44 at the top, about 700 ± 26 in the flat part. The bar was drawn, not derived.

</div>

<div class="card card-secondary card-glass pad-compact">

## ❓ **Four questions**

- Which one number stands for all 91 583 values?
- How far from it does a single value lie?
- How well is that one number known?
- Why is the bar on a count exactly √N?

</div>

</div>

<!--
Speaker: last week's figure, made by the errorbar call of Lecture 08. The same
quantity was computed for 91 583 candidates, and the values differ from row to
row. Ask the room for a guess at the first answer before going on. The four
answers are the mean, the standard deviation, the standard error and the
Poisson distribution of a count. All four are derived today, and the last
slide of the lecture collects them. (~2 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🎲 Compute with **probabilities**: the addition rule, conditional probability, independence, Bayes' theorem

</div>

<div class="card card-secondary card-glass pad-compact">

📊 Say where the **binomial**, the **Poisson** and the **Gaussian** distribution come from, and attach √N to a count

</div>

<div class="card card-accent card-glass pad-compact">

📏 Compute a **mean**, a **standard deviation** and the **standard error** σ/√N, and say which is which

</div>

<div class="card card-success card-glass pad-compact">

🧮 **Propagate** uncertainties through a formula, and write a result with its uncertainty

</div>

<div class="card card-warning card-glass pad-compact">

🎯 Write down a **likelihood** and find its maximum: the mean, and the weighted mean

</div>

</div>

<!--
Speaker: five results, each derived today and each computed on the two files
the room already has: the mass column of D0_KPi.csv and the pendulum table.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Probability and Its **Rules**

Before the bar of ± √N can be derived, a probability has to be defined, and its rules derived from three axioms.

<!--
Speaker: the section defines probability as a frequency, on a die, and derives
the rules the rest of the lecture uses: complement, addition, conditional
probability, independence, Bayes. Independence is then tested on two columns
of the file. (~1 min)
-->

---
hideInToc: true
---

# Probability as a Long-Run **Frequency**

<div class="card card-info card-glass pad-compact mt-sm">

An experiment is repeated $n$ times. The event $A$ occurs in $n_A$ of them. The probability of $A$ is the value at which the fraction settles: $P(A) = \lim\limits_{n \to \infty} n_A / n$. It lies between 0 (never) and 1 (always).

</div>

<img class="fig mt-sm" src="/figures/viz_probability_frequency.svg" style="display:block;margin:0.6rem auto 0;max-height:235px;">

<div class="note-text mt-sm">

A die rolled a million times in NumPy, with the fraction of sixes drawn after every roll. For an event that cannot be repeated, such as rain tomorrow, a probability is read as a degree of belief. The rules are the same for both readings.

</div>

<!--
Speaker: before the next slide, ask the room: what fraction of sixes do ten
rolls give, and how close to 1/6 is the fraction after a million? Write two or
three guesses on the board; the next slide runs it. The frequency reading is
the one a physicist uses for a measurement that can be repeated. The
degree-of-belief reading is the Bayesian one. Nothing derived today depends on
which reading is taken. (~2 min)
-->

---
hideInToc: true
---

# The Frequency of a Six, **Simulated**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Rolls $n$ | 10 | 100 | 1000 | 10 000 | 100 000 | 1 000 000 |
| --- | --- | --- | --- | --- | --- | --- |
| Fraction of sixes | 0.2 | 0.16 | 0.162 | 0.1658 | 0.16636 | 0.166538 |
| Fraction − 1/6 | +0.033 | −0.007 | −0.005 | −0.0009 | −0.0003 | −0.0001 |

</div>

```python {monaco-run} {autorun:false}
rng = np.random.default_rng(1)
rolls = rng.integers(1, 7, 1_000_000)        # one million rolls
for n in [10, 100, 1000, 10_000, 100_000, 1_000_000]:
    print(n, (rolls[:n] == 6).mean())        # fraction of sixes in the first n
```

<div class="note-text mt-sm">

`default_rng` is the seeded generator of Lecture 08, here with the seed 1. The seed fixes the whole sequence, so every laptop rolls the same million. `integers(1, 7, n)` includes 1 and excludes 7. `rolls == 6` is a mask, and its mean is the fraction of `True`. A hundred times more rolls bring the fraction about ten times closer to 1/6.

</div>

<!--
Speaker: run it, and compare with the guesses on the board: ten rolls gave
0.2, a million 0.1665. Run it again: the same numbers. Change the seed to 2:
other numbers, the same pattern. A result that depends on random numbers is
reproducible only if the seed is written down. Then ask for the pattern in the
last row: two more zeros in n, one more zero in the difference. That is a
square root, and the section on the standard error derives it. (~3 min)
-->

---
hideInToc: true
---

# Outcomes and **Events**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **One roll of a die**

- An **outcome** is what one repetition gives: a number from 1 to 6
- The **sample space** Ω is the set of all outcomes: {1, 2, 3, 4, 5, 6}
- An **event** is a set of outcomes. $A$ = "even" = {2, 4, 6}. $B$ = "more than 4" = {5, 6}
- The six outcomes are equally likely, so $P(\text{event})$ = outcomes in it / 6

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔗 **Events combined**

| Event | Outcomes | Probability |
| --- | --- | --- |
| $A$ | {2, 4, 6} | 3/6 = 1/2 |
| $B$ | {5, 6} | 2/6 = 1/3 |
| $A$ and $B$: $A \cap B$ | {6} | 1/6 |
| $A$ or $B$: $A \cup B$ | {2, 4, 5, 6} | 4/6 = 2/3 |
| not $A$: $A^c$ | {1, 3, 5} | 3/6 = 1/2 |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ $P(A \cup B)$ is not $P(A) + P(B)$: 1/2 + 1/3 = 5/6 counts the outcome 6 twice. The correct rule follows from three axioms.

</div>

<!--
Speaker: "or" in probability includes "both". Let the room list A ∪ B before
showing it. (~2 min)
-->

---
hideInToc: true
---

# Three **Axioms**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 1️⃣ **Not negative**

$$P(A) \geq 0$$

for every event $A$

</div>

<div class="card card-secondary card-glass pad-tight">

## 2️⃣ **Something happens**

$$P(\Omega) = 1$$

Ω holds every outcome

</div>

<div class="card card-accent card-glass pad-tight">

## 3️⃣ **Exclusive events add**

$$P(A \cup B) = P(A) + P(B)$$

if $A$ and $B$ share no outcome

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact">

## 📏 **A frequency obeys them**

A fraction $n_A/n$ is never negative. The fraction of "any outcome" is $n/n = 1$. The counts of two events that share no outcome add, and so do their fractions.

</div>

<div class="card card-success card-glass pad-compact">

## 🧮 **Equally likely outcomes**

$N$ outcomes with the same probability $q$ share no outcome and together make Ω. Axioms 3 and 2 give $Nq = 1$, so $q = 1/N$. An event of $m$ outcomes has the probability $m/N$: the counting used for the die.

</div>

</div>

<div class="note-text mt-sm">

Kolmogorov wrote the three axioms down in 1933. Every other rule of probability is derived from them.

</div>

<!--
Speaker: these are the only statements of the lecture that are not derived.
Everything after this slide is. (~2 min)
-->

---
hideInToc: true
---

# Two Rules, **Derived**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔄 **The complement**

$A$ and "not $A$" share no outcome, and together they are Ω. Axioms 3 and 2 give

$$P(A) + P(A^c) = P(\Omega) = 1$$

$$P(A^c) = 1 - P(A)$$

Not a six: 1 − 1/6 = 5/6.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➕ **The addition rule**

Cut $A \cup B$ into three parts that share no outcome: only $A$, only $B$, both. $P(A) + P(B)$ counts the part "both" twice, so it is taken off once:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

The die: 1/2 + 1/3 − 1/6 = 2/3.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

In the million simulated rolls the fractions are 0.5003 for "even", 0.3334 for "more than 4", 0.1665 for both and 0.6672 for either: 0.5003 + 0.3334 − 0.1665 = 0.6672. The complement is the rule used most. "At least one" is hard to count directly and easy as 1 − $P$(none).

</div>

<!--
Speaker: draw the two overlapping circles on the board and shade the three
parts. (~2 min)
-->

---
hideInToc: true
---

# Conditional **Probability**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Given that B occurred**

Only the outcomes in $B$ remain possible. Of these, the ones that are also in $A$ count:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Read the other way, it is the **product rule**:

$$P(A \cap B) = P(A \mid B)\,P(B)$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎲 **Two dice, 36 equally likely pairs**

- $A$: the sum is 8. Five pairs: (2,6), (3,5), (4,4), (5,3), (6,2). $P(A)$ = 5/36 = 0.139
- $B$: the first die shows 3. Six pairs. $P(B)$ = 6/36
- $A \cap B$: only (3,5). $P(A \cap B)$ = 1/36
- $P(A \mid B)$ = (1/36) / (6/36) = 1/6 = 0.167

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Knowing that the first die shows 3 raises the probability of a sum of 8 from 0.139 to 0.167. Had it shown 1, the probability would be 0.

</div>

<!--
Speaker: conditioning is a smaller sample space. Count inside B only: six
pairs, one of them gives 8. (~2 min)
-->

---
hideInToc: true
---

# **Independence**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔀 **B changes nothing**

$A$ and $B$ are independent if $P(A \mid B) = P(A)$. The product rule then becomes

$$P(A \cap B) = P(A)\,P(B)$$

- Two dice: $P$(six and six) = 1/6 × 1/6 = 1/36
- "Sum is 7" and "first die shows 3" are independent: 1/6 with and without the condition
- "Sum is 8" and "first die shows 3" are not: 0.167 against 0.139

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **Repetitions multiply**

For $n$ independent repetitions the probabilities multiply. No six in 4 rolls:

$$\left(\tfrac{5}{6}\right)^4 = 0.482$$

At least one six in 4 rolls, by the complement:

$$1 - 0.482 = 0.518$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Independence is a statement about the experiment: one roll does not influence the next, one particle does not influence the next. Every distribution in this lecture is built on it.

</div>

<!--
Speaker: "at least one six in four rolls" is the bet of the Chevalier de Méré,
1654, the problem that started probability theory. It is a little better than
even. (~2 min)
-->

---
hideInToc: true
---

# Independence, Tested on the **File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **Two events for one row**

```python
M, PT = np.loadtxt("data/raw/D0_KPi.csv",
                   delimiter=",", skiprows=1,
                   usecols=(0, 1), unpack=True)
W = (M > 1855) & (M < 1875)   # in the peak window
H = PT > np.median(PT)        # PT in the upper half
print(W.mean(), H.mean())
print((W & H).mean())
print((W & H).sum() / H.sum())
```

```text
0.33993208346527193 0.4999945404714849
0.2012928163523798
0.4025900286082418
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔀 **The product rule, checked**

| | Probability |
| --- | --- |
| $P(W)$ | 0.340 |
| $P(H)$ | 0.500 |
| $P(W)\,P(H)$, if independent | 0.170 |
| $P(W \cap H)$, counted | 0.201 |
| $P(W \mid H)$ | 0.403 |
| $P(W \mid \text{not } H)$ | 0.277 |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The two events are not independent. Among the rows with a high `PT`, 40 % lie in the peak window; among the others, 28 %. The rows of the file are of two kinds, and a high `PT` makes the kind that forms the peak more likely.

</div>

<!--
Speaker: ask first: does knowing PT change the chance that a row lies in the
peak? Most say no: a momentum and a mass are different things. If W and H were
independent, 0.340 × 0.5 = 0.170 of the rows, 15 566, would be in both. The
file has 18 435. unpack=True and the masks are from Lecture 07; the median
of PT, 3049 MeV/c, splits the rows into two halves, so P(H) is 0.5 by
construction. (~3 min)
-->

---
hideInToc: true
---

# Bayes' **Theorem**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔄 **Two lines**

The product rule, written for $A$ given $B$ and for $B$ given $A$:

$$P(A \mid B)\,P(B) = P(A \cap B) = P(B \mid A)\,P(A)$$

Divide by $P(B)$:

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **What it is for**

- $P(B \mid A)$ is often what is known: the probability of this result if the hypothesis holds
- $P(A \mid B)$ is what is asked: the probability of the hypothesis, given the result
- The two are different numbers

$B$ occurs either with $A$ or without it:

$$P(B) = P(B \mid A)\,P(A) + P(B \mid A^c)\,P(A^c)$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The names: $P(A)$ is the **prior** probability of the hypothesis, before the result is known, and $P(A \mid B)$ the **posterior** probability, after it. The theorem says how much a result changes what is known.

</div>

<!--
Speaker: the theorem turns a conditional probability round. The next slide
puts numbers in. (~2 min)
-->

---
hideInToc: true
---

# Bayes' Theorem: a **Test**

<div class="card card-warning card-glass pad-compact mt-sm">

1 % of a population has a disease. A test is positive for 95 % of the sick and for 10 % of the healthy. A person tests positive. How probable is the disease?

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 👥 **By counting: 10 000 people**

| | Positive | Negative |
| --- | --- | --- |
| 100 sick | 95 | 5 |
| 9900 healthy | 990 | 8910 |
| all | 1085 | 8915 |

Of 1085 positive tests, 95 are sick: 95 / 1085 = 0.088.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **By the theorem**

$$P(D \mid +) = \frac{0.95 \times 0.01}{0.95 \times 0.01 + 0.10 \times 0.99}$$

$$= \frac{0.0095}{0.1085} = 0.088$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

8.8 %, not 95 %. The healthy are 99 times as many as the sick, so their false positives outnumber the true positives: 990 against 95.

</div>

<!--
Speaker: ask for a guess before showing the table. Most say 95 %. 95 % is
P(positive | sick). The patient asks for P(sick | positive). (~3 min)
-->

---
layout: section
hideInToc: true
---

# Random **Variables**

The rules give the probability of an event. A count or a mass is a number, so each outcome now gets a number, and the numbers get a mean and a spread.

<!--
Speaker: from events to numbers. A distribution, its mean and its variance,
and the two rules for sums that carry the rest of the lecture. (~1 min)
-->

---
hideInToc: true
---

# A Random Variable and Its **Distribution**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **A number for each outcome**

A random variable $X$ assigns a number to every outcome. $X$ = the sum of two dice: the pair (3,5) gives $X$ = 8.

Its **distribution** lists each value $x$ with its probability $P(x)$, here the number of pairs out of 36:

| $x$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairs | 1 | 2 | 3 | 4 | 5 | 6 | 5 | 4 | 3 | 2 | 1 |

The probabilities add up to 36/36 = 1.

$X$ is the variable, $x$ one of its values. A variable with separate values, such as a count, is called **discrete**.

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_two_dice.svg" style="display:block;margin:0 auto;max-height:285px;">

</div>

</div>

<!--
Speaker: the distribution is the full description of X. The next two slides
compress it into two numbers. (~2 min)
-->

---
hideInToc: true
---

# The Expected **Value**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➗ **The average of many repetitions**

In $n$ repetitions the value $x$ occurs $n_x$ times. The average of all $n$ results is

$$\frac{1}{n}\sum_x x\,n_x = \sum_x x\,\frac{n_x}{n} \;\longrightarrow\; \sum_x x\,P(x)$$

The limit is the **expected value**, or mean, of $X$:

$$\mu = E[X] = \sum_x x\,P(x)$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎲 **In numbers**

- One die: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
- 3.5 is not a possible roll. It is the average of many rolls
- The sum of two dice: (2×1 + 3×2 + … + 12×1) / 36 = 252 / 36 = 7
- 100 000 simulated pairs of dice give an average of 7.007

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Each value is weighted by its probability. The expected value is the centre of mass of the distribution.

</div>

<!--
Speaker: the step in the first formula is the definition of probability from
the first section: n_x / n tends to P(x). (~2 min)
-->

---
hideInToc: true
---

# Variance and Standard **Deviation**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **The mean squared distance from μ**

$$\sigma^2 = \mathrm{Var}(X) = E\big[(X-\mu)^2\big] = \sum_x (x-\mu)^2\,P(x)$$

The **standard deviation** $\sigma$ is its square root. It has the unit of $X$.

Expanding the square gives a shorter way to compute it:

$$E\big[(X-\mu)^2\big] = E[X^2] - 2\mu\,E[X] + \mu^2 = E[X^2] - \mu^2$$

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🎲 **One die, μ = 3.5**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| $x - \mu$ | −2.5 | −1.5 | −0.5 | 0.5 | 1.5 | 2.5 |
| $(x-\mu)^2$ | 6.25 | 2.25 | 0.25 | 0.25 | 2.25 | 6.25 |

- $\sigma^2$ = 17.5 / 6 = 2.917
- $\sigma$ = 1.708
- The shorter way: $E[X^2]$ = 91/6 = 15.167, and 15.167 − 3.5² = 2.917

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The distances are squared so that those below and above the mean do not cancel. The price is the unit: the variance of a time is in s². The standard deviation brings the unit back.

</div>

<!--
Speaker: do the die on the board. The average of the bottom row is the
variance. (~3 min)
-->

---
hideInToc: true
---

# Sums of Random **Variables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **The mean of a sum**

$$E[X + Y] = E[X] + E[Y]$$

$$E[aX + b] = a\,E[X] + b$$

Both hold always, also when $X$ and $Y$ depend on each other.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **The variance of a sum**

Write $\Delta X = X - \mu_X$ and $\Delta Y = Y - \mu_Y$.

$$\mathrm{Var}(X+Y) = E\big[(\Delta X + \Delta Y)^2\big]$$

$$= \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,E[\Delta X\,\Delta Y]$$

$E[\Delta X\,\Delta Y]$ is the **covariance** $\mathrm{Cov}(X, Y)$. It is 0 for independent variables.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**For independent variables the variances add**, and a factor comes out squared. Every uncertainty derived today follows from these two rules:

$$\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y), \qquad \mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$$

Two dice: mean 3.5 + 3.5 = 7, variance 2.917 + 2.917 = 5.833, $\sigma$ = 2.415. Standard deviations do not add: 1.708 + 1.708 = 3.416 is wrong.

</div>

<!--
Speaker: the two rules in the bottom card are used again for the binomial,
for the standard error, for error propagation and for the weighted mean. A
simulation of 100 000 pairs of dice with default_rng(2) gives a mean of 7.007
and a variance of 5.804. Ask: if the standard deviations added, what would
the spread of the sum be? 3.416, against the 2.415 that the simulation
confirms. (~3 min)
-->

---
hideInToc: true
---

# Continuous Variables: **Density**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **Probability is an area**

A mass or a time can take any value in an interval. One exact value has probability 0. A **density** $f(x)$ gives the probability of an interval:

$$P(a \le X \le b) = \int_a^b f(x)\,dx, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1$$

The sums become integrals:

$$\mu = \int x\,f(x)\,dx, \qquad \sigma^2 = \int (x-\mu)^2 f(x)\,dx$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **The uniform density on [0, 1]**

$f(x) = 1$ inside the interval and 0 outside. `rng.random()` draws from it.

- $P(0.2 \le X \le 0.5)$ = 0.3

$$\mu = \int_0^1 x\,dx = \tfrac{1}{2}$$

$$\sigma^2 = \int_0^1 x^2\,dx - \mu^2 = \tfrac{1}{3} - \tfrac{1}{4} = \tfrac{1}{12}$$

- $\sigma$ = 0.289

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A density is not a probability. Its unit is 1 over the unit of $x$, and it can exceed 1: the uniform density on [0, 0.5] is 2. A histogram of $N$ values with bin width $\Delta x$ shows about $N f(x)\,\Delta x$ values per bin.

</div>

<!--
Speaker: the last sentence is how a density is drawn over a histogram: multiply
it by the number of values and by the bin width. The mean 1/2 and the variance
1/12 of the uniform density are used again in the simulation of sums. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Three **Distributions**

For independent variables the means add and the variances add. Applied to independent trials, these two rules give the binomial, the Poisson and the Gaussian distribution.

<!--
Speaker: the binomial from independent trials, the Poisson as its limit, the
Gaussian as the limit of sums. Each is derived, then checked in numbers.
(~1 min)
-->

---
hideInToc: true
---

# Independent Trials: **Counting**

<div class="card card-info card-glass pad-compact mt-sm">

A trial has two results: success, with probability $p$, or failure, with $1 - p$. There are $n$ independent trials. How probable are exactly $k$ successes?

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 3️⃣ **Three trials, written out**

| $k$ | Sequences | Each has | Number |
| --- | --- | --- | --- |
| 3 | SSS | $p^3$ | 1 |
| 2 | SSF, SFS, FSS | $p^2(1-p)$ | 3 |
| 1 | SFF, FSF, FFS | $p\,(1-p)^2$ | 3 |
| 0 | FFF | $(1-p)^3$ | 1 |

The eight sequences share no outcome, so their probabilities add. The total is $(p + 1 - p)^3 = 1$.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✌️ **Two steps**

1. **Independence.** One given sequence with $k$ successes has probability $p^k(1-p)^{n-k}$, in any order
2. **Counting.** The $k$ successes can be placed in ${n(n-1)\cdots(n-k+1)}$ ordered ways. Each set of places is counted $k!$ times:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

</div>

</div>

<!--
Speaker: check the count on the table: 3! / (2! 1!) = 3 sequences with two
successes. S is a success, F a failure. (~3 min)
-->

---
hideInToc: true
---

# The **Binomial** Distribution

<div class="card card-info card-glass pad-compact mt-sm">

The probability of one sequence times the number of sequences:

$$P(k) = \binom{n}{k}\,p^k\,(1-p)^{n-k}, \qquad k = 0, 1, \dots, n$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔬 **A detector with p = 0.9, ten particles**

| Registered $k$ | 10 | 9 | 8 | 7 or fewer |
| --- | --- | --- | --- | --- |
| $P(k)$ | 0.349 | 0.387 | 0.194 | 0.070 |

- $P(10)$ = 0.9¹⁰ = 0.349
- $P(9)$ = 10 × 0.9⁹ × 0.1 = 0.387

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **Where it applies**

- A fixed number $n$ of trials
- Two results per trial
- The same $p$ in every trial
- Trials that do not influence each other

The rows of a file that pass a selection, the particles a detector registers, the heads in $n$ coin flips.

</div>

</div>

<div class="note-text mt-sm">

A detector that registers nine particles in ten sees all ten of a group in only 35 % of the cases.

</div>

<!--
Speaker: the probability p of a detector is called its efficiency. The four
numbers of the table add up to 1.000. (~2 min)
-->

---
hideInToc: true
---

# The Binomial: **Mean and Variance**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **One trial**

$X$ = 1 for a success, 0 for a failure.

$$E[X] = 1 \cdot p + 0 \cdot (1-p) = p$$

$X^2 = X$, so $E[X^2] = p$ and

$$\mathrm{Var}(X) = E[X^2] - p^2 = p\,(1-p)$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **n trials**

The count is a sum of independent trials, $k = X_1 + \dots + X_n$. By the rules for sums, means add and variances add:

$$E[k] = np$$

$$\mathrm{Var}(k) = np\,(1-p), \qquad \sigma = \sqrt{np\,(1-p)}$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The detector with $p$ = 0.9: of 10 particles it registers 9 ± 0.95, of 1000 particles 900 ± 9.5. The mean grows like $n$ and the spread like $\sqrt{n}$, so the relative spread falls like $1/\sqrt{n}$: 10.5 % for 10 particles, 1.05 % for 1000.

</div>

<!--
Speaker: no sum over binomial coefficients is needed. The rules for the mean
and the variance of a sum do the work. (~2 min)
-->

---
hideInToc: true
---

# From Binomial to **Poisson**

<div class="card card-info card-glass pad-compact mt-sm">

Many trials, each with a small probability: $n \to \infty$ and $p \to 0$, with the mean $\lambda = np$ held fixed. Put $p = \lambda/n$ into the binomial:

$$P(k) = \frac{n(n-1)\cdots(n-k+1)}{n^k}\;\frac{\lambda^k}{k!}\;\left(1-\frac{\lambda}{n}\right)^{n}\left(1-\frac{\lambda}{n}\right)^{-k}$$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **First factor → 1**

$k$ factors, $\frac{n}{n}\cdot\frac{n-1}{n}\cdots$, each close to 1 when $n$ is much larger than $k$

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Third factor → e<sup>−λ</sup>**

For $\lambda$ = 3: 0.0282 for $n$ = 10, 0.0476 for 100, 0.0496 for 1000. $e^{-3}$ = 0.0498

</div>

<div class="card card-accent card-glass pad-compact">

## 3️⃣ **Last factor → 1**

$k$ is fixed and $\lambda/n \to 0$

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

What remains is the **Poisson distribution**, with one parameter:

$$P(k) = \frac{\lambda^k}{k!}\,e^{-\lambda}, \qquad k = 0, 1, 2, \dots$$

</div>

<!--
Speaker: the limit of (1 − λ/n)^n is the definition of the exponential
function. n and p have disappeared: only their product is left. (~3 min)
-->

---
hideInToc: true
---

# The Limit in **Numbers**

<img class="fig" src="/figures/viz_probability_binomial_poisson.svg" style="display:block;margin:0 auto;max-height:285px;">

<div class="card card-info card-glass pad-compact mt-md">

The bars are the binomial distribution, the points the Poisson distribution with $\lambda$ = 3. The mean $np$ is 3 in every panel. With $n$ = 10 the two differ by up to 0.04. With $n$ = 1000 the largest difference is 0.0003. A thousand trials with a probability of 0.003 each cannot be told from the limit.

</div>

<!--
Speaker: n grows by a factor of ten from panel to panel and p falls by the
same factor. (~2 min)
-->

---
hideInToc: true
---

# The Limit, **Computed**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Binomial, $n$ = 1000, $p$ = 0.003 | 0.0496 | 0.1491 | 0.2242 | 0.2244 | 0.1683 | 0.1009 |
| Poisson, $\lambda$ = 3 | 0.0498 | 0.1494 | 0.2240 | 0.2240 | 0.1680 | 0.1008 |

</div>

```python {monaco-run} {autorun:false}
from math import comb, exp, factorial
n, p, lam = 1000, 0.003, 3
for k in range(6):
    binomial = comb(n, k) * p**k * (1 - p)**(n - k)
    poisson = lam**k * exp(-lam) / factorial(k)
    print(k, f"{binomial:.4f}", f"{poisson:.4f}")
```

<!--
Speaker: both formulas are typed as they stand, and comb(n, k) is the binomial
coefficient. Run it, then set n, p = 10, 0.3 and run again: the first column
changes, the second does not. Python computes comb(1000, 5) exactly, as an
integer that does not overflow. (~3 min)
-->

---
hideInToc: true
---

# The **Poisson** Distribution

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **Mean and variance**

Take the binomial results to the limit $p \to 0$, $np = \lambda$:

$$E[k] = np = \lambda$$

$$\mathrm{Var}(k) = np\,(1-p) \to \lambda$$

The variance equals the mean, so

$$\sigma = \sqrt{\lambda}$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **Where it applies**

Events that occur independently, at a constant mean rate, counted in a fixed interval:

- decays of a source per minute
- photons on a pixel per exposure
- rows of a file in one bin of a histogram

For $\lambda$ = 3: no event with probability 0.050, six or more with 0.084.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**A count and its uncertainty.** A count $N$ is one draw from a Poisson distribution whose mean is not known. $N$ is the estimate of $\lambda$ and $\sqrt{N}$ the estimate of $\sigma$. The count is written $N \pm \sqrt{N}$.

</div>

<!--
Speaker: this answers the fourth question of the opening slide: the bar of
± √N on a histogram bin is the standard deviation of a Poisson count. Ask:
a bin holds 2500 rows; how large is its bar, and what is it relative to the
count? 50, which is 2 %. (~2 min)
-->

---
hideInToc: true
---

# √N, **Checked** on the Mass Column

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📊 **14 bins where the histogram is flat**

```python
counts, edges = np.histogram(
    M, bins=np.arange(1816, 1846, 2))
print(counts.min(), counts.max())
print(counts.mean(), counts.std(ddof=1))
```

```text
1419 1534
1460.7857142857142 33.88482431238679
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📏 **The relative uncertainty is 1/√N**

| Count $N$ | $\sqrt{N}$ | $\sqrt{N}/N$ |
| --- | --- | --- |
| 100 | 10 | 10 % |
| 1461 | 38 | 2.6 % |
| 1916, the top bar of Lecture 08 | 44 | 2.3 % |
| 3746, the highest 2 MeV/c² bin | 61 | 1.6 % |
| 10 000 | 100 | 1 % |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Lecture 08 drew a bar of ± √N on every bin and took √N as given. Here is the check: from 1816 to 1844 MeV/c² the bins of 2 MeV/c² hold about the same number of rows, and their counts scatter by 34. The Poisson prediction is √1461 = 38. Fourteen counts fix a standard deviation to about one part in five, so 34 and 38 agree.

</div>

<!--
Speaker: point back at the figure of the opening slide: every bar there is
± the square root of its count, and now it is derived. Nothing in the file
says that the counts are Poisson. The scatter of neighbouring bins shows it.
The bins here are 2 MeV/c² wide, so each holds about twice the rows of a bin
of Lecture 08. (~2 min)
-->

---
hideInToc: true
---

# Adding Makes a **Bell**

<img class="fig" src="/figures/viz_probability_clt.svg" style="display:block;margin:0 auto;max-height:215px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎰 **The simulation**

Each panel holds 100 000 sums of $N$ uniform random numbers. One number is flat, two make a triangle, twelve make a bell. The rules for sums give its centre and its width: the mean $N/2$ and the variance $N/12$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📜 **The central limit theorem**

The sum of $N$ independent random variables with finite variances tends to one bell-shaped curve as $N$ grows, whatever the distribution of each one. Its mean is the sum of the means and its variance the sum of the variances.

</div>

</div>

<!--
Speaker: ask before showing the panels: what does the histogram of sums of
two flat random numbers look like? Most say flat. Nothing in a uniform number
is bell-shaped. The shape comes from adding. The theorem is stated here and
shown by simulation; its proof needs tools this course does not have. (~3 min)
-->

---
hideInToc: true
---

# The Sums in **NumPy**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| $N$ | 1 | 2 | 3 | 12 | Rules for sums |
| --- | --- | --- | --- | --- | --- |
| Mean, standard deviation of the sums | 0.500, 0.289 | 1.000, 0.409 | 1.501, 0.500 | 6.003, 1.002 | $N/2$, $\sqrt{N/12}$ |
| Fraction within ±1σ of the mean | 57.6 % | 64.9 % | 66.7 % | 67.7 % | |

</div>

```python {monaco-run} {autorun:false}
rng = np.random.default_rng(4)
for N in [1, 2, 3, 12]:
    s = rng.random((100_000, N)).sum(axis=1)     # 100 000 sums of N numbers
    z = (s - N / 2) / np.sqrt(N / 12)            # distance from the mean in σ
    print(N, s.mean().round(3), s.std().round(3), (abs(z) < 1).mean().round(3))
```

<div class="note-text mt-sm">

`rng.random((100_000, N))` is a table of 100 000 rows and $N$ columns. `.sum(axis=1)` adds along each row. The fraction within ±1σ climbs with $N$ and settles near 68 %: the bell has a fixed shape.

</div>

<!--
Speaker: run it, then put 50 into the list. The mean and the standard deviation
follow N/2 and the square root of N/12 from the first line on. Only the shape
needs N to grow. (~3 min)
-->

---
hideInToc: true
---

# The Bell Is the **Gaussian**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔔 **The density**

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Two parameters: the mean $\mu$, where the peak is, and the standard deviation $\sigma$, its width. It is also called the normal distribution. The sums of twelve put 67.7 % within ±σ. The curve puts:

| Interval | Probability |
| --- | --- |
| $\mu \pm \sigma$ | 68.27 % |
| $\mu \pm 2\sigma$ | 95.45 % |
| $\mu \pm 3\sigma$ | 99.73 % |

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_gaussian.svg" style="display:block;margin:0 auto;max-height:270px;">

$z = (x - \mu)/\sigma$ is the distance from the mean in units of $\sigma$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

This is what an uncertainty means. A result written $x \pm \sigma$ says: if the measurement is Gaussian, the interval covers the true value in 68 % of repetitions.

</div>

<!--
Speaker: this is the curve drawn over the sums two slides back. The three
percentages are areas under it. They are worth knowing by heart: two in
three, 19 in 20, 369 in 370. (~2 min)
-->

---
hideInToc: true
---

# Where the Gaussian **Applies**

<img class="fig" src="/figures/viz_probability_poisson_gaussian.svg" style="display:block;margin:0 auto;max-height:185px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Counts**

A count is a sum of many trials. For large $\lambda$ the Poisson distribution is close to a Gaussian with $\mu = \lambda$ and $\sigma = \sqrt{\lambda}$. For $\lambda$ = 100, $P(90 \le k \le 110)$ is 0.7065, and 0.7063 from the Gaussian.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **Measurements**

The error of a measurement is the sum of many small independent disturbances. This is why a Gaussian is the usual model of a measurement error.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Not here**

Small counts: for $\lambda$ = 1 the distribution is skewed and has no negative side. A sum in which one term dominates. A sample that mixes two kinds of rows.

</div>

</div>

<!--
Speaker: bars are the Poisson distribution, the curve is the Gaussian with the
same mean and variance. From about λ = 16 on the two agree by eye. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Samples and the Standard **Error**

Each distribution so far came with its μ and σ given. The mass column comes without them: 91 583 values, from which both have to be estimated.

<!--
Speaker: from distributions with known parameters to a sample with unknown
ones. The mean of a sample, its standard deviation, and the uncertainty of the
mean. All on the mass column. (~1 min)
-->

---
hideInToc: true
---

# A Sample and Its **Summaries**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **N values from one distribution**

The sample $x_1, \dots, x_N$ is known. The parameters $\mu$ and $\sigma$ of its distribution are not. They are estimated:

$$\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$$

$$s^2 = \frac{1}{N-1}\sum_{i=1}^{N}(x_i-\bar{x})^2$$

The sample mean $\bar{x}$ estimates $\mu$. The sample standard deviation $s$ estimates $\sigma$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐍 **The mass column**

```python
M = np.loadtxt("data/raw/D0_KPi.csv",
               delimiter=",", skiprows=1,
               usecols=0)
print(len(M), M.mean(), M.std(ddof=1))
```

```text
91583 1864.1045817826453 25.565096122743306
```

- $\bar{x}$ = 1864.10 MeV/c², $s$ = 25.57 MeV/c²
- `ddof=1` divides by $N - 1$. Without it NumPy divides by $N$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The **median** is the middle value of the sorted sample, here 1864.08. One wrong value moves the mean and hardly moves the median. The file has a row with $M$ = 2453.66.

</div>

<!--
Speaker: usecols=0 reads only the first column. A bar over a letter is a
sample mean; s is computed from the sample, sigma belongs to the distribution.
(~3 min)
-->

---
hideInToc: true
---

# Covariance and **Correlation**

<div class="card card-info card-glass pad-compact mt-sm">

Two columns $x$ and $y$ of the same $N$ rows. The **covariance** $s_{xy}$ is positive when $x$ and $y$ lie on the same side of their means together. Divided by both standard deviations it is the **correlation coefficient** $r$, a number without unit between −1 and +1. For two random variables the same ratio is written $\rho$:

$$s_{xy} = \frac{1}{N-1}\sum_{i=1}^{N} (x_i-\bar{x})(y_i-\bar{y}), \qquad r = \frac{s_{xy}}{s_x\,s_y}, \qquad \rho = \frac{\mathrm{Cov}(X, Y)}{\sigma_X\,\sigma_Y}$$

</div>

<img class="fig mt-sm" src="/figures/viz_probability_correlation.svg" style="display:block;margin:0.6rem auto 0;max-height:185px;">

<div class="note-text mt-sm">

$r = \pm 1$: the points lie on a straight line. $r$ = 0: no straight-line relation. In the last panel $y$ follows from $x$ up to a little noise and $r$ is still 0.00: the coefficient sees only the straight-line part of a relation.

</div>

<!--
Speaker: the covariance is the sample version of E[ΔX ΔY] from the slide on
sums. 150 seeded points per panel. (~2 min)
-->

---
hideInToc: true
---

# Correlation in **Numbers**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **The pendulum table, by hand**

Length $x$ in cm, time of 10 swings $y$ in s, nine rows.

- $\bar{x}$ = 60, $\bar{y}$ = 15.139
- $\sum (x_i-\bar{x})(y_i-\bar{y})$ = 813.0
- $s_{xy}$ = 813.0 / 8 = 101.6 cm·s
- $s_x$ = 27.39 cm, $s_y$ = 3.732 s
- $r$ = 101.6 / (27.39 × 3.732) = 0.994

`np.corrcoef(length, t10)[0, 1]` gives 0.9942.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📄 **Four pairs of columns**

| Columns | $r$ |
| --- | --- |
| length, time of 10 swings | 0.994 |
| length, $T^2$ | 0.9999 |
| `M`, `PT` | 0.002 |
| `TAU`, `IPCHI2` | 0.62 |

The time grows like the square root of the length, and $r$ is still 0.994. `M` and `PT` give 0.002, yet a high `PT` raised the share of rows in the peak from 0.28 to 0.40: a dependence, but not along a line.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A correlation does not say why. Two columns move together when one causes the other, when a third quantity drives both, or when the rows were selected in a way that ties them.

</div>

<!--
Speaker: the M, PT row is the pair of Independence, Tested on the File: r is
0.002 and the two are still not independent, as in the last panel of the
slide before. T² against the length is a straight line, r = 0.9999. The last
pair leaves out the 49 rows with TAU = -100, the marker of a missing value.
With them in, the coefficient describes the marker and not the data. (~3 min)
-->

---
hideInToc: true
---

# The Standard Error of the **Mean**

<div class="card card-info card-glass pad-compact mt-sm">

Another sample of the same size gives another $\bar{x}$. The sample mean is itself a random variable. How far from $\mu$ does it lie?

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **Its mean**

$$E[\bar{x}] = \frac{1}{N}\big(E[x_1] + \dots + E[x_N]\big) = \frac{1}{N}\,N\mu = \mu$$

On average $\bar{x}$ is right.

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Its variance**

$$\mathrm{Var}(\bar{x}) = \frac{1}{N^2}\big(\mathrm{Var}(x_1) + \dots + \mathrm{Var}(x_N)\big) = \frac{1}{N^2}\,N\sigma^2 = \frac{\sigma^2}{N}$$

The factor $1/N$ comes out squared. The variances of independent values add.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{N}}$$

The **standard error of the mean**: the standard deviation of $\bar{x}$. In practice $\sigma$ is not known and $s$ takes its place: $s/\sqrt{N}$.

</div>

<!--
Speaker: this is the central derivation of the lecture, and it is two lines,
both from the rules of Sums of Random Variables. It needs independence: N
copies of the same row would not reduce the uncertainty. Ask: how many rows
halve the uncertainty of the mean? Four times as many. (~3 min)
-->

---
hideInToc: true
---

# The Standard Error, **Checked**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎰 **By simulation**

10 000 means of 25 uniform numbers. Prediction: $\sqrt{1/12}\,/\sqrt{25}$.

```python
rng = np.random.default_rng(6)
x = rng.random((10_000, 25))
means = x.mean(axis=1)
print(means.std(), np.sqrt(1/12) / 5)
```

```text
0.05906023806000769 0.057735026918962574
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **On the mass column**

The first 91 500 rows, cut into 915 groups of 100. Prediction: $s/\sqrt{100}$.

```python
groups = M[:91_500].reshape(915, 100)
means = groups.mean(axis=1)
print(means.std(ddof=1),
      M.std(ddof=1) / 10)
```

```text
2.5956512602849324 2.5565096122743305
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`reshape(915, 100)` arranges the values as 915 rows of 100, and `.mean(axis=1)` takes the mean of each row. The means of 100 mass values scatter with a standard deviation of 2.60 MeV/c². The single values scatter with 25.57.

</div>

<!--
Speaker: the left check is on numbers whose sigma is known exactly. The right
one is on real data, where nothing is known in advance. Both agree with sigma
over root N to about 2 %. (~3 min)
-->

---
hideInToc: true
---

# The Means of **100 Mass Values**

<img class="fig" src="/figures/viz_probability_group_means.svg" style="display:block;margin:0 auto;max-height:245px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ❌ **Single values**

The curve is the Gaussian with the mean and the $s$ of the column. It does not describe the values: 62.7 % lie within ±$s$ and 99.9 % within ±2$s$.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✅ **Means of 100**

The curve has the same mean and the width $s/\sqrt{100}$ = 2.56. Of the 915 means, 68.2 % lie within ±1 standard error and 95.1 % within ±2.

</div>

</div>

<div class="note-text mt-sm">

The central limit theorem on real data: the values are not Gaussian, and their mean is.

</div>

<!--
Speaker: this is why a mean can be quoted with a Gaussian uncertainty even when
the data are far from Gaussian. (~2 min)
-->

---
hideInToc: true
---

# Standard Deviation and Standard **Error**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Rows of the mass column | $N$ | $\bar{x}$ | $s$ | $s/\sqrt{N}$ |
| --- | --- | --- | --- | --- |
| the first 100 | 100 | 1865.68 | 26.14 | 2.61 |
| the first 1000 | 1000 | 1863.58 | 25.38 | 0.80 |
| the first 10 000 | 10 000 | 1863.87 | 24.98 | 0.25 |
| all | 91 583 | 1864.10 | 25.57 | 0.084 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📊 **Standard deviation s**

- The spread of single values
- A property of the distribution. More data make it better known, not smaller
- Describes the data

</div>

<div class="card card-accent card-glass pad-compact">

## 🎯 **Standard error s/√N**

- The uncertainty of the mean
- Ten times the data divide it by $\sqrt{10}$ = 3.2. Half the uncertainty costs four times the data
- Belongs to a result: $\bar{x}$ = 1864.10 ± 0.08 MeV/c²

</div>

</div>

<!--
Speaker: read the table down. The third column stays near 25. The last one
falls by 3.2 per row. Each mean agrees with the final one within about one of
its own standard errors. (~3 min)
-->

---
hideInToc: true
---

# Why **N − 1**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **The derivation**

Write $x_i - \mu = (x_i - \bar{x}) + (\bar{x} - \mu)$ and square. The mixed term vanishes, because $\sum_i (x_i - \bar{x}) = 0$:

$$\sum_i (x_i-\bar{x})^2 = \sum_i (x_i-\mu)^2 - N(\bar{x}-\mu)^2$$

Take the expected value. The first sum gives $N\sigma^2$, the last term $N \cdot \sigma^2/N$:

$$E\Big[\sum_i (x_i-\bar{x})^2\Big] = (N-1)\,\sigma^2$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎰 **The check**

100 000 samples of $N$ = 5 with $\sigma^2$ = 1:

```python
rng = np.random.default_rng(5)
x = rng.normal(0, 1, (100_000, 5))
print(x.var(axis=1, ddof=0).mean())
print(x.var(axis=1, ddof=1).mean())
```

```text
0.7989905825485553
0.9987382281856941
```

Dividing by $N$ gives 4/5 of the variance. Dividing by $N - 1$ gives it all.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The distances are measured from $\bar{x}$, which was computed from the same values and lies closer to them than $\mu$ does. For large $N$ it does not matter: the mass column gives 25.5650 with $N$ and 25.5651 with $N - 1$.

</div>

<!--
Speaker: the term that is subtracted is the variance of the mean from the
slide before. (~3 min)
-->

---
hideInToc: true
---

# What the Standard Error Does **Not** Cover

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔍 **The mean depends on the rows**

| Rows with | $N$ | $\bar{x}$ | $s/\sqrt{N}$ |
| --- | --- | --- | --- |
| all | 91 583 | 1864.10 | 0.08 |
| 1840 < $M$ < 1890 | 56 577 | 1864.71 | 0.05 |
| 1850 < $M$ < 1880 | 41 090 | 1864.79 | 0.04 |
| 1855 < $M$ < 1875 | 31 132 | 1864.81 | 0.03 |

The mass of the D⁰ meson is 1864.84 ± 0.05 MeV/c² (Particle Data Group).

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚖️ **Two kinds of uncertainty**

- **Statistical**: from the finite sample. It falls like $1/\sqrt{N}$. The standard error is of this kind
- **Systematic**: from the method. Here the rows are a peak on a flat part that is not D⁰, and the flat part pulls the mean down. More rows do not reduce it

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The mean of all rows lies 0.74 MeV/c² below the D⁰ mass. That is 8.7 standard errors. The standard error answers "how well is the mean of these rows known". It does not answer "is the mean of these rows the mass of the particle".

</div>

<!--
Speaker: ask first: is 1864.10 ± 0.08 the mass of the D0? The answer is on
the slide: no, 0.74 below it. The flat part is the second kind of row found
on Independence, Tested on the File. The selection uses a mask:
M[(M > 1850) & (M < 1880)]. The mean moves by 0.7 between the first and the
last line of the table, far more than any of the standard errors. A small
uncertainty is not the same as a correct result. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Error **Propagation**

The mean of the mass column is known to 0.08 MeV/c². A value of g is not measured but computed from a length and a time, and it inherits their uncertainties.

<!--
Speaker: a measured quantity has an uncertainty. A quantity computed from it
has one too. The rule comes from the tangent to the function and from the
variance of a sum. (~1 min)
-->

---
hideInToc: true
---

# A Function of One **Measurement**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **The tangent**

$x$ is measured as $x_0 \pm \sigma_x$, and $f(x)$ is computed from it. Near $x_0$ the function is close to its tangent, the first two terms of its Taylor series:

$$f(x) \approx f(x_0) + f'(x_0)\,(x - x_0)$$

This is a constant plus a constant times $x$. With $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$:

$$\sigma_f = |f'(x_0)|\;\sigma_x$$

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_propagation.svg" style="display:block;margin:0 auto;max-height:280px;">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The period from the time of 10 swings: $T = t_{10}/10$, so $\sigma_T = \sigma_{t_{10}}/10$. A time known to 0.1 s gives a period known to 0.01 s. Timing ten swings instead of one divides the timing error by ten.

</div>

<!--
Speaker: the figure is g against the period for a length of 1 m. The band in T
is drawn ten times wider than in the example that follows, so that it can be
seen. The slope turns a width in T into a width in g. (~3 min)
-->

---
hideInToc: true
---

# A Function of **Several** Measurements

<div class="card card-primary card-glass pad-compact mt-sm">

The tangent in two variables, with both derivatives taken at the measured values:

$$f(x, y) \approx f(x_0, y_0) + \frac{\partial f}{\partial x}\,(x - x_0) + \frac{\partial f}{\partial y}\,(y - y_0)$$

The variance of this sum, by the rule for $\mathrm{Var}(X + Y)$:

$$\sigma_f^2 = \left(\frac{\partial f}{\partial x}\right)^{2}\sigma_x^2 + \left(\frac{\partial f}{\partial y}\right)^{2}\sigma_y^2 + 2\,\frac{\partial f}{\partial x}\,\frac{\partial f}{\partial y}\,\mathrm{Cov}(x, y)$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔀 **Independent measurements**

The covariance is 0. Each input contributes its derivative times its uncertainty, and the contributions add as squares: **in quadrature**.

</div>

<div class="card card-accent card-glass pad-compact">

## ➕ **More inputs**

One term per input:

$$\sigma_f^2 = \sum_j \left(\frac{\partial f}{\partial x_j}\right)^{2}\sigma_j^2$$

</div>

</div>

<!--
Speaker: each term is how strongly f reacts to the input, times how uncertain
the input is. The covariance term matters when two inputs come from the same
measurement. (~3 min)
-->

---
hideInToc: true
---

# Two Rules That **Follow**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **Sums and differences**

For $f = x + y$ and for $f = x - y$ the derivatives are 1 and ±1:

$$\sigma_f^2 = \sigma_x^2 + \sigma_y^2$$

**Absolute** uncertainties add in quadrature.

12.61 − 11.05 s, each ± 0.10 s: the difference is 1.56 ± 0.14 s.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✖️ **Products, quotients, powers**

For $f = x^a y^b$ the derivatives are $a f/x$ and $b f/y$:

$$\left(\frac{\sigma_f}{f}\right)^{2} = a^2\left(\frac{\sigma_x}{x}\right)^{2} + b^2\left(\frac{\sigma_y}{y}\right)^{2}$$

**Relative** uncertainties add in quadrature, each times its power.

$T$ = 2.001 s ± 0.5 %: $T^2$ = 4.004 s² ± 1.0 %.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

In quadrature the larger term decides. 3 % and 1 % give $\sqrt{9 + 1}$ = 3.2 %, not 4 %. Halving the 1 % term gives 3.04 %.

</div>

<!--
Speaker: a difference of two nearly equal numbers keeps both absolute
uncertainties: 1.56 ± 0.14 is known to 9 %, from two times known to 1 %.
(~3 min)
-->

---
hideInToc: true
---

# *g* from One Pendulum **Measurement**

<div class="card card-info card-glass pad-compact mt-sm">

The period of a pendulum of length $\ell$ is $T = 2\pi\sqrt{\ell/g}$. Solved for $g$:

$$g = \frac{4\pi^2 \ell}{T^2}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📄 **The last row of `pendulum.csv`**

| Quantity | Value | Uncertainty | Relative |
| --- | --- | --- | --- |
| length $\ell$ | 1.000 m | 0.001 m | 0.10 % |
| time of 10 swings $t_{10}$ | 20.01 s | 0.1 s | 0.50 % |
| period $T = t_{10}/10$ | 2.001 s | 0.010 s | 0.50 % |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **The value**

$$g = \frac{4\pi^2 \times 1.000}{2.001^2} = \frac{39.478}{4.004} = 9.860\ \text{m/s}^2$$

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

The uncertainties are stated for this example, not read from the file: 0.1 cm on the length, the smallest division of a ruler, and 0.1 s on the time, for a stopwatch started and stopped by hand. The length is written $\ell$: the letter $L$ is kept for the likelihood.

</div>

<!--
Speaker: the file holds 100 cm and 20.01 s. An uncertainty is part of a
measurement and has to be written down with it. Here it is chosen and stated.
(~2 min)
-->

---
hideInToc: true
---

# The Uncertainty of ***g***

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **By the derivatives**

$$\frac{\partial g}{\partial \ell} = \frac{4\pi^2}{T^2} = \frac{g}{\ell}, \qquad \frac{\partial g}{\partial T} = -\frac{8\pi^2 \ell}{T^3} = -\frac{2g}{T}$$

- From the length: 9.860 × 0.001 = 0.0099 m/s²
- From the period: 9.855 × 0.010 = 0.0985 m/s²

$$\sigma_g = \sqrt{0.0099^2 + 0.0985^2} = 0.0990\ \text{m/s}^2$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **By the rule for powers**

$g = 4\pi^2 \ell^{1}\,T^{-2}$, so

$$\frac{\sigma_g}{g} = \sqrt{(0.10\,\%)^2 + (2 \times 0.50\,\%)^2} = 1.00\,\%$$

1.00 % of 9.860 is 0.099 m/s².

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

**$g$ = 9.86 ± 0.10 m/s².** The timing gives 99 % of the variance, the ruler 1 %. A better ruler changes nothing. Timing 50 swings instead of 10 gives $\sigma_g$ = 0.022 m/s².

</div>

<!--
Speaker: ask: which instrument would you improve, the ruler or the
stopwatch? The stopwatch: it gives 99 % of the variance. The two ways are the
same computation. The second one shows at a glance which input matters: the
period enters squared, so its relative uncertainty counts twice. (~3 min)
-->

---
hideInToc: true
---

# The Same by **Simulation**

<div class="note-text mt-sm">

The measurement is repeated 100 000 times in the computer: the length and the time are drawn from Gaussians with the stated uncertainties, and $g$ is computed for each pair.

</div>

```python {monaco-run} {autorun:false}
rng = np.random.default_rng(3)
length = rng.normal(1.000, 0.001, 100_000)   # 100 000 lengths, m
t10 = rng.normal(20.01, 0.1, 100_000)        # 100 000 times of 10 swings, s
g = 4 * np.pi**2 * length / (t10 / 10)**2
print(g.mean(), g.std())
```

<div class="card card-info card-glass pad-compact mt-sm">

The output is `9.860474937008293 0.09899416541917416`: the spread is 0.0990 m/s², as from the formula. With 2.0 s in place of 0.1 s the formula gives 1.97 m/s² and the simulation 2.15, and the mean of $g$ moves to 10.17. Over so wide an interval the curve is not close to its tangent. The first-order rule needs small relative uncertainties.

</div>

<!--
Speaker: run it, then change 0.1 to 2.0 in the third line. A simulation needs
no derivative and works for any formula. It is the check to make when the
uncertainties are large. (~3 min)
-->

---
hideInToc: true
---

# Writing a **Result**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **Five rules**

1. Value, uncertainty and unit, in this order
2. The uncertainty with one or two significant digits
3. The value rounded to the same decimal place
4. A word on what the uncertainty is: a standard deviation, a standard error, a propagated uncertainty
5. Compute with all digits. Round once, at the end

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **Applied**

| Computed | Written |
| --- | --- |
| 9.859742 ± 0.099040 m/s² | 9.86 ± 0.10 m/s² |
| 1864.1046 ± 0.0845 MeV/c² | 1864.10 ± 0.08 MeV/c² |
| 3746 ± 61.2 rows | 3746 ± 61 rows |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The digits of 9.859742 beyond the second decimal carry no information: the uncertainty is in the first decimal. A value without an uncertainty cannot be compared with another value.

</div>

<!--
Speaker: the uncertainty decides how many digits of the value mean something.
The same point was made for a float32 in the lecture on how computers work:
digits beyond the precision are not information. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Testing a **Hypothesis**

Error propagation gave g = 9.86 ± 0.10 m/s² from one pendulum row. A value with its uncertainty can now be set against a value known from elsewhere.

<!--
Speaker: a short section. A result and its uncertainty are compared with a
value that is known from elsewhere: g with 9.81, the mean of the mass column
with the D0 mass. (~1 min)
-->

---
hideInToc: true
---

# Is a Result Compatible with a Known **Value**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **The distance in units of σ**

Measured: $g$ = 9.86 ± 0.10 m/s². The reference value is 9.81 m/s². Hypothesis: the measurement is a Gaussian draw around 9.81 with $\sigma$ = 0.10.

$$z = \frac{x - \mu_0}{\sigma} = \frac{9.86 - 9.81}{0.10} = 0.5$$

The **p-value** is the probability, if the hypothesis holds, of a distance at least as large as the observed one.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔔 **From the Gaussian, both sides**

| $\lvert z \rvert$ | p-value |
| --- | --- |
| 0.5 | 0.62 |
| 1 | 0.32 |
| 2 | 0.046 |
| 3 | 0.0027 |
| 5 | 5.7 × 10⁻⁷ |

In Python: `math.erfc(z / math.sqrt(2))`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$p$ = 0.62: a distance of this size or more occurs in 62 % of repetitions. The result is compatible with 9.81. The mean of the mass column against the D⁰ mass: $z$ = (1864.10 − 1864.84) / 0.084 = −8.7 and $p$ = 3 × 10⁻¹⁸. That hypothesis is rejected, and the reason is known: the rows are not all D⁰.

</div>

<!--
Speaker: the table is one minus the areas of the Gaussian slide: 1 − 0.6827 =
0.32. Particle physics asks for 5 sigma before it speaks of a discovery. Many
fields use p below 0.05, which is 2 sigma. (~3 min)
-->

---
hideInToc: true
---

# What a p-Value Is **Not**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔄 **Not the probability of the hypothesis**

It is $P(\text{data this far off} \mid \text{hypothesis})$. The reverse, $P(\text{hypothesis} \mid \text{data})$, needs Bayes' theorem and a prior probability of the hypothesis.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🤷 **A large p proves nothing**

$p$ = 0.62 says that the data do not contradict 9.81. With an uncertainty of 0.10 they would not contradict 9.75 or 9.90 either.

</div>

<div class="card card-warning card-glass pad-compact">

## 🎣 **Many tests**

20 independent tests at the 5 % level, every hypothesis true. The probability that at least one gives $p$ < 0.05 is 1 − 0.95²⁰ = 0.64.

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **Significant is not large**

With 91 583 rows a difference of 0.74 MeV/c² in 1864, which is 0.04 %, stands 8.7σ away. The p-value measures how sure a difference is, not how big.

</div>

</div>

<!--
Speaker: the third card uses the complement and the independence of the first
section. The remedy is to decide what to test before looking at the data and
to report every test that was made. Conventions: many fields call a result
significant at p < 0.05, about 2 sigma. Particle physics speaks of evidence at
3 sigma and of an observation at 5 sigma, counted on one side: 2.9 × 10⁻⁷, or
1 in 3.5 million. A threshold is a convention; the value, its uncertainty and
the distance in sigma are the result. (~3 min)
-->

---
layout: section
hideInToc: true
---

# **Likelihood**

Until now a parameter was given and the data were predicted, or tested against it. Read the other way, the same formulas say which parameter makes the observed data most probable.

<!--
Speaker: so far a parameter was given and the data were predicted. Now the
data are given and the parameter is estimated. The section ends with the mean
and the weighted mean as maximum-likelihood estimates. (~1 min)
-->

---
hideInToc: true
---

# Probability, Read the **Other Way**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔬 **7 of 10 particles registered**

The efficiency $p$ of the detector is not known.

- **Probability**: $p$ is given, $k$ varies. Summed over $k$ it gives 1
- **Likelihood**: $k$ = 7 is given, $p$ varies

$$L(p) = \binom{10}{7}\,p^7\,(1-p)^3$$

| $p$ | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| --- | --- | --- | --- | --- | --- |
| $L(p)$ | 0.117 | 0.215 | 0.267 | 0.201 | 0.057 |

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_likelihood_binomial.svg" style="display:block;margin:0 auto;max-height:285px;">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The likelihood is the probability of the observed data, as a function of the parameter. It is the binomial formula with the roles of $k$ and $p$ exchanged. It is not a probability of $p$: its area over $p$ is 1/11, not 1.

</div>

<!--
Speaker: each registered particle contributes a factor p and each missed one a
factor 1 − p. The trials are independent, so the factors multiply: p to the 7
times (1 − p) to the 3. (~3 min)
-->

---
hideInToc: true
---

# Maximum **Likelihood**

<div class="card card-info card-glass pad-compact mt-sm">

The estimate $\hat{p}$ is the value of the parameter at which the likelihood is largest: the value under which the observed data are most probable.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **k successes in n trials**

$$\ln L(p) = k\,\ln p + (n-k)\,\ln(1-p) + \text{const}$$

$$\frac{d \ln L}{dp} = \frac{k}{p} - \frac{n-k}{1-p} = 0$$

$$\hat{p} = \frac{k}{n}$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 💡 **Reading it**

- 7 of 10: $\hat{p}$ = 0.7. The maximum-likelihood estimate of a probability is the observed fraction
- The logarithm turns the product into a sum, which is easier to differentiate
- $\ln L$ has its maximum where $L$ has it, because the logarithm is an increasing function
- A hat marks an estimate: $\hat{p}$ estimates $p$

</div>

</div>

<!--
Speaker: solve the middle line on the board: k(1 − p) = (n − k)p, so k = np.
The constant is the logarithm of the binomial coefficient. It does not depend
on p. (~3 min)
-->

---
hideInToc: true
---

# The Likelihood of Many **Measurements**

<div class="card card-primary card-glass pad-compact mt-sm">

$N$ independent measurements $x_1, \dots, x_N$, each with the density $f(x_i;\theta)$, where $\theta$ stands for the parameters. Independent probabilities multiply:

$$L(\theta) = \prod_{i=1}^{N} f(x_i;\theta), \qquad \ln L(\theta) = \sum_{i=1}^{N} \ln f(x_i;\theta)$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

Gaussian measurements of one quantity $\mu$, each with the same known $\sigma$. The logarithm of the Gaussian density is $-(x_i-\mu)^2/(2\sigma^2)$ minus $\ln(\sigma\sqrt{2\pi})$:

$$\ln L(\mu) = -\sum_{i=1}^{N}\frac{(x_i-\mu)^2}{2\sigma^2} + \text{const}$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

Each measurement lowers $\ln L$ by half the square of its distance from $\mu$, counted in units of $\sigma$. The constant does not depend on $\mu$.

</div>

<!--
Speaker: this formula is the end point of the first four sections: the
Gaussian density, independence, and the product rule. Notation from here on:
theta for parameters, L of theta for the likelihood. (~3 min)
-->

---
hideInToc: true
---

# The Gaussian Mean Is the **Sample Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **Set the derivative to zero**

$$\frac{d \ln L}{d\mu} = \sum_{i=1}^{N} \frac{x_i-\mu}{\sigma^2} = 0$$

$$\sum_{i=1}^{N} x_i = N\mu$$

$$\hat{\mu} = \frac{1}{N}\sum_{i=1}^{N} x_i = \bar{x}$$

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ⏱️ **Five timings of 10 swings**

20.01, 19.93, 20.12, 19.98, 20.06 s, each with $\sigma$ = 0.1 s. Example values for the 100 cm pendulum. $\bar{x}$ = 20.02 s.

| $\mu$ | 19.95 | 20.00 | 20.02 | 20.05 | 20.10 |
| --- | --- | --- | --- | --- | --- |
| $\ln L(\mu) - \ln L(\bar{x})$ | −1.225 | −0.100 | 0 | −0.225 | −1.600 |

- The five values add up to 100.10 s. Divided by 5: 20.02 s
- $\ln L$ is highest at $\bar{x}$ and falls on both sides of it

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

The sample mean is not a convention. It is the maximum-likelihood estimate of the mean of Gaussian measurements with equal uncertainties.

</div>

<!--
Speaker: sigma drops out of the estimate, because it is the same for every
measurement. It comes back in the uncertainty of the estimate. (~3 min)
-->

---
hideInToc: true
---

# The Width of the **Likelihood**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **A parabola in μ**

With $\sum_i (x_i-\mu)^2 = \sum_i (x_i-\bar{x})^2 + N(\bar{x}-\mu)^2$:

$$\ln L(\mu) = \ln L(\bar{x}) - \frac{(\mu-\bar{x})^2}{2\,(\sigma/\sqrt{N})^2}$$

As a function of $\mu$ the likelihood is a Gaussian centred at $\bar{x}$ with the width $\sigma/\sqrt{N}$: the standard error.

At $\mu = \bar{x} \pm \sigma/\sqrt{N}$ the logarithm is lower than its maximum by 1/2.

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_likelihood_mean.svg" style="display:block;margin:0 auto;max-height:270px;">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The five timings: 0.1 / √5 = 0.045, so $\hat{\mu}$ = 20.02 ± 0.045 s. The uncertainty of a maximum-likelihood estimate is the distance over which $\ln L$ falls by 1/2 from its maximum.

</div>

<!--
Speaker: the identity in the first line is the one from the slide on N − 1.
The likelihood gives the estimate and its uncertainty in one curve: the place
of the maximum and the width around it. (~3 min)
-->

---
hideInToc: true
---

# Unequal Uncertainties: the **Weighted Mean**

<div class="card card-info card-glass pad-compact mt-sm">

$N$ measurements of the same quantity, each with its own uncertainty: $x_i \pm \sigma_i$. In the likelihood each term now has its own $\sigma_i$:

$$\ln L(\mu) = -\sum_{i=1}^{N}\frac{(x_i-\mu)^2}{2\sigma_i^2} + \text{const}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **Set the derivative to zero**

$$\frac{d \ln L}{d\mu} = \sum_{i=1}^{N} \frac{x_i-\mu}{\sigma_i^2} = 0$$

$$\sum_{i=1}^{N} \frac{x_i}{\sigma_i^2} = \mu \sum_{i=1}^{N} \frac{1}{\sigma_i^2}$$

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚖️ **The weighted mean**

$$\hat{\mu} = \frac{\displaystyle\sum_i w_i\,x_i}{\displaystyle\sum_i w_i}, \qquad w_i = \frac{1}{\sigma_i^2}$$

- A measurement with half the uncertainty counts four times
- Equal uncertainties: the weights cancel, and $\hat{\mu} = \bar{x}$

</div>

</div>

<!--
Speaker: the same three lines as for the plain mean, with sigma_i inside the
sum. A precise measurement pulls harder. (~3 min)
-->

---
hideInToc: true
---

# The Uncertainty of the Weighted **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **By error propagation**

$\hat{\mu}$ is a sum of the $x_i$ with the factors $w_i / \sum_j w_j$. Each factor comes out squared, and $w_i^2\,\sigma_i^2 = w_i$:

$$\sigma_{\hat{\mu}}^2 = \frac{\sum_i w_i^2\,\sigma_i^2}{\big(\sum_j w_j\big)^2} = \frac{1}{\sum_i w_i}$$

$$\sigma_{\hat{\mu}} = \Big(\sum_{i=1}^{N} \frac{1}{\sigma_i^2}\Big)^{-1/2}$$

Equal uncertainties: $(N/\sigma^2)^{-1/2} = \sigma/\sqrt{N}$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Two values of g**

From the 20 cm row: 9.70 ± 0.22 m/s². From the 100 cm row: 9.86 ± 0.10 m/s².

- $w$ = 1/0.22² = 20.7 and 1/0.10² = 100
- $\hat{\mu}$ = (20.7 × 9.70 + 100 × 9.86) / 120.7 = 9.833
- $\sigma_{\hat{\mu}}$ = 1/√120.7 = 0.091

**9.83 ± 0.09 m/s²**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The result lies closer to the more precise value, and it is more precise than either: 0.091 against 0.10. A measurement with a large uncertainty still adds information. The plain mean of the two, 9.78, would give it too much weight.

</div>

<!--
Speaker: before the numbers, ask the room to guess the combination of
9.70 ± 0.22 and 9.86 ± 0.10. Most say 9.78, the plain mean; it is 9.83. The
weights add. Every further measurement increases the sum of the weights and so
reduces the uncertainty, however little. (~3 min)
-->

---
hideInToc: true
---

# *g* from **Nine** Measurements

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🐍 **Every row of the table**

```python
data = np.loadtxt("data/processed/pendulum.csv",
                  delimiter=",", skiprows=1)
length = data[:, 0]         # cm
t10 = data[:, 1]            # s, 10 swings

g = (4 * np.pi**2 * (length / 100)
     / (t10 / 10)**2)
sg = g * np.sqrt((0.1 / length)**2
                 + (2 * 0.1 / t10)**2)
w = 1 / sg**2
print((w * g).sum() / w.sum(),
      1 / np.sqrt(w.sum()))
```

```text
9.804687035873261 0.04240703343795726
```

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_probability_weighted_mean.svg" style="display:block;margin:0 auto;max-height:265px;">

**$g$ = 9.80 ± 0.04 m/s²**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The uncertainties run from 0.22 m/s² for 20 cm to 0.10 for 100 cm: the same 0.1 s is a larger part of a shorter time. All nine error bars cross the result. For Gaussian errors about two in three are expected to, so the stated 0.1 s is larger than the scatter of these example values.

</div>

<!--
Speaker: the relative uncertainties are divided by the same units as the
values: 0.1 cm by the length in cm, 0.1 s by the time in s. One row gave
9.86 ± 0.10. Nine rows give 9.80 ± 0.04. Ask: all nine bars cross the result;
is that good? About six of nine should, so the stated 0.1 s is larger than
the real scatter. (~3 min)
-->

---
hideInToc: true
---

# The Four Questions, **Answered**

<img class="fig" src="/figures/viz_probability_mass.svg" style="display:block;margin:0 auto;max-height:140px;">

<div class="grid-2 gap-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📍 **One number**: the mean, 1864.10 MeV/c², the maximum of the likelihood for equal uncertainties.

</div>

<div class="card card-secondary card-glass pad-compact">

↔️ **One value**: the standard deviation $s$ = 25.57 MeV/c². More rows make it better known, not smaller.

</div>

<div class="card card-accent card-glass pad-compact">

🎯 **How well**: the standard error $s/\sqrt{N}$ = 0.08 MeV/c². The mean lies 8.7 of them below the D⁰ mass: a systematic error.

</div>

<div class="card card-info card-glass pad-compact">

📊 **The bar**: a count is Poisson, its variance equals its mean: 1916 ± 44. Checked: 34 against √1461 = 38.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

✅ One rule carried every uncertainty: for independent values the variances add. It gave √N, $s/\sqrt{N}$, and $g$ = 9.86 ± 0.10 m/s² from one pendulum row and 9.80 ± 0.04 m/s² from nine.

</div>

<!--
Speaker: back to the four questions of the opening slide, now answered with
numbers the room has seen computed. The figure is the mass column with its
mean and the band of ± s. The list of skills is on the workbook page, under
Take-aways. Do not cut this slide. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="2 % of a population has a condition. A test is positive for 90 % of those who have it and for 5 % of those who do not. A person tests positive. What is the probability that the person has the condition?"
  :options="[
    '90 %',
    '27 %',
    '2 %',
    '95 %'
  ]"
  :correct="1"
  explanation="Of 10 000 people, 200 have the condition and 180 of them test positive. Of the 9800 others, 490 test positive. 180 / (180 + 490) = 0.27. 90 % is the probability of a positive test given the condition, which is a different question."
/>

---
hideInToc: true
---

<MCQ
  question="A detector registers each particle with probability 0.8, independently. Five particles pass. What is the probability that exactly four are registered?"
  :options="[
    '0.80',
    '0.41',
    '0.33',
    '0.08'
  ]"
  :correct="1"
  explanation="Binomial with n = 5, k = 4, p = 0.8: there are 5 sequences with one miss, each with probability 0.8⁴ × 0.2 = 0.082, so 5 × 0.082 = 0.41. 0.33 is the probability of all five, 0.8⁵."
/>

---
hideInToc: true
---

<MCQ
  question="One bin of a histogram holds 400 rows. What is the uncertainty of this count, and what is it relative to the count?"
  :options="[
    '± 400, which is 100 %',
    '± 20, which is 5 %',
    '± 200, which is 50 %',
    '± 4, which is 1 %'
  ]"
  :correct="1"
  explanation="A count follows a Poisson distribution, whose standard deviation is the square root of its mean: √400 = 20. Relative to the count this is 1/√400 = 5 %. For 1 % the bin would need 10 000 rows."
/>

---
hideInToc: true
---

<MCQ
  question="144 measurements have a sample standard deviation of 12 units. What is the standard error of their mean, and how many measurements would halve it?"
  :options="[
    '12 units; 288 measurements',
    '1 unit; 576 measurements',
    '1 unit; 288 measurements',
    '0.083 units; 576 measurements'
  ]"
  :correct="1"
  explanation="The standard error is s/√N = 12/√144 = 1 unit. It falls like 1/√N, so half the standard error needs four times the data: 4 × 144 = 576. The standard deviation of the single values stays near 12."
/>

---
hideInToc: true
---

<MCQ
  question="The sides of a rectangle are a = 2.00 ± 0.02 m and b = 5.00 ± 0.10 m, measured independently. What is its area?"
  :options="[
    '10.00 ± 0.12 m²',
    '10.00 ± 0.22 m²',
    '10.00 ± 0.30 m²',
    '10.00 ± 0.002 m²'
  ]"
  :correct="1"
  explanation="For a product the relative uncertainties add in quadrature: 1 % for a and 2 % for b give √(1 + 4) = 2.2 %, which is 0.22 m². Adding the absolute uncertainties (0.12) or the relative ones without squares (3 %, 0.30) is wrong."
/>

---
hideInToc: true
---

<MCQ
  question="A measurement gives 5.3 ± 0.2 and the expected value is 4.7. How many standard deviations apart are they, and what is the two-sided p-value?"
  :options="[
    '0.6σ; p = 0.55',
    '3σ; p = 0.0027',
    '3σ; p = 0.32',
    '6σ; p = 2 × 10⁻⁹'
  ]"
  :correct="1"
  explanation="z = (5.3 − 4.7) / 0.2 = 3. For a Gaussian, 99.73 % of repetitions lie within 3σ, so a distance of 3σ or more has the probability 0.0027. This is the probability of such data if the expected value is right, not the probability that it is right."
/>

---
hideInToc: true
---

<MCQ
  question="Two independent measurements of the same quantity give 10.0 ± 0.1 and 10.6 ± 0.3. What is their weighted mean?"
  :options="[
    '10.30 ± 0.16',
    '10.06 ± 0.09',
    '10.30 ± 0.32',
    '10.06 ± 0.20'
  ]"
  :correct="1"
  explanation="The weights are 1/0.1² = 100 and 1/0.3² = 11.1. The weighted mean is (100 × 10.0 + 11.1 × 10.6) / 111.1 = 10.06, and its uncertainty is 1/√111.1 = 0.09. The plain mean, 10.30, gives the less precise value as much say as the precise one."
/>
