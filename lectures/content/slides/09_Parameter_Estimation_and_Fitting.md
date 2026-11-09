---
layout: cover
title: "Parameter Estimation and Fitting"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Parameter Estimation and Fitting

##### <span class="aims-badge">🔧 tool-agnostic · ♻️ reproducibility</span>

<!--
**Ask:** who has drawn a trend line in a spreadsheet? Where did its two numbers come from?
**Say:** today a fit is worked out by hand: what a model is, which numbers fit best, how sure they are, how a computer walks to them, and how to tell a good fit from a bad one. Everything on the weather log.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# All models are wrong but some are **useful**.
George E. P. Box, *Robustness in the Strategy of Scientific Model Building* (1979)

---
hideInToc: true
class: fill
---

# Is It Getting **Warmer**?

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

📈 The mean of each year of the weather log, 2016 to 2025.

</div>

<div class="card card-success card-glass pad-compact">

2017 → 2023: **+1.80 °C**

</div>

<div class="card card-warning card-glass pad-compact">

2023 → 2025: **−2.33 °C**

</div>

<div class="card card-info card-glass pad-compact">

❓ Which number answers the question?

</div>

</div>

<img class="fig" src="/figures/viz_fitting_year_means.svg">

</div>

<!--
**Ask:** hands up: warmer, colder, cannot tell?
**Say:** two years picked from ten give any answer we like. A line through all ten gives one number, and the lecture ends with that number and how sure it is.
**If asked:** the dashed line is the mean of all 87 552 hours, 7.16 °C.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# A Model Has **Parameters**

A formula with numbers left open. The data set them.

<!--
**Say:** first the simplest model, one number for a handful of values, and the tool that finds the best number: the derivative.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Three Models of the Weather **Log**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Parameters: one, μ; two, a and b; three, c, A and d₀. **Fitting** finds the values that match the data best.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_three_models.svg">

<!--
**Say:** a parameter is a number the formula leaves open. x is the year counted from 2016, d the day counted from 1 January 2016.
**Ask:** in the middle panel, what do a and b mean? a: °C per year; b: the value of the line in 2016.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Three Parts of a **Fit**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 A model with open parameters, data with their scatter, a measure of the miss. The fit: the parameter values with the **smallest miss**.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_parts.svg">

<!--
**Say:** every fit in physics, finance or machine learning has these three parts. Today: which measure of the miss, why, how to find its lowest point, and how sure that point is.
**If asked:** σ = 0.70 °C is how much the ten yearly means scatter around their mean (Lecture 8).
(~1.5 min)
-->

---
hideInToc: true
---

# Reading the **Formulas**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Symbol | Read | The four hours of 21 July 2019 |
| --- | --- | --- |
| $y_i$ | value number i | $y_1$ = 27.3, $y_4$ = 23.6 |
| $\sum_{i=1}^{N} y_i$ | add the values, i from 1 to N | 27.3 + 25.6 + 24.6 + 23.6 = 101.1 |
| $\prod_{i=1}^{N} p_i$ | multiply them | the likelihood L of ten years |
| $\hat\mu$ | the value the data choose, "mu hat" | 25.275 |
| $\hat y_i$ | the model's value for point i | 7.41 for 2016, on the best line |
| $\sigma$ | the scatter of one value | 0.70 °C for a yearly mean |

</div>

<!--
**Say:** the symbols of the lecture, each once, with the four hours where a number fits.
(~1.5 min)
-->

---
hideInToc: true
---

# Which μ Fits Four **Hours**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **21 July 2019, 20:00 to 23:00**

27.3, 25.6, 24.6, 23.6 °C

Model: every hour is μ. A miss: $y_i - \mu$.

$$S(\mu) = \sum_{i=1}^{4} (y_i - \mu)^2$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **μ = 25**

<div v-click>

misses: 2.3, 0.6, −0.4, −1.4

</div>

<div v-click>

squares: 5.29, 0.36, 0.16, 1.96

</div>

<div v-click>

$S(25) = 7.77$

</div>

</div>

</div>

<!--
**Say:** the evening of 21 July 2019, the four hours before the sensor failed. One number for all four: which one?
**Do:** three clicks: the misses, their squares, the sum.
**Ask:** which μ would give a smaller S?
(~2 min)
-->

---
hideInToc: true
class: fill
---

# S Is Smallest at the **Mean**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact table-compact">

| μ (°C) | S(μ) (°C²) |
| --- | --- |
| 24 | 13.97 |
| 25 | 7.77 |
| **25.275** | **7.47** |
| 26 | 9.57 |

The lowest point: 101.1 / 4 = **25.275**, the mean.

</div>

<img class="fig" src="/figures/viz_fitting_sum_squares.svg">

</div>

<!--
**Say:** S is a parabola in μ, with one lowest point. It lies at 25.275, the mean of the four hours.
**If asked:** S(μ) = 7.4675 + 4 (μ − 25.275)²: four hours, so the parabola rises four times as fast as one square.
(~1.5 min)
-->

---
hideInToc: true
---

# Why the **Squares**

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ➕ **Plain misses**

$\sum (y_i - \mu)$

μ = 100 gives −298.9: no lowest point.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **Sizes of misses**

$\sum |y_i - \mu|$

4.7 for every μ from 24.6 to 25.6: no single answer.

</div>

<div class="card card-success card-glass pad-compact">

## ◻️ **Squares**

$\sum (y_i - \mu)^2$

One lowest point. A large miss counts more: 2.3² = 5.29, 0.6² = 0.36.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Gaussian scatter, too, leads to the squares.

</div>

<!--
**Say:** the plain sum can be pushed as low as we like, so it ranks nothing. The sum of sizes is flat between the two middle values: any μ from 24.6 to 25.6 ties, the median's range. The squares give one answer.
**If asked:** the sum of sizes is the right measure for scatter with long tails; it is minimised by the median.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The **Derivative**: How Fast S Changes

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

Nudge μ by a small h:

$$\frac{dS}{d\mu} \approx \frac{S(\mu + h) - S(\mu)}{h}$$

At μ = 25, h = 0.001:

(7.767804 − 7.770000) / 0.001 = **−2.196**

Negative: S falls as μ grows. Zero: the bottom.

</div>

<img class="fig" src="/figures/viz_fitting_tangent.svg">

</div>

<!--
**Say:** the derivative is the slope of the curve at one point: how much S changes per unit of μ, for a very small step. The orange line touches the curve at 25 with slope −2.2; at the mean the touching line is flat.
**If asked:** S(25.001) = 7.767804. Smaller h gives −2.1996, −2.19996: the limit is −2.2.
(~2.5 min)
-->

---
hideInToc: true
---

# The Derivative of a **Square**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **One term,** $d = y - \mu$

$$(d - h)^2 - d^2 = -2dh + h^2$$

Divide by h: $-2d + h$. Let h shrink:

$$\frac{d}{d\mu}(y - \mu)^2 = -2\,(y - \mu)$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Checked**

<div v-click>

y = 27.3, μ = 25: d = 2.3

(2.29² − 2.3²) / 0.01 = −4.59 = −4.6 + 0.01

</div>

<div v-click>

All four hours:

$$\frac{dS}{d\mu} = -2\sum_i (y_i - \mu) = -2 \times 1.1 = -2.2$$

</div>

</div>

</div>

<!--
**Say:** raising μ by h shrinks every miss by h. The square changes by −2dh plus h², and the h² vanishes as h shrinks. A sum of terms has the sum of their derivatives.
**Do:** two clicks: one hour by the nudge, then all four by the rule; the nudge of the previous slide gave −2.196.
(~3 min)
-->

---
hideInToc: true
---

# The Mean Is the **Least-Squares** Value

<div class="card card-primary card-glass pad-compact mt-md">

## 🎯 **At the bottom the derivative is zero**

$$\frac{dS}{d\mu} = -2\sum_{i=1}^{N} (y_i - \hat\mu) = 0 \quad\Longrightarrow\quad \sum_i y_i = N\hat\mu \quad\Longrightarrow\quad \hat\mu = \frac{1}{N}\sum_i y_i$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🌡️ **Four hours**

$\hat\mu$ = 101.1 / 4 = **25.275 °C**

</div>

<div class="card card-success card-glass pad-compact">

## 📅 **Ten years**

$\hat\mu$ = 71.60 / 10 = **7.16 °C**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$\hat\mu$, "mu hat": the value the data choose. The mean is the number with the smallest sum of squared misses.

</div>

<!--
**Say:** setting the derivative to zero turns "find the lowest point" into an equation. Its solution is the mean, for any data. The yearly means give 7.16, the mean of the log.
(~2 min)
-->

---
hideInToc: true
---

# The Slope of S by Formula and by **Nudge**

```py {monaco-run} {autorun:false}
y = [27.3, 25.6, 24.6, 23.6]            # 21 July 2019, 20:00 to 23:00
def S(mu):                              # the sum of squared deviations
    total = 0
    for v in y:
        total = total + (v - mu) ** 2
    return total
h = 0.001                               # a small nudge
for mu in [24, 25, 26]:
    slope = -2 * (sum(y) - 4 * mu)      # the formula
    print(mu, round(slope, 3), round((S(mu + h) - S(mu)) / h, 3))   # 25 -2.2 -2.196
```

<!--
**Do:** press ▶. Each row: μ, the slope by the formula, the slope by the nudge.
**Say:** the two columns agree to the third decimal; the rest is the h² of the previous slide. A derivative worked out on paper is checked this way before a program uses it.
**Ask:** where does the sign change? Between 25 and 26: at 25.275.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# From Likelihood to **χ²**

Where the squares come from: the Gaussian of Lecture 8.

<!--
**Say:** the ten yearly means now. Each scatters around the model; the Gaussian says how probable each value is, and the most probable model has the smallest sum of squares.
(~0.5 min)
-->

---
hideInToc: true
---

# Where σ = 0.70 °C Comes **From**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 📅 **The scatter of the ten yearly means**

$$s = \sqrt{\frac{\sum_i (y_i - \bar y)^2}{N - 1}} = \sqrt{\frac{4.451}{9}} = 0.70\ \text{°C}$$

</div>

<div class="card card-warning card-glass pad-compact">

## ⏱️ **Not from the hours**

8.85 / √8760 = 0.09 °C: too small, since neighbouring hours are alike.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

σ: the uncertainty of **one yearly mean**, the same for every year.

</div>

<!--
**Say:** Lecture 8 found both numbers: the hours scatter by 8.85 °C, but a year of hours is not 8760 independent values, and the yearly means themselves scatter by 0.70 °C. That is the σ of each point of today's fit.
**If asked:** the 120 missing hours of July 2019 lower its mean by about 0.14 °C: filled with the 17.46 °C of 22–26 July in the other years, 2019 would be 7.41 instead of 7.27; well inside 0.70.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Ten Years Around a Flat **Line**

<div class="card card-info card-glass pad-compact mt-sm">

📊 Model: 7.16 °C every year. Each yearly mean scatters around it as a Gaussian of σ = 0.70 °C, the scatter of the ten (Lecture 8).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_gauss.svg">

<!--
**Say:** each orange bell is the probability density of a yearly mean if the model is right. The dotted line from each point to its bell is that density: high near the line, low for 2023 and 2025.
(~1.5 min)
-->

---
hideInToc: true
---

# How Probable Is **2016**?

<div class="card card-primary card-glass pad-compact mt-md">

## 🔔 **The Gaussian, the model in place of its mean**

$$p(y \mid \mu) = \frac{1}{\sigma\sqrt{2\pi}}\; e^{-(y - \mu)^2 / 2\sigma^2}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **y = 7.605, μ = 7.16, σ = 0.70**

<div v-click>

(7.605 − 7.16) / 0.70 = 0.64 standard deviations

</div>

<div v-click>

$e^{-0.64^2/2}$ = 0.82, and $0.70\sqrt{2\pi}$ = 1.75

</div>

<div v-click>

p = 0.82 / 1.75 = **0.47 per °C**

</div>

</div>

<!--
**Say:** a density, not a probability: 0.47 per °C means that a window 0.1 °C wide around 7.6 holds a chance of about 0.047.
**Do:** three clicks, one step each.
(~2 min)
-->

---
hideInToc: true
---

# The Likelihood of Ten **Years**

<div class="card card-primary card-glass pad-compact mt-md">

## ✖️ **Independent years: the densities multiply**

$$L(\mu) = \prod_{i=1}^{10} p(y_i \mid \mu)$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.47 | 0.37 | 0.29 | 0.56 | 0.51 | 0.57 | 0.41 | 0.15 | 0.56 | 0.14 |

L(7.16) = 0.47 × 0.37 × … × 0.14 ≈ **4 × 10⁻⁵**

</div>

<div class="card card-info card-glass pad-compact mt-md">

**Maximum likelihood**: the parameters that make L largest.

</div>

<!--
**Say:** L is the probability density of all ten values at once, read as a function of the model's parameters. A tiny number, and that is normal: ten densities below 1 multiplied.
**Ask:** which two years pull L down most? 2023 and 2025, the farthest from the line.
(~2 min)
-->

---
hideInToc: true
---

# Maximum Likelihood Is Minimum **χ²**

<div class="card card-primary card-glass pad-compact mt-md">

## 🪵 **The logarithm: a product becomes a sum**

$\ln(ab) = \ln a + \ln b$ and $\ln e^u = u$, so

$$-2\ln L = \sum_{i} \frac{\big(y_i - f(x_i)\big)^2}{\sigma^2} + \text{const} = \chi^2 + \text{const}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Line at 7.16**

−2 ln L = 20.33 = **9.08** + 11.25

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **Least squares**

Largest L, smallest χ²: the same parameters.

</div>

</div>

<!--
**Say:** f(x_i) is what the model says for point i: here 7.16 every year, or a line. The constant is 20 ln(0.70 √2π) = 11.25, the same for every model, so it never moves the minimum. With Gaussian scatter, the most probable model is the one with the smallest χ², "chi-squared".
**If asked:** with a different σ_i for each point, each term keeps its own σ_i²: a precise point counts more.
(~3 min)
-->

---
hideInToc: true
---

# χ² of the Flat Line, Year by **Year**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Year | y (°C) | y − 7.16 | pull | pull² |
| --- | --- | --- | --- | --- |
| 2016 | 7.605 | 0.445 | 0.64 | 0.40 |
| 2017 | 6.508 | −0.652 | −0.93 | 0.87 |
| 2018 | 7.975 | 0.815 | 1.16 | 1.35 |
| 2019 | 7.270 | 0.110 | 0.16 | 0.02 |
| 2020 | 6.831 | −0.329 | −0.47 | 0.22 |
| 2021 | 7.248 | 0.088 | 0.13 | 0.02 |
| 2022 | 6.600 | −0.560 | −0.80 | 0.64 |
| 2023 | 8.310 | 1.150 | 1.64 | 2.70 |
| 2024 | 7.273 | 0.113 | 0.16 | 0.03 |
| 2025 | 5.982 | −1.178 | −1.68 | 2.83 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## 📏 **The pull**

$\dfrac{y_i - f(x_i)}{\sigma}$: the miss in units of σ = 0.70.

</div>

<div class="card card-success card-glass pad-compact">

## ➕ **The sum**

χ² = 0.40 + 0.87 + … + 2.83 = **9.08**

</div>

<div class="card card-warning card-glass pad-compact">

2023 and 2025 give 5.53 of the 9.08.

</div>

</div>

</div>

<!--
**Say:** a point one σ away adds 1, two σ away adds 4. The squares make the far points count most.
**Do:** first row on the board: 7.605 − 7.16 = 0.445; / 0.70 = 0.64; squared, 0.40.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Two Guessed **Lines**

<div class="card card-info card-glass pad-compact mt-sm">

📐 $f(x) = a\,x + b$, x = years since 2016. The sticks are the misses. Which line is best of all?

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_guesses.svg">

<!--
**Say:** the grey sticks are the misses; χ² adds up their squares in units of σ. B misses 2025 by 1.62 °C, 2.3 σ: 5.34 of its 12.64.
**Ask:** where would you move line B to lower its χ²?
(~1.5 min)
-->

---
hideInToc: true
---

# Your Line, **Live**

```py {monaco-run} {autorun:false}
y = [7.6045, 6.5078, 7.9745, 7.2697, 6.8314, 7.2478, 6.5997, 8.3102, 7.2729, 5.9821]
a, b = 0.1, 6.7                         # <-- try your own line
chi2 = 0
for x in range(10):                     # x = years since 2016
    pull = (y[x] - (a * x + b)) / 0.70
    chi2 = chi2 + pull ** 2
print(round(chi2, 2))                   # 12.64
```

<div class="card card-warning card-glass pad-compact mt-md">

❓ Who can beat **9.08**, the flat line?

</div>

<!--
**Do:** press ▶: 12.64, line B. Then take two or three lines from the room, change a and b, run each.
**Say:** the list holds the ten yearly means, 2016 first. Guessing works, slowly.
**If asked:** a = 0, b = 7.16 gives 9.08; the best line, a = −0.0555, b = 7.41, gives 8.56.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# The Best Line in **Closed Form**

Two parameters, two derivatives, both set to zero.

<!--
**Say:** the derivative of the first section, now for two parameters at once. The answer is a formula: five sums of the data, pushed through by hand.
(~0.5 min)
-->

---
hideInToc: true
---

# The Derivatives of χ² for a **Line**

<div class="card card-primary card-glass pad-compact mt-md">

## 📐 **χ² of a line**

$$\chi^2(a, b) = \frac{1}{\sigma^2}\sum_{i=1}^{N} (y_i - a\,x_i - b)^2$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🧭 **Partial derivatives: one parameter moves, the other stays**

$$\frac{\partial\chi^2}{\partial a} = -\frac{2}{\sigma^2}\sum_i x_i\,(y_i - a\,x_i - b), \qquad \frac{\partial\chi^2}{\partial b} = -\frac{2}{\sigma^2}\sum_i (y_i - a\,x_i - b)$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

Raising a by h moves the miss of point i by $x_i h$: hence the extra $x_i$. At the lowest point both are **zero**.

</div>

<!--
**Say:** the rule of the square again: −2 times the miss, times how fast the miss changes with the parameter: x_i for a, 1 for b.
**If asked:** for line A (a = 0, b = 7.16), ∂χ²/∂a = 18.69; a nudge of 0.0001 gives 18.75. Positive: a smaller slope lowers χ².
(~2.5 min)
-->

---
hideInToc: true
---

# The Normal **Equations**

<div class="card card-primary card-glass pad-compact mt-md">

## 🟰 **Both derivatives zero, multiplied out (σ cancels)**

$$a\sum x_i^2 + b\sum x_i = \sum x_i y_i \qquad\qquad a\sum x_i + b\,N = \sum y_i$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ➕ **The data enter through five numbers**

$$N, \qquad \sum x_i, \qquad \sum y_i, \qquad \sum x_i^2, \qquad \sum x_i y_i$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

Two equations, two unknowns: the **normal equations**. Ten points or a million, still five sums.

</div>

<!--
**Do:** on the board, the second one: Σ(y_i − a x_i − b) = 0 splits into Σy_i − aΣx_i − N b = 0.
**Say:** σ is the same for every year, so it divides out: the best line does not depend on σ. Its uncertainty will.
(~2 min)
-->

---
hideInToc: true
---

# Slope and Intercept from the **Sums**

<div class="card card-primary card-glass pad-compact mt-md">

## ✂️ **Solve the two equations**

$$\Delta = N\sum x_i^2 - \Big(\sum x_i\Big)^2$$

$$\hat a = \frac{N\sum x_i y_i - \sum x_i \sum y_i}{\Delta} \qquad\qquad \hat b = \frac{\sum x_i^2 \sum y_i - \sum x_i \sum x_i y_i}{\Delta}$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

📋 The formula behind a spreadsheet's trend line.

</div>

<!--
**Say:** multiply the second equation by Σx_i, the first by N, subtract: b drops out and â is left. The same for b̂.
**If asked:** Δ is zero only when all x_i are equal: then no line is defined.
(~2 min)
-->

---
hideInToc: true
---

# The Ten Years in a **Table**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Year | x | y (°C) | x² | x·y |
| --- | --- | --- | --- | --- |
| 2016 | 0 | 7.605 | 0 | 0 |
| 2017 | 1 | 6.508 | 1 | 6.508 |
| 2018 | 2 | 7.975 | 4 | 15.950 |
| 2019 | 3 | 7.270 | 9 | 21.810 |
| 2020 | 4 | 6.831 | 16 | 27.324 |
| 2021 | 5 | 7.248 | 25 | 36.240 |
| 2022 | 6 | 6.600 | 36 | 39.600 |
| 2023 | 7 | 8.310 | 49 | 58.170 |
| 2024 | 8 | 7.273 | 64 | 58.184 |
| 2025 | 9 | 5.982 | 81 | 53.838 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

## ➕ **The five sums**

N = 10

Σx = 45

Σy = 71.60

Σx² = 285

Σxy = 317.62

</div>

<div class="card card-info card-glass pad-compact">

x = years since 2016. y: three decimals.

</div>

</div>

</div>

<!--
**Say:** x counts the years from 2016, so the numbers stay small: Σx = 0 + 1 + … + 9 = 45, Σx² = 285.
**Do:** let the room check one row: 2018, x = 2: x² = 4, x·y = 15.950.
(~2 min)
-->

---
hideInToc: true
---

# The Sums Pushed **Through**

<div class="card card-primary card-glass pad-compact mt-md">

## Δ

Δ = 10 × 285 − 45² = 2850 − 2025 = **825**

</div>

<div class="card card-secondary card-glass pad-compact mt-md" v-click>

## Slope â

â = (10 × 317.62 − 45 × 71.60) / 825 = (3176.2 − 3222.0) / 825 = **−0.056 °C a year**

</div>

<div class="card card-accent card-glass pad-compact mt-md" v-click>

## Intercept b̂

b̂ = (285 × 71.60 − 45 × 317.62) / 825 = (20 406.0 − 14 292.9) / 825 = **7.41 °C**

</div>

<div class="card card-success card-glass pad-compact mt-md" v-click>

**−0.56 °C per decade**, starting from 7.41 °C in 2016.

</div>

<!--
**Do:** one click per line; the room can follow on a calculator.
**Say:** the slope is a small difference of two large numbers, 3176.2 and 3222.0: keep every digit of the sums until the end.
(~2.5 min)
-->

---
hideInToc: true
class: fill
---

# The Best **Line**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

📉 **χ² = 8.56**, below A (9.08) and B (12.64).

</div>

<div class="card card-info card-glass pad-compact">

Through (4.5, 7.16): the middle year and the mean. 7.41 − 0.056 × 4.5 = 7.16.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_best_line.svg">

</div>

<!--
**Say:** no other line has a smaller χ². The dashed lines are the two guesses. The second normal equation, divided by N, says the line passes through the mean point.
(~1.5 min)
-->

---
hideInToc: true
---

# The Five Sums in **Python**

```py {monaco-run} {autorun:false}
y = [7.6045, 6.5078, 7.9745, 7.2697, 6.8314, 7.2478, 6.5997, 8.3102, 7.2729, 5.9821]
n, sx, sy, sxx, sxy = 10, 0, 0, 0, 0
for x in range(10):                     # x = years since 2016
    sx, sy = sx + x, sy + y[x]
    sxx, sxy = sxx + x * x, sxy + x * y[x]
d = n * sxx - sx ** 2
a = (n * sxy - sx * sy) / d
b = (sxx * sy - sx * sxy) / d
print(round(sx), round(sy, 2), sxx, round(sxy, 2), d)   # 45 71.6 285 317.62 825
print(round(a, 3), round(b, 2))                         # -0.056 7.41
```

<!--
**Do:** press ▶: the five sums, Δ, then the slope and the intercept of the previous slides.
**Say:** a loop, five running totals, two formulas. Nothing in it knows about weather: any two columns of numbers go through the same lines.
(~2 min)
-->

---
hideInToc: true
---

# Why x Counts from **2016**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📅 **x = the year itself**

Δ = 10 × 40 824 285 − 20 205² = 408 242 850 − 408 242 025 = 825

b̂ = **119.35 °C**: the line in the year 0

</div>

<div class="card card-success card-glass pad-compact">

## 📍 **x = years since 2016**

Δ = 2850 − 2025 = 825

b̂ = **7.41 °C**: the line in 2016

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same line, the same slope. The intercept is the line at **x = 0**: choose where x = 0 means something.

</div>

<!--
**Say:** with the calendar year, Δ is the difference of two nine-digit numbers that agree in their first six digits: a computer keeps enough digits, a calculator may not. And the intercept, 119 °C two thousand years ago, means nothing.
(~2 min)
-->

---
hideInToc: true
---

# The Slope as r Times the **Spreads**

<div class="card card-primary card-glass pad-compact mt-md">

## 📐 **With x and y measured from their means**

$$\hat a = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sum_i (x_i - \bar x)^2} = r\,\frac{s_y}{s_x}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Sums**

−4.581 / 82.5 = **−0.0555 °C a year**

</div>

<div class="card card-success card-glass pad-compact">

## 🔗 **Correlation**

r = −0.239, s_y = 0.703 °C, s_x = 3.03 years:

−0.239 × 0.703 / 3.03 = **−0.0555**

</div>

</div>

<!--
**Say:** the same slope, a third way: the correlation of Lecture 8, scaled from standard deviations of x to standard deviations of y. A weak correlation, −0.24, and a slope to match.
**If asked:** the five-sum formula is this one multiplied out.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# How Sure Is the **Slope**?

Another ten years would give another slope. How far could it lie?

<!--
**Say:** the uncertainty of a fitted parameter, from the shape of χ² around its lowest point.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# χ² Around Its **Minimum**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

📈 For each slope, the best intercept; then χ².

</div>

<div class="card card-secondary card-glass pad-compact">

A parabola: **8.56** at −0.56, **9.56** at −0.56 ± 0.77 °C per decade.

</div>

<div class="card card-success card-glass pad-compact">

The rule: **one σ raises χ² by 1**.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_chi2_slope.svg">

</div>

<!--
**Say:** move the slope away from its best value, let the intercept follow, and χ² climbs. Where it has risen by 1 lies one standard deviation of the slope. A narrow parabola means a well-known slope.
**Ask:** where does the parabola cross the dashed line of no trend? At 9.08, the flat line: less than 1 above the minimum.
(~2 min)
-->

---
hideInToc: true
---

# Why **Δχ² = 1**

<div class="card card-primary card-glass pad-compact mt-md">

## 🔔 **Near the minimum χ² is a parabola, so L is a Gaussian in a**

$$\chi^2(a) = \chi^2_{\min} + \frac{(a - \hat a)^2}{\sigma_a^2} \quad\Longrightarrow\quad L \propto e^{-\chi^2/2} \propto e^{-(a - \hat a)^2 / 2\sigma_a^2}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **At â ± σₐ**

$\left(\sigma_a / \sigma_a\right)^2 = 1$: χ² = 8.56 + 1 = **9.56**

</div>

<div class="card card-info card-glass pad-compact mt-md">

The width of that Gaussian is the uncertainty of the slope, σₐ.

</div>

<!--
**Say:** the likelihood of the slope is a Gaussian, the bell of Lecture 8; its σ is read off where χ² has risen by 1. Two σ raise χ² by 4.
(~2 min)
-->

---
hideInToc: true
---

# σₐ in Closed **Form**

<div class="card card-primary card-glass pad-compact mt-md">

## 📏 **Equal σ for every point**

$$\sigma_a = \frac{\sigma}{\sqrt{\sum_i (x_i - \bar x)^2}} = \sigma\sqrt{\frac{N}{\Delta}}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **The ten years**

σₐ = 0.70 × √(10 / 825) = 0.70 × 0.110 = **0.077 °C a year** = 0.77 °C per decade

</div>

<div class="card card-info card-glass pad-compact mt-md">

σ = 0.70 °C: the yearly means about their mean. No y in it: σ and the spread of the years decide it.

</div>

<!--
**Say:** Σ(x_i − x̄)² = 82.5 for the ten years: the farther apart the years, the better the slope is known. Doubling σ doubles σ_a.
**If asked:** â = Σ c_i y_i, a weighted sum of the ten y_i; the variances of independent terms add, so σ_a² = σ² Σ c_i² = σ² N / Δ.
**If asked:** σ from the residuals about the line instead, with n − 2 = 8: 0.72 °C and ± 0.80 per decade, the textbook error of a least-squares slope. The conclusion stays.
(~2 min)
-->

---
hideInToc: true
---

# The Intercept and Its **±**

<div class="card card-primary card-glass pad-compact mt-md">

## 📏 **The same way, for b**

$$\sigma_b = \sigma\sqrt{\frac{\sum x_i^2}{\Delta}} = 0.70 \times \sqrt{\frac{285}{825}} = 0.70 \times 0.588 = 0.41\ \text{°C}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📉 **Slope**

â = −0.056 ± 0.077 °C a year

</div>

<div class="card card-success card-glass pad-compact">

## 📍 **Intercept**

b̂ = 7.41 ± 0.41 °C, the line in 2016

</div>

</div>

<!--
**Say:** b is known less well than the mean of the ten years, ± 0.22, because 2016 lies at the edge of the data: the line pivots around its middle.
(~1.5 min)
-->

---
hideInToc: true
---

# The Line's Value for **2026**

<div class="card card-primary card-glass pad-compact mt-md">

## 🔮 **The line, one year past the data**

7.4099 − 0.0555 × 10 = 6.854 ≈ **6.85 °C**

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 📏 **Its ±: the mean, and the slope times the distance from 2020.5**

$$\sigma_f^2 = \frac{\sigma^2}{N} + (x - \bar x)^2\,\sigma_a^2 = 0.049 + 5.5^2 \times 0.0059 = 0.23, \qquad \sigma_f = 0.48$$

</div>

<div class="card card-success card-glass pad-compact mt-md">

One year scatters by 0.70 around the line: √(0.23 + 0.49) = 0.85. **2026: 6.0 to 7.7 °C.**

</div>

<!--
**Say:** the farther from the middle of the data, the more the uncertain slope matters: the band around a fitted line widens at both ends. A single year adds its own scatter on top.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Ten Years Cannot Show This **Trend**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

**−0.56 ± 0.77 °C per decade**, σ = 0.70 °C from the scatter of the yearly means

</div>

<div class="card card-info card-glass pad-compact">

Zero lies 0.7 σ away.

</div>

<div class="card card-warning card-glass pad-compact">

Within one σ: from −1.3 to +0.2: falling and rising lines alike.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_band.svg">

</div>

<!--
**Say:** the answer to the opening question, for this station: ten years do not say. Every line in the fan fits within one σ, and they all pass near the mean point.
**Ask:** is it then not getting warmer? Not shown either way: "cannot tell" is a result.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# What **± 0.77** Means

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

🔔 The slope's likelihood: a Gaussian of σₐ = 0.77 °C per decade.

</div>

<div class="card card-secondary card-glass pad-compact">

**68 %**: −0.56 ± 0.77, from −1.3 to +0.2

</div>

<div class="card card-accent card-glass pad-compact">

**95 %**: −0.56 ± 1.54, from −2.1 to +1.0

</div>

<div class="card card-success card-glass pad-compact">

Zero, no trend, lies inside both.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_slope_gauss.svg">

</div>

<!--
**Say:** the 68/95 rule of Lecture 8, now for a fitted slope. Repeating the ten years many times, about two in three slopes would fall within one σ of the true one.
**If asked:** with only 8 degrees of freedom and σ taken from the data, the ranges are a little wider still (Student's t); the conclusion stays.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The ± with More **Years**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

σₐ falls as $N^{-3/2}$: more years, and farther apart.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

| Years | σₐ (°C per decade) |
| --- | --- |
| 10 | 0.77 |
| 20 | 0.27 |
| 40 | 0.10 |

</div>

</div>

<img class="fig" src="/figures/viz_fitting_years_needed.svg">

</div>

<!--
**Say:** with the same σ = 0.70 a year, 20 years would put a slope of 0.56 per decade two σ from zero; 40 years would measure 0.2 per decade.
**If asked:** for N years one apart, Σ(x_i − x̄)² = N(N² − 1)/12.
(~1.5 min)
-->

---
layout: section
hideInToc: true
---

# Walking **Downhill**

When the derivatives cannot be solved, follow them a step at a time.

<!--
**Say:** the closed form needed a model whose derivatives can be solved by hand. Most cannot. A computer then walks downhill: the same idea that trains every neural network.
(~0.5 min)
-->

---
hideInToc: true
---

# No Closed Form for the **Cycle**

<div class="card card-primary card-glass pad-compact mt-md">

## 🌊 **The yearly cycle, three parameters**

$$T(d) = c - A\cos\frac{2\pi\,(d - d_0)}{365.25}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🚫 **d₀ inside the cosine**

$\partial\chi^2 / \partial d_0 = 0$ cannot be solved for d₀.

</div>

<div class="card card-success card-glass pad-compact">

## 👣 **What is left**

χ² and its slope at any point. Step downhill, repeat.

</div>

</div>

<!--
**Say:** d is the day, counted from 1 January 2016; c is the level, A the amplitude, d₀ the coldest day. The derivative with respect to d₀ has d₀ inside a cosine, and no rearranging gets it out.
(~1.5 min)
-->

---
hideInToc: true
---

# The Update **Rule**

<div class="card card-primary card-glass pad-compact mt-md">

## 👣 **Gradient descent**

$$\theta \;\leftarrow\; \theta - \eta\,\frac{dS}{d\theta}$$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## θ

the parameter: μ, a, b, d₀

</div>

<div class="card card-accent card-glass pad-compact">

## η

the **step size** (learning rate), chosen by hand

</div>

<div class="card card-info card-glass pad-compact">

## −dS/dθ

downhill; it shrinks near the bottom

</div>

</div>

<!--
**Say:** where the slope is negative, θ grows; where positive, θ shrinks: always downhill. The steps shorten on their own, because the slope goes to zero at the bottom.
**If asked:** "gradient" is the list of all partial derivatives; for one parameter it is the derivative.
**If asked:** machine learning calls the number it minimises the loss; here it is S.
(~2 min)
-->

---
hideInToc: true
---

# Three Steps by **Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **The four hours**

$\dfrac{dS}{d\mu} = -2\,(101.1 - 4\mu)$

Start μ = 20, η = 0.1.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

| Step | μ | dS/dμ | μ − 0.1 × dS/dμ |
| --- | --- | --- | --- |
| 1 | 20 | −42.2 | **24.22** |
| 2 | 24.22 | −8.44 | **25.064** |
| 3 | 25.064 | −1.688 | **25.233** |

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

The gap to 25.275 shrinks fivefold each step: 5.275, 1.055, 0.211, 0.042.

</div>

<!--
**Do:** the first row on the board: −2 × (101.1 − 80) = −42.2; 20 + 0.1 × 42.2 = 24.22.
**Say:** each step closes four fifths of the gap, without knowing where the bottom is.
(~2.5 min)
-->

---
hideInToc: true
class: fill
---

# A Step That Is Too **Large**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ η = 0.3: each step overshoots, and the gap grows 1.4 times. η = 0.25: 20 → 30.55 → 20 … forever. A step works only for η < 2 / 8 = 0.25.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_descent_hours.svg">

<!--
**Say:** 8 is how fast the slope changes, the second derivative of S: twice the four hours. A step longer than twice the distance to the bottom lands higher on the other side.
**Ask:** a step that is too small: safe, but how slow? η = 0.01 closes only 8 % of the gap per step.
(~2 min)
-->

---
hideInToc: true
---

# Each Step Multiplies the Gap by **1 − 8η**

<div class="card card-primary card-glass pad-compact mt-md">

## ✏️ **One step, the gap to the mean**

$\dfrac{dS}{d\mu} = -2N\,(\hat\mu - \mu)$, so

$$\mu_{\text{new}} - \hat\mu = (1 - 2N\eta)\,(\mu - \hat\mu) = (1 - 8\eta)\,(\mu - \hat\mu)$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| η | 0.01 | 0.1 | 0.25 | 0.3 |
| --- | --- | --- | --- | --- |
| 1 − 8η | 0.92 | 0.2 | −1 | −1.4 |
| each step | creeps | settles | swings forever | flies off |

</div>

<!--
**Say:** the whole behaviour in one factor. Between 0 and 1: steady approach. Between −1 and 0: overshoot that still settles. −1: a swing that never ends. Beyond: each step lands farther away.
**Do:** check η = 0.1 against the table of three steps: the gap 5.275, then 1.055, 0.211.
(~2 min)
-->

---
hideInToc: true
---

# Choose the Step Size, **Live**

```py {monaco-run} {autorun:false}
y = [27.3, 25.6, 24.6, 23.6]            # 21 July 2019, 20:00 to 23:00
mu, eta = 20.0, 0.1                     # <-- try eta = 0.25, 0.3, 0.01
for step in range(1, 6):
    slope = -2 * (sum(y) - 4 * mu)      # dS/dmu
    mu = mu - eta * slope
    print(step, round(mu, 3))           # 1 24.22 2 25.064 3 25.233 4 25.267 5 25.273
```

<div class="grid-2 mt-md gap-md" v-click>

<div class="card card-warning card-glass pad-compact">

η = 0.3: 32.66, 14.936, 39.75, 5.011, 53.645

</div>

<div class="card card-info card-glass pad-compact">

η = 0.01: 20.422, 20.81, 21.167, 21.496, 21.798

</div>

</div>

<!--
**Do:** press ▶ with 0.1, then change eta to 0.3, 0.25 and 0.01, pressing ▶ each time; the click shows two of the runs, for a room without the network.
**Ask:** before each run: will it settle, swing or fly off?
(~2.5 min)
-->

---
hideInToc: true
---

# The Update Rule for a **Line**

<div class="card card-primary card-glass pad-compact mt-md">

## 👣 **One step for each, with** $\hat y_i = a\,x_i + b$ **and** $S = \sum (\hat y_i - y_i)^2$

$$a \leftarrow a - \eta \sum_i 2\,(\hat y_i - y_i)\,x_i \qquad\qquad b \leftarrow b - \eta \sum_i 2\,(\hat y_i - y_i)$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **From a = 0, b = 7, η = 0.003**

<div v-click>

slopes: ∂S/∂a = −5.24, ∂S/∂b = −3.20

</div>

<div v-click>

a = 0 + 0.003 × 5.24 = **0.0157**, b = 7 + 0.003 × 3.20 = **7.0096**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The miss of the model, times the input: one term per point.

</div>

<!--
**Say:** S is χ² without the σ, which does not move the minimum. ŷ is what the model predicts, y the data; their difference times x_i drives the slope, the difference alone drives the intercept.
(~2.5 min)
-->

---
hideInToc: true
---

# Gradient Descent on Ten **Years**

```py {monaco-run} {autorun:false}
y = [7.6045, 6.5078, 7.9745, 7.2697, 6.8314, 7.2478, 6.5997, 8.3102, 7.2729, 5.9821]
a, b, eta = 0.0, 7.0, 0.003             # the start and the step size
for step in range(1, 501):
    ga, gb = 0, 0
    for x in range(10):                 # x = years since 2016
        r = a * x + b - y[x]            # the model minus the data
        ga, gb = ga + 2 * r * x, gb + 2 * r
    a, b = a - eta * ga, b - eta * gb
    if step in (1, 2, 3, 100, 500):
        print(step, round(a, 4), round(b, 3))   # ... 500 -0.0555 7.41
```

<!--
**Do:** press ▶: steps 1, 2, 3, 100, 500. Then set eta = 0.004 and run again.
**Say:** after 500 steps the closed form: −0.0555 and 7.41. With 0.004 the steps grow instead.
**If asked:** the first steps swing the slope up and down: 0.0157, 0.0020, 0.0105.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# The Path **Downhill**

<div class="card card-info card-glass pad-compact mt-sm">

🗺️ The contours of S(a, b), the path from (0, 7). A zigzag across a narrow valley, then along it: 500 steps to (−0.56 per decade, 7.41).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_descent_line.svg">

<!--
**Say:** across the valley S is steep, along it nearly flat: the steepness differs 103 times, and one η has to suit both. Right: how far S still is from its minimum, falling tenfold every 60 steps or so.
(~1.5 min)
-->

---
layout: section
hideInToc: true
---

# A **Curve**: the Yearly Cycle

Three parameters, one of them inside a cosine.

<!--
**Say:** the same steps on a model that is not a line: the cycle of the seasons, fitted to the daily means.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Daily Means of Ten **Years**

<div class="card card-info card-glass pad-compact mt-sm">

📅 3648 days with 24 measured hours (five days of July 2019 are missing). Ten waves: no line can follow this.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_daily.svg">

<!--
**Ask:** read the waves: about where is the middle, how high is the summer above it, when is the coldest day?
**Say:** these three readings are the three parameters of the model.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# A Cosine with Three **Parameters**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

$$T(d) = c - A\cos\frac{2\pi(d - d_0)}{365.25}$$

</div>

<div class="card card-secondary card-glass pad-compact">

**c**: the level. **A**: the amplitude, half of summer minus winter. **d₀**: the coldest day.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_cycle_parts.svg">

</div>

<!--
**Say:** the ten years folded onto one, each day at its place in the year. At d = d₀ the cosine is 1 and T = c − A, the coldest; half a year later it is −1 and T = c + A.
**If asked:** 365.25 days per turn, so the leap days keep the cycle in step.
(~2 min)
-->

---
hideInToc: true
---

# Two Days Pushed **Through**

<div class="card card-primary card-glass pad-compact mt-md">

## 👁️ **Read off the plot:** c = 7, A = 11, d₀ = 15

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ❄️ **16 January 2016, d = 15**

2π (15 − 15) / 365.25 = 0, cos 0 = 1

T = 7 − 11 × 1 = **−4 °C**

</div>

<div class="card card-accent card-glass pad-compact" v-click>

## ☀️ **17 July 2016, d = 198**

2π (198 − 15) / 365.25 = 3.148, cos = −1.000

T = 7 + 11 = **18 °C**

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

With these values the misses of 3648 days: **2.952 °C** root mean square.

</div>

<!--
**Say:** starting values read off a plot are good enough when they put the curve near the data; the descent does the rest.
**If asked:** root mean square: the square root of the mean squared miss, a typical miss in °C.
(~2 min)
-->

---
hideInToc: true
---

# The Descent from the Starting **Values**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Step | c | A | d₀ | rms miss |
| --- | --- | --- | --- | --- |
| 0 | 7.00 | 11.00 | 15.0 | 2.952 |
| 1 | 7.18 | 11.09 | 15.0 | 2.944 |
| 10 | 7.18 | 11.18 | 15.2 | 2.943 |
| 100 | 7.18 | 11.18 | 15.8 | 2.941 |
| 300 | 7.18 | 11.18 | 15.9 | 2.941 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

The update rule, three derivatives at once, η = 0.5.

</div>

<div class="card card-info card-glass pad-compact">

c settles in 1 step, A in 10, d₀ in 300: the misses change little along d₀.

</div>

</div>

</div>

<!--
**Say:** the descent minimised the mean squared miss of the 3648 days, so η can be 0.5. A shift of the coldest day by one day changes the misses very little: the slow direction.
**If asked:** a fitting program also uses the curvature, and takes larger steps where the valley is flat: the Newton and Levenberg–Marquardt methods.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Fitted **Cycle**

<div class="card card-success card-glass pad-compact mt-sm">

🌊 c = **7.18 °C**, A = **11.18 °C**, d₀ = **15.9**: the coldest day 16 January (−4.00 °C), the warmest 17 July (18.36 °C).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_cycle_fit.svg">

<!--
**Say:** one curve with three numbers describes 3648 days to within about 3 °C. Summer and winter differ by 2A = 22.4 °C.
**Ask:** where does the curve miss most? In cold spells, January 2017, 2019 and 2025, up to 9.5 °C below it, and the warm Junes of 2018 and 2019, up to 10.4 °C above.
(~1.5 min)
-->

---
layout: section
hideInToc: true
---

# **Residuals**: What the Model Leaves

A good model leaves only scatter.

<!--
**Say:** a fit always returns numbers. Whether to believe them is read from what is left over: the residuals, and χ².
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Residuals of the **Line**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

$r_i = y_i - \hat y_i$: what the line leaves.

</div>

<div class="card card-secondary card-glass pad-compact">

They add up to **0**. The largest, 2023: +1.29 °C, 1.8 σ.

</div>

<div class="card card-success card-glass pad-compact">

No pattern: up and down, no run.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_line_resid.svg">

</div>

<!--
**Say:** the residuals sum to zero because of the second normal equation. Seven of ten lie within ±σ, as a Gaussian would have it.
(~1.5 min)
-->

---
hideInToc: true
---

# The **Pulls** of the Line

<div class="card card-primary card-glass pad-compact mt-md table-compact">

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.28 | −1.21 | 0.97 | 0.04 | −0.51 | 0.17 | −0.68 | 1.84 | 0.44 | −1.33 |

pull = residual / σ, σ = 0.70 °C

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🎯 **Around 0**

They add up to 0.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **Two in three within ±1**

Here 7 of 10.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚠️ **One in 20 beyond ±2**

Here none.

</div>

</div>

<!--
**Say:** pulls have no unit, so points with different σ can be compared on one scale. These three checks describe a Gaussian of width 1: what a right model with the right σ leaves.
(~1.5 min)
-->

---
hideInToc: true
---

# What χ² Should **Be**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **One per point**

A right model: each pull² averages 1.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➖ **Minus one per parameter**

Each fitted parameter takes about 1 off χ².

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$$\langle\chi^2\rangle = N - k = \text{ndf}, \qquad \text{the degrees of freedom}$$

</div>

<div class="card card-success card-glass pad-compact mt-md">

The line: N = 10, k = 2, ndf = 8. χ² = 8.56: **1.07 per degree of freedom**.

</div>

<!--
**Say:** a line through two points always has χ² = 0: two parameters, no freedom left. So the expected χ² counts only the points the parameters did not use up.
**If asked:** χ² for a right model scatters around ndf by √(2 ndf), 4 for ndf = 8.
(~2 min)
-->

---
hideInToc: true
---

# When χ² Is Not a **Test**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔁 **σ = 0.70 came from these ten points**

The flat line: χ² = 9.08 for ndf = 9, by construction.

</div>

<div class="card card-success card-glass pad-compact">

## 🔬 **A test needs σ from elsewhere**

The instrument's stated error, or repeated measurements.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

χ² far above ndf: a missed pattern or σ too small. Far below: σ too large.

</div>

<!--
**Say:** σ was the scatter of the yearly means around their mean. Then χ² of the flat line is (N − 1) s²/σ², 9 up to the rounding of σ: it cannot fail. Honest, but no test.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Residuals of the **Cycle**

<div class="card card-info card-glass pad-compact mt-sm">

🌀 sd **2.94 °C**. Runs of warm and cold weeks: a day's residual predicts the next day's, **r = 0.875**.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_cycle_resid.svg">

<!--
**Say:** left: 2024, day by day; the weather stays warm or cold for a week or two. Right: every day's residual against the next day's: a tight cloud along the diagonal. r is the correlation of Lecture 8.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# Neighbouring Days Are **Alike**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

📉 Days taken as independent: A = 11.18 **± 0.07** °C

</div>

<div class="card card-success card-glass pad-compact">

📅 One fit per year: 10.41 to 12.60, mean 11.20, scatter 0.79: **± 0.25** °C

</div>

<div class="card card-info card-glass pad-compact">

0.79 / √10 = 0.25: 3.6 times the ± of the fit. As 7.16 ± 0.03 against ± 0.22 in Lecture 8.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_amplitudes.svg">

</div>

<!--
**Say:** 3648 days are not 3648 independent measurements: a warm week counts seven times. Ten separate years are close to independent, and their scatter gives the honest ±.
(~2 min)
-->

---
hideInToc: true
---

# The Same Trend from 3648 **Days**

<div class="card card-primary card-glass pad-compact mt-md">

## 🌊 **The cycle plus a slope k**

$$T(d) = c - A\cos\frac{2\pi(d - d_0)}{365.25} + k\,\frac{d}{3652.5}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📉 **Days taken as independent**

k = **−0.57 ± 0.17 °C per decade**: 3.4 σ from zero?

</div>

<div class="card card-success card-glass pad-compact">

## 📅 **The ten yearly means**

−0.56 **± 0.77**: the same slope, a ± more than four times larger.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Many alike points give a small ± that is wrong: a common false discovery.

</div>

<!--
**Say:** the daily means hold the same information about the trend as the yearly means, and the fit agrees on the slope. Only the ± differs: the daily fit counts each warm or cold spell many times over.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Too Few **Parameters**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ A constant leaves the whole cycle in its residuals. A second cosine (k = 5) gains nothing: 2.94 °C again.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_too_few.svg">

<!--
**Say:** a pattern left in the residuals names the missing term: here a wave of one year. Once the residuals look like scatter, a further term gains almost nothing: 2.942 to 2.936 °C.
(~1.5 min)
-->

---
hideInToc: true
---

# Too Many **Parameters**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📈 **Polynomials through the ten years**

| Degree | k | χ² | ndf | 2026 (°C) |
| --- | --- | --- | --- | --- |
| 0 | 1 | 9.08 | 9 | 7.16 |
| 1 | 2 | 8.56 | 8 | 6.85 |
| 3 | 4 | 6.83 | 6 | 5.18 |
| 5 | 6 | 4.03 | 4 | −1.42 |
| 8 | 9 | 0.53 | 1 | 93.25 |
| 9 | 10 | 0.00 | 0 | 306.66 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

## 🎢 **Every term lowers χ²**

and the forecast for 2026 goes wild.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧵 **Degree 9**

Ten parameters, ten points: χ² = 0, nothing left to test.

</div>

</div>

</div>

<!--
**Say:** a polynomial of degree 9 has ten free numbers and passes through every point. It follows the weather of each year, not the climate, and its next value is nonsense.
**Ask:** which model would you use for 2026? The constant or the line: their forecasts, 7.16 and 6.85, differ by less than one year's scatter.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# A Curve Through Every **Point**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

🎢 Degree 9 hits all ten years and says **307 °C** for 2026.

</div>

<div class="card card-success card-glass pad-compact">

The line says 6.85 °C.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_too_many.svg">

</div>

<!--
**Say:** between the points the curve swings wildly, and beyond the last one it shoots off. Fitting the noise is called overfitting.
(~1 min)
-->

---
hideInToc: true
---

# How Many **Parameters**?

<div class="card card-primary card-glass pad-compact mt-md">

## ⚖️ **χ² near ndf, with the fewest parameters**

A parameter earns its place by lowering χ² by clearly more than 1.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🌊 **The cycle**

A constant to a cosine: sd 8.43 → 2.94 °C. Needed.

</div>

<div class="card card-warning card-glass pad-compact">

## 📉 **The slope of ten years**

χ² 9.08 → 8.56: **−0.52**. Not needed yet.

</div>

</div>

<!--
**Say:** the slope lowered χ² by less than 1: the data do not ask for it. The same answer as −0.56 ± 0.77: a trend cannot be told from zero.
**If asked:** a parameter that the data do not need lowers χ² by about 1 on average, from the scatter alone.
(~2 min)
-->

---
hideInToc: true
---

# Reading the **Residuals**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🌊 **A pattern**

A term is missing. A constant through the daily means leaves the whole cycle: sd 8.43 °C.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔗 **Runs**

The points are not independent: next-day r = 0.875. The ± is too small.

</div>

<div class="card card-accent card-glass pad-compact">

## 📍 **One point far off**

Check its source. 2019 typed as 2.27: pull −6.2, χ² = 52.5 for 8, slope +0.35.

</div>

<div class="card card-info card-glass pad-compact">

## ⚖️ **χ² far from ndf**

A wrong model, or a wrong σ.

</div>

</div>

<!--
**Say:** four things a residual plot shows that the fitted numbers hide. One mistyped value, 2.27 for 7.27, flips the slope to +0.35 per decade, and only its pull of −6 gives it away.
**If asked:** a point is corrected or removed only with a reason found in its source, never because it fits badly.
(~2 min)
-->

---
hideInToc: true
---

# A Shift the Fit Cannot **See**

<div class="card card-warning card-glass pad-compact mt-md">

## 🔧 **Suppose a new sensor from 2021 reads 0.5 °C high**

The five later years rise by 0.5 °C; the fit runs as before.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📉 **As measured**

−0.56 ± 0.77 °C per decade, χ² = 8.56

</div>

<div class="card card-secondary card-glass pad-compact">

## 📈 **With the shift**

**+0.20** ± 0.77 °C per decade, χ² = 9.50: still a good fit

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The ± is **statistical**: the scatter of the points. An error shared by many points is **systematic**: found in the station's records, not in χ².

</div>

<!--
**Say:** a step of 0.5 °C, smaller than one year's scatter, turns the sign of the trend, and neither χ² nor the residuals raise an alarm. This is why stations keep a log of every sensor change, and why physicists list their systematic uncertainties next to the statistical one.
**If asked:** the weights of 2021 to 2025 in the slope add to 0.152; 0.5 × 0.152 = 0.076 °C a year, 0.76 per decade.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Wrap-up**

A fit is a number, its ±, its χ², and the model behind it.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# The Same Line by Every **Method**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Method | a (°C a year) | b (°C) |
| --- | --- | --- |
| The five sums, by hand | −0.056 | 7.41 |
| The five sums, a loop in Python | −0.056 | 7.41 |
| Gradient descent from (0, 7), 500 steps | −0.0555 | 7.410 |

</div>

<div class="card card-success card-glass pad-compact mt-md">

🔧 A spreadsheet's trend line or a fitting library gives the same two numbers: least squares has one answer. A different answer means a different model, σ or data.

</div>

<!--
**Say:** the method is a tool and can be swapped; the model, the data and σ decide the result. That is what tool-agnostic means for a fit.
**If asked:** a spreadsheet's SLOPE and INTERCEPT use the formula of the five sums.
(~1.5 min)
-->

---
hideInToc: true
---

# Reporting a **Fit**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **What a reader needs**

1. The model, as a formula
2. The data, and where σ comes from
3. The method
4. Each parameter: value ± uncertainty, unit
5. χ² and ndf
6. A figure: data, model, residuals
7. What the ± leaves out

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

## 📉 **The trend**

"A least-squares line through the ten yearly means, 2016–2025, σ = 0.70 °C each from their scatter: −0.56 ± 0.77 °C per decade, χ² = 8.56 for 8."

</div>

<div class="card card-success card-glass pad-compact">

## 🌊 **The cycle**

"A cosine fitted to 3648 daily means: A = 11.18 ± 0.25 °C (scatter of one-year fits), coldest on 16 January."

</div>

</div>

</div>

<!--
**Say:** two sentences hold everything another person needs to check the number or redo it. The ± of the cycle is the one from ten separate years; the fit's own ± 0.07 leaves out that neighbouring days are alike.
(~2 min)
-->

---
hideInToc: true
---

# A **Checklist** for a Fit

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Is the **model** chosen from a plot of the data, with the fewest parameters?

</div>

<div class="card card-secondary card-glass pad-compact">

✅ Is **σ** stated, with where it comes from?

</div>

<div class="card card-accent card-glass pad-compact">

✅ Do the **residuals** look like scatter: no pattern, no runs?

</div>

<div class="card card-info card-glass pad-compact">

✅ Is **χ²** near ndf, and is σ from outside the fitted points?

</div>

<div class="card card-success card-glass pad-compact">

✅ Is the **±** honest: independent points, systematic errors named?

</div>

</div>

<!--
**Say:** each line is a slide of today: the yearly cycle chosen from the waves, σ = 0.70 from the scatter, the runs in the residuals of the cycle, χ² against ndf, the ± 0.07 that should be ± 0.25, and the sensor shift.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# Is It Getting Warmer: the **Answer**

<div class="fig-fill grid-side mt-sm">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

Two picked years: +1.80 or −2.33 °C.

</div>

<div class="card card-success card-glass pad-compact">

All ten, fitted: **−0.56 ± 0.77 °C per decade**. Ten years cannot tell.

</div>

<div class="card card-info card-glass pad-compact">

20 years would measure ± 0.27; 40 years ± 0.10.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_band.svg">

</div>

<!--
**Say:** back to the opening slide. Every year counts once, the scatter sets the ±, and the honest answer for this station is "not yet measurable".
**Ask:** what would you need to answer it? More years, from the same station and the same sensor.
(~1.5 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Name a model's **parameters**, and find the mean as the **least-squares** value

</div>

<div class="card card-success card-glass pad-compact">

✅ Take a **derivative**, and check it with a small nudge

</div>

<div class="card card-success card-glass pad-compact">

✅ Derive **χ²** from the Gaussian likelihood, and compute it point by point

</div>

<div class="card card-success card-glass pad-compact">

✅ Fit a **straight line** from five sums, with its **uncertainty** from Δχ² = 1

</div>

<div class="card card-success card-glass pad-compact">

✅ Walk downhill by **gradient descent**, and choose a step size that works

</div>

<div class="card card-success card-glass pad-compact">

✅ Read **residuals** and χ², and spot too few or too many **parameters**

</div>

</div>

<!--
**Say:** one line per section, each with a number from today: 25.275, −2.2, 9.08, −0.56 ± 0.77, η < 0.25, 307 °C.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

Derivations, matrices, faster minimisers, and two fits from physics.

<!--
**Say:** optional: for the time left, or to read after the lecture.
(~0.5 min)
-->

---
hideInToc: true
---

# σₐ, **Derived**

<div class="card card-primary card-glass pad-compact mt-md">

## ➕ **â is a weighted sum of the yᵢ**

$$\hat a = \sum_i c_i\,y_i, \qquad c_i = \frac{N x_i - \sum x_j}{\Delta}: \quad -0.0545,\ -0.0424,\ \dots,\ 0.0545$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ➡️ **Independent yᵢ, each with σ: the variances add**

$$\sigma_a^2 = \sigma^2 \sum_i c_i^2 = \sigma^2\,\frac{N}{\Delta} = 0.49 \times 0.01212 = 0.00594, \qquad \sigma_a = 0.077$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

Σcᵢ² = (N²Σx² − 2N(Σx)² + N(Σx)²) / Δ² = N / Δ. The weights are largest for the first and the last year.

</div>

---
hideInToc: true
class: fill
---

# Slope and Intercept Are **Correlated**

<div class="card card-info card-glass pad-compact mt-sm">

🔗 cov(a, b) = −σ² Σx / Δ = −0.0267, ρ = −0.84: a steeper line through (4.5, 7.16) starts higher. Count x from mid-2020 and ρ = 0, b = **7.16 ± 0.22**: the mean of Lecture 8.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_ellipse.svg">

---
hideInToc: true
---

# The Normal Equations as **Matrices**

<div class="card card-primary card-glass pad-compact mt-md">

## 🧱 **The ten years**

$$\begin{pmatrix} 285 & 45 \\ 45 & 10 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 317.62 \\ 71.60 \end{pmatrix} \quad\Longrightarrow\quad a = -0.0555, \; b = 7.410$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 📐 **Any model linear in its parameters**

$$A^{\mathsf T}\!A\,\hat\theta = A^{\mathsf T}\mathbf y, \qquad V = \sigma^2 \big(A^{\mathsf T}\!A\big)^{-1}$$

A: one row per point, one column per parameter: here $(x_i, 1)$.

</div>

<div class="card card-info card-glass pad-compact mt-md">

V for the ten years: σₐ² = 0.0059, σ_b² = 0.169, cov = −0.0267, the numbers of the last slides.

</div>

---
hideInToc: true
---

# The Cycle as a Linear **Model**

<div class="card card-primary card-glass pad-compact mt-md">

## 🔀 **cos(u − v) = cos u cos v + sin u sin v**

$$c - A\cos\big(\omega(d - d_0)\big) = c + \alpha\cos\omega d + \beta\sin\omega d, \qquad \omega = \frac{2\pi}{365.25}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Linear in c, α, β**

Three columns: 1, cos ωd, sin ωd. Normal equations, no descent: c = 7.177, α = −10.763, β = −3.023.

</div>

<div class="card card-success card-glass pad-compact">

## ↩️ **Back to A and d₀**

A = √(α² + β²) = 11.18. d₀ from the angle of (−α, −β): 15.9.

</div>

</div>

---
hideInToc: true
---

# Newton's Step and **Levenberg–Marquardt**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏞️ **Why the descent is slow**

The curvature of S across the valley is 103 times that along it. One η, small enough across, creeps along.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **Newton: use the curvature too**

$$\delta = -H^{-1}\,\nabla S$$

From (0, 7), one step lands on (−0.0555, 7.410).

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

H: the second derivatives, $2\begin{pmatrix} 285 & 45 \\ 45 & 10 \end{pmatrix}$. **Levenberg–Marquardt** takes short downhill steps far away and Newton steps near the bottom: what fitting programs use.

</div>

---
hideInToc: true
class: fill
---

# The χ² Distribution and the **p-value**

<div class="card card-info card-glass pad-compact mt-sm">

🎲 If model and σ are right, χ² follows this curve. p: the chance of a χ² this large or larger. The line: 8.56 for 8, p = 0.38. The D⁰ peak of LHCb: 53.4 for 40, p = 0.08.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_chi2_dist.svg">

---
hideInToc: true
class: fill
---

# The Pendulum's **g**

<div class="card card-info card-glass pad-compact mt-sm">

🕰️ Nine lengths and the time of 10 swings, 0.1 s assumed on each. $T^2 = (4\pi^2/g)\,\ell$: slope 4.010 ± 0.037 s²/m, so **g = 9.84 ± 0.09 m/s²**; χ² = 2.65 for 7.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_pendulum_fit.svg">

---
hideInToc: true
class: fill
---

# The D⁰ Mass Peak of **LHCb**

<div class="card card-info card-glass pad-compact mt-sm">

⚛️ 91&nbsp;583 K⁻π⁺ masses: a peak, the D⁰ meson, on a flat part of random pairs. The fit takes 1820 to 1910 MeV/c², 45 bins, σ = √n.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_d0_data.svg">

---
hideInToc: true
class: fill
---

# The D⁰ Peak, **Fitted**

<div class="card card-info card-glass pad-compact mt-sm">

⚛️ A Gaussian on a straight line, five parameters, fitted by Levenberg–Marquardt: **μ = 1864.47 ± 0.10 MeV/c²**, χ² = 53.4 for 40.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_d0_fit.svg">

---
hideInToc: true
class: fill
---

# Too Few Terms on the D⁰ **Peak**

<div class="card card-info card-glass pad-compact mt-sm">

📉 A line leaves the peak in its pulls; a flat background leaves a tilt; a sloped one leaves scatter. The slope lowers χ² by 46.0: needed.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_fitting_d0_models.svg">

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it.

---
hideInToc: true
---

<MCQ
  question="Which value of μ makes the sum of squared misses Σ(y − μ)² smallest for the three values 2, 4 and 9?"
  :options="[
    '4, the middle value',
    '5, the mean',
    '5.5, halfway between the smallest and the largest',
    '9, the largest'
  ]"
  :correct="1"
  explanation="The derivative −2Σ(y − μ) is zero where Σy = 3μ: μ = 15 / 3 = 5, the mean. The middle value, 4, makes the sum of the sizes |y − μ| smallest instead."
/>

---
hideInToc: true
---

<MCQ
  question="Three points have residuals 0.2, −0.3 and 0.1 from a model, each with σ = 0.1. What is χ²?"
  :options="[
    '0.14',
    '1.4',
    '6',
    '14'
  ]"
  :correct="3"
  explanation="The pulls are 2, −3 and 1. Their squares are 4, 9 and 1, and the sum is 14. The point 3σ away gives 9 of the 14."
/>

---
hideInToc: true
---

<MCQ
  question="Three points: x = 0, 1, 2 and y = 1, 3, 4. What is the slope of the least-squares line?"
  :options="[
    '1.5',
    '2',
    '1.17',
    '3'
  ]"
  :correct="0"
  explanation="N = 3, Σx = 3, Σy = 8, Σx² = 5, Σxy = 11. Δ = 3 × 5 − 3² = 6. The slope is (3 × 11 − 3 × 8) / 6 = 9 / 6 = 1.5, and the intercept (5 × 8 − 3 × 11) / 6 = 7 / 6 = 1.17."
/>

---
hideInToc: true
---

<MCQ
  question="A fit with one parameter has χ² = 12.0 at its minimum, θ = 5.00. At θ = 5.20 the χ² is 13.0. What is the uncertainty of θ?"
  :options="[
    '1.0',
    '0.04',
    '0.20',
    '13.0'
  ]"
  :correct="2"
  explanation="One σ raises χ² by 1: σ = 5.20 − 5.00 = 0.20. At θ = 5.40, two σ away, χ² would be 12 + 4 = 16."
/>

---
hideInToc: true
---

<MCQ
  question="Gradient descent on S(θ) = (θ − 3)² starts at θ = 0 with the step size η = 0.25. Where is θ after one step?"
  :options="[
    '1.5',
    '3',
    '−1.5',
    '0.75'
  ]"
  :correct="0"
  explanation="The derivative at θ = 0 is −2 × (3 − 0) = −6. The step: θ = 0 − 0.25 × (−6) = 1.5. With η = 0.5 one step lands on 3; with η = 1 it lands on 6, as far away as the start."
/>

---
hideInToc: true
---

<MCQ
  question="A cosine with three parameters is fitted to 365 daily means. How many degrees of freedom does the fit have?"
  :options="[
    '365',
    '368',
    '362',
    '3'
  ]"
  :correct="2"
  explanation="ndf = N − k = 365 − 3 = 362. If the model and the σ are right, χ² is expected near 362."
/>

---
hideInToc: true
---

<MCQ
  question="A polynomial with ten parameters is fitted to ten yearly means. What happens?"
  :options="[
    'It finds the true trend more exactly than a line',
    'It passes through every point: χ² = 0, nothing is left to test, and its forecast is unreliable',
    'χ² equals 10, one per point',
    'It gives the same forecast as the mean'
  ]"
  :correct="1"
  explanation="Ten free numbers can match ten points exactly. The curve follows each year's weather, and for the yearly means of the weather log it forecasts 307 °C for 2026."
/>

---
hideInToc: true
---

<MCQ
  question="A fit takes 3648 days as independent and gives A = 11.18 ± 0.07 °C, but neighbouring days correlate, r = 0.875. The honest ± is…"
  :options="[
    'smaller than 0.07, since there are many days',
    'exactly 0.07',
    'larger than 0.07: alike neighbours carry less information than independent days',
    'zero, since the cycle repeats every year'
  ]"
  :correct="2"
  explanation="A warm week counts seven times. Ten separate one-year fits scatter by 0.79 °C, which gives ± 0.25 °C for their mean: 3.6 times the ± of the fit."
/>
