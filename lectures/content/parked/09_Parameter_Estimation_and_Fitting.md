<!--
Parked slides from the Data Fitting deck (slides/10_Data_Fitting.md as of
commit 328aba2), taken out on 2026-11-09 when the deck was rebuilt as
slides/09_Parameter_Estimation_and_Fitting.md on the weather log
(docs/superpowers/specs/2026-11-09-weeks-8-12-ideas-and-tools-design.md).

This file is not in decks.json: it is not built, not gated and not deployed.
The new deck teaches each idea on the weather log; the pendulum table and the
LHCb file appear only in its For the Curious. These slides fit there if wanted:
the D⁰ starting values, errors that are not Gaussian, and the number to
report for the D⁰ mass. They speak of "Lecture 09" for the probability lecture,
now Lecture 8. Their figures are still drawn by figures/src/fitting.py.
The whole old deck: git show 328aba2:lectures/content/slides/10_Data_Fitting.md
-->

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 52 (Starting Values from the **Plot**), section 'The D⁰ Peak', after 'The Model: a Gaussian on a Line'. -->

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

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 66 (Starting **Values**), section 'What Goes Wrong', its first slide. -->

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

<img class="fig" src="/figures/viz_fitting_start_values.svg" style="display:block;margin:0.5rem auto 0;max-width:100%;max-height:190px;">

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ The third fit ends in a local minimum, reports small uncertainties and raises no warning. Plot the model at `p0` over the data before fitting.

</div>

<!--
Speaker: a Gaussian of width 2 at 1840 does not overlap the peak at 1865. The
derivative of chi2 with respect to mu is nearly zero there, so the descent has
no direction to the peak and fits a wide negative Gaussian instead. Ask the
room first: which number on the output says that something is wrong? chi2 =
3285 for 40 degrees of freedom, and a negative height A. To show it live,
change p0 in the runner of "The Fit in Code" to [2300, 1840, 2, 1400, 0].
(~3 min)
-->

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 67 (Errors That Are Not Gaussian: Small **Counts**), section 'What Goes Wrong', after 'Starting Values'. -->

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

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 68 (Errors That Are Not Gaussian: an **Outlier**), section 'What Goes Wrong', after 'Errors That Are Not Gaussian: Small Counts'. -->

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

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 69 (What χ² Cannot **See**), section 'What Goes Wrong', after 'Errors That Are Not Gaussian: an Outlier'. -->

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

<!-- Parked 2026-11-09 from the Data Fitting deck, old slide 71 (The Number to **Report**), the wrap-up, after 'Reporting a Fit'. -->

---
hideInToc: true
---

# The Number to **Report**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ⛰️ **One histogram, four models**

| Model, 1820 to 1910 | k | χ²/ndf | p | μ (MeV/c²) |
| --- | --- | --- | --- | --- |
| Gaussian on a constant | 4 | 99.4/41 | 9 × 10⁻⁷ | 1864.34 ± 0.09 |
| Gaussian on a line | 5 | 53.4/40 | 0.08 | 1864.47 ± 0.10 |
| Gaussian on a parabola | 6 | 43.3/39 | 0.29 | 1864.46 ± 0.10 |
| Two Gaussians on a line | 7 | 37.4/38 | 0.50 | 1864.45 ± 0.10 |

</div>

<div class="stack-tight" style="margin-top:0;">

<div class="card card-warning card-glass pad-compact">

## 📏 **The model moves μ**

A background with no slope moves μ by 0.13, more than the statistical uncertainty. χ² rejects that model. The three models it accepts agree within 0.02.

</div>

<div class="card card-success card-glass pad-compact">

## 📝 **The sentence for the report**

"The peak is at μ = 1864.47 ± 0.10 (stat) MeV/c²: a Gaussian on a linear background, fitted from 1820 to 1910 MeV/c², χ² = 53.4 for 40 degrees of freedom."

</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

No window and no model on these slides reaches the PDG value 1864.84. The gap of 0.37 stays open, and the report says so: its uncertainty is statistical only.

</div>

<!--
Speaker: this answers the opening slide. Ask the room again which number they
would report: not one of the four means, but the fit, with its model, its
window and its chi2. The constant background is the middle panel of "Too Few
Terms: the Pulls": the tilt in its pulls is the slope it misses. (~3 min)
-->
