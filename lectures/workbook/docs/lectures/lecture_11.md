# L11: NumPy, Pandas & Real Data

---

## Overview

**Duration**: 90-120 minutes

**Prerequisites**: L5 (Python basics), L10 (Data fitting)

**Learning Objectives**:
- Master NumPy arrays and vectorized operations
- Use Pandas DataFrames for tabular data
- Load, clean, and preprocess real datasets
- Handle missing data and outliers
- Perform group-by and aggregation operations
- Transition from toy examples to real-world data

---

## Lecture Structure

### Part 1: NumPy Foundations (30 min)
- Why NumPy? (Speed, memory, convenience)
- Creating arrays (from lists, zeros, ones, arange, linspace)
- **Speed comparison demo**: Lists vs NumPy (10-100x faster!)
- Vectorization: element-wise operations without loops
- Array indexing, slicing, boolean masking
- Broadcasting rules

### Part 2: Pandas DataFrames (30 min)
- What is a DataFrame? (Excel table, SQL table analog)
- Creating DataFrames from dictionaries
- Reading CSV files (`pd.read_csv`)
- Basic operations: head, describe, info
- Selecting columns and rows (iloc, loc)
- Filtering with boolean indexing
- Adding new columns

### Part 3: Data Cleaning (20 min)
- Handling missing values (NaN)
  - Detect: `df.isnull().sum()`
  - Drop: `df.dropna()`
  - Fill: `df.fillna(value)`, `df.fillna(df.mean())`
- Detecting outliers (z-score, IQR method)
- Data normalization and scaling
  - Standardization: (x - mean) / std
  - Min-max scaling: (x - min) / (max - min)

### Part 4: Group-By Operations (15 min)
- Split-Apply-Combine paradigm
- `df.groupby('column').agg(...)`
- Multiple aggregations
- Practical example: detector-wise statistics

### Part 5: Real Example - CERN Data (15 min)
- Simulated dimuon spectrum (realistic)
- Load, explore, filter, visualize
- Connect to real CERN Open Data Portal

---

## Teaching Tips

### Common Student Struggles

1. **"NumPy arrays vs Python lists - when to use which?"**
   - NumPy: numerical operations, large datasets, performance-critical
   - Lists: mixed types, small data, general Python code
   - Rule: Use NumPy for anything numerical!

2. **"Why is my Pandas operation slow?"**
   - Avoid `iterrows()` - use vectorized operations
   - Use `apply()` for row-wise operations
   - Don't repeatedly append to DataFrame (pre-allocate or use list)

3. **"How do I handle missing data?"**
   - **Understand why it's missing first!**
   - Physics reason? (detector dead time → exclude)
   - Random? (fill with mean, median, interpolate)
   - Show students the impact of different strategies

4. **"My DataFrame doesn't fit in memory!"**
   - Read in chunks: `pd.read_csv(..., chunksize=10000)`
   - Use appropriate dtypes (int32 vs int64)
   - Consider Dask or Polars for very large data

### Interactive Elements

- **Speed race**: Time list comprehension vs NumPy operation live
- **Data detective**: Give students messy dataset, ask them to identify issues
- **Group challenge**: "Find the detector with highest mean energy" using groupby
- **Plot competition**: Who can create the most informative exploratory plot?

### Hands-On Exercises

**Exercise 1** (Warm-up): NumPy basics
```python
# Create array of 100 random numbers
# Calculate mean, std, max, min
# Find all values > mean + std
```

**Exercise 2** (Core): Pandas DataFrame manipulation
```python
# Load CSV file
# Remove rows with missing energy values
# Filter events with energy > 50 GeV
# Group by detector, calculate mean energy
# Create histogram of energy distribution
```

**Exercise 3** (Advanced): Real data analysis
- Download actual CMS or ATLAS open data
- Clean and explore dataset
- Identify interesting features (resonance peaks, etc.)
- Prepare data for fitting (connect to L10!)

---

## Common Questions & Answers

**Q**: Should I use NumPy or Pandas?
**A**: Both! NumPy for arrays and numerical operations, Pandas for labeled tabular data. Pandas is built on NumPy.

**Q**: How do I read Excel files?
**A**: `pd.read_excel('file.xlsx')` - may need `pip install openpyxl`

**Q**: What's the difference between loc and iloc?
**A**: `iloc` uses integer position (0, 1, 2...), `loc` uses labels (column names, row indices)

**Q**: Why are my NumPy operations giving weird results?
**A**: Check data types! Integer division, overflow, broadcasting issues

**Q**: Should I drop or fill missing values?
**A**: Depends on domain! Physics analysis: often drop (can't invent measurements). ML: often fill (but document it!)

---

## Key Code Snippets

### NumPy essentials
```python
import numpy as np

# Create and operate on arrays
arr = np.array([1, 2, 3, 4, 5])
result = arr ** 2 + 2 * arr  # Vectorized!

# Boolean masking
high_values = arr[arr > 3]

# Speed comparison
%timeit [x**2 for x in range(10000)]
%timeit np.arange(10000)**2
```

### Pandas essentials
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Explore
print(df.head())
print(df.describe())

# Filter
signal = df[df['is_signal'] == True]
high_energy = df[df['energy'] > 50]

# Group and aggregate
stats = df.groupby('detector')['energy'].agg(['mean', 'std', 'count'])
```

### Handling missing data
```python
# Check for missing
print(df.isnull().sum())

# Drop rows with any NaN
df_clean = df.dropna()

# Fill with mean
df['energy'].fillna(df['energy'].mean(), inplace=True)
```

---

## Demonstrations

### Demo 1: Speed Comparison (5 min)
Show dramatic speed difference between lists and NumPy:
```python
import time
import numpy as np

n = 1_000_000
lst = list(range(n))
arr = np.arange(n)

# List (slow)
start = time.time()
result_list = [x**2 + 2*x + 1 for x in lst]
print(f"List: {time.time() - start:.3f}s")

# NumPy (fast)
start = time.time()
result_array = arr**2 + 2*arr + 1
print(f"NumPy: {time.time() - start:.3f}s")
```

### Demo 2: Real Data Exploration (10 min)
Walk through complete EDA workflow:
1. Load CSV
2. Check for missing values
3. Summary statistics
4. Visualize distributions
5. Identify outliers
6. Filter and clean
7. Save processed data

---

## Time Estimates

- NumPy (lecture + demos): 30 min
- Pandas (lecture + demos): 30 min
- Data cleaning: 20 min
- Group-by: 15 min
- Real example: 15 min
- Student exercises: 30 min
- **Total**: 140 min (adjust as needed)

---

## Resources for Students

- [NumPy documentation](https://numpy.org/doc/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas (free online)
- [CERN Open Data Portal](http://opendata.cern.ch)

---

## Assessment Ideas

- **Practical quiz**: "Load this CSV, find mean energy per detector, plot results"
- **Data cleaning challenge**: Give messy dataset, students must clean and document steps
- **Speed optimization**: "Rewrite this slow code using NumPy vectorization"
- **Project milestone**: Students must load and clean real dataset for final project

---

## Extension Activities

For advanced students:
- Introduce Dask for out-of-memory datasets
- Show Polars as faster Pandas alternative
- Demonstrate Jupyter notebooks for interactive EDA
- Connect to databases with `pd.read_sql()`
