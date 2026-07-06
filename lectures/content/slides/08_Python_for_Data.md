---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Python for Data Work"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python for Data Work

##### <span class="aims-badge">📁 data & files · 🔧 tool-agnostic</span>

<!--
Speaker: they can already write Python from Lecture 7 — today turns that into real
data work: functions, files, and the right library. Frame it as the bridge. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# You can write Python — now put it to work on data: organise code into functions, read and write files, and reach for the right library. The language stays the same; the leverage grows.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

⚙️ Organise code into reusable **functions** with docstrings

</div>

<div class="card card-secondary card-glass pad-compact">

🛡️ Handle errors safely with **try / except / finally**

</div>

<div class="card card-accent card-glass pad-compact">

🔁 Loop cleanly using **enumerate()** and **zip()**

</div>

<div class="card card-success card-glass pad-compact">

📂 Read and write **files** — loading CSV / JSON / YAML into dicts

</div>

<div class="card card-warning card-glass pad-compact">

📦 Import **modules** and reach for the right library

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Seminar 8 is where they build the
ingest script every later analysis step depends on. Set the expectation. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Functions & **Exceptions**

<!--
Speaker: this block is the "reusable and robust" beat — functions to organise code,
exceptions to survive bad input. Both bite the moment the data is real. (~1 min)
-->

---
hideInToc: true
---

# Functions & Exceptions

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-info card-glass pad-tight">

#### ⚙️ **Functions**

```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```

- Functions help organize code into reusable blocks
- Use `return` to return a value from a function

</div>

</div>

<div>

<div class="card card-warning card-glass pad-tight">

#### 🛡️ **Exception Handling**

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")
```

- Use `try` and `except` to handle errors
- `finally` block always executes

</div>

</div>

</div>

---
hideInToc: true
---

# Try It — Writing Functions

```py {monaco-run}
def describe_data(values):
    """Calculate basic statistics for a list of numbers."""
    n = len(values)
    mean = sum(values) / n
    sorted_vals = sorted(values)
    median = sorted_vals[n // 2] if n % 2 else (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2
    data_range = max(values) - min(values)
    return {"n": n, "mean": mean, "median": median, "range": data_range}

# Test it
temperatures = [22.1, 23.5, 21.8, 24.2, 22.9, 23.1, 25.0, 22.4]
stats = describe_data(temperatures)
for key, value in stats.items():
    print(f"  {key}: {value:.2f}" if isinstance(value, float) else f"  {key}: {value}")
```

*The `"""..."""` line is a **docstring** — it documents what the function does and shows up in `help()`.*

---
hideInToc: true
---

# Common Python Errors

<div class="grid-3 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

## 🐛 **Syntax & Indentation**

```python
if True:
print("oops")  # missing indent!
```

- Whitespace defines structure
- Every block needs **indentation**

</div>

<div class="card card-warning card-glass pad-tight">

## 🐛 **Name & Type Errors**

```python
print(undefined_variable)  # NameError
"hello" + 42                # TypeError
```

- Check **spelling** and **types**

</div>

<div class="card card-warning card-glass pad-tight">

## 🐛 **Value Errors**

```python
float("N/A")  # ValueError!
```

- A malformed CSV field — exactly what Seminar 8's ingest script must catch with `try` / `except ValueError`

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 💡 **Debugging Tip**

Read the error message **bottom to top** — the last line tells you what went wrong, the lines above show where.

</div>

---
hideInToc: true
---

<MCQ
  question="Why is a bare `except:` (no exception type) considered bad practice compared to `except ValueError:`?"
  :options="[
    'It catches everything — typos, Ctrl+C, exit calls — silently hiding real bugs',
    'It runs noticeably slower than a typed except clause',
    'Modern Python no longer allows a bare except',
    'It only works inside a function, never at module level'
  ]"
  :correct="0"
  explanation="A bare except: swallows every exception — a NameError from a typo, KeyboardInterrupt, SystemExit — not just the one you anticipated. That hides real bugs behind a silent pass. Always catch the specific exception(s) you expect, e.g. except ValueError:, so anything unexpected still surfaces and gets fixed."
/>

---
layout: section
hideInToc: true
---

# Advanced **Patterns**

<!--
Speaker: enumerate and zip are the idioms that separate clean Python from index-
juggling loops — worth pausing on the before/after. (~1 min)
-->

---
hideInToc: true
---

# Useful Built-in Patterns

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 🔢 **`enumerate()` — Loop with Index**

```python
detectors = ["ATLAS", "CMS", "ALICE", "LHCb"]

for i, name in enumerate(detectors):
    print(f"{i}: {name}")
# 0: ATLAS
# 1: CMS
# 2: ALICE
# 3: LHCb
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 🔗 **`zip()` — Loop over Multiple Lists**

```python
names    = ["electron", "muon",  "tau"]
masses   = [0.511,      105.66,  1776.9]

for name, mass in zip(names, masses):
    print(f"{name}: {mass} MeV")
# electron: 0.511 MeV
# muon: 105.66 MeV
# tau: 1776.9 MeV
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **Tip**

- `enumerate()` replaces the `for i in range(len(...)):` anti-pattern
- `zip()` stops at the shortest list

</div>

---
hideInToc: true
---

# Try It — enumerate & zip

```py {monaco-run}
# Particle data from the Standard Model
particles = ["electron", "muon", "tau", "proton", "neutron"]
masses_MeV = [0.511, 105.66, 1776.9, 938.3, 939.6]
charges = [-1, -1, -1, +1, 0]

print("Particle Catalog:")
print("-" * 45)
for i, (name, mass, charge) in enumerate(zip(particles, masses_MeV, charges)):
    if charge > 0:
        sign = "+"
    elif charge < 0:
        sign = ""
    else:
        sign = " "
    print(f"  {i+1}. {name:10s}  mass={mass:8.2f} MeV  charge={sign}{charge}")
```

---
layout: section
hideInToc: true
---

# Files & **Modules**

<!--
Speaker: the payoff section — getting data off disk and into Python. with open()
and the CSV/JSON/YAML loaders are exactly what Seminar 8 needs. (~1 min)
-->

---
hideInToc: true
---

# Modules, Imports & File Handling

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

#### 📦 **Modules and Imports**

```python
import math
print(math.sqrt(16))  # 4.0

from random import randint
print(randint(1, 10))  # Random number between 1 and 10
```

- Use `import` to bring in external modules
- `from module import function` imports specific functions

</div>

</div>

<div>

<div class="card card-secondary card-glass pad-tight">

#### 📂 **File Handling**

```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```

- Use `with open()` to handle file operations safely
- `"r"` for reading, `"w"` for writing, `"a"` for appending

</div>

</div>

</div>

---
hideInToc: true
---

# Loading Structured Files into Dicts

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-compact">

#### 📄 JSON

```python
import json
with open("data/raw/lhcb_d0_kpi.meta.json") as f:
    meta = json.load(f)  # column units, DOI, licence
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

#### 📝 YAML

```python
import yaml  # pip install pyyaml
with open("environment.yml") as f:
    env = yaml.safe_load(f)  # pinned deps (Lecture 14)
```

</div>

</div>

<div>

<div class="card card-info card-glass pad-compact">

#### 📊 CSV

```python
import csv
with open("data/raw/lhcb_d0_kpi.csv", newline="") as f:
    rows = list(csv.DictReader(f))
# each row: {'Event': ..., 'H1_PX': ..., 'H2_PX': ..., ...}
```

</div>

<div class="card card-accent card-glass pad-compact mt-sm">

#### 📈 Excel

```python
import pandas as pd  # pip install pandas openpyxl
df   = pd.read_excel("data.xlsx", sheet_name=0)
rows = df.to_dict(orient="records")
```

*A **DataFrame** is pandas' table type (like a spreadsheet); `.to_dict(orient="records")` turns each row into a dict so we can loop over it.*

</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Hands-On **Practice**

<!--
Speaker: live-run the Monaco cells here — dict comprehensions and a text bar chart
tie the whole lecture together before they write a real script. (~2 min)
-->

---
hideInToc: true
---

# Mini Project: Analyse Experiment Data

```py {monaco-run}
# Simulated hit rates from 3 muon-detector chambers
data = {
    "chamber_A": [22.1, 22.4, 22.3, 22.8, 22.5],
    "chamber_B": [23.5, 23.1, 23.8, 23.2, 23.6],
    "chamber_C": [21.9, 22.0, 21.7, 22.1, 21.8],
}

for chamber, readings in data.items():
    avg = sum(readings) / len(readings)
    spread = max(readings) - min(readings)
    print(f"{chamber}: avg={avg:.2f} Hz  spread={spread:.1f} Hz")

# A dict comprehension — same idea as a list comprehension, but it
# produces key: value pairs instead of a plain list.
averages = {c: sum(r)/len(r) for c, r in data.items()}
# key= tells max/min/sorted which value to compare by.
busiest = max(averages, key=averages.get)
print(f"\nBusiest: {busiest} ({averages[busiest]:.2f} Hz)")
```

---
hideInToc: true
---

# Mini Project: Visualise the Results

```py {monaco-run}
# Simple text-based "bar chart" — no matplotlib needed!
data = {
    "chamber_A": [22.1, 22.4, 22.3, 22.8, 22.5],
    "chamber_B": [23.5, 23.1, 23.8, 23.2, 23.6],
    "chamber_C": [21.9, 22.0, 21.7, 22.1, 21.8],
}

averages = {c: sum(r)/len(r) for c, r in data.items()}
min_avg = min(averages.values())

print("Average Hit Rate by Chamber")
print("=" * 40)
for chamber, avg in averages.items():
    bar_length = int((avg - 20) * 10)  # scale for display
    bar = "█" * bar_length
    print(f"{chamber}: {bar} {avg:.2f} Hz")
print("\nNext up: NumPy and matplotlib will make this MUCH easier!")
```

---
hideInToc: true
---

# Time to Write Real Python

The in-browser exercises were great for learning — now let's create an actual Python script you can run, share, and version-control.

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

**1.** In VS Code: `File → New File` → save as `muon_analysis.py`

</div>

<div class="card card-secondary card-glass pad-compact">

**2.** Copy your mini-project code in (or rewrite it from memory!)

</div>

<div class="card card-accent card-glass pad-compact">

**3.** Open the terminal (`` Ctrl+` ``) and run:

```bash
python muon_analysis.py
```

</div>

<div class="card card-success card-glass pad-compact">

**4.** Same output — but now it lives as a file on your machine, not just in a browser tab

</div>

</div>

---
hideInToc: true
---

# Version-Control Your Work

<div class="card card-success card-glass pad-tight mt-md">

## 🔄 **Save Your Progress with Git**

**Recall from Lecture 6:** commit after each working milestone — your future self will thank you.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

```bash
git add muon_analysis.py
git commit -m "Add muon detector hit-rate analysis script"
```

</div>

</div>

---
hideInToc: true
---

# What's Next?

You can now write Python. The upcoming data-analysis lectures build on it with three workhorse libraries:

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🔢 **NumPy**

Fast arrays and math on whole datasets at once.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐼 **pandas**

DataFrames — labelled tables for real, messy data.

</div>

<div class="card card-accent card-glass pad-tight">

## 📈 **Matplotlib**

Turning numbers into plots you can reason about.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md" style="text-align: center;">

Together these handle the bulk of everyday data-analysis work.

</div>

---
hideInToc: true
---

<MCQ
  question="Why is a `with open(...) as f:` block preferred over calling `open()` and assigning the result on its own?"
  :options="[
    'It closes the file automatically, even if an error is raised',
    'It reads the file faster than open() alone',
    'It converts the file into a dictionary for you',
    'It is the only way to import the csv module'
  ]"
  :correct="0"
  explanation="with is a context manager: it guarantees the file is closed when the block ends, even if an exception occurs — so you never leak an open file handle."
/>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Write reusable **functions** and guard code with **try / except**

</div>

<div class="card card-success card-glass pad-compact">

✅ Loop cleanly with **enumerate()** and **zip()**

</div>

<div class="card card-success card-glass pad-compact">

✅ Read and write **files** with `with open()`

</div>

<div class="card card-success card-glass pad-compact">

✅ Load **CSV / JSON / YAML** into Python dicts

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 8 tie-in**

build an ingest script that reads the whole CSV into Python (no Pandas yet) — the foundation every later step builds on.

</div>

<!--
Speaker: this is the "you can now" beat — have them nod along to each card. The
seminar tie-in makes it concrete: their ingest script is the base every later
analysis step builds on. (~1 min)
-->
