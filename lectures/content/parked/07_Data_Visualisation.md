<!--
Parked slides from slides/07_Data_Visualisation.md (Lecture 08 until 5 Nov 2026). This file is not in
decks.json: it is not built, not gated and not deployed. A comment above each
slide says where it stood. To put a slide back, move it into the lecture file.
-->

<!-- Parked 2026-10-06 from Lecture 08, section Wrap-up, after slide 'A Checklist for a Figure': replaced by 'Every Choice in the Two Figures', which answers the opening slide; the reading list moved to the workbook page lecture_8.md under "Further reading" -->

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

<!-- Parked 2026-11-05 from Lecture 07, after slide 3 (The Mean of 87 552 Hours): the lecturer asked whether the first slides were preambles; the deck opens on its question, then the figures, as Lectures 4 to 6 do -->

---
hideInToc: true
---

# Learning **Objectives**

<div class="stack-tight mt-sm">

<div class="card card-info card-glass pad-compact">

🐍 Make a figure with **Matplotlib** from lists: ten years as a line, a histogram, a file in `results/`

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
**Say:** six abilities: the first is new code, the other five are decisions that hold for any plotting program.
(~1 min)
-->

<!-- Parked 2026-11-05 from Lecture 07, after the Learning Objectives: four cards of framing without data; the figures of the opening now show what a figure is for -->

---
hideInToc: true
---

# What a **Figure** Is For

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 👁️ **Reading**

A column of 87 552 temperatures cannot be read, and its mean, 7.16 °C, does not say how the hours are spread. Counts drawn as bars are read in a few seconds.

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
**Say:** one sentence per card.
(~1 min)
-->

<!-- Parked 2026-11-05 from Lecture 07, section Mechanics of a Figure, after 'A Legend Without Samples': on the skip list already; out to keep the deck in its time band after the section Beyond Two Axes came in -->

---
hideInToc: true
class: fill
---

# Legends for Colour, Size and **Shape**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Fuel efficiency of cars against displacement. Colour is power, size is weight, shape is the number of cylinders. Each has a legend with a title, and all three stand in an empty corner.

</div>

<img class="fig fig-fill mt-sm fig-light" src="/figures/data_vis_legend_1.png">

<!-- Parked 2026-11-05 from Lecture 07, section Chart Families, after 'The Dot Plot': on the skip list already; out to keep the deck in its time band after the section Beyond Two Axes came in -->

---
hideInToc: true
class: fill
---

# Life Expectancy in **Alphabetical Order**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Life expectancy in 20 countries (example values), listed alphabetically. The order of the rows says nothing about the values: the highest, the lowest and the spread have to be searched for.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_amounts_lifeexp_alpha_order_bad.svg">

<!-- Parked 2026-11-05 from Lecture 07, section Chart Families, after 'Life Expectancy in Alphabetical Order': on the skip list already; out to keep the deck in its time band after the section Beyond Two Axes came in -->

---
hideInToc: true
class: fill
---

# Life Expectancy as **Sorted Bars**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Sorted, as bars from zero. All values lie between 60 and 82 years, so every bar is long, and the differences take up only the right-hand quarter of the plot.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_amounts_lifeexp_bars_bad.svg">

<!-- Parked 2026-11-05 from Lecture 07, section Chart Families, after 'Visualising Trends': on the skip list already; out to keep the deck in its time band after the section Beyond Two Axes came in -->

---
hideInToc: true
class: fill
---

# Trend and **Seasonal Cycle**

<div class="card card-info card-glass pad-compact mt-sm">

🔬 A series shaped like the CO₂ record of Mauna Loa (synthetic). Left: the series. Centre: its slow rise, the trend. Right: what remains, a yearly cycle and noise.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_trends_keeling_decomposition.svg">

<!-- Parked 2026-11-05 from Lecture 07, section Chart Families, after 'When a Pie Chart Works': on the skip list already; out to keep the deck in its time band after the section Beyond Two Axes came in -->

---
hideInToc: true
class: fill
---

# The **Treemap**

<div class="card card-info card-glass pad-compact mt-sm">

🗂️ For parts that have parts of their own. The area of a rectangle is proportional to its value, and the rectangles of one group share a colour. Here the 200 hours of a research month.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_proportions_treemap.svg">

<!-- Parked 2026-11-07 from Lecture 07, section Chart Families, after 'The Dot Plot': on the skip list; its synthetic example is covered by a figure of the weather log (the Beyond Two Axes heatmap, the month histograms, the films dot plot), and four good-and-bad pairs came in -->

---
hideInToc: true
class: fill
---

# Life Expectancy as **Sorted Dots**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Life expectancy in 12 countries (approximate values, about 2019) as dots, sorted, on an axis from 60 to 85 years. As bars from zero every bar would be long and the differences would fill only the last third of the axis; as dots they use the full width, and the ranking is read from top to bottom.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_amounts_lifeexp_dot_plot.svg">

<!-- Parked 2026-11-07 from Lecture 07, section Chart Families, after 'The Empirical CDF': on the skip list; its synthetic example is covered by a figure of the weather log (the Beyond Two Axes heatmap, the month histograms, the films dot plot), and four good-and-bad pairs came in -->

---
hideInToc: true
class: fill
---

# The **Ridgeline** Plot

<div class="card card-info card-glass pad-compact mt-sm">

🎢 One density curve per group, each shifted up by a fixed step. Here the temperatures of twelve months (synthetic): the peak moves to the right until July and back. On one baseline the curves would hide each other.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_distributions_ii_ridgeline.svg">

<!-- Parked 2026-11-07 from Lecture 07, section Chart Families, after 'Overlaid Densities: Lines or Fill': on the skip list; its synthetic example is covered by a figure of the weather log (the Beyond Two Axes heatmap, the month histograms, the films dot plot), and four good-and-bad pairs came in -->

---
hideInToc: true
class: fill
---

# Temperatures as a **Heatmap**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ Six places by twelve months: 72 mean temperatures (example values). Colour stands for the value, on a sequential palette from dark for cold to light for warm. Whole rows are compared at once: Death Valley is the lightest row, Anchorage the darkest. A single value is read less accurately from a colour than from a position.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_aesthetic_mapping_temp_normals_heatmap.svg">
