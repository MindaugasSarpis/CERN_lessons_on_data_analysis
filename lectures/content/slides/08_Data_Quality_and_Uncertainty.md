---
layout: cover
title: "Data Quality and Uncertainty"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Data Quality and Uncertainty

##### <span class="aims-badge">📁 data & files · ♻️ reproducibility</span>

<!--
**Say:** one number all lecture, the mean temperature of the station, 7.16 °C. First whether every hour behind it is valid; then how the hours spread, how often it freezes, the Gaussian and how two columns move together; at the end, how sure the mean is.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# It is better to be vaguely right than exactly **wrong**.
Carveth Read, *Logic: Deductive and Inductive* (1898)

---
hideInToc: true
---

# How Sure Is 7.16 **°C**?

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`weather.csv`, 2016 to 2025**

- 87 672 hours, one row each
- 120 of them hold −999: the sensor was down
- The mean of the 87 552 measured hours: **7.16 °C**

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📅 **The mean of each year (°C)**

| 2016 | 2017 | 2018 | 2019 | 2020 |
|--|--|--|--|--|
| 7.60 | 6.51 | 7.97 | 7.27 | 6.83 |
| **2021** | **2022** | **2023** | **2024** | **2025** |
| 7.25 | 6.60 | 8.31 | 7.27 | 5.98 |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ 7.16 °C comes from ten years. How far from the station's long-run mean can it be: about 0.03, 0.2, 1 or 9 °C?

</div>

<!--
**Ask:** a show of hands for each of the four; write the counts on the board.
**Say:** the long-run mean is what very many years of the same climate would average to. The years alone differ by up to 2.3 °C: 8.31 in 2023, 5.98 in 2025. By the end each of the four numbers has a meaning, and one of them answers the question.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Is Every Hour **Valid**?

A mean is only as good as the rows that go into it.

<!--
**Say:** before any statistics, the rows: what the file holds, what it should hold, and a count for every rule.
(~0.5 min)
-->

---
hideInToc: true
---

# Six Hours from 20:00 on 21 July **2019**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **Six lines of `weather.csv`**

```text
time,temp_c,humidity_pct,wind_ms
2019-07-21T20:00,27.3,63,4.5
2019-07-21T21:00,25.6,65,4.0
2019-07-21T22:00,24.6,68,3.5
2019-07-21T23:00,23.6,74,3.4
2019-07-22T00:00,-999,76,3.2
2019-07-22T01:00,-999,81,3.0
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Their mean**

With the marks:

$$
\frac{27.3 + 25.6 + 24.6 + 23.6 - 999 - 999}{6} = -316.15\ ^\circ\mathrm{C}
$$

<div v-click>

Without them:

$$
\frac{27.3 + 25.6 + 24.6 + 23.6}{4} = 25.275\ ^\circ\mathrm{C}
$$

</div>

</div>

</div>

<div class="note-text mt-sm">−999 is the station's code for “no reading”: a mark, not a temperature.</div>

<!--
**Ask:** what was the temperature at midnight? Nobody knows: the sensor was down from 00:00 on 22 July to the end of 26 July.
**Say:** humidity and wind were still measured; only the temperature is missing.
(~2 min)
-->

---
hideInToc: true
---

# The Mean of the Log, With and Without the **Marks**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🧮 **The 87 552 measured hours add up to 626 869.3 °C**

$$
\text{mean} = \frac{626\,869.3}{87\,552} = 7.16\ ^\circ\mathrm{C}
$$

</div>

<div v-click class="card card-warning card-glass pad-compact mt-md">

## ⚠️ **The 120 marks read as temperatures**

$$
\frac{626\,869.3 + 120 \times (-999)}{87\,672} = \frac{506\,989.3}{87\,672} = 5.78\ ^\circ\mathrm{C}
$$

</div>

<div v-click class="note-text mt-md">120 rows of 87 672, 0.14 % of the file, moved a ten-year mean by 1.38 °C.</div>

<!--
**Ask:** before the click: with the marks in, will the mean be higher or lower than 7.16, and by how much?
**Say:** the marks add 120 × (−999) = −119 880 to the sum, and 120 to the count.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The 120 Marks in a **Figure**

<div class="card card-warning card-glass pad-compact mt-sm">

📉 Every row of the file in order, −999 read as a temperature. The axis stretches down to −1000 °C, and ten years of weather shrink to a flat band.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_every_row.svg">

<!--
**Say:** a plot of the raw column is the quickest check there is: one line down to −999 shows the mark at once.
(~1 min)
-->

---
hideInToc: true
---

# How Files Mark a Missing **Value**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| In the file | What a program reads, unless told |
|--|--|
| an empty cell | missing |
| `NA`, `NaN`, `n/a` | missing in some programs, text in others |
| `-999`, `9999`, `-99.9` | a number, used in every mean |

</div>

<div class="note-text mt-md">The code is found in the README or by looking at the file, declared before reading, and counted.</div>

<!--
**Say:** an empty cell is honest; a code such as −999 looks like data. Every station, survey or instrument picks its own.
**Ask:** what would a code of 0 have done to the mean? 120 × (0 − 7.16) / 87 672 = −0.0098 °C: a shift nobody would notice, and still wrong.
(~2 min)
-->

---
hideInToc: true
---

# Four Ways to Treat 120 Missing **Hours**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The 120 hours of 22 to 26 July 2019 are | Mean of the ten years |
|--|--|
| read as −999 | 5.783 °C |
| set to 0 °C | 7.150 °C |
| left out | **7.160 °C** |
| set to 17.46 °C, the mean of 22 to 26 July in the other nine years | 7.174 °C |

</div>

<div class="note-text mt-md">Leaving them out is a choice too: five summer days are missing, so the mean of the rest is 0.014 °C too cold.</div>

<!--
**Say:** each line is one decision in a script, and the README says which one was taken. Here: left out, 120 hours, 22 to 26 July 2019.
**Ask:** which choice would you defend in a report, and how would you write it down?
**If asked:** 0.014 °C is small, but not zero: a gap in one season always tilts a yearly mean.
(~2 min)
-->

---
hideInToc: true
---

# A Published Mean Changed by Left-Out **Rows**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **2010, Reinhart and Rogoff**

- countries with public debt above 90 % of GDP: growth **−0.1 %** a year on average
- quoted in debates on budget cuts

</div>

<div v-click class="card card-warning card-glass pad-compact">

## 🔍 **2013, a student re-runs their spreadsheet**

- a formula averaged rows 30 to 44 instead of 30 to 49: 5 of 20 countries left out
- years left out with no written rule
- corrected: **+2.2 %** (Herndon, Ash and Pollin)

</div>

</div>

<div v-click class="note-text mt-md">In a script, every row left out is a rule with a count.</div>

<!--
**Say:** none of it was exotic: a range typed one row too short, rows dropped without a written reason, and a way of averaging nobody could see. In a spreadsheet the calculation hides in the cells; in a script each step is a line.
**If asked:** the third finding was the weighting: each country counted once, whether it had 1 year above 90 % or 19. Reinhart and Rogoff, *Growth in a Time of Debt*, 2010; Herndon, Ash and Pollin, 2013.
(~2 min)
-->

---
hideInToc: true
---

# Five Checks, Each with a **Count**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Check | The rule for `weather.csv` | Rows that break it |
|--|--|--|
| **Completeness** | a value in every cell; −999 counts as missing | 120, all in `temp_c` |
| **Validity** | humidity 0 to 100 %, wind 0 m/s or more, temperature −50 to 50 °C | 0, the 120 marks aside |
| **Uniqueness** | every hour once | 0 |
| **Consistency** | one row per hour, 2016-01-01 00:00 to 2025-12-31 23:00: 3653 days × 24 | 0 missing of 87 672 |
| **Units** | °C, % and m/s, as the README says: the coldest and the warmest hour plausible | 0: −16.3 and 32.4 °C |

</div>

<div class="note-text mt-md">Each rule is written down before the count; the counts go into the README, the zeros too.</div>

<!--
**Say:** the rule comes from what a column means, not from the values found in it. A count of 0 is a result worth writing down: no hour twice, none missing, no humidity of 140 %.
**If asked:** the time steps were checked one by one: every row is exactly one hour after the one before.
(~3 min)
-->

---
hideInToc: true
---

# Is `temp_c` in °C? A Check with **Numbers**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 🌡️ **If the column were in °F**

$$
C = (F - 32) \times \tfrac{5}{9}
$$

- coldest hour: (−16.3 − 32) × 5/9 = **−26.8 °C**
- warmest hour: (32.4 − 32) × 5/9 = **0.2 °C**

A summer that never thaws.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Read as °C**

- coldest hour −16.3 °C, 7 January 2025, 05:00
- warmest hour 32.4 °C, 18 June 2018, 15:00
- January mean −3.9 °C, July mean 18.5 °C

A cold winter and a mild summer: °C.

</div>

</div>

<!--
**Say:** no command finds a unit in a column of numbers. The check is a typical value against something known from elsewhere; a wrong unit shows up as a factor, an offset, or a season that makes no sense.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Describing a **Distribution**

87 552 hours, described by a few numbers.

<!--
**Say:** the mean, how far the hours spread around it, and the middle of the sorted hours: each one as an expression, with the four measured hours of 21 July pushed through it.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Hours in Bins of 1 **°C**

<div class="card card-primary card-glass pad-compact mt-sm">

📊 Two peaks: 3848 hours at −1 to 0 °C, 3032 at 11 to 12 °C. The mean, 7.16 °C, lies in the dip between them: 2706 hours.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_hist_mean.svg">

<!--
**Say:** the histogram of Lecture 7: the cold months pile up near freezing, the warm months near 12 °C. Fewer hours lie near the mean than near either peak.
(~1 min)
-->

---
hideInToc: true
---

# The Cold and the Warm Half of the **Year**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ❄️ **November to March**

36 312 hours, mean **−0.96 °C**

</div>

<div class="card card-secondary card-glass pad-compact">

## ☀️ **April to October**

51 240 hours, mean **12.91 °C**

</div>

</div>

<div v-click class="card card-info card-glass pad-compact mt-md">

$$
\frac{36\,312 \times (-0.96) + 51\,240 \times 12.91}{87\,552} = 7.16\ ^\circ\mathrm{C}
$$

The mean of all hours is the mean of the two halves, weighted by their hours: a temperature typical of neither.

</div>

<!--
**Ask:** before the click: where between −0.96 and 12.91 will the mean of all hours fall, and why not in the middle, 5.98?
**Say:** the warm half has more hours, seven months against five, so the mean leans towards it.
(~2 min)
-->

---
hideInToc: true
---

# Adding Up: the Sum Sign **Σ**

$$
\sum_{i=1}^{N} x_i = x_1 + x_2 + \dots + x_N
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **The parts of the expression**

- $i$ counts from 1 to $N$
- $x_i$ is the $i$-th value
- Σ adds the term after it, once for each $i$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **The four measured hours of 21 July**

$x_1 = 27.3$, $x_2 = 25.6$, $x_3 = 24.6$, $x_4 = 23.6$

$$
\sum_{i=1}^{4} x_i = 27.3 + 25.6 + 24.6 + 23.6 = 101.1
$$

</div>

</div>

<!--
**Say:** Σ is the Greek capital S, for sum: a `for` loop written as a symbol. `total = total + x` for every value is the sum.
(~2 min)
-->

---
hideInToc: true
---

# The **Mean**

$$
\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **The four hours**

$$
\bar{x} = \frac{101.1}{4} = 25.275\ ^\circ\mathrm{C}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **The log**

$$
\bar{x} = \frac{626\,869.3}{87\,552} = 7.16\ ^\circ\mathrm{C}
$$

</div>

</div>

<div class="note-text mt-md">

$\bar{x}$, “x bar”: the mean of the values $x$.

</div>

<!--
**Say:** the same expression for four values and for 87 552: add, then divide by the count.
(~1 min)
-->

---
hideInToc: true
---

# How Far Each Hour Lies from the **Mean**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| 21 July 2019 | 20:00 | 21:00 | 22:00 | 23:00 | Σ |
|--|--|--|--|--|--|
| $x_i$ (°C) | 27.3 | 25.6 | 24.6 | 23.6 | 101.1 |
| $x_i - \bar{x}$ (°C) | +2.025 | +0.325 | −0.675 | −1.675 | 0 |

</div>

<div class="note-text mt-md">The deviations above the mean cancel those below it: their sum is 0 for any values, so their mean says nothing about the spread.</div>

<!--
**Say:** 27.3 − 25.275 = +2.025, and so on. The mean is the balance point of the values: the pulls on either side are equal.
**Ask:** how can the spread be measured if the deviations always cancel?
(~1.5 min)
-->

---
hideInToc: true
---

# Variance and Standard **Deviation**

$$
s^2 = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2 \qquad s = \sqrt{s^2}
$$

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| 21 July 2019 | 20:00 | 21:00 | 22:00 | 23:00 | Σ |
|--|--|--|--|--|--|
| $x_i - \bar{x}$ (°C) | +2.025 | +0.325 | −0.675 | −1.675 | 0 |
| $(x_i - \bar{x})^2$ (°C²) | 4.1006 | 0.1056 | 0.4556 | 2.8056 | 7.4675 |

</div>

<div v-click class="card card-success card-glass pad-compact mt-sm">

$$
s^2 = \frac{7.4675}{3} = 2.489\ ^\circ\mathrm{C}^2 \qquad s = \sqrt{2.489} = 1.58\ ^\circ\mathrm{C}
$$

</div>

<div class="note-text mt-sm">A square is never negative, so nothing cancels; the root brings the unit back to °C.</div>

<!--
**Say:** s², the variance, is the mean squared distance from the mean; s, the standard deviation, is how far a single value typically lies from it.
**If asked:** why N − 1 = 3 and not 4: the deviations are measured from x̄, which was computed from the same four values and lies closer to them than the long-run mean does. Dividing by 4 would give s = 1.37 °C.
(~3 min)
-->

---
hideInToc: true
---

# The Four Hours in **Python**

```py {monaco-run} {autorun:false}
hours = [27.3, 25.6, 24.6, 23.6]       # 21 July 2019, 20:00 to 23:00
n = len(hours)
mean = sum(hours) / n
total = 0
for x in hours:
    total = total + (x - mean) ** 2    # the squared deviation of each hour
var = total / (n - 1)
print(round(mean, 3))                        # 25.275
print(round(var, 3), round(var ** 0.5, 2))   # 2.489 1.58
```

<!--
**Do:** press ▶. Then change one hour, 27.3 to 37.3, and run again: the mean moves by 2.5, the standard deviation from 1.58 to 6.40.
**Say:** each line is a piece of the expression: `sum`, the loop for Σ, `n - 1`, and `** 0.5` for the square root.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Standard Deviation of the 87 552 **Hours**

<div class="card card-primary card-glass pad-compact mt-sm">

📏 $s^2$ = 6 858 427 / 87 551 = 78.34 °C², $s$ = 8.85 °C. The mean ± s, −1.7 to 16.0 °C, holds 62.6 % of the hours.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_hist_sd.svg">

<!--
**Say:** 6 858 427 °C² is the sum of the squared deviations of the 87 552 hours, divided by N − 1 = 87 551. 8.85 °C: how far a single hour typically lies from 7.16. It describes the hours, not how well 7.16 is known.
**Ask:** with 87 552 hours instead of four, should s be larger or smaller than 1.58? Larger: the four hours came from one evening, the log holds winters and summers.
(~2 min)
-->

---
hideInToc: true
---

# The Median Against the **Mean**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The hours of 21 July 2019, sorted | Mean | Median |
|--|--|--|
| 23.6, **24.6**, **25.6**, 27.3: the four measured | 25.275 °C | (24.6 + 25.6) / 2 = 25.1 °C |
| −999, −999, **23.6**, **24.6**, 25.6, 27.3: −999 read as a number | −316.15 °C | (23.6 + 24.6) / 2 = 24.1 °C |

</div>

<div class="note-text mt-md">Two marks move the mean by 341 °C and the median by 1 °C.</div>

<!--
**Say:** the median is the middle of the sorted values; with an even count, the mean of the two in the middle. A few wild values hardly move it.
**Ask:** which one would you report for a file you have not checked yet? Both, and look at why they differ.
(~2 min)
-->

---
hideInToc: true
---

# The Median in **Python**

```py {monaco-run} {autorun:false}
hours = [27.3, 25.6, 24.6, 23.6, -999, -999]   # 21 July 2019, 20:00 to 01:00
s = sorted(hours)
mid = len(s) // 2                               # 3: the upper of the two middle places
print(s)                                        # [-999, -999, 23.6, 24.6, 25.6, 27.3]
print((s[mid - 1] + s[mid]) / 2)                # 24.1, the median
print(round(sum(s) / len(s), 2))                # -316.15, the mean
```

<!--
**Do:** press ▶; then replace one −999 by 25.0 and run again: the median moves to 24.8, the mean to −145.48.
**Say:** `sorted` gives a new list in increasing order; `//` divides and drops the fraction, 6 // 2 = 3; places count from 0, so `s[2]` and `s[3]` are the two in the middle.
(~2 min)
-->

---
hideInToc: true
---

# Percentiles of the 87 552 **Hours**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Share of the hours below | 5 % | 25 % | 50 %, the median | 75 % | 95 % |
|--|--|--|--|--|--|
| Temperature | −6.0 °C | −0.2 °C | 6.7 °C | 14.2 °C | 21.8 °C |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📦 **The middle half**

From −0.2 to 14.2 °C: the box of a boxplot.

</div>

<div class="card card-accent card-glass pad-compact">

## ↔️ **Nine hours in ten**

From −6.0 to 21.8 °C.

</div>

</div>

<!--
**Say:** a percentile is the value below which that share of the hours lies. The median, 6.7 °C, lies 0.46 °C below the mean.
**If asked:** these are the numbers a boxplot draws: the box from the 25 % to the 75 % point, a line at the median.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Probability by **Counting**

A probability is a share of cases: here, a share of hours.

<!--
**Say:** no coins and no dice: every probability today is counted in the log.
(~0.5 min)
-->

---
hideInToc: true
---

# P(frost): a Share of **Hours**

$$
P(A) = \frac{n(A)}{N}
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ❄️ **A: the hour is below 0 °C**

$$
P(\text{frost}) = \frac{22\,352}{87\,552} = 0.255
$$

About one hour in four.

</div>

<div class="card card-secondary card-glass pad-compact">

## ☀️ **Not A**

$$
P(\text{no frost}) = 1 - 0.255 = 0.745
$$

The two add up to 1.

</div>

</div>

<div class="note-text mt-md">n(A): the hours in which A happened; N: all the hours counted.</div>

<!--
**Say:** an event is a statement that is true or false for each hour; its probability is the share of hours in which it is true.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Share Settles as Hours Are **Counted**

<div class="card card-primary card-glass pad-compact mt-sm">

🎲 Hours counted in random order: the share wanders, then settles at 0.255. Counted in time order from 1 January 2016, it stays at 1 for 205 hours, then swings with the seasons for years.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_running_share.svg">

<!--
**Say:** a probability is the share in the long run, and it needs cases that are not linked to each other: in time order the first 205 hours were one cold spell.
**Ask:** why does the time-order line only settle after many years? Each winter pushes it up, each summer down.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# P(frost) in Each **Month**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## ❄️ **The coldest and the warmest months**

- January 0.85, December 0.73
- June to August: 0 of 21 960 hours
- a condition changes the probability: 0.85 in January, 0.255 over the year

</div>

<img class="fig" src="/figures/viz_probability_frost_months.svg">

</div>

<!--
**Say:** the dashed line is all hours together, 0.255: an average over months that are nothing like it.
**If asked:** May has 11 frost hours of 7440, September 2 of 7200.
(~1 min)
-->

---
hideInToc: true
---

# Conditional **Probability**

$$
P(A \mid B) = \frac{n(A \text{ and } B)}{n(B)}
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ❄️ **B: the hour is in January**

$$
P(\text{frost} \mid \text{January}) = \frac{6336}{7440} = 0.852
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## ☀️ **B: the hour is in July**

$$
P(\text{frost} \mid \text{July}) = \frac{0}{7320} = 0
$$

</div>

</div>

<div class="note-text mt-md">“|” reads “given”: only the hours in which B happened are counted.</div>

<!--
**Say:** a condition shrinks the hours that are counted: 7440 January hours instead of 87 552.
**If asked:** July has 7320 measured hours, not 7440: the 120 hours of 2019 are left out.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Frost at 03:00 and at 14:00 in **March**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🕒 **Two conditions: March and the hour**

- all of March: 0.37
- at 03:00: **0.68**
- at 14:00: **0.11**

The night freezes, the afternoon thaws.

</div>

<img class="fig" src="/figures/viz_probability_frost_march.svg">

</div>

<!--
**Say:** each bar counts the March hours at one time of day, 310 of them over ten years. 0.37 for the month hides 0.68 before dawn and 0.11 in the afternoon.
(~1 min)
-->

---
hideInToc: true
---

# Frost Given the Hour **Before**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| 87 550 pairs of neighbouring hours | frost now | no frost now | together |
|--|--|--|--|
| **frost the hour before** | 21 378 | 973 | 22 351 |
| **no frost the hour before** | 973 | 64 226 | 65 199 |

</div>

<div class="grid-2 mt-md gap-md">

<div v-click class="card card-warning card-glass pad-compact">

$$
P(\text{frost} \mid \text{frost before}) = \frac{21\,378}{22\,351} = 0.956
$$

</div>

<div v-click class="card card-success card-glass pad-compact">

$$
P(\text{frost} \mid \text{no frost before}) = \frac{973}{65\,199} = 0.015
$$

</div>

</div>

<!--
**Say:** every hour paired with the hour before it, where both were measured. 973 frosts began and 973 ended.
**Ask:** before the clicks: if it froze at 05:00, how likely is frost at 06:00?
(~2 min)
-->

---
hideInToc: true
---

# Are Neighbouring Hours **Independent**?

<div class="card card-info card-glass pad-compact mt-sm">

A and B are **independent** when B says nothing about A, P(A | B) = P(A). Then

$$
P(A \text{ and } B) = P(A)\,P(B)
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **If neighbouring hours were independent**

$$
P(\text{frost twice}) = 0.255 \times 0.255 = 0.065
$$

</div>

<div v-click class="card card-warning card-glass pad-compact">

## 📄 **Counted**

$$
P(\text{frost twice}) = \frac{21\,378}{87\,550} = 0.244
$$

</div>

</div>

<div v-click class="note-text mt-md">Counted, frost twice in a row is almost four times as common: neighbouring hours are not independent.</div>

<!--
**Say:** the general rule is P(A and B) = P(A | B) P(B) = 0.956 × 0.255 = 0.244, which matches the count. Only for independent events does P(A | B) shrink to P(A).
(~2 min)
-->

---
hideInToc: true
---

# Frost Given the Hour Before, in One **Day**

```py {monaco-run} {autorun:false}
day = [-2.3, -2.1, -2.4, -2.8, -2.8, -2.2, -1.5, -1.3, -0.6, 0.4, 1.2, 1.9,
       2.6, 3.6, 4.3, 4.0, 3.9, 3.6, 2.9, 2.4, 1.6, 0.1, 0.4, -0.4]   # 10 March 2025
before = 0
both = 0
for i in range(1, 24):
    if day[i - 1] < 0:
        before = before + 1           # frost the hour before
        if day[i] < 0:
            both = both + 1           # and frost this hour
print(both, before, round(both / before, 3))   # 8 9 0.889
```

<!--
**Do:** press ▶. Frost from 00:00 to 08:00, a thaw from 09:00, frost again at 23:00.
**Say:** `range(1, 24)` gives i = 1 to 23, so `day[i - 1]` is always the hour before. Of the 9 hours with frost the hour before, 8 kept it: one day gives 0.889, ten years 0.956.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **Gaussian**

One curve and two numbers: where the values centre, and how far they spread.

<!--
**Say:** the curve behind most error bars, then a check whether the hours follow it.
(~0.5 min)
-->

---
hideInToc: true
---

# The Gaussian **Curve**

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\; e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔔 **μ and σ**

- $\mu$: the centre, where the curve peaks
- $\sigma$: its width
- $e = 2.718$; $e^{-1/2} = 0.6065$, $e^{-2} = 0.1353$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **μ = 7.16 °C, σ = 8.85 °C**

- at $x = \mu$: $f = \dfrac{1}{8.85 \times 2.507} = 0.0451$ per °C
- × 87 552 hours: **3946 hours** per bin of 1 °C
- at $\mu \pm \sigma$: × 0.6065 = 2393; at $\mu \pm 2\sigma$: × 0.1353 = 534

</div>

</div>

<div class="note-text mt-sm">

Greek letters for the curve, Latin for the data: $\mu$ is estimated by $\bar{x}$ = 7.16, $\sigma$ by $s$ = 8.85.

</div>

<!--
**Say:** √(2π) = 2.507. The curve is highest at μ and falls off symmetrically; one σ away it is at 0.607 of its top, two σ away at 0.135.
**If asked:** the factor in front makes the area under the curve 1; multiplied by the number of hours and the bin width, the curve says how many hours a bin should hold.
(~3 min)
-->

---
hideInToc: true
---

# The Gaussian in **Python**

```py {monaco-run} {autorun:false}
import math
mu = 7.16           # °C, the mean of the hours
sigma = 8.85        # °C, their s
n = 87552           # hours
for x in [-0.5, 7.5, 11.5]:                 # the middles of three bins of 1 °C
    f = math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
    print(x, round(f, 4), round(n * f))     # -0.5 0.031 2714 | 7.5 0.045 3944 | 11.5 0.04 3500
```

<div class="note-text mt-md">The log has 3848, 2706 and 3032 hours in these three bins.</div>

<!--
**Do:** press ▶; then try x = 32.4, the warmest hour.
**Say:** `math.exp(y)` is e to the power y, `math.sqrt` the square root, `math.pi` 3.14159: the expression of the curve, term by term.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Areas Under the **Gaussian**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🔔 **The area under the curve**

- within μ ± σ: **68.3 %**
- within μ ± 2σ: **95.4 %**
- within μ ± 3σ: **99.7 %**

The same for every Gaussian, whatever μ and σ.

</div>

<img class="fig" src="/figures/viz_probability_gaussian.svg">

</div>

<!--
**Say:** two in three within one σ, nineteen in twenty within two, all but three in a thousand within three. A result quoted as value ± σ leans on these numbers.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Hours Against a **Gaussian**

<div class="card card-warning card-glass pad-compact mt-sm">

📊 A Gaussian with the mean and the s of the hours expects about 3940 hours at 7 to 8 °C; the log has 2706. It expects one peak; the log has two.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_hours_gauss.svg">

<!--
**Ask:** where does the curve over-count, and where does it under-count?
**Say:** too many hours near the mean, too few near freezing and near 12 °C, too many in the far tails.
(~2 min)
-->

---
hideInToc: true
---

# The Gaussian Check in **Numbers**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Interval | A Gaussian holds | The hours hold |
|--|--|--|
| $\bar{x} \pm s$: −1.7 to 16.0 °C | 68.3 % | 62.6 % |
| $\bar{x} \pm 2s$: −10.5 to 24.9 °C | 95.4 % | 97.8 % |
| $\bar{x} \pm 3s$: −19.4 to 33.7 °C | 99.7 % | 100 % |

</div>

<div v-click class="card card-info card-glass pad-compact mt-md">

$$
z = \frac{x - \bar{x}}{s}: \qquad \frac{-16.3 - 7.16}{8.85} = -2.65 \qquad \frac{32.4 - 7.16}{8.85} = +2.85
$$

A Gaussian would put 352 hours below the coldest hour, −16.3 °C, and 190 above the warmest, 32.4 °C. The log has none.

</div>

<!--
**Say:** z is the distance from the mean in units of s. Fewer hours near the mean and no long tails: the hours are not Gaussian, and a rule that assumes a Gaussian does not hold for them.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Means of 100 Random Hours: a **Gaussian**

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

## 🎲 **2000 draws of 100 hours**

- one peak, at 7.14 °C
- the means scatter by 0.89 °C
- 67 % of them within ± 0.885 °C, which is s/√100

Means of many independent values come out Gaussian, whatever the values look like: the central limit theorem.

</div>

<img class="fig" src="/figures/viz_probability_means_random.svg">

</div>

<!--
**Say:** each draw takes 100 hours from anywhere in the ten years, two peaks and all, and keeps only their mean. The two peaks are gone: a mean adds up many values, and sums of many independent values take the Gaussian shape.
**If asked:** the theorem needs independent values with a finite spread; the proof is beyond this course.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Correlation**

Do two columns rise and fall together?

<!--
**Say:** two columns of the same hours, and one number for how closely they move together.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Temperature and Humidity of Every **Hour**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## 💧 **87 552 hours**

- warm hours are drier
- the cloud falls from left to right
- the colour of a cell: how many hours it holds

</div>

<img class="fig" src="/figures/viz_probability_temp_humidity.svg">

</div>

<!--
**Say:** humidity here is relative humidity: warm air holds more water vapour, so the same water makes a lower percentage.
(~1 min)
-->

---
hideInToc: true
---

# Covariance: Do Two Columns Move **Together**?

$$
s_{xy} = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})
$$

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| 21 July 2019 | 20:00 | 21:00 | 22:00 | 23:00 | Σ |
|--|--|--|--|--|--|
| $x_i - \bar{x}$: temperature (°C) | +2.025 | +0.325 | −0.675 | −1.675 | 0 |
| $y_i$: humidity (%) | 63 | 65 | 68 | 74 | 270 |
| $y_i - \bar{y}$ (%) | −4.5 | −2.5 | +0.5 | +6.5 | 0 |
| product | −9.11 | −0.81 | −0.34 | −10.89 | −21.15 |

</div>

<div v-click class="card card-success card-glass pad-compact mt-sm">

$$
s_{xy} = \frac{-21.15}{3} = -7.05\ ^\circ\mathrm{C} \cdot \%
$$

</div>

<div class="note-text mt-sm">Every product is negative: when the temperature lies above its mean, the humidity lies below its own, ȳ = 67.5 %.</div>

<!--
**Say:** a product is positive when both lie on the same side of their means, negative when on opposite sides; the sum says which wins.
**If asked:** ȳ = 270 / 4 = 67.5 %.
(~3 min)
-->

---
hideInToc: true
---

# The Correlation Coefficient **r**

$$
r = \frac{s_{xy}}{s_x\, s_y}
$$

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **The four hours**

- $s_x$ = 1.578 °C, $s_y$ = 4.796 %
- $r = \dfrac{-7.05}{1.578 \times 4.796} = -0.93$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **All 87 552 hours**

- $r$ = −0.70
- the units cancel: $r$ has none
- always from −1 to +1

</div>

</div>

<div class="note-text mt-md">r = +1: the points lie on a rising straight line; −1: on a falling one; 0: no straight line at all.</div>

<!--
**Say:** dividing by both standard deviations takes away the units and the scale: °C or °F, % or a fraction, r stays the same.
**Ask:** why is r closer to −1 for the four hours than for the whole log? One evening of cooling air: four points nearly on a line.
(~2 min)
-->

---
hideInToc: true
---

# r of the Four Hours in **Python**

```py {monaco-run} {autorun:false}
temp = [27.3, 25.6, 24.6, 23.6]    # °C, 21 July 2019, 20:00 to 23:00
hum = [63, 65, 68, 74]             # %, the same hours
mt = sum(temp) / 4
mh = sum(hum) / 4
sxy = 0
sxx = 0
syy = 0
for i in range(4):
    sxy = sxy + (temp[i] - mt) * (hum[i] - mh)
    sxx = sxx + (temp[i] - mt) ** 2
    syy = syy + (hum[i] - mh) ** 2
print(round(sxy / (sxx * syy) ** 0.5, 2))     # -0.93
```

<!--
**Do:** press ▶; then swap the last two humidities, 74 and 68, and run again.
**Say:** the 1/(N − 1) of the covariance and of the two variances cancel in r, so the three sums are enough; sxy is the −21.15 of the covariance table.
(~2 min)
-->

---
hideInToc: true
---

# r for Pairs of **Columns**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Two columns of the hours | r |
|--|--|
| temperature and humidity | −0.70 |
| temperature and wind | −0.12 |
| humidity and wind | −0.05 |
| the temperature of an hour and of the next hour | +0.996 |
| the temperature of an hour and of the same hour a day later | +0.978 |

</div>

<div class="note-text mt-md">Near 0: no straight-line relation. Near 1: the two move together, almost on a line.</div>

<!--
**Say:** the last two rows pair the column with itself, shifted by an hour and by a day: the weather of one hour nearly repeats the one before.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# Two Random Hours, and an Hour and the **Next**

<div class="card card-primary card-glass pad-compact mt-sm">

🔗 4000 pairs each. Two hours drawn at random say nothing about each other: r = 0.02. An hour and the next lie almost on a straight line: r = 0.996.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_pairs.svg">

<!--
**Say:** the left panel is what independent values look like; the right panel is what the log is made of.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# r Measures Only a Straight **Line**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Day of the year and temperature**

- the season sets the temperature: January −3.9 °C, July 18.5 °C
- yet r = 0.21, over 3648 days
- the relation rises, then falls; r measures only a straight line

</div>

<img class="fig" src="/figures/viz_probability_day_of_year.svg">

</div>

<!--
**Say:** a small r does not mean no relation, only no straight one.
**Ask:** does humidity cool the air, since the two are correlated? r says they move together, not why: both follow the time of day and the season.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The Standard **Error**

How far from the long-run mean is a mean of N values?

<!--
**Say:** the one derivation of the lecture, from two rules about variances.
(~0.5 min)
-->

---
hideInToc: true
---

# The Variance of a **Sum**

$$
\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,r\,\sigma_X \sigma_Y
$$

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **Two hours drawn at random: r = 0**

$$
\sqrt{78.34 + 78.34} = 12.52\ ^\circ\mathrm{C}
$$

100 000 such pairs: 12.50 °C

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔗 **An hour and the next: r = 0.996**

$$
\sqrt{78.34 + 78.34 + 2 \times 0.996 \times 78.34} = 17.68\ ^\circ\mathrm{C}
$$

100 000 such pairs: 17.63 °C

</div>

</div>

<div class="note-text mt-sm">X, Y: two hours; Var(X) = σ², 78.34 °C² for one hour. For independent values r = 0: the variances add.</div>

<!--
**Say:** the spread of the sum of two hours, two ways. Independent hours: the variances add, and the standard deviation grows by √2, not by 2. Neighbouring hours move together, so their sum spreads almost twice as much as one hour, 2 × 8.85 = 17.70.
(~3 min)
-->

---
hideInToc: true
---

# A Factor Comes Out **Squared**

$$
\mathrm{Var}(aX + b) = a^2\, \mathrm{Var}(X)
$$

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **The hours in °F: F = 1.8 C + 32**

- variance: 1.8² × 78.34 = 253.8 °F²
- standard deviation: 1.8 × 8.85 = 15.93 °F
- the + 32 moves every hour alike: no spread

</div>

<div class="card card-secondary card-glass pad-compact">

## ➗ **a = 1/N**

$$
\mathrm{Var}\!\left(\frac{X}{N}\right) = \frac{\mathrm{Var}(X)}{N^2}
$$

Dividing by N divides the variance by N².

</div>

</div>

<!--
**Say:** a factor scales every deviation, and the variance holds squared deviations, so the factor enters squared.
(~2 min)
-->

---
hideInToc: true
---

# The Variance of a **Mean**

<div class="card card-primary card-glass pad-compact mt-sm">

$$
\bar{x} = \frac{x_1 + x_2 + \dots + x_N}{N}
$$

</div>

<div v-click class="card card-secondary card-glass pad-compact mt-sm">

$$
\mathrm{Var}(\bar{x}) = \frac{1}{N^2}\, \mathrm{Var}(x_1 + x_2 + \dots + x_N) \qquad \text{the factor } \tfrac{1}{N}\text{, squared}
$$

</div>

<div v-click class="card card-accent card-glass pad-compact mt-sm">

$$
= \frac{1}{N^2}\,(\sigma^2 + \sigma^2 + \dots + \sigma^2) = \frac{N \sigma^2}{N^2} = \frac{\sigma^2}{N} \qquad \text{independent: the variances add}
$$

</div>

<div v-click class="card card-success card-glass pad-compact mt-sm">

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{N}} \approx \frac{s}{\sqrt{N}}
$$

</div>

<div v-click class="note-text mt-sm">The standard error of the mean: how far a mean of N independent values typically lies from the long-run mean.</div>

<!--
**Say:** two rules, two lines. The factor 1/N comes out squared; N independent variances add up to N σ²; what is left is σ²/N.
**Ask:** how many values halve the standard error? Four times as many: √4 = 2.
(~3 min)
-->

---
hideInToc: true
---

# s/√N, Checked on Random **Hours**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Hours per mean | s/√N | 2000 means of hours drawn at random scatter by |
|--|--|--|
| 100 | 8.85 / 10 = 0.885 °C | 0.890 °C |
| 1000 | 8.85 / 31.6 = 0.280 °C | 0.281 °C |

</div>

<div class="note-text mt-md">Hours drawn at random are independent, and for them the rule holds to within 1 %.</div>

<!--
**Say:** the derivation on paper, the draws from the file: they agree.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# The Mean of N Random Hours, **Live**

<div class="card card-info card-glass pad-compact mt-sm">

🎲 Pick how many hours go into each mean: 1000 such means spread by about s/√N

</div>

<MeanSpread class="fig-fill mt-sm" />

<!--
**Do:** start at N = 1: each mean is a single hour, so the means keep the two peaks and spread by 8.86 °C, against s/√1 = 8.85. Click 4, 16, 100 and 1000 and read the spread beside s/√N each time: 4.32 against 4.43, 2.25 against 2.21, 0.883 against 0.885, 0.279 against 0.280. At 100 and 1000, press "zoom in" to see the bell.
**Say:** for hours drawn at random the rule holds at every N: four times the hours, half the spread.
(~3 min)
-->
---
hideInToc: true
class: fill
---

# What ± One Standard Error **Means**

<div class="card card-primary card-glass pad-compact mt-sm">

🎯 50 means of 100 random hours, each ± s/10 = 0.885 °C: 28 of the intervals hold 7.16, the mean of all hours; the red ones miss it. Of 2000 such intervals, 67 % hold it, and 96 % with ± 2 s/10.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_intervals.svg">

<!--
**Say:** a value ± one standard error is an interval that holds the long-run mean in about two cases of three; ± two, in 19 of 20. Here the long-run mean is known: the hours were drawn from the log, whose mean is 7.16.
**Ask:** 28 of 50 is 56 %, not 68 %: is the rule wrong? Fifty intervals are few; 2000 give 67 %.
(~2 min)
-->

---
hideInToc: true
---

# How the Standard Error Shrinks with **N**

```py {monaco-run} {autorun:false}
s = 8.85                       # °C, the standard deviation of the hours
for n in [100, 400, 1600, 6400, 87552]:
    print(n, round(s / n ** 0.5, 3))     # 0.885, 0.443, 0.221, 0.111, 0.03
```

<div class="note-text mt-md">Each step multiplies N by 4 and halves the standard error: √4 = 2.</div>

<!--
**Do:** press ▶; then ask the room for an N that gives ± 0.1 °C, and try it: N = (8.85 / 0.1)² = 7832.
**Say:** precision is expensive: one more correct digit costs a hundred times the data.
(~2 min)
-->

---
hideInToc: true
---

# The Standard Error of **7.16**

<FormulaSteps steps="
  \frac{s}{\sqrt{N}} = \frac{8.85}{\sqrt{87\,552}}
  = \frac{8.85}{295.9}
  = 0.030 \text{ °C}
" />

<div v-click class="card card-warning card-glass pad-compact mt-md">

7.160 ± 0.030 °C, **if the 87 552 hours were independent.**

</div>

<!--
**Do:** click through: √87 552 = 295.9, then 0.030, then the condition.
**Say:** if the hours were independent, 7.16 would be known to 0.03 °C, three hundredths of a degree from ten years of one station.
**Ask:** the hours are not independent: an hour nearly repeats the one before. Is 0.030 too small or too large?
(~2 min)
-->

---
layout: section
hideInToc: true
---

# When Hours Are Not **Independent**

Each hour repeats much of the hour before.

<!--
**Say:** s/√N needs independent values. The log shows what happens without them.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Means of 1000 Hours, Random or in a **Row**

<div class="card card-warning card-glass pad-compact mt-sm">

📅 Means of 1000 random hours scatter by 0.28 °C, as s/√1000 says. Means of 1000 hours in a row, six weeks each, scatter by 7.75 °C: six weeks are one season.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_random_vs_row.svg">

<!--
**Say:** the same number of hours, a scatter 28 times larger. Hours in a row bring one stretch of weather, not 1000 independent hours.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# r Against the Time Between Two **Hours**

<div class="card card-primary card-glass pad-compact mt-sm">

🕰️ r of the temperatures of two hours, against the time between them: 0.996 an hour apart, 0.91 a week apart, 0.78 a month apart; −0.73 half a year apart, summer against winter; 0.88 a year apart.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_lag.svg">

<!--
**Say:** beyond two days the two hours stand at the same time of day. The dip at 12 hours is day against night.
**Ask:** a year apart r is 0.88 again: does the weather remember a whole year? No: the same season comes back.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Spread of the Ten Yearly **Means**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## 📅 **One mean per year**

- deviations from 7.16: +0.44, −0.65, +0.81, +0.11, −0.33, +0.09, −0.56, +1.15, +0.11, −1.18
- the sum of their squares: 4.451
- $s^2$ = 4.451 / 9 = 0.495, $s$ = **0.70 °C**

</div>

<img class="fig" src="/figures/viz_probability_year_means.svg">

</div>

<!--
**Say:** a year holds every season once, so the yearly means are free of the cycle that makes hours alike.
(~2 min)
-->

---
hideInToc: true
---

# The Standard Error from the Ten **Years**

$$
\frac{s_{\text{years}}}{\sqrt{10}} = \frac{0.70}{3.16} = 0.22\ ^\circ\mathrm{C}
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📅 **Ten nearly independent values**

One warm year says little about the next: s/√N holds for the ten yearly means.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚖️ **How many independent hours**

The 87 552 hours tell as much about the mean as about (8.85 / 0.22)² ≈ 1600 independent hours would.

</div>

</div>

<!--
**Say:** the same expression, s/√N, applied to values that are close to independent. 0.22 is the honest standard error of 7.16.
**If asked:** r of each year with the next is −0.41 over nine pairs: no sign that a warm year is followed by another.
(~3 min)
-->

---
hideInToc: true
---

# One Year's Own ± Is Too **Small**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📅 **2025, from its own 8760 hours**

$$
\frac{s}{\sqrt{N}} = \frac{9.70}{\sqrt{8760}} = 0.10\ ^\circ\mathrm{C}
$$

- 2025: 5.98 ± 0.10 °C
- each of the ten years: ± 0.09 to 0.11 °C

</div>

<div class="card card-warning card-glass pad-compact">

## 📊 **The ten years themselves**

They scatter by s = 0.70 °C: seven times the ± each year gives itself.

</div>

</div>

<div class="note-text mt-md">If the hours of a year were independent, the yearly means would scatter by about 0.1 °C.</div>

<!--
**Say:** a direct test of s/√N on the log: the formula promises 0.1 for one year, the years deliver 0.7.
(~2 min)
-->

---
hideInToc: true
---

# Writing a Result with Its **±**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 🚫 **As the program prints it**

7.1599655 ± 0.2223915 °C

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **As it is written**

7.16 ± 0.22 °C, the standard error of ten yearly means

</div>

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

📏 The ± to **two significant digits**: 0.2223915 → 0.22; 0.0299096 → 0.030

</div>

<div class="card card-secondary card-glass pad-compact">

📍 The value to the **same decimal place** as the ±: 7.16 ± 0.22, 7.160 ± 0.030

</div>

<div class="card card-accent card-glass pad-compact">

📝 The **unit** once, and **how the ±** was found

</div>

</div>

<!--
**Say:** digits beyond the ± are noise: 7.1599655 claims a precision of a ten-millionth of a degree.
(~1.5 min)
-->

---
hideInToc: true
---

# Which ± Belongs to **7.16**?

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| ± | What it is | For the mean of ten years |
|--|--|--|
| 8.85 °C | s, the spread of single hours | describes the hours |
| 0.70 °C | the spread of the yearly means | describes single years |
| 0.030 °C | s/√N, as if the hours were independent | too small |
| **0.22 °C** | **the spread of the years / √10** | **the standard error** |

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

✅ The opening question: 7.16 °C is typically within 0.2 °C of the station's long-run mean.

</div>

<!--
**Do:** go back to the counts on the board from the opening slide.
**Say:** all four numbers are right; each answers a different question. Only 0.22 says how well 7.16 is known.
**If asked:** ± two standard errors, 6.72 to 7.60 °C, would hold the long-run mean in 95 % of repetitions if s were known exactly; with s from only ten years, in about 92 %.
(~2 min)
-->

---
hideInToc: true
---

# How Sure Is 7.16? **Answered**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

1\. **Valid rows:** 120 hours of −999 left out and counted; read as numbers they give 5.78 instead of 7.16

</div>

<div class="card card-secondary card-glass pad-compact">

2\. **The hours:** two peaks, s = 8.85 °C, not Gaussian: 62.6 % within ± s

</div>

<div class="card card-accent card-glass pad-compact">

3\. **If independent:** s/√N = 8.85 / 295.9 = 0.030 °C

</div>

<div class="card card-warning card-glass pad-compact">

4\. **Not independent:** P(frost | frost the hour before) = 0.956; r of neighbouring hours 0.996

</div>

<div class="card card-success card-glass pad-compact">

5\. **Ten yearly means:** s = 0.70 °C, 0.70 / √10 = 0.22: **7.16 ± 0.22 °C**

</div>

</div>

<!--
**Say:** the chain of the lecture in five numbers. Each step needs the one before: no ± before the rows are valid, no s/√N before independence is checked.
(~2 min)
-->

---
hideInToc: true
---

# The Answer in the **README**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **`README.md`, the section “How sure is the mean”**

```text
7.16 ± 0.22 °C: the standard error of the ten yearly means, which
scatter by 0.70 °C. The hours are not independent, so
8.85 / √87 552 = 0.030 °C is too small. Left out: 120 hours of
-999, 22 to 26 July 2019. `scripts/how_sure.py` computes it.
```

</div>

<div class="note-text mt-md">The number, its ±, how the ± was found, and what was left out: a reader can check each.</div>

<!--
**Say:** four lines that answer the question of the lecture for anyone who opens the project.
(~1 min)
-->

---
hideInToc: true
---

# A **Checklist** for a Mean

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

✅ Is every **missing mark** declared, counted and left out, with the count in the README?

</div>

<div class="card card-secondary card-glass pad-compact">

✅ Is the **distribution** drawn: one peak or two, long tails or none?

</div>

<div class="card card-accent card-glass pad-compact">

✅ Are the values **independent**, or does each repeat its neighbour?

</div>

<div class="card card-info card-glass pad-compact">

✅ Does the **±** come from independent values: years, not hours?

</div>

<div class="card card-success card-glass pad-compact">

✅ Is the result written as **value ± standard error**, with how the ± was found?

</div>

</div>

<!--
**Say:** five questions for any mean in the project report. A "no" means the number is not finished.
(~1 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Check a table with **one rule per check**, and write each count down

</div>

<div class="card card-success card-glass pad-compact">

✅ Compute a **mean, variance and standard deviation** from their expressions, and a median

</div>

<div class="card card-success card-glass pad-compact">

✅ Count a **probability**, a **conditional probability**, and test independence

</div>

<div class="card card-success card-glass pad-compact">

✅ Use the **Gaussian** and its 68 / 95 / 99.7 %, and check whether data follow it

</div>

<div class="card card-success card-glass pad-compact">

✅ Compute the **correlation r** of two columns, and say what it does not see

</div>

<div class="card card-success card-glass pad-compact">

✅ Derive **s/√N**, and find an honest ± when values are not independent

</div>

</div>

<!--
**Say:** one card per section, each with its number from the log.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

More on the spread, on probability and on the ±, each with the same log: for time left at the end, or to read after the lecture.

<!--
**Say:** optional: each slide extends one of the main ideas with the same log.
(~0.5 min)
-->

---
hideInToc: true
---

# Most of the Spread Is the **Seasons**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ❄️ **Inside each half of the year**

- November to March: s = 4.378 °C
- April to October: s = 6.365 °C
- 0.4148 × 4.378² + 0.5852 × 6.365² = 31.66 °C²

</div>

<div class="card card-secondary card-glass pad-compact">

## ↔️ **Between the two halves**

- their means, −0.956 and 12.911 °C, around 7.160
- 0.4148 × (−0.956 − 7.160)² + 0.5852 × (12.911 − 7.160)² = 46.68 °C²

</div>

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

$$
31.66 + 46.68 = 78.34\ ^\circ\mathrm{C}^2 = s^2
$$

Six tenths of the variance of the hours is the difference between winter and summer.

</div>

<!--
**Say:** 0.4148 and 0.5852 are the shares of the hours in each half, 36 312 and 51 240 of 87 552. The variance of all hours is the variance inside the halves plus the variance of their means.
**Ask:** which share of the variance would vanish if the hours of one season only were used?
(~2 min)
-->

---
hideInToc: true
---

# Why **N − 1**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ✍️ **The derivation**

Write $x_i - \mu = (x_i - \bar{x}) + (\bar{x} - \mu)$, square and add; the mixed term is 0, since the deviations from $\bar{x}$ add up to 0:

$$
\sum_i (x_i - \bar{x})^2 = \sum_i (x_i - \mu)^2 - N(\bar{x} - \mu)^2
$$

On average: $N\sigma^2 - N \cdot \sigma^2/N = (N - 1)\,\sigma^2$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎲 **The check: five random hours, 100 000 times**

- $\sum (x_i - \bar{x})^2 / 5$ averages 62.7 °C²: four fifths of 78.3
- $\sum (x_i - \bar{x})^2 / 4$ averages 78.4 °C²

The deviations from $\bar{x}$ are a little too small: dividing by N − 1 makes up for it.

</div>

</div>

<!--
**Say:** x̄ is computed from the same values, so it sits closer to them than the long-run mean μ does. The term subtracted is N times the variance of the mean, σ²/N.
-->

---
hideInToc: true
---

# Three **Axioms**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | Axiom | With the hours of the log |
|--|--|--|
| 1 | $P(A) \ge 0$ | a count is never negative |
| 2 | $P(\text{all outcomes}) = 1$ | 87 552 of 87 552 hours |
| 3 | $P(A \text{ or } B) = P(A) + P(B)$, for A and B that never happen together | below 0 °C or 20 °C and above: 0.255 + 0.085 = 0.340 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ➖ **Derived: not A**

$$
P(\text{not } A) = 1 - P(A) = 1 - 0.255 = 0.745
$$

</div>

<div class="card card-accent card-glass pad-compact">

## ➕ **Derived: A or B, in general**

$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$: frost now or the hour before, 0.255 + 0.255 − 0.244 = 0.266; counted, 23 324 / 87 550 = 0.266

</div>

</div>

<!--
**Say:** every rule of probability follows from three axioms (Kolmogorov, 1933). The general "or" subtracts the hours counted twice.
(~2 min)
-->

---
hideInToc: true
---

# Bayes' **Rule**

$$
P(A \text{ and } B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A) \quad\Rightarrow\quad P(B \mid A) = \frac{P(A \mid B)\,P(B)}{P(A)}
$$

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **A: frost, B: January**

$$
P(\text{January} \mid \text{frost}) = \frac{0.8516 \times 0.0850}{0.2553} = 0.2835
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Counted**

$$
\frac{6336}{22\,352} = 0.2835
$$

Of the frost hours, 28 % fall in January.

</div>

</div>

<!--
**Say:** Bayes turns a conditional probability around: from frost given January, 0.852, to January given frost, 0.2835. The two differ because January is one month in twelve.
**If asked:** P(January) = 7440 / 87 552 = 0.085.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The **Binomial**: Frost Hours Among Ten

<div class="card card-primary card-glass pad-compact mt-sm">

🎲 $P(k) = \binom{n}{k} p^k (1 - p)^{n-k}$ with n = 10, p = 0.255: P(0) = 0.745¹⁰ = 0.053, P(2) = 45 × 0.255² × 0.745⁸ = 0.278. Ten hours drawn at random follow it; ten hours in a row do not.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_probability_binomial.svg">

<!--
**Say:** the binomial counts successes in n independent trials with the same p. 20 000 draws of 10 random hours match it; 10 hours in a row are all frost or none in 84 % of the draws.
**If asked:** C(10, 2) = 10 × 9 / 2 = 45, the number of ways to pick 2 hours of 10.
-->

---
hideInToc: true
class: fill
---

# The **Poisson**: Rare Hours

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🔥 **Hours of 30 °C or more**

- 86 of 87 552 hours
- among 1000 random hours: λ = 1000 × 86 / 87 552 = 0.982
- $P(k) = \dfrac{\lambda^k e^{-\lambda}}{k!}$
- P(0) = 0.374, P(1) = 0.368, P(2) = 0.181
- mean = variance = λ: a count k spreads by √k

</div>

<img class="fig" src="/figures/viz_probability_poisson.svg">

</div>

<!--
**Say:** the binomial with many trials and a small p becomes the Poisson. Drawn 20 000 times: 0.381, 0.363, 0.176.
**If asked:** per year the count is 5, 0, 13, 59, 0, 0, 0, 8, 0 and 1: a Poisson with mean 8.6 would give 0 in one year of 5400, not five of ten. Hot hours come in heat waves, not independently.
-->

---
hideInToc: true
---

# Error Propagation: Sums and **Factors**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **A factor: °C to °F**

$$
\sigma_F = 1.8\, \sigma_C
$$

7.16 ± 0.22 °C is 1.8 × 7.16 + 32 = 44.89 ± 0.40 °F.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➖ **A difference: 2023 against 2025**

$$
\sigma_{x - y} = \sqrt{\sigma_x^2 + \sigma_y^2}
$$

8.31 − 5.98 = 2.33 ± √(0.70² + 0.70²) = 2.33 ± 0.99 °C

</div>

</div>

<div class="note-text mt-md">2.33 is 2.4 standard errors, but 2023 and 2025 were picked as the warmest and the coldest of ten, after looking.</div>

<!--
**Say:** both rules come from the variance of a sum and the factor squared. A difference is uncertain by more than either value, never by less.
-->

---
hideInToc: true
---

# The ± from Means of Blocks, an Hour to a **Year**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Hours cut into blocks of | Blocks | Their means scatter by | Scatter / √blocks |
|--|--|--|--|
| 1 hour | 87 552 | 8.85 °C | 0.030 °C |
| 1 day | 3648 | 8.43 °C | 0.14 °C |
| 1 week | 521 | 8.27 °C | 0.36 °C |
| 30 days | 121 | 7.95 °C | 0.72 °C |
| 365 days | 9 | 0.59 °C | 0.20 °C |

</div>

<div class="note-text mt-md">Days and weeks scatter almost as much as hours: neighbours are alike. Months scatter by the seasons. A whole year holds every season once.</div>

<!--
**Say:** if the hours were independent, a block of 24 would scatter by 8.85 / √24 = 1.8 °C, not 8.43. Only blocks of a year leave the seasons out, and their ± is close to the 0.22 of the calendar years.
(~2 min)
-->

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
  question="A file holds four temperatures, 10.0, 12.0, −999 and 14.0 °C, where −999 marks a failed reading. What is the mean temperature?"
  :options="[
    '−240.75 °C',
    '12.0 °C',
    '9.0 °C',
    'It cannot be computed'
  ]"
  :correct="1"
  explanation="The mark is not a temperature: the mean is over the three readings, (10.0 + 12.0 + 14.0) / 3 = 12.0 °C. Read as a number, the mark gives (10.0 + 12.0 − 999 + 14.0) / 4 = −240.75 °C."
/>

---
hideInToc: true
---

<MCQ
  question="Three hours measure 2, 4 and 6 °C. What is their standard deviation s, dividing by N − 1?"
  :options="[
    '1.63 °C',
    '2 °C',
    '4 °C',
    '0 °C'
  ]"
  :correct="1"
  explanation="The mean is 4. The deviations are −2, 0 and +2, their squares 4, 0 and 4, which add up to 8. s² = 8 / (3 − 1) = 4 °C², so s = 2 °C. Dividing by N = 3 would give 1.63 °C."
/>

---
hideInToc: true
---

<MCQ
  question="Of 1000 evenings, 400 are clear, and 300 of the clear evenings are followed by frost. What is P(frost | clear evening)?"
  :options="[
    '0.30',
    '0.40',
    '0.75',
    '0.12'
  ]"
  :correct="2"
  explanation="Given a clear evening, only the 400 clear evenings are counted: 300 / 400 = 0.75. 0.30 is P(clear and frost) = 300 / 1000."
/>

---
hideInToc: true
---

<MCQ
  question="A Gaussian holds 68.3 % of its values within the mean ± s. The hours of the log hold 62.6 %. What does this say?"
  :options="[
    'The hours are Gaussian, within rounding',
    'The hours are not Gaussian: fewer lie near the mean, because they form two peaks',
    'The standard deviation was computed wrongly',
    'Every distribution holds 62.6 % within ± s'
  ]"
  :correct="1"
  explanation="The hours of the cold and the warm half of the year form two peaks with a dip at the mean. A Gaussian has one peak at its mean, so it holds more values near it. Checked on 87 552 hours, 62.6 % against 68.3 % is no rounding."
/>

---
hideInToc: true
---

<MCQ
  question="400 independent values have a standard deviation s = 6. What is the standard error of their mean?"
  :options="[
    '6',
    '0.3',
    '0.015',
    '1.5'
  ]"
  :correct="1"
  explanation="s / √N = 6 / √400 = 6 / 20 = 0.3. Four times as many values, 1600, would halve it to 0.15."
/>

---
hideInToc: true
---

<MCQ
  question="The 87 552 hours give s/√N = 0.030 °C, and the ten yearly means give 0.22 °C. Why is 0.030 too small?"
  :options="[
    'The hours are not independent: an hour nearly repeats the hour before',
    '87 552 hours are too few',
    'The yearly means were computed wrongly',
    'The standard deviation of the hours is too large'
  ]"
  :correct="0"
  explanation="s/√N assumes independent values. Neighbouring hours have r = 0.996 and P(frost | frost the hour before) = 0.956, so the hours repeat each other. The yearly means are close to independent, and their scatter, 0.70 / √10, gives the honest 0.22 °C."
/>

---
hideInToc: true
---

<MCQ
  question="The correlation of temperature and humidity over the hours of the log is r = −0.70. Which statement holds?"
  :options="[
    'Humid air makes the hours cold',
    'Warm hours tend to be drier, along a falling line; r alone does not say why',
    'There is no relation, since r is not −1',
    'Seventy per cent of the hours are dry'
  ]"
  :correct="1"
  explanation="r measures how closely two columns follow a straight line: −0.70 is a clear falling trend with scatter. It says nothing about cause; both columns follow the time of day and the season."
/>

---
hideInToc: true
---

<MCQ
  question="Two independent measurements have standard errors 0.3 and 0.4 °C. What is the standard error of their difference?"
  :options="[
    '0.1 °C',
    '0.5 °C',
    '0.7 °C',
    '0.35 °C'
  ]"
  :correct="1"
  explanation="For independent values the variances add, for a difference as for a sum: √(0.3² + 0.4²) = √0.25 = 0.5 °C."
/>
