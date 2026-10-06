---
layout: cover
title: "Pandas & Data Cleaning"
# slidev-addon-python-runner reads this block from slide 1 = this cover (see CLAUDE.md)
python:
  installs: ["numpy", "pandas"]
  prelude: |
    import numpy as np
    import pandas as pd
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Pandas & Data Cleaning

##### <span class="aims-badge">📁 data & files · ⚙️ automation · ♻️ reproducibility</span>

<!--
Speaker: Lectures 9 to 11 computed with tables that were already in order.
Today is about how a table gets into that state. The pendulum table comes back
with the script handed out in Lecture 4, and a second file from the lab
partner. Then the method is used on the file with 91 583 rows. Two things are
new: the library Pandas, and cleaning as a list of rules with a count for
each. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Like families, tidy datasets are all alike but every messy dataset is messy in **its own way**.
Hadley Wickham — *Tidy Data*, Journal of Statistical Software, 2014

---
hideInToc: true
---

# The Partner's **Second File**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`data/raw/pendulum_run2.csv`**

```text
nr;length_cm;t10_s
1;20;8,97
2;30;11,02
3;40;12,74
4;50;14,15
5;60;15,58
6;70;16,83
7;80;
8;90;19,08
9;100;20,04
;Mean;14,80
```

</div>

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

## 🔁 **The form of the first file**

`;` between values, decimal commas, a column `nr`, a summary in the last line. On the first file, Lecture 4's `scripts/clean_pendulum.py` made the four edits of Lecture 2: 9 rows, 97 bytes, SHA-256 `be05af03…fff0870b` on every laptop.

</div>

<div class="card card-info card-glass pad-compact">

## ❓ **The same line on this file**

The partner timed the same nine lengths, 20 to 100 cm. How many rows should the script write?

</div>

</div>

</div>

<!--
Speaker: the lab partner's second series, 125 bytes, made by
pendulum_run2.py in the workbook's data folder. Let the room read the file
for half a minute before asking. The answer they should reach: nine lengths,
and only eight of them have a time. (~2 min)
-->

---
hideInToc: true
---

# What Lecture 4's Script **Wrote**

<div class="card card-info card-glass pad-compact mt-sm">

```text
% python3 scripts/clean_pendulum.py data/raw/pendulum_run2.csv data/processed/run2_script.csv
10 rows written to data/processed/run2_script.csv
PS> python scripts/clean_pendulum.py data/raw/pendulum_run2.csv data/processed/run2_script.csv
10 rows written to data/processed/run2_script.csv
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 📤 **`run2_script.csv`, the end**

```text
70,16.83
80,
90,19.08
100,20.04
Mean,14.80
```

Ten rows for nine lengths. One holds no time, and one is not a measurement.

</div>

<div class="card card-primary card-glass pad-compact">

## 📜 **`clean_pendulum.py`, lines 27–31**

```python
for line in lines:
    if "mean" in line:
        continue
    line = line.replace(",", ".").replace(";", ",")
    out.append(line.split(",", 1)[1])
```

In Lecture 3's ASCII table `A` is 65 and `a` is 97; `M` is 77 and `m` is 109. `"mean" in ";Mean;14,80"` is `False`.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

No error and no warning. The script did what its text says: it moves characters. Nothing in it knows that `t10_s` holds numbers, or that a measurement has a row number.

</div>

<!--
Speaker: the line is the one from Lecture 4 and Seminar 4; only the file
names differ. Python is python3 on macOS and python on Windows. The output is
103 bytes on both systems. Ask: which line of clean() would have to change,
and how would it know? The empty time went through as an empty piece of text.
(~3 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📜 Write a cleaning as a **script**: raw file in, cleaned file out, the same bytes on every run

</div>

<div class="card card-secondary card-glass pad-compact">

🐼 Read a text table into a **DataFrame** and say what the type of each column tells about the file

</div>

<div class="card card-accent card-glass pad-compact">

🎯 Select rows and columns by **name, position and mask**, and compute a new column from others

</div>

<div class="card card-warning card-glass pad-compact">

🕳️ Turn a code for a missing value into **NaN**, and say what NaN does to a mean and to a comparison

</div>

<div class="card card-success card-glass pad-compact">

✅ Run **five checks** on any table: completeness, validity, uniqueness, consistency, units

</div>

<div class="card card-info card-glass pad-compact">

🔀 Reshape, **group** and **join** tables, and write the result to `data/processed/`

</div>

</div>

<!--
Speaker: the first objective is the one that matters most. The other five are
the tools it needs. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Cleaning by **Script**

Lecture 4's script edits characters. A cleaning that knows what a column holds starts by reading the file as a table, first on the file whose right answer is known: 97 bytes.

<!--
Speaker: the first file again, cleaned a second time, now by Pandas. Lecture
4's script and the hand-cleaned copy already agree; the new script has to give
the same bytes before it is trusted with the second file. (~1 min)
-->

---
hideInToc: true
---

# NumPy Does Not Read **This File**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🧪 **The attempt**

```python
import numpy as np

np.loadtxt("data/raw/pendulum.csv",
           delimiter=";", skiprows=1)
```

```text
ValueError: could not convert string
'9,02' to float64 at row 0, column 3.
```

</div>

<div class="card card-primary card-glass pad-compact">

## 🔢 **An array, and this file**

- An array holds one type. This file holds numbers, the word `mean` and an empty cell
- `loadtxt` knows one decimal sign, the point
- An array has positions, `data[:, 2]`. The column names stay behind in line 1 of the file

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🐼 **Pandas** is a library for tables: columns with names, one type per column, cells that may be empty, and readers for files as they arrive. Every numeric column is a NumPy array inside. Install it once with `python -m pip install pandas` (macOS `python3 -m pip install pandas`). The usual import is `import pandas as pd`.

</div>

<!--
Speaker: NumPy is the right tool once the table is clean and numeric. Getting
it there is what Pandas is for. (~2 min)
-->

---
hideInToc: true
---

# Read the File: **Three Attempts**

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 1️⃣ **No options**

```python
df = pd.read_csv(path)
print(df.shape)
```

```text
(10, 1)
```

One column. Pandas expects a comma between values, and here the commas are decimal commas.

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **The separator**

```python
df = pd.read_csv(path, sep=";")
print(df.dtypes)
```

```text
nr           float64
length_cm     object
t10_s         object
dtype: object
```

Three columns. `object` means text: `9,02` is not a number.

</div>

<div class="card card-success card-glass pad-compact">

## 3️⃣ **The decimal sign**

```python
df = pd.read_csv(path, sep=";",
                 decimal=",")
print(df.dtypes)
```

```text
nr           float64
length_cm     object
t10_s        float64
dtype: object
```

`t10_s` is a column of numbers.

</div>

</div>

<div class="note-text mt-sm">

`path` is `"data/raw/pendulum.csv"`. `read_csv` returns the table, here named `df`. The last line of the output is the type of the list of types itself. Pandas 3 prints `str` where earlier versions print `object`.

</div>

<!--
Speaker: these are the two facts the spreadsheet took from the regional
settings of the computer: the separator and the decimal sign. Here they stand
in the code, so the file is read the same way on every laptop. (~3 min)
-->

---
hideInToc: true
---

# What Came Back: a **DataFrame**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖨️ **`print(df)`**

```text
    nr length_cm  t10_s
0  1.0        20   9.02
1  2.0        30  11.05
2  3.0        40  12.61
3  4.0        50  14.23
4  5.0        60  15.49
5  6.0        70  16.84
6  7.0        80  17.90
7  8.0        90  19.10
8  9.0       100  20.01
9  NaN      mean  15.14
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Read it column by column**

- The numbers 0 to 9 on the left are not from the file. They are the **index**: a label for each row
- `nr` is `float64`, 1.0 and 2.0. One cell is empty. Pandas writes it as **NaN**, and NaN exists only as a float
- `length_cm` is text. One cell says `mean`, and a column has one type
- `t10_s` is `float64`: every cell is a number, the mean included

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Two columns have a type they should not have, and both point at row 9. The types are the first check of a table: a column of numbers that is not numeric holds a cell that is not a number.

</div>

<!--
Speaker: let the room find row 9 from the two wrong types before pointing at
it. Nothing has been cleaned yet. The file has only been read. (~2 min)
-->

---
hideInToc: true
---

# Drop the Row That Is **Not a Measurement**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **A mask**

```python
keep = df["nr"].notna()
print(keep.sum(), "of", len(keep))
df = df[keep]
```

```text
9 of 10
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📖 **Line by line**

- `df["nr"]` is one column
- `.notna()` gives True where the cell holds a value, as a mask of a NumPy array does
- `df[keep]` is the table of the rows where the mask is True

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

The line states a rule: a measurement has a row number, and the line with the mean has none. The partner's `;Mean;14,80` has none either. The rule does not depend on how the word is spelt.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ `df = df.iloc[:-1]` also removes the last row. It states a position and no reason. On a file without a mean line it deletes a measurement, and no error is raised.

</div>

<!--
Speaker: the difference between the two lines is the point of the slide. A
rule keeps working on the next file. A position does not. (~2 min)
-->

---
hideInToc: true
---

# Drop the Column, Fix the **Type**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧹 **Three lines**

```python
print(df["length_cm"].sum())
df = df.drop(columns="nr")
df["length_cm"] = df["length_cm"].astype(int)
print(df["length_cm"].sum())
print(df.dtypes)
```

```text
2030405060708090100
540
length_cm      int64
t10_s        float64
dtype: object
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔤 **Text that looks like numbers**

- Before the conversion the column holds the texts `"20"`, `"30"`, … Their sum joins them: `"20" + "30"` is `"2030"`
- `.astype(int)` converts every cell. With the word `mean` still in the column it stops: `invalid literal for int() with base 10: 'mean'`
- `drop(columns="nr")` returns the table without that column. A row number is bookkeeping, not a measurement

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Printed, the text `20` and the number `20` look the same. `df.dtypes` tells them apart.

</div>

<!--
Speaker: the sum 2030405060708090100 is worth a pause. Nothing failed and no
warning was printed. A sum of text is a longer text. (~2 min)
-->

---
hideInToc: true
---

# Write the **File**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 1️⃣ **`df.to_csv(out)`**

```text
,length_cm,t10_s
0,20,9.02
1,30,11.05
…
```

The index is written as a first column without a name. The row numbers are back.

</div>

<div class="card card-success card-glass pad-compact">

## 2️⃣ **`df.to_csv(out, index=False)`**

```text
length_cm,t10_s
20,9.02
30,11.05
…
```

Only the columns of the table. This is the form of Lecture 4's `pendulum_script.csv`.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📁 `out` is `"data/processed/pendulum.csv"`. A script reads from `data/raw/` and writes to `data/processed/`. It never writes into `data/raw/`. Everything in `data/processed/` can be deleted and made again by running the script.

</div>

<div class="note-text mt-sm">

`data/processed/pendulum_script.csv`, written by Lecture 4's script, stays as it is: it is the file to compare with.

</div>

<!--
Speaker: index=False is forgotten once by everybody. The sign is a first
column named "Unnamed: 0" when the file is read again. (~2 min)
-->

---
hideInToc: true
---

# The Same File? **Compare**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **As tables**

```python
script4 = "data/processed/pendulum_script.csv"
before = pd.read_csv(script4)
now = pd.read_csv(out)
print(before.equals(now))
```

```text
True
```

The same columns, the same types, the same values.

</div>

<div class="card card-warning card-glass pad-compact">

## 🧱 **As bytes**

```text
Lecture 4   97 bytes
Pandas      95 bytes

Lecture 4   80,17.90    90,19.10
Pandas      80,17.9     90,19.1
```

Two lines differ, by one character each. On Windows the Pandas file has 105 bytes: ten more.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

17.90 and 17.9 are the same float64, and Pandas writes the shortest text that gives the number back. In the file the zero carried a meaning: the time was read to 0.01 s. Whether two files are *the same* has two answers, and a comparison says which one it gives.

</div>

<!--
Speaker: Lecture 4's script copies the characters of the raw file; Pandas
reads numbers and writes them again. Ask which of the two answers a reader of
a paper needs. For the numbers, the table. For "is this the file that was
published", the bytes. (~2 min)
-->

---
hideInToc: true
---

# Identical, and **How to Know**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Say how a number is written**

```python
df.to_csv(out, index=False,
          float_format="%.2f",
          lineterminator="\n")
```

- `"%.2f"`: two decimals in every row, `17.90`
- `"\n"`: one byte at the end of each line on every system. Without it Windows writes two, CR and LF

</div>

<div class="card card-success card-glass pad-compact">

## 🔐 **Compare the checksums**

```text
% shasum -a 256 pendulum*.csv
be05af03…fff0870b  pendulum.csv
be05af03…fff0870b  pendulum_script.csv
PS> (Get-FileHash pendulum*.csv).Hash
BE05AF03…FFF0870B
BE05AF03…FFF0870B
```

Both files have 97 bytes and one SHA-256. They are identical.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The lines of Lecture 4, run after `cd data/processed`, which is the same in both shells. In Python, on every system: `Path(out).read_bytes() == Path(script4).read_bytes()` gives `True`.

</div>

<!--
Speaker: Lecture 4's script matched the copy cleaned by hand; the Pandas
script now matches Lecture 4's. shasum writes the digits in lower case,
Get-FileHash in upper case: one number. Without lineterminator, Pandas ends
each line with the line ending of the system, CR LF on Windows: 105 bytes.
(~2 min)
-->

---
hideInToc: true
---

# The **Script**

```python
"""Clean the pendulum table: data/raw -> data/processed."""
import pandas as pd

RAW = "data/raw/pendulum.csv"
OUT = "data/processed/pendulum.csv"

df = pd.read_csv(RAW, sep=";", decimal=",")     # ; between values, decimal comma
df = df[df["nr"].notna()]                       # the mean line has no row number
df = df.drop(columns="nr")                      # bookkeeping, not a measurement
df["length_cm"] = df["length_cm"].astype(int)
df.to_csv(OUT, index=False, float_format="%.2f", lineterminator="\n")
print(f"{len(df)} rows written to {OUT}")
```

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ▶️ **Run it**

```text
% python3 scripts/clean.py
9 rows written to data/processed/pendulum.csv
PS> python scripts/clean.py
9 rows written to data/processed/pendulum.csv
```

</div>

<div class="card card-success card-glass pad-compact">

## ♻️ **Run it again**

`scripts/clean.py` is a new file next to Lecture 4's `clean_pendulum.py`. Delete `data/processed/pendulum.csv` and run it: the file is back, with the same 97 bytes.

</div>

</div>

<!--
Speaker: run it live from the terminal of VS Code, delete the output in the
Side Bar, run it again. Each of the four edits of Lecture 2 is one line here:
the two replacements are the two options of read_csv. The line that runs it
is the same in both shells after the first word. (~3 min)
-->

---
hideInToc: true
---

# The Second File, **by Rule**

<div class="card card-info card-glass pad-compact mt-sm">

```text
% python3 scripts/clean.py
9 rows written to data/processed/pendulum_run2.csv
PS> python scripts/clean.py
9 rows written to data/processed/pendulum_run2.csv
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **`raw.isna().sum()`, before cleaning**

```text
nr           1
length_cm    0
t10_s        1
```

`length_cm` is `object` again: one cell says `Mean`.

</div>

<div class="card card-success card-glass pad-compact">

## 📤 **`pendulum_run2.csv`, the end**

```text
70,16.83
80,
90,19.08
100,20.04
```

Nine rows. The summary line is gone.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

The line with `Mean` has no `nr`, so the rule drops it, whatever the spelling. The missing time is NaN and is written as an empty cell: the file still says that 80 cm was not timed.

</div>

<!--
Speaker: RAW and OUT in scripts/clean.py now name pendulum_run2.csv; nothing
else changed. raw is the table as read_csv returns it, before the mask. The
types and the count of empty cells point at both rows before anything is
cleaned: that answers the question the lecture opened with. (~3 min)
-->

---
hideInToc: true
---

# Two Scripts, **Two Files**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| | **Lecture 4: `clean_pendulum.py`** | **Today: `clean.py`** |
| --- | --- | --- |
| What it reads | lines of text | columns with names and types |
| The summary line | skipped if it contains `mean` | dropped: it has no `nr` |
| The first file | 9 rows, 97 bytes, `be05af03…` | 9 rows, 97 bytes, `be05af03…` |
| The second file | 10 rows, `Mean,14.80` kept | 9 rows, one gap at 80 cm |
| A missing time | an empty piece of text | NaN, counted by `isna()` |
| The file names | two words on the command line | `RAW` and `OUT`, typed in the script |

</div>

<div class="card card-success card-glass pad-compact mt-md">

⚙️ Both are scripts: they can be read, run again and kept under Git. The difference is what a rule refers to: the characters of a line, or the meaning of a column.

</div>

<!--
Speaker: the editor remains the right tool for looking at a file. Lecture 4's
script is still right for the first file: same bytes. Ask which row of the
table matters for the next file the partner sends. (~2 min)
-->

---
hideInToc: true
---

# The Cleaning in the **Browser**

```py {monaco-run} {autorun:false}
import io
import pandas as pd
raw = """nr;length_cm;t10_s
1;20;9,02
2;30;11,05
3;40;12,61
;mean;10,89
"""
df = pd.read_csv(io.StringIO(raw), sep=";", decimal=",")
df = df[df["nr"].notna()].drop(columns="nr")
df["length_cm"] = df["length_cm"].astype(int)
print(df.to_csv(index=False, float_format="%.2f"))
```

<div class="note-text mt-sm">

The browser has no project folder, so the first three rows of the file stand in the code, with their own mean line. Take out `decimal=","` and run it again: the times are written as text in quotes, `"9,02"`.

</div>

<!--
Speaker: io.StringIO lets read_csv read a text as if it were a file. With
decimal="," removed nothing fails: t10_s stays text, float_format does not
apply to text, and to_csv puts each value in quotes because it holds a comma.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **DataFrame**

The script read, filtered and wrote a DataFrame without saying what one is: columns with names, one type each, and a label on every row.

<!--
Speaker: the script used a DataFrame without saying what it is. This section
takes it apart on the cleaned pendulum table: columns, rows, masks, new
columns. Every fence runs in the browser. (~1 min)
-->

---
hideInToc: true
---

# A Table with **Names and Types**

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 1.15fr 1fr;">

<div>

<img class="fig" src="/figures/viz_cleaning_dataframe.svg" style="display:block;margin:0 auto;width:100%;">

</div>

<div class="card card-primary card-glass pad-compact">

## 🐼 **The parts**

- A **DataFrame** is a set of columns of equal length that share one set of row labels
- One column is a **Series**: a NumPy array, a name and the row labels
- Each column has its own type. The types are those of NumPy: `int64`, `float64`, `bool`. Text is `object`, or `str` from Pandas 3 on
- The **index** starts as 0, 1, 2, … A row keeps its label when the table is filtered or sorted

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A NumPy array is addressed by position: `data[:, 1]`. A DataFrame is addressed by name: `df["t10_s"]`. The name comes from the file, so the code stays right when the file gets one more column.

</div>

<!--
Speaker: a row is one observation and a column is one variable, as in the
anatomy of a table. The DataFrame adds a type to each column and a label to
each row. (~2 min)
-->

---
hideInToc: true
---

# Build One from a **Dict**

```py {monaco-run} {autorun:false}
import pandas as pd
df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})
print(df.head(3))
print("shape:  ", df.shape)
print("columns:", list(df.columns))
print("dtypes: ", df.dtypes.astype(str).to_dict())
```

<div class="card card-info card-glass pad-compact mt-sm">

A dict with one key per column and a list of values for each: that is a DataFrame written out. `head(3)` is the first three rows. `shape` is rows and columns, as for an array.

</div>

<!--
Speaker: the cleaned pendulum table, typed in. The following fences start
from the same two lines. (~2 min)
-->

---
hideInToc: true
---

# One Column, **Several Columns**

```py {monaco-run} {autorun:false}
import pandas as pd

df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})

t = df["t10_s"]                          # one name: a Series
print(type(t).__name__, t.dtype, len(t))
print(t.sum(), t.mean())                 # 136.25 / 9
print(t.to_numpy())                      # the NumPy array inside
two = df[["length_cm", "t10_s"]]         # a list of names: a DataFrame
print(type(two).__name__, two.shape)
```

<div class="card card-info card-glass pad-compact mt-sm">

One pair of brackets with a name gives a Series. A list of names inside the brackets gives a DataFrame. The mean 15.14 is the number that stood in the last line of the raw file.

</div>

<!--
Speaker: sum, mean, std, min, max and median exist on a Series as on an
array. to_numpy() is the way back to everything the room knows. (~2 min)
-->

---
hideInToc: true
---

# Rows: **Position and Label**

```py {monaco-run} {autorun:false}
import pandas as pd
df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})
print(df.iloc[0].tolist())               # iloc: by position, row 0
print(df.loc[0, "t10_s"])                # loc: by label, row 0, column t10_s
long = df[df["length_cm"] > 70]          # the rows keep their labels
print(long)
print(long.iloc[0].tolist())             # its first row has the label 6
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ After a filter, position and label differ. `long.iloc[0]` is the row of 80 cm. `long.loc[0]` raises `KeyError: 0`: no row has that label any more. `long.reset_index(drop=True)` numbers the rows again from 0.

</div>

<!--
Speaker: the label is what lets a row be found again in the raw table after
any amount of filtering. It is used that way later, to name the bad rows.
(~2 min)
-->

---
hideInToc: true
---

# **Masks**

```py {monaco-run} {autorun:false}
import pandas as pd
df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})

mask = df["t10_s"] > 15                  # a Series of True and False
print(mask.tolist(), mask.sum())
both = (df["length_cm"] >= 40) & (df["t10_s"] < 16)
print(df[both])
print(df[~both].shape)                   # ~ turns the mask round
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ As with NumPy: `&` for and, `|` for or, `~` for not, and each comparison in its own parentheses. Python's `and` stops with `ValueError: The truth value of a Series is ambiguous`.

</div>

<!--
Speaker: replace & by and, run it and read the error with the room. Then take
away one pair of parentheses. (~2 min)
-->

---
hideInToc: true
---

# A New Column from **Other Columns**

```py {monaco-run} {autorun:false}
import numpy as np
import pandas as pd
df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})
df["length_m"] = df["length_cm"] / 100                    # cm to m
df["T_s"] = df["t10_s"] / 10                              # one swing
df["g"] = 4 * np.pi**2 * df["length_m"] / df["T_s"]**2    # from T = 2π √(L/g)
print(df.round(3).head(6))
```

<div class="card card-info card-glass pad-compact mt-sm">

Lecture 7 computed these nine values of g as an array, 9.70 to 9.93. Here they are a column with a name, next to the length and the time they came from. With `length_cm` in the formula the last column reads 970 to 993, a hundred times g: the unit stands in the name.

</div>

<!--
Speaker: head(6) keeps the printout short. An assignment to a new name adds a
column, and the arithmetic runs on whole columns, as with arrays. Put
df["length_cm"] into the formula to show the factor 100. (~2 min)
-->

---
hideInToc: true
---

# Sort and **Summarise**

```py {monaco-run} {autorun:false}
import numpy as np
import pandas as pd
df = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60, 70, 80, 90, 100],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]})
df["g"] = 4 * np.pi**2 * (df["length_cm"] / 100) / (df["t10_s"] / 10)**2
print(df.sort_values("g", ascending=False).head(3).round(3))
g = df["g"]
print(f"std: Pandas {g.std():.3f}, NumPy {g.to_numpy().std():.3f}")
print(f"g = {g.mean():.2f} ± {g.std() / len(g)**0.5:.2f} m/s²")
```

<div class="card card-info card-glass pad-compact mt-sm">

`sort_values` keeps each row's label. Pandas divides by n − 1 in `std`, NumPy by n: 0.085 against 0.080. Here ± 0.03 is 0.085 / √9, the scatter of these nine values. Lecture 9 weighted them with 0.1 cm and 0.1 s assumed: 9.80 ± 0.04. Lecture 10 fitted T² against L: 9.84 ± 0.09. Same rows, three methods, three uncertainties.

</div>

<!--
Speaker: g = 9.80 ± 0.03 m/s² from nine rows and three lines. The n − 1 is
the estimate from a sample. Neither default is wrong, and a report says which
one it used. The three results do not contradict each other: each answers its
own question, and a report names the method next to the number. (~2 min)
-->

---
layout: section
hideInToc: true
---

# A Real **File**

The nine rows of the pendulum table fit on one screen. The LHCb file has 91 583, and every statement about it is the output of a line of code.

<!--
Speaker: the same steps on D0_KPi.csv, 91 583 rows. Nobody can read this file
by eye, so every statement about it is the output of a line of code. The code
and its output on these slides were run on the file itself. (~1 min)
-->

---
hideInToc: true
---

# Read It and **Look**

```python
import numpy as np
import pandas as pd

df = pd.read_csv("data/raw/D0_KPi.csv")
print(df.shape)
print(df.head())
```

```text
(91583, 4)
           M         PT       TAU       IPCHI2
0  1880.6490  3000.9534  0.000413  1299.167500
1  1860.6599  2803.4126  0.000186     0.341822
2  1913.8755  2542.1690  0.000185    17.386473
3  1888.7571  4453.1040  0.000568    56.797930
4  1862.5100  2764.2280  0.000287     3.644997
```

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

One row is one K⁻π⁺ candidate. `M` is its mass in MeV/c², `PT` its transverse momentum in MeV/c, `TAU` its decay time in ns. `IPCHI2` has no unit.

</div>

<div class="card card-secondary card-glass pad-compact">

No option is needed: comma between values, decimal point, names in line 1. The printout is rounded to six decimals. The table holds every digit of the file.

</div>

</div>

<!--
Speaker: IPCHI2 says how well the candidate points back to the collision
point: small means it does. With np.loadtxt the same file became an array of
shape (91583, 4), and line 1 was skipped with skiprows=1. Here line 1 becomes
the names. (~2 min)
-->

---
hideInToc: true
---

# Types and **Memory**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧾 **`df.info()`**

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 91583 entries, 0 to 91582
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   M       91583 non-null  float64
 1   PT      91583 non-null  float64
 2   TAU     91583 non-null  float64
 3   IPCHI2  91583 non-null  float64
dtypes: float64(4)
memory usage: 2.8 MB
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **What it says**

- Four columns of `float64`. No column is text, so every cell was read as a number
- `91583 non-null` four times: no cell is empty
- 91 583 rows × 4 columns × 8 bytes = 2 930 656 bytes. Pandas counts in units of 1024 and prints 2.8 MB
- The same table is 3 926 142 bytes as text on disk

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ By the types this file is clean. The types say that every cell is a number. They do not say that every number is a measurement.

</div>

<!--
Speaker: compare with the pendulum file, where the types found the bad row at
once. Here they find nothing, and the file still has problems. (~2 min)
-->

---
hideInToc: true
---

# `describe()`: Eight Numbers per **Column**

```text
                  M            PT           TAU         IPCHI2
count  91583.000000  91583.000000  91583.000000   91583.000000
mean    1864.104582   3448.928182     -0.052522     457.513042
std       25.565096   1301.067191      2.312500    6378.852807
min     1766.209600    755.268600   -100.000000       0.000014
25%     1845.991900   2723.341800      0.000185       2.124486
50%     1864.078100   3048.925800      0.000272       6.298690
75%     1881.531250   3676.466550      0.000605      27.436283
max     2453.658400  64509.950000      0.578799  891711.060000
```

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

`25%`, `50%`, `75%`: a quarter, a half and three quarters of the rows lie below this value. `50%` is the median.

</div>

<div class="card card-success card-glass pad-compact">

**M**: mean 1864.10, median 1864.08. They agree: the median of Lecture 9, which the row with 2453.66 hardly moves.

</div>

<div class="card card-warning card-glass pad-compact">

**TAU**: median 0.000272, mean −0.0525, minimum −100: the code of Lecture 7, still in the column.

</div>

</div>

<!--
Speaker: print(df.describe()) is the first thing to run on any table. Read it
row by row with the room. Half of the masses lie between 1845.99 and 1881.53.
A mean far from the median means a few values far from the rest; the room
knows the 49 rows of -100 from Lecture 7. (~3 min)
-->

---
hideInToc: true
---

# The Code in a **Histogram**

<img class="fig" src="/figures/viz_cleaning_tau_code.svg" style="display:block;margin:0 auto;max-height:330px;">

<div class="note-text mt-sm">

Left: the column as stored. The code sets the scale of the axis, and all 91 534 measurements fall into two bars. Right: the same column in picoseconds with the code taken out.

</div>

<!--
Speaker: the left panel is what df["TAU"].hist() draws on the raw file. A
histogram with one bar far from all the others is the picture of a code.
(~1 min)
-->

---
hideInToc: true
---

# Lecture 7's Mask, Kept in the **Table**

<div class="note-text mt-sm">

Lecture 7: `TAU.mean()` gave −0.0525 ns with the code and `TAU[mask].mean()` 0.000982 ns without it. The mask went into every calculation, and the 49 rows left the array with their other three values.

</div>

<div class="card card-primary card-glass pad-compact mt-sm">

```python
before = df.mean()
df["TAU"] = df["TAU"].replace(-100, np.nan)
print(pd.DataFrame({"before": before, "after": df.mean()}))
```

```text
             before        after
M       1864.104582  1864.104582
PT      3448.928182  3448.928182
TAU       -0.052522     0.000982
IPCHI2   457.513042   457.513042
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-success card-glass pad-compact">

Only `TAU` changes. The 49 rows stay, with their `M`, `PT` and `IPCHI2`.

</div>

<div class="card card-info card-glass pad-compact">

Every later mean, sum and plot leaves the gap out by itself. No mask is written again.

</div>

</div>

<!--
Speaker: df.mean() gives one mean per column, a Series with the column names
as labels; the DataFrame of two Series puts them side by side. Ask before the
output: which of the four means changes? The median of TAU is 0.000272 in
both cases. (~2 min)
-->

---
hideInToc: true
---

# From a Code to **NaN**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🕳️ **Count the gaps**

```python
print(df.isna().sum())
print(df["TAU"].count(), len(df))
```

```text
M          0
PT         0
TAU       49
IPCHI2     0
dtype: int64
91534 91583
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📖 **What NaN is**

- **NaN**, *not a number*, is a float64 pattern that means *no value here*. Pandas uses it for every empty cell
- `isna()` gives True for NaN. Its sum counts the gaps per column
- `count()` counts the cells that hold a value: 91 534
- `mean`, `sum`, `std` and `describe` leave NaN out

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same at reading: `pd.read_csv(path, na_values={"TAU": [-100]})`. The column is named, because −100 is a code in `TAU` only. In another column it could be a measurement.

</div>

<!--
Speaker: the gap is now visible to every function of Pandas. The 49 rows are
still in the table, with their mass, momentum and IPCHI2. (~2 min)
-->

---
hideInToc: true
---

# How NaN **Behaves**

```py {monaco-run} {autorun:false}
import numpy as np
import pandas as pd
tau = pd.Series([0.41, 0.19, -100, 0.57, -100])
print(tau.mean())                          # the code counts as a value
tau = tau.replace(-100, np.nan)
print(tau.tolist())
print(tau.isna().sum(), tau.count(), len(tau))
print(tau.mean())                          # Pandas leaves NaN out
print(np.mean(tau.to_numpy()))             # NumPy does not
print(np.nan == np.nan, (tau > 0).tolist())
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ NaN equals nothing, not even itself: find a gap with `isna()`, never with `== np.nan`. A comparison with NaN is False.

</div>

<!--
Speaker: the mean with the code is −39.766. np.mean on the array gives nan:
NumPy has np.nanmean for this. Pandas made the other choice, and a mean of a
column with gaps is the mean of the values that are there. (~2 min)
-->

---
hideInToc: true
---

# A Comparison with NaN Is **False**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Count three ways**

```python
print((df["TAU"] >= 0).sum())
print((df["TAU"] < 0).sum())
print(df["TAU"].isna().sum())
```

```text
91531
3
49
```

91 531 + 3 = 91 534. The 49 rows with NaN are in neither group.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Two masks, two tables**

- `df[df["TAU"] >= 0]` has 91 531 rows. It drops the 3 negative values and the 49 gaps, and prints nothing
- `df[~(df["TAU"] < 0)]` has 91 580 rows. It drops the 3 negative values. The gaps stay

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Write the mask for the rows that break a rule, count it, and remove it with `~`. A mask for the good rows also removes every row that could not be compared.

</div>

<!--
Speaker: 52 rows against 3. Both lines look right, and the difference appears
only in the counts. Hence the habit: count before and after every filter.
(~2 min)
-->

---
hideInToc: true
---

# Which Rows Have the **Gap**?

<img class="fig" src="/figures/viz_cleaning_missing_rows.svg" style="display:block;margin:0 auto;max-height:300px;">

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```python
gap = df["TAU"].isna()
print(df.loc[gap, "IPCHI2"].median())
print(df.loc[~gap, "IPCHI2"].median())
```

</div>

<div class="card card-warning card-glass pad-compact">

`31465.645` and `6.29089965`. Of the 49 rows without a decay time, 42 have `IPCHI2` above 1000. Among all rows, 4.6 % do.

</div>

</div>

<!--
Speaker: df.loc[mask, "name"] is rows by mask and a column by name. The gaps
are not spread evenly: they sit in the candidates that do not point back to
the collision point. Dropping them removes one kind of row. (~2 min)
-->

---
hideInToc: true
---

# Why a Value Is Missing: **Three Cases**

<div class="grid-3 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🎲 **By chance**

The gap has nothing to do with any value.

*A cable drops one reading in a hundred.*

Dropping the rows loses data. What stays is still a fair sample.

</div>

<div class="card card-warning card-glass pad-compact">

## 🔗 **Tied to another column**

The gap depends on a value that is in the table.

*`TAU` is missing where `IPCHI2` is large.*

Dropping the rows removes one kind of row. The other column shows which.

</div>

<div class="card card-accent card-glass pad-compact">

## 🚫 **Tied to the value itself**

The gap depends on the value that is missing.

*A sensor writes nothing above its range.*

The table cannot show what it lost. Only knowing how the data were taken can.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Three things can be done with a gap: keep it as NaN, drop the row, or fill it in. A filled value is a number nobody measured. If a gap is filled, a column says in which rows.

</div>

<!--
Speaker: statistics calls the three cases missing completely at random,
missing at random and missing not at random. The names matter less than the
question: are the rows with a gap like the rows without one? The line on the
previous slide answers it. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Data **Quality**

The types said the LHCb file was clean, and 49 codes were still in it. A gap is one kind of problem; four more questions find the others.

<!--
Speaker: the missing values were one kind of problem. This section goes
through the others in a fixed order, each with one line of Pandas and its
result on the file, and ends with the list on one slide. (~1 min)
-->

---
hideInToc: true
---

# A Documented **Case**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **2010 and 2013**

- 2010: a paper in economics reports that countries with public debt above 90 % of GDP grew by −0.1 % a year on average. It is quoted in debates on budget cuts
- 2013: a student asks the authors for their spreadsheet and repeats the calculation. The average is +2.2 %

</div>

<div class="card card-warning card-glass pad-compact">

## 🔍 **What the spreadsheet showed**

- A formula averaged rows 30 to 44. The data ran to row 49: 5 of 20 countries were left out
- The first post-war years of three countries were not in the calculation
- Each country counted once, whether it had 1 year in the group or 19

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

None of the three is exotic: rows left out by a slip, rows left out without a written rule, a way of averaging that nobody could see. In a spreadsheet the calculation sits in the cells, next to the data. In a script every step is a line, and every excluded row has a rule and a count.

</div>

<div class="note-text mt-sm">Reinhart & Rogoff, <em>Growth in a Time of Debt</em>, 2010. Herndon, Ash & Pollin, 2013.</div>

<!--
Speaker: the pendulum file had the same disease in small: a line with a mean,
computed by a formula, stored among the measurements. (~2 min)
-->

---
hideInToc: true
---

# Validity: **Impossible Values**

```python
bad_tau = df["TAU"] < 0
print(bad_tau.sum())
print(df[bad_tau])
```

```text
3
               M          PT       TAU      IPCHI2
22854  1844.2952  10253.5440 -0.137153   64641.477
35318  1822.4904   2943.2370 -0.059467  891711.060
42860  1867.3162   2748.1152 -0.098111  120145.600
```

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Column | Rule from its meaning | Rows that break it |
| --- | --- | --- |
| `M`, `PT` | a mass and a momentum are positive | 0 |
| `TAU` | a decay time is not negative | 3 |
| `IPCHI2` | a χ² is not negative | 0 |

</div>

<div class="card card-info card-glass pad-compact">

A validity rule comes from what the column means, not from the values in the file. Each rule is one mask, and the sum of the mask is the count. The labels on the left name the rows in the raw file.

</div>

</div>

<!--
Speaker: the three rows also have very large IPCHI2, like the rows with the
code. One line more for each of the other rules: (df["M"] <= 0).sum() and so
on, all zero. (~2 min)
-->

---
hideInToc: true
---

# Far from the Rest: **Outliers**

```python
print(df[~df["M"].between(1800, 1930)])
```

```text
               M          PT       TAU      IPCHI2
10046  2453.6584    755.2686  0.227682    1.050094
89859  1766.2096  12493.0220  0.003727  214.383360
```

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **What the file shows**

- Lecture 4 found these two at the ends of the sorted column and left them open. Its search printed lines 10048 and 89861: the header is line 1 and labels start at 0
- All other 91 581 masses lie between 1808.14 and 1920.35 MeV/c²
- Row 10046 also has the smallest `PT` of the file, 755.27

</div>

<div class="card card-warning card-glass pad-compact">

## ⚖️ **Not impossible**

A kaon and a pion can have a mass of 2454 MeV/c². The value breaks no rule of physics. It lies outside the window in which this sample was selected, and that is a statement about the file.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-sm">

An **outlier** is a value far from the others. It can be an error, or the most interesting row of the table. A script may drop it only with a reason written beside the line.

</div>

<!--
Speaker: between(a, b) is True from a to b, both ends included. Line number =
label + 2: one for the header, one because labels count from 0. Row 10046 has
the smallest PT of the file; the next smallest is 2495.66. (~2 min)
-->

---
hideInToc: true
---

# A Rule for Outliers: **1.5 × IQR**

<img class="fig" src="/figures/viz_cleaning_outlier_rule.svg" style="display:block;margin:0 auto;max-height:290px;">

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

Q1 and Q3 are the `25%` and `75%` rows of `describe()`. IQR = Q3 − Q1. The fences are Q1 − 1.5 IQR and Q3 + 1.5 IQR. For `M`: 1881.53 − 1845.99 = 35.54, fences 1792.68 and 1934.84, 2 rows outside. Lecture 8's box plot draws its whiskers to the last masses inside the fences, 1808.14 and 1920.35.

</div>

<div class="card card-warning card-glass pad-compact">

For `TAU` the fences are −0.00044 and 0.00124 ns: 11 435 rows outside, 12.5 % of the column. A decay time has a long tail by its nature. The rule was made for a symmetric column.

</div>

</div>

<!--
Speaker: a rule flags, a person decides. On M the rule finds the two rows a
person would point at. On TAU it would throw away the long-lived candidates,
which are the ones a lifetime measurement needs. (~2 min)
-->

---
hideInToc: true
---

# Uniqueness: **Duplicates**

```py {monaco-run} {autorun:false}
import pandas as pd

df = pd.DataFrame({"length_cm": [20, 30, 30, 40, 40],
                   "t10_s": [9.02, 11.05, 11.05, 12.61, 12.58]})
print(df.duplicated().tolist(), df.duplicated().sum())   # row 2 repeats row 1
print(df.duplicated(subset="length_cm").sum())           # this column only
print(df.drop_duplicates())                              # both rows of 40 cm stay
```

<div class="card card-info card-glass pad-compact mt-sm">

A duplicate is a row that is there twice: a file appended twice, a form sent twice. On `D0_KPi.csv`, `df.duplicated().sum()` is 0. `df["M"].duplicated().sum()` is 5437: equal masses in rows that differ elsewhere. They are not duplicates.

</div>

<!--
Speaker: which columns make a row "the same" is a decision. With an event
number in the file, that column would be the subset. This file has none, so
the whole row is compared. The 5437 equal masses are chance: the source stored
M as float32, with steps of 0.00012 near 1865, and 91 583 values in a window
of 100 MeV/c² must coincide now and then. (~2 min)
-->

---
hideInToc: true
---

# Consistency and **Units**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔗 **Consistency: do the parts agree?**

- With the description: `df.shape` is `(91583, 4)` and `df.dtypes` is four times `float64`, as the README says
- With each other: the raw pendulum file stores a mean, `15,14`. The mean of its nine rows is 15.1389. The two agree
- Within a column: one type, one format, one spelling

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Units: is the size right?**

```python
print(df["M"].median())
print(df["TAU"].median() * 1000)
```

```text
1864.0781
0.27245521000000006
```

The D⁰ mass is 1864.84 MeV/c²: `M` is in MeV/c², not GeV/c². The D⁰ lifetime is 0.410 ps, and a typical `TAU` × 1000 is 0.27: the column is in ns.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Lecture 4 wrote MeV/c² and ns into the README, because no command finds a unit in the file. This check tests that line: a typical value against a number known from elsewhere. A wrong unit shows as a factor of 10, 100 or 1000.

</div>

<!--
Speaker: the unit of a column is metadata. It is in the README or in the name
of the column, and nowhere in the numbers. The check is the only way to catch
a README that is wrong. (~2 min)
-->

---
hideInToc: true
---

# Mixed Units in **One Column**

```py {monaco-run} {autorun:false}
import pandas as pd

df = pd.DataFrame({"length_cm": [20, 30, 0.4, 50, 0.6],
                   "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49]})
in_m = df["length_cm"] < 2                 # nobody built a pendulum of 0.4 cm
print(in_m.sum(), "rows are in metres")
df.loc[in_m, "length_cm"] = df.loc[in_m, "length_cm"] * 100
print(df)
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ `df.loc[mask, "name"] = …` writes into the rows of the mask. `df[mask]["name"] = …` writes into a temporary copy: the table stays as it was, and Pandas prints a warning.

</div>

<!--
Speaker: two people typed into one column, one in centimetres and one in
metres. The mask states the rule, its sum is the count, and loc repairs the
rows in place. (~2 min)
-->

---
hideInToc: true
---

# Five Questions for **Any Table**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Question | One line | `D0_KPi.csv` | `pendulum.csv`, raw |
| --- | --- | --- | --- |
| **Completeness**: is every cell filled? | `df.isna().sum()`, `(df == -100).sum()` | no empty cell, 49 codes in `TAU` | 1 empty cell in `nr` |
| **Validity**: can every value be true? | `(df["TAU"] < 0).sum()` | 3 rows | 0 rows |
| **Uniqueness**: is each row there once? | `df.duplicated().sum()` | 0 rows | 0 rows |
| **Consistency**: do the parts agree? | `df.dtypes`, `df.shape` | 4 × `float64`, 91 583 × 4 | `length_cm` is text |
| **Units**: is a typical value the right size? | `df["M"].median()` | 1864.08, known 1864.84 | g = 979.5 without cm to m |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact">

The five lines take a minute on any table. They are run before the first plot and before the first fit.

</div>

<div class="card card-success card-glass pad-compact">

The result is a list of counts for the README. Lecture 4 counted the 49 codes of `TAU` with `grep -c`. `(df == -100).sum()` counts them in every column at once.

</div>

</div>

<!--
Speaker: this is the slide to keep. The questions stay the same for every
table. The value in each line is taken from the description of the columns.
(~3 min)
-->

---
hideInToc: true
---

# The Checklist as a **Function**

```py {monaco-run} {autorun:false}
import pandas as pd
def audit(df, code=None):
    print("rows, columns: ", df.shape)
    print("types:         ", df.dtypes.astype(str).to_dict())
    print("empty cells:   ", df.isna().sum().to_dict())
    if code is not None:
        print("cells == code: ", (df == code).sum().to_dict())
    print("duplicate rows:", df.duplicated().sum())
    print("smallest:      ", df.min().to_dict())
    print("largest:       ", df.max().to_dict())
df = pd.DataFrame({"length_cm": [20, 30, 30, 40, -999],
                   "t10_s": [9.02, 11.05, 11.05, None, 12.61]})
audit(df, code=-999)
```

<!--
Speaker: five rows with one gap, one code and one duplicate. The function
knows nothing about pendulums: it takes any DataFrame. Validity and units
need the meaning of the columns, so the function prints the smallest and the
largest value and leaves the judgement to the reader. (~2 min)
-->

---
layout: section
hideInToc: true
---

# The Cleaned **Table**

The audit counted 49 codes, 3 negative decay times and 2 masses far outside. Each decision about them becomes one line of a script, with its count.

<!--
Speaker: the audit found 49 codes, 3 negative decay times and 2 masses far
outside. Now the decisions are written as a script, as for the pendulum, and
the script reports what it did. (~1 min)
-->

---
hideInToc: true
---

# One Mask per **Rule**

```python
df = pd.read_csv("data/raw/D0_KPi.csv")

n_code = (df["TAU"] == -100).sum()             # 1. -100 is the code for a missing decay time
df["TAU"] = df["TAU"].replace(-100, np.nan)

bad_tau = df["TAU"] < 0                        # 2. a decay time is not negative
bad_m = ~df["M"].between(1800, 1930)           # 3. outside the mass window of the sample
dup = df.duplicated()                          # 4. one candidate written twice

clean = df[~bad_tau & ~bad_m & ~dup]
```

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

**A gap stays a gap.** The 49 rows keep their mass and momentum. An analysis that needs `TAU` drops them itself.

</div>

<div class="card card-warning card-glass pad-compact">

**A broken rule removes the row.** Each rule has a name, a reason in the comment and a count.

</div>

<div class="card card-info card-glass pad-compact">

**Nothing is filled in** and nothing is removed for being unusual: the long decay times stay.

</div>

</div>

<!--
Speaker: these are decisions, and another analyst may decide otherwise, for
example set the three negative decay times to NaN and keep the rows. What
cannot differ is that the decision is written down and counted. (~3 min)
-->

---
hideInToc: true
---

# The Script and **Its Log**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 💾 **Write and report**

```python
OUT = "data/processed/d0_clean.csv"
clean.to_csv(OUT, index=False,
             lineterminator="\n")

print("rows read          ", len(df))
print("TAU = -100 -> NaN  ", n_code)
print("TAU < 0, dropped   ", bad_tau.sum())
print("M outside, dropped ", bad_m.sum())
print("duplicates, dropped", dup.sum())
print("rows written       ", len(clean))
```

</div>

<div class="card card-success card-glass pad-compact">

## 🧾 **The log of `scripts/clean_d0.py`**

```text
rows read           91583
TAU = -100 -> NaN   49
TAU < 0, dropped    3
M outside, dropped  2
duplicates, dropped 0
rows written        91578
```

91 583 − 3 − 2 = 91 578. Every row that left the table is in one line of the log.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The log is the cleaning written as numbers. It goes into the README. When the raw file changes, the script is run again and the numbers are compared.

</div>

<!--
Speaker: no float_format here. The file has values from 0.000014 to 891 711,
and Pandas writes each number with the digits it read. (~2 min)
-->

---
hideInToc: true
---

# What the Script **Changed**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📊 **`D0_KPi.csv` and `d0_clean.csv`**

| | Raw | Clean |
| --- | --- | --- |
| Rows | 91 583 | 91 578 |
| Bytes | 3 926 142 | 3 925 641 |
| Gaps | 49, written `-100.0` | 49, written as nothing |
| SHA-256 | `25c3c972…c1505136` | `7aa9470b…3bb91b16` |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Line by line**

```text
raw     1818.1002,2978.644,-100.0,9901.186
clean   1818.1002,2978.644,,9901.186
```

- NaN is written as an empty cell, and `read_csv` reads an empty cell as NaN
- 5 lines are gone and 49 have changed. All other lines are the same text in both files

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

📁 The raw file has the same checksum before and after the run. It is read and never written. The cleaned file can be deleted at any time: the script and the raw file make it again.

</div>

<!--
Speaker: the checksum of the raw file is the one computed in Lecture 4,
25c3c972…c1505136. Run it once more after the script: shasum -a 256 on macOS,
(Get-FileHash data\raw\D0_KPi.csv).Hash in PowerShell. (~2 min)
-->

---
hideInToc: true
---

# A Derived Column and **groupby**

```python
clean = pd.read_csv("data/processed/d0_clean.csv")
clean["tau_ps"] = clean["TAU"] * 1000
clean["region"] = np.where(clean["M"].between(1840, 1890), "peak", "side")
print(clean.groupby("region")["tau_ps"].agg(["size", "count", "median"]))
```

```text
         size  count    median
region                        
peak    56575  56546  0.308202
side    35003  34983  0.232948
```

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔀 **Split, apply, combine**

`groupby("region")` splits the rows by the values of that column. `["tau_ps"]` takes one column of each group. `agg` applies the functions and combines the results into one small table.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **The result**

`size` counts rows and `count` counts values: 29 gaps in the peak, 20 beside it. The median decay time is 0.308 ps in the peak and 0.233 ps in the sidebands.

</div>

</div>

<!--
Speaker: np.where(mask, a, b) gives a where the mask is True and b elsewhere.
The analysis starts from the processed file, not from the raw one. (~3 min)
-->

---
hideInToc: true
---

# The Groups in a **Picture**

<img class="fig" src="/figures/viz_cleaning_regions.svg" style="display:block;margin:0 auto;max-height:330px;">

<div class="note-text mt-sm">

Left: the derived column `region` splits the mass axis. Right: the decay times of the two groups, each with its median. The peak region holds the D⁰ mesons, on top of chance pairs of tracks. The sidebands hold chance pairs only. A D⁰ travels before it decays, and the median of the peak region is the larger one.

</div>

<!--
Speaker: one line of groupby computed the two dashed lines. A third region
would be one more value in the column and no new code. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Reshape & **Join**

One table is clean. The partner's second file is a second series of the same lengths, and two tables have to become one.

<!--
Speaker: so far one table. Real work has several: two series of the same
measurement, a table of values and a table of descriptions. Three operations
put them together: melt, concat and merge. (~1 min)
-->

---
hideInToc: true
---

# Tidy **Tables**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ↔️ **Wide: one column per series**

```text
length_cm   run1    run2
20          9.02    8.97
40         12.61   12.74
60         15.49   15.58
```

The number of the series is hidden in the column names. A third series adds a column, and every line of code that names the columns changes.

</div>

<div class="card card-success card-glass pad-compact">

## ↕️ **Tidy: one row per measurement**

```text
length_cm   run   t10_s
20          1      9.02
40          1     12.61
60          1     15.49
20          2      8.97
…
```

A third series adds rows. The code stays.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A table is **tidy** when each row is one observation, each column one variable and each cell one value: the anatomy of a table of Lecture 2. The raw pendulum file broke the rule twice: a row that was not an observation, the mean, and a column that was not a variable, the row number.

</div>

<!--
Speaker: run2 is the partner's second file at three of its lengths, 20, 40
and 60 cm. Wide tables are good for reading and tidy ones for computing.
groupby, plotting and fitting all expect the tidy form. (~2 min)
-->

---
hideInToc: true
---

# From Wide to **Tidy**

```py {monaco-run} {autorun:false}
import pandas as pd

wide = pd.DataFrame({"length_cm": [20, 40, 60],
                     "run1": [9.02, 12.61, 15.49],
                     "run2": [8.97, 12.74, 15.58]})
tidy = wide.melt(id_vars="length_cm", var_name="run", value_name="t10_s")
print(tidy)
print(tidy.groupby("length_cm")["t10_s"].mean().round(3).to_dict())
```

<div class="card card-info card-glass pad-compact mt-sm">

`melt` keeps `length_cm` and turns every other column into rows: the old column name goes into `run` and the value into `t10_s`. Three rows of two values become six rows of one. `groupby` then gives the mean of the two series for each length.

</div>

<!--
Speaker: the way back is tidy.pivot(index="length_cm", columns="run",
values="t10_s"). Type it under the fence. (~2 min)
-->

---
hideInToc: true
---

# Stack Tables: **concat**

```py {monaco-run} {autorun:false}
import pandas as pd

run1 = pd.DataFrame({"length_cm": [20, 40, 60], "t10_s": [9.02, 12.61, 15.49]})
run2 = pd.DataFrame({"length_cm": [20, 40, 60], "t10_s": [8.97, 12.74, 15.58]})
run1["run"] = 1                            # say where each row came from
run2["run"] = 2
both = pd.concat([run1, run2], ignore_index=True)
print(both)
```

<div class="card card-info card-glass pad-compact mt-sm">

`concat` puts tables with the same columns under one another: two files of the same form become one table. A column says which file a row came from, because after the stacking nothing else does. Without `ignore_index=True` the labels would run 0, 1, 2, 0, 1, 2.

</div>

<!--
Speaker: this is how a folder of files with one day each, or one run each,
becomes a single table: read each, add the column, concat the list. (~2 min)
-->

---
hideInToc: true
---

# Join Tables: **merge**

```py {monaco-run} {autorun:false}
import pandas as pd

run1 = pd.DataFrame({"length_cm": [20, 30, 40, 50, 60],
                     "t10_s": [9.02, 11.05, 12.61, 14.23, 15.49]})
run2 = pd.DataFrame({"length_cm": [20, 40, 60], "t10_s": [8.97, 12.74, 15.58]})
left = run1.merge(run2, on="length_cm", how="left", suffixes=("_1", "_2"))
print(left)
inner = run1.merge(run2, on="length_cm", suffixes=("_1", "_2"))
print(len(left), len(inner), left["t10_s_2"].isna().sum())
```

<div class="card card-info card-glass pad-compact mt-sm">

`merge` puts tables side by side and matches the rows by a **key**, here `length_cm`. `how="left"` keeps every row of the left table: 5 rows, and NaN where the right table has no match. The default, `how="inner"`, keeps the 3 rows found in both.

</div>

<!--
Speaker: a left join is a place where gaps are born. The two NaN in t10_s_2
were in neither file. Count the rows before and after every merge. (~2 min)
-->

---
hideInToc: true
---

# A Join Changes the **Row Count**

```py {monaco-run} {autorun:false}
import pandas as pd
run1 = pd.DataFrame({"length_cm": [20, 30, 40], "t10_s": [9.02, 11.05, 12.61]})
run2 = pd.DataFrame({"length_cm": [20, 40, 40], "t10_s": [8.97, 12.74, 12.74]})
m = run1.merge(run2, on="length_cm", how="left", suffixes=("_1", "_2"))
print(m)
print(len(run1), "rows in,", len(m), "rows out")
print(run2.duplicated().sum(), "duplicate in run2")
```

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ A key that stands twice in one table matches twice: the row of 40 cm is in the result two times. Every sum over the joined table then counts it double. Check uniqueness before a join, or let Pandas check: `merge(…, validate="one_to_one")` stops with `MergeError: Merge keys are not unique in right dataset`.

</div>

<!--
Speaker: three rows in, four rows out, and one of them is NaN. Both things a
join can do to a table are on this slide: lose a match and double a row.
(~2 min)
-->

---
hideInToc: true
---

# The Second File, **Five Questions**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Question | One line on `pendulum_run2.csv`, cleaned | Answer |
| --- | --- | --- |
| **Completeness** | `df.isna().sum()` | 1 gap: `t10_s` at 80 cm |
| **Validity** | `(df["t10_s"] <= 0).sum()` | 0 rows |
| **Uniqueness** | `df["length_cm"].duplicated().sum()` | 0 rows |
| **Consistency** | `df["t10_s"].mean()` | 14.80125, the partner wrote `14,80` |
| **Units** | `g.median()`, with `length_cm / 100` | 9.76 m/s² |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

Had the empty cell become a 0, the mean would be 118.41 / 9 = 13.16, and the partner's line would disagree. NaN is left out, as the spreadsheet left out the empty cell.

</div>

<div class="card card-success card-glass pad-compact">

Lecture 4's script wrote 10 rows and no warning. `clean.py` wrote 9, and five lines say what is in them: one gap, every value possible, each length once, the mean confirmed, g of the right size.

</div>

</div>

<!--
Speaker: the closing slide; do not cut it. df is read from
data/processed/pendulum_run2.csv; g is the column of the DataFrame section,
4π² L / T², eight values from 9.73 to 9.86. The partner's mean of the eight
times is 118.41 / 8 = 14.80125. Ask the room which question would have caught
the Mean row of Lecture 4's output: consistency, since length_cm would be
text. (~3 min)
-->

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Clean by **rule**, not by text: a script that reads `data/raw/`, writes `data/processed/`, gives the same bytes on every run, and counts what each rule took

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a file with `read_csv`, state its **separator and decimal sign**, and find a bad cell from the type of its column

</div>

<div class="card card-success card-glass pad-compact">

✅ Select by **name, position and mask**, add a column, sort, and summarise with `describe()`

</div>

<div class="card card-success card-glass pad-compact">

✅ Turn a code into **NaN** and say why 49 rows moved a mean, and why a comparison with NaN is False

</div>

<div class="card card-success card-glass pad-compact">

✅ Run the **five questions** on a table: completeness, validity, uniqueness, consistency, units

</div>

<div class="card card-success card-glass pad-compact">

✅ Make a table tidy, **group** it, **join** it, and count the rows before and after each step

</div>

</div>

<!--
Speaker: the habit to take away is the count. Rows in, rows out, and one
line for every rule in between: 10 in, 9 out, 1 gap for the partner's file;
91 583 in, 91 578 out for the LHCb file. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="A column holds 1000 temperatures. 990 of them have a mean of 20.0, and 10 cells hold the code `-999` for a missing value. What does `mean()` give before the code is replaced?"
  :options="[
    '20.0, because Pandas leaves missing values out',
    '9.81',
    'NaN',
    '−999'
  ]"
  :correct="1"
  explanation="Pandas leaves out NaN, and −999 is a number like any other. The sum is 990 × 20 + 10 × (−999) = 19 800 − 9990 = 9810, and 9810 / 1000 = 9.81. One cell in a hundred halves the mean. After replace(-999, np.nan) the mean is 20.0."
/>

---
hideInToc: true
---

<MCQ
  question="`s = pd.Series([4.0, np.nan, 8.0])`. What are `s.mean()`, `s.count()` and `(s > 5).sum()`?"
  :options="[
    '4.0, 3 and 1',
    'NaN, 3 and 1',
    '6.0, 2 and 1',
    '6.0, 3 and 2'
  ]"
  :correct="2"
  explanation="mean leaves NaN out: (4 + 8) / 2 = 6.0. count counts the cells that hold a value: 2. The comparison NaN > 5 is False, so only 8.0 is counted: 1. len(s) is still 3."
/>

---
hideInToc: true
---

<MCQ
  question="After `pd.read_csv`, the column `mass` of a file with 5000 rows has the type `object` (`str` in Pandas 3). Every value you see on the screen is a number. What is the most likely reason?"
  :options="[
    'The file is too large for the type float64',
    'At least one cell of the column is not a number: a word, a unit, or a decimal comma',
    'Pandas reads every column as text until astype is called',
    'The column has more than six significant digits'
  ]"
  :correct="1"
  explanation="A column has one type. One cell such as n/a, 12,5 or 3.1 kg turns the whole column into text, and head() shows only the first five rows. pd.to_numeric(df.mass, errors='coerce') turns every cell that is not a number into NaN, and isna() then finds the rows."
/>

---
hideInToc: true
---

<MCQ
  question="For a column, `describe()` gives 25% = 10 and 75% = 14. Which of the values 3, 5, 19 and 21 does the 1.5 × IQR rule flag?"
  :options="[
    'All four',
    '3 and 21',
    '21 only',
    'None'
  ]"
  :correct="1"
  explanation="IQR = 14 − 10 = 4, and 1.5 × 4 = 6. The fences are 10 − 6 = 4 and 14 + 6 = 20. The values 3 and 21 lie outside, 5 and 19 inside. The rule flags them. Whether they are errors is a second question."
/>

---
hideInToc: true
---

<MCQ
  question="Table `a` has 5 rows with the keys 1, 2, 3, 4, 5. Table `b` has 4 rows with the keys 2, 3, 3, 6. How many rows does `a.merge(b, on='key', how='left')` have?"
  :options="[
    '3',
    '4',
    '5',
    '6'
  ]"
  :correct="3"
  explanation="A left join keeps every row of a. Keys 1, 4 and 5 have no match and give one row each, with NaN in the columns of b. Key 2 matches once. Key 3 matches twice and gives two rows. 3 + 1 + 2 = 6. Key 6 is only in b and is left out. The inner join has 3 rows."
/>

---
hideInToc: true
---

<MCQ
  question="A cleaned table is saved with `df.to_csv('clean.csv')` and read again with `pd.read_csv('clean.csv')`. The table that comes back has one column more. Where does it come from?"
  :options="[
    'read_csv adds a column with the line numbers of the file',
    'to_csv wrote the index as a first column, and read_csv reads it as data',
    'NaN cells were written into a column of their own',
    'The file was written with CRLF line endings'
  ]"
  :correct="1"
  explanation="Without index=False the row labels are written as the first column, with no name in the header line. At the next read that column is named Unnamed: 0, and a new index is added. to_csv('clean.csv', index=False) writes only the columns of the table."
/>
