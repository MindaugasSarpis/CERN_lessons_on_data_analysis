---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Crash Course on Python Programming"
layout: cover

addons:
  - slidev-addon-python-runner
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Crash Course on Python Programming

---
hideInToc: true
layout: quote
---

# Python is the **Swiss Army knife** of programming — simple enough for beginners, powerful enough for CERN. Learn the basics, and an entire ecosystem of scientific tools opens up.

---
hideInToc: true
---

# Why Python

<div class="card card-primary pad-tight mt-md">

## 🌍 **Most Popular & Easy to Learn**

Python is one of the most popular and easy to learn programming languages in the world

</div>

<div class="card card-secondary pad-tight mt-sm">

## 👥 **Large Community & Ecosystem**

A large community of developers and users as well as a large number of libraries and frameworks make it a very versatile language

</div>

<div class="card card-success pad-tight mt-sm">

## 🆓 **Open-Source & Powerful**

Python itself and many of its libraries and tools are open-source and free to use and at the same time much more powerful than many commercial tools

</div>

---
hideInToc: true
---

# Useful Resources for Starting with Python

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

## 📖 **Official Documentation**

- [Python Official Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html)

</div>

<div class="card card-secondary pad-tight mt-sm">

## 📊 **Data Science**

- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

</div>

</div>

<div class="card card-info pad-tight">

## 🎓 **Free Introductory Courses**

- **Codecademy** — Interactive Python lessons
- **Coursera** — University-level courses
- **edX** — Harvard/MIT offerings
- **Udemy** — Beginner-friendly tutorials

<div class="note-text mt-sm">

All platforms offer free tiers with comprehensive Python content.

</div>

</div>

</div>

---
hideInToc: true
---

<div class="card card-info pad-compact mt-md">

## 🔍 **Do You Have Python?**

Open your terminal (VS Code: `` Ctrl+` ``) and run:

```bash
python --version      # or python3 --version
```

You should see `Python 3.x.x`.

</div>

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary pad-compact">

## 🍎 **macOS / Linux**

```bash
brew install python        # macOS (Homebrew)
sudo apt install python3   # Ubuntu/Debian
```

</div>

<div class="card card-secondary pad-compact">

## 🪟 **Windows**

Download from [python.org](https://www.python.org/downloads/) — check **"Add Python to PATH"** during install.

</div>

</div>

<div class="card card-warning pad-compact mt-sm">

We will use the **in-browser editor** on these slides for learning, but you will need a local Python install for your projects.

</div>

---
layout: section
hideInToc: true
---

# Python **Basics**

---
hideInToc: true
---

# Python Basics

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

### 🚀 **Running Python**

- Interactive mode: `python` or `ipython` in the terminal
- Script mode: `python my_script.py`

</div>

<div class="card card-info pad-tight mt-sm">

### 🔑 **Main Points**

- Indentation is crucial in Python
- Python uses dynamic typing
- Python has a rich standard library and many third-party libraries (many built-in functions)
- eg. `print()`, `len()`, `type()`, `int()`, `str()`, `list()`, `dict()`, etc.

</div>

</div>

<div>

<div class="card card-secondary pad-tight">

### 💬 **Comments**

```python
# This function does ...
```

```python
"""
This is a
multi-line
comment
"""
```

</div>

<div class="card card-accent pad-tight mt-sm">

### ⌨️ **Shortcuts & Tips**

- **Ctrl + /** to comment/uncomment selected lines in many editors
- Use comments for quick debugging / prototyping

</div>

</div>

</div>

---
hideInToc: true
---

# Try It — Live Python

```py {monaco-run}
print("Hello from Python! 🐍", 2 + 2)
```

---
hideInToc: true
---

# Try It — Variables & Types

```py {monaco-run}
# Experiment with variables and types
name = "CERN"
energy = 13.6  # TeV
num_detectors = 4
is_running = True

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Energy: {energy} TeV (type: {type(energy).__name__})")
print(f"Detectors: {num_detectors} (type: {type(num_detectors).__name__})")
print(f"Running: {is_running} (type: {type(is_running).__name__})")

# Try changing the values and re-running!
```

---
hideInToc: true
---

# Operators & Variables

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

#### 🔢 **Basic Operators**

```python
# Arithmetic
2 + 3   # Addition       → 5
5 - 2   # Subtraction    → 3
3 * 4   # Multiplication → 12
6 / 2   # Division       → 3.0 (always float!)
7 // 2  # Floor division → 3
5 % 2   # Modulus        → 1
2 ** 10 # Exponentiation → 1024
```

```python
# Comparison & Logic
3 > 2 and 4 == 4  # True
5 != 3 or 1 > 10  # True
not False          # True
"a" in "abc"       # True
```

</div>

</div>

<div>

<div class="card card-secondary pad-tight">

#### 📝 **Variables and Data Types**

```python
x        = 10      # Integer
y        = 3.14    # Float
name     = "Alice" # String
is_valid = True    # Boolean
```

</div>

<div class="card card-info pad-tight mt-sm">

#### 📦 **More Built-in Types**

- **Tuples** — immutable sequences: `point = (3, 4)`
- **Sets** — unique elements: `unique = {1, 2, 3}`
- **`range()`** — generates number sequences: `range(0, 10, 2)`
- **f-strings** — formatted text: `f"Hello, {name}!"`

</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Structures**

---
hideInToc: true
---

# Strings & Lists

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

#### 🔤 **Strings**

```python
s = "Hello, World!"
print(s[0])      # H (indexing)
print(s[-1])     # ! (negative indexing)
print(s[0:5])    # Hello (slicing)
print(len(s))    # Length of string
print(s.lower()) # Convert to lowercase
print(s.upper()) # Convert to uppercase
print(s.replace("World", "Python")) # Replace
```

</div>

</div>

<div>

<div class="card card-accent pad-tight">

#### 📋 **Lists**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # First element
numbers.append(6)   # Add element
numbers.remove(3)   # Remove element
print(len(numbers)) # Length of list
numbers.sort()      # Sort list
```

- Lists are mutable and can hold mixed data types

```python
customer_info = ["Alice", 25, "New York", "Premium", True]
```

</div>

</div>

</div>

---
hideInToc: true
---

# Try It — Lists in Action

```py {monaco-run}
# Working with lists
measurements = [23.1, 25.4, 22.8, 24.5, 26.1, 23.9]

print(f"Measurements: {measurements}")
print(f"Count: {len(measurements)}")
print(f"First: {measurements[0]}, Last: {measurements[-1]}")
print(f"Sorted: {sorted(measurements)}")

# Add a new measurement
measurements.append(24.2)
print(f"After append: {measurements}")

# Filter: only values above 24
above_24 = [m for m in measurements if m > 24]
print(f"Above 24: {above_24}")
```

---
hideInToc: true
---

# Dictionary Basics

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

### 📖 **Overview**

- Dictionaries map immutable keys (strings, numbers) to values
- Membership checks are fast: `"age" in person`
- View objects `.keys()`, `.values()`, `.items()` reflect live data

</div>

<div class="card card-secondary pad-tight mt-sm">

### 💡 **Tips**

- Use `.get()`/`setdefault()` for optional keys; avoid `KeyError`s from direct indexing
- Nest dictionaries (e.g., parsed JSON) to represent hierarchical structures

</div>

</div>

<div>

<div class="card card-info pad-tight">

##### 🛠️ **Everyday Operations**

```python
person = {"name": "Alice", "age": 25}
person["city"] = "New York"      # Add key-value pair
person["age"] += 1               # Update in place

# Safe lookup with default (returns "N/A" if missing)
print(person.get("role", "N/A"))

# Direct lookup (raises KeyError if missing!)
# print(person["role"])  # KeyError: 'role'

for key, value in person.items():
    print(f"{key}: {value}")
```

</div>

</div>

</div>

---
hideInToc: true
---

# Dictionary Patterns

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

##### 🔄 **Dictionary Comprehension**

```python
squares = {n: n**2 for n in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

</div>

<div class="card card-info pad-tight mt-sm">

##### 🔑 **Merging Dictionaries**

```python
defaults = {"color": "blue", "size": 10}
custom   = {"size": 20, "style": "bold"}
merged   = {**defaults, **custom}
# {"color": "blue", "size": 20, "style": "bold"}
```

</div>

</div>

<div>

<div class="card card-accent pad-tight">

##### 📊 **Counting Word Frequencies**

```python
text  = "the cat chased the dog and the dog chased the cat"
words = text.split()

counts = {}  # empty dictionary

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
# {'the': 4, 'cat': 2, 'chased': 2, 'dog': 2, 'and': 1}
```

</div>

</div>

</div>

---
hideInToc: true
---

# Try It — Dictionaries for Data

```py {monaco-run}
# Storing experiment metadata
experiment = {
    "name": "ATLAS",
    "location": "Geneva",
    "energy_TeV": 13.6,
    "active": True,
    "detectors": ["inner tracker", "calorimeter", "muon spectrometer"]
}

# Access and display
for key, value in experiment.items():
    print(f"  {key}: {value}")

# Add new data
experiment["start_year"] = 2008
experiment["num_detectors"] = len(experiment["detectors"])
print(f"\nUpdated: {experiment['name']} has {experiment['num_detectors']} detector systems")
```

---
layout: section
hideInToc: true
---

# Control **Flow**

---
hideInToc: true
---

# Conditionals & Loops

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

#### 🔀 **Conditional Statements**

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

</div>

</div>

<div>

<div class="card card-secondary pad-tight">

#### 🔁 **Loops**

```python
# For loop
for i in range(5):
    print(i)  # Prints 0 to 4

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
```

</div>

</div>

</div>

<div class="card card-info pad-compact mt-md">

#### 💡 **Remember**

- Indentation defines blocks — no curly braces needed
- `range(start, stop, step)` generates sequences of integers

</div>

---
hideInToc: true
---

# Try It — Loops and Logic

```py {monaco-run}
# Classify particle energies
energies = [0.5, 2.3, 8.1, 15.4, 3.2, 50.0, 1.1, 125.0]

for e in energies:
    if e > 100:
        label = "very high"
    elif e > 10:
        label = "high"
    elif e > 5:
        label = "medium"
    else:
        label = "low"
    print(f"  {e:6.1f} GeV → {label}")

# Count per category
high_count = sum(1 for e in energies if e > 10)
print(f"\nHigh energy events (>10 GeV): {high_count}/{len(energies)}")
```

---
layout: section
hideInToc: true
---

# Functions & **Patterns**

---
hideInToc: true
---

# Functions & Exceptions

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-info pad-tight">

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

<div class="card card-warning pad-tight">

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

---
hideInToc: true
---

# List Comprehensions

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

#### 🔄 **Traditional Loop**

```python
squares = []
for x in range(5):
    squares.append(x**2)
# [0, 1, 4, 9, 16]
```

</div>

<div class="card card-accent pad-tight">

#### ⚡ **Comprehension (Pythonic)**

```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

</div>

</div>

<div class="card card-info pad-tight mt-md">

#### 💡 **When to use**

- Simple transformations and filters → comprehension
- Complex logic with side effects → traditional loop

</div>

---
hideInToc: true
---

# Useful Built-in Patterns

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

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

<div class="card card-secondary pad-tight">

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

<div class="card card-info pad-compact mt-md">

#### 💡 **Tip**

- `enumerate()` replaces the `for i in range(len(...)): ` anti-pattern
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
    sign = "+" if charge > 0 else "" if charge < 0 else " "
    print(f"  {i+1}. {name:10s}  mass={mass:8.2f} MeV  charge={sign}{charge}")
```

---
layout: section
hideInToc: true
---

# Files & **Modules**

---
hideInToc: true
---

# Modules, Imports & File Handling

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

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

<div class="card card-secondary pad-tight">

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

# Common Python Errors

<div class="grid-2 gap-md mt-md">

<div class="card card-warning pad-tight">

## 🐛 **Syntax & Indentation**

```python
# IndentationError
if True:
print("oops")  # missing indent!

# SyntaxError
print("hello"  # missing closing )
```

- Python uses **whitespace** for structure
- Every `if`, `for`, `def` needs an **indented** block

</div>

<div class="card card-warning pad-tight">

## 🐛 **Name & Type Errors**

```python
# NameError
print(undefined_variable)

# TypeError
result = "hello" + 42  # can't add str + int
# Fix: "hello" + str(42)
```

- Check **spelling** of variable names
- Check **types** match the operation

</div>

</div>

<div class="card card-info pad-tight mt-md">

## 💡 **Debugging Tip**

Read the error message **bottom to top** — the last line tells you what went wrong, the lines above show where.

</div>

---
hideInToc: true
---

# Loading Structured Files into Dicts

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

#### 📄 JSON

```python
# JSON -> dict
import json

with open("data.json", "r") as f:
        data = json.load(f)  # dict (or nested dict/list)
```

</div>

<div class="card card-secondary pad-tight mt-sm">

#### 📝 YAML

```python
# YAML -> dict
# pip install pyyaml
import yaml

with open("data.yaml", "r") as f:
        data = yaml.safe_load(f)  # dict (or nested dict/list)
```

</div>

</div>

<div>

<div class="card card-info pad-tight">

#### 📊 CSV

```python
# CSV -> list[dict] (one dict per row)
import csv

with open("data.csv", newline="") as f:
        rows = list(csv.DictReader(f))  # [{'col1': '...', 'col2': '...'}, ...]
```

</div>

<div class="card card-accent pad-tight mt-sm">

#### 📈 Excel

```python
# Excel -> list[dict] via pandas
# pip install pandas openpyxl
import pandas as pd

df   = pd.read_excel("data.xlsx", sheet_name=0)  # DataFrame
rows = df.to_dict(orient="records")             # list[dict]
```

</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Mini **Projects**

---
hideInToc: true
---

# Mini Project: Analyse Experiment Data

```py {monaco-run}
# A complete mini data analysis in pure Python
# (no external libraries needed!)

# Simulated temperature readings from 3 sensors
data = {
    "sensor_A": [22.1, 22.4, 22.3, 22.8, 22.5],
    "sensor_B": [23.5, 23.1, 23.8, 23.2, 23.6],
    "sensor_C": [21.9, 22.0, 21.7, 22.1, 21.8],
}

print("=== Sensor Temperature Report ===\n")
for sensor, readings in data.items():
    avg = sum(readings) / len(readings)
    min_val = min(readings)
    max_val = max(readings)
    spread = max_val - min_val
    print(f"{sensor}: avg={avg:.2f}°C  range=[{min_val}, {max_val}]  spread={spread:.1f}°C")

# Find the hottest sensor
averages = {s: sum(r)/len(r) for s, r in data.items()}
hottest = max(averages, key=averages.get)
print(f"\nHottest sensor: {hottest} ({averages[hottest]:.2f}°C)")
```

---
hideInToc: true
---

# Mini Project: Visualise the Results

```py {monaco-run}
# Simple text-based "bar chart" — no matplotlib needed!
data = {
    "sensor_A": [22.1, 22.4, 22.3, 22.8, 22.5],
    "sensor_B": [23.5, 23.1, 23.8, 23.2, 23.6],
    "sensor_C": [21.9, 22.0, 21.7, 22.1, 21.8],
}

averages = {s: sum(r)/len(r) for s, r in data.items()}
min_avg = min(averages.values())

print("Average Temperature by Sensor")
print("=" * 40)
for sensor, avg in averages.items():
    bar_length = int((avg - 20) * 10)  # scale for display
    bar = "█" * bar_length
    print(f"{sensor}: {bar} {avg:.2f}°C")
print("\nNext up: NumPy and matplotlib will make this MUCH easier!")
```

---
hideInToc: true
---

# From Browser to Real Files

<div class="card card-info pad-tight mt-md">

## 🖥️ **Time to Write Real Python**

The in-browser exercises were great for learning — now let's create an actual Python script you can run, share, and version-control.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

**1.** In VS Code, create a new file: `File → New File` → save as `sensor_analysis.py`

</div>

<div class="card card-secondary pad-compact">

**2.** Copy your mini project code into the file (or write it fresh from memory!)

</div>

<div class="card card-accent pad-compact">

**3.** Open the VS Code terminal (`Ctrl+`` `) and run:

```bash
python sensor_analysis.py
```

</div>

<div class="card card-success pad-compact">

**4.** See the same output — but now it lives as a file on your machine, not just in a browser tab

</div>

</div>

---
hideInToc: true
---

# Version-Control Your Work

<div class="card card-success pad-tight mt-md">

## 🔄 **Save Your Progress with Git**

You learned `git` earlier today — now put it to use! After completing the mini projects:

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

```bash
git add sensor_analysis.py
git commit -m "Add sensor temperature analysis script"
```

</div>

<div class="card card-info pad-compact">

**Good habit**: commit after each working milestone. Your future self will thank you.

</div>

</div>

---
hideInToc: true
---

# What Comes Next

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔮 **Building on Python**

These basics unlock a powerful ecosystem:

- **Next**: Concepts of data analysis — the framework for thinking about data
- Data visualization principles — how to communicate with plots
- **Later**: NumPy, Pandas, matplotlib, probability, statistics, and data fitting

</div>

<div class="card card-secondary pad-tight">

## 💡 **Key Takeaway**

Python's simplicity is deceptive — the language you just learned is the same one used at CERN to process petabytes of collision data, train machine learning models, and automate entire analysis pipelines.

</div>

</div>

---
