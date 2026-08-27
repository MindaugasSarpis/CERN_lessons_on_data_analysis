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

🎯 Index and slice arrays with **boolean masks**; use broadcasting for row/column maths

</div>

<div class="card card-accent card-glass pad-compact">

🐼 Build, filter, sort, and **group** a Pandas DataFrame

</div>

<div class="card card-success card-glass pad-compact">

🧹 Handle missing values, drop **duplicates & invalid rows**, detect outliers, normalize data

</div>

<div class="card card-warning card-glass pad-compact">

📁 Read and write data — **CSV** and Parquet

</div>

</div>

<!--
Speaker: read these as promises, not a checklist. Stress that Seminar 13 is where
they turn the shared D⁰ sample into a clean, tidy table — today builds the toolkit
for that. Set the expectation. (~1 min)
-->

---
hideInToc: true
---

# Motivation: From **Toy** Data to Real Data

<div class="card card-info card-glass pad-tight mt-md">

## 🧪 **Real Data Is Not a Gaussian + Exponential**

In the Data Fitting lecture the data was synthetic. Real-world data:
- Comes in various formats (CSV, Excel, JSON, Parquet, HDF5)
- Has missing values, outliers, duplicates and inconsistencies
- Is often large and needs efficient, loop-free operations

In **Lecture 8** you parsed the D⁰ CSV by hand with `csv.DictReader`. Today the same ingest is **one line** — and the cleaning is **five**.

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

# What is **NumPy**?

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

### ✅ **Why NumPy?**

**Speed**: typically 10× or more faster than Python lists — depends on the operation

**Memory**: compact, typed storage

**Convenience**: write mathematical code naturally

</div>

<div class="card card-secondary card-glass pad-tight">

### 💡 **Key Concept**

**Vectorization**: operations on entire arrays without explicit loops

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

# Creating NumPy **Arrays**

```py {monaco-run} {autorun:false}
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

# Array Operations: **Vectorization**

```py {monaco-run} {autorun:false}
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

# Speed Comparison: Lists vs **NumPy**

```py {monaco-run} {autorun:false}
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

**Key**: NumPy loops run in C, not Python. The speed-up depends on the operation — a plain `sum` gains more than a polynomial that builds temporaries — and grows with array size. Typically 10× or more.

</div>

---
hideInToc: true
---

# Array **Indexing** and Slicing

```py {monaco-run} {autorun:false}
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

# Broadcasting: **Concept**

<div class="card card-info card-glass pad-tight mt-md">

## 📐 **Broadcasting Rules**

NumPy "broadcasts" arrays of different shapes: shapes are compared **from the right**, and a dimension of size 1 (or a missing one) is stretched to match.

```python
arr + 10            # scalar → stretched to every element
matrix + row        # (3, 3) + (3,)  → row added to each row
matrix + col[:, None]   # (3, 3) + (3, 1) → column added to each column
```

</div>

```py {monaco-run} {autorun:false}
import numpy as np

# Scalar broadcasting
arr = np.array([1, 2, 3])
print(f"arr + 100: {arr + 100}")  # 100 broadcast to [100, 100, 100]

# Row broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
print(f"\nMatrix + row:\n{matrix + row}")  # row added to each row
```

---
hideInToc: true
---

# Broadcasting: **Normalization** Example

```py {monaco-run} {autorun:false}
import numpy as np

# Useful for normalization: subtract column means
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])
mean = data.mean(axis=0)  # Mean of each column → shape (2,)

print(f"Data:\n{data}")
print(f"Column means: {mean}")
print(f"Centered data:\n{data - mean}")  # (3, 2) - (2,) → mean subtracted from each column

# Standardization: (x - mean) / std
std = data.std(axis=0)
standardized = (data - mean) / std
print(f"\nStandardized:\n{standardized}")
```

---
hideInToc: true
---

<MCQ
  question="Array `a` has shape `(3, 2)`, `b` has shape `(2,)` and `c` has shape `(3,)`. Which addition is valid NumPy broadcasting?"
  :options="[
    'a + b — shapes align from the right (2 vs 2), so b is repeated for each of the 3 rows',
    'a + c — the leading 3 matches, so c is repeated for each of the 2 columns',
    'Both — NumPy matches whichever dimension happens to agree',
    'Neither — broadcasting only ever works with scalars'
  ]"
  :correct="0"
  explanation="Broadcasting compares shapes from the RIGHT: (3,2) vs (2,) agrees on the last axis, so b is stretched over the rows. (3,2) vs (3,) compares 2 with 3 and fails with 'operands could not be broadcast together'. To add a per-row vector, give it shape (3,1) with c[:, None]."
/>

---
hideInToc: true
---

# NumPy: When It's **Not Enough**

<div class="card card-info card-glass pad-tight mt-md">

## 🧱 **Limitations of NumPy**

NumPy is great for numerical computation, but real-world data often needs more:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### ⚠️ **NumPy limitations**
- All elements must be the same type
- No column names or labels
- No built-in handling of missing values
- Only numeric text I/O (`np.loadtxt`) — no headers, mixed types or Excel

</div>

<div class="card card-success card-glass pad-tight">

### ✅ **Enter Pandas**
- Mixed data types per column
- Named columns and row indices
- `NaN` for missing data
- Read/write CSV, Excel, JSON, Parquet, HDF5

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

**Pandas is built on top of NumPy** — it adds labels, mixed types, and data manipulation tools while keeping NumPy's speed for numerical operations.

</div>

---
layout: section
hideInToc: true
---

# Pandas: **DataFrames**

<!--
Speaker: Pandas is NumPy plus labels, mixed types, and file I/O. Anchor it as
"a spreadsheet you can script." Everything from here uses the DataFrame as the
central object: build it, read it, explore it, select from it. (~1 min)
-->

---
hideInToc: true
---

# What is **Pandas**?

<div class="card card-primary card-glass pad-tight mt-md">

## 🐼 **Pandas = Panel Data (Python Data Analysis Library)**

Built on top of NumPy, adds:
- **DataFrame**: 2D labeled data structure (like a spreadsheet or a database table)
- **Series**: 1D labeled array (single column)
- Easy reading/writing of files (CSV, Excel, JSON, Parquet, etc.)
- Handling missing data
- Group-by operations, merging, reshaping

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 🗂️ **Think of a DataFrame as:**
- A spreadsheet sheet
- A database table
- A dictionary of NumPy arrays
- A collection of labeled columns

</div>

<div class="card card-secondary card-glass pad-tight">

### 🔑 **Key Features:**
- Column/row labels (not just indices)
- Mixed data types per column
- Missing data handling (NaN)
- Powerful data manipulation

</div>

</div>

---
hideInToc: true
---

# Creating a **DataFrame**

```py {monaco-run} {autorun:false}
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

<div class="card card-info card-glass pad-compact mt-sm">

💡 A DataFrame is a **dict of equal-length columns**. Each column is a `Series` backed by a NumPy array — `df['age'].to_numpy()` hands the array back, so every NumPy trick from the first block still applies.

</div>

---
hideInToc: true
---

# Reading Data from **Files**

<div class="card card-primary card-glass pad-compact mt-sm">

📥 **In the seminar**: `df = pd.read_csv('data/raw/d0.csv')` — one line replaces Lecture 8's `csv.DictReader` loop. Below, the same call on an in-memory string so it runs in the browser.

</div>

```py {monaco-run} {autorun:false}
import io, pandas as pd

csv_text = """Run,Event,M,H1_Charge,H1_PX
101,1,1864.8,-1,2130.5
101,2,,1,-980.2
101,3,-999,-1,NA
102,4,1865.3,-999,3300.1
"""
df = pd.read_csv(io.StringIO(csv_text),            # a file path in real life
                 dtype={'Run': 'int32'},             # force a type
                 na_values=['', 'NA', '-999'],       # what counts as missing
                 usecols=['Run', 'Event', 'M', 'H1_Charge'])  # skip the rest
print(df)
print("\ndtypes:\n" + df.dtypes.to_string())
print("\nmissing per column:", df.isna().sum().to_dict())
```

<div class="note-text mt-sm">

💡 Later slides fake data with `np.random.seed(42)`; the modern idiom is `rng = np.random.default_rng(42)`.

</div>

---
hideInToc: true
---

# Exploring a **DataFrame**

```py {monaco-run} {autorun:false}
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
print(df.describe().round(2))

print("\nData types:")
print(df.dtypes)
```

<!--
Speaker: `describe()` is the first thing to run on any new table — the seminar
asks for exactly this printout. Note the text column: pandas 3 prints its dtype as
`str`; older versions (including the browser runner) print `object`. (~2 min)
-->

---
hideInToc: true
---

# Select, **Filter** & Query

```py {monaco-run} {autorun:false}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})
print(f"rows: {len(df)}, signal: {df['is_signal'].sum()}, background: {(~df['is_signal']).sum()}")

high_E = df[df['energy'] > 10]                       # one boolean mask
print(f"E > 10:                 {len(high_E)}")
sig_high = df[df['is_signal'] & (df['energy'] > 10)] # combine with & | ~ and parentheses
print(f"signal and E > 10:      {len(sig_high)}")
print(f"detector A and E > 10:  {len(df.query('energy > 10 and detector == \"A\"'))}")
print(f"detector A or B:        {len(df[df['detector'].isin(['A', 'B'])])}")
print(high_E.head(3))
```

---
hideInToc: true
---

<MCQ
  question="Which expression correctly selects the rows of `df` where column `a` is above 1 AND column `b` is below 2?"
  :options="[
    'df[(df.a > 1) & (df.b < 2)]',
    'df[df.a > 1 and df.b < 2]',
    'df[df.a > 1 & df.b < 2]',
    'df[(df.a > 1) && (df.b < 2)]'
  ]"
  :correct="0"
  explanation="Python's and tries to reduce each whole Series to a single True/False and raises 'The truth value of a Series is ambiguous'. Element-wise logic needs &, | and ~ — with parentheses, because & binds tighter than >, so the third option is parsed as df.a > (1 & df.b) < 2. There is no && in Python."
/>

---
hideInToc: true
---

# New **Columns** & Sorting

```py {monaco-run} {autorun:false}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

# Adding new columns — one vectorised expression, no loop
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

# Filter, then **Add a Column** — the Right Way

```py {monaco-run} {autorun:false}
import numpy as np, pandas as pd

np.random.seed(42)
df = pd.DataFrame({'Event': range(1, 9),
                   'M': np.random.uniform(1800, 2000, 8).round(1)})

# 1. filter with a mask   2. .copy() so the result owns its data
mask = df['M'].between(1800, 2000)
clean = df[mask].copy()

# 3. derive the column with a vectorised expression on the copy
clean['region'] = np.where(clean['M'].between(1845, 1885), 'signal', 'sideband')
print(clean)

# To write into the ORIGINAL frame instead, address it with .loc[mask, col]
df.loc[df['M'].between(1845, 1885), 'region'] = 'signal'
print(df['region'].value_counts(dropna=False))
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ `df2 = df[mask]` then `df2['x'] = 1` — in pandas 1–2 this is the **SettingWithCopyWarning**: is `df2` a view or a copy? Pandas 3 (**Copy-on-Write**) makes `df2` always behave as a copy, so the write never reaches `df`. Either way the intent is clear only with `.copy()` (new table) or `df.loc[mask, 'x'] = 1` (original).

</div>

---
hideInToc: true
---

<MCQ
  question="After `df2 = df[df.M > 1900]` you run `df2['flag'] = True`. What is the safe, intended way to write this?"
  :options="[
    'Take df2 = df[df.M > 1900].copy() first — then the assignment is unambiguous in every pandas version',
    'Nothing — df2 is always an independent copy, so the write is safe everywhere',
    'Use df2.flag = True (attribute assignment) instead of the bracket form',
    'Add warnings.filterwarnings(ignore) so the SettingWithCopyWarning goes away'
  ]"
  :correct="0"
  explanation="In pandas 1–2, df[mask] may be a view or a copy, so writing into it raises SettingWithCopyWarning and may silently not land where you expect. Pandas 3 (Copy-on-Write) makes df2 behave as a copy, but the intent is still clearest with .copy(). To write into the original, use df.loc[mask, 'flag'] = True. Silencing the warning hides the bug, it does not fix it."
/>

---
layout: section
hideInToc: true
---

# Data Cleaning & **Preprocessing**

<!--
Speaker: this is where real data bites — missing values, duplicates, impossible
values, outliers. Emphasize that cleaning is a documented, reproducible step,
never ad-hoc deletion. This block is the heart of the Seminar 13 script. (~1 min)
-->

---
hideInToc: true
---

# Common Data **Quality** Issues

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Missing Values**
- Empty cells, NaN, None, sentinels like `-999`
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

## ⚠️ **Duplicates & Invalid Rows**
- The same `(Run, Event)` counted twice
- Impossible values — negative mass, `|Q| ≠ 1`
- **Fix**: `drop_duplicates`, one boolean mask per rule

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

# Handling **Missing** Data

<div class="card card-warning card-glass pad-tight mt-md">

## 🕳️ **Real Data Has Missing Values!**

Pandas represents missing data with `NaN` (Not a Number) or `None` — `isna()` finds them

</div>

```py {monaco-run} {autorun:false}
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
print(f"\nMissing per column:\n{df.isna().sum()}")
```

---
hideInToc: true
---

# Missing Data: **Strategies**

```py {monaco-run} {autorun:false}
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

# Duplicates & **Invalid** Rows

```py {monaco-run} {autorun:false}
import pandas as pd

df = pd.DataFrame({                      # shaped like the seminar sample
    'Run':       [101, 101, 101, 101, 102, 102, 102],
    'Event':     [1,   2,   2,   3,   1,   2,   3],
    'M':         [1864.8, 1901.2, 1901.2, -1.0, 1866.1, 1879.9, 1850.4],
    'H1_Charge': [-1, 1, 1, -1, 0, 1, -1],
})
print(f"raw rows: {len(df)}")

# Duplicates: the same (Run, Event) pair is the same collision counted twice
dup = df.duplicated(['Run', 'Event'])
print(f"duplicate (Run, Event) pairs: {dup.sum()}")
df = df.drop_duplicates(['Run', 'Event'])

# Invalid: non-physical mass, bad charge — one boolean mask per rule
valid = (df['M'] > 0) & df['H1_Charge'].abs().eq(1)
print(f"invalid rows (M <= 0 or |Q| != 1): {(~valid).sum()}")
df = df[valid]
print(f"\nclean rows: {len(df)}")
print(df)
```

<!--
Speaker: this is Seminar 9's audit policy in six lines, and exactly what Seminar
13 task 2 and task 6 ask for — the counts printed here must match the hand-written
audit numbers. Point out that each rule is one readable boolean mask. (~2 min)
-->

---
hideInToc: true
---

# Detecting Outliers: **Z-Score** Method

```py {monaco-run} {autorun:false}
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

<div class="note-text mt-sm">

💡 NumPy's `.std()` divides by *n* (`ddof=0`); pandas' `.std()` divides by *n − 1* (`ddof=1`) — the sample estimate from Lecture 11. Same data, slightly different numbers.

</div>

<!--
Speaker: five outliers were injected; z-score finds only 4 — the 180 is masked
because the outliers themselves inflate the std to ~29 (vs 10 for the clean
data). That is the weakness of a mean/std rule on contaminated data. (~2 min)
-->

---
hideInToc: true
---

# Detecting Outliers: **IQR** Method

```py {monaco-run} {autorun:false}
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

<!--
Speaker: quartiles are robust, so IQR catches all 5 injected outliers — but it
reports 6: the sixth (73.8) is a legitimate tail point of the Gaussian. Two methods,
two answers — which is why you never delete outliers blindly; flag them, look, and
document the decision (Seminar 9 task 5). (~2 min)
-->

---
hideInToc: true
---

# Data Normalization: **Why** and How

<div class="card card-info card-glass pad-tight mt-md">

## 📏 **Why Normalize?**

- Different features have different scales (energy in GeV, angles in radians)
- Many ML algorithms perform better with normalized data
- Makes features comparable

</div>

```py {monaco-run} {autorun:false}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.uniform(50, 150, 100),
    'angle': np.random.uniform(0, np.pi, 100)
})
print("Original scales:")
print(df.describe().loc[['mean', 'std', 'min', 'max']].round(2))

# Standardization: (x - mean) / std → mean=0, std=1
df_std = (df - df.mean()) / df.std()
print("\nStandardized (z-score):")
print(df_std.describe().loc[['mean', 'std', 'min', 'max']].round(3))
```

---
hideInToc: true
---

# Normalization: **Min-Max** Scaling

```py {monaco-run} {autorun:false}
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
print(df_minmax.describe().loc[['mean', 'std', 'min', 'max']].round(3))

# Compare original vs scaled
print("\nOriginal std:", df.std().values.round(2))
print("Scaled std:  ", df_minmax.std().values.round(2))
```

---
layout: section
hideInToc: true
---

# Group By & **Visualisation**

<!--
Speaker: with a clean table in hand, the questions become "per category": counts
per region, mean per detector. Split-apply-combine answers all of them in one line,
and pandas' built-in plotting shows the answer straight from the frame. (~1 min)
-->

---
hideInToc: true
---

# Group By: **Split-Apply-Combine**

<div class="card card-info card-glass pad-tight mt-md">

## 🔀 **Group By Pattern**

1. **Split** data into groups based on criteria
2. **Apply** a function to each group
3. **Combine** results into a data structure

</div>

```py {monaco-run} {autorun:false}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 200),
    'detector': np.random.choice(['A', 'B', 'C'], 200),
})

print("Statistics per detector:")
print(df.groupby('detector')['energy'].agg(['count', 'mean', 'std']).round(2))
```

<div class="note-text mt-sm">

💡 The same split-apply-combine powers **sideband / signal-region** counts: tag each event with a `region` label, then `df.groupby('region').size()` returns every yield at once — the Seminar 13 stretch goal.

</div>

---
hideInToc: true
---

# Group By: **Advanced** Aggregations

```py {monaco-run} {autorun:false}
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
print(df.groupby(['detector', 'run_number'])['energy'].mean().unstack().round(2))

# Count occurrences
print("\nEvents per detector:")
print(df['detector'].value_counts())
```

---
hideInToc: true
---

# Visualization with Pandas: **Histograms**

<div class="card card-accent card-glass pad-compact mt-sm">

Pandas has built-in plotting (Matplotlib under the hood) — `df['M'].plot.hist(...)` is the Seminar 13 stretch goal. Shared `bins` make two histograms comparable.

</div>

```py {monaco-run} {autorun:false}
import pandas as pd, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
n = 500
is_signal = np.random.choice([True, False], n, p=[0.3, 0.7])
# Signal peaks at 15 GeV; background is a broad gamma tail — different shapes
energy = np.where(is_signal, np.random.normal(15, 2, n), np.random.gamma(5, 2, n))
df = pd.DataFrame({'energy': energy, 'is_signal': is_signal})

fig, ax = plt.subplots(figsize=(10, 4))
bins = np.linspace(0, 30, 31)                  # shared bins → comparable histograms
df.loc[df['is_signal'], 'energy'].hist(bins=bins, alpha=0.5, label='Signal', ax=ax)
df.loc[~df['is_signal'], 'energy'].hist(bins=bins, alpha=0.5, label='Background', ax=ax)
ax.set_xlabel('Energy (GeV)'); ax.set_ylabel('Counts')
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()
```

---
layout: section
hideInToc: true
---

# Saving and **Loading** Data

<!--
Speaker: the output of the cleaning script is a file — which format? CSV for
humans and small tables, Parquet for anything you will read back by machine:
typed, compressed, columnar. The seminar writes events_clean.parquet. (~1 min)
-->

---
hideInToc: true
---

# File I/O with **Pandas**

<div class="card card-primary card-glass pad-tight mt-md">

## 📁 **Pandas Supports Many Formats**

Reading and writing data is easy and consistent across formats

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

### 📥 **Reading Data**

```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# Parquet (large data)
df = pd.read_parquet('data.parquet')
```

</div>

<div class="card card-secondary card-glass pad-tight">

### 📤 **Writing Data**

```python
# CSV
df.to_csv('output.csv', index=False)

# Excel
df.to_excel('output.xlsx', index=False)

# JSON
df.to_json('output.json')

# Parquet
df.to_parquet('output.parquet')
```

</div>

</div>

<div class="note-text mt-sm">

💡 **Best practice**: CSV for human-readable data; HDF5 or Parquet for large datasets (faster, smaller). Modern route for large/mixed tables — the Arrow backend: `pd.read_csv(..., dtype_backend="pyarrow")` or `df.convert_dtypes()`. 📁 *Same idea across formats — pick by need, not habit.*

</div>

---
hideInToc: true
---

# CSV → **Parquet** Round-Trip

```python
import pandas as pd

df = pd.read_csv('data/raw/d0.csv')                          # text in ...
df = df.drop_duplicates(['Run', 'Event'])
df = df[(df['M'] > 0) & df['H1_Charge'].abs().eq(1)]

df.to_parquet('data/processed/events_clean.parquet')         # ... typed, compressed, columnar out
back = pd.read_parquet('data/processed/events_clean.parquet')
assert back.equals(df)                                       # exact round-trip, dtypes included

# Read only the columns you need (Parquet skips the rest on disk)
df = pd.read_csv('data/raw/d0.csv', usecols=['Run', 'Event', 'M'])

# Stream a CSV too big for memory, one chunk at a time
with pd.read_csv('data/raw/d0.csv', chunksize=10_000) as reader:
    n_peak = sum(chunk['M'].between(1845, 1885).sum() for chunk in reader)
```

<div class="card card-warning card-glass pad-compact mt-sm">

🧪 **Not runnable in the browser** — Parquet needs the `pyarrow` engine (`pip install pyarrow`), which the in-browser Python does not ship. Run it in the seminar; this is `scripts/clean.py` minus the `region` column. For GB+ files, chunking or Dask/Polars keep memory flat.

</div>

---
layout: section
hideInToc: true
---

# Worked Example: **CERN** Data

<!--
Speaker: now put the tools to work on physics-shaped problems — a one-frame Higgs
warm-up, then the full clean → label → count → plot chain on a sample shaped like
the seminar's D⁰ file. The same filter/cut pattern reappears in Seminar 13. (~1 min)
-->

---
hideInToc: true
---

# Warm-up: **Higgs** → γγ in One Frame

<div class="card card-info card-glass pad-compact mt-sm">

Signal and background live in **one** DataFrame with a `type` label — so `groupby` describes both at once and a mask counts the window. **Goal**: see the Higgs near 125 GeV.

</div>

```py {monaco-run} {autorun:false}
import pandas as pd, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]
print(df.groupby('type')['mass'].describe()[['count', 'mean', 'std', 'min', 'max']].round(2))
window = df['mass'].between(122, 128)
print(f"events in 122-128 GeV: {window.sum()} (signal: {(window & (df['type'] == 'signal')).sum()})")

fig, ax = plt.subplots(figsize=(10, 3.2))
ax.hist(df['mass'], bins=45, range=(105, 150), edgecolor='white', alpha=0.7)
ax.axvline(125, color='red', ls='--', label='Higgs (125 GeV)')
ax.set_xlabel('m$_{γγ}$ (GeV)'); ax.set_ylabel('Events'); ax.legend()
plt.tight_layout(); plt.show()
```

---
hideInToc: true
---

# CERN Open Data **Portal**

<div class="card card-accent card-glass pad-tight mt-md">

## 🌐 **Explore Real Particle Physics Data**

CERN provides open access to real experimental data from LHC experiments!

**URL**: [http://opendata.cern.ch](http://opendata.cern.ch)

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### 📚 **Available Datasets**

- **LHCb**: beauty/charm decays, dimuon events
- **CMS**: proton-proton collisions (7, 8, 13 TeV)
- **ATLAS**: selected open-data releases
- **ALICE**: heavy-ion collisions

Formats: CSV, ROOT, HDF5

</div>

<div class="card card-secondary card-glass pad-tight">

### 🔬 **Example Analyses**

- Higgs → ZZ → 4 leptons
- W/Z boson production
- Top quark pair production
- Dimuon mass spectrum
- Jet physics

Full tutorials and documentation provided!

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

**Your next step**: Apply these NumPy/Pandas skills to real data — the seminars use the **LHCb D⁰ → K⁻π⁺** open dataset (record 401), whose K⁻π⁺ invariant-mass column `M` (D⁰ peak near **1865 MeV**) you clean, label and plot on the next three slides.

</div>

---
hideInToc: true
---

# D⁰ Sample: **Quality** Cuts

```py {monaco-run} {autorun:false}
import pandas as pd, numpy as np

np.random.seed(42)
n_sig, n_bkg = 800, 4000
df = pd.DataFrame({                                   # shaped like the seminar sample
    'Run':   np.random.choice([101, 102, 103], n_sig + n_bkg),
    'Event': np.arange(n_sig + n_bkg),
    'M':     np.concatenate([np.random.normal(1865, 9, n_sig),        # D⁰ peak (~1865 MeV)
                             np.random.uniform(1800, 2000, n_bkg)]),  # combinatorial background
    'H1_Charge': np.random.choice([-1, 1, 0], n_sig + n_bkg, p=[0.49, 0.49, 0.02]),
})
df.loc[np.random.choice(df.index, 30, replace=False), 'M'] = -999   # a few corrupt masses ...
df = pd.concat([df, df.sample(50, random_state=1)])                 # ... and 50 duplicated events
print(f"raw rows: {len(df)}")
print(f"duplicates: {df.duplicated(['Run', 'Event']).sum()}, "
      f"invalid: {((df['M'] <= 0) | df['H1_Charge'].abs().ne(1)).sum()}")

# The Seminar 9 policy, vectorised: two lines
df = df.drop_duplicates(['Run', 'Event'])
df = df[(df['M'] > 0) & df['H1_Charge'].abs().eq(1)].copy()
print(f"clean rows: {len(df)}")
print(df.describe()[['M', 'H1_Charge']].round(1))
```

---
hideInToc: true
---

# D⁰ Sample: **Signal** Region & Sidebands

```py {monaco-run} {autorun:false}
import pandas as pd, numpy as np

np.random.seed(42)
m = np.concatenate([np.random.normal(1865, 9, 800), np.random.uniform(1800, 2000, 4000)])
df = pd.DataFrame({'Event': np.arange(len(m)), 'M': m})      # the cleaned sample

# Label every event: signal window 1845-1885, sidebands 1800-1830 / 1900-2000
in_signal = df['M'].between(1845, 1885)
in_sideband = df['M'].between(1800, 1830) | df['M'].between(1900, 2000)
df['region'] = np.select([in_signal, in_sideband], ['signal', 'sideband'], default='gap')

print(df.groupby('region').size())                             # every yield at once
print(df.groupby('region')['M'].describe()[['count', 'mean', 'std', 'min', 'max']].round(1))

# Sideband subtraction: background under the peak ≈ sideband density × window width
bkg_per_MeV = (df['region'] == 'sideband').sum() / (30 + 100)
n_sig = (df['region'] == 'signal').sum() - bkg_per_MeV * 40
print(f"\nestimated signal yield: {n_sig:.0f}  (800 injected)")
```

<!--
Speaker: this is the `region` column of Seminar 13 task 3 and the groupby stretch
goal. np.select is the multi-way np.where; pd.cut works too when the bins are
contiguous. The sideband subtraction lands within a few events of the truth. (~2 min)
-->

---
hideInToc: true
---

# D⁰ Sample: **Plot** the Spectrum

```py {monaco-run} {autorun:false}
import pandas as pd, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
m = np.concatenate([np.random.normal(1865, 9, 800), np.random.uniform(1800, 2000, 4000)])
df = pd.DataFrame({'M': m})

fig, ax = plt.subplots(figsize=(10, 4.2))
ax.hist(df['M'], bins=100, range=(1800, 2000), edgecolor='white', linewidth=0.3)
ax.axvspan(1845, 1885, color='red', alpha=0.15, label='signal window')
ax.axvspan(1800, 1830, color='gray', alpha=0.25, label='sidebands')
ax.axvspan(1900, 2000, color='gray', alpha=0.25)
ax.axvline(1865, color='red', ls='--', lw=1.5, label='D⁰ (1865 MeV)')
ax.set_xlabel('K⁻π⁺ invariant mass (MeV/c²)')
ax.set_ylabel('Events')
ax.set_title('K⁻π⁺ invariant-mass spectrum (simulated, shaped like the seminar sample)')
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()
```

<div class="note-text mt-sm">

💡 In the seminar this is one line from the cleaned frame: `df['M'].plot.hist(bins=100, range=(1800, 2000), ax=ax)`.

</div>

---
layout: section
hideInToc: true
---

# Bringing It **Together**

<!--
Speaker: close with habits, not syntax — the do's and don'ts are what separate a
reproducible cleaning script from a notebook full of ad-hoc edits. Then one last
check question and the recap. (~1 min)
-->

---
hideInToc: true
---

# Best Practices: **Do's** and Don'ts

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-tight">

## ✅ **Do**

1. **Visualize first** — distributions before analysis
2. **Check for missing values** before any computation
3. **Document data sources** and every preprocessing step
4. **Validate data quality** — ranges, units, consistency
5. **Keep raw data separate** — `processed/` is regenerable

</div>

<div class="card card-warning card-glass pad-tight">

## ❌ **Don't**

1. **Assume data is clean** without checking
2. **Delete outliers** without understanding why they exist
3. **Mix loading and analysis** — separate the pipeline steps
4. **Hardcode file paths** — use config or CLI arguments
5. **Skip exploratory analysis** — jumping to conclusions costs time

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

**Rule of thumb**: if you can't explain where every number came from, go back and document your pipeline. Version-control the scripts and save intermediate results — more in the Reproducible Workflows lecture.

</div>

---
hideInToc: true
---

# Performance **Tips**

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

✅ Prefer vectorised column operations

⚠️ `apply()` is a Python loop in disguise — last resort

❌ `iterrows()` — almost never

✅ Use categorical dtype for repeated strings

</div>

<div class="card card-info card-glass pad-tight">

### ⚙️ **General**

✅ Profile code to find bottlenecks

✅ Load only needed columns

✅ Filter early (before heavy operations)

✅ Consider Dask/Polars for out-of-memory datasets

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

✅ Clean data — missing values, **duplicates**, outliers, normalization

</div>

<div class="card card-success card-glass pad-compact">

✅ Read and write data — **CSV and Parquet**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 13 tie-in**

Produce a clean, tidy `processed/` table with one Pandas script — `read_csv` → drop invalid rows & `(Run, Event)` duplicates → add a `region` label → `to_parquet` → `describe()` — on the shared D⁰ sample (or your own dataset).

**Next steps**: that script becomes one rule of a `Makefile` — Reproducible Workflows, next lecture.

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each card. The seminar
tie-in makes it concrete: they leave here and turn the shared D⁰ sample into a
tidy, analysis-ready table with a single script. (~1 min)
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
