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
**Say:** pictures first, what a figure should show and how to choose it; then the code that makes it with Matplotlib; then figures of more than two variables.
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

## 📄 **`weather.csv`: a station's log, one row per hour**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
...
2025-12-31T23:00,-11.3,100,4.2
```

87 672 rows. The 120 hours of 22–26 July 2019 hold −999: the sensor failed, so they are left out.

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

❓ Count the hours in each whole degree: −1 to 0 °C, 0 to 1 °C, and so on. Is 7 to 8 °C, where the mean lies, the degree with the most hours?

</div>

<!--
**Say:** ten years of one weather station, hour by hour, and one number for all of it: 7.16 °C. The rest of the lecture looks at the hours themselves.
**Ask:** hands up for "yes, the most hours", hands up for "no". The histogram of the hours answers it.
**If asked:** the same steps are `weather.temps` and `weather.mean` of Lecture 5; `lines[1:]` skips the header row.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Every Hour from 2016 to **2025**

<div class="card card-primary card-glass pad-compact mt-sm">

📈 The 87 552 measured hours, each at its time: ten winters, ten summers. The coldest hour, −16.3 °C, was on 7 January 2025; the warmest, 32.4 °C, on 18 June 2018.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_handson_hours_view.svg">

<!--
**Ask:** what can be read here that the mean, 7.16 °C, does not say?
**Say:** the cycle of the year, how far each winter and summer reach, and that no year looks very different from the others.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Same Hours Counted in Bins of 1 **°C**

<div class="card card-success card-glass pad-compact mt-sm">

📊 Two peaks: 3848 hours at −1 to 0 °C, nine in ten of them from November to March; 3032 at 11 to 12 °C, nearly all from April to October. Between them, at 7 to 8 °C, 2706: the mean lies in the dip.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_handson_temp_view.svg">

<!--
**Ask:** the opening question: is 7 to 8 °C the fullest degree?
**Say:** no: it lies in the dip, with fewer hours than either peak. The mean, 7.16 °C, falls between the cold months and the warm months and describes neither: Tukey's quote at the start.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Anscombe's **Quartet**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four tables of 11 points (Anscombe, 1973). All four have the same mean of x, 9.0, the same mean of y, 7.5, and the same straight line through them, y = 3.00 + 0.50x. What do the four tables look like?

</div>

<div class="fig-fill mt-sm" v-click>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg">

<div class="note-text mt-sm text-center">Only the plot tells the four apart.</div>

</div>

<!--
**Do:** read the four numbers first.
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

The two plots of the weather log put every number on a position along an axis. Position is one channel among several, and the channels are not read equally well.

<!--
**Say:** the parts of a plot before the kinds of plot: which channel carries the number, what a legend is for, how the axes change what is read.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# The Visual **Channels**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 A plot assigns each variable to one channel: position on x or y, colour, shape, size, line width, line type. In the ten-year plot the time is the position on x, the temperature the position on y.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_aesthetic_mapping_common_aesthetics.svg">

<!--
**Say:** every figure is a set of such choices; the ten-year plot used only the two positions.
**Ask:** which channel would show a third variable of that plot, the humidity?
(~1 min)
-->

---
hideInToc: true
---

# The Ranking of **Visual Channels**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Measured accuracy, best first**

People were shown the same values in each channel and asked to read them (Cleveland and McGill, 1984): positions were read most exactly, colours least. The most important variable goes on the best channel still free.

</div>

<div class="stack-tight mt-md">

<div class="card card-success card-glass pad-compact">

1\. **Position on a common scale**: bar chart, scatter plot

</div>

<div class="card card-primary card-glass pad-compact">

2\. **Position on identical scales that are not aligned**: small multiples

</div>

<div class="card card-secondary card-glass pad-compact">

3\. **Length**: the segments of a stacked bar

</div>

<div class="card card-accent card-glass pad-compact">

4\. **Angle, slope, area**: pie chart, bubble chart

</div>

<div class="card card-warning card-glass pad-compact">

5\. **Colour saturation and hue**: heatmap. For a third variable, or when position is taken

</div>

</div>

<!--
**Say:** the two figures of the start used the first channel only: a position on x and a position on y.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Parts of a **Figure**

<div class="fig-fill anatomy-stack mt-sm">
  <img src="/figures/viz_anatomy_stage1.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage2.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage3.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage4.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage5.svg" alt="">
  <img v-click src="/figures/viz_anatomy_stage6.svg" alt="">
</div>

<div class="note-text mt-sm">The histogram of the 87 552 hours, one part per click: the frame, the axes with their units, the data, a reference line, an annotation, a title that states the finding.</div>

<!--
**Do:** click through: frame, axes with units, the data, the mean as a reference line, the annotation, the title that states the finding.
**Say:** an element that carries no information is left out.
(~2 min)
-->

<style>
.anatomy-stack { position: relative; }
.anatomy-stack img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; }
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

<!--
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

🚫 **Names without samples**: which line is which? In which unit?

</div>

<div v-click class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_legend_samples_good.svg">

✅ **A name at the end of each line**, and the unit on the axis

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

🏷️ The same curve twice. On the left the axes are called `x` and `val`. On the right they name the quantity and its unit: the time of day in hours, the temperature in °C.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_axes_labels_bad_good.svg">

<!--
**Ask:** what does the left plot measure, and in what? Nobody can say.
**Say:** a label names the quantity and its unit in round brackets: `temperature (°C)`.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Axis Labels: **Size**

<div class="card card-info card-glass pad-compact mt-sm">

🔍 The same scatter plot with two font sizes. Labels sized for a printed page cannot be read from the back of a lecture room.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_too_small.svg">

🚫 **Too small**: unreadable from 5 m

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_balanced.svg">

✅ **Readable**: labels in proportion to the plot

</div>

</div>

<!--
**Do:** ask the back row to read the left labels.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Coordinate System**

<div class="card card-info card-glass pad-compact mt-sm">

🧭 Data that repeat after a full turn can be drawn on a circle: days of a year, hours of a day, compass bearings. On the circle the end meets the start, 360° is 0°, and the pattern closes on itself: three maxima, 120° apart.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_polar_vs_cartesian.svg">

<!--
**Say:** the same 145 values twice: on a straight axis 0° and 360° lie at the two ends; on a circle they meet.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The **Aspect Ratio**

<div class="card card-info card-glass pad-compact mt-sm">

📐 One temperature series over 365 days (example values), drawn in three shapes. A tall, narrow plot makes the slopes steep, a wide one shallow. Slopes are compared most accurately near 45° (Cleveland): here, the square plot.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_houston_temps_aspect_ratios.svg">

<!--
**Ask:** in which of the three does the temperature look most dramatic? The tall one, with the same numbers.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Chart **Families**

Position is read most accurately. What is compared decides the chart: amounts, a distribution, parts of a whole, two variables, a change over time.

<!--
**Say:** amounts, distributions, proportions, associations, trends, uncertainty: for each the usual chart, the usual mistake and its correction.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Long Labels on **Vertical Bars**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

⚠️ Five films and their opening-weekend gross. The titles do not fit under vertical bars and have to be rotated. Rotated text is read slowly.

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

📏 The same five films on a chart as wide as the slide: each title has room under its bar, on two lines, and is read level. With more films or longer titles the room runs out again.

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

🎬 The same five values as horizontal bars: each title level on one line, however long, and one film more adds a row, not width. Sorted by value, the order of the bars is the ranking.

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

⚠️ Pass rates from 58.2 % down to 49.1 %. The axis starts at 48, so the first bar is 10.2 units long and the last 1.1: nine times as long, for a value 1.19 times as large.

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

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

✅ The axis starts at zero. The length of each bar is proportional to its value, and the five schools are seen to differ by less than a fifth.

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_fixed.svg">

</div>

<!--
**Say:** the same five rates as before; only the axis changed.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Median Income by **Age Group**

<div class="card card-info card-glass pad-compact mt-sm">

👥 Median household income by age of the householder, USA 2016, in thousand dollars. Age groups are **ordinal**: they have an order of their own. Sort by value only when the categories have none.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_amounts_income_by_value_bad.svg">

🚫 **Sorted by income**: the ages jump back and forth

</div>

<div v-click class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_amounts_income_by_age_good.svg">

✅ **In the order of age**: the income rises to 45–54, then falls

</div>

</div>

<!--
**Ask:** before the click: the films were sorted by value. Does the same rule fit here?
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

📊 Students enrolled per year, split by programme: a bar is a total and a segment a part of it. The totals and the bottom segments share a baseline and are compared by position. The upper segments are compared by length only, which is less accurate.

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

⚠️ Sales of five products: 61, 57, 63, 59 and 60 thousand units. In perspective the bars at the back look smaller, and no bar top can be read against the axis.

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

✅ Flat bars in one colour, with the value written on each. The five values are read directly. They differ by 6 thousand at most.

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

⚠️ Life expectancy at birth in 26 countries, about 2019, in alphabetical order. The order of the rows says nothing about the values: the highest, the lowest and the groups have to be searched for.

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

⚠️ Sorted now, but as bars from zero. Every value lies between 60 and 84 years, so every bar is long, and the differences fill only the last 24 years of an 86-year axis.

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

🎯 One dot per country on a common scale (Cleveland), sorted. A dot shows its value by position, not by length, so the axis need not start at zero and the values use its full width: 13 countries at 81 to 84 years, 4 at 60 to 66.

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

# **Density**: a Smoothed Histogram

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

📈 The ages of 714 passengers of the Titanic. A density is a smoothed histogram: each age becomes a small bump, and the bumps are added up. How wide the bumps are is chosen by the author, as a bin width is.

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

<div class="card card-info card-glass pad-compact mt-sm">

📦 The hourly temperatures of the weather log: the cold months, the warm months and all hours, drawn three ways.

</div>

<div class="fig-fill grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_boxplot.svg">

📦 **Boxplot**: the box of all hours spans both seasons and shows one block

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_violin.svg">

🎻 **Violin**: a density curve and its mirror image: all hours show two peaks

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_weather_strip.svg">

〰️ **Strip**: hours as points, shifted sideways at random

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

📐 The box holds the middle half of the values. The line in it is the **median**: half of the values lie below it, half above. The whiskers reach out to the values that are not unusually far from the box.

</div>

<!--
**Say:** on all 87 552 hours the quartiles are −0.2, 6.7 and 14.2 °C: the box runs across both seasons and the dip between them, and nothing in it says two peaks. The violin of all hours has the two bumps of the histogram.
**If asked:** a quarter of the values lie below the box (the first quartile), a quarter above it (the third); the box length is the interquartile range, IQR. A whisker ends at the last value within 1.5 × IQR of the box; values beyond it are drawn one by one.
**Ask:** which of the three charts shows that all hours are two seasons?
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Overlaid Densities: Lines or **Fill**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Petal length of three iris species. Lines have to be followed one by one and matched to a legend. A transparent fill shows each group as an area, and a name beside each area replaces the legend.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_lines.svg">

🚫 **Lines and a legend**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_filled.svg">

✅ **Fill and direct labels**

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

<div class="card card-info card-glass pad-tight mt-sm">

## 🧩 **The shares of six tools**

The shares of six tools in a survey of 240 people, as a pie, as one stacked bar and as separate bars. In the pie the shares are compared by angle. As separate bars they are compared by position on a common scale.

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

🥧 A pie works for one whole with few parts, when the point is a share of that whole. The German Bundestag of 1976 had 496 seats in three groups. SPD and FDP together held 253 of them, 51 %, and the pie shows them as slightly more than half the circle.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_marketshare_pies_bad.svg">

❌ **Three pies**: a share that changes from year to year cannot be followed across circles

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_bundestag_pie_good.svg">

✅ **One pie**: one whole, three parts, one share to read

</div>

</div>

<!--
**Say:** one whole, three parts, one question, whether two parties together hold more than half: then a pie works.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Visualising **Associations**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-tight">

## 🔵 **The scatter plot**

Each point is one penguin, with the length and the depth of its bill. Look for a trend, the spread around it, groups, and single points away from the rest. Colour adds a third variable, the species: the three groups are three species.

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

# Visualising **Trends**

<div class="card card-info card-glass pad-tight mt-sm">

## 📉 **The data and the trend together**

The daily means of 2024 and 2025 from the weather log as a thin grey line, and their mean over 21 days as a thick one. Both are drawn, so the reader sees what the smoothing removed.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_trends_lincoln_temps_raw_smooth.svg">

<!--
**Say:** the grey line is every day, the cyan line the mean over three weeks around each day: the season without the day-to-day weather.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A Line Through Missing **Data**

<div class="card card-info card-glass pad-compact mt-sm">

🕳️ 19 to 29 July 2019, hour by hour. For 120 hours, 22 to 26 July, the file holds −999 in place of the temperature; a line drawn over them invents five days near 22 °C.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_gap_bad.svg">

🚫 **Joined**: a straight line across five days

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_gap_good.svg">

✅ **A gap**: the missing hours stay missing

</div>

</div>

<!--
**Ask:** what was the weather on 24 July? Nobody knows: the line on the left is drawn, not measured.
**Say:** `weather.hours` leaves the −999 rows out, so `ax.plot` joins the hours on either side. With `float("nan")` in their place, Matplotlib leaves the gap.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Visualising **Uncertainty**

<div class="fig-fill grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_error_bars.svg">

📏 **Error bars**: a mean ± its standard error: the standard deviation of the *N* values, their typical distance from the mean, divided by √*N*

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_ci_band.svg">

🎗️ **Band**: where the line could lie, given how far the points scatter. The wider the band, the less certain the line

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_hop_demo.svg">

🎰 **Many lines**: 28 of these lines drawn together. Where they fan out, the line is least certain

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 Error bars are the convention for measured points, and a band suits a curve. Many lines can be read without knowing what a standard error is.

</div>

<!--
**Say:** the standard deviation is the typical distance of a value from the mean. Nine values with a standard deviation of 0.3 °C have a mean with a standard error of 0.3 / √9 = 0.1 °C.
**If asked:** the band: the straight line is redrawn for 400 copies of the data, each made of 60 points drawn from the 60 at random, with repeats; the band holds 95 % of these lines, and the many lines are 28 of them.
(~2 min)
-->

---
hideInToc: true
---

# Which **Chart** for Which Question

<div class="grid-2 mt-sm gap-md">

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

<!--
**Say:** the table of this section in one slide; the question decides the chart.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Design **Principles**

The chart follows from what is compared. How it is drawn, its ink, its colours and its scale, decides whether the comparison can still be read.

<!--
**Say:** from which chart to how it is drawn: ink, colour, scales, panels.
(~0.5 min)
-->

---
hideInToc: true
---

# The **Data-Ink** Ratio

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **Edward Tufte, 1983**

> “Above all else show the data.” The **data-ink ratio** is the ink that shows data divided by all the ink of the figure. Ink that can be erased without losing information is erased.

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
**Ask:** which ink in a plot drawn with the defaults shows no data?
(~1 min)
-->

---
hideInToc: true
class: fill
---

# The Same Scatter with **Less Ink**

<div class="card card-info card-glass pad-compact mt-sm">

✂️ The same 90 points twice. On the right the box, the inner ticks, the background and the dense grid are gone. No point and no axis value was removed.

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

## 🎨 **Who cannot tell red from green**

About 8 % of men and 0.5 % of women see colours differently, most of them with red and green hard to tell apart. Among 20 men and 20 women that is 1.7 people on average.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Palettes built for this: `viridis` and `cividis` for ordered values, Okabe–Ito for categories

</div>

<div class="card card-secondary card-glass pad-compact">

🚫 **Avoid**: red against green as the **only** difference between two groups

</div>

<div class="card card-accent card-glass pad-compact">

🔲 A **second channel** beside colour: marker shape, line type or a direct label

</div>

<div class="card card-warning card-glass pad-compact">

🧪 A **check**: view the figure through a simulator such as Color Oracle, or print it in grey

</div>

</div>

<!--
**Say:** in a room of 40 people, one or two see red and green alike.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Red and Green, **Simulated**

<div class="card card-warning card-glass pad-compact mt-sm">

👓 Left: two groups in red and green. Right: the same plot as seen with deuteranopia, the most common colour-vision deficiency. The two groups have one colour.

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

<div class="card card-warning card-glass pad-compact mt-sm">

🌈 One field of values drawn with two palettes: `jet` on the left, `viridis` on the right.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_bad.svg">

🚫 **Rainbow**: sharp colour steps where the values change smoothly

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_fix.svg">

✅ **Viridis**: lightness rises with the value, also when printed in grey

</div>

</div>

<!--
**Ask:** where are the sharp edges in the data on the left? There are none: the yellow band is a step of the palette.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Population growth of US states from 2010 to 2020 (census). The three fastest are in colour and carry their value, the others are grey. The reader finds the three first, and the grey bars remain as the comparison.

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

🍝 The daily mean of every day, one line per year. In ten colours no year can be followed; in grey with one year in colour, that year is read against the others.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_spaghetti_bad.svg">

🚫 **Ten colours and a legend**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_highlight_good.svg">

✅ **Nine in grey, 2025 in colour**

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

📐 The citations of five papers: 5, 60, 540, 4900 and 46 000. On a linear axis the three smallest lie in the lowest 2 % of the axis. On a logarithmic axis each step multiplies by ten: 1, 10, 100, 1000 stand equally far apart, and all five are apart. The values are drawn as dots: a bar would need a zero, and a logarithmic axis has none.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_proportional_ink_log_scale.svg">

<!--
**Say:** 540 / 50 000 = 1.1 %: on the linear axis, which runs to 50 000, the third paper sits at about a hundredth of its height. On the logarithmic axis each value is 9 to 12 times the one before, so the five are almost evenly spaced.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Six regions, one panel each, all with the same axes. In each panel one curve is in colour and the other five grey. In a single panel six coloured curves would cover each other.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_multi_panel_small_multiples_gapminder.svg">

<!--
**Say:** one panel per group, every panel with the same axes, so the eye compares by position.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Small Multiples: a **Shared Axis**

<div class="card card-info card-glass pad-compact mt-sm">

🚢 The fraction of Titanic passengers who survived, by class and sex. With a y-axis of its own in each panel, the three panels look alike. With one axis from 0 to 1 the difference shows: nearly all women in first class survived, and about half of the women in third class.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_bad.svg">

🚫 **An axis per panel**: three panels that look alike

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_good.svg">

✅ **One shared axis**: third class is seen to differ

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

📊 The monthly means of temperature and humidity. On two y-axes, where the curves cross depends on two ranges chosen by hand; in two panels, each curve is read on its own scale.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_two_axes_bad.svg">

🚫 **Two y-axes**: the curves cross where the ranges put them

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_goodbad_two_axes_good.svg">

✅ **Two panels, one x-axis**: the months line up

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

A figure with little ink, a palette that fits and the right scale is correct, and the reader can still miss what it shows.

<!--
**Say:** four means: the title, direct labels, an annotation, a reference line.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Title as the **Finding**

<div class="card card-info card-glass pad-compact mt-sm">

✍️ A title can describe the figure, *Sales 2019–2025*, or state what it shows, *Sales doubled after 2022*. The second saves the reader the work.

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
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Direct **Labels**

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ Four lines and a legend: the reader looks from a line to the legend and back, four times. With a name at the end of each line the legend is not needed.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_bad_legend.svg">

🚫 **A legend at the side**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_good_no_legend.svg">

✅ **Names at the ends of the lines**

</div>

</div>

<!--
**Say:** a legend makes the eye travel; a name at the line does not.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# **Annotations**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 The number of active users over ten weeks, plain and with one annotation. The arrow marks the week in which a feature was released. The reader no longer has to guess why the curve rises there.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_telling_a_story_annotated_vs_plain.svg">

<!--
**Say:** one arrow and one line of text answer the question the plain plot raises.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A Window Chosen for Its **Story**

<div class="card card-info card-glass pad-compact mt-sm">

✂️ The yearly means. From the cold 2017 to the warm 2023, with the axis cut close: +1.8 °C in six years. All ten years against their mean: no trend to read.

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

The two figures of the start, drawn by Matplotlib from the lists that `weather.py` reads, one call for each part.

<!--
**Say:** from here on, code: Matplotlib again, from the four hours of Lecture 5 to the two figures of the start.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Figure, Axes, **Artists**

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **Matplotlib draws lists**

- `import matplotlib.pyplot as plt` loads the library under the short name `plt`
- `fig, ax = plt.subplots()` makes a **Figure**, the whole picture, and one **Axes**, the region with an x-axis and a y-axis
- A call on `ax` adds an **artist**: `ax.plot` draws points or a line, `ax.hist` bars, `ax.set_xlabel` a text
- `fig.savefig("results/month_means.png")` writes the picture to a file

</div>

<div>

<img class="fig" src="/figures/viz_handson_figure_axes.svg">

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Matplotlib is a package from conda-forge, installed into the project's environment with `conda install matplotlib-base=3.11`.

</div>

<!--
**Say:** the Figure is the sheet, the Axes one plot on it, and everything drawn is an artist that a call on `ax` put there. Lecture 5 drew four hours this way.
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

```python {all|1-2|4|6-7|8|all}
import matplotlib.pyplot as plt
import weather

values = weather.temps("data/raw/weather.csv")

fig, ax = plt.subplots()
ax.plot(values)
fig.savefig("results/every_hour.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

The script `scripts/figures.py` sits beside `weather.py` and runs with `$ python scripts/figures.py`. `weather.temps` is the function of Lecture 5: the 87 552 temperatures, without the −999 rows. Given one list, `ax.plot` draws it against its positions 0, 1, 2, …

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_hours_default.svg">

⚠️ **The output.** Ten summers and ten winters. The x-axis counts list positions, not time, and no axis says what it shows or in which unit.

</div>

</div>

<!--
**Ask:** what can be read already, and what is missing?
**If asked:** after 2019-07-21T23:00 the next value is 2019-07-27T00:00: the 120 hours the sensor did not record are left out, so every later position is 120 hours early.
(~2 min)
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
**Do:** first step: `temps` of Lecture 5; click: the four lines that change.
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
class: fill
---

# A Histogram Counts Values in **Bins**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

```python {all|1|3|4|5|all}
values = weather.temps("data/raw/weather.csv")

fig, ax = plt.subplots()
ax.hist(values)
fig.savefig("results/temp_hist.png")
```

<div class="card card-info card-glass pad-compact mt-sm">

`ax.hist` cuts the range from the smallest to the largest value into 10 bins of equal width, counts the values in each bin and draws one bar per bin. The counts, which `ax.hist` also returns:

```text
337  3173  12733  17255  13892
14619  13466  8797  2948  332
```

</div>

</div>

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_temp_default.svg">

⚠️ **The output.** From −16.3 to 32.4 °C in 10 bins: 4.87 °C each, with edges at −16.3, −11.43, … The fullest bin, −1.69 to 3.18 °C, holds 17 255 hours.

</div>

</div>

<!--
**Say:** one value is one hour, so there is nothing to plot it against: the question is how often each temperature occurs.
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

📏 **Range.** −17 to 33 °C holds all 87 552 hours, from the coldest, −16.3, to the warmest, 32.4, and puts the edges on whole degrees.

</div>

<div class="card card-secondary card-glass pad-compact">

📐 **Bin width.** The station records tenths of a degree. A bin holds several recorded values, and enough hours that neighbouring bins do not differ by chance.

</div>

</div>

<img v-click class="fig fig-fill mt-sm" src="/figures/viz_handson_temp_binwidths.svg">

<div v-click class="card card-success card-glass pad-compact mt-sm">

✅ **1 °C per bin.** At 10 °C one hump; at 1 °C two peaks. At 0.05 °C only 21 values occur between 0 and 2 °C, 0.0, 0.1, …, 2.0, so 20 of the 41 bins, every other one, are empty.

</div>

<!--
**Ask:** before the figure: what will bins of 10 °C show?
**Say:** a bin narrower than the steps of the data counts the rounding, not the weather.
**If asked:** in ten years the station recorded 477 different values, every tenth of a degree that occurred.
(~3 min)
-->

---
hideInToc: true
class: runner-side
---

# Choose the Bin Width, **Live**

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

- 50 bins from −17 to 33 °C: (33 − (−17)) / 50 = 1 °C per bin
- The y-label states the bin width. A count per bin has no meaning without it

</div>

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_temp_hist.svg">

✅ **The output.** Two peaks: 3848 hours at −1 to 0 °C, 3032 at 11 to 12 °C. Between them, at 7 to 8 °C, 2706 hours: the mean lies in the dip.

</div>

</div>

<!--
**Say:** the histogram of the start, made by five lines. Both choices came from numbers: the range holds every hour, and 1 °C shows the two peaks.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Hands-on **Matplotlib**

Each new element of a figure is one more call on `ax`.

<!--
**Say:** the same module, per year and per month.
(~0.5 min)
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

## 🔁 **Save SVG and PNG**

```python
fig.savefig("results/temp_hist.svg", bbox_inches="tight")
fig.savefig("results/temp_hist.png", dpi=150, bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 `bbox_inches="tight"` cuts the empty margin. Keep the script next to the figures and commit all three: a figure that a script makes again from the data file can be checked and corrected.

</div>

<!--
**Say:** SVG for slides and papers, PNG for the web; the script makes both again from the file.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Beyond Two **Axes**

A plane has two positions. Colour and motion each carry one more variable, read less exactly than a position.

<!--
**Say:** two figures that show a third variable, as colour and as time; more of them come after the recap.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Day, Hour and Temperature on One Plane: `imshow`

<div class="card card-primary card-glass pad-compact mt-sm">

🌡️ The ten-year mean of every hour of every day of the year: days across, hours up, the temperature as colour, diverging at 0 °C. July afternoons reach 25.3 °C, January nights −7.9 °C. `ax.imshow(grid, aspect="auto", origin="lower", cmap="RdBu_r", vmin=-30, vmax=30)`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_heatmap.svg">

<!--
**Say:** three variables on a plane: two positions and a colour. 366 × 24 cells, each the mean of 10 hours or fewer. Both cycles at once: the year from left to right, the day from bottom to top.
**Ask:** where is the day-night difference largest? In summer: a July day swings 10 °C, a January day 4 °C.
**If asked:** the grid comes from `weather.group(path, 5, 13)`: the key `07-28T15` is a day and an hour.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Time as One More Variable: an **Animation**

<div class="card card-success card-glass pad-compact mt-sm">

🎞️ The hours of each month as a histogram, January to December, over the outline of all hours ÷ 12. Each month is one bump, from −3.9 °C in January to 18.5 °C in July and back; the twelve bumps add up to the two peaks of the year. `FuncAnimation(fig, draw, frames=12)`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_month_hist.gif">

<!--
**Say:** this answers why the year has two peaks: the months from November to March are narrow and pile up near 0 °C; April to October are wide, and where spring, summer and autumn overlap, near 11 to 12 °C, they make the second peak.
**If asked:** `draw(i)` sets the bar heights of month `i`; `ani.save("months.gif", writer=PillowWriter(fps=1.5))` writes the file. A video or a GIF goes on a slide or a web page, not into a printed paper.
(~2 min)
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

## 🧪 **Before a figure goes into a report**

A "no" means the figure is not finished.

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

<!--
(~1 min)
-->

---
hideInToc: true
---

# Every Choice in the Two **Figures**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **Ten years, hour by hour**

- `weather.hours`: each temperature at its own time, so the hours after the gap of July 2019 keep their dates
- `linewidth=0.2`: 87 552 values as one hairline
- Each axis names its quantity: time on x, with the years as ticks, temperature (°C) on y

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **The hours as a histogram**

- −17 to 33 °C holds every hour, −16.3 to 32.4, with edges on whole degrees
- 1 °C per bin shows two peaks; 10 °C one hump; 0.05 °C the rounding of the station
- The y-label states the bin width: hours per 1 °C

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Given only the list, `ax.hist` chose 10 bins of 4.87 °C. Every choice that shows the mean in the dip comes from a number and is kept in the script.

</div>

<!--
**Say:** the answer to the opening slide, in the room's own numbers.
**Ask:** point at each line: which slide did it come from?
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Make a figure with **Matplotlib** from lists: `plt.subplots`, `ax.plot`, `ax.hist`, labels with units, `fig.savefig`

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **range and bin width** of a histogram, and state the bin width on the axis

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **chart** for amounts, distributions, proportions, associations, trends, and more than two variables

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
**Say:** one line per card, with the ten-year line and the histogram as the two examples for each.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

More chart types, and figures of three to five variables: for time left at the end, or to read after the lecture.

<!--
**Say:** optional, for the time left or for after the lecture: more ways to show a distribution and two variables, two more scales, then figures of three to five variables, each with what it costs.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Bin Widths of 0.5, 5 and 20 **Years**

<div class="card card-info card-glass pad-compact mt-sm">

📏 The same ages with bins of 0.5, 5 and 20 years. With 0.5 years the bars jump between a few people and thirty: ages are whole years, so every second bin is nearly empty. With 20 years the shape is four bars.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_distributions_i_titanic_hist_binwidth.svg">

---
hideInToc: true
class: fill
---

# The Empirical **CDF**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

📈 The empirical cumulative distribution function: at each value *x* the curve gives the fraction of observations that are ≤ *x*. Every observation is one step up, and no bin width is chosen. The median is where the curve crosses 0.5, at 28 years for the Titanic passengers.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_ecdf.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Bubble** Chart

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

🫧 A third numeric variable as the size of the marker, here the body mass. Area is read less accurately than position, so size is for the variable that matters least. The area is proportional to the value, not the radius.

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_bubble.svg">

</div>


---
hideInToc: true
class: fill
---

# When **Points Overlap**

<div class="card card-info card-glass pad-tight mt-sm">

## 🫧 **Three ways to draw 3000 points**

Two answers on a scale from 0 to 10, from 3000 people: whole numbers, so many points lie on top of each other. Left: plain points. Centre: each shifted a little at random (jitter) and made transparent. Right: cells coloured by the number of points.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_no_3d_jitter_overplot_jitter_alpha.svg">

---
hideInToc: true
class: fill
---

# Many Points: **Hexagonal Bins**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 20 000 flights: arrival delay against departure delay. Drawn as points, the centre is one solid area. Hexagonal bins show the count of each cell as a colour, a histogram in two dimensions.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_points.svg">

🚫 **Points**: the centre is one solid area

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_hex_bins.svg">

✅ **Hexagonal bins**: colour is the number of flights per cell

</div>

</div>

---
hideInToc: true
class: fill
---

# The **Correlation** Heatmap

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

🔥 The correlation *r* says how close two columns lie to a straight line: +1 all points on a rising line, −1 on a falling one, 0 no straight-line trend. Every pair of seven columns of a table of cars; red below 0, blue above.

</div>

<img class="fig" src="/figures/viz_associations_mtcars_corr_heatmap.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Pair** Plot

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

🔲 Every pair of columns as a scatter plot, with the histogram of each column on the diagonal. Here three measurements of penguins. It is a first look at a table with several numeric columns.

</div>

<img class="fig" src="/figures/viz_multi_panel_correlogram.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Slopegraph**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

📈 One value per group at two dates, joined by a line. Here tonnes of CO₂ per person in 2000 and 2020 (approximate). The slope is the change: the USA falls from 20.5 to 14.2, China rises from 2.7 to 7.4.

</div>

<img class="fig" src="/figures/viz_associations_co2_slopegraph.svg">

</div>


---
hideInToc: true
class: fill
---

# The **Square-Root** Scale

<div class="card card-info card-glass pad-compact mt-sm">

√ For counts. A count *N* scatters by about √*N* from one repetition of a measurement to the next: 48 ± 7, 3 ± 1.7, the bars drawn here. On a square-root axis, which spaces 0, 1, 4, 9, 16 evenly, every bar has about the same length. A count of zero stays on the axis, which a logarithmic axis cannot show.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_sqrt_scale.svg">

<!--
**If asked:** the half unit in one line: √(N + √N) ≈ √N + ½; for N = 100, √110 = 10.49.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A **Reference** Line

<div class="card card-info card-glass pad-compact mt-sm">

🧬 The abundance of mRNA in a mutant against the wild type, on logarithmic axes. Most genes are unchanged and lie where y&nbsp;=&nbsp;x. Without that line the reader has to estimate it. With it, the genes off the line are the result, and here they also have a second colour.

</div>

<div class="fig-fill grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_bad.svg">

🚫 **No reference**

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_good.svg">

✅ **The line y = x**: the points off it have changed

</div>

</div>

---
hideInToc: true
class: fill
---

# The Same Grid as a Surface: `plot_surface`

<div class="card card-secondary card-glass pad-compact mt-sm">

⛰️ The 8784 means as a landscape: a ridge of summer afternoons, a valley of winter nights, a daily ripple deeper in summer. The shape is seen at once; no value can be read off, and the far side is hidden. `ax = fig.add_subplot(projection="3d")`, `ax.plot_surface(x, y, grid, cmap="RdBu_r")`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_surface.svg">

<!--
**Say:** the same numbers as the heatmap, with the temperature as height too. A surface shows a shape; for values the flat heatmap is better, because perspective makes far values look smaller and hides some of them.
**If asked:** `ax.plot_surface(x, y, grid, cmap="RdBu_r")`, and `ax.view_init(elev=32, azim=-42)` turns the view.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Temperature as Colour, Humidity as **Contour Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

🗺️ Day, hour, the mean temperature as colour, the mean humidity as lines of equal value, like heights on a map. The 70 % line closes around summer afternoons; January nights pass 90 %. `cs = ax.contour(x, y, hum, levels=[70, 80, 90])`, `ax.clabel(cs)`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_contours.svg">

<!--
**Say:** two fields on one plane: colour for one, lines for the other. Where the colour is warm the lines show dry air; humidity falls as the air warms, r = −0.81 over the 8784 cells.
**Ask:** at what time of day is the air driest? Mid-afternoon: in July 62.8 % at 15:00 against 81.3 % at 03:00, in January 78.0 % against 94.8 %.
**If asked:** each cell is the mean of about 10 hours, too noisy for smooth lines, so the humidity is a running mean over 15 days before `contour` draws it. The driest cell, 20 June at 15:00, holds 61.5 %.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Year, Day, Hour and Temperature in **3D**

<div class="card card-secondary card-glass pad-compact mt-sm">

🧱 All 87 552 hours, one plane per year from 2016 to 2025: three positions and a colour. Each plane hides most of the one below: the 120 missing hours of July 2019 cannot be found. `ax.plot_surface(x, y, z, facecolors=cmap(norm(grid)))` per year

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_slices.svg">

<!--
**Ask:** which year had the warmest summer? The planes above cover the planes below, and perspective shrinks the far ones; the figure cannot answer.
**If asked:** each plane is a flat surface at the height of its year, coloured cell by cell with `facecolors`; a missing hour gets a transparent colour.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Same Hours as Ten **Panels**

<div class="card card-success card-glass pad-compact mt-sm">

🧩 The same four variables, the year as a panel instead of a height: nothing hidden, one colour scale for all ten. The dark line in 2019 is 22–26 July, the 120 missing hours. `fig, axs = plt.subplots(2, 5, sharex=True, sharey=True)`, one `imshow` per panel

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_multiples.svg">

<!--
**Say:** small multiples again: when a third axis hides data, a row of flat panels usually shows it all.
**Ask:** which year was warmest? 2023, mean 8.31 °C; the coldest 2025, 5.98 °C. A colour difference of 2 °C is hard to see, so the number still goes into the text or a separate plot.
**If asked:** the warmest hour, 32.4 °C, was 18 June 2018 at 15:00. `extent=(0, 365, 0, 24)` puts every year on the same axis, a leap year has one column more.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Five Variables of Each Day: **Parallel Coordinates**

<div class="card card-accent card-glass pad-compact mt-sm">

🪢 3648 days, one line each, through four axes on their own scales; the month as colour. From daily range to temperature the lines run level: warm days swing more (r = +0.82). From temperature to humidity they cross: warm days are dry (r = −0.73).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_advanced_parallel.svg">

<!--
**Say:** any number of variables, each on its own vertical axis. The order of the axes decides which pairs can be compared: only neighbours.
**Ask:** what does a July day look like? A daily range of 10.4 °C on average, 71.9 % humidity, 2.89 m/s; a January day 4.9 °C, 86.8 %, 4.32 m/s.
**If asked:** `LineCollection` draws the 3648 lines in one call, `set_array(month)` colours them; drawn in a random order, so no month lies on top of the rest.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Temperature, Humidity, Wind and **Month**

<div class="card card-accent card-glass pad-compact mt-sm">

🧭 3648 days: three daily means on three axes, the month as colour. Days below 0 °C: 86.5 % and 4.0 m/s on average; above 20 °C: 67.6 % and 2.8 m/s. `ax.scatter(temp, hum, wind, c=month)`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_scatter4d.svg">

<!--
**Say:** four variables in one figure: three positions and a colour. The groups are seen; single points are not read.
**Ask:** which pair of the three measurements moves together most? Temperature and humidity: r = −0.73.
**If asked:** the palette is cyclic, built from the course colours, so the year closes on itself.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Four-Variable Scatter, **Turning**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

🌀 Temperature, humidity, wind and month of 3648 days, turning once every 3 s. A still 3D scatter leaves the depth to guess; turning, points in front move one way and points behind the other. `ax.view_init(elev=18, azim=a)` in each frame of `FuncAnimation`

</div>

<img class="fig" src="/figures/viz_advanced_rotate.gif">

</div>

<!--
**Say:** motion is one more channel, for depth. For a paper, pick the one view that shows the finding, or use flat panels.
**If asked:** 36 frames, 10° apart, at 12 frames per second, written with `PillowWriter`; in a notebook or with `plt.show()` the mouse turns the figure.
(~1 min)
-->

---
hideInToc: true
class: fill
---

# A 2D Histogram with Its **Projections**

<div class="card card-info card-glass pad-compact mt-sm">

⚛️ LHCb pairs of a K⁻ and a π⁺, the 90 753 with transverse momentum from 2.5 to 9 GeV/c: their combined mass across, the momentum up, the count per cell as colour (log scale); above and right, each variable alone. Pairs from a D⁰ decay make the band at 1865 MeV/c². `ax.hist2d(m, pt, norm=LogNorm())`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_d0_hist2d.svg">

<!--
**Say:** the standard figure of a particle physics analysis: two variables as positions, their count as colour, and each variable alone on the side, so that nothing is hidden.
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

⚛️ Every pair of `M`, `PT`, `TAU` and `IPCHI2` as a 2D histogram, each column alone on the diagonal: 91 534 candidates. The D⁰ is the band at 1865 MeV/c² in the mass column. `plt.subplots(4, 4)`, the upper triangle hidden

</div>

<img class="fig" src="/figures/viz_advanced_corner.svg">

</div>

<!--
**Say:** the standard first look at a physics data set: n columns give n(n − 1)/2 pairs, here six. It is the pair plot of the gallery with 2D histograms in place of points, because 91 534 points would cover each other.
**Ask:** which pair moves together? τ and log χ²_IP, r = 0.35: both grow when the D⁰ flies further from the collision before it decays. Every other pair has |r| ≤ 0.07.
**If asked:** 49 rows have `TAU` = −100, a missing value, and are left out. χ²_IP runs from 10⁻⁵ to 10⁶, so its axis is log₁₀. The horizontal edge at 0.15 ps in the τ panels is a cut of the selection that made the file.
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
