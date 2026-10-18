# Seminar 16 · Machine Learning

**Paired lecture:** 16 Machine Learning & AI · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** Can a model forecast tomorrow's temperature? Every student starts from today's folder, adds
scikit-learn to its environment, builds a table of days, measures two
baselines, trains a linear model and a tree on 2016 to 2023, tests them once
on 2024 and 2025, and writes the errors in °C into the README.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows) and in one script, `scripts/forecast.py`, which grows from
section to section. In the blocks, a line that starts with `$` is typed in
the terminal, and every other line is what comes back.

**If time runs short:** leave out sections 8 and 10 (use depth 6), and do
section 12.

??? info "Before the session"
    - **Room:** VS Code and Miniforge (Seminar 4, or the Setup page), and
      internet: today's folder is 0.6 MB, its environment about 90
      packages, scikit-learn about 10 MB more. Nothing from an earlier
      seminar is needed.
    - **You:** nothing to prepare. The numbers on this page come from
      `data/raw/weather.csv` and are the same on every laptop; scikit-learn
      1.9.1, pandas 3.0.
    - **Keys** are written for Windows, macOS in brackets. Every line typed is
      the same on both systems.

---

## Part 1 · Today's folder and scikit-learn { #part-1 }

<!-- 0:00 to 0:25 -->

scikit-learn is a library of ready-made models: a straight-line fit, a decision tree and many more, all used the same way.

Further reading: [scikit-learn, Getting Started](https://scikit-learn.org/stable/getting_started.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Everything today's seminar needs is in one zip: the data, the scripts and an `environment.yml` with Python, NumPy, pandas and Matplotlib.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s16.zip`.
2. In a terminal (VS Code: **View** > **Terminal**), unpack it into the
   home folder and look inside.

    ```text
    $ unzip -q ~/Downloads/weather-s16.zip -d ~
    $ cd ~/weather-s16
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s16 ~` instead of `unzip`.

3. **File** > **Open Folder...** > `weather-s16`. Then **View** >
   **Terminal**: the new terminal starts in the folder.
4. Make the environment of this seminar, `s16`, from the file. conda
   downloads what is not yet in its cache; it ends with the line that
   switches it on.

    ```text
    $ conda env create -n s16 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s16
    ```

5. Switch it on; the prompt starts with `(s16)`.

    ```text
    $ conda activate s16
    $ python --version
    Python 3.14.8
    ```

**Check:** `(s16)` at the start of the prompt, in the folder `weather-s16`.

---

### 2. Install scikit-learn { #install }

<!-- 0:10 · 10 min -->

conda installs it, and what it needs, from conda-forge into `s16`.

1. Install. conda lists what it will add and asks.

    ```text
    $ conda install scikit-learn
    The following NEW packages will be INSTALLED:

      cloudpickle        conda-forge/noarch::cloudpickle-3.1.2-pyhcf101f3_1
      joblib             conda-forge/noarch::joblib-1.6.0-pyhcf101f3_0
      narwhals           conda-forge/noarch::narwhals-2.27.1-pyh5ded981_0
      scikit-learn       conda-forge/linux-64::scikit-learn-1.9.1-np2py314h9e1d7c2_1
      scipy              conda-forge/linux-64::scipy-1.18.1-py314h36f0660_1
      threadpoolctl      conda-forge/noarch::threadpoolctl-3.7.0-pyhc455866_0

    Proceed ([y]/n)?
    ```

    This run was on Linux: `linux-64` reads `osx-arm64` on a Mac, `win-64`
    on Windows. SciPy comes along: scikit-learn needs it.

2. Press `Enter`. The prompt comes back when it is done.
3. Check: the package is imported as `sklearn`.

    ```text
    $ python -c "import sklearn; print(sklearn.__version__)"
    1.9.1
    ```

**Check:** a version from 1.9 on.

!!! warning "`EnvironmentNotWritableError` or the prompt shows `(base)`"
    The install went to the wrong environment. Run `conda activate s16`,
    then the install again.

---

### 3. Write it into `environment.yml` { #environment }

<!-- 0:20 · 5 min -->

Another laptop builds the same environment from this file only if the file names scikit-learn.

1. Open `environment.yml` and add one line at the end of `dependencies`,
   with the version of section 2, step 3: the file gives every package its
   full version. Save.

    ```text
      - scikit-learn=1.9.1
    ```

2. The whole file now.

    ```text
    $ cat environment.yml
    name: s16
    channels:
      - conda-forge
    dependencies:
      - python=3.14.8
      - numpy=2.5.4
      - pandas=3.0.6
      - matplotlib-base=3.11.2
      - scikit-learn=1.9.1
    ```

    `conda env create -f environment.yml` on another laptop now installs
    scikit-learn too.

**Check:** `environment.yml` ends with `- scikit-learn=1.9.1`.

!!! question "Task: ask conda for the version"
    Check the version in `environment.yml` against what conda installed in
    `s16`.

??? success "Answer"
    ```text
    $ conda list scikit-learn
    # packages in environment at /Users/smilte/miniforge3/envs/s16:
    #
    # Name                     Version          Build               Channel
    scikit-learn               1.9.1            np2py314h9e1d7c2_1  conda-forge
    ```

    The **Build** column differs between macOS, Windows and Linux; the
    version does not.

---

## Part 2 · A table of days { #part-2 }

<!-- 0:25 to 0:45 -->

One row per day: today's mean temperature and, beside it, tomorrow's, the number to forecast.

Further reading: [pandas, time series](https://pandas.pydata.org/docs/user_guide/timeseries.html).

---

### 4. Daily means { #days }

<!-- 0:25 · 10 min -->

pandas turns 87 672 hours into 3653 days.

1. **File** > **New File...**, type `scripts/forecast.py`, press `Enter`.
   Write and save. `na_values=[-999]` reads the marked hours as missing;
   `resample("D").mean()` averages the hours of each day.

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
    $ python scripts/forecast.py
    (3653, 3)
                temp_c  humidity_pct  wind_ms
    time
    2016-01-01   -4.87         89.54     3.31
    2016-01-02   -5.13         89.71     0.30
    2016-01-03   -3.14         84.33     1.22
    ```

**Check:** 3653 days, three columns.

---

### 5. Tomorrow beside today { #tomorrow }

<!-- 0:35 · 5 min -->

`shift(-1)` moves a column up one row: each day gets the next day's value.

1. At the top of the script, add:

    ```python
    import numpy as np
    ```

2. At the end, add and save. The cosine and sine of the day of the year
   tell the model the time of year: 31 December and 1 January get nearly
   the same two numbers.

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
    $ python scripts/forecast.py
    3644
                yesterday  temp_c  tomorrow
    time
    2016-01-02      -4.87   -5.13     -3.14
    2016-01-03      -5.13   -3.14     -4.30
    2016-01-04      -3.14   -4.30     -3.83
    ```

4. Read a row: on 2 January, yesterday −4.87, today −5.13, tomorrow
   −3.14; the next row has them one day on.

**Check:** 3644 rows. Nine days dropped: the first and the last, and seven
around the five days of July 2019 without a temperature.

---

### 6. Train on the past, test on the future { #split }

<!-- 0:40 · 5 min -->

The test days must come after every training day, as a real forecast does.

1. Add and save:

    ```python

    train = days[days.index.year <= 2023]
    test = days[days.index.year >= 2024]
    print("train", len(train), "test", len(test))
    ```

2. Run it. The last line:

    ```text
    $ python scripts/forecast.py
    train 2914 test 730
    ```

**Check:** 2914 training days, 730 test days. The test days are looked at
once, in section 11 and not before.

!!! question "Task: why 730?"
    2024 and 2025 have 731 days. Which one is missing from `test`, and why?

??? success "Answer"
    31 December 2025: its tomorrow is not in the file, so `dropna` removed
    it. 2024 gives 366 rows, 2025 gives 364.

---

## Part 3 · Baselines first { #part-3 }

<!-- 0:45 to 1:05 -->

A model is worth something only if it beats the simplest forecast.

---

### 7. Predict tomorrow as today { #persistence }

<!-- 0:45 · 10 min -->

Persistence says tomorrow's mean will be today's; its error is the mean absolute difference in °C.

1. Add and save. `mae` takes two columns of the same length and returns
   how far apart they are on an average day.

    ```python

    def mae(forecast, truth):
        """Mean absolute error: how far off a forecast is, on average."""
        return np.mean(np.abs(np.asarray(forecast) - np.asarray(truth)))

    print(f"persistence  {mae(test['temp_c'], test['tomorrow']):.2f} °C")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/forecast.py
    persistence  1.10 °C
    ```

**Check:** 1.10 °C. A model has to do better than this.

---

### 8. The mean of that date { #climatology }

<!-- 0:55 · 10 min -->

Climatology: tomorrow will be as warm as that date was on average in the training years.

1. Add and save. `groupby` collects the training days by day of the year,
   `reindex` looks up the mean for each test day.

    ```python

    clim = train.groupby(train.index.dayofyear)["tomorrow"].mean()
    guess = clim.reindex(test.index.dayofyear)
    print(f"climatology  {mae(guess, test['tomorrow']):.2f} °C")
    ```

2. Run it. The last two lines:

    ```text
    $ python scripts/forecast.py
    persistence  1.10 °C
    climatology  2.46 °C
    ```

**Check:** 2.46 °C. Weather lasts for days, so today says more about
tomorrow than the calendar does.

!!! question "Task: the bad days of persistence"
    On how many test days was persistence off by more than 3 °C? Add one
    `print` to the script.

??? success "Answer"
    ```python
    print((np.abs(test["temp_c"] - test["tomorrow"]) > 3).sum())
    ```

    ```text
    25
    ```

    25 of 730 days. Delete the line again.

---

## Part 4 · Two models, tested once { #part-4 }

<!-- 1:05 to 2:00 -->

Fit on 2016 to 2023, choose with 2023, test once on 2024 and 2025.

Further reading: [scikit-learn, linear models](https://scikit-learn.org/stable/modules/linear_model.html);
[decision trees](https://scikit-learn.org/stable/modules/tree.html).

---

### 9. A linear model { #linear }

<!-- 1:05 · 15 min -->

Tomorrow as a weighted sum of today, yesterday and the season: a straight-line fit by least squares, with four inputs instead of one.

1. At the top of the script, add:

    ```python
    from sklearn.linear_model import LinearRegression
    ```

2. At the end, add and save. Every scikit-learn model is used the same
   way: `fit` on the training days, then `predict` for other days.

    ```python

    features = ["temp_c", "yesterday", "season_cos", "season_sin"]
    linear = LinearRegression().fit(train[features], train["tomorrow"])
    error = mae(linear.predict(test[features]), test["tomorrow"])
    print(f"linear       {error:.2f} °C")
    print(linear.coef_.round(3), round(linear.intercept_, 3))
    ```

3. Run it. The last lines:

    ```text
    $ python scripts/forecast.py
    persistence  1.10 °C
    climatology  2.46 °C
    linear       1.06 °C
    [ 1.064 -0.217 -1.671 -0.314] 1.123
    ```

4. Read the weights: tomorrow = 1.064 × today − 0.217 × yesterday − 1.671 ×
   season_cos − 0.314 × season_sin + 1.123. Almost all of it is today.

**Check:** 1.06 °C, 0.04 °C better than persistence.

---

### 10. A tree, its depth chosen on 2023 { #depth }

<!-- 1:20 · 10 min -->

A decision tree asks yes-or-no questions about the inputs (is today below 3 °C?) and forecasts the mean of the training days that gave the same answers; its depth is how many questions in a row.

1. At the top of the script, add:

    ```python
    from sklearn.tree import DecisionTreeRegressor
    ```

2. At the end, add and save. The depth is chosen on 2023, a year the tree
   is not fitted on.

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
    $ python scripts/forecast.py
    depth  2  2016-2022 2.15  2023 2.39
    depth  4  2016-2022 1.24  2023 1.30
    depth  6  2016-2022 1.07  2023 1.24
    depth  8  2016-2022 0.89  2023 1.38
    depth 12  2016-2022 0.42  2023 1.59
    depth 20  2016-2022 0.02  2023 1.73
    ```

4. On the days it was fitted on, the error falls to 0.02 °C. On 2023 it is
   smallest at depth 6, then rises: the deep trees learn the noise of
   2016 to 2022. This is **overfitting**.

**Check:** depth 6, with 1.24 °C on 2023.

---

### 11. The tree on 2024 and 2025 { #tree }

<!-- 1:30 · 10 min -->

Depth 6, fitted on all of 2016 to 2023, tested once.

1. Add and save:

    ```python

    tree = DecisionTreeRegressor(max_depth=6, random_state=0)
    tree.fit(train[features], train["tomorrow"])
    error = mae(tree.predict(test[features]), test["tomorrow"])
    print(f"tree         {error:.2f} °C")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/forecast.py
    tree         1.14 °C
    ```

**Check:** 1.14 °C: the tree is worse than persistence (1.10). Only the
linear model beats the baseline.

!!! question "Task: choose the depth on the test years?"
    Someone tries depths 2, 4, 5, 6 and 8 on 2024 and 2025 and reports the
    best. What would they report, and why is it not a test any more?

??? success "Answer"
    Depth 5, 1.12 °C (depth 2: 2.32, 4: 1.21, 6: 1.14, 8: 1.22). The test
    years then chose the model, so 1.12 is the best of five tries on them,
    not the error on days the model has not seen. Even so it does not beat
    1.10.

---

### 12. The errors in the README { #push }

<!-- 1:40 · 15 min -->

Every number with its baseline and the days it was measured on.

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

2. Look at the table: `Ctrl+Shift+V` (macOS `Cmd+Shift+V`) opens the
   README's preview beside the text.

3. The script is the record of how each number was made: open
   `scripts/forecast.py` and find the line that prints each of the four.

**Check:** the four errors in the README's preview, each with the days it
was measured on.

---

### 13. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

| To | Do |
|--|--|
| add a package | `conda install NAME`, then a line in `environment.yml` |
| test a forecast | train on the past, test on the future |
| judge a model | against a baseline: here persistence, 1.10 °C |
| choose a setting | on a validation year, never on the test years |
| report | the error in °C, the days it was measured on, the baseline |

The answer to the question: yes, by 0.04 °C on a typical day, and only the
linear model.

---

## Optional, if the room goes fast { #optional }

Further reading: [scikit-learn, ensembles](https://scikit-learn.org/stable/modules/ensemble.html);
[cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html).

---

### 14. Is 0.04 °C real? { #gain }

<!-- — · 10 min -->

The gain per test day, its mean and its standard error.

1. Add and save. `gain` is, for each test day, how much closer the linear
   model came than persistence.

    ```python

    gain = (np.abs(test["temp_c"] - test["tomorrow"])
            - np.abs(linear.predict(test[features]) - test["tomorrow"]))
    error = gain.std() / np.sqrt(len(gain))
    print(f"linear gains {gain.mean():.3f} ± {error:.3f} °C a day")
    ```

2. Run it. The last line:

    ```text
    $ python scripts/forecast.py
    linear gains 0.042 ± 0.017 °C a day
    ```

**Check:** 0.042 is 2.5 standard errors from zero: small, and probably
real.

---

### 15. A leak that gives an error of 0.00 °C { #leak }

<!-- — · 10 min -->

A smoothed temperature looks like a harmless input.

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
    $ python scripts/forecast.py
    with smooth  0.00 °C
    ```

3. `center=True` averages yesterday, today and tomorrow. Tomorrow is in the
   input: 3 × smooth − today − yesterday. This is a **leak**.
4. Delete the nine lines again.

**Check:** a perfect forecast is a reason to look for a leak.

---

### 16. October 2025 in a plot { #plot }

<!-- — · 10 min -->

Both forecasts against what was measured.

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
    $ python scripts/forecast.py
    ```

3. Both forecasts follow the measured line one day late: they see a change
   only after it has happened, as on 25 to 28 October.

**Check:** three lines from 2 October to 1 November.

---

### 17. Advanced tasks { #advanced }

<!-- — · 30 min -->

Three harder tasks for whoever is done early; try each in a copy, `cp scripts/forecast.py scripts/try.py`, so `forecast.py` stays as it is. The answers are folded.

!!! question "Advanced task: do more inputs help?"
    Give the linear model more to work with: the temperature of the day
    before yesterday, today's humidity, today's wind. Which of them lowers
    the error on 2024 and 2025?

??? success "Answer"
    In `try.py`, in the block of section 5, before `days = days.dropna()`:

    ```python
    days["before"] = days["temp_c"].shift(2)
    ```

    At the end:

    ```python

    for extra in [[], ["before"], ["humidity_pct"], ["wind_ms"],
                  ["before", "humidity_pct", "wind_ms"]]:
        inputs = features + extra
        model = LinearRegression().fit(train[inputs], train["tomorrow"])
        error = mae(model.predict(test[inputs]), test["tomorrow"])
        name = ", ".join(extra) or "nothing"
        print(f"+ {name:30s} {error:.3f} °C")
    ```

    Run it; the new lines:

    ```text
    $ python scripts/try.py
    + nothing                        1.057 °C
    + before                         1.056 °C
    + humidity_pct                   1.058 °C
    + wind_ms                        1.057 °C
    + before, humidity_pct, wind_ms  1.057 °C
    ```

    None moves the error by more than 0.001 °C: today's temperature already
    holds what these inputs know. `train` has 2912 days now, two fewer,
    because `shift(2)` leaves two more days without a value.

!!! question "Advanced task: a forest of trees"
    A **random forest** averages many trees, each fitted on a random
    sample of the training days. Try `RandomForestRegressor` with 200
    trees; choose its `min_samples_leaf` (the fewest training days in a
    leaf) on 2023, as section 10 chose the depth, then test it once. Does
    it beat persistence, and the linear model?

??? success "Answer"
    At the end of `try.py` (`early` and `check` come from section 10):

    ```python

    from sklearn.ensemble import RandomForestRegressor

    for leaf in [1, 5, 20, 50, 100]:
        forest = RandomForestRegressor(n_estimators=200, min_samples_leaf=leaf,
                                       random_state=0)
        forest.fit(early[features], early["tomorrow"])
        error = mae(forest.predict(check[features]), check["tomorrow"])
        print(f"leaf {leaf:3d}  2023 {error:.3f}")

    forest = RandomForestRegressor(n_estimators=200, min_samples_leaf=20,
                                   random_state=0)
    forest.fit(train[features], train["tomorrow"])
    error = mae(forest.predict(test[features]), test["tomorrow"])
    print(f"forest       {error:.2f} °C")
    ```

    Run it; the new lines:

    ```text
    $ python scripts/try.py
    leaf   1  2023 1.224
    leaf   5  2023 1.149
    leaf  20  2023 1.147
    leaf  50  2023 1.189
    leaf 100  2023 1.272
    forest       1.09 °C
    ```

    Leaf 20 is best on 2023. On the test years the forest gives 1.09 °C:
    better than the single tree (1.14) and than persistence (1.10), worse
    than the linear model (1.06). The 200 trees take a few seconds.

!!! question "Advanced task: further ahead"
    Forecast 2, 3, 5 and 7 days ahead instead of one. How do persistence,
    climatology and the linear model compare as the forecast reaches
    further? From how many days on is the calendar better than today?

??? success "Answer"
    A new script, `scripts/ahead.py`: the target is `shift(-ahead)`, and
    the table is built again for each distance.

    ```python
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    hours = pd.read_csv("data/raw/weather.csv", na_values=[-999],
                        parse_dates=["time"], index_col="time")
    days = hours.resample("D").mean()
    days["yesterday"] = days["temp_c"].shift(1)
    angle = 2 * np.pi * days.index.dayofyear / 365.25
    days["season_cos"] = np.cos(angle)
    days["season_sin"] = np.sin(angle)
    features = ["temp_c", "yesterday", "season_cos", "season_sin"]

    def mae(forecast, truth):
        """Mean absolute error: how far off a forecast is, on average."""
        return np.mean(np.abs(np.asarray(forecast) - np.asarray(truth)))

    for ahead in [1, 2, 3, 5, 7]:
        table = days.copy()
        table["target"] = table["temp_c"].shift(-ahead)
        table = table.dropna()
        train = table[table.index.year <= 2023]
        test = table[table.index.year >= 2024]
        clim = train.groupby(train.index.dayofyear)["target"].mean()
        linear = LinearRegression().fit(train[features], train["target"])
        persistence = mae(test["temp_c"], test["target"])
        climatology = mae(clim.reindex(test.index.dayofyear), test["target"])
        model = mae(linear.predict(test[features]), test["target"])
        print(f"+{ahead} days  persistence {persistence:.2f}  "
              f"climatology {climatology:.2f}  linear {model:.2f}")
    ```

    ```text
    $ python scripts/ahead.py
    +1 days  persistence 1.10  climatology 2.46  linear 1.06
    +2 days  persistence 1.63  climatology 2.46  linear 1.52
    +3 days  persistence 1.96  climatology 2.45  linear 1.76
    +5 days  persistence 2.36  climatology 2.45  linear 2.00
    +7 days  persistence 2.66  climatology 2.44  linear 2.10
    ```

    Persistence grows worse with every day; at 7 days it is worse than the
    calendar (2.66 against 2.44). The linear model stays the best, because
    it weighs today less and the season more as the distance grows: 7 days
    ahead its weights are 0.299 for today (1.064 one day ahead) and −8.183
    for `season_cos` (−1.671).

---

## Aims practised

- ♻️ **Reproducibility:** the environment file names the new package; the
  errors in the README come out of one script, on days chosen before the
  run.
- 🔧 **Tool-agnostic:** the same least-squares fit that can be written by
  hand, called from a library; every model in it is used with `fit` and
  `predict`.
- 📁 **Files:** the hourly file becomes a table of days in memory; nothing
  new is written to `data/`.
