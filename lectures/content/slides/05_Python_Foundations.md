---
layout: cover
title: "Python Foundations"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python Foundations

##### <span class="aims-badge">🔧 tool-agnostic · ⚙️ automation</span>

<!--
**Say:** no Python is assumed today. Six steps: values and their types, containers that hold many values, the two lines that repeat and choose, functions and classes, modules, and where the rest of Python comes from.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# A program is a text of instructions that the computer carries out one after another. Python is a language for writing that text

<!--
**Say:** a recipe for the computer, written in a language strict enough that a program can follow it.
(~1 min)
-->

---
hideInToc: true
---

# What Happens When Python Runs

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **A program of three lines**

```py
mean = 7.16
fahrenheit = mean * 9 / 5 + 32
print(fahrenheit)
```

```text
44.888
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **The interpreter**

1. reads the text from the top, one line at a time
2. carries out each line before it reads the next
3. writes to the screen only what `print` gives it

</div>

</div>

<div class="note-text mt-md"><strong>Python</strong> is the language; <code>python</code> is the program that reads it, the <strong>interpreter</strong>. Lines can be typed into it one by one, or kept in a text file ending in <code>.py</code>, a <strong>script</strong>.</div>

<!--
**Say:** the processor itself only runs machine code (Lecture 03); `python` is machine code that reads Python text and does what it says.
**Ask:** what does the program print? 7.16 °C in Fahrenheit, 44.888.
(~2 min)
-->

---
hideInToc: true
---

# The File of Today: `weather.csv`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **The first four lines**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
2016-01-01T02:00,-5.5,95,2.7
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **What it holds**

| | |
| --- | --- |
| rows | 87 672, one per hour |
| years | 2016 to 2025 |
| missing hours | 120, written as −999 |
| mean temperature | 7.16 °C |

</div>

</div>

<div class="note-text mt-md">One weather station, one line of text per hour: the time, the temperature in °C, the humidity in % and the wind in m/s, separated by commas.</div>

<!--
**Say:** today's examples come from this file; Part 3 computes 7.16 in twelve lines of Python.
**Ask:** what would a mean over all rows give, with the −999 hours counted as temperatures? Lower: 5.78.
(~2 min)
-->

---
hideInToc: true
---

<div class="card card-primary card-glass pad-compact table-compact mt-lg">

| Part | Question | Answer |
| --- | --- | --- |
| 1 | What is a value in Python, and what can it do? | ? |
| 2 | How are values kept by name, and in larger objects? | ? |
| 3 | How do `for` and `if` turn 87 672 lines into 7.16? | ? |
| 4 | How is a step written once and used again? | ? |
| 5 | How do several scripts share one file of functions? | ? |
| 6 | Where does the rest of Python come from, and which version arrives? | ? |

</div>

<!--
**Say:** one question per part; the last column is filled at the end.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Values and **Types**

Part 1: what is a value in Python, and what can it do?

<!--
(~1 min)
-->

---
hideInToc: true
---

# A First Line: `print`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
print("Hello")
```
```py
print("Hello")               # Hello
```
```py {2}
print("Hello")               # Hello
print(7.16)
```
```py {2}
print("Hello")               # Hello
print(7.16)                  # 7.16
```
```py {3}
print("Hello")               # Hello
print(7.16)                  # 7.16
print(7.16 * 9 / 5 + 32)
```
```py {3}
print("Hello")               # Hello
print(7.16)                  # 7.16
print(7.16 * 9 / 5 + 32)     # 44.888
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Reading a line**

- `print(…)` shows the value between the brackets
- text stands in quotes; numbers do not
- `*` multiplies, `/` divides: Python works out the line first
- `#` starts a **comment**: Python skips the rest of the line. On these slides a comment shows what the line prints

</div>

</div>

<!--
**Do:** before each result appears, ask the room what will be printed.
**Say:** the third line is the conversion to Fahrenheit: multiplication and division before addition, as in arithmetic.
(~2 min)
-->

---
hideInToc: true
---

# A Name for a Value: `=`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
mean = 7.16
```
```py {2}
mean = 7.16
print(mean)
```
```py {2}
mean = 7.16
print(mean)                       # 7.16
```
```py {3}
mean = 7.16
print(mean)                       # 7.16
fahrenheit = mean * 9 / 5 + 32
```
```py {4}
mean = 7.16
print(mean)                       # 7.16
fahrenheit = mean * 9 / 5 + 32
print(fahrenheit)                 # 44.888
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **`=` in Python**

1. work out the right side
2. put the name on the result

A name with its value is a **variable**. A name has letters, digits and `_`, no spaces, and `Mean` is not `mean`.

</div>

</div>

<!--
**Ask:** step 2: what will `print(mean)` show, the word mean or 7.16? Without quotes, `mean` is a name and Python uses its value.
**Say:** `=` is not the equals of mathematics: it is an instruction, "put this name on that value".
(~2 min)
-->

---
hideInToc: true
---

# Add One to a Count: `count = count + 1`

<div class="grid-2 mt-md gap-md">

<div>

````md magic-move {lines: true}
```py
count = 0
count = count + 1
```
```py {3}
count = 0
count = count + 1
print(count)
```
```py {3}
count = 0
count = count + 1
print(count)   # 1
```
```py {3-5}
count = 0
count = count + 1
count = count + 1
count = count + 1
print(count)   # 3
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **`=` in Python**

1. work out the right side, with the value the name has now
2. put the name on the result

`count = count + 1` is not an equation: it moves `count` from 0 to 1.

</div>

</div>

<!--
**Ask:** before the fourth step: what does `print(count)` show?
**Say:** every count and every sum over a file is this one line, run once per row.
(~2 min)
-->

---
hideInToc: true
---

# Every Value Has a **Type**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🏷️ **Four basic types**

| Value | Type | What it is |
| --- | --- | --- |
| `87672` | `int` | a whole number |
| `7.16` | `float` | a number with a point |
| `"-4.4"` | `str` | text, in quotes |
| `True` | `bool` | `True` or `False` |

</div>

<div>

````md magic-move {lines: true}
```py
print(type(87672))
```
```py
print(type(87672))    # <class 'int'>
```
```py {2}
print(type(87672))    # <class 'int'>
print(type(7.16))     # <class 'float'>
```
```py {3}
print(type(87672))    # <class 'int'>
print(type(7.16))     # <class 'float'>
print(type("-4.4"))   # <class 'str'>
```
```py {4}
print(type(87672))    # <class 'int'>
print(type(7.16))     # <class 'float'>
print(type("-4.4"))   # <class 'str'>
print(type(True))     # <class 'bool'>
```
````

</div>

</div>

<div class="note-text mt-md">The <strong>type</strong> decides what can be done with a value: numbers add up, texts are joined. <code>type()</code> asks a value for its type.</div>

<!--
**Ask:** before the third line: `"-4.4"` with quotes, a number or text?
**Say:** Lecture 03 stored whole numbers, floats and text as bits in different ways; Python keeps the type with every value.
(~2 min)
-->

---
hideInToc: true
---

# Arithmetic with `int` and `float`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
hours = 87672             # ten years of hours
```
```py {2}
hours = 87672             # ten years of hours
print(hours / 24)         # 3653.0
```
```py {3}
hours = 87672             # ten years of hours
print(hours / 24)         # 3653.0
print(hours // 24)        # 3653
```
```py {4}
hours = 87672             # ten years of hours
print(hours / 24)         # 3653.0
print(hours // 24)        # 3653
print(hours % 24)         # 0
```
```py {5}
hours = 87672             # ten years of hours
print(hours / 24)         # 3653.0
print(hours // 24)        # 3653
print(hours % 24)         # 0
print(2 ** 10)            # 1024
```
````

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ➗ **Operators**

| | |
| --- | --- |
| `+ - *` | add, subtract, multiply |
| `/` | divide: always a `float` |
| `//` | the whole part: an `int` |
| `%` | the remainder |
| `**` | the power |

</div>

</div>

<!--
**Ask:** step 2: 87672 / 24, will Python print 3653 or 3653.0?
**Say:** 3653 days: ten years with three leap years. The remainder 0 says the hours fill whole days.
(~2 min)
-->

---
hideInToc: true
---

# A `float` Is Rounded

````md magic-move {lines: true}
```py
print(0.1 + 0.2)               # 0.30000000000000004
```
```py {2}
print(0.1 + 0.2)               # 0.30000000000000004
print(0.1 + 0.2 == 0.3)        # False
```
```py {3}
print(0.1 + 0.2)               # 0.30000000000000004
print(0.1 + 0.2 == 0.3)        # False
print(round(0.1 + 0.2, 2))     # 0.3
```
````

<div class="note-text mt-md">A <code>float</code> is stored in 64 bits, about 16 decimal digits (Lecture 03). 0.1 has no end in binary, so the nearest stored number is used and every sum is rounded a little. <code>==</code> asks whether two values are equal; <code>round(x, 2)</code> keeps two decimals, for printing.</div>

<!--
**Ask:** step 2: is 0.1 + 0.2 equal to 0.3?
**Say:** not a fault of Python: every language with float64 prints the same. Measured values are compared with a tolerance, never with `==`.
(~2 min)
-->

---
hideInToc: true
---

# Compare: `True` or `False`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
hours = 87672
print(hours > 80000)       # True
```
```py {3-4}
hours = 87672
print(hours > 80000)       # True
temp = -999.0
print(temp == -999)        # True
```
```py {5}
hours = 87672
print(hours > 80000)       # True
temp = -999.0
print(temp == -999)        # True
print(temp != -999)        # False
```
```py {6}
hours = 87672
print(hours > 80000)       # True
temp = -999.0
print(temp == -999)        # True
print(temp != -999)        # False
print("-999" == -999)      # False
```
````

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ⚖️ **Comparisons**

| | |
| --- | --- |
| `==` | equal |
| `!=` | not equal |
| `<  >` | less, greater |
| `<= >=` | or equal |

The answer is a `bool`. `=` names a value; `==` compares two.

</div>

</div>

<!--
**Ask:** the last line: the text "-999" and the number −999, equal?
**Say:** never: text is not a number. The −999 rows of the file will be found with exactly this comparison.
(~2 min)
-->

---
hideInToc: true
---

# A `list`: Values in Order

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
temps = [-4.4, -4.8, -5.5]   # 00:00 to 02:00
```
```py {2}
temps = [-4.4, -4.8, -5.5]   # 00:00 to 02:00
print(temps[0])              # -4.4
```
```py {3}
temps = [-4.4, -4.8, -5.5]   # 00:00 to 02:00
print(temps[0])              # -4.4
print(len(temps))            # 3
```
```py {4}
temps = [-4.4, -4.8, -5.5]   # 00:00 to 02:00
print(temps[0])              # -4.4
print(len(temps))            # 3
temps.append(-6.0)           # 03:00
```
```py {5}
temps = [-4.4, -4.8, -5.5]   # 00:00 to 02:00
print(temps[0])              # -4.4
print(len(temps))            # 3
temps.append(-6.0)           # 03:00
print(temps)                 # [-4.4, -4.8, -5.5, -6.0]
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **A list**

- square brackets, items separated by commas
- each item has a position, counted from 0: `temps[0]` is the first
- it can grow: `append` is a method of every list

</div>

</div>

<!--
**Ask:** step 2: which position holds −4.4? Position 0, the first.
**Say:** the first three hours of 1 January 2016; the list keeps them in the order they came. Counting from 0 is how Python counts positions everywhere: in a text too.
(~2 min)
-->

---
hideInToc: true
---

# Text: a `str`, Position by Position

````md magic-move {lines: true}
```py
line = "2016-01-01T00:00,-4.4,93,2.5"
```
```py {2}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(len(line))        # 28
```
```py {3}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(len(line))        # 28
print(line[0])          # 2
```
```py {4}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(len(line))        # 28
print(line[0])          # 2
print(line[0:4])        # 2016
```
```py {5}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(len(line))        # 28
print(line[0])          # 2
print(line[0:4])        # 2016
print(line[5:7])        # 01
```
````

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-secondary card-glass pad-compact">

```text
char  2 0 1 6 - 0 1 - 0 1
pos   0 1 2 3 4 5 6 7 8 9
```

</div>

<div class="note-text">A <strong>str</strong> is a row of characters with positions, like the items of a list: <code>len</code> counts them, <code>line[0]</code> is the first. <code>[start:stop]</code> takes a piece and stops before <code>stop</code>: <code>[0:4]</code> is the year, <code>[5:7]</code> the month.</div>

</div>

<!--
**Do:** point at the positions under the characters while the steps appear.
**Ask:** step 5: which characters are positions 5 and 6?
(~3 min)
-->

---
hideInToc: true
---

# Text Is Not a Number: `float()`

````md magic-move {lines: true}
```py
temp = "-4.4"
print(temp + "1")         # -4.41
```
```py {3}
temp = "-4.4"
print(temp + "1")         # -4.41
print(temp + 1)           # TypeError: can only concatenate str (not "int") to str
```
```py {3-4}
temp = "-4.4"
print(temp + "1")         # -4.41
number = float(temp)
print(number + 1)         # -3.4000000000000004
```
````

<div class="note-text mt-md">For two texts <code>+</code> joins them; a text and a number do not add, and Python stops with a <code>TypeError</code>. <code>float("-4.4")</code> makes the number from the text, <code>int("93")</code> a whole number, <code>str(7.16)</code> text again. A file holds text: every value read from it starts as a <code>str</code>.</div>

<!--
**Ask:** step 1: what is "-4.4" + "1"? Text joined to text: -4.41, not −3.4.
**Say:** the tail of the last result is the rounding of the float slide.
(~2 min)
-->

---
hideInToc: true
---

# Objects Have **Methods**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
name = "weather"
print(name.upper())             # WEATHER
```
```py {3-4}
name = "weather"
print(name.upper())             # WEATHER
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line.split(","))
```
```py {4-5}
name = "weather"
print(name.upper())             # WEATHER
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line.split(","))
# ['2016-01-01T00:00', '-4.4', '93', '2.5']
```
```py {6}
name = "weather"
print(name.upper())             # WEATHER
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line.split(","))
# ['2016-01-01T00:00', '-4.4', '93', '2.5']
print((7.16).is_integer())      # False
```
````

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📦 **An object has**

- a **type**: `str`
- a **value**: `"weather"`
- **methods**: functions of its type, written after a dot

| function | method |
| --- | --- |
| `len(line)` | `line.split(",")` |

</div>

</div>

<!--
**Say:** in Python every value is an **object**. A `str` can split itself at commas; a `float` can say whether it is whole.
**Ask:** step 3: what does `split(",")` hand back? A list of four texts, in square brackets.
**If asked:** `dir(name)` lists every method a `str` has.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Containers and **Objects**

Part 2: how are values kept by name, and in larger objects?

<!--
(~1 min)
-->

---
hideInToc: true
---

# A `dict`: Values Found by a **Name**

````md magic-move {lines: true}
```py
row = {"temp_c": -4.4, "humidity_pct": 93}
```
```py {2}
row = {"temp_c": -4.4, "humidity_pct": 93}
print(row["temp_c"])        # -4.4
```
```py {3}
row = {"temp_c": -4.4, "humidity_pct": 93}
print(row["temp_c"])        # -4.4
row["wind_ms"] = 2.5
```
```py {4}
row = {"temp_c": -4.4, "humidity_pct": 93}
print(row["temp_c"])        # -4.4
row["wind_ms"] = 2.5
print(row)                  # {'temp_c': -4.4, 'humidity_pct': 93, 'wind_ms': 2.5}
```
```py {5}
row = {"temp_c": -4.4, "humidity_pct": 93}
print(row["temp_c"])        # -4.4
row["wind_ms"] = 2.5
print(row)                  # {'temp_c': -4.4, 'humidity_pct': 93, 'wind_ms': 2.5}
print(row["rain_mm"])       # KeyError: 'rain_mm'
```
````

<div class="note-text mt-md">A <strong>dictionary</strong> holds pairs <code>key: value</code> in curly brackets. A list finds a value by its position, a dictionary by its key, here the name of the column. Assigning to a new key adds it; asking for a key that is not there stops with <code>KeyError</code>.</div>

<!--
**Ask:** step 2: what does `row["temp_c"]` give? And step 5, a key that is not there?
**Say:** the dictionary is one row of the file with the header's names attached.
(~2 min)
-->

---
hideInToc: true
---

# Four **Containers**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Container | Written | Finds a value by | Can change | Example |
| --- | --- | --- | --- | --- |
| **list** | `[ … ]` | position | yes | `[-4.4, -4.8, -5.5]` |
| **tuple** | `( … )` | position | no | `("2016-01-01T00:00", -4.4)` |
| **dict** | `{key: value}` | key | yes | `{"temp_c": -4.4}` |
| **set** | `{ … }` | (each value once) | yes | `{"2016", "2017"}` |

</div>

<div class="note-text mt-md">A container holds any objects, other containers too. A list of dictionaries is a table: one dictionary per row.</div>

<!--
**Say:** a tuple is a record that must stay as it was read; a set answers "which different values are there".
**Ask:** which container for the temperature of every hour, in order? A list. For one row with column names? A dict.
(~2 min)
-->

---
hideInToc: true
---

# Objects Inside Objects: a **Table**

````md magic-move {lines: true}
```py
rows = [{"time": "00:00", "temp_c": -4.4},
        {"time": "01:00", "temp_c": -4.8}]
```
```py {3}
rows = [{"time": "00:00", "temp_c": -4.4},
        {"time": "01:00", "temp_c": -4.8}]
print(len(rows))              # 2
```
```py {4}
rows = [{"time": "00:00", "temp_c": -4.4},
        {"time": "01:00", "temp_c": -4.8}]
print(len(rows))              # 2
print(rows[1])                # {'time': '01:00', 'temp_c': -4.8}
```
```py {5}
rows = [{"time": "00:00", "temp_c": -4.4},
        {"time": "01:00", "temp_c": -4.8}]
print(len(rows))              # 2
print(rows[1])                # {'time': '01:00', 'temp_c': -4.8}
print(rows[1]["temp_c"])      # -4.8
```
````

<div class="note-text mt-md">Read from the outside in: <code>rows[1]</code> is the second dictionary, and <code>["temp_c"]</code> picks a value inside it.</div>

<!--
**Ask:** step 4: what is `rows[1]`, a number or a dictionary?
**Say:** larger objects are built the same way: objects that hold objects, each with its own methods.
(~2 min)
-->

---
hideInToc: true
---

# A Larger Object: a **Figure**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
import matplotlib.pyplot as plt
```
```py {2}
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
```
```py {3}
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
print(type(fig))   # <class 'matplotlib.figure.Figure'>
```
```py {4}
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
print(type(fig))   # <class 'matplotlib.figure.Figure'>
ax.plot([0, 1, 2, 3], [-4.4, -4.8, -5.5, -6.0])
```
```py {5}
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
print(type(fig))   # <class 'matplotlib.figure.Figure'>
ax.plot([0, 1, 2, 3], [-4.4, -4.8, -5.5, -6.0])
plt.show()
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 🖼️ **Objects inside objects**

```text
Figure          the image
└─ Axes         one plot area
   └─ Line2D    one line of data
```

`import` (Part 5) brings in a package that is not part of Python (Part 6). `plt.subplots()` hands back two objects, named `fig` and `ax`.

</div>

</div>

<!--
**Say:** a figure is an object like −4.4, with more inside: axes, lines, labels, each an object with methods such as `ax.plot` and `fig.savefig`.
**Ask:** step 4: two lists go into `ax.plot`. Which is the hour and which the temperature?
(~2 min)
-->

---
hideInToc: true
---

# Draw the Figure

```py {monaco-run} {autorun:false}
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.3), layout="constrained")
print(type(fig))   # <class 'matplotlib.figure.Figure'>
hours = [0, 1, 2, 3]
ax.plot(hours, [-4.4, -4.8, -5.5, -6.0])
ax.set(xlabel="hour", ylabel="temp_c")
plt.show()
```

<!--
**Do:** press ▶; the first run waits a few seconds for matplotlib to load.
**Ask:** change `figsize=(6, 1.3)` to `(6, 1)` and run again: what changes?
**If asked:** `len(fig.axes)` is 1 and `len(ax.lines)` is 1: each object keeps a list of the objects inside it.
(~2 min)
-->

---
hideInToc: true
---

# An Object from Text: **JSON**

````md magic-move {lines: true}
```py
import json
text = '{"temp_c": 8.7, "unit": "°C"}'
```
```py {3}
import json
text = '{"temp_c": 8.7, "unit": "°C"}'
answer = json.loads(text)
```
```py {4}
import json
text = '{"temp_c": 8.7, "unit": "°C"}'
answer = json.loads(text)
print(type(text), type(answer))   # <class 'str'> <class 'dict'>
```
```py {5}
import json
text = '{"temp_c": 8.7, "unit": "°C"}'
answer = json.loads(text)
print(type(text), type(answer))   # <class 'str'> <class 'dict'>
print(answer["temp_c"])           # 8.7
```
````

<div class="note-text mt-md"><strong>JSON</strong> is a way of writing numbers, texts, lists and dictionaries as text, so that programs can send them to each other. <code>json.loads</code> reads that text and builds the Python objects; <code>json</code> comes with every Python.</div>

<!--
**Ask:** step 3: before and after `json.loads`, what has changed? The same content, first as one text, then as a dictionary.
**Say:** a weather service on the internet answers in JSON.
(~2 min)
-->

---
hideInToc: true
---

# The Answer of a Weather Service: a `dict` of `dict`s

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 🌐 **api.open-meteo.com, 18 Oct 2026, 10:30**

```text
{"latitude": 54.68259,
 "longitude": 25.273773,
 "elevation": 95.0,
 "current_units": {"temperature_2m": "°C",
                   "wind_speed_10m": "km/h"},
 "current": {"time": "2026-10-18T10:30",
             "temperature_2m": 8.7,
             "wind_speed_10m": 10.4}}
```

</div>

<div>

````md magic-move {lines: true}
```py
print(type(answer))              # <class 'dict'>
```
```py {2}
print(type(answer))              # <class 'dict'>
print(type(answer["current"]))   # <class 'dict'>
```
```py {3}
print(type(answer))              # <class 'dict'>
print(type(answer["current"]))   # <class 'dict'>
print(answer["current"]["temperature_2m"])  # 8.7
```
```py {4-5}
print(type(answer))              # <class 'dict'>
print(type(answer["current"]))   # <class 'dict'>
print(answer["current"]["temperature_2m"])  # 8.7
units = answer["current_units"]
print(units["temperature_2m"])   # °C
```
````

</div>

</div>

<div class="note-text mt-md">The answer of api.open-meteo.com for Vilnius, read with <code>json.loads</code> into <code>answer</code>: a dictionary whose values are dictionaries, read one key at a time.</div>

<!--
**Say:** five numbers about Vilnius right now, and the units beside them. Square brackets twice: the dictionary inside the dictionary.
**If asked:** a few keys are left out here (`generationtime_ms`, `timezone`, …); the answer has nine.
(~2 min)
-->

---
hideInToc: true
---

# Ask the Weather Service Now

```py {monaco-run} {autorun:false}
import json
from pyodide.http import open_url   # in a browser; urllib on a laptop
url = ("https://api.open-meteo.com/v1/forecast?latitude=54.69"
       "&longitude=25.28&current=temperature_2m,wind_speed_10m")
answer = json.loads(open_url(url).read())
print(len(answer))                         # 9 keys
print(answer["current"]["time"])           # 2026-10-18T10:30 when written
print(answer["current"]["temperature_2m"]) # 8.7 when written
```

<div class="note-text mt-md">The same three steps as for <code>weather.csv</code>: text arrives, becomes objects, one value is picked out. The block needs the internet; its answer changes every 15 minutes.</div>

<!--
**Do:** press ▶. Compare the temperature with the window.
**Say:** the object was built a second ago on a server in another country; to the program it is a dictionary like `row`.
**If asked:** on a laptop the second line is `from urllib.request import urlopen`, and `urlopen(url).read()` gives the bytes.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Combine Objects: `for` and **`if`**

Part 3: how do `for` and `if` turn 87 672 lines into 7.16?

<!--
**Say:** the values and containers are known; now the two lines that repeat a step and choose between steps.
(~1 min)
-->

---
hideInToc: true
---

# `for`: Once for Each **Item**

<div class="grid-2 mt-md gap-md">

<div>

````md magic-move {lines: true}
```py
temps = [-4.4, -4.8, -5.5, -6.0]
for t in temps:
    print(t)
```
```py {2,4}
temps = [-4.4, -4.8, -5.5, -6.0]
total = 0.0
for t in temps:
    total = total + t
    print(t)
```
```py {5}
temps = [-4.4, -4.8, -5.5, -6.0]
total = 0.0
for t in temps:
    total = total + t
    print(t, total)
```
```py {6}
temps = [-4.4, -4.8, -5.5, -6.0]
total = 0.0
for t in temps:
    total = total + t
    print(t, total)
print(total / len(temps))   # -5.175
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **The rules**

- The `for` line ends with `:`
- The **block** is the lines below it, indented by 4 spaces
- `t` names each item in turn; the block runs once for each
- The first line that is not indented runs after the last item

</div>

</div>

<!--
**Ask:** after step 1: how many lines does it print? Four, one per item.
**Say:** a start value before the loop, an update inside it, the result after it. Every count and sum over a file has these three places.
(~2 min)
-->

---
hideInToc: true
---

# The Loop, Turn by **Turn**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The loop**

```py
temps = [-4.4, -4.8, -5.5, -6.0]
total = 0.0
for t in temps:
    total = total + t
    print(t, total)
print(total / len(temps))
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔁 **Each turn**

| Turn | `t` | `total` after line 4 |
| --- | --- | --- |
| before | | 0.0 |
| <span v-click="1">1</span> | <span v-click="1">−4.4</span> | <span v-click="1">−4.4</span> |
| <span v-click="2">2</span> | <span v-click="2">−4.8</span> | <span v-click="2">−9.2</span> |
| <span v-click="3">3</span> | <span v-click="3">−5.5</span> | <span v-click="3">−14.7</span> |
| <span v-click="4">4</span> | <span v-click="4">−6.0</span> | <span v-click="4">−20.7</span> |
| <span v-click="5">after</span> | | <span v-click="5">−20.7 / 4 = −5.175</span> |

</div>

</div>

<!--
**Do:** before each click, have the room say the next `total`.
**Say:** the computer does exactly this, 87 672 times for `weather.csv`.
(~2 min)
-->

---
hideInToc: true
---

# Choose a Block: `if`, `elif`, `else`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
temp = -999.0
if temp == -999:
    print("missing")         # printed
```
```py {4-5}
temp = -999.0
if temp == -999:
    print("missing")         # printed
else:
    print("measured")
```
```py {1,3,5}
temp = -4.4
if temp == -999:
    print("missing")
else:
    print("measured")        # printed
```
```py {4-5,7}
temp = -4.4
if temp == -999:
    print("missing")
elif temp < 0:
    print("below freezing")  # printed
else:
    print("measured")
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **The rules**

- `==` asks: equal? The answer is a `bool`
- The conditions are tried from the top; the first `True` one runs its block
- `elif` and `else` can be left out

</div>

</div>

<!--
**Ask:** at the last step, −4.4 is also "not missing": why "below freezing" and not "measured"? The first true condition wins.
**Say:** `=` puts a name on a value; `==` compares two values.
(~2 min)
-->

---
hideInToc: true
---

# Skip the −999 Rows: `continue`

````md magic-move {lines: true}
```py
temps = [23.6, -999.0, -999.0, 21.9]   # 21 July 2019 23:00, two marks, 27 July 00:00
total = 0.0
count = 0
for temp in temps:
    total = total + temp
    count = count + 1
print(count, total / count)            # 4 -488.125
```
```py {5-6}
temps = [23.6, -999.0, -999.0, 21.9]   # 21 July 2019 23:00, two marks, 27 July 00:00
total = 0.0
count = 0
for temp in temps:
    if temp == -999:
        continue                       # on to the next item at once
    total = total + temp
    count = count + 1
print(count, total / count)            # 2 22.75
```
````

<div class="note-text mt-md"><code>continue</code> ends this turn of the loop: the two lines below it are skipped for a −999 row.</div>

<!--
**Ask:** with the two marks in: what is the mean? −488.125 °C. And after the two new lines?
**Say:** the two hours around the gap give 22.75, a July night. The marks must be left out before any arithmetic.
(~2 min)
-->

---
hideInToc: true
---

# A Loop over the Lines of a **File**

````md magic-move {lines: true}
```py
lines = ["time,temp_c,humidity_pct,wind_ms",
         "2016-01-01T00:00,-4.4,93,2.5",
         "2016-01-01T01:00,-4.8,95,2.6",
         "2016-01-01T02:00,-5.5,95,2.7"]
for line in lines:
    print(line)
```
```py {5}
lines = ["time,temp_c,humidity_pct,wind_ms",
         "2016-01-01T00:00,-4.4,93,2.5",
         "2016-01-01T01:00,-4.8,95,2.6",
         "2016-01-01T02:00,-5.5,95,2.7"]
for line in lines[1:]:
    print(line)
```
```py {6-7}
lines = ["time,temp_c,humidity_pct,wind_ms",
         "2016-01-01T00:00,-4.4,93,2.5",
         "2016-01-01T01:00,-4.8,95,2.6",
         "2016-01-01T02:00,-5.5,95,2.7"]
for line in lines[1:]:
    parts = line.split(",")
    print(float(parts[1]))
```
```py {5,8-9}
lines = ["time,temp_c,humidity_pct,wind_ms",
         "2016-01-01T00:00,-4.4,93,2.5",
         "2016-01-01T01:00,-4.8,95,2.6",
         "2016-01-01T02:00,-5.5,95,2.7"]
total = 0.0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
print(total)    # -14.7
```
````

<div class="note-text mt-md">The first four lines of <code>weather.csv</code> as a list of strings. <code>lines[1:]</code> is every line but the first, the header.</div>

<!--
**Ask:** why `lines[1:]`? What would `float` do with the header's second part, `temp_c`?
**Say:** inside the loop: cut, pick part 1, convert, add. The same lines run on 3 lines and on 87 672.
(~2 min)
-->

---
hideInToc: true
---

# Read a File: `open`

````md magic-move {lines: true}
```py
text = open("data/raw/weather.csv").read()
```
```py {2}
text = open("data/raw/weather.csv").read()
print(len(text))          # 2515215
```
```py {3}
text = open("data/raw/weather.csv").read()
print(len(text))          # 2515215
lines = text.splitlines()
```
```py {4}
text = open("data/raw/weather.csv").read()
print(len(text))          # 2515215
lines = text.splitlines()
print(len(lines))         # 87673
```
```py {5}
text = open("data/raw/weather.csv").read()
print(len(text))          # 2515215
lines = text.splitlines()
print(len(lines))         # 87673
print(lines[1])           # 2016-01-01T00:00,-4.4,93,2.5
```
````

<div class="note-text mt-md"><code>open</code> finds the file, and its method <code>read</code> hands back all of the text as one <code>str</code> of 2 515 215 characters. <code>splitlines</code> cuts it at the line ends into a list of 87 673 strings: the header, then one line per hour. The path starts at the folder the program runs in.</div>

<!--
**Ask:** step 4: 87 673 lines, and the file has 87 672 hours. Where is the extra line? The header, `lines[0]`.
**If asked:** the slides' runnable blocks work in the browser and cannot read a file on a laptop, so this one is shown, not run.
(~2 min)
-->

---
hideInToc: true
---

# The Mean of All 87 672 **Rows**

````md magic-move {lines: true}
```py {1-3}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
print(len(lines))
```
```py {3-7}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
print(total)
```
```py {4,8-9}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
    count = count + 1
print(count, total / count)
```
````

<div class="card card-secondary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ python scripts/mean_all.py
```

<v-click>

```text
87672 5.782796103659093
```

</v-click>

</div>

<v-click>

<div class="note-text mt-sm">5.7828: the 120 rows of −999 are counted as temperatures. Python gives no warning; the script does exactly what it says.</div>

</v-click>

<!--
**Do:** click through the program as it grows: the lines of the file (it prints 87673), the sum in a loop (506989.30000000005), the count and the mean.
**Ask:** before the output: 7.16 or 5.78?
**Say:** the script does what it says: every row is a temperature to it. Python gives no warning.
(~3 min)
-->

---
hideInToc: true
---

# The Mean Without the −999 **Rows**

````md magic-move {lines: true}
```py {5-8}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
    count = count + 1
print(count, total / count)
```
```py {7-11}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp == -999:
        continue
    total = total + temp
    count = count + 1
print(count, total / count)
```
````

<div class="grid-2 mt-sm gap-md">

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python scripts/mean_temp.py
```

<v-click>

```text
87552 7.15996550621346
```

</v-click>

</div>

<div v-click class="card card-success card-glass pad-compact">

✅ Part 3: 7.15996550621346 from 87 552 rows: the 7.16 °C of the file, 120 hours left out.

</div>

</div>

<!--
**Do:** start from the loop of all rows, then click: the temperature gets a name, and three lines leave out the mark.
**Ask:** how many rows will be counted now? 87 672 − 120.
**Say:** our own twelve lines give Smiltė's number, and agree with a program written by someone else.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Functions and **Classes**

Part 4: how is a step written once and used again?

<!--
**Say:** the mean works. Every project then asks more: the coldest hour, the mean wind, each a new script.
(~1 min)
-->

---
hideInToc: true
---

# The Same Lines in Two Scripts

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`mean_temp.py`**

```py {1,2,5-9}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp == -999:
        continue
    total = total + temp
    count = count + 1
print(count, total / count)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **`coldest_hour.py`**

```py {1,2,5-9}
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
coldest = 100.0
coldest_time = ""
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp == -999:
        continue
    if temp < coldest:
        coldest = temp
        coldest_time = parts[0]
print(coldest_time, coldest)
```

</div>

</div>

<div class="note-text mt-sm">Seven lines are the same. A new column before <code>temp_c</code>, or a new mark for a missing hour, is an edit in every copy; a copy that is missed gives a wrong number, with no error.</div>

<!--
**Do:** point at the lit lines in both scripts: reading the file, cutting a line, the temperature, the −999 test.
**Ask:** a third script, for the mean wind: how many of its lines would be copied from these two?
**Say:** copies drift apart. One gets a fix, the other does not, and both still run.
(~2 min)
-->

---
hideInToc: true
---

# Write a Step Once: `def`

````md magic-move {lines: true}
```py
line1 = "2016-01-01T00:00,-4.4,93,2.5"
print(float(line1.split(",")[1]))   # -4.4
```
```py {3-4}
line1 = "2016-01-01T00:00,-4.4,93,2.5"
print(float(line1.split(",")[1]))   # -4.4
line2 = "2016-01-01T01:00,-4.8,95,2.6"
print(float(line2.split(",")[1]))   # -4.8
```
```py {1-3,7-8}
def temp_of(line):
    """The temp_c of one line of weather.csv."""
    return float(line.split(",")[1])

line1 = "2016-01-01T00:00,-4.4,93,2.5"
line2 = "2016-01-01T01:00,-4.8,95,2.6"
print(temp_of(line1))               # -4.4
print(temp_of(line2))               # -4.8
```
```py {5-7}
def temp_of(line):
    """The temp_c of one line of weather.csv."""
    return float(line.split(",")[1])

for line in ["2016-01-01T00:00,-4.4,93,2.5",
             "2016-01-01T01:00,-4.8,95,2.6"]:
    print(temp_of(line))            # -4.4, then -4.8
```
````

<div class="note-text mt-md"><code>def</code> gives a block a name and names its input, the <strong>parameter</strong>. <code>return</code> hands the result back. The block runs when the function is called, once per call. The text in three quotes says what it does.</div>

<!--
**Ask:** after step 2: the same line written twice with one name changed. What goes wrong when the column moves?
**Say:** the step is written once, under a name, and the loop says `temp_of(line)`. A change to the column is one edit, in the function.
(~3 min)
-->

---
hideInToc: true
---

# All Temperatures of a File: `temps(path)`

````md magic-move {lines: true}
```py
def read_lines(path):
    return open(path).read().splitlines()[1:]

print(len(read_lines("data/raw/weather.csv")))   # 87672
```
```py {4-5}
def read_lines(path):
    return open(path).read().splitlines()[1:]

def temp_of(line):
    return float(line.split(",")[1])

print(len(read_lines("data/raw/weather.csv")))   # 87672
```
```py {7-13,15}
def read_lines(path):
    return open(path).read().splitlines()[1:]

def temp_of(line):
    return float(line.split(",")[1])

def temps(path):
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != -999:
            result.append(temp)
    return result

print(len(temps("data/raw/weather.csv")))        # 87552
```
````

<div class="note-text mt-sm"><code>temps</code> calls <code>read_lines</code> and <code>temp_of</code>: each function does one step and can be checked alone. <code>result</code> exists only while <code>temps</code> runs; outside it the name is unknown.</div>

<!--
**Do:** click through: the lines without the header, one temperature, then the list of all temperatures without −999.
**Ask:** `!=` instead of `==` and `continue`: which rows reach `append`?
**If asked:** `print(result)` after the function gives `NameError: name 'result' is not defined`. Names made inside a function are its own, so two functions can both say `result` without a clash.
(~3 min)
-->

---
hideInToc: true
---

# The Mean of a List: `mean(values)`

````md magic-move {lines: true}
```py
def mean(values):
    return sum(values) / len(values)

print(mean([-4.4, -4.8, -5.5, -6.0]))          # -5.175
```
```py {5}
def mean(values):
    return sum(values) / len(values)

print(mean([-4.4, -4.8, -5.5, -6.0]))          # -5.175
print(mean(temps("data/raw/weather.csv")))     # 7.15996550621345
```
````

<div class="note-text mt-md">The twelve lines of Part 3 are one line now, read from the inside out: the temperatures of the file, then their mean. <code>sum</code> is built in, like <code>len</code>; <code>mean</code> works for any list of numbers, not only this file.</div>

<!--
**Ask:** before the second step: what will `mean(temps(...))` print?
**Say:** small functions, each one tested on four numbers, then put together. The same mean as the loop of Part 3.
**If asked:** the last digit is 5 here and 6 from the loop: since Python 3.12 `sum` adds floats with a correction for their rounding, and the loop does not.
(~2 min)
-->

---
hideInToc: true
---

# The Time Beside the Temperature: `class`

````md magic-move {lines: true}
```py
line = "2016-01-01T00:00,-4.4,93,2.5"
print(temp_of(line))           # -4.4, the time is lost
```
```py
class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])
```
```py {7-9}
class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

h = Hour("2016-01-01T00:00,-4.4,93,2.5")
print(h.time, h.temp)          # 2016-01-01T00:00 -4.4
print(type(h))                 # <class '__main__.Hour'>
```
````

<div class="note-text mt-sm">A <strong>class</strong> is a new type. <code>Hour(line)</code> makes an object of it and runs <code>__init__</code> once; <code>self</code> is that new object, and <code>self.time</code> keeps a value in it, an <strong>attribute</strong>. <code>str</code>, <code>dict</code> and <code>Figure</code> are classes too.</div>

<!--
**Ask:** the coldest hour needs its time. `temp_of` gives only the number: where does the time go?
**Say:** the values of one hour are kept together in one object, and reached by name after a dot, like `fig.axes`.
**If asked:** `__main__` is the name of the script that defined the class; from a module it reads `weather.Hour`.
(~3 min)
-->

---
hideInToc: true
---

# A Method: `is_missing()`

````md magic-move {lines: true}
```py
class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])
```
```py {7-8}
class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

    def is_missing(self):
        return self.temp == -999
```
```py {10-13}
class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

    def is_missing(self):
        return self.temp == -999

h = Hour("2016-01-01T00:00,-4.4,93,2.5")
print(h.is_missing())          # False
h = Hour("2019-07-22T00:00,-999,76,3.2")
print(h.is_missing())          # True
```
````

<div class="note-text mt-sm">A <strong>method</strong> is a <code>def</code> inside the class. Python passes the object before the dot as <code>self</code>, so <code>h.is_missing()</code> asks <code>h</code> about its own temperature, as <code>line.split(",")</code> asks <code>line</code>.</div>

<!--
**Say:** the −999 rule now lives in one place, inside the class. A script asks the hour, and does not need to know the mark.
**If asked:** the second line is a real hour of the file: 22 July 2019, midnight, one of the 120 missing hours.
(~2 min)
-->

---
hideInToc: true
---

# The Coldest Hour with `Hour` Objects

````md magic-move {lines: true}
```py
lines = read_lines("data/raw/weather.csv")
coldest = Hour(lines[0])
print(coldest.time, coldest.temp)    # 2016-01-01T00:00 -4.4
```
```py {3-6}
lines = read_lines("data/raw/weather.csv")
coldest = Hour(lines[0])
for line in lines[1:]:
    h = Hour(line)
    if not h.is_missing() and h.temp < coldest.temp:
        coldest = h
print(coldest.time, coldest.temp)    # 2025-01-07T05:00 -16.3
```
````

<div class="note-text mt-sm"><code>not</code> turns <code>True</code> into <code>False</code>; <code>and</code> is <code>True</code> when both sides are. The object found keeps its time with its temperature, so nothing has to be copied beside it.</div>

<div v-click class="card card-success card-glass pad-compact mt-sm">

✅ Part 4: a step is written once as a function, `def`, and called by its name; values that belong together are one object of a class, with methods. The coldest hour: 2025-01-07T05:00, −16.3 °C.

</div>

<!--
**Do:** first step: start from the first hour as the coldest so far; second step: each hour that is colder takes its place.
**Ask:** what if the first hour of the file were a −999? `coldest.temp` would start at −999 and no hour would be colder.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Modules and **`import`**

Part 5: how do several scripts share one file of functions?

<!--
**Say:** the functions and the class are still inside one script; the other scripts cannot see them.
(~1 min)
-->

---
hideInToc: true
---

# A Module: a File of Functions, `weather.py`

````md magic-move {lines: true}
```py
"""Read the hourly log of the weather station."""

MISSING = -999.0
```
```py {5-6}
"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]
```
```py {8-15}
"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]

class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

    def is_missing(self):
        return self.temp == MISSING
```
```py {17-18}
"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]

class Hour:
    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

    def is_missing(self):
        return self.temp == MISSING

def mean(values):
    return sum(values) / len(values)
```
````

<!--
**Say:** a **module** is a `.py` file of definitions. This one asks no question and prints nothing: it only defines a name for the mark, a function, a class, and the mean.
**Do:** click through: the text at the top says what the file is; `MISSING` gives the mark a name, written in capitals as a constant.
(~2 min)
-->

---
hideInToc: true
---

# Use the Module: `import weather`

````md magic-move {lines: true}
```py
text = open("data/raw/weather.csv").read()
lines = text.splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp == -999:
        continue
    total = total + temp
    count = count + 1
print(count, total / count)
```
```py
import weather

temps = []
for line in weather.read_lines("data/raw/weather.csv"):
    h = weather.Hour(line)
    if not h.is_missing():
        temps.append(h.temp)
print(len(temps), weather.mean(temps))
```
````

<div class="card card-secondary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**, with `weather.py` and `mean_temp.py` in `scripts/`

```text
$ python scripts/mean_temp.py
87552 7.15996550621345
```

</div>

<!--
**Do:** first step: `mean_temp.py` of Part 3; second step: the same script with the module.
**Say:** what is left in the script is its own question. How a line is cut and what −999 means is in `weather.py`.
**If asked:** `temps` is not in the module because `Hour` keeps the time beside the temperature; a list of numbers would lose it.
(~2 min)
-->

---
hideInToc: true
---

# What `import weather` Does

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **Three steps**

1. finds `weather.py`: in the script's folder, then in the standard library, then in the environment's packages
2. runs it once, top to bottom: `def` and `class` make the functions and the class
3. names the result `weather`: `weather.Hour` is the class inside it

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## ✍️ **Three ways to write it**

| The line | Then |
| --- | --- |
| `import weather` | `weather.Hour(line)` |
| `from weather import Hour` | `Hour(line)` |
| `import matplotlib.pyplot as plt` | `plt.subplots()` |

</div>

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**, in a folder without `weather.py`

```text
$ python -c "import weather"
ModuleNotFoundError: No module named 'weather'
```

</div>

<!--
**Ask:** a script imports `weather` twice: does `weather.py` run twice? No: once per program; the second `import` reuses the module.
**If asked:** the folders searched are the list `sys.path`. A folder `__pycache__` appears beside `weather.py`: the module translated for this Python, to start faster next time.
(~2 min)
-->

---
hideInToc: true
---

# Every Script Imports the Module

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 📁 **The project**

```text
weather-project/
├── data/raw/weather.csv
└── scripts/
    ├── weather.py
    ├── mean_temp.py
    └── coldest_hour.py
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **`coldest_hour.py`**

```py
import weather

lines = weather.read_lines("data/raw/weather.csv")
coldest = weather.Hour(lines[0])
for line in lines[1:]:
    h = weather.Hour(line)
    if not h.is_missing() and h.temp < coldest.temp:
        coldest = h
print(coldest.time, coldest.temp)
```

</div>

</div>

<div class="note-text mt-sm">Functions and classes are written once, in <code>weather.py</code>; each script imports them and holds only its own question. A new column in the file is one edit, in <code>weather.py</code>, and every script follows.</div>

<!--
**Ask:** the station adds a column `pressure_hpa` after `time`. Which files change? Only `weather.py`: `parts[1]` becomes `parts[2]`.
**Say:** the rule of every programming project: what is used twice goes into a module; a script imports it and does not define it again.
(~2 min)
-->

---
hideInToc: true
---

# A Library: Modules Someone Else Wrote

```py {monaco-run} {autorun:false}
import statistics
import math

print(statistics.mean([-4.4, -4.8, -5.5, -6.0]))   # -5.175
print(math.sqrt(87672))                            # 296.09457948432623
print(math.pi)                                     # 3.141592653589793
```

<div class="card card-success card-glass pad-compact mt-md">

✅ Part 5: a **module** is a `.py` file of functions and classes; `import` finds it, runs it once and gives it a name. A **library** is modules someone else wrote and tested, imported the same way: `statistics.mean` does what our `mean` does.

</div>

<!--
**Do:** run the block: two modules that come with Python.
**Say:** `weather.py` was written by us for one file; `statistics` by others, for every list of numbers, and tested by thousands of users.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Packages and **Versions**

Part 6: where does the rest of Python come from, and which version arrives?

<!--
**Say:** `float` and `dict` are built in, `statistics` came with Python; the `Figure` did not.
(~1 min)
-->

---
hideInToc: true
---

# Built In, Standard Library, **Packages**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | Where it is | Examples | Used as |
| --- | --- | --- | --- |
| **built in** | in `python` itself | `float`, `str`, `dict`, `print`, `len`, `open` | at once |
| **standard library** | comes with every Python | `math`, `json`, `urllib`, `csv` | `import json` |
| **packages** | installed by a package manager | `matplotlib`, `numpy`, `pandas` | `import numpy`, after an install |

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**, in an environment with only Python

```text
$ python -c "import json; print(json.loads('[7.16]'))"
[7.16]
$ python -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
```

</div>

<!--
**Say:** a **package** is a folder of modules, installed together: `matplotlib.pyplot` is the module `pyplot` in the package `matplotlib`.
**If asked:** `python -c` runs the text after it as a one-line script. The traceback above `ModuleNotFoundError` is left out.
(~2 min)
-->

---
hideInToc: true
---

# PyPI and conda-forge: Where Packages **Come From**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Index | Packages on 18 Oct 2026 | Installed with | Who publishes |
| --- | --- | --- | --- |
| **PyPI**, pypi.org | 916 606 projects | `pip install NAME` | anyone with an account |
| **conda-forge**, conda-forge.org | 34 699 packages | `conda install NAME` | a community that builds and reviews each recipe |

</div>

<div class="note-text mt-md">A <strong>package manager</strong> finds a package in an index, downloads the build for your system and Python, and puts it into one environment. Miniforge's <code>conda</code> installs only from conda-forge: fewer packages, each built the same way for macOS, Windows and Linux, with the libraries it needs.</div>

<!--
**Ask:** guess the number of projects on PyPI before the table appears. Most of them are small, old or abandoned; a few thousand are used by nearly everyone.
**If asked:** the count on PyPI is of the project names in its simple index; conda-forge's from its channel data.
(~2 min)
-->

---
hideInToc: true
---

# A Package Brings Other **Packages**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| A new environment with | Packages installed | Among them |
| --- | --- | --- |
| `python=3.14` | 23 | `python`, `openssl`, `libsqlite`, `tk`, `pip` |
| `python=3.14 jupyterlab` | 139 | the 23, `ipykernel`, `ipython`, `tornado`, `jinja2`, … |

</div>

<div class="note-text mt-md">A package names the packages it needs, its <strong>dependencies</strong>, each with the versions it works with; they name theirs. Asking for one package, JupyterLab, brings 116. Counted with <code>conda create --dry-run</code> from conda-forge on Linux, 18 Oct 2026; macOS and Windows differ by a few.</div>

<!--
**Say:** the package manager solves a puzzle: one version of each of 139 packages, all compatible with each other and with Python 3.14.
**Ask:** what can go wrong when two projects share one set of packages? One needs NumPy 1, the other NumPy 2.
(~2 min)
-->

---
hideInToc: true
---

# How Often Packages **Change**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Package | Releases, 18 Oct 2025 to 18 Oct 2026 | From | To |
| --- | --- | --- | --- |
| `numpy` | 15 | 2.3.5 | 2.5.4 |
| `pandas` | 11 | 3.0.0rc0 | 3.1.0rc0 |
| `matplotlib` | 7 | 3.10.8 | 3.11.2 |
| `requests` | 6 | 2.33.0 | 2.34.2 |
| `jupyterlab` | 33 | 4.4.10 | 4.7.0a2 |
| Python | 1 a year, in October | 3.14.0, 7 Oct 2025 | 3.15.0, 9 Oct 2026 |

</div>

<div class="note-text mt-md">An install without a version takes the newest. The same line typed a year apart gives other packages, and a script can give another number or stop.</div>

<!--
**Say:** release dates from PyPI and python.org. Each Python is supported about five years: 3.10 ended on 1 October 2026.
**Ask:** a script written today, run next October with whatever is newest: what has changed under it?
(~2 min)
-->

---
hideInToc: true
---

# Reading a Version Number: 2.5.4

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Part | Example | What a change means |
| --- | --- | --- |
| **major** | pandas 2.3 → **3**.0 | old code may break: pandas 3.0 changed defaults (copy-on-write, a new string type) |
| **minor** | numpy 2.4 → 2.**5** | new functions; old code keeps working, a few old names go after a warning |
| **patch** | numpy 2.5.3 → 2.5.**4** | fixes only |
| pre-release | pandas 3.1.0**rc0**, jupyterlab 4.7.0**a2** | release candidate, alpha: for testing, not for results |

</div>

<div class="note-text mt-md">Most scientific packages follow this scheme, <strong>semantic versioning</strong>, more or less closely. Pinning <code>numpy=2.5</code> takes the newest 2.5.x: fixes yes, new minor versions no.</div>

<!--
**Ask:** 2.5.4 to 2.6.0: which part changed, and is it safe? The minor: new things, mostly safe.
(~2 min)
-->

---
hideInToc: true
---

# Which Python a Package **Supports**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🐍 **Python versions**

| Version | Released | Supported until |
| --- | --- | --- |
| 3.15 | 9 Oct 2026 | Oct 2031 |
| 3.14 | 7 Oct 2025 | Oct 2030 |
| 3.13 | 7 Oct 2024 | Oct 2029 |
| 3.12 | 2 Oct 2023 | Oct 2028 |
| 3.11 | 24 Oct 2022 | Oct 2027 |

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📦 **Builds on PyPI, 18 Oct 2026**

| Package | For Python |
| --- | --- |
| numpy 2.5.4 | 3.12 to 3.15 |
| pandas 3.0.6 | 3.11 to 3.15 |
| matplotlib 3.11.2 | 3.11 to 3.15 |

</div>

</div>

<div class="note-text mt-md">An environment with Python 3.11 cannot have NumPy 2.5: the package manager takes an older NumPy that still supports 3.11. The Python version is one more version to write down.</div>

<!--
**Say:** a package drops a Python a few years after its release; a new Python gets builds within weeks.
(~2 min)
-->

---
hideInToc: true
---

# An Environment: One Python and Its **Packages**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **`miniforge3/envs/weather/`** on macOS

```text
bin/python                 Python 3.14.8
lib/python3.14/site-packages/
├─ jupyterlab/             4.6.4
├─ numpy/                  2.5.4
└─ …
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📁 **`miniforge3/envs/old-thesis/`**

```text
bin/python                 Python 3.11.17
lib/python3.11/site-packages/
├─ numpy/                  1.26.4
└─ …
```

</div>

</div>

<div class="note-text mt-md">An <strong>environment</strong> is a folder with one Python and the packages installed for it. One environment per project, so an upgrade for one project cannot break another. <code>conda activate weather</code> puts its <code>bin</code> first on <code>PATH</code> (Lecture 04): <code>python</code> then means that Python. On Windows: <code>envs\weather\python.exe</code> and <code>Lib\site-packages</code>.</div>

<!--
**Say:** Miniforge's own environment is `base`; projects get their own.
**Ask:** after `conda activate old-thesis`, what does `import numpy; print(numpy.__version__)` print? 1.26.4.
(~3 min)
-->

---
hideInToc: true
---

# Write the Versions Down: `environment.yml`

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **`environment.yml`**

```yaml
name: weather
channels:
  - conda-forge
dependencies:
  - python=3.14
  - jupyterlab=4.6
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ conda create -n weather python=3.14 jupyterlab=4.6
$ conda env export --from-history -f environment.yml
$ conda env create -f environment.yml
```

1. make the environment
2. write down what was asked for
3. on another laptop: make the same environment

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Part 6: from the standard library with `import`, from conda-forge or PyPI by a package manager, into one environment per project, with the versions pinned and written down.

</div>

<!--
**Say:** six lines that let anyone rebuild the environment, and you yourself next year. They go into the project folder, beside `data/` and `scripts/`.
**If asked:** `--from-history` writes only what was typed, not all 139 packages; the export ends with a `prefix:` line, the folder on this laptop, which is deleted.
(~2 min)
-->

---
hideInToc: true
---

<div class="card card-success card-glass pad-compact table-compact mt-md">

| Part | Answer |
| --- | --- |
| 1 · a value | an object with a type, `int`, `float`, `bool`, `str`; methods after a dot: `line.split(",")` |
| 2 · containers | `list` by position, `dict` by key, `tuple`, `set`; a `Figure` is a container of objects |
| 3 · `for` and `if` | a loop over the lines, `split` and `float`, `continue` for −999: 7.15996550621346 |
| 4 · write it once | a function, `def`; the values of one hour together in an object of a class, `Hour` |
| 5 · share it | a module, `weather.py`, written once; each script says `import weather` |
| 6 · the rest | the standard library; packages from conda-forge or PyPI, one environment per project |

</div>

<!--
**Say:** 7.16 now comes from a script of eight lines and a module that every script of the project imports.
(~1 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Read a line of Python, name the type of a value, `int`, `float`, `bool` or `str`, and turn text into a number with `float()`

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose a container, `list`, `tuple`, `dict` or `set`, and read an object inside an object

</div>

<div class="card card-success card-glass pad-compact">

✅ Repeat a step with `for`, choose with `if`, leave out rows with `continue`

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a step once with `def`, keep the values of one hour in an object of a class, and import both from a module

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a version number, and say why each project has its own environment with pinned versions

</div>

</div>

<!--
(~1 min)
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
  question="`x = '7.16'` and `y = '1'`. What is `x + y`?"
  :options="[
    'The number 8.16',
    'The text 7.161',
    'A TypeError',
    'The text 7.16 + 1'
  ]"
  :correct="1"
  explanation="Both values are strings, and + joins two strings, with no error. float(x) + float(y) gives 8.16. A TypeError appears only when a string meets a number, as in '7.16' + 1."
/>

---
hideInToc: true
---

<MCQ
  question="What do `100 / 4` and `100 // 4` give?"
  :options="[
    '25 and 25',
    '25.0 and 25',
    '25 and 25.0',
    '25.0 and 25.0'
  ]"
  :correct="1"
  explanation="/ always gives a float, also when it divides evenly: 25.0. // gives the whole part of the division, an int when both sides are ints: 25."
/>

---
hideInToc: true
---

<MCQ
  question="`line = '2020-02-29T12:00,3.1,88,4.0'`. What is `line.split(',')[2]`?"
  :options="[
    'The number 3.1',
    'The text 3.1',
    'The text 88',
    'The number 88'
  ]"
  :correct="2"
  explanation="Positions count from 0: part 0 is the time, part 1 the temperature, part 2 the humidity. split hands back strings, so it is the text '88'."
/>

---
hideInToc: true
---

<MCQ
  question="`lines` holds 250 strings: a header and 249 rows. How many times does the block of `for line in lines[2:]:` run?"
  :options="[
    '250',
    '249',
    '248',
    '2'
  ]"
  :correct="2"
  explanation="lines[2:] starts at the third item, position 2, so it leaves out the header and the first row: 248. lines[1:] would leave out only the header: 249."
/>

---
hideInToc: true
---

<MCQ
  question="Which container holds one row of `weather.csv` so that its temperature is found as `row['temp_c']`?"
  :options="[
    'A list',
    'A tuple',
    'A dict',
    'A set'
  ]"
  :correct="2"
  explanation="A dict finds a value by its key, here the column name. A list and a tuple find values by position (row[1]); a set has no order and no keys."
/>

---
hideInToc: true
---

<MCQ
  question="`row = {'temp_c': -4.4}`. What does `row['rain_mm']` do?"
  :options="[
    'It gives 0',
    'It gives None',
    'It stops with KeyError',
    'It adds the key rain_mm'
  ]"
  :correct="2"
  explanation="A key that is not in the dictionary stops the program with KeyError: 'rain_mm'. Assigning row['rain_mm'] = 0.0 would add the key."
/>

---
hideInToc: true
---

<MCQ
  question="In the loop for 7.16, `count = count + 1` is moved above the `if temp == -999:` line. The sum is unchanged. What does the script print as the mean?"
  :options="[
    '7.15996550621346, as before',
    '7.150165389177845, with no message',
    '5.782796103659093',
    'A ValueError'
  ]"
  :correct="1"
  explanation="The sum still leaves out the marks, 626 869.3, but the count is now 87 672: 626 869.3 / 87 672 = 7.150165389177845. No message: only a number known beforehand shows it."
/>

---
hideInToc: true
---

<MCQ
  question="`scripts/weather.py` defines the class `Hour`. A script in `scripts/` starts with `import weather`. How does it make an `Hour` from `line`?"
  :options="[
    'Hour(line)',
    'weather.Hour(line)',
    'import Hour(line)',
    'weather(Hour, line)'
  ]"
  :correct="1"
  explanation="import weather gives the script one name, weather; what the module defines is reached after a dot. Hour(line) alone is a NameError, unless the script says from weather import Hour."
/>

---
hideInToc: true
---

<MCQ
  question="Why do the scripts of a project import `weather.py` instead of each defining `read_lines` and `Hour` again?"
  :options="[
    'Python cannot call a function defined in the same script',
    'A script may hold only one def',
    'A change, such as a new column in the file, is then one edit, and every script follows',
    'An imported function runs faster'
  ]"
  :correct="2"
  explanation="A function defined in a script works too, but every copy has to be changed when the file changes, and a copy that is missed gives a wrong number without an error. Defined once and imported, the step changes in one place."
/>

---
hideInToc: true
---

<MCQ
  question="NumPy goes from 2.5.4 to 2.6.0. Which part of the version changed, and what does it mean?"
  :options="[
    'The major: old code may break',
    'The minor: new functions, old code keeps working',
    'The patch: fixes only',
    'A pre-release: not for results'
  ]"
  :correct="1"
  explanation="MAJOR.MINOR.PATCH: 2.5 to 2.6 is the minor part, new functions with old code still working. 3.0.0 would be a major release, 2.5.5 a patch."
/>

---
hideInToc: true
---

<MCQ
  question="Two projects need NumPy 1.26 and NumPy 2.5. What keeps both working on one laptop?"
  :options="[
    'Installing both versions into base',
    'An environment per project, each with its own NumPy',
    'Upgrading the older project to NumPy 2.5 at once',
    'Installing NumPy 2.5 from PyPI and 1.26 from conda-forge'
  ]"
  :correct="1"
  explanation="One environment holds one version of each package. Each project gets its own environment, with its NumPy pinned and written down in environment.yml."
/>
