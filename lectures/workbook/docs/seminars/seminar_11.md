# Seminar 11 — Will It Freeze Tonight? A Perceptron on the Weather Data

**Paired lecture:** 11 The Perceptron · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student writes a neuron that predicts frost at
06:00 from the temperature and humidity at 18:00 the evening before,
trains it on 2016 to 2022, tests it on 2023 to 2025 (95.9 ± 0.6 % right),
compares it with a one-line rule, commits and pushes.

Everything is typed in VS Code: the scripts in the editor, the runs in its
terminal (PowerShell 7, `weather` environment). Nothing is installed today.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · Evenings and mornings** · 35 min | | |
| 0:00 | [1. Open the project](#start) | `conda activate weather`, `git pull` | `(weather)` in the prompt |
| 0:05 | [2. One row per evening](#evenings) | `scripts/frost_rule.py`, `reshape(-1, 24)` | 3646 evenings, 1229 frosts |
| 0:20 | [3. The two clouds](#clouds) | `ax.plot(X[y == 1, 0], …)` | `results/frost_points.png` |
| | **Part 2 · A neuron and Rosenblatt's rule** · 25 min | | |
| 0:35 | [4. A neuron with weights set by hand](#by-hand) | `predict(X, w, b)` | 0.916 against 0.663 |
| 0:45 | [5. Rosenblatt's rule](#rule) | the rule, ten epochs | 231 updates in every epoch |
| | **Part 3 · The logistic neuron** · 40 min | | |
| 1:00 | [6. Train years and test years](#split) | `scripts/frost_neuron.py`, `year <= 2022` | 2551 and 1095 evenings |
| 1:05 | [7. Standardise the inputs](#standardise) | `Z = (X - m) / s` | m and s of the training years |
| 1:10 | [8. The training loop](#loop) | sigmoid, loss, gradient | loss 0.6931 down to 0.1137 |
| 1:25 | [9. Back to °C and %](#units) | `wx = w / s` | the boundary at 4.10 °C |
| | **Part 4 · The answer** · 20 min | | |
| 1:40 | [10. The test years, against the rule](#test) | `p > 0.5` on `Z[test]` | 0.959 ± 0.006 for both |
| 1:50 | [11. The README, a commit, a push](#commit) | `git commit`, `git push` | the neuron on GitHub |
| 1:55 | [12. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [13. Draw the boundary](#boundary) | `ax.plot(-(bx + wx[1] * h) / wx[0], h)` | the line over the clouds |
| — | [14. Without standardising](#raw) | `Z = X` | `nan` |
| — | [15. Temperature alone](#one-input) | one column in `X` | 0.957 |

**If time runs short:** leave out section 5 and the Task of Part 3;
sections 10 and 11 stay.

??? info "Before the session"
    - **Room:** `weather-project` and the `weather` environment (NumPy,
      Matplotlib, SciPy) of Seminars 7 to 10.
    - **You:** nothing to prepare. The data are the same in every clone, so
      every number on this page is the number in the room. Commit ids differ.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · Evenings and mornings { #part-1 }

**0:00 to 0:35** · Seminar 9 found P(frost at 06:00) = 0.984 when 18:00 was below 2 °C. Today a neuron learns that line.

---

### 1. Open the project { #start }

**0:00 · 5 min** · The same repository, the same environment.

1. Open `weather-project` in VS Code, then the terminal. Switch on the
   environment.

    ```text
    conda activate weather
    ```

2. Bring in any commit from GitHub.

    ```text
    git pull
    ```

    ```text
    Already up to date.
    ```

**Check:** `(weather)` in the prompt.

---

### 2. One row per evening { #evenings }

**0:05 · 15 min** · Inputs: temperature and humidity at 18:00. Label: 1 if 06:00 next morning is below 0 °C.

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

    `temp[:-1, 18]` is column 18 of every day but the last; `temp[1:, 6]`
    is column 6 of every day but the first: each evening beside the next
    morning.

2. Run it.

    ```text
    python scripts/frost_rule.py
    ```

    ```text
    evenings 3646 frost mornings 1229
    ```

**Check:** 3646 evenings (3652 pairs, six touch the days of `-999`), 1229
with frost the next morning.

---

### 3. The two clouds { #clouds }

**0:20 · 10 min** · Each evening is a point; its colour is the morning.

1. Add at the end, save, run.

    ```python

    fig, ax = plt.subplots()
    ax.plot(X[y == 0, 0], X[y == 0, 1], ".", ms=3, label="no frost")
    ax.plot(X[y == 1, 0], X[y == 1, 1], ".", ms=3, label="frost")
    ax.set_xlabel("temperature at 18:00 (°C)")
    ax.set_ylabel("humidity at 18:00 (%)")
    ax.legend()
    fig.savefig("results/frost_points.png", dpi=150)
    ```

    ```text
    python scripts/frost_rule.py
    ```

2. Open `results/frost_points.png` from the Explorer.

**Check:** frost on the left, no frost on the right, the two touching near
4 °C at every humidity.

!!! question "Task: read the plot"
    1. What share of the mornings froze?
    2. Where would you draw a straight line between the clouds? Does
       humidity help?

??? note "Answer"
    1. 1229 / 3646 = 0.337.
    2. Nearly upright, at about 4 °C. The colours change from left to right,
       hardly from bottom to top: humidity adds little.

---

## Part 2 · A neuron and Rosenblatt's rule { #part-2 }

**0:35 to 1:00** · A neuron says 1 when w · x + b > 0: a line in the plot.

---

### 4. A neuron with weights set by hand { #by-hand }

**0:35 · 10 min** · w = (−1, 0), b = 2 says frost when −T + 2 > 0, that is when T < 2 °C.

1. Add at the end, save.

    ```python

    def predict(X, w, b):
        return (X @ w + b > 0).astype(int)

    w = np.array([-1.0, 0.0])
    b = 2.0
    print(f"frost if below 2 °C: {np.mean(predict(X, w, b) == y):.3f}")
    print(f"never frost: {np.mean(y == 0):.3f}")
    ```

2. Run it.

    ```text
    python scripts/frost_rule.py
    ```

    ```text
    evenings 3646 frost mornings 1229
    frost if below 2 °C: 0.916
    never frost: 0.663
    ```

**Check:** 91.6 % right; "never frost" is already 66.3 %, the number to
beat.

---

### 5. Rosenblatt's rule { #rule }

**0:45 · 10 min** · The rule of the lecture: after each wrong answer, add η (target − ŷ) x to w.

1. Add at the end, save.

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

2. Run it.

    ```text
    python scripts/frost_rule.py
    ```

    The new lines:

    ```text
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

**Check:** the updates never reach 0. The clouds overlap, so no line
separates them, and the convergence theorem does not apply. The last w is
wherever the rule stopped: 67.1 %.

!!! question "Task: the best threshold"
    Try the rule "frost if below c °C" for c = 0.0, 0.1, … 5.9 on all
    evenings. Which c is best, and how often is it right?

??? note "Answer"
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

**1:00 to 1:40** · The step becomes a sigmoid, the error a loss, the rule gradient descent.

---

### 6. Train years and test years { #split }

**1:00 · 5 min** · The neuron learns from 2016 to 2022; 2023 to 2025 judge it.

1. New file `scripts/frost_neuron.py`. Copy lines 1 to 13 of
   `frost_rule.py` and add the `time` line and the split. Save.

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

    year = np.array([int(t[:4]) for t in time[::24]])[:-1][ok]
    train = year <= 2022
    test = year >= 2023
    print("train", train.sum(), "test", test.sum())
    ```

    `time[::24]` is every 24th time: one per day.

2. Run it.

    ```text
    python scripts/frost_neuron.py
    ```

    ```text
    train 2551 test 1095
    ```

**Check:** 2551 + 1095 = 3646.

---

### 7. Standardise the inputs { #standardise }

**1:05 · 5 min** · Temperature and humidity have different units and ranges; each becomes mean 0, standard deviation 1. m and s come from the training years only.

1. Add at the end, save, run.

    ```python

    m = X[train].mean(axis=0)
    s = X[train].std(axis=0)
    Z = (X - m) / s
    print("m", m.round(2), "s", s.round(2))
    ```

    ```text
    python scripts/frost_neuron.py
    ```

    The last line:

    ```text
    m [ 9.6  72.97] s [9.04 8.53]
    ```

**Check:** 9.6 °C and 72.97 %, spread 9.04 °C and 8.53 %.

---

### 8. The training loop { #loop }

**1:10 · 15 min** · The four lines of the lecture's loop: ŷ, the loss, w, b.

1. Add at the end, save.

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

2. Run it.

    ```text
    python scripts/frost_neuron.py
    ```

    The new lines: epoch, loss, share correct.

    ```text
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

**1:25 · 10 min** · With z = (x − m)/s: w in data units is w/s, and b loses Σ w m/s.

1. Add at the end, save, run.

    ```python

    wx = w / s
    bx = b - np.sum(w * m / s)
    print("per °C and per %:", wx.round(3), "b", round(bx, 2))
    print(f"boundary at 75 %: {-(bx + wx[1] * 75) / wx[0]:.2f} °C")
    ```

    ```text
    python scripts/frost_neuron.py
    ```

    The last two lines:

    ```text
    per °C and per %: [-0.759  0.004] b 2.8
    boundary at 75 %: 4.10 °C
    ```

**Check:** the boundary is the line −0.759 T + 0.004 H + 2.8 = 0: at 75 %
humidity, 4.10 °C. 10 % more humidity moves it by 0.05 °C.

!!! question "Task: the learning rate"
    Train with `eta = 2.0`, then with `eta = 0.05`. What is the loss at
    epoch 1000, and the weight of humidity in °C and %? Set it back to 0.5.

??? note "Answer"
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

**1:40 to 2:00** · The test years, seen for the first time.

---

### 10. The test years, against the rule { #test }

**1:40 · 10 min** · An accuracy is a count: ± √(p(1 − p)/N), as in the lecture. The rule's threshold is chosen on the training years.

1. Add at the end, save.

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

    `Z[test]` uses the m and s of the training years.

2. Run it.

    ```text
    python scripts/frost_neuron.py
    ```

    The last two lines:

    ```text
    neuron on 2023-2025: 0.959 ± 0.006
    rule 'below 3.6 °C' on 2023-2025: 0.959
    ```

**Check:** 95.9 % for both. The neuron learned the rule, and humidity
adds nothing these data can show.

---

### 11. The README, a commit, a push { #commit }

**1:50 · 5 min** · The answer, with the script that gives it.

1. At the end of `README.md`, add and save:

    ```text

    ## Frost tomorrow morning

    A neuron trained on the evenings of 2016 to 2022 (`scripts/frost_neuron.py`)
    predicts frost at 06:00 from the temperature and humidity at 18:00. On the
    evenings of 2023 to 2025 it is right 95.9 ± 0.6 % of the time, the same as
    the rule "frost if 18:00 is below 3.6 °C". Humidity gets a weight near zero.
    ```

2. Stage, commit, push.

    ```text
    git add README.md scripts
    ```

    ```text
    git commit -m "Predict frost at 06:00 with a neuron"
    ```

    ```text
    [main e7d4f68] Predict frost at 06:00 with a neuron
     3 files changed, 101 insertions(+)
     create mode 100644 scripts/frost_neuron.py
     create mode 100644 scripts/frost_rule.py
    ```

    ```text
    git push
    ```

    ```text
    To https://github.com/your-username/weather-project.git
       f6ce821..e7d4f68  main -> main
    ```

    Your ids differ, and so do the counts if you kept the Task lines.

**Check:** on GitHub, the README shows **Frost tomorrow morning**.

!!! question "Task: tonight"
    The sigmoid gives a probability. At 85 % humidity, what is P(frost at
    06:00) for an evening at 1 °C, 3 °C and 5 °C?

??? note "Answer"
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

**1:55 · 5 min**

| To | Type |
|--|--|
| one row per day | `temp.reshape(-1, 24)` |
| a neuron | `(X @ w + b > 0).astype(int)` |
| Rosenblatt's rule | `w = w + eta * (target - y_hat) * x` |
| standardise | `Z = (X - m) / s`, m and s from the training rows |
| one step of gradient descent | `w = w - eta * Zt.T @ (y_hat - yt) / len(yt)` |
| an accuracy with its ± | `np.sqrt(acc * (1 - acc) / n)` |

Seminar 12 starts from this repository.

---

## Optional, if the room is fast { #optional }

---

### 13. Draw the boundary { #boundary }

**— · 5 min** · The line where w · x + b = 0, over the two clouds.

1. Add at the end of `frost_neuron.py`, save, run.

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

    ```text
    python scripts/frost_neuron.py
    ```

2. Open `results/frost_boundary.png`.

**Check:** a nearly upright line at about 4 °C, between the clouds.

---

### 14. Without standardising { #raw }

**— · 5 min** · The lecture's warning, on these data.

1. Change the line `Z = (X - m) / s` to `Z = X`, save, run.

    ```text
    python scripts/frost_neuron.py
    ```

    Among the lines (the path shortened):

    ```text
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

**— · 5 min** · Is humidity worth its column?

1. In `frost_neuron.py`, change two lines, save, run.

    ```python
    X = np.column_stack([evening_t])[ok]
    ```

    ```python
    w, b, eta = np.zeros(1), 0.0, 0.5
    ```

    Delete the line that prints `boundary at 75 %`.

    ```text
    python scripts/frost_neuron.py
    ```

    The line of the test:

    ```text
    neuron on 2023-2025: 0.957 ± 0.006
    ```

2. Undo the changes: `Ctrl+Z` (macOS `Cmd+Z`) in the editor, save.

**Check:** 0.957 against 0.959: two evenings of 1095, far inside ± 0.006.

---

## Aims practised

- ♻️ **Reproducibility:** the split is by years, written in the script, so
  every laptop trains on the same evenings and gets 0.959.
- 🔧 **Tool-agnostic:** a neuron in a dozen lines of NumPy, no machine
  learning library.
- 📁 **Files:** the inputs and the label are read from `weather.csv` itself;
  no file is made by hand.
