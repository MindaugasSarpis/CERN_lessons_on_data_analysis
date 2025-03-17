---
background: /intro_background.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 7: Crash Course on Python Programming"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 7:

## Crash Course on Python Programming

---
hideInToc: true
---

# Useful Resources for starting with Python

- ## [Python Official Documentation](https://docs.python.org/)
- ## [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- ## [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- ## Free introductory courses on codecademy, coursera, udemy, etc.

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

- #### **Running python** 

  - Interactive mode: `python` or `ipython`

  - Script mode: `python script.py`

  - Use `print("Hello, World!")` to output text

- #### **Comments** 

<div style="max-width: 350px;">
```python
# This line does ...
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

::right::

#### **Variables and Data Types**

<div style="max-width: 350px;">
```python
x        = 10       # Integer
y        = 3.14     # Float
name     = "Alice"  # String
is_valid = True     # Boolean
```
</div>

#### **Basic Operators**

<div style="max-width: 350px;">
```python
# Arithmetic
2 + 3  # Addition
5 - 2  # Subtraction
3 * 4  # Multiplication
10 / 2  # Division
5 % 2  # Modulus
```
</div>

<div style="max-width: 350px;">
```python
# Comparison
3 > 2  # True
4 == 4  # True
5 != 3  # True
```
</div>

---
hideInToc: true
layout: two-cols
---

#### **Strings**

<div style="max-width: 350px;">
```python
s = "Hello, World!"
print(s[0])  # H (indexing)
print(s[-1])  # ! (negative indexing)
print(s[0:5])  # Hello (slicing)
print(len(s))  # Length of string
print(s.lower())  # Convert to lowercase
print(s.upper())  # Convert to uppercase
print(s.replace("World", "Python")) # Replace
```
</div>

#### **Lists**

<div style="max-width: 350px;">
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # First element
numbers.append(6)  # Add element
numbers.remove(3)  # Remove element
print(len(numbers))  # Length of list
numbers.sort()  # Sort list
```
</div>

- Lists are mutable and can hold mixed data types

```python
customer_info = ["Alice", 25, "New York", "Premium", True]
```

::right::

#### Dictionaries

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
person["age"] = 26  # Update value
person["city"] = "New York"  # Add key-value pair
print(person.keys())  # Get all keys
print(person.values())  # Get all values
```

- Dictionaries store key-value pairs and are mutable

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
