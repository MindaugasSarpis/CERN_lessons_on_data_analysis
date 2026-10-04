---
layout: cover
title: "Data Visualisation"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Data Visualisation

##### <span class="aims-badge">🔧 tool-agnostic · 📁 data & files · ♻️ reproducibility</span>

##### Inspired by: C. O. Wilke, *Fundamentals of Data Visualization*

<!--
Speaker: ask who has had to read a figure whose axes had no labels. The lecture
has two parts: how a figure is made with Matplotlib, and how to decide what the
figure shows. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The greatest value of a picture is when it forces us to notice what we **never expected to see**.
John W. Tukey, *Exploratory Data Analysis* (1977)

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-info card-glass pad-compact">

🐍 Make a figure with **Matplotlib**: points with labelled axes, a histogram, a file in `results/`

</div>

<div class="card card-primary card-glass pad-compact">

📊 Choose the **chart type** for amounts, distributions, proportions, associations and trends

</div>

<div class="card card-secondary card-glass pad-compact">

👁️ Put the data on the most accurate **visual channel**: position before angle and area

</div>

<div class="card card-accent card-glass pad-compact">

🏷️ Label **axes** with units and choose the scale: from zero, logarithmic or square-root

</div>

<div class="card card-success card-glass pad-compact">

🎨 Remove **ink** that shows no data, and choose a palette that fits the variable

</div>

<div class="card card-warning card-glass pad-compact">

✍️ State the **finding** in the title, label directly, and keep the script that makes the figure

</div>

</div>

<!--
Speaker: six abilities. The first is new code, the other five are decisions
that hold for any plotting program. (~1 min)
-->

---
hideInToc: true
---

# What a **Figure** Is For

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 👁️ **Reading**

A column of 91 583 masses cannot be read. Its histogram is read in a few seconds: one peak on a flat background.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Finding**

A figure shows groups, trends, gaps and single points away from the rest. A mean and a standard deviation show none of these.

</div>

<div class="card card-accent card-glass pad-tight">

## 📢 **Reporting**

A reader looks at the figures before the text, and often at nothing else. The figure has to carry the result without the text.

</div>

<div class="card card-info card-glass pad-tight">

## ⚠️ **Checking**

The rules for an honest figure are the rules by which a misleading one is recognised: bars that do not start at zero, an axis without a unit.

</div>

</div>

<!--
Speaker: one sentence per card. The next slide is the second card in numbers.
(~1 min)
-->

---
hideInToc: true
---

# Anscombe's **Quartet**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four tables of 11 points (Anscombe, 1973). In each one the mean of x is 9.0, the mean of y is 7.5, and the closest straight line is y = 3.00 + 0.50x. Each has r = 0.82, where r measures how near the points lie to a straight line: 1 on a rising line, 0 with no trend. Only the plot tells the four apart.

</div>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg" style="display:block;margin:0 auto;max-height:350px;">

<!--
Speaker: read the four numbers first and ask what the data look like. Then the
panels: a line with scatter, a curve, a line with one point off it, and ten
points at one x with a single point that makes the whole slope. (~2 min)
-->

---
layout: section
hideInToc: true
---

# A First **Plot**

<!--
Speaker: Matplotlib from its first line, on the two files the room already has:
the pendulum table and the mass column of D0_KPi.csv. Run each slide live in
VS Code and open the saved picture beside the script. (~0.5 min)
-->

---
hideInToc: true
---

# Figure, Axes, **Artists**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **Matplotlib draws arrays**

- `import matplotlib.pyplot as plt` loads the library under the short name `plt`
- `fig, ax = plt.subplots()` makes a **Figure**, the whole picture, and one **Axes**, the region with an x-axis and a y-axis
- A call on `ax` adds an **artist**: `ax.plot` draws points or a line, `ax.hist` bars, `ax.set_xlabel` a text
- `fig.savefig("plot.png")` writes the picture to a file

</div>

<div>

<img class="fig" src="/figures/viz_handson_figure_axes.svg" style="display:block;margin:0 auto;max-height:290px;">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Matplotlib is a Python library, installed with `python -m pip install matplotlib`. Shorter calls such as `plt.plot(x, y)` exist and draw into the figure that was made last. A call on `ax` names the axes it draws into, which stays clear when a script makes several figures.

</div>

<!--
Speaker: three words for the rest of the lecture. The Figure is the sheet, the
Axes is one plot on it, and everything drawn is an artist that a call on ax put
there. NumPy holds the numbers, Matplotlib draws them. (~2 min)
-->

---
hideInToc: true
---

# A Plot in **Four Lines**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-2|4-7|9|10|11|all}
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/processed/pendulum.csv",
                  delimiter=",", skiprows=1)
length = data[:, 0]    # cm
t10 = data[:, 1]       # s

fig, ax = plt.subplots()
ax.plot(length, t10)
fig.savefig("results/pendulum_plot.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

Lines 2, 9, 10 and 11 are Matplotlib. `ax.plot(x, y)` takes two arrays of equal length and joins the points with straight lines. The ending of the file name sets the format.

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_pendulum_default.svg" style="display:block;margin:0 auto;max-height:250px;">

⚠️ **The output.** Nine measurements drawn as one line. No axis says what it shows or in which unit, and the axes begin just below the smallest values, 20 and 9.02.

</div>

</div>

<!--
Speaker: the table is the one cleaned by hand in Lecture 2: nine lengths in cm
and the time of 10 swings in s. np.loadtxt is from Lecture 7. Run the script and
open results/pendulum_plot.png in VS Code. Ask what is missing before the next
slide. (~2 min)
-->

---
hideInToc: true
---

# Points, Labels, **Units**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|2|3-4|5-6|7|all}
fig, ax = plt.subplots()
ax.plot(length, t10, "o")
ax.set_xlabel("length (cm)")
ax.set_ylabel("time of 10 swings (s)")
ax.set_xlim(0, 110)
ax.set_ylim(0, 22)
fig.savefig("results/pendulum_plot.png", dpi=150)
```

<div class="card card-info card-glass pad-compact mt-sm">

- `"o"` draws a circle at each point and no line. A line would claim values between the nine lengths
- A label names the quantity and gives the unit in brackets
- Both axes start at 0, so the bend shows: 5 times the length takes 2.2 times the time
- `dpi=150` saves 150 pixels per inch: 960 × 720 pixels

</div>

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_pendulum_points.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output.** Nine points, two axes with a name and a unit, both from zero.

</div>

</div>

<div class="note-text mt-sm"><code>ax.set(xlabel="length (cm)", xlim=(0, 110))</code> sets several of these in one call.</div>

<!--
Speaker: four changes, each one line. The figure is saved under the same name,
so the picture in VS Code changes when the script runs again. 20.01 / 9.02 is
2.22, and the square root of 5 is 2.24. (~2 min)
-->

---
hideInToc: true
---

# A Histogram Counts Values in **Bins**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-2|4|5|6|all}
m = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
               skiprows=1, usecols=0)

fig, ax = plt.subplots()
ax.hist(m)
fig.savefig("results/mass_hist.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

`m` holds the 91 583 values of column `M`: the mass of each K⁻π⁺ pair in MeV/c². `ax.hist(m)` cuts the range from the smallest to the largest value into 10 bins of equal width, counts the values in each bin and draws one bar per bin. `np.histogram(m)` returns the same counts:

```text
14575  69648  7359  0  0  0  0  0  0  1
```

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_mass_default.svg" style="display:block;margin:0 auto;max-height:250px;">

⚠️ **The output.** The values run from 1766.2 to 2453.7, so a bin is 68.7 MeV/c² wide. Three bars hold all rows but one, and the peak is inside the second bar.

</div>

</div>

<!--
Speaker: the second running example, the file from Lecture 2. One row is one
candidate, so there is nothing to plot against: the question is how often each
value occurs. np.histogram is from Lecture 7; ax.hist counts in the same way and
draws. Ask why the x-axis runs to 2450. (~2 min)
-->

---
hideInToc: true
---

# The Range and the **Bin Width**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

📏 **Range.** `((m > 1810) & (m < 1920)).sum()` gives 91 579. Four of the 91 583 values lie outside 1810 to 1920 MeV/c², and one of them, 2453.7, makes the default range six times as wide.

</div>

<div class="card card-secondary card-glass pad-compact">

📐 **Bin width.** The peak is 16 MeV/c² wide at half its height. A bin is several times narrower than that, and wide enough that neighbouring bins do not differ by chance.

</div>

</div>

<img class="fig" src="/figures/viz_handson_mass_binwidths.svg" style="display:block;margin:0.6rem auto 0;max-height:240px;">

<div class="card card-success card-glass pad-compact mt-sm">

✅ **2 MeV/c² per bin.** Eight bins lie across the peak. A bin of the flat part holds about 1460 values, and neighbouring bins differ by 4 %. With 0.2 per bin it holds 146, and neighbours differ by 10 %: more noise, and nothing new to see.

</div>

<!--
Speaker: two decisions, each with a number. The range comes from a mask and a
count. The width comes from the feature to be shown: with 10 per bin the peak is
one bar with a step on each side, with 0.2 per bin it is 80 bars that jump.
(~3 min)
-->

---
hideInToc: true
---

# The Mass Column as a **Histogram**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|2|3-4|5|all}
fig, ax = plt.subplots()
ax.hist(m, bins=55, range=(1810, 1920))
ax.set_xlabel(r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)")
ax.set_ylabel(r"candidates per 2 MeV/$c^2$")
fig.savefig("results/mass_hist.png", dpi=150)
```

<div class="card card-info card-glass pad-compact mt-sm">

- 55 bins from 1810 to 1920: 110 / 55 = 2 MeV/c² per bin
- The y-label states the bin width. A count per bin has no meaning without it
- Text between `$` signs is set as a formula: `^` raises the next character and `\pi` is π. The `r` before the quote keeps the backslash as typed

</div>

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_mass_hist.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output.** A peak near 1865 MeV/c² on a flat background of about 1400 per bin. The tallest bin, 1862 to 1864, holds 3746 candidates.

</div>

</div>

<!--
Speaker: the same call with two more arguments, and two labels. The peak is the
D0 meson: pairs that come from its decay have its mass, 1865 MeV/c², and the
others have any mass in the window. The window itself, about 1815 to 1915, was
set when the file was made. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Mechanics of a **Figure**

<!--
Speaker: the parts of a plot before the kinds of plot: which channel carries
the number, what a legend is for, how the axes change what is read. (~0.5 min)
-->

---
hideInToc: true
---

# The Ranking of **Visual Channels**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Channels are not read equally well**

Cleveland and McGill (1984) asked people to judge quantities shown in different ways, and Heer and Bostock (2010) repeated the tests with more people. The list runs from the most to the least accurate channel. The most important variable gets the highest channel that is free.

</div>

<div class="stack-tight mt-md">

<div class="card card-success card-glass pad-compact">

🥇 **Position on a common scale**: bar chart, scatter plot

</div>

<div class="card card-primary card-glass pad-compact">

🥈 **Position on identical scales that are not aligned**: small multiples

</div>

<div class="card card-secondary card-glass pad-compact">

🥉 **Length**: the segments of a stacked bar

</div>

<div class="card card-accent card-glass pad-compact">

**Angle, slope, area**: pie chart, bubble chart

</div>

<div class="card card-warning card-glass pad-compact">

**Colour saturation and hue**: heatmap. For a third variable, or when position is taken

</div>

</div>

<!--
Speaker: the two plots of the last section used the first channel only: a
position on x and a position on y. (~1 min)
-->

---
hideInToc: true
---

# The Visual **Channels**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 A plot assigns each variable to one channel: position on x or y, colour, shape, size, line width, line type. In the pendulum plot the length is the position on x, the time the position on y.

</div>

<img class="fig" src="/figures/viz_aesthetic_mapping_common_aesthetics.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# The Parts of a **Figure**

<div class="anatomy-stack mt-md">
  <img src="/figures/viz_anatomy_stage1.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage2.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage3.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage4.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage5.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage6.svg" alt="">
</div>

<div class="note-text mt-sm">Example values. The bar on each point is the uncertainty of the count: ± √N for a count of N.</div>

<!--
Click through: frame → axes with units → the data → its uncertainty → the
annotation → the title that states the finding. An element that carries no
information is left out.
-->

<style>
.anatomy-stack { position: relative; max-width: 76%; margin-inline: auto; }
.anatomy-stack img { width: 100%; display: block; }
.anatomy-layer { position: absolute; inset: 0; }
</style>

---
hideInToc: true
---

# The **Legend**

<div class="card card-info card-glass pad-tight mt-sm">

## 🏷️ **What a legend does**

A legend lists the colours, shapes and sizes used in a plot and says which group or value each one stands for.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

📌 A plot with one line or one set of bars needs **no legend**. The axis labels say what it shows

</div>

<div class="card card-secondary card-glass pad-compact">

📍 The legend stands where it **covers no data**: in an empty corner, or outside the axes

</div>

<div class="card card-accent card-glass pad-compact">

🔑 It names **every** colour, shape and size of the plot, with a sample of each

</div>

<div class="card card-success card-glass pad-compact">

📏 A legend for a numeric variable has a **title and a unit**, like an axis

</div>

</div>

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ The legend names two countries and shows no sample of either line: nothing says which colour is which. The y-axis has no unit.

</div>

<img class="fig fig-light" src="/figures/data_vis_legend_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Three **Legends**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Fuel efficiency of cars against displacement. Colour is power, size is weight, shape is the number of cylinders. Each has a legend with a title, and all three stand in an empty corner.

</div>

<img class="fig fig-light" src="/figures/data_vis_legend_1.png" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# Axis Labels with **Units**

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ The same curve twice. On the left the axes are called `x` and `val`. On the right they name the quantity and its unit: the time of day in hours, the temperature in °C.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_axes_labels_bad_good.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Axis Labels: **Size**

<div class="card card-info card-glass pad-compact mt-sm">

🔍 The same scatter plot with two font sizes. Labels sized for a printed page cannot be read from the back of a lecture room.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_too_small.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Too small**: unreadable from 5 m

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_balanced.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Readable**: labels in proportion to the plot

</div>

</div>

---
hideInToc: true
---

# The **Coordinate System**

<div class="card card-info card-glass pad-compact mt-sm">

🧭 Data that repeat after a full turn can be drawn on a circle: days of a year, hours of a day, compass bearings. On the circle the three maxima are seen to lie 120° apart.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_polar_vs_cartesian.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# The **Aspect Ratio**

<div class="card card-info card-glass pad-compact mt-sm">

📐 One temperature series over 365 days (example values), drawn in three shapes. A tall, narrow plot makes the slopes steep, a wide plot makes them shallow. Slopes are compared most accurately when they lie near 45° (Cleveland).

</div>

<img class="fig" src="/figures/viz_coordinates_axes_houston_temps_aspect_ratios.svg" style="display:block;margin:0 auto;max-height:320px;">

---
layout: section
hideInToc: true
---

# Chart **Families**

<!--
Speaker: the families of charts: amounts, distributions, proportions,
associations, trends, uncertainty. For each one the usual chart, the usual
mistake and its correction. (~0.5 min)
-->

---
hideInToc: true
---

# Long Labels on **Vertical Bars**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Five films and their opening-weekend gross (invented titles). The titles do not fit under vertical bars and have to be rotated. Rotated text is read slowly.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_rotated_bad.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# The Same Bars, **Horizontal**

<div class="card card-info card-glass pad-compact mt-sm">

🎬 The same five values. The bars are horizontal, start at zero and are sorted by value. Every title is written horizontally, and the order of the bars is the ranking of the films.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_horizontal.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Bars That Do Not **Start at Zero**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Pass rates from 58.2 % down to 49.1 %. The axis starts at 48, so the first bar is 10.2 units long and the last 1.1: nine times as long, for a value 1.19 times as large.

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# The Same Bars **from Zero**

<div class="card card-success card-glass pad-compact mt-sm">

✅ The axis starts at zero. The length of each bar is proportional to its value, and the five schools are seen to differ by less than a fifth.

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Median income by age group, sorted by income. Age groups are **ordinal**: they have an order of their own, and sorting by value breaks it. Sort by value only when the categories have no order.

</div>

<img class="fig fig-light" src="/figures/data_vis_bar_chart_error_3.png" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# **Stacked** Bars

<div class="card card-info card-glass pad-compact mt-sm">

📊 A bar is a total and a segment a part of it. The totals and the bottom segments share a baseline and are compared by position. The upper segments are compared by length only, which is less accurate.

</div>

<img class="fig" src="/figures/viz_amounts_students_stacked_bars.svg" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# Bars in **Three Dimensions**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Sales of five products: 61, 57, 63, 59 and 60 thousand units. In perspective the bars at the back look smaller, and no bar top can be read against the axis.

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_3d_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# The Same Bars in **Two Dimensions**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Flat bars in one colour, with the value written on each. The five values are read directly. They differ by 6 thousand at most.

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_2d_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# The **Dot Plot**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 One dot per category on a common scale (Cleveland). Less ink than bars, and readable for many categories. A dot shows its value by position, not by a length, so its axis need not start at zero.

</div>

<img class="fig" src="/figures/viz_amounts_cleveland_dot_plot.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Life Expectancy — **Alphabetical Order**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Life expectancy in 20 countries (example values), listed alphabetically. The order of the rows says nothing about the values: the highest, the lowest and the spread have to be searched for.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_alpha_order_bad.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# Life Expectancy — **Sorted Bars**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Sorted, as bars from zero. All values lie between 60 and 82 years, so every bar is long, and the differences take up only the right-hand quarter of the plot.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_bars_bad.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# Life Expectancy — **Sorted Dots**

<div class="card card-success card-glass pad-compact mt-sm">

✅ The same values as dots, sorted, on an axis from 60 to 85 years. The differences now use the full width, and the ranking is read from top to bottom.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_dot_plot.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# **Density**: a Smoothed Histogram

<div class="card card-info card-glass pad-compact mt-sm">

📈 The ages of 714 passengers of the Titanic. A kernel density estimate replaces each value by a small bell-shaped bump and adds the bumps up. The y-axis is scaled so that the area under the curve is 1. The width of the bumps, the bandwidth, is chosen by the author, as a bin width is.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_density.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# One Dataset, Three **Bin Widths**

<div class="card card-info card-glass pad-compact mt-sm">

📏 The same ages with bins of 0.5, 5 and 20 years. With 0.5 years the bars jump between a few people and thirty. With 20 years the shape is four bars.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_hist_binwidth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Try It — **Bin Width**

```python {monaco-run} {autorun:false}
import numpy as np, matplotlib.pyplot as plt
rng = np.random.default_rng(7)   # random numbers, the same on every run
a = rng.normal(0, 1, 800)        # 800 values scattered around 0
b = rng.normal(4, 0.5, 300)      # 300 values scattered around 4
data = np.concatenate([a, b])
BINS = 30                        # <-- try 5, 30, 200
fig, ax = plt.subplots()
ax.hist(data, bins=BINS)
ax.set(xlabel="value", ylabel="count", title=f"bins = {BINS}")
plt.show()
```

<!--
Speaker: rng.normal(4, 0.5, 300) draws 300 random numbers that scatter around
4, most of them within 0.5 of it. With 5 bins the two groups merge, with 200
the bars jump. plt.show() draws the figure under the code. In a script on a
laptop it opens a window instead. (~2 min)
-->

---
hideInToc: true
---

# One Distribution, **Three Charts**

<div class="card card-info card-glass pad-compact mt-sm">

📦 The fuel economy of cars with 4, 6 and 8 cylinders, drawn three ways.

</div>

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_boxplot.svg" style="display:block;margin:0 auto;max-height:160px;">

📦 **Boxplot**: five numbers per group. It hides a second peak

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_violin.svg" style="display:block;margin:0 auto;max-height:160px;">

🎻 **Violin**: a density curve and its mirror image. It shows a second peak

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_strip_jitter.svg" style="display:block;margin:0 auto;max-height:160px;">

〰️ **Strip**: every value as a point, shifted sideways at random

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

📐 The **median** has half of the values below it. A quarter lie below the first **quartile** and three quarters below the third. The box runs from the first to the third quartile, and its length is the interquartile range (**IQR**). The line in the box is the median. A whisker ends at the last value within 1.5 × IQR of the box, and values beyond it are drawn one by one.

</div>

---
hideInToc: true
---

# The Empirical **CDF**

<div class="card card-info card-glass pad-compact mt-sm">

📈 The empirical cumulative distribution function: at each value *x* the curve gives the fraction of observations that are ≤ *x*. Every observation is one step up, and no bin width is chosen. The median is where the curve crosses 0.5, at 28 years for the Titanic passengers. The quartiles are where it crosses 0.25 and 0.75.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_ecdf.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# The **Ridgeline** Plot

<div class="card card-info card-glass pad-compact mt-sm">

🎢 One density curve per group, each shifted up by a fixed step. Here the temperatures of twelve months (synthetic): the peak moves to the right until July and back. On one baseline the curves would hide each other.

</div>

<img class="fig" src="/figures/viz_distributions_ii_ridgeline.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Overlaid Densities: Lines or **Fill**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Petal length of three iris species. Lines have to be followed one by one and matched to a legend. A transparent fill shows each group as an area, and a name on the area replaces the legend.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_lines.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Lines and a legend**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_filled.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Fill and direct labels**

</div>

</div>

---
hideInToc: true
---

# Temperatures as a **Heatmap**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ Six places by twelve months: 72 mean temperatures (example values). Colour stands for the value, on a sequential palette from dark for cold to light for warm. Whole rows are compared at once: Death Valley is the lightest row, Anchorage the darkest. A single value is read less accurately from a colour than from a position.

</div>

<img class="fig" src="/figures/viz_aesthetic_mapping_temp_normals_heatmap.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Visualising **Proportions**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧩 **One survey, three charts**

The shares of six tools in a survey of 240 people, as a pie, as one stacked bar and as separate bars. In the pie the shares are compared by angle. As separate bars they are compared by position on a common scale.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_pie_bad.svg" style="display:block;margin:0 auto;max-height:230px;">

🥧 **Pie**: compared by angle

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_stacked_bar.svg" style="display:block;margin:0 auto;max-height:230px;">

📚 **Stacked bar**: compared by length

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_side_by_side_bars.svg" style="display:block;margin:0 auto;max-height:230px;">

📊 **Separate bars**: compared by position

</div>

</div>

---
hideInToc: true
---

# When a **Pie Chart** Works

<div class="card card-info card-glass pad-compact mt-sm">

🥧 A pie works for one whole with few parts, when the point is a share of that whole. The German Bundestag of 1976 had 496 seats in three groups. SPD and FDP together held 253 of them, 51 %, and the pie shows them as slightly more than half the circle.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_marketshare_pies_bad.svg" style="display:block;margin:0 auto;max-height:240px;">

❌ **Three pies**: a share that changes from year to year cannot be followed across circles

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_bundestag_pie_good.svg" style="display:block;margin:0 auto;max-height:240px;">

✅ **One pie**: one whole, three parts, one share to read

</div>

</div>

---
hideInToc: true
---

# The **Treemap**

<div class="card card-info card-glass pad-compact mt-sm">

🗂️ For parts that have parts of their own. The area of a rectangle is proportional to its value, and the rectangles of one group share a colour. Here the 200 hours of a research month.

</div>

<img class="fig" src="/figures/viz_proportions_treemap.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Visualising **Associations**

<div class="card card-info card-glass pad-tight mt-sm">

## 🔵 **The scatter plot**

Each point is one observation with two measured values: here one penguin, with the length and the depth of its bill. Look for a trend, for the spread around it, for groups and for single points away from the rest. Colour adds a third variable, the species, and shows that the three groups are three species.

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_scatter.svg" style="display:block;margin:0 auto;max-height:310px;">

---
hideInToc: true
---

# The **Bubble** Chart

<div class="card card-info card-glass pad-compact mt-sm">

🫧 A third numeric variable as the size of the marker, here the body mass. Area is read less accurately than position, so size is for the variable that matters least. The area is proportional to the value, not the radius.

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_bubble.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# When **Points Overlap**

<div class="card card-info card-glass pad-tight mt-sm">

## 🫧 **Three ways to draw 3000 points**

Two answers on a scale from 0 to 10, from 3000 people (synthetic). The answers are whole numbers, so many points lie on top of each other. Left: plain points. Centre: each point shifted by a small random amount (jitter) and made transparent. Right: the plane cut into cells, coloured by the number of points in each.

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_overplot_jitter_alpha.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Many Points: **Hexagonal Bins**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 20 000 flights (synthetic): arrival delay against departure delay. Beyond about 10 000 points transparency no longer helps, because the centre of the cloud is solid. Hexagonal bins count the points in each cell and show the count as a colour: a histogram in two dimensions.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_points.svg" style="display:block;margin:0 auto;max-height:240px;">

🚫 **Points**: the centre is one solid area

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_hex_bins.svg" style="display:block;margin:0 auto;max-height:240px;">

✅ **Hexagonal bins**: colour is the number of flights per cell

</div>

</div>

---
hideInToc: true
---

# The **Correlation** Heatmap

<div class="card card-info card-glass pad-compact mt-sm">

🔥 The correlation coefficient *r* of two columns is a number from −1 to +1: +1 when the points lie on a rising straight line, −1 on a falling one, 0 with no straight-line trend. The heatmap shows *r* for every pair among seven columns of a table of cars, on a diverging palette centred at 0.

</div>

<img class="fig" src="/figures/viz_associations_mtcars_corr_heatmap.svg" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# The **Pair** Plot

<div class="card card-info card-glass pad-compact mt-sm">

🔲 Every pair of columns as a scatter plot, with the histogram of each column on the diagonal. Here three measurements of penguins. It is a first look at a table with several numeric columns.

</div>

<img class="fig" src="/figures/viz_multi_panel_correlogram.svg" style="display:block;margin:0 auto;max-height:390px;">

---
hideInToc: true
---

# The **Slopegraph**

<div class="card card-info card-glass pad-compact mt-sm">

📈 One value per group at two dates, joined by a line. Here tonnes of CO₂ per person in 2000 and 2020 (approximate). The slope is the change: the USA falls from 20.5 to 14.2, China rises from 2.7 to 7.4.

</div>

<img class="fig" src="/figures/viz_associations_co2_slopegraph.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Trends**

<div class="card card-info card-glass pad-tight mt-sm">

## 📉 **The data and the trend together**

Daily temperatures (synthetic) as a thin grey line, and their mean over 21 days as a thick one. Both are drawn, so the reader sees what the smoothing removed.

</div>

<img class="fig" src="/figures/viz_trends_lincoln_temps_raw_smooth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Trend and **Seasonal Cycle**

<div class="card card-info card-glass pad-compact mt-sm">

🔬 A series shaped like the CO₂ record of Mauna Loa (synthetic). Top: the series. Middle: its slow rise, the trend. Bottom: what remains, a yearly cycle and noise.

</div>

<img class="fig" src="/figures/viz_trends_keeling_decomposition.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Uncertainty**

<div class="card card-info card-glass pad-compact mt-sm">

📏 A measured or estimated value has an uncertainty. Three ways to draw it.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_error_bars.svg" style="display:block;margin:0 auto;max-height:140px;">

📏 **Error bars**: a mean ± its standard error, which is the standard deviation of the *N* values divided by √*N*

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_ci_band.svg" style="display:block;margin:0 auto;max-height:140px;">

🎗️ **Band**: the closest straight line, redrawn for 400 resampled copies of the data. The band holds 95 % of the lines

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_hop_demo.svg" style="display:block;margin:0 auto;max-height:140px;">

🎰 **Many lines**: 28 such lines drawn one by one. Their spread is the uncertainty of the line

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 Error bars are the convention for measured points, and a band suits a curve. Many lines can be read without knowing what a standard error is.

</div>

<!--
Speaker: the standard deviation is np.std from Lecture 7. Nine timings with a
standard deviation of 0.3 s have a mean with a standard error of 0.3 / 3 =
0.1 s. A resampled copy draws N rows from the table at random, with repeats.
(~2 min)
-->

---
hideInToc: true
---

# Which **Chart** for Which Question

<div class="card card-info card-glass pad-compact mt-sm">

The chart follows from what is compared:

</div>

<div class="grid-2 mt-md gap-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

📊 **Amounts** across categories → bar chart or dot plot

</div>

<div class="card card-secondary card-glass pad-compact">

📈 **Change** over time → line plot

</div>

<div class="card card-accent card-glass pad-compact">

🔵 **Association** of two variables → scatter plot

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-compact">

📦 **Distribution** of one variable → histogram, density or boxplot

</div>

<div class="card card-success card-glass pad-compact">

🧩 **Parts of a whole** → stacked bar, or separate bars

</div>

<div class="card card-warning card-glass pad-compact">

🌡️ **A value on a grid** of two variables → heatmap

</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 🥧 **Pie charts**

A pie is read by angle and area, the fourth of the five ranks of channels. Bars show the same shares by position, the first rank. The exception is one whole with few parts, as in the Bundestag example.

</div>

---
layout: section
hideInToc: true
---

# Design **Principles**

<!--
Speaker: from which chart to how it is drawn: ink, colour, scales, panels.
(~0.5 min)
-->

---
hideInToc: true
---

# The **Data-Ink** Ratio

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **Edward Tufte, 1983**

> "Above all else show the data." The **data-ink ratio** is the ink that shows data divided by all the ink of the figure. Ink that can be erased without losing information is erased.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 🚫 **Ink without data**

- 3D effects and shadows
- Background fills and gradients
- A box around the plot and a dense grid
- A legend for a single series

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **What stays**

- The data
- Axes with a label and a unit
- A light grid, if values are read from it
- The labels and annotations the reader needs

</div>

</div>

<!--
Speaker: ask the room to name the ink that shows no data in the left panel of
the next slide. The defaults of plotting programs are a common source of it.
(~1 min)
-->

---
hideInToc: true
---

# The Same Scatter with **Less Ink**

<div class="card card-info card-glass pad-compact mt-sm">

✂️ The same 90 points twice. On the right the box, the inner ticks, the background and the dense grid are gone. No point and no axis value was removed.

</div>

<img class="fig" src="/figures/viz_balance_data_context_grid_vs_no_grid.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Colour-Vision** Deficiency

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **Who cannot tell red from green**

About 8 % of men and 0.5 % of women see colours differently, most of them with red and green hard to tell apart. Among 20 men and 20 women that is 1.7 people on average.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Palettes built for this: `viridis` and `cividis` for ordered values, Okabe–Ito for categories

</div>

<div class="card card-secondary card-glass pad-compact">

🚫 Red against green as the **only** difference between two groups

</div>

<div class="card card-accent card-glass pad-compact">

🔲 A **second channel** beside colour: marker shape, line type or a direct label

</div>

<div class="card card-warning card-glass pad-compact">

🧪 A **check**: view the figure through a simulator such as Color Oracle, or print it in grey

</div>

</div>

---
hideInToc: true
---

# Red and Green, **Simulated**

<div class="card card-warning card-glass pad-compact mt-sm">

👓 Left: two groups in red and green. Right: the same plot as seen with deuteranopia, the most common colour-vision deficiency. The two groups have one colour.

</div>

<img class="fig" src="/figures/viz_pitfalls_of_color_use_red_green_cvd_sim.svg" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# Three **Kinds of Palette**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 The palette follows the kind of variable: categories without an order, values from low to high, or values on both sides of a midpoint such as zero.

</div>

<div style="display:grid; grid-template-columns: 1fr 2fr; align-items:center; column-gap: 1.5rem; row-gap: 1rem; margin-top: 1.2rem;">

<div>

🎨 **Qualitative**: categories without an order

</div>

<img class="fig" src="/figures/viz_color_palette_qualitative.svg" style="width:100%;max-height:70px;">

<div>

📈 **Sequential**: from low to high

</div>

<img class="fig" src="/figures/viz_color_palette_sequential.svg" style="width:100%;max-height:70px;">

<div>

⚖️ **Diverging**: below and above a midpoint

</div>

<img class="fig" src="/figures/viz_color_palette_diverging.svg" style="width:100%;max-height:55px;">

</div>

---
hideInToc: true
---

# Rainbow and **Viridis**

<div class="card card-warning card-glass pad-compact mt-sm">

🌈 One field of values drawn with two palettes: `jet` on the left, `viridis` on the right.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_bad.svg" style="display:block;margin:0 auto;max-height:250px;">

🚫 **Rainbow**: sharp colour steps where the values change smoothly

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_fix.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **Viridis**: lightness rises with the value, also when printed in grey

</div>

</div>

---
hideInToc: true
---

# Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Population growth by state (example values). Three bars are in colour and carry their value, the others are grey. The reader finds the three first, and the grey bars remain as the comparison.

</div>

<img class="fig" src="/figures/viz_color_popgrowth_us_highlight.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# The **Logarithmic** Scale

<div class="card card-info card-glass pad-compact mt-sm">

📐 The citations of five papers: 5, 60, 540, 4900 and 46 000. On a linear axis the three smallest lie in the lowest 1 % of the axis. On a logarithmic axis equal distances are equal factors, and all five are apart. The values are drawn as dots: a bar would need a zero, and a logarithmic axis has none.

</div>

<img class="fig" src="/figures/viz_proportional_ink_log_scale.svg" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# Try It — **Which Scale?**

```python {monaco-run} {autorun:false}
import numpy as np, matplotlib.pyplot as plt
x = np.arange(1, 60)
y = 5 * np.exp(0.18 * x)       # exponential growth

SCALE = "linear"               # <-- try "log"
fig, ax = plt.subplots()
ax.plot(x, y, "o-", ms=3)
ax.set_yscale(SCALE)
ax.set(xlabel="x", ylabel="y", title=f"y-scale: {SCALE}")
plt.show()
```

<!--
Speaker: "o-" draws a circle at each point and a line between them, ms is the
marker size. On the logarithmic axis the exponential is a straight line: each
step in x multiplies y by the same factor, exp(0.18) = 1.20. (~2 min)
-->

---
hideInToc: true
---

# The **Square-Root** Scale

<div class="card card-info card-glass pad-compact mt-sm">

√ For counts. A count *N* scatters by about √*N* from one repetition of a measurement to the next: 100 ± 10, 2000 ± 45. On a square-root axis this scatter has the same length at every height, half a unit. A count of zero stays on the axis, which a logarithmic axis cannot show.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_sqrt_scale.svg" style="display:block;margin:0 auto;max-height:320px;">

<!--
Speaker: the half unit in one line. The square root of N + √N is about
√N + 1/2: for N = 100, the square root of 110 is 10.49. (~1 min)
-->

---
hideInToc: true
---

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Six regions, one panel each, all with the same axes (synthetic). In each panel one curve is in colour and the other five grey. In a single panel six coloured curves would cover each other.

</div>

<img class="fig" src="/figures/viz_multi_panel_small_multiples_gapminder.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# Small Multiples: a **Shared Axis**

<div class="card card-info card-glass pad-compact mt-sm">

🚢 The fraction of Titanic passengers who survived, by class and sex. With a y-axis of its own in each panel, the three panels look alike. With one axis from 0 to 1 the difference shows: nearly all women in first class survived, and about half of the women in third class.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_bad.svg" style="display:block;margin:0 auto;max-height:290px;">

🚫 **An axis per panel**: three panels that look alike

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_good.svg" style="display:block;margin:0 auto;max-height:290px;">

✅ **One shared axis**: third class is seen to differ

</div>

</div>

---
layout: section
hideInToc: true
---

# Stating the **Finding**

<!--
Speaker: a correct figure can still leave the reader to work out what it
shows. Four means: the title, direct labels, an annotation, a reference line.
(~0.5 min)
-->

---
hideInToc: true
---

# Title as the **Finding**

<div class="card card-info card-glass pad-compact mt-sm">

✍️ A title can describe the figure, *Sales 2019–2025*, or state what it shows, *Sales doubled after 2022*. The second saves the reader the work.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_story_titles_captions.svg" style="display:block;margin:0 auto;max-height:230px;">

📖 **Title, subtitle, caption**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_title_as_finding.svg" style="display:block;margin:0 auto;max-height:230px;">

✅ **A description and a finding** over the same plot

</div>

</div>

---
hideInToc: true
---

# Direct **Labels**

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ Four lines and a legend: the reader looks from a line to the legend and back, four times. With a name at the end of each line the legend is not needed.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_bad_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

🚫 **A legend at the side**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_good_no_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

✅ **Names at the ends of the lines**

</div>

</div>

---
hideInToc: true
---

# **Annotations**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 The number of active users over ten weeks, plain and with one annotation. The arrow marks the week in which a feature was released. The reader no longer has to guess why the curve rises there.

</div>

<img class="fig" src="/figures/viz_telling_a_story_annotated_vs_plain.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# A **Reference** Line

<div class="card card-info card-glass pad-compact mt-sm">

🧬 The abundance of mRNA in a mutant against the wild type, on logarithmic axes (synthetic). Most genes are unchanged and lie where y&nbsp;=&nbsp;x. Without that line the reader has to estimate it. With it, the genes off the line are the result, and here they also have a second colour.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_bad.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **No reference**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_good.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **The line y = x**: the points off it have changed

</div>

</div>

---
layout: section
hideInToc: true
---

# Hands-on **Matplotlib**

<!--
Speaker: back to code. Three scripts with their output, then one style for
all figures, then file formats. (~0.5 min)
-->

---
hideInToc: true
---

# A Minimal **Bar Chart**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1|3-4|6-9|11-15|all}
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [22, 25, 31, 28, 36]

fig, ax = plt.subplots(figsize=(6, 3.2))
ax.bar(days, sales, color="#56B4E9", width=0.7)
ax.set(xlabel="weekday", ylabel="sales (M USD)",
       ylim=(0, 40))

ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
fig.savefig("sales.svg", bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_bar_minimal.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output.** One colour, bars from zero, a grid on y only, no box

</div>

</div>

<div class="note-text mt-sm"><code>figsize</code> is the size in inches. The four <code>ax.spines</code> are the lines of the box around the plot. <code>set_axisbelow(True)</code> draws the grid behind the bars.</div>

---
hideInToc: true
---

# Points and a **Formula Curve**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-6|8-9|11-15|16-20|all}
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/processed/pendulum.csv",
                  delimiter=",", skiprows=1)
length, t10 = data[:, 0], data[:, 1]

L = np.linspace(0, 110, 200)      # 200 lengths, cm
formula = 10 * 2 * np.pi * np.sqrt(L / 100 / 9.81)

fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.plot(L, formula, color="#D55E00",
        label="formula, g = 9.81 m/s²")
ax.plot(length, t10, "o", color="#56B4E9",
        label="measured")
ax.set(xlabel="length (cm)",
       ylabel="time of 10 swings (s)",
       xlim=(0, 110), ylim=(0, 22))
ax.legend(frameon=False, loc="lower right")
fig.savefig("results/pendulum_curve.png", dpi=150)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_pendulum_curve.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output.** The curve is T = 2π√(L/g), times 10, at 200 lengths. The points are the nine measurements. No fit is made: g is put in as 9.81 m/s²

</div>

</div>

<!--
Speaker: two calls of ax.plot on the same axes give two layers. Each gets a
label, and ax.legend collects the labels. np.linspace and the arithmetic on a
whole array are from Lecture 7. L / 100 turns cm into m. (~2 min)
-->

---
hideInToc: true
---

# Counts with **Error Bars**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-8|10-12|13-16|17-21|all}
import numpy as np
import matplotlib.pyplot as plt

m = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
               skiprows=1, usecols=0)
counts, edges = np.histogram(m, bins=110,
                             range=(1810, 1920))
centres = (edges[:-1] + edges[1:]) / 2

fig, ax = plt.subplots(figsize=(5.6, 3.6))
ax.errorbar(centres, counts, yerr=np.sqrt(counts),
            fmt="o", ms=3, color="#56B4E9")
arrow = {"arrowstyle": "->", "color": "#D55E00"}
ax.annotate("$D^0$", xy=(1870, 1650),
            xytext=(1885, 1900), color="#D55E00",
            arrowprops=arrow)
ax.set(xlabel=r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)",
       ylabel=r"candidates per 1 MeV/$c^2$",
       ylim=(0, 2100))
ax.set_title(r"A peak at 1865 MeV/$c^2$")
fig.savefig("results/mass_peak.png", dpi=150)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_mass_errorbars.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output.** A count *N* scatters by about √*N* when the measurement is repeated. The bar on each point is ± √*N*: 1916 ± 44 at the top, about 700 ± 26 in the flat part

</div>

</div>

<!--
Speaker: the parts of the figure from the Mechanics section, one call each:
the data with its uncertainty (errorbar), the annotation (annotate: a text at
xytext and an arrow to xy), axes with units, a title that states the finding.
The counts come from np.histogram, with 1 MeV/c² per bin. (~2 min)
-->

---
hideInToc: true
---

# One **Style** for All Figures

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **`rcParams`: the defaults of Matplotlib**

Colours, fonts and line widths that would be repeated in every script are set once. `mpl.rcParams.update({...})` at the top of a script changes the defaults for every figure made after it.

</div>

```python {all|1-5|7-14|all}
import matplotlib as mpl

OKABE_ITO = ["#000000", "#E69F00", "#56B4E9", "#009E73",
             "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

mpl.rcParams.update({
    "font.family": ["Helvetica", "Arial", "DejaVu Sans"],
    "axes.prop_cycle": mpl.cycler(color=OKABE_ITO),  # the colours of successive lines
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.axisbelow":    True,
    "savefig.dpi":       150,
    "savefig.bbox":      "tight",
})
```

---
hideInToc: true
---

# Saving a **Figure**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧩 **Vector**: `.svg`, `.pdf`

`fig.savefig("fig.svg")` stores lines and text as shapes. The figure stays sharp at any size. For papers, posters and slides.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🖼️ **Raster**: `.png`

`fig.savefig("fig.png", dpi=150)` stores pixels: the size in inches times `dpi`. The default 6.4 × 4.8 in gives 960 × 720 pixels. For Markdown and web pages.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🔁 **One script, two files**

```python
for ext in ("svg", "png"):
    fig.savefig(f"results/mass_hist.{ext}", dpi=150, bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 `bbox_inches="tight"` cuts the empty margin. Keep the script next to the figures and commit all three: a figure that a script makes again from the data file can be checked and corrected.

</div>

---
layout: section
hideInToc: true
---

# **Wrap-up**

<!--
Speaker: a checklist, an exercise, the sources, the recap. (~0.5 min)
-->

---
hideInToc: true
---

# A **Checklist** for a Figure

<div class="card card-info card-glass pad-tight mt-sm">

## 🧪 **Before a figure goes into a report**

Five questions. A "no" means the figure is not finished.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Does the **chart type** fit what is compared: amounts, a distribution, parts, an association, a change?

</div>

<div class="card card-secondary card-glass pad-compact">

✅ Do the **axes** have a label and a unit, and is the scale stated: from zero, logarithmic, the bin width?

</div>

<div class="card card-accent card-glass pad-compact">

✅ Does the **palette** fit the kind of variable, and can the figure be read without colour?

</div>

<div class="card card-info card-glass pad-compact">

✅ Does the **title** or the caption state the finding?

</div>

<div class="card card-success card-glass pad-compact">

✅ Is the **script** kept with the figure, and does it make the figure again from the data file?

</div>

</div>

---
hideInToc: true
---

# Further **Reading**

<div class="card card-info card-glass pad-compact mt-sm">

📚 The sources of this lecture. Wilke's book is free online. Every Matplotlib call is documented at matplotlib.org, with a gallery of examples and their code.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📈 **C. O. Wilke**, *Fundamentals of Data Visualization*: clauswilke.com/dataviz

</div>

<div class="card card-secondary card-glass pad-compact">

📊 **W. S. Cleveland**, *The Elements of Graphing Data*: the ranking of visual channels

</div>

<div class="card card-accent card-glass pad-compact">

🎨 **A. Cairo**, *The Truthful Art*: charts and maps for a general reader

</div>

<div class="card card-info card-glass pad-compact">

📐 **E. R. Tufte**, *The Visual Display of Quantitative Information*: the data-ink ratio

</div>

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Make a figure with **Matplotlib**: `plt.subplots`, `ax.plot`, `ax.hist`, labels with units, `fig.savefig`

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **range and bin width** of a histogram, and state them on the axis

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **chart** for amounts, distributions, proportions, associations and trends

</div>

<div class="card card-success card-glass pad-compact">

✅ Put the main variable on **position**, and start bars at zero

</div>

<div class="card card-success card-glass pad-compact">

✅ Remove **ink** that shows no data, and choose a **palette** that fits the variable

</div>

<div class="card card-success card-glass pad-compact">

✅ State the **finding** in the title, and keep the **script** with the figure

</div>

</div>

<!--
Speaker: one line per card, with the pendulum plot and the mass histogram as
the two examples for each. (~1 min)
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
  question="Four tables give the same mean of x, the same mean of y, the same closest straight line and the same r. What comes before any of these numbers is used?"
  :options="[
    'Nothing: four numbers that agree describe the tables completely',
    'A plot of each table: the same numbers can come from a line, a curve or one far point',
    'More decimal places of the four numbers, until the tables differ',
    'The mean of the four tables, since they are equivalent'
  ]"
  :correct="1"
  explanation="This is Anscombe's quartet. The four tables share their means, their line y = 3.00 + 0.50x and r = 0.82, and they are a line with scatter, a curve, a line with one point off it, and a column of points with one far point. Only the plot shows which."
/>

---
hideInToc: true
---

<MCQ
  question="A script calls `ax.hist(v, bins=40, range=(100, 300))`. How wide is one bin?"
  :options="[
    '40 units',
    '2.5 units',
    '5 units',
    '200 units'
  ]"
  :correct="2"
  explanation="The range is 300 − 100 = 200 units wide and is cut into 40 bins of equal width: 200 / 40 = 5 units. Values of v outside 100 to 300 are not counted."
/>

---
hideInToc: true
---

<MCQ
  question="A column holds 20 000 values between 200 and 300, with a peak about 8 units wide. Which binning shows the peak?"
  :options="[
    '5 bins of 20 units',
    '50 bins of 2 units',
    '10 000 bins of 0.01 units',
    '10 bins between 0 and 1000'
  ]"
  :correct="1"
  explanation="With 2 units per bin the peak covers 4 bins, and a bin holds 400 values on average. Bins of 20 or of 100 units are wider than the peak, so it disappears inside one bar. With 0.01 units a bin holds 2 values on average, and the bars only show chance."
/>

---
hideInToc: true
---

<MCQ
  question="Two bars show the values 50 and 52. The value axis starts at 48. How does the second bar look next to the first?"
  :options="[
    '1.04 times as long, like the values',
    'Twice as long',
    '4 times as long',
    'Equally long'
  ]"
  :correct="1"
  explanation="The bars are drawn from 48, so their lengths are 50 − 48 = 2 and 52 − 48 = 4: the second is twice as long. The values differ by 4 %. A bar shows its value by its length, so its axis starts at zero."
/>

---
hideInToc: true
---

<MCQ
  question="Measured values run from 10 to 10 000 000 across categories. Which y-axis keeps the small and the large values apart?"
  :options="[
    'A linear axis from zero',
    'A logarithmic axis',
    'A linear axis that starts at 10',
    'An axis without tick labels'
  ]"
  :correct="1"
  explanation="The values span six factors of ten. On a linear axis everything below 100 000 lies in the lowest hundredth. On a logarithmic axis each factor of ten takes the same length."
/>

---
hideInToc: true
---

<MCQ
  question="Nine timings of a pendulum have a standard deviation of 0.3 s. What is the standard error of their mean?"
  :options="[
    '0.3 s',
    '0.1 s',
    '0.033 s',
    '2.7 s'
  ]"
  :correct="1"
  explanation="The standard error of a mean of N values is their standard deviation divided by √N: 0.3 s / √9 = 0.1 s. An error bar of ± one standard error on the mean is 0.2 s long from end to end."
/>

---
hideInToc: true
---

<MCQ
  question="A map shows how far the temperature of each region lies below or above the long-term mean, from −3 °C to +3 °C. Which palette fits?"
  :options="[
    'Qualitative: one unrelated colour per value',
    'Sequential: from light to dark',
    'Diverging: two hues that meet in a neutral colour at zero',
    'Rainbow: as many hues as possible'
  ]"
  :correct="2"
  explanation="The values lie on both sides of a midpoint, zero, and the sign matters. A diverging palette gives each side a hue and the midpoint a neutral colour. A sequential palette would show −3 and +3 as the two ends of one scale, with nothing to mark zero."
/>

---
hideInToc: true
---

<MCQ
  question="A figure is made with `figsize=(6, 4)` and saved with `dpi=200`. How many pixels does the PNG file have?"
  :options="[
    '600 × 400',
    '1200 × 800',
    '200 × 200',
    '6 × 4'
  ]"
  :correct="1"
  explanation="figsize is in inches and dpi is pixels per inch: 6 × 200 = 1200 pixels wide and 4 × 200 = 800 high. The same figure saved as SVG has no pixels and stays sharp at any size."
/>
