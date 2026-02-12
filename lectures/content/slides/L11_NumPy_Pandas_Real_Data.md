---
mermaid: true
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

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

# Lessons on **Data Analysis** from **CERN**

## NumPy, Pandas & Real Data

---
hideInToc: true
layout: quote
---

# Real data is messy, incomplete, and comes in various formats. NumPy and Pandas are the foundational tools for handling, cleaning, and analyzing data efficiently in Python.

---
hideInToc: true
---

# Motivation

<div class="card card-info pad-tight mt-md">

## **From Toy Examples to Real Data**

In L10, we worked with synthetic data (Gaussian + exponential). But real-world data:
- Comes in various formats (CSV, Excel, JSON, HDF5)
- Has missing values, outliers, and inconsistencies
- Requires cleaning and preprocessing
- Is often large and requires efficient operations

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

### 🔢 **NumPy**
- Efficient numerical arrays
- Vectorized operations (fast!)
- Mathematical functions
- Foundation for scientific Python

</div>

<div class="card card-secondary pad-tight">

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

<div class="card card-primary pad-tight mt-md">

## **NumPy = Numerical Python**

The fundamental package for scientific computing in Python:
- Multi-dimensional arrays (`ndarray`)
- Fast element-wise operations (vectorization)
- Linear algebra, random numbers, Fourier transforms
- Foundation for SciPy, Pandas, Matplotlib, scikit-learn, etc.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info pad-tight">

### **Why NumPy?**

✅ **Speed**: 10-100× faster than Python lists

✅ **Memory**: More efficient storage

✅ **Convenience**: Write mathematical code naturally

</div>

<div class="card card-secondary pad-tight">

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
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr1}")
print(f"Type: {type(arr1)}, dtype: {arr1.dtype}")

# Create arrays with built-in functions
zeros = np.zeros(5)
ones = np.ones(5)
arange = np.arange(0, 10, 2)  # start, stop, step (like range())
linspace = np.linspace(0, 1, 5)  # start, stop, num_points (inclusive)

print(f"\nzeros:    {zeros}")
print(f"ones:     {ones}")
print(f"arange:   {arange}")
print(f"linspace: {linspace}")

# 2D arrays (matrices)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"\n2D array:\n{matrix}")
print(f"Shape: {matrix.shape}")  # (rows, columns)
```

---
hideInToc: true
---

# Array Operations: Vectorization

```py {monaco-run}
import numpy as np

# Create sample data
x = np.array([1, 2, 3, 4, 5])

# Element-wise operations (no loops needed!)
print(f"Original:     {x}")
print(f"x + 10:       {x + 10}")
print(f"x * 2:        {x * 2}")
print(f"x ** 2:       {x ** 2}")
print(f"np.sqrt(x):   {np.sqrt(x)}")
print(f"np.exp(x):    {np.exp(x)}")

# Operations between arrays
y = np.array([10, 20, 30, 40, 50])
print(f"\ny:            {y}")
print(f"x + y:        {x + y}")
print(f"x * y:        {x * y}")

# Aggregation functions
print(f"\nSum:  {x.sum()}")
print(f"Mean: {x.mean()}")
print(f"Std:  {x.std()}")
print(f"Min:  {x.min()}, Max: {x.max()}")
```

<div class="card card-accent pad-tight mt-sm">

**Key**: All these operations are implemented in C, making them extremely fast even for millions of elements!

</div>

---
hideInToc: true
---

# Speed Comparison: Lists vs NumPy

```py {monaco-run}
import numpy as np
import time

# Create large dataset
n = 100000
python_list = list(range(n))
numpy_array = np.arange(n)

# Test 1: Sum (Python list with loop)
start = time.time()
total = 0
for x in python_list:
    total += x
list_time = time.time() - start

# Test 2: Sum (NumPy)
start = time.time()
total_np = numpy_array.sum()
numpy_time = time.time() - start

print(f"Python list sum: {list_time*1000:.3f} ms")
print(f"NumPy sum:       {numpy_time*1000:.3f} ms")
print(f"Speedup:         {list_time/numpy_time:.1f}x faster")

# Test element-wise operations
start = time.time()
result_list = [x**2 + 2*x + 1 for x in python_list]
list_time2 = time.time() - start

start = time.time()
result_numpy = numpy_array**2 + 2*numpy_array + 1
numpy_time2 = time.time() - start

print(f"\nPolynomial evaluation:")
print(f"Python list:     {list_time2*1000:.3f} ms")
print(f"NumPy:           {numpy_time2*1000:.3f} ms")
print(f"Speedup:         {list_time2/numpy_time2:.1f}x faster")
```

---
hideInToc: true
---

# Array Indexing and Slicing

```py {monaco-run}
import numpy as np

# 1D arrays
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(f"Array: {arr}")
print(f"arr[0]:     {arr[0]}")      # First element
print(f"arr[-1]:    {arr[-1]}")     # Last element
print(f"arr[2:5]:   {arr[2:5]}")    # Slice [start:stop)
print(f"arr[::2]:   {arr[::2]}")    # Every 2nd element
print(f"arr[::-1]:  {arr[::-1]}")   # Reverse

# Boolean indexing (very powerful!)
mask = arr > 50
print(f"\nmask (arr > 50): {mask}")
print(f"arr[arr > 50]:   {arr[mask]}")

# 2D arrays
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\nMatrix:\n{matrix}")
print(f"matrix[1, 2]:    {matrix[1, 2]}")     # Row 1, Col 2 = 6
print(f"matrix[1, :]:    {matrix[1, :]}")     # Entire row 1
print(f"matrix[:, 2]:    {matrix[:, 2]}")     # Entire column 2
```

---
hideInToc: true
---

# Broadcasting: Operating on Different Shapes

<div class="card card-info pad-tight mt-md">

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

# Example 1: Scalar broadcasting
arr = np.array([1, 2, 3])
print(f"arr:       {arr}")
print(f"arr + 100: {arr + 100}")  # 100 broadcast to [100, 100, 100]

# Example 2: Row broadcasting
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row = np.array([10, 20, 30])

print(f"\nMatrix:\n{matrix}")
print(f"Row: {row}")
print(f"\nMatrix + row:\n{matrix + row}")  # row broadcast to each row

# Example 3: Useful for normalization
data = np.array([[1, 2], [3, 4], [5, 6]])
mean = data.mean(axis=0)  # Mean of each column
print(f"\nData:\n{data}")
print(f"Column means: {mean}")
print(f"Centered data:\n{data - mean}")  # Subtract mean from each column
```

---
layout: section
hideInToc: true
---

# Pandas: **DataFrames** & Real Data

---
hideInToc: true
---

# What is Pandas?

<div class="card card-primary pad-tight mt-md">

## **Pandas = Panel Data (Python Data Analysis Library)**

Built on top of NumPy, adds:
- **DataFrame**: 2D labeled data structure (like Excel spreadsheet or SQL table)
- **Series**: 1D labeled array (single column)
- Easy reading/writing of files (CSV, Excel, JSON, SQL, etc.)
- Handling missing data
- Group-by operations, merging, reshaping

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info pad-tight">

### **Think of DataFrame as:**
- Excel spreadsheet
- SQL table
- Dictionary of NumPy arrays
- Collection of labeled columns

</div>

<div class="card card-secondary pad-tight">

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
import numpy as np

# Method 1: From dictionary
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['Geneva', 'Zurich', 'Geneva', 'Bern'],
    'salary': [75000, 85000, 95000, 80000]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print(f"\nShape: {df.shape} (rows, columns)")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types:\n{df.dtypes}")

# Accessing columns
print(f"\nNames: {df['name'].tolist()}")
print(f"Average age: {df['age'].mean():.1f}")

# Accessing rows by index
print(f"\nFirst row:\n{df.iloc[0]}")  # iloc = integer location
```

---
hideInToc: true
---

# Reading Data from Files

<div class="card card-primary pad-tight mt-md">

## **Most Common: CSV Files**

Pandas makes reading data trivial:

```python
df = pd.read_csv('data.csv')
```

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

# Simulate reading a CSV by creating sample data
# In practice, you'd use: df = pd.read_csv('experiment_data.csv')

# Create synthetic experimental data
np.random.seed(42)
df = pd.DataFrame({
    'event_id': range(1, 101),
    'energy': np.random.gamma(5, 2, 100),  # Particle energy (GeV)
    'momentum': np.random.normal(10, 3, 100),  # Momentum (GeV/c)
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nInfo about dataset:")
df.info()
```

---
hideInToc: true
---

# Data Exploration: Basic Operations

```py {monaco-run}
import pandas as pd
import numpy as np

# Create sample particle physics data
np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

# Basic operations
print(f"Number of rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# Selection
print(f"\nSignal events: {df['is_signal'].sum()}")
print(f"Background events: {(~df['is_signal']).sum()}")

# Filtering (boolean indexing)
signal_df = df[df['is_signal']]
high_energy = df[df['energy'] > 10]

print(f"\nSignal events with E > 10 GeV: {len(signal_df[signal_df['energy'] > 10])}")

# Adding new columns
df['E/p_ratio'] = df['energy'] / df['momentum']
print(f"\nNew column 'E/p_ratio' created")
print(df[['energy', 'momentum', 'E/p_ratio']].head())

# Sorting
df_sorted = df.sort_values('energy', ascending=False)
print(f"\nTop 3 highest energy events:")
print(df_sorted[['energy', 'detector', 'is_signal']].head(3))
```

---
hideInToc: true
---

# Handling Missing Data

<div class="card card-warning pad-tight mt-md">

## **Real Data Has Missing Values!**

Pandas represents missing data with `NaN` (Not a Number) or `None`

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

# Create data with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50],
    'C': [100, 200, 300, 400, 500]
})

print("DataFrame with missing values:")
print(df)

# Check for missing values
print(f"\nMissing values per column:")
print(df.isnull().sum())

# Drop rows with any missing values
print(f"\nDrop rows with NaN:")
print(df.dropna())

# Fill missing values
print(f"\nFill NaN with 0:")
print(df.fillna(0))

# Fill with column mean
print(f"\nFill NaN with column mean:")
print(df.fillna(df.mean()))

# Forward fill (use previous value)
print(f"\nForward fill:")
print(df.ffill())
```

---
hideInToc: true
---

# Group By: Split-Apply-Combine

<div class="card card-info pad-tight mt-md">

## **Group By Pattern**

1. **Split** data into groups based on criteria
2. **Apply** a function to each group
3. **Combine** results into a data structure

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

# Create particle physics data
np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 200),
    'detector': np.random.choice(['A', 'B', 'C'], 200),
    'run_number': np.random.choice([1, 2, 3], 200)
})

# Group by detector
print("Statistics per detector:")
print(df.groupby('detector')['energy'].describe())

# Multiple aggregations
print("\nCustom aggregations per detector:")
print(df.groupby('detector')['energy'].agg(['count', 'mean', 'std', 'min', 'max']))

# Group by multiple columns
print("\nMean energy per detector per run:")
print(df.groupby(['detector', 'run_number'])['energy'].mean())

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

# Create sample dataset
np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 100),
    'momentum': np.random.normal(10, 3, 100),
    'detector': np.random.choice(['A', 'B', 'C'], 100),
    'is_signal': np.random.choice([True, False], 100, p=[0.3, 0.7])
})

# Method 1: Boolean indexing
high_energy = df[df['energy'] > 12]
print(f"High energy events (E > 12): {len(high_energy)}")

# Method 2: Multiple conditions with & (and) | (or)
signal_high_E = df[(df['is_signal']) & (df['energy'] > 10)]
print(f"Signal events with E > 10: {len(signal_high_E)}")

# Method 3: Query method (more readable for complex conditions)
result = df.query('energy > 10 and detector == "A"')
print(f"\nDetector A events with E > 10: {len(result)}")

# isin() for multiple values
detector_AB = df[df['detector'].isin(['A', 'B'])]
print(f"Events in detectors A or B: {len(detector_AB)}")

# Select specific columns
subset = df[df['is_signal']][['energy', 'momentum', 'detector']]
print(f"\nSignal events (selected columns):")
print(subset.head())
```

---
hideInToc: true
---

# Visualization with Pandas

<div class="card card-accent pad-tight mt-md">

Pandas has built-in plotting (uses Matplotlib under the hood)

</div>

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.gamma(5, 2, 500),
    'detector': np.random.choice(['A', 'B', 'C'], 500),
    'is_signal': np.random.choice([True, False], 500, p=[0.3, 0.7])
})

# Histogram
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

df['energy'].hist(bins=30, ax=axes[0], edgecolor='white')
axes[0].set_xlabel('Energy (GeV)')
axes[0].set_ylabel('Counts')
axes[0].set_title('Energy Distribution')
axes[0].grid(alpha=0.3)

# Grouped histogram
df[df['is_signal']]['energy'].hist(bins=30, alpha=0.5, label='Signal', ax=axes[1])
df[~df['is_signal']]['energy'].hist(bins=30, alpha=0.5, label='Background', ax=axes[1])
axes[1].set_xlabel('Energy (GeV)')
axes[1].set_ylabel('Counts')
axes[1].set_title('Signal vs Background')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Summary statistics
print("Energy statistics by signal type:")
print(df.groupby('is_signal')['energy'].describe())
```

---
layout: section
hideInToc: true
---

# Real-World Example: **CERN Data**

---
hideInToc: true
---

# Example: Higgs to Two Photons Analysis

<div class="card card-info pad-tight mt-md">

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
import matplotlib.pyplot as plt

# Simulate Higgs -> gamma gamma data
np.random.seed(42)
n_signal, n_background = 300, 2000

# Signal: Gaussian around 125 GeV
signal_mass = np.random.normal(125, 1.5, n_signal)
signal_df = pd.DataFrame({
    'mass': signal_mass,
    'type': 'signal',
    'photon1_E': np.random.uniform(50, 100, n_signal),
    'photon2_E': np.random.uniform(40, 90, n_signal)
})

# Background: Exponential
background_mass = np.random.exponential(30, n_background) + 105
background_df = pd.DataFrame({
    'mass': background_mass,
    'type': 'background',
    'photon1_E': np.random.uniform(40, 110, n_background),
    'photon2_E': np.random.uniform(35, 100, n_background)
})

# Combine
df = pd.concat([signal_df, background_df], ignore_index=True)
df = df[df['mass'] < 150]  # Analysis window

print(f"Total events: {len(df)}")
print(f"Signal: {len(signal_df)}, Background: {len(background_df)}")
print(f"\nFirst few events:")
print(df.head())
```

---
hideInToc: true
---

# Exploratory Data Analysis

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Recreate dataset
np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]

# Basic statistics
print("Summary statistics:")
print(df.groupby('type')['mass'].describe())

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Histogram of all data
ax1.hist(df['mass'], bins=50, range=(105, 150), edgecolor='white', alpha=0.7)
ax1.set_xlabel('m$_{γγ}$ (GeV)', fontsize=11)
ax1.set_ylabel('Events / 0.9 GeV', fontsize=11)
ax1.set_title('Diphoton Mass Distribution', fontsize=12)
ax1.grid(alpha=0.3)
ax1.axvline(125, color='red', linestyle='--', linewidth=1.5, label='Higgs mass')
ax1.legend()

# Separate signal and background
ax2.hist(df[df['type']=='background']['mass'], bins=50, range=(105, 150),
         alpha=0.5, label='Background', edgecolor='white')
ax2.hist(df[df['type']=='signal']['mass'], bins=50, range=(105, 150),
         alpha=0.7, label='Signal', edgecolor='white')
ax2.set_xlabel('m$_{γγ}$ (GeV)', fontsize=11)
ax2.set_ylabel('Events', fontsize=11)
ax2.set_title('Signal vs Background', fontsize=12)
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Data Filtering and Selection

```py {monaco-run}
import pandas as pd
import numpy as np

# Recreate dataset
np.random.seed(42)
df = pd.DataFrame({
    'mass': np.concatenate([
        np.random.normal(125, 1.5, 300),
        np.random.exponential(30, 2000) + 105
    ]),
    'photon1_E': np.random.uniform(40, 110, 2300),
    'photon2_E': np.random.uniform(35, 100, 2300),
    'detector_qual': np.random.choice(['good', 'bad'], 2300, p=[0.9, 0.1])
})
df = df[df['mass'] < 150]

# Apply quality cuts
print(f"Events before cuts: {len(df)}")

# Cut 1: Detector quality
df_qual = df[df['detector_qual'] == 'good']
print(f"After quality cut: {len(df_qual)}")

# Cut 2: Photon energy requirements
df_cut = df_qual[(df_qual['photon1_E'] > 50) & (df_qual['photon2_E'] > 45)]
print(f"After energy cuts: {len(df_cut)}")

# Cut 3: Signal region (mass window around Higgs)
signal_region = df_cut[(df_cut['mass'] > 122) & (df_cut['mass'] < 128)]
print(f"Events in signal region (122-128 GeV): {len(signal_region)}")

# Sideband regions (for background estimation)
sideband_low = df_cut[(df_cut['mass'] > 110) & (df_cut['mass'] < 120)]
sideband_high = df_cut[(df_cut['mass'] > 130) & (df_cut['mass'] < 140)]
print(f"Sideband events: {len(sideband_low) + len(sideband_high)}")

print(f"\nSignal region statistics:")
print(signal_region['mass'].describe())
```

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

<div class="card card-warning pad-tight">

## ⚠️ **Missing Values**
- Empty cells, NaN, None
- Measurement failures
- Detector dead time

**Solutions**: Drop, fill (mean/median/interpolate), or flag

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Outliers**
- Measurement errors
- Rare events (physics or noise?)
- Data entry mistakes

**Solutions**: Statistical tests, domain knowledge, robust statistics

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Duplicates**
- Repeated measurements
- Data processing errors
- Accidental double-counting

**Solutions**: Identify and remove based on unique identifiers

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Inconsistent Formats**
- Mixed units (GeV vs MeV)
- Date/time formats
- Categorical encoding

**Solutions**: Standardize, convert, validate

</div>

</div>

---
hideInToc: true
---

# Detecting and Handling Outliers

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data with outliers
np.random.seed(42)
normal_data = np.random.normal(100, 10, 95)
outliers = np.array([200, 210, -50, 250, 180])  # Artificial outliers
data = np.concatenate([normal_data, outliers])

df = pd.DataFrame({'measurement': data})

# Method 1: Z-score (standard deviations from mean)
mean, std = df['measurement'].mean(), df['measurement'].std()
df['z_score'] = np.abs((df['measurement'] - mean) / std)
outliers_z = df[df['z_score'] > 3]

print(f"Mean: {mean:.2f}, Std: {std:.2f}")
print(f"Outliers (|z| > 3): {len(outliers_z)}")
print(outliers_z)

# Method 2: IQR (Interquartile Range)
Q1 = df['measurement'].quantile(0.25)
Q3 = df['measurement'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_iqr = df[(df['measurement'] < lower_bound) | (df['measurement'] > upper_bound)]
print(f"\nIQR method: {len(outliers_iqr)} outliers")
print(f"Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")

# Visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(range(len(df)), df['measurement'], alpha=0.6, label='Data')
ax.scatter(outliers_z.index, outliers_z['measurement'], color='red', s=100,
           marker='x', label='Outliers (Z-score)', zorder=5)
ax.axhline(mean, color='green', linestyle='--', label='Mean', linewidth=1.5)
ax.axhline(mean + 3*std, color='orange', linestyle=':', label='±3σ', linewidth=1)
ax.axhline(mean - 3*std, color='orange', linestyle=':', linewidth=1)
ax.set_xlabel('Index')
ax.set_ylabel('Measurement')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Data Normalization and Scaling

<div class="card card-info pad-tight mt-md">

## **Why Normalize?**

- Different features have different scales (energy in GeV, angles in radians)
- Many ML algorithms perform better with normalized data
- Makes features comparable

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

# Create dataset with different scales
np.random.seed(42)
df = pd.DataFrame({
    'energy': np.random.uniform(50, 150, 100),      # GeV
    'momentum': np.random.uniform(1, 5, 100),       # GeV/c
    'angle': np.random.uniform(0, np.pi, 100)       # radians
})

print("Original data:")
print(df.describe())

# Method 1: Standardization (z-score normalization)
# (x - mean) / std  →  mean=0, std=1
df_standardized = (df - df.mean()) / df.std()
print("\nStandardized (z-score):")
print(df_standardized.describe())

# Method 2: Min-Max scaling
# (x - min) / (max - min)  →  range [0, 1]
df_minmax = (df - df.min()) / (df.max() - df.min())
print("\nMin-Max scaled [0, 1]:")
print(df_minmax.describe())

# Verify: all columns now comparable
print("\nComparison of scales:")
print(f"Original std: {df.std().values}")
print(f"Standardized std: {df_standardized.std().values}")
print(f"Min-Max range: [{df_minmax.min().values}, {df_minmax.max().values}]")
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

<div class="card card-primary pad-tight mt-md">

## **Pandas Supports Many Formats**

Reading and writing data is easy and consistent across formats

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info pad-tight">

### **Reading Data**

```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# SQL
df = pd.read_sql(query, connection)

# HDF5 (large datasets)
df = pd.read_hdf('data.h5', 'key')
```

</div>

<div class="card card-secondary pad-tight">

### **Writing Data**

```python
# CSV
df.to_csv('output.csv', index=False)

# Excel
df.to_excel('output.xlsx')

# JSON
df.to_json('output.json')

# SQL
df.to_sql('table', connection)

# HDF5
df.to_hdf('output.h5', 'key')
```

</div>

</div>

<div class="card card-accent pad-tight mt-md">

**Best practice**: Use CSV for human-readable data, HDF5 or Parquet for large datasets (faster, smaller)

</div>

---
hideInToc: true
---

# CSV Read/Write Example

```python
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

<div class="card card-warning pad-tight mt-sm">

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

# Data Analysis Workflow Best Practices

<div class="grid-2 mt-md gap-md">

<div class="card card-success pad-tight">

## ✅ **Do**

1. **Always visualize first** (distributions, correlations)
2. **Check for missing values** before analysis
3. **Document data sources** and preprocessing
4. **Validate data quality** (ranges, units, consistency)
5. **Keep raw data separate** from processed
6. **Use version control** for analysis scripts
7. **Save intermediate results** for reproducibility
8. **Write tests** for data processing functions

</div>

<div class="card card-warning pad-tight">

## ❌ **Don't**

1. **Don't assume data is clean** without checking
2. **Don't delete outliers** without understanding why
3. **Don't mix data loading and analysis** (separate!)
4. **Don't hardcode file paths** (use config files)
5. **Don't work with copies unnecessarily** (memory!)
6. **Don't forget to document units** and conventions
7. **Don't skip exploratory analysis**
8. **Don't trust a single metric**

</div>

</div>

---
hideInToc: true
---

# Performance Tips

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### **NumPy**

✅ Use vectorized operations (no loops!)

✅ Pre-allocate arrays if possible

✅ Use appropriate data types (int32 vs int64)

✅ Avoid unnecessary copies

</div>

<div class="card card-secondary pad-tight">

### **Pandas**

✅ Use `iterrows()` sparingly (slow!)

✅ Prefer vectorized operations or `apply()`

✅ Set index on frequently-filtered columns

✅ Use categorical dtype for repeated strings

</div>

<div class="card card-info pad-tight">

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

<div class="card card-accent pad-tight mt-md">

## **Explore Real Particle Physics Data**

CERN provides open access to real experimental data from LHC experiments!

**URL**: [http://opendata.cern.ch](http://opendata.cern.ch)

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

### **Available Datasets**

- **CMS**: Proton-proton collisions (7, 8, 13 TeV)
- **ATLAS**: Limited open data releases
- **ALICE**: Heavy-ion collisions
- **LHCb**: B-physics data

Formats: CSV, ROOT, HDF5

</div>

<div class="card card-secondary pad-tight">

### **Example Analyses**

- Higgs → ZZ → 4 leptons
- W/Z boson production
- Top quark pair production
- Dimuon mass spectrum
- Jet physics

Full tutorials and documentation provided!

</div>

</div>

<div class="card card-info pad-tight mt-md">

**Your next step**: Download a real dataset and apply NumPy/Pandas skills! Example: Dimuon spectrum showing J/ψ, Υ resonances

</div>

---
hideInToc: true
---

# Example: CMS Dimuon Spectrum

```python
import pandas as pd
import matplotlib.pyplot as plt

# Real CMS open data (simplified)
# URL: http://opendata.cern.ch/record/5200
# df = pd.read_csv('CMS_DoubleMu_Run2011A.csv')

# For demonstration: simulate similar data
import numpy as np
np.random.seed(42)

# J/psi peak (~3.1 GeV), Upsilon peaks (~9-10 GeV), continuum background
jpsi = np.random.normal(3.1, 0.1, 500)
upsilon = np.random.normal(9.5, 0.2, 200)
background = np.random.exponential(2.0, 2000)

mass = np.concatenate([jpsi, upsilon, background])
df = pd.DataFrame({'dimuon_mass': mass[mass < 15]})

# Analysis
print(f"Total events: {len(df)}")
print(f"Events in J/psi region (2.8-3.4 GeV): {len(df[(df['dimuon_mass'] > 2.8) & (df['dimuon_mass'] < 3.4)])}")
print(f"Events in Upsilon region (9-10.5 GeV): {len(df[(df['dimuon_mass'] > 9) & (df['dimuon_mass'] < 10.5)])}")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(df['dimuon_mass'], bins=100, range=(0, 15), edgecolor='white', linewidth=0.3)
plt.xlabel('Dimuon Mass (GeV/c²)', fontsize=12)
plt.ylabel('Events', fontsize=12)
plt.title('Dimuon Mass Spectrum (simulated CMS data)', fontsize=14)
plt.axvline(3.1, color='red', linestyle='--', label='J/ψ (3.1 GeV)', linewidth=1.5)
plt.axvline(9.5, color='green', linestyle='--', label='Υ (9.5 GeV)', linewidth=1.5)
plt.legend()
plt.grid(alpha=0.3)
plt.yscale('log')
plt.tight_layout()
plt.show()
```

---
layout: section
hideInToc: true
---

# Summary

---
hideInToc: true
---

# What We Learned Today

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **NumPy**

✅ ndarray: efficient multi-dimensional arrays

✅ Vectorization: fast element-wise operations

✅ Broadcasting: operations on different shapes

✅ Indexing, slicing, boolean masks

✅ 10-100× faster than Python lists

</div>

<div class="card card-secondary pad-tight">

## **Pandas**

✅ DataFrame: labeled 2D data structure

✅ Reading/writing files (CSV, Excel, JSON, etc.)

✅ Missing data handling

✅ Filtering, grouping, aggregating

✅ Data cleaning and preprocessing

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-info pad-tight">

### **Skills Acquired**

- Load real datasets
- Clean messy data
- Exploratory analysis
- Statistical summaries
- Visualization

</div>

<div class="card card-success pad-tight">

### **Best Practices**

- Visualize first
- Document everything
- Validate data quality
- Save intermediate results
- Keep raw data separate

</div>

<div class="card card-accent pad-tight">

### **Next Steps**

- Apply to real CERN data
- Combine with L10 fitting
- Build analysis pipelines
- **L12: Automation!**

</div>

</div>

---
hideInToc: true
layout: quote
---

# You now have the tools to work with real, messy data. In L12, we'll learn to automate your entire workflow—from data loading to final plots—with reproducible scripts and version control.

---
hideInToc: true
layout: end
---

# Questions?

## Next lecture: **Reproducible Workflows & Automation**
