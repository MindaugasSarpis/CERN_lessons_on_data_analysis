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

# Great data visualization is not about making things look pretty—it is about making the **data speak clearly**. A well-designed figure tells a story that numbers alone cannot.

---
hideInToc: true
---

# Why Data Visualization Matters

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

# **Aesthetics** of Data Visualization

<div class="card card-info card-glass pad-compact mt-sm">

Every data point is mapped to visual properties — **position**, **color**, **shape**, **size**, **line style**. These mappings are called **aesthetic mappings**, and choosing them well is the core skill of visualization.

</div>

<img src="/figures/data_vis_aesthetics.png" style="display:block;margin:0 auto;width:70%;">

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
layout: section
hideInToc: true
---

# Plot **Components**

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

<img src="/figures/data_vis_legend_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Too many legend entries make the chart unreadable — consider direct labeling or grouping

</div>

<img src="/figures/data_vis_legend_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Legend placed outside the plot area — data is fully visible and the legend is easy to read

</div>

<img src="/figures/data_vis_legend_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Clean legend with well-chosen colors and clear labels — each group is easily distinguishable

</div>

<img src="/figures/data_vis_legend_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Axes**

<div class="card card-info card-glass pad-tight mt-sm">

## 📐 **What are Axes?**

Axes are the reference lines that define the coordinate system of the plot. They orient the viewer and give meaning to every data point's position.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

🏷️ Axes should be **clearly labeled** with units and titles

</div>

<div class="card card-secondary card-glass pad-compact">

📏 Axes should have appropriate **tick marks and grid lines** to help interpret the data

</div>

<div class="card card-accent card-glass pad-compact">

🔍 Axes should be **scaled appropriately** to show the data clearly

</div>

<div class="card card-warning card-glass pad-compact">

🔗 Axes should show the **relationship** between different variables in the data

</div>

</div>

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/data_vis_axes_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/data_vis_axes_2.png
---

---
layout: section
hideInToc: true
---

# Visualizing **Data**

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

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Bars do not start at zero — this exaggerates differences and misleads the viewer

</div>

<img src="/figures/data_vis_bar_chart_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Y-axis starts at zero — bar lengths accurately represent the data values

</div>

<img src="/figures/data_vis_bar_chart_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Categories are unsorted — makes it hard to compare values or spot patterns

</div>

<img src="/figures/data_vis_bar_chart_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Bars sorted by value — trends and rankings are immediately visible

</div>

<img src="/figures/data_vis_bar_chart_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Stacking makes individual group comparisons difficult — consider grouped bars instead

</div>

<img src="/figures/data_vis_bar_chart_error_3.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# Stacked Bar Charts

<div class="card card-info card-glass pad-compact mt-sm">

📊 Stacked bars work well for **part-to-whole** comparisons — each segment shows a proportion of the total

</div>

<img src="/figures/data_vis_bar_chart_stacked.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Too many categories with similar colors — the chart becomes hard to decode

</div>

<img src="/figures/data_vis_bar_chart_error_4.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ 3D effects distort perception — bar heights become ambiguous and comparisons unreliable

</div>

<img src="/figures/data_vis_bar_chart_error_5.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Clean 2D bars with distinct colors and clear labels — easy to read and compare

</div>

<img src="/figures/data_vis_bar_chart_3.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Poor color choices — rainbow palettes can confuse meaning and are not accessible to colorblind viewers

</div>

<img src="/figures/data_vis_color_error.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/data_vis_heatmap.png
---

---
hideInToc: true
---

# Histograms

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
image: /figures/data_vis_hist.png
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
disabled: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Bin width too large or too small — the distribution shape is distorted or obscured by noise

</div>

<img src="/figures/data_vis_hist_error.png" style="display:block;margin:0 auto;max-height:370px;">

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

# More **Plot Types**

<div class="card card-info card-glass pad-tight mt-sm">

## 📈 **Beyond Bar Charts and Histograms**

There are many more plot types used in data analysis. Here are a few you will encounter:

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

📈 **Line Plots** — Show trends over time or continuous variables

</div>

<div class="card card-secondary card-glass pad-compact">

🔵 **Scatter Plots** — Reveal relationships between two variables

</div>

<div class="card card-accent card-glass pad-compact">

📦 **Box Plots** — Summarize distributions with median, quartiles, and outliers

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

## 🔗 **Coming in Lecture 11**

We will create scatter plots, line plots, box plots, and more **interactively** using Pandas and Matplotlib. You will learn to write Python code that generates publication-quality figures.

</div>

---
layout: section
hideInToc: true
---

# Design **Principles**

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

# Key Takeaways

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

## 🔗 **What Comes Next**

- **L9–L10**: Statistics and data fitting — you will visualize distributions, fits, and residuals
- **L11**: Create plots interactively with `matplotlib` and Pandas
- Use **git** (already covered!) to version-control your figures and analysis

Good visualization is not decoration — it is **analysis**. A well-chosen plot reveals structure that statistics alone cannot.

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
