# Seminar 8 · pandas

**Paired lecture:** 08 Data Quality and Uncertainty · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** How sure is 7.16?

**Today's goal:** every student makes the conda environment `analysis` from
today's folder, adds pandas to it and to `environment.yml`, reads
`weather.csv` into a table, finds its mean with the `-999` marks and without
them (5.78 and 7.16), its standard deviation and standard error, the mean of
each month and of each year, writes 7.16 ± 0.22 °C into the README, and then
reads a data file of their own project the same way.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both). In the blocks, a line that starts with `$` is typed in the terminal,
a line that starts with `>>>` is typed at Python's prompt, and every other
line is what comes back; `...` stands for lines left out.

**If time runs short:** skip the Tasks, but keep section 10, the answer in
the README, and section 12, your project; sections 13 to 16 are optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the download
      (0.6 MB) and for conda: Python and Matplotlib about 80 MB on a Mac and
      200 MB on Windows, less when conda has them from Seminar 7; pandas
      about 16 MB more. Nothing from earlier seminars is needed.
    - **Students with data for their project** bring the file to section
      12: a CSV file, or a spreadsheet saved as CSV.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** if you made `analysis` before, remove it (`conda env remove
      -n analysis`) to make it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · pandas in the environment { #part-1 }

<!-- 0:00 to 0:25 -->

pandas reads a table into Python and computes with its columns. It goes into the project's environment, and into the file that lists it.

Further reading: [pandas, 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html);
[HSF Analysis Essentials, Python](https://hsf-training.github.io/analysis-essentials/python/README.html).

---

### 1. Get today's folder, make the environment { #start }

<!-- 0:00 · 15 min -->

Today's folder holds the data, the module `weather.py` and `environment.yml`, the list from which conda makes the environment `analysis`: Python and Matplotlib.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s08.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s08.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s08.zip
       creating: /Users/smilte/weather-s08/
    ...
      inflating: /Users/smilte/weather-s08/scripts/weather.py
    $ cd ~/weather-s08
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s08 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s08` > **Open**. The window
   reloads: open the terminal again (**View** > **Terminal**); it starts in
   the folder.
3. The list for the environment: its name, where the packages come from,
   and what goes in.

    ```text
    $ cat environment.yml
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - matplotlib-base=3.11
      - python=3.14
    ```

4. Make the environment from it; conda takes its name from the file's
   first line. Then switch it on: the prompt starts with `(analysis)`.

    ```text
    $ conda env create -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate analysis
    $ conda activate analysis
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/analysis` in its path. The
   Status Bar shows `analysis`.

**Check:** `(analysis)` at the start of the prompt, `analysis` in the
Status Bar.

---

### 2. Install pandas, write it down { #install }

<!-- 0:15 · 10 min -->

A new package goes into the active environment, never into `base`, and into the file that lists it, or the next laptop cannot run the script.

1. pandas is not in it yet.

    ```text
    $ python -c "import pandas"
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'pandas'
    ```

2. Install it, with its version.

    ```text
    $ conda install pandas=3.1
    ...
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/analysis

      added / updated specs:
        - pandas=3.1
    ...
    Proceed ([y]/n)?
    ```

3. At `Proceed ([y]/n)?` press `Enter`. Then ask for the version.

    ```text
    $ python -c "import pandas; print(pandas.__version__)"
    3.1.1
    ```

4. Export the list again.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

5. Open `environment.yml`, delete its last line, `prefix: ...` (a folder
   on this laptop), save: pandas is the new last line. The lines above it
   may stand in another order on your laptop.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - matplotlib-base=3.11
      - python=3.14
      - pandas=3.1
    ```

**Check:** `3.1.1` (the last digit may be higher), and `- pandas=3.1` at
the end of `environment.yml`.

!!! warning "`ModuleNotFoundError: No module named 'pandas'`"
    The prompt says `(base)`: `conda activate analysis`, then again. VS
    Code's Status Bar must show `analysis` too (section 1, step 5).

---

## Part 2 · A first look at the table { #part-2 }

<!-- 0:25 to 0:55 -->

At Python's prompt: the file as a table, one of its columns, and its mean, twice.

---

### 3. Read the file into a table { #read }

<!-- 0:25 · 10 min -->

`read_csv` reads a CSV file into a **DataFrame**: a table whose columns have names and whose rows have numbers.

1. Start Python in the terminal, in the project folder, and import pandas.
   `pd` is the short name everyone uses for it.

    ```pycon
    $ python
    >>> import pandas as pd
    ```

2. Read the file, then ask for its size: (rows, columns).

    ```pycon
    >>> df = pd.read_csv("data/raw/weather.csv")
    >>> df.shape
    (87672, 4)
    ```

3. The first five rows. The numbers on the left are the **index**, the
   name of each row; the names on top come from the header line of the
   file.

    ```pycon
    >>> df.head()
                   time  temp_c  humidity_pct  wind_ms
    0  2016-01-01T00:00    -4.4            93      2.5
    1  2016-01-01T01:00    -4.8            95      2.6
    2  2016-01-01T02:00    -5.5            95      2.7
    3  2016-01-01T03:00    -6.0            96      1.9
    4  2016-01-01T04:00    -5.9            94      2.0
    ```

**Check:** `(87672, 4)`: one row per hour of ten years, four columns.

---

### 4. One column and its mean { #column }

<!-- 0:35 · 10 min -->

One column of a DataFrame is a **Series**: its values with the index beside them, and methods that work on the whole column.

1. A column by its name, in square brackets. pandas shows the first and the
   last rows and the length.

    ```pycon
    >>> df["temp_c"]
    0        -4.4
    1        -4.8
    2        -5.5
    3        -6.0
    4        -5.9
             ...
    87667    -8.1
    87668    -8.5
    87669    -9.5
    87670    -9.9
    87671   -11.3
    Name: temp_c, Length: 87672, dtype: float64
    ```

2. Its mean and its smallest value.

    ```pycon
    >>> print(df["temp_c"].mean())
    5.782796103659092
    >>> print(df["temp_c"].min())
    -999.0
    ```

3. `==` compares every value of the column with `-999` and gives `True` or
   `False` for each; `sum` counts the `True`s.

    ```pycon
    >>> print((df["temp_c"] == -999).sum())
    120
    ```

**Check:** 5.78, and `-999.0` as the minimum: the 120 hours the sensor
was down are in the mean as temperatures of −999 °C.

---

### 5. Read `-999` as missing { #missing }

<!-- 0:45 · 10 min (Task: 5 min, skip if late) -->

`na_values` names the code that stands for a missing value; pandas reads it as **NaN**, "not a number", and leaves it out of every mean.

1. Read the file again, with the code.

    ```pycon
    >>> df = pd.read_csv("data/raw/weather.csv", na_values=[-999])
    ```

2. `isna()` is `True` where a value is missing: count them, then take the
   mean again.

    ```pycon
    >>> print(df["temp_c"].isna().sum())
    120
    >>> print(df["temp_c"].mean())
    7.1599655062134495
    ```

3. Eight numbers for every numeric column: `describe()` is the first look
   at any table. `count` leaves the missing values out; `std` is the
   standard deviation; `25%`, `50%` and `75%` are the values below which
   that share of the hours lies.

    ```pycon
    >>> df.describe()
                 temp_c  humidity_pct       wind_ms
    count  87552.000000  87672.000000  87672.000000
    mean       7.159966     79.097409      3.503523
    std        8.850783     10.695959      1.928826
    min      -16.300000     34.000000      0.000000
    25%       -0.200000     72.000000      2.100000
    50%        6.700000     79.000000      3.500000
    75%       14.200000     87.000000      4.800000
    max       32.400000    100.000000     12.000000
    >>> exit()
    ```

**Check:** the mean 7.16, `count` 87552 for `temp_c`, and the minimum a
winter night, −16.3 °C.

!!! question "Task: which hours are missing?"
    A Series of `True` and `False` in square brackets keeps the rows where
    it is `True`: `df[df["temp_c"].isna()]`. Start `python` again, read the
    file with `na_values`, and show the rows of the missing hours. From
    when to when was the sensor down?

??? success "Answer"
    ```pycon
    >>> import pandas as pd
    >>> df = pd.read_csv("data/raw/weather.csv", na_values=[-999])
    >>> df[df["temp_c"].isna()]
                       time  temp_c  humidity_pct  wind_ms
    31152  2019-07-22T00:00     NaN            76      3.2
    31153  2019-07-22T01:00     NaN            81      3.0
    31154  2019-07-22T02:00     NaN            80      3.4
    31155  2019-07-22T03:00     NaN            79      3.2
    31156  2019-07-22T04:00     NaN            81      2.9
    ...                 ...     ...           ...      ...
    31267  2019-07-26T19:00     NaN            55      2.4
    31268  2019-07-26T20:00     NaN            59      2.3
    31269  2019-07-26T21:00     NaN            61      1.3
    31270  2019-07-26T22:00     NaN            65      1.5
    31271  2019-07-26T23:00     NaN            66      1.9

    [120 rows x 4 columns]
    ```

    From 22 July 2019, 00:00, to 26 July, 23:00: five days. The humidity
    and the wind were still measured.

---

## Part 3 · How sure is 7.16? { #part-3 }

<!-- 0:55 to 1:45 -->

The lines that matter go into a script, `scripts/how_sure.py`, so that one command computes every number again.

---

### 6. The spread, the count and the standard error { #error }

<!-- 0:55 · 10 min -->

The **standard error** s / √n says how far a mean of n independent values typically lies from the long-run mean.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `how_sure.py`, press `Enter`. Type, save.

    ```python
    import pandas as pd

    df = pd.read_csv("data/raw/weather.csv", na_values=[-999])
    temps = df["temp_c"]
    print(f"missing {temps.isna().sum()}")

    m = temps.mean()
    s = temps.std()
    n = temps.count()
    print(f"mean {m:.2f}, s {s:.2f}, n {n}")
    print(f"standard error {s / n ** 0.5:.3f}")
    ```

    The first `print` counts the missing values, as at the prompt.
    `std()` is the standard deviation s, which divides by n − 1;
    `count()` counts the values that are not missing (`len(temps)` would
    count all 87 672 rows); `** 0.5` is the square root. In an f-string,
    `{m:.2f}` writes `m` with two decimals.

2. Run it.

    ```text
    $ python scripts/how_sure.py
    missing 120
    mean 7.16, s 8.85, n 87552
    standard error 0.030
    ```

**Check:** `standard error 0.030`: 8.85 / √87 552, the ± of 7.16 if the
hours were independent.

---

### 7. The mean of each month: `groupby` { #months }

<!-- 1:05 · 10 min -->

`groupby` puts together the rows with the same key, and a method then works on each group.

1. At the end of `how_sure.py`, add these lines, save.

    ```python

    month = df["time"].str[5:7]
    print(df.groupby(month)["temp_c"].mean().round(1))
    ```

    `.str[5:7]` cuts characters 5 and 6 out of every time, as `line[5:7]`
    cuts a line of text: the month, `01` to `12`.
    `df.groupby(month)["temp_c"].mean()` is the mean temperature of each
    month; `round(1)` keeps one decimal.

2. Run it. The first three lines come back, then the months.

    ```text
    $ python scripts/how_sure.py
    missing 120
    mean 7.16, s 8.85, n 87552
    standard error 0.030
    time
    01    -3.9
    02    -2.4
    03     1.2
    04     6.4
    05    12.2
    06    17.2
    07    18.5
    08    16.1
    09    13.0
    10     6.9
    11     2.6
    12    -2.3
    Name: temp_c, dtype: float64
    ```

**Check:** January −3.9 °C, July 18.5 °C: 22.4 °C between them.

---

### 8. The mean of each year, and an honest ± { #years }

<!-- 1:15 · 10 min -->

An hour nearly repeats the hour before, so the 87 552 hours are not 87 552 independent values, and 0.030 is too small. Ten yearly means are close to independent: their spread divided by √10 is the honest ±.

1. At the end of `how_sure.py`, add these lines, save.

    ```python

    year = df["time"].str[0:4]
    means = df.groupby(year)["temp_c"].mean()
    print(means.round(2))
    sy = means.std()
    print(f"years scatter by {sy:.2f}")
    print(f"mean {means.mean():.2f} ± {sy / len(means) ** 0.5:.2f}")
    ```

2. Run it. The last lines are new.

    ```text
    $ python scripts/how_sure.py
    ...
    time
    2016    7.60
    2017    6.51
    2018    7.97
    2019    7.27
    2020    6.83
    2021    7.25
    2022    6.60
    2023    8.31
    2024    7.27
    2025    5.98
    Name: temp_c, dtype: float64
    years scatter by 0.70
    mean 7.16 ± 0.22
    ```

**Check:** 7.16 ± 0.22 °C, a ± seven times larger than 0.030.

---

### 9. A histogram of the hours { #histogram }

<!-- 1:25 · 10 min -->

A histogram counts the values in bins of equal width and draws one bar per bin; here with the mean and the mean ± s drawn in.

1. Add a first line to `how_sure.py`, above `import pandas as pd`:

    ```python
    import matplotlib.pyplot as plt
    ```

2. At the end of the script, add these lines, save, run.

    ```python

    fig, ax = plt.subplots()
    ax.hist(temps.dropna(), bins=50, range=(-17, 33))
    ax.axvline(m, color="black")
    ax.axvline(m - s, color="black", linestyle="--")
    ax.axvline(m + s, color="black", linestyle="--")
    ax.set_xlabel("Hourly temperature (°C)")
    ax.set_ylabel("Hours per 1 °C")
    ax.set_title("The mean, 7.16 °C, and the mean ± s")
    fig.savefig("results/temp_hist.png", dpi=150)
    ```

    `plt.subplots()` makes a figure and its axes; `ax.hist` counts the
    values in 50 bins of 1 °C from −17 to 33 °C; `dropna()` gives the column
    without its missing values; `ax.axvline(x)` draws a vertical line at
    `x`, dashed with `linestyle="--"`; `fig.savefig` writes the figure to a
    file.

3. In the Explorer, click `results/temp_hist.png`: two peaks, near −1 °C
   and near 12 °C, the mean in the dip between them, and the dashed lines
   at −1.7 and 16.0 °C.

**Check:** a solid line at 7.16 and two dashed lines, 8.85 °C to either
side.

!!! question "Task: how many hours lie within the mean ± s?"
    A Gaussian holds 68.3 % of its values within the mean ± s. Count the
    share of the hours there: `temps[(temps > m - s) & (temps < m + s)]`
    keeps them (`&` is "and" for two Series).

??? success "Answer"
    At the end of `how_sure.py`:

    ```python

    inside = temps[(temps > m - s) & (temps < m + s)]
    print(f"within the mean ± s: {inside.count() / n:.3f}")
    ```

    ```text
    $ python scripts/how_sure.py
    ...
    within the mean ± s: 0.626
    ```

    62.6 %, not 68.3 %: two peaks put fewer hours near the mean than a
    Gaussian would.

---

### 10. Write the answer into the README { #readme }

<!-- 1:35 · 5 min -->

The number goes into the README with its ±, how the ± was found, and the script that computes it.

1. At the end of `README.md`, add and save:

    ```text

    ## How sure is the mean

    7.16 ± 0.22 °C: the standard error of the ten yearly means, which
    scatter by 0.70 °C. The hours are not independent, so
    8.85 / √87 552 = 0.030 °C is too small. Left out: 120 hours of
    -999, 22 to 26 July 2019. `scripts/how_sure.py` computes it.
    ```

2. Run the script once more and compare: the README is true only as long
   as the script prints the same.

    ```text
    $ python scripts/how_sure.py
    missing 120
    mean 7.16, s 8.85, n 87552
    standard error 0.030
    ...
    years scatter by 0.70
    mean 7.16 ± 0.22
    ```

**Check:** the README ends with **How sure is the mean**, and the script
prints each of its numbers: 7.16, 0.22, 0.70, 8.85, 0.030 and the 120
missing hours.

---

### 11. Wrap up { #wrap-up }

<!-- 1:40 · 5 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| make the environment of a folder | `conda env create -f environment.yml`, `conda activate analysis` |
| add a package, write it down | `conda install NAME=VERSION`, `conda env export --from-history -f environment.yml`, delete `prefix:` |
| read a CSV file | `df = pd.read_csv(PATH)`, with `na_values=[-999]` for a code that marks missing values |
| look at a table | `df.shape`, `df.head()`, `df.describe()` |
| one column | `df["temp_c"]`, `.mean()`, `.std()`, `.count()`, `.min()` |
| count | `(df["temp_c"] == -999).sum()`, `df["temp_c"].isna().sum()` |
| the standard error | `s / n ** 0.5` |
| a mean per group | `df.groupby(df["time"].str[0:4])["temp_c"].mean()` |

---

## Part 4 · Your project { #part-4 }

<!-- 1:45 to 2:00 -->

The same first steps on a data file of your own project. No data yet: help a neighbour, or go on with section 13.

---

### 12. Your project: read it, look at it, one mean with its ± { #project }

<!-- 1:45 · 15 min -->

Nothing new: the lines of sections 3 to 6, with your file and your column.

1. Your project folder, with the folders `data/raw`, `data/processed`,
   `scripts` and `results`. If you have none, make one (any name, here
   `project`), and give it today's `environment.yml`: your project uses
   `analysis` too.

    ```text
    $ mkdir -p ~/project/data/raw ~/project/data/processed ~/project/scripts ~/project/results
    $ cp ~/weather-s08/environment.yml ~/project/
    ```

2. **File** > **Open Folder...** > `project` > **Open**. Open the terminal
   again (**View** > **Terminal**): it starts in `project`. Switch the
   environment on. A folder without a `README.md` gets one: in the
   Explorer, **New File...**, `README.md`.

    ```text
    $ conda activate analysis
    ```

3. Copy your file into `data/raw`, as it arrived: drag it onto `data/raw`
   in VS Code's Explorer, or `cp ~/Downloads/YOUR_FILE.csv data/raw/`.
4. Read it at Python's prompt, with your file's name, and look.

    ```pycon
    $ python
    >>> import pandas as pd
    >>> df = pd.read_csv("data/raw/YOUR_FILE.csv")
    >>> df.shape
    >>> df.head()
    >>> df.describe()
    ```

5. Pick one numeric column: its mean and its standard error.

    ```pycon
    >>> col = df["YOUR_COLUMN"]
    >>> m = col.mean()
    >>> s = col.std()
    >>> n = col.count()
    >>> print(f"{m:.2f} ± {s / n ** 0.5:.2f}")
    ```

6. In your project's `README.md`, a section **A first look at the data**:
   the file, its rows and columns, the missing values and how the file
   marks them, and the mean of one column with its ±. Add one sentence on
   whether the rows are independent: rows in time order rarely are, and
   then the ± is too small.

**Check:** your README holds one mean with its ± and the sentence on
independence.

??? tip "One column only, or numbers cut at a comma?"
    A spreadsheet with European settings writes `;` between the values and
    a comma in decimals, as `daily_export.csv` of today's folder does. Try
    it there: `cd ~/weather-s08`, `python`, `import pandas as pd`. Read as a
    plain CSV, `6,3` is cut in two:

    ```pycon
    >>> ex = pd.read_csv("data/raw/daily_export.csv")
    >>> ex.head(3)
                    nr;date;temp_c
    1;2025-10-01;6               3
    2;2025-10-02;5               0
    3;2025-10-03;5               6
    ```

    `sep=";"` and `decimal=","` read it right; `dropna()` drops the
    summary row, which has no `nr`:

    ```pycon
    >>> ex = pd.read_csv("data/raw/daily_export.csv", sep=";", decimal=",")
    >>> ex.tail(2)
        nr        date  temp_c
    8  9.0  2025-10-09    9.80
    9  NaN        mean    7.97
    >>> ex = ex.dropna()
    >>> print(ex["temp_c"].mean())
    7.966666666666667
    ```

    A file that marks missing values with a code reads it with
    `na_values=[...]`, as `-999` in section 5.

---

## Optional, if the room goes fast { #optional }

---

### 13. Correlation: temperature and humidity { #correlation }

<!-- — · 10 min -->

The correlation coefficient r is +1 when two columns rise together along a straight line, −1 when one falls as the other rises, and 0 with no straight-line relation.

1. Back to today's folder, start `python` and read the file.

    ```pycon
    $ cd ~/weather-s08
    $ python
    >>> import pandas as pd
    >>> df = pd.read_csv("data/raw/weather.csv", na_values=[-999])
    ```

2. r of the temperature and the humidity of the same hours.

    ```pycon
    >>> print(df["temp_c"].corr(df["humidity_pct"]))
    -0.7027079498404432
    ```

3. `shift(1)` moves every value one row down: each row then holds the hour
   before. r of an hour and the hour before:

    ```pycon
    >>> df["temp_c"].shift(1).head(3)
    0    NaN
    1   -4.4
    2   -4.8
    Name: temp_c, dtype: float64
    >>> print(df["temp_c"].corr(df["temp_c"].shift(1)))
    0.9960625426692195
    ```

**Check:** −0.70: warm hours are drier. 0.996: an hour nearly repeats the
hour before, which is why 0.030 was too small.

---

### 14. The median and percentiles { #percentiles }

<!-- — · 5 min -->

A percentile is the value below which that share of the values lies; the median is the 50 % point.

1. At the prompt, with `df` read as in section 13:

    ```pycon
    >>> temps = df["temp_c"]
    >>> print(temps.median())
    6.7
    >>> temps.quantile([0.05, 0.25, 0.75, 0.95])
    0.05    -6.0
    0.25    -0.2
    0.75    14.2
    0.95    21.8
    Name: temp_c, dtype: float64
    ```

**Check:** half the hours lie below 6.7 °C; nine in ten between −6.0 and
21.8 °C.

---

### 15. Frost by counting { #frost }

<!-- — · 10 min -->

A probability counted from data is a share: the frost hours divided by all measured hours.

1. At the same prompt, with `temps` of section 14. P(frost): the mean of
   `True` and `False` is the share of `True`.

    ```pycon
    >>> frost = temps.dropna() < 0
    >>> print(frost.sum(), frost.mean())
    22352 0.25529970760233917
    ```

2. Frost given frost the hour before, over the pairs of hours that were
   both measured. `notna()` is `True` where a value is there; `~` turns
   `True` into `False`.

    ```pycon
    >>> before = temps.shift(1)
    >>> pairs = temps.notna() & before.notna()
    >>> now_frost = (temps < 0)[pairs]
    >>> before_frost = (before < 0)[pairs]
    >>> print(len(now_frost))
    87550
    >>> print(now_frost[before_frost].mean())
    0.9564672721578453
    >>> print(now_frost[~before_frost].mean())
    0.01492354177211307
    ```

**Check:** P(frost) = 0.255; given frost the hour before, 0.956; given
none, 0.015.

---

### 16. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder and open: each in `how_sure.py`, with its answer folded.

!!! question "Advanced task: the same yearly means in plain Python"
    `scripts/weather.py`, the module of the earlier seminars, has a
    function `group(path, start, stop)`: a dictionary with a list of
    temperatures for each key `line[start:stop]`, the `-999` hours left
    out. Compute the ten yearly means with it and compare them with
    `groupby`.

??? success "Answer"
    `import weather` finds `weather.py` because the script stands in the
    same folder, `scripts`. At the end of `how_sure.py`:

    ```python

    import weather

    years = weather.group("data/raw/weather.csv", 0, 4)
    for key in years:
        print(key, round(weather.mean(years[key]), 2))
    ```

    ```text
    $ python scripts/how_sure.py
    ...
    2016 7.6
    2017 6.51
    2018 7.97
    2019 7.27
    2020 6.83
    2021 7.25
    2022 6.6
    2023 8.31
    2024 7.27
    2025 5.98
    ```

    The same ten numbers as `groupby`, in a loop over the lines.

!!! question "Advanced task: one year's own ±"
    Compute the mean of 2025 with s / √n of its own hours. Compare that ±
    with how much the ten yearly means scatter.

??? success "Answer"
    ```python

    t25 = df[year == "2025"]["temp_c"]
    print(f"2025: {t25.mean():.2f} ± {t25.std() / t25.count() ** 0.5:.2f}")
    ```

    ```text
    $ python scripts/how_sure.py
    ...
    2025: 5.98 ± 0.10
    ```

    The year gives itself ± 0.10, but the years scatter by 0.70: seven
    times more. Its hours are not independent either.

!!! question "Advanced task: a mean per day"
    Group the hours by day (`df["time"].str[0:10]`). How many days, how
    many with a mean, and what is the ± from the daily means?

??? success "Answer"
    ```python

    day = df["time"].str[0:10]
    daily = df.groupby(day)["temp_c"].mean()
    print(len(daily), daily.count())
    print(f"days scatter by {daily.std():.2f}, ± {daily.std() / daily.count() ** 0.5:.2f}")
    ```

    ```text
    $ python scripts/how_sure.py
    ...
    3653 3648
    days scatter by 8.43, ± 0.14
    ```

    3653 days; 5 have no measured hour, so their mean is NaN. The days
    scatter almost as much as the hours, 8.43 against 8.85 °C, because
    neighbouring days are alike: ± 0.14 is still too small against 0.22.

---

## Aims practised

- ♻️ **Reproducibility:** one script, `how_sure.py`, computes every number
  of the README from the raw file; `environment.yml` lists pandas with its
  version.
- 📁 **Files:** the missing values are declared when the file is read and
  counted, never edited out of `data/raw`.
- 🔧 **Tool-agnostic:** the same mean, 7.16, from a loop over the lines
  and from pandas; the same lines in zsh and in Git Bash.
