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
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

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

# Operators & Data Types

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

<div class="card card-secondary pad-tight mt-sm">

#### 📝 **Variables and Data Types**

```python
x        = 10      # Integer
y        = 3.14    # Float
name     = "Alice" # String
is_valid = True    # Boolean
```

</div>

</div>

<div>

<div class="card card-info pad-tight">

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

<div class="card card-accent pad-tight mt-sm">

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

# Dictionaries

<div class="grid-2 gap-md mt-md">

<div>

<div class="card card-primary pad-tight">

### 📖 **Overview**

- Dictionaries hold mutable mappings of hashable keys to values
- Membership checks are fast: `"age" in person`
- View objects `.keys()`, `.values()`, `.items()` reflect live data; cast to `list()` only when you need a snapshot

</div>

<div class="card card-info pad-tight mt-sm">

##### 🛠️ Everyday Operations

```python
person = {"name": "Alice", "age": 25}
person["city"] = "New York"      # Add key-value pair
person["age"] += 1               # Update in place
# Print value of a key (KeyError if missing)
print(person.get("role", "N/A"))
# Safe lookup with default
print(person["role"])

for key, value in person.items():
    print(f"{key}: {value}")
```

</div>

</div>

<div>

<div class="card card-secondary pad-tight">

### 💡 **Tips**

- Use `.get()`/`setdefault()` for optional keys; avoid `KeyError`s from direct indexing
- Nest dictionaries (e.g., parsed JSON) to represent hierarchical structures

</div>

<div class="card card-accent pad-tight mt-sm">

##### 🔄 Common Patterns

```python
# Dictionary comprehension
squares = {n: n**2 for n in range(5)}

# Counting with a default
# Stand-alone example of counting word frequencies

text = "the cat chased the dog and the dog chased the cat"
words = text.split()

counts = {}  # empty dictionary

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

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

# Control Flow & Functions

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

<div class="card card-secondary pad-tight mt-sm">

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

<div class="card card-warning pad-tight mt-sm">

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
