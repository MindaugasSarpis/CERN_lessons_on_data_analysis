# Seminar 14 — Was October 2025 Unusually Warm? A Blind Analysis

**Paired lecture:** 14 Concepts of Data Analysis · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student fixes a rule before looking, answers the
question with it, sees how many "unusual" months chance alone gives, checks
the answer under other choices, and pushes it all to GitHub.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows), in the weather project, with the `weather` environment active.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · The scripts and the reference** · 20 min | | |
| 0:00 | [1. Get today's scripts](#pull) | `git pull --no-edit course main` | three new scripts |
| 0:10 | [2. Look at the other years only](#blind) | `python scripts/month_check.py 2025 10` | mean 7.03, sd 1.95, October 2025 hidden |
| | **Part 2 · Fix the rule, then look** · 30 min | | |
| 0:20 | [3. Write the rule down](#plan) | `analysis_plan.md` | six lines |
| 0:30 | [4. Commit the rule](#commit-plan) | `git commit` | the rule in the history |
| 0:35 | [5. Unblind: compute October 2025](#unblind) | `--unblind` | z = −0.47: not unusual |
| 0:40 | [6. Write the result](#result) | `README.md`, `git commit -am` | plan, then result, in `git log` |
| | **Part 3 · Look elsewhere** · 35 min | | |
| 0:50 | [7. Check all 120 months](#scan) | `python scripts/scan_months.py` | 11 months beyond 2 sd |
| 1:00 | [8. What chance alone gives](#chance) | `python scripts/chance_scan.py` | 11.3 on average |
| 1:10 | [9. Why April 2025 scores −8.79](#april) | `--pooled` | −2.24 |
| | **Part 4 · Other choices** · 35 min | | |
| 1:25 | [10. Another daily mean](#minmax) | `--minmax` | −0.45 |
| 1:30 | [11. Another reference, another sd](#reference) | `--first 2020`, `--pooled` | −0.16 and −0.57 |
| 1:40 | [12. The table, then push](#push) | `git push` | the verdict under four choices on GitHub |
| 1:55 | [13. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [14. A neighbour checks the order](#review) | `git log --format=...` | the plan older than the result |
| — | [15. A data management plan](#dmp) | `DMP.md` | six headings, committed |

**If time runs short:** stop after section 9 and push; Part 4 is the table
of section 12 with four lines.

??? info "Before the session"
    - **Room:** the weather project as it stands after Seminar 13, pushed to
      the student's own GitHub repository, with the `course` remote of
      Seminar 6 and the `weather` environment (pandas in it).
    - **You:** nothing to prepare. The numbers on this page come from
      `data/raw/weather.csv` and are the same on every laptop. Commit ids
      differ.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · The scripts and the reference { #part-1 }

**0:00 to 0:20** · The question of today: was October 2025 unusually warm?

---

### 1. Get today's scripts { #pull }

**0:00 · 10 min** · Today's three scripts come from the course repository.

1. Open the weather project in VS Code, then the terminal: **View** >
   **Terminal**.
2. Activate the environment.

    ```text
    conda activate weather
    ```

    The prompt starts with `(weather)`.

3. Check that the last session left nothing uncommitted.

    ```text
    git status --short
    ```

    It prints nothing.

4. Get the scripts.

    ```text
    git pull --no-edit course main
    ```

    ```text
    From https://github.com/MindaugasSarpis/weather-project
     * branch            main       -> FETCH_HEAD
    Merge made by the 'ort' strategy.
     scripts/chance_scan.py | 32 ++++++++++++++++++++++++++
     scripts/month_check.py | 62 ++++++++++++++++++++++++++++++++++++++++++++++++++
     scripts/scan_months.py | 36 +++++++++++++++++++++++++++++
     3 files changed, 130 insertions(+)
    ```

**Check:** three new files in `scripts`.

---

### 2. Look at the other years only { #blind }

**0:10 · 10 min** · `month_check.py` compares a month with the same month of the other years, and hides the month itself.

1. Run it for October 2025.

    ```text
    python scripts/month_check.py 2025 10
    ```

    ```text
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.95 °C
    2025-10    hidden: run again with --unblind
    ```

2. The first line holds the mean temperature of October in each of the nine
   years. October 2018 was the warmest, 2020 the coldest.
3. Open `scripts/month_check.py` and find `if args.unblind:` near the end.
   Without `--unblind` the value of October 2025 is never printed.

**Check:** mean 7.03 °C, sd 1.95 °C, and no number for October 2025.

!!! question "Task: the rule as two numbers"
    "Unusual" will mean more than 2 sd from the mean of the nine years. Before
    anyone looks, work out above which October mean 2025 would be unusually
    warm, and below which unusually cold.

??? note "Answer"
    ```text
    python -c "print(7.03 + 2 * 1.95, 7.03 - 2 * 1.95)"
    ```

    ```text
    10.93 3.1300000000000003
    ```

    Above 10.93 °C warm, below 3.13 °C cold. Only 2018 (10.17) and 2020
    (3.43) came near.

---

## Part 2 · Fix the rule, then look { #part-2 }

**0:20 to 0:50** · A rule written after the result can be bent to fit it. A rule committed before cannot.

---

### 3. Write the rule down { #plan }

**0:20 · 10 min** · The plan says what is compared, how, and what counts as unusual.

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

**Check:** `analysis_plan.md` in the Explorer, saved.

---

### 4. Commit the rule { #commit-plan }

**0:30 · 5 min** · The commit records when the rule was written.

1. Stage the plan.

    ```text
    git add analysis_plan.md
    ```

2. Commit it.

    ```text
    git commit -m "Fix the rule before looking at October 2025"
    ```

    ```text
    [main b371f71] Fix the rule before looking at October 2025
     1 file changed, 10 insertions(+)
     create mode 100644 analysis_plan.md
    ```

    Your id differs.

**Check:** `git status --short` prints nothing.

---

### 5. Unblind: compute October 2025 { #unblind }

**0:35 · 5 min** · Now, and only now, the value itself.

1. Run the script with `--unblind`.

    ```text
    python scripts/month_check.py 2025 10 --unblind
    ```

    ```text
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.95 °C
    2025-10    mean 6.12 °C  z -0.47
    ```

2. Apply the rule: −0.47 lies between −2 and +2.

**Check:** z = −0.47. October 2025 was not unusually warm; it was a little
cooler than the average October.

---

### 6. Write the result { #result }

**0:40 · 10 min** · The answer goes into the README, in a commit after the plan.

1. In `README.md`, above `## How to rebuild`, add a section and save.

    ```text
    ## October 2025

    Mean 6.12 °C. October 2016 to 2024: mean 7.03 °C, sd 1.95 °C.
    z = -0.47: not unusual, by the rule in `analysis_plan.md`.
    ```

2. Commit every changed file at once.

    ```text
    git commit -am "October 2025: z = -0.47, not unusual"
    ```

    ```text
    [main fa9cfb6] October 2025: z = -0.47, not unusual
     1 file changed, 5 insertions(+)
    ```

3. The order in the history.

    ```text
    git log --oneline -n 3
    ```

    ```text
    fa9cfb6 October 2025: z = -0.47, not unusual
    b371f71 Fix the rule before looking at October 2025
    1a57bac Merge branch 'main' of https://github.com/MindaugasSarpis/weather-project
    ```

**Check:** the plan's commit stands below the result's commit.

!!! question "Task: November 2025, the same way"
    Check November 2025 with the same rule. Look at the reference first,
    then unblind.

??? note "Answer"
    ```text
    python scripts/month_check.py 2025 11
    ```

    ```text
    2016 to 2024: 2.87 3.23 3.01 5.03 2.88 3.74 1.55 0.69 2.43
    reference  9 years  mean 2.83 °C  sd 1.24 °C
    2025-11    hidden: run again with --unblind
    ```

    ```text
    python scripts/month_check.py 2025 11 --unblind
    ```

    ```text
    2016 to 2024: 2.87 3.23 3.01 5.03 2.88 3.74 1.55 0.69 2.43
    reference  9 years  mean 2.83 °C  sd 1.24 °C
    2025-11    mean 0.98 °C  z -1.49
    ```

    Colder than usual, not unusually cold: −1.49 is above −2.

---

## Part 3 · Look elsewhere { #part-3 }

**0:50 to 1:25** · Someone else checks every month instead of one, and reports the most extreme.

---

### 7. Check all 120 months { #scan }

**0:50 · 10 min** · `scan_months.py` applies the rule to every month of 2016 to 2025, each against the other nine years.

1. Run it.

    ```text
    python scripts/scan_months.py
    ```

    ```text
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

### 8. What chance alone gives { #chance }

**1:00 · 10 min** · `chance_scan.py` draws 2000 decades of monthly means in which no month is unusual, and scans each as section 7 did.

1. Run it.

    ```text
    python scripts/chance_scan.py
    ```

    ```text
    decades of pure chance  2000
    months beyond 2 sd, on average  11.3 of 120
    decades with at least one       100.0%
    largest z of a decade, median    4.0
    ```

2. Compare with section 7: 11 months beyond 2 sd is what a decade without
   any unusual month gives.
3. One month seldom crosses 2 sd by chance; of 120 months, about 11 do.
   This is the look-elsewhere effect of the lecture.

**Check:** 11.3 by chance against 11 in the data.

---

### 9. Why April 2025 scores −8.79 { #april }

**1:10 · 15 min** · A z far beyond what chance gives, so look at its parts.

1. April 2025 on its own.

    ```text
    python scripts/month_check.py 2025 4 --unblind
    ```

    ```text
    2016 to 2024: 6.95 6.49 6.94 7.10 6.96 5.96 6.58 7.29 6.44
    reference  9 years  mean 6.75 °C  sd 0.41 °C
    2025-04    mean 3.14 °C  z -8.79
    ```

2. The nine Aprils lie within 1.3 °C of each other, so their sd is 0.41 °C.
   Section 2 gave 1.95 °C for October. Nine values give a rough sd.
3. Take the sd from all twelve months instead: each month minus the mean of
   its own month, 108 values.

    ```text
    python scripts/month_check.py 2025 4 --unblind --pooled
    ```

    ```text
    2016 to 2024: 6.95 6.49 6.94 7.10 6.96 5.96 6.58 7.29 6.44
    reference  9 years  mean 6.75 °C  sd 1.61 °C
    2025-04    mean 3.14 °C  z -2.24
    ```

4. The whole scan with that sd.

    ```text
    python scripts/scan_months.py --pooled
    ```

    ```text
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

??? note "Answer"
    ```text
    python -c "print(round((26 * 23.12 + 5 * 18.11) / 31, 2))"
    ```

    ```text
    22.31
    ```

    ```text
    python -c "print(round((22.31 - 18.11) / 1.61, 2))"
    ```

    ```text
    2.61
    ```

    Still beyond 2 sd. With average weather on the missing days z is 2.61,
    not 3.12: the missing days are an uncertainty of their own, which no
    number of other hours would shrink.

---

## Part 4 · Other choices { #part-4 }

**1:25 to 2:00** · The plan made three choices. Change each, and see whether the verdict moves.

---

### 10. Another daily mean { #minmax }

**1:25 · 5 min** · Many stations take a day's mean as (min + max) / 2, not as the mean of 24 hours.

1. Run with `--minmax`.

    ```text
    python scripts/month_check.py 2025 10 --unblind --minmax
    ```

    ```text
    2016 to 2024: 6.83 6.60 10.13 7.31 3.34 6.00 5.85 7.75 9.08
    reference  9 years  mean 6.99 °C  sd 1.96 °C
    2025-10    mean 6.11 °C  z -0.45
    ```

**Check:** z = −0.45 against −0.47.

---

### 11. Another reference, another sd { #reference }

**1:30 · 10 min** · The reference years and the sd were choices too.

1. Only the last five years as reference.

    ```text
    python scripts/month_check.py 2025 10 --unblind --first 2020
    ```

    ```text
    2020 to 2024: 3.43 6.11 5.86 7.80 9.11
    reference  5 years  mean 6.46 °C  sd 2.15 °C
    2025-10    mean 6.12 °C  z -0.16
    ```

2. The sd of all twelve months, as in section 9.

    ```text
    python scripts/month_check.py 2025 10 --unblind --pooled
    ```

    ```text
    2016 to 2024: 6.84 6.62 10.17 7.37 3.43 6.11 5.86 7.80 9.11
    reference  9 years  mean 7.03 °C  sd 1.61 °C
    2025-10    mean 6.12 °C  z -0.57
    ```

**Check:** z from −0.57 to −0.16. Each choice moves z, none moves it near
±2.

---

### 12. The table, then push { #push }

**1:40 · 15 min** · The checks belong next to the result.

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
    git commit -am "October 2025: the verdict under four choices"
    ```

    ```text
    [main 0184479] October 2025: the verdict under four choices
     1 file changed, 7 insertions(+)
    ```

4. Push.

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       42e9b25..0184479  main -> main
    ```

**Check:** on GitHub, `README.md` shows the October 2025 section and its
table.

!!! question "Task: report the scan honestly"
    Section 7 said "April 2025, 8.79 sd below normal". Write, in two lines
    under the table, what an honest report of the scan would say instead.
    Commit and push it.

??? note "Answer"
    For example:

    ```text
    A scan of all 120 months finds 11 beyond 2 sd; chance alone gives 11.3.
    With the sd of all months, April 2025 is at -2.24, one of eight.
    ```

    ```text
    git commit -am "Report the scan of all months"
    ```

    ```text
    git push
    ```

---

### 13. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Do |
|--|--|
| keep the result from steering the rule | write the rule first, commit it, then unblind |
| judge one number | compare it with its spread: z = (value − mean) / sd |
| report a search | say how many places were searched and what chance gives there |
| trust a verdict | change each choice of the method and see that it holds |

---

## Optional, if the room is fast { #optional }

---

### 14. A neighbour checks the order { #review }

**— · 10 min** · A reviewer can see from the history whether the rule came first.

1. Swap laptops with a neighbour. On theirs, list the last commits with
   their dates.

    ```text
    git log --format="%h %ad %s" --date=format:"%H:%M" -n 4
    ```

    ```text
    0184479 19:50 October 2025: the verdict under four choices
    fa9cfb6 19:50 October 2025: z = -0.47, not unusual
    b371f71 19:50 Fix the rule before looking at October 2025
    1a57bac 19:50 Merge branch 'main' of https://github.com/MindaugasSarpis/weather-project
    ```

    Your ids and times differ.

2. Rerun their result.

    ```text
    python scripts/month_check.py 2025 10 --unblind
    ```

3. Answer three questions, out loud: Is the plan older than the result? Does
   the rerun give the README's number? Does the README give the verdict the
   plan's rule gives?

**Check:** three times yes, or a note to the neighbour saying which not.

---

### 15. A data management plan { #dmp }

**— · 15 min** · What the project's data is, where it lives, and what happens to it at the end.

1. The sizes of the raw files.

    ```text
    wc -c data/raw/*
    ```

    ```text
        180 data/raw/daily_export.csv
     234439 data/raw/hill_station.csv
    2515215 data/raw/weather.csv
    2749834 total
    ```

    macOS pads the numbers with a few more spaces.

2. **File** > **New File...**, `DMP.md`. Write one line under each heading.

    ```text
    # Data management plan

    ## Data
    weather.csv, 2 515 215 bytes; hill_station.csv, 234 439 bytes;
    daily_export.csv, 180 bytes.

    ## Documentation
    README.md: source, columns, units, the -999 hours.

    ## Storage and backup
    Laptop, and the private repository on GitHub.

    ## Legal and ethical questions
    No personal data. Data under CC0, from the station's operator.

    ## Sharing and preservation
    At the end: the repository to Zenodo, with a DOI.

    ## Responsibilities
    Your Name. No cost.
    ```

3. Commit and push.

    ```text
    git add DMP.md
    ```

    ```text
    git commit -m "Add a data management plan"
    ```

    ```text
    git push
    ```

**Check:** `DMP.md` on GitHub, six headings, a line under each.

---

## Aims practised

- ♻️ **Reproducibility:** the rule, the result and the checks are commits in
  order, and any of them reruns with one line.
- 🔧 **Tool-agnostic:** the same lines in zsh and Git Bash; the
  reasoning (z, chance, choices) holds in any language.
- 📁 **Files:** the plan is a file in the repository, so its date is the
  date of its commit.
