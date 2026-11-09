---
layout: cover
title: "Code That Lasts"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Code That Lasts

##### <span class="aims-badge">♻️ reproducibility · ⚙️ automation · 🔧 tool-agnostic · 📁 data & files</span>

##### Inspired by: G. Wilson et al., *Good Enough Practices in Scientific Computing* (2017)

<!--
**Ask:** who has opened a script of their own from a year ago and could not make it run?
**Say:** the last lecture before the presentations: what keeps a result alive after the day it was made. Modules, objects, tests, environments, one command, and the proof that it all works.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# An article about computational science in a scientific publication is not the scholarship itself, it is merely **advertising** of the scholarship.
J. Buckheit and D. Donoho (1995), after Jon Claerbout

<!--
**Say:** the sentence goes on: the scholarship is the software environment and the complete set of instructions that made the figures. That folder is the subject of today.
(~0.5 min)
-->

---
hideInToc: true
---

# The Mean of Four Hours in Python 3.11 and **3.14**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🐍 **Python 3.11**

```text
>>> v = [27.3, 25.6, 24.6, 23.6]
>>> sum(v) / len(v)
25.275
>>> sum(v) / len(v) == 25.275
True
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐍 **Python 3.14**

```text
>>> v = [27.3, 25.6, 24.6, 23.6]
>>> sum(v) / len(v)
25.275000000000002
>>> sum(v) / len(v) == 25.275
False
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ The same lines, the four measured hours of 21 July 2019. Which laptop is right? And will 7.16 come out again next year, on another laptop?

</div>

<!--
**Say:** the four hours of the evening the sensor failed, 20:00 to 23:00, typed in Seminar 5. By hand: 101.1 / 4 = 25.275.
**Ask:** which laptop is right? Hands up for 3.11, for 3.14, for both.
**Say:** both: the two numbers differ in the 16th digit. The code and the data are the same; the Python is not. A result depends on more than its data and its code.
(~3 min)
-->

---
hideInToc: true
---

# What 7.16 **Depends On**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| **7.16 depends on** | **Kept in** |
| --- | --- |
| the 87 672 rows, as received | `data/raw/weather.csv`, SHA-256 `3f1ad06d…` |
| the steps: read, leave out −999, average | `scripts/weather.py` |
| a check that the steps are right | `scripts/test_weather.py` |
| Python and its packages, each in a version | `environment.yml` |
| the order of the steps | `scripts/rebuild.sh` |

</div>

<div class="note-text mt-md">One file per row, each written by hand. Everything else in the folder is made from them.</div>

<!--
**Say:** the lecture takes the rows in this order: modules, objects, tests, environments, the one command; then deletes every result and makes it again from these files alone.
**If asked:** the checksum of the raw file was taken in Lecture 4: 3f1ad06d…fbe00756, 2 515 215 bytes.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Modules**

Each step written once, in the file where it belongs.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# The Steps Behind 7.16, One **Function** Each

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **Step** | **Function** | **The six hours** | **The whole log** |
| --- | --- | --- | --- |
| read the lines | `read_lines(path)` | 6 lines | 87 672 lines |
| take `temp_c` | `temp_of(line)` | 27.3, 25.6, 24.6, 23.6, −999, −999 | 87 672 values |
| leave out −999 | `temps(path)` | 27.3, 25.6, 24.6, 23.6 | 87 552 values |
| average | `mean(values)` | 25.275 | 7.16 |

</div>

<div v-click class="card card-info card-glass pad-compact mt-md">

$$
\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i: \qquad \frac{101.1}{4} = 25.275, \qquad \frac{626\,869.3}{87\,552} = 7.16
$$

</div>

<!--
**Say:** the four functions of Lecture 5, one step each; each hands its result to the next: `mean(temps(path))`. The six hours and the whole log go through the same four.
**Ask:** the station marks a missing hour with an empty field instead of −999. Which function changes? Only `temps`, through the name `MISSING`.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# What Goes **Where**

<div class="card card-info card-glass pad-compact mt-sm">

📁 As received, the recipe, and what the recipe makes. Only the first two go into Git.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_project.svg">

<!--
**Say:** `data/raw` is read, never written. The recipe is written by hand: the module, its tests, the steps, the order, the versions, the README. `data/processed` and `results` are written only by `rebuild.sh`, so they can be deleted at any time.
**Ask:** a figure for the report: which column? The third, made by a script listed in `rebuild.sh`.
(~2 min)
-->

---
hideInToc: true
---

# The Module and a Script That **Imports** It

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📦 **`scripts/weather.py`**

```python
"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]

def temp_of(line):
    return float(line.split(",")[1])

def temps(path):
    ...  # temp_of of each line, MISSING left out

def mean(values):
    return sum(values) / len(values)
```

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## ❓ **`scripts/mean_temp.py`**

```python
import weather

values = weather.temps("data/raw/weather.csv")
print(len(values), weather.mean(values))
```

```text
$ python scripts/mean_temp.py
87552 7.15996550621345
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

- The module: names and functions. It prints nothing and names no file
- A script: one question, its file names, its `print`

</div>

</div>

</div>

<!--
**Say:** the rule of Lecture 5: what is used twice goes into the module; what belongs to one question stays in its script. The figures of Lecture 7 and the tests of today import the same module.
**If asked:** `temps` is six lines; the slide cuts it to its comment.
(~2 min)
-->

---
hideInToc: true
---

# A New Column in the **File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **The station adds `pressure_hpa` after `time`**

```text
time,pressure_hpa,temp_c,humidity_pct,wind_ms
```

```diff
 def temp_of(line):
-    return float(line.split(",")[1])
+    return float(line.split(",")[2])
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

✅ **With the module:** one line, in `weather.py`. Every script that imports it follows.

</div>

<div class="card card-warning card-glass pad-compact">

⚠️ **With copies:** one edit per copy. A copy that is missed reads another column and runs without an error, like the humidity column taken by mistake: a mean of 79.10.

</div>

</div>

<!--
**Ask:** before the diff: how many files change? With the module, one line in one file.
**Say:** a missed copy is the dangerous case: nothing fails, the number is wrong.
(~2 min)
-->

---
hideInToc: true
---

# A Function That Returns Can Be **Checked**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🖨️ **Prints**

```python
def show_mean(values):
    print(sum(values) / len(values))
```

Only a person can look at what it printed.

</div>

<div class="card card-success card-glass pad-compact">

## ↩️ **Returns**

```python
def mean(values):
    return sum(values) / len(values)
```

Another line of code can compare the result with 25.275.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`mean` names no file: four values typed by hand can go straight in. `temps(path)` needs a file; `mean(values)` needs only a list.

</div>

<!--
**Say:** two properties make a function easy to check: it returns its result, and it takes its data as an argument. Then a number known in advance can be compared with it.
(~2 min)
-->

---
hideInToc: true
---

# A Docstring Says What a Function Is **For**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📦 **In `scripts/weather.py`**

```python
def mean(values):
    """The mean of a list of numbers: their sum over their count."""
    return sum(values) / len(values)
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**, in `scripts`

```text
$ python -c "import weather; print(weather.mean.__doc__)"
The mean of a list of numbers: their sum over their count.
```

</div>

<div class="note-text mt-md">The text in three quotes under a <code>def</code> stays with the function: VS Code shows it beside every call.</div>

<!--
**Say:** a year later, the reader is often the author. One line under each `def` says what goes in and what comes out; the code says how.
**If asked:** the first line of `weather.py` is the module's own docstring: `print(weather.__doc__)` gives "Read the hourly log of the weather station."
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Objects**

Data and the functions that work on it, kept together.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# `str`, `list` and `Figure` Are **Objects**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| **Object** | **Holds** | **A method** | **Gives** |
| --- | --- | --- | --- |
| `line`, a `str` | `"2019-07-21T20:00,27.3,63,4.5"` | `line.split(",")` | 4 parts |
| `temps`, a `list` | `[27.3, 25.6, 24.6]` | `temps.append(23.6)` | 4 values |
| `fig`, a `Figure` | a picture | `fig.savefig("results/temp_hist.png")` | a file |

</div>

<div class="note-text mt-md"><code>object.method(…)</code>: a function that belongs to its object and works on the object's own data.</div>

<!--
**Say:** the room has used objects since the first `split`. A **class** is how a new kind of object is written, with its own data and its own methods; Lecture 10 wrote one.
(~2 min)
-->

---
hideInToc: true
---

# A Perceptron Predicts Frost for **One Evening**

<div class="card card-info card-glass pad-compact mt-sm">

$$
z = w_1 x_1 + w_2 x_2 + b, \qquad \text{frost at 06:00 if } z > 0; \qquad w_1 = -1,\; w_2 = 0,\; b = 3.8
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ❄️ **8 December 2025, 18:00**

$x_1 = 2.6$ °C, $x_2 = 0.85$

<v-click>

$z = (-1)(2.6) + 0 \cdot 0.85 + 3.8 = 1.2$: frost

</v-click>

<v-click>

06:00 next morning: −2.0 °C

</v-click>

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗃️ **What the model is**

- three numbers: $w_1$, $w_2$, $b$
- two things done with them: **predict** an evening, **fit** the numbers to evenings

</div>

</div>

<div v-click class="note-text mt-md">The rule "below 3.8 °C": 3490 of 3646 evenings right, 95.7 %. "Never frost": 66.3 %.</div>

<!--
**Say:** the neuron of Lecture 10, its weights set by hand: frost when the evening is below 3.8 °C, the humidity, as a fraction, given weight 0.
**Do:** click through: z, then the morning.
(~2 min)
-->

---
hideInToc: true
---

# The Perceptron as a **Class**

```py {monaco-run} {autorun:false}
class Perceptron:
    def __init__(self):
        self.w = [0.0, 0.0]
        self.b = 0.0
    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if z > 0:
            return 1
        return 0

model = Perceptron()
model.w = [-1.0, 0.0]                  # the rule "below 3.8 °C"
model.b = 3.8
print(model.predict([2.6, 0.85]))      # 1: 8 Dec 2025
print(model.predict([5.4, 0.75]))      # 0: 1 Nov 2024
```

<div class="note-text mt-sm">The object keeps its numbers: <code>model.predict(x)</code> needs only the evening. <code>self</code> is the object the method was called on.</div>

<!--
**Do:** press ▶: 1, then 0.
**Say:** the class of Lecture 10, with `fit` left out: `__init__` runs once, when `Perceptron()` makes the object; `predict` reads `self.w` and `self.b`, the numbers of that object.
**If asked:** `Perceptron().predict([2.6, 0.85])` gives 0: a new object starts from its own zeros, z = 0, which is not above 0.
(~3 min)
-->

---
hideInToc: true
---

# A Model's Numbers, Kept in a **File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 💾 **Written once, by a script**

```python
import json

numbers = {"w": model.w, "b": model.b}
open("results/model.json", "w").write(json.dumps(numbers))
```

```text
{"w": [-1.0, 0.0], "b": 3.8}
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📂 **Read back, anywhere**

```python
numbers = json.loads(open("results/model.json").read())
model = Perceptron()
model.w = numbers["w"]
model.b = numbers["b"]
```

</div>

</div>

<div class="note-text mt-md">The class is the recipe, in <code>scripts/</code>; its fitted numbers are a result, in <code>results/</code>, made again by the rebuild like 7.16.</div>

<!--
**Say:** an object lives as long as the program; its numbers live as long as the file. JSON is the text format of Lecture 5.
(~2 min)
-->
---
hideInToc: true
---

# Why Library Models Are **Objects**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **Model** | **Its numbers** | **`fit` sets them from** | **`predict` gives** |
| --- | --- | --- | --- |
| a straight line | slope, intercept: −0.56 °C per decade | the ten yearly means | the mean of a year |
| the perceptron | $w_1$, $w_2$, $b$ | the evenings and their mornings | frost or not |
| any model of a library | its own | inputs and their answers | an answer for new inputs |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ One shape for every model: make it, `fit` it, `predict` with it. Trying another model changes one line.

</div>

<!--
**Say:** this is why the models of a library are objects: what was learned from the data stays inside the object, and every model answers the same two calls. A test written against `fit` and `predict` keeps working when the inside changes.
**If asked:** libraries keep the learned numbers in attributes; scikit-learn's perceptron calls its weights `coef_`.
(~2 min)
-->

---
hideInToc: true
---

# A Class or **Functions**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔧 **Functions**

Data in, result out, nothing kept between calls.

`read_lines`, `temp_of`, `temps`, `mean`

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **A class**

Numbers that several functions share, and that change together.

The perceptron's $w_1$, $w_2$, $b$

</div>

</div>

<div class="note-text mt-md"><code>weather.py</code> stays a module of functions. A class earns its place when the same numbers would otherwise travel with every call.</div>

<!--
**Say:** a class is not better than a function; it is the right shape when data and its methods belong together.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# **Tests**

A fact known without the code, checked by the code on every run.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# The Mean of the Six Hours, **by Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| **time** | **temp_c** |
| --- | --- |
| 2019-07-21T20:00 | 27.3 |
| 2019-07-21T21:00 | 25.6 |
| 2019-07-21T22:00 | 24.6 |
| 2019-07-21T23:00 | 23.6 |
| 2019-07-22T00:00 | −999 |
| 2019-07-22T01:00 | −999 |

</div>

<div class="card card-info card-glass pad-compact">

## ✏️ **By hand**

<v-click>

$$
\bar{x} = \frac{27.3 + 25.6 + 24.6 + 23.6}{4}
$$

</v-click>

<v-click>

$$
= \frac{101.1}{4} = 25.275
$$

</v-click>

<v-click>

The two −999 are left out: the sensor failed at midnight.

</v-click>

</div>

</div>

<!--
**Say:** a pencil gives 25.275, and so does any calculator. Nothing in `weather.py` is needed for it. That is what makes it a test: the number comes from outside the code.
(~2 min)
-->

---
hideInToc: true
---

# assert: Silent When True, **AssertionError** When False

```py {monaco-run} {autorun:false}
assert 87672 - 120 == 87552    # true: nothing happens
print("still running")
assert 87672 - 120 == 87553    # false: AssertionError
print("never printed")
```

<div class="note-text mt-md"><code>assert</code> and a statement: when it is false, the program stops with <code>AssertionError</code>.</div>

<!--
**Do:** press ▶: one line printed, then the error.
**Say:** 87 672 rows, 120 of them −999: 87 552 measured hours, the count the README states.
(~2 min)
-->

---
hideInToc: true
---

# A Test of mean, Run: **AssertionError**

```py {monaco-run} {autorun:false}
def mean(values):
    return sum(values) / len(values)

def test_mean_of_four_hours():
    four = [27.3, 25.6, 24.6, 23.6]
    assert mean(four) == 25.275, mean(four)

test_mean_of_four_hours()     # AssertionError
```

<div class="note-text mt-md">A <strong>test</strong>: a function named <code>test_…</code> that runs the code on an input whose answer is known, and asserts the answer. After the comma: what to print when it fails.</div>

<!--
**Ask:** before ▶: does it pass?
**Do:** press ▶: `AssertionError: 25.275000000000002`.
(~2 min)
-->

---
hideInToc: true
---

# Read the **Failure**

<div class="card card-warning card-glass pad-compact mt-sm">

```text
$ python test_mean.py
Traceback (most recent call last):
  File ".../test_mean.py", line 8, in <module>
    test_mean_of_four_hours()
  File ".../test_mean.py", line 6, in test_mean_of_four_hours
    assert mean(four) == 25.275, mean(four)
           ^^^^^^^^^^^^^^^^^^^^
AssertionError: 25.275000000000002
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🧪 **Which test:** `test_mean_of_four_hours`

</div>

<div class="card card-secondary card-glass pad-compact">

📍 **Which line:** 6, the `assert`

</div>

<div class="card card-accent card-glass pad-compact">

🔢 **Which value:** 25.275000000000002, not 25.275

</div>

</div>

<!--
**Ask:** is `mean` wrong, or is the test wrong?
**Say:** read from the bottom up: what went wrong, where, and which test called it. The code is right; the test asks for more digits than a float can promise.
(~2 min)
-->

---
hideInToc: true
---

# Why the Last Digit Is **2**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| | **Exact value** | **Printed** |
| --- | --- | --- |
| `27.3`, as stored | 27.300 000 000 000 000 711… | 27.3 |
| the four stored values, added exactly | 101.100 000 000 000 004 97… | |
| the nearest float: `sum(four)` | 101.100 000 000 000 008 53… | 101.10000000000001 |
| divided by 4 | 25.275 000 000 000 002 13… | 25.275000000000002 |
| `25.275`, as stored | 25.274 999 999 999 998 58… | 25.275 |

</div>

<div class="note-text mt-md">A float keeps about 16 digits. The two differ by 3.6 × 10⁻¹⁵; <code>==</code> compares every digit.</div>

<!--
**Say:** none of the four temperatures is stored exactly; their sum is rounded once more. 25.275 itself is stored a hair below.
**If asked:** Python 3.11 added the four one after the other and its rounding errors happened to land on 101.1. Since 3.12, `sum` corrects for rounding and finds the float nearest the exact sum, which prints longer.
(~2 min)
-->

---
hideInToc: true
---

# Compare Within a **Tolerance**

<div class="card card-info card-glass pad-compact mt-sm">

$$
|\bar{x} - 25.275| < 10^{-9}
$$

</div>

```py {monaco-run} {autorun:false}
def mean(values):
    return sum(values) / len(values)

four = [27.3, 25.6, 24.6, 23.6]
six = four + [-999, -999]
print(abs(mean(four) - 25.275))          # 3.552713678800501e-15
print(abs(mean(four) - 25.275) < 1e-9)   # True
print(abs(mean(six) - 25.275))           # 341.425
print(abs(mean(six) - 25.275) < 1e-9)    # False
```

<div class="note-text mt-sm">10⁻⁹ lets the rounding through and stops a real mistake: the −999 left in give −316.15, 341.425 away.</div>

<!--
**Do:** press ▶: four lines.
**Say:** `abs` is the distance, without its sign; `1e-9` is 0.000000001. The tolerance is chosen far above the rounding, 10⁻¹⁵, and far below any mistake that matters.
(~2 min)
-->

---
hideInToc: true
---

# A Test of the **Object**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🧪 **Two evenings, z worked out by hand**

```python
def test_rule_below_3_8():
    model = Perceptron()
    model.w = [-1.0, 0.0]
    model.b = 3.8
    assert model.predict([2.6, 0.85]) == 1   # z = -2.6 + 3.8 = 1.2
    assert model.predict([5.4, 0.75]) == 0   # z = -5.4 + 3.8 = -1.6
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The test checks the arithmetic of `predict`, not the weather: after 1 November 2024 frost came, −0.2 °C at 06:00, and the rule said none.

</div>

<!--
**Say:** an object is tested like a function: make it, give it numbers known in advance, assert what it must answer. A `fit` is tested the same way, on data whose answer is known: the AND table of Lecture 10 must come out 0, 0, 0, 1.
(~2 min)
-->

---
hideInToc: true
---

# A Test of the **Result File**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧪 **`scripts/test_weather.py`**

```python
def test_mean_temperature():
    stats = {}
    for line in open("results/temp_c.txt").read().splitlines():
        parts = line.split()
        stats[parts[0]] = parts[1]
    assert stats["rows"] == "87552"
    assert abs(float(stats["mean"]) - 7.16) < 0.005
```

</div>

<div>

<div class="card card-success card-glass pad-compact">

✅ `results/temp_c.txt` as made from `weather_valid.csv`

```text
rows    87552
mean    7.15997
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❌ Tomas's change: made from the raw file

```text
rows    87672
mean    5.7828
```

</div>

</div>

</div>

<!--
**Say:** the second kind of test reads what the rebuild wrote. 87 552 comes from the README: 87 672 hours, 120 of them −999. 7.16 is the README's number, so the tolerance is half of its last digit.
**Ask:** which assert catches Tomas's change first? The count: 87 672.
(~3 min)
-->

---
hideInToc: true
---

# The Tests Stand Beside the **Module**

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 🧪 **`scripts/test_weather.py`**

```python
import weather

def test_temp_of():
    assert weather.temp_of("2019-07-21T20:00,27.3,63,4.5") == 27.3

def test_mean_of_four_hours():
    m = weather.mean([27.3, 25.6, 24.6, 23.6])
    assert abs(m - 25.275) < 1e-9

def test_mean_temperature():
    ...   # the result file: 87552 rows, 7.16
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📁 **Why in `scripts/`**

- beside `weather.py`, so `import weather` finds it
- one fact per test, each named after its fact
- run from the project folder, so `results/temp_c.txt` is found

</div>

</div>

<!--
**Say:** three tests, one file, beside the module it tests: a line, four hours, the result. Larger projects keep their tests in a folder `tests/` and tell the runner where the module is; one file beside the module needs no setting.
(~2 min)
-->

---
hideInToc: true
---

# A Mistake Found Once Gets a **Test**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🕵️ **Without a test: found by a person**

Commit `85e435e`, "Take the mean over all rows of weather.csv": 5.78 in the README. Found by reading the history, then reverted.

</div>

<div class="card card-success card-glass pad-compact">

## 🧪 **Today: checked by the code**

```python
assert stats["rows"] == "87552"
```

The same change now stops every rebuild: 87 672 rows are not 87 552.

</div>

</div>

<div class="note-text mt-md">A mistake that happened once can happen again. Its test makes sure it is noticed in a second, not in a month.</div>

<!--
**Say:** the habit that pays most: when a mistake is found, first a test that fails on it, then the repair. The test stays.
(~2 min)
-->

---
hideInToc: true
---

# Two Kinds of **Test**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| | **A test of a function** | **A test of the result** |
| --- | --- | --- |
| checks | `mean`, on four hours typed in | `results/temp_c.txt`, after the rebuild |
| the fact | 25.275, by hand | 87 552 rows and 7.16, from the README |
| catches | a wrong formula | a wrong file, column or step |
| runs | in a millisecond | after every rebuild |

</div>

<!--
**Say:** both are functions named `test_…` in the same file. The first checks one piece on a case worked by hand; the second checks the end of the whole chain.
(~2 min)
-->

---
hideInToc: true
---

# A Test Must Be Able to **Fail**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ❌ **Cannot fail**

```python
assert mean(four) == mean(four)
```

True for any `mean`, right or wrong.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Seen to fail once**

```python
return sum(values) / (len(values) - 1)
```

A broken `mean` gives 33.7: the test stops it. Then the line is put back.

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🎯 **Worth a test:** a count (87 552), a value by hand (25.275), a mistake that happened once (5.78)

</div>

<div class="card card-secondary card-glass pad-compact">

🎨 **Not worth a test:** the colour of a line, the wording of a label

</div>

</div>

<!--
**Say:** a fact from outside the code, one fact per test, and a test that has been seen to fail. A test that has never failed may be checking nothing.
(~2 min)
-->

---
hideInToc: true
---

# A Test Runner Runs **Every** Test

<div class="grid-2 mt-sm gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **All pass**

```text
$ python -m pytest -q
...                       [100%]
3 passed in 0.01s
```

</div>

<div class="card card-warning card-glass pad-compact">

## ❌ **One fails**

```text
$ python -m pytest -q
..F                       [100%]
...
1 failed, 2 passed in 0.01s
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔍 It finds every function named `test_…` in files named `test_….py` and runs each: a dot per pass, `F` per failure. Its exit status is 0 only when every test passed.

</div>

<!--
**Say:** the runner is pytest, a package; it does what the last slides did by hand, for every test at once, and prints the failing line with its values.
**If asked:** `-q` is the short form: one line of dots and the summary.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Environments**

Which Python and which packages a result was made with.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# Python 3.12 Changed the Last Digit of **7.16**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| | **Python 3.11** | **Python 3.12, 3.13, 3.14** |
| --- | --- | --- |
| `sum` of the 87 552 hours | 626 869.300 000 000 9 | 626 869.3 |
| their mean | 7.159 965 506 213 46 | 7.159 965 506 213 45 |
| the four hours, `sum(v) / len(v)` | 25.275 | 25.275000000000002 |
| `== 25.275` | `True` | `False` |

</div>

<div class="note-text mt-md">Since 3.12, <code>sum</code> corrects floats for rounding. 7.16 stays 7.16; an exact comparison does not survive the upgrade.</div>

<!--
**Say:** every value on the slide was run in Python 3.11.18, 3.12.12, 3.13.9 and 3.14.10. The opening slide, explained: the version of Python is part of the result.
**Ask:** which of the two fixes would have kept the test of 25.275 green on both laptops? A tolerance, or the same Python on both.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# pandas Brings **NumPy**

<div class="card card-info card-glass pad-compact mt-sm">

📦 `python=3.14 pandas=3.1` on macOS: 2 asked for, 32 installed; Python alone is 18. On Windows: 36 and 20.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_tree_pandas.svg">

<!--
**Say:** a package names the packages it needs, its dependencies, each with a range of versions; they name theirs. NumPy brings a library for linear algebra, OpenBLAS, and the compiled libraries it runs on.
**If asked:** counted by solving the environment on conda-forge without installing it, on 9 November 2026.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Four Packages and Everything They **Need**

<div class="card card-info card-glass pad-compact mt-sm">

🧮 Python, Matplotlib, pandas, pytest: 4 asked for; 89 installed on macOS, 88 on Windows, 95 on Linux.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_env.svg">

<!--
**Say:** one square per package of the environment `analysis` on a Mac. Nobody chose the 85 grey ones; the package manager did, from the ranges the four ask for.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# One NumPy That Fits **Every** Range

<div class="card card-info card-glass pad-compact mt-sm">

🎯 Together: ≥ 2.0.2 and < 3, 30 releases. The newest of them, 2.5.4, is installed.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_numpy_ranges.svg">

<!--
**Say:** three packages of the environment need NumPy, each within its own range. The package manager looks for one version inside all of them, and takes the newest: [1.25, 3) ∩ [2.0, ∞) ∩ [2.0.2, ∞) = [2.0.2, 3).
**If asked:** when no version fits every range, the install stops with a conflict; that is what "solving the environment" means.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# pandas Releases **Since 2023**

<div class="card card-info card-glass pad-compact mt-sm">

📅 The newest pandas on 1 October 2025: 2.3.3. On 9 November 2026: 3.1.1, a new major version.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_pandas_versions.svg">

<!--
**Say:** every dot is a release on conda-forge. A line `- pandas` with no version gets the newest on the day the environment is made.
**If asked:** pandas 3.0 changed defaults that old code relied on, among them copy-on-write and a new type for text (Lecture 5).
(~2 min)
-->

---
hideInToc: true
---

# Ranges and Pins in **environment.yml**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| **The line** | **Allows** | **Made on 1 Oct 2025** | **Made on 9 Nov 2026** |
| --- | --- | --- | --- |
| `- pandas` | any version | 2.3.3 | 3.1.1 |
| `- pandas=2.3` | 2.3.0, 2.3.1, … | 2.3.3 | 2.3.3 |
| `- pandas=2.3.3` | 2.3.3 only | 2.3.3 | 2.3.3 |

</div>

<div class="note-text mt-md">A <strong>range</strong> follows new releases; a <strong>pin</strong> names one version. The same line, a year apart.</div>

<!--
**Say:** `pandas=2.3` lets fixes in, 2.3.4 if it ever comes; `pandas=2.3.3` lets nothing in. The course's files so far used ranges, `pandas=3.1`; today they get pins.
(~2 min)
-->

---
hideInToc: true
---

# One Pin Moves **Another** Package

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| **Asked for** | **pandas** | **NumPy installed** |
| --- | --- | --- |
| `python=3.14 pandas=3.1` | 3.1.1 | 2.5.4 |
| `python=3.11 pandas=3.1` | 3.1.1 | 2.4.6 |

</div>

<div class="note-text mt-md">NumPy 2.5 has no build for Python 3.11, so the newest that has one is taken. Solved on conda-forge, 9 November 2026.</div>

<!--
**Say:** nobody asked for NumPy, and the pin on Python decided its version. The packages are one puzzle, solved together.
(~1 min)
-->

---
hideInToc: true
---

# Write It Down After **Every Install**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ conda install pytest=9.2
...
  added / updated specs:
    - pytest=9.2
...
$ conda env export --from-history -f environment.yml
```

8 packages: pytest and 7 it needs, 1.4 MB.

</div>

<div class="card card-success card-glass pad-compact">

## 📄 **`environment.yml`, the `prefix:` line deleted**

```yaml
name: analysis
channels:
  - conda-forge
dependencies:
  - python=3.14
  - matplotlib-base=3.11
  - pandas=3.1
  - pytest=9.2
```

</div>

</div>

<!--
**Say:** `--from-history` writes what was asked for, not the 89 packages that came with it. The last line, `prefix:`, names a folder on this laptop and is deleted. The order of the first lines can differ between laptops; the new package comes last.
(~2 min)
-->

---
hideInToc: true
---

# What the File Fixes, and What It **Does Not**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **`environment.yml` lists** | **Fixed** | **Chosen on the day** |
| --- | --- | --- |
| ranges: `pandas=3.1` | the major and minor of 4 packages | their last digit; the other 85 |
| exact versions: `pandas=3.1.1` | the 4 asked for | the 85 they need |
| every package, with its build | all 89 | nothing, on macOS; on Windows it does not install |

</div>

<div class="note-text mt-md">The same file brings OpenBLAS on macOS and Intel's MKL on Windows: the system is not in the file.</div>

<!--
**Say:** exact versions of the packages asked for is the course's choice: it installs on every system, and the result is checked anyway, by the tests.
**If asked:** the full list is `conda env export` without `--from-history`: 89 lines with builds, valid on one system only.
(~2 min)
-->

---
hideInToc: true
---

# A Fresh Environment Is the **Proof**

<div class="card card-warning card-glass pad-compact mt-sm">

## 🧪 **pytest installed by hand, never written into `environment.yml`**

```text
$ conda env create -n check -f environment.yml
$ conda activate check
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
/Users/smilte/miniforge3/envs/check/bin/python: No module named pytest
$ echo $?
1
```

</div>

<div class="note-text mt-md">On the laptop that made it, everything ran. Only an environment made from the file alone shows what the file forgot.</div>

<!--
**Say:** the environment of the laptop holds everything ever installed into it. A new one, made from `environment.yml` and nothing else, is the colleague's laptop, tried on your own.
(~2 min)
-->

---
hideInToc: true
---

# The Project's environment.yml, **Pinned**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **The exact versions**

```text
$ conda list "^(python|matplotlib-base|pandas|pytest)$"
...
matplotlib-base     3.11.2
pandas              3.1.1
pytest              9.2.0
python              3.14.10
```

</div>

<div class="card card-success card-glass pad-compact">

## 📌 **`environment.yml`**

```yaml
name: analysis
channels:
  - conda-forge
dependencies:
  - python=3.14.10
  - matplotlib-base=3.11.2
  - pandas=3.1.1
  - pytest=9.2.0
```

</div>

</div>

<!--
**Say:** four lines that name exact versions; a fresh environment from this file is made before the result leaves the laptop.
**If asked:** `conda list` also prints a build and a channel for each package; the slide cuts them.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# One **Command**

`rebuild.sh` makes every result again, then checks it.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# rebuild.sh Before the **Tests**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/rebuild.sh`**

```bash
#!/usr/bin/env bash
set -e
mkdir -p data/processed results
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
```

</div>

<!--
**Say:** the room has had this file since Lecture 4: every line typed then, in order. It makes `data/processed` and `results` from `data/raw`.
(~2 min)
-->

---
hideInToc: true
---

# The Tests as Its **Last Line**

<div class="card card-primary card-glass pad-compact mt-sm">

````md magic-move
```bash
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```
```bash
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
python -m pytest -q
```
````

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
...                       [100%]
3 passed in 0.00s
$ echo $?
0
```

</div>

<!--
**Say:** one line more: after every result is made, every test runs on it. The lines above write the files, the tests read them, so the tests come last.
(~2 min)
-->

---
hideInToc: true
---

# set -e: the First Failure **Stops** It

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **Line of `rebuild.sh`** | **Exit status** | **With a wrong file** |
| --- | --- | --- |
| `grep -v ',-999,' …` | 0 | 0 |
| `python scripts/clean_export.py …` | 0 | 0 |
| `python scripts/column_stats.py …` | 0 | 0 |
| `python -m pytest -q` | 0 | 1 |
| **the script** | **0** | **1** |

</div>

<div class="note-text mt-md">The script ends with 0 only when every line ended with 0. <code>$?</code> holds the last one.</div>

<!--
**Say:** Lecture 4's `set -e`: a line that ends with anything but 0 stops the script, and the script hands that number on. With the tests as the last line, a wrong number becomes a failed rebuild.
(~2 min)
-->

---
hideInToc: true
---

# A Wrong Mean Stops the **Rebuild**

<div class="card card-warning card-glass pad-compact mt-sm">

## ❌ **Tomas's change: `column_stats.py data/raw/weather.csv`**

```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
..F                       [100%]
...
>       assert stats["rows"] == "87552"
E       AssertionError: assert '87672' == '87552'
...
FAILED scripts/test_weather.py::test_mean_temperature - AssertionError: asser...
1 failed, 2 passed in 0.01s
$ echo $?
1
```

</div>

<div class="note-text mt-md">The file says 5.78 and the rebuild says it failed. Without the tests, the same change was found only by reading the history.</div>

<!--
**Say:** the result was written, the check refused it. Without the last line, 5.78 would have gone into the README with nothing said.
**If asked:** pytest prints more lines than the slide: the whole test, the line marked `>`, the values marked `E`, and a summary.
(~2 min)
-->

---
hideInToc: true
---

# Why the Tests Come **Last**

<div class="card card-primary card-glass pad-tight table-compact mt-md">

| **Where the tests stand** | **With Tomas's change** | **`$?`** |
| --- | --- | --- |
| the last line | the wrong file is written, the tests read it: `1 failed` | 1 |
| before `column_stats.py` | the tests read the file of the run before: `3 passed`; then 5.7828 is written | 0 |

</div>

<div class="note-text mt-md">A test of the result reads what the lines above it wrote, so it runs after them.</div>

<!--
**Say:** both orders were run on the weather project. With the tests too early, the rebuild reports success over a wrong number.
(~2 min)
-->

---
hideInToc: true
---

# How to Rebuild, in the **README**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **`README.md`**

```md
## How to rebuild

In the project folder, in zsh on macOS or Git Bash on Windows, with
Miniforge:

    conda env create -f environment.yml
    conda activate analysis
    ./scripts/rebuild.sh

It makes `data/processed` and `results` from `data/raw`, then runs the
tests: `3 passed`.
```

</div>

<!--
**Say:** three lines a stranger types: the environment from the file, then the one command, which rebuilds and checks. The section passes when someone follows it on another laptop without asking a question.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Delete and **Rebuild**

Fresh folders, the same bytes.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# Delete the Results, Rebuild, **Compare**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Git Bash** · on macOS `shasum -a 256`

````md magic-move
```text
$ sha256sum data/processed/*.csv results/temp_c.txt
33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
ade2805b90fe64a0053fa65e28329eee616ad0389f9ca55db86400b1c7a9a18b  results/temp_c.txt
```
```text
$ rm -r data/processed results
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
...                       [100%]
3 passed in 0.00s
```
```text
$ sha256sum data/processed/*.csv results/temp_c.txt
33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
85b1f38d0df905a9232078d97c6bb21455e87239ea8754faceda0d868b564881  data/processed/weather_valid.csv
ade2805b90fe64a0053fa65e28329eee616ad0389f9ca55db86400b1c7a9a18b  results/temp_c.txt
```
````

</div>

<div class="note-text mt-md">Every file made again from <code>data/raw</code>, the same bytes: no result was edited by hand.</div>

<!--
**Do:** click through: the checksums, the delete and the rebuild, the checksums again.
**Say:** a checksum changes when any byte changes; three equal lines mean three equal files.
(~2 min)
-->

---
hideInToc: true
---

# A Fresh Clone Holds Only What Was **Committed**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ cd ~
$ git clone weather-s12 weather-check
Cloning into 'weather-check'...
done.
$ cd weather-check
$ ls data
raw
```
```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
...                       [100%]
3 passed in 0.01s
$ sha256sum data/processed/*.csv results/temp_c.txt
33fe5e77…  data/processed/daily.csv
85b1f38d…  data/processed/weather_valid.csv
ade2805b…  results/temp_c.txt
```
````

</div>

<div class="note-text mt-md">A clone has the committed files and nothing else: what a colleague gets from GitHub.</div>

<!--
**Do:** first step: the clone has no `data/processed` and no `results`; click: one command makes them, with the same checksums.
**Say:** cloning a folder on the same laptop is the stranger's copy without the network: only what is in Git arrives.
(~2 min)
-->

---
hideInToc: true
---

# What Goes into **Git**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **`.gitignore`**

```text
data/processed/
results/
__pycache__/
.pytest_cache/
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

| **Files** | **In Git** |
| --- | --- |
| `data/raw`, `scripts`, `environment.yml`, `README.md` | yes: written or received |
| `data/processed`, `results` | no: made by `rebuild.sh` |
| `__pycache__`, `.pytest_cache` | no: notes Python and pytest keep |

</div>

</div>

<div class="note-text mt-md">What a person wrote goes in; what a command makes stays out. The clone then rebuilds the rest.</div>

<!--
**If asked:** `weather.csv`, 2.5 MB, is ours to share and small; a raw file that is large or not ours stays out, and the README says where to fetch it and gives its checksum.
(~2 min)
-->

---
hideInToc: true
---

# A Test File Never **Committed**

<div class="card card-warning card-glass pad-compact mt-sm">

## ❌ **`git status` showed `?? scripts/test_weather.py`, and it stayed so**

```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv

no tests ran in 0.00s
$ echo $?
5
```

</div>

<div class="note-text mt-md">On the author's laptop: <code>3 passed</code>. In the clone the file is missing, and pytest's exit status 5 stops the rebuild.</div>

<!--
**Say:** a file that exists only on one laptop is a step that exists only in the author's head. The fresh clone finds it in a second.
(~2 min)
-->

---
hideInToc: true
---

# Four Tests of a Reproducible **Result**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **Another…** | **Tried with** | **Found** |
| --- | --- | --- |
| folder | a fresh clone | a file never committed |
| laptop | an environment from `environment.yml` alone | a package never written down |
| time | pinned versions | a new release that changes a digit |
| system | macOS beside Windows | `temp_c.txt`: 113 bytes and 119 |

</div>

<div class="note-text mt-md">Windows ends each of the 6 lines of <code>temp_c.txt</code> with CRLF, one byte more: another checksum, the same mean. The test reads the number, so it passes on both.</div>

<!--
**Say:** another person, another computer, a later time: each has a test that takes a minute. The checksums of the two CSV files are the same on every system; the README states those.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The Four **Aims**

FAIR, a checklist for the project, and how to check 7.16.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# **FAIR**: Data Others Can Use

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **Findable**

A permanent address and an identifier: `github.com/MindaugasSarpis/weather-project`; a DOI for a finished version

</div>

<div class="card card-secondary card-glass pad-compact">

## 🌐 **Accessible**

Fetched over HTTPS without a login: `git clone`, a zip from the release

</div>

<div class="card card-accent card-glass pad-compact">

## 🔗 **Interoperable**

Open formats and standard units: CSV, ISO 8601 times, °C named in the README

</div>

<div class="card card-success card-glass pad-compact">

## ♻️ **Reusable**

A licence, where the data came from, and one command that rebuilds

</div>

</div>

<div class="note-text mt-sm">Wilkinson et al., <em>The FAIR Guiding Principles for scientific data management and stewardship</em>, Scientific Data 3, 160018 (2016).</div>

<!--
**Say:** funders and journals ask for FAIR. It does not say "open": data can be FAIR behind a login. It says that a stranger, or a program, can find out what the data is and how to get it.
**If asked:** Zenodo, run by CERN, stores a copy of a GitHub release and gives it a DOI.
(~2 min)
-->

---
hideInToc: true
---

# The Four Aims, Each With Its **File**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔧 **Tool-agnostic**

Plain text throughout: CSV, `.py`, `.yml`, `.md`; one `rebuild.sh` for zsh and Git Bash

</div>

<div class="card card-secondary card-glass pad-compact">

## ♻️ **Reproducible**

`environment.yml` pinned; a fresh clone in a fresh environment gives the same checksums

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Automated**

`./scripts/rebuild.sh`: every result, then 3 tests, one exit status

</div>

<div class="card card-success card-glass pad-compact">

## 📁 **Data & files**

`data/raw` never written, SHA-256 `3f1ad06d…`; `data/processed` and `results` deleted at will

</div>

</div>

<!--
**Say:** the four piles of answers from the first lecture, each now a file in the folder.
(~2 min)
-->

---
hideInToc: true
---

# A Checklist for the **Project**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔨 **Rebuild**

1. Does the README say where the data came from?
2. Does one command rebuild every number and figure?
3. Do the rebuilt numbers equal those in the report?

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗂️ **Data**

4. Is `data/raw` untouched?
5. Is every removed or changed row listed, with a reason?
6. Are the columns and their units written down?

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **Method**

7. Was the question fixed before the result was seen?
8. Does every result have an uncertainty?
9. Is there a check that could have failed?

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Report**

10. Do the figures have axis labels with units?
11. Does the conclusion claim no more than the numbers?
12. Are sources, data and tools named?

</div>

</div>

<!--
**Say:** twelve questions, each answered yes, no, or "could not tell", by the author first and then by a reviewer. Questions 2 and 3 take the most time and find the most.
**Do:** ask the room to answer them for their own project, now, on paper.
(~3 min)
-->

---
hideInToc: true
---

# Decide Before You **Look**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **Write it first**

The question, the rows, the method, the checks: in the README, committed before the number is computed. The commit carries the date.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🙈 **Blind analysis**

LHC experiments hide the region where a signal would be until the selection and the fit are fixed and reviewed.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔢 **Count the looks**

Seven ways to take the mean of one file give 5.78 to 7.29. The one picked after seeing all seven is not a result.

</div>

</div>

<!--
**Say:** question 7 of the checklist, the one a folder cannot answer by itself: was the method chosen before the number was seen? A dated commit answers it.
(~2 min)
-->

---
hideInToc: true
---

# The Weather Project, **Checked**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| | **The weather project** |
| --- | --- |
| 1–3 | the station's operator, received 13 Oct 2026; `./scripts/rebuild.sh`; 7.15997, reported as 7.16 |
| 4–6 | SHA-256 `3f1ad06d…`; 120 hours of −999, 22 to 26 July 2019; four columns with units |
| 7–9 | the mean of the measured hours, committed before the number; 7.16 ± 0.22 °C from the ten yearly means; 3 tests |
| 10–12 | °C on every axis; "no trend": the slope, −0.56 ± 0.77 °C per decade; the README |

</div>

<div class="note-text mt-md">Twelve yes. Each answer points to a file or a number.</div>

<!--
**Say:** the course's own example, run through the checklist: every answer has evidence the reviewer can open. Question 11 is the one most reports fail: ten years of yearly means do not show a trend, and the conclusion says so.
(~2 min)
-->

---
hideInToc: true
---

# A Review Comment Someone Can **Act On**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ❌ **Vague**

"The numbers seem off. Please check the analysis."

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Run, placed, marked**

**Must fix.** On Windows, Git Bash, Python 3.14.10: `./scripts/rebuild.sh` ends with `1 failed, 2 passed`. Line 6 reads `data/raw/weather.csv`, so `temp_c.txt` has 87 672 rows; the README's 7.16 needs `weather_valid.csv`.

</div>

</div>

<div class="note-text mt-md">What was run and where, what came out, the file and the line: must fix, suggestion or question.</div>

<!--
**Say:** a reviewer runs the checklist on someone else's folder and writes comments like the right card: the author can act on each without asking back. The comment is about the work, never the person.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Smiltė's 7.16 and Ben's **7.11**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ Smiltė: the mean of every hour. Ben: halfway between each day's lowest and highest hour. On 3648 days the two differ by −1.15 to +0.91 °C, on average −0.05.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_lasting_two_means.svg">

<!--
**Say:** the opening of Lecture 1: one file, two honest methods, 7.16 and 7.11. Ben's midrange looks at two hours of 24: one cold hour at 23:00 on 12 November 2021 pulls it 1.15 °C below the mean.
**If asked:** on 2023 of the 3648 days the midrange is below the mean; the average difference, −0.05, is the gap between 7.16 and 7.11.
(~2 min)
-->

---
hideInToc: true
---

# Ben's Way: One More **Function**

```py {monaco-run} {autorun:false}
def mean(values):
    return sum(values) / len(values)

def midrange(values):
    return (min(values) + max(values)) / 2

four = [27.3, 25.6, 24.6, 23.6]
print(mean(four))       # 25.275000000000002: Smiltė
print(midrange(four))   # 25.450000000000003: Ben, (23.6 + 27.3) / 2
```

<div class="card card-success card-glass pad-compact mt-md">

```python
days = weather.group("data/raw/weather.csv", 0, 10)
mids = []
for day in days:
    mids.append(weather.midrange(days[day]))
print(len(mids), round(weather.mean(mids), 2))     # 3648 7.11
```

</div>

<!--
**Do:** press ▶: the two methods on the four hours, 25.275 and 25.45.
**Say:** Ben's method is one function in the module, tested on the four hours like `mean`; `group` of Lecture 7 gives the hours of each day. The difference between 7.16 and 7.11 is now written down, in code that anyone can run.
(~2 min)
-->

---
hideInToc: true
---

# I Send You Only 7.16. How Do You **Check** It?

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| | **I send you** | **You type** | **You get** |
| --- | --- | --- | --- |
| 📁 | `data/raw/weather.csv` | `sha256sum data/raw/weather.csv` | `3f1ad06d…`, the file I started from |
| ♻️ | `environment.yml`, pinned | `conda env create -f environment.yml` | the same versions |
| ⚙️ | `scripts/rebuild.sh`, with the tests | `./scripts/rebuild.sh` | 7.15997 and `3 passed` |
| 🔧 | plain text: CSV, `.py`, `.md` | any editor | every step, readable |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ **7.16, checked**: rebuilt on your laptop, and Ben's 7.11 is one function away.

</div>

<!--
**Say:** the question of the first lecture, answered with the files of this one. Send the folder, not the number.
(~3 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Put each step in a **module** as a function that returns its result, and keep each file where it belongs

</div>

<div class="card card-success card-glass pad-compact">

✅ Say when data and its methods belong together in an **object**, and why library models are objects

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a **test** from a fact known without the code, compare floats within a tolerance, and read a failure

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **dependency** tree, and choose between a range and a pin in `environment.yml`

</div>

<div class="card card-success card-glass pad-compact">

✅ Rebuild every result and run the tests with **one command**, stopped by the first failure

</div>

<div class="card card-success card-glass pad-compact">

✅ **Prove** a result: delete and rebuild, a fresh clone, a fresh environment, the same checksums

</div>

</div>

<!--
**Ask:** which of the six does your own project lack today?
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

Arguments and a config file, rebuilding only what changed, a server that rebuilds, containers, and how a test runner works.

<!--
**Say:** optional: for time left at the end, or to read afterwards.
(~0.5 min)
-->

---
hideInToc: true
---

# File Names as **Arguments**: argparse

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`scripts/mean_temp.py`**

```python
import argparse
import weather

parser = argparse.ArgumentParser(
    description="Mean temperature of a log.")
parser.add_argument("path", help="CSV file")
args = parser.parse_args()

values = weather.temps(args.path)
print(len(values), round(weather.mean(values), 2))
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ❔ **`--help`, written by argparse**

```text
$ python scripts/mean_temp.py --help
usage: mean_temp.py [-h] path

Mean temperature of a log.

positional arguments:
  path        CSV file
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
$ python scripts/mean_temp.py data/raw/weather.csv
87552 7.16
$ python scripts/mean_temp.py
usage: mean_temp.py [-h] path
mean_temp.py: error: the following arguments are required: path
```

</div>

<!--
**Say:** the file name leaves the code: one script for every log. `column_stats.py` of Lecture 4 already took its file and its column as words after its name; argparse adds names, a help text and checks. Without the file name it ends with exit status 2.
(~2 min)
-->

---
hideInToc: true
---

# The Method in a **Config File**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`config.json`**

```json
{"path": "data/raw/weather.csv", "method": "midrange"}
```

## 📄 **`scripts/mean_by_method.py`**

```python
import json
import weather

config = json.load(open("config.json"))
days = weather.group(config["path"], 0, 10)
values = []
for day in days:
    if config["method"] == "midrange":
        values.append(weather.midrange(days[day]))
    else:
        values.extend(days[day])
print(config["method"], round(weather.mean(values), 2))
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python scripts/mean_by_method.py
midrange 7.11
```

After `"method": "hours"`:

```text
$ python scripts/mean_by_method.py
hours 7.16
```

</div>

</div>

<!--
**Say:** the choices of an analysis, written in one file that Git versions: a change of method is a commit, with a date and a reason.
**If asked:** `extend` adds every value of a list, `append` adds one value.
(~2 min)
-->

---
hideInToc: true
---

# Rebuild Only What **Changed**: Make

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`Makefile`**

```make
results/temp_c.txt: data/processed/weather_valid.csv
	python scripts/column_stats.py $< temp_c > $@

data/processed/weather_valid.csv: data/raw/weather.csv
	grep -v ',-999,' $< > $@
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The rule**

A file is made again when it is missing or older than a file it is made from. `$<` is the first input, `$@` the file made.

`make results/temp_c.txt` runs only the lines that are out of date.

</div>

</div>

<div class="note-text mt-sm">Make (Bell Labs, 1976) on macOS and Linux; Snakemake (2012), a Python package from conda-forge, writes the same rules in Python.</div>

<!--
**Say:** the rebuild of the weather project takes under a second, so it runs whole every time. An analysis with stages of an hour each needs this rule.
**If asked:** Git Bash has no make; `conda install make` adds one.
(~2 min)
-->

---
hideInToc: true
---

# Every Push Rebuilt: **Continuous Integration**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`.github/workflows/rebuild.yml`**

```yaml
name: rebuild
on: [push]
jobs:
  rebuild:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash -el {0}
    steps:
      - uses: actions/checkout@v4
      - uses: conda-incubator/setup-miniconda@v3
        with:
          miniforge-version: latest
          environment-file: environment.yml
          activate-environment: analysis
      - run: ./scripts/rebuild.sh
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🤖 **What GitHub does**

- after every `git push`: a fresh Linux machine, a fresh clone
- Miniforge, the environment from the file
- `./scripts/rebuild.sh`: a red cross on the commit when it ends with anything but 0

The fresh clone and the fresh environment of this lecture, after every push, without anyone remembering.

</div>

</div>

<!--
**Say:** shown as an example, not run for the slides. The course's own slides are built and checked this way after every push.
(~2 min)
-->

---
hideInToc: true
---

# The System Too: **Containers**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`Dockerfile`**

```dockerfile
FROM condaforge/miniforge3
WORKDIR /project
COPY . .
RUN conda env create -f environment.yml
CMD ["conda", "run", "-n", "analysis", "./scripts/rebuild.sh"]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **An image**

A file holding a small Linux, Miniforge, the environment and the project. `docker build` makes it, `docker run` starts it on any computer with Docker.

</div>

</div>

<div class="note-text mt-sm"><code>environment.yml</code> fixes the packages, not the system: OpenBLAS on macOS, MKL on Windows. A container fixes the system as well, at the cost of installing Docker.</div>

<!--
**Say:** shown as an example, not built for the slides. The experiments at CERN run their analysis software in containers so that a result can be rebuilt years later.
(~2 min)
-->

---
hideInToc: true
---

# How a Test Runner **Finds** the Tests

<div class="grid-2 mt-sm gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **`run_tests.py`**

```python
def mean(values):
    return sum(values) / len(values)

def test_four_hours():
    assert abs(mean([27.3, 25.6, 24.6, 23.6]) - 25.275) < 1e-9

def test_one_hour():
    assert mean([7.16]) == 7.16

for name, thing in list(globals().items()):
    if name.startswith("test_"):
        thing()
        print("passed:", name)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python run_tests.py
passed: test_four_hours
passed: test_one_hour
```

`globals()` holds every name of the program; the loop calls each one that starts with `test_`.

</div>

</div>

<div class="note-text mt-sm">pytest does the same for every file named <code>test_….py</code>, and catches each failure instead of stopping at the first.</div>

<!--
**Say:** no magic in a test runner: names, a loop, a report.
(~2 min)
-->

---
hideInToc: true
---

# Why sum Changed in **Python 3.12**

<div class="card card-primary card-glass pad-tight table-compact mt-sm">

| **Adding 27.3, 25.6, 24.6, 23.6** | **The result, exactly** | **Off by** |
| --- | --- | --- |
| exactly, as stored | 101.100 000 000 000 004 97… | |
| one after the other (3.11) | 101.099 999 999 999 994 32… | 1.07 × 10⁻¹⁴ |
| with a correction (3.12 on) | 101.100 000 000 000 008 53… | 3.55 × 10⁻¹⁵ |

</div>

<div class="note-text mt-md">Each addition rounds; 3.12 keeps the lost part of each rounding and adds it back at the end (Neumaier, 1974). Its result is the nearer float, and it prints longer.</div>

<!--
**Say:** the "pretty" 101.1 of Python 3.11 is the less accurate one. Over the 87 552 hours it is the other way round: 3.11 prints 626 869.3000000009, 3.12 626 869.3.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it.

---
hideInToc: true
---

<MCQ
  question="`assert mean([27.3, 25.6, 24.6, 23.6]) == 25.275` fails: the mean is 25.275000000000002. What is the repair?"
  :options="[
    'Change <code>mean</code> until it returns 25.275 exactly',
    'Compare within a tolerance: <code>abs(mean(four) - 25.275) &lt; 1e-9</code>',
    'Delete the test: floats cannot be tested',
    'Round both sides to whole degrees'
  ]"
  :correct="1"
  explanation="mean is right: the four temperatures are stored in binary with about 16 digits, and their sum is rounded once more. A tolerance of 1e-9 accepts that rounding, 3.6e-15, and still stops a real mistake such as the −999 left in, 341.4 away. Rounding to whole degrees would let mistakes of up to half a degree through."
/>

---
hideInToc: true
---

<MCQ
  question="Which of these is the best test for the cleaned file `weather_valid.csv`?"
  :options="[
    'It has 87 553 lines: 87 672 hours less the 120 marked −999, plus the header, as the README states',
    'Its line count equals the line count that the same script computed a moment earlier',
    'Its checksum equals the checksum it had after the last rebuild, whatever that was',
    'It opens in a spreadsheet without an error'
  ]"
  :correct="0"
  explanation="A test states a fact known without the code: 87 672 hours and 120 marked rows are counts from the README, so 87 553 lines can be wrong only if the cleaning is wrong. Comparing the script with itself can never fail, and a checksum taken from the last run accepts a wrong file once it has been made."
/>

---
hideInToc: true
---

<MCQ
  question="`environment.yml` holds the line `- pandas=3.1`. Which pandas can a fresh environment made next year get?"
  :options="[
    'Exactly 3.1.1, the version of today',
    'The newest 3.1.x on that day: 3.1.1 or a later fix',
    'The newest pandas of any version',
    'None: a range cannot be installed'
  ]"
  :correct="1"
  explanation="pandas=3.1 is a range: every release whose version starts with 3.1. The package manager takes the newest of them on the day the environment is made. A pin, pandas=3.1.1, would allow only 3.1.1; a bare pandas would allow 4.0 as well."
/>

---
hideInToc: true
---

<MCQ
  question="pandas 3.1.1 needs NumPy ≥ 2.0.2; Matplotlib 3.11.2 needs NumPy ≥ 1.25 and < 3. Which NumPy can the environment hold?"
  :options="[
    'Any NumPy ≥ 1.25',
    'NumPy ≥ 2.0.2 and < 3',
    'Two NumPys, one for each package',
    'Only NumPy 2.0.2'
  ]"
  :correct="1"
  explanation="An environment holds one version of each package, and it must lie inside every range at once: [1.25, 3) and [2.0.2, ∞) overlap in [2.0.2, 3). The package manager takes the newest release in it, 2.5.4 on 9 November 2026."
/>

---
hideInToc: true
---

<MCQ
  question="In an environment made fresh from `environment.yml`, `rebuild.sh` stops at its last line: `No module named pytest`. On the author's laptop it passes. What happened?"
  :options="[
    'pytest is broken on the new laptop',
    'pytest was installed into the author\'s environment by hand and never written into environment.yml',
    'The tests found a wrong number',
    'The clone is missing the test file'
  ]"
  :correct="1"
  explanation="The author's environment holds everything ever installed into it; the fresh one holds only what the file lists. conda env export --from-history after each install, and a fresh environment before a result leaves the laptop, catch it. A missing test file gives a different message: no tests ran."
/>

---
hideInToc: true
---

<MCQ
  question="`rebuild.sh` starts with `set -e` and ends with `python -m pytest -q`. One test fails. What is `$?` afterwards?"
  :options="[
    '0, because every result file was written',
    '1, the exit status of pytest, which the script hands on',
    '5, because no tests ran',
    'Nothing: a failed test does not change the exit status'
  ]"
  :correct="1"
  explanation="pytest ends with 1 when a test failed, and with set -e the script stops at that line and ends with the same status. The result files above were written before the tests ran: the status says that they are not to be trusted. pytest ends with 5 when it found no test at all."
/>

---
hideInToc: true
---

<MCQ
  question="After a delete and rebuild, `results/temp_c.txt` has 113 bytes on a Mac and 119 on Windows, and the tests pass on both. Why?"
  :options="[
    'Windows rounds the mean to more digits',
    'Windows ends each of the 6 lines with CRLF; the test reads the number, which is the same',
    'One of the two laptops has a wrong pandas',
    'The checksum test is switched off on Windows'
  ]"
  :correct="1"
  explanation="Python's print ends a line as the system does: LF on macOS, CRLF on Windows, one byte more on each of the 6 lines. The checksums differ, the six lines say the same, and the test compares rows 87552 and mean 7.15997 with 7.16."
/>

---
hideInToc: true
---

<MCQ
  question="A fresh clone runs `rebuild.sh`, and pytest prints `no tests ran` with exit status 5. On the author's laptop: `3 passed`. What is the most likely cause?"
  :options="[
    'The clone is from an older commit of GitHub',
    '<code>scripts/test_weather.py</code> was never committed',
    'pytest is a different version in the clone',
    'The results folder is missing in the clone'
  ]"
  :correct="1"
  explanation="A clone holds only committed files. git status had listed the test file as ?? (untracked), and it stayed on the author's laptop. The results folder is meant to be missing: rebuild.sh makes it."
/>
