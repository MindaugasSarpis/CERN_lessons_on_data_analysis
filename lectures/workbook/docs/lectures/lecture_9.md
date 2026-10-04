# 9: Probability & Statistics

Lecture 8 drew the data: the pendulum table as points and the mass column as
a histogram, with error bars taken as given. Lecture 9 says what an error bar
is. It derives how a quantity that comes out differently every time is
described, and it ends with the likelihood, the starting point of fitting.

## What the lecture covers

1. **Probability and its rules** — probability as a long-run frequency,
   shown with a million simulated rolls; random numbers in NumPy with a
   seed; outcomes and events; the three axioms; the complement and the
   addition rule derived from them; conditional probability; independence;
   Bayes' theorem with a test worked by counting and by formula.
2. **Random variables** — a distribution (the sum of two dice); the
   expected value as the average of many repetitions; variance and standard
   deviation; the mean and the variance of a sum, with the covariance;
   densities for continuous variables, and the uniform density with its
   variance 1/12.
3. **Three distributions** — the binomial from independent trials and
   counting; its mean np and variance np(1 − p) from the rules for sums; the
   Poisson distribution as its limit, derived and then computed for
   n = 1000, p = 0.003 against λ = 3; a count as N ± √N, checked on 14 bins
   of the mass histogram; the Gaussian and its 68.3 %, 95.4 %, 99.7 %; the
   central limit theorem by simulation, with sums of uniform numbers.
4. **Samples and the standard error** — sample mean x̄ and standard
   deviation s; σ/√N derived from the variance of a sum and checked by
   simulation and on 915 groups of 100 mass values; standard deviation
   against standard error; why N − 1; what the standard error does not
   cover; covariance and the correlation coefficient.
5. **Error propagation** — the first-order Taylor expansion for one and for
   several measurements; the rules for sums and for products of powers;
   g = 4π²ℓ/T² from one pendulum row with stated uncertainties; the same by
   simulation; how a result is written.
6. **Likelihood** — the binomial read as a function of p; maximum
   likelihood; the likelihood L(θ) of independent measurements; the Gaussian
   mean is the sample mean; the width of the likelihood is the standard
   error; unequal uncertainties give the weighted mean with weights 1/σᵢ²
   and the uncertainty (Σ 1/σᵢ²)^(−1/2); g from nine rows.
7. **Testing a hypothesis** — the distance from a known value in units of
   σ, the p-value, and what a p-value is not.

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
| Mass column, 91 583 rows: mean ± standard error | 1864.10 ± 0.08 MeV/c² |
| Mass column: standard deviation | 25.57 MeV/c² |
| 14 flat bins of 2 MeV/c²: mean count, scatter, √N | 1461, 34, 38 |
| 915 means of 100 mass values: scatter, s/√100 | 2.60, 2.56 MeV/c² |
| g from the row 100 cm, 20.01 s | 9.86 ± 0.10 m/s² |
| g from nine rows, weighted mean | 9.80 ± 0.04 m/s² |

The pendulum file holds no uncertainties. The lecture states them: 0.1 cm on
the length and 0.1 s on the time of 10 swings.

## The lecture in 90 minutes

The lecture is slides 1–65 and estimates about 140 min. Slides 66–73 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table: the estimate is then about 95 min. To jump, type
the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7, 9–13 | Probability and its rules |
| 0:22 | 16–21 | Random variables: mean, variance, sums, density |
| 0:35 | 22–27, 29, 31–32 | Binomial, Poisson, Gaussian, sums tend to a Gaussian |
| 0:53 | 35–37, 40, 43 | Sample, standard error, covariance and correlation |
| 1:03 | 45–50 | Error propagation, g from one pendulum row |
| 1:15 | 53–60 | Likelihood, the mean, the weighted mean |
| 1:32 | 65 | Recap |
| 1:35 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| The Frequency of a Six, Simulated | 8 | 4 min |
| Bayes' Theorem, Bayes' Theorem: a Test | 14–15 | 5 min |
| The Limit, Computed | 28 | 3 min |
| √N, Checked on the Mass Column | 30 | 2 min |
| The Sums in NumPy, Where the Gaussian Applies | 33–34 | 6 min |
| The Standard Error, Checked; The Means of 100 Mass Values | 38–39 | 4 min |
| Why N − 1, What the Standard Error Does Not Cover | 41–42 | 5 min |
| Correlation in Numbers | 44 | 3 min |
| The Same by Simulation, Writing a Result | 51–52 | 6 min |
| g from Nine Measurements | 61 | 2 min |
| Testing a Hypothesis | 62–64 | 5 min |

- **Do not cut** slides 20 (sums of random variables), 37 (the standard
  error), 46–50 (error propagation and g) or 56–60 (the likelihood of many
  measurements, the mean, the weighted mean and its uncertainty). Slide 20
  carries the two rules that every later derivation uses. Slides 56–60 are
  what the lecture on fitting starts from.
- **Slides 38, 39, 51 and 61 are repeated in the seminar** as typed scripts,
  with the same numbers. They are the first to skip.
- **Slides 8, 28, 33 and 51 run live.** Each has a code block with a play
  button. The first run loads NumPy into the browser and takes some seconds:
  run slide 8 once before the session. Then change one number: the seed on
  slide 8, `n, p = 10, 0.3` on slide 28, a `50` in the list on slide 33,
  `2.0` in place of `0.1` on slide 51.
- **Slides 10–13, 19, 23, 26, 37, 55, 57 and 59 are derivations.** Do them on
  the board, one line at a time, and use the slide as the fair copy.
- **Slide 49** states the uncertainties of the pendulum example, 0.1 cm and
  0.1 s. Say that they are chosen, not read from the file.
- If the clock is still behind, slides 10 (Three Axioms) and 58 (The Width
  of the Likelihood) can also go: 5 min.

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
6. Two measurements give 10.0 ± 0.1 and 10.6 ± 0.3. What is their weighted
   mean?
   *10.06 ± 0.09, with the weights 100 and 11.1.*
7. A measurement gives 5.3 ± 0.2 and the expected value is 4.7. How far
   apart are they, and what is the p-value?
   *3σ, and p = 0.0027 for both sides.*

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
