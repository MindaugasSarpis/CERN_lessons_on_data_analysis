---
layout: cover
title: "Python for Data & NumPy"
# slidev-addon-python-runner reads this block from slide 1 = this cover (see CLAUDE.md)
python:
  installs: ["numpy"]
  prelude: |
    import numpy as np
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python for Data & NumPy

##### <span class="aims-badge">📁 data & files · ⚙️ automation · 🔧 tool-agnostic</span>

<!--
Speaker: Lecture 06 gave values, types, loops, lists and dicts, and one line of
the data file was turned into numbers. Today the whole file is read and
computed with, twice: with a loop over lists, then with a NumPy array. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The goal of this lecture is to read a file of 91 583 rows into Python and compute with it. First row by row, with a loop over lists. Then as one **array**, with NumPy.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

⚙️ Write a **function** with parameters, a default value and a `return`

</div>

<div class="card card-secondary card-glass pad-compact">

🛡️ Catch the **exception** you expect with `try` and `except`, and let every other one stop the program

</div>

<div class="card card-accent card-glass pad-compact">

📁 Build a path with **pathlib** and read a CSV file into lists with the **csv** module

</div>

<div class="card card-success card-glass pad-compact">

🔢 Read the same file into a **NumPy array** and state its `dtype` and its `shape`

</div>

<div class="card card-warning card-glass pad-compact">

🎯 Select values with an index, a slice and a **boolean mask**

</div>

<div class="card card-info card-glass pad-compact">

➗ Compute on whole arrays: arithmetic, **broadcasting**, `mean`, `std`, `np.histogram`

</div>

</div>

---
hideInToc: true
---

# One Task, **Two Ways**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The file**, `data/raw/D0_KPi.csv`

```text
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
1913.8755,2542.169,0.00018464602,17.386473
…
```

91 583 rows, four columns, 3 926 142 bytes. `M` is a mass in MeV/c². `TAU` is a decay time in ns, and `-100` in that column marks a missing value.

</div>

<div class="card card-secondary card-glass pad-compact">

## ❓ **Four questions**

1. How many rows does the file have?
2. What is the mean of `M`?
3. In how many rows is `TAU` valid?
4. What is the mean of the valid `TAU`?

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The questions are answered twice. First with lists and a loop, which needs three new tools: functions, exceptions and the `csv` module. Then with a NumPy array. Both versions are timed.

</div>

<!--
Speaker: the file is the one in data/raw since week 2. The room has parsed one
of its lines by hand. Write the four questions on the board: they stay there
for the whole lecture and get their answers on the way. (~2 min)
-->

---
layout: section
hideInToc: true
---

# **Functions**

<!--
Speaker: so far every script was a list of steps run once from top to bottom.
A function gives a group of steps a name, so that they can be run again with
other values. (~1 min)
-->

---
hideInToc: true
---

# Defining a **Function**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Definition and two calls**

```python
import math

def period(length_m):
    return 2 * math.pi * math.sqrt(length_m / 9.81)

print(period(0.20))    # 0.8971402930932747
print(period(1.00))    # 2.0060666807106475
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **The parts**

- `def` starts the definition and `period` is the name
- `length_m` is a **parameter**: a name for the value that comes in
- The indented lines are the body. They run at every call, not at the definition
- `return` ends the call and hands a value back

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The body is the formula for one swing of a pendulum of length *L*: *T* = 2π√(*L*/*g*). The first row of the pendulum table has *L* = 20 cm. The function gives 0.897 s for one swing, so 8.97 s for ten. The measured time is 9.02 s.

</div>

<!--
Speaker: type it live. `import math` makes math.pi and math.sqrt available.
Call the function before the def line once, to show the NameError: a function
exists only after its definition has run. (~3 min)
-->

---
hideInToc: true
---

# Parameters, Arguments, **Defaults**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **A second parameter with a default**

```python
def period(length_m, g=9.81):
    return 2 * math.pi * math.sqrt(length_m / g)

print(period(0.20))           # 0.8971402930932747
print(period(0.20, 1.62))     # 2.2076862812880225
print(period(0.20, g=1.62))   # 2.2076862812880225
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **How a call is matched**

- An **argument** is the value given at the call: `0.20`
- Arguments are matched by position, or by name: `g=1.62`
- A parameter with a default may be left out of the call
- Parameters with a default stand after those without

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The unit is in the name: `length_m`. The call `period(20)` raises no error. It returns 8.97 s, the period of a pendulum 20 m long. A function cannot check what a number means.

</div>

<div class="note-text mt-sm">1.62 m/s² is <em>g</em> on the Moon. The same pendulum takes 2.2 s for a swing there.</div>

---
hideInToc: true
---

# `return` Is Not `print`

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🖨️ **A function that prints**

```python
def show_period(length_m):
    print(2 * math.pi * math.sqrt(length_m / 9.81))

t = show_period(0.20)   # prints 0.8971402930932747
print(t)                # None
print(10 * t)           # TypeError
```

`TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'`

</div>

<div class="card card-success card-glass pad-compact">

## ↩️ **A function that returns**

```python
def period(length_m):
    return 2 * math.pi * math.sqrt(length_m / 9.81)

t = period(0.20)
print(round(10 * t, 2))   # 8.97
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`print` shows a value to a person. `return` gives it to the program. A function without `return` gives back `None`. A function that computes should return its result, and the code that called it decides what is printed.

</div>

---
hideInToc: true
---

# Names Inside a Function Are **Local**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **A mean, by loop**

```python
def mean(values):
    total = 0.0
    for v in values:
        total += v
    return total / len(values)

print(mean([9.02, 11.05, 12.61]))
print(total)
```

```text
10.893333333333333
NameError: name 'total' is not defined
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔒 **What is visible where**

- `values`, `total` and `v` exist only while a call runs
- Input comes in through the parameters. Output leaves through `return`
- Two functions can both use the name `total`. They do not touch each other
- A function that reads a name defined outside of it depends on something its call does not show. Pass that value in as a parameter

</div>

</div>

<!--
Speaker: this is why a function can be tested alone and reused in another
script: everything it needs is in its parameter list. (~2 min)
-->

---
hideInToc: true
---

# Try It — A Function for the **Mean**

```py {monaco-run} {autorun:false}
def mean(values):
    total = 0.0
    for v in values:
        total += v
    return total / len(values)

t10 = [9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01]
print(mean(t10))
print(round(mean(t10), 2))
```

<div class="card card-info card-glass pad-compact mt-md">

These are the nine times of the pendulum table. The file as received had a last line with their mean, `15,14`. Then write `spread(values)`, which returns the largest value minus the smallest. For this list it is 10.99, rounded to two decimals.

</div>

<!--
Speaker: run it: 15.138888888888886 and 15.14. Let the room write spread with
max() and min(), or with a loop. Then call mean([]) and read the
ZeroDivisionError: the next section is about such cases. (~4 min)
-->

---
hideInToc: true
---

# One Line of the File as a **Function**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Strip, split, convert**

```python
def parse_line(line):
    numbers = []
    for part in line.strip().split(","):
        numbers.append(float(part))
    return numbers

row = parse_line(
    "1880.649,3000.9534,0.00041271152,1299.1675\n")
print(row)
print(row[0] + row[1])
```

```text
[1880.649, 3000.9534, 0.00041271152, 1299.1675]
4881.6024
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ✅ **Test it on a line you can check**

- The three steps of Lecture 06 now have a name
- The test line is line 2 of the file. Its four numbers can be compared by eye
- A function is checked once on a case with a known answer. Then it is used on 91 583 lines
- Line 1 of the file is `M,PT,TAU,IPCHI2`. What does `parse_line` do with it?

</div>

</div>

---
layout: section
hideInToc: true
---

# **Exceptions**

<!--
Speaker: a data file has a header, empty fields and typing errors. A program
that reads it has to say what happens then. (~1 min)
-->

---
hideInToc: true
---

# An Exception **Stops the Program**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 💥 **The header line**

```python
row = parse_line("M,PT,TAU,IPCHI2\n")
print("done")
```

```text
Traceback (most recent call last):
  File "…/scripts/parse.py", line 7, in <module>
    row = parse_line("M,PT,TAU,IPCHI2\n")
  File "…/scripts/parse.py", line 4, in parse_line
    numbers.append(float(part))
ValueError: could not convert string to float: 'M'
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **What happened**

- `float("M")` has no number to return. It **raises** an exception: an object with a type, `ValueError`, and a message
- The exception leaves `float`, then `parse_line`, then the script. Nothing on the way handles it
- The program stops. `done` is never printed
- The traceback is that path. Its last line gives the type and the message

</div>

</div>

<!--
Speaker: the room read tracebacks from the bottom in Lecture 06. New here: the
traceback has two levels, because the error happened inside a function that
was called from the script. Python 3.11 and later also print a line of ~ and ^
signs under the part of the line that failed. (~2 min)
-->

---
hideInToc: true
---

# `try` and `except`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Two texts, one of them not a number**

```python
for text in ["1864.8", "N/A"]:
    try:
        value = float(text)
        print("converted")
    except ValueError:
        value = None
        print("not a number")
    print(value)
```

```text
converted
1864.8
not a number
None
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔀 **Which lines run**

| | `"1864.8"` | `"N/A"` |
| --- | --- | --- |
| `float(text)` | returns 1864.8 | raises `ValueError` |
| rest of the `try` block | runs | is skipped |
| the `except` block | is skipped | runs |
| the line after it | runs | runs |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`try` marks the lines that may fail. `except ValueError` names the one failure that is handled and says what to do instead. Any other exception passes through and stops the program.

</div>

---
hideInToc: true
---

# Exceptions in **Data Files**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The line | Raises | The usual cause |
| --- | --- | --- |
| `float("N/A")` | `ValueError` | A field that is not a number |
| `float("9,02")` | `ValueError` | A decimal comma |
| `row[4]`, in a row of four fields | `IndexError` | A short row, or a wrong column number |
| `row["mass"]`, in a dict | `KeyError` | The column has another name: `M` |
| `open("data/D0_KPi.csv")` | `FileNotFoundError` | A wrong folder or file name |
| `mean([])` | `ZeroDivisionError` | No row passed the selection |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 💬 **The message names the value**

```text
ValueError: could not convert string
to float: '9,02'
IndexError: list index out of range
KeyError: 'mass'
```

</div>

<div class="card card-info card-glass pad-compact">

## 🧭 **Expected or not**

The first four happen in any file that people have typed or exported. A program handles them: it skips the row, or stops with a clear message. The type of the exception says which case it is.

</div>

</div>

<!--
Speaker: every message here was produced by running the line. Ask which of
these the room has already met in its own scripts. (~2 min)
-->

---
hideInToc: true
---

# Try It — Skip a Bad Row, **Count It**

```py {monaco-run} {autorun:false}
rows = ["1,1864.8", "2,N/A", "3,1865.9", "4"]
masses = []
skipped = 0
for line in rows:
    try:
        masses.append(float(line.split(",")[1]))
    except (ValueError, IndexError):
        skipped += 1
print(masses)
print("skipped:", skipped)
```

<div class="card card-info card-glass pad-compact mt-md">

A bad row must not stop the run, and it must not vanish without a trace. Skip it, count it, report the count. `"2,N/A"` raises `ValueError` and `"4"` raises `IndexError`. The tuple after `except` names both.

</div>

<!--
Speaker: run it: [1864.8, 1865.9] and skipped: 2. Then remove IndexError from
the tuple and run again: the program stops at the row "4". (~3 min)
-->

---
hideInToc: true
---

# Catch Only What You **Expect**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ❌ **`except:` with no type**

```python
for line in rows:
    try:
        masses.append(flaot(line.split(",")[1]))
    except:
        skipped += 1
print(masses)
print("skipped:", skipped)
```

```text
[]
skipped: 4
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **The two types named**

```python
    except (ValueError, IndexError):
        skipped += 1
```

```text
NameError: name 'flaot' is not defined
```

The typo stops the program at the first row, and the traceback points at the line.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A bare `except:` catches everything, the typo `flaot` included. The program ends without an error and reports four bad rows in a list that has two. A function reports a problem of its own in the same way: `raise ValueError("mean of an empty list")`.

</div>

---
layout: section
hideInToc: true
---

# Files & the **csv Module**

<!--
Speaker: three steps to the whole file in Python: open it, find it from any
laptop, and split its lines by the rules of the CSV format. (~1 min)
-->

---
hideInToc: true
---

# Reading and Writing a **Text File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📖 **Read, line by line**

```python
n_lines = 0
with open("data/raw/D0_KPi.csv",
          encoding="utf-8") as f:
    for line in f:
        n_lines += 1
        if n_lines <= 2:
            print(repr(line))
print(n_lines, "lines")
```

```text
'M,PT,TAU,IPCHI2\n'
'1880.649,3000.9534,0.00041271152,1299.1675\n'
91584 lines
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ✍️ **Write**

```python
with open("results/summary.txt", "w",
          encoding="utf-8") as f:
    f.write(f"rows {n_lines - 1}\n")
```

The file then holds one line: `rows 91583`.

- `"w"` replaces the file if it exists. `"a"` adds to its end
- `write` adds no line break. The `\n` is written out

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`open` gives a file object, and the loop takes one line at a time as a `str` that ends in `\n`. `with` closes the file at the end of the block, also when an exception is raised inside it. `encoding="utf-8"` names the table from bytes to characters. Without it Python takes the default of the system, and that differs between laptops.

</div>

<!--
Speaker: 91 584 lines are one header line and 91 583 rows. That is the answer
to question 1, and it agrees with the line count in VS Code. repr shows the
line break that print would turn into an empty line. (~3 min)
-->

---
hideInToc: true
---

# A Path Starts at the **Working Directory**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 `scripts/first_line.py`

```python
with open("data/raw/D0_KPi.csv",
          encoding="utf-8") as f:
    print(f.readline().strip())
```

Run in the project folder:

```text
$ python scripts/first_line.py
M,PT,TAU,IPCHI2
```

Run in `scripts`:

```text
$ cd scripts
$ python first_line.py
FileNotFoundError: [Errno 2] No such file
or directory: 'data/raw/D0_KPi.csv'
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **Where a relative path begins**

- A relative path begins at the folder the terminal is in: the working directory. `pwd` prints it
- It does not begin at the folder of the script
- The **Run** button of VS Code starts the script in the folder that is open
- Open the project folder, run from the project folder, write every path from the project folder
- An absolute path such as `C:\Users\ona\Documents\…` exists on one laptop only. It does not go into a script

</div>

</div>

<!--
Speaker: do both runs live. This error is the most common one of the first
weeks with files, and its cause is never in the script. (~2 min)
-->

---
hideInToc: true
---

# `pathlib`: a Path as an **Object**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Build it, ask it**

```python
from pathlib import Path

path = Path("data") / "raw" / "D0_KPi.csv"

print(path)                  # data/raw/D0_KPi.csv
print(path.name)             # D0_KPi.csv
print(path.suffix)           # .csv
print(path.parent)           # data/raw
print(path.exists())         # True
print(path.stat().st_size)   # 3926142
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **What it gives**

- `/` joins the parts. On Windows the first line prints `data\raw\D0_KPi.csv`, and the script is the same on every system
- A string knows nothing about folders and endings. A `Path` has them as attributes
- `exists()` answers before `open` fails
- `st_size` is the size in bytes, the number `ls -l` shows
- `open(path)` takes a `Path` wherever it takes a string

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`Path.cwd()` is the working directory. In a script that lies in `scripts/`, `Path(__file__).resolve().parent.parent` is the project folder, from wherever the script is started: `__file__` is the path of the script itself.

</div>

---
hideInToc: true
---

# `csv.reader`: One Row, One **List of Strings**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **The header and the first row**

```python
import csv

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    first = next(reader)

print(header)
print(first)
```

```text
['M', 'PT', 'TAU', 'IPCHI2']
['1880.649', '3000.9534', '0.00041271152', '1299.1675']
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **What the module does**

- `csv` is part of Python. Nothing is installed
- The reader gives one list per line. `next` takes the next one
- `newline=""` leaves the line endings to the module, so a file with LF and one with CRLF read the same
- Every value is a `str`. `first[0] + first[1]` is `'1880.6493000.9534'`. With `float` around each it is 4881.6024

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `split(",")` cuts at every comma. A field that contains a comma is written in quotes, and the line `20,"9,02"` has two fields. `split` returns `['20', '"9', '02"']`. `csv.reader` returns `['20', '9,02']`. For a file with semicolons: `csv.reader(f, delimiter=";")`.

</div>

---
hideInToc: true
---

# Four Columns, Four **Lists**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **The whole file**

```python
M, PT, TAU, IPCHI2 = [], [], [], []
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        M.append(float(row[0]))
        PT.append(float(row[1]))
        TAU.append(float(row[2]))
        IPCHI2.append(float(row[3]))

print(len(M), "rows")   # 91583 rows
print(M[:3])   # [1880.649, 1860.6599, 1913.8755]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **What the loop does**

- `next` takes the header off before the loop starts
- `float` runs on every field: 4 × 91 583 = 366 332 conversions
- One list per column, because a sum or a mean is taken over a column
- The four lists stay in step: index 0 of each belongs to the first row of the file

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`csv.DictReader(f)` gives every row as a dict with the header as keys, so a field is `row["M"]` and not `row[0]`. It reads the `M` column of this file in 94 ms. `csv.reader` takes 39 ms.

</div>

<!--
Speaker: the dict costs time because one is built for each of the 91 583 rows.
For a file of this size both are fast. The names are worth the time when the
file has many columns. (~3 min)
-->

---
hideInToc: true
---

# A Mean and a Count **by Loop**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Two loops**

```python
total = 0.0
for m in M:
    total += m
print(total / len(M))

n_valid = 0
for t in TAU:
    if t != -100:
        n_valid += 1
print(n_valid, len(TAU) - n_valid)
```

```text
1864.1045817826146
91534 49
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ✅ **The answers so far**

| Question | Answer |
| --- | --- |
| Rows | 91 583 |
| Mean of `M` | 1864.10 MeV/c² |
| Rows with a valid `TAU` | 91 534 |
| Rows with `TAU` = −100 | 49 |

The mean lies at the D⁰ peak near 1865 MeV/c². The 49 are the places that Find showed for `-100` when the file was first opened in VS Code.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every further question is a further loop: the smallest value, the largest, the mean of the valid `TAU`, the same for `PT`.

</div>

---
hideInToc: true
---

# The Script as **Functions**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧰 **Two tools**

```python
def read_column(path, index):
    values = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            values.append(float(row[index]))
    return values

def mean(values):
    total = 0.0
    for v in values:
        total += v
    return total / len(values)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ▶️ **The script that uses them**

```python
path = Path("data") / "raw" / "D0_KPi.csv"
M = read_column(path, 0)
PT = read_column(path, 1)
print(len(M), "rows")
print(mean(M))
print(mean(PT))
```

```text
91583 rows
1864.1045817826146
3448.9281822936355
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The part that does the work is six lines and reads like the task. The second column costs one more line, not one more loop. Each function can be tested alone on a small case.

</div>

<!--
Speaker: this is the first half of the lecture in one slide: a path, the csv
module, a loop, two functions. Keep the two numbers on the board. The second
half gets them again with an array. (~3 min)
-->

---
layout: section
hideInToc: true
---

# From Lists to **Arrays**

<!--
Speaker: the loop works. The question of this section is what it costs, in
time and in memory, and what has to change to make it cheaper. (~1 min)
-->

---
hideInToc: true
---

# What the Loop **Costs**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⏱️ **Measured on 91 583 rows**

```python
import time

t0 = time.perf_counter()
total = mean(M)
t1 = time.perf_counter()
print((t1 - t0) * 1000, "ms")
```

- The sum by loop takes 1.6 ms. That is 17 ns for each row
- The built-in `sum(M)` takes 0.29 ms
- The mean and the standard deviation, two loops, take 6.7 ms

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **One step of `total += v`**

1. Take the next reference from the list
2. Follow it to the float object
3. Look up the types of `total` and `v` to find the right addition
4. Add the two numbers
5. Make a new float object for the result
6. Give it the name `total` and release the old object

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Only step 4 is arithmetic. A processor adds two floats in less than 1 ns. The other 16 ns are spent on finding out, 91 583 times, that the next value is a float once more.

</div>

<!--
Speaker: time.perf_counter() is a clock in seconds. A single measurement
scatters, so the numbers here are the median of 51 runs on one laptop. At
17 ns for each row, 100 million rows take 1.7 s for a single sum. (~3 min)
-->

---
hideInToc: true
---

# A List and an Array in **Memory**

<img class="fig" src="/figures/viz_arrays_list_vs_array.svg" style="display:block;margin:0.4rem auto 0;max-height:290px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📦 **The list `M`**

A float object is 24 bytes: its type, a counter and the value. The list keeps a reference of 8 bytes to each. For 91 583 numbers that is 2 930 712 bytes.

</div>

<div class="card card-primary card-glass pad-compact">

## 🧱 **The array `M`**

One type for all values, stored once. The values lie side by side, 8 bytes each: 732 664 bytes. That is a quarter of the list, and a loop over it has nothing to look up.

</div>

</div>

<!--
Speaker: sys.getsizeof(1880.649) is 24, and the list itself is 732 720 bytes
of references. The array is the idea of the binary file from Lecture 03: the
numbers themselves, in a row, with the type written once. (~3 min)
-->

---
hideInToc: true
---

# **NumPy**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **What it is**

- A library for arrays of numbers. It is not part of Python and is installed once
- Its type is the array, `ndarray`: values of one type in one block of memory
- Its loops are compiled code, not Python
- The scientific libraries of Python take arrays in and give arrays back

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **Install, import, first array**

```text
python -m pip install numpy
```

```python
import numpy as np

t10 = np.array([9.02, 11.05, 12.61])
print(t10)           # [ 9.02 11.05 12.61]
print(type(t10))     # <class 'numpy.ndarray'>
print(t10.sum())     # 32.68
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`pip` is the installer that comes with Python. It fetches the library from the Python Package Index, pypi.org. On macOS the command starts with `python3`. `np` is the name everyone gives the library on import.

</div>

---
hideInToc: true
---

# The Same Task with **NumPy**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **The file, the mean, the count**

```python
import numpy as np

data = np.loadtxt("data/raw/D0_KPi.csv",
                  delimiter=",", skiprows=1)
print(data.shape)

M = data[:, 0]
TAU = data[:, 2]
print(M.mean())
print((TAU != -100).sum())
```

```text
(91583, 4)
1864.1045817826453
91534
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Line by line**

- `np.loadtxt` reads the whole file into one array of 91 583 rows and 4 columns
- `data[:, 0]` is the first column
- `M.mean()` is the loop over 91 583 values, run in compiled code
- `TAU != -100` compares every value, and `.sum()` counts the `True`

Each of these is taken apart in the rest of the lecture.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The loop gave 1864.1045817826146. The two means differ from the 14th digit on. NumPy adds the values in another order, and every addition of floats rounds. A float64 holds 15 to 16 digits, so both are right to that precision.

</div>

---
hideInToc: true
---

# Measured: Loop Against **Array**

<img class="fig" src="/figures/viz_arrays_timing.svg" style="display:block;margin:0.4rem auto 0;max-height:330px;">

<div class="card card-info card-glass pad-compact mt-md">

Each task is run 51 times, reading the file 15 times, and the median is shown. Reading gains a factor 3.4: turning text into numbers is the work in both versions. Computing gains a factor 47 to 70. Apple M2 Pro, Python 3.13, NumPy 2.3.

</div>

<!--
Speaker: the axis is logarithmic, each grid line is ten times the one before.
Both versions are fast on 91 583 rows. The factor matters for a file a
thousand times larger, and for a computation that is repeated a thousand
times. (~3 min)
-->

---
hideInToc: true
---

# Try It — **Time Both**

```py {monaco-run} {autorun:false}
import time
import numpy as np

array = np.linspace(1800, 1900, 91583)
values = array.tolist()            # the same numbers as a list

t0 = time.perf_counter()
for repeat in range(20):
    total = 0.0
    for v in values:
        total += v
t1 = time.perf_counter()
for repeat in range(20):
    total = array.sum()
t2 = time.perf_counter()
print(f"loop  {(t1 - t0) / 20 * 1000:.3f} ms")
print(f"NumPy {(t2 - t1) / 20 * 1000:.3f} ms")
```

<div class="note-text mt-sm">The data file is not in the browser, so 91 583 numbers are made here. Each version runs 20 times.</div>

<!--
Speaker: run it twice and compare the two results: timings scatter. The
browser runs Python more slowly than the laptop does, and the factor between
the two lines stays large. (~3 min)
-->

---
layout: section
hideInToc: true
---

# `dtype` & **Shape**

<!--
Speaker: an array is described by two things: the type of its values and how
many there are along each direction. (~1 min)
-->

---
hideInToc: true
---

# One Type per Array: **`dtype`**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **The type is chosen once**

```python
a = np.array([1, 2, 3])
b = np.array([1, 2.5, 3])
print(a, a.dtype)             # [1 2 3] int64
print(b, b.dtype)             # [1.  2.5 3. ] float64
print(b.itemsize, b.nbytes)   # 8 24

a[0] = 7.9
print(a)                      # [7 2 3]
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📏 **The usual types**

| `dtype` | Bytes | Holds |
| --- | --- | --- |
| `int8` | 1 | −128 to 127 |
| `int32` | 4 | about ±2.1 × 10⁹ |
| `int64` | 8 | about ±9.2 × 10¹⁸ |
| `float32` | 4 | about 7 digits |
| `float64` | 8 | about 15 digits |
| `bool` | 1 | `True`, `False` |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

These are the integers of fixed width and the floats of Lecture 03. One float among the values makes the whole array `float64`. The type belongs to the array and not to a value: writing 7.9 into an integer array stores 7.

</div>

<!--
Speaker: np.loadtxt gave float64, the same type as a Python float. In the
browser the first line prints int32: the runner there is a 32-bit system with
an older NumPy. (~2 min)
-->

---
hideInToc: true
---

# Fixed Width: `int8` **Wraps Around**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 💥 **Three bytes, plus 10**

```python
x = np.array([100, 120, 127], dtype=np.int8)
print(x + 10)       # [ 110 -126 -119]
print(x.nbytes)     # 3
```

No error and no warning.

```python
n = np.array([30000, 30000], dtype=np.int16)
print(n + 5000)     # [-30536 -30536]
```

</div>

<div class="card card-primary card-glass pad-compact">

## ⚖️ **By the weights of Lecture 03**

```text
127 + 10 = 137 = 10001001 in binary

weights   -128  64  32  16   8   4   2   1
pattern      1   0   0   0   1   0   0   1

as int8   -128 + 8 + 1  =  -119
```

Eight bits hold 256 patterns. A result past 127 comes back as the result minus 256.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A Python `int` grows as needed: `2**100` is 1267650600228229401496703205376. An array trades that for speed and size. Keep `int64` and `float64`, the defaults, unless memory forces a smaller type, and then check the range of the values first.

</div>

---
hideInToc: true
---

# `float32` and `float64` on the **Data File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **The mass column in 32 bits**

```python
M32 = M.astype(np.float32)
print(M.nbytes, M32.nbytes)   # 732664 366332
print(float(M32[0]))          # 1880.6490478515625

print(f"{M.sum():.1f}")       # 170720289.9
print(f"{M32.sum():.1f}")     # 170720288.0

total = np.float32(0)
for m in M32:
    total += m
print(f"{total:.1f}")         # 170720880.0
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🎯 **Three sums of the same column**

| How | Sum | Error |
| --- | --- | --- |
| `float64` | 170 720 289.9 | |
| `float32`, `.sum()` | 170 720 288.0 | −1.9 |
| `float32`, running total | 170 720 880.0 | +590.1 |

Near 1.7 × 10⁸ the step from one `float32` to the next is 16. Towards the end of the loop, every mass of about 1864 that is added to the running total is rounded to a multiple of 16.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`.sum()` adds in pairs, so its partial sums stay small for longer and lose less. Store in `float32` when 7 digits are enough: the file takes half the memory. Compute sums in `float64`.

</div>

<!--
Speaker: Lecture 03 said that adding many small numbers to one large number
loses the small ones. Here it is on the data file: 590 MeV off in the sum, 6
keV off in the mean. (~3 min)
-->

---
hideInToc: true
---

# Try It — **Creating Arrays**

```py {monaco-run} {autorun:false}
import numpy as np

print(np.array([20, 30, 40]))
print(np.zeros(4))
print(np.arange(20, 101, 10))
print(np.linspace(1815, 1915, 5))
print(np.zeros((2, 3)))
```

<div class="card card-info card-glass pad-compact mt-md">

`np.array` takes a list. `np.zeros(n)` gives *n* zeros to be filled later. `np.arange(start, stop, step)` counts like `range` and leaves the stop out. `np.linspace(start, stop, n)` gives *n* values at equal distances and includes both ends. `np.zeros((2, 3))` has two rows and three columns.

</div>

<!--
Speaker: run it, then ask for the nine lengths of the pendulum table in
metres: np.arange(20, 101, 10) / 100, or np.linspace(0.2, 1.0, 9). (~3 min)
-->

---
hideInToc: true
---

# **Shape**: Rows and Columns

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **One and two dimensions**

```python
t10 = np.array([9.02, 11.05, 12.61])
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(t10.shape)                # (3,)
print(A.shape)                  # (2, 3)
print(A.ndim, A.size, len(A))   # 2 6 2
print(A.reshape(3, 2))
```

```text
[[1 2]
 [3 4]
 [5 6]]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Reading a shape**

- The shape is a tuple with one length for each dimension
- `(3,)` is one row of three values. `(2, 3)` is 2 rows and 3 columns: rows come first
- `size` is the number of values. `len` is the number of rows
- `reshape` keeps the values in their order and cuts them into rows anew. The size must stay: `A.reshape(4, 2)` raises `ValueError`
- `A.T` swaps rows and columns: shape `(3, 2)`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`data.shape` is `(91583, 4)`: 366 332 values of 8 bytes, 2 930 656 bytes in memory.

</div>

---
layout: section
hideInToc: true
---

# Indexing, Slicing & **Masks**

<!--
Speaker: three ways to take a part of an array: by position, by a range of
positions, and by a condition on the values. The third is the one data
analysis runs on. (~1 min)
-->

---
hideInToc: true
---

# Index and Slice, as in a **List**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **One dimension**

```python
t10 = np.array([9.02, 11.05, 12.61, 14.23, 15.49,
                16.84, 17.90, 19.10, 20.01])

print(t10[0], t10[-1])   # 9.02 20.01
print(t10[2:5])          # [12.61 14.23 15.49]
print(t10[::2])          # [ 9.02 12.61 15.49 17.9  20.01]
print(t10[[0, 3, 8]])    # [ 9.02 14.23 20.01]
```

The last line is new: a list of positions inside the brackets.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **A slice is a view**

```python
part = t10[1:3]
part[0] = 0.0
print(t10[:3])     # [ 9.02  0.   12.61]
```

- A slice of a list is a copy. A slice of an array is the same memory under another name
- That makes slicing free, also for 91 583 rows
- Writing into the slice changes the original. `t10[1:3].copy()` is an array of its own

</div>

</div>

---
hideInToc: true
---

# Two Dimensions: `data[row, column]`

<img class="fig" src="/figures/viz_arrays_indexing.svg" style="display:block;margin:0.4rem auto 0;max-height:215px;">

<div class="card card-primary card-glass pad-compact mt-md">

```python
print(data[1, 2])       # 0.0001864154
print(data[0])          # [1.8806490e+03 3.0009534e+03 4.1271152e-04 1.2991675e+03]
print(data[:, 0])       # [1880.649  1860.6599 1913.8755 ... 1871.8434 1871.4323 1911.2631]
print(data[1:3, :2])    # [[1860.6599 2803.4126]
                        #  [1913.8755 2542.169 ]]
```

</div>

<div class="note-text mt-sm">One index or slice for each dimension, with a comma between them. A <code>:</code> alone takes everything along that dimension. NumPy prints a long array with <code>...</code> in the middle and a row of mixed sizes in powers of ten. The values are not changed by that.</div>

<!--
Speaker: the figure shows the first five rows of data. Counting starts at 0,
and a slice leaves its end out, as in a list. (~2 min)
-->

---
hideInToc: true
---

# The Four **Columns**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **A name for each column**

```python
M = data[:, 0]        # mass, MeV/c^2
PT = data[:, 1]       # transverse momentum, MeV/c
TAU = data[:, 2]      # decay time, ns; -100 = missing
IPCHI2 = data[:, 3]   # chi^2 of the impact parameter

print(M.shape)        # (91583,)
print(TAU[:3])
```

```text
[0.00041271 0.00018642 0.00018465]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **What the array does not hold**

- An array has no column names. The header line was skipped
- The script holds the meaning: one line per column, with the unit in a comment
- Each column is a view of `data`. Nothing is copied
- `M, PT, TAU, IPCHI2 = data.T` does the same in one line: `data.T` has shape `(4, 91583)`, and the four names take its four rows

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The order of the columns is known only from the header of the file. Read line 1 of the file before writing these four lines.

</div>

---
hideInToc: true
---

# A Comparison Gives an Array of **Booleans**

<img class="fig" src="/figures/viz_arrays_mask.svg" style="display:block;margin:0.4rem auto 0;max-height:225px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

```python
mask = tau != -100
print(mask.dtype, mask.sum())   # bool 4
print(tau[mask])        # [0.41 0.19 0.57 0.29]
print(mass[mask])       # [1880.6 1860.7 1888.8 1862.5]
```

</div>

<div class="card card-secondary card-glass pad-compact">

- The comparison is made for every value. The result is an array of `True` and `False`: a **mask**
- In a sum `True` counts as 1, so `mask.sum()` is the number of `True`
- An array indexed with a mask gives the values where the mask is `True`

</div>

</div>

<!--
Speaker: the mask is made from one column and used on another. That works
because the columns are in step: position 2 of each belongs to the same row.
(~3 min)
-->

---
hideInToc: true
---

# A Mask **Selects Rows**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **On the file**

```python
mask = TAU != -100

print(mask.sum())          # 91534
print((~mask).sum())       # 49
print(TAU[mask].shape)     # (91534,)
print(M[mask].shape)       # (91534,)
print(data[mask].shape)    # (91534, 4)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Reading it**

- `~mask` turns every `True` into `False` and back: the 49 rows without a decay time
- `M[mask]` is the mass of the rows in which `TAU` is valid
- `data[mask]` keeps whole rows: all four columns of the 91 534
- The result of a mask is a copy, not a view. Its length depends on the values

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

These are questions 1 and 3, answered without a loop: 91 583 rows, 91 534 of them with a valid `TAU`. The numbers agree with the loop.

</div>

---
hideInToc: true
---

# What 49 Rows Do to a **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ✏️ **With and without the mask**

```python
print(TAU.mean())         # -0.05252210273908192
print(TAU[mask].mean())   # 0.000981802006321804
print(TAU.min())          # -100.0
```

The first is −52.5 ps. The second is +0.98 ps.

</div>

<div class="card card-primary card-glass pad-compact">

## 🧮 **Where −0.0525 comes from**

```text
sum of the 91 534 valid values      89.868
49 values of -100                -4900.000
sum of all 91 583 values         -4810.132

-4810.132 / 91 583  =  -0.0525 ns
   89.868 / 91 534  =   0.000982 ns
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

49 rows are 0.05 % of the file. They give the mean the wrong sign and make it 53 times too large. `-100` is not a measurement. It is a mark for "no value", and it has to be taken out before any number is computed from the column. The minimum shows it at once: no decay time is −100 ns.

</div>

<!--
Speaker: this is question 4. Ask the room for the answer before showing the
right-hand card: the mean of the valid values is 0.98 ps, about one
picosecond. Then ask what a histogram of the unmasked column would look like.
(~3 min)
-->

---
hideInToc: true
---

# Combining Masks: `&`, `|`, `~`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **A window around the peak**

```python
window = (M > 1840) & (M < 1890)

print(window.sum())            # 56577
print(window.mean())           # 0.6177674895995982
print((window & mask).sum())   # 56548
print((~window).sum())         # 35006
print(M[window].mean())        # 1864.7115145624548
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔀 **Three operators**

| Sign | Meaning | `True` where |
| --- | --- | --- |
| `&` | and | both are `True` |
| `\|` | or | at least one is `True` |
| `~` | not | the mask is `False` |

The brackets are needed: `&` is applied before `>` and `<`.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `and`, `or` and `not` work on single values. With arrays they raise `ValueError: The truth value of an array with more than one element is ambiguous`. The mean of a mask is the fraction of `True`: 61.8 % of the rows lie within 25 MeV/c² of 1865.

</div>

---
hideInToc: true
---

# Try It — **Masks**

```py {monaco-run} {autorun:false}
import numpy as np

mass = np.array([1880.6, 1860.7, 1913.9, 1888.8, 1862.5, 1845.2])
tau = np.array([0.41, 0.19, -100.0, 0.57, 0.29, -100.0])

mask = tau != -100
window = (mass > 1850) & (mass < 1890)
print(mask.sum(), window.sum())
print(mass[mask & window])
print(tau[mask].mean(), tau.mean())
```

<div class="card card-info card-glass pad-compact mt-md">

Six rows of the kind the file has. Predict the three lines before running. Then change the window so that it keeps `1845.2`, and count the rows that are inside the window and have no decay time.

</div>

<!--
Speaker: the output is 4 4, then [1880.6 1860.7 1888.8 1862.5], then 0.365
and -33.09. With (mass > 1840) the window keeps five values, and
(window & ~mask).sum() is 1. (~4 min)
-->

---
layout: section
hideInToc: true
---

# Arithmetic & **Broadcasting**

<!--
Speaker: an operator between arrays works on all their values at once. This
section is the rule for which shapes may meet in one operation. (~1 min)
-->

---
hideInToc: true
---

# Arithmetic on **Whole Arrays**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📋 **Lists**

```python
print([1, 2, 3] * 2)
print([1, 2, 3] + [10, 20, 30])
```

```text
[1, 2, 3, 1, 2, 3]
[1, 2, 3, 10, 20, 30]
```

For a list `*` repeats and `+` joins. `[1, 2, 3] / 10` raises `TypeError`.

</div>

<div class="card card-primary card-glass pad-compact">

## 🔢 **Arrays**

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a * 2)      # [2 4 6]
print(a + b)      # [11 22 33]
print(a * b)      # [10 40 90]
print(a / 10)     # [0.1 0.2 0.3]
print(a ** 2)     # [1 4 9]
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

An operator between arrays acts on each pair of values at the same position, and no loop is written. This is called **vectorised** arithmetic. A change of unit for a whole column is one line: `M / 1000` is the mass in GeV/c², and `TAU[mask] * 1000` is the decay time in ps.

</div>

---
hideInToc: true
---

# *g* from Nine Pendulums, **Without a Loop**

<div class="card card-primary card-glass pad-compact mt-md">

```python
length_cm = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100])
t10 = np.array([9.02, 11.05, 12.61, 14.23, 15.49, 16.84, 17.90, 19.10, 20.01])

T = t10 / 10                                    # one swing, s
g = 4 * np.pi**2 * (length_cm / 100) / T**2     # m/s^2

print(g.round(2))     # [9.7  9.7  9.93 9.75 9.87 9.74 9.86 9.74 9.86]
print(g.mean())       # 9.795148016389398
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧮 **The formula, once**

*T* = 2π√(*L*/*g*) solved for *g* is *g* = 4π²*L*/*T*². The line for `g` is that formula as it is written on paper. It runs on nine lengths and nine times at once.

</div>

<div class="card card-info card-glass pad-compact">

## ✅ **The result**

Nine values between 9.70 and 9.93 m/s², with a mean of 9.80. Each row of the table is one measurement of *g*.

</div>

</div>

<!--
Speaker: this is the pendulum table of week 2. Every operand is either an
array of nine values or a single number. The single numbers, 10, 100 and
4π², are used for all nine. That is the first case of broadcasting. (~3 min)
-->

---
hideInToc: true
---

# Functions on **Whole Arrays**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **`period`, with `np` in place of `math`**

```python
def period(length_m, g=9.81):
    return 2 * np.pi * np.sqrt(length_m / g)

predicted = 10 * period(length_cm / 100)
print(predicted.round(2))
print((t10 - predicted).round(2))
```

```text
[ 8.97 10.99 12.69 14.19 15.54 16.78 17.94 19.03 20.06]
[ 0.05  0.06 -0.08  0.04 -0.05  0.06 -0.04  0.07 -0.05]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **One function, both cases**

- `np.sqrt`, `np.exp`, `np.log`, `np.sin` and `np.abs` act on every value of an array, and on a single number too
- `math.sqrt(length_cm)` raises `TypeError: only length-1 arrays can be converted to Python scalars`
- The function from the start of the lecture now takes nine lengths and returns nine periods

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The second line of the output is measured minus predicted for each length. No difference is larger than 0.08 s in a time of 9 to 20 s.

</div>

---
hideInToc: true
---

# Two Shapes in One Operation: **Broadcasting**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **The rule**

1. Write the two shapes one under the other, aligned at the right
2. Compare the lengths column by column, from the right
3. Two lengths fit if they are equal, or if one of them is 1. A missing length counts as 1
4. Where a length is 1, that array is used again for every position of the other

If one pair does not fit, NumPy raises `ValueError`.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🧮 **Shapes that meet**

| First | Second | Result |
| --- | --- | --- |
| `(9,)` | a number | `(9,)` |
| `(2, 3)` | `(3,)` | `(2, 3)` |
| `(2, 3)` | `(2, 1)` | `(2, 3)` |
| `(2, 3)` | `(2,)` | error: 3 against 2 |
| `(91583, 4)` | `(4,)` | `(91583, 4)` |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`t10 / 10` was the first row of the table: nine values and one number. Nothing is copied in memory. The compiled loop reads the same value again.

</div>

---
hideInToc: true
---

# Broadcasting: a Worked **2-by-3** Example

<img class="fig" src="/figures/viz_arrays_broadcasting.svg" style="display:block;margin:0.3rem auto 0;max-height:240px;">

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
row = np.array([10, 20, 30])       # (3,)
col = np.array([[100], [200]])     # (2, 1)
print(A + row)
print(A + col)
```

</div>

<div class="card card-warning card-glass pad-compact">

```python
two = np.array([100, 200])         # (2,)
print(A + two)
```

`ValueError: operands could not be broadcast together with shapes (2,3) (2,)`

From the right, 3 stands against 2. `two.reshape(2, 1)` is the column, and it fits.

</div>

</div>

<!--
Speaker: work the two additions on the board before showing the figure. The
outputs are [[11 22 33] [14 25 36]] and [[101 102 103] [204 205 206]]. The
dashed cells are not in memory. (~4 min)
-->

---
hideInToc: true
---

# `axis`: Down the Rows or Along Them

<div class="grid-2 mt-md gap-md">

<div>

<img class="fig" src="/figures/viz_arrays_axis.svg" style="display:block;margin:0 auto;max-height:190px;">

<div class="card card-info card-glass pad-compact mt-md">

`axis` names the dimension that is added up and disappears. `axis=0` adds along the rows, and one number for each column is left: shape `(2, 3)` becomes `(3,)`.

</div>

</div>

<div class="card card-primary card-glass pad-compact">

## ✏️ **On `A` and on the file**

```python
print(A.sum())          # 21
print(A.sum(axis=0))    # [5 7 9]
print(A.sum(axis=1))    # [ 6 15]
print(A.mean(axis=0))   # [2.5 3.5 4.5]

print(data.mean(axis=0))
```

```text
[ 1.86410458e+03  3.44892818e+03
 -5.25221027e-02  4.57513042e+02]
```

The four numbers are the means of `M`, `PT`, `TAU` and `IPCHI2` over all 91 583 rows. The third is the −0.0525 from before.

</div>

</div>

---
layout: section
hideInToc: true
---

# Summary Numbers & the **Histogram**

<!--
Speaker: a column of 91 583 values is described by a few numbers, and then by
counts in intervals. Both are computed here. Drawing them is a separate step.
(~1 min)
-->

---
hideInToc: true
---

# Mean and **Standard Deviation**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **By hand, on eight values**

```text
x              2   4   4   4   5   5   7   9
mean           40 / 8 = 5
x - mean      -3  -1  -1  -1   0   0   2   4
squared        9   1   1   1   0   0   4  16
their mean     32 / 8 = 4
square root    2
```

The mean is 5. The standard deviation is 2: the typical distance of a value from the mean.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **The same steps as array code**

```python
x = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print(x.mean())                                  # 5.0
print(np.sqrt(((x - x.mean()) ** 2).mean()))     # 2.0
print(x.std())                                   # 2.0

print(M.mean())    # 1864.1045817826453
print(M.std())     # 25.564956548991027
print(M.min(), M.max())    # 1766.2096 2453.6584
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`x - x.mean()` is eight values minus one number, `** 2` squares each, `.mean()` averages, `np.sqrt` takes the root. `std` divides by the number of values. `x.std(ddof=1)` divides by one less and gives 2.14.

</div>

<!--
Speaker: the standard deviation is defined here by its steps and used as a
measure of width. The mass column has a mean of 1864.10 and a standard
deviation of 25.56 MeV/c². (~3 min)
-->

---
hideInToc: true
---

# The Four Columns in **Numbers**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Rows with a valid `TAU`**

```python
good = data[mask]            # (91534, 4)

print(good.mean(axis=0))
print(good.std(axis=0))
print(good.min(axis=0))
print(good.max(axis=0))
print(np.median(good, axis=0))
```

Each line prints four numbers, one for each column. The median is the value in the middle when the column is sorted.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📊 **The output as a table**

| | `M` | `PT` | `TAU` | `IPCHI2` |
| --- | --- | --- | --- | --- |
| mean | 1864.10 | 3447.60 | 0.00098 | 436.4 |
| std | 25.56 | 1282.96 | 0.00438 | 6230.8 |
| min | 1766.21 | 755.27 | −0.1372 | 0.0000136 |
| max | 2453.66 | 57 514.80 | 0.5788 | 891 711.1 |
| median | 1864.08 | 3048.76 | 0.00027 | 6.29 |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ For `M` the mean and the median agree, and the standard deviation says how wide the column is. For `IPCHI2` the mean is 436 and the median is 6.29: a few very large values carry the mean. Read the minimum, the maximum and the median before trusting a mean.

</div>

---
hideInToc: true
---

# Broadcasting on the File: **Centre and Scale**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Every column at once**

```python
mean = good.mean(axis=0)       # (4,)
std = good.std(axis=0)         # (4,)
z = (good - mean) / std        # (91534, 4)

print(z[0].round(3))
print(z.mean(axis=0).round(6))
print(z.std(axis=0))
print(z.max(axis=0).round(2))
```

```text
[ 0.647 -0.348 -0.13   0.138]
[ 0.  0. -0.  0.]
[1. 1. 1. 1.]
[ 23.06  42.14 131.86 143.04]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Reading it**

- `(91534, 4)` minus `(4,)`: from the right, 4 fits 4. Each column gets its own mean subtracted and is divided by its own standard deviation
- `z` says how many standard deviations a value lies from the mean of its column. The first row has a mass 0.647 standard deviations above the mean
- Every column of `z` has mean 0 and standard deviation 1, whatever its unit was
- The largest mass, 2453.66, lies 23 standard deviations above the mean

</div>

</div>

<div class="note-text mt-sm">The <code>-0.</code> is a zero that was rounded from a small negative number.</div>

---
hideInToc: true
---

# `np.loadtxt` in **Full**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🧩 **The arguments**

| Argument | Meaning |
| --- | --- |
| `delimiter=","` | The sign between the values. The default is empty space |
| `skiprows=1` | Lines to leave out at the top: the header |
| `usecols=(0, 2)` | Read these columns only |
| `unpack=True` | Give one array per column |
| `dtype=np.float32` | The type of the array. The default is `float64` |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **Two columns, two arrays**

```python
M, TAU = np.loadtxt(
    "data/raw/D0_KPi.csv", delimiter=",",
    skiprows=1, usecols=(0, 2), unpack=True)
print(M.shape, TAU.shape)
# (91583,) (91583,)
```

Without `skiprows`:

`ValueError: could not convert string 'M' to float64 at row 0, column 1.`

Without `delimiter`, the whole line is taken as one value and the same error names it.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`np.loadtxt` reads a file in which every field is a number. A header is skipped, not read. One field that is not a number stops it with the row and the column in the message. The `csv` module and `try` are the tools for a file with such fields.

</div>

---
hideInToc: true
---

# An Array on Disk: **Text or Binary**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Save and load**

```python
np.save("data/processed/D0_KPi.npy", data)
back = np.load("data/processed/D0_KPi.npy")

print(back.shape, back.dtype)       # (91583, 4) float64
print(np.array_equal(back, data))   # True
```

`np.save` writes the bytes of the array with a header that holds the `dtype` and the shape. `np.savetxt(name, data, delimiter=",")` writes text.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ⚖️ **The same table, two files**

| | `D0_KPi.csv` | `D0_KPi.npy` |
| --- | --- | --- |
| Bytes | 3 926 142 | 2 930 784 |
| Time to read | 18 ms | 0.25 ms |
| Opens in an editor | yes | no |
| Read by | any program | NumPy |

2 930 784 is 366 332 values of 8 bytes and a header of 128 bytes.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Reading the binary file is 70 times faster, because no text is turned into numbers. The CSV file stays in `data/raw/` as the original. The `.npy` file is made from it by a script and belongs in `data/processed/`: it can be deleted and made again.

</div>

<!--
Speaker: this is the slide "One Number, Two Files" of Lecture 03 at the scale
of the whole table. As float32 the .npy file has 1 465 456 bytes. (~2 min)
-->

---
hideInToc: true
---

# `np.histogram`: Counting in **Bins**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **Nine values, three bins**

```python
x = np.array([1.2, 1.9, 2.1, 2.5, 2.7,
              3.3, 3.8, 3.9, 4.0])
counts, edges = np.histogram(x, bins=3, range=(1, 4))
print(counts)    # [2 3 4]
print(edges)     # [1. 2. 3. 4.]
```

```text
bin 0   from 1 to 2    1.2 1.9            2
bin 1   from 2 to 3    2.1 2.5 2.7        3
bin 2   from 3 to 4    3.3 3.8 3.9 4.0    4
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **What comes back**

- The range is cut into `bins` intervals of equal width. Their borders are the `edges`
- `counts[i]` is the number of values from `edges[i]` up to `edges[i + 1]`
- Three bins have four edges: `len(edges)` is `len(counts) + 1`
- A value on an edge goes to the bin on its right. The last bin takes its right edge too: `4.0` is counted
- A value outside the range is not counted at all

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The function returns two arrays, and the two names on the left take them. No picture is made. The counts are numbers to compute with.

</div>

---
hideInToc: true
---

# The Mass Column in **20 Bins**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Bins of 5 MeV/c²**

```python
counts, edges = np.histogram(
    M, bins=20, range=(1815, 1915))
print(counts)
print(edges[:4])
print(counts.sum(), len(M) - counts.sum())
i = counts.argmax()
print(i, edges[i], edges[i + 1], counts[i])
```

```text
[3500 3622 3623 3643 3741 3722 4224 5083
 7124 8931 8565 6512 4876 3938 3602 3378
 3412 3397 3287 3064]
[1815. 1820. 1825. 1830.]
91244 339
9 1860.0 1865.0 8931
```

</div>

<div>

<img class="fig" src="/figures/viz_arrays_histogram.svg" style="display:block;margin:0 auto;max-height:250px;">

<div class="card card-secondary card-glass pad-compact mt-md">

- 91 244 rows are counted. 339 lie outside the range
- `argmax` is the position of the largest count: bin 9, from 1860 to 1865, with 8931 rows
- Far from the peak a bin holds about 3500 rows
- The figure is these 20 numbers drawn as bars

</div>

</div>

</div>

<!--
Speaker: the peak is the D⁰ meson at 1865 MeV/c². It was invisible in the
mean and the standard deviation and it is plain in 20 counts. The counts and
the edges are all that a drawing needs. (~3 min)
-->

---
hideInToc: true
---

# The Whole Analysis in One **Script**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 `scripts/summary.py`

```python
import numpy as np

data = np.loadtxt("data/raw/D0_KPi.csv",
                  delimiter=",", skiprows=1)
M = data[:, 0]
TAU = data[:, 2]
mask = TAU != -100
tau_ps = TAU[mask] * 1000

print("rows:", len(data), " valid TAU:", mask.sum())
print(f"M    mean {M.mean():.2f}  std {M.std():.2f}")
print(f"TAU  mean {tau_ps.mean():.3f}  std {tau_ps.std():.3f}")

counts, edges = np.histogram(M, bins=20, range=(1815, 1915))
i = counts.argmax()
print("fullest bin:", edges[i], "to", edges[i + 1])
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ▶️ **Its output**

```text
rows: 91583  valid TAU: 91534
M    mean 1864.10  std 25.56
TAU  mean 0.982  std 4.382
fullest bin: 1860.0 to 1865.0
```

- Thirteen lines of code, no loop. The script runs in about a tenth of a second
- The mask is applied to `TAU` only. The mass is valid in all 91 583 rows
- The units, MeV/c² and ps, belong next to these numbers wherever they are reported

</div>

</div>

<!--
Speaker: the four questions from the start are the first three lines of the
output. The script reads the raw file and changes nothing in it. Run again,
it prints the same four lines. (~2 min)
-->

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Write a **function** that takes values in through parameters and gives one back with `return`

</div>

<div class="card card-success card-glass pad-compact">

✅ Catch a named **exception** with `try` and `except`, count the rows that were skipped

</div>

<div class="card card-success card-glass pad-compact">

✅ Build a path with **pathlib** and read a CSV file with **csv.reader** into lists

</div>

<div class="card card-success card-glass pad-compact">

✅ Read the file with **np.loadtxt** and state the `dtype` and the `shape` of the array

</div>

<div class="card card-success card-glass pad-compact">

✅ Select with an index, a slice and a **mask**, and combine masks with `&`, `|`, `~`

</div>

<div class="card card-success card-glass pad-compact">

✅ Compute on whole arrays, with **broadcasting** and `axis`, and count in bins with **np.histogram**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Before computing with a column**

Print its `shape`, its `dtype`, its minimum and its maximum. Count the values that mark "missing" and mask them. Then take the mean.

</div>

<!--
Speaker: the loop took 6.7 ms for a mean and a standard deviation and the
array 0.14 ms. The 49 rows changed the sign of a mean. Those are the two
numbers to remember. (~1 min)
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
  question="A function is defined as `def double(x): x * 2`. What does `print(double(4))` print?"
  :options="[
    '8',
    'None',
    'Nothing: the call raises a TypeError',
    '4'
  ]"
  :correct="1"
  explanation="The body computes 8 and does nothing with it. Without return the call gives back None, and print shows None. With return x * 2 it prints 8."
/>

---
hideInToc: true
---

<MCQ
  question="`rows = ['3.5', 'x', '', '7']`. A loop adds `float(r)` to `total` inside `try`, and `except ValueError` adds 1 to `skipped`. What are `total` and `skipped` at the end?"
  :options="[
    '10.5 and 2',
    '3.5 and 3',
    '10.5 and 1',
    'The program stops at the second row'
  ]"
  :correct="0"
  explanation="float('x') and float('') both raise ValueError, so two rows are skipped. '3.5' and '7' convert, and 3.5 + 7.0 is 10.5. An empty string is not a number."
/>

---
hideInToc: true
---

<MCQ
  question="What does `np.array([200], dtype=np.uint8) + 100` give?"
  :options="[
    '[300]',
    '[44]',
    '[255]',
    'An OverflowError'
  ]"
  :correct="1"
  explanation="A uint8 holds 0 to 255 in one byte. 300 is 100101100 in binary and needs nine bits. The top bit does not fit, and the eight bits that stay are 00101100, which is 44, or 300 − 256. There is no error and no warning."
/>

---
hideInToc: true
---

<MCQ
  question="`x = np.array([3, 8, -1, 5, -1, 9])`, and `-1` marks a missing value. What is `x[x != -1].mean()`?"
  :options="[
    '3.83',
    '6.25',
    '4.0',
    '25'
  ]"
  :correct="1"
  explanation="The mask keeps 3, 8, 5 and 9. Their sum is 25 and there are four of them: 6.25. Without the mask the mean is 23 / 6 = 3.83, because the two marks are added as if they were measurements."
/>

---
hideInToc: true
---

<MCQ
  question="The array `a` has shape `(4, 3)`. Which of these cannot be added to it?"
  :options="[
    'An array of shape <code>(3,)</code>',
    'An array of shape <code>(4, 1)</code>',
    'An array of shape <code>(4,)</code>',
    'A single number'
  ]"
  :correct="2"
  explanation="Shapes are compared from the right. (4, 3) against (4,) compares 3 with 4: they are not equal and neither is 1, so NumPy raises ValueError. (3,) fits and is used for every row. (4, 1) fits and is used for every column. A number fits every shape."
/>

---
hideInToc: true
---

<MCQ
  question="What are the counts of `np.histogram([0.5, 1.5, 1.7, 2.0, 3.0], bins=3, range=(0, 3))`?"
  :options="[
    '[1 2 2]',
    '[1 3 1]',
    '[1 2 1]',
    '[2 2 1]'
  ]"
  :correct="0"
  explanation="The edges are 0, 1, 2 and 3. A value on an edge goes to the bin on its right, so 2.0 is in the third bin. The last bin takes its right edge too, so 3.0 is counted there: 1, 2, 2."
/>
