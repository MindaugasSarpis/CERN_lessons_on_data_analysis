# Seminar 9 — How Sure Is 7.16? Probability on the Weather Data

**Paired lecture:** 09 Probability & Statistics · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student gives the mean temperature of the weather
project with an honest uncertainty, 7.16 ± 0.22 °C, and the probability of
a frost hour in each month, commits the scripts and pushes them.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (zsh on macOS, Git Bash on Windows, with the `weather`
environment switched on).

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · The hours as a distribution** · 40 min | | |
| 0:00 | [1. Open the project](#start) | `conda activate weather`, `git pull` | `(weather)` in the prompt |
| 0:05 | [2. Read the temperature column](#read) | `scripts/distribution.py` | 87 552 valid hours |
| 0:15 | [3. Mean, standard deviation, percentiles](#summaries) | `valid.std(ddof=1)`, `np.percentile` | 7.16, 8.85, −6.0 and 21.8 |
| 0:25 | [4. The histogram](#histogram) | `ax.hist` | two humps, winter and summer |
| | **Part 2 · How sure is 7.16?** · 40 min | | |
| 0:40 | [5. The standard error](#standard-error) | `s / np.sqrt(n)` | 7.160 ± 0.030 |
| 0:45 | [6. One hour and the next](#correlation) | `np.corrcoef` | 0.996 |
| 0:55 | [7. The mean of each year](#years) | a loop over the years | 7.16 ± 0.22 |
| 1:05 | [8. Random hours against hours in a row](#simulation) | `rng.choice` | 0.28 against 7.84 |
| | **Part 3 · How often does it freeze?** · 25 min | | |
| 1:20 | [9. A frost hour, month by month](#frost) | `frost[ok].mean()` | 0.255, and 0.852 in January |
| 1:30 | [10. Frost given the hour before](#conditional) | `a[b].mean()` | 0.956 against 0.255 |
| | **Part 4 · Write it down** · 15 min | | |
| 1:45 | [11. The README, a commit, a push](#commit) | `git commit`, `git push` | the scripts on GitHub |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. Is 2025 a cold year?](#cold-year) | `math.erfc` | z = −2.17, p = 0.030 |
| — | [14. 2023 against 2025](#difference) | `math.sqrt(2) * sy` | 2.33 ± 0.99 °C |

**If time runs short:** leave out section 8 and the Task of Part 3;
section 11 stays.

??? info "Before the session"
    - **Room:** the `weather-project` repository of Seminar 6 on every
      laptop, and the `weather` environment (Python, NumPy, Matplotlib) of
      Seminars 7 and 8. Nothing is installed today.
    - **You:** nothing to prepare. The data are the same in every clone, so
      every number on this page is the number in the room. Commit ids differ.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · The hours as a distribution { #part-1 }

**0:00 to 0:40** · 87 552 hours of `temp_c`, described by a few numbers and a picture.

---

### 1. Open the project { #start }

**0:00 · 5 min** · The same repository, the same environment, the latest commits.

1. VS Code: **File** > **Open Folder...** > `weather-project`. Then
   **View** > **Terminal**.
2. Switch on the environment.

    ```text
    conda activate weather
    ```

    The prompt starts with `(weather)`.

3. Bring in any commit made on GitHub.

    ```text
    git pull
    ```

    ```text
    Already up to date.
    ```

**Check:** `(weather)` in the prompt, and `git status` ends with
`nothing to commit, working tree clean`.

---

### 2. Read the temperature column { #read }

**0:05 · 10 min** · One array of all hours, then the hours without `-999`.

1. **File** > **New File...**, name it `scripts/distribution.py`. Type and
   save.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    valid = temp[temp != -999]
    print("hours", len(temp), "valid", len(valid))
    ```

2. Run it.

    ```text
    python scripts/distribution.py
    ```

    ```text
    hours 87672 valid 87552
    ```

**Check:** 120 hours fewer in `valid`: the five days of July 2019.

---

### 3. Mean, standard deviation, percentiles { #summaries }

**0:15 · 10 min** · The mean says where the values are, the standard deviation how far they spread.

1. Add at the end of the script, save.

    ```python

    m = valid.mean()
    s = valid.std(ddof=1)
    print(f"mean {m:.2f}, standard deviation {s:.2f}")
    print("median", np.median(valid))
    print("5 % and 95 %:", np.percentile(valid, [5, 95]))
    ```

2. Run it again: `↑`, then `Enter`.

    ```text
    python scripts/distribution.py
    ```

    ```text
    hours 87672 valid 87552
    mean 7.16, standard deviation 8.85
    median 6.7
    5 % and 95 %: [-6.  21.8]
    ```

    `ddof=1` divides by N − 1, as in the lecture. 5 % of the hours are
    colder than −6.0 °C, 5 % warmer than 21.8 °C.

**Check:** mean 7.16, standard deviation 8.85.

---

### 4. The histogram { #histogram }

**0:25 · 10 min** · The picture behind the four numbers.

1. Add at the end, save, run.

    ```python

    fig, ax = plt.subplots()
    ax.hist(valid, bins=np.arange(-17, 34, 1))
    ax.set_xlabel("temp_c (°C)")
    ax.set_ylabel("hours per 1 °C bin")
    fig.savefig("results/temp_distribution.png", dpi=150)
    ```

    ```text
    python scripts/distribution.py
    ```

2. Open `results/temp_distribution.png` from the Explorer.

    Two humps: the winter hours near 0 °C (the tallest bin, −1 to 0 °C,
    holds 3848 hours) and the summer hours near 12 °C.

**Check:** the figure has two humps. It is not a Gaussian.

!!! question "Task: how far from a Gaussian?"
    1. A Gaussian has 68.3 % of its values within mean ± s. What share of
       the hours lies there?
    2. Between which two temperatures lie 98 % of the hours?

??? note "Answer"
    Add at the end of `distribution.py`:

    ```python

    inside = (valid > m - s) & (valid < m + s)
    print(f"within mean ± s: {inside.mean():.3f}")
    print("1 % and 99 %:", np.percentile(valid, [1, 99]))
    ```

    The last two lines of the run:

    ```text
    within mean ± s: 0.626
    1 % and 99 %: [-9.6 25.8]
    ```

    1. 62.6 %, not 68.3 %. 2. From −9.6 °C to 25.8 °C.

---

## Part 2 · How sure is 7.16? { #part-2 }

**0:40 to 1:20** · Lecture 9 gives the standard error s/√N. It assumes the values are independent.

---

### 5. The standard error { #standard-error }

**0:40 · 5 min** · s/√N: how far the mean of N independent values scatters.

1. New file `scripts/mean_error.py`. Type and save.

    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    ok = temp != -999
    valid = temp[ok]
    n = len(valid)
    s = valid.std(ddof=1)
    print(f"mean {valid.mean():.3f} ± {s / np.sqrt(n):.3f}")
    ```

    `dtype=str` reads the `time` column as text, used in section 7.

2. Run it.

    ```text
    python scripts/mean_error.py
    ```

    ```text
    mean 7.160 ± 0.030
    ```

**Check:** 7.160 ± 0.030 °C, if the 87 552 hours were independent.

---

### 6. One hour and the next { #correlation }

**0:45 · 10 min** · The correlation coefficient r of the lecture, between each hour and the one after it.

1. Add at the end, save.

    ```python

    r1 = np.corrcoef(valid[:-1], valid[1:])[0, 1]
    r24 = np.corrcoef(valid[:-24], valid[24:])[0, 1]
    print(f"one hour apart {r1:.3f}, one day apart {r24:.3f}")
    ```

    `valid[:-1]` is every hour but the last, `valid[1:]` every hour but the
    first: each hour beside the next.

2. Run it.

    ```text
    python scripts/mean_error.py
    ```

    ```text
    mean 7.160 ± 0.030
    one hour apart 0.996, one day apart 0.978
    ```

**Check:** 0.996. An hour nearly repeats the hour before; the hours are
not independent.

---

### 7. The mean of each year { #years }

**0:55 · 10 min** · Ten years are ten nearly independent means; their scatter shows how sure one mean is.

1. Add at the end, save.

    ```python

    year = np.array([int(t[:4]) for t in time])
    means = []
    for y in range(2016, 2026):
        means.append(temp[ok & (year == y)].mean())
    means = np.array(means)
    print(means.round(2))
    sy = means.std(ddof=1)
    print(f"years scatter by {sy:.2f}")
    print(f"mean {means.mean():.2f} ± {sy / np.sqrt(10):.2f}")
    ```

    `t[:4]` is the first four characters of a time: the year.

2. Run it.

    ```text
    python scripts/mean_error.py
    ```

    ```text
    mean 7.160 ± 0.030
    one hour apart 0.996, one day apart 0.978
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    years scatter by 0.70
    mean 7.16 ± 0.22
    ```

**Check:** 7.16 ± 0.22 °C: an uncertainty seven times larger than 0.030.

---

### 8. Random hours against hours in a row { #simulation }

**1:05 · 10 min** · A simulation: means of 1000 hours drawn at random, and of 1000 hours in a row.

1. Add at the end, save.

    ```python

    rng = np.random.default_rng(1)
    random_means = []
    row_means = []
    for i in range(2000):
        random_means.append(rng.choice(valid, 1000).mean())
        k = rng.integers(0, n - 1000)
        row_means.append(valid[k:k + 1000].mean())
    print(f"s / sqrt(1000)      {s / np.sqrt(1000):.2f}")
    print(f"1000 random hours   {np.std(random_means):.2f}")
    print(f"1000 hours in a row {np.std(row_means):.2f}")
    ```

2. Run it.

    ```text
    python scripts/mean_error.py
    ```

    The last three lines:

    ```text
    s / sqrt(1000)      0.28
    1000 random hours   0.28
    1000 hours in a row 7.84
    ```

**Check:** s/√N holds for random hours (0.28), not for hours in a row
(7.84).

!!! question "Task: one year alone"
    1. Compute the mean of 2025 with s/√N of its own 8760 hours.
    2. Compare that ± with how much the ten years scatter.
    3. How many years would give the decade's mean to ± 0.1 °C?

??? note "Answer"
    Add at the end of `mean_error.py`:

    ```python

    t25 = temp[year == 2025]
    print(f"2025: {t25.mean():.2f} ± {t25.std(ddof=1) / np.sqrt(len(t25)):.2f}")
    ```

    ```text
    2025: 5.98 ± 0.10
    ```

    1. 5.98 ± 0.10 °C. 2. The years scatter by 0.70 °C, seven times more.
    3. 0.70/√N = 0.1 gives N = (0.70/0.1)² = 49 years.

---

## Part 3 · How often does it freeze? { #part-3 }

**1:20 to 1:45** · A probability as a frequency: the share of hours below 0 °C.

---

### 9. A frost hour, month by month { #frost }

**1:20 · 10 min** · P(frost) for all hours, then for the hours of each month.

1. New file `scripts/frost_hours.py`. Type and save.

    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    ok = temp != -999
    frost = temp < 0
    print(f"P(frost) = {frost[ok].mean():.3f}")

    month = np.array([int(t[5:7]) for t in time])
    for k in range(1, 13):
        print(k, f"{frost[ok & (month == k)].mean():.3f}")
    ```

    `-999` is below 0 too, hence `frost[ok]`.

2. Run it.

    ```text
    python scripts/frost_hours.py
    ```

    ```text
    P(frost) = 0.255
    1 0.852
    2 0.747
    3 0.373
    4 0.068
    5 0.001
    6 0.000
    7 0.000
    8 0.000
    9 0.000
    10 0.053
    11 0.259
    12 0.727
    ```

**Check:** one hour in four freezes; in January 85 % of the hours.

---

### 10. Frost given the hour before { #conditional }

**1:30 · 10 min** · P(A | B), and the product rule P(A and B) = P(A) P(B), which holds only for independent events.

1. Add at the end, save.

    ```python

    f = frost[ok]
    a = f[1:]       # A: frost in this hour
    b = f[:-1]      # B: frost in the hour before
    print(f"P(A) = {a.mean():.3f}, P(B) = {b.mean():.3f}")
    print(f"P(A | B) = {a[b].mean():.3f}")
    print(f"P(A and B) = {(a & b).mean():.3f}")
    print(f"P(A) P(B)  = {a.mean() * b.mean():.3f}")
    ```

    `a[b]` keeps the hours whose hour before froze.

2. Run it.

    ```text
    python scripts/frost_hours.py
    ```

    The last four lines:

    ```text
    P(A) = 0.255, P(B) = 0.255
    P(A | B) = 0.956
    P(A and B) = 0.244
    P(A) P(B)  = 0.065
    ```

**Check:** P(A | B) = 0.956 is far from P(A) = 0.255: the events are not
independent, and 0.244 is not 0.065.

!!! question "Task: frost tomorrow morning"
    Each day has 24 rows, so `temp.reshape(-1, 24)` has one row per day.
    Compute P(frost at 06:00), and the same given that 18:00 the evening
    before was below 2 °C, and given that it was not.

??? note "Answer"
    Add at the end of `frost_hours.py`:

    ```python

    days = temp.reshape(-1, 24)
    evening = days[:-1, 18]
    morning = days[1:, 6]
    pair = (evening != -999) & (morning != -999)
    cold = morning[pair] < 0
    print(f"P(frost at 06:00) = {cold.mean():.3f}")
    chilly = evening[pair] < 2
    print(f"... if 18:00 was below 2 °C: {cold[chilly].mean():.3f}")
    print(f"... if not: {cold[~chilly].mean():.3f}")
    ```

    ```text
    P(frost at 06:00) = 0.337
    ... if 18:00 was below 2 °C: 0.984
    ... if not: 0.108
    ```

    `~` turns `True` into `False`. Seminar 11 builds a predictor on this.

---

## Part 4 · Write it down { #part-4 }

**1:45 to 2:00**

---

### 11. The README, a commit, a push { #commit }

**1:45 · 10 min** · The number goes into the README with the script that makes it.

1. At the end of `README.md`, add and save:

    ```text

    ## How sure is the mean

    7.16 ± 0.22 °C. The ± is the standard error from the ten yearly means
    (they scatter by 0.70 °C). The hours are not independent: one hour and
    the next correlate by 0.996, so s/√N = 0.03 °C is too small.
    `scripts/mean_error.py` computes it.
    ```

2. What changed.

    ```text
    git status --short
    ```

    ```text
     M README.md
    ?? scripts/distribution.py
    ?? scripts/frost_hours.py
    ?? scripts/mean_error.py
    ```

    `results/` stays out: `.gitignore` of Seminar 6.

3. Stage, commit.

    ```text
    git add README.md scripts
    ```

    ```text
    git commit -m "Add the uncertainty of the mean and the frost probabilities"
    ```

    ```text
    [main 3c589a2] Add the uncertainty of the mean and the frost probabilities
     4 files changed, 83 insertions(+)
     create mode 100644 scripts/distribution.py
     create mode 100644 scripts/frost_hours.py
     create mode 100644 scripts/mean_error.py
    ```

    Your id differs, and so do the counts if you kept the Task lines.

4. Send it to GitHub.

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       f5907be..3c589a2  main -> main
    ```

**Check:** on GitHub, `README.md` shows **How sure is the mean**.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
| mean, standard deviation | `x.mean()`, `x.std(ddof=1)` |
| median, percentiles | `np.median(x)`, `np.percentile(x, [5, 95])` |
| standard error, if independent | `s / np.sqrt(n)` |
| correlation of neighbours | `np.corrcoef(x[:-1], x[1:])[0, 1]` |
| a probability from data | `(x < 0).mean()` |
| P(A given B) | `a[b].mean()` |

Seminar 10 fits the yearly cycle to the same hours.

---

## Optional, if the room is fast { #optional }

---

### 13. Is 2025 a cold year? { #cold-year }

**— · 10 min** · The distance from the other years in units of their scatter, and its p-value.

1. Add at the end of `mean_error.py`, save, run.

    ```python

    import math
    other = means[:-1]
    z = (means[-1] - other.mean()) / other.std(ddof=1)
    print(f"2025: z = {z:.2f}, p = {math.erfc(abs(z) / math.sqrt(2)):.3f}")
    ```

    ```text
    python scripts/mean_error.py
    ```

    The last line:

    ```text
    2025: z = -2.17, p = 0.030
    ```

    `math.erfc(abs(z) / math.sqrt(2))` is the two-sided p-value of the
    Gaussian, as in the lecture.

**Check:** p = 0.030. But 2025 was picked because it looked cold. With ten
years to pick from, the chance that one of them reaches p ≤ 0.03 is
1 − 0.97¹⁰ = 0.26.

---

### 14. 2023 against 2025 { #difference }

**— · 5 min** · The uncertainty of a difference: σ√2 for two values with the same σ.

1. Add at the end, save, run.

    ```python

    diff = means[7] - means[9]
    sd = math.sqrt(2) * sy
    print(f"2023 - 2025 = {diff:.2f} ± {sd:.2f}, z = {diff / sd:.2f}")
    print(f"p = {math.erfc(diff / sd / math.sqrt(2)):.3f}")
    ```

    ```text
    python scripts/mean_error.py
    ```

    The last two lines:

    ```text
    2023 - 2025 = 2.33 ± 0.99, z = 2.34
    p = 0.019
    ```

**Check:** 2.33 ± 0.99 °C between the warmest and the coldest year of ten,
chosen after looking.

---

## Aims practised

- ♻️ **Reproducibility:** every number comes from a committed script, and
  the README says which one.
- 🔧 **Tool-agnostic:** the same `python` and `git` lines in zsh on macOS
  and in Git Bash on Windows.
- 📁 **Files:** figures stay in `results/`, out of the history; scripts and
  README go in.
