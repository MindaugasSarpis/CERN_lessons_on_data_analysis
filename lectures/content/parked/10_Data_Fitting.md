<!--
Parked slides from slides/10_Data_Fitting.md, taken out on 2026-10-06.

This file is not in decks.json: it is not built, not gated and not deployed.
To put a slide back, move it into the lecture file at the place its comment
names. The deck estimates close to the 145-min ceiling, so a slide put back
needs another one taken out.
-->

<!-- Parked 2026-10-06 from Lecture 10, section 'From Likelihood to χ²', after 'χ² in Numbers': a detour between 'the best of all lines' and the closed form, and a number-for-number repeat of Lecture 09's 'g from Nine Measurements'; its result (9.806 ± 0.042 through the origin) stays on 'The Uncertainty of g'. Moved out to keep the deck at or under 145 min after the storytelling rework (opening on Lecture 09's window table, the D0 runner and the closing answer slide). -->

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


<!-- Parked 2026-10-06 from Lecture 10, section 'The Same in Matrix Form', after 'One Equation for All Points': the fifth computation of the same pendulum numbers; V is now one line on 'One Equation for All Points'. Moved out to keep the deck at or under 145 min after the storytelling rework (opening on Lecture 09's window table, the D0 runner and the closing answer slide). -->

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


<!-- Parked 2026-10-06 from Lecture 10, section 'Models That Are Not Linear', after 'Why the Descent Is Slow, and the Remedy': an install slide; Seminar 10 installs SciPy, and 'curve_fit: the Call' says what SciPy is in one line. Moved out to keep the deck at or under 145 min after the storytelling rework (opening on Lecture 09's window table, the D0 runner and the closing answer slide). -->

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


<!-- Parked 2026-10-06 from Lecture 10, section 'What Goes Wrong', after 'Starting Values': the lesson of 'Why Slope and Intercept Are Correlated' a second time, on N_sig. Moved out to keep the deck at or under 145 min after the storytelling rework (opening on Lecture 09's window table, the D0 runner and the closing answer slide). -->

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

