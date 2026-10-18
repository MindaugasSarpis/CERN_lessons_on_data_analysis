# Seminar 14 · Data Analysis

**Paired lecture:** 14 Concepts of Data Analysis · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** Was October 2025 unusually warm? Every student works out
by hand what the month's check computes, fixes a rule before looking,
answers the question with it, sees how many "unusual" months chance alone
gives, checks the answer under other choices, and records each step in a
commit.

Everything is typed in VS Code's terminal (zsh on macOS, Git Bash on
Windows), in today's folder `weather-s14`, with the `s14` environment active.
In the blocks, a line that starts with `$` is typed in the terminal, a line
that starts with `>>>` or `...` is typed at Python's prompt, and every
other line is what comes back.

**If time runs short:** stop after section 10; Part 4 is the table
of section 13 with four lines.

??? info "Before the session"
    - **Room:** VS Code, Miniforge (`conda`), Git with a name and e-mail
      set, and internet: section 1 downloads today's folder and makes its
      environment. Nothing from an earlier seminar is needed.
    - **You:** nothing to prepare. Today's folder is
      [`weather-s14.zip`](https://github.com/MindaugasSarpis/weather-project/releases)
      on the course repository's Releases page: the weather project with
      today's three scripts, as a Git repository with one commit. The
      numbers on this page come from `data/raw/weather.csv` and are the
      same on every laptop. Ids of commits made today differ.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · The scripts and the reference { #part-1 }

<!-- 0:00 to 0:35 -->

The question of today: was October 2025 unusually warm? First the course's script, then the same numbers by hand.

Further reading: [The Turing Way, Research data management](https://book.the-turing-way.org/reproducible-research/rdm);
[HSF Analysis Essentials](https://hsf-training.github.io/analysis-essentials/python/README.html).

---

### 1. Today's folder and its environment { #pull }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the three scripts of today and `environment.yml`; it is a Git repository with one commit.

1. On the course repository's
   [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s14.zip`. In VS Code's terminal,
   unpack it into the home folder and go in.

    ```text
    $ unzip ~/Downloads/weather-s14.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s14.zip
       creating: /Users/smilte/weather-s14/
    ...
    $ cd ~/weather-s14
    $ ls scripts
    chance_scan.py   clean_hill.py    month_check.py  scan_months.py
    clean_export.py  column_stats.py  rebuild.sh
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s14 ~` instead of `unzip`.

    `month_check.py`, `scan_months.py` and `chance_scan.py` are today's.

2. **File** > **Open Folder...** > `weather-s14`, then **View** >
   **Terminal**. One commit, and nothing changed: `git status --short`
   prints nothing.

    ```text
    $ git log --oneline
    7a606c9 The starting folder of the seminar
    $ git status --short
    ```

3. Make the conda environment `s14` from `environment.yml` (Python with
   NumPy and pandas), then switch it on: the prompt starts with `(s14)`.

    ```text
    $ conda env create -n s14 -f environment.yml
    ...
    #     $ conda activate s14
    $ conda activate s14
    ```

**Check:** `(s14)` in the prompt, and the three scripts of today in
`scripts`.

---

### 2. Look at the other years only { #blind }

<!-- 0:10 · 10 min -->

`month_check.py` compares a month with the same month of the other years, and hides the month itself.

1. Run it for October 2025.

    ```text
    $ python scripts/month_check.py 2025 10
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.95 °C
    2025-10    hidden: run again with --unblind
    ```

2. The first line holds the mean temperature of October in each of the nine
   years: October 2018 was the warmest, 2020 the coldest. The second line
   is their mean and their standard deviation (sd), the typical distance
   of a value from the mean.
3. Open `scripts/month_check.py` and find `if args.unblind:` near the end.
   Without `--unblind` the value of October 2025 is never printed.

**Check:** mean 7.03 °C, sd 1.95 °C, and no number for October 2025.

---

### 3. The same numbers by hand { #by-hand }

<!-- 0:20 · 15 min -->

Hours become days, days become months, and the Octobers of the other years give the reference: four lines of pandas.

1. Start Python, read the log with −999 as missing, with `time` as the
   index.

    ```pycon
    $ python
    >>> import pandas as pd
    >>> hours = pd.read_csv("data/raw/weather.csv", na_values=[-999], parse_dates=["time"], index_col="time")
    >>> temp = hours["temp_c"]
    >>> temp.head(3)
    time
    2016-01-01 00:00:00   -4.4
    2016-01-01 01:00:00   -4.8
    2016-01-01 02:00:00   -5.5
    Name: temp_c, dtype: float64
    ```

2. The mean of each day, then the mean of each month's days. `"D"` is a
   day, `"MS"` a month labelled by its first day.

    ```pycon
    >>> days = temp.resample("D").mean()
    >>> len(days)
    3653
    >>> months = days.resample("MS").mean()
    >>> len(months)
    120
    >>> months.head(3).round(2)
    time
    2016-01-01   -2.80
    2016-02-01   -1.97
    2016-03-01    0.97
    Freq: MS, Name: temp_c, dtype: float64
    ```

3. The Octobers, then those that are not 2025: a mask on the index.

    ```pycon
    >>> octobers = months[months.index.month == 10]
    >>> len(octobers)
    10
    >>> ref = octobers[octobers.index.year != 2025]
    >>> ref.round(2)
    time
    2016-10-01     6.84
    2017-10-01     6.62
    2018-10-01    10.17
    2019-10-01     7.37
    2020-10-01     3.43
    2021-10-01     6.11
    2022-10-01     5.86
    2023-10-01     7.80
    2024-10-01     9.11
    Name: temp_c, dtype: float64
    ```

4. `octobers` holds October 2025 too: printing it would unblind, so only
   `ref` is printed. The mean and the sd of the nine. pandas' `std` divides by n − 1 = 8,
   the usual sd of a sample; dividing by n = 9 gives a smaller number.
   Then leave Python.

    ```pycon
    >>> print(round(ref.mean(), 2), round(ref.std(), 2))
    7.03 1.95
    >>> print(round(ref.std(ddof=0), 2))
    1.83
    >>> exit()
    ```

**Check:** the nine values, 7.03 and 1.95: the script's second line.

!!! question "Task: the rule as two numbers"
    "Unusual" will mean more than 2 sd from the mean of the nine years. Before
    anyone looks, work out above which October mean 2025 would be unusually
    warm, and below which unusually cold.

??? success "Answer"
    ```text
    $ python -c "print(7.03 + 2 * 1.95, 7.03 - 2 * 1.95)"
    10.93 3.1300000000000003
    ```

    Above 10.93 °C warm, below 3.13 °C cold. Only 2018 (10.17) and 2020
    (3.43) came near.

---

## Part 2 · Fix the rule, then look { #part-2 }

<!-- 0:35 to 1:05 -->

A rule written after the result can be bent to fit it. A rule committed before cannot.

---

### 4. Write the rule down { #plan }

<!-- 0:35 · 10 min -->

The plan says what is compared, how, and what counts as unusual.

1. **File** > **New File...**, type `analysis_plan.md`, press `Enter`.
2. Write the plan and save. Put today's date in the second line.

    ```text
    # Plan: was October 2025 unusually warm?

    Written on 2026-10-20, before the mean of October 2025 was looked at.

    - Data: `data/raw/weather.csv`, the hours marked -999 left out.
    - The mean of a month: the mean of its daily means.
    - Reference: October of 2016 to 2024, nine values.
    - z = (October 2025 - mean of the nine) / sd of the nine.
    - Unusually warm: z above +2. Unusually cold: z below -2.
    - Reported whatever comes out: the mean, z and the verdict.
    ```

    **z** is the distance from the mean, counted in sd.

**Check:** `analysis_plan.md` in the Explorer, saved.

---

### 5. Commit the rule { #commit-plan }

<!-- 0:45 · 5 min -->

The commit records when the rule was written.

1. Stage the plan and commit it.

    ```text
    $ git add analysis_plan.md
    $ git commit -m "Fix the rule before looking at October 2025"
    [main 5917213] Fix the rule before looking at October 2025
     1 file changed, 10 insertions(+)
     create mode 100644 analysis_plan.md
    ```

    Your id differs.

**Check:** `git status --short` prints nothing.

---

### 6. Unblind: compute October 2025 { #unblind }

<!-- 0:50 · 5 min -->

Now, and only now, the value itself.

1. Run the script with `--unblind`.

    ```text
    $ python scripts/month_check.py 2025 10 --unblind
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.95 °C
    2025-10    mean 6.12 °C  z -0.47
    ```

2. Apply the rule: −0.47 lies between −2 and +2. By hand:
   (6.12 − 7.03) / 1.95 = −0.47.

**Check:** z = −0.47. October 2025 was not unusually warm; it was a little
cooler than the average October.

---

### 7. Write the result { #result }

<!-- 0:55 · 10 min -->

The answer goes into the README, in a commit after the plan.

1. In `README.md`, above `## How to rebuild`, add a section and save.

    ```text
    ## October 2025

    Mean 6.12 °C. October 2016 to 2024: mean 7.03 °C, sd 1.95 °C.
    z = -0.47: not unusual, by the rule in `analysis_plan.md`.
    ```

2. Commit every changed file at once.

    ```text
    $ git commit -am "October 2025: z = -0.47, not unusual"
    [main c1a8b66] October 2025: z = -0.47, not unusual
     1 file changed, 5 insertions(+)
    ```

3. The order in the history.

    ```text
    $ git log --oneline -n 3
    c1a8b66 October 2025: z = -0.47, not unusual
    5917213 Fix the rule before looking at October 2025
    7a606c9 The starting folder of the seminar
    ```

**Check:** the plan's commit stands below the result's commit.

!!! question "Task: November 2025, the same way"
    Check November 2025 with the same rule. Look at the reference first,
    then unblind.

??? success "Answer"
    ```text
    $ python scripts/month_check.py 2025 11
    2016 to 2024: 2.87 3.23 3.01 5.03 2.88 3.74 1.55 0.69 2.43
    reference  9 years  mean 2.83 °C  sd 1.24 °C
    2025-11    hidden: run again with --unblind
    $ python scripts/month_check.py 2025 11 --unblind
    2016 to 2024: 2.87 3.23 3.01 5.03 2.88 3.74 1.55 0.69 2.43
    reference  9 years  mean 2.83 °C  sd 1.24 °C
    2025-11    mean 0.98 °C  z -1.49
    ```

    Colder than usual, not unusually cold: −1.49 is above −2.

---

## Part 3 · Look elsewhere { #part-3 }

<!-- 1:05 to 1:40 -->

Someone else checks every month instead of one, and reports the most extreme.

---

### 8. Check all 120 months { #scan }

<!-- 1:05 · 10 min -->

`scan_months.py` applies the rule to every month of 2016 to 2025, each against the same month of the other nine years.

1. Run it. The first line counts the months beyond 2 sd; the others are
   the five largest z, by size.

    ```text
    $ python scripts/scan_months.py
    months checked 120   beyond 2 sd 11
    2025-04  mean   3.14 °C  z -8.79
    2019-07  mean  23.12 °C  z +3.94
    2020-03  mean  -1.03 °C  z -3.22
    2025-02  mean  -5.15 °C  z -3.15
    2020-10  mean   3.43 °C  z -2.65
    ```

2. Read it as a headline: "April 2025, 8.79 sd below normal".

**Check:** 11 of 120 months beyond 2 sd; April 2025 at −8.79.

---

### 9. What chance alone gives { #chance }

<!-- 1:15 · 10 min -->

`chance_scan.py` draws 2000 decades of monthly means in which no month is unusual, and scans each as section 8 did.

1. Run it. The numbers are drawn at random from a normal distribution
   with a fixed seed, so every laptop prints the same.

    ```text
    $ python scripts/chance_scan.py
    decades of pure chance  2000
    months beyond 2 sd, on average  11.3 of 120
    decades with at least one       100.0%
    largest z of a decade, median    4.0
    ```

2. Compare with section 8: 11 months beyond 2 sd is what a decade without
   any unusual month gives.
3. One month seldom crosses 2 sd by chance; of 120 months, about 11 do.
   Searching many places for the most extreme one is the
   **look-elsewhere effect**: the more places searched, the more extreme
   the best find, by chance alone.

**Check:** 11.3 by chance against 11 in the data.

---

### 10. Why April 2025 scores −8.79 { #april }

<!-- 1:25 · 15 min -->

A z far beyond what chance gives, so look at its parts.

1. April 2025 on its own.

    ```text
    $ python scripts/month_check.py 2025 4 --unblind
    2016 to 2024: 6.95 6.49 6.94 7.10 6.96 5.96 6.58 7.29 6.44
    reference  9 years  mean 6.75 °C  sd 0.41 °C
    2025-04    mean 3.14 °C  z -8.79
    ```

2. The nine Aprils lie within 1.3 °C of each other, so their sd is 0.41 °C.
   Section 2 gave 1.95 °C for October. Nine values give a rough sd.
3. Take the sd from all twelve months instead: each month minus the mean of
   its own month, 108 values (`--pooled`).

    ```text
    $ python scripts/month_check.py 2025 4 --unblind --pooled
    2016 to 2024: 6.95 6.49 6.94 7.10 6.96 5.96 6.58 7.29 6.44
    reference  9 years  mean 6.75 °C  sd 1.61 °C
    2025-04    mean 3.14 °C  z -2.24
    ```

4. The whole scan with that sd.

    ```text
    $ python scripts/scan_months.py --pooled
    months checked 120   beyond 2 sd 8
    2019-07  mean  23.12 °C  z +3.12
    2018-01  mean   0.15 °C  z +2.73
    2025-12  mean  -5.86 °C  z -2.46
    2023-06  mean  20.76 °C  z +2.37
    2020-10  mean   3.43 °C  z -2.35
    ```

**Check:** April 2025 falls from −8.79 to −2.24, one of eight months beyond
2 sd. The −8.79 came from the small sd of nine Aprils.

!!! question "Task: July 2019 and its missing days"
    July 2019 now leads, at +3.12. It is also the month in which the sensor
    was down for 5 days (the `-999` hours). Suppose those 5 days had been as
    warm as an average July, 18.11 °C. What would the month's mean and z be?
    The other 26 days have a mean of 23.12 °C.

??? success "Answer"
    ```text
    $ python -c "print(round((26 * 23.12 + 5 * 18.11) / 31, 2))"
    22.31
    $ python -c "print(round((22.31 - 18.11) / 1.61, 2))"
    2.61
    ```

    Still beyond 2 sd. With average weather on the missing days z is 2.61,
    not 3.12: the missing days are an uncertainty of their own, which no
    number of other hours would shrink.

---

## Part 4 · Other choices { #part-4 }

<!-- 1:40 to 2:15 -->

The plan made three choices. Change each, and see whether the verdict moves.

---

### 11. Another daily mean { #minmax }

<!-- 1:40 · 5 min -->

Many stations take a day's mean as (min + max) / 2, not as the mean of 24 hours.

1. Run with `--minmax`.

    ```text
    $ python scripts/month_check.py 2025 10 --unblind --minmax
    2016 to 2024: 6.83 6.60 10.13 7.31 3.34 6.00 5.85 7.75 9.08
    reference  9 years  mean 6.99 °C  sd 1.96 °C
    2025-10    mean 6.11 °C  z -0.45
    ```

**Check:** z = −0.45 against −0.47.

---

### 12. Another reference, another sd { #reference }

<!-- 1:45 · 10 min -->

The reference years and the sd were choices too.

1. Only the last five years as reference.

    ```text
    $ python scripts/month_check.py 2025 10 --unblind --first 2020
    2020 to 2024: 3.43 6.11 5.86 7.80 9.11
    reference  5 years  mean 6.46 °C  sd 2.15 °C
    2025-10    mean 6.12 °C  z -0.16
    ```

2. The sd of all twelve months, as in section 10.

    ```text
    $ python scripts/month_check.py 2025 10 --unblind --pooled
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.61 °C
    2025-10    mean 6.12 °C  z -0.57
    ```

**Check:** z from −0.57 to −0.16. Each choice moves z, none moves it near
±2.

---

### 13. The table { #push }

<!-- 1:55 · 15 min -->

The checks belong next to the result.

1. In `README.md`, under the line `z = -0.47: ...`, add a table and save.

    ```text
    | Choice | z |
    |--|--|
    | as planned | -0.47 |
    | a day's mean is (min + max) / 2 | -0.45 |
    | reference 2020 to 2024 only | -0.16 |
    | sd of all twelve months | -0.57 |
    ```

2. Look at it: right-click `README.md` > **Open Preview**.
3. Commit.

    ```text
    $ git commit -am "October 2025: the verdict under four choices"
    [main 66b033c] October 2025: the verdict under four choices
     1 file changed, 7 insertions(+)
    ```

**Check:** the preview of `README.md` shows the October 2025 section and
its table.

!!! question "Task: report the scan honestly"
    Section 8 said "April 2025, 8.79 sd below normal". Write, in two lines
    under the table, what an honest report of the scan would say instead.
    Commit it.

??? success "Answer"
    For example:

    ```text
    A scan of all 120 months finds 11 beyond 2 sd; chance alone gives 11.3.
    With the sd of all months, April 2025 is at -2.24, one of eight.
    ```

    ```text
    $ git commit -am "Report the scan of all months"
    ```

---

### 14. Wrap up { #wrap-up }

<!-- 2:10 · 5 min -->

| To | Do |
|--|--|
| months from hours | `temp.resample("D").mean().resample("MS").mean()` |
| keep the result from steering the rule | write the rule first, commit it, then unblind |
| judge one number | compare it with its spread: z = (value − mean) / sd |
| report a search | say how many places were searched and what chance gives there |
| trust a verdict | change each choice of the method and see that it holds |

---

## Optional, if the room goes fast { #optional }

---

### 15. A neighbour checks the order { #review }

<!-- — · 10 min -->

A reviewer can see from the history whether the rule came first.

1. Swap laptops with a neighbour. On theirs, list the last commits with
   their times.

    ```text
    $ git log --format="%h %ad %s" --date=format:"%H:%M" -n 4
    66b033c 15:43 October 2025: the verdict under four choices
    c1a8b66 15:43 October 2025: z = -0.47, not unusual
    5917213 15:43 Fix the rule before looking at October 2025
    7a606c9 09:00 The starting folder of the seminar
    ```

    Your ids and times differ, except the first commit's, which came in
    the zip.

2. Rerun their result.

    ```text
    $ python scripts/month_check.py 2025 10 --unblind
    ```

3. Answer three questions, out loud: Is the plan older than the result? Does
   the rerun give the README's number? Does the README give the verdict the
   plan's rule gives?

**Check:** three times yes, or a note to the neighbour saying which not.

---

### 16. A data management plan { #dmp }

<!-- — · 15 min -->

What the project's data is, where it lives, and what happens to it at the end.

1. The sizes of the raw files. macOS pads the numbers with a few more
   spaces.

    ```text
    $ wc -c data/raw/*
        180 data/raw/daily_export.csv
     234439 data/raw/hill_station.csv
    2515215 data/raw/weather.csv
    2749834 total
    ```

2. **File** > **New File...**, `DMP.md`. Write one line under each heading;
   the first three:

    ```text
    # Data management plan

    ## Data
    weather.csv, 2 515 215 bytes; hill_station.csv, 234 439 bytes;
    daily_export.csv, 180 bytes.

    ## Documentation
    README.md: source, columns, units, the -999 hours.

    ## Storage and backup
    Laptop, in a Git repository; a copy on an external disk.
    ```

3. The last three. Save.

    ```text
    ## Legal and ethical questions
    No personal data. Data under CC0, from the station's operator.

    ## Sharing and preservation
    At the end: the repository to Zenodo, with a DOI.

    ## Responsibilities
    Your Name. No cost.
    ```

4. Commit.

    ```text
    $ git add DMP.md
    $ git commit -m "Add a data management plan"
    ```

**Check:** `DMP.md` committed, six headings, a line under each.

---

### 17. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions on the same data, for a room that is done early. Each answer is one way; others are fine.

!!! question "Advanced task: is October 2025 unusually windy?"
    Answer it blind, the way of section 3, for the column `wind_ms`: the
    reference first, the rule (2 sd), then October 2025 itself.

??? success "Answer"
    At `>>>`, after the `read_csv` line of section 3:

    ```pycon
    >>> wind = hours["wind_ms"].resample("D").mean().resample("MS").mean()
    >>> oct_wind = wind[wind.index.month == 10]
    >>> wref = oct_wind[oct_wind.index.year != 2025]
    >>> print(" ".join(f"{x:.2f}" for x in wref))
    3.66 3.13 3.59 2.96 2.75 4.50 3.69 4.33 2.50
    >>> print(round(wref.mean(), 2), round(wref.std(), 2))
    3.46 0.68
    ```

    The rule: unusual above 3.46 + 2 × 0.68 = 4.82 m/s or below 2.10 m/s.
    Only then:

    ```pycon
    >>> value = oct_wind[oct_wind.index.year == 2025].iloc[0]
    >>> print(round(value, 2), round((value - wref.mean()) / wref.std(), 2))
    4.41 1.4
    ```

    4.41 m/s, z = 1.4: windier than most Octobers, not unusual.

!!! question "Advanced task: one month, by chance"
    `chance_scan.py` counts the months beyond 2 sd in a whole decade. How
    often is **one** given month, decided beforehand, beyond 2 sd by
    chance alone? Many expect 5 %, the share of a normal distribution
    beyond 2 sd. Change a copy of `chance_scan.py` to find out.

??? success "Answer"
    `scripts/chance_one.py`: the last year's October against the nine
    before it, in each of 2000 decades:

    ```python
    import numpy as np

    rng = np.random.default_rng(2026)
    decades = 2000
    hits = 0
    for _ in range(decades):
        months = rng.normal(0, 1, size=(10, 12))
        ref = months[:9, 9]                 # October of the nine other years
        z = (months[9, 9] - ref.mean()) / ref.std(ddof=1)
        hits += abs(z) > 2
    print(f"one month beyond 2 sd: {hits} of {decades} decades, {hits / decades:.1%}")
    ```

    ```text
    $ python scripts/chance_one.py
    one month beyond 2 sd: 191 of 2000 decades, 9.6%
    ```

    Nearly 10 %, not 5 %: the mean and the sd of nine values are
    themselves uncertain, so a z of 2 is easier to reach than with the true
    mean and sd (the t distribution with 8 degrees of freedom). The rule
    of section 4 calls one October in ten "unusual" by chance.

!!! question "Advanced task: chance with the pooled sd"
    Section 10 found 8 months beyond 2 sd with the sd of all twelve months.
    What does chance alone give for that scan?

??? success "Answer"
    In a copy of `chance_scan.py`, the sd of each year's reference is the
    pooled one: every value minus the mean of its month, squared, summed,
    divided by 108 − 12.

    ```python
    import numpy as np

    rng = np.random.default_rng(2026)
    decades = 2000
    counts = []
    for _ in range(decades):
        months = rng.normal(0, 1, size=(10, 12))
        z = np.empty_like(months)
        for y in range(10):
            ref = np.delete(months, y, axis=0)            # the other nine years
            dev = ref - ref.mean(axis=0)                  # each minus its month's mean
            sd = np.sqrt((dev ** 2).sum() / (dev.size - 12))
            z[y] = (months[y] - ref.mean(axis=0)) / sd
        counts.append(np.sum(np.abs(z) > 2))
    print(f"months beyond 2 sd, pooled sd, on average  {np.mean(counts):.1f} of 120")
    ```

    ```text
    $ python scripts/chance_pooled.py
    months beyond 2 sd, pooled sd, on average  7.3 of 120
    ```

    7.3 by chance, 8 in the data: with a better sd, the scan still finds
    what chance gives. July 2019 at +3.12 is the only month a reviewer
    might look at again, and its 5 missing days (the Task of section 10)
    weaken it.

---

## Aims practised

- ♻️ **Reproducibility:** the rule, the result and the checks are commits in
  order, and any of them reruns with one line.
- 🔧 **Tool-agnostic:** the same lines in zsh and Git Bash; the
  reasoning (z, chance, choices) holds in any language.
- 📁 **Files:** the plan is a file in the repository, so its date is the
  date of its commit.
