# 5: Python Foundations

The first Python of the course, for a room that has never written any: what
a line of Python is, values and their types, containers and larger objects,
the two lines that repeat and choose (`for` and `if`), why a step is
written once as a function and the values of one hour kept in a class,
modules and `import`, and where the rest of Python comes from, with which
version. Every piece of code grows on its slide one line, or one result,
per click. The example is the weather station's `weather.csv`, introduced
on slide 4; Part 3 computes its mean, 7.16 °C, in eleven lines, and Part 5
moves the steps into a module `weather.py` that every script imports. The
tools (the interpreter, a notebook, an editor, scripts) are shown live in
Seminar 5.

| Part | Question | Answer |
|--|--|--|
| 1 | What is a value in Python, and what can it do? | An object with a type: `int`, `float`, `bool`, `str`, and the `list`. The type says what can be done with it; its methods are written after a dot: `line.split(",")` |
| 2 | How are values kept by name, and in larger objects? | In a `dict` by key; a `tuple` is fixed, a `set` keeps each value once. A matplotlib `Figure` and the answer of a weather service are objects that hold objects |
| 3 | How do `for` and `if` turn 87 672 lines into 7.16? | A `for` over the lines, `split` and `float` on each, `if` and `continue` for −999: 7.15996550621346 from 87 552 rows (5.782796103659093 with the −999 rows) |
| 4 | How is a step written once and used again? | As a function, `def`, called by its name; the values that belong together, the time and the temperature of one hour, as an object of a class, `Hour`, with a method `is_missing()` |
| 5 | How do several scripts share one file of functions? | A module, `weather.py`, holds the functions and the class once; each script says `import weather` and keeps only its own question. A library is modules someone else wrote |
| 6 | Where does the rest of Python come from, and which version arrives? | The standard library, or packages from conda-forge and PyPI; the newest unless pinned. So one environment per project, its versions written down in `environment.yml` |

## What the lecture covers

1. **What Python is** (slides 1–5): a program is text that the
   interpreter, `python`, carries out line by line from the top; a script
   is that text in a `.py` file. The file of today, `weather.csv`: 87 672
   hours, 2016 to 2025, 120 of them written as −999.
2. **Values and types** (slides 6–17): `print` and a comment; a name with
   `=`; `count = count + 1`; the four basic types; arithmetic (`/` always a
   `float`, `//`, `%`, `**`); a `float` is rounded (`0.1 + 0.2`); comparisons
   and `bool`; a `list` and its positions from 0; a `str` has positions like
   a list (`line[0:4]` is the year); `"-4.4" + 1` is a `TypeError` until
   `float()`; every value is an object with methods (`upper`, `split`,
   `is_integer`).
3. **Containers and objects** (slides 18–26): a `dict` finds a value by its
   key; list, tuple, dict and set in one table; a list of dictionaries as a
   table; a matplotlib `Figure` that holds `Axes` that hold a `Line2D`,
   built and then drawn; JSON read into a `dict` with `json.loads`; the
   answer of the Open-Meteo weather service as a dictionary of
   dictionaries, then fetched live for Vilnius.
4. **`for` and `if`** (slides 27–36): a `for` loop growing line by line
   (mean −5.175 of four hours) and the same loop turn by turn; `if`, `elif`,
   `else`; `continue` on four hours around the gap (22.75 against
   −488.125); a loop over lines of text with `lines[1:]`; reading the file
   with `open`, `read` and `splitlines` (87 673 lines); the mean of all
   rows, 5.782796103659093; without the −999 rows, 7.15996550621346 from
   87 552 rows.
5. **Functions and classes** (slides 36–43): `mean_temp.py` and
   `coldest_hour.py` share seven lines; a step written twice, then once
   with `def`; `read_lines`, `temp_of` and `temps` (87 552 values), names
   inside a function stay inside; `mean(values)` (7.15996550621345: `sum`
   rounds one digit differently from the loop); the class `Hour` keeps the
   time beside the temperature, `__init__`, `self`, attributes; the method
   `is_missing()`; the coldest hour, 2025-01-07T05:00, −16.3 °C, with `not`
   and `and`.
6. **Modules and `import`** (slides 44–49): `weather.py` built up
   (`MISSING`, `read_lines`, `Hour`, `mean`); `mean_temp.py` with
   `import weather` (87552 7.15996550621345); what `import` does (where
   it looks, it runs the file once, the name `weather`), `from … import`,
   `import … as`, `ModuleNotFoundError`; the project, every script
   importing one module; a library, `statistics` and `math`, run live.
7. **Packages and versions** (slides 50–58): built in, standard library,
   packages; PyPI (916 606 projects) and conda-forge (34 699 packages) on 18
   October 2026; a new environment with Python holds 23 packages, with
   JupyterLab 139; releases in one year (NumPy 15, pandas 11, matplotlib 7,
   JupyterLab 33, one Python each October); major, minor and patch; which
   Pythons a package supports; an environment as a folder with one Python
   and its packages; `environment.yml`.
8. **The end** (slides 59–60): the six questions answered; the recap.

## The lecture, part by part

Week 5 gives the lecture about 1 h 45 min and the seminar the rest of the
four hours. The lecture is slides 1–60; when time is short, skip the
slides of the second table. Slide 61 opens the self-check section, and
slides 62–72 are its eleven quizzes: they take no lecture time. To jump,
type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–5 | What Python is, the file of today, the six questions |
| 6–17 | Part 1: values and types |
| 18–26 | Part 2: containers, a figure, a weather service |
| 27–35 | Part 3: `for` and `if`, to 7.16 |
| 36–43 | Part 4: functions and a class |
| 44–49 | Part 5: modules, `import`, libraries |
| 50–58 | Part 6: packages, versions, environments |
| 59–60 | The questions answered, recap |

| Skip | Slides |
|--|--|
| A `float` Is Rounded | 12 |
| Four Containers; Objects Inside Objects | 20, 21 |
| Draw the Figure; Ask the Weather Service Now (the two runnable blocks) | 23, 26 |
| Skip the −999 Rows: `continue` (slide 35 adds the same lines) | 31 |
| Reading a Version Number; Which Python a Package Supports | 55, 56 |

- **Never skip** slides 7–10 (`print`, `=`, `count = count + 1`, types),
  14–17 (list, `str`, `float()`, methods), 19 (`dict`), 28–29 (the loop and
  the loop turn by turn), 33–35 (the file, the two means), 37–38 (the
  repeated lines, `def`), 41–43 (the class, its method, the coldest hour),
  45–48 (the module, `import`, the project), 53–54 (how many packages a
  package brings, how often they change) and 57 (an environment).
- **The code grows on the slide** (Shiki magic move): each click adds a
  line, or the result of the line before as a trailing `# …` comment.
  Before the click that brings a result, have the room predict it.
- **Three blocks run** in the browser (Pyodide), slides 23 (the figure),
  26 (the weather service, which also needs Open-Meteo to answer) and 49
  (`statistics` and `math`). They need the internet in the room; press one ▶ before the lecture so that
  Pyodide and matplotlib have loaded. Slide 25 shows the answer of 18 Oct
  2026, 10:30, if the network fails.
- **No terminal** is used in the lecture: the two slides that show one have
  their output on the slide, behind a click.
- **Every speaker note has the same form**: **Do** (something done with the
  room), **Say** (the one point of the slide), **Ask** (a question for the
  room), **If asked** (the detail kept off the slide).

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 61–72: eleven quiz slides for students to try afterwards. The same
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
6. `row = {'temp_c': -4.4}`. What does `row['rain_mm']` do?
   *It stops with `KeyError: 'rain_mm'`: the key is not in the dictionary.
   Assigning `row['rain_mm'] = 0.0` would add it.*
7. In the loop for 7.16, `count = count + 1` is moved above the
   `if temp == -999:` line. What does the script print as the mean?
   *7.150165389177845: the sum still leaves out the marks, 626 869.3, but
   the count is now 87 672. No message: only a number known beforehand
   shows it.*
8. `scripts/weather.py` defines the class `Hour`. A script in `scripts/`
   starts with `import weather`. How does it make an `Hour` from `line`?
   *`weather.Hour(line)`: `import weather` gives the script one name,
   `weather`, and what the module defines is reached after a dot.
   `Hour(line)` alone is a `NameError`, unless the script says
   `from weather import Hour`.*
9. Why do the scripts of a project import `weather.py` instead of each
   defining `read_lines` and `Hour` again?
   *A change, such as a new column in the file, is then one edit, and
   every script follows. A function defined in a script works too, but
   every copy has to be changed, and a copy that is missed gives a wrong
   number without an error.*
10. NumPy goes from 2.5.4 to 2.6.0. Which part of the version changed, and
   what does it mean?
   *The minor part: new functions, and old code keeps working. 3.0.0 would
   be a major release, 2.5.5 a patch.*
11. Two projects need NumPy 1.26 and NumPy 2.5. What keeps both working on
   one laptop?
   *An environment per project, each with its own NumPy, pinned and written
   down in `environment.yml`. One environment holds one version of each
   package.*

## Paired seminar

[Seminar 5](../seminars/seminar_05.md) follows and shows live what the
lecture explained: Python at the `>>>` prompt, a conda environment with
JupyterLab and a first notebook, an editor (IDLE, then VS Code), the script
`scripts/mean_temp.py` that prints 7.16, the same steps as functions, a
class `Hour`, and a module `scripts/weather.py` that `mean_temp.py` and
`coldest_hour.py` import, the standard library (the Open-Meteo answer fetched with
`urllib` and `json`), and the environment written down in
`environment.yml`. It starts from an empty folder.

## What left the deck

On 13 October 2026 Python Foundations became Lecture 5 (Git moved to
Lecture 6) and was rebuilt on the weather project. On 18 October 2026, two
days before it was given, the lecturer split week 5 into a theory lecture
and a long live seminar; the tool slides went to the seminar. Later the
same day, after "the code blocks need to be built up gradually, a bit more
theoretical content. It gets complicated too soon", the lecture was rebuilt
again for a room without Python: it starts from what a program and the
interpreter are, without Lecture 4's `column_stats.py`, and each idea has
its own slide (`print`, `=`, types, arithmetic, rounding, comparisons, a
list before a `str`, methods, a `dict`, nested objects, JSON before the
weather service, `open` before the means). Out went
`python` as a program on `PATH`, the `>>>` prompt, a script, VS Code and
its ▶ button, what `python` does with a file, the reading of tracebacks and
the debugger, the complete `mean_temp.py` with `MISSING` and f-strings,
`int` without a fixed width, Unicode text, f-strings and column widths,
calling functions and `math.isclose`, the mean of each year with two
dictionaries (2023 the warmest, 8.31 °C), and the eight-step table. The
slides are in `lectures/content/parked/05_Python_Foundations.md`, each with
a note saying where it stood. On 19 October 2026 the lecturer asked to
"gradually show functionality of python, then show why we should have
functions / classes, and only then show how import works and what are
modules / libraries": the one `def` slide became Part 4 (functions and a
class, `Hour`) and Part 5 (modules, `import`, the project, libraries), and
week 5 moved to 105 minutes of lecture and 135 of seminar.

## Where to look things up

All of these are free. At the prompt, `help(round)` prints the description
of a function, and `help(str)` lists every string method.

- [The Python Tutorial](https://docs.python.org/3/tutorial/), chapters 3
  to 5: numbers, strings, lists, `if`, `for`, dictionaries; 4.8: functions;
  6: modules; 9: classes
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
  slides 25–26, free and without a key

## Take-aways

- Every value is an object: a type, a value, and the methods its type
  gives it. `type()` says which.
- An `int` is a whole number; a `float` is a float64 and rounds;
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
  A class is a type of your own: its objects keep values together, its
  methods are functions that belong to them.
- A module is a `.py` file of functions and classes. `import` finds it,
  runs it once and gives it a name; scripts import the module instead of
  defining the same steps again. A library is modules someone else wrote.
- Python brings built-in objects and a standard library; packages come
  from PyPI or conda-forge, bring dependencies of their own, and change
  every few weeks. An install without a version takes the newest.
- One environment per project, the versions pinned and written down in
  `environment.yml`, so that the same packages can be made again.
