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

# The Mean of 87 552 **Hours**

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **The first and the last lines of `weather.csv`**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
...
2025-12-31T23:00,-11.3,100,4.2
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python scripts/mean_temp.py
87552 7.15996550621345
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ The mean of the 87 552 hours is 7.16 °C. Is 7 to 8 °C, the degree of the mean, the fullest degree, or do the degrees around it hold more hours?

</div>

<!--
**Say:** the script of Lecture 5: every hour of the station without the −999 rows, and their mean.
**Ask:** hands up for the fullest, hands up for not. The answer comes with the first histogram.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Anscombe's **Quartet**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four tables of 11 points (Anscombe, 1973). In each one the mean of x is 9.0, the mean of y is 7.5, and the closest straight line is y = 3.00 + 0.50x. Each has r = 0.82, where r measures how near the points lie to a straight line: 1 on a rising line, −1 on a falling one, 0 with no trend. What do the four tables look like?

</div>

<div class="fig-fill mt-sm" v-click>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg">

<div class="note-text mt-sm text-center">Only the plot tells the four apart.</div>

</div>

<!--
**Do:** read the four numbers first.
**Ask:** what do the four tables look like?
**Say:** after the click: a line with scatter, a curve, a line with one point off it, and ten points at one x with a single point that makes the whole slope. The mean 7.16 °C is one such number.
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
layout: section
hideInToc: true
---

# Mechanics of a **Figure**

Both plots put every number on a position along an axis. Position is one channel among several, and the channels are not read equally well.

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

---
hideInToc: true
---

# The Ranking of **Visual Channels**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Channels are not read equally well**

Cleveland and McGill (1984), and Heer and Bostock (2010) with more people, measured how exactly each channel is read, from the most to the least accurate. The most important variable gets the highest channel that is free.

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

<div class="note-text mt-sm">Example values. The bar on each point is the uncertainty of the count: ± √N for a count of N.</div>

<!--
**Do:** click through: frame, axes with units, the data, its uncertainty, the annotation, the title that states the finding.
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

---
hideInToc: true
class: fill
---

# A Legend Without **Samples**

<div class="fig-fill grid-side mt-sm">

<div v-click class="card card-warning card-glass pad-compact">

⚠️ The legend names two countries and shows no sample of either line: nothing says which colour is which. The y-axis has no unit.

</div>

<img class="fig fig-light" src="/figures/data_vis_legend_error_1.png">

</div>


<!--
**Ask:** before the click: which line is which country, and in which unit?
(~1 min)
-->

---
hideInToc: true
class: fill
---

# Axis Labels with **Units**

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ The same curve twice. On the left the axes are called `x` and `val`. On the right they name the quantity and its unit: the time of day in hours, the temperature in °C. The ten-year plot names the temperature and its unit on y; years on x need no more.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_axes_labels_bad_good.svg">

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

---
hideInToc: true
class: fill
---

# The **Coordinate System**

<div class="card card-info card-glass pad-compact mt-sm">

🧭 Data that repeat after a full turn can be drawn on a circle: days of a year, hours of a day, compass bearings. On the circle the end meets the start, 360° is 0°, and the pattern closes on itself: three maxima, 120° apart.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_polar_vs_cartesian.svg">

---
hideInToc: true
class: fill
---

# The **Aspect Ratio**

<div class="card card-info card-glass pad-compact mt-sm">

📐 One temperature series over 365 days (example values), drawn in three shapes. A tall, narrow plot makes the slopes steep, a wide plot makes them shallow. Slopes are compared most accurately when they lie near 45° (Cleveland).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_coordinates_axes_houston_temps_aspect_ratios.svg">

---
layout: section
hideInToc: true
---

# Chart **Families**

Position is read most accurately. Which chart puts a comparison on position follows from what is compared: amounts, a distribution, parts of a whole, two variables, a change over time.

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

⚠️ Five films and their opening-weekend gross (invented titles). The titles do not fit under vertical bars and have to be rotated. Rotated text is read slowly.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_rotated_bad.svg">

</div>


---
hideInToc: true
class: fill
---

# The Same Bars, **Horizontal**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

🎬 The same five values as horizontal bars: every title is written level, and the order of the bars is the ranking of the films.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_horizontal.svg">

</div>


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


---
hideInToc: true
class: fill
---

# Median Income by **Age Group**

<div class="fig-fill grid-side mt-sm">

<div v-click class="card card-warning card-glass pad-compact">

⚠️ Median income by age group, sorted by income. Age groups are **ordinal**: they have an order of their own, and sorting by value breaks it. Sort by value only when the categories have no order.

</div>

<img class="fig fig-light" src="/figures/data_vis_bar_chart_error_3.png">

</div>


<!--
**Ask:** before the click: the films were sorted by value. Does the same rule fit here?
(~1 min)
-->

---
hideInToc: true
class: fill
---

# **Stacked** Bars

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

📊 A bar is a total and a segment a part of it. The totals and the bottom segments share a baseline and are compared by position. The upper segments are compared by length only, which is less accurate.

</div>

<img class="fig" src="/figures/viz_amounts_students_stacked_bars.svg">

</div>


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


---
hideInToc: true
class: fill
---

# The **Dot Plot**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

🎯 One dot per category on a common scale (Cleveland). Less ink than bars, and readable for many categories. A dot shows its value by position, not by a length, so its axis need not start at zero.

</div>

<img class="fig" src="/figures/viz_amounts_cleveland_dot_plot.svg">

</div>


---
hideInToc: true
class: fill
---

# **Density**: a Smoothed Histogram

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

📈 The ages of 714 passengers of the Titanic. A kernel density estimate replaces each value by a small bell-shaped bump and adds the bumps up. The y-axis is scaled so that the area under the curve is 1. The width of the bumps, the bandwidth, is chosen by the author, as a bin width is.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_density.svg">

</div>


---
hideInToc: true
class: fill
---

# Bin Widths of 0.5, 5 and 20 **Years**

<div class="card card-info card-glass pad-compact mt-sm">

📏 The same ages with bins of 0.5, 5 and 20 years. With 0.5 years the bars jump between a few people and thirty. With 20 years the shape is four bars.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_distributions_i_titanic_hist_binwidth.svg">

---
hideInToc: true
class: fill
---

<div class="card card-info card-glass pad-compact">

📦 The fuel economy of cars with 4, 6 and 8 cylinders, drawn three ways.

</div>

<div class="fig-fill grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_boxplot.svg">

📦 **Boxplot**: five numbers per group. It would hide a second peak

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_violin.svg">

🎻 **Violin**: a density curve and its mirror image. It would show a second peak

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_strip_jitter.svg">

〰️ **Strip**: every value as a point, shifted sideways at random

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

📐 The **median** has half of the values below it. A quarter lie below the first **quartile** and three quarters below the third. The box runs from the first to the third quartile, and its length is the interquartile range (**IQR**). The line in the box is the median. A whisker ends at the last value within 1.5 × IQR of the box, and values beyond it are drawn one by one.

</div>

<!--
**Say:** on the 87 552 hours the quartiles are −0.2, 6.7 and 14.2 °C: the box runs across both seasons and the dip between them, and nothing in it says two peaks.
**Ask:** which of the three charts would show them?
(~2 min)
-->

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

# Overlaid Densities: Lines or **Fill**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Petal length of three iris species. Lines have to be followed one by one and matched to a legend. A transparent fill shows each group as an area, and a name on the area replaces the legend.

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

Two answers on a scale from 0 to 10, from 3000 people (synthetic): whole numbers, so many points lie on top of each other. Left: plain points. Centre: each shifted a little at random (jitter) and made transparent. Right: cells coloured by the number of points.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_no_3d_jitter_overplot_jitter_alpha.svg">

---
hideInToc: true
class: fill
---

# Many Points: **Hexagonal Bins**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 20 000 flights (synthetic): arrival delay against departure delay. Beyond about 10 000 points transparency no longer helps: the centre is solid. Hexagonal bins show the count of each cell as a colour, a histogram in two dimensions.

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

🔥 The correlation *r*, from −1 on a falling line to +1 on a rising one, for every pair among seven columns of a table of cars, on a diverging palette centred at 0.

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

# Visualising **Trends**

<div class="card card-info card-glass pad-tight mt-sm">

## 📉 **The data and the trend together**

Daily temperatures (synthetic) as a thin grey line, and their mean over 21 days as a thick one. Both are drawn, so the reader sees what the smoothing removed.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_trends_lincoln_temps_raw_smooth.svg">

---
hideInToc: true
class: fill
---

# A Line Through Missing **Data**

<div class="card card-info card-glass pad-compact mt-sm">

🕳️ 19 to 29 July 2019, hour by hour. The sensor recorded nothing for 120 hours; a line drawn over them invents five days near 22 °C.

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

🎗️ **Band**: the closest straight line, redrawn for 400 resampled copies of the data. The band holds 95 % of the lines

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_hop_demo.svg">

🎰 **Many lines**: 28 such lines drawn one by one. Their spread is the uncertainty of the line

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 Error bars are the convention for measured points, and a band suits a curve. Many lines can be read without knowing what a standard error is.

</div>

<!--
**Say:** the standard deviation is the typical distance of a value from the mean. Nine values with a standard deviation of 0.3 °C have a mean with a standard error of 0.3 / √9 = 0.1 °C.
**If asked:** a resampled copy draws N rows from the table at random, with repeats.
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
class: fill
---

# Red and Green, **Simulated**

<div class="card card-warning card-glass pad-compact mt-sm">

👓 Left: two groups in red and green. Right: the same plot as seen with deuteranopia, the most common colour-vision deficiency. The two groups have one colour.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_pitfalls_of_color_use_red_green_cvd_sim.svg">

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

---
hideInToc: true
class: fill
---

# Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Population growth by state (example values). Three bars are in colour and carry their value, the others are grey. The reader finds the three first, and the grey bars remain as the comparison.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_color_popgrowth_us_highlight.svg">

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

📐 The citations of five papers: 5, 60, 540, 4900 and 46 000. On a linear axis the three smallest lie in the lowest 2 % of the axis. On a logarithmic axis equal distances are equal factors, and all five are apart. The values are drawn as dots: a bar would need a zero, and a logarithmic axis has none.

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

# The **Square-Root** Scale

<div class="card card-info card-glass pad-compact mt-sm">

√ For counts. A count *N* scatters by about √*N* from one repetition of a measurement to the next: 48 ± 7, 3 ± 1.7, the bars drawn here. On a square-root axis this scatter has the same length at every height, half a unit. A count of zero stays on the axis, which a logarithmic axis cannot show.

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

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Six regions, one panel each, all with the same axes (synthetic). In each panel one curve is in colour and the other five grey. In a single panel six coloured curves would cover each other.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_multi_panel_small_multiples_gapminder.svg">

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

---
hideInToc: true
class: fill
---

# **Annotations**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 The number of active users over ten weeks, plain and with one annotation. The arrow marks the week in which a feature was released. The reader no longer has to guess why the curve rises there.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_telling_a_story_annotated_vs_plain.svg">

---
hideInToc: true
class: fill
---

# A **Reference** Line

<div class="card card-info card-glass pad-compact mt-sm">

🧬 The abundance of mRNA in a mutant against the wild type, on logarithmic axes (synthetic). Most genes are unchanged and lie where y&nbsp;=&nbsp;x. Without that line the reader has to estimate it. With it, the genes off the line are the result, and here they also have a second colour.

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

`weather.temps` is the function of Lecture 5: the 87 552 temperatures of the file, without the −999 rows. Given one list, `ax.plot` draws it against 0, 1, 2, …, its positions in the list, and joins the points with straight lines.

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
- `dpi=150` saves 150 pixels per inch: 960 × 720 pixels

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

✅ **1 °C per bin.** At 10 °C one hump; at 1 °C two peaks. At 0.05 °C only 21 values occur between 0 and 2 °C, 0.0, 0.1, …, 2.0, so 19 of the 40 bins are empty.

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
    values.append(round(cold, 1))   # in tenths, as the
    values.append(round(warm, 1))   # station writes them
BINS = 5                        # <-- try 5, 55, 1100
fig, ax = plt.subplots(figsize=(5, 4.6),
                       layout="constrained")
ax.hist(values, bins=BINS, range=(-20, 35))
ax.set_xlabel("temperature (°C)")
ax.set_ylabel("values per bin")
plt.show()
```

<!--
**Say:** the browser cannot read the file on the laptop, so `random.gauss(-1, 4)` draws a number near −1 with a spread of 4, and `random.gauss(13, 5)` one near 13: cold and warm months, 6000 values, rounded to tenths. `range(3000)` counts 0 to 2999, so the loop runs 3000 times.
**Do:** press ▶ with 5, then 55, then 1100: bins of 11 °C, 1 °C and 0.05 °C.
**Ask:** with 1100 bins, why is every other bar missing where the values are dense? The values are tenths, and a bin of 0.05 °C between two tenths stays empty, as on the slide before.
**If asked:** `plt.show()` draws the figure under the code; in a script on a laptop it opens a window.
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

- 50 bins from −17 to 33: 50 / 50 = 1 °C per bin
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

Bars, a reference line, a legend, an annotation, a style: one call on `ax` each.

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
years = weather.group("data/raw/weather.csv", 0, 4)
print(len(years))                # 10
print(list(years))               # ['2016', '2017', ..., '2025']
print(len(years["2019"]))        # 8640
print(weather.mean(years["2025"]))   # 5.982077625570776
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

<div class="note-text mt-sm">A <code>dict</code> of lists in <code>weather.py</code>: one list of temperatures per key, in the order the keys first occur. <code>key not in groups</code> is <code>True</code> the first time a key turns up; <code>for year in years</code> runs over the keys, and <code>list(years)</code> lists them.</div>

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
for year in years:
    count = 0
    for temp in years[year]:
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
means = []
for year in years:
    means.append(weather.mean(years[year]))

fig, ax = plt.subplots(figsize=(5.2, 3.6))
all_hours = weather.mean(weather.temps("data/raw/weather.csv"))
ax.axhline(all_hours, color="#D55E00", label="2016–2025: 7.16 °C")
ax.plot(range(2016, 2026), means, "o", color="#56B4E9",
        label="one year")
ax.set(xlabel="year", ylabel="mean temperature (°C)", ylim=(5, 9))
ax.legend(frameon=False, loc="lower left")
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
**If asked:** `range(2016, 2026)` gives 2016 to 2025, the years as numbers, so Matplotlib chooses which to label. `"o"` draws a point at each value and no line.
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
means = []
for month in months:
    means.append(weather.mean(months[month]))

fig, ax = plt.subplots(figsize=(5.6, 3.6))
ax.plot(list(months), means, "o-", color="#56B4E9")
arrow = {"arrowstyle": "->", "color": "#D55E00"}
ax.annotate("July, 18.5 °C", xy=("07", means[6]), xytext=("09", 19.5),
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
**If asked:** `"o-"` draws a point at each value and joins the points by lines, which shows the order of the twelve months; `means[6]` is the seventh mean, July's.
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

---
layout: section
hideInToc: true
---

# Beyond Two **Axes**

A plane has two positions. Colour, a third axis and motion each carry one more variable, read less exactly than a position.

<!--
**Say:** five figures that show three, four or more variables at once, with the call that makes each.
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

# The Same Grid as a Surface: `plot_surface`

<div class="card card-secondary card-glass pad-compact mt-sm">

⛰️ The 8784 means as a landscape: a ridge of summer afternoons, a valley of winter nights, a daily ripple deeper in summer. The shape is seen at once; no value can be read off, and the far side is hidden. `ax = fig.add_subplot(projection="3d")`

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

# Temperature, Humidity, Wind and **Month**

<div class="card card-accent card-glass pad-compact mt-sm">

🧭 One point per day, 3648 days: three measurements on three axes, the month as colour, December beside January. Cold days are humid and windy, warm days dry and calm: below 0 °C 86.5 % and 4.0 m/s on average, above 20 °C 67.6 % and 2.8 m/s. `ax.scatter(temp, hum, wind, c=month)`

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
hideInToc: true
class: fill
---

# A 2D Histogram with Its **Projections**

<div class="card card-info card-glass pad-compact mt-sm">

⚛️ 90 753 K⁻π⁺ candidates from LHCb: mass across, transverse momentum up, the count of each cell as colour on a logarithmic scale; above and to the right, the histogram of each variable alone. The D⁰ is the band at 1865 MeV/c², at every momentum. `ax.hist2d(m, pt, norm=LogNorm())`

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_beyond_d0_hist2d.svg">

<!--
**Say:** the standard figure of a particle physics analysis: two variables as positions, their count as colour, and each variable alone on the side, so that nothing is hidden.
**Ask:** why a logarithmic colour scale? The cells hold from 1 to 178 candidates; on a linear scale every cell with a few candidates, which is most cells of high momentum, would be the same dark colour.
**If asked:** a candidate is a K⁻ and a π⁺ whose combined mass is computed; those from a D⁰ decay have its mass, the others any. Almost none lie below 2500 MeV/c: the selection that made the file cut there. `plt.subplot_mosaic` lays out the three panels, and `sharex`, `sharey` tie their axes.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Wrap-up**

Every choice in the two figures of the start, ten years as a line and the hours as a histogram, with the number behind it.

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
- Each axis names its quantity and unit: years on x, temperature (°C) on y

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

# **Recap**

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Make a figure with **Matplotlib** from lists: `plt.subplots`, `ax.plot`, `ax.hist`, labels with units, `fig.savefig`

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose the **range and bin width** of a histogram, and state them on the axis

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
  question="The mean of ten years of hourly temperatures is 7.16 °C. With 1 °C bins, 7 to 8 °C holds 2706 hours, −1 to 0 °C 3848 and 11 to 12 °C 3032. What does this say about the mean?"
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
  explanation="From 0 to 2 °C the sensor can record 21 values, 0.0 to 2.0, and 40 bins of 0.05 °C cover that range: a bin with a value is followed by one without. The bars show the rounding of the sensor, not the weather. A bin holds several recorded values."
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
  question="From the cold 2017 to the warm 2023 the yearly mean of the station rose by 1.8 °C. What should a figure of its yearly means show?"
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
