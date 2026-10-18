# Seminar 12 · Pandas

**Paired lecture:** 12 Pandas & Data Cleaning · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** How cold is the hill? Every student reads a second station's messy export with
pandas, cleans it rule by rule with a count for each rule, compares it day
by day with the valley station, and writes the result into the README.

Everything is typed in VS Code's terminal (zsh on macOS, Git Bash on
Windows), in today's folder `weather-s12`. In the blocks, a line that
starts with `$` is typed in the terminal, a line that starts with `>>>` or
`...` is typed at Python's prompt, and every other line is what comes back.

**If time runs short:** skip section 9 at the prompt; the script of
section 10 holds the same lines. Sections 13 to 15 are optional.

??? info "Before the session"
    - **Room:** VS Code, Miniforge (`conda`) and internet: section 1
      downloads today's folder and makes its conda environment (about 200
      packages, a few minutes the first time). Nothing from an earlier
      seminar is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** nothing to prepare. Today's folder is
      [`weather-s12.zip`](https://github.com/MindaugasSarpis/weather-project/releases)
      on the course repository's Releases page; it holds the valley's log,
      the hill station's export and `environment.yml`.
    - **Keys** are written for Windows, macOS in brackets. Every line typed
      is the same on macOS and Windows.

---

## Part 1 · pandas and the new file { #part-1 }

<!-- 0:00 to 0:20 -->

A second station stands on a hill 4 km from the valley station, 180 m higher. Its operator sent the hourly export of 2025.

Further reading: [pandas, 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html);
[HSF Analysis Essentials, Pandas](https://hsf-training.github.io/analysis-essentials/python/README.html).

---

### 1. Today's folder, its environment and pandas { #install }

<!-- 0:00 · 10 min -->

Everything for today is in one zip. **pandas**, which reads and cleans tables, is a package: it goes into the folder's conda environment and into `environment.yml`.

1. On the course repository's
   [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s12.zip`. In VS Code, **View** >
   **Terminal**, then unpack it into the home folder and go in.

    ```text
    $ unzip ~/Downloads/weather-s12.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s12.zip
       creating: /Users/smilte/weather-s12/
    ...
    $ cd ~/weather-s12
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s12 ~` instead of `unzip`.

2. **File** > **Open Folder...** > `weather-s12`, then **View** >
   **Terminal** again: the terminal now starts in the folder.

3. Make the conda environment `s12` from the folder's `environment.yml`:
   Python 3.14 with NumPy, Matplotlib and SciPy. It ends with the line to
   switch it on; type it. The prompt then starts with `(s12)`.

    ```text
    $ conda env create -n s12 -f environment.yml
    ...
    #     $ conda activate s12
    $ conda activate s12
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

4. pandas is not there yet. `python -c` runs one line of Python from the
   shell.

    ```text
    $ python -c "import pandas"
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
        import pandas
    ModuleNotFoundError: No module named 'pandas'
    ```

5. Install pandas 3.0.6 from conda-forge. conda shows its plan and asks;
   press `Enter` at `Proceed ([y]/n)?`. Then check the version.

    ```text
    $ conda install pandas=3.0.6
      added / updated specs:
        - pandas=3.0.6
    ...
    $ python -c "import pandas; print(pandas.__version__)"
    3.0.6
    ```

6. Write the environment down again. `--from-history` lists only what was
   asked for, with the versions typed.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

7. In `environment.yml`, delete the last line, `prefix: ...` (it names a
   folder on this laptop only), save, and look at the file.

    ```text
    $ cat environment.yml
    name: s12
    channels:
      - conda-forge
    dependencies:
      - jupyterlab=4.6
      - matplotlib-base=3.11
      - numpy=2.5
      - python=3.14
      - scipy=1.18
      - pandas=3.0.6
    ```

**Check:** `(s12)` in the prompt, `3.0.6`, and `environment.yml` ends with
`- pandas=3.0.6`.

!!! warning "`conda install` ran with `(base)` in the prompt"
    pandas went into `base`. Run `conda remove pandas`, then
    `conda activate s12` and install it again.

---

### 2. The hill station's file { #pull }

<!-- 0:10 · 10 min -->

The hill's export is `data/raw/hill_station.csv`, next to the valley's `weather.csv`. First a look in the shell.

1. The first lines. Look at what separates the values and how a decimal
   is written.

    ```text
    $ head -n 4 data/raw/hill_station.csv
    time;temp;unit;humidity
    01.01.2025 00:00;-3,9;C;100
    01.01.2025 01:00;-4,1;C;100
    01.01.2025 02:00;-4,7;C;100
    ```

2. The number of lines. On macOS `wc` pads the number with spaces on the
   left.

    ```text
    $ wc -l data/raw/hill_station.csv
    8741 data/raw/hill_station.csv
    ```

**Check:** `;` between the values, a decimal comma, the day before the
month, a column `unit`. 8 741 lines: the header and 8 740 rows, for the
8 760 hours of 2025.

!!! question "Task: two odd days"
    Print the lines of 26 October 2025 from 01:00 to 05:00, then those of
    30 March 2025. What is odd, and why?

??? success "Answer"
    ```text
    $ grep -n '^26\.10\.2025 0[1-5]' data/raw/hill_station.csv
    7110:26.10.2025 01:00;-1,7;C;98
    7111:26.10.2025 02:00;-2,3;C;97
    7112:26.10.2025 03:00;-3,1;C;100
    7113:26.10.2025 03:00;-2,8;C;100
    7114:26.10.2025 04:00;-3,4;C;100
    7115:26.10.2025 05:00;-3,2;C;100
    $ grep -n '^30\.03\.2025 0[1-5]' data/raw/hill_station.csv
    2071:30.03.2025 01:00;5,3;C;98
    2072:30.03.2025 02:00;5,0;C;95
    2073:30.03.2025 04:00;4,5;C;99
    2074:30.03.2025 05:00;4,8;C;100
    ```

    03:00 comes twice on 26 October and not at all on 30 March. The logger
    writes the local clock: summer time ended at 04:00 on 26 October
    (back to 03:00) and began at 03:00 on 30 March (on to 04:00). The
    valley's `weather.csv` has 87 672 = 3 653 × 24 rows, no hour twice and
    none missing: it keeps winter time all year.

---

## Part 2 · Read it { #part-2 }

<!-- 0:20 to 0:55 -->

First a table of three rows typed by hand, then the valley's clean file, then the hill's messy one: every option of `read_csv` answers one thing seen in its first lines.

---

### 3. A table in pandas: DataFrame and Series { #frame }

<!-- 0:20 · 15 min -->

A **DataFrame** is a table: named columns, numbered rows. One column of it is a **Series**.

1. Start Python. Every line up to section 9 is typed at its prompt `>>>`.
   `import pandas as pd` is the usual short name.

    ```pycon
    $ python
    >>> import pandas as pd
    ```

2. A table of the first three hours of the valley's log, typed as a
   dictionary: each key is a column name, each value the column's list.

    ```pycon
    >>> df = pd.DataFrame({"time": ["2016-01-01T00:00", "2016-01-01T01:00", "2016-01-01T02:00"], "temp_c": [-4.4, -4.8, -5.5]})
    >>> df
                   time  temp_c
    0  2016-01-01T00:00    -4.4
    1  2016-01-01T01:00    -4.8
    2  2016-01-01T02:00    -5.5
    >>> df.shape
    (3, 2)
    ```

    The numbers on the left are the **index**, the name of each row.
    `shape` is (rows, columns).

3. A column by its name, in square brackets: a Series, with the index
   beside each value. A Series has methods for the whole column.

    ```pycon
    >>> df["temp_c"]
    0   -4.4
    1   -4.8
    2   -5.5
    Name: temp_c, dtype: float64
    >>> df["temp_c"].max()
    np.float64(-4.4)
    ```

    pandas keeps numbers as NumPy's (Seminar 7): `np.float64(-4.4)` is the
    value −4.4.

4. A comparison on a column gives a Series of `True` and `False`, a
   **mask**. A mask in square brackets keeps the rows where it is `True`.

    ```pycon
    >>> df["temp_c"] < -4.5
    0    False
    1     True
    2     True
    Name: temp_c, dtype: bool
    >>> df[df["temp_c"] < -4.5]
                   time  temp_c
    1  2016-01-01T01:00    -4.8
    2  2016-01-01T02:00    -5.5
    ```

5. `df.loc[rows, column]` picks cells, and with `=` changes them: here the
   cells of the masked rows in `temp_c`.

    ```pycon
    >>> df.loc[df["temp_c"] < -4.5, "temp_c"] = -5.0
    >>> df
                   time  temp_c
    0  2016-01-01T00:00    -4.4
    1  2016-01-01T01:00    -5.0
    2  2016-01-01T02:00    -5.0
    ```

6. A file becomes a DataFrame with `read_csv`. The valley's log is a clean
   CSV, so no option is needed.

    ```pycon
    >>> v = pd.read_csv("data/raw/weather.csv")
    >>> v.shape
    (87672, 4)
    >>> v.head(3)
                   time  temp_c  humidity_pct  wind_ms
    0  2016-01-01T00:00    -4.4            93      2.5
    1  2016-01-01T01:00    -4.8            95      2.6
    2  2016-01-01T02:00    -5.5            95      2.7
    >>> v.dtypes
    time                str
    temp_c          float64
    humidity_pct      int64
    wind_ms         float64
    dtype: object
    ```

    `dtypes` is the type of each column: text (`str`), floats, integers.

7. The −999 hours are in it as numbers: a mask and `sum` count them
   (`True` counts as 1).

    ```pycon
    >>> v["temp_c"].min()
    np.float64(-999.0)
    >>> (v["temp_c"] == -999).sum()
    np.int64(120)
    ```

**Check:** `(87672, 4)`, and 120 rows of −999.

---

### 4. Separator and decimal comma { #read }

<!-- 0:35 · 10 min -->

`read_csv` assumes `,` between values and `.` as the decimal sign. The hill's file has neither.

1. Name the file, read it with no options, and ask for its size.

    ```pycon
    >>> RAW = "data/raw/hill_station.csv"
    >>> df = pd.read_csv(RAW)
    >>> df.shape
    (8740, 1)
    >>> df.columns
    Index(['time;temp;unit;humidity'], dtype='str')
    ```

    One column: pandas found no `,` in the header, so the whole line is
    one name.

2. Read it with the separator.

    ```pycon
    >>> df = pd.read_csv(RAW, sep=";")
    >>> df.dtypes
    time            str
    temp            str
    unit            str
    humidity    float64
    dtype: object
    ```

    `temp` is text: `-3,9` is not a number to pandas.

3. Read it with the decimal comma too.

    ```pycon
    >>> df = pd.read_csv(RAW, sep=";", decimal=",")
    >>> df.dtypes
    time            str
    temp        float64
    unit            str
    humidity    float64
    dtype: object
    >>> df.head(3)
                   time  temp unit  humidity
    0  01.01.2025 00:00  -3.9    C     100.0
    1  01.01.2025 01:00  -4.1    C     100.0
    2  01.01.2025 02:00  -4.7    C     100.0
    ```

**Check:** `temp` and `humidity` are `float64`; 8 740 rows.

---

### 5. -999 and empty cells { #missing }

<!-- 0:45 · 10 min -->

A missing value must be `NaN` ("not a number"), the value pandas leaves out of every mean.

1. Eight numbers per column: `describe` is the first look at any table.

    ```pycon
    >>> df.describe()
                  temp     humidity
    count  8731.000000  8710.000000
    mean      3.192005    84.451206
    std      46.800672    10.998819
    min    -999.000000    49.000000
    25%      -2.650000    76.000000
    50%       4.500000    85.000000
    75%      12.300000    94.000000
    max      73.600000   100.000000
    ```

    `min` is −999, the mark for a failed reading. `count` is below 8 740:
    the empty cells are already `NaN`.

2. Read again, with −999 as missing, and count the missing values in each
   column.

    ```pycon
    >>> df = pd.read_csv(RAW, sep=";", decimal=",", na_values=["-999"])
    >>> df.isna().sum()
    time         0
    temp        27
    unit         0
    humidity    30
    dtype: int64
    ```

3. The temperature again.

    ```pycon
    >>> df["temp"].describe()
    count    8713.000000
    mean        5.262412
    std        10.740471
    min       -17.400000
    25%        -2.600000
    50%         4.500000
    75%        12.400000
    max        73.600000
    Name: temp, dtype: float64
    ```

    The minimum is a winter night now. The maximum, 73.6, is not a
    temperature on a Lithuanian hill in °C.

**Check:** 27 missing temperatures, 30 missing humidities, and `max 73.6`.

!!! question "Task: where are the missing values?"
    1. Of the 27 missing temperatures, how many were `-999` in the file
       and how many were empty cells? Count in a second terminal (**+** in
       the terminal panel), with `grep -c`.
    2. From which hour to which hour is the humidity missing?

??? success "Answer"
    1. 18 and 9; 18 + 9 = 27.

        ```text
        $ grep -c ';-999;' data/raw/hill_station.csv
        18
        $ grep -c ';;' data/raw/hill_station.csv
        9
        ```

    2. From 2 September 12:00 to 3 September 17:00, 30 hours in a row.

        ```pycon
        >>> df[df["humidity"].isna()]["time"].iloc[[0, -1]]
        5823    02.09.2025 12:00
        5852    03.09.2025 17:00
        Name: time, dtype: str
        ```

---

## Part 3 · Clean it { #part-3 }

<!-- 0:55 to 1:25 -->

Each rule is a mask or a method, and each one is counted.

---

### 6. Two units in one column { #units }

<!-- 0:55 · 10 min -->

The column `unit` says how each value is written: the 73.6 is in °F.

1. Count the units, then make a mask for the rows in °F and look at the
   first of them.

    ```pycon
    >>> df["unit"].value_counts()
    unit
    C    8668
    F      72
    Name: count, dtype: int64
    >>> f = df["unit"] == "F"
    >>> df[f].head(3)
                      time  temp unit  humidity
    4477  08.07.2025 10:00  63.5    F      86.0
    4478  08.07.2025 11:00  65.8    F      82.0
    4479  08.07.2025 12:00  67.8    F      78.0
    ```

2. Convert those rows, °C = (°F − 32) × 5 / 9, and say so in `unit`. The
   arithmetic runs on the whole masked column at once.

    ```pycon
    >>> df.loc[f, "temp"] = ((df.loc[f, "temp"] - 32) * 5 / 9).round(1)
    >>> df.loc[f, "unit"] = "C"
    >>> df[f].head(3)
                      time  temp unit  humidity
    4477  08.07.2025 10:00  17.5    C      86.0
    4478  08.07.2025 11:00  18.8    C      82.0
    4479  08.07.2025 12:00  19.9    C      78.0
    ```

    63.5 °F: (63.5 − 32) × 5 / 9 = 17.5 °C.

3. The largest value now.

    ```pycon
    >>> df["temp"].max()
    np.float64(28.4)
    ```

**Check:** 72 rows converted, the maximum 28.4 °C.

---

### 7. Rows twice, and the hour twice { #duplicates }

<!-- 1:05 · 10 min -->

A row exported twice is dropped; an hour that happened twice is kept.

1. Rows that are exact copies of an earlier row, then rows whose time
   came before.

    ```pycon
    >>> print(df.duplicated().sum())
    24
    >>> print(df.duplicated(subset="time").sum())
    25
    ```

2. One more by time: the 03:00 of 26 October, a real second hour (the
   Task of Part 1).

    ```pycon
    >>> df[df["time"] == "26.10.2025 03:00"]
                      time  temp unit  humidity
    7110  26.10.2025 03:00  -3.1    C     100.0
    7111  26.10.2025 03:00  -2.8    C     100.0
    ```

3. Which day was exported twice: the first and the last copied row.

    ```pycon
    >>> df[df.duplicated()]["time"].iloc[[0, -1]]
    7732    20.11.2025 00:00
    7755    20.11.2025 23:00
    Name: time, dtype: str
    ```

4. Drop the exact copies only.

    ```pycon
    >>> df = df.drop_duplicates()
    >>> len(df)
    8716
    ```

**Check:** 8 740 − 24 = 8 716 rows; both 03:00 rows of 26 October are still there.

---

### 8. Times and daily means { #daily }

<!-- 1:15 · 10 min -->

The valley is compared day by day, so the hours become days.

1. Turn the text into times; the format says where the day and the month
   are (`%d.%m.%Y %H:%M`).

    ```pycon
    >>> df["time"] = pd.to_datetime(df["time"], format="%d.%m.%Y %H:%M")
    >>> df.head(3)
                     time  temp unit  humidity
    0 2025-01-01 00:00:00  -3.9    C     100.0
    1 2025-01-01 01:00:00  -4.1    C     100.0
    2 2025-01-01 02:00:00  -4.7    C     100.0
    ```

2. The temperature, indexed by time; then one row per day with
   `resample("D")`: the mean, and the number of hours it is made of.

    ```pycon
    >>> temp = df.set_index("time")["temp"]
    >>> day = temp.resample("D").agg(hill="mean", hours="count")
    >>> day.head(3)
                    hill  hours
    time
    2025-01-01 -3.416667     24
    2025-01-02 -5.441667     24
    2025-01-03 -6.995833     24
    ```

3. How many days, and which have fewer than 20 hours.

    ```pycon
    >>> len(day)
    365
    >>> day[day["hours"] < 20]
                     hill  hours
    time
    2025-02-11 -11.935714     14
    2025-02-12        NaN      0
    2025-02-13 -11.521429     14
    2025-04-14  -3.850000      6
    ```

    The logger was off from 11 February 14:00 to 13 February 09:00. On
    14 April only the six night hours are left, so that mean is too cold.

**Check:** 365 days, four of them with fewer than 20 hours.

!!! question "Task: 23 and 25 hours"
    How many hours do 30 March and 26 October have in `day`? Which other
    days do not have 24, and why?

??? success "Answer"
    ```pycon
    >>> day.loc["2025-10-26"]
    hill     -0.396
    hours    25.000
    Name: 2025-10-26 00:00:00, dtype: float64
    ```

    30 March has 23 hours, 26 October 25: the summer-time days.

    ```pycon
    >>> day[day["hours"] != 24]
                     hill  hours
    time
    2025-01-26  -4.752174     23
    2025-02-09  -9.047826     23
    2025-02-11 -11.935714     14
    2025-02-12        NaN      0
    2025-02-13 -11.521429     14
    2025-03-30   8.795652     23
    2025-04-11  -0.673913     23
    2025-04-14  -3.850000      6
    2025-04-22   1.143478     23
    2025-06-22  12.773913     23
    2025-08-13  10.908696     23
    2025-10-03   4.560870     23
    2025-10-22   6.308696     23
    2025-10-26  -0.396000     25
    2025-12-22  -8.600000     23
    ```

    The other days with 23 hours each hold one of the 9 empty cells:
    `count` counts only values that are not `NaN`.

---

## Part 4 · Compare, by script { #part-4 }

<!-- 1:25 to 2:00 -->

The valley's daily means, joined to the hill's by date; then the lines of the prompt go into a script.

---

### 9. Join with the valley { #join }

<!-- 1:25 · 10 min -->

`merge` keeps the dates both tables have.

1. The valley station again, now with −999 as missing and `time` read as
   times; then its daily means.

    ```pycon
    >>> v = pd.read_csv("data/raw/weather.csv", na_values=["-999"], parse_dates=["time"])
    >>> valley = v.set_index("time")["temp_c"].resample("D").mean()
    >>> len(valley)
    3653
    ```

2. Join the two by date, then keep the days with 20 hours or more.

    ```pycon
    >>> both = pd.merge(valley, day, on="time")
    >>> len(both)
    365
    >>> both = both[both["hours"] >= 20]
    >>> len(both)
    361
    ```

    3 653 days and 365 days give 365: only 2025 is in both.

3. Hill minus valley, on average. Then leave Python.

    ```pycon
    >>> diff = both["hill"] - both["temp_c"]
    >>> print(round(diff.mean(), 2))
    -1.19
    >>> exit()
    ```

**Check:** −1.19 °C over 361 days. Air cools by about 6.5 °C per km of
height: 0.18 km × 6.5 = 1.17 °C.

---

### 10. The script { #script }

<!-- 1:35 · 15 min -->

The lines of sections 4 to 9 in one file, with a count for every rule.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `clean_hill.py`. Write its first part: the files, the reading, two counts.

    ```python
    """Clean the hill station's export; compare it with the valley, day by day.

    Run from the project folder:  python scripts/clean_hill.py
    """
    import os

    import pandas as pd

    HILL = "data/raw/hill_station.csv"
    VALLEY = "data/raw/weather.csv"
    OUT = "data/processed/hill_daily.csv"

    df = pd.read_csv(HILL, sep=";", decimal=",", na_values=["-999"])
    print("rows read      ", len(df))
    print("temp missing   ", df["temp"].isna().sum())
    ```

2. Under it, the rules of sections 6 and 7, each with a count.

    ```python
    f = df["unit"] == "F"
    df.loc[f, "temp"] = ((df.loc[f, "temp"] - 32) * 5 / 9).round(1)
    df.loc[f, "unit"] = "C"
    print("rows in F      ", f.sum())

    print("duplicate rows ", df.duplicated().sum())
    df = df.drop_duplicates()
    ```

3. Under it, the days and the comparison of sections 8 and 9. Save.

    ```python
    df["time"] = pd.to_datetime(df["time"], format="%d.%m.%Y %H:%M")
    temp = df.set_index("time")["temp"]
    day = temp.resample("D").agg(hill="mean", hours="count")
    print("days < 20 hours", (day["hours"] < 20).sum())
    day = day[day["hours"] >= 20]
    os.makedirs("data/processed", exist_ok=True)
    day["hill"].round(2).to_csv(OUT, date_format="%Y-%m-%d", lineterminator="\n")

    v = pd.read_csv(VALLEY, na_values=["-999"], parse_dates=["time"])
    valley = v.set_index("time")["temp_c"].resample("D").mean()
    both = pd.merge(valley, day, on="time")
    diff = both["hill"] - both["temp_c"]
    print("days compared  ", len(both))
    print("hill - valley  ", round(diff.mean(), 2))
    ```

4. Run it. (`lineterminator="\n"` makes `hill_daily.csv` end its lines
   the same way on macOS and Windows, so it has the same checksum on
   both.)

    ```text
    $ python scripts/clean_hill.py
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    ```

5. The file it wrote.

    ```text
    $ head -n 3 data/processed/hill_daily.csv
    time,hill
    2025-01-01,-3.42
    2025-01-02,-5.44
    $ wc -l data/processed/hill_daily.csv
    362 data/processed/hill_daily.csv
    ```

**Check:** the seven lines of the log, and 362 lines in `hill_daily.csv`:
the header and 361 days.

---

### 11. Rebuild and README { #push }

<!-- 1:50 · 10 min -->

The rebuild script runs the new script too, and the README says what it found.

1. In `scripts/rebuild.sh`, add a last line and save. `>` writes what the
   script prints into a file.

    ```text
    python scripts/clean_hill.py > results/hill.txt
    ```

2. Rebuild, then read the new result.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    $ cat results/hill.txt
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    ```

3. In `README.md`, above `## How to rebuild`, add and save:

    ```text
    ## Hill station

    `scripts/clean_hill.py` cleans `data/raw/hill_station.csv` (2025, 4 km
    away, 180 m higher). Over 361 days the hill is 1.19 °C colder than the
    valley. The counts of each rule are in `results/hill.txt`.
    ```

4. Look at it: right-click `README.md` > **Open Preview**.

**Check:** `results/hill.txt` holds the seven lines of the log, and the
README's preview shows the **Hill station** section.

!!! question "Task: what if the units were left as they are?"
    Put `#` before the two lines of `clean_hill.py` that convert the °F rows
    (`df.loc[f, …]`), run the script, read the last line. Then remove the
    two `#` again and save.

??? success "Answer"
    ```text
    $ python scripts/clean_hill.py
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -0.81
    ```

    The four days of 8 to 11 July read 16 to 45 °C warmer than the valley
    and pull the mean from −1.19 to −0.81 °C. The script ran without an
    error.

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

| To | Type |
|--|--|
| make a table by hand | `pd.DataFrame({"col": [...], ...})` |
| one column, as a Series | `df["temp"]` |
| keep the rows of a mask | `df[df["temp"] < 0]` |
| read a European export | `pd.read_csv(FILE, sep=";", decimal=",")` |
| turn a mark into a missing value | `na_values=["-999"]` |
| count missing values | `df.isna().sum()` |
| change the rows of a mask | `df.loc[mask, "col"] = …` |
| drop exact copies | `df.drop_duplicates()` |
| text into times | `pd.to_datetime(col, format="%d.%m.%Y %H:%M")` |
| hours into days | `.resample("D").agg(hill="mean", hours="count")` |
| join two tables by a key | `pd.merge(a, b, on="time")` |

Seminar 13 makes the whole project from `data/raw` with one command.

---

## Optional, if the room goes fast { #optional }

---

### 13. The summer-time hour in winter time { #timezone }

<!-- — · 15 min -->

Hour by hour, the hill's summer clock is one hour ahead of the valley's.

1. Start Python and run the script inside it with `exec`: its tables
   (`df`, `temp`, `v`, `diff`) stay at the prompt.

    ```pycon
    $ python
    >>> exec(open("scripts/clean_hill.py").read())
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    ```

2. Join hour by hour, and take the spread (standard deviation) of the
   difference.

    ```pycon
    >>> hourly = v.set_index("time")["temp_c"]
    >>> h = pd.merge(hourly, temp, on="time")
    >>> print(round((h["temp"] - h["temp_c"]).std(), 2))
    0.82
    ```

3. The 03:00 of 26 October is still there twice, so the index is not
   unique.

    ```pycon
    >>> temp.index.is_unique
    False
    ```

4. Say which clock the times are on, then move them to winter time,
   UTC+2 (written `Etc/GMT-2`). `ambiguous="infer"` sorts out the two
   03:00 hours by their order.

    ```pycon
    >>> local = temp.index.tz_localize("Europe/Vilnius", ambiguous="infer")
    >>> temp.index = local.tz_convert("Etc/GMT-2").tz_localize(None)
    >>> temp.index.is_unique
    True
    ```

5. Join again.

    ```pycon
    >>> h = pd.merge(hourly, temp, on="time")
    >>> print(round((h["temp"] - h["temp_c"]).std(), 2))
    0.44
    ```

**Check:** the spread halves, from 0.82 to 0.44 °C: in summer the old join
set each hill hour beside the valley hour one hour later.

---

### 14. The difference month by month { #month }

<!-- — · 10 min -->

`groupby` splits the 361 differences by month and takes each mean.

1. At the prompt of section 13:

    ```pycon
    >>> month = diff.groupby(diff.index.month).mean().round(2)
    >>> month
    time
    1    -0.84
    2    -0.92
    3    -0.97
    4    -1.23
    5    -1.37
    6    -1.50
    7    -1.57
    8    -1.63
    9    -1.29
    10   -1.12
    11   -1.03
    12   -0.82
    dtype: float64
    ```

2. As a bar chart, saved into `results`.

    ```pycon
    >>> import matplotlib.pyplot as plt
    >>> month.plot.bar(xlabel="month", ylabel="hill - valley (°C)")
    <Axes: xlabel='month', ylabel='hill - valley (°C)'>
    >>> plt.savefig("results/hill_by_month.png")
    ```

3. Open `results/hill_by_month.png` in the Explorer.

**Check:** twelve bars, the shortest in December (−0.82), the longest in
August (−1.63). In winter, cold air settles in the valley.

---

### 15. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions on the same files, for a room that is done early. Each answer is one way; others are fine.

!!! question "Advanced task: find the °F rows without the column `unit`"
    Suppose the export had no column `unit`. Find the 72 rows in °F from
    the temperatures alone. Hint: from one hour to the next, the air does
    not warm by 40 °C.

??? success "Answer"
    `diff()` is each value minus the one before it. The jump into °F and
    the jump back out of it are the only two jumps above 10 °C:

    ```pycon
    >>> raw = pd.read_csv("data/raw/hill_station.csv", sep=";", decimal=",", na_values=["-999"]).drop_duplicates()
    >>> raw["time"] = pd.to_datetime(raw["time"], format="%d.%m.%Y %H:%M")
    >>> t = raw.set_index("time")["temp"]
    >>> jump = t.diff().abs()
    >>> t[jump > 10]
    time
    2025-07-08 10:00:00    63.5
    2025-07-11 10:00:00    17.0
    Name: temp, dtype: float64
    ```

    The °F rows run from 8 July 10:00 up to, not including, 11 July 10:00:
    3 days × 24 = 72 hours. A rule like this finds a fault no column
    announces; it would also flag a real front passing, so look at what it
    finds before acting on it.

!!! question "Advanced task: the humidity, the same way"
    Is the hill more or less humid than the valley? Use the hill's
    `humidity` and the valley's `humidity_pct`, day by day, on the days
    with at least 20 hours of humidity.

??? success "Answer"
    After `exec(open("scripts/clean_hill.py").read())` (section 13, step 1):

    ```pycon
    >>> hum = df.set_index("time")["humidity"].resample("D").agg(hill="mean", hours="count")
    >>> vh = v.set_index("time")["humidity_pct"].resample("D").mean()
    >>> b = pd.merge(vh, hum, on="time")
    >>> b = b[b["hours"] >= 20]
    >>> print(len(b), round((b["hill"] - b["humidity_pct"]).mean(), 2))
    360 4.55
    ```

    On 360 days, the hill's air is 4.55 percentage points more humid:
    colder air holds less water, so the same water is a higher relative
    humidity. Five days have fewer than 20 hours of humidity: the three
    days of February when the logger was off, and 2 and 3 September (12
    and 6 hours), the 30 missing hours.

!!! question "Advanced task: is there a daily cycle?"
    After section 13 (winter-time hours), take the mean of hill minus
    valley for each hour of the day. At which hour is the difference
    largest, at which smallest, and is that a cycle worth reporting?

??? success "Answer"
    ```pycon
    >>> d = h["temp"] - h["temp_c"]
    >>> by_hour = d.groupby(d.index.hour).mean().round(2)
    >>> print(by_hour.idxmin(), by_hour.min(), by_hour.idxmax(), by_hour.max())
    2 -1.21 11 -1.16
    ```

    From −1.21 °C at 02:00 to −1.16 °C at 11:00: 0.05 °C apart, against
    a spread of 0.44 °C for single hours. There is no daily cycle to
    report; the difference is the same at every hour.

---

## Aims practised

- 📁 **Files:** a European export read as it is, with every fault named,
  counted and fixed by a rule; the raw file is never edited.
- ♻️ **Reproducibility:** the script and its log rebuild the comparison,
  the README holds the number it prints, and `environment.yml` says what
  the script needs.
- 🔧 **Tool-agnostic:** the same pandas lines at the prompt and in the
  script, the same lines in zsh on macOS and Git Bash on Windows.
