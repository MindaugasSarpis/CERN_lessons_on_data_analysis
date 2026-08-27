---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Data Visualisation"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Data Visualisation

##### <span class="aims-badge">🔧 tool-agnostic · 📁 data & files · ♻️ reproducibility</span>

##### Inspired by: C. O. Wilke, *Fundamentals of Data Visualization*

<!--
Speaker: open by asking who has ever squinted at a figure they couldn't read.
Frame the lecture as a craft — the figure is the argument, not decoration. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Great data visualisation is not about making things look pretty — it is about making the **data speak clearly**. A well-designed figure tells a story that numbers alone cannot.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📊 Match the **chart type** to the relationship — amounts, distributions, proportions, trends

</div>

<div class="card card-secondary card-glass pad-compact">

👁️ Encode data on the most accurate **visual channel** — position beats angle and area

</div>

<div class="card card-accent card-glass pad-compact">

🏷️ Label **axes** with units and pick an honest scale — zero base, log, or square-root

</div>

<div class="card card-success card-glass pad-compact">

🎨 Maximise the **data-to-ink ratio** and choose colour-blind-safe palettes

</div>

<div class="card card-warning card-glass pad-compact">

✍️ Tell a **story** — title as the finding, direct labels, a reproducible figure

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. The paired Seminar 10 is where
they build their first real figure from particle-physics data — today is the
"why" and the vocabulary. Set the expectation. (~1 min)
-->

---
hideInToc: true
---

# Why Data Visualisation <span class="gradient-text">**Matters**</span>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 👁️ **Visual Perception**

The human brain processes images far faster than text. A well-designed chart can communicate in seconds what a table of numbers takes minutes to parse.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Pattern Discovery**

Visualisations reveal structure — clusters, trends, outliers, and gaps — that summary statistics alone can hide. Anscombe's quartet is the classic proof.

</div>

<div class="card card-accent card-glass pad-tight">

## 📢 **Communication**

A plot is often the first (and sometimes only) thing a reader looks at. It carries your argument. Bad figures undermine credible analysis.

</div>

<div class="card card-info card-glass pad-tight">

## ⚠️ **Deception Prevention**

Understanding visualisation principles protects you from being misled — and from accidentally misleading others.

</div>

</div>

<!--
Speaker: hammer the last card — the same skills that make an honest figure let
you spot a dishonest one. Anscombe's quartet (next) is the proof. (~1 min)
-->

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

<!--
Speaker: this is the map for the hour — mechanics, chart families, design,
storytelling, then hands-on matplotlib. Tell them we finish with a real figure
they will build in the seminar. (~1 min)
-->

---
hideInToc: true
---

# Anscombe's **Quartet** — summary stats lie

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Four datasets with the **same** mean, variance, correlation, and regression line. You only spot the difference by *plotting* them.

</div>

<img class="fig" src="/figures/viz_distributions_i_anscombes_quartet.svg" style="display:block;margin:0 auto;max-height:380px;">

---
hideInToc: true
---

<MCQ
  question="Four datasets share the same mean, variance, correlation, and regression line — identical summary statistics. What's the first thing you should do before trusting any of them?"
  :options="[
    'Report the summary statistics directly — they already describe the data',
    'Plot the data — visualisation reveals structure the statistics can hide',
    'Compute a higher-order statistic (e.g. skewness) instead',
    'Assume the datasets are equivalent, since their statistics match'
  ]"
  :correct="1"
  explanation="Anscombe's quartet makes exactly this point: identical summary statistics can hide a straight line, a curve, a single outlier, or a vertical cluster. Plotting is the only way to catch the difference."
/>

---
layout: section
hideInToc: true
---

# Mechanics of a **Figure**

<!--
Speaker: the parts of a plot before the families of plots — which visual
channel carries the number, what a legend is for, how axes and coordinate
systems shape the read. Everything later builds on these. (~0.5 min)
-->

---
hideInToc: true
---

# The **Perceptual Hierarchy**

<div class="card card-info card-glass pad-tight mt-sm">

## 👁️ **Not all visual channels are equal**

Cleveland & McGill's classic experiments (1984), extended by later crowdsourced replications (Heer & Bostock 2010), ranked how accurately humans decode different visual encodings of quantity. Put the signal on the most accurate channel available.

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

# **Aesthetics** — the visual channels

<div class="card card-info card-glass pad-compact mt-sm">

🎨 Every plot maps data variables to **visual channels** — position on x, position on y, colour, shape, size, line style. Choosing these mappings well is the core skill: the mapping is the contract between your data and what the reader sees.

</div>

<img class="fig" src="/figures/viz_aesthetic_mapping_common_aesthetics.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Anatomy of a **Figure** — every element earns its place

<div class="anatomy-stack mt-md">
  <img src="/figures/viz_anatomy_stage1.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage2.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage3.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage4.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage5.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage6.svg" alt="">
</div>

<!--
Click through: frame → axes with units → the data → its uncertainty →
the annotation that makes the point → the title that states the finding.
If an element doesn't earn its place, it goes.
-->

<style>
.anatomy-stack { position: relative; max-width: 82%; margin-inline: auto; }
.anatomy-stack img { width: 100%; display: block; }
.anatomy-layer { position: absolute; inset: 0; }
</style>

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
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Legend placement obscures the data — it overlaps with the plotted points

</div>

<img class="fig fig-light" src="/figures/data_vis_legend_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Legend placed outside the plot area — data is fully visible and the legend is easy to read

</div>

<img class="fig fig-light" src="/figures/data_vis_legend_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Bad vs **Good** Axis Labelling

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ Same data, same curve — only the axis labelling differs. Units, readable ticks, and a zero baseline turn a cryptic sketch into a figure that stands on its own.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_axes_labels_bad_good.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Axis Labels**: Make Them Readable

<div class="card card-info card-glass pad-compact mt-sm">

🔍 Same scatter, same data — only the tick-label and axis-title font size differs. Tiny labels look "professional" in a paper margin but vanish when projected on a lecture-room wall.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_too_small.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Too small** — unreadable at 5 m

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_small_axis_labels_aus_athletes_balanced.svg" style="display:block;margin:0 auto;max-height:210px;">

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

<img class="fig" src="/figures/viz_coordinates_axes_polar_vs_cartesian.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Aspect Ratio** Matters

<div class="card card-info card-glass pad-compact mt-sm">

📐 The *same* temperature series, drawn at three aspect ratios. Tall-and-thin exaggerates the slopes; wide keeps the day-to-day change readable. Banking to ≈ 45° (Cleveland's rule) makes slope comparisons most accurate.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_houston_temps_aspect_ratios.svg" style="display:block;margin:0 auto;max-height:320px;">

---
layout: section
hideInToc: true
---

# Chart **Families**

<!--
Speaker: now the families — amounts, distributions, proportions,
associations, trends, uncertainty. For each: the default chart, the classic
mistake, and the fix. (~0.5 min)
-->

---
hideInToc: true
---

# What's **Wrong?** — rotated labels

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Vertical bars force long category labels to rotate, hurting legibility. Switch to a **horizontal** bar chart (or a dot plot) and every label stays readable.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_rotated_bad.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# A **Good** Bar Chart

<div class="card card-info card-glass pad-compact mt-sm">

🎬 Weekend box-office gross. Horizontal bars, zero-based axis, sorted by value — the eye reads the ranking immediately and the magnitudes honestly.

</div>

<img class="fig" src="/figures/viz_amounts_boxoffice_horizontal.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Truncated y-axis — **bars lie**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Bars do not start at zero — this exaggerates differences and misleads the viewer

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Y-axis starts at zero — bar lengths accurately represent the data values

</div>

<img class="fig" src="/figures/viz_proportional_ink_truncated_bar_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Age groups are **ordinal** — sorting them by value scrambles the natural order. Sort by value only for nominal categories.

</div>

<img class="fig fig-light" src="/figures/data_vis_bar_chart_error_3.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Stacked **Bars** — part-to-whole

<div class="card card-info card-glass pad-compact mt-sm">

📊 Stacked bars show **part-to-whole** — each segment is a share of the total. Totals read off the bar tops; only the bottom segment has a common baseline, so compare the others with care.

</div>

<img class="fig" src="/figures/viz_amounts_students_stacked_bars.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# 3D Effects **Distort Magnitude**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ 3D effects distort perception — bar heights become ambiguous and comparisons unreliable

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_3d_bad.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Clean 2D bars, one colour, value labels — easy to read, easy to compare

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_bar_2d_fixed.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Cleveland Dot Plots** — the sober bar

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Replaces the bar with a single dot per category, usually on a horizontal axis with labels on the left. Advantages over bars when **n** is large: less ink, labels stay horizontal, and the reader's eye snaps to a point rather than scanning a bar edge. No implicit zero-base requirement either — you can truncate honestly because a dot, unlike a bar, doesn't encode magnitude by length.

</div>

<img class="fig" src="/figures/viz_amounts_cleveland_dot_plot.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Life Expectancy — **Alphabetical Order**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Same life-expectancy data, but countries listed **alphabetically**. The ordering tells the reader nothing about the values — ranking, outliers, and the overall shape of the distribution are all lost in the noise.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_alpha_order_bad.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# Life Expectancy — **Bars (Still Bad)**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Now sorted — progress — but **bars are the wrong chart type** for this data. Values cluster between 60 and 81 years, so every bar is long and all bars are nearly the same length. The eye lands in the *middle* of the bars and the real differences between countries are lost.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_bars_bad.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# Life Expectancy — **Sorted by Value**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Same data, dots placed on a common horizontal scale with countries **sorted by value** — the ranking, spread, and outliers are all readable at a glance.

</div>

<img class="fig" src="/figures/viz_amounts_lifeexp_dot_plot.svg" style="display:block;margin:0 auto;max-height:360px;">

---
hideInToc: true
---

# **Density** — a smoothed histogram

<div class="card card-info card-glass pad-compact mt-sm">

📈 A kernel density estimate smooths the histogram of a single continuous variable into a curve — here Titanic passenger ages. Easier to read than bars, but the smoothing bandwidth is a choice, exactly like bin width.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_density.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Bin **Width Matters**

<div class="card card-info card-glass pad-compact mt-sm">

📏 Same data (Titanic passenger ages), three bin widths. Too narrow and the histogram looks like noise; too wide and the shape disappears. There is no universally "right" bin width — always try a few.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_hist_binwidth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Try It — **Bin Width**

```python {monaco-run} {autorun:false}
import numpy as np, matplotlib.pyplot as plt
rng = np.random.default_rng(7)
data = np.concatenate([rng.normal(0, 1, 800), rng.normal(4, 0.5, 300)])

BINS = 30          # <-- try 5, 30, 200
fig, ax = plt.subplots()
ax.hist(data, bins=BINS)
ax.set(xlabel="value", ylabel="count", title=f"bins = {BINS}")
plt.show()
```

---
hideInToc: true
---

# Visualising **Distributions** — three views

<div class="card card-info card-glass pad-compact mt-sm">

📦 Same data shown three ways. As you move from boxplot to strip, you lose summary clarity but gain fidelity to the raw data.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_boxplot.svg" style="display:block;margin:0 auto;max-height:170px;">

📦 **Boxplot** — box = middle 50 % (the IQR), line = median; whiskers reach the furthest point within 1.5 × IQR, beyond = outliers. Formalised in the next lecture (Lecture 11).

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_violin.svg" style="display:block;margin:0 auto;max-height:170px;">

🎻 **Violin** — a mirrored density outline, wide where data is dense — reveals two-humped (bimodal) shapes a boxplot hides

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_distributions_ii_mpg_strip_jitter.svg" style="display:block;margin:0 auto;max-height:170px;">

〰️ **Strip + jitter** — every point plotted; small horizontal jitter avoids stacking

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 **Rule of thumb:** boxplot for quick summaries, violin when shape matters, strip when *n* is small enough to show every point.

</div>

---
hideInToc: true
---

# Empirical **CDF**

<div class="card card-info card-glass pad-compact mt-sm">

📈 An **empirical cumulative distribution function (ECDF)**: for any value *x*, the curve's *y* is **the fraction of observations ≤ x**. No bin-width choice, no density estimation — every data point contributes one step. The median is where the curve crosses 0.5; quartiles are at 0.25 / 0.75; outliers show as flat tails.

</div>

<img class="fig" src="/figures/viz_distributions_i_titanic_ecdf.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# **Q–Q** Plots — does it look Normal?

<div class="grid-2 mt-sm gap-md">

<div class="card card-info card-glass pad-tight">

## 📐 **How to read one**

Plot the data's quantiles against a reference distribution's (usually Normal, formalised in the next lecture, Lecture 11). Points on the line = good match.

- **On the line** → data is Normal
- **S-curve** → heavy tails (more extreme values)
- **Inverted S** → light tails (compressed)
- **Upward bend** → right-skew; **downward** → left-skew

</div>

<div>

<img class="fig" src="/figures/viz_distributions_i_qq_plot.svg" style="display:block;margin:0 auto;max-height:400px;">

</div>

</div>

---
hideInToc: true
---

# **Ridgeline** Plots — shape at a glance

<div class="card card-info card-glass pad-compact mt-sm">

🎢 One smoothed density curve **per group**, stacked with a small vertical offset so they overlap slightly. Great for 5–20 groups where you want to spot drift in the mode, shift in spread, or new bumps appearing over time.

</div>

<img class="fig" src="/figures/viz_distributions_ii_ridgeline.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# Filled **Density** beats Line Density

<div class="card card-info card-glass pad-compact mt-sm">

🎨 For overlaid densities, **transparent fill** reads faster than coloured lines alone. Lines force the eye to trace each curve; fills make each group's area pre-attentive. Direct labels on the fills let you drop the legend too.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_lines.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **Lines only** — slower to read, species harder to tell apart

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_avoid_line_drawings_iris_densities_filled.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **Filled** — species instantly separable

</div>

</div>

---
hideInToc: true
---

# Temperatures as a **Heatmap**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ Month (x) × location (y), colour = mean temperature. A well-chosen sequential palette turns a matrix of numbers into a single image where seasonality and climate differences pop at once.

</div>

<img class="fig" src="/figures/viz_aesthetic_mapping_temp_normals_heatmap.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Proportions**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧩 **Three ways, one story**

Same six-category breakdown shown as pie, stacked bar, and side-by-side bars. Pie charts force angle comparison (hard); bars let the reader read values directly.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_pie_bad.svg" style="display:block;margin:0 auto;max-height:230px;">

🥧 **Pie** — angles are hard

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_stacked_bar.svg" style="display:block;margin:0 auto;max-height:230px;">

📚 **Stacked** — part-to-whole

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_proportions_side_by_side_bars.svg" style="display:block;margin:0 auto;max-height:230px;">

📊 **Side-by-side** — easy to compare

</div>

</div>

---
hideInToc: true
---

# When Pies **Actually Work**

<div class="card card-info card-glass pad-compact mt-sm">

🥧 Pies work when the "whole" is unambiguous and the parts sum to an obviously complete 100%. The 1976 German Bundestag: three groups (CDU/CSU, SPD, FDP), one legislature — the SPD–FDP coalition's **slim majority** is the whole story.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_marketshare_pies_bad.svg" style="display:block;margin:0 auto;max-height:240px;">

❌ **Fails** — comparing many pies with similar wedge sizes

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_proportions_bundestag_pie_good.svg" style="display:block;margin:0 auto;max-height:240px;">

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

<img class="fig" src="/figures/viz_proportions_treemap.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Visualising **Associations**

<div class="card card-info card-glass pad-tight mt-sm">

## 🔵 **Scatter plot — the default for two continuous variables**

Each point is one observation. Look for **trend** (does y rise with x?), **spread** (how tight is the cloud?), **clusters** (natural groupings?), and **outliers** (points far from the rest). Colour or shape can add a third, categorical dimension — here, penguin species.

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_scatter.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# **Bubble Chart** — a third dimension

<div class="card card-info card-glass pad-compact mt-sm">

🫧 Encode a third continuous variable as **marker size**. Humans read area less accurately than position — reserve the bubble encoding for the least-important variable, and scale marker *area* (not radius) proportional to value.

</div>

<img class="fig" src="/figures/viz_associations_blue_jays_bubble.svg" style="display:block;margin:0 auto;max-height:320px;">

---
hideInToc: true
---

# When **Points Overlap**

<div class="card card-info card-glass pad-tight mt-sm">

## 🫧 **Three fixes for overplotting**

Raw scatter · jitter + transparency · 2-D density. As point count grows, the same data shows completely different stories depending on technique.

</div>

<img class="fig" src="/figures/viz_no_3d_jitter_overplot_jitter_alpha.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Big Data? **Bin It**

<div class="card card-info card-glass pad-compact mt-sm">

🫘 Past ~10 000 points jitter + alpha saturates into a blob. **Hex binning** divides the plane into hexagons (better packing than squares, no orientation bias) and colours each by the number of points falling inside — structure stays visible at millions of points.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_points.svg" style="display:block;margin:0 auto;max-height:240px;">

🚫 **Raw scatter** — 20 000 NYC flight delays collapse into a blob

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_overlapping_points_nycflights_hex_bins.svg" style="display:block;margin:0 auto;max-height:240px;">

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

<img class="fig" src="/figures/viz_associations_mtcars_corr_heatmap.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Pair Plot / **Correlogram**

<div class="card card-info card-glass pad-compact mt-sm">

🔲 A grid of pairwise scatters (with histograms on the diagonal) lets you eyeball every bivariate relationship in one screen. Essential first look at a new multi-variable dataset.

</div>

<img class="fig" src="/figures/viz_multi_panel_correlogram.svg" style="display:block;margin:0 auto;max-height:390px;">

---
hideInToc: true
---

# **Slopegraph** — two points, many stories

<div class="card card-info card-glass pad-compact mt-sm">

📈 Show the *change* of a variable between two time points by connecting each category's before and after with a straight line — here tonnes of CO₂ per person. Slope = direction and magnitude of change; crossings highlight reversals.

</div>

<img class="fig" src="/figures/viz_associations_co2_slopegraph.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Trends**

<div class="card card-info card-glass pad-tight mt-sm">

## 📉 **Show the data and the trend together**

Raw observations + a smoothed curve is usually more honest than either alone — make the smoothing visible, not hidden. By convention **time runs left-to-right on the x-axis**; keep it continuous and never sort by y.

</div>

<img class="fig" src="/figures/viz_trends_lincoln_temps_raw_smooth.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Trend + **Seasonality** Decomposition

<div class="card card-info card-glass pad-compact mt-sm">

🔬 The Keeling curve isn't one signal — it's a slow upward trend **plus** an annual breathing cycle **plus** residual noise. Decomposing makes each visible on its own terms.

</div>

<img class="fig" src="/figures/viz_trends_keeling_decomposition.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Visualising **Uncertainty**

<div class="card card-info card-glass pad-compact mt-sm">

📏 Every estimate has error — a report without it is a report that overclaims. Three honest ways to show it, from most common to most modern.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_error_bars.svg" style="display:block;margin:0 auto;max-height:140px;">

📏 **Error bars** — ticks spanning ± 1 or 2 standard errors (defined in the next lecture, Lecture 11); smaller bar = more certain

</div>

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_ci_band.svg" style="display:block;margin:0 auto;max-height:140px;">

🎗️ **CI band** — shaded envelope around a fitted curve; width = 95 % uncertainty

</div>

<div class="card card-accent card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_uncertainty_hop_demo.svg" style="display:block;margin:0 auto;max-height:140px;">

🎰 **HOP (hypothetical outcome plot)** — overlay many plausible fits; the spread *is* the uncertainty

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 **Match the audience.** Error bars are the scientific norm; bands work for trends; HOPs are surprisingly intuitive for non-expert readers.

</div>

---
hideInToc: true
---

# Quantile **Dot Plot** — probability you can count

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Lay out N equally-likely outcomes as discrete dots. The reader counts the dots that fall in the region they care about — intuitive, honest, no mis-reading of continuous density.

</div>

<img class="fig" src="/figures/viz_uncertainty_election_quantile_dot.svg" style="display:block;margin:0 auto;max-height:330px;">

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

🧩 **Part-to-whole** → Stacked bar (pie only for one whole with ≤5 parts)

</div>

<div class="card card-warning card-glass pad-compact">

🌡️ **Two-variable density** → Heat map

</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## 🥧 **A Note on Pie Charts**

Humans are poor at comparing angles and areas, so a pie is almost always worse than a simple bar chart — unless the whole is unambiguous and the parts are few (see "When Pies Actually Work").

</div>

---
layout: section
hideInToc: true
---

# Design **Principles**

<!--
Speaker: from "which chart" to "how it looks" — ink, colour, accessibility,
scales, panels. Tufte's one rule opens the section. (~0.5 min)
-->

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

<!--
Speaker: Tufte's one rule — above all else, show the data. Ask them to name the
non-data ink on the next few figures; the library defaults are the worst
offender. (~1 min)
-->

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

<img class="fig" src="/figures/viz_color_palette_qualitative.svg" style="width:100%;max-height:70px;">

<div>

📈 **Sequential** — ordered magnitudes

</div>

<img class="fig" src="/figures/viz_color_palette_sequential.svg" style="width:100%;max-height:70px;">

<div>

⚖️ **Diverging** — signed deviations from a midpoint

</div>

<img class="fig" src="/figures/viz_color_palette_diverging.svg" style="width:100%;max-height:55px;">

</div>

---
hideInToc: true
---

# Use Colour to **Highlight**

<div class="card card-info card-glass pad-compact mt-sm">

🔦 Colour draws the eye. Reserve saturated colour for the category you want the reader to see first; leave the rest grey. The same dataset, told differently — three signals up front instead of thirty competing for attention.

</div>

<img class="fig" src="/figures/viz_color_popgrowth_us_highlight.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Red-Green **Fails Twice**

<div class="card card-warning card-glass pad-compact mt-sm">

👓 Left: the plot as designed. Right: the same plot as a deuteranopic viewer sees it.

</div>

<img class="fig" src="/figures/viz_pitfalls_of_color_use_red_green_cvd_sim.svg" style="display:block;margin:0 auto;max-height:350px;">

---
hideInToc: true
---

# Log **Scale**

<div class="card card-info card-glass pad-compact mt-sm">

📐 When values span orders of magnitude, a log axis spreads them out — here five papers' citations from 5 to 46 000. Use dots, not bars: on a log axis a bar has no meaningful base.

</div>

<img class="fig" src="/figures/viz_proportional_ink_log_scale.svg" style="display:block;margin:0 auto;max-height:370px;">

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

---
hideInToc: true
---

# **Square-Root** Scale — for counts

<div class="card card-info card-glass pad-compact mt-sm">

√ When the y-axis is a **count** of rare events (radioactive decays, defects), whose spread grows with the mean — a square-root scale stabilises it. Cleaner than log when values include zero. Dots again, not bars: a non-linear axis has no honest bar base.

</div>

<img class="fig" src="/figures/viz_coordinates_axes_sqrt_scale.svg" style="display:block;margin:0 auto;max-height:330px;">

---
hideInToc: true
---

# Small **Multiples**

<div class="card card-info card-glass pad-compact mt-sm">

🧩 Faceting replaces a crowded single plot with a grid of small, consistent panels — easier comparison, less visual overload.

</div>

<img class="fig" src="/figures/viz_multi_panel_small_multiples_gapminder.svg" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# Small Multiples — **Share the Scale**

<div class="card card-info card-glass pad-compact mt-sm">

🚢 Titanic survival by class × sex. The key insight — **first-class women almost all survived, third-class men mostly didn't** — only pops out when each panel shares a y-axis. Free-scale faceting makes every panel look "interesting" and hides the real pattern.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_bad.svg" style="display:block;margin:0 auto;max-height:300px;">

🚫 **Per-panel scales** — the story disappears

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_titanic_survival_good.svg" style="display:block;margin:0 auto;max-height:300px;">

✅ **Shared y-axis** — the class × sex pattern jumps out

</div>

</div>

---
layout: section
hideInToc: true
---

# Telling a **Story**

<!--
Speaker: a correct figure is not yet a persuasive one. Title as the finding,
direct labels, annotations, reference lines — and two colour pitfalls to
close. (~0.5 min)
-->

---
hideInToc: true
---

# Title as the **Finding**

<div class="card card-info card-glass pad-compact mt-sm">

✍️ The title states the finding, the subtitle adds scope, the caption cites the source — together the figure stands alone. "*Sales 2019–2025*" says what the figure **is**; "*Sales doubled after 2022*" says what it **means**. Prefer the finding.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_story_titles_captions.svg" style="display:block;margin:0 auto;max-height:230px;">

📖 **Title · subtitle · caption** — the plot's voice

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_telling_a_story_title_as_finding.svg" style="display:block;margin:0 auto;max-height:230px;">

✅ **Description vs finding** — same plot, different title

</div>

</div>

---
hideInToc: true
---

# Label **Directly**, Drop the Legend

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ A legend forces the reader's eye to **hop** between the plot and the key. Label each line or group **directly on the plot** and the reader stays in one place — fewer cognitive switches, clearer story.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_bad_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

🚫 **Legend off to the side** — reader has to look twice

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_redundant_coding_tech_stocks_good_no_legend.svg" style="display:block;margin:0 auto;max-height:220px;">

✅ **Direct labels at the line ends** — one glance

</div>

</div>

---
hideInToc: true
---

# Annotate the **Point You Want Made**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 The same line chart can be plain or annotated. Call out the outlier, the trend, or the decision threshold — don't make the reader hunt for it.

</div>

<img class="fig" src="/figures/viz_telling_a_story_annotated_vs_plain.svg" style="display:block;margin:0 auto;max-height:340px;">

---
hideInToc: true
---

# Add a **Reference Line**

<div class="card card-info card-glass pad-compact mt-sm">

🧬 Wild-type vs mutant mRNA abundance (log–log). Without a reference, the reader has to guess whether mutant &gt; or &lt; wild-type. Drawing the **y = x diagonal** makes deviations — the genes whose expression changed — jump out immediately.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_bad.svg" style="display:block;margin:0 auto;max-height:210px;">

🚫 **No reference** — deviations are invisible

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_balance_data_context_gene_expression_good.svg" style="display:block;margin:0 auto;max-height:210px;">

✅ **y = x diagonal** — off-diagonal points are the finding

</div>

</div>

---
hideInToc: true
---

# Rainbow is **Not a Palette**

<div class="card card-warning card-glass pad-compact mt-sm">

🌈 Same field, same data — `jet` on the left, `viridis` on the right.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_bad.svg" style="display:block;margin:0 auto;max-height:250px;">

🚫 **Rainbow** — false boundaries, unreadable magnitudes

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_pitfalls_of_color_use_rainbow_fix.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **Perceptually uniform** — clear, colour-blind safe

</div>

</div>

---
hideInToc: true
---

# Less **Ink**, Same Data

<div class="card card-info card-glass pad-compact mt-sm">

✂️ Tufte's data-to-ink ratio in practice: same scatter, same point — but on the right we've removed the box, heavy ticks, and every non-essential gridline. Nothing lost; everything cleaner.

</div>

<img class="fig" src="/figures/viz_balance_data_context_grid_vs_no_grid.svg" style="display:block;margin:0 auto;max-height:340px;">

---
layout: section
hideInToc: true
---

# Hands-on **Matplotlib**

<!--
Speaker: the pivot from principles to code. Three small scripts, each with its
output beside it, then a reusable style and how to save. (~0.5 min)
-->

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

<!--
Speaker: this is the pivot from theory to code. Get the Figure / Axes / Artists
mental model to stick — every matplotlib snippet that follows is just these
three layers. (~1 min)
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

✅ **The output** — one colour, zero base, y-grid only, no box

</div>

</div>

---
hideInToc: true
---

# Scatter **with a Fit**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-3|5-6|8-10|12-17|all}
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(0)

x = rng.uniform(0, 10, 60)
y = 0.8 * x + rng.normal(0, 1.2, 60)

slope, intercept = np.polyfit(x, y, 1)
xs = np.linspace(0, 10, 100)
ys = slope * xs + intercept

fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.scatter(x, y, s=30, color="#56B4E9", alpha=0.85,
           edgecolor="white", linewidth=0.5)
ax.plot(xs, ys, color="#D55E00", linewidth=2,
        label=f"y = {slope:.2f} x + {intercept:.2f}")
ax.set(xlabel="x", ylabel="y")
ax.legend(frameon=False)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_scatter_fit.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output** — points, fitted line, the fit equation as its label

</div>

</div>

---
hideInToc: true
---

# Histogram + **Density Overlay**

<div class="grid-2 mt-sm gap-md">

<div>

```python {all|1-3|5-6|8-9|11-16|all}
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

rng = np.random.default_rng(1)
data = rng.normal(loc=5, scale=1.5, size=500)

kde = gaussian_kde(data)   # smooth density curve
xs = np.linspace(data.min(), data.max(), 300)

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.hist(data, bins=25, density=True,   # counts -> density
        color="#56B4E9", alpha=0.75, edgecolor="white")
ax.plot(xs, kde(xs), color="#D55E00", linewidth=2,
        label="kde")
ax.set(xlabel="value", ylabel="density")
ax.legend(frameon=False)
```

</div>

<div class="card card-success card-glass pad-compact text-center">

<img class="fig" src="/figures/viz_handson_hist_kde.svg" style="display:block;margin:0 auto;max-height:250px;">

✅ **The output** — normalised histogram with the KDE on top

</div>

</div>

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
    "axes.prop_cycle": mpl.cycler(color=OKABE_ITO),  # cycle through a colour-blind-safe palette
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

<div class="card card-accent card-glass pad-compact mt-md">

## 🔁 **One script → two files**

```python
for ext in ("svg", "png"):
    fig.savefig(f"results/mass_spectrum.{ext}", dpi=150, bbox_inches="tight")
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 **Commit both**: SVG for long-term editability, PNG for reliable rendering. Keep the source `.py` alongside — then the figure is **reproducible**, not just a static file.

</div>

---
layout: section
hideInToc: true
---

# **Wrap-up**

<!--
Speaker: land the plane — the seminar dataset they will plot, one last
question, the checklist, the recap, and what to read next. (~0.5 min)
-->

---
hideInToc: true
---

# The Seminar Dataset — the D⁰ **spectrum**

<div class="card card-info card-glass pad-compact mt-sm">

🎯 **Seminar 10** turns a table of numbers into this figure — the **LHCb D⁰ → K⁻π⁺ mass spectrum**. Every principle from this lecture is in it.

</div>

<img class="fig" src="/figures/lhcb_d0_spectrum.png" style="display:block;margin:0 auto;max-height:310px;background:#fff;border-radius:8px;">

<div class="note-text mt-sm">⚠️ <strong>Raw stage</strong> — in Seminar 10 you build it yourself: axis units, a finding-as-title (this one only describes), a sensible bin width, a 1.80–1.94 GeV zoom with a log y-axis, and PNG + SVG exported from one script.</div>

---
hideInToc: true
---

<MCQ
  question="Your measurements span 10 to 10 000 000 across categories. Which axis choice best reveals the structure at every magnitude?"
  :options="[
    'A linear y-axis starting at zero',
    'A logarithmic y-axis',
    'A linear y-axis truncated to start at 10',
    'Drop the axis labels to reduce clutter'
  ]"
  :correct="1"
  explanation="When values span several orders of magnitude, a log scale spreads them out so structure stays visible at every scale; a linear axis crushes the small values against the baseline."
/>

---
hideInToc: true
---

# Your Turn — the **Checklist**

<div class="card card-info card-glass pad-tight mt-sm">

## 🧪 **Before you hit save**

Run through this checklist on your own plot. If any answer is "no", the figure isn't finished.

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

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Choose the **right chart** for amounts, distributions, proportions, and trends

</div>

<div class="card card-success card-glass pad-compact">

✅ Label **axes** with units and pick an honest scale — zero base, log, or square-root

</div>

<div class="card card-success card-glass pad-compact">

✅ Cut **chart junk** and use colour-blind-safe palettes

</div>

<div class="card card-success card-glass pad-compact">

✅ Title a figure with its **finding** and make it **reproducible**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 10 tie-in**

Produce your first committed figure — the LHCb D⁰ → K⁻π⁺ mass spectrum with axis units and a finding-as-title, a zoom on the 1865 MeV peak with a log y-axis, exported PNG + SVG from one script.

</div>

<!--
Speaker: this is the "you can now" beat — have them nod along to each card. The
seminar tie-in makes the payoff concrete: they leave the lecture and produce
their first committed figure from real LHCb data. (~1 min)
-->

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

**3.** Add a **title, axis labels, and direct labels** (or a legend if you must) — make sure someone unfamiliar with your data can understand the figure

</div>

<div class="card card-warning card-glass pad-compact">

**4.** **Critique** your own plot: Does the y-axis start at zero? Is the color palette accessible? Are the labels clear?

</div>

</div>

---
hideInToc: true
---

# Further **Reading**

<div class="card card-info card-glass pad-compact mt-sm">

📚 This lecture is built on these — Wilke is free online:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📈 **C. O. Wilke** — *Fundamentals of Data Visualization* · free at clauswilke.com/dataviz

</div>

<div class="card card-secondary card-glass pad-compact">

📊 **Cleveland** — *The Elements of Graphing Data* (the perceptual-hierarchy source)

</div>

<div class="card card-accent card-glass pad-compact">

🎨 **Cairo** — *The Truthful Art* — honest, clear data storytelling

</div>

<div class="card card-info card-glass pad-compact">

📐 **Tufte** — *The Visual Display of Quantitative Information* — the classic

</div>

</div>
