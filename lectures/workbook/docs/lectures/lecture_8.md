# 8: Data Quality and Uncertainty

Lecture 7 drew the hours of the weather station and found the mean of ten
years, 7.16 °C, in the dip between a cold and a warm peak. Lecture 8 asks how
sure that number is. It first checks that every hour behind it is valid (120
hours of `-999` turn 7.16 into 5.78), then describes the hours by a few
numbers, counts probabilities in them, sets them against the Gaussian, and
measures how two columns move together. Each idea comes as an expression with
the numbers of the log pushed through it, often the four measured hours of
the evening of 21 July 2019. It ends on the one derivation of the lecture,
the standard error s/√N: 0.030 °C if the hours were independent, and, since
an hour nearly repeats the hour before, 0.22 °C from the ten yearly means.
The answer is written as the README writes it: 7.16 ± 0.22 °C.

## What the lecture covers

1. **The question**: the mean of 87 552 hours, the ten yearly means, and
   how far 7.16 °C can be from the station's long-run mean: 0.03, 0.2, 1 or
   9 °C?
2. **Is every hour valid?** The six hours of 21 July 2019, two of them
   `-999`: the mean −316.15 °C with the marks, 25.275 °C without; the whole
   log, 5.78 and 7.16 °C; the marks in a figure; how files mark a missing
   value; four ways to treat the 120 hours (5.783, 7.150, 7.160, 7.174 °C);
   a published mean changed by left-out rows (Reinhart and Rogoff,
   corrected by Herndon, Ash and Pollin); five checks, each with a count;
   the unit of `temp_c`, checked with numbers.
3. **Describing a distribution**: the hours in bins of 1 °C; the mean of
   the cold and the warm half of the year; the sum sign Σ; the mean, the
   deviations, the variance and the standard deviation, each with the four
   hours pushed through (25.275 °C, s = 1.58 °C) and run in Python; the log,
   s = 8.85 °C; the median against the mean, and in Python; percentiles.
4. **Probability by counting**: P(frost) = 22 352 / 87 552 = 0.255; the
   share settles as hours are counted at random; P(frost) in each month and
   at each hour of a March day; conditional probability; frost given the
   hour before, 0.956, and given no frost before, 0.015; neighbouring hours
   are not independent (0.244 counted against 0.065); the same count on one
   day, live.
5. **The Gaussian**: the curve with μ = 7.16 and σ = 8.85 °C pushed through
   it (3946 hours per 1 °C at the top), live; the 68 / 95 / 99.7 % areas; the
   hours against the curve: 62.6 % within ± s, not 68.3 %, and no long
   tails; means of 100 random hours are Gaussian.
6. **Correlation**: temperature and humidity of every hour; the covariance
   and r, pushed through with the four hours (r = −0.93) and live; r of
   pairs of columns (−0.70 for temperature and humidity, 0.996 for an hour
   and the next); random pairs against neighbouring hours; r measures only a
   straight line (day of the year, r = 0.21).
7. **The standard error**: the variance of a sum, checked with two random
   hours (12.52 °C) and two neighbouring hours (17.68 °C); a factor comes out
   squared; the variance of a mean, σ²/N, derived; s/√N checked on random
   hours, and live for N = 1 to 1000; what ± one standard error means, as 50
   intervals; how it shrinks with N, live; the standard error of 7.16 if the
   hours were independent, 0.030 °C.
8. **When hours are not independent**: means of 1000 hours at random (0.28)
   and in a row (7.75 °C); r against the time between two hours; the ten
   yearly means, s = 0.70 °C, and their standard error, 0.22 °C; one year's
   own ± (0.10) against the scatter of the years (0.70); writing a result
   with its ±; which ± belongs to 7.16.
9. **Wrap-up**: the answer in five steps, the answer in the README, a
   checklist for a mean, the recap.
10. **For the curious**, after the recap and outside the lecture time: six
    tenths of the variance of the hours is the seasons; why the variance
    divides by N − 1; the three axioms of probability; Bayes' rule
    (P(January | frost) = 0.2835); the binomial (frost hours among ten, at
    random and in a row); the Poisson (hours of 30 °C or more); error
    propagation for factors and differences; the ± from means of blocks, an
    hour to a year.

## The lecture, part by part

The lecture is slides 1–69 and estimates about 116 min, so in the two-hour
slot **plan to skip the slides of the second table** (about 12 min).
Slides 70–78 are the optional section For the Curious and slides 79–87 the
self-check quizzes; neither takes lecture time. To jump, type the slide
number and press Enter.

| Slides | Part |
|--|--|
| 1–3 | The question: how far can 7.16 °C be from the station's long-run mean? A show of hands for 0.03, 0.2, 1 or 9 °C |
| 4–7, 9, 11 | Is every hour valid: the six hours, the whole log with and without the marks, the marks in a figure, four ways to treat 120 missing hours, five checks with counts |
| 13–22, 24 | Describing a distribution: the histogram, the two halves of the year, Σ, the mean, the deviations, variance and standard deviation, the four hours in Python, s of the log, the median, percentiles |
| 25–29, 31–33 | Probability by counting: P(frost), the share settling, frost in each month, conditional probability, frost given the hour before, independence, one day live |
| 34–35, 37–40 | The Gaussian: the curve, its areas, the hours against it, the check in numbers, means of random hours |
| 41–48 | Correlation: the scatter of temperature and humidity, covariance, r, r live, pairs of columns, random and neighbouring pairs, r and a curve |
| 49–57 | The standard error: the variance of a sum, a factor squared, the variance of a mean, the check, the mean of N random hours live, what ± means, how it shrinks with N, 0.030 |
| 58–63, 65 | Not independent: hours in a row, r against the time between hours, the ten yearly means, 0.22, one year's own ±, which ± belongs to 7.16 |
| 66–69 | The answer in five steps, the README, a checklist, the recap |

| Skip | Slides |
|--|--|
| How files mark a missing value | 8 |
| A published mean changed by left-out rows | 10 |
| The unit of `temp_c`, checked with numbers | 12 |
| The median in Python | 23 |
| Frost at 03:00 and at 14:00 in March | 30 |
| The Gaussian in Python | 36 |
| Writing a result with its ± | 64 |

- **Do not cut** slide 3 (the question, with the counts of the show of
  hands on the board) or slide 65, which answers it with the four numbers
  of the opening.
- **Do not cut** slides 50–57 and 59–62: the one derivation of the lecture,
  s/√N, and the reason it fails for the hours. The seminar computes the
  same 0.030 and 0.22 with pandas.
- **Slides 5, 6, 10, 15, 19, 31, 32, 39, 43 and 65** show the question or
  the numbers first and the result on a click; ask the room before
  clicking. **Slide 52** builds the variance of a mean in four clicks, one
  line of the derivation each, and **slide 57** the standard error of 7.16
  in three: √87 552, then 0.030, then the condition.
- **Slide 54 is an interactive figure** that works offline: pick N = 1, 4,
  16, 100 or 1000 hours per mean and read the spread of the 1000 means
  beside s/√N; at 100 and 1000 press "zoom in". Use it on the projected
  window, not in the presenter view.
- **Slides 20, 23, 33, 36, 45 and 56** run plain Python in the browser,
  each pushing a list of the log through the slide's expression. The first
  run downloads the Python runtime and needs internet in the room, so press
  one ▶ before the lecture. The notes of each say what to change and run
  again.
- **Every figure fills its slide** and is drawn from `weather.csv` by
  `figures/src/probability.py`, which also prints every number the slides
  state: `python figures/src/probability.py`.
- **Slide 55** shows 50 intervals of ± one standard error; 28 of them hold
  the mean, against 67 % of 2000. The note says why 50 is not enough to
  show 68 %.
- **Slides 70–78** (For the Curious) are for time left at the end or for
  students afterwards.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 79–87: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A file holds four temperatures, 10.0, 12.0, −999 and 14.0 °C, where
   −999 marks a failed reading. What is the mean temperature?
   *12.0 °C, the mean of the three readings. Read as a number, the mark
   gives (10.0 + 12.0 − 999 + 14.0) / 4 = −240.75 °C.*
2. Three hours measure 2, 4 and 6 °C. What is their standard deviation s,
   dividing by N − 1?
   *2 °C: the deviations from the mean 4 are −2, 0 and +2, their squares
   add up to 8, and 8 / 2 = 4 °C², whose root is 2. Dividing by N = 3 would
   give 1.63 °C.*
3. Of 1000 evenings, 400 are clear, and 300 of the clear evenings are
   followed by frost. What is P(frost | clear evening)?
   *0.75: only the 400 clear evenings are counted, 300 / 400. 0.30 is
   P(clear and frost).*
4. A Gaussian holds 68.3 % of its values within the mean ± s. The hours of
   the log hold 62.6 %. What does this say?
   *The hours are not Gaussian: the cold and the warm half of the year form
   two peaks with a dip at the mean, so fewer hours lie near it.*
5. 400 independent values have a standard deviation s = 6. What is the
   standard error of their mean?
   *6 / √400 = 0.3. Four times as many values would halve it.*
6. The 87 552 hours give s/√N = 0.030 °C, and the ten yearly means give
   0.22 °C. Why is 0.030 too small?
   *The hours are not independent: an hour nearly repeats the hour before
   (r = 0.996, P(frost | frost the hour before) = 0.956). The yearly means
   are close to independent.*
7. The correlation of temperature and humidity over the hours of the log is
   r = −0.70. Which statement holds?
   *Warm hours tend to be drier, along a falling line with scatter; r alone
   does not say why. Both follow the time of day and the season.*
8. Two independent measurements have standard errors 0.3 and 0.4 °C. What
   is the standard error of their difference?
   *√(0.3² + 0.4²) = 0.5 °C: for independent values the variances add, for
   a difference as for a sum.*

## Paired seminar

[Seminar 8 · pandas](../seminars/seminar_08.md) answers the same question
with the library pandas. Every student makes the conda environment
`analysis` from today's folder, adds pandas to it, reads `weather.csv` into
a table, finds 5.78 with the `-999` marks and 7.16 without them, the
standard deviation 8.85 and the standard error 0.030, the mean of each
month and of each year, and writes 7.16 ± 0.22 °C into the README; then
reads a file of their own project the same way.

## Before Lecture 8

Until 9 November 2026 week 8 was *Python for Data & NumPy* and week 9
*Probability & Statistics*, built on the pendulum table and the LHCb file
`D0_KPi.csv`. Both moved: NumPy and pandas are now taught in the seminars,
and this lecture was rebuilt on the weather log from the statistics deck.
It keeps that deck's derivation of the standard error and its Gaussian; the
dice, the binomial and Poisson derivations, the likelihood, error
propagation and the LHCb and pendulum examples stay in the parked deck,
`lectures/content/parked/decks/09_Probability_and_Statistics.md`.

## Further reading

- **D. Freedman, R. Pisani, R. Purves**, *Statistics*: probability, the
  normal curve and the standard error in plain words, with worked numbers.
- **R. J. Barlow**, *Statistics: A Guide to the Use of Statistical Methods
  in the Physical Sciences*: the same ideas as physicists use them.
- **JCGM 100:2008**, *Guide to the Expression of Uncertainty in
  Measurement* (GUM): how a result and its uncertainty are written.
- **T. Herndon, M. Ash, R. Pollin** (2013), *Does High Public Debt
  Consistently Stifle Economic Growth? A Critique of Reinhart and Rogoff*.

## Take-aways

- A missing value is declared, counted and left out, and the README says
  how many and why. A code read as a number moves a mean far: 120 rows
  of −999 turn 7.16 into 5.78 °C.
- Every check of a table is a rule written before the count, with its
  count, zeros included.
- The mean is the balance point of the values; the standard deviation s is
  how far a single value typically lies from it; the median is the middle of
  the sorted values and hardly moves for a few wild ones.
- A probability counted from data is a share: P(frost) = 0.255. A condition
  changes it: 0.956 after a frost hour, 0.015 after none.
- The Gaussian holds 68.3 % within ± σ and 95.4 % within ± 2σ. The hours
  are not Gaussian; means of many independent values are.
- r measures how closely two columns follow a straight line, from −1 to +1,
  and says nothing about why; a curve can have r near 0.
- For N independent values the standard error of the mean is s/√N; four
  times the data halve it.
- Values that repeat their neighbours make s/√N too small. An honest ±
  comes from values that are close to independent: here the ten yearly
  means, 7.16 ± 0.22 °C.
