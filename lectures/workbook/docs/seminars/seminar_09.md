# Seminar 9 · NumPy

**Paired lecture:** 09 Parameter Estimation and Fitting · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Is it getting warmer?

**Today's goal:** every student finds NumPy in the `analysis` environment,
turns a column of `weather.csv` into a NumPy array and computes on it
whole, fits a straight line through the ten yearly means by the five sums
and with `np.polyfit` (−0.56 ± 0.77 °C per decade), draws the points, the
line and the residuals, and fits a line to a file of their own.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both). In the blocks, a line that starts with `$` is typed in the
terminal, a line that starts with `>>>` is typed at Python's prompt, and
every other line is what comes back; `...` stands for lines left out.

**If time runs short:** skip the Tasks; keep section 12, the figure, and
Part 4, your own data. Sections 15 and 16 are optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the zip (0.6 MB)
      and, for a student without the `analysis` environment, for conda:
      Python, Matplotlib and pandas, pandas about 20 MB more than Seminar
      7's Python and Matplotlib. Nothing from earlier seminars is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **Your project:** students with a data file of their own bring it
      (a CSV file with two number columns is enough).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · NumPy is already installed { #part-1 }

<!-- 0:00 to 0:15 -->

Today's package is in the environment already: Matplotlib and pandas both need it.

Further reading: [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 5 min -->

Today's folder holds the data, the scripts of the project and `environment.yml`, the list of the `analysis` environment.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s09.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s09.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s09.zip
       creating: /Users/smilte/weather-s09/
    ...
      inflating: /Users/smilte/weather-s09/scripts/weather.py
    $ cd ~/weather-s09
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s09 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s09` > **Open**. The window
   reloads: open the terminal again (**View** > **Terminal**); it starts in
   the folder.

**Check:** `ls` shows `README.md  data  environment.yml  results  scripts`.

---

### 2. Switch on `analysis`, or make it { #env }

<!-- 0:05 · 5 min -->

One conda environment, `analysis`, serves weeks 8 to 12. Whoever made it in Seminar 8 switches it on; everyone else makes it from the folder's list.

1. The list of the environment:

    ```text
    $ cat environment.yml
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - matplotlib-base=3.11
      - pandas=3.1
    ```

2. Is `analysis` on this laptop? Conda lists its environments; yours may
   hold more lines (`weather`, `s07`, ...).

    ```text
    $ conda env list
    # conda environments:
    #
    base                 * /Users/smilte/miniforge3
    analysis               /Users/smilte/miniforge3/envs/analysis
    ```

3. No `analysis` line: make it from the list. It takes a few minutes.

    ```text
    $ conda env create -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate analysis
    ```

4. Switch it on: the prompt starts with `(analysis)`.

    ```text
    $ conda activate analysis
    ```

5. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/analysis` in its path. The
   Status Bar shows `analysis`.

**Check:** `(analysis)` at the start of the prompt, `analysis` in the Status Bar.

!!! warning "`CondaValueError: prefix already exists`"
    `analysis` is there already: skip step 3, `conda activate analysis`.

---

### 3. NumPy is already there: a dependency { #dependency }

<!-- 0:10 · 5 min -->

Matplotlib and pandas are both built on NumPy, so conda installed NumPy with them, unasked. A package that another package needs is a **dependency**.

1. The list names three packages, and no NumPy. Ask conda for it anyway.

    ```text
    $ conda list numpy
    # packages in environment at /Users/smilte/miniforge3/envs/analysis:
    #
    # Name                    Version                   Build  Channel
    numpy                     2.5.4           py314hd3a7d6b_0  conda-forge
    ```

    The build, third column, differs from laptop to laptop.

2. Python finds it, with its version:

    ```text
    $ python -c "import numpy; print(numpy.__version__)"
    2.5.4
    ```

**Check:** `2.5.4` (the last digit may be higher), and no NumPy line in `environment.yml`.

---

## Part 2 · Arrays { #part-2 }

<!-- 0:15 to 0:45 -->

A NumPy **array** holds numbers of one type, and arithmetic on it works on all of them at once.

---

### 4. An array, and arithmetic on all of it { #array }

<!-- 0:15 · 10 min -->

`np.array` turns a list into an array; `+`, `-`, `*`, `/` and `**` then work on every element.

1. Start Python in the terminal, `python`, import NumPy under its usual
   short name, and make an array of the four hours of 21 July 2019, 20:00 to
   23:00.

    ```pycon
    >>> import numpy as np
    >>> hours = np.array([27.3, 25.6, 24.6, 23.6])
    >>> hours
    array([27.3, 25.6, 24.6, 23.6])
    >>> hours.size
    4
    >>> hours.mean()
    np.float64(25.275)
    ```

    `np.float64` is NumPy's float. `size` counts the elements, `mean()`
    averages them.

2. The four hours in °F, one line for all four. A list does something else
   with `*`: it repeats itself.

    ```pycon
    >>> hours * 9 / 5 + 32
    array([81.14, 78.08, 76.28, 74.48])
    >>> [27.3, 25.6] * 2
    [27.3, 25.6, 27.3, 25.6]
    >>> hours * 2
    array([54.6, 51.2, 49.2, 47.2])
    ```

3. The misses from the mean, their squares and their sum: the sum of
   squares S of the lecture, at its lowest point.

    ```pycon
    >>> miss = hours - hours.mean()
    >>> miss
    array([ 2.025,  0.325, -0.675, -1.675])
    >>> miss ** 2
    array([4.100625, 0.105625, 0.455625, 2.805625])
    >>> (miss ** 2).sum()
    np.float64(7.467499999999997)
    ```

    7.467499999999997 is 7.4675: a float stores most decimals a little
    off, as `0.1 + 0.2` gives `0.30000000000000004`.

**Check:** `7.4675` up to the float tail; Python still running for section 5.

---

### 5. A mask keeps some of the values { #mask }

<!-- 0:25 · 5 min -->

A comparison on an array gives an array of `True` and `False`, a **mask**; the array indexed with a mask keeps the elements where it is `True`.

1. The six hours of that evening, the last two marked `-999`: the sensor
   failed. Then leave Python.

    ```pycon
    >>> six = np.array([27.3, 25.6, 24.6, 23.6, -999, -999])
    >>> six.mean()
    np.float64(-316.15000000000003)
    >>> ok = six != -999
    >>> ok
    array([ True,  True,  True,  True, False, False])
    >>> six[ok]
    array([27.3, 25.6, 24.6, 23.6])
    >>> six[ok].mean()
    np.float64(25.275)
    >>> ok.sum()
    np.int64(4)
    >>> exit()
    ```

    `ok.sum()` counts the `True` values: `True` adds as 1.

**Check:** −316.15 with the marks, 25.275 without them.

---

### 6. A column of the file as an array { #column }

<!-- 0:30 · 15 min (Task: 5 min) -->

pandas reads `weather.csv` into a table, a **DataFrame**; `df["temp_c"]` is one column, and `.to_numpy()` turns it into a NumPy array.

1. New file `scripts/trend.py`. Type, save.

    ```python
    import numpy as np
    import pandas as pd

    df = pd.read_csv("data/raw/weather.csv")
    temp = df["temp_c"].to_numpy()
    print(type(temp), temp.size, temp[:3])
    ok = temp != -999
    print(ok.sum(), temp[ok].mean())
    ```

    `temp[:3]` is the first three elements, as for a list.

2. Run it.

    ```text
    $ python scripts/trend.py
    <class 'numpy.ndarray'> 87672 [-4.4 -4.8 -5.5]
    87552 7.1599655062134495
    ```

    87 672 hours, 87 552 of them measured; their mean, 7.16 °C, in one
    line and without a loop.

**Check:** `87552 7.1599655062134495`.

!!! warning "`FileNotFoundError: ... 'data/raw/weather.csv'`"
    The terminal is not in the project folder: `cd ~/weather-s09`, then
    run again.

!!! question "Task: the hours below 0 °C"
    How many measured hours were below 0 °C, and what share of all
    measured hours is that? Hint: `temp[ok] < 0` is a mask too.

??? success "Answer"
    At the end of `trend.py`, two lines; take them out again afterwards.

    ```python
    frost = temp[ok] < 0
    print(frost.sum(), f"{frost.sum() / ok.sum():.3f}")
    ```

    ```text
    $ python scripts/trend.py
    ...
    22352 0.255
    ```

    22 352 hours, a quarter of the ten years.

---

## Part 3 · Is it getting warmer? { #part-3 }

<!-- 0:45 to 1:35 -->

A straight line through the ten yearly means: its slope is the change per year, and its ± says whether the change is real.

---

### 7. The ten yearly means { #yearly }

<!-- 0:45 · 10 min -->

The year of each hour is the first four characters of its time; `&` joins two masks, "measured and in this year".

1. At the end of `trend.py`, add these lines, save.

    ```python

    year = df["time"].str[:4].astype(int).to_numpy()
    years = np.arange(2016, 2026)
    means = []
    for k in years:
        means.append(temp[ok & (year == k)].mean())
    y = np.array(means)
    print(y.round(2))
    ```

    `.str[:4]` cuts the first four characters of each time,
    `.astype(int)` turns `"2016"` into the number 2016.
    `np.arange(2016, 2026)` is the years 2016 to 2025: the end is left out,
    as in `range`. `round(2)` shows two decimals.

2. Run it.

    ```text
    $ python scripts/trend.py
    ...
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    ```

**Check:** ten means, from 5.98 (2025) to 8.31 (2023).

---

### 8. The five sums, the slope and the intercept { #sums }

<!-- 0:55 · 10 min -->

The best line y = a x + b, with x the years since 2016, comes from five sums of the data: N, Σx, Σy, Σx² and Σxy.

1. Add these lines, save, run.

    ```python

    x = years - 2016
    n = x.size
    sx, sy = x.sum(), y.sum()
    sxx, sxy = (x * x).sum(), (x * y).sum()
    print(n, sx, round(sy, 2), sxx, round(sxy, 2))
    ```

    ```text
    $ python scripts/trend.py
    ...
    10 45 71.6 285 317.62
    ```

    `x * y` multiplies year by year; `sum()` adds the ten products.

2. Then the slope and the intercept. Add, save, run.

    ```python
    d = n * sxx - sx ** 2
    a = (n * sxy - sx * sy) / d
    b = (sxx * sy - sx * sxy) / d
    print(f"a = {a:.4f} °C per year, b = {b:.2f} °C")
    print(f"{10 * a:.2f} °C per decade")
    ```

    ```text
    $ python scripts/trend.py
    ...
    a = -0.0555 °C per year, b = 7.41 °C
    -0.56 °C per decade
    ```

    `{a:.4f}` writes `a` with four decimals. b is the line's value in 2016,
    where x = 0.

**Check:** a = −0.0555 °C per year, b = 7.41 °C.

---

### 9. `np.polyfit` gives the same line { #polyfit }

<!-- 1:05 · 5 min -->

`np.polyfit(x, y, 1)` fits a polynomial of degree 1, a straight line, by least squares, and returns its slope and intercept.

1. Add one line, save, run.

    ```python
    print(np.polyfit(x, y, 1))
    ```

    ```text
    $ python scripts/trend.py
    ...
    [-0.05552739  7.40992628]
    ```

**Check:** the a and b of section 8, with more digits.

---

### 10. The uncertainty of the slope { #uncertainty }

<!-- 1:10 · 10 min -->

Each yearly mean is uncertain by σ, the scatter of the ten years; the slope inherits σ_a = σ √(N / Δ).

1. Add these lines, save, run.

    ```python

    s = y.std(ddof=1)
    print(f"scatter of the years {s:.2f} °C")
    sigma = 0.70
    sa = sigma * np.sqrt(n / d)
    print(f"slope {10 * a:.2f} ± {10 * sa:.2f} °C per decade")
    ```

    ```text
    $ python scripts/trend.py
    ...
    scatter of the years 0.70 °C
    slope -0.56 ± 0.77 °C per decade
    ```

    `std(ddof=1)` is the standard deviation with N − 1 in the denominator,
    the scatter of a sample. `sigma` keeps it to two digits, 0.70.

**Check:** −0.56 ± 0.77 °C per decade: zero lies inside one σ. Ten years do not show a trend.

---

### 11. The residuals { #residuals }

<!-- 1:20 · 5 min -->

A **residual** is a point minus the line: what the model leaves over. Divided by σ, squared and added, they give χ².

1. Add these lines, save, run.

    ```python

    r = y - (a * x + b)
    print(r.round(2))
    print(f"chi2 {((r / sigma) ** 2).sum():.2f} for {n - 2} degrees of freedom")
    ```

    ```text
    $ python scripts/trend.py
    ...
    [ 0.19 -0.85  0.68  0.03 -0.36  0.12 -0.48  1.29  0.31 -0.93]
    chi2 8.56 for 8 degrees of freedom
    ```

    χ² near the degrees of freedom, 10 points − 2 parameters, is what a
    right model gives. Here it is no test: σ came from the scatter of
    these same ten points, so χ² lands near 8 whatever the model.

**Check:** the largest residual, 1.29 °C, is 2023; χ² 8.56.

---

### 12. Points, line and residuals in one figure { #figure }

<!-- 1:25 · 10 min (Task: 5 min) -->

Two panels, one above the other with a shared x-axis: the data with the line, and under it what the line leaves.

1. Under `import numpy as np` at the top of `trend.py`, add one line.

    ```python
    import matplotlib.pyplot as plt
    ```

2. At the end, add these lines, save, run.

    ```python

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(6, 5), sharex=True)
    top.plot(years, y, "o", label="yearly mean")
    top.plot(years, a * x + b, label="fitted line")
    top.set_ylabel("Mean temperature (°C)")
    top.legend()
    bottom.plot(years, r, "o")
    bottom.axhline(0, color="grey")
    bottom.set_xlabel("Year")
    bottom.set_ylabel("Residual (°C)")
    fig.savefig("results/trend.png", dpi=150)
    ```

    `plt.subplots(2, 1, ...)` makes two Axes in one column;
    `sharex=True` gives them one x-axis. `"o"` draws points, no line.

3. In the Explorer, click `results/trend.png`: ten points around a slightly
   falling line, and below it ten residuals scattered around zero, 2023
   highest and 2025 lowest.

4. At the end of `README.md`, add the answer and save.

    ```text

    ## Trend

    A straight line through the ten yearly means, `scripts/trend.py`:
    −0.56 ± 0.77 °C per decade (σ = 0.70 °C per year, from their scatter).
    Ten years cannot tell whether it is getting warmer.
    ```

**Check:** `results/trend.png` with two panels, and the trend in the README.

!!! question "Task: one year less"
    Fit the line without 2025, the coldest year: what slope do 2016 to
    2024 give? Hint: `keep = x != 9` is a mask; fit `x[keep]` and `y[keep]`
    with `np.polyfit`.

??? success "Answer"
    At the end of `trend.py`:

    ```python
    keep = x != 9
    print(f"{10 * np.polyfit(x[keep], y[keep], 1)[0]:.2f} °C per decade")
    ```

    ```text
    $ python scripts/trend.py
    ...
    0.22 °C per decade
    ```

    +0.22 without 2025, against −0.56 with it: one year turns the sign. That
    is what ± 0.77 says: the slope of ten years is not known to better than
    about 0.8 °C per decade.

---

## Part 4 · Your project { #part-4 }

<!-- 1:35 to 1:55 -->

The same steps on a file of your own: two columns, a line, its slope in the README. Without a file yet, use the humidity and temperature of `weather.csv`.

---

### 13. A straight line through your own data { #project }

<!-- 1:35 · 20 min -->

Any two columns of numbers go through the same lines; only the file and the column names change.

1. Open your project's folder in VS Code (**File** > **Open Folder...**),
   with your data file in `data/raw`. No folder yet: make one, then copy
   your file into `data/raw`.

    ```text
    $ mkdir -p ~/myproject/data/raw ~/myproject/scripts ~/myproject/results
    ```

2. New file `scripts/fit.py`. Type, with your file's name, save, run: the
   names of its columns.

    ```python
    import numpy as np
    import pandas as pd

    df = pd.read_csv("data/raw/YOUR_FILE.csv")
    print(df.columns)
    ```

    Without your own data: in `weather-s09`, `data/raw/weather.csv`.

    ```text
    $ python scripts/fit.py
    Index(['time', 'temp_c', 'humidity_pct', 'wind_ms'], dtype='str')
    ```

3. Pick the column across (x) and the column up (y). Add these lines with
   your names, save, run. `dropna` leaves out the rows where either is
   missing; `na_values=[-999]` turns the station's mark into "missing".

    ```python

    df = pd.read_csv("data/raw/YOUR_FILE.csv", na_values=[-999])
    df = df.dropna(subset=["YOUR_X", "YOUR_Y"])
    x = df["YOUR_X"].to_numpy()
    y = df["YOUR_Y"].to_numpy()
    a, b = np.polyfit(x, y, 1)
    r = y - (a * x + b)
    print(x.size, f"slope {a:.4g}, intercept {b:.4g}, residual sd {r.std(ddof=2):.3g}")
    ```

    With `temp_c` across and `humidity_pct` up:

    ```text
    $ python scripts/fit.py
    Index(['time', 'temp_c', 'humidity_pct', 'wind_ms'], dtype='str')
    87552 slope -0.8484, intercept 85.19, residual sd 7.6
    ```

    `{a:.4g}` writes four significant digits, whatever the size of the
    number. Humidity falls by 0.85 % per °C.

4. The figure of section 12 for your columns. Put
   `import matplotlib.pyplot as plt` at the top of `fit.py`, add these
   lines at the end with your names and units, save, run, and open
   `results/fit.png`.

    ```python

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(6, 5), sharex=True)
    top.plot(x, y, ".", label="data")
    top.plot(x, a * x + b, label="fitted line")
    top.set_ylabel("YOUR_Y (unit)")
    top.legend()
    bottom.plot(x, r, ".")
    bottom.axhline(0, color="grey")
    bottom.set_xlabel("YOUR_X (unit)")
    bottom.set_ylabel("Residual (unit)")
    fig.savefig("results/fit.png", dpi=150)
    ```

    `"."` draws small dots, for many points. With the humidity, the
    residuals end on a straight edge at the top: humidity stops at 100 %,
    which a straight line does not know.

5. In your README: the two columns, the number of points, the slope with
   its unit, and the script that computed it.

**Check:** a slope with its unit in your README, and a figure in `results`.

!!! warning "`df.columns` shows one long name with `;` in it"
    The file uses `;` between columns and a comma for decimals, as a
    spreadsheet with Lithuanian settings saves it: read it with
    `pd.read_csv("data/raw/YOUR_FILE.csv", sep=";", decimal=",")`.

---

### 14. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| see if a package is in the environment | `conda list numpy` |
| an array from a list, or from a column | `np.array([...])`, `df["temp_c"].to_numpy()` |
| arithmetic on every element | `a * 2`, `a - a.mean()`, `(a ** 2).sum()` |
| keep some elements | `a[a != -999]`, masks joined with `&` |
| count the `True` of a mask | `mask.sum()` |
| a straight line by hand | the five sums, `d = n * sxx - sx ** 2` |
| the same in one call | `np.polyfit(x, y, 1)` |
| the scatter of a sample | `y.std(ddof=1)` |
| two panels, one x-axis | `plt.subplots(2, 1, sharex=True)` |

---

## Optional, if the room goes fast { #optional }

---

### 15. SciPy and the yearly cycle { #scipy }

<!-- — · 20 min -->

The cycle of the seasons, T = c − A cos(2π(d − d₀)/365.25), has d₀ inside the cosine; `curve_fit` of **SciPy**, a library of scientific methods built on NumPy, finds it by walking downhill from starting values.

1. Install SciPy into `analysis`, with its version. At `Proceed ([y]/n)?`
   press `Enter`.

    ```text
    $ conda install scipy=1.18
    ...
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/analysis

      added / updated specs:
        - scipy=1.18
    ...
    Proceed ([y]/n)?
    $ python -c "import scipy; print(scipy.__version__)"
    1.18.1
    ```

2. Write the list again, then open `environment.yml`, delete its last
   line, `prefix: ...` (a folder on this laptop), save.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - matplotlib-base=3.11
      - pandas=3.1
      - scipy=1.18
    ```

    SciPy, the package just installed, is the last line; the lines above
    it may come in another order.

3. New file `scripts/cycle.py`: the 87 672 hours as 3653 rows of 24, one
   row per day, and the mean of each row. Type, save, run.

    ```python
    import numpy as np
    import pandas as pd

    df = pd.read_csv("data/raw/weather.csv", na_values=[-999])
    days = df["temp_c"].to_numpy().reshape(-1, 24)
    T = days.mean(axis=1)
    d = np.arange(T.size)
    good = ~np.isnan(T)
    print(days.shape, good.sum())
    ```

    ```text
    $ python scripts/cycle.py
    (3653, 24) 3648
    ```

    `reshape(-1, 24)` cuts the column into rows of 24; `mean(axis=1)`
    averages each row. A day with a missing hour has the mean `nan`, not a
    number; `~np.isnan(T)` keeps the other 3648. `d` counts the days from
    1 January 2016.

4. The model as a function, and the fit from the values read off a plot:
   level 7, amplitude 11, coldest day 15. Add, save, run.

    ```python

    from scipy.optimize import curve_fit


    def cycle(d, c, amp, d0):
        return c - amp * np.cos(2 * np.pi * (d - d0) / 365.25)


    popt, pcov = curve_fit(cycle, d[good], T[good], p0=[7, 11, 15])
    print(popt.round(2))
    ```

    ```text
    $ python scripts/cycle.py
    (3653, 24) 3648
    [ 7.18 11.18 15.92]
    ```

    `popt` holds the best c, A and d₀: 7.18 °C, 11.18 °C, day 15.92, the
    16th of January.

**Check:** `[ 7.18 11.18 15.92]`, and `scipy=1.18` in `environment.yml`.

!!! question "Task: start in summer"
    Start from `p0=[7, 11, 200]`. Is the curve different?

??? success "Answer"
    ```text
    [  7.18 -11.18 198.54]
    ```

    The same curve: a negative amplitude turns the cosine over, and day
    198.54 is the warmest day, 17 July, half a year after 15.92.

---

### 16. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions on `trend.py`, for a room that is done early. Each answer is folded under its task.

!!! question "Advanced task: the ± of the slope from χ²"
    The slopes whose best line has a χ² at most 1 above the minimum lie
    within ± σ_a. Try slopes t from −0.3 to 0.2 in steps of 0.001; for
    each, the best intercept is `(sy - t * sx) / n`. Which slopes keep χ²
    within 1 of the minimum?

??? success "Answer"
    At the end of `trend.py`:

    ```python

    chi2_min = ((r / sigma) ** 2).sum()
    inside = []
    for t in np.arange(-0.3, 0.2, 0.001):
        rt = y - (t * x + (sy - t * sx) / n)
        if ((rt / sigma) ** 2).sum() <= chi2_min + 1:
            inside.append(t)
    print(f"from {min(inside):.3f} to {max(inside):.3f}")
    ```

    ```text
    $ python scripts/trend.py
    ...
    from -0.132 to 0.021
    ```

    Half the width, (0.021 + 0.132) / 2 = 0.077 °C per year: σ_a of
    section 10. For a model whose χ² is not a parabola, this scan is how a
    ± is found.

!!! question "Advanced task: leave each year out"
    Fit the slope ten times, each time without one year. How much does the
    trend per decade depend on a single year?

??? success "Answer"
    ```python

    for k in range(10):
        keep = x != k
        slope = np.polyfit(x[keep], y[keep], 1)[0]
        print(2016 + k, f"{10 * slope:.2f}")
    ```

    ```text
    $ python scripts/trend.py
    ...
    2016 -0.39
    2017 -1.03
    2018 -0.31
    2019 -0.55
    2020 -0.58
    2021 -0.56
    2022 -0.46
    2023 -1.03
    2024 -0.73
    2025 0.22
    ```

    From −1.03 to +0.22 °C per decade: the spread of one σ, 0.77.

!!! question "Advanced task: the same line as a matrix"
    Put a column of the x and a column of ones side by side,
    `A = np.column_stack([x, np.ones(n)])`, and solve least squares with
    `np.linalg.lstsq(A, y)`. Same a and b?

??? success "Answer"
    ```python

    A = np.column_stack([x, np.ones(n)])
    print(np.linalg.lstsq(A, y)[0])
    ```

    ```text
    $ python scripts/trend.py
    ...
    [-0.05552739  7.40992628]
    ```

    The same. `A` has one row per year and one column per parameter; any
    model that is a sum of columns times parameters is solved this way.

---

## Aims practised

- ♻️ **Reproducibility:** one script turns the raw file into the slope,
  its ± and the figure; the README says which script and which σ.
- 🔧 **Tool-agnostic:** the same line by five sums and by `np.polyfit`,
  the same numbers.
- 📁 **Files:** the figure in `results/`, the answer in the README, the
  package list in `environment.yml`.
