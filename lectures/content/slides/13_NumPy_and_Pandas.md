---
mermaid: true
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "NumPy, Pandas & Real Data"
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

# Best Research and Data Analysis Practices from CERN

## NumPy, Pandas & Real Data

##### <span class="aims-badge">📁 data & files · ⚙️ automation · 🔧 tool-agnostic</span>

<!--
Speaker: this is the workhorse lecture — the tools they will use in almost every
seminar from here on. Frame NumPy + Pandas as the bridge from toy data to real,
messy data. Lots of live code today, so keep the pace up. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Real data is messy, incomplete, and comes in various formats. NumPy and Pandas are the foundational tools for handling, cleaning, and analyzing data efficiently in Python.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🔢 Write fast, loop-free array code with NumPy **vectorization**

</div>

<div class="card card-secondary card-glass pad-compact">

🎯 Index, slice, and **broadcast** arrays using boolean masks

</div>

<div class="card card-accent card-glass pad-compact">

🐼 Build, filter, sort, and **group** a Pandas DataFrame

</div>

<div class="card card-success card-glass pad-compact">

🧹 Handle missing values, detect **outliers**, and normalize data

</div>

<div class="card card-warning card-glass pad-compact">

📁 Read and write data across formats — CSV, Excel, **Parquet**

</div>

</div>

<!--
Speaker: read these as promises, not a checklist. Stress that Seminar 13 is where
they turn their own raw dataset into a clean, tidy table — today builds the toolkit
for that. Set the expectation. (~1 min)
-->

---
hideInToc: true
---

# Motivation

<div class="card card-info card-glass pad-tight mt-md">

## **From Toy Examples to Real Data**

In the Data Fitting lecture, we worked with synthetic data (Gaussian + exponential). But real-world data:
- Comes in various formats (CSV, Excel, JSON, HDF5)
- Has missing values, outliers, and inconsistencies
- Requires cleaning and preprocessing
- Is often large and requires efficient operations

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

<!--
Speaker: the one idea to land in this block is vectorization — operate on whole
arrays, never element by element. The speed benchmark a few slides on makes it
visceral. (~1 min)
-->

---
hideInToc: true
---

# What is NumPy?

<div class="card card-primary card-glass pad-tight mt-md">

## **NumPy = Numerical Python**

The fundamental package for scientific computing in Python:
- Multi-dimensional arrays (`ndarray`)
- Fast element-wise operations (vectorization)
- Linear algebra, random numbers, Fourier transforms
- Foundation for SciPy, Pandas, Matplotlib, scikit-learn, etc.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### **Why NumPy?**

✅ **Speed**: 10-100× faster than Python lists

✅ **Memory**: More efficient storage

✅ **Convenience**: Write mathematical code naturally

</div>

<div class="card card-secondary card-glass pad-tight">

### **Key Concept**

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
t = time.perf_counter(); sum(py_list); t1 = time.perf_counter() - t
t = time.perf_counter(); np_arr.sum(); t2 = time.perf_counter() - t
print(f"Sum — Python: {t1*1000:.2f} ms, NumPy: {t2*1000:.2f} ms → {t1/max(t2,1e-9):.0f}x faster")

# Polynomial x² + 2x + 1
t = time.perf_counter(); [x**2+2*x+1 for x in py_list]; t1 = time.perf_counter() - t
t = time.perf_counter(); np_arr**2 + 2*np_arr + 1; t2 = time.perf_counter() - t
print(f"Poly — Python: {t1*1000:.2f} ms, NumPy: {t2*1000:.2f} ms → {t1/max(t2,1e-9):.0f}x faster")
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

## **Broadcasting Rules**

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

## **Limitations of NumPy**

NumPy is great for numerical computation, but real-world data often needs more:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### **NumPy limitations**
- All elements must be same type
- No column names or labels
- No built-in handling of missing values
- No built-in file I/O (CSV, Excel)

</div>

<div class="card card-success card-glass pad-tight">

### **Enter Pandas**
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

# Pandas: **DataFrames** & Real Data

<!--
Speaker: Pandas is NumPy plus labels, mixed types, and file I/O. Anchor it as
"Excel/SQL table you can script." Everything from here uses the DataFrame as the
central object. (~1 min)
-->

---
hideInToc: true
---

# What is Pandas?

<div class="card card-primary card-glass pad-tight mt-md">

## **Pandas = Panel Data (Python Data Analysis Library)**

Built on top of NumPy, adds:
- **DataFrame**: 2D labeled data structure (like Excel spreadsheet or SQL table)
- **Series**: 1D labeled array (single column)
- Easy reading/writing of files (CSV, Excel, JSON, SQL, etc.)
- Handling missing data
- Group-by operations, merging, reshaping

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### **Think of DataFrame as:**
- Excel spreadsheet
- SQL table
- Dictionary of NumPy arrays
- Collection of labeled columns

</div>

<div class="card card-secondary card-glass pad-tight">

### **Key Features:**
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

## **Most Common: CSV Files**

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

## **Real Data Has Missing Values!**

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

## **Group By Pattern**

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

# Group By: Advanced Aggregations

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 200),
    'detector': np.random.choice(['A', 'B', 'C'], 200),
    'run_number': np.random.choice([1, 2, 3], 200)
})

# Group by multiple columns
print("Mean energy per detector per run:")
print(df.groupby(['detector', 'run_number'])['energy'].mean().unstack())

# Count occurrences
print("\nEvents per detector:")
print(df['detector'].value_counts())
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
layout: section
hideInToc: true
---

# Real-World Example: **CERN Data**

<!--
Speaker: now put the tools to work on a physics-shaped problem — Higgs to two
photons. Walk through the signal-plus-background mindset; the same filter/cut
pattern reappears in their seminar project. (~1 min)
-->

---
hideInToc: true
---

# Example: Higgs to Two Photons Analysis

<div class="card card-info card-glass pad-tight mt-md">

## **Realistic Scenario**

You have data from a particle physics experiment looking for Higgs → γγ (two photons). Each event has:
- Two photon energies and directions
- Invariant mass (m<sub>γγ</sub>)
- Detector information
- Event quality flags

**Goal**: Identify Higgs signal around 125 GeV

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
n_sig, n_bkg = 300, 2000

signal_df = pd.DataFrame({'mass': np.random.normal(125, 1.5, n_sig), 'type': 'signal'})
background_df = pd.DataFrame({'mass': np.random.exponential(30, n_bkg) + 105, 'type': 'background'})

df = pd.concat([signal_df, background_df], ignore_index=True)
df = df[df['mass'] < 150]
counts = df['type'].value_counts()
print(f"Total events: {len(df)} (Signal: {counts['signal']}, Background: {counts['background']})")
```

---
hideInToc: true
---

# Exploratory Data Analysis: Statistics

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]

print("Summary statistics by type:")
print(df.groupby('type')['mass'].describe())

print(f"\nEvents near Higgs mass (124-126 GeV): {len(df[(df['mass']>124) & (df['mass']<126)])}")
```

---
hideInToc: true
---

# Exploratory Data Analysis: Visualization

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.hist(df['mass'], bins=50, range=(105, 150), edgecolor='white', alpha=0.7)
ax1.axvline(125, color='red', linestyle='--', label='Higgs mass')
ax1.set_xlabel('m$_{γγ}$ (GeV)'); ax1.set_ylabel('Events'); ax1.legend()

ax2.hist(df[df['type']=='background']['mass'], bins=50, range=(105,150), alpha=0.5, label='Bkg')
ax2.hist(df[df['type']=='signal']['mass'], bins=50, range=(105,150), alpha=0.7, label='Signal')
ax2.set_xlabel('m$_{γγ}$ (GeV)'); ax2.set_ylabel('Events'); ax2.legend()
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Data Filtering: Quality Cuts

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'mass': np.concatenate([np.random.normal(125, 1.5, 300),
                            np.random.exponential(30, 2000) + 105]),
    'photon1_E': np.random.uniform(40, 110, 2300),
    'photon2_E': np.random.uniform(35, 100, 2300),
    'detector_qual': np.random.choice(['good', 'bad'], 2300, p=[0.9, 0.1])
})
df = df[df['mass'] < 150]
print(f"Events before cuts: {len(df)}")

# Quality cut
df_qual = df[df['detector_qual'] == 'good']
print(f"After quality cut:  {len(df_qual)}")

# Energy cuts
df_cut = df_qual[(df_qual['photon1_E'] > 50) & (df_qual['photon2_E'] > 45)]
print(f"After energy cuts:  {len(df_cut)}")
```

---
hideInToc: true
---

# Data Filtering: Signal Region

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'mass': np.concatenate([np.random.normal(125, 1.5, 300),
                            np.random.exponential(30, 2000) + 105]),
    'photon1_E': np.random.uniform(40, 110, 2300),
    'photon2_E': np.random.uniform(35, 100, 2300),
    'detector_qual': np.random.choice(['good', 'bad'], 2300, p=[0.9, 0.1])
})
df = df[(df['mass'] < 150) & (df['detector_qual'] == 'good')]
df = df[(df['photon1_E'] > 50) & (df['photon2_E'] > 45)]

# Signal region (mass window around Higgs)
signal_region = df[(df['mass'] > 122) & (df['mass'] < 128)]
print(f"Events in signal region (122-128 GeV): {len(signal_region)}")

# Sideband regions (for background estimation)
sideband_low = df[(df['mass'] > 110) & (df['mass'] < 120)]
sideband_high = df[(df['mass'] > 130) & (df['mass'] < 140)]
print(f"Sideband events: {len(sideband_low) + len(sideband_high)}")
print(f"\nSignal region statistics:\n{signal_region['mass'].describe()}")
```

---
layout: section
hideInToc: true
---

# Data Cleaning & **Preprocessing**

<!--
Speaker: this is where real data bites — missing values, outliers, mixed formats.
Emphasize that cleaning is a documented, reproducible step, never ad-hoc deletion.
This is the heart of the seminar deliverable. (~1 min)
-->

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

## **Why Normalize?**

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
hideInToc: true
---

# Data Normalization: Min-Max Scaling

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.uniform(50, 150, 100),
    'momentum': np.random.uniform(1, 5, 100),
    'angle': np.random.uniform(0, np.pi, 100)
})

# Min-Max scaling: (x - min) / (max - min) → range [0, 1]
df_minmax = (df - df.min()) / (df.max() - df.min())

print("Min-Max scaled [0, 1]:")
print(df_minmax.describe().loc[['mean', 'std', 'min', 'max']])

# Compare original vs scaled
print("\nOriginal std:", df.std().values.round(2))
print("Scaled std:  ", df_minmax.std().values.round(2))
```

---
layout: section
hideInToc: true
---

# Saving and Loading Data

---
hideInToc: true
---

# File I/O with Pandas

<div class="card card-primary card-glass pad-tight mt-md">

## **Pandas Supports Many Formats**

Reading and writing data is easy and consistent across formats

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### **Reading Data**

```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# SQL / Parquet (large data)
df = pd.read_parquet('data.parquet')
```

</div>

<div class="card card-secondary card-glass pad-tight">

### **Writing Data**

```python
# CSV
df.to_csv('output.csv', index=False)

# Excel
df.to_excel('output.xlsx')

# JSON
df.to_json('output.json')

# SQL / Parquet
df.to_parquet('output.parquet')
```

</div>

</div>

<div class="note-text mt-sm">

💡 **Best practice**: CSV for human-readable data; HDF5 or Parquet for large datasets (faster, smaller). 📁 *Same idea across formats — pick by need, not habit.*

</div>

---
hideInToc: true
---

# CSV Read/Write Example

```python {*}{maxHeight:'380px'}
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'event_id': range(1, 101),
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100)
})

# Save to CSV
df.to_csv('particle_data.csv', index=False)
print("Saved to particle_data.csv")

# Read back
df_loaded = pd.read_csv('particle_data.csv')
print("\nLoaded data:")
print(df_loaded.head())

# Advanced: Read only specific columns
df_subset = pd.read_csv('particle_data.csv', usecols=['event_id', 'energy'])
print("\nSubset (selected columns):")
print(df_subset.head())

# Advanced: Read in chunks (for large files)
chunk_size = 10
for chunk in pd.read_csv('particle_data.csv', chunksize=chunk_size):
    print(f"Processing chunk of {len(chunk)} rows...")
    # Process chunk here
    break  # Just show first chunk
```

<div class="card card-warning card-glass pad-tight mt-sm">

**For very large files (GB+)**, use chunking or consider Dask/Polars for out-of-memory processing

</div>

---
layout: section
hideInToc: true
---

# Best Practices

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

**Remember**: Version control your analysis scripts and save intermediate results for reproducibility (more in the Reproducible Workflows lecture!)

</div>

---
hideInToc: true
---

# Performance Tips

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### **NumPy**

✅ Use vectorized operations (no loops!)

✅ Pre-allocate arrays if possible

✅ Use appropriate data types (int32 vs int64)

✅ Avoid unnecessary copies

</div>

<div class="card card-secondary card-glass pad-tight">

### **Pandas**

✅ Use `iterrows()` sparingly (slow!)

✅ Prefer vectorized operations or `apply()`

✅ Set index on frequently-filtered columns

✅ Use categorical dtype for repeated strings

</div>

<div class="card card-info card-glass pad-tight">

### **General**

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

# Real CERN Open Data

---
hideInToc: true
---

# CERN Open Data Portal

<div class="card card-accent card-glass pad-tight mt-md">

## **Explore Real Particle Physics Data**

CERN provides open access to real experimental data from LHC experiments!

**URL**: [http://opendata.cern.ch](http://opendata.cern.ch)

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### **Available Datasets**

- **LHCb**: beauty/charm decays, dimuon events
- **CMS**: proton-proton collisions (7, 8, 13 TeV)
- **ATLAS**: selected open-data releases
- **ALICE**: heavy-ion collisions

Formats: CSV, ROOT, HDF5

</div>

<div class="card card-secondary card-glass pad-tight">

### **Example Analyses**

- Higgs → ZZ → 4 leptons
- W/Z boson production
- Top quark pair production
- Dimuon mass spectrum
- Jet physics

Full tutorials and documentation provided!

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

**Your next step**: Apply these NumPy/Pandas skills to real data — the seminar running project uses the **LHCb D⁰ → K⁻π⁺** open dataset. The dimuon spectrum below (J/ψ, Υ) is a second LHCb example.

</div>

---
hideInToc: true
---

# Example: LHCb Dimuon Spectrum — Data

```py {monaco-run}
import pandas as pd
import numpy as np

# Simulated LHCb dimuon spectrum (illustrative — LHCb studies J/ψ, ψ(2S), Υ → μμ)
np.random.seed(42)
jpsi = np.random.normal(3.1, 0.1, 500)       # J/ψ peak (~3.1 GeV)
upsilon = np.random.normal(9.5, 0.2, 200)     # Υ peak (~9.5 GeV)
background = np.random.exponential(2.0, 2000)  # Continuum background

mass = np.concatenate([jpsi, upsilon, background])
df = pd.DataFrame({'dimuon_mass': mass[mass < 15]})

print(f"Total events: {len(df)}")
print(f"J/ψ region (2.8-3.4 GeV):    {len(df[(df['dimuon_mass']>2.8) & (df['dimuon_mass']<3.4)])}")
print(f"Υ region (9.0-10.5 GeV):     {len(df[(df['dimuon_mass']>9) & (df['dimuon_mass']<10.5)])}")
```

---
hideInToc: true
---

# Example: LHCb Dimuon Spectrum — Plot

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
jpsi = np.random.normal(3.1, 0.1, 500)
upsilon = np.random.normal(9.5, 0.2, 200)
background = np.random.exponential(2.0, 2000)
mass = np.concatenate([jpsi, upsilon, background])
df = pd.DataFrame({'dimuon_mass': mass[mass < 15]})

plt.figure(figsize=(10, 5))
plt.hist(df['dimuon_mass'], bins=100, range=(0, 15), edgecolor='white', linewidth=0.3)
plt.xlabel('Dimuon Mass (GeV/c²)', fontsize=12)
plt.ylabel('Events', fontsize=12)
plt.title('Dimuon Mass Spectrum (simulated LHCb data)', fontsize=14)
plt.axvline(3.1, color='red', ls='--', label='J/ψ (3.1 GeV)', lw=1.5)
plt.axvline(9.5, color='green', ls='--', label='Υ (9.5 GeV)', lw=1.5)
plt.legend(); plt.grid(alpha=0.3); plt.yscale('log')
plt.tight_layout(); plt.show()
```

---
layout: section
hideInToc: true
---

# Summary

---
hideInToc: true
---

# What We Learned: NumPy & Pandas

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **NumPy**

✅ ndarray: efficient multi-dimensional arrays

✅ Vectorization: fast element-wise operations

✅ Broadcasting: operations on different shapes

✅ Indexing, slicing, boolean masks

✅ 10-100× faster than Python lists

</div>

<div class="card card-secondary card-glass pad-tight">

## **Pandas**

✅ DataFrame: labeled 2D data structure

✅ Reading/writing files (CSV, Excel, JSON, etc.)

✅ Missing data handling

✅ Filtering, grouping, aggregating

✅ Data cleaning and preprocessing

</div>

</div>

---
hideInToc: true
---

# What We Learned: Skills & Next Steps

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### **Skills Acquired**

- Load real datasets
- Clean messy data
- Exploratory analysis
- Statistical summaries
- Visualization

</div>

<div class="card card-success card-glass pad-tight">

### **Best Practices**

- Visualize first
- Document everything
- Validate data quality
- Save intermediate results
- Keep raw data separate

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

### **Next Steps**

- Apply skills to real CERN open data
- Combine with the Data Fitting techniques
- Build complete analysis pipelines
- **Reproducible Workflows — automate your entire workflow!**

</div>

---
hideInToc: true
---

<MCQ
  question="You need the square of every value in a large NumPy array. Which is the fast, idiomatic NumPy approach?"
  :options="[
    'arr ** 2 — one vectorised operation over the whole array',
    'A Python for-loop that appends x*x to a list',
    'A list comprehension [x**2 for x in arr]',
    'arr.apply(lambda x: x**2)'
  ]"
  :correct="0"
  explanation="Vectorised operations run in C across the entire array at once — far faster than any Python-level loop or comprehension, and NumPy arrays have no apply method."
/>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Write vectorized NumPy code with **no explicit loops**

</div>

<div class="card card-success card-glass pad-compact">

✅ Build, filter, sort, and **group** a Pandas DataFrame

</div>

<div class="card card-success card-glass pad-compact">

✅ Clean data — missing values, **outliers**, normalization

</div>

<div class="card card-success card-glass pad-compact">

✅ Read and write data across **file formats**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 13 tie-in**

produce a clean, tidy processed table with Pandas — the analysis-ready version of your raw data.

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each card. The seminar
tie-in makes it concrete: they leave here and turn their own raw data into a
tidy, analysis-ready table. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# You now have the tools to work with real, messy data. 
---
hideInToc: true
layout: end
---

# Questions?

## Next lecture: **Reproducible Workflows & Automation**
