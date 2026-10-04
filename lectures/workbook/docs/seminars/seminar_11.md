# Seminar 11 — A Perceptron from an Empty File

**Paired lecture:** 11 The Perceptron · **Format:** follow-along · **~120 min**
in class

The seminar has four parts, in this order.

1. **A neuron by hand.** The room reads a file of 300 labelled points, plots
   it, and writes the neuron as a function with weights read off the plot.
2. **Rosenblatt's rule.** The rule is written and checked on the AND gate
   against the table of the lecture, then run on the file.
3. **The logistic neuron.** Sigmoid, loss, gradient and the training loop.
   The loop fails on the inputs as they are, works on standardised inputs,
   and is judged on points it has not seen.
4. **The result.** The boundary is drawn over the data and the numbers are
   written into the report.

Everything is typed. The room starts from an empty file and ends with a
script of about 100 lines that needs NumPy and Matplotlib and nothing else.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows, with macOS in brackets. The script is run from
the terminal in the project folder:

```text
Windows (Git Bash)    python scripts/perceptron.py
macOS, Linux          python3 scripts/perceptron.py
```

The page writes `python` from here on. Every number on this page was
produced by running the step as written. The data file is generated with a
fixed seed and the split uses a fixed seed, so every laptop prints the same
numbers.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · A neuron by hand** · 30 min | |
| 0:00 | [1. Get the file and look at it](#file) | The file in `data/raw/`, its three columns named |
| 0:08 | [2. Load and plot](#plot) | Two arrays and a picture of two clouds |
| 0:20 | [3. A neuron with weights set by hand](#by-hand) | 88 % correct with a line read off the plot |
| | **Part 2 · Rosenblatt's rule** · 25 min | |
| 0:30 | [4. The rule on AND](#gate) | The ten updates of the lecture, reproduced |
| 0:45 | [5. The rule on the file](#rule-on-data) | A rule that never stops |
| | **Part 3 · The logistic neuron** · 45 min | |
| 0:55 | [6. Sigmoid and loss](#loss) | The loss 0.6931 for zero weights |
| 1:05 | [7. The gradient and the loop](#loop) | A loop that prints `nan` |
| 1:20 | [8. Standardise the inputs](#standardise) | The loss falling to 0.2542 |
| 1:30 | [9. Train and test](#test) | 67 of 75 unseen points correct |
| | **Part 4 · The result** · 20 min | |
| 1:40 | [10. Draw the boundary](#boundary) | The line over the two clouds |
| 1:50 | [11. Write it down](#report) | Five lines and a picture in the report |
| 1:55 | [12. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, leave out sections 5 and 9 and train on all 300 points.
Section 10 then starts from the weights of section 8.

## Prerequisites

For the room: the project folder with `data/raw/`, `scripts/` and
`results/`, Python with NumPy and Matplotlib, and the lecture's slides
*The Rule*, *The Training Loop* and *Standardising the Inputs* at hand.

For you, before the session:

- The whole page done once on your own laptop, with the script kept as a
  reference.
- [`perceptron_points.csv`](../data/perceptron_points.csv) on a USB stick,
  in case the network fails.
- The lecture's table *AND by the Rule* ready to show beside the terminal
  in section 4.

## Part 1 · A neuron by hand { #part-1 }

**0:00 to 0:30 · sections 1 to 3**

The room ends this part with the data as two arrays, a picture of them, and
a neuron whose three numbers were read off the picture.

## 1. Get the file and look at it { #file }

**0:00 · 8 min**

The file holds 300 points. Each has two inputs, `x1` and `x2`, and a label,
0 or 1. The points are generated: the script that made them is
[`perceptron_make_points.py`](../data/perceptron_make_points.py). The task
of the session is a rule that gives the label from the two inputs. Before
any code the file is read as text.

1. Download [`perceptron_points.csv`](../data/perceptron_points.csv) and
   drag it from **Downloads** onto the `raw` folder in the Side Bar.

2. Select the file to open it. Line 1 names the columns: `x1,x2,label`.

3. Press `Ctrl+End` (macOS `Cmd+↓`). VS Code numbers 302 lines and the last
   one is empty: one header line and 300 rows.

4. Open the terminal and look at the same file from there.

    ```text
    head -5 data/raw/perceptron_points.csv
    wc -l data/raw/perceptron_points.csv
    ```

5. Ask the room what one row is, and how large the numbers of each column
   are. `x1` is near 5. `x2` is near 300.

You should now see, in the terminal, the header with four rows, and 301
lines:

```text
x1,x2,label
4.37,374.2,0
7.42,522.4,1
6.43,426.7,1
7.98,471.3,1
```

## 2. Load and plot { #plot }

**0:08 · 12 min**

A classifier is built on a picture of the data. The file is read into one
array with `np.loadtxt`, the first two columns become the inputs `X` and
the third the labels `y`. A mask picks the points of one class, as in the
lecture on NumPy.

1. Select the `scripts` folder, then **New File**, and type
   `perceptron.py`. The file is empty.

2. Type the block and save.

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.loadtxt("data/raw/perceptron_points.csv",
                      delimiter=",", skiprows=1)
    X = data[:, :2]          # the two inputs, one row per point
    y = data[:, 2]           # the label, 0 or 1
    print(X.shape, y.shape)
    print("class 1:", int(y.sum()), "of", len(y))
    print("mean:", X.mean(axis=0).round(2),
          " std:", X.std(axis=0).round(2))

    fig, ax = plt.subplots()
    ax.plot(X[y == 0, 0], X[y == 0, 1], "o", label="class 0")
    ax.plot(X[y == 1, 0], X[y == 1, 1], "^", label="class 1")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.legend()
    fig.savefig("results/perceptron_points.png", dpi=150)
    ```

3. Run it: `python scripts/perceptron.py`.

4. Select `results/perceptron_points.png` in the Side Bar. Ask the room:
   can one straight line separate the two classes?

You should now see three lines in the terminal, and a picture of two clouds
that overlap in the middle:

```text
(300, 2) (300,)
class 1: 150 of 300
mean: [  5.06 329.43]  std: [  1.4  113.75]
```

No line separates the classes completely. The two columns are on different
scales: `x2` is about 65 times larger than `x1`. Both facts come back later.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` | The terminal is not in the project folder. Run `pwd`, then `cd` to it |
    | `ModuleNotFoundError: No module named 'matplotlib'` | `python -m pip install matplotlib` |
    | A window with the plot opens and the script waits | There is a `plt.show()` in the file. Delete it: the picture is saved to a file |

## 3. A neuron with weights set by hand { #by-hand }

**0:20 · 10 min**

The neuron of the lecture is two operations: the weighted sum
`z = w · x + b` and the step. With `X @ w` the sum is computed for all 300
points at once. Its weights are first set by hand: once as a threshold on
one input, once as a line read off the plot.

1. Add the neuron at the end of the script.

    ```text
    def predict(X, w, b):
        return (X @ w + b > 0).astype(int)
    ```

2. A threshold on `x1` alone: class 1 if `x1 > 5`. That is `w = (1, 0)` and
   `b = -5`. Add:

    ```text
    w = np.array([1.0, 0.0])
    b = -5.0
    print("x1 > 5:", np.mean(predict(X, w, b) == y))
    ```

3. Now a line. On the plot, a line from about (4.25, 400) to (6.25, 200)
   runs between the clouds. Work out its equation with the room on the
   board: the slope is (200 − 400) / (6.25 − 4.25) = −100, so
   `x2 = -100 x1 + 825`, or `100 x1 + x2 - 825 = 0`. Add:

    ```text
    w = np.array([100.0, 1.0])
    b = -825.0
    print("a line by eye:", np.mean(predict(X, w, b) == y))
    ```

4. Run the script.

You should now see two more lines:

```text
x1 > 5: 0.83
a line by eye: 0.8833333333333333
```

The threshold is right for 249 of the 300 points and the line for 265.
Using both inputs gains 16 points. The rest of the session finds the three
numbers from the data.

!!! warning "Watch for"
    `ValueError: matmul: Input operand 1 has a mismatch`. Then `w` does not
    have two numbers, or `X` was built with `data[:, :3]`.

## Part 2 · Rosenblatt's rule { #part-2 }

**0:30 to 0:55 · sections 4 and 5**

The rule of the lecture is written once on a problem with a known answer,
and then let loose on the file.

## 4. The rule on AND { #gate }

**0:30 · 15 min**

A new piece of code is tested on a case where the answer is known. The
lecture worked the AND gate through by hand: ten updates, and at the end
`w = (2, 1)`, `b = -2`. The code has to print the same.

1. Select the `scripts` folder, then **New File**, and type `gate.py`.

2. Type the block. The two lines after `y_hat` are the rule: the weights
   change by the error times the input.

    ```text
    import numpy as np

    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])       # AND
    w = np.zeros(2)
    b = 0.0

    for epoch in range(1, 7):
        updates = 0
        for x, target in zip(X, y):
            y_hat = int(w @ x + b > 0)
            w = w + (target - y_hat) * x
            b = b + (target - y_hat)
            updates = updates + int(y_hat != target)
        print("epoch", epoch, " w", w, " b", b, " updates", updates)
    ```

3. Run it: `python scripts/gate.py`. Compare each line with the table of
   the lecture: the weights after steps 4, 8, 12, 16, 20 and 24.

4. Change the targets to OR, `y = np.array([0, 1, 1, 1])`, and run again.
   Ask the room to check the last line by hand for all four inputs.

You should now see, for AND:

```text
epoch 1  w [1. 1.]  b 1.0  updates 1
epoch 2  w [2. 1.]  b 0.0  updates 3
epoch 3  w [2. 1.]  b -1.0  updates 3
epoch 4  w [2. 2.]  b -1.0  updates 2
epoch 5  w [2. 1.]  b -2.0  updates 1
epoch 6  w [2. 1.]  b -2.0  updates 0
```

For OR the updates are 1, 2, 1 and then 0, and the weights end at
`w [1. 1.]  b 0.0`. An epoch without an update means that every point is
right, and the weights stay as they are.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The updates never reach 0 | The comparison is `>= 0` in place of `> 0`, or `b` is not updated |
    | `IndentationError` | The four lines under `for x, target` are indented by eight spaces, the `print` by four |

## 5. The rule on the file { #rule-on-data }

**0:45 · 10 min**

The convergence theorem holds for data that a line can separate. The plot
showed that the 300 points are not of that kind. The room runs the rule on
them and sees what the theorem does not cover.

1. In `perceptron.py`, add at the end:

    ```text
    w = np.zeros(2)
    b = 0.0
    for epoch in range(1, 11):
        updates = 0
        for x, target in zip(X, y):
            y_hat = int(w @ x + b > 0)
            w = w + (target - y_hat) * x
            b = b + (target - y_hat)
            updates = updates + int(y_hat != target)
        print("epoch", epoch, "updates", updates,
              "correct", np.mean(predict(X, w, b) == y))
    ```

2. Run the script.

3. Ask the room for the smallest number of updates in an epoch, and for
   the share of correct points.

4. Select the eleven lines of this step and press `Ctrl+/` (macOS `Cmd+/`).
   Each line gets a `#` in front and is no longer run.

You should now see ten lines of this kind. The first two are:

```text
epoch 1 updates 143 correct 0.5
epoch 2 updates 142 correct 0.5
```

Every epoch has between 135 and 147 updates, and after every epoch half of
the points are right: the neuron gives all 300 points the same label. The
rule does not settle, for two reasons. The classes overlap, so some point
is always wrong. And one update adds a whole point to the weights: with
`x2` near 300 a single update throws the line across the entire cloud.

## Part 3 · The logistic neuron { #part-3 }

**0:55 to 1:40 · sections 6 to 9**

The step is replaced by the sigmoid and the rule by gradient descent on the
cross-entropy. Each piece is typed as a function and checked on a number
known from the lecture before the next one is added.

## 6. Sigmoid and loss { #loss }

**0:55 · 10 min**

Two functions. The sigmoid turns `z` into a probability. The loss is the
mean of `-ln` of the probability that the neuron gives to the true label.
Both are checked on numbers from the lecture: σ(2) = 0.881, and a neuron
with zero weights has the loss ln 2 = 0.6931, whatever the data.

1. Add at the end of `perceptron.py`:

    ```text
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))


    def loss(y, y_hat):
        return -np.mean(y * np.log(y_hat)
                        + (1 - y) * np.log(1 - y_hat))


    print(sigmoid(np.array([-2.0, 0.0, 2.0])).round(3))
    w = np.zeros(2)
    b = 0.0
    print("loss with zero weights:", loss(y, sigmoid(X @ w + b)).round(4))
    ```

2. Run the script.

3. Ask why the loss is 0.6931 before the neuron has seen anything. With
   zero weights every `z` is 0 and every output is 0.5, and −ln 0.5 = ln 2.

You should now see:

```text
[0.119 0.5   0.881]
loss with zero weights: 0.6931
```

## 7. The gradient and the loop { #loop }

**1:05 · 15 min**

The lecture derived the gradient of the loss: the mean of the error
`y_hat - y` times the input, and for the bias the mean of the error. In
NumPy that is `X.T @ (y_hat - y) / len(y)` and `np.mean(y_hat - y)`. One
pass of the loop computes the outputs, then moves the weights one step
against the gradient.

1. Add at the end:

    ```text
    eta = 0.5
    for epoch in range(1001):
        y_hat = sigmoid(X @ w + b)
        if epoch % 200 == 0:
            print(epoch, loss(y, y_hat).round(4),
                  np.mean((y_hat > 0.5) == y))
        w = w - eta * X.T @ (y_hat - y) / len(y)
        b = b - eta * np.mean(y_hat - y)
    ```

2. Before running, ask the room which of the two weights gets the larger
   steps. The gradient for `w2` is a mean of errors times `x2`, and `x2`
   is near 300.

3. Run the script.

You should now see warnings, and a loss that is not a number:

```text
RuntimeWarning: overflow encountered in exp
RuntimeWarning: divide by zero encountered in log
0 0.6931 0.5
200 nan 0.5
400 nan 0.5
```

The code is right and the result is useless. After the first step `w2` is
so large that every `z` is a huge number, every output is exactly 0 or 1,
and the loss contains ln 0. Half of the points are right because the
neuron gives all of them the same label.

!!! warning "Watch for"
    A student who lowers `eta` until the warnings stop. With
    `eta = 0.00001` they are gone, and after 1000 epochs the loss is 0.6702
    with half of the points right: the loop hardly moves. Say that this is
    the other half of the same problem, and go on to section 8.

## 8. Standardise the inputs { #standardise }

**1:20 · 10 min**

The remedy of the lecture: bring every column to mean 0 and standard
deviation 1. Then one learning rate suits both weights, and the result no
longer depends on the units of the file.

1. Above the line `eta = 0.5`, add:

    ```text
    m = X.mean(axis=0)
    s = X.std(axis=0)
    Z = (X - m) / s
    ```

2. In the loop, change `X` to `Z` in two places: in the line of `y_hat` and
   in the line of `w`.

3. Under the loop, without indentation, add:

    ```text
    print("w", w.round(3), "b", b.round(3))
    ```

4. Run the script.

You should now see no warning, and the loss falling:

```text
0 0.6931 0.5
200 0.2544 0.8866666666666667
400 0.2542 0.89
600 0.2542 0.89
800 0.2542 0.89
1000 0.2542 0.89
w [2.707 1.977] b -0.142
```

267 of the 300 points are right, two more than with the line read off the
plot. The loss has reached its minimum after about 400 epochs: more epochs
change nothing.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Still `nan` | One of the two `X` in the loop was not changed to `Z` |
    | The loss stays near 0.69 | `eta` is still the small value tried in section 7. Set it back to 0.5 |

## 9. Train and test { #test }

**1:30 · 10 min**

The 89 % were measured on the points the neuron was trained on. The task
was a rule for points it has not seen. So 75 points are held back: the loop
does not see them, and they are used once, at the end. The mean and
standard deviation for standardising come from the training points alone.

1. Replace the three lines of section 8 that make `m`, `s` and `Z` by:

    ```text
    rng = np.random.default_rng(11)
    order = rng.permutation(len(y))
    train = order[:225]
    test = order[225:]

    m = X[train].mean(axis=0)
    s = X[train].std(axis=0)
    Z = (X - m) / s
    ```

2. Change the loop so that it uses the training points only. It then reads:

    ```text
    eta = 0.5
    for epoch in range(1001):
        y_hat = sigmoid(Z[train] @ w + b)
        if epoch % 200 == 0:
            print(epoch, loss(y[train], y_hat).round(4))
        w = w - eta * Z[train].T @ (y_hat - y[train]) / len(train)
        b = b - eta * np.mean(y_hat - y[train])
    print("w", w.round(3), "b", b.round(3))
    ```

3. Under it, count the correct points of each set:

    ```text
    correct = predict(Z, w, b) == y
    print("train:", correct[train].sum(), "of", len(train),
          correct[train].mean().round(3))
    print("test: ", correct[test].sum(), "of", len(test),
          correct[test].mean().round(3))
    ```

4. Run the script.

5. Work out the uncertainty of the test accuracy with the room. Each test
   point is right or wrong, a binomial count: √(0.893 · 0.107 / 75) = 0.036.

You should now see:

```text
0 0.6931
200 0.2504
400 0.2501
600 0.2501
800 0.2501
1000 0.2501
w [2.848 1.678] b 0.11
train: 201 of 225 0.893
test:  67 of 75 0.893
```

The result of the session is the test accuracy with its uncertainty:
89 % ± 4 %. The training accuracy is the same here. A neuron with three
parameters cannot learn 225 points by heart.

!!! warning "Watch for"
    `order[:225]` typed as `order[225]`. Then `train` is one number, and the
    script stops with an error about a dimension.

## Part 4 · The result { #part-4 }

**1:40 to 2:00 · sections 10 to 12**

## 10. Draw the boundary { #boundary }

**1:40 · 10 min**

The weights belong to the standardised inputs. To draw the line on the plot
of section 2, they are converted back to the units of the file. Insert
`z = (x - m) / s` into `w · z + b`: the weight of each column is divided by
its `s`, and the bias takes up the means.

1. Add at the end:

    ```text
    w_x = w / s
    b_x = b - np.sum(w * m / s)
    print("for the file's units: w", w_x.round(4), "b", b_x.round(2))
    print("same answers:",
          np.all(predict(X, w_x, b_x) == predict(Z, w, b)))
    ```

2. Use the neuron on a point that is not in the file, `x1 = 5.0` and
   `x2 = 300`:

    ```text
    point = np.array([5.0, 300.0])
    print("P(class 1) at (5.0, 300):",
          sigmoid(point @ w_x + b_x).round(3))
    ```

3. Draw the line into the picture of section 2. On the boundary `z = 0`,
   so `x2 = -(w1 x1 + b) / w2`:

    ```text
    x1 = np.array([X[:, 0].min(), X[:, 0].max()])
    x2 = -(w_x[0] * x1 + b_x) / w_x[1]
    ax.plot(x1, x2, "k-", label="boundary")
    ax.set_ylim(0, 620)
    ax.legend()
    fig.savefig("results/perceptron_boundary.png", dpi=150)
    ```

4. Run the script and open `results/perceptron_boundary.png`.

You should now see three more lines, and a straight line between the two
clouds in the new picture:

```text
for the file's units: w [2.034  0.0143] b -14.79
same answers: True
P(class 1) at (5.0, 300): 0.417
```

Compare with the line read off the plot in section 3. Divided by its `w2`,
the trained neuron is `142 x1 + x2 - 1035 = 0`. The hand-set line was
`100 x1 + x2 - 825 = 0`. The point (5.0, 300) lies almost on the boundary:
the neuron gives it to class 1 with probability 0.42.

## 11. Write it down { #report }

**1:50 · 5 min**

A result that is not written down has to be computed again. The report gets
what a reader needs to repeat it: the data, the method, the settings and
the number with its uncertainty.

1. Open `results/report.md` and add at the end:

    ```text
    ## A logistic neuron on two classes

    - **Data:** `data/raw/perceptron_points.csv`, 300 generated
      points, two inputs, one label
    - **Model:** one neuron with a sigmoid, cross-entropy loss
    - **Training:** 225 points, inputs standardised, learning
      rate 0.5, 1000 epochs, seed 11 for the split
    - **Test:** 67 of 75 points correct, 89 % ± 4 %
    - **Boundary:** 2.034 x1 + 0.0143 x2 - 14.79 = 0

    ![The two classes and the boundary](perceptron_boundary.png)
    ```

2. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

3. In the Source Control view, stage `scripts/perceptron.py`,
   `scripts/gate.py`, the report and the two pictures, and commit them
   with the message `Train a logistic neuron on two classes`.

You should now see the five lines and the picture in the preview, and no
changed files left in the Source Control view.

## 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- A neuron is a weighted sum, a bias and a threshold. In NumPy it is one
  line for all points: `X @ w + b > 0`.
- New code is tested on a case with a known answer. The rule printed the
  ten updates of the AND gate before it was trusted with data.
- Rosenblatt's rule stops only when a line separates the classes. On
  overlapping classes it never does.
- The logistic neuron has a loss, and gradient descent lowers it. With zero
  weights the loss is ln 2 = 0.6931.
- Inputs on different scales break the loop. Standardised inputs repair it.
- A result is judged on points that were held back, and an accuracy is
  quoted with its uncertainty.

## Next steps, at home

**45 min, before the next session**

1. In your own dataset, choose two columns of numbers as inputs and a
   yes-or-no property as the label. If the data have no such column, make
   one: a third column above or below its median.

2. Copy `perceptron.py` to a new script and change the lines that read the
   file. Plot the two classes first.

3. Standardise, hold back a quarter of the rows, train, and write into your
   README the test accuracy with its uncertainty, and the accuracy of
   always answering with the more frequent class. A neuron that does not
   beat that number has learned nothing.

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- In section 8, run the loop with `eta = 0.05` and with `eta = 5`. The
  answer: the loss after 1000 epochs is 0.257 and 0.2542. The small rate
  has not arrived yet. The large one arrives at the same minimum.
- Take the `#` signs off the rule of section 5 and run it on `Z` in place
  of `X`, after the lines of section 8. The answer: 45 to 51 updates in
  every epoch and between 82 % and 89 % correct. Better than on the raw
  inputs, and still without an end.
- Change the seed of the split from 11 to each of 0 to 9. The answer: the
  number of correct test points lies between 62 and 69 of 75. That spread
  is what ± 4 % means.
- Write the three neurons of the lecture for XOR: hidden weights `(1, 1)`
  with biases `-0.5` and `-1.5`, output weights `(1, -1)` with bias
  `-0.5`. Use `predict` three times. The answer for the four inputs is
  `[0 1 1 0]`.
- Run `gate.py` with the targets of XOR, `[0, 1, 1, 0]`, and 12 epochs.
  The answer: from epoch 3 on every epoch has 4 updates and ends at
  `w [-1.  0.]  b 1.0`.

## If students ask for more

| Question | Answer |
|--|--|
| Why 89 % and not more? | The file was generated from two overlapping Gaussian clouds. No rule can be right for more than 91.5 % of such points on average |
| Is there a library for this? | Yes. `LogisticRegression` in scikit-learn minimises the same loss. The 100 lines of today are what it does inside |
| Can it learn a curved boundary? | Not one neuron. The lecture's XOR example shows why, and what a second layer changes |

## Aims practised

⚙️ a model trained by a script, from file to figure · 🔧 NumPy and nothing else · ♻️ fixed seeds, the same numbers on every laptop · 📁 the raw file read and never written
