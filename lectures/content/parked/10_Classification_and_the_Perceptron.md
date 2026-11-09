<!--
Parked slides from slides/10_Classification_and_the_Perceptron.md, taken out
on 9 Nov 2026 when the lecture was rebuilt on the weather log ("will it
freeze tonight?"). Until then the file was the old Lecture 11, The Perceptron,
on 200 generated points; a comment above each slide gives its number in that
deck, which can be read whole with
  git show 328aba2:lectures/content/slides/11_The_Perceptron.md
The figures of the generated points (viz_perceptron_points,
_threshold_vs_line, _eta and the other figures of that dataset) are no
longer drawn: a slide put back needs its figure redrawn on the weather log.
This file is not in decks.json: it is not built, not gated and not deployed.
To put a slide back, move it into the lecture file.
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 2: the goal quote; preambles left Lectures 6 to 12 on 9 Nov 2026 (no goal quote, no Learning Objectives). The New York Times of 8 July 1958 is the quote now. -->

---
hideInToc: true
layout: quote
---

# The goal of this lecture is to build **one artificial neuron** from first principles: what it computes, how it is trained, and what it cannot do

<!-- Parked 2026-11-09, old Lecture 11 slide 3: Learning Objectives; removed by the same rule. The deck opens on its question, Will It Freeze Tonight? -->

---
hideInToc: true
---

# Learning **Objectives**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📐 Compute the output of a neuron, draw its **decision boundary**, and give the distance of a point from it

</div>

<div class="card card-secondary card-glass pad-compact">

✏️ Apply **Rosenblatt's learning rule** by hand, and state when it stops and when it never does

</div>

<div class="card card-accent card-glass pad-compact">

📉 Derive the **cross-entropy loss** from the Bernoulli likelihood, and its gradient $(\hat{y} - y)\,\mathbf{x}$ by the chain rule

</div>

<div class="card card-success card-glass pad-compact">

🐍 Write the **training loop** in NumPy, and judge the result on points the neuron has not seen

</div>

<div class="card card-warning card-glass pad-compact">

🚧 Show that one neuron cannot compute **XOR**, and that two neurons in a hidden layer can

</div>

</div>

<!--
Speaker: five objectives, five parts of one argument. Nothing today needs a
library beyond NumPy. (~1 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 5: the 200 generated points around (0, 0) and (2, 2); the lecture now runs on the evenings of the weather log (slides 3, 4, 6 and 7). -->

---
hideInToc: true
---

# A Classification **Problem**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 📋 **The data**

- 200 points, generated with a fixed seed
- Each point has two **inputs**, $x_1$ and $x_2$
- Each point has a **label** $y$: 0 or 1
- 100 points of class 0 lie around (0, 0), 100 of class 1 around (2, 2)

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🎯 **The task**

Find a rule that gives the label of a point from its two inputs. The rule has to be found from the 200 examples, and it has to work on a point that is not among them.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_points.svg" style="display:block;margin:0 auto;max-height:400px;">

</div>

</div>

<!--
Speaker: think of two measured properties of an object and a yes-or-no question
about it. The two clouds overlap: no rule will be right for every point, and the
lecture computes how many it can get right. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 6: threshold against line on the 200 generated points; replaced by A Threshold on the Temperature and The Decision Boundary Is a Line, on the evenings. -->

---
hideInToc: true
---

# Classify by a Threshold or by a **Line**

<img class="fig" src="/figures/viz_perceptron_threshold_vs_line.svg" style="display:block;margin:0 auto;max-height:330px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**A threshold on $x_1$.** Of all thresholds, $x_1 > 1.39$ is right most often: for 177 of the 200 points, 88.5 %. It has one parameter.

</div>

<div class="card card-secondary card-glass pad-compact">

**A line.** The line on the right is correct for 185 points, 92.5 %. It uses both inputs and has three parameters: $w_1 x_1 + w_2 x_2 + b = 0$.

</div>

</div>

<!--
Speaker: the threshold was found by trying every value. The line was found by
the method of this lecture. The question of the lecture is how. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 7: a fit and a classification side by side; its last row is now the table One Update for Three Models, and the likelihood steps are on the slides of the sigmoid section. -->

---
hideInToc: true
---

<div class="card card-info card-glass pad-compact table-compact">

| | **A fit** (Lecture 10) | **A classification** (this lecture) |
| --- | --- | --- |
| The data | points $(x_i, y_i)$, with $y_i$ a measured number | points $(\mathbf{x}_i, y_i)$, with $y_i$ either 0 or 1 |
| The model | a curve $f(x; \theta)$ | a function of $\mathbf{w} \cdot \mathbf{x} + b$ |
| The parameters | $\theta$: slope, intercept, mass, width | the weights $\mathbf{w}$ and the bias $b$ |
| The probability of the data | Gaussian around the curve | Bernoulli: $y = 1$ with probability $\hat{y}$ |
| The loss, from the likelihood $\mathcal{L}$ | $-2 \ln \mathcal{L} = \chi^2 + \text{const}$ | $-\frac{1}{N} \ln \mathcal{L}$, the cross-entropy |
| How it is minimised | in closed form, or $\theta \leftarrow \theta - \eta \nabla \chi^2$ | $\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla L$ |

</div>

<div class="card card-primary card-glass pad-compact mt-md">

Only two things are new: the output is a class, and the probability that describes a class is not a Gaussian. An index $i$ numbers the points, $i = 1 \ldots N$; an index 1 or 2 numbers the inputs.

</div>

<!--
Speaker: read the table as the plan for the question of the last slide, how
the line of 185 was found. Each row of the right column is derived today. The
last row is the same line of mathematics in both columns. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 18: AND by the rule, epochs 3 and 4; the deck keeps one pass by hand (epochs 1 and 2) and the ten updates as lines. -->

---
hideInToc: true
---

# AND by the Rule: Epochs **3 and 4**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Step | $\mathbf{x}$ | $y$ | $\mathbf{w}$ before | $b$ before | $z$ | $\hat{y}$ | $y - \hat{y}$ | $\mathbf{w}$ after | $b$ after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | (0, 0) | 0 | (2, 1) | 0 | 0 | 0 | 0 | (2, 1) | 0 |
| 10 | (0, 1) | 0 | (2, 1) | 0 | 1 | 1 | **−1** | **(2, 0)** | **−1** |
| 11 | (1, 0) | 0 | (2, 0) | −1 | 1 | 1 | **−1** | **(1, 0)** | **−2** |
| 12 | (1, 1) | 1 | (1, 0) | −2 | −1 | 0 | **+1** | **(2, 1)** | **−1** |
| 13 | (0, 0) | 0 | (2, 1) | −1 | −1 | 0 | 0 | (2, 1) | −1 |
| 14 | (0, 1) | 0 | (2, 1) | −1 | 0 | 0 | 0 | (2, 1) | −1 |
| 15 | (1, 0) | 0 | (2, 1) | −1 | 1 | 1 | **−1** | **(1, 1)** | **−2** |
| 16 | (1, 1) | 1 | (1, 1) | −2 | 0 | 0 | **+1** | **(2, 2)** | **−1** |

</div>

<div class="card card-info card-glass pad-compact mt-md">

Epochs 2 and 3 have three updates each, epoch 4 has two. The bias has fallen from 1 to −1: the line moves away from the origin, towards the corner (1, 1).

</div>

<!--
Speaker: give the room steps 13 to 16 to do on paper, then show the rows. The
number of updates per epoch is 1, 3, 3, 2 so far. It does not fall steadily.
(~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 19: AND by the rule, epochs 5 and 6; as above. -->

---
hideInToc: true
---

# AND by the Rule: Epochs **5 and 6**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Step | $\mathbf{x}$ | $y$ | $\mathbf{w}$ before | $b$ before | $z$ | $\hat{y}$ | $y - \hat{y}$ | $\mathbf{w}$ after | $b$ after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | (0, 0) | 0 | (2, 2) | −1 | −1 | 0 | 0 | (2, 2) | −1 |
| 18 | (0, 1) | 0 | (2, 2) | −1 | 1 | 1 | **−1** | **(2, 1)** | **−2** |
| 19 | (1, 0) | 0 | (2, 1) | −2 | 0 | 0 | 0 | (2, 1) | −2 |
| 20 | (1, 1) | 1 | (2, 1) | −2 | 1 | 1 | 0 | (2, 1) | −2 |
| 21 | (0, 0) | 0 | (2, 1) | −2 | −2 | 0 | 0 | (2, 1) | −2 |
| 22 | (0, 1) | 0 | (2, 1) | −2 | −1 | 0 | 0 | (2, 1) | −2 |
| 23 | (1, 0) | 0 | (2, 1) | −2 | 0 | 0 | 0 | (2, 1) | −2 |
| 24 | (1, 1) | 1 | (2, 1) | −2 | 1 | 1 | 0 | (2, 1) | −2 |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 18 is the last update, the tenth. Epoch 6 goes through all four points without a change, so the run has ended: $\mathbf{w} = (2, 1)$, $b = -2$. The neuron computes AND.

</div>

<!--
Speaker: ten updates in 24 steps. The result is not the hand-set (1, 1) and
-1.5 of the earlier slide. Many lines separate these four points, and the rule
stops at the first one it reaches. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 34: the section slide of the loss; the likelihood and the cross-entropy are now part of the section From the Step to the Sigmoid. -->

---
layout: section
hideInToc: true
---

# The Loss: From Likelihood to **Cross-Entropy**

The output is now a probability, so every label has one, and the 200 labels have a likelihood. Lecture 10 turned the Gaussian likelihood into $\chi^2$. The same three steps, applied to labels that are 0 or 1, give the loss of the logistic neuron and its gradient.

<!--
Speaker: this is the centre of the lecture. Nothing in it is chosen for
convenience: the loss follows from the model, and the gradient follows from the
loss. (~1 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 45: the section Training in NumPy; no library calls on a lecture slide (9 Nov 2026). The loop is now plain Python: Training, Rosenblatt's Loop with One Change. -->

---
layout: section
hideInToc: true
---

# Training in **NumPy**

The loss has one minimum, and its gradient is a mean of $(\hat{y} - y)\,\mathbf{x}$ over the points. NumPy computes that mean for all 200 points in one line, and the whole training loop is a dozen lines.

<!--
Speaker: first the notation for all points at once, then the loop, then what
it does to the 200 points. (~1 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 46: the NumPy loop, line by line; as above. -->

---
hideInToc: true
---

# Reading the **Loop**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Line of the loop | Formula | Derived on the slide |
| --- | --- | --- |
| `y_hat = 1 / (1 + np.exp(-(X @ w + b)))` | $\hat{y}_i = \sigma(\mathbf{w} \cdot \mathbf{x}_i + b)$ | The Output Is a Probability |
| `loss = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))` | $L = -\frac{1}{N} \sum \bigl[ y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \bigr]$ | The Likelihood of All Points |
| `w = w - eta * X.T @ (y_hat - y) / len(y)` | $\mathbf{w} \leftarrow \mathbf{w} - \eta\,\frac{1}{N} \sum (\hat{y}_i - y_i)\,\mathbf{x}_i$ | The Gradient, Part 3 |
| `b = b - eta * np.mean(y_hat - y)` | $b \leftarrow b - \eta\,\frac{1}{N} \sum (\hat{y}_i - y_i)$ | The Gradient, Part 3 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

**All points at once.** `X` has one row per point. `X @ w` is the dot product of every row with `w`: 200 values of $z$ without a loop. `X.T @ (y_hat - y)` is the sum $\sum_i (\hat{y}_i - y_i)\,\mathbf{x}_i$.

</div>

<div class="card card-info card-glass pad-compact">

**An epoch** is one pass of the loop: all points are used once, and the weights change once. Rosenblatt's rule changed them after every single point.

</div>

</div>

<!--
Speaker: four lines of code, four formulas, each derived in the last half
hour. X.T is X with rows and columns exchanged. The loss is not needed for the
update: the loop computes it only to print it. (~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 47: the NumPy training loop on the 200 generated points; as above. -->

---
hideInToc: true
---

# The Training **Loop**

```py {monaco-run} {autorun:false}
import numpy as np
rng = np.random.default_rng(11)
X = np.vstack([rng.normal((0, 0), 1, (100, 2)),     # class 0
               rng.normal((2, 2), 1, (100, 2))])    # class 1
y = np.repeat([0, 1], 100)
w, b, eta = np.zeros(2), 0.0, 0.5
for epoch in range(1001):
    y_hat = 1 / (1 + np.exp(-(X @ w + b)))
    loss = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
    if epoch % 250 == 0:
        print(epoch, round(loss, 4), np.mean((y_hat > 0.5) == y))
    w = w - eta * X.T @ (y_hat - y) / len(y)
    b = b - eta * np.mean(y_hat - y)
print("w", w.round(3), "b", round(b, 3))
```

<!--
Speaker: run it. Each line of output is the epoch, the loss and the share of
points classified correctly. Measured: 0.6931 and 0.5 at epoch 0, 0.1651 and
0.92 at epoch 250, 0.1616 and 0.925 at epoch 1000, then w [2.1 2.257] and b
-4.315. 0.925 of 200 is 185: this is the line of the slide Classify by a
Threshold or by a Line, found. Change eta to 0.05 and run again: the loss at
epoch 1000 is 0.1809, not yet at the minimum. Why 0.6931 at the start: with
w = 0 and b = 0 every y-hat is 0.5, and each point costs ln 2. The loss falls
at every epoch, the accuracy does not: 93.5 % at epoch 50, 92.5 % at 100, 92 %
at 200. The loop minimises the loss, and the accuracy only follows it roughly.
(~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 49: the weights against the exact ones of two Gaussian clouds of generated points; no counterpart in the weather log. -->

---
hideInToc: true
---

# What the Result **Means**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ⚖️ **The weights**

| | $w_1$ | $w_2$ | $b$ |
| --- | --- | --- | --- |
| After 1000 epochs | 2.10 | 2.26 | −4.31 |
| At the minimum | 2.13 | 2.28 | −4.37 |
| Exact, from the two Gaussians | 2 | 2 | −4 |

The exact values follow from the slide Where the Sigmoid Comes From: $\mathbf{w}$ is the difference of the centres, $(2, 2) - (0, 0)$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **The accuracy**

- The trained neuron: 185 of 200, 92.5 %. Six points of class 0 and nine of class 1 are on the wrong side
- The exact line $x_1 + x_2 = 2$ on the same points: 184 of 200
- The exact line on new points from the same generator: 92.1 % on average

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The line of the slide **Classify by a Threshold or by a Line**, right for 185 of 200, is this neuron. It has recovered the rule that made the data, to within what 200 points allow. No rule does better than 92.1 % on new points: the clouds overlap.

</div>

<!--
Speaker: 92.1 % is the probability that a Gaussian value lies less than the
square root of 2 above its mean: the centres are 2.83 apart, the line is half
way, 1.41 from each. The fitted weights differ from the exact ones as a fitted
slope differs from the true one: by the scatter of a finite sample. (~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 50: the section Training in Practice; the learning rate and the scale of the inputs are handled by the humidity as a fraction (For the Curious: Humidity in Percent, the Rule Fails). -->

---
layout: section
hideInToc: true
---

# Training in **Practice**

The loop recovered the line of the generator, on 200 points whose inputs are of order 1 and with a learning rate that suits them. Other data need three decisions: the learning rate, the scale of the inputs, and the points on which the result is judged.

<!--
Speaker: nothing new is derived in this section. It is the same loop under
other conditions, each run and measured. (~1 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 51: the learning rate on the 200 generated points; as above. -->

---
hideInToc: true
---

# The **Learning Rate**

<div class="grid-2 mt-sm gap-md">

<div>

<img class="fig" src="/figures/viz_perceptron_eta.svg" style="display:block;margin:0 auto;width:100%;">

</div>

<div>

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **The same loop, four values of $\eta$**

| $\eta$ | Loss after 1000 epochs | |
| --- | --- | --- |
| 0.01 | 0.2742 | too slow |
| 0.1 | 0.1674 | not yet there |
| 1 | 0.1616 | at the minimum |
| 20 | 0.2049 | jumps to and fro |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ With $\eta = 20$ the loop prints `nan` for the first epochs. The weights jump so far that some $\hat{y}$ is exactly 0 or 1 in floating point, and the line of the loss computes $0 \cdot \ln 0$.

</div>

</div>

</div>

<!--
Speaker: as in Lecture 10. Too small a step wastes epochs. Too large a step
jumps across the valley and never settles: from epoch 100 on the red curve
swings between 0.20 and 0.24. Try 0.1, 1 and 20 in the runner of the training
loop. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 53: standardising the inputs; as above. -->

---
hideInToc: true
---

# **Standardising** the Inputs

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚖️ **Mean 0 and standard deviation 1**

For each column, subtract its mean and divide by its standard deviation:

```python
m = X.mean(axis=0)     # [1.057 1.032]
s = X.std(axis=0)      # [1.414 1.403]
Z = (X - m) / s
```

`Z` is the same whatever the units of `X` were. Trained on `Z` with $\eta = 0.5$, the loop reaches loss 0.1616 and 92.5 %, also for the file with $x_2$ times 100.

</div>

<div class="card card-secondary card-glass pad-compact">

## ↩️ **Back to the units of the data**

The neuron trained on `Z` has weights $\mathbf{w}'$ and bias $b'$. Insert $z_j = (x_j - m_j) / s_j$:

$$
w_j = \frac{w'_j}{s_j} \qquad b = b' - \sum_j \frac{w'_j\,m_j}{s_j}
$$

Here $\mathbf{w}' = (3.00, 3.20)$ and $b' = 0.23$ give $\mathbf{w} = (2.12, 2.28)$ and $b = -4.36$: the same line as before.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A new point is transformed with the **same** `m` and `s` before it is given to the neuron. They are part of the model, like the weights.

</div>

<!--
Speaker: the standard deviation of each column is 1.41, the square root of 2:
variance 1 inside a class plus 1 from the distance of the two centres. On
standardised inputs the loss passes 0.162 after 327 epochs instead of 523.
(~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 59: two lines separate XOR; the network of two layers is Lecture 11, From Neurons to Language Models (its figures, viz_perceptron_xor_strip, _network and _xor_hidden, are still drawn by figures/src/perceptron.py). -->

---
hideInToc: true
---

# Two Lines Separate **XOR**

<div class="grid-2 mt-sm gap-md">

<div>

<img class="fig" src="/figures/viz_perceptron_xor_strip.svg" style="display:block;margin:0 auto;max-height:400px;">

</div>

<div>

<div class="card card-primary card-glass pad-compact">

## ✌️ **XOR is "OR, but not AND"**

Both lines were on the slide of the gates:

- $h_1$: the OR neuron, $x_1 + x_2 - 0.5 > 0$
- $h_2$: the AND neuron, $x_1 + x_2 - 1.5 > 0$

The points of class 1 lie between the two lines: above the first and not above the second.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 3️⃣ **A third neuron combines them**

It takes $h_1$ and $h_2$ as its inputs and fires for "$h_1$ and not $h_2$":

$$
\hat{y} = \text{step}(h_1 - h_2 - 0.5)
$$

</div>

</div>

</div>

<!--
Speaker: one line cannot cut out a strip. Two lines can, and
a third neuron has to say "between". Its inputs are the outputs of the first
two. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 60: a network of three neurons; as above. -->

---
hideInToc: true
---

# A Network of **Three Neurons**

<img class="fig" src="/figures/viz_perceptron_network.svg" style="display:block;margin:0 auto;max-height:280px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**$h_1$** has weights $(1, 1)$ and bias $-0.5$. It computes OR.

</div>

<div class="card card-secondary card-glass pad-compact">

**$h_2$** has weights $(1, 1)$ and bias $-1.5$. It computes AND.

</div>

<div class="card card-accent card-glass pad-compact">

**The output** has weights $(1, -1)$ and bias $-0.5$, on the inputs $h_1$ and $h_2$.

</div>

</div>

<div class="note-text mt-sm">

Two inputs, two neurons in between, one output: a 2-2-1 network. The layer in between is called **hidden**, because its outputs are neither inputs nor the result. The network has $3 + 3 + 3 = 9$ parameters, all set by hand here.

</div>

<!--
Speaker: every circle is the neuron of the second section: a weighted sum, a
bias, a step. Nothing new has been added except that the output of one neuron
is the input of another. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 61: all four inputs of the network, verified (a NumPy runner); as above. -->

---
hideInToc: true
---

# All Four Inputs, **Verified**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| $x_1$ | $x_2$ | $z_1 = x_1 + x_2 - 0.5$ | $h_1$ | $z_2 = x_1 + x_2 - 1.5$ | $h_2$ | $z_{\text{out}} = h_1 - h_2 - 0.5$ | $\hat{y}$ | XOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | −0.5 | 0 | −1.5 | 0 | −0.5 | 0 | 0 |
| 0 | 1 | 0.5 | 1 | −0.5 | 0 | 0.5 | 1 | 1 |
| 1 | 0 | 0.5 | 1 | −0.5 | 0 | 0.5 | 1 | 1 |
| 1 | 1 | 1.5 | 1 | 0.5 | 1 | −0.5 | 0 | 0 |

</div>

```py {monaco-run} {autorun:false}
import numpy as np
def step(z):
    return (z > 0).astype(int)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
W1 = np.array([[1, 1], [1, 1]])     # one row per hidden neuron
b1 = np.array([-0.5, -1.5])
w2, b2 = np.array([1, -1]), -0.5
H = step(X @ W1.T + b1)             # hidden outputs h1, h2
print(H.tolist(), step(H @ w2 + b2))
```

<!--
Speaker: the table by hand, then the same in nine lines. The output is
[[0, 0], [1, 0], [1, 0], [1, 1]] for the hidden layer and [0 1 1 0] for the
network. Change b1 to [-0.5, -0.5] and see the network fail. (~3 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 62: the hidden layer changes the coordinates; as above. -->

---
hideInToc: true
---

# The Hidden Layer Changes the **Coordinates**

<img class="fig" src="/figures/viz_perceptron_xor_hidden.svg" style="display:block;margin:0 auto;max-height:300px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**From $(x_1, x_2)$ to $(h_1, h_2)$.** The output neuron does not see the inputs. It sees the two hidden outputs: (0, 0) goes to (0, 0), both (0, 1) and (1, 0) go to (1, 0), and (1, 1) goes to (1, 1).

</div>

<div class="card card-success card-glass pad-compact">

In these coordinates there are three points, and the line $h_1 - h_2 = 0.5$ separates them. The hidden layer has turned a problem that is not linearly separable into one that is.

</div>

</div>

<!--
Speaker: this is the one idea to take from the last section. A layer of
neurons computes new coordinates, and in the new coordinates a line is enough.
(~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 63: what is missing: hidden layers cannot be trained by the rules of this lecture; as above. -->

---
hideInToc: true
---

# What Is **Missing**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ✋ **The nine numbers were set by hand**

That was possible because XOR is known in advance to be "OR, but not AND". For data, nobody knows which hidden neurons are needed.

</div>

<div class="card card-primary card-glass pad-compact">

## 🚫 **Neither rule of this lecture trains them**

- Rosenblatt's rule needs a target for every neuron. The data give a target for the output only, and none for $h_1$ and $h_2$
- Gradient descent needs a slope, and a hidden **step** has none

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

With sigmoid units in the hidden layer the loss does have a slope in every weight, and the chain rule of this lecture gives it: one more factor for every layer between a weight and the loss.

</div>

<!--
Speaker: the lecture stops here, with one neuron understood completely and the
reason why more are needed. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 66: what a modern network keeps; for Lecture 11. -->

---
hideInToc: true
---

# What a Modern Network **Keeps**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ♻️ **Unchanged**

- The unit: a weighted sum, a bias, then a fixed function of $z$
- The loss: minus the logarithm of a likelihood
- The training: the gradient of the loss by the chain rule, and steps of size $\eta$ against it
- For two classes, the last unit of a network is the logistic neuron of this lecture, with the cross-entropy as its loss

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔄 **Changed**

- The number of units: from 1 here to millions, in layers
- The function after the sum: the step is gone. Smooth or piecewise-linear functions took its place, such as $\max(0, z)$
- The number of parameters: 3 in this lecture, more than $10^9$ in large networks
- The points per update: a random part of the data in place of all of it

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The neuron of this lecture is the building block. What was derived for it, the likelihood, the loss and the gradient, is what is computed for every unit of a large network.

</div>

<!--
Speaker: the mathematics of this lecture has not been replaced. It is repeated
many times over. (~2 min)
-->

<!-- Parked 2026-11-09, old Lecture 11 slide 70: the quiz on the distance from the line; the distance is now in For the Curious. -->

---
hideInToc: true
---

<MCQ
  question="A neuron has w = (6, 8) and b = −5. How far is the point x = (2, 1) from its decision boundary?"
  :options="[
    '15',
    '0.5',
    '1.5',
    '3'
  ]"
  :correct="2"
  explanation="z = 12 + 8 − 5 = 15 and the length of w is the square root of 36 + 64, which is 10. The distance is z divided by the length of w: 1.5. It is positive, so the point is on the side of class 1."
/>
