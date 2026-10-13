# Seminar 7 — Is It Getting Warmer? Functions and NumPy on the Weather Project

**Paired lecture:** 07 Python for Data & NumPy · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student gives the project a conda environment with
NumPy, written down in `environment.yml`; reads `weather.csv` with
functions and then as one NumPy array; finds the coldest day and the mean
of each year; commits and pushes.

Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both).

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · An environment for the project** · 25 min | | |
| 0:00 | [1. Make the environment `weather`](#install) | `conda create -n weather python=3.14 numpy=2.5` | `(weather)` in the prompt |
| 0:10 | [2. VS Code uses it](#interpreter) | **Python: Select Interpreter** | `3.14.8` in the Status Bar |
| 0:15 | [3. Write it down: `environment.yml`](#yml) | `conda env export --from-history -f environment.yml` | the file committed |
| | **Part 2 · Functions and the csv module** · 30 min | | |
| 0:25 | [4. A function for the mean](#function) | `def mean_valid(values):` | `2.0` |
| 0:35 | [5. A column with the csv module](#csv) | `csv.reader(f)` | `mean 7.15997 °C` |
| 0:45 | [6. A path that works from any folder](#pathlib) | `Path(__file__)` | the same mean from `scripts` |
| | **Part 3 · The file as one array** · 30 min | | |
| 0:55 | [7. The file into an array](#loadtxt) | `np.loadtxt(...)` | `(87672, 3) float64` |
| 1:05 | [8. A mask for `-999`](#mask) | `valid = temp != -999` | `120`, `7.15997` |
| 1:15 | [9. One row per day: `reshape`](#reshape) | `temp.reshape(3653, 24)` | coldest day 2019-01-26 |
| | **Part 4 · Is it getting warmer?** · 35 min | | |
| 1:25 | [10. The year of every row](#year) | `int(t[:4])` | `[2016 2016] [2025 2025]` |
| 1:30 | [11. A mean for each year](#yearly) | `(year == y) & valid` | ten means, 5.98 to 8.31 |
| 1:40 | [12. Write the answer, commit, push](#commit) | `git push` | `results/yearly_temp.txt` |
| 1:55 | [13. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [14. Loop against array: time both](#timing) | `time.perf_counter()` | 6 ms against 0.4 ms |
| — | [15. Count in bins: `np.histogram`](#histogram) | `np.histogram(v, bins=...)` | eleven counts |
| — | [16. Skip a bad row: `try` and `except`](#except) | `except ValueError:` | the export's nine values |

**If time runs short:** stop after section 12; sections 14 to 16 are optional.

??? info "Before the session"
    - **Room:** the weather project as Seminar 6 left it, internet for
      conda (the environment downloads about 50 MB).
    - **You:** nothing to prepare. Delete your own `weather` environment
      first (`conda env remove -n weather`) to make it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · An environment for the project { #part-1 }

**0:00 to 0:25** · NumPy is not part of Python. It goes into an environment of the project's own.

---

### 1. Make the environment `weather` { #install }

**0:00 · 10 min** · An environment is a folder with its own Python and packages; activating it puts it first on `PATH`.

1. Open `weather-project` in VS Code, then the terminal. The prompt starts
   with `(base)`.
2. Make the environment, with the versions written in.

    ```text
    conda create -n weather python=3.14 numpy=2.5
    ```

    conda shows its plan, then a list of packages:

    ```text
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/weather

      added / updated specs:
        - numpy=2.5
        - python=3.14
    ```

3. At `Proceed ([y]/n)?` press `Enter`. It ends with:

    ```text
    #     $ conda activate weather
    ```

4. Switch it on. The prompt starts with `(weather)`.

    ```text
    conda activate weather
    ```

5. Ask its Python and its NumPy.

    ```text
    python --version
    ```

    ```text
    Python 3.14.8
    ```

    ```text
    python -c "import numpy; print(numpy.__version__)"
    ```

    ```text
    2.5.4
    ```

**Check:** `(weather)` at the start of the prompt, and `2.5.4`.

!!! warning "`ModuleNotFoundError: No module named 'numpy'`"
    The prompt still says `(base)`: `conda activate weather`, then again.

---

### 2. VS Code uses it { #interpreter }

**0:10 · 5 min** · The ▶ button and the colours of the editor use the interpreter selected here.

1. `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select Interpreter`,
   pick the entry with `envs/weather` in its path.
2. The Status Bar, bottom right, shows `3.14.8` and `weather`.
3. A new terminal (`+` in the terminal panel) starts with `(weather)`.

**Check:** `weather` in the Status Bar.

---

### 3. Write it down: `environment.yml` { #yml }

**0:15 · 10 min** · The file lists what was asked for; any laptop makes the same environment from it.

1. Export what was asked for.

    ```text
    conda env export --from-history -f environment.yml
    ```

2. Open `environment.yml`.

    ```text
    name: weather
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - numpy=2.5
    prefix: /Users/smilte/miniforge3/envs/weather
    ```

3. Delete the last line, `prefix: ...`: it names a folder on this laptop.
   Save.
4. Commit it.

    ```text
    git add environment.yml
    ```

    ```text
    git commit -m "Add the conda environment of the project"
    ```

    ```text
    [main eb08d7c] Add the conda environment of the project
     1 file changed, 6 insertions(+)
     create mode 100644 environment.yml
    ```

    Your id differs.

**Check:** `environment.yml` of six lines in the history.

!!! question "Task: does the file make the environment?"
    Make a second environment, `weather-check`, from `environment.yml`.
    Ask it for its NumPy version without activating it, then remove it.

??? note "Answer"
    ```text
    conda env create -n weather-check -f environment.yml
    ```

    It ends with `#     $ conda activate weather-check`. The packages come
    from conda's cache, so it is quick.

    ```text
    conda run -n weather-check python -c "import numpy; print(numpy.__version__)"
    ```

    ```text
    2.5.4
    ```

    ```text
    conda env remove -n weather-check
    ```

---

## Part 2 · Functions and the csv module { #part-2 }

**0:25 to 0:55** · Seminar 6 computed the mean in one block of lines. Here the steps get names.

---

### 4. A function for the mean { #function }

**0:25 · 10 min** · `def` gives a block a name and inputs; `return` hands a value back.

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
    python scripts/column_mean.py
    ```

    ```text
    2.0
    21.0
    ```

    The `-999` of the first list is left out: (1 + 3) / 2.

**Check:** `2.0` and `21.0`.

---

### 5. A column with the csv module { #csv }

**0:35 · 10 min** · `csv.reader` cuts every line into a list of strings; `with` closes the file at the end of the block.

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

3. Replace the three lines at the bottom with these, save, run.

    ```python
    temp = read_column("data/raw/weather.csv", 1)
    print(len(temp), temp[:3])
    print(f"mean {mean_valid(temp):.5f} °C")
    ```

    ```text
    python scripts/column_mean.py
    ```

    ```text
    ['time', 'temp_c', 'humidity_pct', 'wind_ms']
    87672 [-4.4, -4.8, -5.5]
    mean 7.15997 °C
    ```

    `next(reader)` takes the header line; the loop gets the rest.

**Check:** `mean 7.15997 °C`, from two functions.

---

### 6. A path that works from any folder { #pathlib }

**0:45 · 10 min** · A relative path starts at the terminal's folder, not at the script's.

1. Run the script from the folder `scripts`.

    ```text
    cd scripts
    ```

    ```text
    python column_mean.py
    ```

    The last lines:

    ```text
      File "/Users/smilte/weather-project/scripts/column_mean.py", line 13, in read_column
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
    python column_mean.py
    ```

    ```text
    /Users/smilte/weather-project
    mean 7.15997 °C
    ```

    ```text
    cd ..
    ```

**Check:** the same mean from `scripts` and from the project folder.

!!! question "Task: humidity and wind"
    Add two lines to `column_mean.py` that print the mean of
    `humidity_pct` (column 2) and of `wind_ms` (column 3), with two decimals.

??? note "Answer"
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

**0:55 to 1:25** · A NumPy array holds numbers of one type, and computes on all of them at once.

---

### 7. The file into an array { #loadtxt }

**0:55 · 10 min** · `np.loadtxt` reads a table of numbers into a two-dimensional array.

1. New file `scripts/coldest_day.py`. Type, save.

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

2. Run it.

    ```text
    python scripts/coldest_day.py
    ```

    ```text
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

**1:05 · 10 min** · A comparison on an array gives an array of `True` and `False`, a mask; a mask selects rows.

1. At the end of the file, add these lines, save, run.

    ```python
    temp = data[:, 0]
    valid = temp != -999
    print(valid[:3], valid.sum(), (~valid).sum())
    print(f"all rows   {temp.mean():.5f}")
    print(f"valid rows {temp[valid].mean():.5f}")
    ```

    ```text
    python scripts/coldest_day.py
    ```

    The new lines:

    ```text
    [ True  True  True] 87552 120
    all rows   5.78280
    valid rows 7.15997
    ```

    `sum` counts the `True`; `~` turns the mask round.

**Check:** 120 rows of `-999`, and 7.15997 without them.

---

### 9. One row per day: `reshape` { #reshape }

**1:15 · 10 min** · 87 672 hours are 3653 days of 24 hours; `reshape` cuts the column into those rows.

1. Add these lines, save, run.

    ```python
    days = temp.reshape(3653, 24)
    day_means = days.mean(axis=1)
    print(days.shape, day_means[:3])
    dates = np.arange("2016-01-01", "2026-01-01", dtype="datetime64[D]")
    print(dates[:2], dates[-1])
    ```

    The new lines:

    ```text
    (3653, 24) [-4.87083333 -5.13333333 -3.14166667]
    ['2016-01-01' '2016-01-02'] 2025-12-31
    ```

    `axis=1` averages along each row: one mean per day. `dates` holds the
    3653 days, in the same order.

2. The sensor failure covers whole days, so their mean is exactly `-999`.
   Add a mask for the days, then the coldest day.

    ```python
    ok = day_means != -999
    print(ok.sum(), dates[~ok])
    i = day_means[ok].argmin()
    print("coldest day", dates[ok][i], f"{day_means[ok][i]:.2f}")
    ```

    ```text
    3648 ['2019-07-22' '2019-07-23' '2019-07-24' '2019-07-25' '2019-07-26']
    coldest day 2019-01-26 -13.00
    ```

    `argmin` gives the position of the smallest value. The same mask on
    `dates` keeps the days in step.

**Check:** `coldest day 2019-01-26 -13.00`.

!!! question "Task: the warmest day, and the frost days"
    Add lines that print the warmest day and its mean, and the number of
    days whose mean is below 0 °C.

??? note "Answer"
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

**1:25 to 2:00** · Ten years of the same station: compare the mean of each year.

---

### 10. The year of every row { #year }

**1:25 · 5 min** · The year is the first four characters of `time`.

1. New file `scripts/yearly_means.py`. Type, save, run.

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

    ```text
    python scripts/yearly_means.py
    ```

    ```text
    ['2016-01-01T00:00' '2016-01-01T01:00'] [2016 2016] [2025 2025]
    ```

**Check:** `2016` at the start, `2025` at the end.

---

### 11. A mean for each year { #yearly }

**1:30 · 10 min** · `&` joins two masks: this year, and not `-999`.

1. Replace the `print` line with a loop, save, run.

    ```python
    for y in range(2016, 2026):
        m = (year == y) & valid
        print(y, f"{temp[m].mean():.2f}", m.sum())
    ```

    ```text
    python scripts/yearly_means.py
    ```

    ```text
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

2. Read it: the years go up and down by up to 2.3 °C, in no order. 2019
   has 120 hours fewer, the five summer days of the failure.

**Check:** ten means between 5.98 and 8.31.

---

### 12. Write the answer, commit, push { #commit }

**1:40 · 15 min** · The script writes its answer to `results/`; the script goes into the history, the answer does not.

1. Replace the loop with these lines, save, run.

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

    ```text
    python scripts/yearly_means.py
    ```

    The last two lines:

    ```text
    2016-2020  7.24
    2021-2025  7.08
    ```

    The answer: not warmer. The second five years are 0.16 °C colder,
    less than the step from one year to the next.

2. The file.

    ```text
    tail -n 2 results/yearly_temp.txt
    ```

    ```text
    2016-2020  7.24
    2021-2025  7.08
    ```

3. What Git sees: the scripts, not `results/`.

    ```text
    git status --short
    ```

    ```text
    ?? scripts/coldest_day.py
    ?? scripts/column_mean.py
    ?? scripts/yearly_means.py
    ```

4. Commit, push.

    ```text
    git add scripts
    ```

    ```text
    git commit -m "Read the weather data with functions and NumPy"
    ```

    ```text
    [main 8cc45c7] Read the weather data with functions and NumPy
     3 files changed, 79 insertions(+)
     create mode 100644 scripts/coldest_day.py
     create mode 100644 scripts/column_mean.py
     create mode 100644 scripts/yearly_means.py
    ```

    Your id and counts differ.

    ```text
    git push
    ```

**Check:** on GitHub, `environment.yml` and the three scripts.

!!! question "Task: the warmest and the coldest month"
    Add the month of every row (`t[5:7]`) and print the mean temperature of
    each month over the ten years.

??? note "Answer"
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

**1:55 · 5 min**

| To | Type |
|--|--|
| make the project's environment | `conda create -n weather python=3.14 numpy=2.5` |
| switch it on | `conda activate weather` |
| write it down | `conda env export --from-history -f environment.yml` |
| make it on another laptop | `conda env create -f environment.yml` |
| name a block of steps | `def name(inputs):` ... `return value` |
| read a CSV file | `csv.reader(f)`, `next(reader)` for the header |
| a path from the project folder | `Path(__file__).resolve().parent.parent` |
| a table into an array | `np.loadtxt(path, delimiter=",", skiprows=1, usecols=...)` |
| select rows | `temp[temp != -999]`, masks joined with `&` |

Seminar 8 starts from this repository and the environment `weather`.

---

## Optional, if the room is fast { #optional }

---

### 14. Loop against array: time both { #timing }

**— · 10 min** · `time.perf_counter()` is a clock in seconds; the difference of two readings is the time between them.

1. New file `scripts/time_both.py`. Type, save, run twice.

    ```python
    import time

    import numpy as np

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",", skiprows=1, usecols=1)
    temps = temp.tolist()

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

    ```text
    python scripts/time_both.py
    ```

    ```text
    loop  7.15997 in 6.2 ms
    array 7.15997 in 0.4 ms
    ```

    Your times differ.

**Check:** the same mean, the array about 15 times faster.

---

### 15. Count in bins: `np.histogram` { #histogram }

**— · 5 min** · A histogram counts the values that fall into each bin.

1. At the end of `coldest_day.py`, add these lines, save, run.

    ```python
    counts, edges = np.histogram(temp[valid], bins=np.arange(-20, 40, 5))
    print(edges)
    print(counts)
    ```

    The new lines:

    ```text
    [-20 -15 -10  -5   0   5  10  15  20  25  30  35]
    [   12   686  5589 16065 16582 14050 14880 12261  6111  1230    86]
    ```

    Twelve edges make eleven bins: 12 hours from −20 to −15 °C, 86 from
    30 to 35 °C.

**Check:** the counts add up to 87 552.

---

### 16. Skip a bad row: `try` and `except` { #except }

**— · 10 min** · `try` runs a block; if it raises the error named after `except`, that block runs instead.

1. New file `scripts/export_values.py`, for the spreadsheet export with
   `;` and decimal commas. Type, save, run.

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

    print(len(values), values)
    print(f"mean {sum(values) / len(values):.2f}")
    ```

    ```text
    python scripts/export_values.py
    ```

    ```text
    skipped: ['', 'mean', '7,97']
    9 [6.3, 5.0, 5.6, 7.0, 9.4, 10.4, 9.2, 9.0, 9.8]
    mean 7.97
    ```

    The last line of the export has no `nr`: `int('')` raises
    `ValueError`, and the row is skipped.

**Check:** nine values, the mean the spreadsheet wrote, 7.97.

---

## Aims practised

- ♻️ **Reproducibility:** `environment.yml` makes the same environment on
  any laptop; the answer is a file the script writes again at any time.
- 🔧 **Tool-agnostic:** the same `conda` and `python` lines on macOS and
  Windows; a path from `Path(__file__)` works from any folder.
- 📁 **Files:** the file read three ways (lines, csv, NumPy) to the same
  7.15997; made files stay in the ignored `results/`.
