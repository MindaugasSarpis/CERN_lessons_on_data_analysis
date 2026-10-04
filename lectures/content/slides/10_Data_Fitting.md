---
layout: cover
title: "Data Fitting from First Principles"
# slidev-addon-python-runner reads this block from slide 1 = this cover (see CLAUDE.md).
# The prelude holds the pendulum arrays of the slide "The Same in NumPy", so
# every later runner works without that slide having been run first.
python:
  installs: ["numpy", "scipy"]
  prelude: |
    import numpy as np
    from scipy.optimize import curve_fit
    t10 = np.array([9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01])
    x = np.arange(20, 101, 10) / 100
    T = t10 / 10
    y = T**2
    sy = 2 * T * 0.01
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Data Fitting from First Principles

##### <span class="aims-badge">⚙️ automation · 🔧 tool-agnostic</span>

<!--
Speaker: one table of nine rows carries most of the lecture. Every step is done
on it three times: with a calculator, in NumPy, with SciPy. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The goal of this lecture is to derive the fit of a model to data from the **likelihood**, and to carry it out three times: by hand, in **NumPy** and with **SciPy**

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📐 Derive **χ²** from the Gaussian likelihood

</div>

<div class="card card-secondary card-glass pad-compact">

🧮 Fit a **straight line** in closed form, from five sums

</div>

<div class="card card-accent card-glass pad-compact">

📏 Get parameter **uncertainties** and their covariance from the curvature of χ²

</div>

<div class="card card-info card-glass pad-compact">

⛰️ Minimise χ² by **gradient descent**, and say what the learning rate does

</div>

<div class="card card-success card-glass pad-compact">

🐍 Fit a nonlinear model with **`scipy.optimize.curve_fit`**

</div>

<div class="card card-warning card-glass pad-compact">

🔍 Judge a fit by **χ² per degree of freedom**, residuals and pulls

</div>

</div>

---
hideInToc: true
---

# What Lecture 09 **Established**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **Likelihood**

The likelihood $L(\theta)$ is the probability of the measured data, read as a function of the parameters $\theta$.

The maximum-likelihood estimate $\hat\theta$ is the value of $\theta$ at which $L(\theta)$ is largest.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚖️ **The weighted mean**

$N$ measurements $y_i \pm \sigma_i$ of one quantity $\mu$, with Gaussian scatter. The likelihood is largest at

$$\hat\mu = \frac{\sum_i y_i/\sigma_i^2}{\sum_i 1/\sigma_i^2}, \qquad \sigma_{\hat\mu}^2 = \frac{1}{\sum_i 1/\sigma_i^2}$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Today the measured quantity changes with a second quantity $x$, and a model $f(x;\theta)$ says how. The steps stay the same: write the likelihood, find its maximum, find the uncertainty of the result.

</div>

<!--
Speaker: write the two formulas of the weighted mean on the board and leave
them there. They come back three times today. (~2 min)
-->

---
layout: section
hideInToc: true
---

# What a **Fit** Is

---
hideInToc: true
---

# The Pendulum **Table**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📄 **`pendulum.csv`, with two columns added**

| ℓ (cm) | t₁₀ (s) | T (s) | T² (s²) |
| --- | --- | --- | --- |
| 20 | 9.02 | 0.902 | 0.8136 |
| 30 | 11.05 | 1.105 | 1.2210 |
| 40 | 12.61 | 1.261 | 1.5901 |
| 50 | 14.23 | 1.423 | 2.0249 |
| 60 | 15.49 | 1.549 | 2.3994 |
| 70 | 16.84 | 1.684 | 2.8359 |
| 80 | 17.90 | 1.790 | 3.2041 |
| 90 | 19.10 | 1.910 | 3.6481 |
| 100 | 20.01 | 2.001 | 4.0040 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## ⏱️ **What was measured**

Nine lengths $\ell$ and the time $t_{10}$ of 10 swings. One period is $T = t_{10}/10$.

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **What theory says**

$$T = 2\pi\sqrt{\frac{\ell}{g}} \quad\Longrightarrow\quad T^2 = \frac{4\pi^2}{g}\,\ell$$

$T^2$ against $\ell$ is a straight line through the origin with slope $4\pi^2/g$. For $g = 9.81$ m/s² the slope is 4.024 s²/m.

</div>

<div class="card card-info card-glass pad-compact">

The length is written $\ell$ today. The letter $L$ is the likelihood.

</div>

</div>

</div>

<!--
Speaker: the table is the one cleaned by hand in Lecture 02. Ask the room what
they would plot to get g. (~2 min)
-->

---
hideInToc: true
---

# From a Curve to a **Straight Line**

<div class="note-text mt-sm">

The same nine rows, plotted twice. A straight line has two parameters and can be fitted by hand. The dashed curves are the theory with $g = 9.81$ m/s².

</div>

<img class="fig" src="/figures/viz_fitting_pendulum_data.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:345px;">

---
hideInToc: true
---

# The Uncertainties We **Assume**

<div class="grid-2 mt-md gap-md">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

## ✋ **One assumption**

The stopwatch is worked by hand. Take $\sigma_{t_{10}} = 0.1$ s for every row. Then $\sigma_T = \sigma_{t_{10}}/10 = 0.01$ s.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➡️ **Propagated to T²**

By error propagation (Lecture 09):

$$\sigma_{T^2} = \left|\frac{d(T^2)}{dT}\right|\sigma_T = 2\,T\,\sigma_T$$

First row: 2 × 0.902 × 0.01 = 0.0180 s².

</div>

<div class="card card-info card-glass pad-compact">

The length is taken as exact. An error of 1 mm in $\ell$ moves $T^2$ by 0.004 s², less than a quarter of the smallest $\sigma_{T^2}$.

</div>

</div>

<div class="card card-accent card-glass pad-compact table-compact">

## 📏 **The data of the fit**

| x = ℓ (m) | y = T² (s²) | σ (s²) |
| --- | --- | --- |
| 0.2 | 0.8136 | 0.0180 |
| 0.3 | 1.2210 | 0.0221 |
| 0.4 | 1.5901 | 0.0252 |
| 0.5 | 2.0249 | 0.0285 |
| 0.6 | 2.3994 | 0.0310 |
| 0.7 | 2.8359 | 0.0337 |
| 0.8 | 3.2041 | 0.0358 |
| 0.9 | 3.6481 | 0.0382 |
| 1.0 | 4.0040 | 0.0400 |

</div>

</div>

<!--
Speaker: the 0.1 s is an assumption, and the lecture says so every time it is
used. The goodness of fit later tests it. The uncertainties are not equal: the
long pendulum has twice the uncertainty in T squared. (~2 min)
-->

---
hideInToc: true
---

# The Three Parts of a **Fit**

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **A model**

A function $f(x;\theta)$ with parameters $\theta$. Here $f(x; a, b) = a\,x + b$, with $x = \ell$ and $y = T^2$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **Data with uncertainties**

$N$ points $(x_i, y_i)$ with uncertainties $\sigma_i$, $i = 1 \dots N$. Here $N = 9$.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎯 **A measure of mismatch**

One number that says how far the model with parameters $\theta$ is from the data. The fit is the $\theta$ that makes it smallest.

</div>

</div>

<div class="note-text mt-sm">

Three lines chosen by eye. At full scale they look alike. With $4\ell$ subtracted they differ by a few 0.01 s², the size of the error bars. The measure has to rank them, and it has to use the $\sigma_i$.

</div>

<img class="fig" src="/figures/viz_fitting_candidates.svg" style="display:block;margin:0.4rem auto 0;max-width:100%;max-height:235px;">

<!--
Speaker: ask for a vote on A, B or C before going on. The slope a gives
g = 4 pi squared over a. The intercept b tests the theory, which demands
b = 0. The right panel is the data with one known line subtracted; the lecture
uses this view again. (~3 min)
-->

---
layout: section
hideInToc: true
---

# From Likelihood to **χ²**

---
hideInToc: true
---

# One Point, One **Gaussian**

<div class="grid-2 mt-md gap-md">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

## 📍 **The assumption**

If the model is right, the measured $y_i$ scatters around the model value $f(x_i;\theta)$ as a Gaussian of width $\sigma_i$:

$$p(y_i \mid \theta) = \frac{1}{\sqrt{2\pi}\,\sigma_i}\,\exp\!\left[-\frac{\big(y_i - f(x_i;\theta)\big)^2}{2\sigma_i^2}\right]$$

</div>

<div class="card card-info card-glass pad-compact">

The Gaussian of Lecture 09, with $f(x_i;\theta)$ in the place of the mean $\mu$. Three assumptions are in it: the scatter is Gaussian, the $\sigma_i$ are known, and the $x_i$ are exact.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_likelihood.svg" style="display:block;width:100%;">

</div>

---
hideInToc: true
---

# All Points: the **Likelihood**

<div class="card card-primary card-glass pad-compact mt-md">

## ✖️ **A fourth assumption: independent points, so the probabilities multiply**

$$L(\theta) = \prod_{i=1}^{N} \frac{1}{\sqrt{2\pi}\,\sigma_i}\,\exp\!\left[-\frac{\big(y_i - f(x_i;\theta)\big)^2}{2\sigma_i^2}\right]$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🪵 **Take the logarithm**

The logarithm turns the product into a sum, and it is largest at the same $\theta$ as $L$ itself:

$$\ln L(\theta) = -\frac{1}{2}\sum_{i=1}^{N}\frac{\big(y_i - f(x_i;\theta)\big)^2}{\sigma_i^2} \;-\; \sum_{i=1}^{N}\ln\!\big(\sqrt{2\pi}\,\sigma_i\big)$$

The second sum does not contain $\theta$. It is a constant.

</div>

---
hideInToc: true
---

# Maximum Likelihood Is Minimum **χ²**

<div class="card card-info card-glass pad-compact mt-md">

$$-2\ln L(\theta) = \chi^2(\theta) + \text{const}, \qquad \chi^2(\theta) = \sum_{i=1}^{N}\frac{\big(y_i - f(x_i;\theta)\big)^2}{\sigma_i^2}$$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔁 **The same estimate**

$L$ is largest where $\chi^2$ is smallest. With Gaussian uncertainties, maximum likelihood is the method of **least squares**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **One term**

The residual $y_i - f(x_i;\theta)$, divided by $\sigma_i$, is the **pull**. $\chi^2$ is the sum of the squared pulls. A point 1σ from the model adds 1. A point 3σ away adds 9.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚖️ **Equal uncertainties**

If every $\sigma_i$ is the same $\sigma$, then $\chi^2 = \frac{1}{\sigma^2}\sum_i (y_i - f)^2$. The minimum is where the plain sum of squares is smallest.

</div>

</div>

<!--
Speaker: this is the central step of the lecture. The measure of mismatch was
not chosen. It follows from the Gaussian and from independence. (~3 min)
-->

---
hideInToc: true
---

# χ² in **Numbers**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🧮 **Line A:** $a = 4$, $b = 0$

| ℓ | y | y − 4ℓ | σ | pull | pull² |
| --- | --- | --- | --- | --- | --- |
| 0.2 | 0.8136 | 0.0136 | 0.0180 | 0.75 | 0.57 |
| 0.3 | 1.2210 | 0.0210 | 0.0221 | 0.95 | 0.91 |
| 0.4 | 1.5901 | −0.0099 | 0.0252 | −0.39 | 0.15 |
| 0.5 | 2.0249 | 0.0249 | 0.0285 | 0.88 | 0.77 |
| 0.6 | 2.3994 | −0.0006 | 0.0310 | −0.02 | 0.00 |
| 0.7 | 2.8359 | 0.0359 | 0.0337 | 1.06 | 1.13 |
| 0.8 | 3.2041 | 0.0041 | 0.0358 | 0.11 | 0.01 |
| 0.9 | 3.6481 | 0.0481 | 0.0382 | 1.26 | 1.59 |
| 1.0 | 4.0040 | 0.0040 | 0.0400 | 0.10 | 0.01 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## ➕ **The sum**

$\chi^2 = 0.57 + 0.91 + \dots + 0.01 = 5.14$

</div>

<div class="card card-accent card-glass pad-compact table-compact">

## 🏁 **The three candidates**

| Line | a | b | χ² |
| --- | --- | --- | --- |
| A | 4.0 | 0 | 5.14 |
| B | 3.9 | 0.05 | 13.11 |
| C | 4.1 | −0.05 | 12.28 |

</div>

<div class="card card-info card-glass pad-compact">

A is the best of the three. The fit asks for the best of all lines: the $(a, b)$ at which $\chi^2$ is smallest.

</div>

</div>

</div>

<!--
Speaker: do the first row on the board. 0.8136 minus 0.8 is 0.0136; divided by
0.0180 it is 0.75; squared, 0.57. (~2 min)
-->

---
hideInToc: true
---

# The Weighted Mean Is a **Fit**

<div class="card card-primary card-glass pad-compact mt-md">

## 1️⃣ **The simplest model: a constant,** $f(x;\mu) = \mu$

$$\chi^2(\mu) = \sum_i \frac{(y_i-\mu)^2}{\sigma_i^2}, \qquad \frac{d\chi^2}{d\mu} = -2\sum_i \frac{y_i-\mu}{\sigma_i^2} = 0 \quad\Longrightarrow\quad \hat\mu = \frac{\sum_i y_i/\sigma_i^2}{\sum_i 1/\sigma_i^2}$$

The weighted mean of Lecture 09 is the least-squares fit of a constant.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🕰️ **On the pendulum**

Each row gives its own $g_i = 4\pi^2\ell_i/T_i^2$, from $9.70 \pm 0.22$ at 0.2 m to $9.86 \pm 0.10$ at 1.0 m. The fit of a constant to the nine values:

$$\hat g = 9.804 \pm 0.042\ \text{m/s}^2$$

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **What this leaves open**

- It takes $T^2 = (4\pi^2/g)\,\ell$ as exact. Nothing tests it
- If every length is off by the same amount, the line misses the origin, and each $g_i$ is wrong by a different factor
- A line with a free intercept has two parameters, and no value per row to average

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

🧭 The recipe for any model: write $\chi^2$, set its derivative with respect to each parameter to zero, solve for the parameters.

</div>

<!--
Speaker: the nine values are 9.70, 9.70, 9.93, 9.75, 9.87, 9.74, 9.86, 9.74,
9.86 with uncertainties 0.22, 0.18, 0.16, 0.14, 0.13, 0.12, 0.11, 0.10, 0.10.
Keep 9.804 plus or minus 0.042 in mind: the straight-line fit returns to it
when the intercept is fixed at zero. (~3 min)
-->

---
layout: section
hideInToc: true
---

# The Straight Line in **Closed Form**

---
hideInToc: true
---

# Two Derivatives Set to **Zero**

<div class="card card-primary card-glass pad-compact mt-md">

## 📐 **χ² of the straight line**

$$\chi^2(a,b) = \sum_{i=1}^{N}\frac{(y_i - a\,x_i - b)^2}{\sigma_i^2}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 0️⃣ **At the minimum both partial derivatives vanish**

$$\frac{\partial\chi^2}{\partial a} = -2\sum_i \frac{x_i\,(y_i - a\,x_i - b)}{\sigma_i^2} = 0, \qquad \frac{\partial\chi^2}{\partial b} = -2\sum_i \frac{y_i - a\,x_i - b}{\sigma_i^2} = 0$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

A partial derivative is the derivative with respect to one parameter while the other is held fixed. $\chi^2$ is a quadratic function of $a$ and $b$, a bowl with one lowest point, so the point where both derivatives are zero is the minimum.

</div>

---
hideInToc: true
---

# The Normal **Equations**

<div class="card card-primary card-glass pad-compact mt-md">

## ➕ **Five sums over the data**

$$S = \sum_i \frac{1}{\sigma_i^2},\quad S_x = \sum_i \frac{x_i}{\sigma_i^2},\quad S_y = \sum_i \frac{y_i}{\sigma_i^2},\quad S_{xx} = \sum_i \frac{x_i^2}{\sigma_i^2},\quad S_{xy} = \sum_i \frac{x_i\,y_i}{\sigma_i^2}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🟰 **The two conditions, written with the sums**

$$a\,S_{xx} + b\,S_x = S_{xy} \qquad\qquad a\,S_x + b\,S = S_y$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

Two linear equations for two unknowns. They are called the **normal equations**. The data enter only through the five sums, whatever the number of points.

</div>

<!--
Speaker: derive the first equation on the board: multiply out x times the
bracket, split the sum into three, and name each sum. (~3 min)
-->

---
hideInToc: true
---

# Slope and Intercept in **Closed Form**

<div class="card card-primary card-glass pad-compact mt-md">

## ✂️ **Eliminate b**

Multiply the first equation by $S$, the second by $S_x$, and subtract:

$$a\,\big(S\,S_{xx} - S_x^2\big) = S\,S_{xy} - S_x S_y$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ✅ **The solution**

$$\Delta = S\,S_{xx} - S_x^2, \qquad \hat a = \frac{S\,S_{xy} - S_x S_y}{\Delta}, \qquad \hat b = \frac{S_{xx}\,S_y - S_x S_{xy}}{\Delta}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

The second equation, divided by $S$, reads $\bar y = \hat a\,\bar x + \hat b$ with $\bar x = S_x/S$, $\bar y = S_y/S$. The line passes through the weighted mean point.

</div>

<div class="card card-info card-glass pad-compact">

With equal $\sigma_i$ the formula for the slope becomes $\hat a = \dfrac{N\sum x_i y_i - \sum x_i \sum y_i}{N\sum x_i^2 - (\sum x_i)^2}$, the one built into every spreadsheet.

</div>

</div>

---
hideInToc: true
---

# The Pendulum: Five **Sums**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| x = ℓ | w = 1/σ² | w·x | w·y | w·x² | w·x·y |
| --- | --- | --- | --- | --- | --- |
| 0.2 | 3072.75 | 614.55 | 2500.00 | 122.91 | 500.00 |
| 0.3 | 2047.46 | 614.24 | 2500.00 | 184.27 | 750.00 |
| 0.4 | 1572.21 | 628.88 | 2500.00 | 251.55 | 1000.00 |
| 0.5 | 1234.61 | 617.31 | 2500.00 | 308.65 | 1250.00 |
| 0.6 | 1041.93 | 625.16 | 2500.00 | 375.09 | 1500.00 |
| 0.7 | 881.57 | 617.10 | 2500.00 | 431.97 | 1750.00 |
| 0.8 | 780.25 | 624.20 | 2500.00 | 499.36 | 2000.00 |
| 0.9 | 685.29 | 616.76 | 2500.00 | 555.08 | 2250.00 |
| 1.0 | 624.38 | 624.38 | 2500.00 | 624.38 | 2500.00 |
| **Sum** | $S$ = 11 940.44 | $S_x$ = 5582.56 | $S_y$ = 22 500.00 | $S_{xx}$ = 3353.27 | $S_{xy}$ = 13 500.00 |

</div>

<div class="card card-info card-glass pad-compact mt-sm">

Every $w\,y$ is 2500 because $\sigma_i = 2\,T_i\,\sigma_T$: then $y_i/\sigma_i^2 = T_i^2/(4\,T_i^2\,\sigma_T^2) = 1/(4 \times 0.01^2)$. The rows are rounded; the sums were taken before rounding.

</div>

<!--
Speaker: let the room compute one row. Row 1: 1 over 0.01804 squared is
3072.75; times 0.2 is 614.55; times 0.8136 is 2500. (~3 min)
-->

---
hideInToc: true
---

# The Pendulum: Slope and **Intercept**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **The denominator**

```text
Δ = S·Sxx − Sx²
  = 11 940.44 × 3353.27 − 5582.56²
  = 40 039 519 − 31 164 976
  = 8 874 543
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📈 **Slope and intercept**

```text
a = (S·Sxy − Sx·Sy) / Δ
  = (161 195 940 − 125 607 600) / Δ
  = 35 588 340 / 8 874 543 = 4.0102 s²/m

b = (Sxx·Sy − Sx·Sxy) / Δ
  = (75 448 575 − 75 364 560) / Δ
  = 84 015 / 8 874 543     = 0.0095 s²
```

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

$g = 4\pi^2/a = 39.4784 / 4.01018 = 9.845$ m/s². What this number is worth depends on the uncertainty of $a$.

</div>

<div class="card card-warning card-glass pad-compact">

⚠️ $b$ is the difference of two numbers that agree in their first three digits. Sums rounded to four digits give a wrong $b$. Keep all digits until the end.

</div>

</div>

<!--
Speaker: with the sums to all digits, NumPy gives 8 874 453 for the denominator,
a = 4.010181 and b = 0.009455. The calculator values on the slide agree with
them to the four decimals shown. (~3 min)
-->

---
hideInToc: true
---

# The Fitted **Line**

<div class="note-text mt-sm">

$T^2 = 4.010\,\ell + 0.009$. Left: the line through the nine points. Right: what is left of each point after the line is subtracted, the **residual**, with its error bar $\sigma_i$.

</div>

<img class="fig" src="/figures/viz_fitting_pendulum_fit.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:345px;">

---
hideInToc: true
---

# The Same in **NumPy**

```python {monaco-run} {autorun:false}
import numpy as np
x   = np.arange(20, 101, 10) / 100                 # length in m
t10 = np.array([9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01])
T   = t10 / 10                                     # one period in s
y   = T**2
sy  = 2 * T * 0.01                                 # uncertainty of T squared

w = 1 / sy**2
S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
Sxx, Sxy  = (w * x * x).sum(), (w * x * y).sum()
D = S * Sxx - Sx**2
a = (S * Sxy - Sx * Sy) / D
b = (Sxx * Sy - Sx * Sxy) / D
print(f"a = {a:.6f}   b = {b:.6f}   g = {4 * np.pi**2 / a:.4f}")
```

<!--
Speaker: prints a = 4.010181, b = 0.009455, g = 9.8445. The nine numbers are
typed in here because the browser has no file to read. In a script the two
columns come from np.loadtxt on pendulum.csv. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Uncertainties of the **Parameters**

---
hideInToc: true
---

# The Slope Is a Sum over the **Data**

<div class="card card-primary card-glass pad-compact mt-md">

## ➕ **â is linear in the yᵢ**

$S_{xy}$ and $S_y$ are sums over the $y_i$. Nothing else in $\hat a$ contains them:

$$\hat a = \frac{S\,S_{xy} - S_x S_y}{\Delta} = \sum_i c_i\,y_i, \qquad c_i = \frac{S\,x_i - S_x}{\sigma_i^2\,\Delta}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ➡️ **Error propagation for a sum of independent terms (Lecture 09)**

$$\sigma_a^2 = \sum_i c_i^2\,\sigma_i^2 = \frac{1}{\Delta^2}\sum_i \frac{(S\,x_i - S_x)^2}{\sigma_i^2} = \frac{S^2 S_{xx} - 2\,S\,S_x^2 + S_x^2\,S}{\Delta^2} = \frac{S\,\Delta}{\Delta^2} = \frac{S}{\Delta}$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

If the nine times were measured again, each $y_i$ would come out a little different, and so would $\hat a$. $\sigma_a$ is the width of that scatter.

</div>

<!--
Speaker: the middle step: square the bracket, sum term by term, and recognise
S squared times Sxx, S times Sx squared twice with a minus, and Sx squared
times S. (~3 min)
-->

---
hideInToc: true
---

# Two Uncertainties and a **Covariance**

<div class="card card-primary card-glass pad-compact mt-md">

The same steps for $\hat b$, and for the product of the two:

$$\sigma_a^2 = \frac{S}{\Delta}, \qquad \sigma_b^2 = \frac{S_{xx}}{\Delta}, \qquad \operatorname{cov}(a,b) = -\frac{S_x}{\Delta}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧮 **The pendulum**

```text
σa  = √(11 940.44 / 8 874 543) = 0.0367 s²/m
σb  = √( 3353.27 / 8 874 543)  = 0.0194 s²
cov = −5582.56 / 8 874 543     = −0.000629
ρ   = cov / (σa σb)            = −0.88
```

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

$a = 4.010 \pm 0.037$ s²/m, $\quad b = 0.009 \pm 0.019$ s²

</div>

<div class="card card-info card-glass pad-compact">

$\hat a$ and $\hat b$ come from the same nine $y_i$, so they are not independent. Covariance and $\rho$ are those of Lecture 09.

</div>

<div class="card card-accent card-glass pad-compact">

The three formulas contain the $x_i$ and $\sigma_i$ and no $y_i$. The uncertainties are known before the measurement is made.

</div>

</div>

</div>

---
hideInToc: true
---

# χ² Around Its **Minimum**

<div class="card card-primary card-glass pad-compact mt-md">

## 🥣 **A quadratic bowl**

$\chi^2(a,b)$ is quadratic in $a$ and $b$. Around its minimum $(\hat a, \hat b)$ it is exactly

$$\chi^2(a,b) = \chi^2_{\min} + S_{xx}\,(a-\hat a)^2 + 2\,S_x\,(a-\hat a)(b-\hat b) + S\,(b-\hat b)^2$$

The coefficients are half the second derivatives of $\chi^2$.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔻 **Move a, and let b follow**

For a given $a$ the lowest $\chi^2$ is at $b = \hat b - (S_x/S)\,(a - \hat a)$. Along that path

$$\chi^2(a) = \chi^2_{\min} + \Big(S_{xx} - \frac{S_x^2}{S}\Big)(a-\hat a)^2 = \chi^2_{\min} + \frac{(a-\hat a)^2}{\sigma_a^2}$$

</div>

<!--
Speaker: Sxx minus Sx squared over S is Delta over S, and that is one over
sigma a squared. The uncertainty found by error propagation is the width of
the bowl. (~3 min)
-->

---
hideInToc: true
---

# The Rule **Δχ² = 1**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **One σ raises χ² by 1**

At $a = \hat a \pm \sigma_a$, with the other parameters re-minimised, $\chi^2 = \chi^2_{\min} + 1$. Pendulum: 2.647 at the minimum, 3.647 at $a = 3.974$ and at $a = 4.047$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔔 **Why 1**

$L \propto e^{-\chi^2/2} = \text{const} \times e^{-(a-\hat a)^2/2\sigma_a^2}$. The likelihood is a Gaussian in $a$ of width $\sigma_a$. A sharp minimum of $\chi^2$ means a small uncertainty.

</div>

</div>

<img class="fig" src="/figures/viz_fitting_chi2_curvature.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:300px;">

<!--
Speaker: dashed parabola: b held at its best value. chi2 then rises by 1 at
plus or minus 0.017, the uncertainty a would have if b were known exactly.
Right: the contour of chi2 min plus 1 touches the lines a hat plus or minus
sigma a and b hat plus or minus sigma b. (~3 min)
-->

---
hideInToc: true
---

# The Covariance **Matrix**

<div class="card card-primary card-glass pad-compact mt-md">

## 🥣 **Curvature of χ²**

$$\frac{1}{2}\begin{pmatrix} \dfrac{\partial^2\chi^2}{\partial a^2} & \dfrac{\partial^2\chi^2}{\partial a\,\partial b}\\[2.5mm] \dfrac{\partial^2\chi^2}{\partial a\,\partial b} & \dfrac{\partial^2\chi^2}{\partial b^2}\end{pmatrix} = \begin{pmatrix} S_{xx} & S_x\\ S_x & S\end{pmatrix}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔄 **Its inverse**

$$V = \begin{pmatrix} S_{xx} & S_x\\ S_x & S\end{pmatrix}^{-1} = \frac{1}{\Delta}\begin{pmatrix} S & -S_x\\ -S_x & S_{xx}\end{pmatrix} = \begin{pmatrix}\sigma_a^2 & \operatorname{cov}(a,b)\\ \operatorname{cov}(a,b) & \sigma_b^2\end{pmatrix}$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

The covariance matrix of the parameters is the inverse of the curvature matrix of $\chi^2$ at its minimum. This holds for any number of parameters, and it is how a fitting program computes uncertainties.

</div>

---
hideInToc: true
---

# Why Slope and Intercept Are **Correlated**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ↔️ **ρ = −0.88**

The line passes through $(\bar x, \bar y) = (0.468\ \text{m},\ 1.884\ \text{s}^2)$, and all points lie to the right of $x = 0$. A steeper line through that point meets the axis $x = 0$ lower: a larger $a$ goes with a smaller $b$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **A result that uses both**

The fitted $T^2$ at $\ell = 0.5$ m is $f = 0.5\,a + b = 2.0145$ s². By error propagation for two correlated quantities:

$$\sigma_f^2 = x^2\sigma_a^2 + \sigma_b^2 + 2\,x\operatorname{cov}(a,b)$$

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

```text
with the covariance:     0.000336 + 0.000378 − 0.000629 = 0.000085     σf = 0.0092 s²
without the covariance:  0.000336 + 0.000378            = 0.000714     σf = 0.0267 s²
```

Without the covariance the uncertainty is three times too large. When two fitted parameters enter one result, their covariance enters too.

</div>

---
hideInToc: true
---

# The Uncertainty of **g**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➡️ **Propagate σₐ**

$$g = \frac{4\pi^2}{a}, \qquad \sigma_g = \left|\frac{dg}{da}\right|\sigma_a = g\,\frac{\sigma_a}{a}$$

```text
g  = 39.4784 / 4.01018        = 9.845
σg = 9.845 × 0.0367 / 4.0102  = 0.090
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **The result**

$$g = 9.84 \pm 0.09\ \text{m/s}^2$$

A relative uncertainty of 0.9 %. The value 9.81 m/s² lies 0.4σ below. Only $a$ enters $g$: no covariance term.

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧪 **The intercept tests the theory**

$b = 0.009 \pm 0.019$ s² is 0.5σ from zero. The data agree with a line through the origin.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔒 **With b fixed at 0**

One parameter: $a = S_{xy}/S_{xx} = 4.026 \pm 0.017$ and $g = 9.806 \pm 0.042$ m/s², the weighted mean of the nine $g_i$. The free intercept doubles $\sigma_g$. That is the price of the test.

</div>

</div>

<!--
Speaker: the weighted mean of the nine values was 9.804; the fit through the
origin gives 9.806. They are the same analysis up to the linear approximation
in the error propagation. (~3 min)
-->

---
layout: section
hideInToc: true
---

# The Same in **Matrix Form**

---
hideInToc: true
---

# One Equation for All **Points**

<div class="card card-primary card-glass pad-compact mt-md">

## 🧱 **The design matrix**

$$\underbrace{\begin{pmatrix} y_1\\ y_2\\ \vdots\\ y_N\end{pmatrix}}_{\mathbf y} \approx \underbrace{\begin{pmatrix} x_1 & 1\\ x_2 & 1\\ \vdots & \vdots\\ x_N & 1\end{pmatrix}}_{A}\, \underbrace{\begin{pmatrix} a\\ b\end{pmatrix}}_{\boldsymbol\theta}, \qquad W = \begin{pmatrix} 1/\sigma_1^2 & & \\ & \ddots & \\ & & 1/\sigma_N^2\end{pmatrix}, \qquad \chi^2 = (\mathbf y - A\boldsymbol\theta)^{\mathsf T}\,W\,(\mathbf y - A\boldsymbol\theta)$$

$A$ has one row per point and one column per parameter.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🟰 **All derivatives set to zero at once**

$$A^{\mathsf T} W A\;\hat{\boldsymbol\theta} = A^{\mathsf T} W\,\mathbf y, \qquad V = \big(A^{\mathsf T} W A\big)^{-1}$$

The normal equations and the covariance matrix, for any number of parameters.

</div>

---
hideInToc: true
---

# The Pendulum as **Matrices**

<div class="card card-primary card-glass pad-compact mt-md">

## ➕ **The products are the five sums**

$$A^{\mathsf T} W A = \begin{pmatrix} S_{xx} & S_x\\ S_x & S\end{pmatrix} = \begin{pmatrix} 3353.27 & 5582.56\\ 5582.56 & 11\,940.44\end{pmatrix}, \qquad A^{\mathsf T} W\,\mathbf y = \begin{pmatrix} S_{xy}\\ S_y\end{pmatrix} = \begin{pmatrix} 13\,500\\ 22\,500\end{pmatrix}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔄 **Invert and multiply**

$$V = \begin{pmatrix} 0.001345 & -0.000629\\ -0.000629 & 0.000378\end{pmatrix}, \qquad \hat{\boldsymbol\theta} = V\,A^{\mathsf T} W\,\mathbf y = \begin{pmatrix} 4.0102\\ 0.0095\end{pmatrix}$$

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same numbers as before: $\sqrt{0.001345} = 0.0367 = \sigma_a$, $\sqrt{0.000378} = 0.0194 = \sigma_b$, and the off-diagonal element is $\operatorname{cov}(a,b)$.

</div>

---
hideInToc: true
---

# Linear in the **Parameters**

<div class="card card-info card-glass pad-compact mt-md">

The matrix form used only that $f$ is a sum of known functions of $x$, each multiplied by one parameter:

$$f(x;\theta) = \theta_1\,g_1(x) + \theta_2\,g_2(x) + \dots + \theta_k\,g_k(x)$$

Column $j$ of the design matrix holds $g_j(x_i)$. Everything else stays as it is.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Linear**

- $a\,x + b$
- $c\,x^2 + a\,x + b$: a curve in $x$, linear in $a, b, c$
- $A\sin\omega t + B\cos\omega t$ with $\omega$ known

</div>

<div class="card card-warning card-glass pad-compact">

## ❌ **Not linear**

- $N_0\,e^{-t/\tau}$: $\tau$ is in the exponent
- A Gaussian peak: position and width
- $A\sin\omega t$ with $\omega$ unknown

</div>

<div class="card card-accent card-glass pad-compact">

## 🧪 **A third column**

Pendulum with columns $x^2$, $x$, 1: $c = 0.03 \pm 0.16$ s²/m², and $\chi^2$ falls from 2.65 to 2.60. The data do not ask for a curve.

</div>

</div>

---
hideInToc: true
---

# `np.linalg.lstsq` and `np.polyfit`

```python
# x, y, sy: the pendulum arrays of the slide "The Same in NumPy"
A = np.column_stack([x, np.ones_like(x)])     # design matrix: 9 rows, 2 columns
Aw, yw = A / sy[:, None], y / sy              # every row divided by its sigma

theta, *rest = np.linalg.lstsq(Aw, yw, rcond=None)
V = np.linalg.inv(Aw.T @ Aw)                  # covariance matrix
print("lstsq  ", theta, np.sqrt(np.diag(V)))

p, C = np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")
print("polyfit", p, np.sqrt(np.diag(C)))
```

```text
lstsq   [4.01018132 0.00945546] [0.03668084 0.01943853]
polyfit [4.01018132 0.00945546] [0.03668084 0.01943853]
```

<div class="card card-info card-glass pad-compact mt-sm">

`lstsq` minimises the plain sum of squares of `Aw @ theta - yw`. Every row divided by its $\sigma_i$ makes that sum $\chi^2$. `@` is the matrix product, `.T` the transpose. `polyfit` takes `w` as $1/\sigma$, not $1/\sigma^2$; `cov="unscaled"` keeps the $\sigma_i$ as given.

</div>

---
layout: section
hideInToc: true
---

# Models That Are **Not Linear**

---
hideInToc: true
---

# No Closed **Form**

<div class="card card-primary card-glass pad-compact mt-md">

## ⛰️ **A peak:** $f(x;\,A,\mu,\sigma) = A\,e^{-(x-\mu)^2/2\sigma^2}$

The derivative of $\chi^2$ with respect to the position $\mu$ of the peak:

$$\frac{\partial\chi^2}{\partial\mu} = -2\sum_i \frac{y_i - A\,e^{-(x_i-\mu)^2/2\sigma^2}}{\sigma_i^2}\;\frac{x_i-\mu}{\sigma^2}\;A\,e^{-(x_i-\mu)^2/2\sigma^2} = 0$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🚫 **No normal equations**

$\mu$ stands inside an exponential in every term. No rearrangement isolates it, and no five sums summarise the data.

</div>

<div class="card card-success card-glass pad-compact">

## 👣 **What is left**

$\chi^2(\theta)$ and its derivatives can be computed for any $\theta$. Start from a guess and walk downhill, one step at a time.

</div>

</div>

<div class="note-text mt-sm">

Here $\sigma$ without an index is the width of the peak, a parameter. $\sigma_i$ is the uncertainty of point $i$.

</div>

---
hideInToc: true
---

# The **Gradient**

<div class="card card-primary card-glass pad-compact mt-md">

## 🧭 **All partial derivatives in one vector**

$$\nabla\chi^2 = \left(\frac{\partial\chi^2}{\partial\theta_1},\ \dots,\ \frac{\partial\chi^2}{\partial\theta_k}\right), \qquad \frac{\partial\chi^2}{\partial\theta_j} = -2\sum_{i=1}^{N}\frac{y_i - f(x_i;\theta)}{\sigma_i^2}\;\frac{\partial f(x_i;\theta)}{\partial\theta_j}$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 📈 **A small step δ changes χ² by**

$$\chi^2(\theta + \delta) \approx \chi^2(\theta) + \nabla\chi^2\cdot\delta$$

This is the first-order expansion that gave the error-propagation formula in Lecture 09.

</div>

<div class="card card-info card-glass pad-compact mt-md">

Among all small steps of one length, the step along $\nabla\chi^2$ raises $\chi^2$ the most, and the opposite step lowers it the most. The gradient points uphill.

</div>

---
hideInToc: true
---

# The Update **Rule**

<div class="card card-primary card-glass pad-compact mt-md">

## 👣 **Gradient descent**

$$\theta \;\leftarrow\; \theta - \eta\,\nabla\chi^2$$

$\eta$ is the **learning rate**: a small positive number, chosen by hand, that sets the length of the step.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⬇️ **Why χ² goes down**

Put $\delta = -\eta\,\nabla\chi^2$ into the expansion:

$$\chi^2(\theta - \eta\nabla\chi^2) \approx \chi^2(\theta) - \eta\,\big|\nabla\chi^2\big|^2$$

The change is negative until the gradient is zero. The expansion holds for small steps only.

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **For the straight line**

The gradient is known from the normal equations:

$$\frac{\partial\chi^2}{\partial a} = -2\,(S_{xy} - a\,S_{xx} - b\,S_x)$$

$$\frac{\partial\chi^2}{\partial b} = -2\,(S_y - a\,S_x - b\,S)$$

</div>

</div>

<!--
Speaker: the rule is three symbols long and is the whole algorithm. Repeat it
until chi2 stops falling. (~2 min)
-->

---
hideInToc: true
---

# Gradient Descent by **Hand**

<div class="grid-2 mt-md gap-md">

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **The first step**

Start at $a = 3$, $b = 0$ with $\eta = 3 \times 10^{-5}$.

```text
∂χ²/∂a = −2 (13 500 − 3 × 3353.27)
       = −6880.4
∂χ²/∂b = −2 (22 500 − 3 × 5582.56)
       = −11 504.6

a ← 3 + 0.00003 × 6880.4   = 3.2064
b ← 0 + 0.00003 × 11 504.6 = 0.3451
```

</div>

<div class="card card-info card-glass pad-compact">

After 500 steps the result is that of the closed formulas: $a = 4.0102$, $b = 0.0095$, $\chi^2 = 2.65$.

</div>

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📋 **Step by step**

| Step | a | b | χ² |
| --- | --- | --- | --- |
| 0 | 3.0000 | 0.0000 | 3532.26 |
| 1 | 3.2064 | 0.3451 | 502.01 |
| 2 | 3.2557 | 0.3739 | 427.36 |
| 3 | 3.2854 | 0.3655 | 396.58 |
| 4 | 3.3120 | 0.3532 | 368.53 |
| 5 | 3.3373 | 0.3408 | 342.49 |
| 50 | 3.8824 | 0.0724 | 14.90 |
| 100 | 3.9900 | 0.0194 | 2.95 |
| 200 | 4.0097 | 0.0097 | 2.65 |
| 500 | 4.0102 | 0.0095 | 2.65 |

</div>

</div>

<!--
Speaker: have the room do step 1 on the calculator. The first step removes six
sevenths of chi2. Then the progress is slow: the slide after next shows why.
(~3 min)
-->

---
hideInToc: true
---

# A Learning Rate That Is Too **Large**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact table-compact">

## 💥 **The same start,** $\eta = 1 \times 10^{-4}$

| Step | a | b | χ² |
| --- | --- | --- | --- |
| 0 | 3.0000 | 0.0000 | 3532 |
| 1 | 3.6880 | 1.1505 | 11 792 |
| 2 | 2.6301 | −1.2147 | 43 144 |
| 3 | 4.9224 | 3.2495 | 161 144 |
| 4 | 0.6931 | −5.5066 | 604 495 |
| 5 | 9.0764 | 11.3698 | 2 269 656 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-primary card-glass pad-compact">

## ↔️ **Each step overshoots**

The step is in the right direction and too long. It crosses the valley and lands higher on the other side. $\chi^2$ grows nearly fourfold per step.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **The limit for this χ²**

The descent converges only for $\eta$ below $6.8 \times 10^{-5}$, which is 2 divided by the largest curvature of $\chi^2$.

</div>

<div class="card card-info card-glass pad-compact">

A rate that is too small is safe and slow: $\eta = 3 \times 10^{-6}$ needs ten times as many steps.

</div>

</div>

</div>

---
hideInToc: true
---

# Two Learning Rates, **Drawn**

<div class="note-text mt-sm">

Contours of $\chi^2$ in the $(a, b)$ plane with the path of the descent. The star is the minimum. Right: $\chi^2$ against the step number, on a logarithmic scale.

</div>

<img class="fig" src="/figures/viz_fitting_descent.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:335px;">

---
hideInToc: true
---

# Gradient Descent in **NumPy**

```python {monaco-run} {autorun:false}
# x, y, sy: the pendulum arrays of the slide "The Same in NumPy"
def chi2_at(a, b):
    return np.sum(((y - a * x - b) / sy) ** 2)

a, b, eta = 3.0, 0.0, 3e-5                    # start and learning rate
for step in range(501):
    r = (y - a * x - b) / sy**2               # residuals divided by sigma squared
    grad_a, grad_b = -2 * np.sum(r * x), -2 * np.sum(r)
    if step in (0, 1, 2, 5, 50, 100, 200, 500):
        print(f"{step:4d}  a = {a:.4f}  b = {b:.4f}  chi2 = {chi2_at(a, b):.2f}")
    a, b = a - eta * grad_a, b - eta * grad_b
```

<div class="note-text mt-sm">

Run it, then set `eta` to `1e-4` and run it again.

</div>

<!--
Speaker: the two gradient lines are the general formula with df/da = x and
df/db = 1. Nothing in the loop knows that the model is a straight line except
those two lines and chi2_at. (~3 min)
-->

---
hideInToc: true
---

# Why the Descent Is Slow, and the **Remedy**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏞️ **A long, narrow valley**

$\chi^2$ fell from 3532 to 502 in one step and needed 200 more for the rest. Across the valley $\chi^2$ is steep, along it nearly flat: the curvatures differ by a factor of 24. One $\eta$, small enough for the steep direction, creeps along the flat one. The valley is narrow because $a$ and $b$ are correlated.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **Use the curvature too**

Newton's step solves

$$\begin{pmatrix} S_{xx} & S_x\\ S_x & S\end{pmatrix}\delta = -\tfrac{1}{2}\nabla\chi^2$$

From $(3, 0)$ it lands on $(4.0102,\ 0.0095)$ in one step. For a model linear in its parameters, Newton's step is the normal equations.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

For a nonlinear model the curvature changes from place to place, and the step is repeated. The **Levenberg–Marquardt** method takes short gradient steps far from the minimum and Newton steps near it. `scipy.optimize.curve_fit` uses it.

</div>

---
hideInToc: true
---

# **SciPy**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📦 **What it is**

A library of numerical methods that work on NumPy arrays: minimisation and fitting (`scipy.optimize`), probability distributions (`scipy.stats`), integration, interpolation, linear algebra, signal processing.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬇️ **Install it once**

```text
Windows         python -m pip install scipy
macOS, Linux    python3 -m pip install scipy
```

The code on these slides was run with SciPy 1.16 and NumPy 2.3.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🐍 **Import the one function**

```python
import numpy as np
from scipy.optimize import curve_fit
```

SciPy is imported part by part. `curve_fit` minimises $\chi^2$ for a model given as a Python function, linear in its parameters or not.

</div>

---
hideInToc: true
---

# `curve_fit`: the **Call**

```python
popt, pcov = curve_fit(f, xdata, ydata, p0=[...], sigma=..., absolute_sigma=True)
```

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Argument | Meaning |
| --- | --- |
| `f` | The model, a function `f(x, a, b, ...)`: `x` first, then one argument for each parameter |
| `xdata`, `ydata` | The arrays of the $x_i$ and $y_i$ |
| `p0` | Starting values, one for each parameter. Left out, every parameter starts at 1 |
| `sigma` | The array of the $\sigma_i$. Left out, all points count equally |
| `absolute_sigma=True` | The $\sigma_i$ are uncertainties in the units of $y$ |
| `bounds=(lower, upper)` | Optional limits for the parameters |

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-secondary card-glass pad-compact">

`popt`: the estimates $\hat\theta$, in the order of the arguments of `f`.

</div>

<div class="card card-accent card-glass pad-compact">

`pcov`: the covariance matrix $V$. The uncertainties are `np.sqrt(np.diag(pcov))`.

</div>

</div>

---
hideInToc: true
---

# `absolute_sigma`: the Default **Rescales**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Without `absolute_sigma=True`**

`curve_fit` treats `sigma` as relative weights. It multiplies `pcov` by $\chi^2_{\min}/(N-k)$, with $k$ the number of parameters, as if the points scattered exactly as much as their $\sigma_i$ say.

</div>

<div class="card card-primary card-glass pad-compact table-compact">

## 🧮 **On the pendulum**

| | $\sigma_a$ | $\sigma_b$ |
| --- | --- | --- |
| Closed formulas | 0.0367 | 0.0194 |
| `absolute_sigma=True` | 0.0367 | 0.0194 |
| Default | 0.0226 | 0.0120 |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Here $\chi^2_{\min}/(N-k) = 2.647/7 = 0.378$, and the default shrinks both uncertainties by $\sqrt{0.378} = 0.61$. The default is the right choice only when the $\sigma_i$ are unknown and the model is trusted. Then the scatter of the points sets the uncertainties, and $\chi^2$ can no longer test the model.

</div>

---
hideInToc: true
---

# Three Ways, One **Result**

```python {monaco-run} {autorun:false}
from scipy.optimize import curve_fit
def line(x, a, b):                            # x, y, sy: the pendulum arrays
    return a * x + b

popt, pcov = curve_fit(line, x, y, p0=[3.0, 0.0], sigma=sy, absolute_sigma=True)
a, b = popt
sa, sb = np.sqrt(np.diag(pcov))
g, sg = 4 * np.pi**2 / a, 4 * np.pi**2 / a**2 * sa
print(f"a = {a:.6f} +- {sa:.6f}   b = {b:.6f} +- {sb:.6f}")
print(f"cov(a, b) = {pcov[0, 1]:.6f}   g = {g:.3f} +- {sg:.3f}")
```

<div class="card card-success card-glass pad-compact table-compact mt-sm">

| Method | $a$ | $\sigma_a$ | $b$ | $\sigma_b$ | cov($a$, $b$) |
| --- | --- | --- | --- | --- | --- |
| Closed formulas | 4.010181 | 0.036681 | 0.009455 | 0.019439 | −0.000629 |
| `np.polyfit` | 4.010181 | 0.036681 | 0.009455 | 0.019439 | −0.000629 |
| `curve_fit` | 4.010181 | 0.036681 | 0.009455 | 0.019439 | −0.000629 |

</div>

<!--
Speaker: the three agree in all six decimals, and g = 9.845 plus or minus 0.090
from each. curve_fit got there by iteration from a = 3, b = 0, the start of
the hand descent. (~3 min)
-->

---
hideInToc: true
---

# The D⁰ Mass Peak: the **Data**

<div class="note-text mt-sm">

Column `M` of `D0_KPi.csv`: 91 583 K⁻π⁺ masses, selected between about 1815 and 1915 MeV/c². The fit uses 1820 to 1910: 84 680 rows in 45 bins of 2 MeV.

</div>

<img class="fig" src="/figures/viz_fitting_d0_data.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:335px;">

<!--
Speaker: the model has to hold over the whole window. At the edges of the file
the counts drop for a reason that has nothing to do with the D0, so the window
stays away from them. (~2 min)
-->

---
hideInToc: true
---

# Counts and Their **Uncertainty**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **A bin count is a Poisson variable**

Its variance equals its mean (Lecture 09). With the observed count $n$ as the estimate of the mean:

$$\sigma_n = \sqrt{n}$$

For large $n$ the Poisson distribution is close to a Gaussian, so $\chi^2$ applies.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📊 **In this histogram**

| Bin | n | √n | relative |
| --- | --- | --- | --- |
| smallest | 1310 | 36.2 | 2.8 % |
| largest | 3746 | 61.2 | 1.6 % |

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

```python
M = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)
n, edges = np.histogram(M, bins=45, range=(1820, 1910))
m = (edges[:-1] + edges[1:]) / 2          # bin centres
s = np.sqrt(n)                            # Poisson uncertainty of each count
```

</div>

---
hideInToc: true
---

# The Model: a Gaussian on a **Line**

<div class="card card-info card-glass pad-compact mt-md">

$$f(m;\,A,\mu,\sigma,c_0,c_1) = A\,\exp\!\left[-\frac{(m-\mu)^2}{2\sigma^2}\right] + c_0 + c_1\,(m - 1865)$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔤 **Five parameters**

| | Meaning | Unit |
| --- | --- | --- |
| A | height of the peak above the background | entries per bin |
| μ | position of the peak | MeV/c² |
| σ | width of the peak | MeV/c² |
| c₀ | background at m = 1865 | entries per bin |
| c₁ | slope of the background | entries per bin per MeV/c² |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## 🤔 **Why this shape**

The detector measures each mass with a random error, which smears a sharp mass into a bell. Under the peak lie random K⁻π⁺ pairs whose number changes slowly with $m$.

</div>

<div class="card card-accent card-glass pad-compact">

Not linear in $\mu$ and $\sigma$: no closed form. The line is written around 1865, the middle of the window. Written as $c_0 + c_1 m$, its two parameters would be correlated with $\rho = -0.9998$.

</div>

</div>

</div>

---
hideInToc: true
---

# Starting Values from the **Plot**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 👁️ **Read off the histogram**

| | Start | Read from |
| --- | --- | --- |
| c₀ | 1400 | the level left and right of the peak |
| c₁ | 0 | the two sides are nearly level |
| A | 2300 | the top, 3700, minus 1400 |
| μ | 1865 | where the peak is highest |
| σ | 8 | the width at half height, 17 MeV |

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **From the width at half height to σ**

A Gaussian falls to half its height where

$$e^{-d^2/2\sigma^2} = \tfrac{1}{2} \quad\Longrightarrow\quad d = \sigma\sqrt{2\ln 2} = 1.177\,\sigma$$

The full width at half maximum is $2d = 2.355\,\sigma$.

Half height above the background is at 1400 + 1150 = 2550 entries. The peak is 17 MeV wide there: $\sigma \approx 17/2.355 = 7.2$. A start of 8 is near enough.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The starting values need not be good. They have to put the model near the data, so that downhill leads to the right minimum.

</div>

---
hideInToc: true
---

# The Fit in **Code**

<div class="grid-2 gap-md mt-sm" style="grid-template-columns: 1.75fr 1fr;">

<div>

```python
def model(m, A, mu, sigma, c0, c1):
    peak = A * np.exp(-(m - mu)**2 / (2 * sigma**2))
    return peak + c0 + c1 * (m - 1865)

p0 = [2300, 1865, 8, 1400, 0]
popt, pcov = curve_fit(model, m, n, p0=p0,
                       sigma=s, absolute_sigma=True)
err = np.sqrt(np.diag(pcov))
pull = (n - model(m, *popt)) / s
chi2 = np.sum(pull**2)
names = ["A", "mu", "sigma", "c0", "c1"]
for name, v, e in zip(names, popt, err):
    print(f"{name:5s} = {v:9.3f} +- {e:.3f}")
print(f"chi2 = {chi2:.1f}, ndf = {len(m) - 5}")
```

</div>

<div class="card card-success card-glass pad-compact">

## 🖨️ **Output**

```text
A     =  2190.942 +- 27.180
mu    =  1864.472 +- 0.096
sigma =     7.645 +- 0.099
c0    =  1414.085 +- 7.654
c1    =    -1.508 +- 0.222
chi2 = 53.4, ndf = 40
```

`*popt` passes the five values as five arguments.

</div>

</div>

<!--
Speaker: m, n and s are the arrays of the slide "Counts and Their
Uncertainty". curve_fit evaluated the model 31 times. Plain gradient descent
with one learning rate for the five parameters is at chi2 = 57.6 after
100 000 steps. (~3 min)
-->

---
hideInToc: true
---

# The Fit and Its **Pulls**

<img class="fig" src="/figures/viz_fitting_d0_fit.svg" style="display:block;margin:0.4rem auto 0;max-width:100%;max-height:420px;">

---
hideInToc: true
---

# What the Result **Says**

<div class="card card-success card-glass pad-compact mt-md">

$$\mu = 1864.47 \pm 0.10\ \text{MeV}/c^2, \qquad \sigma = 7.65 \pm 0.10\ \text{MeV}/c^2, \qquad \chi^2/\text{ndf} = 53.4/40$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✅ **What it means**

- 0.10 MeV/c² is the statistical uncertainty: the scatter of $\mu$ over repetitions with as many new events
- Bins of 1 MeV give 1864.48, bins of 3 MeV give 1864.50: less than the uncertainty
- $\sigma$ is the mass resolution of the detector. The natural width of the D⁰ is a billion times smaller

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **What it does not mean**

- It is not a measurement of the D⁰ mass. The Particle Data Group value is 1864.84 ± 0.05 MeV/c². The fit lies 0.37 below, nearly four times its statistical uncertainty
- The fit knows nothing of the calibration of the detector or of the true shape of the peak. Those are systematic uncertainties. This teaching file comes without them

</div>

</div>

<!--
Speaker: the honest sentence for a report: the peak in this file is at
1864.47 plus or minus 0.10 (statistical), with a Gaussian on a linear
background fitted between 1820 and 1910. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Goodness of **Fit**

---
hideInToc: true
---

# What χ² Should **Be**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **One per point**

If the model and the $\sigma_i$ are right, each pull is a Gaussian number of mean 0 and width 1. Its square is 1 on average. $N$ points give $\chi^2 \approx N$.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➖ **Minus one per parameter**

The fit moves the curve towards the points. Each of the $k$ fitted parameters lowers $\chi^2$ by 1 on average. A line through $N = 2$ points has $\chi^2 = 0$ every time.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$$\langle\chi^2\rangle = N - k = \text{ndf}, \qquad \text{standard deviation of } \chi^2 = \sqrt{2\,\text{ndf}}$$

ndf is the number of **degrees of freedom**.

</div>

<div class="card card-accent card-glass pad-compact table-compact mt-md">

| Fit | N | k | ndf | Expected χ² | Observed χ² |
| --- | --- | --- | --- | --- | --- |
| Pendulum, straight line | 9 | 2 | 7 | 7 ± 3.7 | 2.65 |
| D⁰ peak, Gaussian on a line | 45 | 5 | 40 | 40 ± 8.9 | 53.4 |

</div>

---
hideInToc: true
---

# The χ² Distribution and the **p-value**

<img class="fig" src="/figures/viz_fitting_chi2_dist.svg" style="display:block;margin:0.4rem auto 0;max-width:100%;max-height:300px;">

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

The **p-value** is the probability of a $\chi^2$ as large as the observed one or larger, if the model and the $\sigma_i$ are right. 0.08 means: 1 correct fit in 13 looks this bad or worse.

</div>

<div class="card card-secondary card-glass pad-compact">

```python
from scipy.stats import chi2
chi2.sf(2.65, 7)     # 0.915
chi2.sf(53.4, 40)    # 0.076
```

</div>

</div>

<!--
Speaker: sf is the survival function, one minus the cumulative distribution.
A p-value of 0.001 would say that the model or the uncertainties are wrong.
A p-value near 1 says the points lie closer to the curve than their
uncertainties allow for. (~3 min)
-->

---
hideInToc: true
---

# Reading **χ²/ndf**

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Near 1**

The points scatter around the model as much as their $\sigma_i$ say.

</div>

<div class="card card-warning card-glass pad-compact">

## ⬆️ **Far above 1**

The model misses structure in the data, or the $\sigma_i$ are too small.

</div>

<div class="card card-accent card-glass pad-compact">

## ⬇️ **Far below 1**

The $\sigma_i$ are too large, or the model has parameters that follow the noise.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

How near is near? The standard deviation of $\chi^2/\text{ndf}$ is $\sqrt{2/\text{ndf}}$: 0.53 for 7 degrees of freedom, 0.22 for 40.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🕰️ **Pendulum: 2.65/7 = 0.38**

1.2 standard deviations below 1. With $\sigma_{t_{10}} = 0.06$ s instead of 0.1 s it would be about 1. Seven degrees of freedom cannot tell the two apart.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⛰️ **D⁰: 53.4/40 = 1.33**

1.5 standard deviations above 1. Acceptable, and a hint that one Gaussian is not the exact shape of the peak.

</div>

</div>

---
hideInToc: true
---

# Residuals and **Pulls**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Two definitions**

$$r_i = y_i - f(x_i;\hat\theta), \qquad \text{pull}_i = \frac{r_i}{\sigma_i}$$

The residual has the unit of $y$. The pull has none: pulls of points with different $\sigma_i$ can be compared.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✅ **In a good fit the pulls**

- scatter around 0 with a standard deviation near 1
- show no pattern along $x$
- lie beyond ±2 in about 1 case in 20

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-accent card-glass pad-compact">

## ⛰️ **D⁰: 45 pulls**

Mean 0.01, standard deviation 1.09. Three lie beyond ±2, where two are expected. The largest is 2.9.

</div>

<div class="card card-info card-glass pad-compact">

## 🕰️ **Pendulum: 9 pulls**

0.12, 0.39, −0.93, 0.36, −0.52, 0.57, −0.38, 0.77, −0.39. All within ±1.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

$\chi^2$ is one number and does not say where the misfit is. The pull plot does. Draw it under every fit.

</div>

---
hideInToc: true
---

# A Model with Too Few **Terms**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ⛰️ **Four models for the D⁰ histogram**

| Model | k | χ² | ndf | χ²/ndf |
| --- | --- | --- | --- | --- |
| Straight line | 2 | 8337.0 | 43 | 193.9 |
| Gaussian on a constant | 4 | 99.4 | 41 | 2.42 |
| Gaussian on a line | 5 | 53.4 | 40 | 1.33 |
| Two Gaussians on a line | 7 | 37.4 | 38 | 0.98 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## 📉 **Is the added parameter needed?**

A parameter the data do not need lowers $\chi^2$ by about 1. The slope $c_1$ lowers it by 46.0. It is needed.

</div>

<div class="card card-accent card-glass pad-compact">

A second Gaussian with the same $\mu$ lowers $\chi^2$ by 16.0 for two parameters: the peak has wider tails than one Gaussian. $\mu$ moves to 1864.45.

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A model with too few terms **underfits**: $\chi^2/\text{ndf}$ is far above 1 and the pulls show a pattern. The pattern says which term is missing.

</div>

---
hideInToc: true
---

# Too Few Terms: the **Pulls**

<img class="fig" src="/figures/viz_fitting_d0_models.svg" style="display:block;margin:0.4rem auto 0;max-width:100%;max-height:425px;">

<!--
Speaker: top: the pulls are the peak itself. Middle: positive on the left,
negative on the right, a tilt that a constant background cannot follow.
Bottom: no pattern. (~2 min)
-->

---
hideInToc: true
---

# A Model with Too Many **Terms**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🕰️ **Polynomials through the pendulum points**

| Degree | k | χ² | ndf | T² at 1.2 m |
| --- | --- | --- | --- | --- |
| 0 | 1 | 11 954.89 | 8 | 1.88 |
| 1 | 2 | 2.65 | 7 | 4.82 |
| 2 | 3 | 2.60 | 6 | 4.83 |
| 4 | 5 | 2.16 | 4 | 4.62 |
| 6 | 7 | 1.38 | 2 | 2.18 |
| 8 | 9 | 0.00 | 0 | −63.37 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

## 🎢 **Degree 8**

Nine parameters for nine points: the curve passes through every point, $\chi^2 = 0$, and no degree of freedom is left to test anything. At 1.2 m it predicts $T^2 = -63$ s²; the line, 4.82.

</div>

<div class="card card-secondary card-glass pad-compact">

From degree 1 to 2, $\chi^2$ falls by 0.04, and each further term buys less than 1. The line is enough.

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A model with too many terms **overfits**: it follows the scatter of these nine points and fails on the next one. The aim is a $\chi^2$ near ndf with the fewest parameters, not the smallest $\chi^2$.

</div>

---
hideInToc: true
---

# Too Few, Enough, Too **Many**

<div class="note-text mt-sm">

Left: a straight line through $T$ against $\ell$, the wrong model. The pulls form an arch. Middle: the line through $T^2$. Right: the polynomial of degree 8, with $4\ell$ subtracted.

</div>

<img class="fig" src="/figures/viz_fitting_overfit.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:335px;">

---
layout: section
hideInToc: true
---

# What Goes **Wrong**

---
hideInToc: true
---

# Starting **Values**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| `p0`: A, μ, σ, c₀, c₁ | Result | χ² | Message |
| --- | --- | --- | --- |
| 2300, 1865, 8, 1400, 0 | μ = 1864.47 ± 0.10 | 53.4 | none |
| 2300, 1850, 3, 1400, 0 | μ = 1864.47 ± 0.10 | 53.4 | none |
| 2300, 1840, 2, 1400, 0 | μ = 1827.57 ± 0.28, A = −2876 | 3285.3 | none |
| not given: all 1 | nothing moved but the line | 8337.0 | covariance could not be estimated |

</div>

<img class="fig" src="/figures/viz_fitting_start_values.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:215px;">

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ The third fit ends in a local minimum, reports small uncertainties and raises no warning. Plot the model at `p0` over the data before fitting.

</div>

<!--
Speaker: a Gaussian of width 2 at 1840 does not overlap the peak at 1865. The
derivative of chi2 with respect to mu is nearly zero there, so the descent has
no direction to the peak and fits a wide negative Gaussian instead. (~3 min)
-->

---
hideInToc: true
---

# Correlated **Parameters**

<img class="fig" src="/figures/viz_fitting_covariance.svg" style="display:block;margin:0.4rem auto 0;max-width:100%;max-height:285px;">

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ↔️ **ρ(A, σ) = −0.46**

A higher, narrower peak and a lower, wider one describe the data almost equally well. The data fix the area of the peak better than its height or width.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **The number of D⁰ in the peak**

$N_{\text{sig}} = A\,\sigma\sqrt{2\pi}\,/\,(2\ \text{MeV}) = 20\,990$. Its uncertainty is 280 with the covariance of $A$ and $\sigma$, and 380 without it.

</div>

</div>

---
hideInToc: true
---

# Errors That Are Not Gaussian: Small **Counts**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Four bins: 2, 4, 6, 8**

Fit a constant with $\sigma_i^2 = n_i$. The weighted mean becomes

$$\hat\mu = \frac{\sum_i n_i/n_i}{\sum_i 1/n_i} = \frac{4}{\tfrac12 + \tfrac14 + \tfrac16 + \tfrac18} = 3.84$$

The mean of the counts is 5. A bin that came out low gets a small $\sigma$, a large weight, and pulls the fit down.

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-secondary card-glass pad-compact">

## ⛰️ **The D⁰ bins above 1886**

The same fit gives 1362.1; the mean of the 12 counts is 1363.8. At 1400 entries per bin the effect is 0.1 %.

</div>

<div class="card card-warning card-glass pad-compact">

## 0️⃣ **An empty bin**

$\sigma = \sqrt{0} = 0$ divides by zero. With the window 1800 to 1930 and its 8 empty bins, `curve_fit` returns the starting values and infinite uncertainties.

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The remedy is the likelihood of the right distribution. For Poisson counts, $-2\ln L = 2\sum_i \big(f_i - n_i \ln f_i\big) + \text{const}$ with $f_i = f(x_i;\theta)$. Minimising $-2\ln L$ works for every distribution. It gives $\chi^2$ only for the Gaussian.

</div>

---
hideInToc: true
---

# Errors That Are Not Gaussian: an **Outlier**

<div class="note-text mt-sm">

One value of the pendulum table typed with two digits exchanged: 16.21 in place of 12.61. The fit gives $g = 10.09 \pm 0.09$ m/s² with $\chi^2 = 884.7$ for 7 degrees of freedom. The pull of that point is 28.

</div>

<img class="fig" src="/figures/viz_fitting_outlier.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:300px;">

<div class="card card-warning card-glass pad-compact mt-sm">

The square in $\chi^2$ gives a point 28σ away the weight of 800 ordinary points. Find it in the pull plot, go back to the source of the number, and correct it or remove it with the reason written down. A point is never removed only because it fits badly.

</div>

---
hideInToc: true
---

# What χ² Cannot **See**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📏 **An error common to all points**

| The table | g (m/s²) | χ² |
| --- | --- | --- |
| as measured | 9.845 ± 0.090 | 2.647 |
| every length 1 % too long | 9.943 ± 0.091 | 2.647 |
| every t₁₀ 0.2 s too long | 9.707 ± 0.089 | 2.581 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

## 🙈 **The fit stays good**

A stretched tape measure moves $g$ by 0.10, more than its uncertainty, and leaves $\chi^2$ unchanged in every digit.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📣 **Statistical and systematic**

The uncertainty from a fit is **statistical**: it comes from the scatter of the points and shrinks with more points. An error shared by all points is **systematic**. It is estimated and reported separately.

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

With every $t_{10}$ 0.2 s too long, the intercept becomes $0.036 \pm 0.020$ s², 1.8σ from zero. The free intercept is the one place where this error leaves a trace.

</div>

---
hideInToc: true
---

# Reporting a **Fit**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **What a reader needs**

1. The model, as a formula
2. The data, and where the $\sigma_i$ come from
3. The method and the starting values
4. Each parameter as value ± uncertainty, with its unit
5. The correlation, if a result uses two parameters
6. $\chi^2$ and the number of degrees of freedom
7. A figure of data and model, with the pulls below
8. What the uncertainty does not include

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-success card-glass pad-compact">

## 🕰️ **The pendulum, in two sentences**

"A weighted least-squares fit of $T^2 = a\,\ell + b$ to nine points, with 0.1 s assumed on the time of 10 swings, gives $a = 4.010 \pm 0.037$ s²/m and $b = 0.009 \pm 0.019$ s² ($\rho = -0.88$), with $\chi^2 = 2.65$ for 7 degrees of freedom. From the slope, $g = 9.84 \pm 0.09$ m/s² (statistical)."

</div>

<div class="card card-info card-glass pad-compact">

A number without an uncertainty cannot be compared with anything. An uncertainty without its assumptions cannot be checked.

</div>

</div>

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Derive **χ²** from the Gaussian likelihood: $-2\ln L = \chi^2 + \text{const}$

</div>

<div class="card card-success card-glass pad-compact">

✅ Fit a **straight line** from five sums, by hand and in NumPy

</div>

<div class="card card-success card-glass pad-compact">

✅ Get **uncertainties** and the covariance from the curvature of χ², with $\Delta\chi^2 = 1$

</div>

<div class="card card-success card-glass pad-compact">

✅ Minimise χ² by **gradient descent**: $\theta \leftarrow \theta - \eta\,\nabla\chi^2$

</div>

<div class="card card-success card-glass pad-compact">

✅ Fit a nonlinear model with **`curve_fit`**, with starting values and `absolute_sigma=True`

</div>

<div class="card card-success card-glass pad-compact">

✅ Judge a fit by **χ²/ndf** and the pulls, and say what its uncertainty leaves out

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **The two results of today**

Pendulum: $g = 9.84 \pm 0.09$ m/s², $\chi^2/\text{ndf} = 2.65/7$. D⁰ peak: $\mu = 1864.47 \pm 0.10$ MeV/c², $\sigma = 7.65 \pm 0.10$ MeV/c², $\chi^2/\text{ndf} = 53.4/40$. Both uncertainties are statistical.

</div>

<!--
Speaker: every line of this recap was derived or computed today on one of two
files. (~1 min)
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
  question="Three points have residuals 0.2, −0.3 and 0.1 from a model. Each has σ = 0.1. What is χ²?"
  :options="[
    '6',
    '14',
    '0.14',
    '1.4'
  ]"
  :correct="1"
  explanation="The pulls are 2, −3 and 1. Their squares are 4, 9 and 1, and the sum is 14. The point 3σ away contributes 9 of the 14."
/>

---
hideInToc: true
---

<MCQ
  question="A histogram with 30 bins is fitted with a Gaussian on a parabola: six parameters. How many degrees of freedom does the fit have?"
  :options="[
    '30',
    '36',
    '24',
    '6'
  ]"
  :correct="2"
  explanation="ndf = N − k = 30 − 6 = 24. If the model and the uncertainties are right, χ² is expected at 24, with a standard deviation of √48 = 6.9."
/>

---
hideInToc: true
---

<MCQ
  question="A fit with one parameter has χ² = 12.0 at its minimum, θ = 5.00. At θ = 5.20, χ² is 13.0. What is the uncertainty of θ?"
  :options="[
    '1.0',
    '0.04',
    '13.0',
    '0.20'
  ]"
  :correct="3"
  explanation="The uncertainty is the distance from the minimum at which χ² has risen by 1. Here that is 5.20 − 5.00 = 0.20. At θ = 5.40, two σ away, χ² would be 12 + 4 = 16."
/>

---
hideInToc: true
---

<MCQ
  question="Gradient descent on χ²(θ) = (θ − 3)² starts at θ = 0 with the learning rate η = 0.25. Where is θ after one step?"
  :options="[
    '1.5',
    '3',
    '−1.5',
    '0.75'
  ]"
  :correct="0"
  explanation="The derivative at θ = 0 is 2 × (0 − 3) = −6. The step is θ − η × (−6) = 0 + 1.5 = 1.5. With η = 0.5 one step lands on the minimum. With η = 1 it lands on 6, as far from 3 as the start, and for any larger η the distance grows."
/>

---
hideInToc: true
---

<MCQ
  question="A fit of 27 points with 2 parameters gives χ² = 100. The model is known to be right. By what factor were the σ of the points too small?"
  :options="[
    '4',
    '2',
    '16',
    'They were too large, not too small'
  ]"
  :correct="1"
  explanation="ndf = 27 − 2 = 25 and χ²/ndf = 4. Each term of χ² contains 1/σ², so doubling every σ divides χ² by 4 and brings it to 25. The estimates of the parameters stay the same; their uncertainties double."
/>

---
hideInToc: true
---

<MCQ
  question="A straight-line fit of T² against the length of a pendulum gives the slope a = 3.95 ± 0.04 s²/m. What is g = 4π²/a?"
  :options="[
    '9.99 ± 0.04 m/s²',
    '9.99 ± 0.01 m/s²',
    '9.99 ± 0.10 m/s²',
    '9.81 ± 0.10 m/s²'
  ]"
  :correct="2"
  explanation="g = 39.478 / 3.95 = 9.99. The relative uncertainty of g equals that of a, 0.04 / 3.95 = 1.0 %, so σ = 9.99 × 0.0101 = 0.10 m/s²."
/>
