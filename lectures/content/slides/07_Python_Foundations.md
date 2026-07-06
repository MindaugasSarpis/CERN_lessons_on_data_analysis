---
background: /figures/background_intro.jpg
class: text-left
colorSchema: dark
theme: ./theme
drawings:
  persist: false
title: "Crash Course on Python Programming"
layout: cover
addons:
  - slidev-addon-python-runner
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python Foundations

##### <span class="aims-badge">🔧 tool-agnostic</span>

<!--
Speaker: gauge the room — who has written Python before? Reassure absolute
beginners: the live editor on these slides means no setup needed to follow
along. Everything runs in the browser. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Python is the **Swiss Army knife** of programming — simple enough for beginners, powerful enough for CERN. Learn the basics, and an entire ecosystem of scientific tools opens up.

<!--
Speaker: this is the tool-agnostic aim in action — the ideas transfer, Python is
just today's vehicle. Frame the next ~40 min as the vocabulary they'll reuse in
every seminar. (~1 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🐍 Run Python and read its core **syntax** — indentation, dynamic typing, comments

</div>

<div class="card card-secondary card-glass pad-compact">

🔢 Work with built-in **types** and operators — numbers, strings, booleans

</div>

<div class="card card-accent card-glass pad-compact">

📋 Pick the right **data structure** — lists, tuples, sets, dictionaries

</div>

<div class="card card-success card-glass pad-compact">

⚡ Transform data with **comprehensions** and string methods

</div>

<div class="card card-warning card-glass pad-compact">

🔀 Steer a program with **conditionals** and **loops**

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Point out that the paired
Seminar 7 is where they write their first parser — today gives them the building
blocks. (~1 min)
-->

---
hideInToc: true
---

# Why <span class="gradient-text">Python</span>

<div class="card card-primary card-glass pad-tight mt-md reveal-left glow">

## 🌍 **Most Popular & Easy to Learn**

Python is one of the most popular and easiest-to-learn programming languages in the world

</div>

<div class="card card-secondary card-glass pad-tight mt-sm reveal-left">

## 👥 **Large Community & Ecosystem**

A large community of developers and users, as well as a large number of libraries and frameworks, makes it a very versatile language

</div>

<div class="card card-success card-glass pad-tight mt-sm reveal-left">

## 🆓 **Open-Source & Powerful**

Python itself and many of its libraries and tools are open-source and free to use — and at the same time much more powerful than many commercial tools

</div>

---
hideInToc: true
---

# Useful Resources for Starting with Python

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

## 📖 **Official Documentation**

- [Python Official Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html)

</div>

<div class="card card-secondary card-glass pad-tight mt-sm">

## 📊 **Data Science**

- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

</div>

</div>

<div class="card card-info card-glass pad-tight">

## 🎓 **Free Introductory Courses**

- **The official Python tutorial** — docs.python.org, fully free
- **Coursera / edX** — university courses, free to audit
- **freeCodeCamp & Kaggle Learn** — fully free, hands-on
- **Codecademy / Udemy** — polished, but the good parts are usually paid

<div class="note-text mt-sm">

Free coverage varies by platform — the fully-free options above are more than enough for this course.

</div>

</div>

</div>

---
hideInToc: true
---

# Do You Have Python?

<div class="card card-info card-glass pad-compact mt-md">

## 🔍 **Check Your Installation**

Open your terminal (VS Code: `` Ctrl+` ``) and run:

```bash
python --version      # or python3 --version
```

You should see `Python 3.x.x`.

</div>

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS / Linux**

```bash
brew install python        # macOS (Homebrew)
sudo apt install python3   # Ubuntu/Debian
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows**

Download from [python.org](https://www.python.org/downloads/) — check **"Add Python to PATH"** during install.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

We will use the **in-browser editor** on these slides for learning, but you will need a local Python install for your projects. *Isolated environments (`venv`, `conda`) that keep each project's packages separate exist too — properly covered in Lecture 14.*

</div>

---
hideInToc: true
---

# Python Basics

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

### 🚀 **Running Python**

- Interactive mode: `python` or `ipython` in the terminal
- Script mode: `python my_script.py`

</div>

<div class="card card-info card-glass pad-tight mt-sm">

### 🔑 **Main Points**

- Indentation is crucial in Python
- Python uses dynamic typing *(you don't declare types — Python infers them from the value)*
- Python has a rich standard library and many third-party libraries
- Many built-in functions, e.g. `print()`, `len()`, `type()`, `int()`, `str()`, `list()`, `dict()`

</div>

</div>

<div>

<div class="card card-secondary card-glass pad-tight">

### 💬 **Comments**

```python
# This function does ...
```

```python
"""Strictly speaking this is a
string literal, not a comment —
but an unassigned one works
like a multi-line comment."""
```

<div class="note-text mt-sm">`#` is Python's only true comment. Triple-quoted strings become <strong>docstrings</strong> when placed first in a function — you'll meet those soon.</div>

</div>

<div class="card card-accent card-glass pad-tight mt-sm">

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

```py {monaco-run} {autorun:false}
print("Hello from Python! 🐍", 2 + 2)
```

---
hideInToc: true
---

# Try It — Variables & Types

```py {monaco-run} {autorun:false}
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

<div class="card card-primary card-glass pad-compact">

#### 🔢 **Basic Operators**

```python
2 + 3   # Addition       → 5
3 * 4   # Multiplication → 12
6 / 2   # Division       → 3.0 (always float!)
7 // 2  # Floor division → 3
5 % 2   # Modulus        → 1
2 ** 10 # Exponentiation → 1024
```

```python
3 > 2 and 4 == 4  # True
not False          # True
"a" in "abc"       # True
```

</div>

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

#### 📝 **Variables and Data Types**

```python
x        = 10      # Integer
y        = 3.14    # Float
name     = "Alice" # String
is_valid = True    # Boolean
```

</div>

<div class="card card-info card-glass pad-compact mt-sm">

#### 📦 **More Built-in Types**

- **Tuples** — immutable *(can't be changed after creation)*: `point = (3, 4)`
- **Sets** — unique elements: `{1, 2, 3}`
- **`range()`** — number sequences: `range(0, 10, 2)`
- **f-strings** — formatted: `f"Hello, {name}!"`

</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Data **Structures**

<!--
Speaker: this is the heart of the lecture. Frame the choice — list vs. tuple vs.
set vs. dict is about matching the container to the data. Real analysis code is
mostly moving data between these four. (~1 min)
-->

---
hideInToc: true
---

# Strings & Lists

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

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

<div class="card card-accent card-glass pad-tight">

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

# Strings for Data Wrangling

<div class="card card-info card-glass pad-compact mt-sm">

🧵 Three string methods do most of the work when reading real data files:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

#### ✂️ **`.strip()` and `.split()`**

```python
line = "1049,-1204.5,873.2,15320.7,980.1,-650.4,9210.3\n"
clean = line.strip()        # no newline
parts = clean.split(",")    # list of pieces
# event ID, then kaon (H1) & pion (H2) momentum components
values = [float(p) for p in parts[1:]]
```

</div>

<div class="card card-accent card-glass pad-tight">

#### 🔗 **`.join()` — the reverse**

```python
names = ["run1", "run2", "run3"]
print(", ".join(names))
# run1, run2, run3
```

Build output lines and filenames from lists.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 `strip → split → convert` is the classic recipe for parsing a line of a data file — you'll use it in the file-handling section shortly.

</div>

<!--
Speaker: slow down here — this is exactly what Seminar 7 asks for. Walk the
recipe on the raw line live: strip the newline, split on the comma, float() each
piece. Everything else is variation on this. (~2 min)
-->

---
hideInToc: true
---

# A Peek Ahead — Skipping Junk Lines Safely

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Real data files have junk lines too — a header, a blank line, a corrupted row. `float()` on non-numeric text raises a `ValueError` and crashes your script.

</div>

```py {monaco-run} {autorun:false}
lines = ["1049,-1204.5,873.2", "# comment row, not data", "1050,988.1,-650.4"]

for line in lines:
    try:
        event_id, k_px, pi_px = line.split(",")
        print(f"event {event_id}: K px={float(k_px)}, pi px={float(pi_px)}")
    except ValueError:
        print(f"skipped junk line: {line!r}")
```

<div class="card card-info card-glass pad-compact mt-sm">

💡 The full `try` / `except` / `finally` toolkit — with multiple exception types — comes in Lecture 08. For now: wrap the risky conversion, catch `ValueError`, move on.

</div>

<!--
Speaker: this is a preview only — Seminar 7 needs it before L08 formally teaches
exceptions. Don't dwell on syntax; the message is "some lines are junk, skip
them safely." (~1 min)
-->

---
hideInToc: true
---

# Tuples, Sets & Unpacking

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

#### 📌 **Tuples — frozen lists**

```python
point = (3, 4)          # can't be modified
x, y = point            # unpacking!
x, y = y, x             # the classic swap
```

Ideal for things that belong together: coordinates, (name, value) pairs.

</div>

<div class="card card-secondary card-glass pad-tight">

#### 🎯 **Sets — no duplicates**

```python
hits = [3, 7, 3, 2, 7, 7]
set(hits)         # {2, 3, 7}
len(set(hits))    # 3 distinct sensors
7 in set(hits)    # fast membership test
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 You'll soon use tuple unpacking without noticing: `for key, value in data.items()` unpacks a tuple on every loop turn.

</div>

---
hideInToc: true
---

# Try It — Lists in Action

```py {monaco-run} {autorun:false}
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
# List comprehension — explained on the next slide
above_24 = [m for m in measurements if m > 24]
print(f"Above 24: {above_24}")
```

---
hideInToc: true
---

# List Comprehensions

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

#### 🔄 **Traditional Loop**

```python
squares = []
for x in range(5):
    squares.append(x**2)
# [0, 1, 4, 9, 16]
```

</div>

<div class="card card-accent card-glass pad-tight">

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

<div class="card card-info card-glass pad-tight mt-md">

#### 💡 **When to use**

- Simple transformations and filters → comprehension
- Complex logic with side effects → traditional loop

</div>

---
hideInToc: true
---

<MCQ
  question="After running:  a = [1, 2, 3]   then   b = a   then   b.append(4) — what is `a`?"
  :options="[
    '[1, 2, 3] — b is a copy, so a is unchanged',
    '[1, 2, 3, 4] — a and b are the same list',
    'An error — lists cannot be assigned to two names',
    '[4] — b replaces the contents of a'
  ]"
  :correct="1"
  explanation="Assignment never copies in Python — b = a just gives the same list a second name, so changes through either name are visible through both. To get an independent copy, use b = a.copy() or b = list(a). This aliasing surprise is one of the most common beginner bugs."
/>

---
hideInToc: true
---

<MCQ
  question="masses = [1866, 1810, 1871]   then   result = masses.sort() — what is `result`, and what is `masses` now?"
  :options="[
    'result is None; masses is now [1810, 1866, 1871] — sort() mutates in place and returns nothing',
    'result is [1810, 1866, 1871]; masses is unchanged — sort() returns a new sorted list',
    'result is None; masses is unchanged — sort() only previews the order',
    'Both result and masses are [1810, 1866, 1871] — they always match'
  ]"
  :correct="0"
  explanation="list.sort() sorts in place and returns None — printing result would show 'None', a classic beginner trap. sorted(masses) is the alternative: it leaves the original list untouched and returns a new sorted list. Use .sort() when mutating is fine; use sorted() when you need the original preserved too."
/>

---
hideInToc: true
---

# Dictionary Basics

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

### 📖 **Overview**

- Dictionaries map immutable keys (strings, numbers) to values
- Membership checks are fast: `"age" in person`
- View objects `.keys()`, `.values()`, `.items()` reflect live data

</div>

<div class="card card-secondary card-glass pad-tight mt-sm">

### 💡 **Tips**

- Use `.get()`/`.setdefault()` for optional keys; avoid `KeyError`s from direct indexing
- Nest dictionaries (e.g., parsed JSON) to represent hierarchical structures

</div>

</div>

<div>

<div class="card card-info card-glass pad-tight">

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

<div class="card card-primary card-glass pad-tight">

##### 🔄 **Dictionary Comprehension**

```python
squares = {n: n**2 for n in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

</div>

<div class="card card-info card-glass pad-tight mt-sm">

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

<div class="card card-accent card-glass pad-tight">

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

```py {monaco-run} {autorun:false}
# Storing one D0 -> K- pi+ candidate
event = {
    "event_id": 1049,
    "run": 98213,
    "decay": "D0 -> K- pi+",
    "H1_charge": -1,  # the kaon
    "H2_charge": 1,   # the pion
}

# Access and display
for key, value in event.items():
    print(f"  {key}: {value}")

# Add new data
event["dataset"] = "LHCb Open Data record 401"
event["momentum_cols"] = ["H1_PX", "H1_PY", "H1_PZ", "H2_PX", "H2_PY", "H2_PZ"]
print(f"\nUpdated: event {event['event_id']} tracks {len(event['momentum_cols'])} momentum components")
```

---
layout: section
hideInToc: true
---

# Control **Flow**

<!--
Speaker: last building block — deciding and repeating. Stress that indentation,
not braces, defines a block; a stray space is a real bug in Python. Loops over
lists and dicts are where the data structures pay off. (~1 min)
-->

---
hideInToc: true
---

# Conditionals & Loops

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary card-glass pad-tight">

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

<div class="card card-secondary card-glass pad-tight">

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

<div class="card card-info card-glass pad-compact mt-md">

#### 💡 **Remember**

- Indentation defines blocks — no curly braces needed
- `range(start, stop, step)` generates sequences of integers

</div>

---
hideInToc: true
---

# Try It — Loops and Logic

```py {monaco-run} {autorun:false}
# Classify K-pi invariant masses against the D0 peak (~1865 MeV)
masses_MeV = [1810.2, 1863.5, 1866.9, 1870.1, 1920.4]

for m in masses_MeV:
    if 1855 <= m <= 1875:
        label = "near D0 peak"
    elif m < 1855:
        label = "below peak"
    else:
        label = "above peak"
    print(f"  {m:7.1f} MeV → {label}")

# Count per category
near_peak = sum(1 for m in masses_MeV if 1855 <= m <= 1875)
print(f"\nEvents near the D0 peak: {near_peak}/{len(masses_MeV)}")
```

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Run Python and use its core **syntax** and built-in types

</div>

<div class="card card-success card-glass pad-compact">

✅ Build and manipulate **lists, dicts, tuples, and sets**

</div>

<div class="card card-success card-glass pad-compact">

✅ Write **comprehensions** and parse text with string methods

</div>

<div class="card card-success card-glass pad-compact">

✅ Direct program flow with **conditionals** and **loops**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 7 tie-in**

Write your first parser — turn one raw event line from the dataset into usable numbers.

</div>

<!--
Speaker: the "you can now" beat — have them mentally tick each box. The seminar
tie-in makes it concrete: they leave with the strip → split → convert recipe and
apply it to a real line of the D0 -> K-pi+ dataset. (~1 min)
-->
