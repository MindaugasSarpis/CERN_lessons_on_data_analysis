# Seminar 16 · Machine Learning

**Paired lecture:** 16 Machine Learning & AI · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Will tomorrow in Vilnius be warmer than today? Can a model say so more often than a coin?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in VS Code: the scripts in the editor, the commands in its
terminal (zsh on macOS, Git Bash on Windows; the same lines in both). A line
that starts with `$` is typed without the `$`; `...` stands for lines left out.

**If time runs short:** leave out section 6 (k-means); its calls are on the library card.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page); internet for conda (if
      `analysis` has to be made, or has no scikit-learn yet) and for the
      data. Nothing from earlier seminars is needed.
    - **No file is handed out.** The scripts fetch their data from public
      addresses:
        - size measurements of 344 penguins of three species, Palmer
          Station, Antarctica, 2007–2009 (16 kB): Palmer Station LTER and
          K. Gorman, published by Gorman, Williams and Fraser, *PLoS ONE* 9
          (2014) e90081; the R package `palmerpenguins` (CC0), as a CSV file
          of the Rdatasets collection;
        - in Part 3, the daily record of the Vilnius station,
          `LH000026730.csv` (6.1 MB, 1881 to 24 August 2025), from
          GHCN-Daily, NOAA NCEI, "for free and unrestricted use in research,
          education, and other non-commercial activities" (WMO Resolution
          40); cite Menne et al. 2012, *Global Historical Climatology
          Network - Daily (GHCN-Daily)*, Version 3.35, NOAA NCDC,
          [doi:10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ), accessed
          10 November 2026.
    - **The numbers** on this page come from runs on 10 November 2026 with
      scikit-learn 1.9.1. Every split and every model has a fixed
      `random_state`, so the same versions print the same numbers.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Set up { #part-1 }

### 1. A new folder, and scikit-learn in `analysis` { #start }

<!-- 0:00 · 8 min -->

scikit-learn is the Python library of ready-made models: one neuron, a network, a decision tree, k-means and many more, all used with the same two calls, `fit` and `predict`.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s16
    $ cd ~/weather-s16
    ```

2. **File** > **Open Folder...** > `weather-s16` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. **If `analysis` is on this laptop** (Seminars 8 to 15): switch it on and
   add scikit-learn. At `Proceed ([y]/n)?` press `Enter`; SciPy comes with
   it.

    ```text
    $ conda activate analysis
    $ conda install scikit-learn=1.9
    ...
    Proceed ([y]/n)?
    ```

4. **If it is not:** make it in one line, with today's packages. Then
   switch it on.

    ```text
    $ conda create -n analysis python=3.14 pandas=3.1 matplotlib-base=3.11 scikit-learn=1.9
    ...
    Proceed ([y]/n)?
    ...
    $ conda activate analysis
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. Ask for the versions. The package is installed as `scikit-learn` and
   imported as `sklearn`.

    ```text
    $ python -c "import sklearn, pandas; print(sklearn.__version__, pandas.__version__)"
    1.9.1 3.1.1
    ```

**Check:** `(analysis)` at the start of the prompt, and `1.9.1 3.1.1` (the last digits may be higher).

---

### 2. Write the environment down { #install }

<!-- 0:08 · 7 min -->

`environment.yml` lists what the environment holds, so that another laptop can make the same one.

1. Write it into the folder.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

2. Click `environment.yml` in the Explorer, delete its last line,
   `prefix: ...` (a folder on this laptop), save (`Ctrl+S`, macOS `Cmd+S`).
   Made today, it reads as below; an `analysis` from earlier weeks lists
   more packages.

    ```text
    name: analysis
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - pandas=3.1
      - matplotlib-base=3.11
      - scikit-learn=1.9
    ```

3. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/analysis` in its
   path. The Status Bar shows `analysis`.

**Check:** `- scikit-learn=1.9` in `environment.yml`, and `analysis` in the Status Bar.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs four complete scripts on the penguins of Palmer Station; the
room watches or types along. For each: in the Explorer, right-click > **New
File...**, the name above the code, paste, save, run it in the terminal. A
window opens with the figure; close it and the prompt comes back.

### 3. Three species from two bill measurements: one neuron and a network { #species }

<!-- 0:15 · 10 min -->

A model learns from the training rows and is graded on test rows it has not seen; one neuron (`LogisticRegression`) separates the classes with straight lines, a network with a hidden layer (`MLPClassifier`) with bent ones.

```python title="species.py"
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

url = ("https://vincentarelbundock.github.io/Rdatasets/csv/palmerpenguins/"
       "penguins.csv")
df = pd.read_csv(url).dropna()
X, y = df[["bill_length_mm", "bill_depth_mm"]], df["species"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0, stratify=y)
print(len(X_train), "training rows,", len(X_test), "test rows")
print("always the largest class:", y_test.value_counts(normalize=True).max())

neuron = make_pipeline(StandardScaler(), LogisticRegression())
net = make_pipeline(StandardScaler(), MLPClassifier(
    hidden_layer_sizes=(8,), solver="lbfgs", max_iter=5000, random_state=0))
for name, model in [("one neuron", neuron), ("network", net)]:
    model.fit(X_train, y_train)                     # learn from the rows
    print(name, "test accuracy:", round(model.score(X_test, y_test), 3))
print(confusion_matrix(y_test, net.predict(X_test)))  # rows: the truth

fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")
DecisionBoundaryDisplay.from_estimator(           # the class at each point
    net, X, ax=ax, response_method="predict", grid_resolution=300,
    multiclass_colors=["C0", "C1", "C2"], alpha=0.25,
    xlabel="Bill length (mm)", ylabel="Bill depth (mm)")
for species, rows in X_test.groupby(y_test):
    ax.scatter(rows["bill_length_mm"], rows["bill_depth_mm"], label=species)
ax.set_title("The network's regions; the points are the test rows")
ax.legend(frameon=False)
fig.savefig("species.svg")
plt.show()
```

```text
$ python species.py
233 training rows, 100 test rows
always the largest class: 0.44
one neuron test accuracy: 0.94
network test accuracy: 0.96
[[42  2  0]
 [ 0 18  2]
 [ 0  0 36]]
```

![Bill depth against bill length for the 100 test penguins, coloured by species, over the three regions the network assigns: Adelie (blue) upper left with short, deep bills; Gentoo (green) lower right with long, shallow bills; Chinstrap (orange) between them on the right with long, deep bills, its region bent around the points and reaching into the empty lower left corner](img/s16/species.svg)

**Notice:** the confusion matrix has the truth in its rows (Adelie, Chinstrap, Gentoo) and the model's answer in its columns: 4 of the 100 test penguins are on the wrong side.

**Ask the room:** the network's Chinstrap region reaches into the lower left corner. What would it say about a penguin with a 33 mm bill, 14 mm deep?

??? note "Answer"
    Chinstrap; one neuron says Adelie. Neither answer means anything: no
    penguin of the training rows lies there, and the network bent its
    boundary to fit the rows it had. A model is tested only where it has
    seen data; outside it, the straight lines and the bends extrapolate,
    each in its own way.

---

### 4. Chinstrap or not, from the bill length alone: the threshold is a choice { #threshold }

<!-- 0:25 · 9 min -->

A classifier gives a score between 0 and 1; the cut that turns it into yes or no is set by a person, from what each kind of error costs.

```python title="chinstrap.py"
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

url = ("https://vincentarelbundock.github.io/Rdatasets/csv/palmerpenguins/"
       "penguins.csv")
df = pd.read_csv(url).dropna()
X = df[["bill_length_mm"]]                       # one measurement only
y = df["species"] == "Chinstrap"                 # True for 68 of 333
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0, stratify=y)

model = LogisticRegression().fit(X_train, y_train)
score = model.predict_proba(X_test)[:, 1]        # between 0 and 1
print("never Chinstrap, accuracy:", round(1 - y_test.mean(), 2))
print("area under the ROC curve:", round(roc_auc_score(y_test, score), 3))
for cut in [0.2, 0.5, 0.8]:
    tn, fp, fn, tp = confusion_matrix(y_test, score > cut).ravel()
    print(f"cut {cut}: accuracy {(tp + tn) / len(y_test):.2f}, "
          f"found {tp} of {tp + fn} Chinstraps, {fp} others called one")
```

```text
$ python chinstrap.py
never Chinstrap, accuracy: 0.8
area under the ROC curve: 0.842
cut 0.2: accuracy 0.68, found 16 of 20 Chinstraps, 28 others called one
cut 0.5: accuracy 0.82, found 4 of 20 Chinstraps, 2 others called one
cut 0.8: accuracy 0.81, found 1 of 20 Chinstraps, 0 others called one
```

**Notice:** at the usual cut of 0.5 the model is right for 82 % of the test penguins, against 80 % for the rule "never a Chinstrap", and finds 4 of the 20 Chinstraps.

**Ask the room:** you count Chinstraps for a survey and a researcher checks every penguin the model names. Which cut, and why is the accuracy the wrong number to choose it by?

??? note "Answer"
    0.2: it finds 16 of the 20, and the researcher removes the 28 others by
    looking. A missed Chinstrap is lost; a wrong one costs a look. The
    accuracy (0.68) is the lowest of the three, because it counts both
    errors alike and four penguins in five are not Chinstraps. The area
    under the ROC curve, 0.842, needs no cut: the chance that a random
    Chinstrap scores higher than a random other penguin.

---

### 5. Male or female: deeper trees fit the learned rows, not new ones { #depth }

<!-- 0:34 · 9 min -->

A model that fits its training rows better and better gets worse on rows it has not seen; cross-validation holds out each fifth of the rows in turn and gives a mean and a spread.

```python title="depth.py"
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

url = ("https://vincentarelbundock.github.io/Rdatasets/csv/palmerpenguins/"
       "penguins.csv")
df = pd.read_csv(url).dropna()
X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm",
        "body_mass_g"]]
y = df["sex"]                                    # 168 male, 165 female

folds5 = KFold(n_splits=5, shuffle=True, random_state=0)  # rows shuffled
depths, fitted, folds, spread = range(1, 11), [], [], []
for depth in depths:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=0)
    scores = cross_val_score(tree, X, y, cv=folds5)  # each fold held out once
    fitted.append(tree.fit(X, y).score(X, y))    # on the rows it learned
    folds.append(scores.mean())
    spread.append(scores.std())
    print(f"depth {depth:2d}: learned rows {fitted[-1]:.3f}, "
          f"held-out folds {scores.mean():.3f} ± {scores.std():.3f}")

fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
ax.plot(depths, fitted, "o-", label="the rows it learned from")
ax.errorbar(depths, folds, yerr=spread, fmt="o-", capsize=3,
            label="held-out folds, mean ± sd of 5")
ax.set_xticks(depths)
ax.set_xlabel("Depth of the tree (questions in a row)")
ax.set_ylabel("Accuracy, male or female")
ax.set_title("Penguins, male or female: deeper trees learn the rows by heart")
ax.legend(frameon=False)
fig.savefig("depth.svg")
plt.show()
```

```text
$ python depth.py
depth  1: learned rows 0.724, held-out folds 0.703 ± 0.017
depth  2: learned rows 0.880, held-out folds 0.883 ± 0.043
depth  3: learned rows 0.916, held-out folds 0.892 ± 0.019
depth  4: learned rows 0.931, held-out folds 0.880 ± 0.014
depth  5: learned rows 0.952, held-out folds 0.886 ± 0.022
depth  6: learned rows 0.967, held-out folds 0.868 ± 0.022
depth  7: learned rows 0.985, held-out folds 0.868 ± 0.029
depth  8: learned rows 0.988, held-out folds 0.859 ± 0.030
depth  9: learned rows 0.994, held-out folds 0.853 ± 0.041
depth 10: learned rows 1.000, held-out folds 0.856 ± 0.037
```

![Accuracy against the depth of the tree, 1 to 10: on the rows it learned from (blue) it rises from 0.72 to 1.00; on the held-out folds (orange, with error bars of one standard deviation of the five folds) it rises to 0.89 at depth 3 and falls slowly to 0.86 at depth 10](img/s16/depth.svg)

**Notice:** at depth 10 the tree is right for every row it learned from and for 86 % of new ones; on new rows depths 2 to 5 lie within their spread of each other.

**Ask the room:** a tree a question deeper always fits the learned rows better. Why does it get worse on new ones?

??? note "Answer"
    Each question splits the rows into smaller groups; ten questions in a
    row leave groups of one or two penguins, so the tree remembers
    individual birds, their measurement errors included. Those details do
    not repeat in new penguins. The depth is chosen by the held-out folds,
    never by the learned rows; any depth from 2 to 5 is as good as the
    others within the spread.

---

### 6. Three groups without labels: k-means on grams and millimetres { #kmeans }

<!-- 0:43 · 8 min -->

k-means puts the rows into k groups by distance, without labels; a column with large numbers decides the distances unless every column is put on one scale first.

```python title="clusters.py"
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

url = ("https://vincentarelbundock.github.io/Rdatasets/csv/palmerpenguins/"
       "penguins.csv")
df = pd.read_csv(url).dropna()
X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm",
        "body_mass_g"]]
print(X.describe().loc[["mean", "std"]].round(1))

kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)  # 10 starts
raw = kmeans.fit_predict(X)                      # grams and millimetres
scaled = kmeans.fit_predict(StandardScaler().fit_transform(X))
print(pd.crosstab(df["species"], raw, colnames=["group, raw"]))
print(pd.crosstab(df["species"], scaled, colnames=["group, scaled"]))
```

```text
$ python clusters.py
      bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
mean            44.0           17.2              201.0       4207.1
std              5.5            2.0               14.0        805.2
group, raw   0    1   2
species                
Adelie       0  108  38
Chinstrap    0   52  16
Gentoo      70    1  48
group, scaled    0    1   2
species                    
Adelie         124    0  22
Chinstrap        5    0  63
Gentoo           0  119   0
```

**Notice:** without scaling the groups follow the body mass, whose standard deviation, 805 g, dwarfs the 2 mm of the bill depth; scaled, each group is mostly one species.

**Ask the room:** k-means was asked for 3 groups. What would it return for 5, and would that show that there are 5 kinds of penguin?

??? note "Answer"
    Five groups: k-means always returns as many as it is asked for, whether
    the data has them or not. The number is a choice of the person; that
    the scaled groups match the three species is a check that only labels
    could make. Here they exist; for unlabelled data, the groups are a
    question, not a finding.

---

### 7. Library card: the calls of this page { #card }

<!-- 0:51 · 4 min -->

Every call of the examples and of the solution below, one line each. Every model of scikit-learn has `fit` and `predict`.

| Call | What it does |
|--|--|
| `train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)` | 70 % of the rows to learn from, 30 % to test, the classes in the same shares |
| `make_pipeline(StandardScaler(), model)` | scale each column with the training rows' mean and sd, then the model |
| `LogisticRegression()` | one neuron: a weighted sum through the sigmoid |
| `MLPClassifier(hidden_layer_sizes=(8,), solver="lbfgs", max_iter=5000)` | a network with one hidden layer of 8 neurons |
| `DecisionTreeClassifier(max_depth=3)`, `RandomForestClassifier(n_estimators=200)` | a tree of at most 3 questions in a row; 200 trees on random samples, their votes |
| `model.fit(X, y)`, `model.predict(X)`, `model.score(X, y)` | learn; answer; the share of right answers |
| `model.predict_proba(X)[:, 1]` | the score of the second class, between 0 and 1 |
| `confusion_matrix(truth, answers)` | counts: truth in the rows, answers in the columns |
| `roc_auc_score(truth, score)` | the chance that a random row of class 1 scores higher than one of class 0 |
| `cross_val_score(model, X, y, cv=KFold(5, shuffle=True))` | the accuracy on each of 5 held-out folds |
| `KMeans(n_clusters=3, n_init=10).fit_predict(X)` | a group number for each row, the best of 10 starts |
| `pd.crosstab(a, b)` | how often each pair of values occurs |
| `DecisionBoundaryDisplay.from_estimator(model, X, response_method="predict")` | the class the model gives at each point of the plane |
| `series.shift(1)`, `series.shift(-1)`, `series.asfreq("D")` | yesterday's and tomorrow's value beside today's; one row for every day |

---

## Part 3 · The problem { #part-3 }

### 8. Will tomorrow be warmer than today? { #problem }

<!-- 0:55 · 50 min: predict 5, solve 25, check 10, hand in 10 -->

The daily mean temperature of Vilnius, 1881 to August 2025 (GHCN-Daily, NOAA
NCEI; terms and citation under "Before the session"), `TAVG` in tenths of °C.
From today, yesterday and the time of year, can a model say whether tomorrow's
mean will be higher than today's, more often than a coin? Download the file
once (6.1 MB); the times in curl's last line differ per laptop.

```text
$ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5976k  100 5976k    0     0  3602k      0  0:00:01  0:00:01 --:--:-- 3600k
```

Work in pairs, with any tools, an LLM too: the work is the split, the comparison and the checks, not the typing.

1. **Predict**, before any code: on what share of days will your model be
   right (50 %? 60 %? 90 %?), and what could it know that a coin does not?
   One reason.
2. **Solve.** Learn from 1951–2010, choose between models on 2011–2015,
   and test the chosen one once on 2016–2023: its accuracy with its ±,
   and the accuracy of the simplest rule.
3. **Check the machine's work.**
    - By hand: the first three rows of your table; is "warmer" right for
      each? What does your code do when tomorrow equals today?
    - The split: does every test day come after every training day? A
      shuffled split, the default of many examples, mixes the years.
    - The baseline and the n: on what share of test days was tomorrow
      warmer, and what does "always no" score? Your ± with n = the number of
      test days: √(p (1 − p) / n).
    - A leak: is every input known on the evening of today? A result above
      90 % is a reason to look for one.
    - Against your prediction: if they differ, why?
4. **Hand in** the test accuracy with its ±, the accuracy of the simplest
   rule beside it, and two sentences: what the model knows that a coin does
   not, and how sure you are.

??? tip "Hint 1: one row per day"
    `temp = (df["TAVG"] / 10).asfreq("D")` gives one row for every day, a
    missing day as `NaN`, so that `temp.shift(-1)` (tomorrow beside today)
    does not jump over a gap. Then `dropna()` and the column `warmer`:
    `tomorrow > today`.

??? tip "Hint 2: the time of year as two numbers"
    The model does not know that 31 December lies next to 1 January. With
    `angle = 2π × day of year / 365.25`, the two inputs `cos(angle)` and
    `sin(angle)` put the days on a circle, and the two ends of the year
    meet.

??? tip "Hint 3: the split by years"
    `days[(year >= 1951) & (year <= 2010)]` and so on, with `year =
    days.index.year`. Choose between models (one neuron, a forest) by their
    accuracy on 2011–2015; look at 2016–2023 once, at the end, with the one
    you chose.

??? note "One solution"
    ```python title="warmer.py"
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix, roc_auc_score

    df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"],
                     parse_dates=["DATE"], index_col="DATE")
    temp = (df["TAVG"] / 10).asfreq("D")             # a missing day becomes NaN
    days = pd.DataFrame({"yesterday": temp.shift(1), "today": temp,
                         "tomorrow": temp.shift(-1)})
    angle = 2 * np.pi * days.index.day_of_year / 365.25
    days["season_cos"], days["season_sin"] = np.cos(angle), np.sin(angle)
    days = days.dropna()
    days["warmer"] = days["tomorrow"] > days["today"]
    print(days.head(3))
    inputs = ["yesterday", "today", "season_cos", "season_sin"]
    year = days.index.year
    train = days[(year >= 1951) & (year <= 2010)]
    valid = days[(year >= 2011) & (year <= 2015)]    # to choose the model
    test = days[(year >= 2016) & (year <= 2023)]     # looked at once, at the end
    print(len(train), len(valid), len(test), "days; warmer on",
          round(test["warmer"].mean(), 3), "of the test days")

    neuron = LogisticRegression()
    forest = RandomForestClassifier(n_estimators=200, random_state=0)
    for name, model in [("neuron", neuron), ("forest", forest)]:
        model.fit(train[inputs], train["warmer"])
        print(f"{name}: training {model.score(train[inputs], train['warmer']):.3f}"
              f", validation {model.score(valid[inputs], valid['warmer']):.3f}")

    accuracy = neuron.score(test[inputs], test["warmer"])
    error = (accuracy * (1 - accuracy) / len(test)) ** 0.5
    score = neuron.predict_proba(test[inputs])[:, 1]
    print(f"test, the neuron: {accuracy:.3f} ± {error:.3f}, "
          f"AUC {roc_auc_score(test['warmer'], score):.3f}")
    print(confusion_matrix(test["warmer"], neuron.predict(test[inputs])))
    ```

    ```text
    $ python warmer.py
                yesterday  today  tomorrow  season_cos  season_sin  warmer
    DATE                                                                  
    1881-01-02        1.2   -0.8       1.6    0.999408    0.034398    True
    1881-01-03       -0.8    1.6       1.6    0.998669    0.051584   False
    1881-01-04        1.6    1.6       0.2    0.997634    0.068755   False
    21903 1826 2915 days; warmer on 0.498 of the test days
    neuron: training 0.615, validation 0.607
    forest: training 0.999, validation 0.580
    test, the neuron: 0.614 ± 0.009, AUC 0.666
    [[1118  344]
     [ 780  673]]
    ```

    The forest learned the training years almost perfectly and was worse
    on 2011–2015, so the neuron was chosen. On the 2915 days of 2016–2023
    it was right on 61.4 ± 0.9 % of them; "never warmer" is right on
    50.2 %. The model says whether tomorrow will be warmer more often than
    a coin, by 11 points, 12 standard errors. Today and the time of year
    tell it whether today is unusually cold or warm for its date, and the
    weather tends to return towards the usual (Part 4). On the 1881-01-03
    row tomorrow equals today, and `>` counts it as not warmer.

**With your own project data:** a yes-or-no question about the next
measurement of your project. Split by time, compare a model with the simplest
rule on rows it has never seen, and give the accuracy with its ±.

---

## Part 4 · Show and discuss { #part-4 }

### 9. Three questions about the pairs' models { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their accuracy, the simplest rule beside it, and read their two sentences.

**Ask the room:** one pair added the 3-day mean around today as an input and got 100 %. What happened?

??? note "Answer"
    A leak: the mean of yesterday, today and tomorrow holds tomorrow. Given
    it and today, "warmer" can be read off exactly. The same happens with
    any input measured after the evening of today. A result far above the
    simplest rule is checked for a leak before it is believed.

    ```python title="leak.py"
    import pandas as pd
    from sklearn.linear_model import LogisticRegression

    df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"],
                     parse_dates=["DATE"], index_col="DATE")
    temp = (df["TAVG"] / 10).asfreq("D")
    days = pd.DataFrame({"yesterday": temp.shift(1), "today": temp,
                         "tomorrow": temp.shift(-1),
                         "smooth": temp.rolling(3, center=True).mean()})
    days = days.dropna()
    days["warmer"] = days["tomorrow"] > days["today"]
    train = days[(days.index.year >= 1951) & (days.index.year <= 2010)]
    test = days[(days.index.year >= 2016) & (days.index.year <= 2023)]
    for inputs in [["yesterday", "today"], ["yesterday", "today", "smooth"]]:
        model = LogisticRegression(max_iter=1000).fit(train[inputs],
                                                      train["warmer"])
        print(inputs, round(model.score(test[inputs], test["warmer"]), 3))
    ```

    ```text
    $ python leak.py
    ['yesterday', 'today'] 0.544
    ['yesterday', 'today', 'smooth'] 1.0
    ```

**Ask the room:** the forest was right on 99.9 % of the training days and on 58 % of 2011–2015. Which number says how good it is?

??? note "Answer"
    The 58 %. 200 deep trees remember every training day, its noise
    included, as the deep tree of section 5 remembered single penguins. The
    weather of a day repeats only in its broad lines; the 0.1 °C details
    the forest learned do not come back. Had the test years been used to
    choose between the two, the test would no longer measure days the
    choice had not seen.

**Ask the room:** what does the model know that a coin does not? Predict first: after a day 6 °C colder than usual for its date, how often is the next day warmer?

??? note "Answer"
    About two times in three. Weather returns towards the usual for the
    time of year: an unusually cold day is more often followed by a warmer
    one, an unusually warm day by a colder one. On 1951–2010:

    ```python title="anomaly.py"
    import pandas as pd

    df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"],
                     parse_dates=["DATE"], index_col="DATE")
    temp = (df["TAVG"] / 10).asfreq("D")
    days = pd.DataFrame({"today": temp, "tomorrow": temp.shift(-1)}).dropna()
    days = days[(days.index.year >= 1951) & (days.index.year <= 2010)]
    days["warmer"] = days["tomorrow"] > days["today"]
    usual = days.groupby(days.index.day_of_year)["today"].transform("mean")
    days["anomaly"] = days["today"] - usual          # °C above the usual day
    groups = pd.cut(days["anomaly"], [-30, -6, -2, 2, 6, 30])
    print(days.groupby(groups, observed=True)["warmer"].agg(["mean", "count"])
          .round(3))
    ```

    ```text
    $ python anomaly.py
                mean  count
    anomaly                
    (-30, -6]  0.680   1552
    (-6, -2]   0.618   4965
    (-2, 2]    0.498   8226
    (2, 6]     0.399   5769
    (6, 30]    0.276   1395
    ```

    On days within 2 °C of the usual the next day is warmer half the time,
    as with a coin; the model's 61 % comes from the days far from the usual.

A model is judged on days it has never seen, against the simplest rule, and a result far better than that rule is checked for a leak before it is believed.

---

## Optional, if the room is fast { #optional }

### 10. How much warmer: a forecast in °C { #how-much }

<!-- — · 15 min -->

Instead of yes or no, forecast tomorrow's mean itself (`LinearRegression`),
and compare it with the simplest forecast, "tomorrow as today", by the mean
absolute error in °C on 2016–2023. Predict, solve, check, hand in, as in
section 8.

??? note "One solution"
    ```python title="howmuch.py"
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error

    df = pd.read_csv("LH000026730.csv", usecols=["DATE", "TAVG"],
                     parse_dates=["DATE"], index_col="DATE")
    temp = (df["TAVG"] / 10).asfreq("D")
    days = pd.DataFrame({"yesterday": temp.shift(1), "today": temp,
                         "tomorrow": temp.shift(-1)})
    angle = 2 * np.pi * days.index.day_of_year / 365.25
    days["season_cos"], days["season_sin"] = np.cos(angle), np.sin(angle)
    days = days.dropna()
    inputs = ["yesterday", "today", "season_cos", "season_sin"]
    train = days[(days.index.year >= 1951) & (days.index.year <= 2015)]
    test = days[(days.index.year >= 2016) & (days.index.year <= 2023)]

    model = LinearRegression().fit(train[inputs], train["tomorrow"])
    forecast = model.predict(test[inputs])
    print(f"tomorrow as today: off by "
          f"{mean_absolute_error(test['tomorrow'], test['today']):.2f} °C")
    print(f"linear model:      off by "
          f"{mean_absolute_error(test['tomorrow'], forecast):.2f} °C")
    print("weights:", ", ".join(f"{name} {weight:+.3f}"
                                for name, weight in zip(inputs, model.coef_)))
    ```

    ```text
    $ python howmuch.py
    tomorrow as today: off by 1.81 °C
    linear model:      off by 1.72 °C
    weights: yesterday -0.161, today +0.962, season_cos -2.278, season_sin -0.515
    ```

    The model is off by 1.72 °C on an average day, "tomorrow as today" by
    1.81 °C: 5 % better. Almost all of the forecast is today (weight
    0.962); the season and yesterday pull it a little towards the usual.

---

## Aims practised

- ♻️ **Reproducibility:** every split and model has a fixed
  `random_state`; the test years are looked at once, and `environment.yml`
  names scikit-learn's version.
- 🔧 **Tool-agnosticism:** one neuron, a network, a tree, a forest and
  k-means, all with `fit` and `predict`; the checks (a test on unseen rows,
  the simplest rule, a leak) hold whatever wrote the code.
- 📁 **Data & files:** one public file of 145 years becomes a table of days
  in memory; nothing is written to disk but the figures.
