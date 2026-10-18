# Seminar 7 · NumPy

**Paired lecture:** 07 Python for Data & NumPy · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Is it getting warmer?

**Today's goal:** every student makes today's conda environment from the
folder's `environment.yml`, adds NumPy to it and to the file; reads
`weather.csv` with functions and then as one NumPy array; finds the coldest
day and the mean of each year, and writes the answer to a file.

Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both). In the blocks, a line that starts with `$` is typed in the
terminal, a line that starts with `>>>` is typed at Python's prompt, and
every other line is what comes back; `...` stands for lines left out.

**If time runs short:** stop after section 12; sections 14 to 17 are optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the download and
      for conda (Python about 30 MB, NumPy about 9 MB, less when conda has
      them already). Nothing from earlier seminars is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** if you made `s07` before, remove it (`conda env remove -n
      s07`) to make it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · An environment for the project { #part-1 }

<!-- 0:00 to 0:25 -->

NumPy is not part of Python. It goes into the project's environment, and into the file that lists it.

Further reading: [conda, Managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the scripts that come with it and `environment.yml`, the list from which conda makes today's environment.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s07.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s07.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s07.zip
       creating: /Users/smilte/weather-s07/
    ...
      inflating: /Users/smilte/weather-s07/scripts/rebuild.sh
    $ cd ~/weather-s07
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s07 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s07` > **Open**. The terminal
   now starts in it.
3. The list for today's environment: a name, where packages come from,
   and what goes in. Only Python, so far.

    ```text
    $ cat environment.yml
    name: s07
    channels:
      - conda-forge
    dependencies:
      - python=3.14
    ```

4. Make the environment from it. A **conda environment** is a folder with
   its own Python and packages, here `miniforge3/envs/s07`.

    ```text
    $ conda env create -n s07 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s07
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. Switch it on: the prompt starts with `(s07)`, and `python` is the
   environment's Python.

    ```text
    $ conda activate s07
    $ python --version
    Python 3.14.8
    ```

6. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/s07` in its path. The Status
   Bar, bottom right, shows `3.14.8` and `s07`; a new terminal starts with
   `(s07)`.

**Check:** `(s07)` at the start of the prompt, `s07` in the Status Bar.

---

### 2. Add NumPy to the environment { #install }

<!-- 0:10 · 5 min -->

Activating an environment puts its folder first on `PATH`; `conda install` adds a package to the active one.

1. NumPy is not in it yet.

    ```text
    $ python -c "import numpy"
    ModuleNotFoundError: No module named 'numpy'
    ```

2. Install it, with the version written in. conda shows its plan, then a
   list of packages:

    ```text
    $ conda install numpy=2.5
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/s07

      added / updated specs:
        - numpy=2.5
    ```

3. At `Proceed ([y]/n)?` press `Enter`. It ends with `done`. Ask for the
   version.

    ```text
    $ python -c "import numpy; print(numpy.__version__)"
    2.5.4
    ```

**Check:** `2.5.4`, with `(s07)` in the prompt.

!!! warning "`ModuleNotFoundError` after the install"
    The prompt says `(base)`: `conda activate s07`, then again.

---

### 3. Write it down: `environment.yml` { #yml }

<!-- 0:15 · 10 min -->

The file lists what was asked for; any laptop makes the same environment from it. NumPy goes in too.

1. Export what was asked for, over the file from the zip.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

2. Open `environment.yml`. NumPy is the new last dependency.

    ```text
    name: s07
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - numpy=2.5
    prefix: /Users/smilte/miniforge3/envs/s07
    ```

3. Delete the last line, `prefix: ...`: it names a folder on this laptop.
   Save.

**Check:** `environment.yml` ends with `- numpy=2.5`.

!!! question "Task: does the file make the environment?"
    Make a second environment, `s07-check`, from `environment.yml`.
    Ask it for its NumPy version without activating it, then remove it.

??? success "Answer"
    ```text
    $ conda env create -n s07-check -f environment.yml
    ```

    It ends with `#     $ conda activate s07-check`. The packages come
    from conda's cache, so it takes a minute.

    ```text
    $ conda run -n s07-check python -c "import numpy; print(numpy.__version__)"
    2.5.4
    $ conda env remove -n s07-check
    ```

---

## Part 2 · Functions and the csv module { #part-2 }

<!-- 0:25 to 0:55 -->

A function gives a block of steps a name. Here the mean becomes a function, and the csv module reads the file.

Further reading: [The Python Tutorial, Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

---

### 4. A function for the mean { #function }

<!-- 0:25 · 10 min -->

`def` gives a block a name and inputs; `return` hands a value back.

1. New file `scripts/column_mean.py`. Type, save.

    ```python
    def mean_valid(values):
        """The mean of the values that are not -999."""
        valid = [v for v in values if v != -999]
        return sum(valid) / len(valid)

    print(mean_valid([1.0, -999, 3.0]))
    result = mean_valid([20.5, 21.5])
    print(result)
    ```

2. Run it.

    ```text
    $ python scripts/column_mean.py
    2.0
    21.0
    ```

    The `-999` of the first list is left out: (1 + 3) / 2.
    `[v for v in values if v != -999]` makes a new list of the values that
    are not −999: a **list comprehension**, a `for` and an `if` in one line.

**Check:** `2.0` and `21.0`.

---

### 5. A column with the csv module { #csv }

<!-- 0:35 · 10 min -->

`csv.reader` cuts every line into a list of strings; `with` closes the file at the end of the block.

1. At the top of the file, add one line.

    ```python
    import csv
    ```

2. Under `mean_valid`, add a second function.

    ```python
    def read_column(path, index):
        """One column of a CSV file with a header line, as floats."""
        values = []
        with open(path, newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            print(header)
            for row in reader:
                values.append(float(row[index]))
        return values
    ```

3. Replace the three lines at the bottom with these, save.

    ```python
    temp = read_column("data/raw/weather.csv", 1)
    print(len(temp), temp[:3])
    print(f"mean {mean_valid(temp):.5f} °C")
    ```

4. Run it.

    ```text
    $ python scripts/column_mean.py
    ['time', 'temp_c', 'humidity_pct', 'wind_ms']
    87672 [-4.4, -4.8, -5.5]
    mean 7.15997 °C
    ```

    `next(reader)` takes the header line; the loop gets the rest.

**Check:** `mean 7.15997 °C`, from two functions.

---

### 6. A path that works from any folder { #pathlib }

<!-- 0:45 · 10 min -->

A relative path starts at the terminal's folder, not at the script's.

1. Run the script from the folder `scripts`.

    ```text
    $ cd scripts
    $ python column_mean.py
    ...
      File "/Users/smilte/weather-s07/scripts/column_mean.py", line 13, in read_column
        with open(path, newline="") as f:
             ~~~~^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'data/raw/weather.csv'
    ```

2. Under `import csv`, add two lines.

    ```python
    from pathlib import Path

    ROOT = Path(__file__).resolve().parent.parent
    ```

    `__file__` is the script's path; two `.parent` up is the project folder.

3. In `read_column`, replace the two lines `header = next(reader)` and
   `print(header)` with one, `next(reader)`. Replace the three lines at the
   bottom with these, save.

    ```python
    print(ROOT)
    temp = read_column(ROOT / "data/raw/weather.csv", 1)
    print(f"mean {mean_valid(temp):.5f} °C")
    ```

4. Run it again from `scripts`, then go back.

    ```text
    $ python column_mean.py
    /Users/smilte/weather-s07
    mean 7.15997 °C
    $ cd ..
    ```

**Check:** the same mean from `scripts` and from the project folder.

!!! question "Task: humidity and wind"
    Add two lines to `column_mean.py` that print the mean of
    `humidity_pct` (column 2) and of `wind_ms` (column 3), with two decimals.

??? success "Answer"
    ```python
    print(f"humidity {mean_valid(read_column(ROOT / 'data/raw/weather.csv', 2)):.2f} %")
    print(f"wind {mean_valid(read_column(ROOT / 'data/raw/weather.csv', 3)):.2f} m/s")
    ```

    ```text
    humidity 79.10 %
    wind 3.50 m/s
    ```

    A name for the path, `path = ROOT / "data/raw/weather.csv"`, makes
    both lines shorter.

---

## Part 3 · The file as one array { #part-3 }

<!-- 0:55 to 1:25 -->

A NumPy array holds numbers of one type, and computes on all of them at once.

Further reading: [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html).

---

### 7. Arrays at the prompt, then the file into an array { #loadtxt }

<!-- 0:55 · 20 min -->

An **array** is a block of numbers of one type; arithmetic and comparisons work on every number at once. `np.loadtxt` reads a table of numbers into a two-dimensional array.

1. Start Python in the terminal (`python`), import NumPy under the short
   name `np`, and make an array from a list of four hours. Every element is
   a `float64`; `shape` says how many there are.

    ```pycon
    >>> import numpy as np
    >>> temps = [-4.4, -4.8, -999.0, -5.5]
    >>> a = np.array(temps)
    >>> a
    array([  -4.4,   -4.8, -999. ,   -5.5])
    >>> a.dtype
    dtype('float64')
    >>> a.shape
    (4,)
    ```

2. Arithmetic on an array works on each element. On a list, `*` repeats
   the list instead.

    ```pycon
    >>> a * 9 / 5 + 32
    array([   24.08,    23.36, -1766.2 ,    22.1 ])
    >>> temps * 2
    [-4.4, -4.8, -999.0, -5.5, -4.4, -4.8, -999.0, -5.5]
    >>> a * 2
    array([   -8.8,    -9.6, -1998. ,   -11. ])
    ```

3. A comparison gives an array of `True` and `False`, a **mask**. An array
   indexed with a mask keeps the elements where the mask is `True`.

    ```pycon
    >>> a != -999
    array([ True,  True, False,  True])
    >>> a[a != -999]
    array([-4.4, -4.8, -5.5])
    >>> a[a != -999].mean()
    np.float64(-4.8999999999999995)
    ```

    `np.float64` is NumPy's float; the tail is the float rounding of any
    sum, (−4.4 − 4.8 − 5.5) / 3 = −4.9.

4. An array can have rows and columns. `axis=1` works along each row,
   `axis=0` down each column. Then leave Python.

    ```pycon
    >>> b = np.array([[1, 2, 3], [4, 5, 6]])
    >>> b.shape
    (2, 3)
    >>> b.mean(axis=1)
    array([2., 5.])
    >>> b.mean(axis=0)
    array([2.5, 3.5, 4.5])
    >>> exit()
    ```

5. Now the file. New file `scripts/coldest_day.py`. Type, save.

    ```python
    from pathlib import Path

    import numpy as np

    ROOT = Path(__file__).resolve().parent.parent
    path = ROOT / "data/raw/weather.csv"

    data = np.loadtxt(path, delimiter=",", skiprows=1, usecols=(1, 2, 3))
    print(data.shape, data.dtype)
    print(data[0])
    print(data[:3, 0])
    ```

6. Run it.

    ```text
    $ python scripts/coldest_day.py
    (87672, 3) float64
    [-4.4 93.   2.5]
    [-4.4 -4.8 -5.5]
    ```

    87 672 rows, 3 columns. `data[0]` is the first row; `data[:3, 0]` the
    first three rows of column 0, `temp_c`.

**Check:** `(87672, 3) float64`.

!!! warning "`ValueError: could not convert string '2016-01-01T00:00' to float64`"
    `usecols` is missing: the time column is not a number.

---

### 8. A mask for `-999` { #mask }

<!-- 1:05 · 10 min -->

The mask of section 7, on the whole column of 87 672 temperatures.

1. At the end of the file, add these lines, save.

    ```python
    temp = data[:, 0]
    valid = temp != -999
    print(valid[:3], valid.sum(), (~valid).sum())
    print(f"all rows   {temp.mean():.5f}")
    print(f"valid rows {temp[valid].mean():.5f}")
    ```

2. Run it.

    ```text
    $ python scripts/coldest_day.py
    ...
    [ True  True  True] 87552 120
    all rows   5.78280
    valid rows 7.15997
    ```

    `sum` counts the `True`; `~` turns the mask round.

**Check:** 120 rows of `-999`, and 7.15997 without them.

---

### 9. One row per day: `reshape` { #reshape }

<!-- 1:15 · 10 min -->

87 672 hours are 3653 days of 24 hours; `reshape` cuts the column into those rows.

1. Add these lines, save.

    ```python
    days = temp.reshape(3653, 24)
    day_means = days.mean(axis=1)
    print(days.shape, day_means[:3])
    dates = np.arange("2016-01-01", "2026-01-01", dtype="datetime64[D]")
    print(dates[:2], dates[-1])
    ```

2. Run it.

    ```text
    $ python scripts/coldest_day.py
    ...
    (3653, 24) [-4.87083333 -5.13333333 -3.14166667]
    ['2016-01-01' '2016-01-02'] 2025-12-31
    ```

    `axis=1` averages along each row: one mean per day. `dates` holds the
    3653 days, in the same order.

3. The sensor failure covers whole days, so their mean is exactly `-999`.
   Add a mask for the days, then the coldest day.

    ```python
    ok = day_means != -999
    print(ok.sum(), dates[~ok])
    i = day_means[ok].argmin()
    print("coldest day", dates[ok][i], f"{day_means[ok][i]:.2f}")
    ```

4. Run it.

    ```text
    $ python scripts/coldest_day.py
    ...
    3648 ['2019-07-22' '2019-07-23' '2019-07-24' '2019-07-25' '2019-07-26']
    coldest day 2019-01-26 -13.00
    ```

    `argmin` gives the position of the smallest value. The same mask on
    `dates` keeps the days in step.

**Check:** `coldest day 2019-01-26 -13.00`.

!!! question "Task: the warmest day, and the frost days"
    Add lines that print the warmest day and its mean, and the number of
    days whose mean is below 0 °C.

??? success "Answer"
    ```python
    j = day_means[ok].argmax()
    print("warmest day", dates[ok][j], f"{day_means[ok][j]:.2f}")
    print("days below 0 °C", (day_means[ok] < 0).sum())
    ```

    ```text
    warmest day 2018-06-18 26.93
    days below 0 °C 922
    ```

---

## Part 4 · Is it getting warmer? { #part-4 }

<!-- 1:25 to 2:00 -->

Ten years of the same station: compare the mean of each year.

---

### 10. The year of every row { #year }

<!-- 1:25 · 5 min -->

The year is the first four characters of `time`.

1. New file `scripts/yearly_means.py`. Type, save.

    ```python
    from pathlib import Path

    import numpy as np

    ROOT = Path(__file__).resolve().parent.parent
    path = ROOT / "data/raw/weather.csv"

    temp = np.loadtxt(path, delimiter=",", skiprows=1, usecols=1)
    time = np.loadtxt(path, delimiter=",", skiprows=1, usecols=0, dtype=str)
    valid = temp != -999
    year = np.array([int(t[:4]) for t in time])
    print(time[:2], year[:2], year[-2:])
    ```

2. Run it.

    ```text
    $ python scripts/yearly_means.py
    ['2016-01-01T00:00' '2016-01-01T01:00'] [2016 2016] [2025 2025]
    ```

**Check:** `2016` at the start, `2025` at the end.

---

### 11. A mean for each year { #yearly }

<!-- 1:30 · 10 min -->

`&` joins two masks: this year, and not `-999`.

1. Replace the `print` line with a loop, save.

    ```python
    for y in range(2016, 2026):
        m = (year == y) & valid
        print(y, f"{temp[m].mean():.2f}", m.sum())
    ```

2. Run it.

    ```text
    $ python scripts/yearly_means.py
    2016 7.60 8784
    2017 6.51 8760
    2018 7.97 8760
    2019 7.27 8640
    2020 6.83 8784
    2021 7.25 8760
    2022 6.60 8760
    2023 8.31 8760
    2024 7.27 8784
    2025 5.98 8760
    ```

3. Read it: the years go up and down by up to 2.3 °C, in no order. 2019
   has 120 hours fewer, the five summer days of the failure.

**Check:** ten means between 5.98 and 8.31.

---

### 12. Write the answer to a file { #commit }

<!-- 1:40 · 15 min -->

The script writes its answer to `results/`, and writes it again, the same, at every run.

1. Replace the loop with these lines, save.

    ```python
    lines = []
    for y in range(2016, 2026):
        m = (year == y) & valid
        lines.append(f"{y}  {temp[m].mean():.2f}  {m.sum()}")

    first = (year <= 2020) & valid
    last = (year >= 2021) & valid
    lines.append(f"2016-2020  {temp[first].mean():.2f}")
    lines.append(f"2021-2025  {temp[last].mean():.2f}")

    text = "\n".join(lines) + "\n"
    print(text, end="")
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "results/yearly_temp.txt").write_text(text)
    ```

2. Run it.

    ```text
    $ python scripts/yearly_means.py
    ...
    2016-2020  7.24
    2021-2025  7.08
    ```

    The answer: not warmer. The second five years are 0.16 °C colder,
    less than the step from one year to the next.

3. The file.

    ```text
    $ tail -n 2 results/yearly_temp.txt
    2016-2020  7.24
    2021-2025  7.08
    ```

**Check:** `results/yearly_temp.txt`, twelve lines: ten years and the two halves.

!!! question "Task: the warmest and the coldest month"
    Add the month of every row (`t[5:7]`) and print the mean temperature of
    each month over the ten years.

??? success "Answer"
    ```python
    month = np.array([int(t[5:7]) for t in time])
    for mo in range(1, 13):
        m = (month == mo) & valid
        print(mo, f"{temp[m].mean():.2f}")
    ```

    ```text
    1 -3.87
    2 -2.45
    3 1.19
    4 6.39
    5 12.16
    6 17.25
    7 18.53
    8 16.12
    9 13.01
    10 6.94
    11 2.64
    12 -2.30
    ```

    July is the warmest, 18.53 °C; January the coldest, −3.87 °C.

---

### 13. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->


| To | Type |
|--|--|
| make the environment of a folder | `conda env create -n s07 -f environment.yml` |
| switch it on | `conda activate s07` |
| add a package to it | `conda install numpy=2.5` |
| write it down | `conda env export --from-history -f environment.yml` |
| name a block of steps | `def name(inputs):` ... `return value` |
| read a CSV file | `csv.reader(f)`, `next(reader)` for the header |
| a path from the project folder | `Path(__file__).resolve().parent.parent` |
| an array from a list | `a = np.array(values)`, then `a * 2`, `a.mean()` |
| a table into an array | `np.loadtxt(path, delimiter=",", skiprows=1, usecols=...)` |
| select rows | `temp[temp != -999]`, masks joined with `&` |

---

## Optional, if the room goes fast { #optional }

---

### 14. Loop against array: time both { #timing }

<!-- — · 10 min -->

`time.perf_counter()` is a clock in seconds; the difference of two readings is the time between them.

1. New file `scripts/time_both.py`: the column once as an array and once
   as a plain list (`tolist`). Type, save.

    ```python
    import time

    import numpy as np

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",", skiprows=1, usecols=1)
    temps = temp.tolist()
    ```

2. Under them, the mean twice, each between two clock readings. Save.

    ```python
    t0 = time.perf_counter()
    total = 0.0
    count = 0
    for t in temps:
        if t != -999:
            total = total + t
            count = count + 1
    t1 = time.perf_counter()
    array_mean = temp[temp != -999].mean()
    t2 = time.perf_counter()

    print(f"loop  {total / count:.5f} in {(t1 - t0) * 1000:.1f} ms")
    print(f"array {array_mean:.5f} in {(t2 - t1) * 1000:.1f} ms")
    ```

3. Run it, twice.

    ```text
    $ python scripts/time_both.py
    loop  7.15997 in 6.2 ms
    array 7.15997 in 0.4 ms
    ```

    Your times differ.

**Check:** the same mean, the array about 15 times faster.

---

### 15. Count in bins: `np.histogram` { #histogram }

<!-- — · 5 min -->

A histogram counts the values that fall into each bin.

1. At the end of `coldest_day.py`, add these lines, save.

    ```python
    counts, edges = np.histogram(temp[valid], bins=np.arange(-20, 40, 5))
    print(edges)
    print(counts)
    ```

2. Run it.

    ```text
    $ python scripts/coldest_day.py
    ...
    [-20 -15 -10  -5   0   5  10  15  20  25  30  35]
    [   12   686  5589 16065 16582 14050 14880 12261  6111  1230    86]
    ```

    Twelve edges make eleven bins: 12 hours from −20 to −15 °C, 86 from
    30 to 35 °C.

**Check:** the counts add up to 87 552.

---

### 16. Skip a bad row: `try` and `except` { #except }

<!-- — · 10 min -->

`try` runs a block; if it raises the error named after `except`, that block runs instead.

1. New file `scripts/export_values.py`, for the spreadsheet export with
   `;` and decimal commas. Type, save.

    ```python
    import csv

    values = []
    with open("data/raw/daily_export.csv", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            try:
                nr = int(row[0])
            except ValueError:
                print("skipped:", row)
                continue
            values.append(float(row[2].replace(",", ".")))
    ```

2. At the end, two lines, not indented. Save, run.

    ```python
    print(len(values), values)
    print(f"mean {sum(values) / len(values):.2f}")
    ```

    ```text
    $ python scripts/export_values.py
    skipped: ['', 'mean', '7,97']
    9 [6.3, 5.0, 5.6, 7.0, 9.4, 10.4, 9.2, 9.0, 9.8]
    mean 7.97
    ```

    The last line of the export has no `nr`: `int('')` raises
    `ValueError`, and the row is skipped.

**Check:** nine values, the mean the spreadsheet wrote, 7.97.

### 17. Advanced tasks { #advanced }

<!-- — · 25 min -->

Harder questions on the same arrays, for a room that is done early. Each answer is folded under its task.

!!! question "Advanced task: a straight line through the ten years"
    `np.polyfit(x, y, 1)` fits a straight line and returns its slope and
    intercept. Fit one through the ten yearly means of `yearly_means.py`.
    How many °C per year is the slope, and is it large next to how much
    the years scatter (`means.std()`)?

??? success "Answer"
    At the end of `yearly_means.py`:

    ```python
    years = np.arange(2016, 2026)
    means = np.array([temp[(year == y) & valid].mean() for y in years])
    slope, intercept = np.polyfit(years, means, 1)
    print(f"slope {slope:.3f} °C per year")
    print(f"spread of the years {means.std():.2f} °C")
    ```

    ```text
    $ python scripts/yearly_means.py
    ...
    slope -0.056 °C per year
    spread of the years 0.67 °C
    ```

    −0.056 °C per year is 0.56 °C per decade, less than the 0.67 °C by
    which single years scatter: ten points cannot show a trend this small.

!!! question "Advanced task: the day's cycle in one line"
    `days` has one row per day and one column per hour. Which hour of the
    day is the coldest on average, and which the warmest?

??? success "Answer"
    `axis=0` averages down each column: one mean per hour. At the end of
    `coldest_day.py`:

    ```python
    hour_means = days[ok].mean(axis=0)
    print(np.round(hour_means, 1))
    print("coldest hour", hour_means.argmin(), "warmest hour", hour_means.argmax())
    ```

    ```text
    $ python scripts/coldest_day.py
    ...
    [ 4.7  4.1  3.8  3.7  3.8  4.1  4.7  5.4  6.2  7.2  8.1  8.9  9.6 10.2
     10.5 10.7 10.5 10.2  9.6  8.9  8.1  7.2  6.3  5.4]
    coldest hour 3 warmest hour 15
    ```

    03:00 and 15:00, 7 °C apart.

!!! question "Advanced task: the day with the largest swing"
    For each day, the warmest hour minus the coldest. Which day swung the
    most, and how much does a day swing on average?

??? success "Answer"
    ```python
    swing = days[ok].max(axis=1) - days[ok].min(axis=1)
    k = swing.argmax()
    print("largest swing", dates[ok][k], f"{swing[k]:.1f}", days[ok][k].min(), days[ok][k].max())
    print(f"mean swing {swing.mean():.1f}")
    ```

    ```text
    $ python scripts/coldest_day.py
    ...
    largest swing 2016-08-03 14.4 11.6 26.0
    mean swing 7.6
    ```

    3 August 2016: from 11.6 °C at night to 26.0 °C in the afternoon.

!!! question "Advanced task: the longest frost"
    The longest run of hours in a row below 0 °C: how long, and from when
    to when? A loop over the mask that counts the current run is enough.

??? success "Answer"
    New file `scripts/frost.py`:

    ```python
    import numpy as np

    path = "data/raw/weather.csv"
    temp = np.loadtxt(path, delimiter=",", skiprows=1, usecols=1)
    time = np.loadtxt(path, delimiter=",", skiprows=1, usecols=0, dtype=str)

    frost = (temp < 0) & (temp != -999)
    longest = 0
    run = 0
    for i in range(len(frost)):
        if frost[i]:
            run = run + 1
        else:
            run = 0
        if run > longest:
            longest = run
            end = i
    start = end - longest + 1
    print(longest, "hours,", time[start], "to", time[end])
    ```

    ```text
    $ python scripts/frost.py
    1172 hours, 2024-12-31T16:00 to 2025-02-18T11:00
    ```

    About 49 days without a thaw, in the winter of 2025.

---

## Aims practised

- ♻️ **Reproducibility:** `environment.yml` makes the same environment on
  any laptop; the answer is a file the script writes again at any time.
- 🔧 **Tool-agnostic:** the same `conda` and `python` lines on macOS and
  Windows; a path from `Path(__file__)` works from any folder.
- 📁 **Files:** the file read three ways (lines, csv, NumPy) to the same
  7.15997; made files go to `results/`, and the scripts make them again.
