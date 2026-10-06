# 9: Probability & Statistics

Lecture 8 drew the data: the pendulum table as points and the mass column as
a histogram, with a bar of ± √N on every bin taken as given. Lecture 9 opens
on that figure and four questions: which one number stands for the 91 583
masses, how far a single value lies from it, how well that number is known,
and why the bar on a count is √N. It derives how a quantity that comes out
differently every time is described, ends with the likelihood, and closes on
the four answers.

## What the lecture covers

1. **Probability and its rules** — probability as a long-run frequency,
   shown with a million simulated rolls from a seeded generator; outcomes
   and events; the three axioms; the complement and the addition rule
   derived from them; conditional probability; independence, and a test of
   it on the file: a high `PT` raises the share of rows in the peak window
   from 0.28 to 0.40; Bayes' theorem with a test worked by counting and by
   formula.
2. **Random variables** — a distribution (the sum of two dice); the
   expected value as the average of many repetitions; variance and standard
   deviation; the mean and the variance of a sum, with the covariance;
   densities for continuous variables, and the uniform density with its
   variance 1/12.
3. **Three distributions** — the binomial from independent trials and
   counting; its mean np and variance np(1 − p) from the rules for sums; the
   Poisson distribution as its limit, derived and then computed for
   n = 1000, p = 0.003 against λ = 3; a count as N ± √N, the bar of
   Lecture 8, checked on 14 bins of the mass histogram; sums of uniform
   numbers that turn into a bell, the central limit theorem; the bell named
   as the Gaussian, with its 68.3 %, 95.4 %, 99.7 %.
4. **Samples and the standard error** — sample mean x̄ and standard
   deviation s; covariance and the correlation coefficient; σ/√N derived
   from the variance of a sum and checked by simulation and on 915 groups
   of 100 mass values; standard deviation against standard error; why
   N − 1; what the standard error does not cover: the mean lies 8.7
   standard errors below the D⁰ mass.
5. **Error propagation** — the first-order Taylor expansion for one and for
   several measurements; the rules for sums and for products of powers;
   g = 4π²ℓ/T² from one pendulum row with stated uncertainties; the same by
   simulation; how a result is written.
6. **Testing a hypothesis** — the distance from a known value in units of
   σ, the p-value, and what a p-value is not.
7. **Likelihood** — the binomial read as a function of p; maximum
   likelihood; the likelihood L(θ) of independent measurements; the Gaussian
   mean is the sample mean; the width of the likelihood is the standard
   error; unequal uncertainties give the weighted mean with weights 1/σᵢ²
   and the uncertainty (Σ 1/σᵢ²)^(−1/2); g from nine rows. The closing
   slide answers the four questions of the opening one.

## Notation

| Symbol | Meaning |
|--|--|
| xᵢ, yᵢ, σᵢ, i = 1…N | measured values and their uncertainties |
| μ, σ | mean and standard deviation of a distribution |
| x̄, s | mean and standard deviation of a sample |
| θ, L(θ) | parameters and the likelihood |
| μ̂, p̂ | an estimate: the value at which L is largest |
| ℓ, t₁₀, T | pendulum length, time of 10 swings, period. The length is ℓ because L is the likelihood |
| r, ρ | correlation coefficient of a sample and of two random variables |

## The numbers of the lecture

Every number on a slide was computed with NumPy from the two files of the
project folder, or from a seeded simulation.

| Quantity | Value |
|--|--|
| Rows in the peak window 1855 < M < 1875 | 31 132, P(W) = 0.340 |
| Share in the window for PT above / below its median | 0.403 / 0.277 |
| Top bar of the Lecture 8 histogram (1 MeV/c² bins) | 1916 ± 44 |
| Mass column, 91 583 rows: mean ± standard error | 1864.10 ± 0.08 MeV/c² |
| Mass column: standard deviation | 25.57 MeV/c² |
| 14 flat bins of 2 MeV/c²: mean count, scatter, √N | 1461, 34, 38 |
| 915 means of 100 mass values: scatter, s/√100 | 2.60, 2.56 MeV/c² |
| g from the row 100 cm, 20.01 s | 9.86 ± 0.10 m/s² |
| g from nine rows, weighted mean | 9.80 ± 0.04 m/s² |

The pendulum file holds no uncertainties. The lecture states them: 0.1 cm on
the length and 0.1 s on the time of 10 swings.

## The lecture in 90 minutes

The lecture is slides 1–65 and estimates about 141 min. Slides 66–73 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table: the estimate is then about 97 min. To jump, type
the slide number and press Enter.

The opening slide (3) asks four questions about last week's histogram. The
plan answers them by about minute 60: the bar of ± √N on slide 30 (about
0:50), the mean, s and the standard error on slides 36 and 39 (about 1:00),
and what the standard error does not cover on slide 44.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–8, 10–13, 15 | Four questions; probability and its rules; independence on the file; Bayes by counting |
| 0:26 | 16–22 | Random variables: mean, variance, sums, density |
| 0:39 | 24–26, 29–31, 33 | Binomial, Poisson, √N on the mass column, adding makes a bell, the Gaussian |
| 0:56 | 35–36, 39, 41–42, 44 | Mean, s and standard error of the mass column; what it does not cover |
| 1:08 | 45–50 | Error propagation, g from one pendulum row |
| 1:20 | 56–57, 59–60, 62–64 | Likelihood, the mean, the weighted mean, g from nine rows |
| 1:35 | 65 | The four questions, answered |
| 1:37 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Three Axioms | 9 | 2 min |
| Bayes' Theorem (slide 15 is worked by counting) | 14 | 3 min |
| Independent Trials: Counting | 23 | 2 min |
| The Limit in Numbers, The Limit, Computed | 27–28 | 5 min |
| The Sums in NumPy | 32 | 4 min |
| Where the Gaussian Applies | 34 | 2 min |
| Covariance and Correlation, Correlation in Numbers | 37–38 | 5 min |
| The Standard Error, Checked | 40 | 2 min |
| Why N − 1 | 43 | 3 min |
| The Same by Simulation, Writing a Result | 51–52 | 6 min |
| Testing a Hypothesis | 53–55 | 5 min |
| Maximum Likelihood | 58 | 2 min |
| The Width of the Likelihood | 61 | 2 min |

- **Do not cut** slide 65, the closing slide: it answers the four questions
  of slide 3. Do not cut slides 3 (the questions), 20 (sums of random
  variables), 30 (√N, checked), 39 (the standard error), 44 (what the
  standard error does not cover), 46–50 (error propagation and g) or 59–63
  (the likelihood of many measurements, the mean, the weighted mean and its
  uncertainty). Slide 20 carries the two rules that every later derivation
  uses.
- **Slides 40, 41, 51 and 64 are repeated in the seminar** as typed
  scripts, with the same numbers. Slides 40 and 51 are skipped above; if
  the clock is behind, slide 41 goes next.
- **Slides 7, 28, 32 and 51 run live.** Each has a code block with a play
  button. The first run loads NumPy into the browser and takes some seconds:
  run slide 7 once before the session. Then change one number: the seed on
  slide 7, `n, p = 10, 0.3` on slide 28, a `50` in the list on slide 32,
  `2.0` in place of `0.1` on slide 51.
- **Ask before showing.** Slide 6: the fraction of sixes after ten rolls and
  after a million (slide 7 answers). Slide 13: does knowing `PT` change the
  chance that a row lies in the peak? Slide 31: what do sums of two flat
  numbers look like? Slide 62: the combination of 9.70 ± 0.22 and
  9.86 ± 0.10 (most say 9.78; it is 9.83).
- **Slides 9–12, 19, 23, 26, 39, 58, 60 and 62 are derivations.** Do them on
  the board, one line at a time, and use the slide as the fair copy.
- **Slide 49** states the uncertainties of the pendulum example, 0.1 cm and
  0.1 s. Say that they are chosen, not read from the file.
- If the clock is still behind, slides 21 (Continuous Variables: Density)
  and 41 (The Means of 100 Mass Values) can also go: 5 min.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 66–73: seven quiz slides for students to try afterwards. The same
questions, with their answers:

1. 2 % of a population has a condition. A test is positive for 90 % of those
   who have it and for 5 % of those who do not. A person tests positive. How
   probable is the condition?
   *27 %. Of 10 000 people, 180 of the 200 with the condition and 490 of the
   9800 others test positive: 180 / 670.*
2. A detector registers each particle with probability 0.8. Five particles
   pass. How probable are exactly four registered?
   *0.41: five sequences, each with 0.8⁴ × 0.2.*
3. A bin of a histogram holds 400 rows. What is the uncertainty of the
   count?
   *√400 = 20, which is 5 %.*
4. 144 measurements have a sample standard deviation of 12 units. What is
   the standard error of the mean, and how many measurements halve it?
   *12 / √144 = 1 unit. Four times the data: 576.*
5. A rectangle has the sides 2.00 ± 0.02 m and 5.00 ± 0.10 m. What is its
   area?
   *10.00 ± 0.22 m². The relative uncertainties 1 % and 2 % add in
   quadrature to 2.2 %.*
6. A measurement gives 5.3 ± 0.2 and the expected value is 4.7. How far
   apart are they, and what is the p-value?
   *3σ, and p = 0.0027 for both sides.*
7. Two measurements give 10.0 ± 0.1 and 10.6 ± 0.3. What is their weighted
   mean?
   *10.06 ± 0.09, with the weights 100 and 11.1.*

## Paired seminar

[Seminar 9 — A Result with Its Uncertainty](../seminars/seminar_09.md) is a
follow-along session in four parts: the mean of the mass column with its
standard error; the histogram of the column against a Gaussian, and the
means of 100 values against a Gaussian; g and its propagated uncertainty
for every row of the pendulum table, their weighted mean, and a check by
simulation; the results written into the report.

## Further reading

- Taylor, *An Introduction to Error Analysis*: uncertainties and their
  propagation, with laboratory examples.
- Barlow, *Statistics: A Guide to the Use of Statistical Methods in the
  Physical Sciences*.
- Cowan, *Statistical Data Analysis*: likelihood and estimation, written
  for particle physics.
- Blitzstein and Hwang, *Introduction to Probability*: free online, with
  the Harvard course Stat 110.

## Take-aways

- A probability is the fraction at which a long run of repetitions settles.
  The complement, the addition rule, conditional probability and Bayes'
  theorem follow from three axioms.
- For independent variables the variances add, and a factor comes out
  squared. The standard error and error propagation both follow from this.
- Independent trials give the binomial distribution. Many trials with a
  small probability give the Poisson distribution, whose variance equals
  its mean: a count is N ± √N.
- A sum of many independent terms tends to a Gaussian. Within ±σ lie
  68.3 %, within ±2σ 95.4 %.
- The standard deviation s describes the spread of the data. The standard
  error s/√N is the uncertainty of their mean, and it falls with more data.
- The standard error does not cover a wrong choice of rows or of method.
- To first order, each input adds its derivative times its uncertainty, in
  quadrature. For products of powers the relative uncertainties add in
  quadrature, each times its power.
- The likelihood is the probability of the observed data as a function of
  the parameters. Its maximum is the estimate, and the distance over which
  ln L falls by 1/2 is the uncertainty.
- For Gaussian measurements the maximum-likelihood estimate of the mean is
  the sample mean. With unequal uncertainties it is the weighted mean with
  weights 1/σᵢ², and its uncertainty is (Σ 1/σᵢ²)^(−1/2).
- A result is a value, an uncertainty, a unit and a word on what the
  uncertainty is.
