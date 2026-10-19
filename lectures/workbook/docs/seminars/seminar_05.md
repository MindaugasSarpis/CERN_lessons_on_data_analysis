# Seminar 5 · Python

**Paired lecture:** 05 Python Foundations · **Format:** type-along tutorial, in class

<!-- ~205 min: the length pnpm timing:check reads -->

**Today's goal:** Can Python compute 7.16 for us? Every student types Python in four places (the
interpreter, a Jupyter notebook, an editor, a script with its own module)
and gets the mean temperature of `weather.csv`, 7.16 °C, in each; repairs a
script with two bugs; writes its steps once, as functions and a class in a
module `weather.py` that every script imports; asks a weather service for
the temperature now; and writes the project's conda environment into
`environment.yml`.

Everything is typed in VS Code's terminal (zsh on macOS, Git Bash on
Windows; the lines are the same in both). In the blocks, a line that starts
with `$` is typed in the terminal, a line that starts with `>>>` or `...`
is typed at Python's prompt, and every other line is what comes back.

**If time runs short:** leave out sections 10 to 12 (tuples and
dictionaries, the order of cells, IDLE) and 18 (the temperature now).
Sections 15 to 17, functions, a class and a module, are the point of the
day; do them, and 19 (the environment file).

??? info "Before the session"
    - **Room:** VS Code, and Miniforge with `(base)` in the prompt of
      VS Code's terminal; a laptop without Miniforge (or, on Windows,
      without Git Bash) installs them in section 1, step 2. Internet: the environment is about 70 MB per laptop, the
      weather log 2.5 MB. The session needs nothing from any other
      seminar: it starts in an empty folder.
    - **You:** remove the Python extension from your VS Code beforehand, to
      install it with the room in section 13. Paths are shown for a Mac
      (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`. Keys are
      written for Windows, macOS in brackets.

---

## Getting ready { #part-0 }

<!-- 0:00 to 0:15 -->

An empty folder for today, and one conda environment for the Python and the programs of today.

---

### 1. A folder and an environment { #start }

<!-- 0:00 · 15 min -->

**conda** installs Python and packages; it comes with **Miniforge**. A **conda environment** is a folder with one Python and the packages one project needs. Today's needs JupyterLab, the notebook program; it brings about 140 packages with it.

1. In VS Code, **View** > **Terminal**. Check that conda is there.

    ```text
    $ conda --version
    conda 26.7.2
    ```

    Any version is fine. The prompt starts with `(base)`: conda's own
    environment, which stays as it is.

2. `command not found`, or a Windows terminal without `$` in its prompt?
   Install the tools now, about 10 minutes; the others go on with step 3.
   A laptop without an administrator's password pairs with a neighbour
   today.

    === "macOS"

        1. Open the system's terminal: `Cmd+Space`, type `Terminal`,
           `Enter`. Its shell is `zsh`.
        2. Check the package manager **Homebrew**.

            ```text
            $ brew --version
            Homebrew …
            ```

        3. `command not found`? Install Homebrew. Type the laptop's
           password when asked: nothing shows while typing. It may install
           the developer tools of macOS first, which takes a while.

            ```text
            $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            ```

            At the end it prints **Next steps**: copy the lines it lists
            there, paste them, `Enter`.

        4. Install Miniforge, then let conda set up `zsh`, so that every
           new terminal finds Python.

            ```text
            $ brew install --cask miniforge
            $ conda init zsh
            ==> For changes to take effect, close and re-open your current shell. <==
            ```

    === "Windows"

        1. Open PowerShell: Windows key, type `powershell`, `Enter`. Only
           the next two lines are typed here.
        2. Install Git, which brings **Git Bash**, the course's shell on
           Windows, and Miniforge, one line at a time. Each ends with
           `Successfully installed`. Answer `Y` if winget asks about the
           source agreements, **Yes** if Windows asks for permission.

            ```text
            PS> winget install --id Git.Git -e
            PS> winget install --id CondaForge.Miniforge3 -e
            ```

        3. Quit VS Code and start it again. Command Palette,
           `Ctrl+Shift+P`, type and choose `Terminal: Select Default
           Profile`, take **Git Bash**. Then `Terminal: Create New
           Terminal` from the Command Palette.
        4. Let conda set up Git Bash.

            ```text
            $ ~/miniforge3/Scripts/conda.exe init bash
            ==> For changes to take effect, close and re-open your current shell. <==
            ```

    Quit VS Code (**File** > **Exit**, macOS `Cmd+Q`), start it again and
    open **View** > **Terminal**: `(base)` at the start of the prompt, and
    `conda --version` prints a version as in step 1.

3. An empty folder for today, in your home folder. The files arrive
   when they are needed.

    ```text
    $ mkdir ~/weather-s05
    $ cd ~/weather-s05
    $ pwd
    /Users/smilte/weather-s05
    ```

4. **File** > **Open Folder...** > `weather-s05` (in your home folder) >
   **Open**, then **View** > **Terminal**: the new terminal starts in the
   folder.

5. Make the environment `s05` with Python 3.14 and JupyterLab 4.6. conda
   downloads them from **conda-forge**, the free collection of packages
   that Miniforge uses: nothing more to install. It lists what it will
   download and asks.

    ```text
    $ conda create -n s05 python=3.14 jupyterlab=4.6
    ...
      added / updated specs:
        - jupyterlab=4.6
        - python=3.14
    ...
    Proceed ([y]/n)?
    ```

6. Press `Enter`. The download takes a few minutes. It ends with:

    ```text
    #     $ conda activate s05
    ```

7. Switch it on: the prompt starts with `(s05)`. Each new terminal starts
   in `(base)`, so type this line first in each.

    ```text
    $ conda activate s05
    $ python --version
    Python 3.14.8
    ```

8. How many packages came with it. `conda list` prints one line per
   package after three lines of header.

    ```text
    $ conda list | wc -l
    142
    ```

    About 140 (macOS pads the number with spaces, and macOS and Windows
    differ by a few packages). Python alone is about 25: the rest is
    JupyterLab and what it needs.

**Check:** `(s05)` at the start of the prompt and `Python 3.14.8`.

---

## Part 1 · The interpreter { #part-1 }

<!-- 0:15 to 1:00 -->

Python reads one line, works it out and prints the answer. Nothing typed here is kept.

Further reading: [The Python Tutorial, chapters 2 and 3](https://docs.python.org/3/tutorial/introduction.html);
[HSF Analysis Essentials, Python](https://hsf-training.github.io/analysis-essentials/python/README.html).

---

### 2. Python as a calculator { #numbers }

<!-- 0:15 · 10 min -->

The `>>>` prompt: the place to try one line.

1. Start the interpreter. The first line names the version; `>>>` is
   Python's prompt, waiting for a line.

    ```text
    $ python
    Python 3.14.8 | packaged by conda-forge | ...
    >>>
    ```

2. Type an expression and press `Enter`: Python prints its value. The
   station's mean temperature, 7.16 °C, in Fahrenheit:

    ```pycon
    >>> 2 + 2
    4
    >>> 7.16 * 9 / 5 + 32
    44.888
    ```

3. `/` always gives a **float** (a number with a point); `//` and `%`
   give the whole part and the remainder as **int**s. `**` is the power.

    ```pycon
    >>> 87672 / 24
    3653.0
    >>> 87672 // 24
    3653
    >>> 87672 % 24
    0
    >>> 2 ** 10
    1024
    ```

4. A float is stored in binary with about 16 digits, so some decimals
   come out slightly off.

    ```pycon
    >>> 0.1 + 0.2
    0.30000000000000004
    ```

    Measured values are compared with a tolerance, never for exact
    equality.

**Check:** `44.888` and `3653`.

---

### 3. Give a value a name { #names }

<!-- 0:25 · 5 min -->

`=` puts a name on a value, so a later line can use it.

1. How many hourly rows should ten years have? Three of them (2016, 2020,
   2024) are leap years. `=` prints nothing; typing the name shows its
   value.

    ```pycon
    >>> hours = 365 * 24 * 10 + 3 * 24
    >>> hours
    87672
    >>> days = hours // 24
    >>> days
    3653
    ```

2. `=` works out the right side first, then puts the name on the result.
   So a name can be used to change itself:

    ```pycon
    >>> count = 0
    >>> count = count + 1
    >>> count = count + 1
    >>> count
    2
    ```

    A name has letters, digits and `_`, does not start with a digit, and
    `Count` is another name than `count`.

**Check:** `hours` gives `87672`.

---

### 4. Text: one line of `weather.csv` { #strings }

<!-- 0:30 · 10 min -->

Text between quotes is a **string** (`str`). The file is text, so each line arrives as a string.

1. The first row of the log, as a string. At the prompt Python shows it
   with quotes; `print` shows the text itself.

    ```pycon
    >>> line = "2016-01-01T00:00,-4.4,93,2.5"
    >>> line
    '2016-01-01T00:00,-4.4,93,2.5'
    >>> print(line)
    2016-01-01T00:00,-4.4,93,2.5
    >>> len(line)
    28
    ```

2. Each character has a position, counted from 0. `line[0]` is the first
   character; `line[0:4]` runs from position 0 up to, not including, 4. A
   negative position counts from the end.

    ```pycon
    >>> line[0]
    '2'
    >>> line[0:4]
    '2016'
    >>> line[5:7]
    '01'
    >>> line[-3:]
    '2.5'
    >>> line[17:21]
    '-4.4'
    ```

3. `'-4.4'` is four characters, not a number. `+` joins two strings, and
   refuses a string and a number:

    ```pycon
    >>> "-4.4" + "1"
    '-4.41'
    >>> "-4.4" + 1
    Traceback (most recent call last):
      ...
    TypeError: can only concatenate str (not "int") to str
    ```

    The last line of an error says what went wrong.

4. `float(...)` turns the text into a number (`int(...)` into a whole
   number). The tail of digits is the float of section 2, step 4.

    ```pycon
    >>> float("-4.4") + 1
    -3.4000000000000004
    ```

**Check:** `line[17:21]` gives `'-4.4'`, with quotes.

---

### 5. Lists, and what can change { #lists }

<!-- 0:40 · 10 min -->

A **list** holds several values in order, in square brackets.

1. `split(",")` cuts the line at each comma and hands back a list of four
   strings. A list counts from 0 like a string.

    ```pycon
    >>> parts = line.split(",")
    >>> parts
    ['2016-01-01T00:00', '-4.4', '93', '2.5']
    >>> parts[1]
    '-4.4'
    >>> len(parts)
    4
    ```

2. A list of numbers: the first three hours of 2016. `append` adds a
   fourth; `sum`, `len`, `min` work on the whole list.

    ```pycon
    >>> temps = [-4.4, -4.8, -5.5]
    >>> temps.append(-6.0)
    >>> temps
    [-4.4, -4.8, -5.5, -6.0]
    >>> sum(temps) / len(temps)
    -5.175
    >>> min(temps)
    -6.0
    ```

3. A list can be changed in place. A string cannot: a changed text is
   always a new string.

    ```pycon
    >>> temps[0] = -4.5
    >>> temps
    [-4.5, -4.8, -5.5, -6.0]
    >>> line[0] = "3"
    Traceback (most recent call last):
      ...
    TypeError: 'str' object does not support item assignment
    ```

    A value that can change is **mutable** (a list); one that cannot is
    **immutable** (a string, a number).

**Check:** the mean of the four hours, `-5.175`, before step 3 changed the
first one.

---

### 6. Ask an object what it is { #objects }

<!-- 0:50 · 10 min -->

Every value is an **object**: it has a type, and the type decides what it can do.

1. `type` names the type.

    ```pycon
    >>> type(7.16)
    <class 'float'>
    >>> type(line)
    <class 'str'>
    >>> type(parts)
    <class 'list'>
    ```

2. `dir` lists what an object can do. A string can do 81 things; the last
   twelve:

    ```pycon
    >>> len(dir(line))
    81
    >>> dir(line)[-12:]
    ['rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>> line.count(",")
    3
    ```

    A function that belongs to an object is a **method**, called with a
    dot: `line.split(",")`, `line.count(",")`.

3. `help` explains one of them. It opens a pager: arrows scroll, `q`
   leaves it.

    ```pycon
    >>> help(str.split)
    Help on method descriptor split:

    split(self, /, sep=None, maxsplit=-1) unbound builtins.str method
        Return a list of the substrings in the string, using sep as the separator string.
    ```

4. The arrow up brings back the lines typed before. Leave the
   interpreter, start it again, and ask for `hours`:

    ```pycon
    >>> exit()
    $ python
    >>> hours
    Traceback (most recent call last):
      ...
    NameError: name 'hours' is not defined
    >>> exit()
    ```

    Everything typed at `>>>` is gone when it ends. Part 2 keeps it.

**Check:** `NameError` for `hours` in the new interpreter, and the shell's
prompt (`%` or `$`) after `exit()`.

!!! question "Task: the wind in km/h, the temperature in °F"
    From `parts` of the first row, work out at `>>>` the wind in km/h (the
    fourth value, in m/s, × 3.6) and the temperature in °F (× 9 / 5 + 32).
    Make `line` and `parts` again first: the new interpreter forgot them.

??? success "Answer"
    ```pycon
    >>> line = "2016-01-01T00:00,-4.4,93,2.5"
    >>> parts = line.split(",")
    >>> float(parts[3]) * 3.6
    9.0
    >>> float(parts[1]) * 9 / 5 + 32
    24.08
    ```

    `parts[3]` is the fourth value: positions start at 0.

---

## Part 2 · A notebook { #part-2 }

<!-- 1:00 to 1:55 -->

A Jupyter notebook keeps the code, its output and notes in one file, in cells run one at a time.

Further reading: [The Python Tutorial, chapters 4 and 5](https://docs.python.org/3/tutorial/controlflow.html).

---

### 7. Start JupyterLab { #jupyter }

<!-- 1:00 · 10 min -->

JupyterLab is a program in the browser; the terminal runs its server.

1. The weather log, from the course's Releases page into `data/raw`.
   `curl` downloads a file: `-sSL` is quiet, but shows errors and follows
   GitHub's redirect; `-o` names the file to write. Then look at its
   first lines.

    ```text
    $ mkdir -p data/raw
    $ curl -sSL -o data/raw/weather.csv https://github.com/MindaugasSarpis/weather-project/releases/download/seminar-files/weather.csv
    $ head -n 3 data/raw/weather.csv
    time,temp_c,humidity_pct,wind_ms
    2016-01-01T00:00,-4.4,93,2.5
    2016-01-01T01:00,-4.8,95,2.6
    ```

    One reading per hour, 2016 to 2025: the time, the temperature in °C,
    the humidity in %, the wind in m/s. An hour without a reading has
    `-999`.

2. A folder for notebooks, then start JupyterLab in the project folder,
   with `(s05)` in the prompt.

    ```text
    $ mkdir notebooks
    $ jupyter lab
    [I 2026-10-18 13:37:05.535 ServerApp] Serving notebooks from local directory: /Users/smilte/weather-s05
    [I 2026-10-18 13:37:05.535 ServerApp] Jupyter Server 2.21.1 is running at:
    [I 2026-10-18 13:37:05.535 ServerApp] http://localhost:8888/lab?token=a6e4e80196...
    ```

    The browser opens JupyterLab. The terminal stays busy while it runs:
    leave it open.

3. On the left, the files of the project. Double-click `notebooks`.
4. In the **Launcher**, under **Notebook**, click **Python 3
   (ipykernel)**. A file `Untitled.ipynb` opens.
5. Right-click its tab > **Rename Notebook...**, type `explore.ipynb`,
   **Rename**.

**Check:** `notebooks/explore.ipynb` in the file list, an empty cell with
`[ ]:` beside it.

!!! warning "No browser window"
    Copy the line `http://localhost:8888/lab?token=...` from the terminal
    into the browser.

---

### 8. Cells: the whole file in a list { #cells }

<!-- 1:10 · 10 min -->

A cell is run with `Shift+Enter`; the value of its last line appears under it.

1. Type in the first cell, then `Shift+Enter`. `[1]` beside it counts the
   runs; the answer appears under it, and a new cell below.

    ```python
    2 + 2
    ```

    ```text
    4
    ```

2. Read the file into a list of lines. The notebook runs in
   `notebooks`, so the path starts with `..`, the folder above.

    ```python
    lines = open("../data/raw/weather.csv").read().splitlines()
    len(lines)
    ```

    ```text
    87673
    ```

    The header and 87 672 hours, the number of section 3.

3. One cell per question: the second line and the last.

    ```python
    lines[1]
    ```

    ```text
    '2016-01-01T00:00,-4.4,93,2.5'
    ```

    ```python
    lines[-1]
    ```

    ```text
    '2025-12-31T23:00,-11.3,100,4.2'
    ```

4. A note between the cells: click the first cell's left edge, press `B`
   (a new cell below), `M` (make it Markdown), type, `Shift+Enter`.

    ```text
    # The hourly log of weather.csv
    ```

    It shows as a heading. Save: `Ctrl+S` (macOS `Cmd+S`).

**Check:** `87673` under the cell, a heading above it.

---

### 9. Repeat and decide: `for` and `if` { #loop }

<!-- 1:20 · 15 min -->

`for` runs the indented lines once for each item of a list; `if` runs them only when a condition is true.

1. The first three hours, one per turn of the loop. The lines indented
   by four spaces under the `:` are the ones that repeat.

    ```python
    for line in lines[1:4]:
        print(line)
    ```

    ```text
    2016-01-01T00:00,-4.4,93,2.5
    2016-01-01T01:00,-4.8,95,2.6
    2016-01-01T02:00,-5.5,95,2.7
    ```

    `lines[1:4]` is positions 1, 2 and 3: the header, position 0, is left
    out.

2. `if`, then `else` for the other case. `<` compares; `==` asks "equal?"
   (one `=` gives a name).

    ```python
    for line in lines[1:4]:
        temp = float(line.split(",")[1])
        if temp < -5:
            print(temp, "below -5")
        else:
            print(temp, "-5 or warmer")
    ```

    ```text
    -4.4 -5 or warmer
    -4.8 -5 or warmer
    -5.5 below -5
    ```

3. The mean of every hour. One cell starts the sum and the count, the
   next adds each hour, the third divides. A cell can show two values,
   separated by a comma.

    ```python
    total = 0.0
    count = 0
    ```

    ```python
    for line in lines[1:]:
        temp = float(line.split(",")[1])
        total = total + temp
        count = count + 1
    ```

    ```python
    count, total / count
    ```

    ```text
    (87672, 5.782796103659093)
    ```

4. 5.78, not 7.16: the 120 hours marked `-999` are in the sum. Add the
   two `if` lines (`continue` skips to the next line), then run the three
   cells again from the first.

    ```python
    for line in lines[1:]:
        temp = float(line.split(",")[1])
        if temp == -999:
            continue
        total = total + temp
        count = count + 1
    ```

    ```text
    (87552, 7.15996550621346)
    ```

5. The 7.16: round only what is printed. An `f` before the
   quotes puts the value of each `{...}` into the text; `:.2f` gives two
   decimals.

    ```python
    f"{count} hours, mean {total / count:.2f} °C"
    ```

    ```text
    '87552 hours, mean 7.16 °C'
    ```

**Check:** `(87552, 7.15996550621346)`: 120 hours fewer than 87 672.

!!! warning "`IndentationError`"
    The lines under `for` or `if` need the same indentation. JupyterLab
    adds four spaces after `:` and `Enter`.

---

### 10. Tuples and dictionaries { #dict }

<!-- 1:35 · 10 min -->

A **tuple** is a fixed group of values, in round brackets. A **dictionary** (`dict`) finds a value by a key, in curly brackets.

1. The cell `count, total / count` gave a tuple. A tuple holds values that
   belong together, and it cannot be changed.

    ```python
    first = (lines[1][:16], float(lines[1].split(",")[1]))
    first
    ```

    ```text
    ('2016-01-01T00:00', -4.4)
    ```

2. Hours per year, with the year (`line[:4]`) as key. `hours.get(year,
   0)` is the count so far, 0 for a new year.

    ```python
    hours = {}
    for line in lines[1:]:
        year = line[:4]
        hours[year] = hours.get(year, 0) + 1
    ```

3. The whole dictionary, in a cell of its own. JupyterLab prints a long
   one with one key per line.

    ```python
    hours
    ```

    ```text
    {'2016': 8784,
     '2017': 8760,
     '2018': 8760,
     '2019': 8760,
     '2020': 8784,
     '2021': 8760,
     '2022': 8760,
     '2023': 8760,
     '2024': 8784,
     '2025': 8760}
    ```

4. One value by its key.

    ```python
    hours["2016"]
    ```

    ```text
    8784
    ```

    366 × 24: 2016 is a leap year.

**Check:** 8784 hours in 2016, 2020 and 2024, 8760 in the other years.

---

### 11. Run the cells in order { #order }

<!-- 1:45 · 10 min -->

A notebook remembers what ran, not what the page shows: a cell run twice, or out of order, gives another answer.

1. Run only the loop's cell of section 9 again (click it, `Shift+Enter`),
   then the cell `count, total / count`. Its number beside it is now
   higher than the others.

    ```text
    (175104, 7.159965506213419)
    ```

    Twice the hours: the loop added to the sum and count of the first run.
    The mean barely changed, so the mistake is easy to miss.

2. **Kernel** > **Restart Kernel and Run All Cells...** > **Restart**. The
   kernel, the Python behind the notebook, forgets everything; the cells
   run from the top, numbered 1, 2, 3, …

    ```text
    (87552, 7.15996550621346)
    ```

3. Save (`Ctrl+S`). Stop JupyterLab: **File** > **Shut Down** >
   **Shut Down**. The terminal's prompt comes back.

**Check:** after **Run All**, the cells numbered in order from the top and
`87552` again.

!!! question "Task: the mean of each year"
    In a new cell of `explore.ipynb`, the mean temperature of each year,
    without the `-999` hours, with two decimals. Which year was the
    warmest? Start JupyterLab again with `jupyter lab` and open the
    notebook.

??? success "Answer"
    Two dictionaries with the year as key: one for the sums, one for the
    counts.

    ```python
    sums = {}
    counts = {}
    for line in lines[1:]:
        year = line[:4]
        temp = float(line.split(",")[1])
        if temp == -999:
            continue
        sums[year] = sums.get(year, 0.0) + temp
        counts[year] = counts.get(year, 0) + 1

    for year in sums:
        print(year, f"{sums[year] / counts[year]:.2f}")
    ```

    ```text
    2016 7.60
    2017 6.51
    2018 7.97
    2019 7.27
    2020 6.83
    2021 7.25
    2022 6.60
    2023 8.31
    2024 7.27
    2025 5.98
    ```

    The warmest year is 2023, the coldest 2025.

---

## Part 3 · An editor that runs code { #part-3 }

<!-- 1:55 to 2:30 -->

An editor keeps the code in a `.py` file and runs it with one key; a script runs the same way every time.

Further reading: [IDLE](https://docs.python.org/3/library/idle.html);
[The Python Tutorial, chapter 8: errors](https://docs.python.org/3/tutorial/errors.html).

---

### 12. IDLE, the editor that comes with Python { #idle }

<!-- 1:55 · 10 min -->

IDLE comes with every Python: a prompt, an editor and a Run key. It shows what an IDE is.

1. Start it, with `(s05)` in the prompt. A window **IDLE Shell
   3.14.8** opens: the `>>>` of Part 1, with colours.

    ```text
    $ python -m idlelib
    ```

2. In the IDLE Shell, try one line.

    ```pycon
    >>> 7.16 * 9 / 5 + 32
    44.888
    ```

3. **File** > **New File**. Type three lines.

    ```python
    days = 365 * 10 + 3
    hours = days * 24
    print(hours)
    ```

4. A folder for the scripts: in VS Code's terminal, `mkdir scripts`.
   Then in IDLE **File** > **Save As...**, go to `weather-s05`, then
   `scripts`, name it `hours.py`, **Save**.
5. **Run** > **Run Module** (`F5`). The Shell prints a line with
   `RESTART` and the file's path, then the result:

    ```text
    87672
    ```

    In a file only `print` shows a value; at `>>>` every value is shown.

6. Close both IDLE windows.

**Check:** `scripts/hours.py` in VS Code's Explorer, and `87672` printed
by `F5`.

---

### 13. VS Code: a script for the mean { #script }

<!-- 2:05 · 10 min -->

VS Code is the editor of the course; its Python extension runs a file with the environment's Python.

1. **Extensions** (`Ctrl+Shift+X`, macOS `Cmd+Shift+X`), type `python`,
   click **Python** by Microsoft, **Install**.
2. `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), type **Python: Select
   Interpreter**, `Enter`, pick the entry **s05** (its path contains
   `envs/s05`). The Status Bar, bottom right, shows `3.14.8`.
3. In the Explorer, right-click `scripts` > **New File...**, type
   `mean_temp.py`, `Enter`. Type the notebook's cells as one program, and
   save. The script runs in the project folder, so the path has no `..`.

    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    total = 0.0
    count = 0
    for line in lines[1:]:
        temp = float(line.split(",")[1])
        if temp == -999:
            continue
        total = total + temp
        count = count + 1

    print(f"{count} hours, mean {total / count:.2f} °C")
    ```

4. Run it with the ▶ at the top right of the editor: VS Code types the
   full path of Python and of the file into the terminal. Then run it by
   hand, the line that goes into a README:

    ```text
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    ```

**Check:** `87552 hours, mean 7.16 °C`, from the ▶ and from the typed
line.

!!! warning "`FileNotFoundError: ... 'data/raw/weather.csv'`"
    The terminal is not in the project folder: `cd ~/weather-s05`,
    then run again.

---

### 14. Repair a script with the debugger { #debug }

<!-- 2:15 · 15 min -->

`coldest_hour.py` should print the coldest hour of the ten years. It has two bugs: one Python reports, one it cannot see.

1. Download it into `scripts`, as the weather log in section 7.

    ```text
    $ curl -sSL -o scripts/coldest_hour.py https://github.com/MindaugasSarpis/weather-project/releases/download/seminar-files/coldest_hour.py
    $ ls scripts
    coldest_hour.py  hours.py  mean_temp.py
    ```

2. Open `scripts/coldest_hour.py` and run it. An error message, a
   **traceback**, is read from the bottom: the last line says what, the
   lines above it where.

    ```text
    $ python scripts/coldest_hour.py
    Traceback (most recent call last):
      File "/Users/smilte/weather-s05/scripts/coldest_hour.py", line 13, in <module>
        print(f"coldest hour: {coldest_tme}, {coldest} °C")
                               ^^^^^^^^^^^
    NameError: name 'coldest_tme' is not defined. Did you mean: 'coldest_time'?
    ```

3. `Ctrl+click` (macOS `Cmd+click`) the path: VS Code opens line 13.
   Change `coldest_tme` to `coldest_time`, save, run.

    ```text
    $ python scripts/coldest_hour.py
    coldest hour: 2019-07-22T00:00, -999.0 °C
    ```

    No message, and a temperature that cannot be.

4. A **breakpoint** stops the script at a line. Click left of line 10
   (a red dot), right-click it > **Edit Breakpoint...**, type
   `temp < -900`, `Enter`: it stops only when that is true.
5. `F5` > **Python Debugger** > **Python File**. The script stops on line
   10. In **Run and Debug**, **Variables** > **Locals**:

    ```text
    coldest: -16.0
    coldest_time: '2017-01-15T02:00'
    line: '2019-07-22T00:00,-999,76,3.2'
    parts: ['2019-07-22T00:00', '-999', '76', '3.2']
    temp: -999.0
    ```

    The first `-999` beats every real temperature.

6. `Shift+F5` stops the debugger. Click the red dot to remove it. Change
   line 9 so that `-999` never counts, save, run.

    ```python
        if temp != -999 and temp < coldest:
    ```

    ```text
    $ python scripts/coldest_hour.py
    coldest hour: 2025-01-07T05:00, -16.3 °C
    ```

**Check:** `-16.3 °C` on 7 January 2025.

!!! question "Task: the warmest hour"
    Copy `coldest_hour.py` to `scripts/warmest_hour.py` and change it to
    print the warmest hour. Does it need the `-999` check?

??? success "Answer"
    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    warmest = -100.0
    warmest_time = ""
    for line in lines[1:]:
        parts = line.split(",")
        temp = float(parts[1])
        if temp > warmest:
            warmest = temp
            warmest_time = parts[0]

    print(f"warmest hour: {warmest_time}, {warmest} °C")
    ```

    ```text
    $ python scripts/warmest_hour.py
    warmest hour: 2018-06-18T15:00, 32.4 °C
    ```

    No check: `-999` is never the largest. The start value `-100.0` must
    be below every real temperature.

---

## Part 4 · Functions, classes, modules { #part-4 }

<!-- 2:30 to 3:25 -->

Three scripts now repeat the same lines. A function writes a step once, a class keeps the values of one hour together, and a module holds both for every script.

Further reading: [The Python Tutorial, 4.8: defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions),
[chapter 9: classes](https://docs.python.org/3/tutorial/classes.html),
[chapter 6: modules](https://docs.python.org/3/tutorial/modules.html).

---

### 15. Write a step once: functions { #functions }

<!-- 2:30 · 10 min -->

`def` gives a few lines a name; `return` hands their result back to the line that called them.

1. `mean_temp.py`, `coldest_hour.py` and `warmest_hour.py` each read the
   file, cut a line and take its second value. Try one step as a function
   at `>>>` first. The block of a `def` ends with an empty line.

    ```pycon
    >>> def temp_of(line):
    ...     return float(line.split(",")[1])
    ...
    >>> temp_of("2016-01-01T00:00,-4.4,93,2.5")
    -4.4
    >>> temp_of("2016-01-01T01:00,-4.8,95,2.6")
    -4.8
    >>> def mean(values):
    ...     return sum(values) / len(values)
    ...
    >>> mean([-4.4, -4.8, -5.5, -6.0])
    -5.175
    ```

    `sum` is built in, like `len`. `mean` works on any list of numbers.

2. A name made inside a function is its own: it is gone when the
   function returns.

    ```pycon
    >>> def double(x):
    ...     result = 2 * x
    ...     return result
    ...
    >>> double(3.5)
    7.0
    >>> result
    Traceback (most recent call last):
      ...
    NameError: name 'result' is not defined
    >>> exit()
    ```

3. Rewrite `mean_temp.py` with three functions at the top. The text in
   three quotes under a `def` says what the function does.

    ```python
    def read_lines(path):
        """The lines of a file, without its header."""
        return open(path).read().splitlines()[1:]

    def temp_of(line):
        """The temp_c of one line of weather.csv."""
        return float(line.split(",")[1])

    def mean(values):
        """The mean of a list of numbers."""
        return sum(values) / len(values)

    temps = []
    for line in read_lines("data/raw/weather.csv"):
        temp = temp_of(line)
        if temp != -999:
            temps.append(temp)

    print(f"{len(temps)} hours, mean {mean(temps):.2f} °C")
    ```

4. Run it: the same result as before.

    ```text
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    ```

**Check:** `87552 hours, mean 7.16 °C` from the script with three `def`s.

---

### 16. One hour as an object: a class { #class }

<!-- 2:40 · 10 min -->

A **class** is a type of your own: its objects keep values together, and its methods are functions that belong to them.

1. At `>>>`, a class `Hour` made from one line of the file. `__init__`
   runs once when `Hour(...)` makes an object; `self` is that object, and
   `self.time = ...` keeps a value in it. Inside a class at `>>>`, leave no
   empty line between the two `def`s.

    ```pycon
    >>> class Hour:
    ...     def __init__(self, line):
    ...         parts = line.split(",")
    ...         self.time = parts[0]
    ...         self.temp = float(parts[1])
    ...     def is_missing(self):
    ...         return self.temp == -999
    ...
    >>> h = Hour("2016-01-01T00:00,-4.4,93,2.5")
    >>> h.time
    '2016-01-01T00:00'
    >>> h.temp
    -4.4
    >>> h.is_missing()
    False
    >>> Hour("2019-07-22T00:00,-999,76,3.2").is_missing()
    True
    >>> type(h)
    <class '__main__.Hour'>
    >>> exit()
    ```

    `is_missing` is a **method**: Python passes the object before the dot
    as `self`, as `line.split(",")` passes `line`.

2. Rewrite `coldest_hour.py` with the class. The coldest hour so far is
   an `Hour`, so its time stays with its temperature. `not` turns `True`
   into `False`; `and` is true when both sides are.

    ```python
    class Hour:
        """One line of weather.csv: its time and temperature."""

        def __init__(self, line):
            parts = line.split(",")
            self.time = parts[0]
            self.temp = float(parts[1])

        def is_missing(self):
            return self.temp == -999

    lines = open("data/raw/weather.csv").read().splitlines()[1:]

    coldest = Hour(lines[0])
    for line in lines[1:]:
        h = Hour(line)
        if not h.is_missing() and h.temp < coldest.temp:
            coldest = h

    print(f"coldest hour: {coldest.time}, {coldest.temp} °C")
    ```

3. Run it.

    ```text
    $ python scripts/coldest_hour.py
    coldest hour: 2025-01-07T05:00, -16.3 °C
    ```

**Check:** `-16.3 °C` on 7 January 2025, from the script with `class Hour`.

---

### 17. A module for every script { #module }

<!-- 2:50 · 15 min -->

A **module** is a `.py` file of definitions; `import` runs it once and gives the script its names.

1. New file `scripts/weather.py`: the functions and the class, once.
   It asks no question and prints nothing. `MISSING` gives the mark a
   name, in capitals because it never changes.

    ```python
    """Read the hourly log of the weather station."""

    MISSING = -999.0

    def read_lines(path):
        """The lines of a file, without its header."""
        return open(path).read().splitlines()[1:]

    class Hour:
        """One line of weather.csv: its time and temperature."""

        def __init__(self, line):
            parts = line.split(",")
            self.time = parts[0]
            self.temp = float(parts[1])

        def is_missing(self):
            return self.temp == MISSING

    def mean(values):
        """The mean of a list of numbers."""
        return sum(values) / len(values)
    ```

2. Replace `mean_temp.py` with a script that imports it. `import weather`
   finds `weather.py` in the script's folder; its names are then used
   with `weather.` in front.

    ```python
    import weather

    temps = []
    for line in weather.read_lines("data/raw/weather.csv"):
        h = weather.Hour(line)
        if not h.is_missing():
            temps.append(h.temp)

    print(f"{len(temps)} hours, mean {weather.mean(temps):.2f} °C")
    ```

3. Replace `coldest_hour.py` the same way: the class goes, the import
   comes.

    ```python
    import weather

    lines = weather.read_lines("data/raw/weather.csv")

    coldest = weather.Hour(lines[0])
    for line in lines[1:]:
        h = weather.Hour(line)
        if not h.is_missing() and h.temp < coldest.temp:
            coldest = h

    print(f"coldest hour: {coldest.time}, {coldest.temp} °C")
    ```

4. Run both: the same results, from one module.

    ```text
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    $ python scripts/coldest_hour.py
    coldest hour: 2025-01-07T05:00, -16.3 °C
    $ ls scripts/__pycache__
    weather.cpython-314.pyc
    ```

    The new folder `scripts/__pycache__` holds `weather.py` translated for
    Python 3.14, to start faster next time. Python makes it again when it
    is missing.

5. Python looks for a module in the folder of the script it runs, and at
   `>>>` in the folder of the terminal. From the project folder,
   `weather` is not found; from `scripts` it is, and `from ... import`
   takes one name out of it.

    ```text
    $ python
    >>> import weather
    Traceback (most recent call last):
      ...
    ModuleNotFoundError: No module named 'weather'
    >>> exit()
    $ cd scripts
    $ python
    >>> from weather import Hour
    >>> Hour("2016-01-01T00:00,-4.4,93,2.5").temp
    -4.4
    >>> exit()
    $ cd ..
    ```

**Check:** both scripts start with `import weather`, define nothing
themselves, and print 7.16 and −16.3.

!!! question "Task: the mean wind"
    Give `Hour` a third value, `self.wind`, the fourth part of the line
    (`wind_ms`), and write `scripts/mean_wind.py`: the mean wind of all
    hours with two decimals, from `weather.Hour` and `weather.mean`. The
    wind has no `-999`. Does `mean_temp.py` still run?

??? success "Answer"
    In `weather.py`, one line more in `__init__`:

    ```python
            self.wind = float(parts[3])
    ```

    `scripts/mean_wind.py`:

    ```python
    import weather

    winds = []
    for line in weather.read_lines("data/raw/weather.csv"):
        winds.append(weather.Hour(line).wind)

    print(f"{len(winds)} hours, mean wind {weather.mean(winds):.2f} m/s")
    ```

    ```text
    $ python scripts/mean_wind.py
    87672 hours, mean wind 3.50 m/s
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    ```

    One edit in the module, and every script that imports it has the wind.

!!! question "Task: the warmest hour, with the module"
    Rewrite `warmest_hour.py` of section 14 so that it imports `weather`
    and defines nothing itself.

??? success "Answer"
    ```python
    import weather

    lines = weather.read_lines("data/raw/weather.csv")

    warmest = weather.Hour(lines[0])
    for line in lines[1:]:
        h = weather.Hour(line)
        if h.temp > warmest.temp:
            warmest = h

    print(f"warmest hour: {warmest.time}, {warmest.temp} °C")
    ```

    ```text
    $ python scripts/warmest_hour.py
    warmest hour: 2018-06-18T15:00, 32.4 °C
    ```

---

### 18. The standard library: the temperature now { #stdlib }

<!-- 3:05 · 10 min -->

Python comes with about 200 modules, the **standard library**: no install needed.

1. Two of them at `>>>`: `math` and `statistics`.

    ```pycon
    >>> import math
    >>> math.sqrt(87672)
    296.09457948432623
    >>> import statistics
    >>> statistics.mean([-4.4, -4.8, -5.5, -6.0])
    -5.175
    >>> exit()
    ```

2. New file `scripts/now.py`: it asks the free weather service
   Open-Meteo for Vilnius now. `urllib.request` downloads, `json` turns
   the answer into Python objects.

    ```python
    import json
    import urllib.request

    URL = ("https://api.open-meteo.com/v1/forecast"
           "?latitude=54.69&longitude=25.28&current=temperature_2m,wind_speed_10m")

    with urllib.request.urlopen(URL) as response:
        data = json.load(response)

    print(type(data))
    print(data["current"])
    print(f"Vilnius now: {data['current']['temperature_2m']} °C")
    ```

    `with` closes the connection at the end of its block.

3. Run it. The answer is a dictionary with dictionaries inside; two keys
   in a row reach the temperature.

    ```text
    $ python scripts/now.py
    <class 'dict'>
    {'time': '2026-10-18T10:30', 'interval': 900, 'temperature_2m': 8.7, 'wind_speed_10m': 10.4}
    Vilnius now: 8.7 °C
    ```

    Your time and numbers differ: they are today's. The time is in UTC.

**Check:** `Vilnius now:` and a temperature that fits the window.

---

### 19. Write the environment down { #environment }

<!-- 3:15 · 5 min -->

A package from conda lives in the environment's folder. `environment.yml` lists what the project asked for, so another laptop can make the same environment.

1. Where a module comes from: `__file__` is its file. `json` is part of
   the environment's Python.

    === "macOS"

        ```text
        $ python -c "import json; print(json.__file__)"
        /Users/smilte/miniforge3/envs/s05/lib/python3.14/json/__init__.py
        ```

    === "Windows"

        ```text
        $ python -c "import json; print(json.__file__)"
        C:\Users\smilte\miniforge3\envs\s05\Lib\json\__init__.py
        ```

2. JupyterLab came from conda into this environment; NumPy is not
   installed (Seminar 7 adds it).

    ```text
    $ python -c "import jupyterlab; print(jupyterlab.__version__)"
    4.6.4
    $ python -c "import numpy"
    ...
    ModuleNotFoundError: No module named 'numpy'
    ```

3. Write the environment down. `--from-history` writes only what was
   asked for, not all 140 packages.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

4. Open `environment.yml`, delete the last line, `prefix: ...` (it names
   a folder on this laptop), save.

    ```text
    $ cat environment.yml
    name: s05
    channels:
      - conda-forge
    dependencies:
      - jupyterlab=4.6
      - python=3.14
    ```

5. A `README.md` says what the folder is and what came out. New file
   `README.md` in the folder, type four lines, save.

    ```text
    # Weather station, Seminar 5

    The mean, `python scripts/mean_temp.py`: 7.16 °C over 87 552 hours.
    The coldest hour, `python scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.
    ```

**Check:** `environment.yml` with two dependencies, and a `README.md` with
the two results.

---

### 20. Wrap up { #wrap-up }

<!-- 3:20 · 5 min -->


| Where | Good for | Start |
|--|--|--|
| the interpreter | one line, a quick question | `python`, then `exit()` |
| a notebook | trying step by step, output kept beside the code | `jupyter lab` |
| an editor (IDLE, VS Code) | a program in a file, the debugger | `python -m idlelib`, `code .` |
| a script | the same result every time, from one line | `python scripts/mean_temp.py` |

| To | Type |
|--|--|
| switch the environment on | `conda activate s05` |
| cut a line, convert a part | `line.split(",")`, `float(parts[1])` |
| repeat, decide | `for line in lines[1:]:`, `if temp == -999:` |
| count by key | `hours[year] = hours.get(year, 0) + 1` |
| print with decimals | `f"{mean:.2f}"` |
| write a step once | `def mean(values):` … `return sum(values) / len(values)` |
| keep the values of one hour together | `class Hour:`, `h = Hour(line)`, `h.temp`, `h.is_missing()` |
| use a module | `import weather`, `weather.Hour(line)` |
| write the environment down | `conda env export --from-history -f environment.yml` |

The files of today: `data/raw/weather.csv`, `notebooks/explore.ipynb`,
`scripts/hours.py`, the module `weather.py` and the scripts that import it,
`mean_temp.py`, `coldest_hour.py` (repaired, then rewritten) and
`mean_wind.py`; `now.py`, `environment.yml`, `README.md`.

---

## Optional, if the room goes fast { #optional }

---

### 21. The mean in two lines { #comprehension }

<!-- — · 5 min -->

A **list comprehension** builds a list in one line, with an `if` to filter.

1. In a new cell of `explore.ipynb` (or at the end of a script):

    ```python
    temps = [float(line.split(",")[1]) for line in lines[1:]]
    valid = [t for t in temps if t != -999]
    len(temps), len(valid), min(valid), max(valid)
    ```

    ```text
    (87672, 87552, -16.3, 32.4)
    ```

2. The mean, with five decimals.

    ```python
    f"{sum(valid) / len(valid):.5f}"
    ```

    ```text
    '7.15997'
    ```

**Check:** the same mean as the loop of section 9.

---

### 22. Write the result into a file { #write }

<!-- — · 5 min -->

`open(path, "w")` opens a file for writing; `with` closes it at the end of the block.

1. A folder for results, in the terminal: `mkdir results`. Then at the
   end of `mean_temp.py`, add three lines, save, run.

    ```python
    with open("results/mean_temp.txt", "w") as out:
        out.write(f"{len(temps)} hours\n")
        out.write(f"mean {weather.mean(temps):.5f} °C\n")
    ```

    ```text
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    $ cat results/mean_temp.txt
    87552 hours
    mean 7.15997 °C
    ```

    `\n` ends a line.

**Check:** `results/mean_temp.txt` with two lines.

---

### 23. A module that is also a script { #main }

<!-- — · 5 min -->

When a file runs as a script, its `__name__` is `"__main__"`; when it is imported, its module name.

1. At the end of `weather.py`, add two lines, save.

    ```python
    if __name__ == "__main__":
        print(Hour("2016-01-01T00:00,-4.4,93,2.5").temp)
    ```

2. Run `weather.py` itself, then `mean_temp.py`, which imports it.

    ```text
    $ python scripts/weather.py
    -4.4
    $ python scripts/mean_temp.py
    87552 hours, mean 7.16 °C
    ```

    The check runs only when `weather.py` is the script.

**Check:** `-4.4` from `weather.py`, and no `-4.4` from `mean_temp.py`.

---

### 24. Advanced tasks { #advanced }

<!-- — · 30 min -->

Four harder tasks for whoever is done early, each solved with what today showed; the answers are folded.

!!! question "Advanced task: the longest frost"
    The most hours in a row below 0 °C, and when that frost began. A loop
    that remembers the length of the current run. Mind the `-999` hours:
    they are below 0 too.

??? success "Answer"
    `scripts/longest_frost.py`:

    ```python
    import weather

    run = 0                 # hours below 0 °C in a row, up to this line
    run_start = ""
    longest = 0
    longest_start = ""
    for line in weather.read_lines("data/raw/weather.csv"):
        h = weather.Hour(line)
        if h.temp < 0 and not h.is_missing():
            if run == 0:
                run_start = h.time
            run = run + 1
            if run > longest:
                longest = run
                longest_start = run_start
        else:
            run = 0

    print(f"longest frost: {longest} hours ({longest / 24:.1f} days) from {longest_start}")
    ```

    ```text
    $ python scripts/longest_frost.py
    longest frost: 1172 hours (48.8 days) from 2024-12-31T16:00
    ```

    Without `not h.is_missing()`, the 120 marked hours of July 2019
    would count as a frost of five days in summer.

!!! question "Advanced task: the column from the command line"
    A script `scripts/column_mean.py` that takes the name of a column when
    it is started, `python scripts/column_mean.py wind_ms`, and prints its
    mean without the `-999` values. A wrong name or no name should print a
    short message, not a traceback. `sys.argv` is the list of words of the
    command line: `sys.argv[1]` is the first word after the script.

??? success "Answer"
    `sys.exit("text")` prints the text and ends the script with exit
    status 1.

    ```python
    import sys

    PATH = "data/raw/weather.csv"

    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/column_mean.py COLUMN")
    column = sys.argv[1]

    lines = open(PATH).read().splitlines()
    header = lines[0].split(",")
    if column not in header:
        sys.exit(f"no column {column!r}; the columns are {', '.join(header[1:])}")
    i = header.index(column)

    values = [float(line.split(",")[i]) for line in lines[1:]]
    valid = [v for v in values if v != -999]
    print(f"{column}: {len(valid)} values, mean {sum(valid) / len(valid):.2f}")
    ```

    ```text
    $ python scripts/column_mean.py temp_c
    temp_c: 87552 values, mean 7.16
    $ python scripts/column_mean.py humidity_pct
    humidity_pct: 87672 values, mean 79.10
    $ python scripts/column_mean.py rain_mm
    no column 'rain_mm'; the columns are temp_c, humidity_pct, wind_ms
    $ python scripts/column_mean.py
    usage: python scripts/column_mean.py COLUMN
    ```

!!! question "Advanced task: tomorrow against ten years"
    Ask Open-Meteo for the hourly forecast of tomorrow (add
    `&hourly=temperature_2m&forecast_days=2` to the address instead of
    `&current=...`) and compare its mean with the station's mean of the
    same date over 2016 to 2025. Is tomorrow warmer than usual?

??? success "Answer"
    `data["hourly"]` holds two lists of 48 values, `time` and
    `temperature_2m`; `zip` walks through both together.

    ```python
    import json
    import urllib.request

    import weather

    URL = ("https://api.open-meteo.com/v1/forecast"
           "?latitude=54.69&longitude=25.28&hourly=temperature_2m&forecast_days=2")

    with urllib.request.urlopen(URL) as response:
        data = json.load(response)

    times = data["hourly"]["time"]           # '2026-10-18T00:00', ... 48 hours
    temps = data["hourly"]["temperature_2m"]
    tomorrow = times[24][:10]                # the date of hour 24
    forecast = [t for when, t in zip(times, temps) if when.startswith(tomorrow)]

    day = tomorrow[5:]                       # '10-19': month and day
    station = []
    for line in weather.read_lines("data/raw/weather.csv"):
        h = weather.Hour(line)
        if h.time[5:10] == day and not h.is_missing():
            station.append(h.temp)

    print(f"{tomorrow}: forecast mean {sum(forecast) / len(forecast):.1f} °C "
          f"from {len(forecast)} hours")
    print(f"{day} in 2016-2025: mean {sum(station) / len(station):.1f} °C "
          f"from {len(station)} hours")
    ```

    ```text
    $ python scripts/tomorrow.py
    2026-10-19: forecast mean 7.1 °C from 24 hours
    10-19 in 2016-2025: mean 5.8 °C from 240 hours
    ```

    Run on 18 October; your date and numbers differ. 240 hours: ten years
    of 24 hours. The forecast is in UTC, as is the station's log.

!!! question "Advanced task: a check that 7.16 stays 7.16"
    Add a function `mean_valid(values)` to `weather.py` (the mean without
    `MISSING`), and a script `scripts/check_weather.py` that checks
    `Hour`, `mean_valid` on a short list whose mean you know, and the
    mean of the whole file. `assert condition` does nothing when the
    condition is true and stops with `AssertionError` when it is false.
    Then break `mean_valid` on purpose and run the checks again.

??? success "Answer"
    In `weather.py`:

    ```python
    def mean_valid(values):
        """The mean of the values that are not MISSING."""
        valid = [v for v in values if v != MISSING]
        return sum(valid) / len(valid)
    ```

    `scripts/check_weather.py`:

    ```python
    """Checks of weather.py: run with  python scripts/check_weather.py"""
    import weather

    assert weather.Hour("2016-01-01T00:00,-4.4,93,2.5").temp == -4.4
    assert weather.mean_valid([1.0, -999.0, 3.0]) == 2.0

    temps = [weather.Hour(line).temp for line in weather.read_lines("data/raw/weather.csv")]
    mean = weather.mean_valid(temps)
    assert abs(mean - 7.16) < 0.005, mean

    print(f"3 checks passed, mean {mean:.5f} °C")
    ```

    ```text
    $ python scripts/check_weather.py
    3 checks passed, mean 7.15997 °C
    ```

    With `valid = list(values)` in `mean_valid` (the `-999` check gone):

    ```text
    $ python scripts/check_weather.py
    Traceback (most recent call last):
      File ".../scripts/check_weather.py", line 5, in <module>
        assert weather.mean_valid([1.0, -999.0, 3.0]) == 2.0
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
    ```

    The short list catches the mistake before the whole file is read.
    Seminar 13 runs such checks with `pytest`.

---

## Aims practised

- ♻️ **Reproducibility:** the 7.16 of the README comes out of a script and
  a notebook each student typed, and `environment.yml` says which Python
  and packages they need.
- 🔧 **Tool-agnostic:** the same Python in the interpreter, a notebook,
  IDLE and VS Code, on macOS and Windows.
- ⚙️ **Automation:** a loop does for 87 672 lines what was done by hand
  for one, and `now.py` asks a weather service without a browser.
