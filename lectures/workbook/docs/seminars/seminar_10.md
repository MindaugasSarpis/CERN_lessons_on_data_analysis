# Seminar 10 — How Strong Is the Yearly Cycle? Fitting the Weather Data

**Paired lecture:** 10 Fitting from First Principles · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student fits a straight line to the ten yearly
means by the closed formulas of the lecture (−0.6 ± 0.8 °C per decade) and
a cosine to the 3648 daily means (amplitude 11.18 °C, coldest on
16 January), reads the residuals, commits and pushes.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (zsh on macOS, Git Bash on Windows; `weather` environment). SciPy is installed in
section 1.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · SciPy and the daily means** · 30 min | | |
| 0:00 | [1. Install SciPy](#install) | `conda install scipy` | `1.18.1`, `scipy=1.18` in `environment.yml` |
| 0:10 | [2. The daily means](#daily) | `scripts/fit_cycle.py`, `reshape(-1, 24)` | 3648 daily means |
| 0:20 | [3. Plot them](#plot) | `ax.plot(d, T, ".")` | ten waves |
| | **Part 2 · Is it getting warmer?** · 30 min | | |
| 0:30 | [4. Ten yearly means](#yearly) | `scripts/fit_trend.py` | ten points, σ = 0.70 |
| 0:35 | [5. Five sums, slope and intercept](#sums) | `D = S * Sxx - Sx**2` | a = −0.0555 °C per year |
| 0:45 | [6. Uncertainties and χ²](#chi2) | `np.sqrt(S / D)` | −0.6 ± 0.8 °C per decade |
| | **Part 3 · The yearly cycle** · 35 min | | |
| 1:00 | [7. A cosine and a sine column](#lstsq) | `np.linalg.lstsq` | c, a, b |
| 1:10 | [8. Amplitude and the coldest day](#amplitude) | `np.hypot(a, b)` | 11.18 °C, day 15.9 |
| 1:20 | [9. The same with `curve_fit`](#curve-fit) | `curve_fit(cycle, d, T, p0=…)` | 11.179 ± 0.069 |
| | **Part 4 · The residuals** · 15 min | | |
| 1:35 | [10. Residuals](#residuals) | `np.corrcoef(res[:-1], res[1:])` | 0.875, `results/cycle_fit.png` |
| | **Part 5 · Write it down** · 10 min | | |
| 1:50 | [11. The README, a commit, a push](#commit) | `git commit`, `git push` | the fits on GitHub |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. The amplitude year by year](#by-year) | a loop of ten fits | 11.20 ± 0.25 °C |
| — | [14. The daily cycle](#daily-cycle) | a period of 24 hours | 3.50 °C, warmest at 15:00 |

**If time runs short:** leave out section 3 and the Task of Part 3;
sections 10 and 11 stay.

??? info "Before the session"
    - **Room:** `weather-project` with `environment.yml` and the `weather`
      environment of Seminars 7 and 8, `scripts/mean_error.py` of Seminar 9.
      Internet for `conda install scipy`.
    - **You:** nothing to prepare. The data are the same in every clone, so
      every number on this page is the number in the room. Commit ids differ.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · SciPy and the daily means { #part-1 }

**0:00 to 0:30**

---

### 1. Install SciPy { #install }

**0:00 · 10 min** · `curve_fit` lives in SciPy. It goes into the environment and into `environment.yml`.

1. Open `weather-project` in VS Code, then the terminal. Switch on the
   environment and bring in any commit from GitHub.

    ```text
    conda activate weather
    ```

    ```text
    git pull
    ```

    ```text
    Already up to date.
    ```

2. Install SciPy.

    ```text
    conda install scipy
    ```

    ```text
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/weather

      added / updated specs:
        - scipy


    The following NEW packages will be INSTALLED:

      scipy              conda-forge/linux-64::scipy-1.18.1-py314h36f0660_1


    Proceed ([y]/n)?
    ```

    Press `Enter`. Your line names your system (`osx-arm64`, `win-64`), and
    on Windows the folder is `C:\Users\smilte\miniforge3\envs\weather`
    (in Git Bash `/c/Users/smilte/miniforge3/envs/weather`).

3. Check.

    ```text
    python -c "import scipy; print(scipy.__version__)"
    ```

    ```text
    1.18.1
    ```

4. Open `environment.yml`. Add one line at the end of `dependencies`, with
   the version pinned like the others, save.

    ```text
      - scipy=1.18
    ```

5. Look at the change, commit it.

    ```text
    git diff
    ```

    ```text
    @@ -5,3 +5,4 @@ dependencies:
       - python=3.14
       - numpy=2.5
       - matplotlib-base=3.11
    +  - scipy=1.18
    ```

    ```text
    git commit -am "Add SciPy to the environment"
    ```

    ```text
    [main b3c4d6b] Add SciPy to the environment
     1 file changed, 1 insertion(+)
    ```

**Check:** `1.18.1`, and `git status` clean.

---

### 2. The daily means { #daily }

**0:10 · 10 min** · 24 rows make a day: `reshape(-1, 24)` gives one row per day.

1. New file `scripts/fit_cycle.py`. Type and save.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    days = temp.reshape(-1, 24)
    good = (days != -999).all(axis=1)
    T = days[good].mean(axis=1)
    d = np.arange(len(days))[good]
    print("days", len(days), "with 24 hours", len(T))
    ```

    `good` keeps the days whose 24 hours are all valid; `d` is the day
    number, 0 for 1 January 2016.

2. Run it.

    ```text
    python scripts/fit_cycle.py
    ```

    ```text
    days 3653 with 24 hours 3648
    ```

**Check:** 3648 days: the five days of July 2019 are out.

---

### 3. Plot them { #plot }

**0:20 · 5 min** · The model is chosen from the picture.

1. Add at the end, save, run.

    ```python

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(d, T, ".", ms=2)
    ax.set_xlabel("day since 2016-01-01")
    ax.set_ylabel("daily mean (°C)")
    fig.savefig("results/daily_means.png", dpi=150, bbox_inches="tight")
    ```

    ```text
    python scripts/fit_cycle.py
    ```

2. Open `results/daily_means.png` from the Explorer: ten waves, one per
   year.

**Check:** ten waves, low at the start of each year, high in summer.

!!! question "Task: read the model off the plot"
    From the plot alone: the mean level, the amplitude (half the distance
    from winter to summer), and the day of the coldest point. These are the
    starting values of section 9.

??? note "Answer"
    Winter about −4 °C, summer about 18 °C: level (18 − 4)/2 ≈ 7 °C,
    amplitude (18 + 4)/2 ≈ 11 °C, coldest near day 15, mid-January. The fit
    gives 7.18, 11.18 and 15.9.

---

## Part 2 · Is it getting warmer? { #part-2 }

**0:30 to 1:00** · A straight line through the ten yearly means, by the five sums of the lecture.

---

### 4. Ten yearly means { #yearly }

**0:30 · 5 min** · x is the year since 2016; σ of each point is 0.70 °C, the scatter of the years in Seminar 9.

1. New file `scripts/fit_trend.py`. Type and save.

    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1)
    year = np.array([int(t[:4]) for t in time])
    ok = temp != -999
    x = np.arange(10)              # years since 2016
    y = np.array([temp[ok & (year == 2016 + k)].mean() for k in x])
    sy = np.full(10, 0.70)         # the scatter of the years, Seminar 9
    print(y.round(2))
    ```

2. Run it.

    ```text
    python scripts/fit_trend.py
    ```

    ```text
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    ```

**Check:** the ten means of Seminar 9.

---

### 5. Five sums, slope and intercept { #sums }

**0:35 · 10 min** · χ² is smallest where both derivatives are zero; the solution needs five sums.

1. Add at the end, save.

    ```python

    w = 1 / sy**2
    S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
    Sxx, Sxy = (w * x * x).sum(), (w * x * y).sum()
    print(f"S {S:.2f}, Sx {Sx:.2f}, Sy {Sy:.2f}, Sxx {Sxx:.2f}, Sxy {Sxy:.2f}")
    D = S * Sxx - Sx**2
    a = (S * Sxy - Sx * Sy) / D
    b = (Sxx * Sy - Sx * Sxy) / D
    print(f"a = {a:.4f} °C per year, b = {b:.3f} °C")
    ```

2. Run it.

    ```text
    python scripts/fit_trend.py
    ```

    ```text
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    S 20.41, Sx 91.84, Sy 146.12, Sxx 581.63, Sxy 648.21
    a = -0.0555 °C per year, b = 7.410 °C
    ```

**Check:** a = −0.0555 °C per year; b = 7.410 °C, the line's value in 2016.

---

### 6. Uncertainties and χ² { #chi2 }

**0:45 · 10 min** · σ_a = √(S/Δ), σ_b = √(Sxx/Δ), cov = −Sx/Δ; χ² near the number of degrees of freedom says the σ fit the scatter.

1. Add at the end, save.

    ```python

    sa = np.sqrt(S / D)
    sb = np.sqrt(Sxx / D)
    chi2 = (((y - a * x - b) / sy)**2).sum()
    print(f"a = {a:.3f} ± {sa:.3f}, b = {b:.2f} ± {sb:.2f}, cov {-Sx / D:.4f}")
    print(f"chi2 = {chi2:.2f} for {len(x) - 2} degrees of freedom")
    print(f"per decade: {10 * a:.1f} ± {10 * sa:.1f} °C")
    ```

2. Run it.

    ```text
    python scripts/fit_trend.py
    ```

    The last three lines:

    ```text
    a = -0.056 ± 0.077, b = 7.41 ± 0.41, cov -0.0267
    chi2 = 8.56 for 8 degrees of freedom
    per decade: -0.6 ± 0.8 °C
    ```

**Check:** −0.6 ± 0.8 °C per decade: less than one σ from zero. Ten years
show no trend.

!!! question "Task: the same with `np.polyfit`, then with x centred"
    1. Fit the same line with `np.polyfit` (lecture: `w=1 / sy`,
       `cov="unscaled"`). Same numbers?
    2. Fit again with `x - 4.5` in place of `x`. What happens to the
       intercept, its ± and the covariance?

??? note "Answer"
    Add at the end of `fit_trend.py`:

    ```python

    p, C = np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")
    print("polyfit", p, np.sqrt(np.diag(C)))
    p, C = np.polyfit(x - 4.5, y, 1, w=1 / sy, cov="unscaled")
    print("centred", p, np.sqrt(np.diag(C)), f"cov {C[0, 1]:.4f}")
    ```

    ```text
    polyfit [-0.05552739  7.40992628] [0.07706746 0.41142767]
    centred [-0.05552739  7.16005304] [0.07706746 0.22135944] cov -0.0000
    ```

    1. The same a, b and ±. 2. With x centred the intercept is the mean
       of the decade, 7.16 ± 0.22 °C (Seminar 9), and the covariance is
       zero (it may print `0.0000`).

---

## Part 3 · The yearly cycle { #part-3 }

**1:00 to 1:35** · T = c + a cos ωd + b sin ωd, with ω = 2π/365.25 known, is linear in c, a and b.

---

### 7. A cosine and a sine column { #lstsq }

**1:00 · 10 min** · The design matrix of the lecture: one column per parameter.

1. Add at the end of `fit_cycle.py`, save.

    ```python

    om = 2 * np.pi / 365.25
    A = np.column_stack([np.ones(len(d)), np.cos(om * d), np.sin(om * d)])
    theta, *rest = np.linalg.lstsq(A, T, rcond=None)
    c, a, b = theta
    print(f"c = {c:.3f}, a = {a:.3f}, b = {b:.3f}")
    ```

2. Run it.

    ```text
    python scripts/fit_cycle.py
    ```

    ```text
    days 3653 with 24 hours 3648
    c = 7.177, a = -10.763, b = -3.023
    ```

**Check:** c = 7.177 °C, near the mean of Seminar 9.

---

### 8. Amplitude and the coldest day { #amplitude }

**1:10 · 10 min** · a cos ωd + b sin ωd = A cos(ωd − φ), with A = √(a² + b²) and φ = atan2(b, a); the minimum is half a period after φ.

1. Add at the end, save.

    ```python

    amp = np.hypot(a, b)
    d0 = (np.arctan2(b, a) + np.pi) / om
    print(f"amplitude {amp:.2f} °C, coldest on day {d0:.1f}")
    ```

2. Run it.

    ```text
    python scripts/fit_cycle.py
    ```

    The last line:

    ```text
    amplitude 11.18 °C, coldest on day 15.9
    ```

**Check:** 11.18 °C; day 15.9 is 16 January.

---

### 9. The same with `curve_fit` { #curve-fit }

**1:20 · 10 min** · Written as c − A cos(ω(d − d0)), the model is not linear in d0: `curve_fit` iterates from starting values.

1. Add at the end, save.

    ```python

    def cycle(d, c, amp, d0):
        return c - amp * np.cos(om * (d - d0))

    popt, pcov = curve_fit(cycle, d, T, p0=[7, 11, 15])
    err = np.sqrt(np.diag(pcov))
    print(f"c   = {popt[0]:.3f} ± {err[0]:.3f}")
    print(f"amp = {popt[1]:.3f} ± {err[1]:.3f}")
    print(f"d0  = {popt[2]:.2f} ± {err[2]:.2f}")
    ```

    No `sigma`: the daily means have no σ of their own. `curve_fit` then
    takes the scatter of the points around the curve as σ (the lecture's
    default without `absolute_sigma`).

2. Run it.

    ```text
    python scripts/fit_cycle.py
    ```

    The last three lines:

    ```text
    c   = 7.177 ± 0.049
    amp = 11.179 ± 0.069
    d0  = 15.92 ± 0.36
    ```

**Check:** the numbers of sections 7 and 8, now with a ±.

!!! question "Task: other starting values"
    1. Start from `p0=[7, 11, 200]`, the warm side of the year.
    2. Leave `p0` out.
    Is the curve different?

??? note "Answer"
    1. `amp = -11.179 ± 0.069` and `d0 = 198.54 ± 0.36`: the warmest
       day, with the sign of the amplitude turned. 198.54 − 365.25/2 =
       15.92: the same curve.
    2. Every parameter starts at 1; here it still finds 11.179 and 15.92.
       On other data a bad start can end in a wrong minimum.

---

## Part 4 · The residuals { #part-4 }

**1:35 to 1:50**

---

### 10. Residuals { #residuals }

**1:35 · 10 min** · What the curve leaves over, and whether one day's residual predicts the next.

1. Add at the end, save.

    ```python

    res = T - cycle(d, *popt)
    print(f"residuals: std {res.std(ddof=3):.2f}, "
          f"next day {np.corrcoef(res[:-1], res[1:])[0, 1]:.3f}")
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    top.plot(d, T, ".", ms=2)
    top.plot(d, cycle(d, *popt), "-")
    top.set_ylabel("daily mean (°C)")
    bottom.plot(d, res, ".", ms=2)
    bottom.axhline(0, color="black")
    bottom.set_xlabel("day since 2016-01-01")
    bottom.set_ylabel("residual (°C)")
    fig.savefig("results/cycle_fit.png", dpi=150, bbox_inches="tight")
    ```

    `*popt` passes the three values as three arguments.

2. Run it.

    ```text
    python scripts/fit_cycle.py
    ```

    The last line:

    ```text
    residuals: std 2.94, next day 0.875
    ```

3. Open `results/cycle_fit.png`: the curve through the points, and below
   it the residuals in runs of warm and cold weeks.

**Check:** a day's residual correlates with the next by 0.875: the 3648
points are not independent, so ± 0.069 is too small.

!!! question "Task: the trend from the daily means"
    Add a term `k * d / 3652.5` (k in °C per decade) to the model and fit
    it with `curve_fit`. Compare k with section 6.

??? note "Answer"
    Add at the end of `fit_cycle.py`:

    ```python

    def cycle_trend(d, c, amp, d0, k):
        return cycle(d, c, amp, d0) + k * d / 3652.5

    p4, c4 = curve_fit(cycle_trend, d, T, p0=[7, 11, 15, 0])
    print(f"trend {p4[3]:.2f} ± {np.sqrt(c4[3, 3]):.2f} °C per decade")
    ```

    ```text
    trend -0.57 ± 0.17 °C per decade
    ```

    The same slope as the yearly means (−0.6), with a ± 4.5 times
    smaller: 3.4 σ from zero. It counts 3648 correlated days as
    independent. The ten yearly means give the honest ± 0.8.

---

## Part 5 · Write it down { #part-5 }

**1:50 to 2:00**

---

### 11. The README, a commit, a push { #commit }

**1:50 · 5 min** · The two results, with the scripts that make them.

1. At the end of `README.md`, add and save:

    ```text

    ## The yearly cycle

    Daily means fitted with c − A cos(2π(d − d0)/365.25) by
    `scripts/fit_cycle.py`: A = 11.18 °C, coldest on day 15.9 (16 January).
    The fit's ± 0.07 °C is too small: the residuals of neighbouring days
    correlate by 0.875.

    Trend of the ten yearly means, `scripts/fit_trend.py`: −0.6 ± 0.8 °C per
    decade, compatible with zero.
    ```

2. Stage, commit, push.

    ```text
    git add README.md scripts
    ```

    ```text
    git commit -m "Fit the yearly cycle and the trend"
    ```

    ```text
    [main f6ce821] Fit the yearly cycle and the trend
     3 files changed, 87 insertions(+)
     create mode 100644 scripts/fit_cycle.py
     create mode 100644 scripts/fit_trend.py
    ```

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       3c589a2..f6ce821  main -> main
    ```

    Your ids differ, and so do the counts if you kept the Task lines.

**Check:** on GitHub, `environment.yml` lists `scipy` and the README shows
**The yearly cycle**.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
| a straight line by hand | the five sums, `D = S * Sxx - Sx**2` |
| the same in one call | `np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")` |
| a model linear in its parameters | `np.linalg.lstsq(A, T, rcond=None)` |
| any model | `curve_fit(f, x, y, p0=[…])` |
| the uncertainties | `np.sqrt(np.diag(pcov))` |
| check the fit | residuals, and their correlation |
| add a package | `conda install NAME`, a pinned line in `environment.yml` |

Seminar 11 predicts frost from the evening's weather.

---

## Optional, if the room is fast { #optional }

---

### 13. The amplitude year by year { #by-year }

**— · 10 min** · Ten fits, one per year: their scatter gives an honest ± for the amplitude.

1. Add at the end of `fit_cycle.py`, save, run.

    ```python

    amps = []
    for y in range(10):
        sel = (d >= 365.25 * y) & (d < 365.25 * (y + 1))
        p, cv = curve_fit(cycle, d[sel], T[sel], p0=[7, 11, 15 + 365.25 * y])
        amps.append(p[1])
    amps = np.array(amps)
    print(amps.round(2))
    print(f"amplitude {amps.mean():.2f} ± {amps.std(ddof=1) / np.sqrt(10):.2f}")
    ```

    ```text
    python scripts/fit_cycle.py
    ```

    The last two lines:

    ```text
    [11.18 11.   10.63 12.6  10.42 10.41 10.71 11.48 11.06 12.49]
    amplitude 11.20 ± 0.25
    ```

**Check:** ± 0.25 °C, 3.6 times the ± 0.069 of section 9.

---

### 14. The daily cycle { #daily-cycle }

**— · 10 min** · The same model with a period of 24 hours, on the mean of each hour of the day.

1. Add at the end, save, run.

    ```python

    hours = days[good].mean(axis=0)
    h = np.arange(24)
    B = np.column_stack([np.ones(24), np.cos(2 * np.pi * h / 24),
                         np.sin(2 * np.pi * h / 24)])
    (c24, a24, b24), *rest = np.linalg.lstsq(B, hours, rcond=None)
    warm = (np.arctan2(b24, a24) / (2 * np.pi / 24)) % 24
    print(f"daily amplitude {np.hypot(a24, b24):.2f} °C, warmest at {warm:.1f} h")
    ```

    ```text
    python scripts/fit_cycle.py
    ```

    The last line:

    ```text
    daily amplitude 3.50 °C, warmest at 15.0 h
    ```

**Check:** 3.50 °C between the mean and the warmest hour, 15:00.

---

## Aims practised

- ♻️ **Reproducibility:** SciPy is written into `environment.yml`, so
  `conda env create -f environment.yml` makes the same environment.
- 🔧 **Tool-agnostic:** the same fit three ways (five sums, `polyfit`,
  `curve_fit`), the same numbers.
- ⚙️ **Automation:** each number in the README comes from one script run.
