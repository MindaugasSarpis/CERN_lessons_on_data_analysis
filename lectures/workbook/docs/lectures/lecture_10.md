# 10: Data Fitting from First Principles

Lecture 9 left two loose ends. Its table of four means of the mass
column, each with a small standard error, disagreed by 0.7 MeV/c², because
the rows are a peak on a flat part that is not D⁰. And the nine pendulum rows
gave g = 9.80 ± 0.04 m/s² with the formula T² = 4π²ℓ/g taken as exact.
Lecture 10 opens on the first of them, "which of the four numbers would you
report?", and answers it with a fit. The fit is derived from the same
likelihood and built on the pendulum table (`pendulum.csv`, 97 bytes, as
`scripts/clean_pendulum.py` writes it), where every step can be checked with
a calculator; then it is carried to the D⁰ peak of `D0_KPi.csv`.

## What the lecture covers

1. **The opening table** — Lecture 9's four means of column `M`, 1864.10 to
   1864.81 MeV/c², and the question which one to report.
2. **What a fit is** — the pendulum table as T² against length, a straight
   line whose slope is 4π²/g; the uncertainty assumed for each point, 0.1 s
   on the time of ten swings, propagated to T²; the three parts of a fit: a
   model, data with uncertainties, a measure of mismatch.
3. **From likelihood to χ²** — one Gaussian per point, the product over all
   points, the logarithm: −2 ln L = χ² + const. χ² worked out for three lines
   drawn by eye.
4. **The straight line in closed form** — two derivatives set to zero, the
   normal equations, slope and intercept from five sums; the sums of the
   pendulum table, row by row; the best line beats all three drawn by eye;
   the same in NumPy.
5. **Uncertainties of the parameters** — the slope as a weighted sum of the
   data and its uncertainty by error propagation; χ² around its minimum, the
   rule Δχ² = 1, the covariance matrix as the inverse of the curvature
   matrix; why slope and intercept are correlated; g with its uncertainty,
   and the intercept as the test of the formula.
6. **The same in matrix form** — the design matrix, the normal equations for
   any model that is linear in its parameters, `np.linalg.lstsq` and
   `np.polyfit`.
7. **Models that are not linear** — the gradient (the chain rule), the update
   rule θ ← θ − η∇χ², five steps by hand, a learning rate that is too large;
   why the descent is slow and what Newton's step does; `curve_fit` with its
   arguments.
8. **The D⁰ peak** — counts with Poisson uncertainties, a Gaussian on a
   linear background, starting values from the plot, the fit run on the
   slide, and the answer to the opening table: a mean follows its window, a
   fit does not.
9. **Goodness of fit** — the expected χ², degrees of freedom, the p-value,
   χ²/ndf, residuals and pulls; a model with too few terms and one with too
   many.
10. **What goes wrong** — starting values and a local minimum, small counts,
    an outlier, an error common to all points; how a fit is reported; the
    number to report for the peak, with the models that move it.

## The results of the lecture

| | Result |
|--|--|
| Pendulum, slope | a = 4.010 ± 0.037 s²/m |
| Pendulum, intercept | b = 0.009 ± 0.019 s², correlation with a: −0.88 |
| Pendulum, g | 9.84 ± 0.09 m/s², with χ² = 2.65 for 7 degrees of freedom |
| D⁰ peak, position | 1864.47 ± 0.10 MeV/c² |
| D⁰ peak, width | 7.65 ± 0.10 MeV/c², with χ² = 53.4 for 40 degrees of freedom |
| Mean of `M`, window 1855–1875 and 1854–1874 | 1864.81 and 1864.06 ± 0.03 MeV/c² |
| Fit, window moved 4 MeV either way | μ = 1864.45 and 1864.50 MeV/c² |
| Fit, background without slope (rejected, χ² = 99.4/41) | μ = 1864.34 ± 0.09 MeV/c² |
| Fit, background parabola; two Gaussians on a line | μ = 1864.46 and 1864.45 MeV/c² |

All uncertainties are statistical. The closed formulas, `np.polyfit` and
`curve_fit` give the same pendulum numbers to six decimals. The PDG value of
the D⁰ mass, 1864.84 ± 0.05 MeV/c², lies 0.37 above the fit, and no window or
model in the table reaches it. The numbers of the first seven rows are printed
by `python figures/src/fitting.py` in the course repository, which reads
`pendulum.csv` and `D0_KPi.csv`. The last four rows use the same histogram
(45 bins of 2 MeV) and the same `curve_fit` call with the window or the model
changed as named.

## The lecture in 90 minutes

The lecture is slides 1–72 and estimates about 143 min. Slides 73–79 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.
The opening question of slide 2 is answered on slide 55, at about minute 58.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3, 5 | The opening table and the vote; what Lecture 9 established |
| 0:05 | 6–10 | The pendulum table, its uncertainties, three lines drawn by eye |
| 0:12 | 11–15 | From the likelihood to χ² |
| 0:20 | 16–22 | The straight line in closed form, on the pendulum |
| 0:30 | 24, 26, 28, 31 | Uncertainties, Δχ² = 1, g and the test of the intercept |
| 0:37 | 36–41 | The gradient, the update rule, steps by hand, a learning rate too large |
| 0:46 | 44–45 | Newton's step and the `curve_fit` call |
| 0:48 | 48–51, 53–55 | The D⁰ peak, the fit run live, the opening table answered |
| 0:58 | 56–57, 59–61, 63 | Goodness of fit |
| 1:08 | 65–66, 68–69 | Starting values, an outlier, what χ² cannot see |
| 1:15 | 71–72 | The number to report, Recap |
| 1:21 | | Questions; move to the seminar |

The plan leaves about nine minutes for the two votes and for questions.

| Skip | Slides | Saves |
|--|--|--|
| Learning Objectives | 4 | 2 min |
| The Same in NumPy: the seminar types it | 23 | 4 min |
| The Slope Is a Sum over the Data | 25 | 2 min |
| χ² Around Its Minimum | 27 | 2 min |
| The Covariance Matrix | 29 | 2 min |
| Why Slope and Intercept Are Correlated | 30 | 2 min |
| The Same in Matrix Form, the whole section | 32–35 | 8 min |
| Two Learning Rates, Drawn | 42 | 1 min |
| Gradient Descent in NumPy | 43 | 4 min |
| `absolute_sigma`: the Default Rescales | 46 | 2 min |
| Three Ways, One Result | 47 | 4 min |
| Starting Values from the Plot | 52 | 2 min |
| The χ² Distribution and the p-value | 58 | 2 min |
| Too Few Terms: the Pulls | 62 | 1 min |
| Too Few, Enough, Too Many | 64 | 1 min |
| Errors That Are Not Gaussian: Small Counts | 67 | 3 min |
| Reporting a Fit | 70 | 3 min |

- **Do not cut** slide 2 (the opening table), slides 12–14 (the derivation
  of χ²), 17–21 (the normal equations and the five sums of the pendulum),
  26 and 31 (the uncertainties and g), 39–41 (the update rule, the steps by
  hand, the learning rate that is too large), 53 and 55 (the D⁰ fit and the
  answer to the opening table), and **71–72, the closing: do not cut**. The
  seminar computes the pendulum numbers, and the closing answers the question
  the lecture opens on.
- **Slide 2**: take a vote on the four rows and write it on the board. Most
  pick the last row, nearest the PDG value. Slide 55 answers it: Lecture 9's
  windows were all centred on 1865, and a window moved by 1 MeV moves the
  mean by 0.75.
- **If slide 46 is skipped**, say its one sentence at slide 45: with real
  uncertainties, `absolute_sigma=True` belongs in every call.
- **Slide 20** (The Pendulum: Five Sums): let the room compute the first row
  on a calculator. 1/0.01804² = 3072.75, times 0.2 is 614.55, times 0.8136
  is 2500.
- **Slide 21** (Slope and Intercept): the calculator values use the sums
  rounded to two decimals and give a denominator of 8 874 543. NumPy keeps
  all digits and gets 8 874 453. Slope and intercept agree to the four
  decimals shown.
- **Slide 40** (Gradient Descent by Hand): the room does the first step on
  the calculator and gets a = 3.2064, b = 0.3451.
- **Slides 23, 43, 47 and 53** hold code that runs on the slide with the ▶
  button. The first run loads Python into the browser and takes some
  seconds. The same code runs in VS Code.
  On slide 43, set `eta` to `1e-4` and run again to see χ² grow.
- **Slide 53** (The Fit in Code) fits the D⁰ peak live. The 45 bin counts
  are typed into the page, because the browser cannot read `D0_KPi.csv`; in
  a script they come from the `np.histogram` line of slide 50. At slide 66
  (Starting Values), change `p0` in this runner to `[2300, 1840, 2, 1400, 0]`
  and run it: μ = 1827.57, A = −2876, χ² = 3285.3, and no warning.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 73–79: six quiz slides for students to try afterwards. The same
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
- A mean over a window follows the window: moved by 1 MeV, it moves by
  0.75. A fit of peak and background moves by 0.03 when its window moves by
  4 MeV. A background model that χ² rejects moves μ by 0.13; the models it
  accepts agree within 0.02.
- The uncertainty from a fit is statistical. An error shared by all points
  changes the result and leaves χ² as it was.
