# 9: Parameter Estimation and Fitting

Lecture 8 asked how sure the mean of the weather log is, 7.16 ± 0.22 °C,
and found that the ten yearly means scatter by 0.70 °C. Lecture 9 asks
whether it is getting warmer. Two years picked from ten give any answer
(+1.80 °C from 2017 to 2023, −2.33 °C from 2023 to 2025), so the lecture
builds the tool that uses all ten: a model with parameters, fitted by least
squares. It starts with the smallest fit there is, one number for four hours
of 21 July 2019, and teaches the derivative there, checked with a small
nudge. From the Gaussian of Lecture 8 it derives χ², works out the straight
line in closed form from five sums of the ten yearly means, and reads the
slope's uncertainty off χ²: −0.56 ± 0.77 °C per decade, so ten years cannot
tell. Then it walks downhill by gradient descent, first by hand and then for
the line, fits the yearly cycle of the 3648 daily means (an amplitude of
11.18 °C, coldest on 16 January), and reads the residuals: what they show,
when χ² is a test, and what too few or too many parameters do. No library is
used on a slide; the seminar does the same with NumPy.

## What the lecture covers

1. **A model has parameters**: three models of the weather log with one,
   two and three parameters; the ten yearly means with error bars of
   ± 0.70 °C (7 of the 10 bars reach 7.16); the three parts of a fit (a model, data with
   their scatter, a measure of the miss); the symbols of the lecture; the sum
   of squared misses S(μ) of the four hours, smallest at their mean, 25.275;
   why squares and not the plain or the absolute misses; the derivative as
   the slope of S, by a nudge (−2.196) and by the rule for a square (−2.2);
   the mean as the least-squares value.
2. **From likelihood to χ²**: where σ = 0.70 °C comes from (the scatter of
   the ten yearly means, not the hours); the Gaussian as a bell of width σ
   (68 % within ± σ, 7 of the 10 years; a density, 0.57 per °C at the top);
   the density of one yearly mean (2016: 0.47 per °C); the likelihood of ten
   independent years; the logarithm (ln 0.47 = −0.755, a product becomes a
   sum), which turns maximum likelihood into minimum χ²; χ² of a flat
   line year by year (9.08) and of a rising one (12.64); a line from the
   room, live.
3. **The best line in closed form**: the derivatives of χ² for a line, the
   normal equations and their five sums, slope and intercept, the ten years
   in a table and the sums pushed through: −0.056 °C a year and 7.41 °C,
   χ² = 8.56; the same in plain Python; why x counts from 2016; the slope as
   the correlation r times the spreads.
4. **How sure is the slope**: χ² against the slope, a parabola; the rule
   Δχ² = 1 and why; σ_a in closed form, 0.077 °C a year; the intercept's ±;
   the line's value for 2026 with its ±; −0.56 ± 0.77 °C per decade, so ten
   years cannot show a trend; what ± 0.77 means as 68 % and 95 %; the ± for
   20 and 40 years.
5. **Walking downhill**: why the cycle has no closed form; the update rule
   θ ← θ − η dS/dθ; three steps by hand on the four hours; a step that is too
   large; why each step multiplies the gap by 1 − 8η; the step size live; the
   rule for the line, the miss times the input; gradient descent on the ten
   years, live; its path down a narrow valley.
6. **A curve, the yearly cycle**: the daily means; a cosine with a level, an
   amplitude and a coldest day; two days pushed through with starting values
   read off the plot; the descent from them; the fitted cycle, 7.18 °C,
   11.18 °C, 16 January.
7. **Residuals**: the residuals and the pulls of the line; what χ² should
   be, and why it is not a test when σ comes from the same points; the
   residuals of the cycle in runs (next-day r = 0.875); the honest ± of the
   amplitude from ten one-year fits (0.25 against 0.07); the same trend from
   3648 days with a ± that is too small; too few parameters (a constant
   through the cycle); too many (a polynomial of degree 9, 307 °C for 2026);
   how many parameters; reading residuals; a sensor shift that χ² cannot see.
8. **Wrap-up**: the same line by every method; reporting a fit, with the
   trend and the cycle as two sentences; a checklist for a fit; the opening
   question answered; the recap.
9. **For the curious**, after the recap and outside the lecture time: σ_a
   derived; the correlation of slope and intercept, and x centred, which
   gives 7.16 ± 0.22; the normal equations as matrices; the cycle as a
   linear model; Newton's step and Levenberg–Marquardt; the χ² distribution
   and the p-value; the pendulum's g; the D⁰ mass peak of LHCb, fitted, and
   with too few terms.

## Mathematics used for the first time

The lecture teaches each tool once, where it is first needed, with numbers.

| Tool | Slide | As taught there |
|--|--|--|
| An error bar | 6 | ± σ on each yearly mean: 2016, 7.60 ± 0.70, a bar from 6.90 to 8.30 °C; 7 of 10 bars reach 7.16 |
| Σ, ∏, a hat | 8 | Read aloud, with the four hours as the example |
| The derivative | 12–13 | The slope of S for a small nudge h; the rule d(y − μ)²/dμ = −2(y − μ) from (d − h)² − d² = −2dh + h² |
| Setting a derivative to zero | 14 | The lowest point of S, where the slope is zero: the mean |
| The Gaussian bell, a density | 18 | μ = 7.16, σ = 0.70 °C: 68 % of the area within ± σ, 95 % within ± 2σ; the height a chance per °C, 0.57 at the top |
| The logarithm | 22 | ln x, the power of e that gives x: ln 0.47 = −0.755; ln(0.47 × 0.37) = ln 0.47 + ln 0.37 = −1.749, so a product becomes a sum |
| Partial derivatives | 28 | One parameter moves, the other stays; the extra x_i for the slope |
| The second derivative | 50–51 | How fast the slope changes, 2N = 8 for the four hours: the limit of the step size |

## The lecture, part by part

The lecture is slides 1–81 and estimates about 123 min, so in the two-hour
slot **plan to skip the slides of the second table** (about 10 min).
Slides 82–92 are the optional section For the Curious, and slides 93–101 the
self-check quizzes; neither takes lecture time. To jump, type the slide
number and press Enter.

| Slides | Part |
|--|--|
| 1–3 | The question: is it getting warmer? Two picked pairs of years, +1.80 and −2.33 °C |
| 4–15 | A model has parameters; the yearly means with error bars; S(μ) of four hours; why squares; the derivative and its nudge; the mean as the least-squares value; the slope checked live |
| 16–26 | σ = 0.70 °C; the Gaussian bell; the Gaussian of one year; the likelihood of ten; the logarithm; minimum χ²; χ² of a flat line year by year; two guessed lines; a line from the room, dragged live |
| 27–34 | The derivatives for a line; the normal equations; the formulas; the table of ten years; the sums pushed through; the best line; the same in Python, live |
| 37–40, 42–44 | χ² around its minimum; Δχ² = 1; σ_a; the value for 2026; −0.56 ± 0.77 °C per decade; what the ± means |
| 46–50, 52–55 | No closed form for the cycle; the update rule; three steps by hand; a step too large; the step size, live; the rule for a line; descent on ten years, live; its path |
| 56–61 | The daily means; the cosine and its three parameters; two days pushed through; the descent from the starting values; the fitted cycle |
| 62–63, 65–68, 70–75 | Residuals of the line; what χ² should be; when it is not a test; residuals of the cycle; neighbouring days alike; too few and too many parameters; how many; reading residuals; a sensor shift |
| 76–81 | The same line by every method; reporting a fit; a checklist; the answer; the recap |

| Skip | Slides |
|--|--|
| Why x counts from 2016; the slope as r times the spreads | 35–36 |
| The intercept and its ± | 41 |
| The ± with more years | 45 |
| Each step multiplies the gap by 1 − 8η | 51 |
| The pulls of the line | 64 |
| The same trend from 3648 days | 69 |

- **Do not cut** slides 3 and 80: the opening question and its answer,
  −0.56 ± 0.77 °C per decade, with the same fan of lines.
- **Do not cut** slides 12–14, the derivative: the only place the course
  teaches it, and the base of every later slope, χ² minimum and descent
  step. Lecture 10 uses the same update rule for the perceptron.
- **Do not cut** slides 78–79, reporting a fit and the checklist: the two
  slides a student needs for the project.
- **Slides 9, 13, 53 and 59** push numbers through one click at a time:
  the misses, their squares and S; the nudge and the rule; one descent step
  for the line; the summer day of the cycle. **Slides 20, 22, 32, 40 and
  42** step a formula one click at a time, the symbols first, then the
  numbers in their place (in the accent colour), then the result: the
  Gaussian of 2016; the logarithm of a product; Δ, the slope and the
  intercept (three clicks each); σ_a; the ± of the line for 2026. Slide 52
  shows two runs on its click.
- **New notions get an explainer where they first appear**: error bars
  (slide 6, before the three parts of a fit), the Gaussian bell and a
  density (18), the logarithm (22); one line on the slide for χ² read
  aloud (23), r (36), ∝ (39), N^−3/2 (45), contour lines and a logarithmic
  axis (55), the root mean square (59), ⟨χ²⟩ (65), sd (67), √n for a count
  (90).
- **Slide 26 is an interactive figure** that works offline: drag the line or
  its ends and χ² follows, term by term; tap a year to push its numbers
  through; take a line from the room to beat the flat line's 9.08, then press
  "best fit" (least squares 8.56; the rounded line itself reads 8.57). Use it
  on the projected window, not in the presenter view.
- **Slides 15, 34, 52 and 54** run plain Python in the browser: the slope of
  S by formula and by nudge; the five sums; the step size; gradient descent
  on ten years. The first run downloads the Python runtime, so run one before
  the lecture. On slide 52 the room chooses the step sizes 0.3, 0.25 and
  0.01.
- **Every number** on the slides is printed by
  `python figures/src/fitting.py` from `weather.csv`; the ten yearly means
  are shown with three decimals so that the sums and the slope come out the
  same by hand.
- **Slides 82–92** (For the Curious) are for time left at the end or for
  students afterwards; the pendulum and the LHCb file appear only there.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/09-parameter-estimation-and-fitting/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 93–101: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. Which value of μ makes the sum of squared misses Σ(y − μ)² smallest for
   the three values 2, 4 and 9?
   *5, the mean: the derivative −2Σ(y − μ) is zero where Σy = 3μ. The middle
   value, 4, makes the sum of the sizes |y − μ| smallest instead.*
2. Three points have residuals 0.2, −0.3 and 0.1 from a model, each with
   σ = 0.1. What is χ²?
   *14: the pulls are 2, −3 and 1, their squares 4, 9 and 1.*
3. Three points: x = 0, 1, 2 and y = 1, 3, 4. What is the slope of the
   least-squares line?
   *1.5: N = 3, Σx = 3, Σy = 8, Σx² = 5, Σxy = 11, Δ = 6, and the slope
   (3 × 11 − 3 × 8) / 6 = 1.5; the intercept is 7 / 6 = 1.17.*
4. A fit with one parameter has χ² = 12.0 at its minimum, θ = 5.00. At
   θ = 5.20 the χ² is 13.0. What is the uncertainty of θ?
   *0.20: one σ raises χ² by 1.*
5. Gradient descent on S(θ) = (θ − 3)² starts at θ = 0 with the step size
   η = 0.25. Where is θ after one step?
   *1.5: the derivative at 0 is −6, and 0 − 0.25 × (−6) = 1.5.*
6. A cosine with three parameters is fitted to 365 daily means. How many
   degrees of freedom does the fit have?
   *362 = 365 − 3.*
7. A polynomial with ten parameters is fitted to ten yearly means. What
   happens?
   *It passes through every point: χ² = 0, nothing is left to test, and its
   forecast is unreliable; for the weather log it says 307 °C for 2026.*
8. A fit takes 3648 days as independent and gives A = 11.18 ± 0.07 °C,
   but neighbouring days correlate, r = 0.875. The honest ± is…
   *Larger: ten one-year fits scatter by 0.79 °C, which gives ± 0.25 °C,
   3.6 times the ± of the fit.*

## Paired seminar

[Seminar 9 · NumPy](../seminars/seminar_09.md) asks how fast Vilnius is getting warmer, at the real station. The lecturer runs four NumPy scripts on open data: the squared misses of the 365 days of 2023 for 1600 guesses, smallest at the mean; a line through 67 yearly means of CO₂ at Mauna Loa by the five sums and by `np.polyfit` (1.6720 ± 0.0008 ppm a year with NOAA's σ = 0.12 ppm); its residuals, a U with χ²/ndf = 1484, against a parabola's 40; polynomials of degree 0 to 9 through ten years of Vilnius, degree 9 saying 44.7 °C for 2023. In pairs, LLMs allowed, the room fits the yearly means of NOAA's GHCN-Daily station file, 1881–2024: one line since 1881 gives 0.05 ± 0.02 °C per decade, a model its residuals reject (χ² = 187 for 132, σ = 0.82 °C from neighbouring years); since 1981, 0.48 ± 0.09 (χ² = 36 for 42). NumPy is already in `analysis`, a dependency of pandas and Matplotlib. Optional: SciPy's `curve_fit` for the yearly cycle (A = 11.03 ± 0.09 °C from all days, ± 0.35 from ten separate years).

## Slides that left the deck

On 9 November 2026 the deck was rebuilt for week 9 on the weather log
(design: `docs/superpowers/specs/2026-11-09-weeks-8-12-ideas-and-tools-design.md`).
The Data Fitting lecture before it, built on the pendulum table and the LHCb
file, can be read with
`git show 328aba2:lectures/content/slides/10_Data_Fitting.md`; six of its
slides are parked in `lectures/content/parked/09_Parameter_Estimation_and_Fitting.md`.

| Earlier slide | What happened | Reason |
|--|--|--|
| Which Number Would You Report? (the four window means of the D⁰ mass) | Replaced by slide 3, Is It Getting Warmer? | The opening asks about the room's own data; Lecture 8 no longer computes the window means |
| The goal quote; Learning Objectives; What Lecture 09 Established | Removed | Preambles; the deck opens on its question |
| The Pendulum Table; From a Curve to a Straight Line; The Uncertainties We Assume | Replaced by slides 5–6 and 16 | The models of the weather log; σ = 0.70 °C from the scatter of the yearly means |
| The Three Parts of a Fit | Kept, slide 6 | On the yearly means |
| The Gaussian Scatter of One Point; The Likelihood of All Points; Maximum Likelihood Is Minimum χ²; χ² of Lines A, B and C | Rebuilt as slides 17–22 | On the ten yearly means, each value pushed through |
| Two Derivatives Set to Zero; The Normal Equations; Slope and Intercept in Closed Form; The Pendulum: Five Sums; Slope and Intercept | Rebuilt as slides 25–29 | Equal σ, so five plain sums; the ten years in a table |
| The Fitted Line; The Same in NumPy | Slides 30–31 | The best line of the ten years; plain Python in place of NumPy |
| The Rule Δχ² = 1; χ² Around Its Minimum | Slides 35–36 | The slope of the ten years |
| The Slope Is a Sum over the Data; Two Uncertainties and a Covariance; The Covariance Matrix; Why Slope and Intercept Are Correlated | Moved to For the Curious, slides 80–82 | Derivations and the covariance leave the main path |
| The Uncertainty of g; the pendulum's fit | For the Curious, slide 86 | The pendulum appears only there |
| The Same in Matrix Form; `np.linalg.lstsq` and `np.polyfit` | Slide 82; the calls moved to Seminar 9 | No library on a lecture slide |
| No Closed Form; The Gradient; The Update Rule; Gradient Descent by Hand; A Learning Rate That Is Too Large; Descent Paths | Rebuilt as slides 44–52 | The four hours by hand, then the line of the ten years |
| Gradient Descent in NumPy | Slide 51, plain Python | No library on a lecture slide |
| Why the Descent Is Slow, and the Remedy | For the Curious, slide 84 | Newton and Levenberg–Marquardt |
| `curve_fit`: the Call; `absolute_sigma`; Closed Formulas, `polyfit` and `curve_fit` Agree | Removed; `curve_fit` is in Seminar 9's optional part | Library calls belong to the seminar |
| The D⁰ Peak (data, counts, model, the fit in code, the fit and its pulls, what the result says) | For the Curious, slides 87–89; the starting values parked | The CERN example is kept for the curious |
| The Fit in Code; The Fit and Its Pulls; What the Result Says | Redone on the yearly cycle, slides 54–58 | The design's curve: a cosine with three parameters |
| What χ² Should Be; The χ² Distribution and the p-value; Reading χ²/ndf; Residuals and Pulls | Slides 60–63; the distribution in For the Curious, slide 85 | On the line of the ten years |
| A Model with Too Few Terms; Too Few Terms: the Pulls | Slide 67 on the cycle; the D⁰ version in For the Curious, slide 89 | The weather log first |
| A Model with Too Many Terms; Three Pendulum Models and Their Pulls | Slides 68–69 | Polynomials through the ten yearly means |
| Starting Values; Errors That Are Not Gaussian (small counts, an outlier); What χ² Cannot See; The Number to Report | Parked | The outlier and the systematic shift are on slides 71–72 with weather numbers |
| Reporting a Fit | Kept, slide 75 | With two sentences on the weather log |

## Further reading

- **J. R. Taylor**, *An Introduction to Error Analysis*: chapter 8, the
  straight line by least squares, with the uncertainties of slope and
  intercept.
- **R. J. Barlow**, *Statistics: A Guide to the Use of Statistical Methods
  in the Physical Sciences*: likelihood, χ² and fitting.
- **G. Cowan**, *Statistical Data Analysis*: the method of least squares and
  the χ² distribution, for physicists.

## Take-aways

- A model is a formula with parameters; fitting sets them from the data by
  making one measure of the miss as small as it can be.
- The mean is the value with the smallest sum of squared misses.
- A derivative is the slope of a curve for a small nudge; at the lowest
  point it is zero. Check a derivative worked out on paper with a nudge.
- With Gaussian scatter, the most probable parameters have the smallest
  χ² = Σ(y − model)² / σ²: maximum likelihood is least squares.
- A straight line needs five sums of the data: N, Σx, Σy, Σx², Σxy.
- One σ of a parameter raises χ² by 1. For the ten yearly means the slope
  is −0.56 ± 0.77 °C per decade: ten years cannot tell a trend from zero.
- Gradient descent repeats θ ← θ − η dS/dθ; a step size above 2 divided by
  the curvature flies off.
- Residuals show what χ² hides: a pattern means a missing term, runs mean
  points that are not independent and a ± that is too small, one far point
  means a value to check at its source.
- χ² near the degrees of freedom tests a model only if σ comes from outside
  the fitted points.
- More parameters always lower χ²; a parameter earns its place by lowering it
  clearly more than 1. A curve through every point forecasts nonsense.
- The ± of a fit is statistical; an error shared by many points is
  systematic and is found in the records, not in χ².
- A fit is reported with its model, its data and σ, each parameter with its
  ± and unit, χ² and the degrees of freedom, a figure with the residuals,
  and what the ± leaves out.
