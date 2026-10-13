# 5: Python Foundations

Lecture 4 checked Smiltė's ten-year mean, **7.16 °C**, with typed lines, and
in the end with `scripts/column_stats.py`, a Python program someone else
wrote, run without being read. Lecture 5 writes that program: the lines that
turn `weather.csv` into 7.16 are built one piece at a time, each piece short
and shown with its output, and in the end 18 lines of our own give the same
number. Along the way the lecture says what the interpreter does with a file,
and ties Python's values to Lecture 3: an `int` does not overflow, a `float`
is the float64 of Lecture 3, a `str` is Unicode text. The room knows the
shell (zsh on macOS, Git Bash on Windows), relative paths and the weather
project from Lecture 4; Git comes in Lecture 6.

| Step | Question | Answer |
|--|--|--|
| 1 | What runs a `.py` file, and in which order? | `python`, the interpreter: it checks the whole file, then runs it from the top, one statement at a time, and stops at the first error |
| 2 | Is `-4.4` in `weather.csv` a number? | No: text, four characters; `float("-4.4")` makes the number |
| 3 | What are the four values of one line? | `'2016-01-01T00:00'`, `-4.4`, `93`, `2.5`: a `str`, a `float`, an `int` and a `float` |
| 4 | What is the mean of all 87 672 rows? | 5.782796103659093, the 120 rows of −999 counted as temperatures |
| 5 | What is it without the −999 rows? | 7.15996550621346, from 87 552 rows |
| 6 | How does 7.15996550621346 become 7.16 on the screen? | `f"{mean:.2f}"`; the name keeps every digit |
| 7 | Which year was the warmest? | 2023, 8.31 °C; the coldest 2025, 5.98 °C |
| 8 | Where and why does a script stop? | The traceback: its last line says what, the lines above it where |

## What the lecture covers

1. **The question** (slides 1–4): `column_stats.py` gives 5.7828 on the raw
   file and 7.15997 without the −999 rows; it is 53 lines of Python. The
   eight steps of a program for 7.16.
2. **Running Python** (slides 5–11): `python` is a program on `PATH`,
   Python 3.14.7 from Miniforge; the interpreter; the `>>>` prompt against
   the shell's `$` (`7.16 * 9 / 5 + 32` is 44.888 at one and `command not
   found` at the other); a script, `scripts/hours.py`, which prints 87 672;
   the Python extension of VS Code and the ▶ button, which types the full
   paths of the interpreter and the file; what `python` does with a file in
   six steps (read as UTF-8, check the grammar of the whole file, bytecode,
   run from the top, stop at an error with exit status 1, end with 0); a run
   that prints two lines and stops at `ZeroDivisionError`.
3. **Values and types** (slides 12–19): `int`, `float`, `str`, `bool`;
   `87672 / 24` is `3653.0`, `//` gives `3653`; an `int` grows past 64 bits
   (2¹⁰⁰ has 101 bits, 127 + 1 is 128); a `float` is float64
   (`0.1 + 0.2`, 7.16 stored as 7.16000000000000014211, `-4.4 + 1` is
   −3.4000000000000004); a `str` counts characters (`"°C"` is 2 characters
   and 3 bytes); a name points to a value and does not follow another name
   as a spreadsheet cell does; comparisons, and `"-999" == -999` is
   `False`; `float()` and `int()` turn text into numbers, `"-4.4" + 1` is a
   `TypeError`.
4. **One line** (slides 20–23): index and slice on
   `2016-01-01T00:00,-4.4,93,2.5` (28 characters, 29 bytes with LF);
   `split(",")` gives a list of four strings; each part converted under the
   name of its column.
5. **Lists and loops** (slides 24–29): a list, `append`, `len`, `min`,
   `sum`; `for` and its indented block (four temperatures, mean −5.175);
   every line of `weather.csv` in a list at the prompt (87 673 lines, the
   header first); a loop over pasted lines with `lines[1:]`; the program
   grows on one slide (Shiki magic move) from reading the file to the mean
   of all rows, 5.782796103659093, the 5.7828 of `awk` and
   `column_stats.py`.
6. **Decide with `if`** (slides 30–34): `if`, `elif`, `else`; the same five
   lines with `print` indented or not (1 and 2, against 2); `continue` on
   four hours around the gap (22.75 against −488.125); the program gains
   three lines and gives 7.15996550621346 from 87 552 rows.
7. **Readable output** (slides 35–37): f-strings (`{mean:.2f}`, `{count:,}`,
   `{x:.2%}`), the value unchanged after printing; widths and alignment.
8. **Functions and dictionaries** (slides 38–45): calling built-in
   functions and `math`; `def` and `return` with `to_fahrenheit` (−16.3 °C
   is 2.6599999999999966 °F); `temp_of(line)`, and a name made inside a
   function is gone after the call; a dictionary, `get` against `[]` and
   `KeyError`; counting rows per year; the mean of each year from two
   dictionaries (2019 has 8640 measured hours, 8760 − 120); 2023 the
   warmest, 8.31 °C, 2025 the coldest, 5.98 °C.
9. **Read a traceback** (slides 46–53): syntax error, exception and wrong
   result; a traceback read from the bottom (`ValueError: could not convert
   string to float: 'temp_c'` on line 6, caused by line 4 without `[1:]`);
   `FileNotFoundError` when the script is run from `scripts/`; `NameError`
   with `Did you mean`; seven common messages; a mean of −3.675 for three
   hours of −4.4 to −5.5, the header counted, found with `{name=}`; the
   debugger of VS Code stopped at line 9.
10. **The program, complete** (slides 54–57): `mean_temp.py` grows on one
    slide into its last form (a function `temp_of`, a name `MISSING`, two
    f-strings) and prints `87552 hours, 120 left out` and
    `mean temp_c: 7.16 °C`; the eight steps answered; the recap.

## The lecture in two hours

The lecture is slides 1–57. Its speaker notes add up to about 123 minutes,
the two live moments included; a two-hour slot has about 110 minutes of
teaching. Slide 58 opens the self-check section, and slides 59–67 are its
nine quizzes: they take no lecture time. To jump, type the slide number and
press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | `column_stats.py`, and the eight steps |
| 0:07 | 5–11 | Step 1: the interpreter, `>>>` (live), a script, VS Code |
| 0:22 | 12–19 | Step 2: values and types, names, text to number |
| 0:38 | 20–23 | Step 3: one line cut and converted |
| 0:46 | 24–29 | Step 4: lists, `for`, the mean of all rows |
| 1:02 | 30–34 | Step 5: `if`, `continue`, the mean without −999 |
| 1:14 | 35–37 | Step 6: f-strings |
| 1:20 | 38–45 | Step 7: functions, dictionaries, the warmest year |
| 1:38 | 46–53 | Step 8: tracebacks, a wrong number, the debugger |
| 1:56 | 54–57 | The program complete (live), the steps answered, recap |
| 2:04 | | End |

In a two-hour slot, skip the slides below: about 15 minutes. None is needed
by a later slide.

| Skip if time is short | Slides | Saves |
|--|--|--|
| `int` Has No Fixed Width; `bool`: Comparisons | 14, 18 | 4 min |
| A Width for Columns (say Step 6's answer at slide 36) | 37 | 2 min |
| Calling a Function | 39 | 2 min |
| Count Rows per Year | 43 | 3 min |
| A Name Never Made; Common Error Messages | 50, 51 | 4 min |

- **Never skip** slide 4 (the eight steps), 10 (what `python` does with a
  file), 17 (a name points to a value), 19 (text to number), 22–23 (split
  and convert), 26 (`for`), 29 and 34 (the program grows: 5.78, then
  7.16), 32 (the indentation), 44 (the mean of each year), 48 (a traceback
  read), 52 (a wrong number without a message), 54–56 (the program
  complete, run, the steps answered).
- **Predict, then reveal.** Most slides hold a few lines; the note's
  **Ask** has the room predict the output before ▶ is pressed or the
  output is clicked in. The Python blocks run in the browser (Pyodide) and
  need the internet in the room; press one ▶ before the lecture so it has
  loaded. A block that reads a file cannot run in the browser: those slides
  show the terminal, with the output behind a click.
- **The program grows on three slides** (29, 34, 54) by Shiki magic move:
  each click changes the code in place and lights the lines that changed;
  the output comes in on the click after.
- **Each section slide names its step**, and each section ends on a card
  with a ✅ and the step's answer. Point back to slide 4 there.
- **No whole scripts are typed in the lecture.** Typing them is the
  seminar's work.
- **Every speaker note has the same form**: **Live** (a line run in the
  terminal, only on the two slides below), **Do** (something done with the
  room), **Say** (the one point of the slide), **Ask** (a question for the
  room), **If asked** (the detail kept off the slide), then the minutes.

## Live in the lecture

Two moments run in a terminal what their slide shows. If a line
misbehaves, go to the slide: it has the output.

**Before the lecture.** On the Mac that drives the projector, open the
weather project in VS Code, open its terminal (zsh) and make the font large
(`Cmd +` a few times). Check `python --version` (3.14) in that terminal.
Save the program of slide 54, last step, as `scripts/mean_temp.py` (below).
Run `clear` before each moment.

| Slide | What to type |
|--|--|
| 7 | `python`, then `365 * 10 + 3` and `7.16 * 9 / 5 + 32`, then `exit()` |
| 55 | `python scripts/mean_temp.py` |

```text
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

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 58–67: nine quiz slides for students to try afterwards. The same
questions, with their answers:

1. `x = '7.16'` and `y = '1'`. What is `x + y`?
   *The text `7.161`. Both are strings, and `+` joins two strings, with no
   error. `float(x) + float(y)` gives 8.16; `'7.16' + 1` would be a
   `TypeError`.*
2. What do `100 / 4` and `100 // 4` give?
   *`25.0` and `25`. `/` always gives a float; `//` gives the whole part,
   an `int` when both sides are ints.*
3. `line = '2020-02-29T12:00,3.1,88,4.0'`. What is `line.split(',')[2]`?
   *The text `'88'`, the humidity: positions count from 0, and `split`
   hands back strings.*
4. `lines` holds 250 strings: a header and 249 rows. How many times does
   the block of `for line in lines[2:]:` run?
   *248. `lines[2:]` starts at the third item; `lines[1:]` skips only the
   header and has 249.*
5. `a = 5`, then `b = a`, then `a = a + 1`. What does `print(b)` show?
   *5. `b` points to the value 5; `a = a + 1` moves the name `a` to a new
   value, 6.*
6. In `mean_temp.py`, `count = count + 1` is moved above the
   `if temp == -999:` line. What does the script print as the mean?
   *7.150165389177845: the sum still leaves out the marks, 626 869.3, but
   the count is now 87 672. No message: only a number known beforehand
   shows it.*
7. A script prints `rows read: 6`, then a traceback that names line 12 and
   ends with `ValueError: could not convert string to float: ''`. What do
   you know?
   *The lines above line 12 ran; on line 12 `float()` was given an empty
   text, a value missing between two commas in the file.*
8. `t = 2.6599999999999966`. What does `print(f'{t:.1f} °F')` write, and
   what does `t` hold afterwards?
   *`2.7 °F`, and `t` is unchanged: the f-string builds a new string.*
9. `hours = {'2016': 8784}`. What do `hours.get('2026', 0)` and
   `hours['2026']` do?
   *The first gives 0, the second stops with `KeyError: '2026'`. Neither
   adds a key.*

## Paired seminar

[Seminar 5](../seminars/seminar_05.md), "Can You Compute 7.16 Yourself?",
works on the same weather project: the room installs the Python extension,
works at `>>>`, writes a script that cuts one line of `weather.csv` into
numbers, then the loop and the `if` that give 7.15997 °C, and fixes a
script with two bugs.

## What left the deck

On 13 October 2026 Python Foundations became Lecture 5 (Git moved to
Lecture 6), and the deck was rebuilt on the weather project of Lectures 1
to 4, around one question: can we write the program that computes 7.16
ourselves? Each topic now leads to the next step of that program, and the
program grows on three slides. Out went the pendulum table, the LHCb file
and the reading of `clean_pendulum.py` line by line (and the 97 bytes it
wrote), arithmetic operators in a table, a second name for one list, `while`
and `range`, list comprehensions, tuples and sets, readable names and PEP 8,
the methods `replace`, `startswith` and `strip` on the spreadsheet export,
and the rounding of a long sum (626 869.3000000009 against 626 869.3). The
slides are in `lectures/content/parked/05_Python_Foundations.md`, each with a
note saying where it stood.

## Script or notebook

A notebook (`.ipynb`) keeps cells of code with their output and plots
below each. Cells can be run in any order, and the names of every earlier
run stay, so a result may depend on a cell that was changed or deleted
since. That suits a first look at data. This course writes scripts: plain
text, run from the top, the same order and the same result at every run.
A notebook can be trusted once it gives the same output after **Restart**
and **Run All**, which is the test a script passes every time it runs.

## Where to look things up

All of these are free. At the prompt, `help(round)` prints the description
of a function, and `help(str)` lists every string method.

- [The Python Tutorial](https://docs.python.org/3/tutorial/), chapters 3
  to 5: numbers, strings, lists, `if`, `for`, dictionaries
- [Built-in Functions](https://docs.python.org/3/library/functions.html):
  the full list, one paragraph each
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)

## Take-aways

- `python` is a program, the interpreter. It reads a `.py` file, checks the
  grammar of all of it, then runs it from the top, one statement at a time,
  and stops at the first error.
- Every value has a type. A Python `int` grows as needed; a `float` is a
  float64 and rounds; a `str` is text, and `"-4.4"` is not a number until
  `float()` makes it one.
- A name points to a value. `=` works out the right side, then moves the
  name; nothing follows a formula.
- One line of a CSV file becomes numbers in two steps: `split(",")`, then
  convert each part. A `for` loop does it for every line; `lines[1:]`
  leaves out the header.
- `if` and `continue` leave out the rows of −999. Without them the mean of
  `weather.csv` is 5.78; with them, 7.16, the same as `column_stats.py`.
- A dictionary counts and sums by key: hours and means per year.
- An f-string rounds what is printed, never the value.
- A traceback is read from the bottom: what, then where. The cause is often
  a line higher up. A wrong number has no traceback; a value known
  beforehand finds it.
