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

⚙️ Organise code into reusable **functions** with docstrings and light **type hints**

</div>

<div class="card card-secondary card-glass pad-compact">

🛡️ Handle errors with **try / except** and loop cleanly with **enumerate() / zip()**

</div>

<div class="card card-accent card-glass pad-compact">

📁 Work with paths portably using **pathlib** — glob data folders, no hard-coded paths

</div>

<div class="card card-success card-glass pad-compact">

📂 Read and write **data formats** — CSV / JSON / YAML round-trips into dicts

</div>

<div class="card card-warning card-glass pad-compact">

📦 Split a project into **modules** — `src/`, `scripts/`, and the `__main__` guard

</div>

<div class="card card-info card-glass pad-compact">

⌨️ Turn a script into a re-runnable **CLI tool** with argparse and exit codes

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

```py {monaco-run} {autorun:false}
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

```py {monaco-run} {autorun:false}
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

# Paths & File **Organisation**

<!--
Speaker: the invisible skill that makes an analysis reproducible — addressing files
so the code runs on any machine, not just the laptop it was written on. (~1 min)
-->

---
hideInToc: true
---

# Stop Passing Paths as Strings

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

#### 🧵 **Strings are fragile**

```python
folder = "data/raw"
path = folder + "/" + name   # slash by hand
```

- One missing (or doubled) slash breaks it
- Windows uses `\`, Unix uses `/`
- No easy way to get the name or extension

</div>

<div class="card card-primary card-glass pad-tight">

#### 📁 **`Path` objects**

```python
from pathlib import Path
raw = Path("data") / "raw"
f = raw / "lhcb_d0_kpi.csv"
print(f.suffix)   # .csv
```

- The `/` operator joins parts correctly
- Same code on every operating system

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **One import, everywhere**

`from pathlib import Path` is the modern default — reach for it instead of raw strings whenever you touch the filesystem.

</div>

---
hideInToc: true
---

# Try It — Paths with `pathlib`

```py {monaco-run} {autorun:false}
from pathlib import Path

# The / operator joins path parts — no manual slashes needed
data_file = Path("data") / "raw" / "lhcb_d0_kpi.csv"

print("full path :", data_file)
print("name      :", data_file.name)    # lhcb_d0_kpi.csv
print("stem      :", data_file.stem)    # lhcb_d0_kpi
print("suffix    :", data_file.suffix)  # .csv
print("parent    :", data_file.parent)  # data/raw

# Build an OUTPUT path next to the input, changing the extension
out = data_file.with_suffix(".json")
print("output    :", out)               # data/raw/lhcb_d0_kpi.json
```

*`Path` gives you the pieces of a filename by name — no string slicing.*

---
hideInToc: true
---

# Finding Files with `glob`

<div class="card card-primary card-glass pad-tight mt-md">

## 🔎 **Ask the folder what's in it**

```python
from pathlib import Path

raw = Path("data/raw")
for path in sorted(raw.glob("*.csv")):
    print(path.name)
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

- `glob("*.csv")` — every CSV in **one** folder
- `glob("**/*.csv")` — every CSV in the **whole tree**

</div>

<div class="card card-accent card-glass pad-compact">

- Each result is a `Path`, ready to `open()`
- `sorted()` makes the order reproducible

</div>

</div>

---
hideInToc: true
---

# Try It — Glob a Data Folder

```py {monaco-run} {autorun:false}
from pathlib import Path

# Set up a fake data folder with three files (normally already on disk)
raw = Path("data/raw")
raw.mkdir(parents=True, exist_ok=True)
for name in ["chamber_A.csv", "chamber_B.csv", "notes.txt"]:
    (raw / name).write_text("...")

# Ask the folder for just its CSV files — sorted, so the order is repeatable
for path in sorted(raw.glob("*.csv")):
    print(path.name, "-> stem:", path.stem)

print("total CSVs:", len(list(raw.glob("*.csv"))))
```

*This is how a script finds every run file to process without you listing them by hand.*

---
hideInToc: true
---

# Hard-Coded Paths Kill Reproducibility ♻️

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

#### ❌ **Only works on one laptop**

```python
path = "/home/maria/thesis/data/d0.csv"
```

- Breaks on every other machine
- Breaks when you rename a folder
- A reviewer who clones your repo can't run it

</div>

<div class="card card-success card-glass pad-tight">

#### ✅ **Relative to the project**

```python
ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "data" / "raw" / "d0.csv"
```

- Works for anyone who clones the repo
- The repo is the single source of truth

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **Rule**

No absolute paths in code. Anchor to the repo root and build everything from there.

</div>

---
hideInToc: true
---

# Try It — Making Output Folders

```py {monaco-run} {autorun:false}
from pathlib import Path

# Create the results folder — no error if it already exists
out_dir = Path("results")
out_dir.mkdir(parents=True, exist_ok=True)

# pathlib does quick whole-file I/O without open() boilerplate
summary = out_dir / "d0_summary.txt"
summary.write_text("sample: LHCb D0 -> K- pi+\nevents: 12345\n")

print("wrote:", summary)
print("---")
print(summary.read_text())   # read it straight back
```

*`mkdir(exist_ok=True)` is safe to re-run — a small thing that makes a script repeatable.*

---
layout: section
hideInToc: true
---

# Working with **Data Formats**

<!--
Speaker: text on disk is dumb — structure lives in the format you choose. The one
idea: pick the format that matches the shape of the data, don't fight it. (~1 min)
-->

---
hideInToc: true
---

# Text, Bytes & the Right Format

<div class="grid-3 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

#### 📄 **Plain text**

Logs, notes, a README. Human-readable, but no structure to parse back out.

</div>

<div class="card card-primary card-glass pad-compact">

#### 🔢 **CSV**

Rows and columns — one flat table. Opens in Excel. The lab default for measurements.

</div>

<div class="card card-secondary card-glass pad-compact">

#### 🌳 **JSON**

Nested keys, lists, numbers. Perfect for metadata, configs, and API replies. Not tabular.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

#### 💡 **Rule of thumb**

A **table** → CSV. **Settings or metadata** → JSON. A **paragraph** → plain text. Match the format to the shape of the data.

</div>

---
hideInToc: true
---

# Text or Bytes? Open Modes

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 📄 **Text mode (the default)**

```python
open("d0.csv", "r", encoding="utf-8")
# str in, str out — decoded for you
```

- For anything human-readable: CSV, JSON, notes
- Set `encoding="utf-8"` so accents and symbols survive

</div>

<div class="card card-secondary card-glass pad-tight">

#### 🔟 **Binary mode (`"rb"` / `"wb"`)**

```python
open("d0.root", "rb")   # raw bytes, no decoding
```

- For images, ROOT / Parquet, any non-text blob
- Decoding bytes as the wrong text is where garbled characters come from

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **Which one?**

A table or a document is **text**; a compiled or compressed blob is **bytes**. When in doubt, it's text.

</div>

---
hideInToc: true
---

# Reading & Writing CSV

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 📥 **Read → dicts**

```python
import csv
with open("d0.csv", newline="") as f:
    rows = list(csv.DictReader(f))
# rows[0] == {'event': '1', 'mass_MeV': '1864.8', ...}
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 📤 **Write ← dicts**

```python
with open("out.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

#### ⚠️ **Two gotchas**

Always pass `newline=""` (stops blank lines on Windows), and remember every value arrives as a **string** — `float(row["mass_MeV"])` before you do maths.

</div>

---
hideInToc: true
---

# Try It — CSV Round-Trip

```py {monaco-run} {autorun:false}
import csv, io

# A tiny in-memory CSV (normally this is a file on disk)
text = "event,mass_MeV,charge\n1,1864.8,0\n2,1865.9,0\n3,1901.2,0\n"

reader = csv.DictReader(io.StringIO(text))   # each row -> a dict
rows = list(reader)
print("rows read:", len(rows), "| first:", rows[0])

# Keep only rows near the D0 mass, then write them back out as CSV
peak = [r for r in rows if 1840 < float(r["mass_MeV"]) < 1890]
buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=rows[0].keys())
writer.writeheader()
writer.writerows(peak)
print("--- filtered CSV ---")
print(buf.getvalue())
```

---
hideInToc: true
---

# Try It — JSON Round-Trip

```py {monaco-run} {autorun:false}
import json

# A Python dict describing the dataset (mixed types + a list)
meta = {
    "sample": "LHCb D0 -> K- pi+",
    "events": 12345,
    "columns": ["event", "mass_MeV", "charge"],
    "mass_window_MeV": [1830, 1900],
}

text = json.dumps(meta, indent=2)   # dict -> JSON text
print(text)

back = json.loads(text)             # JSON text -> dict
print("\nkeys:", list(back.keys()))
print("events + 1 =", back["events"] + 1)   # a real int, not a string
```

*`json.dump`/`json.load` do the same, straight to and from a file object.*

---
hideInToc: true
---

# Try It — Mini Pipeline: CSV → JSON

```py {monaco-run} {autorun:false}
import csv, io, json

# Raw measurements arrive as CSV...
csv_text = "event,mass_MeV\n1,1864.8\n2,1865.9\n3,1901.2\n4,1863.2\n"
rows = list(csv.DictReader(io.StringIO(csv_text)))

# ...compute a summary...
masses = [float(r["mass_MeV"]) for r in rows]
in_peak = [m for m in masses if 1840 < m < 1890]
summary = {
    "n_events": len(rows),
    "n_in_peak": len(in_peak),
    "mean_peak_MeV": round(sum(in_peak) / len(in_peak), 2),
}

# ...and write the summary out as JSON — the shape this metadata deserves.
print(json.dumps(summary, indent=2))
```

*This is the shape of Seminar 8's ingest step: a CSV in, a small JSON summary out.*

---
hideInToc: true
---

# Why Binary & Columnar Formats Exist

<div class="card card-info card-glass pad-tight mt-md">

## 📦 **CSV and JSON are text — that has a cost**

- A number like `1864.8` is stored as **6 characters** and re-parsed on every read
- Millions of rows → slow to load and large on disk
- Text can't record whether a column is `int`, `float`, or a date

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## ⚡ **Binary / columnar formats fix this**

Parquet, HDF5, and ROOT store **real numbers**, compress well, and let you read just the columns you need. We meet them properly in **Lecture 15** — for now, know they exist and why.

</div>

---
hideInToc: true
---

<MCQ
  question="You need to save a dataset's run parameters — sample name, number of events, and the list of column names — beside the data. Which format fits best?"
  :options="[
    'JSON — it stores nested keys, a list, and a number directly as data',
    'CSV — one row can hold all of it',
    'A .txt file with the values separated by commas',
    'An Excel sheet with one value per cell'
  ]"
  :correct="0"
  explanation="The parameters are nested and mixed-type — a string, an int, and a list — which is exactly what JSON represents. CSV is for flat tables of rows and columns; forcing nested metadata into CSV (or ad-hoc text) means writing a fragile parser later. json.dump / json.load round-trips the whole structure in one line."
/>

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

```py {monaco-run} {autorun:false}
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

```py {monaco-run} {autorun:false}
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
layout: section
hideInToc: true
---

# Docstrings & **Type Hints**

<!--
Speaker: the difference between code that works once and code a teammate (or future-
you) can pick up. Documentation you write while writing, not after. (~1 min)
-->

---
hideInToc: true
---

# Reading the Docs with `help()`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 📖 **`help()` reads the docstring**

```python
help(len)
# len(obj) -> integer
# Return the number of items in a container.
```

Every docstring you write shows up here — and as a tooltip in your editor.

</div>

<div class="card card-secondary card-glass pad-tight">

#### 💬 **A docstring is just a string**

```python
def load(path):
    """Read a CSV into a list of dicts."""
    ...
print(load.__doc__)
```

Python stores that first `"""..."""` as the function's `__doc__`.

</div>

</div>

---
hideInToc: true
---

# Writing One Good Docstring

<div class="card card-primary card-glass pad-tight mt-md">

## ✍️ **Summary, then inputs and outputs**

```python
def mass_window(rows, low, high):
    """Return rows whose mass_MeV is in [low, high].

    Args:
        rows: list of dicts, each with a 'mass_MeV' key.
        low, high: window edges in MeV.
    Returns:
        A new list with only the rows inside the window.
    """
    return [r for r in rows if low <= float(r["mass_MeV"]) <= high]
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

- First line: a one-sentence summary in the imperative ("Return…")
- Then what goes **in** (Args) and what comes **out** (Returns)

</div>

---
hideInToc: true
---

# Type Hints — Docs the Tools Can Read

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 🏷️ **What they look like**

```python
def mass_window(
    rows: list[dict],
    low: float,
    high: float,
) -> list[dict]:
    ...
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 🎯 **What they're for**

- **Not** enforced at run time — Python still runs either way
- They document intent, so editors autocomplete and flag mistakes
- Start light: annotate your key functions' inputs and return

</div>

</div>

---
hideInToc: true
---

# Try It — Docstrings & `help()`

```py {monaco-run} {autorun:false}
def describe(values: list[float]) -> dict:
    """Return the count, mean and range of some numbers.

    Args:
        values: the measurements to summarise.
    Returns:
        A dict with keys 'n', 'mean' and 'range'.
    """
    return {
        "n": len(values),
        "mean": sum(values) / len(values),
        "range": max(values) - min(values),
    }

help(describe)                              # your docstring, discoverable
print("annotations:", describe.__annotations__)
print(describe([22.1, 23.5, 21.8, 24.2]))
```

---
layout: section
hideInToc: true
---

# Organising Code into **Modules**

<!--
Speaker: the jump from one long script to a small, tidy project. Functions in one
file, the steps that call them in another — the layout every seminar uses. (~1 min)
-->

---
hideInToc: true
---

# One File Becomes a Module

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 📄 **`stats.py` — the module**

```python
def mean(values):
    return sum(values) / len(values)

def spread(values):
    return max(values) - min(values)
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 📄 **`analysis.py` — uses it**

```python
from stats import mean, spread

rates = [22.1, 22.4, 22.3]
print(mean(rates), spread(rates))
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **The rule**

Any `.py` file is importable by its name (minus the `.py`) from a sibling file. Group related functions into one module; import what you need.

</div>

---
hideInToc: true
---

# The `__main__` Guard

<div class="card card-primary card-glass pad-tight mt-md">

## 🚪 **A file that is both module and script**

```python
# stats.py
def mean(values):
    return sum(values) / len(values)

if __name__ == "__main__":
    # runs ONLY with `python stats.py`, not on import
    print(mean([1, 2, 3]))
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

- Importing a module runs its top level — so bare code runs on import (surprise!)
- The guard keeps "do the work" code from firing when someone just imports your functions

</div>

---
hideInToc: true
---

# A Small Analysis Repo Layout

<div class="card card-primary card-glass pad-tight mt-md">

## 🗂️ **Where each kind of code lives**

```
myanalysis/
├── data/raw/        # inputs, never edited by hand
├── src/             # importable functions (stats.py, io.py)
├── scripts/         # runnable steps (ingest.py, fit.py)
├── results/         # generated outputs (gitignored)
└── environment.yml  # pinned dependencies (Lecture 14)
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

- Code that **computes** lives in `src/`; code you **run** lives in `scripts/`
- Data flows one way: `data/raw` → `scripts/` → `results/`
- This is the layout the running project uses across every seminar

</div>

---
hideInToc: true
---

# Try It — The `__main__` Guard

```py {monaco-run} {autorun:false}
# Pretend this file is `stats.py`
def mean(values):
    """Arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

def spread(values):
    """Largest minus smallest value."""
    return max(values) - min(values)

# This block runs only when the file is executed directly,
# never when another file does `import stats`.
if __name__ == "__main__":
    rates = [22.1, 22.4, 22.3, 22.8, 22.5]
    print("mean  :", round(mean(rates), 2))
    print("spread:", round(spread(rates), 2))
    print("__name__ is:", __name__)
```

---
layout: section
hideInToc: true
---

# From Script to **Command-Line Tool** ⚙️

<!--
Speaker: the automation payoff — one script that runs on any file you hand it, not
one you edit every time. This is what makes an analysis step re-runnable. (~1 min)
-->

---
hideInToc: true
---

# The Problem: One Hard-Coded File

<div class="card card-warning card-glass pad-tight mt-md">

## 😩 **Editing the code to change the input**

```python
# analyse.py — works, but only for ONE file
INPUT = "data/raw/chamber_A.csv"   # edit this line every time
rows = load(INPUT)
print(summarise(rows))
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

- To analyse a different file you must **edit the source** — error-prone, not repeatable
- A shell loop (Lecture 4) can't help here — the script ignores its arguments while the filename is hard-coded
- The fix: read the filename as an **argument** when the script runs

</div>

---
hideInToc: true
---

# `sys.argv` — the Raw Arguments

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 📥 **The simplest way**

```python
import sys

# python analyse.py data/raw/chamber_B.csv
infile = sys.argv[1]
print("analysing", infile)
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 📝 **What it gives you**

- `sys.argv` is the list of words after `python`
- `sys.argv[0]` is the script's own name
- Simple — but no `--help`, no defaults, no type checks

</div>

</div>

---
hideInToc: true
---

# `argparse` — a Real Interface

<div class="card card-primary card-glass pad-tight mt-md">

## 🧰 **Named arguments, defaults, and free help**

```python
import argparse

p = argparse.ArgumentParser(description="Summarise a detector CSV.")
p.add_argument("input", help="path to the CSV file")
p.add_argument("--window", type=float, default=5.0,
               help="mass-window half-width in MeV")
args = p.parse_args()

print(args.input, args.window)
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

Free `--help` text, type conversion, defaults, and clear error messages — the standard way to make a script re-runnable on any input.

</div>

---
hideInToc: true
---

# Try It — `argparse`

```py {monaco-run} {autorun:false}
import argparse

parser = argparse.ArgumentParser(description="Summarise a detector CSV.")
parser.add_argument("input", help="path to the CSV file")
parser.add_argument("--window", type=float, default=5.0,
                    help="mass-window half-width in MeV")

# Normally argparse reads the real command line. Here we pass a list
# so it runs inside the slide — try editing these values:
args = parser.parse_args(["data/raw/d0.csv", "--window", "8"])

print("input :", args.input)
print("window:", args.window, "MeV")
print("window is a", type(args.window).__name__)   # float — converted for us
```

---
hideInToc: true
---

# Exit Codes — Did It Work?

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 🚦 **Signal success or failure**

```python
import sys

if not rows:
    print("no data found", file=sys.stderr)
    sys.exit(1)   # non-zero = failure
sys.exit(0)       # zero = success
```

</div>

<div class="card card-secondary card-glass pad-tight">

#### 🔗 **Why it matters**

- The shell reads the code: `0` = success, anything else = failure
- Chain steps: `ingest.py && fit.py` stops if ingest fails
- Automation and CI depend on honest exit codes (Lecture 14)

</div>

</div>

---
hideInToc: true
---

# The Whole Tool in One File

<div class="card card-primary card-glass pad-tight mt-md">

## 🧩 **Everything from today, working together**

```python
import argparse, csv, sys
from pathlib import Path

p = argparse.ArgumentParser(description="Count events in a CSV.")
p.add_argument("input")
args = p.parse_args()

path = Path(args.input)
if not path.exists():
    sys.exit(f"no such file: {path}")   # stderr + non-zero exit
rows = list(csv.DictReader(path.open(newline="")))
print(f"{path.name}: {len(rows)} events")
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

Robust paths, a real interface, safe reading, an honest exit code — drop it in `scripts/` and run it on any CSV.

</div>

---
hideInToc: true
---

# Now It's a Reusable Tool

<div class="card card-success card-glass pad-tight mt-md">

## ⚙️ **One script, any input, no edits**

```bash
# analyse a single file
python analyse.py data/raw/chamber_A.csv --window 8

# or loop over every file from the shell
for f in data/raw/*.csv; do
    python analyse.py "$f" --window 8
done
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

Fully repeatable, scriptable, and shareable — the automation aim ⚙️ in one small change. Your analysis step now runs the same way every time, on any file.

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

<div class="card card-success card-glass pad-compact">

✅ Handle paths portably with **pathlib** and organise a small analysis repo

</div>

<div class="card card-success card-glass pad-compact">

✅ Document with **docstrings & type hints** and ship an **argparse** CLI tool

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
