---
layout: cover
title: "Python Foundations"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python Foundations

##### <span class="aims-badge">🔧 tool-agnostic · ⚙️ automation</span>

<!--
**Say:** Lecture 04 got 7.16 from a program someone else wrote. Today: what Python is made of, objects and the lines that combine them, and where the objects come from that Python does not have.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# In Python every value is an object of a type. A program combines objects with `for` and `if`; packages bring objects that other people wrote

<!--
**Say:** three parts, in this order: the objects, the lines that combine them, the packages.
(~1 min)
-->

---
hideInToc: true
---

# The Mean from `column_stats.py`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ python scripts/column_stats.py data/raw/weather.csv temp_c
file    data/raw/weather.csv
column  temp_c
rows    87672
min     -999.0
max     32.4
mean    5.7828
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| File | rows | mean |
| --- | --- | --- |
| `data/raw/weather.csv` | 87 672 | 5.7828 |
| `data/processed/weather_valid.csv`, without the −999 rows | 87 552 | 7.15997 |

</div>

<div class="note-text mt-md"><code>column_stats.py</code> is 53 lines of Python. Lecture 04 ran it without reading it.</div>

<!--
**Say:** the two numbers of Lecture 04: 5.78 with the 120 marked rows, 7.16 without them. Both came out of a program nobody here has read.
**Ask:** what does a program need to get 7.16 out of `weather.csv`? Collect on the board: the file's text, a number per line, a sum, a count, a rule that leaves out −999.
(~2 min)
-->

---
hideInToc: true
---

<div class="card card-primary card-glass pad-compact table-compact mt-lg">

| Part | Question | Answer |
| --- | --- | --- |
| 1 | What kinds of values does Python have, and what can each do? | ? |
| 2 | How do `for` and `if` turn 87 672 lines into 7.16? | ? |
| 3 | Where do the objects come from that Python does not have, and which version arrives? | ? |

</div>

<!--
**Say:** one question per part; the answers fill the last column at the end.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Objects and **Types**

Part 1: what kinds of values does Python have, and what can each do?

<!--
(~1 min)
-->

---
hideInToc: true
---

# Every Value Is an **Object**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
temp = -4.4
print(type(temp))
```
```py
temp = -4.4
print(type(temp))        # <class 'float'>
```
```py {3}
temp = -4.4
print(type(temp))        # <class 'float'>
print(temp.is_integer()) # False
```
```py {4}
temp = -4.4
print(type(temp))        # <class 'float'>
print(temp.is_integer()) # False
print(round(temp))       # -4
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **An object has**

- a **type**: `float`
- a **value**: −4.4
- **methods**, written after a dot: `temp.is_integer()`

`temp = -4.4` puts the name `temp` on the object.

</div>

</div>

<!--
**Do:** click line by line; before each comment appears, ask for the output.
**Say:** `type()` and `round()` are functions; `is_integer()` is a method, a function that belongs to the float and is written after a dot.
**If asked:** `dir(temp)` lists every method a float has.
(~2 min)
-->

---
hideInToc: true
---

# Numbers: `int`, `float`, `bool`

````md magic-move {lines: true}
```py
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
```
```py {3}
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
print(hours / 24)
```
```py {3-4}
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
print(hours / 24)             # 3653.0: / always gives a float
print(hours // 24)            # 3653: the whole part, an int
```
```py {5}
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
print(hours / 24)             # 3653.0: / always gives a float
print(hours // 24)            # 3653: the whole part, an int
print(2 ** 100)               # 1267650600228229401496703205376
```
```py {6-7}
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
print(hours / 24)             # 3653.0: / always gives a float
print(hours // 24)            # 3653: the whole part, an int
print(2 ** 100)               # 1267650600228229401496703205376
print(hours > 80000)          # True
print(type(hours > 80000))    # <class 'bool'>
```
```py {8}
hours = 87672                 # ten years of hours
print(type(hours))            # <class 'int'>
print(hours / 24)             # 3653.0: / always gives a float
print(hours // 24)            # 3653: the whole part, an int
print(2 ** 100)               # 1267650600228229401496703205376
print(hours > 80000)          # True
print(type(hours > 80000))    # <class 'bool'>
print(0.1 + 0.2)              # 0.30000000000000004
```
````

<div class="note-text mt-md">An <code>int</code> takes as many bits as its number needs: 2¹⁰⁰ needs 101, and nothing wraps. A <code>float</code> is the float64 of Lecture 03, rounded to about 16 digits. A comparison gives a <code>bool</code>.</div>

<!--
**Ask:** before the third step: 87672 / 24, is it 3653 or 3653.0?
**Say:** `**` is the power. 3653 days: ten years with three leap years. The last line is float64 showing through: measured values are compared with a tolerance, never with `==`.
(~2 min)
-->

---
hideInToc: true
---

# A Line of `weather.csv` Is a `str`

````md magic-move {lines: true}
```py
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line[0:4])                  # 2016
```
```py {3-4}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line[0:4])                  # 2016
parts = line.split(",")
print(parts)                      # ['2016-01-01T00:00', '-4.4', '93', '2.5']
```
```py {5}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line[0:4])                  # 2016
parts = line.split(",")
print(parts)                      # ['2016-01-01T00:00', '-4.4', '93', '2.5']
print(parts[1], type(parts[1]))   # -4.4 <class 'str'>
```
```py {6}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line[0:4])                  # 2016
parts = line.split(",")
print(parts)                      # ['2016-01-01T00:00', '-4.4', '93', '2.5']
print(parts[1], type(parts[1]))   # -4.4 <class 'str'>
print(parts[1] + 1)               # TypeError: can only concatenate str (not "int") to str
```
```py {6-7}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(line[0:4])                  # 2016
parts = line.split(",")
print(parts)                      # ['2016-01-01T00:00', '-4.4', '93', '2.5']
print(parts[1], type(parts[1]))   # -4.4 <class 'str'>
temp = float(parts[1])
print(temp + 1)                   # -3.4000000000000004
```
````

<div class="note-text mt-md">Positions count from 0; <code>[0:4]</code> stops before 4. <code>split(",")</code> cuts at the commas and hands back a list of four strings. In the file <code>-4.4</code> is text, four characters, until <code>float()</code> makes the number.</div>

<!--
**Do:** draw the first ten characters on the board with their positions 0 to 9 below them.
**Ask:** after the split, is `parts[1]` a number? What does `parts[1] + 1` do?
**Say:** cut, then convert: two steps for every line of the file.
(~3 min)
-->

---
hideInToc: true
---

# Containers: `list` and `tuple`

````md magic-move {lines: true}
```py
temps = [-4.4, -4.8, -5.5]         # 00:00 to 02:00, 1 Jan 2016
print(temps[0], len(temps))        # -4.4 3
```
```py {3-4}
temps = [-4.4, -4.8, -5.5]         # 00:00 to 02:00, 1 Jan 2016
print(temps[0], len(temps))        # -4.4 3
temps.append(-6.0)                 # 03:00
print(temps)                       # [-4.4, -4.8, -5.5, -6.0]
```
```py {5-6}
temps = [-4.4, -4.8, -5.5]         # 00:00 to 02:00, 1 Jan 2016
print(temps[0], len(temps))        # -4.4 3
temps.append(-6.0)                 # 03:00
print(temps)                       # [-4.4, -4.8, -5.5, -6.0]
row = ("2016-01-01T00:00", -4.4, 93, 2.5)
print(row[1])                      # -4.4
```
```py {7}
temps = [-4.4, -4.8, -5.5]         # 00:00 to 02:00, 1 Jan 2016
print(temps[0], len(temps))        # -4.4 3
temps.append(-6.0)                 # 03:00
print(temps)                       # [-4.4, -4.8, -5.5, -6.0]
row = ("2016-01-01T00:00", -4.4, 93, 2.5)
print(row[1])                      # -4.4
row[1] = 0.0                       # TypeError: 'tuple' object does not support item assignment
```
````

<div class="note-text mt-md">A <strong>list</strong> <code>[…]</code> holds values in order and can grow. A <strong>tuple</strong> <code>(…)</code> holds values in order and never changes: one row of the file, fixed.</div>

<!--
**Ask:** after the `append`, what is `temps[-1]`? A negative position counts from the end: −6.0.
**Say:** both are indexed like a string. The list is for values that come in one by one; the tuple for a record that must stay as it was read.
(~2 min)
-->

---
hideInToc: true
---

# Containers: `dict` and `set`

````md magic-move {lines: true}
```py
row = {"time": "2016-01-01T00:00", "temp_c": -4.4,
       "humidity_pct": 93, "wind_ms": 2.5}
print(row["temp_c"])              # -4.4
```
```py {4-5}
row = {"time": "2016-01-01T00:00", "temp_c": -4.4,
       "humidity_pct": 93, "wind_ms": 2.5}
print(row["temp_c"])              # -4.4
row["temp_f"] = row["temp_c"] * 9 / 5 + 32
print(row["temp_f"])              # 24.08
```
```py {6-7}
row = {"time": "2016-01-01T00:00", "temp_c": -4.4,
       "humidity_pct": 93, "wind_ms": 2.5}
print(row["temp_c"])              # -4.4
row["temp_f"] = row["temp_c"] * 9 / 5 + 32
print(row["temp_f"])              # 24.08
print(row.get("rain_mm", 0))      # 0: no such key
print(row["rain_mm"])             # KeyError: 'rain_mm'
```
```py {8-9}
row = {"time": "2016-01-01T00:00", "temp_c": -4.4,
       "humidity_pct": 93, "wind_ms": 2.5}
print(row["temp_c"])              # -4.4
row["temp_f"] = row["temp_c"] * 9 / 5 + 32
print(row["temp_f"])              # 24.08
print(row.get("rain_mm", 0))      # 0: no such key
print(row["rain_mm"])             # KeyError: 'rain_mm'
years = {"2016", "2016", "2017"}
print(len(years))                 # 2
```
````

<div class="note-text mt-md">A <strong>dict</strong> <code>{key: value}</code> finds a value by its key, here by the name of the column. A <strong>set</strong> <code>{…}</code> keeps each value once. Containers hold any objects, other containers too: a list of tuples, a dictionary of dictionaries.</div>

<!--
**Ask:** `row.get("rain_mm", 0)` against `row["rain_mm"]`: what does each do?
**Say:** the dictionary is the row with its header attached: `row["temp_c"]` instead of `parts[1]`. Assigning to a new key adds it.
(~2 min)
-->

---
hideInToc: true
---

# A matplotlib Figure, Built Line by **Line**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div>

````md magic-move {lines: true}
```py
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.3), layout="constrained")
```
```py {3}
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.3), layout="constrained")
print(type(fig))   # <class 'matplotlib.figure.Figure'>
```
```py {4-5}
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.3), layout="constrained")
print(type(fig))   # <class 'matplotlib.figure.Figure'>
hours = [0, 1, 2, 3]
ax.plot(hours, [-4.4, -4.8, -5.5, -6.0])
```
```py {6-7}
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.3), layout="constrained")
print(type(fig))   # <class 'matplotlib.figure.Figure'>
hours = [0, 1, 2, 3]
ax.plot(hours, [-4.4, -4.8, -5.5, -6.0])
ax.set(xlabel="hour", ylabel="temp_c")
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

Each has its own methods: `ax.plot`, `ax.set`, `fig.savefig`.

</div>

</div>

<!--
**Say:** `matplotlib` is a package, not part of Python; Part 3 is about where it comes from. A figure is an object like −4.4, only with more inside it.
**If asked:** `plt.subplots` hands back two objects at once, a figure and its axes, and `fig, ax =` names both.
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

# The Answer of a Weather Service: **JSON**

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

<div class="note-text mt-md"><strong>JSON</strong> is text that writes numbers, strings, lists and dictionaries. <code>json.loads</code> turns it into Python objects: here a dictionary of dictionaries, read one key at a time.</div>

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

Part 2: how do `for` and `if` turn 87 672 lines into 7.16?

<!--
**Say:** the objects are known; now the lines that repeat a step and choose between steps.
(~1 min)
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

# The Mean of All 87 672 **Rows**

````md magic-move {lines: true}
```py {1-2}
lines = open("data/raw/weather.csv").read().splitlines()
print(len(lines))
```
```py {2-6}
lines = open("data/raw/weather.csv").read().splitlines()
total = 0.0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
print(total)
```
```py {3,7-8}
lines = open("data/raw/weather.csv").read().splitlines()
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

<div class="note-text mt-sm"><code>open</code>, <code>read</code> and <code>splitlines</code> turn the file into a list of 87 673 strings, the header first. 5.7828 is the mean of <code>column_stats.py</code> on the raw file: the 120 rows of −999 are counted as temperatures.</div>

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

# The Mean Without the −999 **Rows**

````md magic-move {lines: true}
```py {4-7}
lines = open("data/raw/weather.csv").read().splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    parts = line.split(",")
    total = total + float(parts[1])
    count = count + 1
print(count, total / count)
```
```py {6-10}
lines = open("data/raw/weather.csv").read().splitlines()
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

✅ Part 2: 7.15996550621346 from 87 552 rows, the 7.15997 of `column_stats.py`.

</div>

</div>

<!--
**Do:** start from the loop of all rows, then click: the temperature gets a name, and three lines leave out the mark.
**Ask:** how many rows will be counted now? 87 672 − 120.
**Say:** our own eleven lines give Smiltė's number, and agree with a program written by someone else.
(~3 min)
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
**Say:** the step is written once, under a name, and the loop says `temp_of(line)`. A file of such functions can be used by many scripts: a module.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Packages and **Versions**

Part 3: where do the objects come from that Python does not have, and which version arrives?

<!--
**Say:** `float` and `dict` came with Python; the `Figure` did not.
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
**Say:** a **module** is a `.py` file of functions; `import` runs it once and makes its names available. A **package** is a folder of modules, installed together.
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

✅ Part 3: from the standard library with `import`, from conda-forge or PyPI by a package manager, into one environment per project, with the versions pinned and written down.

</div>

<!--
**Say:** six lines that let anyone rebuild the environment, and you yourself next year. They go into the project folder, beside `data/` and `scripts/`.
**If asked:** `--from-history` writes only what was typed, not all 139 packages; the export ends with a `prefix:` line, the folder on this laptop, which is deleted.
(~2 min)
-->

---
hideInToc: true
---

<div class="stack-tight mt-lg">

<div class="card card-success card-glass pad-compact">

**1. What kinds of values does Python have, and what can each do?** Objects of a type: `int`, `float`, `bool`, `str`; the containers `list`, `tuple`, `dict`, `set`; larger objects such as a `Figure` or the answer of a web service. The type says which methods it has.

</div>

<div class="card card-success card-glass pad-compact">

**2. How do `for` and `if` turn 87 672 lines into 7.16?** A `for` over the lines, `split` and `float` on each, `if` and `continue` for −999: 7.15996550621346 from 87 552 rows.

</div>

<div class="card card-success card-glass pad-compact">

**3. Where do the other objects come from, and which version arrives?** From the standard library, or as packages from conda-forge and PyPI; the newest unless pinned. So: one environment per project, written down in `environment.yml`.

</div>

</div>

<!--
**Say:** 7.16 now comes from eleven lines anyone here can read, and each object in them has a type that says what it can do.
(~1 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Name the type of a value, `int`, `float`, `bool` or `str`, and turn text into a number

</div>

<div class="card card-success card-glass pad-compact">

✅ Choose a container, `list`, `tuple`, `dict` or `set`, and read a dictionary of dictionaries

</div>

<div class="card card-success card-glass pad-compact">

✅ Repeat a step with `for`, choose with `if`, leave out rows with `continue`

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a step once as a function with `def`

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
  question="`hours = {'2016': 8784}`. What do `hours.get('2026', 0)` and `hours['2026']` do?"
  :options="[
    'Both give 0',
    'The first gives 0, the second stops with KeyError',
    'Both stop with KeyError',
    'Both add the key 2026'
  ]"
  :correct="1"
  explanation="get hands back the default for a key that is not there; square brackets stop with KeyError: '2026'. Neither adds a key."
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
