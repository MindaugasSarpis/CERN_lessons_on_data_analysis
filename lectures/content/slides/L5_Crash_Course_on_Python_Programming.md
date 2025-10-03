---
background: /background_intro.jpg
marp: true
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
---

# Useful Resources for starting with Python

- ## [Python Official Documentation](https://docs.python.org/)

- ## [Python Tutorial](https://docs.python.org/3/tutorial/index.html)

- ## [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

- ## Free introductory courses on:

  - ### *codecademy*

  - ### *coursera*

  - ### *edx*

  - ### *udemy*

---
hideInToc: true
---

# Why Python

- ## Python is one of the most popular and easy to learn programming languages in the world

- ## A large community of developers and users as well as a large number of libraries and frameworks make it a very versatile language

- ## Python itself and many of its libraries and tools are open-source and free to use and at the same time much more powerful than many commercial tools 

---
hideInToc: true
layout: two-cols-header
---

# Python Basics

::left::

- ### **Running python** 

  - Interactive mode: `python` or `ipython` in the terminal

  - Script mode: `python my_script.py`
  
- ### **Main points**

  - Indentation is crucial in Python

  - Python uses dynamic typing

  - Python has a rich standard library and many third-party libraries (many built-in functions)

  - eg. `print()`, `len()`, `type()`, `int()`, `str()`, `list()`, `dict()`, etc.

::right::

- ### **Comments** 

<div style="max-width: 350px;">

```python
# This function does ...
```

</div>

<div style="max-width: 350px;">
```python
"""
This is a 
multi-line
comment
"""
```
</div>

- ### **Ctrl + /** to comment/uncomment selected lines in many editors

- ### Use comments for quick debugging / prototyping

---
hideInToc: true
layout: two-cols
---

#### **Basic Operators**

<div style="max-width: 350px;">
```python
# Arithmetic
2 + 3 # Addition
5 - 2 # Subtraction
3 * 4 # Multiplication
6 / 2 # Division
5 % 2 # Modulus
```
</div>

<div style="max-width: 350px;">
```python
# Comparison
3  > 2 # True
4 == 4 # True
5 != 3 # True
```
</div>

#### **Variables and Data Types**

<div style="max-width: 350px;">
```python
x        = 10      # Integer
y        = 3.14    # Float
name     = "Alice" # String
is_valid = True    # Boolean
```
</div>

::right::

#### **Strings**

<div style="max-width: 350px;">
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

#### **Lists**

<div style="max-width: 350px;">
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # First element
numbers.append(6)   # Add element
numbers.remove(3)   # Remove element
print(len(numbers)) # Length of list
numbers.sort()      # Sort list
```
</div>

- Lists are mutable and can hold mixed data types

```python
customer_info = ["Alice", 25, "New York", "Premium", True]
```

--- 
hideInToc: true
layout: two-cols
---

### Dictionaries

- Dictionaries hold mutable mappings of hashable keys to values
- Membership checks are fast: `"age" in person`
- View objects `.keys()`, `.values()`, `.items()` reflect live data; cast to `list()` only when you need a snapshot

##### Everyday operations

<div style="max-width: 400px;">

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


::right::

- Use `.get()`/`setdefault()` for optional keys; avoid `KeyError`s from direct indexing
- Nest dictionaries (e.g., parsed JSON) to represent hierarchical structures

##### Common patterns

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
--- 
hideInToc: true
layout: two-cols
---

### Loading structured files into dicts

<div style="max-width: 350px;">

#### JSON
```python
# JSON -> dict
import json

with open("data.json", "r") as f:
        data = json.load(f)  # dict (or nested dict/list)
```
</div>

&nbsp;

<div style="max-width: 350px;">

#### YAML 

```python
# YAML -> dict
# pip install pyyaml
import yaml

with open("data.yaml", "r") as f:
        data = yaml.safe_load(f)  # dict (or nested dict/list)
```
</div>

:: right::

<div style="max-width: 350px; margin-top: 35px;">

#### CSV

```python
# CSV -> list[dict] (one dict per row)
import csv

with open("data.csv", newline="") as f:
        rows = list(csv.DictReader(f))  # [{'col1': '...', 'col2': '...'}, ...]
```
</div>

&nbsp;

#### Excel

<div style="max-width: 350px;">

```python
# Excel -> list[dict] via pandas
# pip install pandas openpyxl
import pandas as pd

df   = pd.read_excel("data.xlsx", sheet_name=0)  # DataFrame
rows = df.to_dict(orient="records")             # list[dict]
```
</div>

--- 
hideInToc: true
layout: two-cols
---

#### Control Flow: Conditional Statements

<div style="max-width: 350px;">
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

#### Control Flow: Loops

<div style="max-width: 350px;">
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

::right::

#### Functions

<div style="max-width: 350px;">
```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```
</div>

- Functions help organize code into reusable blocks
- Use `return` to return a value from a function -->

#### Exception Handling

<div style="max-width: 350px;">
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")
```
</div>

- Use `try` and `except` to handle errors
- `finally` block always executes

---
hideInToc: true
---
#### Modules and Imports

<div style="max-width: 500px;">
```python
import math
print(math.sqrt(16))  # 4.0

from random import randint
print(randint(1, 10))  # Random number between 1 and 10
```
</div>

- Use `import` to bring in external modules
- `from module import function` imports specific functions

#### File Handling

<div style="max-width: 500px;">
```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```
</div>

- Use `with open()` to handle file operations safely

- `"r"` for reading, `"w"` for writing, `"a"` for appending
