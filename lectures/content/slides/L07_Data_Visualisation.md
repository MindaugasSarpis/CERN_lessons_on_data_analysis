---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Data Visualization"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Data Visualization

##### Inspired by: C. O. Wilke Fundamentals of Data Visualization

---
hideInToc: true
layout: quote
---

# Great data visualization is not about making things look pretty — it is about making the **data speak clearly**. A well-designed figure tells a story that numbers alone cannot.

---
hideInToc: true
---

# Why Data Visualization **Matters**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 👁️ **Visual Perception**

The human brain processes images 60,000x faster than text. A well-designed chart can communicate in seconds what a table of numbers takes minutes to parse.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Pattern Discovery**

Visualizations reveal structure — clusters, trends, outliers, and gaps — that summary statistics alone can hide. Anscombe's quartet is the classic proof.

</div>

<div class="card card-accent card-glass pad-tight">

## 📢 **Communication**

A plot is often the first (and sometimes only) thing a reader looks at. It carries your argument. Bad figures undermine credible analysis.

</div>

<div class="card card-info card-glass pad-tight">

## ⚠️ **Deception Prevention**

Understanding visualization principles protects you from being misled — and from accidentally misleading others.

</div>

</div>

---
hideInToc: true
---

# Roadmap for this **Lecture**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **Mechanics**

Aesthetics, legend, axes, coordinate systems — the parts of a plot.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **Chart families**

Amounts, distributions, proportions, associations, trends, uncertainty.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎨 **Design principles**

Data-to-ink, palettes, accessibility, log scale, small multiples.

</div>

<div class="card card-info card-glass pad-compact">

## 📖 **Telling a story**

Title as finding, annotations, rainbow pitfalls, less-ink-same-data.

</div>

<div class="card card-success card-glass pad-compact">

## 🐍 **Hands-on**

Matplotlib from scratch — figure/axes, bars, scatter, histograms, saving.

</div>

<div class="card card-warning card-glass pad-compact">

## 🏋️ **Practice**

A checklist and an exercise to take away — build one of these yourself.

</div>

</div>

---
hideInToc: true
---

# Anscombe's **Quartet** — summary stats lie

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four datasets with the **same** mean, variance, correlation, and regression line. You only spot the difference by *plotting* them.

</div>

<img class="fig" src="/figures/cwilke_distributions_i_anscombes_quartet.svg" style="display:block;margin:0 auto;max-height:380px;">

---
hideInToc: true
---

# The **Perceptual Hierarchy**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Not all visual channels are equal**

Cleveland & McGill's experiments ranked how accurately humans decode different visual encodings of quantity. Put the signal on the most accurate channel available.

</div>

<div class="stack-tight mt-md">

<div class="card card-success card-glass pad-compact">

🥇 **Position along a common scale** (bar chart, scatter plot) — most accurate

</div>

<div class="card card-primary card-glass pad-compact">

🥈 **Position on identical non-aligned scales** (small multiples) — very good

</div>

<div class="card card-secondary card-glass pad-compact">

🥉 **Length** (stacked bars) — good, but harder than unaligned positions

</div>

<div class="card card-accent card-glass pad-compact">

**Angle · slope · area** (pie, bubble) — poor; human angle/area judgement is unreliable

</div>

<div class="card card-warning card-glass pad-compact">

**Colour saturation · hue** (heatmap) — worst; use only as a fallback or a third dimension

</div>

</div>

---
hideInToc: true
---

# **Aesthetics** of Data Visualization

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Data points are mapped to visual properties — **position**, **colour**, **shape**, **size**, **line style**. Choosing these mappings well is the core skill.

</div>

<img class="fig" src="/figures/cwilke_aesthetic_mapping_iris_aesthetics.svg" style="display:block;margin:0 auto;max-height:310px;">

---
hideInToc: true
---

# The **Visual Channels**

<div class="card card-info card-glass pad-compact mt-sm">

📐 Every plot maps one or more data variables to a **visual channel**: position on x, position on y, colour, shape, size, line style. The aesthetic mapping is the contract between your data and what the reader sees.

</div>

<img class="fig" src="/figures/cwilke_aesthetic_mapping_common_aesthetics.svg" style="display:block;margin:0 auto;max-height:320px;">

---
layout: iframe
hideInToc: true
disabled: true
url: https://datavizcatalogue.com/
---

---
hideInToc: true
layout: image
backgroundSize: cover
image: /figures/data_vis_anatomy_of_a_figure.svg
---

---
hideInToc: true
---

# **Legend**

<div class="card card-info card-glass pad-tight mt-sm">

## 🏷️ **What is a Legend?**

A legend is a key component of a plot that explains the meaning of the data. It maps visual encodings (colors, shapes, sizes) to their semantic meaning.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

📌 Legend might **not be necessary** if the data is self-explanatory (e.g. bar chart, single-line plot, direct annotations)

</div>

<div class="card card-secondary card-glass pad-compact">

📍 Legend should be **placed** so it does not obscure the data

</div>

<div class="card card-accent card-glass pad-compact">

👁️ Legend should be **easy to read** and understand

</div>

<div class="card card-success card-glass pad-compact">

🎨 Legend should be **consistent** with the overall design of the plot

</div>

<div class="card card-warning card-glass pad-compact">

🔑 Legend should explain **colors, shapes, sizes**, and other visual encodings used in the plot

</div>

</div>

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Legend placement obscures the data — it overlaps with the plotted points

</div>

<img class="fig" src="/figures/data_vis_legend_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Too many legend entries make the chart unreadable — consider direct labeling or grouping

</div>

<img class="fig" src="/figures/data_vis_legend_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Legend placed outside the plot area — data is fully visible and the legend is easy to read

</div>

<img class="fig" src="/figures/data_vis_legend_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Clean legend with well-chosen colors and clear labels — each group is easily distinguishable

</div>

<img class="fig" src="/figures/data_vis_legend_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Bad vs **Good** Axis Labelling

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ Same data, same curve — only the axis labelling differs. Units, readable ticks, and a zero baseline turn a cryptic sketch into a figure that stands on its own.

</div>

<img class="fig" src="/figures/cwilke_coordinates_axes_axes_labels_bad_good.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Axis Labels**: Make Them Readable

<div class="card card-info card-glass pad-compact mt-sm">

🔍 Same scatter, same data — only the tick-label and axis-title font size differs. Tiny labels look "professional" in a paper margin but vanish when projected on a lecture-room wall.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_small_axis_labels_aus_athletes_too_small.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Too small** — unreadable at 5 m

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_small_axis_labels_aus_athletes_balanced.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Balanced** — labels in proportion to data

</div>

</div>

---
hideInToc: true
---

# Choose the **Coordinate System**

<div class="card card-info card-glass pad-compact mt-sm">

🧭 Periodic data (days of the year, hours of the day, compass bearings) lives naturally on a circle. Pick the geometry that matches the phenomenon.

</div>

<img class="fig" src="/figures/cwilke_coordinates_axes_polar_vs_cartesian.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Aspect Ratio** Matters

<div class="card card-info card-glass pad-compact mt-sm">

📐 The *same* temperature series, drawn at three different aspect ratios. Tall-and-thin exaggerates swings; short-and-wide flattens them. Banking to ≈ 45° (Cleveland's rule) makes slope comparisons most accurate.

</div>

<img class="fig" src="/figures/cwilke_coordinates_axes_houston_temps_aspect_ratios.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Visualizing **Amounts**

<div class="card card-info card-glass pad-tight mt-sm">

## 📊 **Common Chart Types for Amounts**

When your data represents quantities associated with categories, these are the go-to visualizations:

</div>

<div class="grid-2 mt-md gap-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

📊 **Bar Charts** — Compare values across categories

</div>

<div class="card card-secondary card-glass pad-compact">

📊 **Grouped Bar Charts** — Compare sub-groups side by side

</div>

</div>

<div class="stack-tight">

<div class="card card-accent card-glass pad-compact">

📊 **Stacked Bar Charts** — Show part-to-whole relationships

</div>

<div class="card card-warning card-glass pad-compact">

🌡️ **Heat Maps** — Encode values as color intensity in a grid

</div>

</div>

</div>

---
hideInToc: true
---

# What's **Wrong?** — rotated labels

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Vertical bars force long category labels to rotate, hurting legibility. Switch to a **horizontal** bar chart (or a dot plot) and every label stays readable.

</div>

<img class="fig" src="/figures/cwilke_amounts_boxoffice_rotated_bad.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# A **Good** Bar Chart

<div class="card card-info card-glass pad-compact mt-sm">

🎬 Weekend box-office gross. Horizontal bars, zero-based axis, sorted by value — the eye reads the ranking immediately and the magnitudes honestly.

</div>

<img class="fig" src="/figures/cwilke_amounts_boxoffice_horizontal.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Truncated y-axis — **bars lie**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Bars do not start at zero — this exaggerates differences and misleads the viewer

</div>

<img class="fig" src="/figures/cwilke_proportional_ink_truncated_bar_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Y-axis starts at zero — bar lengths accurately represent the data values

</div>

<img class="fig" src="/figures/cwilke_proportional_ink_truncated_bar_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Categories are unsorted — makes it hard to compare values or spot patterns

</div>

<img class="fig" src="/figures/data_vis_bar_chart_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Bars sorted by value — trends and rankings are immediately visible

</div>

<img class="fig" src="/figures/cwilke_amounts_boxoffice_horizontal.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Stacking makes individual group comparisons difficult — consider grouped bars instead

</div>

<img class="fig" src="/figures/data_vis_bar_chart_error_3.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# Stacked **Bar Charts**

<div class="card card-info card-glass pad-compact mt-sm">

📊 Stacked bars work well for **part-to-whole** comparisons — each segment shows a proportion of the total

</div>

<img class="fig" src="/figures/cwilke_amounts_students_stacked_bars.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# 3D Effects **Distort Magnitude**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ 3D effects distort perception — bar heights become ambiguous and comparisons unreliable

</div>

<img class="fig" src="/figures/cwilke_no_3d_jitter_bar_3d_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Clean 2D bars with distinct colors and clear labels — easy to read and compare

</div>

<img class="fig" src="/figures/cwilke_no_3d_jitter_bar_2d_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Cleveland Dot Plots** — the sober bar

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Replaces the bar with a single dot per category, usually on a horizontal axis with labels on the left. Advantages over bars when **n** is large: less ink, labels stay horizontal, and the reader's eye snaps to a point rather than scanning a bar edge. No implicit zero-base requirement either — you can truncate honestly because a dot, unlike a bar, doesn't encode magnitude by length.

</div>

<img class="fig" src="/figures/cwilke_amounts_cleveland_dot_plot.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Life Expectancy — **Alphabetical Order**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Same life-expectancy data, but countries listed **alphabetically**. The ordering tells the reader nothing about the values — ranking, outliers, and the overall shape of the distribution are all lost in the noise.

</div>

<img class="fig" src="/figures/cwilke_amounts_lifeexp_alpha_order_bad.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Life Expectancy — **Bars (Still Bad)**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Now sorted — progress — but **bars are the wrong chart type** for this data. Values cluster between 60 and 81 years, so every bar is long and all bars are nearly the same length. The eye lands in the *middle* of the bars and the real differences between countries are lost.

</div>

<img class="fig" src="/figures/cwilke_amounts_lifeexp_bars_bad.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Life Expectancy — **Sorted by Value**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Same data, dots placed on a common horizontal scale with countries **sorted by value** — the ranking, spread, and outliers are all readable at a glance.

</div>

<img class="fig" src="/figures/cwilke_amounts_lifeexp_dot_plot.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Poor color choices — rainbow palettes can confuse meaning and are not accessible to colorblind viewers

</div>

<img class="fig" src="/figures/cwilke_color_colorblind_simulation.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/cwilke_amounts_health_heatmap.svg
---

---
hideInToc: true
---

# **Histograms**

<div class="card card-info card-glass pad-tight mt-sm">

## 📈 **What are Histograms?**

Histograms visualize the **distribution** of a single continuous variable by dividing the data range into bins and counting observations in each bin.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

📏 Histograms should have appropriate **bin widths** to show the shape of the distribution

</div>

<div class="card card-secondary card-glass pad-compact">

🏷️ Histograms should have **clear labels and titles**

</div>

<div class="card card-accent card-glass pad-compact">

🎨 Histograms should be **consistent** with the overall design of the plot

</div>

<div class="card card-success card-glass pad-compact">

🔍 Histograms should be used to identify **patterns, trends, and outliers** in the data

</div>

</div>

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/cwilke_distributions_i_titanic_density.svg
---

---
hideInToc: true
disabled: true
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_comp.png
---

---
hideInToc: true
---

# Bin **Width Matters**

<div class="card card-info card-glass pad-compact mt-sm">

📏 Same data (Titanic passenger ages), four bin widths. Too narrow and the histogram looks like noise; too wide and the shape disappears. There is no universally "right" bin width — always try a few.

</div>

<img class="fig" src="/figures/cwilke_distributions_i_titanic_hist_binwidth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
disabled: true
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_scientific_1.png
---

---
hideInToc: true
disabled: true
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_scientific_2.png
---

---
hideInToc: true
---

# Visualising **Distributions** — three views

<div class="card card-info card-glass pad-compact mt-sm">

📦 Same data shown three ways. As you move from boxplot to strip, you lose summary clarity but gain fidelity to the raw data.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_distributions_ii_mpg_boxplot.svg" style="display:block;margin:0 auto;max-height:170px;">

📦 **Boxplot** — box = IQR (Q1→Q3), line = median, whiskers = 1.5 × IQR, dots = outliers

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_distributions_ii_mpg_violin.svg" style="display:block;margin:0 auto;max-height:170px;">

🎻 **Violin** — mirrored kernel density; width ∝ point density, so bimodality is visible

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_distributions_ii_mpg_strip_jitter.svg" style="display:block;margin:0 auto;max-height:170px;">

〰️ **Strip + jitter** — every point plotted; small horizontal jitter avoids stacking

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 **Rule of thumb:** boxplot for quick summaries, violin when shape matters (skew, multiple modes), strip when *n* is small enough to show every observation.

</div>

---
hideInToc: true
---

# Empirical **CDF**

<div class="card card-info card-glass pad-compact mt-sm">

📈 Plot each value's rank / *n* against the value: for every *x*, the curve's *y* is **the fraction of observations ≤ x**. No bin-width choices, no density estimation, and every data point contributes one step. The median is where the curve crosses 0.5; quartiles are at 0.25 / 0.75; outliers show as flat tails.

</div>

<img class="fig" src="/figures/cwilke_distributions_i_titanic_ecdf.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Q–Q** Plots — does it look Normal?

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **How to read one**

Plot the **data's quantiles** against the **theoretical quantiles** of a reference (usually Normal). If the data matches the reference, the points fall on the diagonal.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

- **On the line** → data is Normal
- **S-curve** → heavy tails (more extreme values than Normal)
- **Inverted-S** → light tails (compressed)
- **Upward bend** → right-skew; **downward** → left-skew

</div>

<div>

<img class="fig" src="/figures/cwilke_distributions_i_qq_plot.svg" style="display:block;margin:0 auto;max-height:290px;">

</div>

</div>

---
hideInToc: true
---

# **Ridgeline** Plots — shape at a glance

<div class="card card-info card-glass pad-compact mt-sm">

🎢 One smoothed density curve **per group**, stacked with a small vertical offset so they overlap slightly. Great for 5–20 groups where you want to spot drift in the mode, shift in spread, or new bumps appearing over time.

</div>

<img class="fig" src="/figures/cwilke_distributions_ii_ridgeline.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Filled **Density** beats Line Density

<div class="card card-info card-glass pad-compact mt-sm">

🎨 For overlaid densities, **transparent fill** reads faster than coloured lines alone. Lines force the eye to trace each curve; fills make each group's area pre-attentive. Direct labels on the fills let you drop the legend too.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_avoid_line_drawings_iris_densities_lines.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Lines only** — slower to read, species swap harder

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_avoid_line_drawings_iris_densities_filled.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Filled** — species instantly separable

</div>

</div>

---
hideInToc: true
---

# Temperatures as a **Heatmap**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ Day-of-year (x) × location (y), colour = mean temperature. A well-chosen sequential palette turns a matrix of numbers into a single image where seasonality and climate differences pop at once.

</div>

<img class="fig" src="/figures/cwilke_aesthetic_mapping_temp_normals_heatmap.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Proportions**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧩 **Three ways, one story**

Same three-category breakdown shown as pie, stacked bar, and side-by-side bars. Pie charts force angle comparison (hard); bars let the reader read values directly.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_proportions_pie_bad.svg" style="display:block;margin:0 auto;max-height:200px;">

🥧 **Pie** — angles are hard

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_proportions_proportions_stacked_bar.svg" style="display:block;margin:0 auto;max-height:200px;">

📚 **Stacked** — part-to-whole

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_proportions_proportions_side_by_side_bars.svg" style="display:block;margin:0 auto;max-height:200px;">

📊 **Side-by-side** — easy to compare

</div>

</div>

---
hideInToc: true
---

# When Pies **Actually Work**

<div class="card card-info card-glass pad-compact mt-sm">

🥧 Pies work when the "whole" is unambiguous and the parts sum to an obviously complete 100%. The 1976 German Bundestag: four parties, one legislature, a simple supermajority story.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_proportions_marketshare_pies_bad.svg" style="display:block;margin:0 auto;max-height:240px;">

❌ **Fails** — comparing many pies with similar wedge sizes

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_proportions_bundestag_pie_good.svg" style="display:block;margin:0 auto;max-height:240px;">

✅ **Works** — one whole, ≤5 parts, clear majority claim

</div>

</div>

---
hideInToc: true
---

# **Treemap** — hierarchy by area

<div class="card card-info card-glass pad-compact mt-sm">

🗂️ When a proportion has **nested structure** (categories within categories), a treemap packs the whole hierarchy into one figure. Each rectangle's area is proportional to its value.

</div>

<img class="fig" src="/figures/cwilke_proportions_treemap.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Visualising **Associations**

<div class="card card-info card-glass pad-tight mt-sm">

## 🔵 **Scatter plot — the default for two continuous variables**

Each point is one observation. Look for **trend** (does y rise with x?), **spread** (how tight is the cloud?), **clusters** (natural groupings?), and **outliers** (points far from the rest). Colour or shape can add a third, categorical dimension — here, sex of the blue jay.

</div>

<img class="fig" src="/figures/cwilke_associations_blue_jays_scatter.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# **Bubble Chart** — a third dimension

<div class="card card-info card-glass pad-compact mt-sm">

🫧 Encode a third continuous variable as **marker size**. Humans read area less accurately than position — reserve the bubble encoding for the least-important variable, and scale marker *area* (not radius) proportional to value.

</div>

<img class="fig" src="/figures/cwilke_associations_blue_jays_bubble.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# When **Points Overlap**

<div class="card card-info card-glass pad-tight mt-sm">

## 🫧 **Three fixes for overplotting**

Raw scatter · jitter + transparency · 2-D density. As point count grows, the same data shows completely different stories depending on technique.

</div>

<img class="fig" src="/figures/cwilke_no_3d_jitter_overplot_jitter_alpha.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Big Data? **Bin It**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 Past ~10 000 points jitter + alpha saturates into a blob. **Hex binning** divides the plane into hexagons (better packing than squares, no orientation bias) and colours each by the number of points falling inside — structure stays visible at millions of points.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_overlapping_points_nycflights_points.svg" style="display:block;margin:0 auto;max-height:240px;">

🚫 **Raw scatter** — 300 k NYC flight delays collapse into a blob

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_overlapping_points_nycflights_hex_bins.svg" style="display:block;margin:0 auto;max-height:240px;">

✅ **Hex bins** — density becomes the story

</div>

</div>

---
hideInToc: true
---

# **Correlation** heatmap

<div class="card card-info card-glass pad-compact mt-sm">

🔥 For a quick overview of pairwise linear relationships, plot the correlation matrix as a heatmap — diverging colour centred at zero.

</div>

<img class="fig" src="/figures/cwilke_associations_mtcars_corr_heatmap.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Pair Plot / **Correlogram**

<div class="card card-info card-glass pad-compact mt-sm">

🔲 A grid of pairwise scatters (with densities on the diagonal) lets you eyeball every bivariate relationship in one screen. Essential first look at a new multi-variable dataset.

</div>

<img class="fig" src="/figures/cwilke_multi_panel_correlogram.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# **Slopegraph** — two points, many stories

<div class="card card-info card-glass pad-compact mt-sm">

📈 Show the *change* of a variable between two time points by connecting each category's before and after with a straight line. Slope = direction and magnitude of change; crossings highlight reversals.

</div>

<img class="fig" src="/figures/cwilke_associations_co2_slopegraph.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Trends**

<div class="card card-info card-glass pad-tight mt-sm">

## 📉 **Show the data and the trend together**

Raw observations + a smoothed curve is usually more honest than either alone. Make the smoothing visible, not hidden.

</div>

<img class="fig" src="/figures/cwilke_trends_lincoln_temps_raw_smooth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Separating **Seasonality from Trend**

<div class="card card-info card-glass pad-compact mt-sm">

🔁 Detrending — subtracting a slow-moving component — exposes the repeating seasonal structure the raw series can hide.

</div>

<img class="fig" src="/figures/cwilke_trends_detrended_price.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Time on the **x-axis**

<div class="card card-info card-glass pad-compact mt-sm">

📈 By convention, **time runs left-to-right on the x-axis** — readers parse this instinctively. Keep the x-axis continuous; do not sort by y.

</div>

<img class="fig" src="/figures/cwilke_trends_keeling_curve.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Trend + **Seasonality** Decomposition

<div class="card card-info card-glass pad-compact mt-sm">

🔬 The Keeling curve isn't one signal — it's a slow upward trend **plus** an annual breathing cycle **plus** residual noise. Decomposing makes each visible on its own terms.

</div>

<img class="fig" src="/figures/cwilke_trends_keeling_decomposition.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Uncertainty**

<div class="card card-info card-glass pad-compact mt-sm">

📏 Every estimate has error — a report without it is a report that overclaims. Three honest ways to show it, from most common to most modern.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_uncertainty_error_bars.svg" style="display:block;margin:0 auto;max-height:155px;">

📏 **Error bars** — discrete ticks spanning ± 1 or 2 standard errors; good for a few points

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_uncertainty_ci_band.svg" style="display:block;margin:0 auto;max-height:155px;">

🎗️ **CI band** — shaded envelope around a fitted curve; width = 95 % uncertainty

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_uncertainty_hop_demo.svg" style="display:block;margin:0 auto;max-height:155px;">

🎰 **HOP** — overlay many plausible fits; the spread *is* the uncertainty

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 **Pick the one that matches the audience.** Error bars are the scientific norm. Bands work for trends. Hypothetical outcomes are surprisingly intuitive for non-expert readers.

</div>

---
hideInToc: true
---

# Quantile **Dot Plot** — probability you can count

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Lay out N equally-likely outcomes as discrete dots. The reader counts the dots that fall in the region they care about — intuitive, honest, no mis-reading of continuous density.

</div>

<img class="fig" src="/figures/cwilke_uncertainty_election_quantile_dot.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Choosing the **Right Chart**

<div class="card card-info card-glass pad-compact mt-sm">

Match the chart type to the relationship you want to show:

</div>

<div class="grid-2 mt-md gap-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

📊 **Comparison** across categories → Bar chart

</div>

<div class="card card-secondary card-glass pad-compact">

📈 **Trend** over time → Line plot

</div>

<div class="card card-accent card-glass pad-compact">

🔵 **Relationship** between two variables → Scatter plot

</div>

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-compact">

📦 **Distribution** of values → Histogram or box plot

</div>

<div class="card card-success card-glass pad-compact">

🧩 **Part-to-whole** → Stacked bar (NOT pie chart)

</div>

<div class="card card-warning card-glass pad-compact">

🌡️ **Two-variable density** → Heat map

</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 🥧 **A Note on Pie Charts**

Humans are poor at comparing angles and areas. Pie charts are almost always worse than a simple bar chart. Avoid them — use bar charts or stacked bars instead.

</div>

---
hideInToc: true
---

# The **Data-to-Ink Ratio**

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **Edward Tufte's Principle**

> "Above all else, show the data." Every drop of ink on a chart should serve a purpose. The **data-to-ink ratio** = (ink used to display data) / (total ink used in the graphic).

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 🚫 **Chart Junk**

- Unnecessary 3D effects
- Decorative backgrounds and gradients
- Redundant gridlines and borders
- Excessive labels and annotations

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **Clean Design**

- Remove non-data ink (borders, fills, redundant axes)
- Let the data be the visual focus
- Use whitespace intentionally
- Every element earns its place

</div>

</div>

---
hideInToc: true
---

# **Defaults** Are Not Design

<div class="card card-info card-glass pad-compact mt-sm">

🎛️ Plotting libraries ship with safe-but-noisy defaults: heavy grid, grey background, boxed axes. Those are engineered for *universal legibility*, not for communicating a finding. Strip the non-data ink; the figure gets quieter and louder at the same time.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_price_plot_ggplot_default.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Out-of-the-box default** — grey panel, heavy grid

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_price_plot_no_grid.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Clean** — no grid, white background, lines do the work

</div>

</div>

---
hideInToc: true
---

# **Accessibility** in Visualization

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **Colorblind-Safe Palettes**

Approximately 8% of men and 0.5% of women have some form of color vision deficiency. Your plots must be accessible to **all** readers.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Use **colorblind-safe palettes** such as `viridis`, `cividis`, or `plasma` — they are perceptually uniform and distinguishable by colorblind viewers

</div>

<div class="card card-secondary card-glass pad-compact">

🚫 Avoid **red-green** combinations — the most common form of color blindness confuses these two colors

</div>

<div class="card card-accent card-glass pad-compact">

🔲 Use **redundant encodings** — combine color with shape, pattern, or line style so information is not conveyed by color alone

</div>

<div class="card card-warning card-glass pad-compact">

🧪 **Test your plots** — tools like Color Oracle or Coblis can simulate how your figures look to colorblind viewers

</div>

</div>

---
hideInToc: true
---

# Three **Kinds of Palette**

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Pick the palette that matches your data: **qualitative** for categories, **sequential** for ordered magnitudes, **diverging** for signed deviations from a midpoint.

</div>

<div style="display:grid; grid-template-columns: 1fr 2fr; align-items:center; column-gap: 1.5rem; row-gap: 1rem; margin-top: 1.2rem;">

<div>

🎨 **Qualitative** — unordered categories

</div>

<img class="fig" src="/figures/cwilke_color_palette_qualitative.svg" style="width:100%;max-height:70px;">

<div>

📈 **Sequential** — ordered magnitudes

</div>

<img class="fig" src="/figures/cwilke_color_palette_sequential.svg" style="width:100%;max-height:70px;">

<div>

⚖️ **Diverging** — signed deviations from a midpoint

</div>

<img class="fig" src="/figures/cwilke_color_palette_diverging.svg" style="width:100%;max-height:55px;">

</div>

---
hideInToc: true
---

# Use Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Colour draws the eye. Reserve saturated colour for the category you want the reader to see first; leave the rest grey. The same dataset, told differently — one signal up front instead of twelve competing for attention.

</div>

<img class="fig" src="/figures/cwilke_color_popgrowth_us_highlight.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Red-Green **Fails Twice**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Red-green is the most common form of colour-vision deficiency. A plot that relies on red/green contrast is unreadable for ~8 % of men. Simulation (right) shows what a deuteranopic viewer sees.

</div>

<img class="fig" src="/figures/cwilke_pitfalls_of_color_use_red_green_cvd_sim.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Log **Scale**

<div class="card card-info card-glass pad-compact mt-sm">

📐 When values span orders of magnitude, a log axis turns power-law relationships into straight lines and reveals structure a linear axis hides.

</div>

<img class="fig" src="/figures/cwilke_proportional_ink_log_scale.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Square-Root** Scale — for counts

<div class="card card-info card-glass pad-compact mt-sm">

√ When the y-axis is a **count** and the variance grows with the mean (Poisson data), a square-root transform stabilises variance. Cleaner than log when values include zero.

</div>

<img class="fig" src="/figures/cwilke_coordinates_axes_sqrt_scale.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Faceting replaces a crowded single plot with a grid of small, consistent panels — easier comparison, less visual overload.

</div>

<img class="fig" src="/figures/cwilke_multi_panel_small_multiples_gapminder.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Small Multiples — **Share the Scale**

<div class="card card-info card-glass pad-compact mt-sm">

🚢 Titanic survival by class × sex. The key insight — **first-class women almost all survived, third-class men mostly didn't** — only pops out when each panel shares a y-axis. Free-scale faceting makes every panel look "interesting" and hides the real pattern.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_titanic_survival_bad.svg" style="display:block;margin:0 auto;max-height:230px;">

🚫 **Per-panel scales** — the story disappears

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_titanic_survival_good.svg" style="display:block;margin:0 auto;max-height:230px;">

✅ **Shared y-axis** — the class × sex pattern jumps out

</div>

</div>

---
hideInToc: true
---

# Telling a **Story**

<div class="card card-info card-glass pad-tight mt-sm">

## 📖 **Title, subtitle, caption — the plot's voice**

A good title states the finding. The subtitle adds scope. The caption cites the source. Together they make the figure stand alone.

</div>

<img class="fig" src="/figures/cwilke_telling_a_story_story_titles_captions.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Title as the **Finding**

<div class="card card-info card-glass pad-compact mt-sm">

✍️ A title like "*CPI vs HDI*" says what the figure **is**. A title like "*Cleaner government correlates with higher human development*" says what the figure **means**. Prefer the finding.

</div>

<img class="fig" src="/figures/cwilke_telling_a_story_title_as_finding.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Label **Directly**, Drop the Legend

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ A legend forces the reader's eye to **hop** between the plot and the key. Label each line or group **directly on the plot** and the reader stays in one place — fewer cognitive switches, clearer story.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_redundant_coding_tech_stocks_bad_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

🚫 **Legend off to the side** — reader has to look twice

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_redundant_coding_tech_stocks_good_no_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

✅ **Direct labels at the line ends** — one glance

</div>

</div>

---
hideInToc: true
---

# Annotate the **Point You Want Made**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 The same scatter can be plain or annotated. Call out the outlier, the trend, or the decision threshold — don't make the reader hunt for it.

</div>

<img class="fig" src="/figures/cwilke_telling_a_story_annotated_vs_plain.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Add a **Reference Line**

<div class="card card-info card-glass pad-compact mt-sm">

🧬 Wild-type vs mutant mRNA abundance (log–log). Without a reference, the reader has to guess whether mutant &gt; or &lt; wild-type. Drawing the **y = x diagonal** makes deviations — the genes whose expression changed — jump out immediately.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_gene_expression_bad.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **No reference** — deviations are invisible

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_balance_data_context_gene_expression_good.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **y = x diagonal** — off-diagonal points are the finding

</div>

</div>

---
hideInToc: true
---

# Rainbow is **Not a Palette**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ `jet`, `rainbow`, `hsv` — perceptually non-uniform, misleading about magnitude, and terrible for colour-vision deficiency. Use `viridis`, `cividis`, `plasma`, or a categorical palette like **Okabe-Ito** instead.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_pitfalls_of_color_use_rainbow_bad.svg" style="display:block;margin:0 auto;max-height:230px;">

🚫 **Rainbow** — unreadable magnitudes

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/cwilke_pitfalls_of_color_use_rainbow_fix.svg" style="display:block;margin:0 auto;max-height:230px;">

✅ **Okabe-Ito** — clear, colour-blind safe

</div>

</div>

---
hideInToc: true
---

# Less **Ink**, Same Data

<div class="card card-info card-glass pad-compact mt-sm">

✂️ Tufte's data-to-ink ratio in practice: same scatter, same point — but on the right we've removed the box, heavy ticks, and every non-essential gridline. Nothing lost; everything cleaner.

</div>

<img class="fig" src="/figures/cwilke_balance_data_context_grid_vs_no_grid.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# The **Mental Model**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧩 **Figure · Axes · Artists**

Every matplotlib plot has three nested layers. The **Figure** is the whole canvas, an **Axes** is one plotting region on that canvas, and **Artists** (lines, bars, text) live inside the Axes.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖼️ **Figure**

`fig = plt.figure()` — the sheet of paper.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Axes**

`ax = fig.subplots()` — one plot area; has x/y axes, title, legend.

</div>

<div class="card card-accent card-glass pad-compact">

## ✏️ **Artists**

`ax.plot(...)`, `ax.bar(...)`, `ax.scatter(...)` — the data-drawing methods.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 **Rule of thumb:** always create `fig, ax = plt.subplots(...)` and call methods on `ax`. Avoid `plt.plot(...)` — the state-machine interface gets confusing fast.

</div>

---
hideInToc: true
---

# A Minimal **Bar Chart**

```python {all|1-2|4-5|7-9|11-14|all}
import matplotlib.pyplot as plt
import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [22, 25, 31, 28, 36]

fig, ax = plt.subplots(figsize=(6, 3.2))
ax.bar(days, sales, color="#56B4E9", width=0.7)
ax.set(xlabel="weekday", ylabel="sales (M USD)", ylim=(0, 40))

ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
ax.set_axisbelow(True)
for side in ("top", "right", "left"): ax.spines[side].set_visible(False)
fig.savefig("sales.svg", bbox_inches="tight")
```

---
hideInToc: true
---

# Scatter **with a Fit**

```python {all|1-3|5-6|8-10|12-14|all}
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(0)

x = rng.uniform(0, 10, 60)
y = 0.8 * x + rng.normal(0, 1.2, 60)

slope, intercept = np.polyfit(x, y, 1)
xs = np.linspace(0, 10, 100)
ys = slope * xs + intercept

fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.scatter(x, y, s=30, color="#0072B2", alpha=0.85, edgecolor="white", linewidth=0.5)
ax.plot(xs, ys, color="#D55E00", linewidth=2, label=f"y = {slope:.2f} x + {intercept:.2f}")
ax.set(xlabel="x", ylabel="y")
ax.legend(frameon=False)
```

---
hideInToc: true
---

# Histogram + **Density Overlay**

```python {all|1-3|5-6|8-9|11-15|all}
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

rng = np.random.default_rng(1)
data = rng.normal(loc=5, scale=1.5, size=500)

kde = gaussian_kde(data)
xs = np.linspace(data.min(), data.max(), 300)

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.hist(data, bins=25, density=True, color="#56B4E9",
        alpha=0.75, edgecolor="white")
ax.plot(xs, kde(xs), color="#D55E00", linewidth=2, label="kde")
ax.set(xlabel="value", ylabel="density")
ax.legend(frameon=False)
```

---
hideInToc: true
---

# Reusable **Style**

<div class="card card-info card-glass pad-tight mt-sm">

## 🎨 **Set rcParams once, everywhere**

Stop repeating colours and fonts in every plot. Define a style in one place — a module, a `matplotlib` style sheet, or a `rcParams.update(...)` call at the top of your notebook — and every subsequent figure inherits it.

</div>

```python {all|1-5|7-14|all}
import matplotlib as mpl

OKABE_ITO = ["#000000", "#E69F00", "#56B4E9", "#009E73",
             "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

mpl.rcParams.update({
    "font.family": ["Helvetica", "Arial", "DejaVu Sans"],
    "axes.prop_cycle": mpl.cycler(color=OKABE_ITO),
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

# Saving for **Publication**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧩 **Vector** — `.svg`, `.pdf`

`fig.savefig("fig.svg")` → infinite resolution, editable in Illustrator/Inkscape. Use for slides, papers, posters.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🖼️ **Raster** — `.png`

`fig.savefig("fig.png", dpi=150)` → fixed resolution but universal. Use for web, documentation, quick previews.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 **Commit both**: figure out vector for long-term editability, and PNG for reliable rendering. Keep source `.py` alongside — then the figure is **reproducible**, not just a static file.

</div>

---
hideInToc: true
---

# Your Turn — **Pre-Exercise**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧪 **A checklist before you hit save**

Before exporting any figure, run through the next-slide exercise on your own plot. If any answer is "no", the figure isn't finished.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

✅ Is the **chart type** the right one for the question you're answering?

</div>

<div class="card card-secondary card-glass pad-compact">

✅ Do the **axes** have units, and does the scale make sense (zero base, log, etc.)?

</div>

<div class="card card-accent card-glass pad-compact">

✅ Does the **palette** match the data (qualitative / sequential / diverging) and remain accessible?

</div>

<div class="card card-info card-glass pad-compact">

✅ Does the **title** state the finding, not just describe the figure?

</div>

<div class="card card-success card-glass pad-compact">

✅ Is it **reproducible** — source code committed, input data versioned, output regenerable with one command?

</div>

</div>

---
hideInToc: true
---

# Key **Takeaways**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📊 **Design Principles**

- Every visual encoding (color, shape, size) must be **meaningful**
- Axes must be clearly labeled with **units**
- Legends should be **placed carefully** to not obscure data
- Avoid chart junk — maximize the **data-to-ink ratio**
- Use **colorblind-safe palettes** for accessibility

</div>

<div class="card card-secondary card-glass pad-tight">

## 📖 **The figure is your argument**

- A figure is the first — and often the only — thing a reader looks at
- Choose the chart type to match the **question**, not the dataset
- Title states the **finding**; axes show the units; caption cites the source
- Prefer **open** formats: SVG for vector, PNG for raster, both version-controlled
- Good visualization is not decoration — it is **analysis made visible**

</div>

</div>

---
hideInToc: true
---

# Practice **Exercise**

<div class="card card-info card-glass pad-tight mt-sm">

## 🏋️ **Try It Yourself**

Pick any dataset you find interesting (or use one from a previous lecture) and create the following visualizations:

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

**1.** Create a **histogram** of a continuous variable — experiment with different bin widths and observe how the shape changes

</div>

<div class="card card-secondary card-glass pad-compact">

**2.** Create a **bar chart** comparing categories — sort the bars, label the axes, and include units

</div>

<div class="card card-accent card-glass pad-compact">

**3.** Add a **title, axis labels, and a legend** to your plot — make sure someone unfamiliar with your data can understand the figure

</div>

<div class="card card-warning card-glass pad-compact">

**4.** **Critique** your own plot: Does the y-axis start at zero? Is the color palette accessible? Is the legend clear?

</div>

</div>
