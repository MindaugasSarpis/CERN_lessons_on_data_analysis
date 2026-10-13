# Seminar 16 — Can a Model Forecast Tomorrow's Temperature? scikit-learn on the Weather Project

**Paired lecture:** 16 Machine Learning & AI · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student adds scikit-learn to the environment, builds
a table of days, measures two baselines, trains a linear model and a tree on
2016 to 2023, tests them once on 2024 and 2025, and pushes the errors in °C.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows) and in one script, `scripts/forecast.py`, which grows from
section to section.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · scikit-learn in the environment** · 20 min | | |
| 0:00 | [1. Install scikit-learn](#install) | `conda install scikit-learn` | `1.9.1` or newer |
| 0:15 | [2. Write it into `environment.yml`](#environment) | `git commit` | `scikit-learn=1.9.1` in `environment.yml` |
| | **Part 2 · A table of days** · 25 min | | |
| 0:20 | [3. Daily means](#days) | `days = hours.resample("D").mean()` | 3653 days |
| 0:30 | [4. Tomorrow beside today](#tomorrow) | `shift(-1)` | 3644 rows with today and tomorrow |
| 0:40 | [5. Train on the past, test on the future](#split) | `days.index.year <= 2023` | 2914 and 730 days |
| | **Part 3 · Baselines first** · 20 min | | |
| 0:45 | [6. Predict tomorrow as today](#persistence) | `def mae` | 1.10 °C |
| 0:55 | [7. The mean of that date](#climatology) | `groupby(...dayofyear)` | 2.46 °C |
| | **Part 4 · Two models, tested once** · 55 min | | |
| 1:05 | [8. A linear model](#linear) | `LinearRegression()` | 1.06 °C |
| 1:20 | [9. A tree, its depth chosen on 2023](#depth) | `DecisionTreeRegressor` | depth 6 |
| 1:30 | [10. The tree on 2024 and 2025](#tree) | `max_depth=6` | 1.14 °C |
| 1:40 | [11. The errors in the README, push](#push) | `git push` | the table on GitHub |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. Is 0.04 °C real?](#gain) | `gain.std()` | 0.042 ± 0.017 °C |
| — | [14. A leak that gives an error of 0.00 °C](#leak) | `rolling(3, center=True)` | a leak found |
| — | [15. October 2025 in a plot](#plot) | `plt.savefig` | a figure in `results/` |

**If time runs short:** leave out sections 7 and 9 (use depth 6), and do
section 11.

??? info "Before the session"
    - **Room:** the weather project as it stands after Seminar 13, pushed to
      the student's own GitHub repository, with the `weather` environment
      (NumPy, pandas, matplotlib). Internet for the install.
    - **You:** nothing to prepare. The numbers on this page come from
      `data/raw/weather.csv` and are the same on every laptop; scikit-learn
      1.9.1, pandas 3.0. Commit ids differ.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · scikit-learn in the environment { #part-1 }

**0:00 to 0:20** · scikit-learn holds the models the lecture built by hand, ready to use.

---

### 1. Install scikit-learn { #install }

**0:00 · 15 min** · conda installs it, and what it needs, from conda-forge into `weather`.

1. Open the weather project in VS Code, then the terminal: **View** >
   **Terminal**.
2. Activate the environment.

    ```text
    conda activate weather
    ```

3. Install.

    ```text
    conda install scikit-learn
    ```

    ```text
    The following NEW packages will be INSTALLED:

      cloudpickle        conda-forge/noarch::cloudpickle-3.1.2-pyhcf101f3_1
      joblib             conda-forge/noarch::joblib-1.6.0-pyhcf101f3_0
      narwhals           conda-forge/noarch::narwhals-2.27.1-pyh5ded981_0
      scikit-learn       conda-forge/linux-64::scikit-learn-1.9.1-np2py314h9e1d7c2_1
      threadpoolctl      conda-forge/noarch::threadpoolctl-3.7.0-pyhc455866_0


    Proceed ([y]/n)?
    ```

    This run was on Linux: `linux-64` reads `osx-arm64` on a Mac, `win-64`
    on Windows.

4. Press `Enter`. The prompt comes back when it is done.
5. Check.

    ```text
    python -c "import sklearn; print(sklearn.__version__)"
    ```

    ```text
    1.9.1
    ```

**Check:** a version from 1.9 on.

!!! warning "`EnvironmentNotWritableError` or the prompt shows `(base)`"
    The install went to the wrong environment. Run `conda activate weather`,
    then the install again.

---

### 2. Write it into `environment.yml` { #environment }

**0:15 · 5 min** · Another laptop builds the same environment from this file only if the file names scikit-learn.

1. Open `environment.yml` and add one line at the end of `dependencies`,
   with the version of step 5 (Seminar 13 pinned every line). Save.

    ```text
      - scikit-learn=1.9.1
    ```

2. The change.

    ```text
    git diff
    ```

    ```text
    @@ -8,3 +8,4 @@ dependencies:
       - scipy=1.18.1
       - pandas=3.0.6
       - pytest=9.1.1
    +  - scikit-learn=1.9.1
    ```

3. Commit it.

    ```text
    git commit -am "Add scikit-learn to the environment"
    ```

    ```text
    [main 997c99f] Add scikit-learn to the environment
     1 file changed, 1 insertion(+)
    ```

**Check:** `environment.yml` ends with `- scikit-learn=1.9.1`.

!!! question "Task: ask conda for the version"
    Check the version in `environment.yml` against what conda installed in
    `weather`.

??? note "Answer"
    ```text
    conda list scikit-learn
    ```

    ```text
    # packages in environment at /Users/smilte/miniforge3/envs/weather:
    #
    # Name                     Version          Build               Channel
    scikit-learn               1.9.1            np2py314h9e1d7c2_1  conda-forge
    ```

    The **Build** column differs between macOS, Windows and Linux; the
    version does not.

---

## Part 2 · A table of days { #part-2 }

**0:20 to 0:45** · One row per day: today's mean temperature and, beside it, tomorrow's, the number to forecast.

---

### 3. Daily means { #days }

**0:20 · 10 min** · pandas turns 87 672 hours into 3653 days.

1. **File** > **New File...**, type `scripts/forecast.py`, press `Enter`.
   Write and save.

    ```python
    import pandas as pd

    hours = pd.read_csv("data/raw/weather.csv", na_values=[-999],
                        parse_dates=["time"], index_col="time")
    days = hours.resample("D").mean()
    print(days.shape)
    print(days.head(3).round(2))
    ```

2. Run it.

    ```text
    python scripts/forecast.py
    ```

    ```text
    (3653, 3)
                temp_c  humidity_pct  wind_ms
    time
    2016-01-01   -4.87         89.54     3.31
    2016-01-02   -5.13         89.71     0.30
    2016-01-03   -3.14         84.33     1.22
    ```

**Check:** 3653 days, three columns.

---

### 4. Tomorrow beside today { #tomorrow }

**0:30 · 10 min** · `shift(-1)` moves a column up one row: each day gets the next day's value.

1. At the top of the script, add:

    ```python
    import numpy as np
    ```

2. At the end, add and save:

    ```python

    days["tomorrow"] = days["temp_c"].shift(-1)
    days["yesterday"] = days["temp_c"].shift(1)
    angle = 2 * np.pi * days.index.dayofyear / 365.25
    days["season_cos"] = np.cos(angle)
    days["season_sin"] = np.sin(angle)
    days = days.dropna()
    print(len(days))
    print(days[["yesterday", "temp_c", "tomorrow"]].head(3).round(2))
    ```

3. Run it. The new lines at the end:

    ```text
    python scripts/forecast.py
    ```

    ```text
    3644
                yesterday  temp_c  tomorrow
    time
    2016-01-02      -4.87   -5.13     -3.14
    2016-01-03      -5.13   -3.14     -4.30
    2016-01-04      -3.14   -4.30     -3.83
    ```

4. Read a row: on 2 January, yesterday −4.87, today −5.13, tomorrow
   −3.14; the next row has them one day on. `season_cos` and `season_sin`
   tell the model the time of year.

**Check:** 3644 rows. Nine days dropped: the first and the last, and seven
around the five days of July 2019 without a temperature.

---

### 5. Train on the past, test on the future { #split }

**0:40 · 5 min** · The test days must come after every training day, as a real forecast does.

1. Add and save:

    ```python

    train = days[days.index.year <= 2023]
    test = days[days.index.year >= 2024]
    print("train", len(train), "test", len(test))
    ```

2. Run it.

    ```text
    python scripts/forecast.py
    ```

    ```text
    train 2914 test 730
    ```

**Check:** 2914 training days, 730 test days. The test days are looked at
once, in section 10 and not before.

!!! question "Task: why 730?"
    2024 and 2025 have 731 days. Which one is missing from `test`, and why?

??? note "Answer"
    31 December 2025: its tomorrow is not in the file, so `dropna` removed
    it. 2024 gives 366 rows, 2025 gives 364.

---

## Part 3 · Baselines first { #part-3 }

**0:45 to 1:05** · A model is worth something only if it beats the simplest forecast.

---

### 6. Predict tomorrow as today { #persistence }

**0:45 · 10 min** · Persistence says tomorrow's mean will be today's; its error is the mean absolute difference in °C.

1. Add and save:

    ```python


    def mae(forecast, truth):
        """Mean absolute error: how far off a forecast is, on average."""
        return np.mean(np.abs(np.asarray(forecast) - np.asarray(truth)))


    print(f"persistence  {mae(test['temp_c'], test['tomorrow']):.2f} °C")
    ```

2. Run it.

    ```text
    python scripts/forecast.py
    ```

    ```text
    persistence  1.10 °C
    ```

**Check:** 1.10 °C. A model has to do better than this.

---

### 7. The mean of that date { #climatology }

**0:55 · 10 min** · Climatology: tomorrow will be as warm as that date was on average in the training years.

1. Add and save:

    ```python

    clim = train.groupby(train.index.dayofyear)["tomorrow"].mean()
    guess = clim.reindex(test.index.dayofyear)
    print(f"climatology  {mae(guess, test['tomorrow']):.2f} °C")
    ```

2. Run it.

    ```text
    python scripts/forecast.py
    ```

    ```text
    persistence  1.10 °C
    climatology  2.46 °C
    ```

**Check:** 2.46 °C. Weather lasts for days, so today says more about
tomorrow than the calendar does.

!!! question "Task: the bad days of persistence"
    On how many test days was persistence off by more than 3 °C? Add one
    `print` to the script.

??? note "Answer"
    ```python
    print((np.abs(test["temp_c"] - test["tomorrow"]) > 3).sum())
    ```

    ```text
    25
    ```

    25 of 730 days. Delete the line again.

---

## Part 4 · Two models, tested once { #part-4 }

**1:05 to 2:00** · Fit on 2016 to 2023, choose with 2023, test once on 2024 and 2025.

---

### 8. A linear model { #linear }

**1:05 · 15 min** · Tomorrow as a weighted sum of today, yesterday and the season: the line fit of Lecture 10 with four inputs.

1. At the top of the script, add:

    ```python
    from sklearn.linear_model import LinearRegression
    ```

2. At the end, add and save:

    ```python

    features = ["temp_c", "yesterday", "season_cos", "season_sin"]
    linear = LinearRegression().fit(train[features], train["tomorrow"])
    error = mae(linear.predict(test[features]), test["tomorrow"])
    print(f"linear       {error:.2f} °C")
    print(linear.coef_.round(3), round(linear.intercept_, 3))
    ```

3. Run it.

    ```text
    python scripts/forecast.py
    ```

    ```text
    persistence  1.10 °C
    climatology  2.46 °C
    linear       1.06 °C
    [ 1.064 -0.217 -1.671 -0.314] 1.123
    ```

4. Read the weights: tomorrow = 1.064 × today − 0.217 × yesterday − 1.671 ×
   season_cos − 0.314 × season_sin + 1.123. Almost all of it is today.

**Check:** 1.06 °C, 0.04 °C better than persistence.

---

### 9. A tree, its depth chosen on 2023 { #depth }

**1:20 · 10 min** · A deeper tree fits the training days better; the depth is chosen on 2023, a year it was not fitted on.

1. At the top of the script, add:

    ```python
    from sklearn.tree import DecisionTreeRegressor
    ```

2. At the end, add and save:

    ```python

    early = train[train.index.year <= 2022]
    check = train[train.index.year == 2023]
    for depth in [2, 4, 6, 8, 12, 20]:
        tree = DecisionTreeRegressor(max_depth=depth, random_state=0)
        tree.fit(early[features], early["tomorrow"])
        fit_err = mae(tree.predict(early[features]), early["tomorrow"])
        check_err = mae(tree.predict(check[features]), check["tomorrow"])
        print(f"depth {depth:2d}  2016-2022 {fit_err:.2f}  2023 {check_err:.2f}")
    ```

3. Run it. The new lines:

    ```text
    python scripts/forecast.py
    ```

    ```text
    depth  2  2016-2022 2.15  2023 2.39
    depth  4  2016-2022 1.24  2023 1.30
    depth  6  2016-2022 1.07  2023 1.24
    depth  8  2016-2022 0.89  2023 1.38
    depth 12  2016-2022 0.42  2023 1.59
    depth 20  2016-2022 0.02  2023 1.73
    ```

4. On the days it was fitted on, the error falls to 0.02 °C. On 2023 it is
   smallest at depth 6, then rises: the deep trees learn the noise of
   2016 to 2022. This is overfitting.

**Check:** depth 6, with 1.24 °C on 2023.

---

### 10. The tree on 2024 and 2025 { #tree }

**1:30 · 10 min** · Depth 6, fitted on all of 2016 to 2023, tested once.

1. Add and save:

    ```python

    tree = DecisionTreeRegressor(max_depth=6, random_state=0)
    tree.fit(train[features], train["tomorrow"])
    error = mae(tree.predict(test[features]), test["tomorrow"])
    print(f"tree         {error:.2f} °C")
    ```

2. Run it. The last line:

    ```text
    python scripts/forecast.py
    ```

    ```text
    tree         1.14 °C
    ```

**Check:** 1.14 °C: the tree is worse than persistence (1.10). Only the
linear model beats the baseline.

!!! question "Task: choose the depth on the test years?"
    Someone tries depths 2, 4, 5, 6 and 8 on 2024 and 2025 and reports the
    best. What would they report, and why is it not a test any more?

??? note "Answer"
    Depth 5, 1.12 °C (depth 2: 2.32, 4: 1.21, 6: 1.14, 8: 1.22). The test
    years then chose the model, so 1.12 is the best of five tries on them,
    not the error on days the model has not seen. Even so it does not beat
    1.10.

---

### 11. The errors in the README, push { #push }

**1:40 · 15 min** · Every number with its baseline and the days it was measured on.

1. In `README.md`, above `## How to rebuild`, add a section and save.

    ```text
    ## Forecast of tomorrow's mean temperature

    `scripts/forecast.py`. Trained on 2016 to 2023, tested once on 2024 and
    2025 (730 days). Mean absolute error:

    | Forecast | Error |
    |--|--|
    | persistence: tomorrow as today | 1.10 °C |
    | climatology: the mean of that date | 2.46 °C |
    | linear regression | 1.06 °C |
    | decision tree, depth 6 | 1.14 °C |
    ```

2. What is new.

    ```text
    git status --short
    ```

    ```text
     M README.md
    ?? scripts/forecast.py
    ```

3. Commit both.

    ```text
    git add scripts/forecast.py README.md
    ```

    ```text
    git commit -m "Forecast tomorrow: linear 1.06 °C against persistence 1.10 °C"
    ```

    ```text
    [main 890ac1d] Forecast tomorrow: linear 1.06 °C against persistence 1.10 °C
     2 files changed, 67 insertions(+)
     create mode 100644 scripts/forecast.py
    ```

4. Push.

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       788b165..890ac1d  main -> main
    ```

**Check:** the table on GitHub; `scripts/forecast.py` in the repository.

---

### 12. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Do |
|--|--|
| add a package | `conda install NAME`, then a line in `environment.yml` |
| test a forecast | train on the past, test on the future |
| judge a model | against a baseline: here persistence, 1.10 °C |
| choose a setting | on a validation year, never on the test years |
| report | the error in °C, the days it was measured on, the baseline |

The answer to the title: yes, by 0.04 °C on a typical day, and only the
linear model.

---

## Optional, if the room is fast { #optional }

---

### 13. Is 0.04 °C real? { #gain }

**— · 10 min** · The gain per test day, its mean and its standard error.

1. Add and save:

    ```python

    gain = (np.abs(test["temp_c"] - test["tomorrow"])
            - np.abs(linear.predict(test[features]) - test["tomorrow"]))
    error = gain.std() / np.sqrt(len(gain))
    print(f"linear gains {gain.mean():.3f} ± {error:.3f} °C a day")
    ```

2. Run it. The last line:

    ```text
    python scripts/forecast.py
    ```

    ```text
    linear gains 0.042 ± 0.017 °C a day
    ```

**Check:** 0.042 is 2.5 standard errors from zero: small, and probably
real.

---

### 14. A leak that gives an error of 0.00 °C { #leak }

**— · 10 min** · A smoothed temperature looks like a harmless input.

1. Add and save:

    ```python

    days["smooth"] = days["temp_c"].rolling(3, center=True).mean()
    days = days.dropna()
    train = days[days.index.year <= 2023]
    test = days[days.index.year >= 2024]
    leaky = features + ["smooth"]
    model = LinearRegression().fit(train[leaky], train["tomorrow"])
    error = mae(model.predict(test[leaky]), test["tomorrow"])
    print(f"with smooth  {error:.2f} °C")
    ```

2. Run it. The last line:

    ```text
    python scripts/forecast.py
    ```

    ```text
    with smooth  0.00 °C
    ```

3. `center=True` averages yesterday, today and tomorrow. Tomorrow is in the
   input: 3 × smooth − today − yesterday. This is a leak.
4. Delete the nine lines again.

**Check:** a perfect forecast is a reason to look for a leak.

---

### 15. October 2025 in a plot { #plot }

**— · 10 min** · Both forecasts against what was measured.

1. Add and save:

    ```python

    import matplotlib.pyplot as plt

    october = test.loc["2025-10"]
    when = october.index + pd.Timedelta(days=1)  # the day forecast
    plt.plot(when, october["tomorrow"], label="measured")
    plt.plot(when, linear.predict(october[features]), label="linear")
    plt.plot(when, october["temp_c"], label="persistence")
    plt.ylabel("daily mean temperature (°C)")
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.savefig("results/forecast_october_2025.png")
    ```

2. Run it, then open `results/forecast_october_2025.png` in the Explorer.

    ```text
    python scripts/forecast.py
    ```

3. Both forecasts follow the measured line one day late: they see a change
   only after it has happened, as on 25 to 28 October.

**Check:** three lines from 2 October to 1 November.

---

## Aims practised

- ♻️ **Reproducibility:** the environment file names the new package; the
  errors in the README come out of one script, on days chosen before the
  run.
- 🔧 **Tool-agnostic:** the line fit of Lecture 10 and the models of the
  lecture are the same mathematics in scikit-learn.
- 📁 **Files:** the hourly file becomes a table of days in memory; nothing
  new is written to `data/`.
