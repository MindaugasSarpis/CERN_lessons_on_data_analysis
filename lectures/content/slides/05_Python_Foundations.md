---
layout: cover
title: "Python Foundations"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Python Foundations

##### <span class="aims-badge">🔧 tool-agnostic · ⚙️ automation</span>

<!--
**Say:** Lecture 04 got 7.16 from a program someone else wrote. Today the same number comes from a program written line by line on these slides.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# A program is a text that the interpreter carries out, one statement after another. Today the text that turns `weather.csv` into **7.16 °C** is written in Python

<!--
**Say:** Python is the language; `python` is the program that reads it. Every piece today is short and shown with its output.
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
**Ask:** what does a program have to do to get 7.16 out of `weather.csv`? Collect the steps on the board: read the file, cut each line, turn text into numbers, add, count, leave out −999, print.
(~3 min)
-->

---
hideInToc: true
---

# A Program for 7.16, Step by **Step**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Step | Question | Answer |
| --- | --- | --- |
| 1 | What runs a `.py` file, and in which order? | ? |
| 2 | Is `-4.4` in `weather.csv` a number? | ? |
| 3 | What are the four values of one line? | ? |
| 4 | What is the mean of all 87 672 rows? | ? |
| 5 | What is it without the −999 rows? | ? |
| 6 | How does 7.15996550621346 become 7.16 on the screen? | ? |
| 7 | Which year was the warmest? | ? |
| 8 | Where and why does a script stop? | ? |

</div>

<!--
**Say:** one question per part of the lecture, each answered by a short piece of Python.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Running **Python**

Step 1: what runs a `.py` file, and in which order?

<!--
(~1 min)
-->

---
hideInToc: true
---

# `python` Is a **Program**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**

```text
% type python
python is /opt/homebrew/Caskroom/miniforge/base/bin/python
% python --version
Python 3.14.7
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · Git Bash**

```text
$ type python
python is /c/Users/smilte/miniforge3/python
$ python --version
Python 3.14.7
```

</div>

<div class="note-text mt-md">The <strong>interpreter</strong>: a program that reads Python text and carries out one statement after another. The processor runs only machine code (Lecture 03); <code>python</code> is machine code that reads yours.</div>

<!--
**Say:** the same `type` line as in Lecture 04: `python` is a file in a folder on `PATH`, installed with Miniforge. "Python" names the language, `python` the program.
**If asked:** C or Rust are translated into machine code once, before they run, by a compiler. Python translates each file when it starts, every time.
(~2 min)
-->

---
hideInToc: true
---

# The `>>>` **Prompt**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python
Python 3.14.7 | packaged by conda-forge | …
>>> 365 * 10 + 3
3653
>>> 7.16 * 9 / 5 + 32
44.888
>>> exit()
$
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔀 **Who reads the line**

| Prompt | Read by | `7.16 * 9 / 5 + 32` |
| --- | --- | --- |
| `$`, `%` | the shell | `command not found: 7.16` |
| `>>>` | Python | `44.888` |

</div>

</div>

<div class="note-text mt-md">At <code>&gt;&gt;&gt;</code> Python works out one line and prints its value. 3653 days in ten years, three of them leap years; 7.16 °C is 44.888 °F.</div>

<!--
**Live:** `python`, then the two lines, then `exit()`.
**Ask:** before `Enter` on the second line: what will Python print?
**Say:** the first slip of everyone: Python typed at the shell's prompt, or a shell command typed at `>>>`. The prompt says who reads.
(~3 min)
-->

---
hideInToc: true
---

# A Script: Lines in a **File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`scripts/hours.py`**

```python
days = 365 * 10 + 3    # 2016, 2020, 2024
hours = days * 24
print(hours)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python scripts/hours.py
```

<v-click>

```text
87672
```

</v-click>

</div>

</div>

<div class="note-text mt-md">A script is a text file whose name ends in <code>.py</code>. The shell starts <code>python</code>, and <code>python</code> reads the file. Only <code>print</code> writes to the terminal. <code>#</code> starts a comment: the rest of the line is skipped.</div>

<!--
**Say:** the lines of the prompt, kept in a file; they give the same 87 672 tomorrow. 87 672 is the number of rows Lecture 04 counted with `wc -l`, less the header.
**Ask:** what does the script print without its last line? Nothing: at `>>>` values are shown by themselves, in a script only `print` shows them.
(~2 min)
-->

---
hideInToc: true
---

# Python in **VS Code**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **The Python extension**

- Extensions view, `Python` by Microsoft, **Install**
- Colours the code, completes names, underlines a name that was never made
- Status Bar: `3.14.7`, the interpreter it uses. A click selects another one

</div>

<div class="card card-secondary card-glass pad-compact">

## ▶️ **Run Python File**

The ▶ at the top right of the editor types one line into the terminal: the full path of the interpreter, then the full path of the file.

```text
$ /opt/homebrew/…/base/bin/python /Users/smilte/weather-project/scripts/hours.py
87672
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The extension contains no Python: it runs the interpreter it shows. The file runs as it is saved; a dot on the editor tab means unsaved changes.

</div>

<!--
**Say:** the ▶ button and the typed line do the same thing. The typed line, with relative paths, is the one that goes into a README.
**If asked:** Windows shows `C:\Users\smilte\miniforge3\python.exe` and `C:\Users\smilte\weather-project\scripts\hours.py`.
(~2 min)
-->

---
hideInToc: true
---

# What `python` Does with a **File**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | `python` | With `scripts/hours.py` |
| --- | --- | --- |
| 1 | reads the file's bytes as UTF-8 text | 73 bytes, 3 lines |
| 2 | checks the grammar of the whole file | a missing `)` stops it here: `SyntaxError`, nothing runs |
| 3 | translates it into bytecode, simple steps for itself | |
| 4 | runs the statements from the top, one at a time | line 1, line 2, line 3 |
| 5 | at an error: stops and prints a traceback | exit status 1 |
| 6 | after the last statement: ends | exit status 0, `echo $?` prints `0` |

</div>

<!--
**Say:** the same six-step reading as the shell's in Lecture 04, one level up. Step 2 is why one missing bracket on line 30 means not even line 1 runs.
**Ask:** `print(hours` without its `)` on line 3: does line 1 run? No. Python says `SyntaxError: '(' was never closed` and runs nothing.
**If asked:** the bytecode is kept in `__pycache__` folders for imported modules, so a second start is quicker.
(~3 min)
-->

---
hideInToc: true
---

# The Run Stops at the First **Error**

```py {monaco-run} {autorun:false}
print("start")
hours = 87672
print(hours / 24)    # 3653.0
print(hours / 0)     # ZeroDivisionError
print("end")         # never runs
```

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 1: `python`, the interpreter, checks the whole file, runs it from the top one statement at a time, and stops at the first error.

</div>

<!--
**Ask:** which lines appear before ▶? `start`, `3653.0`, then the error; `end` never.
**Say:** the output before the error is real: those lines ran. The traceback's last line says what stopped the run.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Values and **Types**

Step 2: is `-4.4` in `weather.csv` a number?

<!--
**Say:** Lecture 03 built integers, floats and text out of bits. Python has the same three.
(~1 min)
-->

---
hideInToc: true
---

# Every Value Has a **Type**

```py {monaco-run} {autorun:false}
print(type(87672))      # <class 'int'>
print(type(7.16))       # <class 'float'>
print(type("-4.4"))     # <class 'str'>
print(type(7.16 > 0))   # <class 'bool'>
print(87672 / 24)       # 3653.0: / always gives a float
print(87672 // 24)      # 3653: the whole part, an int
```

<div class="note-text mt-md">The type decides what an operation does with a value. Lecture 03: the same bits mean another value under another type.</div>

<!--
**Ask:** the last two lines: the same division, what does each print? `/` gives a float even when it divides evenly; `//` keeps the whole part.
**Say:** quotes make text. `"-4.4"` is four characters, `-4.4` a number.
(~2 min)
-->

---
hideInToc: true
---

# `int` Has No Fixed **Width**

```py {monaco-run} {autorun:false}
print(127 + 1)                  # 128: no wrap to -128
print(2 ** 63)                  # 9223372036854775808
print(2 ** 100)                 # 1267650600228229401496703205376
print((2 ** 100).bit_length())  # 101 bits
```

<div class="note-text mt-md">In Lecture 03, 8 bits held −128 to 127 and 127 + 1 wrapped to −128. A Python <code>int</code> takes as many bits as its number needs.</div>

<!--
**Ask:** 127 + 1 in Python: 128 or −128?
**Say:** `**` is the power. 2⁶³ does not fit a signed 64-bit integer; Python's `int` grows to 64 bits, then 101, and stays exact.
**If asked:** the price is memory and speed. Large tables of numbers are kept in fixed widths, as the files of Lecture 03 were.
(~2 min)
-->

---
hideInToc: true
---

# `float` Is the float64 of Lecture 03

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
print(f"{7.16:.20f}")     # 7.16000000000000014211
print(-4.4 + 1)           # -3.4000000000000004
```

<div class="note-text mt-md">64 bits: 53 binary digits, about 16 decimal digits. 7.16 has no end in binary, so the nearest float64 is stored, and every sum is rounded.</div>

<!--
**Ask:** −4.4 + 1: what does Python print?
**Say:** the long tails are float64 showing through, not a fault of Python. Measured values are compared with a tolerance, never with `==`.
**If asked:** `:.20f` asks for 20 decimals of the stored value.
(~2 min)
-->

---
hideInToc: true
---

# `str` Is Unicode **Text**

```py {monaco-run} {autorun:false}
temp = "-4.4"
print(len(temp))                  # 4 characters
print(temp + "1")                 # -4.41: text joined to text
unit = "°C"
print(len(unit))                  # 2 characters
print(len(unit.encode("utf-8")))  # 3 bytes: ° is C2 B0
```

<div class="note-text mt-md">A <code>str</code> is a row of Unicode characters. Its bytes appear when it is encoded, as in Lecture 03.</div>

<!--
**Ask:** `temp + "1"`: what comes out? Text plus text is longer text, with no error.
**Say:** `len` counts characters; the bytes of UTF-8 are a different count.
(~2 min)
-->

---
hideInToc: true
---

# A Name Points to a **Value**

<div class="grid-2 mt-md gap-md">

<div>

```py {monaco-run} {autorun:false}
mean = 7.16
old = mean
mean = mean * 9 / 5 + 32
print(mean)   # 44.888
print(old)    # 7.16
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📌 **After line 3**

```text
mean ───▶ 44.888
old  ───▶ 7.16
```

`=` works out the right side first, then puts the name on the result. A name with its value is a **variable**.

</div>

</div>

<div class="note-text mt-md">A spreadsheet cell <code>=A1*9/5+32</code> follows A1. A Python name does not follow anything: line 3 ran once, with the value <code>mean</code> had then.</div>

<!--
**Ask:** what does `old` hold after line 3?
**Say:** line 3 moves the name `mean` to a new value. `old` still points to 7.16. `=` is not the equals of mathematics: `count = count + 1` adds one.
**If asked:** a name has letters, digits and `_`, no digit first, and case counts: `Mean` and `mean` are two names.
(~3 min)
-->

---
hideInToc: true
---

# `bool`: **Comparisons**

```py {monaco-run} {autorun:false}
temp = -999.0
print(temp == -999)      # True: -999.0 equals -999
print(temp < -50)        # True
print(-50 < temp < 50)   # False
print("-999" == -999)    # False: text is never a number
```

<div class="note-text mt-md"><code>=</code> puts a name on a value. <code>==</code> asks whether two values are equal and answers <code>True</code> or <code>False</code>.</div>

<!--
**Ask:** the last line: True or False?
**Say:** the last comparison is the dangerous one: it fails with no error and no warning.
(~2 min)
-->

---
hideInToc: true
---

# From Text to **Number**: `float` and `int`

```py {monaco-run} {autorun:false}
print(float("-4.4"))       # -4.4
print(float("-4.4") + 1)   # -3.4000000000000004
print(int("93") + 1)       # 94
print(float("-999"))       # -999.0
print("-4.4" + 1)          # TypeError
```

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 2: no. In the file `-4.4` is text, four characters. `float("-4.4")` makes the float64 that arithmetic works on.

</div>

<!--
**Ask:** the last line: `-3.4`, `-4.41` or an error? Text and a number do not add: `TypeError: can only concatenate str (not "int") to str`.
**Say:** the type name converts: `float(...)`, `int(...)`, `str(...)`. A file holds text; a value becomes a number only by a step the program states.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# One **Line**

Step 3: what are the four values of one line of `weather.csv`?

<!--
(~1 min)
-->

---
hideInToc: true
---

# Index and **Slice**

```py {monaco-run} {autorun:false}
line = "2016-01-01T00:00,-4.4,93,2.5"
print(len(line))    # 28
print(line[0])      # 2
print(line[0:4])    # 2016: the year
print(line[5:7])    # 01: the month
print(line[-3:])    # 2.5
```

<div class="note-text mt-md">Positions count from 0. <code>[start:stop]</code> stops before <code>stop</code>; a negative position counts from the end. In the file the line has 29 bytes: 28 characters and LF.</div>

<!--
**Do:** draw the first ten characters on the board with their positions 0 to 9 below them.
**Ask:** what is `line[5:7]`? Positions 5 and 6: `01`.
**Say:** the 29 bytes are the row of Lecture 03; every character here is ASCII, one byte each.
(~3 min)
-->

---
hideInToc: true
---

# Cut at the Commas: `split`

```py {monaco-run} {autorun:false}
line = "2016-01-01T00:00,-4.4,93,2.5"
parts = line.split(",")
print(parts)           # ['2016-01-01T00:00', '-4.4', '93', '2.5']
print(len(parts))      # 4
print(parts[1])        # -4.4
print(type(parts[1]))  # <class 'str'>
```

<div class="note-text mt-md"><code>split</code> is a <strong>method</strong>: a function that belongs to a value and is written after a dot. It hands back a <strong>list</strong> of four strings.</div>

<!--
**Ask:** after the split, is `parts[1]` a number?
**Say:** the commas are gone; the four pieces are still text. A list is written in square brackets and indexed like a string.
(~2 min)
-->

---
hideInToc: true
---

# Convert Each **Part**

```py {monaco-run} {autorun:false}
line = "2016-01-01T00:00,-4.4,93,2.5"
parts = line.split(",")
time = parts[0]
temp_c = float(parts[1])
humidity_pct = int(parts[2])
wind_ms = float(parts[3])
print(time, temp_c, humidity_pct, wind_ms)  # 2016-01-01T00:00 -4.4 93 2.5
print(temp_c * 9 / 5 + 32)                  # 24.08
```

<div class="card card-success card-glass pad-compact mt-sm">

✅ Step 3: `'2016-01-01T00:00'`, `-4.4`, `93`, `2.5`: a `str`, a `float`, an `int` and a `float`, under the names of the columns.

</div>

<!--
**Ask:** which of the four stays text, and why? The time: nothing is computed with it today.
**Say:** cut, then convert: two steps for every line of the file. The names are the header's, with their units.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Lists and **Loops**

Step 4: what is the mean of all 87 672 rows?

<!--
**Say:** one line is done. A loop does the same for 87 672 lines.
(~1 min)
-->

---
hideInToc: true
---

# A List Holds Values in **Order**

```py {monaco-run} {autorun:false}
temps = [-4.4, -4.8, -5.5, -6.0]   # 1 January 2016, 00:00 to 03:00
print(len(temps))                  # 4
print(temps[0], temps[-1])         # -4.4 -6.0
temps.append(-5.9)                 # 04:00
print(temps)                       # [-4.4, -4.8, -5.5, -6.0, -5.9]
print(min(temps), sum(temps))      # -6.0 -26.6
```

<div class="note-text mt-md">A list is indexed and sliced like a <code>str</code>, and it can be changed: <code>append</code> adds an item at the end.</div>

<!--
**Ask:** what does `temps[-1]` give before the `append`?
**Say:** `len`, `min`, `max` and `sum` work on any list of numbers.
(~2 min)
-->

---
hideInToc: true
---

# `for`: Once for Each **Item**

<div class="grid-2 mt-md gap-md">

<div>

```py {monaco-run} {autorun:false}
temps = [-4.4, -4.8, -5.5, -6.0]
total = 0.0
for t in temps:
    total = total + t
    print(t, total)
print(total / len(temps))   # -5.175
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **The rules**

- The `for` line ends with `:`
- The **block** is the lines below it, indented by 4 spaces
- `t` names each item in turn, and the block runs once for it
- After the last item Python goes on with the first line that is not indented

</div>

</div>

<!--
**Ask:** how many lines does it print? Four from inside the loop, one after it.
**Say:** a start value before the loop, an update inside it, the result after it. Every count and sum over a file has these three places.
(~3 min)
-->

---
hideInToc: true
---

# Every Line of `weather.csv` in a **List**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ python
>>> lines = open("data/raw/weather.csv").read().splitlines()
>>> len(lines)
87673
>>> lines[0]
'time,temp_c,humidity_pct,wind_ms'
>>> lines[1]
'2016-01-01T00:00,-4.4,93,2.5'
```

</div>

<div class="note-text mt-md"><code>open</code> opens the file, <code>read</code> hands back its text as one <code>str</code> of 2 515 215 characters, <code>splitlines</code> cuts it at the line ends. 87 673 lines: the count of <code>wc -l</code>, the header first.</div>

<!--
**Say:** three calls joined by dots, each on the result of the one before. The path is relative: it starts at the folder the terminal is in, the project folder.
**If asked:** the slides' Python blocks run in the browser and cannot read a file on the laptop; reading a file is shown at the prompt.
(~2 min)
-->

---
hideInToc: true
---

# A Loop over **Lines**

```py {monaco-run} {autorun:false}
text = """time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
2016-01-01T02:00,-5.5,95,2.7"""
lines = text.splitlines()
total = 0.0
for line in lines[1:]:
    total = total + float(line.split(",")[1])
print(len(lines) - 1, total)    # 3 -14.7
```

<div class="note-text mt-md">The first four lines of <code>weather.csv</code>, pasted between three quotes. <code>lines[1:]</code> is every line but the first, the header.</div>

<!--
**Ask:** why `lines[1:]` and not `lines`? What would `float` do with the header's second part, `temp_c`?
**Say:** inside the loop: cut, pick part 1, convert, add. The same three lines run on 3 lines and on 87 672.
(~3 min)
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

<div class="card card-success card-glass pad-compact mt-sm">

✅ Step 4: 5.782796103659093, the 5.7828 of <code>awk</code> and <code>column_stats.py</code> on the raw file. The 120 rows of −999 are counted as temperatures.

</div>

</v-click>

<!--
**Do:** click through the program as it grows: the lines of the file (it prints 87673), the sum in a loop (506989.30000000005), the count and the mean.
**Ask:** before the output: 7.16 or 5.78?
**Say:** the script does what it says: every row is a temperature to it. Python gives no warning; the number known beforehand, 5.7828, shows it computed what `awk` computed.
(~4 min)
-->

---
layout: section
hideInToc: true
---

# Decide with **`if`**

Step 5: what is the mean without the −999 rows?

<!--
(~1 min)
-->

---
hideInToc: true
---

# `if`: Run a Block or Skip **It**

```py {monaco-run} {autorun:false}
for temp in [23.6, -999.0, -4.4]:
    if temp == -999:
        print(temp, "missing")
    elif temp < 0:
        print(temp, "below freezing")
    else:
        print(temp, "measured")
```

<div class="note-text mt-md">The conditions are tried from the top. The first true one runs its block, and the others are skipped. <code>elif</code> and <code>else</code> can be left out.</div>

<!--
**Ask:** what is printed for −999.0? It is below freezing too, but the first true condition wins.
**Say:** 23.6 is 23:00 on 21 July 2019, the hour before the gap.
(~2 min)
-->

---
hideInToc: true
---

# The Indentation Is the **Block**

<div class="grid-2 mt-md gap-md">

<div>

```py {monaco-run} {autorun:false}
count = 0
for temp in [23.6, -999.0, -4.4]:
    if temp != -999:
        count = count + 1
        print(count)
```

</div>

<div>

```py {monaco-run} {autorun:false}
count = 0
for temp in [23.6, -999.0, -4.4]:
    if temp != -999:
        count = count + 1
print(count)
```

</div>

</div>

<div class="note-text mt-md">The same five lines; only the spaces before <code>print</code> differ. In Python the spaces at the start of a line decide which block the line belongs to.</div>

<!--
**Ask:** what does each print? Left: 1 and 2, the `print` is inside the `if`. Right: 2, once, after the loop.
**Say:** `!=` means "not equal". VS Code indents by 4 spaces after a `:`.
**If asked:** a line after `if …:` with no indented block stops Python before anything runs: `IndentationError`.
(~3 min)
-->

---
hideInToc: true
---

# Skip the −999 Rows: `continue`

```py {monaco-run} {autorun:false}
temps = [23.6, -999.0, -999.0, 21.9]   # 21 July 2019 23:00, two marks, 27 July 00:00
total = 0.0
count = 0
for temp in temps:
    if temp == -999:
        continue                       # on to the next item at once
    total = total + temp
    count = count + 1
print(count, total / count)            # 2 22.75
print(sum(temps) / len(temps))         # -488.125
```

<div class="note-text mt-md"><code>continue</code> ends this turn of the loop: the two lines below it are skipped for a −999 row.</div>

<!--
**Ask:** the last line averages all four. What comes out? −488.125 °C: two marks among four rows.
**Say:** the two hours around the gap give 22.75, a July night. The marks must be left out before any arithmetic.
(~3 min)
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

<div class="card card-secondary card-glass pad-compact mt-sm">

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

<v-click>

<div class="card card-success card-glass pad-compact mt-sm">

✅ Step 5: 7.15996550621346, from 87 552 rows; 87 672 − 87 552 = 120 left out. <code>column_stats.py</code> on <code>weather_valid.csv</code>: 7.15997.

</div>

</v-click>

<!--
**Do:** start from the loop of Step 4, then click: the temperature gets a name, and three lines leave out the mark.
**Ask:** how many rows will be counted now?
**Say:** our own program gives Smiltė's number, and agrees with a program written by someone else.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Readable **Output**

Step 6: how does 7.15996550621346 become 7.16 on the screen?

<!--
(~1 min)
-->

---
hideInToc: true
---

# **f-strings**

```py {monaco-run} {autorun:false}
mean = 7.15996550621346
count = 87552
print("mean", mean)                       # mean 7.15996550621346
print(f"mean {mean:.2f} °C")              # mean 7.16 °C
print(f"{count} rows, {count:,} rows")    # 87552 rows, 87,552 rows
print(f"{120 / 87672:.2%} of the rows")   # 0.14% of the rows
print(mean)                               # 7.15996550621346
```

<div class="note-text mt-md">An <code>f</code> before the quote makes a template: <code>{mean}</code> is replaced by the value, <code>{mean:.2f}</code> by the value with two decimals. After the colon stands the <strong>format</strong>.</div>

<!--
**Ask:** after the f-string, what does `mean` hold? Still all 15 digits: the f-string makes a new string and changes nothing.
**Say:** compute with every digit, round only what is printed.
(~3 min)
-->

---
hideInToc: true
---

# A Width for **Columns**

```py {monaco-run} {autorun:false}
print(f"[{7.16:8.2f}]")      # [    7.16]
print(f"[{-16.3:8.2f}]")     # [  -16.30]
print(f"[{87552:>8}]")       # [   87552]
print(f"[{'temp_c':<8}]")    # [temp_c  ]
print(f"[{7:03d}]")          # [007]
```

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 6: `f"{mean:.2f}"` prints 7.16; `mean` keeps 7.15996550621346. `8.2f`: 8 characters wide, 2 decimals; `>` and `<` push to the right or left.

</div>

<!--
**Ask:** how many spaces before 7.16 in a width of 8? Four: `7.16` is four characters.
**Say:** a fixed width per column lines numbers up under each other, as in a table. The brackets only show where the spaces are.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Functions and **Dictionaries**

Step 7: which year was the warmest?

<!--
(~1 min)
-->

---
hideInToc: true
---

# Calling a **Function**

```py {monaco-run} {autorun:false}
print(len("2016-01-01T00:00"))      # 16
print(round(7.15996550621346, 2))   # 7.16
print(max([-4.4, 32.4, -16.3]))     # 32.4
print(abs(-999))                    # 999
import math
print(math.isclose(7.15996550621346, 7.16, abs_tol=0.005))   # True
```

<div class="note-text mt-md">A call is a name, brackets, and the <strong>arguments</strong> between them; the function hands back a value. <code>import math</code> brings in a module of functions, used as <code>math.…</code></div>

<!--
**Say:** `print`, `float`, `len` were calls from the first slide on. A call is worked out from the inside: first the arguments, then the function.
**If asked:** `abs_tol=0.005` is an argument given by name: "close if they differ by less than 0.005".
(~2 min)
-->

---
hideInToc: true
---

# Write a Function: `def`

```py {monaco-run} {autorun:false}
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(to_fahrenheit(7.16))    # 44.888
print(to_fahrenheit(-16.3))   # 2.6599999999999966
print(to_fahrenheit(32.4))    # 90.32
```

<div class="note-text mt-md"><code>def</code> gives the block below it a name and names its input, the <strong>parameter</strong>. <code>return</code> hands the result back. The block runs only when the function is called, once per call.</div>

<!--
**Ask:** the coldest hour of ten years, −16.3 °C: what does the function return? 2.66 °F, with the float64 tail.
**Say:** −16.3 and 32.4 are the min and max of `column_stats.py`. The formula is written once and used three times.
(~3 min)
-->

---
hideInToc: true
---

# A Function for One **Line**

```py {monaco-run} {autorun:false}
def temp_of(line):
    """The temp_c of one line of weather.csv."""
    fields = line.split(",")
    return float(fields[1])

print(temp_of("2016-01-01T00:00,-4.4,93,2.5"))   # -4.4
print(temp_of("2019-07-22T00:00,-999,76,3.2"))   # -999.0
print(fields)                                    # NameError
```

<div class="note-text mt-md">A name made inside a function lives only while the function runs. The text in three quotes under <code>def</code> says what the function does.</div>

<!--
**Ask:** the last line: what does it print? `fields` was made inside `temp_of` and is gone after each call.
**Say:** a function packs a step with a name: the loop can say `temp = temp_of(line)`.
(~2 min)
-->

---
hideInToc: true
---

# A Dictionary: Values Found by a **Key**

```py {monaco-run} {autorun:false}
hours = {"2016": 8784, "2017": 8760}
print(hours["2016"])          # 8784
hours["2018"] = 8760          # a new key and its value
print(len(hours))             # 3
print("2019" in hours)        # False
print(hours.get("2019", 0))   # 0
print(hours["2019"])          # KeyError
```

<div class="note-text mt-md">A <code>dict</code> holds <code>key: value</code> pairs in curly brackets. A list finds a value by its position, a dictionary by its key.</div>

<!--
**Ask:** `hours.get("2019", 0)` against `hours["2019"]`: what does each do?
**Say:** `get` hands back a default for a key that is not there; square brackets stop with `KeyError`. 8784 = 366 × 24: 2016 is a leap year.
(~2 min)
-->

---
hideInToc: true
---

# Count Rows per **Year**

```py {monaco-run} {autorun:false}
lines = ["2016-12-31T22:00,-0.9,78,4.7",
         "2016-12-31T23:00,-1.3,81,4.3",
         "2017-01-01T00:00,-1.9,83,4.8"]
hours = {}
for line in lines:
    year = line[:4]
    hours[year] = hours.get(year, 0) + 1
print(hours)    # {'2016': 2, '2017': 1}
```

<div class="note-text mt-md">The count so far, or 0 for a year not seen yet, plus one. The first time a year appears, the key is made.</div>

<!--
**Ask:** what does the dictionary hold after the loop?
**Say:** the three lines around New Year 2017. A dictionary of counts is the `uniq -c` of Lecture 04, inside a program.
(~3 min)
-->

---
hideInToc: true
---

# The Mean of Each **Year**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **`scripts/year_means.py`**

```python
lines = open("data/raw/weather.csv").read().splitlines()
sums = {}
counts = {}
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp == -999:
        continue
    year = parts[0][:4]
    sums[year] = sums.get(year, 0.0) + temp
    counts[year] = counts.get(year, 0) + 1
for year in sums:
    mean = sums[year] / counts[year]
    print(f"{year} {counts[year]} {mean:.2f}")
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ python scripts/year_means.py
```

<v-click>

```text
2016 8784 7.60
2017 8760 6.51
2018 8760 7.97
2019 8640 7.27
2020 8784 6.83
2021 8760 7.25
2022 8760 6.60
2023 8760 8.31
2024 8784 7.27
2025 8760 5.98
```

</v-click>

</div>

</div>

<!--
**Ask:** which year is short, and by how much? 2019: 8640 = 8760 − 120, the five days of marks.
**Say:** two dictionaries with the same keys: one for the sums, one for the counts. A `for` over a dictionary goes through its keys in the order they were added.
(~3 min)
-->

---
hideInToc: true
---

# The Warmest and the Coldest **Year**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | Year | Measured hours | Mean, °C |
| --- | --- | --- | --- |
| warmest | 2023 | 8760 | 8.31 |
| coldest | 2025 | 8760 | 5.98 |
| all ten years | | 87 552 | 7.16 |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 7: 2023, at 8.31 °C. The ten yearly means lie between 5.98 and 8.31 °C, 2.33 °C apart.

</div>

<!--
**Ask:** is 7.16 the mean of the ten yearly means? Nearly: 7.16005. The leap years have 24 hours more and 2019 has 120 fewer, so the years do not weigh the same.
**Say:** one more `for`, one more dictionary, and the question of a whole decade has an answer per year.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Read a **Traceback**

Step 8: where and why does a script stop?

<!--
**Say:** every program fails many times before it works. Python says where and why, in its last lines.
(~1 min)
-->

---
hideInToc: true
---

# Three Kinds of **Error**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Kind | When | What appears | Example |
| --- | --- | --- | --- |
| **Syntax error**: not valid Python | before line 1 runs | `SyntaxError` and the line, no output | `print(hours` |
| **Exception**: a line cannot be carried out | while it runs | the output so far, then a traceback | `float("temp_c")` |
| **Wrong result** | never | a number that looks fine | 5.78 instead of 7.16 |

</div>

<div class="note-text mt-md">Python finds the first two and names the line. The third is found only by a number known beforehand: 7.15997 from <code>column_stats.py</code>, 87 672 rows from the calendar.</div>

<!--
**Say:** step 2 and step 5 of what `python` does with a file: the grammar check, and the stop at an error.
**Ask:** which kind was `mean_all.py`? The third: no message, and the marks counted as temperatures.
(~2 min)
-->

---
hideInToc: true
---

# Anatomy of a **Traceback**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 📄 **`scripts/mean_temp.py`, `[1:]` left out**

```python {*}{lines:true,startLine:4}
for line in lines:
    parts = line.split(",")
    temp = float(parts[1])
```

</div>

<div class="card card-warning card-glass pad-compact">

## 💥 **The terminal shows**

```text
$ python scripts/mean_temp.py
```

<v-click>

```text
Traceback (most recent call last):
  File "/Users/smilte/weather-project/
    scripts/mean_temp.py", line 6, in <module>
    temp = float(parts[1])
ValueError: could not convert string to
float: 'temp_c'
```

</v-click>

</div>

</div>

<div v-click class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

**1. The last line: what.** The kind of error and the text that failed: `'temp_c'`.

</div>

<div class="card card-accent card-glass pad-compact">

**2. Above it: where.** The file by its full path, line 6, and the line.

</div>

<div class="card card-success card-glass pad-compact">

**3. Then upwards: why.** Line 4 starts the loop at the header. `lines[1:]` skips it.

</div>

</div>

<!--
**Say:** read from the bottom. The line that fails is often not the line that is wrong: line 6 is right, line 4 forgot `[1:]`.
**If asked:** the long lines are wrapped here for the slide; the terminal shows each on one line. On Windows the path is `C:\Users\smilte\weather-project\scripts\mean_temp.py`.
(~3 min)
-->

---
hideInToc: true
---

# The Wrong **Folder**: `FileNotFoundError`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ cd scripts
$ python mean_temp.py
```

<v-click>

```text
Traceback (most recent call last):
  File "/Users/smilte/weather-project/scripts/mean_temp.py", line 1, in <module>
    lines = open("data/raw/weather.csv").read().splitlines()
FileNotFoundError: [Errno 2] No such file or directory: 'data/raw/weather.csv'
$ cd ..
$ python scripts/mean_temp.py
87552 7.15996550621346
```

</v-click>

</div>

<div class="note-text mt-md">A relative path starts at the folder the terminal is in, not at the script (Lecture 04).</div>

<!--
**Ask:** the file is there. Why does Python not find it?
**Say:** from `scripts`, `data/raw/weather.csv` would be `scripts/data/raw/weather.csv`. Run every script from the project folder, as the README says.
**If asked:** Python 3.14 also prints a row of `~` and `^` under the line, pointing at the call that failed; it is left out here.
(~2 min)
-->

---
hideInToc: true
---

# A Name Never Made: `NameError`

```py {monaco-run} {autorun:false}
total = 626869.3
count = 87552
print(totl / count)    # NameError
```

<div class="note-text mt-md">The last line names the nearest name Python knows: <code>Did you mean: 'total'?</code> In VS Code the extension underlines <code>totl</code> before the script runs.</div>

<!--
**Ask:** run it and read the last line aloud. What is the repair?
**Say:** a typo, or a name used above the line that makes it: Python reads from the top.
(~2 min)
-->

---
hideInToc: true
---

# Common Error **Messages**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The last line of the traceback | The usual cause |
| --- | --- |
| `NameError: name 'totl' is not defined. Did you mean: 'total'?` | a typo, or a name used too early |
| `TypeError: can only concatenate str (not "int") to str` | a text never converted to a number |
| `ValueError: could not convert string to float: 'temp_c'` | the right type, a value that cannot be used |
| `IndexError: list index out of range` | `parts[4]` in a list of four |
| `KeyError: '2019'` | a key that is not in the dictionary |
| `SyntaxError: '(' was never closed` | a bracket or a quote without its partner |
| `FileNotFoundError: [Errno 2] No such file or directory` | a path from the wrong folder |

</div>

<div class="note-text mt-md">The text in quotes is exactly what Python was given, so a space or a comma in it shows. Copy the last line as it stands when asking someone.</div>

<!--
**Ask:** cover the right column. Which cause goes with each line?
**Say:** six of the seven were on earlier slides; `IndexError` comes from a position past the end, `parts[4]` in a list of four.
(~2 min)
-->

---
hideInToc: true
---

# A Wrong Number Without a **Message**

```py {monaco-run} {autorun:false}
lines = ["time,temp_c,humidity_pct,wind_ms",
         "2016-01-01T00:00,-4.4,93,2.5",
         "2016-01-01T01:00,-4.8,95,2.6",
         "2016-01-01T02:00,-5.5,95,2.7"]
total = 0.0
for line in lines[1:]:
    total = total + float(line.split(",")[1])
print(total / len(lines))    # -3.675
```

<div class="note-text mt-md">−4.4, −4.8 and −5.5 cannot have a mean above −4.4. <code>print(f"{total=} {len(lines)=}")</code> above the last line prints <code>total=-14.7 len(lines)=4</code>: the header was counted.</div>

<!--
**Ask:** no traceback. Is the number right? Which of the two, the sum or the count, is wrong?
**Say:** `{name=}` in an f-string prints the name and its value. The repair is `len(lines) - 1`: −4.9.
(~3 min)
-->

---
hideInToc: true
---

# Stop at a Line: the **Debugger**

<img src="/figures/python_debugger_weather.svg" alt="The debugger of VS Code stopped before line 9 of mean_temp.py, with the values of its names" style="display:block;margin:0 auto;max-height:250px;">

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | |
| --- | --- |
| click left of line 9 | a red dot: a **breakpoint** |
| `F5`, **Python Debugger: Python File** | the script runs and stops **before** line 9 |
| `F10` / `F5` / `Shift+F5` | one line on / to the next stop / end |

</div>

<div class="card card-success card-glass pad-compact mt-sm">

✅ Step 8: the last line of the traceback says what stopped Python; the lines above it say where. The cause is often a line higher up.

</div>

<!--
**Say:** third stop at line 9: `temp` is −5.5, `total` holds the first two hours, −9.2. The Variables panel lists every name with its value at that moment.
**If asked:** on a Mac the function keys may need `fn`.
(~3 min)
-->

---
hideInToc: true
---

# `mean_temp.py`, **Complete**

````md magic-move {lines: true}
```py {6-8}
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
```py {1-3,10}
def temp_of(line):
    """The temp_c of one line of weather.csv."""
    return float(line.split(",")[1])

lines = open("data/raw/weather.csv").read().splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    temp = temp_of(line)
    if temp == -999:
        continue
    total = total + temp
    count = count + 1
print(count, total / count)
```
```py {1,12,17-18}
MISSING = -999      # the mark for an hour without a reading

def temp_of(line):
    """The temp_c of one line of weather.csv."""
    return float(line.split(",")[1])

lines = open("data/raw/weather.csv").read().splitlines()
total = 0.0
count = 0
for line in lines[1:]:
    temp = temp_of(line)
    if temp == MISSING:
        continue
    total = total + temp
    count = count + 1

print(f"{count} hours, {len(lines) - 1 - count} left out")
print(f"mean temp_c: {total / count:.2f} °C")
```
````

<!--
**Do:** click through: the line's step becomes a function, then the mark gets a name and the output an f-string.
**Ask:** what will the last two lines print?
(~2 min)
-->

---
hideInToc: true
---

# Run `mean_temp.py`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ python scripts/mean_temp.py
```

<v-click>

```text
87552 hours, 120 left out
mean temp_c: 7.16 °C
```

</v-click>

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

✅ 7.16 °C: the number in Smiltė's e-mail, from 18 lines read on these slides. `awk` and `column_stats.py` give the same 7.15997.

</div>

<!--
**Live:** `python scripts/mean_temp.py` in the project folder.
**Ask:** which one change gives the mean wind speed? `[1]` becomes `[3]` in `temp_of`: 3.50 m/s.
**Say:** a number with a meaning gets a name, once, at the top: `MISSING`. Every line of the program was on an earlier slide.
(~3 min)
-->
---
hideInToc: true
---

# The Eight Steps, **Answered**

<div class="card card-success card-glass pad-compact table-compact mt-sm">

| Step | Question | Answer |
| --- | --- | --- |
| 1 | What runs a `.py` file, and in which order? | `python`: the whole file checked, then run from the top |
| 2 | Is `-4.4` in `weather.csv` a number? | No, text; `float("-4.4")` makes it one |
| 3 | The four values of one line? | `'2016-01-01T00:00'`, `-4.4`, `93`, `2.5` |
| 4 | The mean of all 87 672 rows? | 5.782796103659093 |
| 5 | Without the −999 rows? | 7.15996550621346, from 87 552 rows |
| 6 | 7.16 on the screen? | `f"{mean:.2f}"` |
| 7 | The warmest year? | 2023, 8.31 °C |
| 8 | Where and why does a script stop? | the traceback: the last line says what, the lines above it where |

</div>

<!--
**Say:** 7.16 now comes from 18 lines anyone here can read, and agrees with `column_stats.py` and with `awk`.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Run Python at `>>>`, as a script from the terminal, and from VS Code, and say what the interpreter does with a file

</div>

<div class="card card-success card-glass pad-compact">

✅ Name the type of a value, `int`, `float`, `str` or `bool`, and convert text to a number

</div>

<div class="card card-success card-glass pad-compact">

✅ Cut a line into parts with `split`, and repeat a step for every line with `for`

</div>

<div class="card card-success card-glass pad-compact">

✅ Leave out rows with `if` and `continue`, and count by key in a `dict`

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a function, and print numbers with an f-string

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a traceback from the bottom, and catch a wrong number by a value known beforehand

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
    'The int 88',
    'The text 88',
    'The text 3.1',
    'The float 88.0'
  ]"
  :correct="1"
  explanation="Positions count from 0, so [2] is the third part, the humidity. split hands back strings: '88' is text until int('88') converts it."
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
  explanation="lines[2:] starts at position 2, the third item: 250 − 2 = 248 items. lines[1:] skips only the header and has 249. A loop that drops the first row silently gives a result that looks right and is not."
/>

---
hideInToc: true
---

<MCQ
  question="`a = 5`, then `b = a`, then `a = a + 1`. What does `print(b)` show?"
  :options="[
    '6, because b follows a',
    '5, because b still points to the value 5',
    'An error, because a changed',
    '11'
  ]"
  :correct="1"
  explanation="b = a puts the name b on the value 5. a = a + 1 makes a new value, 6, and moves the name a to it. b still points to 5. A Python name does not follow another name, as a spreadsheet cell follows a formula."
/>

---
hideInToc: true
---

<MCQ
  question="In mean_temp.py, `count = count + 1` is moved above the `if temp == -999:` line. The sum is unchanged. What does the script print as the mean?"
  :options="[
    '7.15996550621346, unchanged',
    '5.782796103659093',
    '7.150165389177845',
    'A ValueError'
  ]"
  :correct="2"
  explanation="The sum still leaves out the 120 marks, 626 869.3, but the count now has every row, 87 672. 626 869.3 / 87 672 = 7.150165389177845. No message: a wrong result is found only by a number known beforehand."
/>

---
hideInToc: true
---

<MCQ
  question="A script prints `rows read: 6`, then a traceback that names line 12 and ends with `ValueError: could not convert string to float: ''`. What do you know?"
  :options="[
    'Nothing ran: Python checks the whole file first',
    'The lines above line 12 ran; on line 12 float() was given an empty text, an empty field in the file',
    'The number is too large for a float',
    'The script file is damaged at line 12'
  ]"
  :correct="1"
  explanation="An exception stops the script at one line; everything before it ran, which is why there is output. The text in quotes is what float received: '' is an empty string, a value missing between two commas."
/>

---
hideInToc: true
---

<MCQ
  question="`t = 2.6599999999999966`. What does `print(f'{t:.1f} °F')` write, and what does `t` hold afterwards?"
  :options="[
    '2.6 °F, and t is now 2.6',
    '2.7 °F, and t is now 2.7',
    '2.7 °F, and t is unchanged',
    '2.6599999999999966 °F, and t is unchanged'
  ]"
  :correct="2"
  explanation="The format .1f writes the value rounded to one decimal: 2.7. The f-string builds a new string; the name t still holds the full float64."
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
  explanation="get hands back the default, 0, for a key that is not there. Square brackets look the key up and stop with KeyError: '2026'. Neither adds a key; hours['2026'] = 0 would."
/>
