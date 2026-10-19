# Seminar 9 · Statistics

**Paired lecture:** 09 Probability & Statistics · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** How sure is 7.16? Every student gives the mean temperature of the weather
project with an honest uncertainty, 7.16 ± 0.22 °C, and the probability of
a frost hour in each month, and writes the first into the README.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (zsh on macOS, Git Bash on Windows, with today's environment
`s09` switched on). In the blocks, a line that starts with `$` is
typed in the terminal, a line that starts with `>>>` or `...` is typed at
Python's prompt, and every other line is what comes back.

**If time runs short:** leave out section 8 and the Task of Part 3;
section 11 stays.

??? info "Before the session"
    - **Room:** VS Code and Miniforge on every laptop (Seminar 4, or the
      [Setup](../setup.md) page), and internet: today's folder and its
      packages download in section 1, about 170 MB the first time.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** nothing to prepare. Today's folder is the same for everyone,
      so every number on this page is the number in the room.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · The hours as a distribution { #part-1 }

<!-- 0:00 to 0:40 -->

87 552 hours of `temp_c`, described by a few numbers and a picture.

---

### 1. Get today's folder { #start }

<!-- 0:00 · 5 min -->

Today's folder holds the data, the scripts so far and `environment.yml`; nothing from an earlier seminar is needed.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases)
   of the course repository, under **Assets**, click `weather-s09.zip`.
2. Open VS Code, then **View** > **Terminal**. Unpack the zip into the
   home folder and go there. Git Bash shows `/c/Users/smilte/...`.

    ```text
    $ unzip ~/Downloads/weather-s09.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s09.zip
       creating: /Users/smilte/weather-s09/
    ...
      inflating: /Users/smilte/weather-s09/scripts/weather.py
    $ cd ~/weather-s09
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s09 ~` instead of `unzip`.

3. **File** > **Open Folder...** > `weather-s09`. VS Code opens a new
   window; **View** > **Terminal** there starts in the folder.
4. Make today's environment from `environment.yml`: Python, NumPy,
   Matplotlib and JupyterLab, in the versions the file names. conda keeps
   what it downloads, so the next seminar's environment is quicker.

    ```text
    $ conda env create -n s09 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s09
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. Switch it on. The prompt then starts with `(s09)`.

    ```text
    $ conda activate s09
    $ python -c "import numpy, matplotlib; print(numpy.__version__, matplotlib.__version__)"
    2.5.4 3.11.2
    ```

**Check:** `(s09)` in the prompt, and `2.5.4 3.11.2`.

---

### 2. Read the temperature column { #read }

<!-- 0:05 · 10 min -->

One array of all hours, then the hours without `-999`.

1. **File** > **New File...**, name it `scripts/distribution.py`. Type and
   save. `usecols=1` is the second column, `temp_c` (columns count from
   0); `skiprows=1` skips the header line.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    valid = temp[temp != -999]
    print("hours", len(temp), "valid", len(valid))
    ```

2. Run it. `temp != -999` is an array of `True` and `False`, one per
   hour; `temp[...]` keeps the hours where it is `True`.

    ```text
    $ python scripts/distribution.py
    hours 87672 valid 87552
    ```

**Check:** 120 hours fewer in `valid`: the five days of July 2019.

---

### 3. Mean, standard deviation, percentiles { #summaries }

<!-- 0:15 · 10 min -->

The mean says where the values are, the standard deviation how far they spread around it.

1. First by hand, on the first five hours of 2016. Start `python` in the
   terminal. The mean is the sum divided by the count.

    ```pycon
    $ python
    >>> t = [-4.4, -4.8, -5.5, -6.0, -5.9]
    >>> m = sum(t) / len(t)
    >>> m
    -5.32
    ```

2. The **standard deviation** s: square each distance from the mean, add
   them, divide by N − 1, take the square root. N − 1, not N, because the
   mean was taken from the same five values.

    ```pycon
    >>> total = 0
    >>> for x in t:
    ...     total = total + (x - m) ** 2
    ...
    >>> total / (len(t) - 1)
    0.48699999999999993
    >>> (total / (len(t) - 1)) ** 0.5
    0.697853852894716
    ```

3. NumPy does the same in one call each. `ddof=1` asks for N − 1; without
   it NumPy divides by N.

    ```pycon
    >>> import numpy as np
    >>> a = np.array(t)
    >>> print(a.mean(), a.std(ddof=1))
    -5.32 0.697853852894716
    >>> print(a.std())
    0.6241794613730893
    ```

4. The **median** is the middle value once sorted; a **percentile** is the
   value below which that share of the values lies. Then `exit()`.

    ```pycon
    >>> print(np.median(a))
    -5.5
    >>> print(np.percentile(a, [25, 75]))
    [-5.9 -4.8]
    >>> exit()
    ```

5. Now on all hours. Add at the end of `distribution.py`, save.

    ```python

    m = valid.mean()
    s = valid.std(ddof=1)
    print(f"mean {m:.2f}, standard deviation {s:.2f}")
    print("median", np.median(valid))
    print("5 % and 95 %:", np.percentile(valid, [5, 95]))
    ```

6. Run it again: `↑`, then `Enter`. 5 % of the hours are colder than
   −6.0 °C, 5 % warmer than 21.8 °C.

    ```text
    $ python scripts/distribution.py
    hours 87672 valid 87552
    mean 7.16, standard deviation 8.85
    median 6.7
    5 % and 95 %: [-6.  21.8]
    ```

**Check:** mean 7.16, standard deviation 8.85.

---

### 4. The histogram { #histogram }

<!-- 0:25 · 10 min -->

A **histogram** counts the values in bins: here one bin per 1 °C, from −17 to 34 °C.

1. Add at the end, save.

    ```python

    fig, ax = plt.subplots()
    ax.hist(valid, bins=np.arange(-17, 34, 1))
    ax.set_xlabel("temp_c (°C)")
    ax.set_ylabel("hours per 1 °C bin")
    fig.savefig("results/temp_distribution.png", dpi=150)
    ```

2. Run it. It prints the same four lines and writes the figure.

    ```text
    $ python scripts/distribution.py
    ```

3. Open `results/temp_distribution.png` from the Explorer. Two humps: the
   winter hours near 0 °C (the tallest bin, −1 to 0 °C, holds 3848 hours)
   and the summer hours near 12 °C.

**Check:** the figure has two humps. It is not a Gaussian, the single
symmetric bell that many formulas assume.

!!! question "Task: how far from a Gaussian?"
    1. A Gaussian has 68.3 % of its values within mean ± s. What share of
       the hours lies there?
    2. Between which two temperatures lie 98 % of the hours?

??? success "Answer"
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

    1. 62.6 %, not 68.3 %. `&` is "and" for arrays; the mean of `True`
       and `False` is the share of `True`. 2. From −9.6 °C to 25.8 °C.

---

## Part 2 · How sure is 7.16? { #part-2 }

<!-- 0:40 to 1:20 -->

The **standard error** s/√N says how far the mean of N values would move if the measurement were repeated; it holds only when the values are independent.

---

### 5. The standard error { #standard-error }

<!-- 0:40 · 5 min -->

s/√N: the more values, the closer their mean to the true one.

1. New file `scripts/mean_error.py`. Type and save. `dtype=str` reads
   the `time` column as text; section 7 needs it.

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

2. Run it. 8.85/√87552 = 0.030.

    ```text
    $ python scripts/mean_error.py
    mean 7.160 ± 0.030
    ```

**Check:** 7.160 ± 0.030 °C, if the 87 552 hours were independent.

---

### 6. One hour and the next { #correlation }

<!-- 0:45 · 10 min -->

The **correlation coefficient** r is +1 when two series rise and fall together, 0 when one says nothing about the other.

1. Add at the end, save. `valid[:-1]` is every hour but the last,
   `valid[1:]` every hour but the first: each hour beside the next.

    ```python

    r1 = np.corrcoef(valid[:-1], valid[1:])[0, 1]
    r24 = np.corrcoef(valid[:-24], valid[24:])[0, 1]
    print(f"one hour apart {r1:.3f}, one day apart {r24:.3f}")
    ```

2. Run it.

    ```text
    $ python scripts/mean_error.py
    mean 7.160 ± 0.030
    one hour apart 0.996, one day apart 0.978
    ```

**Check:** 0.996. An hour nearly repeats the hour before; the hours are
not independent.

---

### 7. The mean of each year { #years }

<!-- 0:55 · 10 min -->

Ten years are ten nearly independent means; their scatter shows how sure one mean is.

1. Add at the end, save. `t[:4]` is the first four characters of a time:
   the year.

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

2. Run it. The standard error of ten yearly means is their scatter
   divided by √10.

    ```text
    $ python scripts/mean_error.py
    mean 7.160 ± 0.030
    one hour apart 0.996, one day apart 0.978
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    years scatter by 0.70
    mean 7.16 ± 0.22
    ```

**Check:** 7.16 ± 0.22 °C: an uncertainty seven times larger than 0.030.

---

### 8. Random hours against hours in a row { #simulation }

<!-- 1:05 · 10 min -->

A **simulation** repeats a measurement on the computer: 2000 times the mean of 1000 hours drawn at random, and of 1000 hours in a row.

1. Add at the end, save. `rng.choice(valid, 1000)` draws 1000 hours at
   random; `valid[k:k + 1000]` takes 1000 hours in a row from a random
   start `k`.

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

2. Run it. The last three lines are new; the seed `1` makes every laptop
   draw the same hours.

    ```text
    $ python scripts/mean_error.py
    ...
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

??? success "Answer"
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

<!-- 1:20 to 1:45 -->

A probability as a frequency: the share of hours below 0 °C.

---

### 9. A frost hour, month by month { #frost }

<!-- 1:20 · 10 min -->

P(frost) is the number of frost hours divided by the number of hours: the mean of an array of `True` (1) and `False` (0).

1. New file `scripts/frost_hours.py`. Type and save. `-999` is below 0
   too, hence `frost[ok]`; `t[5:7]` is the month.

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

2. Run it.

    ```text
    $ python scripts/frost_hours.py
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

<!-- 1:30 · 10 min -->

P(A | B), "A given B", is the share of A among the cases where B happened. A and B are **independent** when P(A | B) = P(A); only then P(A and B) = P(A) P(B).

1. Add at the end, save. `a[b]` keeps the hours whose hour before froze.

    ```python

    f = frost[ok]
    a = f[1:]       # A: frost in this hour
    b = f[:-1]      # B: frost in the hour before
    print(f"P(A) = {a.mean():.3f}, P(B) = {b.mean():.3f}")
    print(f"P(A | B) = {a[b].mean():.3f}")
    print(f"P(A and B) = {(a & b).mean():.3f}")
    print(f"P(A) P(B)  = {a.mean() * b.mean():.3f}")
    ```

2. Run it. The last four lines are new.

    ```text
    $ python scripts/frost_hours.py
    ...
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

??? success "Answer"
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

<!-- 1:45 to 2:00 -->

The numbers go into the README, with the scripts that make them.

---

### 11. Write the answer into the README { #commit }

<!-- 1:45 · 10 min -->

The number goes into the README with the script that makes it.

1. At the end of `README.md`, add and save:

    ```text

    ## How sure is the mean

    7.16 ± 0.22 °C. The ± is the standard error from the ten yearly means
    (they scatter by 0.70 °C). The hours are not independent: one hour and
    the next correlate by 0.996, so s/√N = 0.03 °C is too small.
    `scripts/mean_error.py` computes it.
    ```

2. Check that the script still gives every number of the paragraph:
   the README is only true as long as the script says the same.

    ```text
    $ python scripts/mean_error.py
    mean 7.160 ± 0.030
    one hour apart 0.996, one day apart 0.978
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    years scatter by 0.70
    mean 7.16 ± 0.22
    ...
    ```

**Check:** the README ends with **How sure is the mean**, and its numbers
are the ones the script prints.

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, for the next time they are needed.

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

## Optional, if the room goes fast { #optional }

---

### 13. Is 2025 a cold year? { #cold-year }

<!-- — · 10 min -->

z is the distance from the other years in units of their scatter; the **p-value** is the chance of a z at least that far from 0 if nothing special happened.

1. Add at the end of `mean_error.py`, save. `math.erfc(abs(z) / math.sqrt(2))`
   is the two-sided p-value of a Gaussian.

    ```python

    import math
    other = means[:-1]
    z = (means[-1] - other.mean()) / other.std(ddof=1)
    print(f"2025: z = {z:.2f}, p = {math.erfc(abs(z) / math.sqrt(2)):.3f}")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/mean_error.py
    ...
    2025: z = -2.17, p = 0.030
    ```

**Check:** p = 0.030. But 2025 was picked because it looked cold. With ten
years to pick from, the chance that one of them reaches p ≤ 0.03 is
1 − 0.97¹⁰ = 0.26.

---

### 14. 2023 against 2025 { #difference }

<!-- — · 5 min -->

The uncertainty of a difference of two values with the same σ is σ√2.

1. Add at the end, save.

    ```python

    diff = means[7] - means[9]
    sd = math.sqrt(2) * sy
    print(f"2023 - 2025 = {diff:.2f} ± {sd:.2f}, z = {diff / sd:.2f}")
    print(f"p = {math.erfc(diff / sd / math.sqrt(2)):.3f}")
    ```

2. Run it. The last two lines:

    ```text
    $ python scripts/mean_error.py
    ...
    2023 - 2025 = 2.33 ± 0.99, z = 2.34
    p = 0.019
    ```

**Check:** 2.33 ± 0.99 °C between the warmest and the coldest year of ten,
chosen after looking.

---

### 15. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder and open: each in a new script, with its solution folded.

!!! question "Advanced task: how long must a block be?"
    Cut `valid` into blocks of 1 hour, 1 day, 1 week, 30 days and 365 days,
    take the mean of each block, and compute the standard error of the
    block means (their scatter / √number of blocks). How does the ± change
    with the block length? Why do 30-day blocks give the largest ±?

??? success "Answer"
    ```python
    import numpy as np

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    valid = temp[temp != -999]
    for hours in [1, 24, 24 * 7, 24 * 30, 24 * 365]:
        k = len(valid) // hours
        blocks = valid[:k * hours].reshape(k, hours).mean(axis=1)
        print(f"blocks of {hours:5d} h: {k:6d} blocks, "
              f"± {blocks.std(ddof=1) / np.sqrt(k):.2f}")
    ```

    ```text
    blocks of     1 h:  87552 blocks, ± 0.03
    blocks of    24 h:   3648 blocks, ± 0.14
    blocks of   168 h:    521 blocks, ± 0.36
    blocks of   720 h:    121 blocks, ± 0.72
    blocks of  8760 h:      9 blocks, ± 0.20
    ```

    The ± grows while neighbouring blocks are still alike. 30-day blocks
    are not alike for another reason: a January block and a July block
    differ by the season, so their scatter measures the yearly cycle, not
    chance. Only blocks of a whole year are alike, and they give ± 0.20,
    close to the 0.22 of section 7.

!!! question "Advanced task: the longest frost"
    Find the longest run of frost hours in a row, with the times it
    started and ended. Count without NumPy tricks: walk through the hours
    with a counter that grows on a frost hour and goes back to 0 otherwise.

??? success "Answer"
    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    frost = (temp < 0) & (temp != -999)
    run, longest, end = 0, 0, 0
    for i in range(len(frost)):
        if frost[i]:
            run = run + 1
        else:
            run = 0
        if run > longest:
            longest, end = run, i
    print(f"{longest} hours: {time[end - longest + 1]} to {time[end]}")
    ```

    ```text
    1172 hours: 2024-12-31T16:00 to 2025-02-18T11:00
    ```

    49 days without an hour above 0 °C, in the winter of the coldest year.

!!! question "Advanced task: frost by the hour of the day"
    In March, P(frost) depends on the time of day. Compute it for each of
    the 24 hours (`t[11:13]` is the hour) and find the hour with the most
    and the least frost.

??? success "Answer"
    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    ok = temp != -999
    month = np.array([int(t[5:7]) for t in time])
    hour = np.array([int(t[11:13]) for t in time])
    march = np.array([(temp[ok & (month == 3) & (hour == h)] < 0).mean()
                      for h in range(24)])
    print("most frost at", march.argmax(), "h:", march.max().round(2))
    print("least frost at", march.argmin(), "h:", march.min().round(2))
    ```

    ```text
    most frost at 3 h: 0.68
    least frost at 14 h: 0.11
    ```

    The 37 % of March in section 9 hides 68 % before dawn and 11 % in the
    afternoon: a probability depends on what it is conditioned on.

---

## Aims practised

- ♻️ **Reproducibility:** every number comes from a script, and the README
  says which one; today's folder and `environment.yml` give everyone the
  same start.
- 🔧 **Tool-agnostic:** the same `python` lines in zsh on macOS and in Git
  Bash on Windows.
- 📁 **Files:** figures go to `results/`, programs to `scripts/`, the
  answers into the README.
