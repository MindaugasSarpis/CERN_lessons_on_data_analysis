# 5: Python Foundations

Lecture 4 checked Smiltė's ten-year mean, **7.16 °C**, and in the end with
`scripts/column_stats.py`, a Python program someone else wrote, run without
being read. Lecture 5 is the theory under such a program, in about an hour:
what Python's values are, how `for` and `if` combine them into 7.16, and
where the values come from that Python does not have, with which version.
Every piece of code is built on its slide one line at a time. The tools
(the interpreter, a notebook, an editor, scripts and modules) are shown
live in Seminar 5, which follows for about three hours. The room knows the
shell (zsh on macOS, Git Bash on Windows), `PATH` and the weather project
from Lecture 4; Git comes in Lecture 6.

| Part | Question | Answer |
|--|--|--|
| 1 | What kinds of values does Python have, and what can each do? | Objects of a type: `int`, `float`, `bool`, `str`; the containers `list`, `tuple`, `dict`, `set`; larger objects such as a matplotlib `Figure` or the answer of a web service. The type says which methods an object has |
| 2 | How do `for` and `if` turn 87 672 lines into 7.16? | A `for` over the lines, `split` and `float` on each, `if` and `continue` for −999: 7.15996550621346 from 87 552 rows (5.782796103659093 with the −999 rows) |
| 3 | Where do the other objects come from, and which version arrives? | The standard library, or packages from conda-forge and PyPI; the newest unless pinned. So one environment per project, its versions written down in `environment.yml` |

## What the lecture covers

1. **The question** (slides 1–4): `column_stats.py` gives 5.7828 on the raw
   file and 7.15997 without the −999 rows; it is 53 lines of Python. The
   three questions of the lecture.
2. **Objects and types** (slides 5–14): −4.4 is an object with a type
   (`float`), a value and methods (`temp.is_integer()`); `int`, `float` and
   `bool` (`87672 / 24` is `3653.0`, `//` gives `3653`, 2¹⁰⁰ is exact, and
   `0.1 + 0.2` is 0.30000000000000004, the float64 of Lecture 3); a line of
   `weather.csv` as a `str`: a slice, `split(",")`, `"-4.4" + 1` a
   `TypeError`, `float()`; the containers `list` and `tuple` (a tuple
   cannot be changed), `dict` and `set` (`get` against `KeyError`); a
   matplotlib `Figure` that holds `Axes` that hold a `Line2D`, built line by
   line and then drawn; the answer of the Open-Meteo weather service as a
   dictionary of dictionaries, built and then fetched live for Vilnius.
3. **`for` and `if`** (slides 15–24): `count = count + 1`; a `for` loop
   growing line by line (mean −5.175 of four hours), then the same loop turn
   by turn in a table; a loop over the lines of a file with `lines[1:]`;
   the mean of all rows, 5.782796103659093; `if`, `elif`, `else`;
   `continue` on four hours around the gap (22.75 against −488.125); the
   mean without the −999 rows, 7.15996550621346 from 87 552 rows; a step
   written twice, then once as `def temp_of(line)` and called in a loop.
4. **Packages and versions** (slides 25–33): built in, standard library,
   packages, and `ModuleNotFoundError` for a package not installed; PyPI
   (916 606 projects) and conda-forge (34 699 packages) on 18 October 2026;
   a new environment with Python holds 23 packages, with JupyterLab 139;
   releases in one year (NumPy 15, pandas 11, matplotlib 7, JupyterLab 33,
   one Python each October); major, minor and patch; which Pythons NumPy,
   pandas and matplotlib support; an environment as a folder with one
   Python and its packages, one per project; `environment.yml`.
5. **The end** (slides 34–35): the three questions answered; the recap.

## The lecture in one hour

Week 5 gives the lecture about an hour and the seminar about three. The
lecture is slides 1–35. Slide 36 opens the self-check section, and slides
37–45 are its nine quizzes: they take no lecture time. To jump, type the
slide number and press Enter.

| Slides | Part |
|--|--|
| 1–4 | `column_stats.py`, and the three questions |
| 5–14 | Part 1: objects and types, a figure, a web service |
| 15–24 | Part 2: `for` and `if`, to 7.16; `def` |
| 25–33 | Part 3: packages, versions, environments |
| 34–35 | The questions answered, recap |

To end on the hour, skip the slides below. None is needed by a later slide.

| Skip if time is short | Slides |
|--|--|
| Add One to a Count (say it at the `for` slide) | 16 |
| Skip the −999 Rows: `continue` (the next slide adds the same three lines) | 22 |
| Reading a Version Number; Which Python a Package Supports | 30, 31 |

- **Never skip** slide 6 (every value is an object), 8 (a line is a
  `str`), 13–14 (the dictionary of dictionaries, fetched live), 17–18 (the
  loop, and the loop turn by turn), 23 (7.16), 24 (`def`), 28–29 (how many
  packages a package brings, how often they change) and 32 (an
  environment).
- **The code grows on the slide** (Shiki magic move): each click adds a
  line, or the result of the line before as a trailing `# …` comment.
  Before the click that brings a result, have the room predict it.
- **Two blocks run** in the browser (Pyodide), slides 12 (the figure) and
  14 (the weather service, which also needs Open-Meteo to answer). They
  need the internet in the room; press one ▶ before the lecture so that
  Pyodide and matplotlib have loaded. Slide 13 shows the answer of 18 Oct
  2026, 10:30, if the network fails.
- **No terminal** is used in the lecture: the slides that show one have
  their output on the slide, behind a click. Typing is the seminar's work.
- **Every speaker note has the same form**: **Do** (something done with the
  room), **Say** (the one point of the slide), **Ask** (a question for the
  room), **If asked** (the detail kept off the slide).

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 36–45: nine quiz slides for students to try afterwards. The same
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
5. Which container holds one row of `weather.csv` so that its temperature
   is found as `row['temp_c']`?
   *A `dict`: it finds a value by its key, the column name. A list and a
   tuple find values by position (`row[1]`); a set has no order and no
   keys.*
6. `hours = {'2016': 8784}`. What do `hours.get('2026', 0)` and
   `hours['2026']` do?
   *The first gives 0, the second stops with `KeyError: '2026'`. Neither
   adds a key.*
7. In the loop for 7.16, `count = count + 1` is moved above the
   `if temp == -999:` line. What does the script print as the mean?
   *7.150165389177845: the sum still leaves out the marks, 626 869.3, but
   the count is now 87 672. No message: only a number known beforehand
   shows it.*
8. NumPy goes from 2.5.4 to 2.6.0. Which part of the version changed, and
   what does it mean?
   *The minor part: new functions, and old code keeps working. 3.0.0 would
   be a major release, 2.5.5 a patch.*
9. Two projects need NumPy 1.26 and NumPy 2.5. What keeps both working on
   one laptop?
   *An environment per project, each with its own NumPy, pinned and written
   down in `environment.yml`. One environment holds one version of each
   package.*

## Paired seminar

[Seminar 5](../seminars/seminar_05.md) follows for about three hours and
shows live what the lecture explained: Python at the `>>>` prompt, a conda
environment `weather` with JupyterLab and a first notebook, an editor
(IDLE, then VS Code), the script `scripts/mean_temp.py` that prints 7.16, a
module `scripts/weather.py` with `temp_of(line)`, the standard library
(the Open-Meteo answer fetched with `urllib` and `json`), and the
environment written down in `environment.yml`.

## What left the deck

On 13 October 2026 Python Foundations became Lecture 5 (Git moved to
Lecture 6) and was rebuilt on the weather project. On 18 October 2026, two
days before it was given, the lecturer split week 5 into a one-hour lecture
and a three-hour seminar: the lecture became theory in three parts
(objects, `for` and `if`, packages and versions), with every piece of code
built by magic move, and the tool slides went to the seminar. Out went
`python` as a program on `PATH`, the `>>>` prompt, a script, VS Code and
its ▶ button, what `python` does with a file, the reading of tracebacks and
the debugger, the complete `mean_temp.py` with `MISSING` and f-strings, the
runner versions of the type, string, list, loop and `if` slides, `int`
without a fixed width, Unicode text, f-strings and column widths, calling
functions and `math.isclose`, the mean of each year with two dictionaries
(2023 the warmest, 8.31 °C), and the eight-step table. The slides are in
`lectures/content/parked/05_Python_Foundations.md`, each with a note saying
where it stood.

## Where to look things up

All of these are free. At the prompt, `help(round)` prints the description
of a function, and `help(str)` lists every string method.

- [The Python Tutorial](https://docs.python.org/3/tutorial/), chapters 3
  to 5: numbers, strings, lists, `if`, `for`, dictionaries
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html): every
  method of `int`, `float`, `str`, `list`, `tuple`, `dict` and `set`
- [The Python Standard Library](https://docs.python.org/3/library/): what
  comes with every Python
- [PyPI](https://pypi.org) and [conda-forge](https://conda-forge.org/packages/):
  the two package indexes
- [Status of Python versions](https://devguide.python.org/versions/):
  release and end-of-life dates
- [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  in the conda documentation
- [Open-Meteo](https://open-meteo.com/en/docs): the weather service of
  slides 13–14, free and without a key

## Take-aways

- Every value is an object: a type, a value, and the methods its type
  gives it. `type()` says which.
- A Python `int` is exact at any size; a `float` is a float64 and rounds;
  a `str` is text, and `"-4.4"` is not a number until `float()` makes it
  one.
- A `list` holds values in order and grows; a `tuple` is fixed; a `dict`
  finds a value by its key; a `set` keeps each value once. Containers hold
  other containers, as the dictionary of dictionaries of a web service
  does.
- `for` repeats a block once per item; `if`, `elif` and `else` choose a
  block; `continue` ends a turn. Without leaving out −999 the mean of
  `weather.csv` is 5.78; with it, 7.16.
- `def` writes a step once, under a name, for every line that needs it.
- Python brings built-in objects and a standard library; packages come
  from PyPI or conda-forge, bring dependencies of their own, and change
  every few weeks. An install without a version takes the newest.
- One environment per project, the versions pinned and written down in
  `environment.yml`, so that the same packages can be made again.
