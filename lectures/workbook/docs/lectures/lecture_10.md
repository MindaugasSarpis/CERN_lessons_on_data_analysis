# 10: Data Fitting from First Principles

Lecture 9 ended with the likelihood: the estimate of a quantity measured
several times is the value that makes the measured data most probable, and
for Gaussian uncertainties that value is the weighted mean. Lecture 10 takes
the next step. The measured quantity now changes with a second quantity, a
model says how, and the same likelihood gives the method of least squares.
Every step is carried out on the pendulum table of Lecture 2, and the
nonlinear case on the mass column of `D0_KPi.csv`.

## What the lecture covers

1. **What a fit is** — the pendulum table as T² against length, a straight
   line whose slope is 4π²/g; the uncertainty assumed for each point, 0.1 s
   on the time of ten swings, propagated to T²; the three parts of a fit: a
   model, data with uncertainties, a measure of mismatch.
2. **From likelihood to χ²** — one Gaussian per point, the product over all
   points, the logarithm: −2 ln L = χ² + const. χ² worked out for one line by
   hand. The weighted mean as the fit of a constant.
3. **The straight line in closed form** — two derivatives set to zero, the
   normal equations, slope and intercept from five sums; the sums of the
   pendulum table, row by row; the same in NumPy.
4. **Uncertainties of the parameters** — the slope as a weighted sum of the
   data and its uncertainty by error propagation; χ² around its minimum, the
   rule Δχ² = 1, the covariance matrix as the inverse of the curvature
   matrix; why slope and intercept are correlated; g with its uncertainty.
5. **The same in matrix form** — the design matrix, the normal equations for
   any model that is linear in its parameters, `np.linalg.lstsq` and
   `np.polyfit`.
6. **Models that are not linear** — the gradient, the update rule
   θ ← θ − η∇χ², five steps by hand, a learning rate that is too large;
   why the descent is slow and what Newton's step does; SciPy and
   `curve_fit` with its arguments; the D⁰ mass peak fitted with a Gaussian
   on a linear background, and what the result means.
7. **Goodness of fit** — the expected χ², degrees of freedom, the p-value,
   χ²/ndf, residuals and pulls; a model with too few terms and one with too
   many.
8. **What goes wrong** — starting values and a local minimum, correlated
   parameters, small counts, an outlier, an error common to all points;
   how a fit is reported.

## The results of the lecture

| | Result |
|--|--|
| Pendulum, slope | a = 4.010 ± 0.037 s²/m |
| Pendulum, intercept | b = 0.009 ± 0.019 s², correlation with a: −0.88 |
| Pendulum, g | 9.84 ± 0.09 m/s², with χ² = 2.65 for 7 degrees of freedom |
| D⁰ peak, position | 1864.47 ± 0.10 MeV/c² |
| D⁰ peak, width | 7.65 ± 0.10 MeV/c², with χ² = 53.4 for 40 degrees of freedom |

All uncertainties are statistical. The closed formulas, `np.polyfit` and
`curve_fit` give the same pendulum numbers to six decimals. Every number
of the lecture is printed by `python figures/src/fitting.py` in the course
repository, which reads `pendulum.csv` and `D0_KPi.csv`.

## The lecture in 90 minutes

The lecture is slides 1–73 and estimates about 143 min. Slides 74–80 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | What Lecture 9 established |
| 0:03 | 5–9 | The pendulum table, its uncertainties, the three parts of a fit |
| 0:12 | 10–14 | From the likelihood to χ² |
| 0:21 | 16–22 | The straight line in closed form, on the pendulum |
| 0:34 | 24–31 | Uncertainties, Δχ² = 1, the covariance matrix, g |
| 0:43 | 37–45 | Gradient descent |
| 0:59 | 46–47 | SciPy and `curve_fit` |
| 1:03 | 50–56 | The D⁰ mass peak |
| 1:14 | 57–64 | Goodness of fit |
| 1:24 | 66–70 | Starting values, an outlier |
| 1:29 | 73 | Recap |
| 1:31 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Learning Objectives | 3 | 2 min |
| The Weighted Mean Is a Fit | 15 | 3 min |
| The Same in NumPy: the seminar types it | 23 | 4 min |
| The Slope Is a Sum over the Data | 25 | 2 min |
| χ² Around Its Minimum | 27 | 2 min |
| Why Slope and Intercept Are Correlated | 30 | 2 min |
| The Same in Matrix Form, the whole section | 32–36 | 10 min |
| Gradient Descent in NumPy | 44 | 4 min |
| `absolute_sigma`: the Default Rescales | 48 | 2 min |
| Three Ways, One Result | 49 | 4 min |
| Starting Values from the Plot | 53 | 2 min |
| The χ² Distribution and the p-value | 59 | 2 min |
| A Model with Too Few Terms, and its pulls | 62–63 | 3 min |
| Too Few, Enough, Too Many | 65 | 1 min |
| Correlated Parameters | 68 | 2 min |
| Errors That Are Not Gaussian: Small Counts | 69 | 3 min |
| What χ² Cannot See | 71 | 2 min |
| Reporting a Fit | 72 | 3 min |

- **Do not cut** slides 11–13 (the derivation of χ²), 17–21 (the normal
  equations and the five sums of the pendulum), 26 and 31 (the
  uncertainties and g), and 40–42 (the update rule, the steps by hand, the
  learning rate that is too large). The seminar computes exactly these
  numbers, and the rest of the lecture stands on them.
- **If slide 48 is skipped**, say its one sentence at slide 47: with real
  uncertainties, `absolute_sigma=True` belongs in every call.
- **Slide 20** (The Pendulum: Five Sums): let the room compute the first row
  on a calculator. 1/0.01804² = 3072.75, times 0.2 is 614.55, times 0.8136
  is 2500.
- **Slide 21** (Slope and Intercept): the calculator values use the sums
  rounded to two decimals and give a denominator of 8 874 543. NumPy keeps
  all digits and gets 8 874 453. Slope and intercept agree to the four
  decimals shown.
- **Slide 41** (Gradient Descent by Hand): the room does the first step on
  the calculator and gets a = 3.2064, b = 0.3451.
- **Slides 23, 44 and 49** hold code that runs on the slide with the ▶
  button. The first run loads Python into the browser and takes some
  seconds. The same code runs in VS Code.
  On slide 44, set `eta` to `1e-4` and run again to see χ² grow.
- **Slide 54** (The Fit in Code) is static: the browser has no access to
  `D0_KPi.csv`. To show it live, run the code of slides 51 and 54 in VS
  Code from the project folder.
- **Slide 15**: the nine values of g, row by row, are 9.70, 9.70, 9.93,
  9.75, 9.87, 9.74, 9.86, 9.74, 9.86 m/s², with uncertainties 0.22, 0.18,
  0.16, 0.14, 0.13, 0.12, 0.11, 0.10, 0.10.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 74–80: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. Three points have residuals 0.2, −0.3 and 0.1 from a model, each with
   σ = 0.1. What is χ²?
   *14. The pulls are 2, −3 and 1, and their squares add up to 4 + 9 + 1.*
2. A histogram with 30 bins is fitted with a Gaussian on a parabola, six
   parameters. How many degrees of freedom does the fit have?
   *24, the number of points minus the number of fitted parameters.*
3. A one-parameter fit has χ² = 12.0 at its minimum θ = 5.00, and 13.0 at
   θ = 5.20. What is the uncertainty of θ?
   *0.20, the distance at which χ² has risen by 1.*
4. Gradient descent on χ²(θ) = (θ − 3)² starts at θ = 0 with η = 0.25.
   Where is θ after one step?
   *1.5. The derivative at 0 is −6, and 0 − 0.25 × (−6) = 1.5. With η = 1
   the step lands on 6, as far from the minimum as the start.*
5. A fit of 27 points with 2 parameters gives χ² = 100, and the model is
   known to be right. By what factor were the uncertainties of the points
   too small?
   *By 2. χ²/ndf = 100/25 = 4, and doubling every σ divides χ² by 4.*
6. A straight-line fit gives the slope a = 3.95 ± 0.04 s²/m. What is
   g = 4π²/a?
   *9.99 ± 0.10 m/s². The relative uncertainty of g is that of a, 1.0 %.*

## Paired seminar

[Seminar 10 — Fit a Straight Line and Measure g](../seminars/seminar_10.md)
builds one script, `scripts/fit_pendulum.py`. The room reads the pendulum
table, computes the five sums, slope and intercept with their uncertainties
and covariance, g with its uncertainty and χ², repeats the fit with
`curve_fit`, and plots the residuals.

## Take-aways

- A fit has three parts: a model, data with uncertainties, and a measure of
  mismatch. For Gaussian uncertainties the measure follows from the
  likelihood: −2 ln L = χ² + const.
- χ² is the sum of the squared pulls. A point 1σ from the model adds 1, a
  point 3σ away adds 9.
- For a straight line the minimum of χ² is found in closed form from five
  sums over the data. The same sums give the uncertainties of slope and
  intercept and their covariance.
- Moving a parameter by one uncertainty raises χ² by 1. The covariance
  matrix is the inverse of the curvature matrix of χ² at its minimum.
- A quantity computed from fitted parameters gets its uncertainty by
  propagation. If it uses two parameters, their covariance enters.
- Gradient descent, θ ← θ − η∇χ², finds the minimum of any χ². A learning
  rate that is too large makes χ² grow.
- `curve_fit(f, x, y, p0=..., sigma=..., absolute_sigma=True)` returns the
  estimates and the covariance matrix. Starting values that put the model
  near the data lead to the right minimum; others may not.
- χ² is expected near the number of degrees of freedom, points minus
  parameters. The pulls show where a model fails. Too few terms leave a
  pattern in them; too many terms follow the noise.
- The uncertainty from a fit is statistical. An error shared by all points
  changes the result and leaves χ² as it was.
