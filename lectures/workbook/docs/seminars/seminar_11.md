# Seminar 11 · Perceptron

**Paired lecture:** 11 The Perceptron · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** Will it freeze tonight? Every student writes a neuron that predicts frost at
06:00 from the temperature and humidity at 18:00 the evening before,
trains it on 2016 to 2022, tests it on 2023 to 2025 (95.9 ± 0.6 % right),
compares it with a one-line rule, and writes the answer into the README.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (zsh on macOS, Git Bash on Windows; today's environment
`s11`). Nothing is installed beyond today's environment. In the blocks, a line that starts with `$` is
typed in the terminal, and every other line is what comes back.

**If time runs short:** leave out section 5 and the Task of Part 3;
sections 10 and 11 stay.

??? info "Before the session"
    - **Room:** VS Code and Miniforge on every laptop (Seminar 4, or the
      [Setup](../setup.md) page), and internet: today's folder and its
      packages download in section 1, about 180 MB the first time.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** nothing to prepare. Today's folder is the same for everyone,
      so every number on this page is the number in the room.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · Evenings and mornings { #part-1 }

<!-- 0:00 to 0:35 -->

Seminar 9 found P(frost at 06:00) = 0.984 when 18:00 was below 2 °C. Today a neuron learns that line from the data.

---

### 1. Get today's folder { #start }

<!-- 0:00 · 5 min -->

Today's folder holds the data, the scripts so far and `environment.yml`; nothing from an earlier seminar is needed.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases)
   of the course repository, under **Assets**, click `weather-s11.zip`.
2. Open VS Code, then **View** > **Terminal**. Unpack the zip into the
   home folder and go there. Git Bash shows `/c/Users/smilte/...`.

    ```text
    $ unzip ~/Downloads/weather-s11.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s11.zip
       creating: /Users/smilte/weather-s11/
    ...
      inflating: /Users/smilte/weather-s11/scripts/weather.py
    $ cd ~/weather-s11
    ```

    Safari unpacks a download by itself: then type
    `mv ~/Downloads/weather-s11 ~` instead of `unzip`.

3. **File** > **Open Folder...** > `weather-s11`. VS Code opens a new
   window; **View** > **Terminal** there starts in the folder.
4. Make today's environment from `environment.yml`: Python, NumPy,
   Matplotlib, SciPy and JupyterLab, in the versions the file names. conda
   keeps what it downloads, so the next seminar's environment is quicker.

    ```text
    $ conda env create -n s11 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s11
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. Switch it on. The prompt then starts with `(s11)`.

    ```text
    $ conda activate s11
    $ python -c "import numpy, matplotlib; print(numpy.__version__, matplotlib.__version__)"
    2.5.4 3.11.2
    ```

**Check:** `(s11)` in the prompt, and `2.5.4 3.11.2`.

---

### 2. One row per evening { #evenings }

<!-- 0:05 · 15 min -->

Each evening becomes one example: two **inputs**, the temperature and humidity at 18:00, and a **label**, 1 if 06:00 the next morning is below 0 °C, else 0.

1. New file `scripts/frost_rule.py`. Type and save.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=(1, 2))
    temp = data[:, 0].reshape(-1, 24)
    hum = data[:, 1].reshape(-1, 24)
    evening_t = temp[:-1, 18]      # 18:00 of each day
    evening_h = hum[:-1, 18]
    morning_t = temp[1:, 6]        # 06:00 of the next day
    ok = (evening_t != -999) & (morning_t != -999)
    X = np.column_stack([evening_t, evening_h])[ok]
    y = (morning_t[ok] < 0).astype(int)
    print("evenings", len(y), "frost mornings", y.sum())
    ```

2. Run it. With one row per day, `temp[:-1, 18]` is 18:00 of every day
   but the last, `temp[1:, 6]` 06:00 of every day but the first: each
   evening beside the next morning.

    ```text
    $ python scripts/frost_rule.py
    evenings 3646 frost mornings 1229
    ```

**Check:** 3646 evenings (3652 pairs, six touch the days of `-999`), 1229
with frost the next morning.

---

### 3. The two clouds { #clouds }

<!-- 0:20 · 10 min -->

Each evening is a point at (temperature, humidity); its colour is the morning.

1. Add at the end, save. `X[y == 1, 0]` is the temperature column of the
   evenings followed by frost.

    ```python

    fig, ax = plt.subplots()
    ax.plot(X[y == 0, 0], X[y == 0, 1], ".", ms=3, label="no frost")
    ax.plot(X[y == 1, 0], X[y == 1, 1], ".", ms=3, label="frost")
    ax.set_xlabel("temperature at 18:00 (°C)")
    ax.set_ylabel("humidity at 18:00 (%)")
    ax.legend()
    fig.savefig("results/frost_points.png", dpi=150)
    ```

2. Run it, then open `results/frost_points.png` from the Explorer.

    ```text
    $ python scripts/frost_rule.py
    evenings 3646 frost mornings 1229
    ```

**Check:** frost on the left, no frost on the right, the two touching near
4 °C at every humidity.

!!! question "Task: read the plot"
    1. What share of the mornings froze?
    2. Where would you draw a straight line between the clouds? Does
       humidity help?

??? success "Answer"
    1. 1229 / 3646 = 0.337.
    2. Nearly upright, at about 4 °C. The colours change from left to right,
       hardly from bottom to top: humidity adds little.

---

## Part 2 · A neuron and Rosenblatt's rule { #part-2 }

<!-- 0:35 to 1:00 -->

A **neuron** multiplies each input by a **weight**, adds them and a **bias** b, and says 1 when the sum w · x + b is above 0: a straight line in the plot.

---

### 4. A neuron with weights set by hand { #by-hand }

<!-- 0:35 · 10 min -->

w = (−1, 0), b = 2 says frost when −T + 2 > 0, that is when T < 2 °C; humidity gets weight 0.

1. Add at the end, save. `X @ w` multiplies each row of `X` with `w`
   pair by pair and adds: one sum per evening.

    ```python

    def predict(X, w, b):
        return (X @ w + b > 0).astype(int)

    w = np.array([-1.0, 0.0])
    b = 2.0
    print(f"frost if below 2 °C: {np.mean(predict(X, w, b) == y):.3f}")
    print(f"never frost: {np.mean(y == 0):.3f}")
    ```

2. Run it. `np.mean(... == y)` is the share of evenings it gets right.

    ```text
    $ python scripts/frost_rule.py
    evenings 3646 frost mornings 1229
    frost if below 2 °C: 0.916
    never frost: 0.663
    ```

**Check:** 91.6 % right; "never frost" is already 66.3 %, the number to
beat.

---

### 5. Rosenblatt's rule { #rule }

<!-- 0:45 · 10 min -->

The perceptron learns its weights: for each evening it predicts ŷ, and when ŷ is wrong it adds η (target − ŷ) x to w and η (target − ŷ) to b. η, the **learning rate**, sets the step size.

1. Add at the end, save. One pass over all evenings is an **epoch**; the
   loop counts the wrong answers, the updates, in each.

    ```python

    w, b, eta = np.zeros(2), 0.0, 1.0
    for epoch in range(1, 11):
        updates = 0
        for x, target in zip(X, y):
            y_hat = int(w @ x + b > 0)
            w = w + eta * (target - y_hat) * x
            b = b + eta * (target - y_hat)
            updates += int(y_hat != target)
        print("epoch", epoch, "updates", updates)
    print("w", w, "b", b)
    print(f"correct: {np.mean(predict(X, w, b) == y):.3f}")
    ```

2. Run it. The new lines:

    ```text
    $ python scripts/frost_rule.py
    ...
    epoch 1 updates 235
    epoch 2 updates 231
    epoch 3 updates 231
    epoch 4 updates 231
    epoch 5 updates 231
    epoch 6 updates 231
    epoch 7 updates 232
    epoch 8 updates 233
    epoch 9 updates 232
    epoch 10 updates 231
    w [-40.5   9. ] b -10.0
    correct: 0.671
    ```

**Check:** the updates never reach 0. The rule stops only when one line
separates the two clouds without error; these clouds overlap, so the last w
is wherever it stopped: 67.1 %.

!!! question "Task: the best threshold"
    Try the rule "frost if below c °C" for c = 0.0, 0.1, … 5.9 on all
    evenings. Which c is best, and how often is it right?

??? success "Answer"
    Add at the end of `frost_rule.py`:

    ```python

    cs = np.arange(0, 6, 0.1)
    accs = [np.mean((X[:, 0] < c) == y) for c in cs]
    k = np.argmax(accs)
    print(f"best: below {cs[k]:.1f} °C, {accs[k]:.3f} correct")
    ```

    ```text
    best: below 3.8 °C, 0.957 correct
    ```

    The threshold was chosen on the same evenings it is judged on.
    Section 10 does it fairly.

---

## Part 3 · The logistic neuron { #part-3 }

<!-- 1:00 to 1:40 -->

The step becomes a smooth **sigmoid**, 1/(1 + e^−z), which gives a probability between 0 and 1; the count of errors becomes a **loss**; the rule becomes **gradient descent**, small steps downhill on the loss.

---

### 6. Train years and test years { #split }

<!-- 1:00 · 5 min -->

A model is judged on data it has not seen: it learns from 2016 to 2022, and 2023 to 2025 judge it.

1. New file `scripts/frost_neuron.py`; copy from `frost_rule.py`. Save.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    data = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=(1, 2))
    temp = data[:, 0].reshape(-1, 24)
    hum = data[:, 1].reshape(-1, 24)
    evening_t = temp[:-1, 18]      # 18:00 of each day
    evening_h = hum[:-1, 18]
    morning_t = temp[1:, 6]        # 06:00 of the next day
    ok = (evening_t != -999) & (morning_t != -999)
    X = np.column_stack([evening_t, evening_h])[ok]
    y = (morning_t[ok] < 0).astype(int)
    ```

2. Only the `time` line is new above. Add the split at the end, save.
   `time[::24]` is every 24th time: one per day, the year of each evening.

    ```python

    year = np.array([int(t[:4]) for t in time[::24]])[:-1][ok]
    train = year <= 2022
    test = year >= 2023
    print("train", train.sum(), "test", test.sum())
    ```

3. Run it.

    ```text
    $ python scripts/frost_neuron.py
    train 2551 test 1095
    ```

**Check:** 2551 + 1095 = 3646.

---

### 7. Standardise the inputs { #standardise }

<!-- 1:05 · 5 min -->

Temperature and humidity have different units and ranges. **Standardising** turns each into mean 0, standard deviation 1, so that one learning rate suits both; m and s come from the training years only.

1. Add at the end, save. `axis=0` takes the mean of each column.

    ```python

    m = X[train].mean(axis=0)
    s = X[train].std(axis=0)
    Z = (X - m) / s
    print("m", m.round(2), "s", s.round(2))
    ```

2. Run it. The last line:

    ```text
    $ python scripts/frost_neuron.py
    ...
    m [ 9.6  72.97] s [9.04 8.53]
    ```

**Check:** 9.6 °C and 72.97 %, spread 9.04 °C and 8.53 %.

---

### 8. The training loop { #loop }

<!-- 1:10 · 15 min -->

Each epoch: ŷ for every training evening, the **log loss** (small when ŷ is near the label), then one step of w and b against the loss's slope, which for this loss is Zᵀ(ŷ − y)/N.

1. Add at the end, save. Every 250 epochs it prints the epoch, the loss
   and the share correct.

    ```python

    Zt, yt = Z[train], y[train]
    w, b, eta = np.zeros(2), 0.0, 0.5
    for epoch in range(1001):
        y_hat = 1 / (1 + np.exp(-(Zt @ w + b)))
        loss = -np.mean(yt * np.log(y_hat) + (1 - yt) * np.log(1 - y_hat))
        if epoch % 250 == 0:
            print(epoch, round(loss, 4), round(np.mean((y_hat > 0.5) == yt), 3))
        w = w - eta * Zt.T @ (y_hat - yt) / len(yt)
        b = b - eta * np.mean(y_hat - yt)
    print("w", w.round(3), "b", round(b, 3))
    ```

2. Run it. The new lines: epoch, loss, share correct.

    ```text
    $ python scripts/frost_neuron.py
    ...
    0 0.6931 0.667
    250 0.1379 0.951
    500 0.1226 0.955
    750 0.1167 0.954
    1000 0.1137 0.955
    w [-6.862  0.035] b -4.188
    ```

**Check:** the loss starts at ln 2 = 0.6931 (every ŷ is 0.5) and falls;
the temperature weight is about 200 times the humidity weight.

---

### 9. Back to °C and % { #units }

<!-- 1:25 · 10 min -->

The weights belong to the standardised inputs. With z = (x − m)/s, the weight per °C or per % is w/s, and b loses Σ w m/s.

1. Add at the end, save. The boundary is where w · x + b = 0; at 75 %
   humidity it is solved for the temperature.

    ```python

    wx = w / s
    bx = b - np.sum(w * m / s)
    print("per °C and per %:", wx.round(3), "b", round(bx, 2))
    print(f"boundary at 75 %: {-(bx + wx[1] * 75) / wx[0]:.2f} °C")
    ```

2. Run it. The last two lines:

    ```text
    $ python scripts/frost_neuron.py
    ...
    per °C and per %: [-0.759  0.004] b 2.8
    boundary at 75 %: 4.10 °C
    ```

**Check:** the boundary is the line −0.759 T + 0.004 H + 2.8 = 0: at 75 %
humidity, 4.10 °C. 10 % more humidity moves it by 0.05 °C.

!!! question "Task: the learning rate"
    Train with `eta = 2.0`, then with `eta = 0.05`. What is the loss at
    epoch 1000, and the weight of humidity in °C and %? Set it back to 0.5.

??? success "Answer"
    `eta = 2.0`:

    ```text
    1000 0.1082 0.954
    w [-8.962e+00  1.000e-03] b -5.568
    per °C and per %: [-0.991  0.   ] b 3.94
    ```

    `eta = 0.05`:

    ```text
    1000 0.1712 0.943
    w [-3.171  0.322] b -1.839
    per °C and per %: [-0.351  0.038] b -1.23
    ```

    A larger step gets closer to the minimum in 1000 epochs, and the
    humidity weight goes to 0. With 0.05 the loop has not arrived.

---

## Part 4 · The answer { #part-4 }

<!-- 1:40 to 2:00 -->

The test years, seen for the first time.

---

### 10. The test years, against the rule { #test }

<!-- 1:40 · 10 min -->

An accuracy is a share of N evenings, so it has a ± like any count: √(p(1 − p)/N). The rule's threshold is chosen on the training years, for a fair match.

1. Add at the end, save. `Z[test]` uses the m and s of the training
   years.

    ```python

    p = 1 / (1 + np.exp(-(Z[test] @ w + b)))
    acc = np.mean((p > 0.5) == y[test])
    n = test.sum()
    print(f"neuron on 2023-2025: {acc:.3f} ± {np.sqrt(acc * (1 - acc) / n):.3f}")

    cs = np.arange(0, 6, 0.1)
    accs = [np.mean((X[train, 0] < c) == y[train]) for c in cs]
    c = cs[np.argmax(accs)]
    rule = np.mean((X[test, 0] < c) == y[test])
    print(f"rule 'below {c:.1f} °C' on 2023-2025: {rule:.3f}")
    ```

2. Run it. The last two lines:

    ```text
    $ python scripts/frost_neuron.py
    ...
    neuron on 2023-2025: 0.959 ± 0.006
    rule 'below 3.6 °C' on 2023-2025: 0.959
    ```

**Check:** 95.9 % for both. The neuron learned the rule, and humidity
adds nothing these data can show.

---

### 11. Write the answer into the README { #commit }

<!-- 1:50 · 5 min -->

The answer, with the script that gives it.

1. At the end of `README.md`, add and save:

    ```text

    ## Frost tomorrow morning

    A neuron trained on the evenings of 2016 to 2022 (`scripts/frost_neuron.py`)
    predicts frost at 06:00 from the temperature and humidity at 18:00. On the
    evenings of 2023 to 2025 it is right 95.9 ± 0.6 % of the time, the same as
    the rule "frost if 18:00 is below 3.6 °C". Humidity gets a weight near zero.
    ```

2. Run the script once more: the paragraph's numbers are its last lines.

    ```text
    $ python scripts/frost_neuron.py
    ...
    per °C and per %: [-0.759  0.004] b 2.8
    boundary at 75 %: 4.10 °C
    neuron on 2023-2025: 0.959 ± 0.006
    rule 'below 3.6 °C' on 2023-2025: 0.959
    ```

**Check:** the README ends with **Frost tomorrow morning**.

!!! question "Task: tonight"
    The sigmoid gives a probability. At 85 % humidity, what is P(frost at
    06:00) for an evening at 1 °C, 3 °C and 5 °C?

??? success "Answer"
    Add at the end of `frost_neuron.py`:

    ```python

    for t in [1.0, 3.0, 5.0]:
        z = np.array([t, 85.0]) @ wx + bx
        print(f"{t} °C, 85 %: P(frost) = {1 / (1 + np.exp(-z)):.2f}")
    ```

    ```text
    1.0 °C, 85 %: P(frost) = 0.92
    3.0 °C, 85 %: P(frost) = 0.71
    5.0 °C, 85 %: P(frost) = 0.34
    ```

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, for the next time they are needed.

| To | Type |
|--|--|
| one row per day | `temp.reshape(-1, 24)` |
| a neuron | `(X @ w + b > 0).astype(int)` |
| Rosenblatt's rule | `w = w + eta * (target - y_hat) * x` |
| standardise | `Z = (X - m) / s`, m and s from the training rows |
| one step of gradient descent | `w = w - eta * Zt.T @ (y_hat - yt) / len(yt)` |
| an accuracy with its ± | `np.sqrt(acc * (1 - acc) / n)` |

Seminar 12 reads a second station's file with pandas.

---

## Optional, if the room goes fast { #optional }

---

### 13. Draw the boundary { #boundary }

<!-- — · 5 min -->

The line where w · x + b = 0, over the two clouds.

1. Add at the end of `frost_neuron.py`, save. At humidity h the boundary
   temperature is −(b + w_H h)/w_T.

    ```python

    h = np.array([40, 100])
    fig, ax = plt.subplots()
    ax.plot(X[y == 0, 0], X[y == 0, 1], ".", ms=3, label="no frost")
    ax.plot(X[y == 1, 0], X[y == 1, 1], ".", ms=3, label="frost")
    ax.plot(-(bx + wx[1] * h) / wx[0], h, "k-", label="neuron")
    ax.set_xlabel("temperature at 18:00 (°C)")
    ax.set_ylabel("humidity at 18:00 (%)")
    ax.legend()
    fig.savefig("results/frost_boundary.png", dpi=150)
    ```

2. Run it with `python scripts/frost_neuron.py`, then open
   `results/frost_boundary.png`.

**Check:** a nearly upright line at about 4 °C, between the clouds.

---

### 14. Without standardising { #raw }

<!-- — · 5 min -->

What happens when the inputs keep their units.

1. Change the line `Z = (X - m) / s` to `Z = X`, save, run. Among the
   lines (the path shortened):

    ```text
    $ python scripts/frost_neuron.py
    …frost_neuron.py:31: RuntimeWarning: divide by zero encountered in log
    …frost_neuron.py:30: RuntimeWarning: overflow encountered in exp
    0 0.6931 0.667
    250 nan 0.956
    500 nan 0.956
    ```

2. Change it back to `Z = (X - m) / s`.

**Check:** the loss is `nan`. With inputs of tens of units, w · x + b
grows to hundreds, `np.exp` overflows, ŷ becomes exactly 0 or 1, and
log 0 is −∞.

---

### 15. Temperature alone { #one-input }

<!-- — · 5 min -->

Is humidity worth its column?

1. In `frost_neuron.py`, change two lines and delete the line that prints
   `boundary at 75 %`, save.

    ```python
    X = np.column_stack([evening_t])[ok]
    w, b, eta = np.zeros(1), 0.0, 0.5
    ```

2. Run it. The line of the test:

    ```text
    $ python scripts/frost_neuron.py
    ...
    neuron on 2023-2025: 0.957 ± 0.006
    ```

3. Undo the changes: `Ctrl+Z` (macOS `Cmd+Z`) in the editor, save.

**Check:** 0.957 against 0.959: two evenings of 1095, far inside ± 0.006.

---

### 16. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder and open, with the solutions folded.

!!! question "Advanced task: missed frosts against false alarms"
    95.9 % right hides two kinds of error: a frost that was not predicted
    (a gardener loses the plants) and a predicted frost that did not come
    (a false alarm). Count both on the test years for the threshold
    `p > 0.5`, then for `p > 0.3`. Which would a gardener choose?

??? success "Answer"
    Add at the end of `frost_neuron.py`:

    ```python

    for thr in [0.5, 0.3]:
        pred = p > thr
        frost = y[test] == 1
        print(f"threshold {thr}: caught {(pred & frost).sum()}, "
              f"missed {(~pred & frost).sum()}, "
              f"false alarms {(pred & ~frost).sum()}")
    ```

    ```text
    threshold 0.5: caught 361, missed 18, false alarms 27
    threshold 0.3: caught 371, missed 8, false alarms 59
    ```

    At 0.3 the missed frosts fall from 18 to 8, and the false alarms rise
    from 27 to 59; the share right drops to 93.9 %. A gardener takes 0.3:
    the threshold is a choice about which error costs more, not part of
    the model.

!!! question "Advanced task: a third input, the wind"
    A calm evening cools faster. Add the wind at 18:00 (column 3 of
    `weather.csv`) as a third input, train and test again. Does it help?

??? success "Answer"
    In `frost_neuron.py`, read three columns, add `wind`, give `X` a third
    column and `w` three zeros. Delete the lines of the Task "tonight"
    first, if you kept them: they multiply two numbers with three weights.

    ```python
    data = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=(1, 2, 3))
    temp = data[:, 0].reshape(-1, 24)
    hum = data[:, 1].reshape(-1, 24)
    wind = data[:, 2].reshape(-1, 24)
    ```

    ```python
    X = np.column_stack([evening_t, evening_h, wind[:-1, 18]])[ok]
    ```

    ```python
    w, b, eta = np.zeros(3), 0.0, 0.5
    ```

    ```text
    $ python scripts/frost_neuron.py
    train 2551 test 1095
    m [ 9.6  72.97  4.05] s [9.04 8.53 1.88]
    ...
    w [-6.841  0.045  0.069] b -4.19
    ...
    neuron on 2023-2025: 0.958 ± 0.006
    ```

    0.958 against 0.959: no gain. The wind's weight, 0.069, is a hundred
    times smaller than the temperature's. On these data the temperature
    at 18:00 carries the answer.

!!! question "Advanced task: a later evening"
    Would 21:00 or 23:00 predict the 06:00 frost better than 18:00? For
    the hours 12, 15, 18, 21 and 23, choose the best threshold "below c °C"
    on the training years and score it on the test years.

??? success "Answer"
    A new script, `scripts/frost_hour.py`:

    ```python
    import numpy as np

    time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=0, dtype=str)
    temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                      skiprows=1, usecols=1).reshape(-1, 24)
    morning_t = temp[1:, 6]
    year = np.array([int(t[:4]) for t in time[::24]])[:-1]
    cs = np.arange(0, 6, 0.1)
    for h in [12, 15, 18, 21, 23]:
        ev = temp[:-1, h]
        ok = (ev != -999) & (morning_t != -999)
        frost = morning_t < 0
        tr = ok & (year <= 2022)
        te = ok & (year >= 2023)
        accs = [np.mean((ev[tr] < c) == frost[tr]) for c in cs]
        c = cs[np.argmax(accs)]
        acc = np.mean((ev[te] < c) == frost[te])
        print(f"{h}:00  below {c:.1f} °C  {acc:.3f}")
    ```

    ```text
    $ python scripts/frost_hour.py
    12:00  below 4.5 °C  0.946
    15:00  below 4.8 °C  0.953
    18:00  below 3.6 °C  0.959
    21:00  below 2.2 °C  0.961
    23:00  below 0.5 °C  0.972
    ```

    The later the evening, the better the forecast and the lower the
    threshold: at 23:00 the night has done most of its cooling. A forecast
    is a trade between how early it comes and how right it is.

---

## Aims practised

- ♻️ **Reproducibility:** the split is by years, written in the script, so
  every laptop trains on the same evenings and gets 0.959.
- 🔧 **Tool-agnostic:** a neuron in a dozen lines of NumPy, no machine
  learning library.
- 📁 **Files:** the inputs and the label are read from `weather.csv` itself;
  no file is made by hand.
