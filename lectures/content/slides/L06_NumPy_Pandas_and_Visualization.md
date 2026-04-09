---
mermaid: true
background: /figures/background_intro.jpg
class: text-left
colorSchema: dark
theme: ./theme
drawings:
  persist: false
transition: fade
title: "NumPy, Pandas & Visualization"
layout: cover
addons:
  - slidev-addon-python-runner
python:
  installs: ["numpy", "pandas", "matplotlib"]
  prelude: |
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## NumPy, Pandas & Visualization

---
hideInToc: true
layout: quote
---

# Real data requires real tools. NumPy gives you speed, Pandas gives you structure, and matplotlib gives you **sight**. Together, they form the foundation of every data analysis in Python.

---
hideInToc: true
---

# Motivation

<div class="card card-info card-glass pad-tight mt-md">

## 🛠️ **From Python to Data Tools**

In L5, you learned Python basics. But raw Python is too slow and verbose for real data work:
- Loops over millions of numbers? Too slow
- No built-in tables or column labels? Too limiting
- No plotting? Can't see patterns

NumPy, Pandas, and matplotlib solve all three.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### 🔢 **NumPy**
- Efficient numerical arrays
- Vectorized operations (fast!)
- Mathematical functions
- Foundation for scientific Python

</div>

<div class="card card-secondary card-glass pad-tight">

### 🐼 **Pandas**
- DataFrames (like Excel tables)
- Handle missing data
- Read/write many formats
- Group, filter, transform data

</div>

</div>

---
layout: section
hideInToc: true
---

# NumPy: Numerical **Computing**

---
hideInToc: true
---

# What is NumPy?

<div class="card card-primary card-glass pad-tight mt-md">

## 🔢 **NumPy = Numerical Python**

The fundamental package for scientific computing in Python:
- Multi-dimensional arrays (`ndarray`)
- Fast element-wise operations (vectorization)
- Linear algebra, random numbers, Fourier transforms
- Foundation for SciPy, Pandas, Matplotlib, scikit-learn, etc.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 🚀 **Why NumPy?**

✅ **Speed**: 10-100× faster than Python lists

✅ **Memory**: More efficient storage

✅ **Convenience**: Write mathematical code naturally

</div>

<div class="card card-secondary card-glass pad-tight">

### 💡 **Key Concept**

**Vectorization**: Operations on entire arrays without explicit loops

```python
# Python lists (slow)
result = [x**2 for x in data]

# NumPy (fast)
result = data ** 2
```

</div>

</div>

---
hideInToc: true
---

# Creating NumPy Arrays

```py {monaco-run}
import numpy as np

# From Python lists
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}, dtype: {arr.dtype}")

# Built-in creation functions
print(f"zeros:    {np.zeros(5)}")
print(f"arange:   {np.arange(0, 10, 2)}")   # start, stop, step
print(f"linspace: {np.linspace(0, 1, 5)}")   # start, stop, num_points

# 2D arrays (matrices)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{matrix}")
print(f"Shape: {matrix.shape}")  # (rows, columns)
```

---
hideInToc: true
---

# Array Operations: Vectorization

```py {monaco-run}
import numpy as np

x = np.array([1, 2, 3, 4, 5])

# Element-wise operations (no loops needed!)
print(f"x:          {x}")
print(f"x + 10:     {x + 10}")
print(f"x ** 2:     {x ** 2}")
print(f"np.sqrt(x): {np.sqrt(x)}")

# Operations between arrays
y = np.array([10, 20, 30, 40, 50])
print(f"\nx + y: {x + y}")
print(f"x * y: {x * y}")

# Aggregation functions
print(f"\nSum: {x.sum()}, Mean: {x.mean():.2f}, Std: {x.std():.2f}")
```

---
hideInToc: true
---

# Speed Comparison: Lists vs NumPy

```py {monaco-run}
import numpy as np, time

n = 100000
py_list = list(range(n))
np_arr = np.arange(n)

# Sum benchmark
t = time.time(); sum(py_list); t1 = time.time() - t
t = time.time(); np_arr.sum(); t2 = time.time() - t
print(f"Sum — Python: {t1*1000:.2f} ms, NumPy: {t2*1000:.2f} ms → {t1/t2:.0f}x faster")

# Polynomial x² + 2x + 1
t = time.time(); [x**2+2*x+1 for x in py_list]; t1 = time.time() - t
t = time.time(); np_arr**2 + 2*np_arr + 1; t2 = time.time() - t
print(f"Poly — Python: {t1*1000:.2f} ms, NumPy: {t2*1000:.2f} ms → {t1/t2:.0f}x faster")
```

<div class="card card-accent card-glass pad-tight mt-sm">

**Key**: NumPy operations are implemented in C — extremely fast even for millions of elements!

</div>

---
hideInToc: true
---

# Array Indexing and Slicing

```py {monaco-run}
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"arr:       {arr}")
print(f"arr[0]:    {arr[0]},  arr[-1]: {arr[-1]}")
print(f"arr[2:5]:  {arr[2:5]}")
print(f"arr[::2]:  {arr[::2]}")

# Boolean indexing (very powerful!)
print(f"\narr > 50:      {arr > 50}")
print(f"arr[arr > 50]: {arr[arr > 50]}")

# 2D arrays
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nmatrix[1, 2]: {matrix[1, 2]}")
print(f"Row 1:        {matrix[1, :]}")
print(f"Col 2:        {matrix[:, 2]}")
```

---
hideInToc: true
---

# Broadcasting: Concept

<div class="card card-info card-glass pad-tight mt-md">

## 📐 **Broadcasting Rules**

NumPy automatically "broadcasts" arrays of different shapes to make operations work:

```python
# Add scalar to array (broadcast scalar to all elements)
arr + 10

# Add 1D array to 2D array (broadcast row-wise or column-wise)
matrix + row_vector
```

</div>

```py {monaco-run}
import numpy as np

# Scalar broadcasting
arr = np.array([1, 2, 3])
print(f"arr:       {arr}")
print(f"arr + 100: {arr + 100}")  # 100 broadcast to [100, 100, 100]

# Row broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
print(f"\nMatrix + row:\n{matrix + row}")  # row added to each row
```

---
hideInToc: true
---

# Broadcasting: Normalization Example

```py {monaco-run}
import numpy as np

# Useful for normalization: subtract column means
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])
mean = data.mean(axis=0)  # Mean of each column

print(f"Data:\n{data}")
print(f"Column means: {mean}")
print(f"Centered data:\n{data - mean}")  # Subtract mean from each column

# Standardization: (x - mean) / std
std = data.std(axis=0)
standardized = (data - mean) / std
print(f"\nStandardized:\n{standardized}")
```

---
hideInToc: true
---

# NumPy: When It's Not Enough

<div class="card card-info card-glass pad-tight mt-md">

## ⚠️ **Limitations of NumPy**

NumPy is great for numerical computation, but real-world data often needs more:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### 🚫 **NumPy limitations**
- All elements must be same type
- No column names or labels
- No built-in handling of missing values
- No built-in file I/O (CSV, Excel)

</div>

<div class="card card-success card-glass pad-tight">

### 🐼 **Enter Pandas**
- Mixed data types per column
- Named columns and row indices
- `NaN` for missing data
- Read/write CSV, Excel, JSON, SQL, HDF5

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

**Pandas is built on top of NumPy** — it adds labels, mixed types, and data manipulation tools while keeping NumPy's speed for numerical operations.

</div>

---
layout: section
hideInToc: true
---

# Pandas: **DataFrames** & Data

---
hideInToc: true
---

# What is Pandas?

<div class="card card-primary card-glass pad-tight mt-md">

## 🐼 **Pandas = Panel Data (Python Data Analysis Library)**

Built on top of NumPy, adds:
- **DataFrame**: 2D labeled data structure (like Excel spreadsheet or SQL table)
- **Series**: 1D labeled array (single column)
- Easy reading/writing of files (CSV, Excel, JSON, SQL, etc.)
- Handling missing data
- Group-by operations, merging, reshaping

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 🗂️ **Think of DataFrame as:**
- Excel spreadsheet
- SQL table
- Dictionary of NumPy arrays
- Collection of labeled columns

</div>

<div class="card card-secondary card-glass pad-tight">

### ✨ **Key Features:**
- Column/row labels (not just indices)
- Mixed data types per column
- Missing data handling (NaN)
- Powerful data manipulation

</div>

</div>

---
hideInToc: true
---

# Creating a DataFrame

```py {monaco-run}
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['Geneva', 'Zurich', 'Geneva', 'Bern'],
    'salary': [75000, 85000, 95000, 80000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print(f"\nShape: {df.shape}, Columns: {df.columns.tolist()}")
print(f"Average age: {df['age'].mean():.1f}")
print(f"\nFirst row:\n{df.iloc[0]}")
```

---
hideInToc: true
---

# Reading Data from Files

<div class="card card-primary card-glass pad-tight mt-md">

## 📄 **Most Common: CSV Files**

Pandas makes reading data trivial:

```python
df = pd.read_csv('data.csv')
```

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

# Simulate reading a CSV (in practice: df = pd.read_csv('data.csv'))
np.random.seed(42)
df = pd.DataFrame({
    'event_id': range(1, 101),
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
})
print("First 5 rows:")
print(df.head())
```

---
hideInToc: true
---

# Exploring a DataFrame

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'event_id': range(1, 101),
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
})

print("Summary statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)
```

---
hideInToc: true
---

# Data Exploration: Selection & Filtering

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

print(f"Number of rows: {len(df)}")
print(f"Signal events: {df['is_signal'].sum()}")
print(f"Background events: {(~df['is_signal']).sum()}")

# Filtering (boolean indexing)
high_energy = df[df['energy'] > 10]
print(f"\nHigh energy events (E > 10): {len(high_energy)}")
print(high_energy.head())
```

---
hideInToc: true
---

# Data Exploration: New Columns & Sorting

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

# Adding new columns
df['E_over_p'] = df['energy'] / df['momentum']
print("New column 'E_over_p' created:")
print(df[['energy', 'momentum', 'E_over_p']].head())

# Sorting
df_sorted = df.sort_values('energy', ascending=False)
print(f"\nTop 3 highest energy events:")
print(df_sorted[['energy', 'detector', 'is_signal']].head(3))
```

---
hideInToc: true
---

# Handling Missing Data

<div class="card card-warning card-glass pad-tight mt-md">

## ❓ **Real Data Has Missing Values!**

Pandas represents missing data with `NaN` (Not a Number) or `None`

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50],
    'C': [100, 200, 300, 400, 500]
})
print("DataFrame with missing values:")
print(df)

# Check for missing values
print(f"\nMissing per column:\n{df.isnull().sum()}")
```

---
hideInToc: true
---

# Handling Missing Data: Strategies

```py {monaco-run}
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50],
    'C': [100, 200, 300, 400, 500]
})

# Strategy 1: Drop rows with NaN
print("Drop rows with NaN:")
print(df.dropna())

# Strategy 2: Fill with column mean
print("\nFill NaN with column mean:")
print(df.fillna(df.mean()))

# Strategy 3: Forward fill (use previous value)
print("\nForward fill:")
print(df.ffill())
```

---
hideInToc: true
---

# Group By: Split-Apply-Combine

<div class="card card-info card-glass pad-tight mt-md">

## 📊 **Group By Pattern**

1. **Split** data into groups based on criteria
2. **Apply** a function to each group
3. **Combine** results into a data structure

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 200),
    'detector': np.random.choice(['A', 'B', 'C'], 200),
})

print("Statistics per detector:")
print(df.groupby('detector')['energy'].agg(['count', 'mean', 'std']))
```

---
hideInToc: true
---

# Filtering and Querying Data

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

# Boolean indexing with multiple conditions
signal_high_E = df[(df['is_signal']) & (df['energy'] > 10)]
print(f"Signal events with E > 10: {len(signal_high_E)}")

# Query method (more readable)
result = df.query('energy > 10 and detector == "A"')
print(f"Detector A events with E > 10: {len(result)}")

# isin() for multiple values
detector_AB = df[df['detector'].isin(['A', 'B'])]
print(f"Events in detectors A or B: {len(detector_AB)}")
```

---
layout: section
hideInToc: true
---

# Data **Visualization**

---
hideInToc: true
---

# **Aesthetics** of Data Visualization

<img src="/figures/data_vis_aesthetics.png" style="display:block;margin:0 auto;width:75%;">

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
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Legend placement obscures the data — it overlaps with the plotted points

</div>

<img src="/figures/data_vis_legend_error_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Too many legend entries make the chart unreadable — consider direct labeling or grouping

</div>

<img src="/figures/data_vis_legend_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Legend placed outside the plot area — data is fully visible and the legend is easy to read

</div>

<img src="/figures/data_vis_legend_1.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
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
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Categories are unsorted — makes it hard to compare values or spot patterns

</div>

<img src="/figures/data_vis_bar_chart_error_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# **Corrected**

<div class="card card-success card-glass pad-compact mt-sm">

✅ Bars sorted by value — trends and rankings are immediately visible

</div>

<img src="/figures/data_vis_bar_chart_2.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Stacking makes individual group comparisons difficult — consider grouped bars instead

</div>

<img src="/figures/data_vis_bar_chart_error_3.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
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
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_comp.png
---

---
hideInToc: true
---

# What's **Wrong?**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Bin width too large or too small — the distribution shape is distorted or obscured by noise

</div>

<img src="/figures/data_vis_hist_error.png" style="display:block;margin:0 auto;max-height:370px;">

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_scientific_1.png
---

---
hideInToc: true
layout: image
backgroundSize: contain
image: /figures/data_vis_hist_scientific_2.png
---

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

# Visualization with Pandas: Histograms

<div class="card card-accent card-glass pad-compact mt-sm">

Pandas has built-in plotting (uses Matplotlib under the hood)

</div>

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 500),
    'is_signal': np.random.choice([True, False], 500, p=[0.3, 0.7])
})

fig, ax = plt.subplots(figsize=(10, 4))
df['energy'].hist(bins=30, ax=ax, edgecolor='white')
ax.set_xlabel('Energy (GeV)')
ax.set_ylabel('Counts')
ax.set_title('Energy Distribution')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Visualization: Signal vs Background

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 500),
    'detector': np.random.choice(['A', 'B', 'C'], 500),
    'is_signal': np.random.choice([True, False], 500, p=[0.3, 0.7])
})

fig, ax = plt.subplots(figsize=(10, 4))
df[df['is_signal']]['energy'].hist(bins=30, alpha=0.5, label='Signal', ax=ax)
df[~df['is_signal']]['energy'].hist(bins=30, alpha=0.5, label='Background', ax=ax)
ax.set_xlabel('Energy (GeV)')
ax.set_ylabel('Counts')
ax.set_title('Signal vs Background')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Your First matplotlib Plot

```py {monaco-run}
import numpy as np
import matplotlib.pyplot as plt

# Simple scatter plot
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.2, 50)

plt.figure(figsize=(10, 4))
plt.scatter(x, y, alpha=0.6, label='Noisy sine wave')
plt.plot(x, np.sin(x), 'r-', label='True sine', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Trend Line')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Multiple Plot Types

```py {monaco-run}
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
categories = ['ATLAS', 'CMS', 'ALICE', 'LHCb']
events = [245, 312, 178, 156]
errors = [15, 20, 12, 10]

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Bar chart
axes[0].bar(categories, events, color=['#3b82f6', '#8b5cf6', '#06b6d4', '#f59e0b'], edgecolor='white')
axes[0].set_ylabel('Events (thousands)')
axes[0].set_title('Events by Experiment')

# Bar chart with error bars
axes[1].barh(categories, events, xerr=errors, color='#3b82f6', alpha=0.7)
axes[1].set_xlabel('Events (thousands)')
axes[1].set_title('With Uncertainties')

# Box plot
data = [np.random.normal(e, err, 100) for e, err in zip(events, errors)]
axes[2].boxplot(data, labels=categories)
axes[2].set_ylabel('Events')
axes[2].set_title('Distribution Spread')

plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Exercise: Critique These Plots

<div class="card card-warning card-glass pad-tight mt-md">

## ⚠️ **What's Wrong Here?**

For each issue below, identify the visualization principle being violated:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔍 **Checklist**

When reviewing ANY plot, ask:
1. Does the y-axis start at zero (for bar charts)?
2. Are axes labeled with **units**?
3. Is the color palette **colorblind-safe**?
4. Is there a clear **title** that states the takeaway?
5. Is the legend **readable** and not obscuring data?

</div>

<div class="card card-secondary card-glass pad-tight">

## 🏋️ **Your Turn**

Take any dataset and create:
1. A **histogram** — experiment with bin widths
2. A **bar chart** — sort the bars
3. A **scatter plot** — add a trend line
4. Add proper **labels, title, and legend** to each

</div>

</div>

---
layout: section
hideInToc: true
---

# Data Cleaning & **Preprocessing**

---
hideInToc: true
---

# Common Data Quality Issues

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Missing Values**
- Empty cells, NaN, None
- Measurement failures
- **Fix**: Drop, fill (mean/median), or flag

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Outliers**
- Measurement errors or rare events
- Data entry mistakes
- **Fix**: Statistical tests, domain knowledge

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Duplicates**
- Repeated measurements
- Accidental double-counting
- **Fix**: Identify and remove via unique IDs

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Inconsistent Formats**
- Mixed units (GeV vs MeV)
- Date/time format variations
- **Fix**: Standardize, convert, validate

</div>

</div>

---
hideInToc: true
---

# Detecting Outliers: Z-Score Method

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
normal_data = np.random.normal(100, 10, 95)
outliers = np.array([200, 210, -50, 250, 180])
data = np.concatenate([normal_data, outliers])
df = pd.DataFrame({'measurement': data})

# Z-score: how many standard deviations from mean
mean, std = df['measurement'].mean(), df['measurement'].std()
df['z_score'] = np.abs((df['measurement'] - mean) / std)
outliers_z = df[df['z_score'] > 3]

print(f"Mean: {mean:.2f}, Std: {std:.2f}")
print(f"Outliers (|z| > 3): {len(outliers_z)}")
print(outliers_z[['measurement', 'z_score']])
```

---
hideInToc: true
---

# Detecting Outliers: IQR Method

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.concatenate([np.random.normal(100, 10, 95), [200, 210, -50, 250, 180]])
df = pd.DataFrame({'measurement': data})

# IQR: Interquartile Range
Q1, Q3 = df['measurement'].quantile(0.25), df['measurement'].quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = df[(df['measurement'] < lower) | (df['measurement'] > upper)]
print(f"IQR bounds: [{lower:.1f}, {upper:.1f}] → {len(outliers)} outliers")

fig, ax = plt.subplots(figsize=(10, 3.5))
ax.scatter(range(len(df)), df['measurement'], alpha=0.6, label='Data')
ax.scatter(outliers.index, outliers['measurement'], color='red', s=100, marker='x', label='Outliers')
ax.axhline(upper, color='orange', ls=':', label=f'Bounds')
ax.axhline(lower, color='orange', ls=':')
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()
```

---
hideInToc: true
---

# Data Normalization: Why and How

<div class="card card-info card-glass pad-tight mt-md">

## 📏 **Why Normalize?**

- Different features have different scales (energy in GeV, angles in radians)
- Many ML algorithms perform better with normalized data
- Makes features comparable

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.uniform(50, 150, 100),
    'angle': np.random.uniform(0, np.pi, 100)
})
print("Original scales:")
print(df.describe().loc[['mean', 'std', 'min', 'max']])

# Standardization: (x - mean) / std → mean=0, std=1
df_std = (df - df.mean()) / df.std()
print("\nStandardized (z-score):")
print(df_std.describe().loc[['mean', 'std', 'min', 'max']])
```

---
layout: section
hideInToc: true
---

# Best **Practices**

---
hideInToc: true
---

# File I/O with Pandas

<div class="card card-primary card-glass pad-tight mt-md">

## 📁 **Pandas Supports Many Formats**

Reading and writing data follows a consistent pattern: `pd.read_*()` and `df.to_*()`

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 📥 **Reading Data**

```python
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')
df = pd.read_sql(query, connection)
```

</div>

<div class="card card-secondary card-glass pad-tight">

### 📤 **Writing Data**

```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx')
df.to_json('output.json')
df.to_sql('table', connection)
```

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

**Best practice**: Use CSV for human-readable data, HDF5 or Parquet for large datasets (faster, smaller)

</div>

---
hideInToc: true
---

# Data Analysis: Do's

<div class="card card-success card-glass pad-tight mt-md">

## ✅ **Best Practices**

1. **Always visualize first** — look at distributions and correlations before analysis
2. **Check for missing values** before running any computations
3. **Document data sources** and all preprocessing steps
4. **Validate data quality** — check ranges, units, and consistency
5. **Keep raw data separate** from processed data

</div>

<div class="card card-info card-glass pad-tight mt-md">

**Rule of thumb**: If you can't explain where every number came from, go back and document your pipeline.

</div>

---
hideInToc: true
---

# Data Analysis: Don'ts

<div class="card card-warning card-glass pad-tight mt-md">

## ❌ **Common Mistakes**

1. **Don't assume data is clean** without checking first
2. **Don't delete outliers** without understanding why they exist
3. **Don't mix data loading and analysis** — separate your pipeline
4. **Don't hardcode file paths** — use config files or command-line arguments
5. **Don't skip exploratory analysis** — jumping to conclusions costs time

</div>

<div class="card card-info card-glass pad-tight mt-md">

**Remember**: Version control your analysis scripts and save intermediate results for reproducibility.

</div>

---
hideInToc: true
---

# Performance Tips

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### 🔢 **NumPy**

✅ Use vectorized operations (no loops!)

✅ Pre-allocate arrays if possible

✅ Use appropriate data types (int32 vs int64)

✅ Avoid unnecessary copies

</div>

<div class="card card-secondary card-glass pad-tight">

### 🐼 **Pandas**

✅ Use `iterrows()` sparingly (slow!)

✅ Prefer vectorized operations or `apply()`

✅ Set index on frequently-filtered columns

✅ Use categorical dtype for repeated strings

</div>

<div class="card card-info card-glass pad-tight">

### ⚡ **General**

✅ Profile code to find bottlenecks

✅ Load only needed columns

✅ Filter early (before heavy operations)

✅ Consider Dask for out-of-memory datasets

</div>

</div>

```python
# Slow (loop)
for i in range(len(df)):
    df.loc[i, 'new_col'] = df.loc[i, 'A'] * 2

# Fast (vectorized)
df['new_col'] = df['A'] * 2
```

---
layout: section
hideInToc: true
---

# Lecture **Summary**

---
hideInToc: true
---

# What We Learned: NumPy, Pandas & Visualization

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔢 **NumPy**

✅ ndarray: efficient multi-dimensional arrays

✅ Vectorization: fast element-wise operations

✅ Broadcasting: operations on different shapes

✅ Indexing, slicing, boolean masks

✅ 10-100× faster than Python lists

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐼 **Pandas**

✅ DataFrame: labeled 2D data structure

✅ Reading/writing files (CSV, Excel, JSON, etc.)

✅ Missing data handling

✅ Filtering, grouping, aggregating

✅ Data cleaning and preprocessing

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 **Visualization**

✅ Axes, legends, and labels matter

✅ Bar charts must start at zero

✅ Bin width affects histogram shape

✅ Colorblind-safe palettes are essential

✅ matplotlib for publication-quality plots

</div>

</div>

---
hideInToc: true
---

# What We Learned: Skills & Next Steps

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 🎯 **Skills Acquired**

- Create and manipulate NumPy arrays
- Build and explore Pandas DataFrames
- Clean messy data (missing values, outliers)
- Create histograms, bar charts, scatter plots
- Apply visualization best practices

</div>

<div class="card card-success card-glass pad-tight">

### ✅ **Best Practices**

- Visualize first
- Document everything
- Validate data quality
- Use colorblind-safe palettes
- Keep raw data separate

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

### 🔮 **Next Steps**

You now have the tools to work with data efficiently — arrays, tables, and plots. Next, we'll explore the **concepts and principles** of data analysis that guide how you use these tools.

</div>

---
hideInToc: true
layout: quote
---

# You now have the tools to work with data efficiently — arrays, tables, and plots. Next, we'll explore the **concepts and principles** of data analysis that guide how you use these tools.

---
hideInToc: true
layout: end
---

# Questions?

## Next lecture: **Concepts of Data Analysis**
