# 5: Python Foundations

The first Python of the course, for a room that has never written any, told
as one question: why the mean of the weather station is worked out in Python
and not in a spreadsheet. The lecture opens on `weather.csv` in a
spreadsheet, where `AVERAGE` gives 5.78 and `AVERAGEIF` 7.16 but the sheet
keeps no record of the steps, and on three spreadsheet errors that reached
print. Then Python does the same work step by step: values and their types,
containers and larger objects, the two lines that repeat and choose (`for`
and `if`), a step written once as a function, modules and `import`, and
where the rest of Python comes from, with which version. Each part sets a
spreadsheet beside the Python where the comparison is natural, and the
lecture closes on what each leaves behind for the 7.16. Every piece of code
grows on its slide one line, or one result, per click. Writing a class of
your own is in the optional section For the Curious at the end. The tools
(the interpreter, a notebook, an editor, scripts) are shown live in
Seminar 5.

| Part | Question | Answer |
|--|--|--|
| Opening | Why not work out 7.16 in a spreadsheet? | It gets the number (`=AVERAGEIF(B2:B87673;"<>-999")` → 7.16, `=AVERAGE` → 5.78) but keeps no record of what was done to the rows; the old `.xls` holds 65 536 rows, so 22 137 hours would be lost (mean 7.08); a sheet guesses types (`SEPT2` becomes 2-Sep) and takes any range it is given (Reinhart and Rogoff) |
| 1 | What is a value in Python, and what can it do? | An object with a type: `int`, `float`, `bool`, `str`, and the `list`. The type says what can be done with it; Python does not guess it (`float("SEPT2")` is a `ValueError`); its methods are written after a dot: `line.split(",")` |
| 2 | How are values kept by name, and in larger objects? | In a `dict` by key; a `tuple` is fixed, a `set` keeps each value once. A matplotlib `Figure` and the answer of a weather service are objects that hold objects |
| 3 | How do `for` and `if` turn 87 672 lines into 7.16? | A `for` over the lines (written once, where a sheet copies a formula into every row), `split` and `float` on each, `if` and `continue` for −999: 7.15996550621346 from 87 552 rows (5.782796103659093 with the −999 rows) |
| 4 | How is a step written once and used again? | As a function, `def`, called by its name: `read_lines`, `temp_of`, `temps`, `mean`. The coldest hour, 2025-01-07T05:00, −16.3 °C, first from a copy of the mean script, then with two calls |
| 5 | How do several scripts share one file of functions? | A module, `weather.py`, holds the functions and the mark `MISSING` once; each script says `import weather` and keeps only its own question. A library is modules someone else wrote |
| 6 | Where does the rest of Python come from, and which version arrives? | The standard library, or packages from conda-forge and PyPI; the newest unless pinned. So one environment per project, its versions written down in `environment.yml`, where a sheet is worked out by whatever version each laptop has |

## What the lecture covers

1. **Why not a spreadsheet** (slides 2–4): `weather.csv` opened in a
   spreadsheet, its columns `time`, `temp_c`, `humidity_pct`, `wind_ms`;
   `=AVERAGE(B2:B87673)` gives 5.78 because the 120 hours written as −999
   count, `=AVERAGEIF(B2:B87673;"<>-999")` gives 7.16, and the sheet keeps
   the formula but not what was done to the rows. Saved as `.xls` (65 536
   rows) the file would stop after 2023-06-23T14:00: 22 137 hours lost, the
   mean of the rest 7.08 °C; `.xlsx` holds 1 048 576 rows. Public Health
   England lost 15 841 positive Covid-19 cases to that limit in October
   2020. Excel turns `SEPT2` into 2-Sep: such errors in 704 of 3 597 papers
   with gene lists (2016), and 27 human genes renamed by 2020. Reinhart and
   Rogoff's mean covered rows 30 to 44 instead of 49; corrected, growth at a
   debt above 90 % of GDP is 2.2 %, not −0.1 %.
2. **Values and types** (slides 5–16): `print`, a comment, and what the
   interpreter and a script are; a name with `=`; `count = count + 1`; the
   four basic types; arithmetic (`/` always a `float`, `//`, `%`, `**`); a
   `float` is rounded (`0.1 + 0.2`); comparisons and `bool`; a `list` and
   its positions from 0; a `str` has positions like a list (`line[0:4]` is
   the year); `"-4.4" + 1` is a `TypeError` until `float()`, and
   `float("SEPT2")` stops with a `ValueError` where a sheet guessed a date;
   every value is an object with methods (`upper`, `split`, `is_integer`).
3. **Containers and objects** (slides 17–25): a `dict` finds a value by its
   key (`row["temp_c"]`, where a sheet says `B2`); list, tuple, dict and set
   in one table; a list of dictionaries as a table; a matplotlib `Figure`
   that holds `Axes` that hold a `Line2D`, built and then drawn; JSON read
   into a `dict` with `json.loads`; the answer of the Open-Meteo weather
   service as a dictionary of dictionaries, then fetched live for Vilnius.
4. **`for` and `if`** (slides 26–35): a `for` loop growing line by line
   (mean −5.175 of four hours) and the same loop turn by turn; every hour in
   Fahrenheit, a formula copied into 87 672 cells against a loop written
   once (24.08, 23.36, 22.1, 21.2), run live; `if`, `elif`, `else`;
   `continue` on four hours around the gap (22.75 against −488.125); a loop
   over lines of text with `lines[1:]`; reading the file with `open`,
   `read` and `splitlines` (87 673 lines, all of them, where `.xls` stops at
   65 536); the mean of all rows, 5.782796103659093, the number of
   `=AVERAGE`; without the −999 rows, 7.15996550621346 from 87 552 rows.
5. **Functions** (slides 36–41): `coldest_hour.py` made from a copy of
   `mean_temp.py`, seven lines the same (2025-01-07T05:00 −16.3); a step
   written twice, then once with `def`; `read_lines`, `temp_of` and `temps`
   (87 552 values), names inside a function stay inside; `mean(values)`
   (7.15996550621345: `sum` rounds one digit differently from the loop);
   the coldest hour again with `read_lines` and `temp_of`, and `and`.
6. **Modules and `import`** (slides 42–47): `weather.py` built up
   (`MISSING`, `read_lines`, `temp_of`, `temps`, `mean`); `mean_temp.py`
   with `import weather`, four lines (87552 7.15996550621345); what `import`
   does (where it looks, it runs the file once, the name `weather`),
   `from … import`, `import … as`, `ModuleNotFoundError`; the project, both
   scripts importing one module and run; a library, `statistics` and
   `math`, run live.
7. **Packages and versions** (slides 48–56): built in, standard library,
   packages; PyPI (916 606 projects) and conda-forge (34 699 packages) on 18
   October 2026; a new environment with Python holds 23 packages, with
   JupyterLab 139; releases in one year (NumPy 15, pandas 11, matplotlib 7,
   JupyterLab 33, one Python each October); major, minor and patch; which
   Pythons a package supports; an environment as a folder with one Python
   and its packages; `environment.yml`.
8. **The end** (slides 57–58): what the spreadsheet and the script leave
   behind for the 7.16, row by row (the number, how it was made, the −999
   rule, which rows, a text such as `SEPT2`, which program, doing it again);
   the recap.
9. **For the Curious** (slides 59–62), optional: a type of your own, the
   class `Hour` with `__init__`, `self` and attributes; the method
   `is_missing()`; the coldest hour with `Hour` objects, `not` and `and`.

## The lecture, part by part

Week 5 gives the lecture about 1 h 45 min and the seminar the rest of the
four hours. The lecture is slides 1–58; when time is short, skip the
slides of the second table. Slides 59–62, For the Curious, are optional:
show them only if time is left; nothing in the lecture or the quizzes needs
them, and they take no lecture time. Slide 63 opens the self-check section,
and slides 64–76 are its thirteen quizzes: they take no lecture time
either. To jump, type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–4 | The cover; why not a spreadsheet: the mean in a sheet, the `.xls` limit, published errors |
| 5–16 | Part 1: values and types |
| 17–25 | Part 2: containers, a figure, a weather service |
| 26–35 | Part 3: `for` and `if`, to 7.16 |
| 36–41 | Part 4: functions, and the coldest hour |
| 42–47 | Part 5: modules, `import`, libraries |
| 48–56 | Part 6: packages, versions, environments |
| 57–58 | What the sheet and the script leave behind, recap |
| 59–62 | For the Curious (optional): a class `Hour` |

| Skip | Slides |
|--|--|
| A `float` Is Rounded | 11 |
| Four Containers; Objects Inside Objects | 19, 20 |
| Draw the Figure; Ask the Weather Service Now (two of the runnable blocks) | 22, 25 |
| Skip the −999 Rows: `continue` (slide 35 adds the same lines) | 31 |
| Reading a Version Number; Which Python a Package Supports | 53, 54 |

- **Never skip** slides 2–4 (the spreadsheet, the `.xls` limit, the
  published errors: the question of the lecture), 6–9 (`print`, `=`,
  `count = count + 1`, types), 13–16 (list, `str`, `float()`, methods), 18
  (`dict`), 27–29 (the loop, the loop turn by turn, Fahrenheit against the
  copied formula), 33–35 (the file, the two means), 37–38 (the copied
  script, `def`), 41 (the coldest hour with functions), 43–46 (the module,
  `import`, what it does, the project), 51–52 (how many packages a package
  brings, how often they change), 55 (an environment) and 57 (what the
  sheet and the script leave behind).
- **The code grows on the slide** (Shiki magic move): each click adds a
  line, or the result of the line before as a trailing `# …` comment.
  Before the click that brings a result, have the room predict it.
- **Spreadsheet steps are shown as text**, a cell, its formula and what it
  shows (`F1 =AVERAGE(B2:B87673) 5.78`), never as a screenshot. Some
  spreadsheets take `,` between the arguments instead of `;`.
- **Four blocks run** in the browser (Pyodide), slides 22 (the figure),
  25 (the weather service, which also needs Open-Meteo to answer), 29
  (Fahrenheit) and 47 (`statistics` and `math`). They need the internet in
  the room; press one ▶ before the lecture so that Pyodide and matplotlib
  have loaded. Slide 24 shows the answer of 18 Oct 2026, 10:30, if the
  network fails.
- **No planned live moment**: no note says **Live:**, and no terminal is
  used in the lecture; the slides that show one have their output on the
  slide, some behind a click.
- **Every speaker note has the same form**: **Do** (something done with the
  room), **Say** (the one point of the slide), **Ask** (a question for the
  room), **If asked** (the detail kept off the slide, and the sources of
  slides 3 and 4).

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 63–76: thirteen quiz slides for students to try afterwards. The same
questions, with their answers:

1. The old `.xls` format holds 65 536 rows. How many hours of
   `weather.csv`, a header line and 87 672 hours, does it keep?
   *65 535: the header takes the first row. The file stops after
   2023-06-23T14:00, the last 22 137 hours are lost, and the mean of the
   rest is 7.08 °C, not 7.16. Public Health England lost 15 841 positive
   cases to the same limit in 2020.*
2. `x = '7.16'` and `y = '1'`. What is `x + y`?
   *The text `7.161`. Both are strings, and `+` joins two strings, with no
   error. `float(x) + float(y)` gives 8.16; `'7.16' + 1` would be a
   `TypeError`.*
3. A list of gene names read from a file holds the text `'SEPT2'`. What
   does `float('SEPT2')` do?
   *It stops with `ValueError: could not convert string to float:
   'SEPT2'`. Python does not guess a type; a spreadsheet guesses as it opens
   the file, and `SEPT2` becomes the date 2-Sep.*
4. What do `100 / 4` and `100 // 4` give?
   *`25.0` and `25`. `/` always gives a float; `//` gives the whole part,
   an `int` when both sides are ints.*
5. `line = '2020-02-29T12:00,3.1,88,4.0'`. What is `line.split(',')[2]`?
   *The text `'88'`, the humidity: positions count from 0, and `split`
   hands back strings.*
6. `lines` holds 250 strings: a header and 249 rows. How many times does
   the block of `for line in lines[2:]:` run?
   *248. `lines[2:]` starts at the third item; `lines[1:]` skips only the
   header and has 249.*
7. Which container holds one row of `weather.csv` so that its temperature
   is found as `row['temp_c']`?
   *A `dict`: it finds a value by its key, the column name. A list and a
   tuple find values by position (`row[1]`); a set has no order and no
   keys.*
8. `row = {'temp_c': -4.4}`. What does `row['rain_mm']` do?
   *It stops with `KeyError: 'rain_mm'`: the key is not in the dictionary.
   Assigning `row['rain_mm'] = 0.0` would add it.*
9. In the loop for 7.16, `count = count + 1` is moved above the
   `if temp == -999:` line. What does the script print as the mean?
   *7.150165389177845: the sum still leaves out the marks, 626 869.3, but
   the count is now 87 672. No message: only a number known beforehand
   shows it.*
10. `scripts/weather.py` defines the function `temps`. A script in
   `scripts/` starts with `import weather`. How does it call `temps` for
   `path`?
   *`weather.temps(path)`: `import weather` gives the script one name,
   `weather`, and what the module defines is reached after a dot.
   `temps(path)` alone is a `NameError`, unless the script says
   `from weather import temps`.*
11. Why do the scripts of a project import `weather.py` instead of each
   defining `read_lines` and `temp_of` again?
   *A change, such as a new column in the file, is then one edit, and
   every script follows. A function defined in a script works too, but
   every copy has to be changed, and a copy that is missed gives a wrong
   number without an error.*
12. NumPy goes from 2.5.4 to 2.6.0. Which part of the version changed, and
   what does it mean?
   *The minor part: new functions, and old code keeps working. 3.0.0 would
   be a major release, 2.5.5 a patch.*
13. Two projects need NumPy 1.26 and NumPy 2.5. What keeps both working on
   one laptop?
   *An environment per project, each with its own NumPy, pinned and written
   down in `environment.yml`. One environment holds one version of each
   package.*

## Paired seminar

[Seminar 5](../seminars/seminar_05.md) follows and shows live what the
lecture explained: Python at the `>>>` prompt, a conda environment with
JupyterLab and a first notebook, an editor (IDLE, then VS Code), the script
`scripts/mean_temp.py` that prints 25.3 for six typed hours of the log, the
same steps as functions, a
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

After the lecture of 20 October 2026 ("quite dry, just a bunch of python
function not much story telling … Maybe compare with proprietary tools";
"Why we need python, not excel"; "Classes - way too steep"; "what's with
the first 5 slides? I don't need them") the deck was reworked on 21 October
around one question, why Python and not a spreadsheet. Out went the quote,
"What Happens When Python Runs", "The File of Today" and the table of the
six parts (the interpreter is now one sentence on the `print` slide, the
columns of the file are on the spreadsheet slide), the two 13-line scripts
side by side (now one copy built up click by click), the coldest hour with
`Hour` in Part 5, and the six questions answered; they are parked in the
same file. In came the opening on the spreadsheet (slides 2–4), the
Fahrenheit slide, the closing table, and a spreadsheet beside the Python
where it fits (`SEPT2`, `B2`, a copied formula, `lines[1:]` against a typed
range, `"<>-999"` in each formula, the program version). Writing a class
moved to For the Curious, after the recap, so Parts 4 and 5 use functions
only: `weather.py` holds `MISSING`, `read_lines`, `temp_of`, `temps` and
`mean`. Long blocks were cut or built up by magic move.

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
  slides 24–25, free and without a key
- Ziemann, Eren and El-Osta, *Gene name errors are widespread in the
  scientific literature*, Genome Biology 17, 177 (2016), and Herndon, Ash
  and Pollin, *Does high public debt consistently stifle economic growth? A
  critique of Reinhart and Rogoff*, the working paper of April 2013 of the
  Political Economy Research Institute, University of Massachusetts
  Amherst: two of the spreadsheet errors of slide 4

## Take-aways

- A spreadsheet gets the number, 7.16, but keeps no record of the steps:
  what was done to the rows, which range, which rule for −999. It guesses
  types and the old `.xls` stops at 65 536 rows, with a number that still
  looks right. A script writes every step down, and runs again with one
  command.
- Every value is an object: a type, a value, and the methods its type
  gives it. `type()` says which.
- An `int` is a whole number; a `float` is a float64 and rounds;
  a `str` is text, and `"-4.4"` is not a number until `float()` makes it
  one; `float("SEPT2")` stops with a `ValueError` instead of guessing.
- A `list` holds values in order and grows; a `tuple` is fixed; a `dict`
  finds a value by its key; a `set` keeps each value once. Containers hold
  other containers, as the dictionary of dictionaries of a web service
  does.
- `for` repeats a block once per item; `if`, `elif` and `else` choose a
  block; `continue` ends a turn. Without leaving out −999 the mean of
  `weather.csv` is 5.78; with it, 7.16.
- `def` writes a step once, under a name, for every line that needs it,
  where a sheet copies a formula into every row. (For the Curious: a class
  is a type of your own; its objects keep values together, its methods are
  functions that belong to them.)
- A module is a `.py` file of functions. `import` finds it,
  runs it once and gives it a name; scripts import the module instead of
  defining the same steps again. A library is modules someone else wrote.
- Python brings built-in objects and a standard library; packages come
  from PyPI or conda-forge, bring dependencies of their own, and change
  every few weeks. An install without a version takes the newest.
- One environment per project, the versions pinned and written down in
  `environment.yml`, so that the same packages can be made again.
