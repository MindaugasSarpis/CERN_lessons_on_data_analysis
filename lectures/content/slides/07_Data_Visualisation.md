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
**Ask:** who has had to read a figure whose axes had no labels?
**Say:** pictures first: what a figure should show and how to choose it; then the few lines of Matplotlib that draw the figures of the start; then figures of more than two variables.
(~1 min)
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

# The Mean Temperature of Ten **Years**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`weather.csv`: one row per hour**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
...
2025-12-31T23:00,-11.3,100,4.2
```

87 672 rows; 120 hold −999 and are left out.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐍 **The mean of the measured hours**

```python
lines = open("data/raw/weather.csv").read().splitlines()
temps = []
for line in lines[1:]:
    temp = float(line.split(",")[1])   # temp_c
    if temp != -999:
        temps.append(temp)
print(len(temps), sum(temps) / len(temps))
```

```text
87552 7.15996550621345
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ Which whole degree (−1 to 0 °C, 0 to 1 °C, …) holds the most hours? 7 to 8 °C, where the mean lies?

</div>

<!--
**Say:** ten years of one weather station, hour by hour, and one number for all of it: 7.16 °C. The rest of the lecture looks at the hours themselves.
**Ask:** hands up for "yes, the most hours", hands up for "no". The histogram of the hours answers it.
**If asked:** the 120 hours of −999 are 22–26 July 2019, when the sensor failed; `lines[1:]` skips the header row.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Every Hour from 2016 to **2025**

<div class="card card-primary card-glass pad-compact mt-sm">

📈 87 552 hours, each at its time · coldest −16.3 °C, 7 January 2025 · warmest 32.4 °C, 18 June 2018

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_handson_hours_view.svg">

<!--
**Ask:** what can be read here that the mean, 7.16 °C, does not say?
**Say:** ten winters and ten summers: the cycle of the year, how far each winter and summer reach, and that no year looks very different from the others.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Same Hours Counted in Bins of 1 **°C**

<div class="card card-success card-glass pad-compact mt-sm">

📊 Two peaks, the cold months and the warm months, and the mean in the dip between them

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_handson_temp_view.svg">

<!--
**Ask:** the opening question: is 7 to 8 °C the fullest degree?
**Say:** no: it lies in the dip, with fewer hours than either peak, 3848 at −1 to 0 °C and 3032 at 11 to 12 °C. 92 % of the hours of the cold peak are from November to March, 96 % of the warm peak from April to October. The mean, 7.16 °C, falls between the cold months and the warm months and describes neither: Tukey's quote at the start.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Anscombe's **Quartet**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four tables of 11 points (Anscombe, 1973), the same in all four: mean of x 9.0 · mean of y 7.5 · line y = 3.00 + 0.50x

</div>

<div class="fig-fill mt-sm" v-click>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg">

<div class="note-text mt-sm text-center">Only the plot tells the four apart.</div>

</div>

<!--
**Do:** read the numbers first.
**Ask:** what do the four tables look like?
**Say:** after the click: a line with scatter, a curve, a line with one point off it, and ten points at one x with a single point that makes the whole slope. The mean 7.16 °C was one such number: it hid the two peaks.
**If asked:** each panel also prints r = 0.82: r says how near the points lie to a straight line, 1 on a rising line, −1 on a falling one, 0 with no trend. All four tables have the same r.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Mechanics of a **Figure**

Every number takes a channel, and the channels are not read equally well.

<!--
**Say:** the two plots of the weather log put every number on a position along an axis. The parts of a plot before the kinds of plot: which channel carries the number, what a legend is for, how the axes change what is read.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Visual **Channels**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Each variable takes one channel. Ten-year plot: time → position on x, temperature → position on y

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_aesthetic_mapping_common_aesthetics.svg">

<!--
**Say:** the channels: position on x or y, colour, shape, size, line width, line type. Every figure is a set of such choices; the ten-year plot used only the two positions.
**Ask:** which channel would show a third variable of that plot, the humidity?
(~1 min)
-->

---
hideInToc: true
---

# The Ranking of **Visual Channels**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Read most exactly first** (Cleveland and McGill, 1984)

| | Channel | Used in |
| --- | --- | --- |
| 1 | **Position** on a common scale | bar chart, scatter plot |
| 2 | **Position** on identical scales, side by side | small multiples |
| 3 | **Length** | the segments of a stacked bar |
| 4 | **Angle, slope, area** | pie chart, bubble chart |
| 5 | **Colour** hue and saturation | heatmap |

</div>

<div class="note-text mt-md">The most important variable goes on the best channel still free.</div>

<!--
**Say:** people were shown the same values in each channel and asked to read them: positions were read most exactly, colours least. The two figures of the start used the first channel only: a position on x and a position on y.
**If asked:** colour is for a third variable, or when position is taken.
(~1 min)
-->

---
title: The Parts of a Figure
hideInToc: true
class: fill
---

<div class="fig-fill anatomy-stack">
  <img src="/figures/viz_anatomy_stage1.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage2.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage3.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage4.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage5.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage6.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage7.svg" alt="">
</div>

<!--
**Do:** click six times, naming what each click adds: the points (pairs of a K⁻ and a π⁺ from LHCb, counted in bins of 3 MeV/c² of their mass; the first 1500 rows of the file), their error bars √n, the fitted curve with its two components and its result, the known D⁰ mass with the annotation, legend and title, the pulls (in the lower panel, empty until then), the names of the parts.
**Say:** each part answers a reader's question: what is measured, in which units, how sure, which model, and does it fit: every pull within ±2, χ²/ndf = 24.3/25. The top bin holds 95 pairs, so its bar is √95 = 9.7. The fit finds 334 ± 37 D⁰ decays at 1865.2 ± 0.9 MeV/c²; the known mass is 1864.84.
**If asked:** why 1500 rows of 91 583: with every row the top bin holds 5505 pairs and its bar, 74, is shorter than the marker.
(~3 min)
-->

<style>
.anatomy-stack { position: absolute; inset: 0; background: var(--bg); }
.anatomy-stack img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
</style>

---
hideInToc: true
---

# The **Legend**

<div class="card card-info card-glass pad-tight mt-sm">

## 🏷️ **Which colour, shape or size stands for what**

| | |
| --- | --- |
| **One line or one set of bars** | no legend: the axis labels say it |
| **Where** | on no data: an empty corner, or outside the axes |
| **What** | every colour, shape and size, each with a sample |
| **For a number** | a title and a unit, like an axis |

</div>

<!--
**Say:** a legend lists the colours, shapes and sizes of a plot and says which group or value each one stands for.
**Ask:** which of the four rules does a plot with one line need? None: it needs no legend.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A Legend Without **Samples**

<div class="card card-info card-glass pad-compact mt-sm">

📈 The economic growth of China and India, 2010 to 2014.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_legend_samples_bad.svg">

🚫 **Names without samples**: which line is which, in what unit?

</div>

<div v-click class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_legend_samples_good.svg">

✅ **A name at each line**, the unit on the axis

</div>

</div>

<!--
**Ask:** before the click: which line is which country, and in which unit?
**Say:** with two lines, a name at the end of each line needs no legend at all; the eye does not travel between the legend and the data.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Axis Labels with **Units**

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ The same curve: axes called `x` and `val`, then named with quantity and unit, `temperature (°C)`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_axes_labels_bad_good.svg">

<!--
**Ask:** what does the left plot measure, and in what? Nobody can say.
**Say:** a label names the quantity and its unit in round brackets: the time of day in hours, the temperature in °C.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Axis Labels: **Size**

<div class="fig-fill grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_too_small.svg">

🚫 **Sized for a printed page**: unreadable from 5 m

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_balanced.svg">

✅ **Sized for the room**: in proportion to the plot

</div>

</div>

<!--
**Do:** ask the back row to read the left labels.
**Say:** the same scatter plot with two font sizes; labels sized for a printed page cannot be read from the back of a lecture room.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Coordinate System**

<div class="card card-info card-glass pad-compact mt-sm">

🧭 Data that repeat (hours, days, bearings) on a circle: 360° meets 0°, three maxima 120° apart

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_polar_vs_cartesian.svg">

<!--
**Say:** the same 145 values twice: on a straight axis 0° and 360° lie at the two ends; on a circle the end meets the start and the pattern closes on itself.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Aspect Ratio**

<div class="card card-info card-glass pad-compact mt-sm">

📐 One series of 365 days, three shapes: tall makes slopes steep, wide makes them flat; best near 45°

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_houston_temps_aspect_ratios.svg">

<!--
**Ask:** in which of the three does the temperature look most dramatic? The tall one, with the same numbers.
**Say:** slopes are compared most accurately near 45° (Cleveland): here, the square plot.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Chart **Families**

What is compared decides the chart.

<!--
**Say:** position is read most accurately. Amounts, distributions, proportions, associations, trends, uncertainty: for each the usual chart, the usual mistake and its correction.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Long Labels on **Vertical Bars**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Rotated titles**

- Five films, opening-weekend gross
- Titles too long for narrow bars
- Rotated text is read slowly

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_rotated_bad.svg">

</div>

<!--
**Ask:** which film earned the second most? The eye has to tilt to read the titles.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Long Labels Level Under **Wider Bars**

<div class="card card-secondary card-glass pad-compact mt-sm">

📏 A chart as wide as the slide: each title level, on two lines. More films, and the room runs out again

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_amounts_boxoffice_wide.svg">

<!--
**Say:** first repair: give the bars more room, and the titles stand level.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Same Bars, **Horizontal**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 🎬 **One row per film**

- Any title level, on one line
- One film more adds a row, not width
- Sorted by value: the ranking

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_horizontal.svg">

</div>

<!--
**Say:** second repair: turn the chart. A title of any length fits, and a film more adds a row.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Bars That Do Not **Start at Zero**

<div class="fig-fill grid-side mt-sm">

<div v-click class="card card-warning card-glass pad-compact">

## ⚠️ **The axis starts at 48**

- Pass rates: 58.2 % down to 49.1 %
- Bars 10.2 and 1.1 long: 9 times
- Values: 1.19 times

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_bad.svg">

</div>


<!--
**Ask:** before the click: how many times better is the first school than the last?
**Say:** 10.2 / 1.1 is about 9, and 58.2 / 49.1 is 1.19.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Same Bars **from Zero**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Drag where the axis starts: the bars' ratio moves, the values' stays 1.19

</div>

<AxisStartBars class="fig-fill mt-sm" :start="48" />

<!--
**Do:** start at 48, as on the slide before, then drag to 0 while the room watches the first bar ÷ the last.
**Say:** a bar is read by its length, so its axis starts at zero; only then are the lengths 1.19 times apart, as the values are.
**If asked:** at 48 the bars are 10.2 and 1.1 units long, 9.27 times.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Median Income by **Age Group**

<div class="card card-info card-glass pad-compact mt-sm">

👥 Median household income by age, USA 2016, in thousand dollars. Age groups have an order of their own

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_amounts_income_by_value_bad.svg">

🚫 **Sorted by income**: the ages jump back and forth

</div>

<div v-click class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_amounts_income_by_age_good.svg">

✅ **In the order of age**: up to 45–54, then down

</div>

</div>

<!--
**Ask:** before the click: the films were sorted by value. Does the same rule fit here?
**Say:** age groups are **ordinal**: they have an order of their own. Sort by value only when the categories have none.
**Say:** in the order of age the shape is read at once: 42 thousand at 15–24, 77 at 45–54, 31 after 75. Sorted by income, the reader has to put the ages back in order first.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# **Stacked** Bars

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 📊 **Students per year, by programme**

- A bar is a total, a segment a part
- Totals, bottom segments: one baseline, read by position
- Upper segments: by length, less exact

</div>

<img class="fig" src="/figures/viz_amounts_students_stacked_bars.svg">

</div>

<!--
**Ask:** did the Master students grow from 2021 to 2024? Hard to say: their segments start at different heights.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Bars in **Three Dimensions**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Perspective**

- Sales: 61, 57, 63, 59, 60 thousand
- Bars at the back look smaller
- No bar top reads against the axis

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_3d_bad.svg">

</div>

<!--
**Ask:** which product sold most? 63 thousand, the third bar, which looks no taller than the others.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Same Bars in **Two Dimensions**

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

## ✅ **Flat bars, values written**

- One colour, no depth
- Read directly: 6 thousand apart at most

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_2d_fixed.svg">

</div>

<!--
**Say:** the depth added no information, only distortion; flat bars with their values answer at once.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Life Expectancy in **Alphabetical Order**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **26 countries, about 2019**

- The order says nothing about the values
- Highest, lowest, groups: searched for

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_alpha_order_bad.svg">

</div>

<!--
**Ask:** which countries live longest, and how many lie below 70 years? The eye has to visit every row.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Life Expectancy as **Sorted Bars**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Long bars, small differences**

- Every value 60 to 84 years
- The differences: the last 24 of 86 years

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_bars_bad.svg">

</div>

<!--
**Say:** the ranking is there, but the ink goes to the 60 years that every country shares. A bar must start at zero, so the bar is the wrong mark here.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Dot Plot**

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

## 🎯 **Position, not length** (Cleveland)

- No zero needed: the values fill the axis
- 13 countries at 81–84 years, 4 at 60–66

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_dot_plot.svg">

</div>

<!--
**Say:** the same 26 numbers, third try: dots in place of bars, on an axis from 58 to 86 years. Less ink than bars, and it stays readable for many categories.
**If asked:** values from the WHO Global Health Observatory, rounded to whole years; the order of the countries is real.
(~1 min)
-->


---
hideInToc: true
class: fill
---

# Bin Widths of 0.5, 5 and 20 **Years**

<div class="card card-info card-glass pad-compact mt-sm">

📏 The ages of the Titanic passengers in bins of 0.5, 5 and 20 years: whole years leave every other narrow bin nearly empty

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_distributions_i_titanic_hist_binwidth.svg">

<!--
**Say:** the bin width is a choice. With 0.5 years the bars jump between a few people and thirty, because ages are whole years; with 20 years the shape is four bars; 5 years shows it.
**Ask:** which width would you choose? 5 years: narrow enough for the shape, wider than the step of the data.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# **Density**: a Smoothed Histogram

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 📈 **Ages of 714 Titanic passengers**

- Each age a small bump, the bumps added up
- The bump width is chosen, like a bin width

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_density.svg">

</div>

<!--
**Say:** a density is drawn like a histogram, from the same values; it hides the bin edges and shows the shape.
**If asked:** the y-axis is scaled so that the area under the curve is 1; the width of the bumps is called the bandwidth.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Three Ways to Draw a **Distribution**

<div class="fig-fill grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_boxplot.svg">

📦 **Boxplot**: all hours, one block

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_violin.svg">

🎻 **Violin**: all hours, two peaks

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_strip.svg">

〰️ **Strip**: the hours as points

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

📐 The box: the middle half of the values. The line in it: the **median**, half of the values below, half above.

</div>

<!--
**Say:** the hourly temperatures of the weather log, the cold months, the warm months and all hours, drawn three ways. On all 87 552 hours the quartiles are −0.2, 6.7 and 14.2 °C: the box runs across both seasons and the dip between them, and nothing in it says two peaks. The violin, a density curve and its mirror image, has the two bumps of the histogram. The strip shifts each point sideways at random, so they do not cover each other.
**If asked:** a quarter of the values lie below the box (the first quartile), a quarter above it (the third); the box length is the interquartile range, IQR. The whiskers reach out to the values not unusually far from the box: a whisker ends at the last value within 1.5 × IQR of the box; values beyond it are drawn one by one.
**Ask:** which of the three charts shows that all hours are two seasons?
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Overlaid Densities: Lines or **Fill**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Petal length of three iris species

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_lines.svg">

🚫 **Lines and a legend**: followed one by one

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_filled.svg">

✅ **Fill and names**: each species an area

</div>

</div>

<!--
**Ask:** which species has the longest petals? On the left, follow a line to the legend; on the right, read the name.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Visualising **Proportions**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 The shares of six tools in a survey of 240 people, three ways

</div>

<div class="fig-fill grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_pie_bad.svg">

🥧 **Pie**: compared by angle

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_stacked_bar.svg">

📚 **Stacked bar**: compared by length

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_side_by_side_bars.svg">

📊 **Separate bars**: compared by position

</div>

</div>

<!--
**Ask:** which tool is used more, the second or the third? The pie hardly says; the separate bars do.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# When a **Pie Chart** Works

<div class="card card-info card-glass pad-compact mt-sm">

🥧 One whole, few parts, one share: the Bundestag of 1976, SPD and FDP 253 of 496 seats, 51 %

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_marketshare_pies_bad.svg">

🚫 **Three pies**: a share across the years cannot be followed

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_bundestag_pie_good.svg">

✅ **One pie**: just over half the circle

</div>

</div>

<!--
**Say:** a pie works for one whole with few parts, when the point is a share of that whole: three groups, one question, whether two parties together hold more than half.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Visualising **Associations**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 🔵 **The scatter plot**

- A point per penguin: bill length, bill depth
- Look for a trend, its spread, groups, lone points
- Colour adds a third variable: the species

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_scatter.svg">

</div>

<!--
**Ask:** what do you see first: the trend, the three groups, or a single point away from the rest?
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Bubble** Chart

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 🫧 **Body mass as the marker's area**

- A third number on the same scatter
- Area reads less exactly than position: size for what matters least
- The area grows with the value, not the radius

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_bubble.svg">

</div>

<!--
**Ask:** which penguins are heaviest? The big circles are found; how much heavier is hard to say.
**If asked:** with the radius proportional to the value, a value twice as large would look four times as large.
(~1 min)
-->


---
hideInToc: true
class: fill
---

# The **Pair** Plot

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 🔲 **Every pair of columns**

- Three penguin measurements
- A scatter plot for each pair
- Each column's histogram on the diagonal

</div>

<img class="fig" src="/figures/viz_multi_panel_correlogram.svg">

</div>

<!--
**Say:** a first look at a table with several numeric columns: three columns give three pairs, each drawn twice, mirrored across the diagonal.
**Ask:** which pair of measurements rises together most clearly? Bill length and flipper length.
(~1 min)
-->


---
hideInToc: true
class: fill
---

# When **Points Overlap**

<div class="card card-info card-glass pad-compact mt-sm">

🫧 3000 people, two answers from 0 to 10: plain points · shifted at random and transparent · counted per cell

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_no_3d_jitter_overplot_jitter_alpha.svg">

<!--
**Say:** the answers are whole numbers, so many points lie on top of each other: on the left, 3000 people stand on 91 points of the grid. Shifting each a little at random (jitter) and making it transparent shows where they pile up; cells coloured by their count show it as a number.
**Ask:** on the left, which pair of answers is the most common? It cannot be seen; on the right it is 5 and 5, 163 people.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Many Points: **Hexagonal Bins**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 20 000 flights: arrival delay against departure delay

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_points.svg">

🚫 **Points**: the centre is one solid area

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_hex_bins.svg">

✅ **Hexagonal bins**: the colour is the count per cell

</div>

</div>

<!--
**Say:** a histogram in two dimensions: the plane is cut into cells and each cell's count becomes a colour. The colour scale is logarithmic, because the centre holds hundreds of flights per cell and the edges one.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Visualising **Trends**

<div class="card card-info card-glass pad-compact mt-sm">

📉 The daily means of 2024–2025 and their running mean: drag the window from 1 to 61 days

</div>

<SmoothingWindow class="fig-fill mt-sm" :window="21" />

<!--
**Do:** start at 21 days, drag to 1 (the data alone), then to 61 (the season alone).
**Say:** grey is every day, cyan the mean over the window around each day. Both are drawn, so the reader sees what the smoothing removed.
**If asked:** every day runs from −13.0 to 24.1 °C; the mean over 21 days from −8.6 to 20.4 °C, over 61 days from −5.9 to 18.3 °C.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The **Slopegraph**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 📈 **Two dates, a line per country**

- CO₂ per person, 2000 and 2020, in tonnes
- The slope is the change
- USA 20.5 → 14.2, China 2.7 → 7.4

</div>

<img class="fig" src="/figures/viz_associations_co2_slopegraph.svg">

</div>

<!--
**Say:** one value per group at two dates, joined by a line: a change is read as a slope, and two lines that cross show the ranking changing.
**Ask:** which two countries swap places? Germany and Japan: 10.1 and 9.6 in 2000, 7.7 and 8.0 in 2020. China comes up close below them, at 7.4.
(~1 min)
-->


---
hideInToc: true
class: fill
---

# A Line Through Missing **Data**

<div class="card card-info card-glass pad-compact mt-sm">

🕳️ 19–29 July 2019, hour by hour. 22–26 July: 120 hours of −999

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_gap_bad.svg">

🚫 **Joined**: five days near 22 °C, invented

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_gap_good.svg">

✅ **A gap**: the missing hours stay missing

</div>

</div>

<!--
**Ask:** what was the weather on 24 July? Nobody knows: the line on the left is drawn, not measured.
**If asked:** a list without the −999 rows makes `ax.plot` join the hours on either side; with `float("nan")` in their place, Matplotlib leaves the gap.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Error Bars: a Mean ± Its **Standard Error**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 📏 **Standard error = standard deviation ÷ √*N***

- Standard deviation: the typical distance of a value from the mean
- 9 values, standard deviation 0.3&nbsp;°C: 0.3 / √9 = 0.1&nbsp;°C
- The bar: the mean ± 0.1 °C

</div>

<img class="fig" src="/figures/viz_uncertainty_error_bars.svg">

</div>

<!--
**Say:** five group means, each with a bar of ± one standard error. The more values behind a mean, the shorter its bar: √N divides.
**If asked:** with 36 values instead of 9, the same 0.3 °C gives 0.3 / √36 = 0.05 °C.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A Band or Many **Lines**

<div class="card card-info card-glass pad-compact mt-sm">

〰️ One straight line through 60 points, and how far it could move

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_ci_band.svg">

🎗️ **A band**: where the line could lie; wider, less certain

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_hop_demo.svg">

🎰 **Many lines**: they fan out where least certain

</div>

</div>

<!--
**Say:** error bars are the convention for measured points, a band suits a curve. The many lines are 28 possible lines, drawn together; they can be read without knowing what a standard error is.
**If asked:** the band: the straight line is redrawn for 400 copies of the data, each made of 60 points drawn from the 60 at random, with repeats; the band holds 95 % of these lines, and the many lines are 28 of them.
(~1 min)
-->

---
hideInToc: true
---

# Which **Chart** for Which Question

<div class="card card-info card-glass pad-tight mt-sm">

| What is compared | Chart |
| --- | --- |
| 📊 **Amounts** across categories | bar chart, dot plot |
| 📦 The **distribution** of one variable | histogram, density, boxplot |
| 🧩 **Parts** of a whole | separate bars, a stacked bar |
| 🔵 Two variables, their **association** | scatter plot |
| 📈 A **change** over time | line plot |
| 🌡️ A **value on a grid** of two variables | heatmap |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

🥧 **A pie** is read by angle, rank 4 of 5: only for one whole with few parts, as the Bundestag

</div>

<!--
**Say:** the table of this section in one slide; the question decides the chart. Bars show the same shares as a pie by position, the first rank.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Design **Principles**

Ink, colour and scale decide whether the comparison can still be read.

<!--
**Say:** the chart follows from what is compared; now how it is drawn: ink, colour, scales, panels.
(~0.5 min)
-->

---
hideInToc: true
---

# The **Data-Ink** Ratio

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **“Above all else show the data”** (Edward Tufte, 1983)

**Data-ink ratio** = the ink that shows data ÷ all the ink of the figure

| 🚫 Ink without data | ✅ What stays |
| --- | --- |
| 3D effects and shadows | the data |
| background fills and gradients | axes with a label and a unit |
| a heavy frame, a dense grid | a thin frame with ticks inside, as in a paper; a light grid, if values are read from it |
| a legend for a single series | the labels the reader needs |

</div>

<!--
**Say:** ink that can be erased without losing information is erased.
**Ask:** which ink in a plot drawn with the defaults shows no data?
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Same Scatter with **Less Ink**

<div class="card card-info card-glass pad-compact mt-sm">

✂️ The same 90 points. Right: no box, inner ticks, background or dense grid; every point and value kept

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_balance_data_context_grid_vs_no_grid.svg">

<!--
**Ask:** what is lost on the right? Nothing that carries a value.
(~1 min)
-->

---
hideInToc: true
---

# **Colour-Vision** Deficiency

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **About 8 % of men and 0.5 % of women: red and green hard to tell apart**

| | |
| --- | --- |
| ✅ **Use** | `viridis`, `cividis` for ordered values; Okabe–Ito for categories |
| 🚫 **Avoid** | red against green as the **only** difference |
| 🔲 **Add** | a second channel: marker shape, line type, a label |
| 🧪 **Check** | a simulator such as Color Oracle, or print in grey |

</div>

<!--
**Say:** they see colours differently, most of them with red and green hard to tell apart: among 20 men and 20 women, 1.7 people on average. In a room of 40, one or two see red and green alike.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Red and Green, **Simulated**

<div class="card card-warning card-glass pad-compact mt-sm">

👓 Two groups in red and green, then as seen with deuteranopia, the most common deficiency: one colour

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_pitfalls_of_color_use_red_green_cvd_sim.svg">

<!--
**Say:** with deuteranopia the two groups are one; a marker shape or a label would still tell them apart.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Palette Follows the Kind of **Variable**

<div class="fig-fill mt-md" style="display:grid; grid-template-columns: 1fr 2fr; grid-template-rows: repeat(3, minmax(0, 1fr)); align-items:center; column-gap: 1.5rem; row-gap: 1rem;">

<div>

🎨 **Qualitative**: categories without an order

</div>

<img class="fig" src="/figures/viz_color_palette_qualitative.svg" style="height:100%">

<div>

📈 **Sequential**: from low to high

</div>

<img class="fig" src="/figures/viz_color_palette_sequential.svg" style="height:100%">

<div>

⚖️ **Diverging**: below and above a midpoint

</div>

<img class="fig" src="/figures/viz_color_palette_diverging.svg" style="height:100%">

</div>

<!--
**Say:** the palette follows what is shown: names, an amount, or a distance from a midpoint.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Rainbow and **Viridis**

<div class="card card-info card-glass pad-compact mt-sm">

🌈 One grid in four palettes: the ten-year mean of every hour of every day; tap a cell to read it

</div>

<PaletteHeatmap class="fig-fill mt-sm" palette="jet" />

<!--
**Do:** start on the rainbow, then switch to viridis, the diverging palette and greys.
**Ask:** on the rainbow, where are the sharp edges? In the palette, not in the data: the yellow and cyan bands are steps of `jet`.
**Say:** in viridis and greys the lightness rises with the value; the diverging palette marks 0 °C.
**If asked:** 28 July at 15:00 is 25.3 °C, 15 January at 03:00 −7.9 °C.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Population growth of US states, 2010–2020: the three fastest in colour, the rest grey to compare

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_color_popgrowth_us_highlight.svg">

<!--
**Say:** colour for the one thing the figure is about, grey for the rest.
**If asked:** 2010 and 2020 census populations of the 30 most populous states; Utah grew by 18.4 %, Illinois shrank by 0.1 %.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Ten Lines or One in **Colour**

<div class="card card-info card-glass pad-compact mt-sm">

🍝 The daily means, one line per year, 2016–2025

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_spaghetti_bad.svg">

🚫 **Ten colours and a legend**: no year can be followed

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_highlight_good.svg">

✅ **Nine in grey, 2025 in colour**: read against the rest

</div>

</div>

<!--
**Say:** the rule of the highlighted states: colour for the one thing the figure is about, grey for the comparison.
**If asked:** January and February 2025 averaged −5.8 °C; the next coldest, 2017, −5.2 °C.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The **Logarithmic** Scale

<div class="card card-info card-glass pad-compact mt-sm">

📐 Citations of five papers: 5, 60, 540, 4900, 46 000. Linear: three in the lowest 2 %. Logarithmic: each step × 10, all five apart

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_proportional_ink_log_scale.svg">

<!--
**Say:** 540 / 50 000 = 1.1 %: on the linear axis, which runs to 50 000, the third paper sits at about a hundredth of its height. On the logarithmic axis 1, 10, 100, 1000 stand equally far apart, and each value is 9 to 12 times the one before, so the five are almost evenly spaced.
**If asked:** the values are dots, not bars: a bar would need a zero, and a logarithmic axis has none.
(~1 min)
-->

---
hideInToc: true
class: runner-side
---

# Linear or Logarithmic, **Live**

```py {monaco-run} {autorun:false}
import matplotlib.pyplot as plt
days = []
counts = []
for day in range(1, 60):           # 1, 2, ..., 59
    days.append(day)
    counts.append(5 * 1.2 ** day)  # 20 % more every day
SCALE = "linear"                   # <-- try "log"
fig, ax = plt.subplots(figsize=(5, 4.6),
                       layout="constrained")
ax.plot(days, counts, "o-", ms=3)
ax.set_yscale(SCALE)
ax.set(xlabel="day", ylabel="count")
ax.set_title("y-scale: " + SCALE)
plt.show()
```

<!--
**Do:** press ▶, then change `"linear"` to `"log"` and run again.
**Say:** on the logarithmic axis the growth is a straight line: every day multiplies the count by the same factor, 1.2.
**If asked:** `"o-"` draws a circle at each point and a line between them; `ms` is the marker size. `1.2 ** day` is 1.2 to the power `day`.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Six regions, a panel each, the same axes: one curve in colour, the other five grey

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_multi_panel_small_multiples_gapminder.svg">

<!--
**Say:** one panel per group, every panel with the same axes, so the eye compares by position. In a single panel six coloured curves would cover each other.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Small Multiples: a **Shared Axis**

<div class="card card-info card-glass pad-compact mt-sm">

🚢 Titanic survivors by class and sex: nearly all women of first class, about half of third

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_bad.svg">

🚫 **An axis per panel**: three panels alike

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_good.svg">

✅ **One axis, 0 to 1**: third class differs

</div>

</div>

<!--
**Ask:** before the right panel: do the three classes differ? On their own axes they look alike.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Two Y-Axes or Two **Panels**

<div class="card card-info card-glass pad-compact mt-sm">

📊 The monthly means of temperature and humidity

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_two_axes_bad.svg">

🚫 **Two y-axes**: crossings set by two ranges chosen by hand

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_two_axes_good.svg">

✅ **Two panels, one x-axis**: each on its own scale

</div>

</div>

<!--
**Ask:** in which months is the humidity above the temperature? The question has no meaning: the units differ, and `set_ylim(68, 90)` on the right axis alone moves the crossings.
**If asked:** over the twelve months the two move against each other, r = −0.99.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Stating the **Finding**

A correct figure can still be misread: say what it shows.

<!--
**Say:** a figure with little ink, a palette that fits and the right scale is correct, and the reader can still miss what it shows. Four means: the title, direct labels, an annotation, a reference line.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Title as the **Finding**

<div class="card card-info card-glass pad-compact mt-sm">

✍️ *Sales 2019–2025* describes the figure; *Sales doubled after 2022* states what it shows

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_story_titles_captions.svg">

📖 **Title, subtitle, caption**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_title_as_finding.svg">

✅ **A description and a finding** over the same plot

</div>

</div>

<!--
**Ask:** which title tells you what to look for?
**Say:** the second saves the reader the work.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Direct **Labels**

<div class="fig-fill grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_bad_legend.svg">

🚫 **A legend at the side**: four trips there and back

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_good_no_legend.svg">

✅ **A name at the end of each line**: no legend

</div>

</div>

<!--
**Say:** four lines and a legend: the reader looks from a line to the legend and back, four times. A legend makes the eye travel; a name at the line does not.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# **Annotations**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Active users over ten weeks, plain, then with an arrow at the week a feature was released

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_telling_a_story_annotated_vs_plain.svg">

<!--
**Say:** one arrow and one line of text answer the question the plain plot raises: the reader no longer has to guess why the curve rises there.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A **Reference** Line

<div class="card card-info card-glass pad-compact mt-sm">

🧬 Gene activity in a mutant against the normal type: most genes unchanged, on y&nbsp;=&nbsp;x

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_bad.svg">

🚫 **No reference**: where is “unchanged”?

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_good.svg">

✅ **The line y = x**: the genes off it changed

</div>

</div>

<!--
**Say:** the amount of mRNA of each gene in a mutant against the wild type, on logarithmic axes. Without the line the reader has to estimate where "unchanged" lies; with it, the genes off the line are the result, here also in a second colour. The mean line of the histogram at the start is a reference line too.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A Window Chosen for Its **Story**

<div class="card card-info card-glass pad-compact mt-sm">

✂️ The yearly means: the cold 2017 to the warm 2023, axis cut close, +1.8 °C; all ten years, no trend

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_window_bad.svg">

🚫 **Two ends picked, the axis cut**: a trend made by the choice

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_window_good.svg">

✅ **All the years, a reference line**

</div>

</div>

<!--
**Ask:** from 2023 to 2025, what would the same trick give? −2.3 °C in two years.
**Say:** choose the window before looking at the result, and show the whole series.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# A First **Plot**

The figures of the start, in a few lines of Matplotlib.

<!--
**Say:** now the code: the figures of the start, drawn from the list that the opening slide's loop reads, one call for each part. Every hour at its time, with dates on x, is in the reference section after the lecture.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Figure, Axes, **Artists**

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **Four steps to a figure**

- `import matplotlib.pyplot as plt`
- `fig, ax = plt.subplots()`: a **Figure**, the whole picture, and one **Axes**, a plot with two axes
- `ax.plot`, `ax.hist`, `ax.set_xlabel`: each call adds an **artist**
- `fig.savefig("results/month_means.png")`: the picture as a file

</div>

<div>

<img class="fig" src="/figures/viz_handson_figure_axes.svg">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📦 A conda-forge package: `conda install matplotlib-base=3.11`

</div>

<!--
**Say:** the Figure is the sheet, the Axes one plot on it, and everything drawn is an artist that a call on `ax` put there: `ax.plot` points or a line, `ax.hist` bars, `ax.set_xlabel` a text. `plt` is the short name the library is loaded under.
**If asked:** the twelve points are the monthly means of the ten years. Shorter calls such as `plt.plot(x, y)` draw into the figure made last; a call on `ax` names the axes it draws into.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Plot Every Hour: `ax.plot`

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1|3-8|10-11|12|all}
import matplotlib.pyplot as plt

text = open("data/raw/weather.csv").read()
values = []
for line in text.splitlines()[1:]:
    temp = float(line.split(",")[1])   # temp_c
    if temp != -999:
        values.append(temp)

fig, ax = plt.subplots()
ax.plot(values)
fig.savefig("results/every_hour.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

- `values`: 87 552 temperatures; the 120 hours of −999 are left out
- One list: drawn against its positions 0, 1, 2, …

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_hours_default.svg">

⚠️ **The output.** x counts list positions, not time; no axis says what it shows

</div>

</div>

<!--
**Say:** lines 3 to 8 are the opening slide's loop: every line after the header, its second column as a number, the hours of −999 left out. Ten summers and ten winters already show; the axes say nothing, not even a unit.
**Ask:** what can be read already, and what is missing?
**If asked:** after 2019-07-21T23:00 the next value is 2019-07-27T00:00: the 120 hours the sensor did not record are left out, so every later position is 120 hours early.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# A Histogram Counts Values in **Bins**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1|2|3|4|all}
# values: the list of 87 552 temperatures
fig, ax = plt.subplots()
ax.hist(values)
fig.savefig("results/temp_hist.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

10 equal bins from the smallest value to the largest, one bar per bin. The counts, which `ax.hist` returns:

```text
337  3173  12733  17255  13892
14619  13466  8797  2948  332
```

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_temp_default.svg">

⚠️ **The output.** −16.3 to 32.4 °C in 10 bins of 4.87 °C; the fullest, −1.69 to 3.18 °C, 17 255 hours

</div>

</div>

<!--
**Say:** one value is one hour, so there is nothing to plot it against: the question is how often each temperature occurs. `ax.hist` cuts the range into bins of equal width, counts the values in each and draws one bar per bin; the edges are −16.3, −11.43, …
**Ask:** where would you put the edges? On whole degrees.
**If asked:** (32.4 − (−16.3)) / 10 = 4.87.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Range and the **Bin Width**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

📏 **Range: −17 to 33 °C.** Every hour, −16.3 to 32.4, with edges on whole degrees

</div>

<div class="card card-secondary card-glass pad-compact">

📐 **Bin width.** Several of the station's tenths per bin, and enough hours that neighbours do not differ by chance

</div>

</div>

<img v-click class="fig fig-fill mt-sm" src="/figures/viz_handson_temp_binwidths.svg">

<div v-click class="card card-success card-glass pad-compact mt-sm">

✅ **1 °C per bin.** 10 °C: one hump · 1 °C: two peaks · 0.05 °C: 20 of 41 bins empty, every other one

</div>

<!--
**Ask:** before the figure: what will bins of 10 °C show?
**Say:** the station records tenths of a degree. Between 0 and 2 °C only 21 values occur, 0.0, 0.1, …, 2.0, so at 0.05 °C every other bin is empty. A bin narrower than the steps of the data counts the rounding, not the weather.
**If asked:** in ten years the station recorded 477 different values, every tenth of a degree that occurred.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Choose the Bin Width, **Live**

<div class="card card-info card-glass pad-compact mt-sm">

📊 Every hour from 2016 to 2025: drag the bin width from 10 °C down to 0.05 °C

</div>

<BinWidthExplorer class="fig-fill mt-sm" :bin="10" />

<!--
**Do:** drag from 10 °C to 1 °C, then to 0.05 °C, then press "0 to 2 °C".
**Ask:** at which width do the two peaks appear? At 1 °C. At 10 °C one hump; at 0.05 °C a comb.
**Say:** at 0.05 °C every other bin is empty: the station writes tenths, so the comb shows the rounding, not the weather.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# The Temperatures as a **Histogram**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|2|3-4|5|all}
fig, ax = plt.subplots()
ax.hist(values, bins=50, range=(-17, 33))
ax.set_xlabel("temperature (°C)")
ax.set_ylabel("hours per 1 °C")
fig.savefig("results/temp_hist.png", dpi=150)
```

<div class="card card-info card-glass pad-compact mt-sm">

- 50 bins, −17 to 33 °C: (33 − (−17)) / 50 = 1 °C each
- The y-label states the bin width

</div>

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_temp_hist.svg">

✅ **The output.** Peaks of 3848 and 3032 hours; 2706 at 7 to 8&nbsp;°C, the mean's degree

</div>

</div>

<!--
**Say:** the histogram of the start, made by five lines. Both choices came from numbers: the range holds every hour, and 1 °C shows the two peaks, at −1 to 0 °C and at 11 to 12 °C. A count per bin has no meaning without the bin width.
(~2 min)
-->

---
hideInToc: true
---

# Saving a **Figure**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧩 **Vector**: `.svg`, `.pdf`

Shapes: sharp at any size. Papers, posters, slides.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🖼️ **Raster**: `.png`

Pixels: inches × `dpi`. 6.4 × 4.8 in at `dpi=150`: 960 × 720. Web pages.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🔁 **Save SVG and PNG**

```python
fig.savefig("results/temp_hist.svg", bbox_inches="tight")
fig.savefig("results/temp_hist.png", dpi=150, bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 `bbox_inches="tight"` cuts the empty margin. Commit the script with its figures.

</div>

<!--
**Say:** SVG stores lines and text as shapes, PNG pixels: the size in inches times `dpi`, and 6.4 × 4.8 in is the default size. SVG for slides and papers, PNG for Markdown and the web; the script makes both again from the file. A figure that a script makes again from the data file can be checked and corrected.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Beyond Two **Axes**

A plane has two positions; colour, depth and time add one variable each.

<!--
**Say:** each of them is read less exactly than a position. Figures of three to five variables of the weather log: as colour, as lines, as depth, as panels, as time.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Day, Hour and Temperature as a **Heatmap**

<div class="card card-primary card-glass pad-compact mt-sm">

🌡️ The ten-year mean of each hour of each day: July afternoons 25.3 °C, January nights −7.9 °C

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_heatmap.svg">

<!--
**Say:** three variables on a plane: two positions and a colour, diverging at 0 °C. 366 × 24 cells, each the mean of 10 hours or fewer. Both cycles at once: the year from left to right, the day from bottom to top.
**Ask:** where is the day-night difference largest? In summer: a July day swings 10 °C, a January day 4 °C.
**If asked:** `ax.imshow(grid, aspect="auto", origin="lower", cmap="RdBu_r", vmin=-30, vmax=30)`; the grid comes from `weather.group(path, 5, 13)`: the key `07-28T15` is a day and an hour.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Same Grid as a **Surface**

<div class="card card-secondary card-glass pad-compact mt-sm">

⛰️ The same 8784 means as a landscape: the shape at once, but no value can be read off, and the far side is hidden

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_surface.svg">

<!--
**Say:** the same numbers as the heatmap, with the temperature as height too: a ridge of summer afternoons, a valley of winter nights, a daily ripple deeper in summer. A surface shows a shape; for values the flat heatmap is better, because perspective makes far values look smaller and hides some of them.
**If asked:** `ax = fig.add_subplot(projection="3d")`, then `ax.plot_surface(x, y, grid, cmap="RdBu_r")`; `ax.view_init(elev=32, azim=-42)` turns the view.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Temperature as Colour, Humidity as **Contour Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

🗺️ Lines of equal humidity, like heights on a map: 70 % around summer afternoons, above 90 % on January nights

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_contours.svg">

<!--
**Say:** two fields on one plane: the temperature as colour, the humidity as lines. Where the colour is warm the lines show dry air; humidity falls as the air warms, r = −0.81 over the 8784 cells.
**Ask:** at what time of day is the air driest? Mid-afternoon: in July 62.8 % at 15:00 against 81.3 % at 03:00, in January 78.0 % against 94.8 %.
**If asked:** `cs = ax.contour(x, y, hum, levels=[70, 80, 90])` and `ax.clabel(cs)`. Each cell is the mean of about 10 hours, too noisy for smooth lines, so the humidity is a running mean over 15 days before `contour` draws it. The driest cell, 20 June at 15:00, holds 61.5 %.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Year, Day, Hour and Temperature in **3D**

<div class="card card-secondary card-glass pad-compact mt-sm">

🧱 All 87 552 hours, a plane per year: each hides the one below, and the 120 missing hours of July 2019 cannot be found

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_slices.svg">

<!--
**Say:** three positions and a colour: year, day, hour and temperature, from 2016 to 2025.
**Ask:** which year had the warmest summer? The planes above cover the planes below, and perspective shrinks the far ones; the figure cannot answer.
**If asked:** `ax.plot_surface(x, y, z, facecolors=cmap(norm(grid)))` once per year: each plane is a flat surface at the height of its year, coloured cell by cell; a missing hour gets a transparent colour.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Same Hours as Ten **Panels**

<div class="card card-success card-glass pad-compact mt-sm">

🧩 The year as a panel, not a height: nothing hidden, one colour scale. In 2019 a dark line: 22–26 July, the missing hours

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_multiples.svg">

<!--
**Say:** small multiples again, the same four variables: when a third axis hides data, a row of flat panels usually shows it all.
**Ask:** which year was warmest? 2023, mean 8.31 °C; the coldest 2025, 5.98 °C. A colour difference of 2 °C is hard to see, so the number still goes into the text or a separate plot.
**If asked:** `fig, axs = plt.subplots(2, 5, sharex=True, sharey=True)`, one `imshow` per panel; `extent=(0, 365, 0, 24)` puts every year on the same axis, a leap year has one column more. The warmest hour, 32.4 °C, was 18 June 2018 at 15:00.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Temperature, Humidity, Wind and **Month**

<div class="card card-accent card-glass pad-compact mt-sm">

🧭 3648 days, the month as colour. Days below 0 °C: 86.5 %, 4.0 m/s; above 20 °C: 67.6 %, 2.8 m/s

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_scatter4d.svg">

<!--
**Say:** four variables in one figure: three positions, the daily means, and a colour. The groups are seen; single points are not read. Cold days are humid and windy on average, warm days dry and calm.
**Ask:** which pair of the three measurements moves together most? Temperature and humidity: r = −0.73.
**If asked:** `ax.scatter(temp, hum, wind, c=month)` on a 3D axes; the palette is cyclic, built from the course colours, so the year closes on itself.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Four-Variable Scatter, **Turning**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

## 🌀 **The same days: drag to turn**

- Still, the depth is guessed
- Turning, the points in front and behind move apart

</div>

<TurningScatter />

</div>

<!--
**Do:** drag the figure to turn it; stop where the points in front and behind move apart.
**Say:** motion is one more channel, for depth: points in front move one way, points behind the other. For a paper, pick the one view that shows the finding, or use flat panels.
**If asked:** `ax.view_init(elev=18, azim=-55)` sets the view; with `plt.show()` or in a notebook the mouse turns the figure, and `FuncAnimation` with `PillowWriter` writes a turning GIF.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Five Variables of Each Day: **Parallel Coordinates**

<div class="card card-accent card-glass pad-compact mt-sm">

🪢 3648 days, a line each across four axes. Level lines: warm days swing more. Crossing: warm days are dry

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_parallel.svg">

<!--
**Say:** any number of variables, each on its own vertical axis and scale, and the month as colour. The order of the axes decides which pairs can be compared: only neighbours. From daily range to temperature the lines run level (r = +0.82); from temperature to humidity they cross (r = −0.73).
**Ask:** what does a July day look like? A daily range of 10.4 °C on average, 71.9 % humidity, 2.89 m/s; a January day 4.9 °C, 86.8 %, 4.32 m/s.
**If asked:** `LineCollection` draws the 3648 lines in one call, `set_array(month)` colours them; drawn in a random order, so no month lies on top of the rest.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Time as One More Variable: an **Animation**

<div class="card card-success card-glass pad-compact mt-sm">

🎞️ Each month over the year's outline ÷ 12: −3.9 °C in January, 18.5 °C in July. Twelve bumps, two peaks

</div>

<MonthHistograms class="fig-fill mt-sm" />

<!--
**Do:** let the months step by; pause on July, then tap November: one wide bump, one narrow one near 0 °C.
**Say:** this answers why the year has two peaks: the months from November to March are narrow and pile up near 0 °C; April to October are wide, and where spring, summer and autumn overlap, near 11 to 12 °C, they make the second peak.
**If asked:** `FuncAnimation(fig, draw, frames=12)`: `draw(i)` sets the bar heights of month `i`; `ani.save("months.gif", writer=PillowWriter(fps=1.5))` writes the file. A video or a GIF goes on a slide or a web page, not into a printed paper.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Classics and **Maps**

Many variables on one page, each read where it is drawn

<!--
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Deaths in the Army in the East, 1854–56: **Nightingale's Roses**

<div class="card card-info card-glass pad-compact mt-sm">

🌹 A wedge per month, area = deaths: 17 982 deaths, 14 476 (80.5 %) from preventable disease. January 1855 alone: 2761

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_gallery_nightingale.svg">

<!--
**Say:** three variables in each rose: the month as the angle, the cause as colour, the deaths as area, each wedge measured from the centre. The radius grows with the square root: a wedge twice as long holds four times the deaths. First year, on the right: 13 294 deaths, 83.9 % from disease; second year, on the left: 4688.
**If asked:** Florence Nightingale, "Diagram of the causes of mortality in the army in the East", 1858. Data: `Nightingale` of the R package HistData (from Pearson and Short, 2007), as CSV from Rdatasets; GPL; the numbers are historical records. A Sanitary Commission reached the army in March 1855. The file also gives annual rates per 1000 soldiers: the army grew from 8571 (April 1854) to 46 140 (March 1856), so the rates fall further than the counts.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Napoleon's Army in Russia, 1812: **Minard's Map**

<div class="card card-warning card-glass pad-compact mt-sm">

🗺️ Band width = soldiers: 422 000 at Kaunas, 100 000 at Moscow, 10 000 back. Coldest: −30 °Réaumur (−37.5 °C), 6 December

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_gallery_minard.svg">

<!--
**Say:** six variables on one page: the size of the army as the band's width, longitude and latitude, the direction as colour (tan to Moscow, light grey back: Minard drew it black), and below, the temperature on the retreat with its date, joined to the map by thin lines. 422 000 become 10 000, one in 42; the cold of November and December falls on the way back.
**If asked:** Charles Joseph Minard, 1869; Edward Tufte called it perhaps the best statistical graphic ever drawn. Data: `Minard.troops`, `Minard.cities`, `Minard.temp` of the R package HistData (Lee Wilkinson's transcription), as CSV from Rdatasets; GPL; the numbers are historical records. Minard gave degrees Réaumur: × 1.25 for °C. The date 24 November is empty in the file and follows from its column of days (14 Nov + 10).
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Five Variables of 142 Countries: a **Bubble Chart**

<div class="card card-accent card-glass pad-compact mt-sm">

🫧 x: GDP per person (log scale) · y: life expectancy · area: population · colour: continent · motion: the year

</div>

<BubbleChart class="fig-fill mt-sm" />

<!--
**Do:** let it play from 1952 (about 20 s). Then drag the year to 1992 and tap Rwanda: 23.6 years. Tap Africa in the corner.
**Say:** two positions, an area, a colour and motion: five variables, each one readable. Hans Rosling's chart; data: Gapminder Foundation, CC BY 4.0.
**If asked:** between two data years the bubbles move on straight lines (income on the log scale); a still chart rests on a data year, and only there are the numbers shown.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Maunga Whau as a Surface and as a **Contour Map**

<div class="card card-success card-glass pad-compact mt-sm">

⛰️ 87 × 61 heights on a 10 m grid, 94 to 195 m · the same colour for a height in both views

</div>

<TurningSurface class="fig-fill mt-sm" />

<!--
**Do:** drag to turn and tilt; point at the crater beside the summit. Press MAP: the same heights lie flat, isolines every 10 m. Double-click resets the view.
**Say:** the surface shows the shape at a glance; the map lets you read a height, and close lines mean steep ground. Data: R's `volcano`, digitised by Ross Ihaka (GPL).
**If asked:** the surface draws heights twice their true scale, as R's own demo does, and says so under the figure; the map is to scale, with a 100 m bar.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# CERN's Accelerators to Scale and as a **Schematic**

<div class="card card-primary card-glass pad-compact mt-sm">

🧭 The LHC ring is 42 × the PS and 170 × the Booster: to scale, they are dots. The schematic keeps only the order and the four experiments

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_gallery_cern.svg">

<!--
**Say:** the same five machines twice. To scale, the PS, the Booster and Linac4 sit on the Meyrin site as one dot beside ATLAS. As a schematic, distances and shapes are dropped and the connections kept: Linac4, Booster, PS, SPS, then into the LHC beside ALICE and LHCb, where the two beams enter. Harry Beck's London Underground map of 1933 did the same for a city.
**If asked:** circumferences: LHC 26 659 m (home.cern, the LHC page); SPS 6.9 km, 11 × the PS (R. Steerenberg, "CERN's accelerator complex", CERN lecture, 27 Feb 2023; home.cern: "nearly 7 kilometres"); PS 628 m (home.cern, the PS page); Booster 157 m, four stacked rings, each a quarter of the PS (CERN's PS Booster operations page; Steerenberg 2023); Linac4 86 m long (home.cern, the Linac4 page). Places: the experiments from their published coordinates, the SPS and the Meyrin site estimated, to a few hundred metres.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# **Wrap-up**

A figure is finished when every choice in it has a number behind it.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# A **Checklist** for a Figure

<div class="card card-info card-glass pad-tight mt-sm">

## 🧪 **Before a figure goes into a report: a “no” means not finished**

| | |
| --- | --- |
| **Chart** | Does it fit what is compared? |
| **Axes** | A label and a unit on each; the scale stated: zero, logarithmic, bin width? |
| **Palette** | Does it fit the variable? Can it be read without colour? |
| **Title** | Does it state the finding? |
| **Script** | Kept with the figure, and does it make it again from the data? |

</div>

<!--
**Ask:** take the ten-year plot of the start through the five questions.
(~1 min)
-->

---
hideInToc: true
---

# Every Choice in the Two **Figures**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **Ten years, hour by hour**

<img class="fig mt-sm" src="/figures/viz_handson_hours_view.svg">

- Time as the position on x: each hour at its date
- A hairline: 87 552 values on one axis
- Each axis names its quantity and unit

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **The hours as a histogram**

<img class="fig mt-sm" src="/figures/viz_handson_temp_view.svg">

- −17 to 33 °C: every hour, edges on whole degrees
- 1 °C bins: two peaks; 10 °C one hump, 0.05 °C the rounding
- The y-label states the bin width: hours per 1 °C

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The default, 10 bins of 4.87 °C, hid the dip. Every choice comes from a number, kept in the script.

</div>

<!--
**Say:** the answer to the opening slide, in the room's own numbers. Each hour stands at its own time, so the hours after the gap of July 2019 keep their dates; the coldest hour is −16.3 °C, the warmest 32.4 °C.
**Ask:** point at each line: which slide did it come from?
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Draw lists with **Matplotlib**: `subplots`, `plot`, `hist`, labels with units, `savefig`

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose a histogram's **range and bin width**, and state the bin width on the axis

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **chart** for what is compared, also for more than two variables

</div>

<div class="card card-success card-glass pad-compact">

✅ Put the main variable on **position**, and start bars at zero

</div>

<div class="card card-success card-glass pad-compact">

✅ Remove **ink** that shows no data; choose a **palette** that fits the variable

</div>

<div class="card card-success card-glass pad-compact">

✅ State the **finding** in the title; keep the **script** with the figure

</div>

</div>

<!--
**Say:** one line per card, with the ten-year line and the histogram as the two examples for each.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

Figures with a little statistics, and the LHCb file: for time left, or to read later.

<!--
**Say:** optional, for the time left or for after the lecture: the empirical CDF, the correlation of every pair of columns, the square-root scale for counts, then the D⁰ file of LHCb as a 2D histogram and as a corner plot.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Empirical **CDF**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 📈 **The fraction of values ≤ *x***

- One step up per passenger
- No bin width to choose
- The median where it crosses 0.5: 28 years

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_ecdf.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Correlation** Heatmap

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## 🔥 **Seven columns of a table of cars**

- *r*: how near two columns lie to a straight line
- +1 rising, −1 falling, 0 no trend

</div>

<img class="fig" src="/figures/viz_associations_mtcars_corr_heatmap.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Square-Root** Scale

<div class="card card-info card-glass pad-compact mt-sm">

√ A count *N* scatters by about √*N*: 48 ± 7, 3 ± 1.7. A square-root axis draws the bars alike and keeps zero

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_sqrt_scale.svg">

<!--
**Say:** a count scatters by about √N from one repetition of a measurement to the next. A square-root axis spaces 0, 1, 4, 9, 16 evenly, so every error bar has about the same length; a count of zero stays on the axis, which a logarithmic axis cannot show.
**If asked:** the half unit in one line: √(N + √N) ≈ √N + ½; for N = 100, √110 = 10.49.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A 2D Histogram with Its **Projections**

<div class="card card-info card-glass pad-compact mt-sm">

⚛️ 90 753 K⁻π⁺ pairs: mass across, momentum up, count as colour. The D⁰: the band at 1865 MeV/c²

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_d0_hist2d.svg">

<!--
**Say:** the standard figure of a particle physics analysis: two variables as positions, their count as colour (log scale), and each variable alone on the side, so that nothing is hidden. The pairs shown have a transverse momentum from 2.5 to 9 GeV/c. `ax.hist2d(m, pt, norm=LogNorm())`.
**Ask:** why a logarithmic colour scale? The cells hold from 1 to 178 candidates; on a linear scale every cell with a few candidates, which is most cells of high momentum, would be the same dark colour.
**If asked:** a candidate is a K⁻ and a π⁺ whose combined mass is computed; those from a D⁰ decay have its mass, the others any. Almost none lie below 2500 MeV/c: the selection that made the file cut there. `plt.subplot_mosaic` lays out the three panels, and `sharex`, `sharey` tie their axes.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Four Columns of the LHCb File: a **Corner Plot**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

## ⚛️ **`M`, `PT`, `TAU`, `IPCHI2` of 91 534 candidates**

- Each pair a 2D histogram
- Each column alone on the diagonal
- The D⁰: the band at 1865 MeV/c² in `M`

</div>

<img class="fig" src="/figures/viz_advanced_corner.svg">

</div>

<!--
**Say:** the standard first look at a physics data set, `plt.subplots(4, 4)` with the upper triangle hidden: n columns give n(n − 1)/2 pairs, here six. It is the pair plot of the gallery with 2D histograms in place of points, because 91 534 points would cover each other.
**Ask:** which pair moves together? τ and log χ²_IP, r = 0.35: both grow when the D⁰ flies further from the collision before it decays. Every other pair has |r| ≤ 0.07.
**If asked:** 49 rows have `TAU` = −100, a missing value, and are left out. χ²_IP runs from 10⁻⁵ to 10⁶, so its axis is log₁₀. The horizontal edge at 0.15 ps in the τ panels is a cut of the selection that made the file.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# In **Matplotlib**

The figures of the weather log, call by call.

<!--
**Say:** reference for after the lecture: each figure with the lines that draw it.
(~0.5 min)
-->

---
hideInToc: true
---

# The Time of Each Hour: `weather.hours`

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
def temps(path):
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            result.append(temp)
    return result
```
```py {1,2,7,9}
def hours(path):
    times = []
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            times.append(datetime.fromisoformat(line[0:16]))
            result.append(temp)
    return times, result
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 🕐 **A time as an object**

```text
>>> from datetime import datetime
>>> datetime.fromisoformat("2016-01-01T00:00")
datetime.datetime(2016, 1, 1, 0, 0)
```

</div>

</div>

<div class="note-text mt-sm">In <code>weather.py</code>, beside <code>temps</code>, with <code>from datetime import datetime</code> at its top. <code>line[0:16]</code> is the time column. <code>hours</code> returns two lists of equal length; <code>times, values = weather.hours(path)</code> names both, as <code>fig, ax</code> does.</div>

<!--
**Do:** first step: `temps`, the opening slide's loop as a function; click: the four lines that change.
**Say:** `datetime` is in the standard library; a `datetime` object knows its year, month, day and hour, and Matplotlib puts years on an axis of them.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Plot Every Hour at Its **Time**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1|3|4|5-6|all}
times, values = weather.hours("data/raw/weather.csv")
fig, ax = plt.subplots()
ax.plot(times, values, linewidth=0.2)
ax.set_xlabel("time")
ax.set_ylabel("temperature (°C)")
fig.savefig("results/every_hour.png", dpi=150)
```

<div class="card card-info card-glass pad-compact mt-sm">

- With two lists, `ax.plot(x, y)` puts each value at its own time
- `linewidth=0.2` draws a hairline: 87 552 values on one axis
- A label names the quantity and gives the unit in brackets
- `dpi=150` saves 150 pixels per inch: the default 6.4 × 4.8 in gives 960 × 720 pixels

</div>

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_hours_dates.svg">

✅ **The output.** Years on x, read from the `datetime` objects, and a unit on y. Winters reach −16.3 °C, summers 32.4 °C.

</div>

</div>

<!--
**Say:** five lines changed: the time on x, a hairline, two labels, the resolution. The figure is saved under the same name, so the old picture is replaced.
**If asked:** the 120 missing hours of July 2019 are now a straight piece five days long, too short to see at this width.
(~2 min)
-->

---
hideInToc: true
---

# The Temperatures of Each Year: `weather.group`

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
def group(path, start, stop):
    groups = {}
    for line in read_lines(path):
        temp = temp_of(line)
        if temp == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(temp)
    return groups
```
```py
by_year = weather.group("data/raw/weather.csv", 0, 4)
print(len(by_year))                # 10
print(list(by_year))               # ['2016', '2017', ..., '2025']
print(len(by_year["2019"]))        # 8640
print(weather.mean(by_year["2025"]))   # 5.982077625570776
```
````

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔑 **Keys of `2016-01-01T00:00`**

| `start, stop` | key | groups |
| --- | --- | --- |
| `0, 4` | `2016` | 10 years |
| `5, 7` | `01` | 12 months |
| `11, 13` | `00` | 24 hours |
| `0, 10` | `2016-01-01` | 3648 days |

</div>

</div>

<div class="note-text mt-sm">A <code>dict</code> of lists in <code>weather.py</code>: one list of temperatures per key, in the order the keys first occur. <code>key not in groups</code> is <code>True</code> the first time a key turns up; <code>for year in by_year</code> runs over the keys, and <code>list(by_year)</code> lists them.</div>

<!--
**Do:** first step: the function; click: what it gives for the years.
**Ask:** why 8640 hours in 2019, not 8760? The 120 missing hours of July.
**If asked:** 3653 days in ten years; the five days of July 2019 without a single measured hour have no key.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Hours Below 0 °C per Year: `ax.bar`

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1-6|8-9|10-14|all}
frost = []
for year in by_year:
    count = 0
    for temp in by_year[year]:
        if temp < 0:
            count = count + 1
    frost.append(count)

fig, ax = plt.subplots(figsize=(6, 3.2))
ax.bar(range(2016, 2026), frost, color="#56B4E9", width=0.7)
ax.set(xlabel="year", ylabel="hours below 0 °C", ylim=(0, 3000))
ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
fig.savefig("results/frost_hours.svg", bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_frost_bars.svg">

✅ **The output.** One colour, bars from zero, a grid on y only, no box. From 1845 hours in 2023 to 2677 in 2025.

</div>

</div>

<div class="note-text mt-sm"><code>range(2016, 2026)</code> puts the years on x as numbers, so Matplotlib chooses which to label. <code>figsize</code> is the size in inches. The four <code>ax.spines</code> are the lines of the box around the plot; <code>set_axisbelow(True)</code> draws the grid behind the bars.</div>

<!--
**Say:** a count has a true zero, so its bars start at zero; the years keep their own order.
**If asked:** 22 352 of the 87 552 hours were below 0 °C, a quarter.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Yearly Means and the Mean of All **Hours**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1-3|5-6|7-8|9-10|all}
year_means = []
for year in by_year:
    year_means.append(weather.mean(by_year[year]))

fig, ax = plt.subplots(figsize=(5.2, 3.6))
all_mean = weather.mean(weather.temps("data/raw/weather.csv"))
ax.axhline(all_mean, color="#D55E00", label="2016–2025: 7.16 °C")
ax.plot(list(by_year), year_means, "o",   # "o": a point each
        color="#56B4E9", label="one year")
ax.set(xlabel="year", ylabel="mean temperature (°C)", ylim=(5, 9))
ax.legend(loc="lower left")
fig.savefig("results/year_means.png", dpi=150)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_year_means.svg">

✅ **The output.** Ten points around the line: 2023 the warmest, 8.31 °C, 2025 the coldest, 5.98 °C.

</div>

</div>

<!--
**Say:** two calls on the same axes give two layers; each gets a `label`, and `ax.legend` collects them. The line is the reference: each year reads as warmer or colder than the ten-year mean.
**If asked:** `list(by_year)` is the ten keys of the dictionary, `"2016"` to `"2025"`, in the order of the file; `"o"` draws a point at each value and no line.
**Ask:** is it getting warmer? Ten points scatter by about 1 °C around 7.16, and the last year is the coldest: ten years do not say.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Monthly Means, Annotated

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1-4|6-7|8-10|11-13|all}
months = weather.group("data/raw/weather.csv", 5, 7)
month_means = []
for month in months:
    month_means.append(weather.mean(months[month]))

fig, ax = plt.subplots(figsize=(5.6, 3.6))
ax.plot(list(months), month_means, "o-", color="#56B4E9")
arrow = {"arrowstyle": "->", "color": "#D55E00"}
ax.annotate("July, 18.5 °C", xy=("07", month_means[6]), xytext=("09", 19.5),
            color="#D55E00", arrowprops=arrow)
ax.set(xlabel="month", ylabel="mean temperature (°C)", ylim=(-6, 22))
ax.set_title("July is 22.4 °C warmer than January")
fig.savefig("results/month_means.png", dpi=150)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_month_annotated.svg">

✅ **The output.** An annotation, axes with units, a title that states the finding: 18.53 − (−3.87) ≈ 22.4 °C.

</div>

</div>

<!--
**Say:** the parts of a figure from the Mechanics section, one call each. `annotate` writes a text at `xytext` and draws an arrow to `xy`; on this axis a month is named by its key, `"07"`.
**If asked:** `"o-"` draws a point at each value and joins the points by lines, which shows the order of the twelve months; `month_means[6]` is the seventh mean, July's.
(~2 min)
-->

---
hideInToc: true
---

# One **Style** for All Figures

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **`rcParams`: the defaults of Matplotlib**

Colours, fonts and line widths that would be repeated in every script are set once. `plt.rcParams.update({...})` at the top of a script changes the defaults for every figure made after it.

</div>

```python {all|1-5|7-14|all}
import matplotlib.pyplot as plt

OKABE_ITO = ["#000000", "#E69F00", "#56B4E9", "#009E73",
             "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

plt.rcParams.update({
    "font.family": ["Helvetica", "Arial", "DejaVu Sans"],
    "axes.prop_cycle": plt.cycler(color=OKABE_ITO),  # the colours of successive lines
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.axisbelow":    True,
    "savefig.dpi":       150,
    "savefig.bbox":      "tight",
})
```

<!--
**Say:** the eight Okabe–Ito colours stay distinct for the colour-blind. The style lives in one place, for example in `weather.py`, and every script that imports it draws alike.
(~1 min)
-->

---
hideInToc: true
class: runner-side
---

# The Bin Width in **Python**, Live

```py {monaco-run} {autorun:false}
import random, matplotlib.pyplot as plt
random.seed(7)                  # same numbers every run
values = []
for i in range(3000):           # 3000 times
    cold = random.gauss(-1, 4)  # an hour, Nov to Mar
    warm = random.gauss(13, 5)  # an hour, Apr to Oct
    values.append(round(cold, 1))  # tenths, as the
    values.append(round(warm, 1))  # station writes
BINS = 5                        # <-- try 5, 55, 1100
fig, ax = plt.subplots(figsize=(5, 4.6),
                       layout="constrained")
ax.hist(values, bins=BINS, range=(-20.025, 34.975))
ax.set_xlabel("temperature (°C)")
ax.set_ylabel("values per bin")
plt.show()
```

<!--
**Say:** the browser cannot read the file on the laptop, so `random.gauss(-1, 4)` draws a number near −1 with a spread of 4, and `random.gauss(13, 5)` one near 13: cold and warm months, 6000 values, rounded to tenths. `range(3000)` counts 0 to 2999, so the loop runs 3000 times.
**Do:** press ▶ with 5, then 55, then 1100: bins of 11 °C, 1 °C and 0.05 °C.
**Ask:** with 1100 bins, why is every other bar missing where the values are dense? The values are tenths, and a bin of 0.05 °C between two tenths stays empty, as on the slide before.
**If asked:** `plt.show()` draws the figure under the code; in a script on a laptop it opens a window.
**If asked:** the range starts at −20.025, half a narrow bin below −20, so every tenth lies in the middle of a bin and never on an edge, where rounding would decide its side.
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
  question="A column holds 20 000 values between 200 and 300, with a peak about 8 units wide. Which binning shows the shape of the peak?"
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
  question="The mean of ten years of hourly temperatures is 7.16 °C. With 1 °C bins, 3848 hours lie at −1 to 0 °C, 2706 at 7 to 8 °C and 3032 at 11 to 12 °C. What does this say about the mean?"
  :options="[
    'Most hours lie near 7 °C, since the mean is the most common value',
    'The hours fall into a cold and a warm part of the year, and the mean lies between them, where fewer hours are',
    'The histogram is wrong, since a mean lies under the highest bar',
    'Nothing: 1 °C bins are too narrow to show a shape'
  ]"
  :correct="1"
  explanation="A mean is the balance point of the values, not the most common one. The hours form two peaks, near −1 °C from November to March and near 12 °C from April to October, and their mean falls in the dip between them. Only the histogram shows it."
/>

---
hideInToc: true
---

<MCQ
  question="A sensor records tenths of a degree: 0.0, 0.1, 0.2, … A histogram of its values uses bins 0.05 °C wide. What does it show?"
  :options="[
    'A smoother shape than with 1 °C bins',
    'About every other bin empty, since no value lies between two tenths',
    'The same shape as with 1 °C bins, with more detail',
    'One bar per measurement'
  ]"
  :correct="1"
  explanation="From 0 to 2 °C the sensor can record 21 values, 0.0 to 2.0, and 40 bins of 0.05 °C cover that range: a bin with a value is followed by one without. The bars show the rounding of the sensor, not the weather."
/>

---
hideInToc: true
---

<MCQ
  question="A figure shows the days of the year across, the hours of the day up, and the mean temperature of each cell as a colour. How many variables does it show, and which is read least exactly?"
  :options="[
    'Two: the day and the hour',
    'Three; the temperature, because it is a colour',
    'Three; the day, because it runs along the longer axis',
    'Four, counting the colour bar'
  ]"
  :correct="1"
  explanation="Two positions and a colour: three variables. A colour is read less exactly than a position, so the temperature of one cell is the hardest to read. What the heatmap shows well is the pattern across many cells: warm summer afternoons, cold winter nights."
/>

---
hideInToc: true
---

<MCQ
  question="From the cold 2017 to the warm 2023 the yearly mean of the station rose by 1.8 °C. What should a figure of its yearly means show?"
  :options="[
    'Only 2017 to 2023, with the axis from 6.4 to 8.4 °C, so that the rise is clear',
    'All ten years, with the mean of all hours as a reference line',
    'Only 2023 to 2025, to balance the rise with a fall',
    'The two end years as two bars'
  ]"
  :correct="1"
  explanation="Two years picked for their values make any trend: 2017 to 2023 gives +1.8 °C, 2023 to 2025 gives −2.3 °C. All ten years against their mean show what the data hold: values that scatter by about 1 °C, and no trend to read."
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
  question="Nine measurements of a temperature have a standard deviation of 0.3 °C. What is the standard error of their mean?"
  :options="[
    '0.3 °C',
    '0.1 °C',
    '0.033 °C',
    '2.7 °C'
  ]"
  :correct="1"
  explanation="The standard error of a mean of N values is their standard deviation divided by √N: 0.3 °C / √9 = 0.1 °C. An error bar of ± one standard error on the mean is 0.2 °C long from end to end."
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
