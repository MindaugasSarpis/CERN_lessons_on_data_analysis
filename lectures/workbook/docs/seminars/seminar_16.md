# Seminar 16 — A Small Network, Measured

**Paired lecture:** 16 Machine Learning & AI · **Format:** follow-along · **~120 min**
in class

The seminar has three parts, in this order.

1. **The file and the split.** A file with two classes is loaded, plotted and
   split into training, validation and test rows.
2. **The network.** The room writes the network of the lecture as two
   functions, trains it, and chooses the number of hidden units with the
   validation rows.
3. **The measurement.** The test rows are used once. The confusion matrix is
   counted by hand and then with scikit-learn, and the result is written
   into the README.

Everything is typed into one script, `scripts/network.py`, which grows from
section to section. It needs NumPy and Matplotlib. scikit-learn is installed
in section 8.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Commands are written for Windows in Git Bash, with macOS in brackets:
`python` (macOS `python3`). The script is run from the project folder after
every section. Every number on this page was produced by running the step
with NumPy 2.3 and scikit-learn 1.7.2.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · The file and the split** · 25 min | |
| 0:00 | [1. Get the file and look at it](#file) | A plot of the two classes in `results/` |
| 0:12 | [2. Split and scale](#split) | Three sets of row numbers, and scaled inputs |
| | **Part 2 · The network** · 45 min | |
| 0:25 | [3. One neuron first](#neuron) | 65 % of the training rows right |
| 0:35 | [4. The network as two functions](#network) | 95.6 % of the training rows right |
| 0:55 | [5. How many hidden units](#units) | A table of five networks, and a choice |
| | **Part 3 · The measurement** · 50 min | |
| 1:10 | [6. The test rows, once](#test) | 114 of 120 |
| 1:15 | [7. The confusion matrix by hand](#confusion) | Four counts, precision and recall |
| 1:30 | [8. The same with scikit-learn](#sklearn) | The same matrix from a package |
| 1:45 | [9. Write down the result](#readme) | A **Results** section in the README |
| 1:55 | [10. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, leave out section 5 and show its table from the lecture
instead, and give section 9 as homework.

## Prerequisites

For the room: the project folder with `data/raw`, `scripts`, `results` and
`README.md`, and a Python that has NumPy and Matplotlib. The lecture: the
forward pass, the eight lines of backpropagation, the three sets of rows and
the confusion matrix.

For you, before the session:

- The whole script run once on your own laptop, so that you have seen every
  number of this page on your own screen.
- scikit-learn installed on your laptop. Section 8 needs the network for
  `pip`. If the room has none, do section 8 on the projector only.
- [`ml_two_class.csv`](../data/ml_two_class.csv) on a USB stick. The script
  that made it is [`ml_two_class.py`](../data/ml_two_class.py).

## Part 1 · The file and the split { #part-1 }

**0:00 to 0:25 · sections 1 and 2**

The room ends this part with the data loaded, seen as a picture, and divided
into the rows for training, for choosing and for testing.

## 1. Get the file and look at it { #file }

**0:00 · 12 min**

The file has 600 rows. Each row has two measured quantities, `x1` and `x2`,
and a label, 0 or 1. The data are simulated, so the classes are known for
every row. The first thing to do with any data is to look at it.

1. Download [`ml_two_class.csv`](../data/ml_two_class.csv) and put it into
   `data/raw/`. Open it in VS Code and read the first lines.

    ```text
    x1,x2,label
    6.974,28.38,0
    5.062,14.85,0
    ```

2. Create the file `scripts/network.py` and type:

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.loadtxt("data/raw/ml_two_class.csv", delimiter=",",
                      skiprows=1)
    X, y = data[:, :2], data[:, 2]
    print(data.shape, np.sum(y == 1), np.sum(y == 0))
    ```

3. Open the terminal in the project folder and run the script.

    ```text
    python scripts/network.py          (macOS: python3 scripts/network.py)
    ```

    It prints `(600, 3) 300 300`: 600 rows, three columns, 300 rows of each
    class.

4. Add the plot below the `print` line and run again.

    ```text
    plt.scatter(X[y == 0, 0], X[y == 0, 1], s=8, label="class 0")
    plt.scatter(X[y == 1, 0], X[y == 1, 1], s=8, label="class 1")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.savefig("results/ml_two_class.png", dpi=150)
    ```

5. Open `results/ml_two_class.png`. Ask the room: can one straight line
   separate the two colours?

You should now see a picture with class 1 as a cloud in the middle and
class 0 as a ring around it. `x1` runs from about 2 to 8 and `x2` from about
5 to 57.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` | The terminal is not in the project folder. Run `pwd`, then `cd` to the folder that holds `data` and `scripts` |
    | `ModuleNotFoundError: No module named 'matplotlib'` | `python -m pip install numpy matplotlib` (macOS `python3 -m pip ...`) |

## 2. Split and scale { #split }

**0:12 · 13 min**

A model is judged on rows it has not seen. So the rows are divided before
anything is trained: 360 for training, 120 for choosing between models, 120
for the final test. The division is made by a shuffle with a seed, so that
everyone in the room gets the same rows. Then the inputs are standardised,
with the mean and the standard deviation of the training rows only.

1. Add to the script:

    ```text
    rng = np.random.default_rng(0)
    idx = rng.permutation(len(y))
    train, val, test = idx[:360], idx[360:480], idx[480:]
    print(idx[:5], len(train), len(val), len(test))
    ```

2. Run it. The new line of output is `[576 229 363 153 212] 360 120 120`:
   the first five row numbers after the shuffle, and the sizes of the three
   sets.

3. Add the scaling:

    ```text
    mu, sd = X[train].mean(axis=0), X[train].std(axis=0)
    Z = (X - mu) / sd
    print(mu.round(2), sd.round(2))
    print(Z[train].mean(axis=0).round(2), Z[train].std(axis=0).round(2))
    ```

4. Run it. Ask why `mu` and `sd` are computed from `X[train]` and not from
   `X`. The answer: the validation and test rows stand for rows that do not
   exist yet when the model is made. Nothing may be learned from them.

You should now see two more lines:

```text
[ 5.04 28.96] [ 1.09 10.67]
[0. 0.] [1. 1.]
```

The training rows of `Z` have the mean 0 and the standard deviation 1 in both
columns. `train`, `val` and `test` hold row numbers, not rows: `Z[train]` are
the scaled training rows and `y[train]` their labels.

## Part 2 · The network { #part-2 }

**0:25 to 1:10 · sections 3 to 5**

First the neuron of Lecture 11, to see what one line can do on this file.
Then the network with one hidden layer.

## 3. One neuron first { #neuron }

**0:25 · 10 min**

One neuron draws one straight line. The picture of section 1 says that no
line will do. The training loop of Lecture 11 puts a number on that.

1. Add two small functions:

    ```text
    def sigma(z):
        return 1 / (1 + np.exp(-z))

    def accuracy(y_hat, y):
        return np.mean((y_hat > 0.5) == y)
    ```

2. Add the neuron and its training loop:

    ```text
    w, b, eta = np.zeros(2), 0.0, 1.0
    for epoch in range(5000):
        y_hat = sigma(Z[train] @ w + b)
        w = w - eta * Z[train].T @ (y_hat - y[train]) / len(train)
        b = b - eta * np.mean(y_hat - y[train])
    print("neuron", accuracy(sigma(Z[train] @ w + b), y[train]).round(3),
          accuracy(sigma(Z[val] @ w + b), y[val]).round(3))
    ```

3. Run it and read the two numbers: the share of training rows and of
   validation rows that the neuron gets right.

You should now see `neuron 0.653 0.625`. Half the rows are of each class, so
a guess is right for 0.5. The neuron is hardly better.

## 4. The network as two functions { #network }

**0:35 · 20 min**

The network has one hidden layer of `H` sigmoid units and one output neuron.
`fit` is the training loop of the lecture: a forward pass, the backward pass
in two lines, the update in two lines. `predict` is the forward pass alone.
Type it with the room line by line, and say for each line which formula of
the lecture it is.

1. Add `fit`:

    ```text
    def fit(X, y, H, seed=0, eta=1.0, epochs=5000):
        rng = np.random.default_rng(seed)
        V, c = rng.normal(0, 1, (H, 2)), np.zeros(H)
        w, b = rng.normal(0, 1, H), 0.0
        for epoch in range(epochs):
            h = sigma(X @ V.T + c)                    # forward
            y_hat = sigma(h @ w + b)
            d = (y_hat - y) / len(y)                  # backward
            dh = np.outer(d, w) * h * (1 - h)
            w, b = w - eta * h.T @ d, b - eta * d.sum()
            V, c = V - eta * dh.T @ X, c - eta * dh.sum(axis=0)
        return V, c, w, b
    ```

2. Add `predict` and a function for the loss:

    ```text
    def predict(p, X):
        V, c, w, b = p
        return sigma(sigma(X @ V.T + c) @ w + b)

    def loss(y_hat, y):
        return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
    ```

3. Train a network with four hidden units and measure it:

    ```text
    p = fit(Z[train], y[train], H=4)
    print("network", accuracy(predict(p, Z[train]), y[train]).round(3),
          accuracy(predict(p, Z[val]), y[val]).round(3))
    ```

4. Run it. The training takes less than a second.

5. Ask what `p` holds. The answer: four arrays with 8 + 4 + 4 + 1 = 17
   numbers, the parameters of the network.

You should now see `network 0.956 0.917`: 344 of the 360 training rows and
110 of the 120 validation rows are right.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `network 0.683 ...` | The network was trained on `X[train]`. It needs the scaled rows, `Z[train]` |
    | `ValueError: shapes ... not aligned` | `V.T` was typed as `V`, or `h.T @ d` as `h @ d` |
    | Other numbers than 0.956 and 0.917 | A seed differs. Check `default_rng(0)` in section 2 and `seed=0` in `fit` |

## 5. How many hidden units { #units }

**0:55 · 15 min**

The number of hidden units is not found by gradient descent. It is chosen,
and the validation rows make the choice. The training loss cannot: it falls
with every unit that is added.

1. Add a loop over five networks:

    ```text
    for H in (1, 2, 3, 4, 8):
        q = fit(Z[train], y[train], H)
        print(H, loss(predict(q, Z[train]), y[train]).round(3),
              loss(predict(q, Z[val]), y[val]).round(3),
              accuracy(predict(q, Z[val]), y[val]).round(3))
    ```

2. Run it and write the table on the board. The columns are the number of
   hidden units, the training loss, the validation loss and the validation
   accuracy.

3. Ask which network to take. The answer: the one with the lowest validation
   loss, four units.

You should now see:

```text
1 0.57 0.639 0.617
2 0.398 0.626 0.742
3 0.138 0.233 0.9
4 0.123 0.209 0.917
8 0.118 0.219 0.908
```

The training loss falls all the way down the second column. The validation
loss is lowest at four units and rises again at eight. With one or two units
the network cannot close a region around the cloud. Three lines can.

## Part 3 · The measurement { #part-3 }

**1:10 to 2:00 · sections 6 to 10**

The model is chosen. Now the test rows are used, once, and the result is
taken apart into its four counts.

## 6. The test rows, once { #test }

**1:10 · 5 min**

The test rows have not been used for anything so far. That is what makes the
number they give honest. After this step no setting of the model is changed.

1. Add:

    ```text
    score = predict(p, Z[test])
    print("test", accuracy(score, y[test]),
          np.sum((score > 0.5) == y[test]))
    ```

2. Run it.

3. Work out the uncertainty with the room, as in Lecture 11: the square root
   of 0.95 · 0.05 / 120 is 0.020.

You should now see `test 0.95 114`: 114 of the 120 test rows are right. The
result to report is 0.95 ± 0.02.

## 7. The confusion matrix by hand { #confusion }

**1:15 · 15 min**

An accuracy does not say which kind of error was made. The confusion matrix
does: it counts the rows by their true class and by the decision of the
network. The counting is done with two masks.

1. Add:

    ```text
    pred = score > 0.5
    t = y[test] == 1
    TP, FP = np.sum(pred & t), np.sum(pred & ~t)
    FN, TN = np.sum(~pred & t), np.sum(~pred & ~t)
    print(TP, FP, FN, TN)
    ```

2. Run it and write the matrix on the board.

    | | Predicted 1 | Predicted 0 |
    |--|--|--|
    | **Class 1** | 53 | 4 |
    | **Class 0** | 2 | 61 |

3. Let the room compute on paper: precision = TP / (TP + FP) = 53 / 55, and
   recall = TP / (TP + FN) = 53 / 57.

4. Check with one more line:

    ```text
    print((TP / (TP + FP)).round(3), (TP / (TP + FN)).round(3))
    ```

You should now see `53 2 4 61` and `0.964 0.93`. The four counts add up to
120, and 53 + 61 = 114 is the number of section 6.

Say it in these words: of the rows the network called class 1, 96.4 % are
class 1. Of the rows that are class 1, the network found 93.0 %.

## 8. The same with scikit-learn { #sklearn }

**1:30 · 15 min**

scikit-learn is a Python package that holds tested versions of what was just
typed by hand. The first use of a packaged function is a comparison with the
hand version.

1. Install the package from the terminal.

    ```text
    python -m pip install scikit-learn
    (macOS: python3 -m pip install scikit-learn)
    ```

2. Add to the script and run:

    ```text
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_score, recall_score
    print(confusion_matrix(y[test], pred))
    print(round(precision_score(y[test], pred), 3),
          round(recall_score(y[test], pred), 3))
    ```

3. Compare with section 7. The matrix of scikit-learn starts with class 0:
   TN is at the top left and TP at the bottom right.

4. Now let scikit-learn train a network of the same shape:

    ```text
    from sklearn.neural_network import MLPClassifier
    net = MLPClassifier(hidden_layer_sizes=(4,), activation="logistic",
                        solver="lbfgs", random_state=0, max_iter=5000)
    net.fit(Z[train], y[train])
    print(confusion_matrix(y[test], net.predict(Z[test])))
    print(net.score(Z[test], y[test]))
    ```

You should now see, from step 2:

```text
[[61  2]
 [ 4 53]]
0.964 0.93
```

The counts and the two rates are those of the hand version. Step 4 printed,
with scikit-learn 1.7.2:

```text
[[61  2]
 [ 5 52]]
0.9416666666666667
```

That network is right for 113 of the 120 test rows, one fewer than the
network typed by hand. It starts from other random weights and follows the
gradient in another way, so it ends at slightly different weights. Another
version of scikit-learn can differ by a row or two.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No module named 'sklearn'` after installing | `pip` installed into another Python. Use `python -m pip`, with the same `python` that runs the script |
    | The package `sklearn` is installed by name | The package to install is `scikit-learn`. `sklearn` is only the name in `import` |

## 9. Write down the result { #readme }

**1:45 · 10 min**

A trained model is a result, and a result is written down with what is
needed to get it again: the script, the seeds, the split and the versions.

1. Open `README.md` and add a section. The room types the labels and fills
   in its own numbers.

    ```text
    ## Results: a network on ml_two_class.csv

    - Script: `scripts/network.py`, seed 0 for the split and for the
      starting weights
    - Split: 360 training, 120 validation, 120 test rows
    - Model: one hidden layer of 4 sigmoid units, 17 parameters,
      5000 epochs, learning rate 1
    - Chosen by the validation loss among 1, 2, 3, 4 and 8 units
    - Test rows: 114 of 120 right, accuracy 0.95 +- 0.02
    - Confusion matrix: TP 53, FP 2, FN 4, TN 61
    - Precision 0.964, recall 0.930
    - Checked with scikit-learn 1.7.2: the same matrix
    ```

2. Add one line on where the data came from: simulated by
   `ml_two_class.py`, seed 16.

3. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`), and
   read the section.

You should now see a **Results** section in the preview from which someone
else could repeat the run.

## 10. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- A network with one hidden layer is about a dozen lines of NumPy: a forward
  pass, a backward pass, an update.
- The rows are split before anything is trained. Training rows fit the
  weights, validation rows choose the model, test rows are used once.
- The scaling constants come from the training rows.
- The training loss always prefers the larger network. The validation loss
  does not.
- An accuracy has an uncertainty. With 120 test rows it is 0.02.
- The confusion matrix holds four counts. Precision and recall are two
  ratios of them.
- A packaged function is checked against the hand version the first time it
  is used.

## Next steps, at home

**45 min**

1. Find a yes-or-no question in your own dataset: a column with two values,
   or a numeric column cut at a threshold that means something. Choose two
   numeric columns as inputs. Do not use the column from which the label was
   made.

2. Copy `network.py`, load your file, and run sections 2 to 7 on it: split
   with a seed, scale with the training rows, train, choose the number of
   hidden units with the validation rows, test once, count the confusion
   matrix.

3. Write the **Results** section for it into your README, and add one
   sentence: which error costs more in your question, a false positive or a
   false negative?

4. If your dataset has no such question, repeat the seminar with another
   split: change `default_rng(0)` in section 2 to `default_rng(1)`. The test
   result becomes 116 of 120, with the counts 47, 1, 3, 69. Write down why
   it differs from 114.

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Change the cut in `pred = score > 0.5` to 0.1 and to 0.9. The counts TP,
  FP, FN, TN are 57, 19, 0, 44 at 0.1 and 48, 1, 9, 62 at 0.9. Precision and
  recall are 0.750 and 1.000, then 0.980 and 0.842.
- Compute the area under the ROC curve by counting pairs:

    ```text
    s1, s0 = score[t], score[~t]
    pairs = s1[:, None] > s0[None, :]
    print(pairs.size, pairs.sum(), pairs.mean().round(4))
    ```

    The answer is `3591 3558 0.9908`. `roc_auc_score(y[test], score)` from
    `sklearn.metrics` gives 0.9908 as well.
- Train on `X[train]` in place of `Z[train]`. The training accuracy is
  0.683: without scaling, the column with the large numbers saturates the
  hidden units.
- Remove `solver="lbfgs"` from the `MLPClassifier`. With scikit-learn 1.7.2
  the test accuracy falls to 0.483. The default method stops after 213
  passes at a loss of 0.684, before the network has learned anything.
- Ask a language model to write `fit` for you, and check its answer against
  yours on the same seed and rows. The check is the point: equal confusion
  matrices, or a difference you can explain.

## If students ask for more

| Topic | Where |
|--|--|
| Backpropagation for any number of layers | M. Nielsen, *Neural Networks and Deep Learning*, chapter 2, free at neuralnetworksanddeeplearning.com |
| Validation, cross-validation, classification | James, Witten, Hastie, Tibshirani, Taylor, *An Introduction to Statistical Learning with Applications in Python*, free at statlearning.com |
| Every function of section 8 | The user guide at scikit-learn.org |

## Aims practised

♻️ a seeded split and a seeded training, written down so that the run can be repeated · 🔧 the same result by hand and with a package · ⚙️ one script from the raw file to the confusion matrix
