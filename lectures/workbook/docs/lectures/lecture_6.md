# 6: Python Foundations

Lecture 5 put the project folder under Git, so that every change to a text
file is recorded. Until now the text files were data and notes, and the only
program in the folder was a handed-out script: Seminar 4 ran
`scripts/clean_pendulum.py`, and its output had 97 bytes and the checksum
`be05af03…`, but nobody read it. Lecture 6 opens on that script and is the
language it is written in: how Python is run, what its values are, how one
line of a data file becomes numbers, and how a loop repeats that for every
line. Halfway through, every line of the script's `clean()` is read and run
in the browser to the same 97 bytes. It builds on Lecture 3, where integers,
floats and text were made from bits, and on Lecture 4, where the shell, its
prompt and relative paths were introduced.

## What the lecture covers

1. **The script from Seminar 4** — the eight lines of `clean()` in
   `scripts/clean_pendulum.py`, run and checked but not read. The question
   of the lecture: what does each line do?
2. **Running Python** — `python3` (macOS) or `python` (Windows) as a
   program the shell starts; the `>>>` prompt against `%` and `PS>`, and
   what each prompt does with a line meant for another (PowerShell even
   prints `0.902` for `9.02 / 10`); a script run from the project folder; a
   script runs from top to bottom; the Python extension of VS Code and three
   ways to run a file.
3. **Values, types & names** — `int`, `float`, `str` and `bool`. A Python
   `int` has no fixed width and does not overflow. A `float` is the float64
   of Lecture 3, which is why `9.02 / 10` prints `0.9019999999999999`. A
   `str` is Unicode text, counted in characters and not in bytes. Arithmetic
   and its order; what a name is; calling a function; comparisons; turning
   text into a number, and the three messages when that fails. The claim of
   the lecture: a file holds text, a value becomes a number only by a step
   the script states, and a wrong step often gives no message.
4. **Strings & lists** — index and slice on a line of `D0_KPi.csv`; six
   string methods, among them `split(",", 1)` and the two replacements of
   the script's line 30; lists; the recipe *strip, split, convert* that
   turns one line into four floats; two names for one list.
5. **Decisions & loops** — `if`, `for`, `while` and `range`; the pendulum
   table as a list of lines; the period T = t10/10 for every row; a sum in a
   loop; a list comprehension; a missing value skipped with `continue`.
   Then `clean()` read line by line, and its body run on the raw pendulum
   file in the browser: 97 bytes and `be05af03`, as in Seminar 4.
6. **Dictionaries & tuples** — one row with named values; a header line and
   a data line made into a dictionary; counting into bins with a dictionary;
   the four containers side by side.
7. **Readable output** — f-strings; the format after the colon: decimals,
   widths, columns.
8. **Errors & debugging** — syntax error, exception, wrong result; a
   traceback read from the bottom; six messages and their usual causes; a
   wrong mean found with `print` and then with the debugger of VS Code:
   breakpoint, continue, step, inspect.
9. **Code that can be read** — units in names, numbers with names, PEP 8
   and a formatter. The Recap answers the opening question and commits the
   scripts of the day.

Functions are called in this lecture (`print`, `len`, `float`) and not
written: lines 25 and 32 of `clean()`, `def` and `return`, are named and not
taught. No file is opened from Python: the lines of data are pasted into
the script as a string.

## The lecture in 90 minutes

The lecture is slides 1–61 and estimates about 139 min. Slides 62–68 are the
self-check quizzes and take no lecture time. In a 2-hour slot, skip the
*Try It* slides 27 and 42 and the two *Fix It* slides 52 and 53: the seminar
does the same steps. For a 90-minute slot, follow the first table and skip
the slides in the second. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | The goal, the objectives, the script from Seminar 4 and its question |
| 0:05 | 5–9, 11 | Running Python: the interpreter, the `>>>` prompt, the first script, top to bottom, VS Code |
| 0:17 | 12–13, 15, 17–18, 20–21 | Types, the float64, names, calling a function, comparisons, text to number |
| 0:31 | 22–26 | Index and slice, string methods, lists, one line into four numbers |
| 0:41 | 29–34 | `if`, `for`, the table as lines, the period for every row, a sum in a loop |
| 0:53 | 37–39 | `continue`; `clean()` line by line (the opening question answered, about 0:57); the 97 bytes rebuilt |
| 1:03 | 40–41 | A row as a dictionary |
| 1:06 | 45–46 | f-strings |
| 1:09 | 48–50, 54–56 | Three kinds of error, the traceback, `print`, the debugger |
| 1:22 | 58–59 | Names with units |
| 1:25 | 61 | Recap. **Do not cut** |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Try It — The First Script, done live on slide 8 instead | 10 | 3 min |
| `int`: No Fixed Width, `str`: Unicode Text | 14, 19 | 7 min |
| Arithmetic | 16 | 2 min |
| Try It — Parse Another Line, Two Names, One List | 27–28 | 6 min |
| `while` and `range`, A List in One Line | 35–36 | 4 min |
| Try It — Header and Line into a dict, Counting with a dict, Four Containers | 42–44 | 10 min |
| The Format After the Colon | 47 | 3 min |
| Six Messages | 51 | 3 min |
| Fix It — NameError, Fix It — ValueError | 52–53 | 7 min |
| When a Script Fails | 57 | 2 min |
| PEP 8 | 60 | 2 min |

- **Do not cut** slide 4 (the question), slides 37–39 (`continue`, `clean()`
  line by line, the 97 bytes rebuilt: the answer) or slide 61 (the Recap,
  which answers slide 4). If time runs short before 0:53, cut from the
  middle of the table above, never these.
- **Do not cut** either slides 23–26 (index and slice, string methods,
  lists, one line into four numbers), 30–34 (`if`, `for`, the table as
  lines, the period for every row, a sum in a loop) or 49–50 and 54–56
  (errors, the traceback, `print`, the debugger). The seminar repeats every
  one of them on the keyboard, and slide 38 names the slides of 25–37 as it
  reads each line of `clean()`.
- **Slides 14 and 19**, when skipped: say their content in one sentence
  each on slide 13. A Python `int` does not overflow. A `str` is counted in
  characters, and `ą` is one of them.
- **Slide 4** is the hook. Open `scripts/clean_pendulum.py` in VS Code. A
  laptop where the installation failed in Seminar 4 saw the run on the
  projector; it follows today in the browser.
- **Slides 6–11 are shown live.** Keep VS Code open beside the slides with
  the project folder, a zsh terminal on the Mac and a PowerShell 7 terminal
  on Windows if both are at the front. Run `python3 --version` /
  `python --version`, start the prompt and type the lines of slide 7 in both
  shells (`9.02 / 10` at `PS>` prints `0.902`; the float slide explains
  why `0.9019999999999999` is the same number), write `scripts/period.py`
  next to Seminar 4's `hello.py`, install the Python extension and run the
  file in the three ways of slide 11.
- **Slide 15** needs the slide *Why 0.1 Is Not Exact* of Lecture 3. The room
  has seen `0.9019999999999999` since slide 7. This is the slide that
  explains it.
- **Slide 26** (One Line, Four Numbers) is the centre of the first half.
  Type it live in `scripts/parse_line.py` and print after every line. Do
  not rush it.
- **Slide 38** answers the opening question. Let the room read each line
  of `clean()` aloud before showing the right column. **Slide 39** runs the
  same lines on the raw table pasted as text: 10 lines kept, 97 bytes,
  checksum starting `be05af03`. `hashlib` is used as a given module, like
  `math`; nothing about it is taught. Changing `"mean"` to `"means"` gives
  108 bytes and `74e1a2a7`, with no message.
- **Slides 54–56 are shown live** on `scripts/mean_period.py`, the script
  of slide 54 with the full table of ten lines. It prints `1.3625` where
  1.514 is expected. Put a breakpoint on line 16, press `F5` three times and
  read `total` each time, then move the breakpoint to line 17, open `lines`
  under **Variables** and type `total / 9` in the Debug Console. The picture
  on slide 55 is a drawing of the window, not a screenshot. The script is
  in section 9 of the seminar page.
- **Slide 61**, the Recap, answers slide 4 and ends on two lines that are
  the same in zsh and PowerShell: `git add scripts` and
  `git commit -m "First scripts"`. Run them live.
- **The thirteen slides with a play button** (10, 14, 19, 27, 34, 37, 39,
  42, 43, 47, 52, 53, 54) run Python inside the browser. The first run takes
  a few seconds while Python loads. The code can be edited on the slide. A
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
`print` and with the debugger.

## Slides that left the deck

The rework of 4 October 2026 removed these slides: the installation slide
(installing is done in Seminar 4; slide 6 keeps the version check), the two
previews of a function and of `try` and `except` (both belong to
Lecture 7), *Why Formatting Matters*, *The Error Message Is Data*,
*Fix It — TypeError* and *Fix It — IndexError* (both messages are now in
the table on slide 51 and in section 6 of the seminar), *No Magic Numbers*
and *Try It — Rename for Clarity* (now one slide, 59), and three of the
four slides on notebooks. The earlier deck is in Git:
`git show cc65310:lectures/content/slides/06_Python_Foundations.md`.

On 6 October 2026 the deck was given an opening and a close that answers
it: it now opens on `clean_pendulum.py` from Seminar 4 (slide 4) and reads
it on slides 38–39. *Why Python*, *The Editor Does the Typing*, *Script or
Notebook* and *Read More* were parked in
`lectures/content/parked/06_Python_Foundations.md`. Format on save is now
one sentence on the PEP 8 slide; the notebook paragraph and the links are
below.

## Script or notebook

A notebook (`.ipynb`) keeps cells of code with their output and plots
below each. Cells can be run in any order, and the names of every earlier
run stay, so a result may depend on a cell that was changed or deleted
since. That suits a first look at data. This course writes scripts: plain
text, run from top to bottom, the same order and the same result at every
run, and Git shows what changed line by line. A notebook can be trusted
once it gives the same output after **Restart** and **Run All**, which is
the test a script passes every time it runs.

## Where to look things up

All of these are free. At the prompt, `help(round)` prints the description
of a function, and `help(str)` lists every string method.

- [The Python Tutorial](https://docs.python.org/3/tutorial/), chapters 3
  to 5: numbers, strings, lists, `if`, `for`, dictionaries
- [Built-in Functions](https://docs.python.org/3/library/functions.html):
  the full list, one paragraph each
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 8](https://peps.python.org/pep-0008/), the style guide
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
- [Snippets in VS Code](https://code.visualstudio.com/docs/editing/userdefinedsnippets)

## Take-aways

- The eight lines of `clean()` in `clean_pendulum.py` can now be read
  aloud: an empty list, a loop, a test with `in`, `continue`, two
  replacements in order, one cut at the first comma. Run in the browser
  they give the same 97 bytes and `be05af03` as in Seminar 4.
- A file holds text. A value becomes a number only by a step the script
  states, and a wrong step often gives no message.
- Python runs at its own prompt, `>>>`, one line at a time, and as a
  script: a text file that runs from top to bottom and gives the same
  result at every run. `%` and `PS>` are the shell's prompts; a line typed
  at the wrong one fails or, in PowerShell, is computed by the shell.
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
