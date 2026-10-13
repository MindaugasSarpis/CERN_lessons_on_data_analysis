# Seminar 12 — How Cold Is the Hill? pandas on a Second Station's File

**Paired lecture:** 12 Pandas & Data Cleaning · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student reads a second station's messy export with
pandas, cleans it rule by rule with a count for each rule, compares it day
by day with the valley station, and pushes the script and the result.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows), in the `weather-project` folder. Sections 3 to 8 are typed at
the Python prompt `>>>`.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · pandas and the new file** · 20 min | | |
| 0:00 | [1. Install pandas](#install) | `conda install pandas` | `3.0.6`, one more line in `environment.yml` |
| 0:10 | [2. Get the hill station's file](#pull) | `git pull --no-edit course main` | `data/raw/hill_station.csv`, 8 741 lines |
| | **Part 2 · Read it** · 30 min | | |
| 0:20 | [3. Separator and decimal comma](#read) | `pd.read_csv(RAW, sep=";", decimal=",")` | `temp` as `float64` |
| 0:35 | [4. -999 and empty cells](#missing) | `na_values=["-999"]`, `df.isna().sum()` | 27 and 30 missing values |
| | **Part 3 · Clean it** · 30 min | | |
| 0:50 | [5. Two units in one column](#units) | `df.loc[f, "temp"] = …` | 72 hours converted, max 28.4 |
| 1:00 | [6. Rows twice, and the hour twice](#duplicates) | `df.drop_duplicates()` | 8 716 rows |
| 1:10 | [7. Times and daily means](#daily) | `temp.resample("D").agg(…)` | 365 days, 4 too short |
| | **Part 4 · Compare, by script** · 40 min | | |
| 1:20 | [8. Join with the valley](#join) | `pd.merge(valley, day, on="time")` | hill − valley = −1.19 °C |
| 1:30 | [9. The script](#script) | `python scripts/clean_hill.py` | the log and `hill_daily.csv` |
| 1:45 | [10. Rebuild, README, push](#push) | `git push` | the work on GitHub |
| 1:55 | [11. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [12. The summer-time hour in winter time](#timezone) | `tz_localize("Europe/Vilnius")` | hourly spread 0.82 → 0.44 |
| — | [13. The difference month by month](#month) | `diff.groupby(…)`, `plot.bar` | `results/hill_by_month.png` |

**If time runs short:** skip section 8 at the prompt; the script of
section 9 holds the same lines. Sections 12 and 13 are optional.

??? info "Before the session"
    - **Room:** internet (conda downloads pandas). Each student has
      `weather-project` from [Seminar 5](seminar_05.md) on, the conda
      environment `weather`, and the remote `course` from Seminar 6.
    - **You:** nothing to prepare. The course repository has the hill
      station's file; section 2 pulls it. Ids of commits differ on every
      laptop.
    - **Keys** are written for Windows, macOS in brackets. Every line typed
      is the same on macOS and Windows.

---

## Part 1 · pandas and the new file { #part-1 }

**0:00 to 0:20** · A second station stands on a hill 4 km from the valley
station, 180 m higher. Its operator sent the hourly export of 2025.

---

### 1. Install pandas { #install }

**0:00 · 10 min** · pandas reads and cleans tables; it goes into the project's environment.

1. Open `weather-project` in VS Code, then the terminal: **View** >
   **Terminal**. Switch on the environment.

    ```text
    conda activate weather
    ```

    The prompt starts with `(weather)`.

2. pandas is not there yet.

    ```text
    python -c "import pandas"
    ```

    ```text
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
        import pandas
    ModuleNotFoundError: No module named 'pandas'
    ```

3. Install it.

    ```text
    conda install pandas
    ```

    ```text
      added / updated specs:
        - pandas
    ```

    The list below names `pandas-3.0.6`. Press `Enter` at
    `Proceed ([y]/n)?`.

4. Check.

    ```text
    python -c "import pandas; print(pandas.__version__)"
    ```

    ```text
    3.0.6
    ```

5. In `environment.yml`, add a last line and save.

    ```text
      - pandas=3.0.6
    ```

6. Look at the change, then commit it.

    ```text
    git diff
    ```

    ```text
    @@ -6,3 +6,4 @@ dependencies:
       - numpy=2.5
       - matplotlib-base=3.11
       - scipy=1.18
    +  - pandas=3.0.6
    ```

    ```text
    git commit -am "Add pandas to the environment"
    ```

    ```text
    [main 5d6364a] Add pandas to the environment
     1 file changed, 1 insertion(+)
    ```

    Your id differs.

**Check:** `3.0.6`, and `environment.yml` ends with `- pandas=3.0.6`.

!!! warning "`conda install` ran with `(base)` in the prompt"
    pandas went into `base`. Run `conda remove pandas`, then
    `conda activate weather` and install it again.

---

### 2. Get the hill station's file { #pull }

**0:10 · 10 min** · The course repository has one new file; a pull brings it.

1. Pull from the course repository.

    ```text
    git pull --no-edit course main
    ```

    ```text
    Merge made by the 'ort' strategy.
     data/raw/hill_station.csv | 8741 +++++++++++++++++++++++++++++++++++++++++++++
     1 file changed, 8741 insertions(+)
     create mode 100644 data/raw/hill_station.csv
    ```

2. The first lines.

    ```text
    head -n 4 data/raw/hill_station.csv
    ```

    ```text
    time;temp;unit;humidity
    01.01.2025 00:00;-3,9;C;100
    01.01.2025 01:00;-4,1;C;100
    01.01.2025 02:00;-4,7;C;100
    ```

3. The number of lines.

    ```text
    wc -l data/raw/hill_station.csv
    ```

    ```text
    8741 data/raw/hill_station.csv
    ```

    On macOS `wc` pads the number with spaces on the left.

**Check:** `;` between the values, a decimal comma, the day before the
month, a column `unit`. 8 741 lines: the header and 8 740 rows, for the
8 760 hours of 2025.

!!! question "Task: two odd days"
    Print the lines of 26 October 2025 from 01:00 to 05:00, then those of
    30 March 2025. What is odd, and why?

??? note "Answer"
    ```text
    grep -n '^26\.10\.2025 0[1-5]' data/raw/hill_station.csv
    ```

    ```text
    data/raw/hill_station.csv:7110:26.10.2025 01:00;-1,7;C;98
    data/raw/hill_station.csv:7111:26.10.2025 02:00;-2,3;C;97
    data/raw/hill_station.csv:7112:26.10.2025 03:00;-3,1;C;100
    data/raw/hill_station.csv:7113:26.10.2025 03:00;-2,8;C;100
    data/raw/hill_station.csv:7114:26.10.2025 04:00;-3,4;C;100
    data/raw/hill_station.csv:7115:26.10.2025 05:00;-3,2;C;100
    ```

    ```text
    grep -n '^30\.03\.2025 0[1-5]' data/raw/hill_station.csv
    ```

    ```text
    data/raw/hill_station.csv:2071:30.03.2025 01:00;5,3;C;98
    data/raw/hill_station.csv:2072:30.03.2025 02:00;5,0;C;95
    data/raw/hill_station.csv:2073:30.03.2025 04:00;4,5;C;99
    data/raw/hill_station.csv:2074:30.03.2025 05:00;4,8;C;100
    ```

    03:00 comes twice on 26 October and not at all on 30 March. The logger
    writes the local clock: summer time ended at 04:00 on 26 October
    (back to 03:00) and began at 03:00 on 30 March (on to 04:00). The
    valley's `weather.csv` has 87 672 = 3 653 × 24 rows, no hour twice and
    none missing: it keeps winter time all year.

---

## Part 2 · Read it { #part-2 }

**0:20 to 0:50** · Every option of `read_csv` answers one thing seen in the first lines.

---

### 3. Separator and decimal comma { #read }

**0:20 · 15 min** · `read_csv` assumes `,` between values and `.` as the decimal sign. This file has neither.

1. Start Python.

    ```text
    python
    ```

    The prompt is now `>>>`. Every line up to section 8 is typed here.

2. Import pandas and name the file.

    ```text
    import pandas as pd
    ```

    ```text
    RAW = "data/raw/hill_station.csv"
    ```

3. Read it with no options, and ask for its size.

    ```text
    df = pd.read_csv(RAW)
    ```

    ```text
    df.shape
    ```

    ```text
    (8740, 1)
    ```

    One column: pandas found no `,` in the header.

    ```text
    df.columns
    ```

    ```text
    Index(['time;temp;unit;humidity'], dtype='str')
    ```

4. Read it with the separator.

    ```text
    df = pd.read_csv(RAW, sep=";")
    ```

    ```text
    df.dtypes
    ```

    ```text
    time            str
    temp            str
    unit            str
    humidity    float64
    dtype: object
    ```

    `temp` is text: `-3,9` is not a number to pandas.

5. Read it with the decimal comma too.

    ```text
    df = pd.read_csv(RAW, sep=";", decimal=",")
    ```

    ```text
    df.dtypes
    ```

    ```text
    time            str
    temp        float64
    unit            str
    humidity    float64
    dtype: object
    ```

6. The first rows.

    ```text
    df.head(3)
    ```

    ```text
                   time  temp unit  humidity
    0  01.01.2025 00:00  -3.9    C     100.0
    1  01.01.2025 01:00  -4.1    C     100.0
    2  01.01.2025 02:00  -4.7    C     100.0
    ```

**Check:** `temp` and `humidity` are `float64`; 8 740 rows.

---

### 4. -999 and empty cells { #missing }

**0:35 · 15 min** · A missing value must be `NaN`, the value pandas leaves out of every mean.

1. Eight numbers per column.

    ```text
    df.describe()
    ```

    ```text
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

2. Read again, with −999 as missing.

    ```text
    df = pd.read_csv(RAW, sep=";", decimal=",", na_values=["-999"])
    ```

3. Count the missing values in each column.

    ```text
    df.isna().sum()
    ```

    ```text
    time         0
    temp        27
    unit         0
    humidity    30
    dtype: int64
    ```

4. The temperature again.

    ```text
    df["temp"].describe()
    ```

    ```text
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

??? note "Answer"
    1. 18 and 9; 18 + 9 = 27.

        ```text
        grep -c ';-999;' data/raw/hill_station.csv
        ```

        ```text
        18
        ```

        ```text
        grep -c ';;' data/raw/hill_station.csv
        ```

        ```text
        9
        ```

    2. From 2 September 12:00 to 3 September 17:00, 30 hours in a row.

        ```text
        df[df["humidity"].isna()]["time"].iloc[[0, -1]]
        ```

        ```text
        5823    02.09.2025 12:00
        5852    03.09.2025 17:00
        Name: time, dtype: str
        ```

---

## Part 3 · Clean it { #part-3 }

**0:50 to 1:20** · Each rule is a mask or a method, and each one is counted.

---

### 5. Two units in one column { #units }

**0:50 · 10 min** · The column `unit` says how each value is written.

1. Count the units.

    ```text
    df["unit"].value_counts()
    ```

    ```text
    unit
    C    8668
    F      72
    Name: count, dtype: int64
    ```

2. A mask for the rows in °F, and the first of them.

    ```text
    f = df["unit"] == "F"
    ```

    ```text
    df[f].head(3)
    ```

    ```text
                      time  temp unit  humidity
    4477  08.07.2025 10:00  63.5    F      86.0
    4478  08.07.2025 11:00  65.8    F      82.0
    4479  08.07.2025 12:00  67.8    F      78.0
    ```

3. Convert those rows: °C = (°F − 32) × 5 / 9.

    ```text
    df.loc[f, "temp"] = ((df.loc[f, "temp"] - 32) * 5 / 9).round(1)
    ```

    ```text
    df.loc[f, "unit"] = "C"
    ```

4. The same rows now.

    ```text
    df[f].head(3)
    ```

    ```text
                      time  temp unit  humidity
    4477  08.07.2025 10:00  17.5    C      86.0
    4478  08.07.2025 11:00  18.8    C      82.0
    4479  08.07.2025 12:00  19.9    C      78.0
    ```

    63.5 °F: (63.5 − 32) × 5 / 9 = 17.5 °C.

5. The largest value.

    ```text
    df["temp"].max()
    ```

    ```text
    np.float64(28.4)
    ```

**Check:** 72 rows converted, the maximum 28.4 °C.

---

### 6. Rows twice, and the hour twice { #duplicates }

**1:00 · 10 min** · A row exported twice is dropped; an hour that happened twice is kept.

1. Rows that are exact copies of an earlier row.

    ```text
    print(df.duplicated().sum())
    ```

    ```text
    24
    ```

2. Rows whose time came before.

    ```text
    print(df.duplicated(subset="time").sum())
    ```

    ```text
    25
    ```

    One more: the 03:00 of 26 October, a real second hour (Task of
    Part 1).

    ```text
    df[df["time"] == "26.10.2025 03:00"]
    ```

    ```text
                      time  temp unit  humidity
    7110  26.10.2025 03:00  -3.1    C     100.0
    7111  26.10.2025 03:00  -2.8    C     100.0
    ```

3. Which day was exported twice.

    ```text
    df[df.duplicated()]["time"].iloc[[0, -1]]
    ```

    ```text
    7732    20.11.2025 00:00
    7755    20.11.2025 23:00
    Name: time, dtype: str
    ```

4. Drop the exact copies only.

    ```text
    df = df.drop_duplicates()
    ```

    ```text
    len(df)
    ```

    ```text
    8716
    ```

**Check:** 8 740 − 24 = 8 716 rows; both 03:00 rows of 26 October are still there.

---

### 7. Times and daily means { #daily }

**1:10 · 10 min** · The valley is compared day by day, so the hours become days.

1. Turn the text into times; the format says where the day and the month are.

    ```text
    df["time"] = pd.to_datetime(df["time"], format="%d.%m.%Y %H:%M")
    ```

    ```text
    df.head(3)
    ```

    ```text
                     time  temp unit  humidity
    0 2025-01-01 00:00:00  -3.9    C     100.0
    1 2025-01-01 01:00:00  -4.1    C     100.0
    2 2025-01-01 02:00:00  -4.7    C     100.0
    ```

2. The temperature, indexed by time.

    ```text
    temp = df.set_index("time")["temp"]
    ```

3. One row per day: the mean, and the number of hours it is made of.

    ```text
    day = temp.resample("D").agg(hill="mean", hours="count")
    ```

    ```text
    day.head(3)
    ```

    ```text
                    hill  hours
    time
    2025-01-01 -3.416667     24
    2025-01-02 -5.441667     24
    2025-01-03 -6.995833     24
    ```

4. How many days, and which have fewer than 20 hours.

    ```text
    len(day)
    ```

    ```text
    365
    ```

    ```text
    day[day["hours"] < 20]
    ```

    ```text
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

??? note "Answer"
    ```text
    day.loc["2025-10-26"]
    ```

    ```text
    hill     -0.396
    hours    25.000
    Name: 2025-10-26 00:00:00, dtype: float64
    ```

    30 March has 23 hours, 26 October 25: the summer-time days.

    ```text
    day[day["hours"] != 24]
    ```

    ```text
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

**1:20 to 2:00** · The valley's daily means, joined to the hill's by date.

---

### 8. Join with the valley { #join }

**1:20 · 10 min** · `merge` keeps the dates both tables have.

1. The valley station, with −999 as missing.

    ```text
    WEATHER = "data/raw/weather.csv"
    ```

    ```text
    v = pd.read_csv(WEATHER, na_values=["-999"], parse_dates=["time"])
    ```

2. Its daily means.

    ```text
    valley = v.set_index("time")["temp_c"].resample("D").mean()
    ```

    ```text
    len(valley)
    ```

    ```text
    3653
    ```

3. Join the two by date.

    ```text
    both = pd.merge(valley, day, on="time")
    ```

    ```text
    len(both)
    ```

    ```text
    365
    ```

    3 653 days and 365 days give 365: only 2025 is in both.

4. Keep the days with 20 hours or more.

    ```text
    both = both[both["hours"] >= 20]
    ```

    ```text
    len(both)
    ```

    ```text
    361
    ```

5. Hill minus valley, on average.

    ```text
    diff = both["hill"] - both["temp_c"]
    ```

    ```text
    print(round(diff.mean(), 2))
    ```

    ```text
    -1.19
    ```

6. Leave Python.

    ```text
    exit()
    ```

**Check:** −1.19 °C over 361 days. Air cools by about 6.5 °C per km of
height: 0.18 km × 6.5 = 1.17 °C.

---

### 9. The script { #script }

**1:30 · 15 min** · The lines of sections 3 to 8 in one file, with a count for every rule.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `clean_hill.py`, press `Enter`. Write and save:

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

    f = df["unit"] == "F"
    df.loc[f, "temp"] = ((df.loc[f, "temp"] - 32) * 5 / 9).round(1)
    df.loc[f, "unit"] = "C"
    print("rows in F      ", f.sum())

    print("duplicate rows ", df.duplicated().sum())
    df = df.drop_duplicates()

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

    `lineterminator="\n"` makes the file end its lines the same way on
    macOS and Windows, so it has the same checksum on both.

2. Run it.

    ```text
    python scripts/clean_hill.py
    ```

    ```text
    rows read       8740
    temp missing    27
    rows in F       72
    duplicate rows  24
    days < 20 hours 4
    days compared   361
    hill - valley   -1.19
    ```

3. The file it wrote.

    ```text
    head -n 3 data/processed/hill_daily.csv
    ```

    ```text
    time,hill
    2025-01-01,-3.42
    2025-01-02,-5.44
    ```

    ```text
    wc -l data/processed/hill_daily.csv
    ```

    ```text
    362 data/processed/hill_daily.csv
    ```

**Check:** the seven lines of the log, and 362 lines in `hill_daily.csv`:
the header and 361 days.

---

### 10. Rebuild, README, push { #push }

**1:45 · 10 min** · The rebuild script runs the new script too, and the README says what it found.

1. In `scripts/rebuild.sh`, add a last line and save.

    ```text
    python scripts/clean_hill.py > results/hill.txt
    ```

2. Rebuild, then read the new result.

    ```text
    ./scripts/rebuild.sh
    ```

    ```text
    9 rows written to data/processed/daily.csv
    ```

    ```text
    cat results/hill.txt
    ```

    ```text
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

4. What changed.

    ```text
    git status --short
    ```

    ```text
     M README.md
     M scripts/rebuild.sh
    ?? scripts/clean_hill.py
    ```

5. Stage, commit, push.

    ```text
    git add README.md scripts/clean_hill.py scripts/rebuild.sh
    ```

    ```text
    git commit -m "Clean the hill station's file and compare it with the valley"
    ```

    ```text
    [main 40ac9f0] Clean the hill station's file and compare it with the valley
     3 files changed, 45 insertions(+)
     create mode 100644 scripts/clean_hill.py
    ```

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       bcee860..40ac9f0  main -> main
    ```

**Check:** on GitHub, `scripts/clean_hill.py` and the **Hill station**
section of the README.

!!! question "Task: what if the units were left as they are?"
    Put `#` before the two lines of `clean_hill.py` that convert the °F rows
    (`df.loc[f, …]`), run the script, read the last line. Then take the
    file back to its committed state.

??? note "Answer"
    ```text
    python scripts/clean_hill.py
    ```

    ```text
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

    ```text
    git restore scripts/clean_hill.py
    ```

---

### 11. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
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

## Optional, if the room is fast { #optional }

---

### 12. The summer-time hour in winter time { #timezone }

**— · 15 min** · Hour by hour, the hill's summer clock is one hour ahead of the valley's.

1. Start Python and run the script inside it: its tables stay.

    ```text
    python
    ```

    ```text
    exec(open("scripts/clean_hill.py").read())
    ```

    The seven lines of the log follow.

2. Join hour by hour, and take the spread of the difference.

    ```text
    hourly = v.set_index("time")["temp_c"]
    ```

    ```text
    h = pd.merge(hourly, temp, on="time")
    ```

    ```text
    print(round((h["temp"] - h["temp_c"]).std(), 2))
    ```

    ```text
    0.82
    ```

3. The 03:00 of 26 October is still there twice.

    ```text
    temp.index.is_unique
    ```

    ```text
    False
    ```

4. Say which clock the times are on, then move them to winter time,
   UTC+2 (written `Etc/GMT-2`).

    ```text
    local = temp.index.tz_localize("Europe/Vilnius", ambiguous="infer")
    ```

    ```text
    temp.index = local.tz_convert("Etc/GMT-2").tz_localize(None)
    ```

    ```text
    temp.index.is_unique
    ```

    ```text
    True
    ```

5. Join again.

    ```text
    h = pd.merge(hourly, temp, on="time")
    ```

    ```text
    print(round((h["temp"] - h["temp_c"]).std(), 2))
    ```

    ```text
    0.44
    ```

**Check:** the spread halves, from 0.82 to 0.44 °C: in summer the old join
set each hill hour beside the valley hour one hour later.

---

### 13. The difference month by month { #month }

**— · 10 min** · `groupby` splits the 361 differences by month and takes each mean.

1. At the prompt of section 12 (or after `exec(...)` again):

    ```text
    month = diff.groupby(diff.index.month).mean().round(2)
    ```

    ```text
    month
    ```

    ```text
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

2. As a bar chart, saved.

    ```text
    import matplotlib.pyplot as plt
    ```

    ```text
    month.plot.bar(xlabel="month", ylabel="hill - valley (°C)")
    ```

    ```text
    <Axes: xlabel='month', ylabel='hill - valley (°C)'>
    ```

    ```text
    plt.savefig("results/hill_by_month.png")
    ```

3. Open `results/hill_by_month.png` in the Explorer.

**Check:** twelve bars, the shortest in December (−0.82), the longest in
August (−1.63). In winter, cold air settles in the valley.

---

## Aims practised

- 📁 **Files:** a European export read as it is, with every fault named,
  counted and fixed by a rule; the raw file is never edited.
- ♻️ **Reproducibility:** the script and its log rebuild the comparison,
  and the README holds the number it prints.
- 🔧 **Tool-agnostic:** the same pandas lines at the prompt and in the
  script, the same lines in zsh on macOS and Git Bash on Windows.
