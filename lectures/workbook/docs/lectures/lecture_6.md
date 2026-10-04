# 6: Python Foundations

Lecture 5 put the project folder under Git, so that every change to a text
file is recorded. Until now the text files were data and notes, and the only
program in the folder was a handed-out script that was run and not read.
Lecture 6 is the language of that script: how Python is run, what its values
are, and how one line of a data file becomes numbers. It builds on Lecture 3,
where integers, floats and text were made from bits.

## What the lecture covers

1. **Running Python** — the interpreter and its version; the prompt and the
   script; a script runs from top to bottom; the Python extension of VS Code
   and three ways to run a file.
2. **Values, types & names** — `int`, `float`, `str` and `bool`. A Python
   `int` has no fixed width and does not overflow. A `float` is the float64
   of Lecture 3, which is why `9.02 / 10` prints `0.9019999999999999`. A
   `str` is Unicode text, counted in characters and not in bytes. Arithmetic
   and its order; what a name is; calling a function; comparisons; turning
   text into a number, and the three messages when that fails.
3. **Strings & lists** — index and slice on a line of `D0_KPi.csv`; six
   string methods; lists; the recipe *strip, split, convert* that turns one
   line into four floats; two names for one list.
4. **Decisions & loops** — `if`, `for`, `while` and `range`; the pendulum
   table as a list of lines; the period T = t10/10 for every row; a sum in a
   loop; a list comprehension; a missing value skipped inside a loop.
5. **Dictionaries & tuples** — one row with named values; a header line and
   a data line made into a dictionary; counting into bins with a dictionary;
   the four containers side by side.
6. **Readable output** — f-strings; the format after the colon: decimals,
   widths, columns.
7. **Errors & debugging** — syntax error, exception, wrong result; a
   traceback read from the bottom; six messages and their usual causes; a
   wrong mean found with `print` and then with the debugger of VS Code:
   breakpoint, continue, step, inspect.
8. **Code that can be read** — units in names, numbers with names, PEP 8,
   completion, snippets and a formatter; script or notebook.

Functions are called in this lecture (`print`, `len`, `float`) and not
written. No file is opened from Python: the lines of data are pasted into
the script as a string.

## The lecture in 90 minutes

The lecture is slides 1–61 and estimates about 135 min. Slides 62–68 are the
self-check quizzes and take no lecture time. In a 2-hour slot, skip the three
*Try It* slides 26, 36 and 39 and the two *Fix It* slides 49 and 50: the
seminar does the same steps. For a 90-minute slot, skip the slides in the
second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3 | The goal and the objectives |
| 0:03 | 5–8, 10 | Running Python: version, prompt, script, top to bottom, VS Code |
| 0:14 | 11–12, 14–17, 19–20 | Types, the float64, arithmetic, names, calling a function, comparisons, text to number |
| 0:29 | 21–25, 27 | Index and slice, string methods, lists, one line into four numbers, two names for one list |
| 0:42 | 28–34 | `if`, `for`, the table as lines, the period for every row, a sum in a loop, `while` and `range` |
| 0:56 | 37–38, 41 | A row as a dictionary, the four containers |
| 1:01 | 42–44 | f-strings and the format after the colon |
| 1:07 | 45–48, 51–54 | Three kinds of error, the traceback, six messages, `print`, the debugger |
| 1:25 | 55–56, 60 | Names with units, recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Why Python | 4 | 2 min |
| Try It — The First Script, done live on slide 7 instead | 9 | 4 min |
| `int`: No Fixed Width, `str`: Unicode Text | 13, 18 | 7 min |
| Try It — Parse Another Line | 26 | 4 min |
| A List in One Line, Try It — Skip the Missing Value | 35–36 | 6 min |
| Try It — Header and Line into a dict, Counting with a dict | 39–40 | 7 min |
| Fix It — NameError, Fix It — ValueError | 49–50 | 7 min |
| PEP 8, The Editor Does the Typing, Script or Notebook | 57–59 | 7 min |
| Read More | 61 | 2 min |

- **Do not cut** slides 22–25 (index and slice, string methods, lists, one
  line into four numbers), 29–33 (`if`, `for`, the table as lines, the
  period for every row, a sum in a loop) or 46–48 and 51–53 (errors, the
  traceback, `print`, the debugger). The seminar repeats every one of them
  on the keyboard.
- **Slides 13 and 18**, when skipped: say their content in one sentence
  each on slide 12. A Python `int` does not overflow. A `str` is counted in
  characters, and `ą` is one of them.
- **Slides 6–10 are shown live.** Keep VS Code open beside the slides with
  the project folder. Run `python --version`, type the three lines of the
  prompt on slide 7, write `scripts/period.py`, install the Python extension
  and run the file in the three ways of slide 10.
- **Slide 14** needs the slide *Why 0.1 Is Not Exact* of Lecture 3. The room
  has seen `0.9019999999999999` since slide 7. This is the slide that
  explains it.
- **Slide 25** (One Line, Four Numbers) is the centre of the lecture. Type
  it live in `scripts/parse_line.py` and print after every line. Do not rush
  it.
- **Slides 51–53 are shown live** on `scripts/mean_period.py`, the script
  of slide 51 with the full table of ten lines. It prints `1.3625` where
  1.514 is expected. Put a breakpoint on line 16, press `F5` three times and
  read `total` each time, then move the breakpoint to line 17, open `lines`
  under **Variables** and type `total / 9` in the Debug Console. The picture
  on slide 52 is a drawing of the window, not a screenshot. The script is
  in section 9 of the seminar page.
- **The twelve slides with a play button** (9, 13, 18, 26, 33, 36, 39, 40,
  44, 49, 50, 51) run Python inside the browser. The first run takes a few
  seconds while Python loads. The code can be edited on the slide. A
  traceback in the browser begins with a few lines of the runner itself.
  Its last line is the same as in the terminal, which is the line the
  slides ask the room to read.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/06-python-foundations/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 62–68: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. A script has `x = '30'` and `y = '11.05'`. What is `x + y`?
   *The text `3011.05`. Both values are strings, and `+` joins two strings
   without any error. `float(x) + float(y)` gives 41.05.*
2. After `a = [1, 2, 3]`, then `b = a`, then `b.append(4)`: what is `a`?
   *`[1, 2, 3, 4]`. `b = a` puts a second name on the same list and copies
   nothing. `b = a.copy()` makes a second list.*
3. `masses = [1866, 1810, 1871]`, then `result = masses.sort()`. What are
   `result` and `masses` now?
   *`result` is `None` and `masses` is `[1810, 1866, 1871]`. `sort()`
   changes the list in place and hands back nothing. `sorted(masses)` hands
   back a new list.*
4. `lines` is a list of 250 strings: one header line and 249 rows. How many
   times does the block of `for line in lines[2:]:` run?
   *248 times. `lines[2:]` starts at the third item. The slice that skips
   only the header is `lines[1:]`.*
5. A script prints `rows read: 6`, then a traceback that names line 12 and
   ends with `ValueError: could not convert string to float: '12,61'`. What
   do you know?
   *The lines above line 12 ran, which is why there is output. On line 12
   `float()` was given a text with a decimal comma.*
6. `period_s` holds 1.7899999999999998. What does
   `print(f'{period_s:.2f} s')` write, and what does `period_s` hold
   afterwards?
   *It writes `1.79 s`. The name still holds the full value: the f-string
   makes a new string and changes nothing.*

## Paired seminar

[Seminar 6 — A Line of Text into Numbers](../seminars/seminar_06.md) has
four parts. The room checks Python, installs the Python extension and runs
a first script in three ways. One line of `D0_KPi.csv` is pasted into a
script and turned into four numbers, and three errors are made on purpose
and read. The first lines of the file are parsed in a loop, printed as a
table and averaged, with the row that has `TAU = -100` skipped. Last, a
script that prints a wrong mean without any message is examined with
`print` and with the debugger. At home students do the same for the first
rows of their own dataset.

## Slides that left the deck

The rework of 4 October 2026 removed these slides: the installation slide
(installing was homework; slide 6 keeps the version check), the two
previews of a function and of `try` and `except` (both belong to
Lecture 7), *Why Formatting Matters*, *The Error Message Is Data*,
*Fix It — TypeError* and *Fix It — IndexError* (both messages are now in
the table on slide 48 and in section 6 of the seminar), *No Magic Numbers*
and *Try It — Rename for Clarity* (now one slide, 56), and three of the
four slides on notebooks (now one slide, 59). The earlier deck is in Git:
`git show cc65310:lectures/content/slides/06_Python_Foundations.md`.

## Take-aways

- Python runs at a prompt, one line at a time, and as a script: a text file
  that runs from top to bottom and gives the same result at every run.
- Every value has a type, and the type decides what an operation does.
  `"20" + "20"` is `"2020"`.
- A Python `int` does not overflow. A `float` is a float64 with about 16
  digits: `9.02 / 10` is `0.9019999999999999`, and two floats are compared
  with a tolerance.
- A name is put on a value. It does not follow a formula. Two names can
  stand for one list, and a change through one is seen through the other.
- Everything read from a text file is a `str`. A line becomes numbers in
  three steps: `strip`, `split`, `float`.
- A decimal comma is either a `ValueError` or, worse, one value too many
  and no message.
- A loop applies the steps written for one row to every row. The block is
  the indented lines.
- A marker of a missing value, such as `-100`, is taken out with an `if`
  before anything is added up.
- Compute with the full value and round only what is printed:
  `f"{period_s:.3f}"`.
- A traceback is read from the bottom: the last line says what, the lines
  above it say where. The line that fails is often not the line that is
  wrong.
- Python does not find a wrong result. Know one value in advance, and
  compare with `print` or at a breakpoint.
