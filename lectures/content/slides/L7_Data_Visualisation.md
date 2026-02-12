---
background: /background_intro.jpg

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

# Lessons on **Data Analysis** from **CERN**

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

# **Aesthetics** of Data Visualization

<img src="/data_vis_aesthetics.png" style="display:block;margin:0 auto;width:75%;">

---
layout: iframe
hideInToc: true
url: https://datavizcatalogue.com/
---

---
hideInToc: true
layout: image
backgroundSize: cover
image: /data_vis_anatomy_of_a_figure.svg
---

---
hideInToc: true
---

# **Legend**

<div class="card card-info pad-tight mt-sm">

## 🏷️ **What is a Legend?**

A legend is a key component of a plot that explains the meaning of the data. It maps visual encodings (colors, shapes, sizes) to their semantic meaning.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

📌 Legend might **not be necessary** if the data is self-explanatory (e.g. bar chart, single-line plot, direct annotations)

</div>

<div class="card card-secondary pad-compact">

📍 Legend should be **placed** so it does not obscure the data

</div>

<div class="card card-accent pad-compact">

👁️ Legend should be **easy to read** and understand

</div>

<div class="card card-success pad-compact">

🎨 Legend should be **consistent** with the overall design of the plot

</div>

<div class="card card-warning pad-compact">

🔑 Legend should explain **colors, shapes, sizes**, and other visual encodings used in the plot

</div>

</div>

---
hideInToc: true
layout: image
image: /data_vis_legend_error_1.png
backgroundSize: contain
---

---
hideInToc: true
layout: image
image: /data_vis_legend_error_2.png
backgroundSize: contain
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_legend_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_legend_2.png
---

---
hideInToc: true
---

# **Axes**

<div class="card card-info pad-tight mt-sm">

## 📐 **What are Axes?**

Axes are the reference lines that define the coordinate system of the plot. They orient the viewer and give meaning to every data point's position.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

🏷️ Axes should be **clearly labeled** with units and titles

</div>

<div class="card card-secondary pad-compact">

📏 Axes should have appropriate **tick marks and grid lines** to help interpret the data

</div>

<div class="card card-accent pad-compact">

🔍 Axes should be **scaled appropriately** to show the data clearly

</div>

<div class="card card-success pad-compact">

🎨 Axes should be **consistent** with the overall design of the plot

</div>

<div class="card card-warning pad-compact">

🔗 Axes should show the **relationship** between different variables in the data

</div>

<div class="card card-info pad-compact">

📊 Axes should be used to **compare** different groups or categories within the data

</div>

</div>

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_axes_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_axes_2.png
---

---
hideInToc: true
---

# Visualizing **Amounts**

<div class="card card-info pad-tight mt-sm">

## 📊 **Common Chart Types for Amounts**

When your data represents quantities associated with categories, these are the go-to visualizations:

</div>

<div class="grid-2 mt-md gap-md">

<div class="stack-tight">

<div class="card card-primary pad-compact">

📊 **Bar Charts** — Compare values across categories

</div>

<div class="card card-secondary pad-compact">

📊 **Grouped Bar Charts** — Compare sub-groups side by side

</div>

</div>

<div class="stack-tight">

<div class="card card-accent pad-compact">

📊 **Stacked Bar Charts** — Show part-to-whole relationships

</div>

<div class="card card-warning pad-compact">

🌡️ **Heat Maps** — Encode values as color intensity in a grid

</div>

</div>

</div>

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_error_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_error_2.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_2.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_error_3.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_stacked.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_error_4.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_error_5.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_bar_chart_3.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_color_error.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_heatmap.png
---

---
hideInToc: true
---

# Histograms

<div class="card card-info pad-tight mt-sm">

## 📈 **What are Histograms?**

Histograms visualize the **distribution** of a single continuous variable by dividing the data range into bins and counting observations in each bin.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

📏 Histograms should have appropriate **bin widths** to show the shape of the distribution

</div>

<div class="card card-secondary pad-compact">

🏷️ Histograms should have **clear labels and titles**

</div>

<div class="card card-accent pad-compact">

🎨 Histograms should be **consistent** with the overall design of the plot

</div>

<div class="card card-success pad-compact">

🔍 Histograms should be used to identify **patterns, trends, and outliers** in the data

</div>

</div>

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_hist.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_hist_comp.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_hist_error.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_hist_scientific_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /data_vis_hist_scientific_2.png
---

---
hideInToc: true
---

# Key Takeaways

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📊 **Design Principles**

- Every visual encoding (color, shape, size) must be **meaningful**
- Axes must be clearly labeled with **units**
- Legends should be **placed carefully** to not obscure data
- Avoid chart junk — maximize the **data-to-ink ratio**

</div>

<div class="card card-secondary pad-tight">

## 🔗 **What Comes Next**

- **L11**: Create these plots yourself with `matplotlib` and Pandas
- **L10**: Visualize fit results with residual plots
- **L12**: Automate plot generation in reproducible workflows

Good visualization is not decoration — it is **analysis**. A well-chosen plot reveals structure that statistics alone cannot.

</div>

</div>
