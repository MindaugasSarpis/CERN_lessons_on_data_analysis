# Crash Course on Python Programming

---

## Overview

**Duration**: ~120 minutes (2 h slot)

**Prerequisites**: L3 (Computer Science basics), L15 (Computing Infrastructure)

**Learning Objectives**:
- Write and run Python scripts from the command line and in an IDE
- Use core data types: strings, lists, and dictionaries
- Control program flow with conditionals, loops, and functions
- Handle files (text, JSON, CSV) and use built-in modules
- Debug common errors (SyntaxError, NameError, TypeError)

---

## Lecture Structure

### Part 1: Python Basics (25 min)
- Why Python? (popularity, readability, scientific ecosystem)
- Running Python: REPL vs scripts vs notebooks
- Variables, dynamic typing, `type()`
- Operators: arithmetic (`+`, `-`, `*`, `/`, `//`, `**`, `%`), comparison, logical (`and`, `or`, `not`, `in`)
- Built-in functions: `print()`, `len()`, `input()`, `range()`
- Comments and indentation (Python's signature feature)

### Part 2: Data Structures (30 min)
- **Strings**: indexing, slicing (`s[1:4]`), methods (`.upper()`, `.split()`, `.strip()`, `.replace()`), f-strings
- **Lists**: creation, append/remove, sorting, list comprehensions
- **Dictionaries**: key-value pairs, CRUD operations, `.keys()`, `.values()`, `.items()`, nested dicts
- Live demo: Build a particle data dictionary

### Part 3: Control Flow (20 min)
- `if` / `elif` / `else` with comparison operators
- `for` loops (over lists, ranges, strings, dicts)
- `while` loops and `break` / `continue`
- `range()` patterns: `range(n)`, `range(a, b)`, `range(a, b, step)`
- Interactive: Loop exercises in monaco-run

### Part 4: Functions & Patterns (25 min)
- Defining functions: `def`, parameters, `return`
- Default arguments and keyword arguments
- Exception handling: `try` / `except` / `finally`
- Useful patterns: `enumerate()`, `zip()`, list comprehensions
- Interactive: Write a function exercise

### Part 5: Files & Modules (20 min)
- `import` and `from ... import`
- File I/O: `open()`, `read()`, `write()`, context managers (`with`)
- Loading structured data: JSON (`json.load`), CSV (`csv.reader`), YAML
- Common errors gallery: SyntaxError, IndentationError, NameError, TypeError

### Part 6: Mini Projects (30 min)
- Sensor temperature analysis (read CSV, compute stats, flag outliers)
- Text-based bar chart (word frequency → horizontal bar visualization)
- Students work independently, instructor circulates

---

## Teaching Tips

### Common Student Struggles

1. **Indentation errors**
   - Emphasise: Python uses indentation instead of braces — it's not optional
   - Show how mixing tabs and spaces causes `IndentationError`
   - Configure VS Code to insert 4 spaces on Tab

2. **Mutable vs immutable confusion**
   - Lists are mutable (`append` changes the list in place)
   - Strings are immutable (`upper()` returns a NEW string)
   - Demo: `a = [1,2]; b = a; b.append(3)` — both change!

3. **Off-by-one errors with `range()`**
   - `range(5)` gives `0,1,2,3,4` — NOT 5
   - `range(1,5)` gives `1,2,3,4` — NOT including 5
   - Draw the number line on the board

4. **Dictionary KeyError**
   - Accessing a missing key crashes the program
   - Show `.get(key, default)` as a safe alternative
   - Show `if key in dict:` pattern

5. **f-string syntax**
   - Common mistake: forgetting the `f` prefix
   - Show the difference: `"x = {x}"` vs `f"x = {x}"`

### Interactive Elements

- **Live coding**: Type along with students — don't just show finished code
- **Predict the output**: Show code, ask students what it prints before running
- **Error spotting**: Show broken code, have students find the bug
- **monaco-run slides**: Let students experiment directly in the browser

### Hands-On Exercises

**Exercise 1** (Easy): Variables and types
```python
# Create variables for a particle: name, mass, charge
# Print a formatted summary using f-strings
name = "muon"
mass = 105.7  # MeV
charge = -1
print(f"The {name} has mass {mass} MeV and charge {charge}")
```

**Exercise 2** (Medium): List and dictionary operations
```python
# Given a list of measurements, compute mean and find the max
measurements = [23.1, 25.4, 22.8, 24.6, 23.9, 25.1, 22.5]
mean = sum(measurements) / len(measurements)
maximum = max(measurements)
```

**Exercise 3** (Advanced): Mini data analysis
```python
# Read a CSV of sensor data
# Compute average temperature per sensor
# Flag readings above a threshold
```

---

## Common Questions & Answers

**Q**: Why Python and not C++ or Julia?
**A**: Python has the gentlest learning curve, the largest ecosystem for data analysis (NumPy, Pandas, matplotlib, scikit-learn), and is used at CERN alongside C++ (ROOT). Julia is fast but has a smaller community. We teach concepts that transfer to any language.

**Q**: Do I need to memorise all these methods?
**A**: No! Knowing they exist is enough. Use `help()`, documentation, and autocomplete in VS Code. Over time, the common ones become muscle memory.

**Q**: What's the difference between `=` and `==`?
**A**: `=` assigns a value (`x = 5`). `==` checks equality (`x == 5` returns `True` or `False`). This trips up almost every beginner.

**Q**: Why do lists start at index 0?
**A**: Historical convention from C. The index is an *offset* from the start. Most languages use 0-based indexing (Python, C, Java, JavaScript). Some use 1-based (R, MATLAB, Fortran).

**Q**: When should I use a list vs a dictionary?
**A**: Use a **list** for ordered collections of similar items (measurements, filenames). Use a **dictionary** when items have meaningful labels/keys (particle properties, configuration settings).

---

## Key Code Snippets

### Python cheat sheet — types and operators
```python
# Types
x = 42          # int
y = 3.14        # float
s = "hello"     # str
b = True        # bool
n = None        # NoneType

# Arithmetic
10 / 3    # 3.333...  (true division)
10 // 3   # 3         (floor division)
10 % 3    # 1         (modulo)
2 ** 10   # 1024      (exponentiation)

# Logical
True and False   # False
True or False    # True
not True         # False
3 in [1, 2, 3]   # True
```

### String formatting
```python
name, mass = "Higgs", 125.1
print(f"The {name} boson has mass {mass:.1f} GeV")
# Output: The Higgs boson has mass 125.1 GeV
```

### List comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dictionary operations
```python
particle = {"name": "muon", "mass": 105.7, "charge": -1}
particle["spin"] = 0.5              # add key
mass = particle.get("mass", 0)      # safe access
for key, val in particle.items():   # iterate
    print(f"{key}: {val}")
```

### File I/O
```python
# Reading
with open("data.txt") as f:
    lines = f.readlines()

# Writing
with open("output.txt", "w") as f:
    f.write("result: 42\n")

# JSON
import json
with open("config.json") as f:
    config = json.load(f)
```

### enumerate and zip
```python
particles = ["electron", "muon", "tau"]
masses = [0.511, 105.7, 1777]

for i, name in enumerate(particles):
    print(f"{i}: {name}")

for name, mass in zip(particles, masses):
    print(f"{name}: {mass} MeV")
```

---

## Time Estimates

- Lecture (Parts 1-5): 100 min
- Live demos and interactive exercises: 30 min
- Mini projects (Part 6): 30 min
- Q&A throughout: 20 min
- **Total**: ~180 min (full day session)

---

## Resources for Students

- [Python official tutorial](https://docs.python.org/3/tutorial/)
- [CS50P — Introduction to Programming with Python](https://cs50.harvard.edu/python/)
- [Real Python — beginner tutorials](https://realpython.com/)
- [Python cheat sheet (comprehensive)](https://www.pythoncheatsheet.org/)

---

## Assessment Ideas

- **Quiz**: "What does `range(2, 10, 3)` produce?" / "What's the output of this code?"
- **Practical**: "Write a function that takes a list of numbers and returns only the positive ones"
- **Mini project**: Extend the sensor analysis exercise to read real data and produce a summary report
- **Code review**: Give students buggy code to fix (5 common errors embedded)
