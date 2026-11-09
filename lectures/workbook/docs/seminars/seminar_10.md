# Seminar 10 · A Class of Your Own

**Paired lecture:** 10 Classification and the Perceptron · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Will it freeze tonight?

**Today's goal:** every student writes a neuron in plain Python that says
frost or no frost for an evening at 18:00, scores it on the 3646 evenings
of the weather log, lets Rosenblatt's rule learn its three numbers from the
evenings of 2016 to 2022, and then moves the same lines into a class
`Perceptron` of their own, with the methods `predict`, `fit` and `score`,
which is right on 95.5 ± 0.6 % of the evenings of 2023 to 2025.

Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both). In the blocks, a line that starts with `$` is typed in the
terminal, a line that starts with `>>>` or `...` is typed at Python's
prompt, and every other line is what comes back; `...` alone stands for
lines left out.

**If time runs short:** skip the Tasks, but keep sections 6 and 7
(Rosenblatt's rule) and 8 to 11 (the class). Sections 14 to 17 are
optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page); internet for today's folder
      (0.6 MB), and for conda only on a laptop without the environment
      `analysis` (section 1). Nothing from earlier seminars is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** nothing to prepare: every number on this page is the number
      in the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Today's folder and the evenings { #part-1 }

<!-- 0:00 to 0:20 -->

Today's folder brings the weather log and a module `weather.py` that reads it twice a day: the evening and the next morning.

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Today needs only Python; the environment `analysis` of the last seminars has it.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s10.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s10.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s10.zip
       creating: /Users/smilte/weather-s10/
    ...
      inflating: /Users/smilte/weather-s10/scripts/weather.py
    $ cd ~/weather-s10
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s10 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s10` > **Open**. The window
   reloads: open the terminal again (**View** > **Terminal**); it starts in
   the folder.
3. Switch on the environment of the last seminars.

    ```text
    $ conda activate analysis
    ```

    If conda answers that it cannot find `analysis`, make it from the file
    in today's folder (Python, Matplotlib and pandas, a few minutes), then
    switch it on:

    ```text
    $ conda env create -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate analysis
    $ conda activate analysis
    ```

4. Check the Python, then tell VS Code: `Ctrl+Shift+P` (macOS
   `Cmd+Shift+P`), `Python: Select Interpreter`, the entry with
   `envs/analysis` in its path.

    ```text
    $ python --version
    Python 3.14.10
    ```

**Check:** `(analysis)` at the start of the prompt, `analysis` in VS Code's Status Bar, Python 3.14 (the last number may differ).

---

### 2. The evenings, at `>>>` { #evenings }

<!-- 0:10 · 10 min -->

One **evening** is one row: the date, the temperature and the humidity at 18:00, and `1` if it froze by 06:00 the next morning, else `0`.

1. Open `scripts/weather.py`. Its last function, `evenings(path)`, goes
   through the hourly lines 24 at a time: line 18 of each day is 18:00, and
   12 lines later comes 06:00 of the next day. An evening whose
   temperature or morning is `-999` is left out.
2. Try it at `>>>`. Python finds `weather.py` in the terminal's folder, so
   start it in `scripts`; the data is one folder up, `..`.

    ```text
    $ cd scripts
    $ python
    ```

    ```pycon
    >>> import weather
    >>> rows = weather.evenings("../data/raw/weather.csv")
    >>> len(rows)
    3646
    >>> rows[0]
    ['2016-01-01', -4.5, 85.0, 1]
    >>> rows[-1]
    ['2025-12-30', -9.7, 93.0, 1]
    ```

    `rows[-1]` is the last row. 1 January 2016: −4.5 °C and 85 % at 18:00,
    and frost the next morning.

3. Count the evenings followed by frost, then the share without.

    ```pycon
    >>> frost = 0
    >>> for row in rows:
    ...     frost = frost + row[3]
    ...
    >>> frost
    1229
    >>> (len(rows) - frost) / len(rows)
    0.6629182665935272
    >>> exit()
    ```

    ```text
    $ cd ..
    ```

    Press `Enter` once more after the indented line to end the loop. A rule
    that always says "no frost" is right on 2417 of 3646 evenings, 66.3 %:
    the number every rule today has to beat.

**Check:** 3646 evenings, 1229 with frost, 0.663, and the terminal back in `weather-s10` (`cd ..`).

---

## Part 2 · A neuron as a function { #part-2 }

<!-- 0:20 to 0:40 -->

A **neuron** multiplies each input by a **weight**, adds a **bias** `b`, and says 1 (frost) when the sum `z` is above 0: z = w₁x₁ + w₂x₂ + b.

---

### 3. One evening through `predict` { #predict }

<!-- 0:20 · 10 min -->

The inputs of an evening are a list `x`: the temperature, and the humidity as a fraction (85 % is 0.85). The weights are a list `w`.

1. New file `scripts/frost.py`. Type, save.

    ```python
    def predict(x, w, b):
        z = w[0] * x[0] + w[1] * x[1] + b
        if z > 0:
            return 1
        return 0


    x = [2.6, 0.85]      # 8 December 2025 at 18:00: 2.6 °C, 85 %
    w = [-1.0, 0.0]      # the rule "frost below 3.8 °C"
    b = 3.8
    z = w[0] * x[0] + w[1] * x[1] + b
    print(round(z, 2), predict(x, w, b))
    ```

    With `w = [-1.0, 0.0]` the humidity counts for nothing and
    z = 3.8 − x₁: above 0 exactly when the temperature is below 3.8 °C.

2. Run it.

    ```text
    $ python scripts/frost.py
    1.2 1
    ```

    z = −2.6 + 0 + 3.8 = 1.2, so `predict` says 1: frost. It came: −2.0 °C
    at 06:00 on 9 December 2025. `round(z, 2)` hides the float's last
    digits, 1.1999999999999997.

**Check:** `1.2 1`.

---

### 4. Every evening and the accuracy { #accuracy }

<!-- 0:30 · 10 min (Task: 5 min, skip if late) -->

The **accuracy** is the share of evenings on which `predict` says what happened.

1. At the top of `frost.py`, add the first line, `import weather`; at the
   end, these lines. Save, run.

    ```python
    rows = weather.evenings("data/raw/weather.csv")
    xs = []
    ys = []
    for row in rows:
        xs.append([row[1], row[2] / 100])
        ys.append(row[3])
    print(len(xs), xs[0], ys[0])
    ```

    ```text
    $ python scripts/frost.py
    1.2 1
    3646 [-4.5, 0.85] 1
    ```

    `xs` holds the inputs of every evening, `ys` what happened, in the same
    order: `xs[0]` and `ys[0]` are 1 January 2016.

2. Under `predict`, add a second function. `range(len(xs))` counts the
   positions 0, 1, …, 3645, one per evening.

    ```python
    def accuracy(xs, ys, w, b):
        right = 0
        for i in range(len(xs)):
            if predict(xs[i], w, b) == ys[i]:
                right = right + 1
        return right / len(xs)
    ```

3. At the end of the file, one line more. `f"{...:.3f}"` writes the number
   with three decimals. Save, run.

    ```python
    print(f"{accuracy(xs, ys, w, b):.3f}")
    ```

    ```text
    $ python scripts/frost.py
    1.2 1
    3646 [-4.5, 0.85] 1
    0.957
    ```

**Check:** 0.957: the rule "below 3.8 °C" is right on 95.7 % of the evenings, against 66.3 % for "never frost".

!!! question "Task: other numbers"
    Change `b` to 2.0, then 3.0 and 5.0, and run. Then try `w = [-1.0, 4.0]`
    with `b = 0.6`, which gives the humidity a weight. Which numbers do
    best? Put back `w = [-1.0, 0.0]` and `b = 3.8`.

??? success "Answer"
    ```text
    b = 2.0: 0.916    b = 3.0: 0.947    b = 5.0: 0.944
    w = [-1.0, 4.0], b = 0.6: 0.958
    ```

    3.8 is the best threshold; the weight on the humidity changes three
    evenings of 3646. Finding three numbers by trying gets slow: the next
    part lets the evenings choose them.

---

## Part 3 · Rosenblatt's rule { #part-3 }

<!-- 0:40 to 1:05 -->

A neuron can learn its numbers from examples: after each wrong evening, the rule of 1958 moves them a little towards the right answer.

---

### 5. Training years and test years { #split }

<!-- 0:40 · 5 min -->

The numbers are learned from 2016 to 2022 only; the evenings of 2023 to 2025 are kept back to score the result.

1. At the end of `frost.py`, four empty lists: the inputs and the labels of
   the training years, and of the test years.

    ```python
    train_xs = []
    train_ys = []
    test_xs = []
    test_ys = []
    ```

2. Under them, a loop that puts each evening into one pair of lists. Save,
   run.

    ```python
    for row in rows:
        year = int(row[0][0:4])
        x = [row[1], row[2] / 100]
        if year <= 2022:
            train_xs.append(x)
            train_ys.append(row[3])
        else:
            test_xs.append(x)
            test_ys.append(row[3])
    print(len(train_xs), len(test_xs))
    ```

    `row[0][0:4]` is the year of the date, as text; `int` turns `"2016"`
    into the number 2016.

    ```text
    $ python scripts/frost.py
    ...
    0.957
    2551 1095
    ```

**Check:** 2551 + 1095 = 3646.

---

### 6. One learning step { #step }

<!-- 0:45 · 10 min -->

**Rosenblatt's rule:** compute the error, `y − ŷ`, what happened minus what `predict` said: 0 when right, +1 or −1 when wrong. Add the error times each input to its weight, and the error to `b`.

1. At the end of `frost.py`, add these lines. They start from zero
   weights and take one step on the first training evening. Save, run.

    ```python
    w = [0.0, 0.0]
    b = 0.0
    x = train_xs[0]
    error = train_ys[0] - predict(x, w, b)
    w[0] = w[0] + error * x[0]
    w[1] = w[1] + error * x[1]
    b = b + error
    print(error, w, b, predict(x, w, b))
    ```

    ```text
    $ python scripts/frost.py
    ...
    2551 1095
    1 [-4.5, 0.85] 1.0 1
    ```

    With zero weights z = 0 and `predict` says 0; frost came, so the error
    is 1. The step adds the evening's inputs to `w` and 1 to `b`: now z =
    20.25 + 0.72 + 1 = 21.97 and `predict` says 1.

**Check:** `1 [-4.5, 0.85] 1.0 1`: one wrong evening, one step, and it is right.

---

### 7. The loop: five epochs { #loop }

<!-- 0:55 · 10 min -->

One pass over all training evenings is an **epoch**. The loop takes the step of section 6 on every evening, five times over, and prints the accuracy after each pass.

1. At the end of `frost.py`, add these lines. Save, run.

    ```python
    w = [0.0, 0.0]
    b = 0.0
    for epoch in range(5):
        for i in range(len(train_xs)):
            x = train_xs[i]
            error = train_ys[i] - predict(x, w, b)
            w[0] = w[0] + error * x[0]
            w[1] = w[1] + error * x[1]
            b = b + error
        print(epoch + 1, f"{accuracy(train_xs, train_ys, w, b):.3f}")
    print(round(w[0], 2), round(w[1], 2), b)
    ```

    ```text
    $ python scripts/frost.py
    ...
    1 [-4.5, 0.85] 1.0 1
    1 0.952
    2 0.333
    3 0.923
    4 0.886
    5 0.952
    -1.2 1.09 3.0
    ```

    `range(5)` counts 0 to 4, so `epoch + 1` prints 1 to 5. The rule never
    stops: frost and no-frost evenings overlap between 0 and 6 °C, so some
    evening is always wrong and moves the numbers. After the second pass
    every evening says "frost", 33.3 %.

**Check:** 0.952 after the first and the fifth pass, 0.333 after the second; `w` = −1.2 and 1.09, `b` = 3.0.

---

## Part 4 · A class of your own { #part-4 }

<!-- 1:05 to 1:40 -->

`w` and `b` belong together, and every function needs them. A **class** keeps the numbers inside an **object**, with the functions that use them.

---

### 8. A class and its numbers: `__init__` { #init }

<!-- 1:05 · 10 min -->

A **class** is a new type, like `list` or `str`. `Perceptron()` makes an **object** of it and runs its `__init__` once; `self` is that new object, and `self.w` keeps a value in it.

1. New file `scripts/perceptron.py`, a module with only the class. Type,
   save.

    ```python
    class Perceptron:
        def __init__(self):
            self.w = [0.0, 0.0]
            self.b = 0.0
    ```

2. New file `scripts/forecast.py`. `from perceptron import Perceptron`
   takes the class out of the module, as `import weather` took the module.
   Type, save, run.

    ```python
    from perceptron import Perceptron

    model = Perceptron()
    print(model.w, model.b)
    print(type(model))

    other = Perceptron()
    other.b = -5.0
    print(model.b, other.b)
    ```

    ```text
    $ python scripts/forecast.py
    [0.0, 0.0] 0.0
    <class 'perceptron.Perceptron'>
    0.0 -5.0
    ```

    `model.w` reads a value kept in the object. Two objects of one class
    keep their own numbers: changing `other.b` leaves `model.b` alone.

**Check:** `0.0 -5.0`: two objects, two biases.

---

### 9. The method `predict` { #method-predict }

<!-- 1:15 · 5 min -->

A **method** is a `def` inside the class. Python passes the object before the dot as `self`, so `model.predict(x)` takes the numbers of `model`.

1. In `perceptron.py`, under `__init__`, add the method; it is `predict`
   of section 3 with `self.w` and `self.b` in place of `w` and `b`. Save.

    ```python
        def predict(self, x):
            z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
            if z > 0:
                return 1
            return 0
    ```

    The `def` is indented by four spaces, as `def __init__` is: inside
    the class.

2. At the end of `forecast.py`, add these lines. Save, run.

    ```python
    model.w = [-1.0, 0.0]
    model.b = 3.8
    print(model.predict([2.6, 0.85]), other.predict([2.6, 0.85]))
    ```

    ```text
    $ python scripts/forecast.py
    [0.0, 0.0] 0.0
    <class 'perceptron.Perceptron'>
    0.0 -5.0
    1 0
    ```

**Check:** `1 0`: the same evening, one answer from each object's numbers.

---

### 10. The method `fit` { #method-fit }

<!-- 1:20 · 10 min -->

`fit` is the loop of section 7, inside the class: it changes `self.w` and `self.b`, the numbers of the object it is called on.

1. In `perceptron.py`, under `predict`, add the method. Save.

    ```python
        def fit(self, xs, ys, epochs):
            for epoch in range(epochs):
                for i in range(len(xs)):
                    x = xs[i]
                    error = ys[i] - self.predict(x)
                    self.w[0] = self.w[0] + error * x[0]
                    self.w[1] = self.w[1] + error * x[1]
                    self.b = self.b + error
    ```

2. Check it on four points whose answer is known: AND, 1 only for (1, 1).
   At the end of `forecast.py`, add these lines. Save, run.

    ```python
    gate = Perceptron()
    gate.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 0, 0, 1], 6)
    print(gate.w, gate.b)
    ```

    ```text
    $ python scripts/forecast.py
    ...
    1 0
    [2.0, 1.0] -2.0
    ```

    w = (2, 1) and b = −2: the numbers the lecture found by hand for AND,
    in six epochs.

**Check:** `[2.0, 1.0] -2.0`.

---

### 11. Train, then score on the unseen years { #train-test }

<!-- 1:30 · 10 min (Task: 5 min, skip if late) -->

A fourth method, `score`, is `accuracy` of section 4 inside the class. Then the class does the work of Part 3 in two calls, `fit` and `score`.

1. In `perceptron.py`, under `fit`, add the method. Save.

    ```python
        def score(self, xs, ys):
            right = 0
            for i in range(len(xs)):
                if self.predict(xs[i]) == ys[i]:
                    right = right + 1
            return right / len(xs)
    ```

2. Replace everything in `forecast.py` with these lines. Then, under
   them, copy from `frost.py` the lines of section 5, from `train_xs = []`
   to the last `test_ys.append(row[3])`, without the `print`.

    ```python
    import weather
    from perceptron import Perceptron

    rows = weather.evenings("data/raw/weather.csv")
    ```

3. At the end, the two calls and the result with its ±, the standard error
   of a share p of n evenings, √(p (1 − p) / n): `** 0.5` is the square
   root. `test_ys.count(0)` counts the evenings without frost. Save, run.

    ```python
    model = Perceptron()
    model.fit(train_xs, train_ys, 5)
    print(round(model.w[0], 2), round(model.w[1], 2), model.b)
    p = model.score(test_xs, test_ys)
    n = len(test_xs)
    print(f"right on {p:.3f} ± {(p * (1 - p) / n) ** 0.5:.3f} of {n} test evenings")
    print(f"never frost: {test_ys.count(0) / n:.3f}")
    ```

    ```text
    $ python scripts/forecast.py
    -1.2 1.09 3.0
    right on 0.955 ± 0.006 of 1095 test evenings
    never frost: 0.654
    ```

    The same numbers as the loop of section 7: the class is the same code.
    On three winters it has never seen, the neuron is right on 95.5 ± 0.6 %
    of the evenings; "never frost" on 65.4 %.

**Check:** `0.955 ± 0.006`, against 0.654.

!!! question "Task: how many epochs?"
    Fit new objects with 1, 2, 3 and 10 epochs and print `score` on the
    training and the test evenings for each. Which would you report?

??? success "Answer"
    At the end of `forecast.py`:

    ```python
    for epochs in [1, 2, 3, 10]:
        trial = Perceptron()
        trial.fit(train_xs, train_ys, epochs)
        print(epochs, f"{trial.score(train_xs, train_ys):.3f}",
              f"{trial.score(test_xs, test_ys):.3f}")
    ```

    ```text
    1 0.952 0.957
    2 0.333 0.346
    3 0.923 0.916
    10 0.949 0.952
    ```

    The rule jumps from pass to pass, so the number of epochs is a choice.
    It is made on the training years (0.952 after 1 and 5 epochs, 0.949
    after 10), never on the test years: a number chosen by the test score
    uses the test years up, and nothing unseen is left to score it.

---

## Part 5 · Your project { #part-5 }

<!-- 1:40 to 2:00 -->

The same two numbers for a yes-or-no question about your own data: the baseline, and a threshold on one column.

---

### 12. A baseline for a yes-or-no question { #project }

<!-- 1:40 · 15 min -->

Skip this section if your project has no data file yet. Otherwise choose a question your file answers with yes or no for each row, and one column that might tell in advance.

1. New file `scripts/baseline.py` in your project folder. Change the file
   name, the two column numbers and the yes-rule to yours. Save, run.

    ```python
    lines = open("data/raw/MY_FILE.csv").read().splitlines()[1:]
    values = []
    labels = []
    for line in lines:
        parts = line.split(",")
        values.append(float(parts[1]))     # the column that might tell
        if float(parts[2]) > 100:          # the yes-or-no question
            labels.append(1)
        else:
            labels.append(0)
    yes = sum(labels)
    print(len(labels), yes, max(yes, len(labels) - yes) / len(labels))
    ```

    The last number is the baseline: the share right by always giving the
    more common answer.

2. A threshold: at the end, try every value of the column as `c` and keep
   the best rule "yes when the value is below `c`". With more than about
   10 000 rows, write `for c in values[::100]:`, every 100th value.

    ```python
    best_c = values[0]
    best = 0
    for c in values:
        right = 0
        for i in range(len(values)):
            if (values[i] < c) == (labels[i] == 1):
                right = right + 1
        if right > best:
            best_c = c
            best = right
    print(best_c, best / len(values))
    ```

    `(values[i] < c) == (labels[i] == 1)` is `True` when the rule and the
    answer agree. If yes goes with large values, write `>` in place of `<`.

3. In your project's `README.md`, write the question, the baseline and the
   best threshold with its share, and which script gives them.

**Check:** two shares in the README: the baseline and the threshold rule, the second larger, or a sentence saying that the column does not tell.

---

### 13. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| the evenings of the log | `weather.evenings(path)`: `[date, temperature, humidity, frost]` |
| a neuron | `z = w[0] * x[0] + w[1] * x[1] + b`, 1 if `z > 0` |
| one step of Rosenblatt's rule | `error = y - predict(x, w, b)`, each `w[i]` plus `error * x[i]`, `b` plus `error` |
| a class | `class Perceptron:` with `def __init__(self):` and `self.w = ...` |
| a method | a `def` inside the class, first argument `self` |
| an object | `model = Perceptron()`, then `model.fit(xs, ys, 5)`, `model.score(xs, ys)` |
| take a class from a module | `from perceptron import Perceptron` |
| a share with its ± | `(p * (1 - p) / n) ** 0.5` |

---

## Optional, if the room goes fast { #optional }

---

### 14. A smooth output: the sigmoid in `fit` { #sigmoid }

<!-- — · 10 min -->

The lecture's logistic neuron: the step in the error becomes the **sigmoid** 1 / (1 + e^−z), a probability, and each change is multiplied by a small learning rate η. The rule then settles instead of jumping.

1. In `perceptron.py`, add `import math` as the first line, and a method
   under `score`. Save.

    ```python
        def fit_smooth(self, xs, ys, epochs, eta):
            for epoch in range(epochs):
                for i in range(len(xs)):
                    x = xs[i]
                    z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
                    error = ys[i] - 1 / (1 + math.exp(-z))
                    self.w[0] = self.w[0] + eta * error * x[0]
                    self.w[1] = self.w[1] + eta * error * x[1]
                    self.b = self.b + eta * error
    ```

    `math.exp(-z)` is e^−z.

2. At the end of `forecast.py`, add these lines. Save, run.

    ```python
    smooth = Perceptron()
    smooth.fit_smooth(train_xs, train_ys, 5, 0.01)
    print(round(smooth.w[0], 3), round(smooth.w[1], 3), round(smooth.b, 3))
    p = smooth.score(test_xs, test_ys)
    print(f"right on {p:.3f} ± {(p * (1 - p) / n) ** 0.5:.3f} of {n} test evenings")
    ```

    ```text
    $ python scripts/forecast.py
    ...
    never frost: 0.654
    -0.877 1.704 2.227
    right on 0.961 ± 0.006 of 1095 test evenings
    ```

**Check:** −0.877, 1.704 and 2.227, the numbers of the lecture's training, and 0.961 on the test years.

---

### 15. scikit-learn: the same two calls { #sklearn }

<!-- — · 15 min -->

**scikit-learn** is the Python library of machine learning. Its models are classes, with the methods `fit`, `predict` and `score`: today's class, written by others.

1. Install it into the environment, with its version, and write it down.

    ```text
    $ conda install scikit-learn=1.9
    ...
    Proceed ([y]/n)?
    $ python -c "import sklearn; print(sklearn.__version__)"
    1.9.1
    $ conda env export --from-history -f environment.yml
    ```

    At `Proceed ([y]/n)?` press `Enter`. Open `environment.yml`, delete
    its last line, `prefix: ...`, save: `- scikit-learn=1.9` is in the
    list.

2. New file `scripts/library.py`. Copy the lines of `forecast.py` from
   `rows = ...` to the end of the `for` loop, and put two lines above them.

    ```python
    from sklearn.linear_model import LogisticRegression, Perceptron

    import weather
    ```

3. At the end, the library's two models, each with `fit` and `score`.
   `coef_` and `intercept_` are the library's names for `w` and `b`.
   Save, run.

    ```python
    model = Perceptron()
    model.fit(train_xs, train_ys)
    print(model.coef_, model.intercept_, f"{model.score(test_xs, test_ys):.3f}")

    model = LogisticRegression()
    model.fit(train_xs, train_ys)
    print(model.coef_, model.intercept_, f"{model.score(test_xs, test_ys):.3f}")
    print(model.predict_proba([[2.6, 0.85]]))
    ```

    ```text
    $ python scripts/library.py
    [[-8.5  15.37]] [23.] 0.959
    [[-1.04818444 -0.01586714]] [4.16986212] 0.961
    [[0.19292805 0.80707195]]
    ```

    The library's `Perceptron` shuffles the evenings, stops by itself and
    scores 0.959. `LogisticRegression` is the logistic neuron, trained
    close to the lowest point of the loss: frost below about 4.0 °C, and
    for 8 December 2025 a probability of frost of 0.81, the second number.

**Check:** `1.9.1`, and 0.959 and 0.961 on the test years.

---

### 16. Draw the line { #draw }

<!-- — · 10 min -->

The test evenings as points, and the line where the smooth neuron's z is 0.

1. At the end of `forecast.py`, add these lines: the two lists of points
   first. Save, run.

    ```python
    frost_t = []
    frost_h = []
    other_t = []
    other_h = []
    for i in range(len(test_xs)):
        if test_ys[i] == 1:
            frost_t.append(test_xs[i][0])
            frost_h.append(test_xs[i][1])
        else:
            other_t.append(test_xs[i][0])
            other_h.append(test_xs[i][1])
    print(len(frost_t), len(other_t))
    ```

    ```text
    $ python scripts/forecast.py
    ...
    379 716
    ```

2. Then the figure. At humidity h the line is at the temperature
   −(b + w₂h) / w₁. Add, save, run, open `results/frost_line.png`.

    ```python
    import matplotlib.pyplot as plt

    w = smooth.w
    b = smooth.b
    fig, ax = plt.subplots()
    ax.plot(frost_t, frost_h, ".", label="frost")
    ax.plot(other_t, other_h, ".", label="no frost")
    ax.plot([-(b + w[1] * 0.4) / w[0], -(b + w[1] * 1.0) / w[0]], [0.4, 1.0],
            "k-", label="z = 0")
    ax.set_xlabel("temperature at 18:00 (°C)")
    ax.set_ylabel("humidity at 18:00 (fraction)")
    ax.legend()
    fig.savefig("results/frost_line.png", dpi=150)
    ```

**Check:** a nearly upright line near 4 °C, the frost points left of it, the others right, mixed near the line.

---

### 17. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder and open, with the answers folded. Add the lines at the end of `forecast.py`.

!!! question "Advanced task: missed frosts and false alarms"
    The smooth neuron's probability is `1 / (1 + math.exp(-z))`. Add a
    method `probability(self, x)` to the class, and count on the test
    years the frosts it misses and the false alarms it gives, first saying
    frost when the probability is above 0.5, then above 0.2.

??? success "Answer"
    In `perceptron.py`:

    ```python
        def probability(self, x):
            z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
            return 1 / (1 + math.exp(-z))
    ```

    In `forecast.py`:

    ```python
    for cut in [0.5, 0.2]:
        missed = 0
        alarms = 0
        for i in range(len(test_xs)):
            said = smooth.probability(test_xs[i]) > cut
            if test_ys[i] == 1 and not said:
                missed = missed + 1
            if test_ys[i] == 0 and said:
                alarms = alarms + 1
        print(cut, missed, alarms)
    ```

    ```text
    0.5 18 25
    0.2 5 68
    ```

    At 0.2 the missed frosts fall from 18 to 5 and the false alarms rise
    from 25 to 68. A gardener chooses 0.2; the cut is a choice of which
    error costs more, not part of the model.

!!! question "Advanced task: any number of inputs"
    `predict` and `fit` name `w[0]` and `w[1]`. Write a class `Neuron`
    whose `__init__(self, n)` makes `n` weights (`[0.0] * n` is a list of
    `n` zeros) and whose methods loop over the inputs. Check that
    `Neuron(2)` gives the numbers of `Perceptron`, then train `Neuron(1)` on
    the temperature alone.

??? success "Answer"
    ```python
    class Neuron:
        def __init__(self, n):
            self.w = [0.0] * n
            self.b = 0.0

        def predict(self, x):
            z = self.b
            for j in range(len(x)):
                z = z + self.w[j] * x[j]
            if z > 0:
                return 1
            return 0

        def fit(self, xs, ys, epochs):
            for epoch in range(epochs):
                for i in range(len(xs)):
                    x = xs[i]
                    error = ys[i] - self.predict(x)
                    for j in range(len(x)):
                        self.w[j] = self.w[j] + error * x[j]
                    self.b = self.b + error
    ```

    ```python
    two = Neuron(2)
    two.fit(train_xs, train_ys, 5)
    print(round(two.w[0], 2), round(two.w[1], 2), two.b)

    temp_xs = []
    for x in train_xs:
        temp_xs.append([x[0]])
    one = Neuron(1)
    one.fit(temp_xs, train_ys, 5)
    print(one.w, one.b)
    ```

    ```text
    -1.2 1.09 3.0
    [-0.49999999999999867] 8.0
    ```

    `Neuron(2)` repeats `Perceptron`. With the temperature alone the rule
    ends at z = 8 − 0.5 x₁, frost below 16 °C: right on 63 % of the
    training evenings, against 95 % with both inputs. Where Rosenblatt's
    rule stops depends on its inputs and their order, not only on the
    evenings.

---

## Aims practised

- 🔧 **Tool-agnostic:** a neuron, its learning rule and a class in plain
  Python, then the same two calls, `fit` and `predict`, in a library.
- ♻️ **Reproducibility:** the split is by years, written in the script, so
  every laptop learns from the same evenings and gets 0.955.
- ⚙️ **Automation:** five passes over 2551 evenings in a loop; one object
  that holds its numbers and does the work in two calls.
