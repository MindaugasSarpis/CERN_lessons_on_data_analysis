# Seminar 10 · Fitting

**Paired lecture:** 10 Fitting from First Principles · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** How strong is the yearly cycle? Every student fits a straight line to the ten yearly
means by five sums (−0.6 ± 0.8 °C per decade) and a cosine to the 3648
daily means (amplitude 11.18 °C, coldest on 16 January), reads the
residuals, and writes both results into the README.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (zsh on macOS, Git Bash on Windows; today's environment
`s10`). SciPy is installed in section 1. In the blocks, a line that starts with `$` is
typed in the terminal, and every other line is what comes back.

**If time runs short:** leave out section 3 and the Task of Part 3;
sections 10 and 11 stay.

??? info "Before the session"
    - **Room:** VS Code and Miniforge on every laptop (Seminar 4, or the
      [Setup](../setup.md) page), and internet: today's folder and its
      packages download in section 1, about 180 MB the first time.
    - **You:** nothing to prepare. Today's folder is the same for everyone,
      so every number on this page is the number in the room.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · SciPy and the daily means { #part-1 }

<!-- 0:00 to 0:30 -->

A fit needs a model; the model is read off a plot of the data.

---

### 1. Get today's folder, install SciPy { #install }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the scripts so far and `environment.yml`. **SciPy** is the package of scientific methods built on NumPy; its `curve_fit` fits any model. It goes into today's environment and into `environment.yml`.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases)
   of the course repository, under **Assets**, click `weather-s10.zip`.
2. Open VS Code, then **View** > **Terminal**. Unpack the zip into the
   home folder and go there. Git Bash shows `/c/Users/smilte/...`.

    ```text
    $ unzip ~/Downloads/weather-s10.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s10.zip
       creating: /Users/smilte/weather-s10/
    ...
      inflating: /Users/smilte/weather-s10/scripts/weather.py
    $ cd ~/weather-s10
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s10 ~` instead of `unzip`.

3. **File** > **Open Folder...** > `weather-s10`. VS Code opens a new
   window; **View** > **Terminal** there starts in the folder.
4. Make today's environment from `environment.yml`: Python, NumPy,
   Matplotlib and JupyterLab, in the versions the file names. Then switch
   it on: the prompt starts with `(s10)`.

    ```text
    $ conda env create -n s10 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s10
    $ conda activate s10
    ```

5. Install SciPy 1.18 from conda-forge. conda shows its plan and asks.

    ```text
    $ conda install scipy=1.18
    ...
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/s10

      added / updated specs:
        - scipy=1.18

    The following NEW packages will be INSTALLED:

      scipy              conda-forge/linux-64::scipy-1.18.1-py314h36f0660_1

    Proceed ([y]/n)?
    ```

6. Press `Enter`. Your line names your system (`osx-arm64`, `win-64`), and
   on Windows the folder is `/c/Users/smilte/miniforge3/envs/s10`.
   Then check:

    ```text
    $ python -c "import scipy; print(scipy.__version__)"
    1.18.1
    ```

7. Write the environment down again. `--from-history` lists only what was
   asked for, with the versions typed.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

8. In `environment.yml`, delete the last line, `prefix: ...` (it names a
   folder on this laptop only), save. SciPy is the new last line:

    ```text
    $ cat environment.yml
    name: s10
    channels:
      - conda-forge
    dependencies:
      - jupyterlab=4.6
      - matplotlib-base=3.11
      - numpy=2.5
      - python=3.14
      - scipy=1.18
    ```

**Check:** `1.18.1`, and `scipy=1.18` in `environment.yml`.

---

### 2. The daily means { #daily }

<!-- 0:10 · 10 min -->

24 rows make a day: `reshape(-1, 24)` turns the 87 672 hours into 3653 rows of 24, one row per day.

1. New file `scripts/fit_cycle.py`. Type and save. `.all(axis=1)` asks of
   each row whether all its hours are valid; `.mean(axis=1)` averages
   each row.

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

2. Run it. `d` is the day number, 0 for 1 January 2016.

    ```text
    $ python scripts/fit_cycle.py
    days 3653 with 24 hours 3648
    ```

**Check:** 3648 days: the five days of July 2019 are out.

---

### 3. Plot them { #plot }

<!-- 0:20 · 5 min -->

The model is chosen from the picture.

1. Add at the end, save. `"."` draws each day as a dot, `ms=2` small.

    ```python

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(d, T, ".", ms=2)
    ax.set_xlabel("day since 2016-01-01")
    ax.set_ylabel("daily mean (°C)")
    fig.savefig("results/daily_means.png", dpi=150, bbox_inches="tight")
    ```

2. Run it, then open `results/daily_means.png` from the Explorer: ten
   waves, one per year.

    ```text
    $ python scripts/fit_cycle.py
    days 3653 with 24 hours 3648
    ```

**Check:** ten waves, low at the start of each year, high in summer.

!!! question "Task: read the model off the plot"
    From the plot alone: the mean level, the amplitude (half the distance
    from winter to summer), and the day of the coldest point. These are the
    starting values of section 9.

??? success "Answer"
    Winter about −4 °C, summer about 18 °C: level (18 − 4)/2 ≈ 7 °C,
    amplitude (18 + 4)/2 ≈ 11 °C, coldest near day 15, mid-January. The fit
    gives 7.18, 11.18 and 15.9.

---

## Part 2 · Is it getting warmer? { #part-2 }

<!-- 0:30 to 1:00 -->

A straight line y = a x + b through the ten yearly means: a is the change per year.

---

### 4. Ten yearly means, and how well a line fits { #yearly }

<!-- 0:30 · 5 min -->

**χ²** (chi-squared) adds up each point's distance from the line, in units of its σ, squared: the smaller, the better the line fits.

1. New file `scripts/fit_trend.py`. Type and save. x is the year since
   2016; σ of each point is 0.70 °C, how much the years scatter
   (Seminar 9).

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

2. Run it: the ten means of Seminar 9.

    ```text
    $ python scripts/fit_trend.py
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    ```

3. Add a function for χ² of any line, and try two lines by guess: a flat
   one at 7.16 °C, and one rising 0.1 °C per year.

    ```python

    def chi2_of(a, b):
        return (((y - a * x - b) / sy)**2).sum()

    print(f"flat line at 7.16: chi2 {chi2_of(0, 7.16):.2f}")
    print(f"slope 0.1 per year: chi2 {chi2_of(0.1, 6.7):.2f}")
    ```

4. Run it. The rising line fits worse.

    ```text
    $ python scripts/fit_trend.py
    [7.6  6.51 7.97 7.27 6.83 7.25 6.6  8.31 7.27 5.98]
    flat line at 7.16: chi2 9.08
    slope 0.1 per year: chi2 12.64
    ```

**Check:** χ² 9.08 for the flat line, 12.64 for the rising one.

---

### 5. Five sums, slope and intercept { #sums }

<!-- 0:35 · 10 min -->

Guessing is slow. χ² is smallest where its derivatives by a and by b are both zero; solving those two equations needs five sums of the data, each point weighted by w = 1/σ².

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

2. Run it. The last two lines are new.

    ```text
    $ python scripts/fit_trend.py
    ...
    S 20.41, Sx 91.84, Sy 146.12, Sxx 581.63, Sxy 648.21
    a = -0.0555 °C per year, b = 7.410 °C
    ```

**Check:** a = −0.0555 °C per year; b = 7.410 °C, the line's value in 2016.

---

### 6. Uncertainties and χ² { #chi2 }

<!-- 0:45 · 10 min -->

The same sums give the uncertainties: σ_a = √(S/D), σ_b = √(Sxx/D), and the covariance of a and b, −Sx/D. χ² near the **degrees of freedom** (points − parameters, here 10 − 2) says the σ match the scatter.

1. Add at the end, save.

    ```python

    sa = np.sqrt(S / D)
    sb = np.sqrt(Sxx / D)
    chi2 = (((y - a * x - b) / sy)**2).sum()
    print(f"a = {a:.3f} ± {sa:.3f}, b = {b:.2f} ± {sb:.2f}, cov {-Sx / D:.4f}")
    print(f"chi2 = {chi2:.2f} for {len(x) - 2} degrees of freedom")
    print(f"per decade: {10 * a:.1f} ± {10 * sa:.1f} °C")
    ```

2. Run it. The last three lines:

    ```text
    $ python scripts/fit_trend.py
    ...
    a = -0.056 ± 0.077, b = 7.41 ± 0.41, cov -0.0267
    chi2 = 8.56 for 8 degrees of freedom
    per decade: -0.6 ± 0.8 °C
    ```

**Check:** −0.6 ± 0.8 °C per decade: less than one σ from zero. Ten years
show no trend. χ² 8.56 is below both guesses of section 4.

!!! question "Task: the same with `np.polyfit`, then with x centred"
    1. Fit the same line with `np.polyfit(x, y, 1, w=1 / sy,
       cov="unscaled")`: `w=1 / sy` weights each point by 1/σ,
       `cov="unscaled"` takes the σ as given. Same numbers?
    2. Fit again with `x - 4.5` in place of `x`. What happens to the
       intercept, its ± and the covariance?

??? success "Answer"
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

<!-- 1:00 to 1:35 -->

T = c + a cos ωd + b sin ωd, with ω = 2π/365.25 known: a cosine and a sine of the day, each with its own weight.

---

### 7. A cosine and a sine column { #lstsq }

<!-- 1:00 · 10 min -->

The model is linear in c, a and b, so it is solved like the straight line: one column per parameter in a **design matrix** A, and `np.linalg.lstsq` finds the weights with the smallest sum of squares.

1. Add at the end of `fit_cycle.py`, save. `np.column_stack` puts three
   columns side by side: ones (for c), cos ωd, sin ωd.

    ```python

    om = 2 * np.pi / 365.25
    A = np.column_stack([np.ones(len(d)), np.cos(om * d), np.sin(om * d)])
    theta, *rest = np.linalg.lstsq(A, T, rcond=None)
    c, a, b = theta
    print(f"c = {c:.3f}, a = {a:.3f}, b = {b:.3f}")
    ```

2. Run it.

    ```text
    $ python scripts/fit_cycle.py
    days 3653 with 24 hours 3648
    c = 7.177, a = -10.763, b = -3.023
    ```

**Check:** c = 7.177 °C, near the mean of Seminar 9.

---

### 8. Amplitude and the coldest day { #amplitude }

<!-- 1:10 · 10 min -->

A cosine and a sine of the same period add up to one shifted cosine: a cos ωd + b sin ωd = A cos(ωd − φ), with A = √(a² + b²) and φ = atan2(b, a). The minimum is half a period after φ.

1. Add at the end, save. `np.hypot(a, b)` is √(a² + b²).

    ```python

    amp = np.hypot(a, b)
    d0 = (np.arctan2(b, a) + np.pi) / om
    print(f"amplitude {amp:.2f} °C, coldest on day {d0:.1f}")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/fit_cycle.py
    ...
    amplitude 11.18 °C, coldest on day 15.9
    ```

**Check:** 11.18 °C; day 15.9 is 16 January.

---

### 9. The same with `curve_fit` { #curve-fit }

<!-- 1:20 · 10 min -->

Written as c − A cos(ω(d − d0)), the model is not linear in d0. `curve_fit` then searches: it starts from guessed values `p0` and improves them step by step.

1. Add at the end, save. No `sigma`: the daily means have no σ of their
   own, so `curve_fit` takes the scatter of the points around the curve
   as σ.

    ```python

    def cycle(d, c, amp, d0):
        return c - amp * np.cos(om * (d - d0))

    popt, pcov = curve_fit(cycle, d, T, p0=[7, 11, 15])
    err = np.sqrt(np.diag(pcov))
    print(f"c   = {popt[0]:.3f} ± {err[0]:.3f}")
    print(f"amp = {popt[1]:.3f} ± {err[1]:.3f}")
    print(f"d0  = {popt[2]:.2f} ± {err[2]:.2f}")
    ```

2. Run it. `popt` holds the best values, `pcov` their covariance matrix,
   whose diagonal holds the σ².

    ```text
    $ python scripts/fit_cycle.py
    ...
    c   = 7.177 ± 0.049
    amp = 11.179 ± 0.069
    d0  = 15.92 ± 0.36
    ```

**Check:** the numbers of sections 7 and 8, now with a ±.

!!! question "Task: other starting values"
    1. Start from `p0=[7, 11, 200]`, the warm side of the year.
    2. Leave `p0` out.
    Is the curve different?

??? success "Answer"
    1. `amp = -11.179 ± 0.069` and `d0 = 198.54 ± 0.36`: the warmest
       day, with the sign of the amplitude turned. 198.54 − 365.25/2 =
       15.92: the same curve.
    2. Every parameter starts at 1; here it still finds 11.179 and 15.92.
       On other data a bad start can end in a wrong minimum.

---

## Part 4 · The residuals { #part-4 }

<!-- 1:35 to 1:50 -->

A **residual** is a point minus the curve: what the model leaves over.

---

### 10. Residuals { #residuals }

<!-- 1:35 · 10 min -->

What the curve leaves over, and whether one day's residual predicts the next.

1. Add at the end, save. `*popt` passes the three values as three
   arguments.

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

2. Run it. The last line:

    ```text
    $ python scripts/fit_cycle.py
    ...
    residuals: std 2.94, next day 0.875
    ```

3. Open `results/cycle_fit.png`: the curve through the points, and below
   it the residuals in runs of warm and cold weeks.

**Check:** a day's residual correlates with the next by 0.875: the 3648
points are not independent, so ± 0.069 is too small.

!!! question "Task: the trend from the daily means"
    Add a term `k * d / 3652.5` (k in °C per decade) to the model and fit
    it with `curve_fit`. Compare k with section 6.

??? success "Answer"
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

<!-- 1:50 to 2:00 -->

The two results go into the README, with the scripts that make them.

---

### 11. Write the results into the README { #commit }

<!-- 1:50 · 5 min -->

The two results, with the scripts that make them.

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

2. Run both scripts once more: every number of the paragraph is in their
   output.

    ```text
    $ python scripts/fit_trend.py
    ...
    per decade: -0.6 ± 0.8 °C
    $ python scripts/fit_cycle.py
    days 3653 with 24 hours 3648
    c = 7.177, a = -10.763, b = -3.023
    amplitude 11.18 °C, coldest on day 15.9
    ...
    residuals: std 2.94, next day 0.875
    ```

**Check:** the README ends with **The yearly cycle**, and
`environment.yml` lists `scipy=1.18`.

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, for the next time they are needed.

| To | Type |
|--|--|
| a straight line by hand | the five sums, `D = S * Sxx - Sx**2` |
| the same in one call | `np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")` |
| a model linear in its parameters | `np.linalg.lstsq(A, T, rcond=None)` |
| any model | `curve_fit(f, x, y, p0=[…])` |
| the uncertainties | `np.sqrt(np.diag(pcov))` |
| check the fit | residuals, and their correlation |
| add a package | `conda install NAME=VERSION`, then `conda env export --from-history -f environment.yml` |

Seminar 11 predicts frost from the evening's weather.

---

## Optional, if the room goes fast { #optional }

---

### 13. The amplitude year by year { #by-year }

<!-- — · 10 min -->

Ten fits, one per year: their scatter gives an honest ± for the amplitude.

1. Add at the end of `fit_cycle.py`, save. Each year's fit starts from
   the coldest day of that year, `15 + 365.25 * y`.

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

2. Run it. The last two lines:

    ```text
    $ python scripts/fit_cycle.py
    ...
    [11.18 11.   10.63 12.6  10.42 10.41 10.71 11.48 11.06 12.49]
    amplitude 11.20 ± 0.25
    ```

**Check:** ± 0.25 °C, 3.6 times the ± 0.069 of section 9.

---

### 14. The daily cycle { #daily-cycle }

<!-- — · 10 min -->

The same model with a period of 24 hours, on the mean of each hour of the day.

1. Add at the end, save. `days[good].mean(axis=0)` averages each column:
   one mean per hour of the day.

    ```python

    hours = days[good].mean(axis=0)
    h = np.arange(24)
    B = np.column_stack([np.ones(24), np.cos(2 * np.pi * h / 24),
                         np.sin(2 * np.pi * h / 24)])
    (c24, a24, b24), *rest = np.linalg.lstsq(B, hours, rcond=None)
    warm = (np.arctan2(b24, a24) / (2 * np.pi / 24)) % 24
    print(f"daily amplitude {np.hypot(a24, b24):.2f} °C, warmest at {warm:.1f} h")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/fit_cycle.py
    ...
    daily amplitude 3.50 °C, warmest at 15.0 h
    ```

**Check:** 3.50 °C between the mean and the warmest hour, 15:00.

---

### 15. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder and open, with the solutions folded.

!!! question "Advanced task: the ± of the slope from χ²"
    σ_a has a second meaning: the slopes whose best line has a χ² at most
    1 above the minimum lie within a ± σ_a. Scan slopes from −0.3 to 0.2
    in steps of 0.001; for each, the best intercept is `(Sy - t * Sx) / S`.
    Which slopes keep χ² ≤ χ²_min + 1?

??? success "Answer"
    Add at the end of `fit_trend.py`:

    ```python

    chi2_min = chi2_of(a, b)
    slopes = np.arange(-0.3, 0.2, 0.001)
    chi2s = np.array([chi2_of(t, (Sy - t * Sx) / S) for t in slopes])
    inside = slopes[chi2s <= chi2_min + 1]
    print(f"chi2 <= {chi2_min:.2f} + 1 for a from {inside.min():.3f} "
          f"to {inside.max():.3f}")
    ```

    ```text
    chi2 <= 8.56 + 1 for a from -0.132 to 0.021
    ```

    Half the width, (0.021 + 0.132)/2 = 0.077: σ_a of section 6. For a
    model whose χ² is not a parabola, this scan is how the ± is found.

!!! question "Advanced task: leave one year out"
    Fit the slope ten times, each time without one of the years. How much
    does the trend per decade depend on a single year?

??? success "Answer"
    Add at the end of `fit_trend.py`:

    ```python

    for k in range(10):
        keep = x != k
        p = np.polyfit(x[keep], y[keep], 1, w=1 / sy[keep])
        print(2016 + k, f"{10 * p[0]:.2f}")
    ```

    ```text
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

    From −1.03 to +0.22 °C per decade: without the cold 2025 the sign
    turns. The spread is the size of the ± 0.8 of section 6, as it should
    be.

!!! question "Advanced task: the yearly cycle of humidity"
    Fit the same c + a cos ωd + b sin ωd to the daily mean humidity
    (column 2) of the good days. What is its amplitude, and on which day
    is the air most humid? Compare with the coldest day.

??? success "Answer"
    A new script, `scripts/fit_humidity.py`. The most humid day is where
    the cosine peaks: atan2(b, a)/ω.

    ```python
    import numpy as np

    data = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=(1, 2))
    temp = data[:, 0].reshape(-1, 24)
    hum = data[:, 1].reshape(-1, 24)
    good = (temp != -999).all(axis=1)
    H = hum[good].mean(axis=1)
    d = np.arange(len(temp))[good]
    om = 2 * np.pi / 365.25
    A = np.column_stack([np.ones(len(d)), np.cos(om * d), np.sin(om * d)])
    (c, a, b), *rest = np.linalg.lstsq(A, H, rcond=None)
    peak = (np.arctan2(b, a) / om) % 365.25
    print(f"mean {c:.1f} %, amplitude {np.hypot(a, b):.1f} %, "
          f"most humid on day {peak:.0f}")
    ```

    ```text
    $ python scripts/fit_humidity.py
    mean 79.1 %, amplitude 7.1 %, most humid on day 16
    ```

    Day 16, the coldest day of section 8: the two cycles are opposite.
    Cold air holds less water, so the same water is a higher relative
    humidity.

---

## Aims practised

- ♻️ **Reproducibility:** SciPy is written into `environment.yml`, so
  `conda env create -f environment.yml` makes the same environment.
- 🔧 **Tool-agnostic:** the same fit three ways (five sums, `polyfit`,
  `curve_fit`), the same numbers.
- ⚙️ **Automation:** each number in the README comes from one script run.
