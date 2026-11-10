# Seminar 10 · A Class of Your Own

**Paired lecture:** 10 Classification and the Perceptron · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Will it freeze tonight in Vilnius, and how often is a rule right on years it has not seen?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both). A line that starts with `$` is typed without the `$`; every other
line is what comes back; `...` stands for lines left out.

**If time runs short:** leave out section 6 (seen and unseen penguins) and say its idea in one line: a score counts only on rows the model has not seen.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the data and for
      conda: scikit-learn, today's new library, and SciPy, which it needs,
      a few tens of MB; on a laptop without the environment `analysis` also
      Python, pandas and Matplotlib (about 80 MB on a Mac, 200 MB on
      Windows). Nothing from earlier seminars is needed.
    - **No file is handed out.** The data come from their public addresses:
        - bill measurements of 342 penguins of three species, Palmer
          Archipelago, Antarctica, 2007–2009 (16 kB, read by the scripts of
          Part 2): Palmer Station LTER and K. Gorman, the R package
          palmerpenguins (CC0), as a CSV file of the Rdatasets collection;
        - the daily weather of the Vilnius station since 1881 (6.1 MB,
          fetched once with `curl` in section 3): NOAA NCEI, GHCN-Daily
          version 3.35, station `LH000026730` (Menne et al. 2012,
          doi:10.7289/V5D21VHZ, read on 10 November 2026); exchanged under
          WMO Resolution 40, free for research, education and other
          non-commercial use.
    - **The numbers:** every output on this page was printed on
      10 November 2026. The problem uses the years 1945–2009, so days that
      NOAA adds at the end of the station file change nothing.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Set up { #part-1 }

### 1. A new folder, and the environment `analysis` { #start }

<!-- 0:00 · 7 min -->

An environment is a folder with its own Python and its own packages; `analysis` serves weeks 8 to 12, and each week adds its package.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s10
    $ cd ~/weather-s10
    ```

2. **File** > **Open Folder...** > `weather-s10` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. Switch on `analysis`, the environment of Seminars 8 and 9.

    ```text
    $ conda activate analysis
    ```

    Conda answers `Could not find conda environment: analysis`: this laptop
    has none yet. Make it with Python, pandas, Matplotlib and today's
    scikit-learn in one line (a few minutes; at `Proceed ([y]/n)?` press
    `Enter`), then switch it on:

    ```text
    $ conda create -n analysis python=3.14 pandas=3.1 matplotlib-base=3.11 scikit-learn=1.9
    ...
    Proceed ([y]/n)?
    ...
    $ conda activate analysis
    ```

4. Ask which Python answers.

    ```text
    $ python --version
    Python 3.14.10
    ```

**Check:** `(analysis)` at the start of the prompt, and a Python `3.14` (the last number may be higher).

---

### 2. Install scikit-learn, write the list { #install }

<!-- 0:07 · 6 min -->

**scikit-learn** is the Python library of machine learning; each of its models is a class with the methods `fit` and `predict`, as the class of section 4.

1. Install it, with its version. At `Proceed ([y]/n)?` press `Enter`. A
   laptop that made `analysis` in section 1 has it already, and conda says
   so.

    ```text
    $ conda install scikit-learn=1.9
    ...
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/analysis

      added / updated specs:
        - scikit-learn=1.9
    ...
    Proceed ([y]/n)?
    ```

2. Ask for the version. The package is called `scikit-learn`, the module
   `sklearn`.

    ```text
    $ python -c "import sklearn; print(sklearn.__version__)"
    1.9.1
    ```

3. Write the environment into today's folder, then click `environment.yml`
   in the Explorer, delete its last line, `prefix: ...` (a folder on this
   laptop), save (`Ctrl+S`, macOS `Cmd+S`).

    ```text
    $ conda env export --from-history -f environment.yml
    ```

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

    The package just installed is the last line; the others may stand in
    another order, and a laptop that installed SciPy in Seminar 9 has
    `- scipy=1.18` too.

4. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/analysis` in its
   path. The Status Bar shows `analysis`.

**Check:** `1.9.1` (the last digit may be higher), and `- scikit-learn=1.9` in `environment.yml`.

---

### 3. Fetch the daily weather of Vilnius, once { #data }

<!-- 0:13 · 2 min -->

The problem of Part 3 reads one file of NOAA's: the weather station of Vilnius, day by day since 1881, 6.1 MB. `curl` copies it into the folder once; `-O` keeps its name.

```text
$ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
...
```

**Check:** `LH000026730.csv` in the Explorer, about 6.1 MB.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs three complete scripts and one class; the room watches
and may type along. For each: in the Explorer, right-click > **New
File...**, the name above the code, paste, save; run the scripts in the
terminal. A window opens with the figure; close it and the prompt comes
back.

### 4. A class `Perceptron` learns the line between two penguin species { #class }

<!-- 0:15 · 13 min -->

A **class** keeps numbers together with the functions that use them: `Perceptron()` makes an **object** with its own `w` and `b`; its **methods** `fit`, `predict` and `score` change them or use them.

The class goes into a file of its own, a module that every later script imports:

```python title="perceptron.py"
class Perceptron:
    """One neuron that learns by Rosenblatt's rule: w, b, predict, fit."""

    def __init__(self):
        self.w = [0.0, 0.0]   # one weight for each of the two inputs
        self.b = 0.0          # the bias
        self.updates = []     # how many rows changed w in each epoch

    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if z > 0:
            return 1
        return 0

    def fit(self, xs, ys, epochs):
        for epoch in range(epochs):
            changed = 0
            for x, y in zip(xs, ys):        # each row with its label
                error = y - self.predict(x)  # 0 if right, +1 or -1 if not
                if error != 0:
                    self.w[0] = self.w[0] + error * x[0]
                    self.w[1] = self.w[1] + error * x[1]
                    self.b = self.b + error
                    changed = changed + 1
            self.updates.append(changed)
            if changed == 0:                # every row right: stop
                break

    def score(self, xs, ys):
        right = 0
        for x, y in zip(xs, ys):
            if self.predict(x) == y:
                right = right + 1
        return right / len(xs)
```

`__init__` runs once, when `Perceptron()` makes the object; `self` is that
object, and `self.w` a value kept in it. A method is a `def` inside the
class: `model.fit(...)` runs `fit` with `self` set to `model`. `fit` is
**Rosenblatt's rule**: after each wrong row, add the error (+1 or −1) times
each input to its weight, and the error to `b`. One pass over all rows is
an **epoch**.

Then the penguins: the length and the depth of the bill of 274 Adelie and
Gentoo penguins, in mm, and the species as 0 or 1.

```python title="penguins.py"
import matplotlib.pyplot as plt
import pandas as pd
from perceptron import Perceptron

URL = ("https://vincentarelbundock.github.io/Rdatasets/csv/"
       "palmerpenguins/penguins.csv")
df = pd.read_csv(URL).dropna(subset=["bill_length_mm", "bill_depth_mm"])
df = df[df["species"].isin(["Adelie", "Gentoo"])]
xs = df[["bill_length_mm", "bill_depth_mm"]].to_numpy().tolist()
ys = (df["species"] == "Gentoo").astype(int).tolist()   # Gentoo is 1
print(len(xs), "penguins,", sum(ys), "of them Gentoo; the first:",
      xs[0], ys[0])

model = Perceptron()
model.fit(xs, ys, 100)
print("updates in each epoch:", model.updates)
print("w =", [round(v, 1) for v in model.w], "b =", model.b,
      "right on", model.score(xs, ys))

fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
for name, part in df.groupby("species"):
    ax.scatter(part["bill_length_mm"], part["bill_depth_mm"], s=12,
               label=name)
w, b = model.w, model.b
ax.plot([32, 60], [-(w[0] * 32 + b) / w[1], -(w[0] * 60 + b) / w[1]],
        color="black", label="z = 0, the line the class learned")
ax.set_xlabel("Bill length (mm)")
ax.set_ylabel("Bill depth (mm)")
ax.set_title("274 penguins: after 12 epochs, every one on its side")
ax.legend(frameon=False)
fig.savefig("penguins.svg")
plt.show()
```

`isin` keeps the rows of two species; `.to_numpy().tolist()` turns two
columns into a list of rows, `[length, depth]`. The line is where
z = w₁x₁ + w₂x₂ + b is 0: at x₁, the depth x₂ = −(w₁x₁ + b) / w₂.

```text
$ python penguins.py
274 penguins, 123 of them Gentoo; the first: [39.1, 18.7] 0
updates in each epoch: [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0]
w = [29.1, -74.0] b = -1.0 right on 1.0
```

![274 penguins by bill length (32 to 60 mm) and bill depth (13 to 22 mm): the Adelie penguins upper left, short and deep bills; the Gentoo penguins lower right, long and shallow bills; a black line from lower left to upper right with every Adelie above it and every Gentoo below it, one Gentoo close to it at 44.4 and 17.3 mm](img/s10/penguins.svg)

**Notice:** the rule stops by itself in epoch 12, when no row changes `w`: one line has every penguin of the two species on its side.

**Ask the room:** in epoch 1 only one row changed `w`. Which one, and why only one?

??? note "Answer"
    The first Gentoo, row 153 of the file (46.1 and 13.2 mm). From
    w = (0, 0) and b = 0, z is 0 and `predict` says 0, which is right for
    all 151 Adelie rows before it. The first Gentoo is wrong, so
    w = (46.1, 13.2) and b = 1; from then on z is far above 0 for every
    Gentoo, and right again.

!!! warning "An error instead of a figure"
    - `ModuleNotFoundError: No module named 'perceptron'`: the class is
      not saved as `perceptron.py` in `weather-s10`, or the terminal is
      somewhere else: `cd ~/weather-s10`, `ls`.
    - `UserWarning: FigureCanvasAgg is non-interactive`: this Python opens
      no window. The figure is in the file: `open penguins.svg` (macOS) or
      `start penguins.svg` (Git Bash).

---

### 5. Two species that overlap: the class never stops, scikit-learn's model settles { #library }

<!-- 0:28 · 10 min -->

scikit-learn's models are classes with the same methods; `LogisticRegression` is the neuron with the sigmoid, 1 / (1 + e⁻ᶻ) in place of the step: it settles where the classes overlap, and gives a probability.

```python title="library.py"
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from perceptron import Perceptron

URL = ("https://vincentarelbundock.github.io/Rdatasets/csv/"
       "palmerpenguins/penguins.csv")
df = pd.read_csv(URL).dropna(subset=["bill_length_mm", "bill_depth_mm"])
df = df[df["species"].isin(["Adelie", "Chinstrap"])]
xs = df[["bill_length_mm", "bill_depth_mm"]].to_numpy().tolist()
ys = (df["species"] == "Chinstrap").astype(int).tolist()  # Chinstrap: 1

mine = Perceptron()
mine.fit(xs, ys, 1000)
logit = LogisticRegression()
logit.fit(xs, ys)
print("mine: updates in the last five epochs:", mine.updates[-5:])
print("scikit-learn: w =", logit.coef_[0].round(2),
      "b =", logit.intercept_[0].round(2))
print("right:", round(mine.score(xs, ys), 3), round(logit.score(xs, ys), 3))
print("P(Chinstrap) of a bill 45 mm long, 18 mm deep:",
      logit.predict_proba([[45, 18]])[0, 1].round(2))

fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
for name, part in df.groupby("species"):
    ax.scatter(part["bill_length_mm"], part["bill_depth_mm"], s=12,
               label=name)
for label, w, b, colour in [
        ("Mine, after 1000 epochs", mine.w, mine.b, "grey"),
        ("LogisticRegression", logit.coef_[0], logit.intercept_[0], "black")]:
    ends = [-(w[0] * 32 + b) / w[1], -(w[0] * 60 + b) / w[1]]
    ax.plot([32, 60], ends, color=colour, label=label)
ax.set_ylim(15, 22)
ax.set_xlabel("Bill length (mm)")
ax.set_ylabel("Bill depth (mm)")
ax.set_title("Adelie and Chinstrap overlap: two lines, two scores")
ax.legend(frameon=False, loc="lower right")
fig.savefig("library.svg")
plt.show()
```

`coef_` and `intercept_` are scikit-learn's names for w and b; a name that
ends in `_` is set by `fit`. `predict_proba` gives, for each row, the
probability of 0 and of 1.

```text
$ python library.py
mine: updates in the last five epochs: [2, 2, 4, 4, 4]
scikit-learn: w = [ 1.36 -1.92] b = -24.55
right: 0.763 0.973
P(Chinstrap) of a bill 45 mm long, 18 mm deep: 0.87
```

![219 Adelie and Chinstrap penguins by bill length and depth: the Adelie penguins on the left, below 46 mm, the Chinstrap penguins on the right, from 41 to 58 mm, a few of each among the other; a grey line, the class after 1000 epochs, cuts through the Adelie cloud; a black line, LogisticRegression, runs steeply between the two clouds, from 41 mm at a depth of 16 mm to 48 mm at 21 mm](img/s10/library.svg)

**Notice:** after 1000 epochs the class still changes `w` four times an epoch, and where it was stopped, its line is right on 76.3 % of the penguins; `LogisticRegression` settles and is right on 97.3 %.

**Ask the room:** a penguin with a bill 45 mm long and 18 mm deep gets P(Chinstrap) = 0.87. What would the class `Perceptron` say about it, and what does it not say?

??? note "Answer"
    It says 1 or 0, Chinstrap or not, with nothing about how sure. A bill
    of 45 mm lies where both species occur; 0.87 says "Chinstrap, but
    about one such penguin in eight is an Adelie". The step has no slope,
    so Rosenblatt's rule jumps from line to line on overlapping classes;
    the sigmoid gives a loss with a lowest point, which `fit` finds.

---

### 6. Seen and unseen penguins: a rule that remembers every one { #unseen }

<!-- 0:38 · 9 min -->

A score on the rows a model learned from says how well it remembers them; only rows kept back say how well it does on new ones.

```python title="unseen.py"
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

URL = ("https://vincentarelbundock.github.io/Rdatasets/csv/"
       "palmerpenguins/penguins.csv")
df = pd.read_csv(URL).dropna(subset=["bill_length_mm", "bill_depth_mm"])
df = df[df["species"].isin(["Adelie", "Chinstrap"])]
xs = df[["bill_length_mm", "bill_depth_mm"]].to_numpy()
ys = (df["species"] == "Chinstrap").astype(int).to_numpy()

seen_x, unseen_x, seen_y, unseen_y = train_test_split(
    xs, ys, test_size=0.3, random_state=0)   # 30 % kept back
print(len(seen_y), "penguins to learn from,", len(unseen_y), "kept back")

for model in [KNeighborsClassifier(n_neighbors=1), LogisticRegression()]:
    model.fit(seen_x, seen_y)
    seen = model.score(seen_x, seen_y)
    unseen = model.score(unseen_x, unseen_y)
    error = (unseen * (1 - unseen) / len(unseen_y)) ** 0.5
    print(f"{type(model).__name__}: seen {seen:.3f},",
          f"unseen {unseen:.3f} ± {error:.3f}")
```

`KNeighborsClassifier(n_neighbors=1)` keeps all 153 penguins it learns
from and answers like the nearest one. `random_state=0` keeps back the
same 66 penguins on every laptop. The ± of a share p of n rows is
√(p (1 − p) / n).

```text
$ python unseen.py
153 penguins to learn from, 66 kept back
KNeighborsClassifier: seen 1.000, unseen 0.955 ± 0.026
LogisticRegression: seen 0.961, unseen 0.985 ± 0.015
```

**Notice:** the rule that remembers every penguin is right on all 153 it has seen and on 95.5 % of the others; the logistic line, three numbers, on 96.1 % and 98.5 %.

**Ask the room:** here 66 penguins were kept back at random. Why should the days of a weather station be kept back by whole years instead?

??? note "Answer"
    Penguins are separate animals; neighbouring days are not. A day's
    weather nearly repeats the day before, so a test day picked at random
    has its yesterday and its tomorrow among the training days, and the
    score looks better than it will be next winter. Whole years kept back
    are new weather.

---

### 7. Library card: the calls of this page { #card }

<!-- 0:47 · 3 min -->

Every call of the examples and of the solution below, one line each.

| Call | What it does |
|--|--|
| `class Perceptron:` | a new type; each `def` inside it is a method |
| `def __init__(self):`, `self.w = [0.0, 0.0]` | runs once when an object is made; keeps a value in the object |
| `model = Perceptron()` | a new object, with its own `w` and `b` |
| `model.fit(xs, ys, 100)`, `model.predict(x)`, `model.score(xs, ys)` | the methods of the class, with `self` set to `model` |
| `from perceptron import Perceptron` | the class from the file `perceptron.py` |
| `for x, y in zip(xs, ys):` | each row with its label |
| `df[df["species"].isin(["Adelie", "Gentoo"])]` | keep the rows of two species |
| `df[["a", "b"]].to_numpy().tolist()` | two columns as a list of rows |
| `LogisticRegression()`, `KNeighborsClassifier(n_neighbors=1)` | two models of scikit-learn: the neuron with the sigmoid; the nearest row |
| `model.fit(X, y)`, `model.predict(X)`, `model.score(X, y)` | learn; answer 0 or 1 for each row; the share right |
| `model.coef_`, `model.intercept_` | the learned w and b |
| `model.predict_proba(X)[:, 1]` | the probability of 1 for each row |
| `train_test_split(X, y, test_size=0.3, random_state=0)` | 30 % of the rows kept back, the same ones on every run |
| `days["low"].shift(-1)` | each row gets the value of the next row: tomorrow's |
| `ax.scatter(x, y, s=12, label="Gentoo")` | points of size 12 |

---

## Part 3 · The problem { #part-3 }

### 8. Will it freeze tonight? A threshold of your own against scikit-learn { #problem }

<!-- 0:50 · 55 min: predict 5, solve 30, check 10, hand in 10 -->

From today's lowest and highest temperature in Vilnius, will tomorrow's
lowest fall below 0 °C? The file of section 3 holds `TMIN` and `TMAX`, the
lowest and the highest of each day, in tenths of a degree; both are there
for every day from 1945 to 2009 (later years have gaps). Learn from
1945–1999; score on the days of 2000–2009.

Source: NOAA NCEI, GHCN-Daily version 3.35 (Menne et al. 2012, doi:10.7289/V5D21VHZ, read on 10 November 2026); exchanged under WMO Resolution 40, free for research, education and other non-commercial use.

Work in pairs, with any tools, an LLM too: the work is the idea and the checks, not the typing.

1. **Predict**, before any code, on paper. The share of the test days that
   the rule "never frost" gets right. How often a threshold on today's
   lowest is right, and whether today's highest adds anything. Which test
   days a rule gets wrong: cold ones, warm ones, or those near 0 °C. The
   signs of the two weights. One reason each.
2. **Solve.** Two classes with `fit` and `predict`: one of your own that
   learns the best threshold on today's lowest from 1945–1999, and
   scikit-learn's `LogisticRegression` on both temperatures. Score both,
   and "never frost", on 2000–2009.
3. **Check the machine's work.**
    - 8 December 2009 by hand: lowest 0.5 °C, highest 4.0 °C. With your
      logistic model's numbers, z = w₁ × 0.5 + w₂ × 4.0 + b, then
      1 / (1 + e⁻ᶻ); `predict_proba` must agree. What did each of your
      rules say? The lowest of 9 December was 2.0 °C.
    - The ± of each share, √(p (1 − p) / n), with n the number of test
      days: is the gap between your two rules larger than it?
    - The wrong test days: how many had today's lowest between −3 and
      +3 °C? Set it against your prediction.
4. **Hand in** the share of your best rule right on 2000–2009 with its ±,
   next to "never frost", and two sentences in your own words: how much
   better than no rule, and on which days it fails.

??? tip "Hint 1: the days and their labels"
    `TMIN` and `TMAX` are in tenths of a degree; on 30 May 1994 `TMAX` is
    empty. With the days of 1945–2009 in a table, one row a day and none
    missing, `days["low"].shift(-1)` moves the column up by one row: each
    day gets tomorrow's lowest, and `< 0` turns it into 1 or 0.

??? tip "Hint 2: a class of your own"
    It holds what it learned and does two things. `fit(lows, frosts)` tries
    thresholds from −5.0 to 5.0 °C in steps of 0.1 (`np.arange(-50, 51) /
    10`: whole numbers divided by 10, as the data are) and keeps the one
    right on most training days;
    `predict(lows)` says 1 where the lowest is below it. scikit-learn's
    `LogisticRegression` takes a table of two columns: `fit(X, y)`,
    `predict(X)`, `predict_proba(X)`, `coef_`, `intercept_`.

??? tip "Hint 3: why by years"
    The label of a day, tomorrow's lowest below 0 °C, is the input of the
    next day. Split at random, a test day would have both its neighbours
    among the training days; whole years kept back are weather the rule
    has not seen.

??? note "One solution"
    ```python title="frost.py"
    import math
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression

    df = pd.read_csv("LH000026730.csv", parse_dates=["DATE"])
    df = df[df["DATE"].dt.year.between(1945, 2009)]      # no day missing
    days = pd.DataFrame({"date": df["DATE"], "year": df["DATE"].dt.year,
                         "low": df["TMIN"] / 10, "high": df["TMAX"] / 10})
    days["frost"] = (days["low"].shift(-1) < 0).astype(int)   # tomorrow
    days = days.iloc[:-1]               # the last day has no tomorrow here
    days = days.dropna()                # 30 May 1994 has no highest
    train = days[days["year"] <= 1999]
    test = days[days["year"] >= 2000]
    n = len(test)
    print(len(train), "days to learn from;", n, "test days,",
          test["frost"].sum(), "with frost")


    class Threshold:
        """Frost when today's lowest is below c; fit finds the best c."""

        def fit(self, lows, frosts):
            tries = np.arange(-50, 51) / 10              # -5.0 to 5.0 °C
            right = [((lows < c) == frosts).sum() for c in tries]
            self.c = tries[np.argmax(right)]

        def predict(self, lows):
            return (lows < self.c).astype(int)


    rule = Threshold()
    rule.fit(train["low"], train["frost"])
    logit = LogisticRegression()
    logit.fit(train[["low", "high"]], train["frost"])
    w, b = logit.coef_[0], logit.intercept_[0]
    print(f"c = {rule.c} °C; w = {w.round(3)}, b = {b:.3f}")
    said = logit.predict(test[["low", "high"]])
    for name, answers in [("never frost", 0),
                          ("lowest below c", rule.predict(test["low"])),
                          ("LogisticRegression", said)]:
        p = (answers == test["frost"]).mean()
        print(f"{name}: right on {p:.3f} ± {math.sqrt(p * (1 - p) / n):.3f}")

    wrong = test[said != test["frost"]]
    print(len(wrong), "wrong;", wrong["low"].between(-3, 3).sum(),
          "of them with today's lowest from -3 to 3 °C")
    day = test[test["date"] == "2009-12-08"]
    print(day)
    print("P(frost):", logit.predict_proba(day[["low", "high"]])[0, 1].round(3))
    ```

    ```text
    $ python frost.py
    20087 days to learn from; 3652 test days, 1177 with frost
    c = -0.2 °C; w = [-0.329 -0.217], b = 1.142
    never frost: right on 0.678 ± 0.008
    lowest below c: right on 0.897 ± 0.005
    LogisticRegression: right on 0.903 ± 0.005
    353 wrong; 292 of them with today's lowest from -3 to 3 °C
                date  year  low  high  frost
    45316 2009-12-08  2009  0.5   4.0      0
    P(frost): 0.527
    ```

    By hand, 8 December 2009: z = −0.329 × 0.5 − 0.217 × 4.0 + 1.142 =
    −0.1645 − 0.868 + 1.142 = 0.1095, and 1 / (1 + e^(−0.1095)) = 0.527. The
    logistic model says frost, the threshold says none (0.5 is not below
    −0.2), and 9 December stayed at 2.0 °C: the threshold was right.
    Both weights are negative: a colder lowest and a colder highest both
    raise the chance of frost.

    Handed in: *On the 3652 days of 2000–2009 the logistic model on
    today's lowest and highest was right on 90.3 ± 0.5 %, against
    67.8 ± 0.8 % for "never frost"; the threshold "today's lowest below
    −0.2 °C", learned from 1945–1999, was right on 89.7 ± 0.5 %, as good
    within the ±. Of the 353 wrong days, 292 had a lowest between −3 and
    +3 °C: the rules fail on the nights that could go either way.*

**With your own project data:** a yes-or-no question about the rows of your
own file. The share right for the more common answer (the baseline), a
threshold class of your own on one column, and `LogisticRegression` on two,
each scored on rows kept back, by time or by group where neighbouring rows
are alike.

---

## Part 4 · Show and discuss { #part-4 }

### 9. Three questions about the pairs' shares { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their number and read their two sentences.

**Ask the room:** one pair hands in "right on 90.3 %", another "90.3 %, against 67.8 % for never frost". What does the second say that the first does not?

??? note "Answer"
    How much of the 90.3 % the rule earned. Saying "no frost" every day
    is right on 67.8 % of these days for free. The model is wrong on 353
    days where "never frost" is wrong on 1177, all the frosts: it removes
    seven of every ten mistakes.

**Ask the room:** for 8 December 2009 the model said P(frost) = 0.53, and it did not freeze. Was the model wrong?

??? note "Answer"
    Not by that one night. 0.53 says "about one such night in two
    freezes": of the 200 test days with P from 0.4 to 0.6, 90 froze. A
    probability is checked on many days at once, never on one.

**Ask the room:** the threshold keeps one number, `LogisticRegression` three. Does today's highest help to tell frost?

??? note "Answer"
    Not that ten years can show: 0.903 against 0.897, a gap of 0.006 with
    a ± of 0.005 on each share. The two rules agree on 3408 of the 3652
    days. Today's lowest carries almost all of it; a second input earns its
    place only when the score on unseen days rises by clearly more than
    its ±.

A rule for a yes-or-no question is scored on data it has not seen, next to the rule that needs no data, with the ± of a share; its mistakes lie near its line.

---

## Optional, if the room is fast { #optional }

### 10. XOR: four points no line separates { #xor }

<!-- — · 10 min -->

XOR is 1 when exactly one of two inputs is 1. One neuron draws one line, and no line has (0, 1) and (1, 0) on one side and (0, 0) and (1, 1) on the other.

```python title="xor.py"
from sklearn.linear_model import LogisticRegression
from perceptron import Perceptron

xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
for name, ys in [("AND", [0, 0, 0, 1]), ("XOR", [0, 1, 1, 0])]:
    model = Perceptron()
    model.fit(xs, ys, 12)
    print(name, "updates in each epoch:", model.updates)
    print("   w =", model.w, "b =", model.b, "right:", model.score(xs, ys))

logit = LogisticRegression()
logit.fit(xs, [0, 1, 1, 0])
print("LogisticRegression on XOR, P(1):", logit.predict_proba(xs)[:, 1])
```

```text
$ python xor.py
AND updates in each epoch: [1, 3, 3, 2, 1, 0]
   w = [2.0, 1.0] b = -2.0 right: 1.0
XOR updates in each epoch: [2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
   w = [-1.0, 0.0] b = 1.0 right: 0.5
LogisticRegression on XOR, P(1): [0.5 0.5 0.5 0.5]
```

**Notice:** on AND the class stops after six epochs; on XOR it changes `w` four times in every epoch, for ever, and `LogisticRegression` says 0.5 for all four points: the best one line can do is to know nothing.

**Ask the room:** what would solve XOR?

??? note "Answer"
    Two lines: one neuron that says "at least one is 1" (OR), one that
    says "not both" (NAND), and a third that says 1 when both of them do.
    A network of neurons in layers.

---

## Aims practised

- 🔧 **Tool-agnostic:** the same three calls, `fit`, `predict` and
  `score`, in a class of a few dozen lines and in scikit-learn; the checks
  (one evening by hand, the ± of a share, the baseline) hold whichever tool
  or LLM wrote the code.
- ♻️ **Reproducibility:** the station's file is fetched once and kept as
  received; the split by years and `random_state=0` give every laptop the
  same numbers.
- 📁 **Files:** the class lives in its own module, `perceptron.py`, which
  every script of the page imports.
