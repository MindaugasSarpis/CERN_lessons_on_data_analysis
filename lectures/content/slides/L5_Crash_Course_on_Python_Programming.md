---
background: /background_intro.jpg

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

# Operators & Variables

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

#### 🔢 **Basic Operators**

```python
# Arithmetic
2 + 3 # Addition
5 - 2 # Subtraction
3 * 4 # Multiplication
6 / 2 # Division
5 % 2 # Modulus
```

```python
# Comparison
3  > 2 # True
4 == 4 # True
5 != 3 # True
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
hideInToc: true
---

# What Comes Next

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔮 **Building on Python**

These basics unlock a powerful ecosystem:

- **L7**: Data visualization with `matplotlib`
- **L9**: Statistics with `scipy.stats`
- **L10**: Data fitting with `scipy.optimize`
- **L11**: NumPy arrays & Pandas DataFrames

</div>

<div class="card card-secondary pad-tight">

## 💡 **Key Takeaway**

Python's simplicity is deceptive — the language you just learned is the same one used at CERN to process petabytes of collision data, train machine learning models, and automate entire analysis pipelines.

</div>

</div>

---
