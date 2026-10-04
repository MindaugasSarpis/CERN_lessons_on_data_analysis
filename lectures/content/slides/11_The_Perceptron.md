---
layout: cover
title: "The Perceptron"
# slidev-addon-python-runner reads this block from slide 1 = this cover (see CLAUDE.md)
python:
  installs: ["numpy"]
  prelude: |
    import numpy as np
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## The Perceptron

##### <span class="aims-badge">⚙️ automation · 🔧 tool-agnostic</span>

<!--
Speaker: Lecture 10 fitted a number: a slope, a mass, a width. Today the thing
to predict is a class, 0 or 1. The whole lecture builds one unit, the artificial
neuron, and every formula in it is derived from what Lectures 09 and 10
established: likelihood, the chain rule, gradient descent. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The goal of this lecture is to build **one artificial neuron** from first principles: what it computes, how it is trained, and what it cannot do

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

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

---
layout: section
hideInToc: true
---

# From a Number to a **Class**

A fit returns a number with an uncertainty. A classifier returns one of two labels. The method stays the same: a model with parameters, a likelihood, a loss to minimise.

<!--
Speaker: this section sets the problem and the data, and fixes the symbols.
(~1 min)
-->

---
hideInToc: true
---

# What Lecture 10 **Built**, and What Changes

<div class="card card-info card-glass pad-compact mt-sm table-compact">

| | **A fit** (Lecture 10) | **A classification** (this lecture) |
| --- | --- | --- |
| The data | points $(x_i, y_i)$, with $y_i$ a measured number | points $(\mathbf{x}_i, y_i)$, with $y_i$ either 0 or 1 |
| The model | a curve $f(x; \theta)$ | a function of $\mathbf{w} \cdot \mathbf{x} + b$ |
| The parameters | $\theta$: slope, intercept, mass, width | the weights $\mathbf{w}$ and the bias $b$ |
| The probability of the data | Gaussian around the curve | Bernoulli: $y = 1$ with probability $\hat{y}$ |
| The loss, $-\ln$ of the likelihood | $\chi^2$ | the cross-entropy |
| How it is minimised | in closed form, or $\theta \leftarrow \theta - \eta \nabla \chi^2$ | $\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla L$ |

</div>

<div class="card card-primary card-glass pad-compact mt-md">

The left column is known. The right column is this lecture, row by row. Only two things are new: the output is a class, and the probability that describes a class is not a Gaussian.

</div>

<!--
Speaker: read the table as the plan. Each row of the right column is derived
today. The last row is the same line of mathematics in both columns. (~2 min)
-->

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

---
hideInToc: true
---

# A Rule with One Input, a Rule with **Two**

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
the method of this lecture. The question for the next 80 minutes is how. (~2 min)
-->

---
hideInToc: true
---

# The **Symbols** of This Lecture

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Symbol | Meaning |
| --- | --- |
| $\mathbf{x} = (x_1, x_2)$ | the inputs of one point, a vector |
| $y$ | its label, the **target**: 0 or 1 |
| $\mathbf{w} = (w_1, w_2)$ | the **weights**, one per input |
| $b$ | the **bias**, one number |
| $z = \mathbf{w} \cdot \mathbf{x} + b$ | the weighted sum |
| $\hat{y}$ | the **output** of the neuron |
| $\eta$ | the learning rate |
| $L$ | the loss |

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## ✖️ **The dot product**

$$
\mathbf{w} \cdot \mathbf{x} = w_1 x_1 + w_2 x_2
$$

With $\mathbf{w} = (2, -1)$ and $\mathbf{x} = (3, 2)$: $\;2 \cdot 3 + (-1) \cdot 2 = 4$.

</div>

<div class="card card-info card-glass pad-compact mt-md">

An index $i$ numbers the points: $\mathbf{x}_i$, $y_i$, with $i = 1 \ldots N$. An index 1 or 2 on a plain letter numbers the inputs. The parameters of the model are $w_1$, $w_2$ and $b$: three numbers.

</div>

</div>

</div>

<!--
Speaker: bold letters are vectors. The hat on y marks what the model says, as
the hat on theta marked an estimate in Lecture 10. (~2 min)
-->

---
layout: section
hideInToc: true
---

# One **Neuron**

A weighted sum, a bias and a threshold. What it computes is a line in the plane of the inputs, and everything about that line can be read off the weights.

<!--
Speaker: no learning yet. The weights are set by hand in this section, so that
the geometry is clear before anything moves. (~1 min)
-->

---
hideInToc: true
---

# Weighted Sum, Bias, **Step**

<img class="fig" src="/figures/viz_perceptron_unit_step.svg" style="display:block;margin:0 auto;max-height:215px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **Two operations**

$$
z = \mathbf{w} \cdot \mathbf{x} + b \qquad\quad \hat{y} = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{if } z \le 0 \end{cases}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **With numbers**

$\mathbf{w} = (2, -1)$, $b = -1$.

- $\mathbf{x} = (3, 2)$: $z = 6 - 2 - 1 = 3$, so $\hat{y} = 1$
- $\mathbf{x} = (1, 2)$: $z = 2 - 2 - 1 = -1$, so $\hat{y} = 0$

</div>

</div>

<!--
Speaker: this unit with the step is the perceptron. The bias is drawn as a
weight on a constant input 1: that picture is used again in the proof. On the
convention: z exactly 0 gives 0 here. Other books choose 1. It matters only for
points exactly on the line. (~2 min)
-->

---
hideInToc: true
---

# A Neuron Computes **AND** and **OR**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔌 **Weights set by hand: $\mathbf{w} = (1, 1)$**

| $x_1$ | $x_2$ | $z$ with $b = -1.5$ | AND | $z$ with $b = -0.5$ | OR |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | −1.5 | 0 | −0.5 | 0 |
| 0 | 1 | −0.5 | 0 | 0.5 | 1 |
| 1 | 0 | −0.5 | 0 | 0.5 | 1 |
| 1 | 1 | 0.5 | 1 | 1.5 | 1 |

The same weights give both gates. Only the bias differs: it sets how large the sum $x_1 + x_2$ must be.

NOT needs one input: $w = -1$, $b = 0.5$ gives $z = 0.5$ for 0 and $z = -0.5$ for 1.

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_gates.svg" style="display:block;margin:0 auto;width:100%;">

</div>

</div>

<!--
Speaker: these are the truth tables of Lecture 03, now computed by a weighted
sum and a threshold. Let the room check one row of each. In the pictures the
shaded side is where z is positive. (~2 min)
-->

---
hideInToc: true
---

# The Decision Boundary Is a **Line**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## ✏️ **Where the output changes**

The output changes where $z = 0$:

$$
w_1 x_1 + w_2 x_2 + b = 0 \quad\Longrightarrow\quad x_2 = -\frac{w_1}{w_2}\,x_1 - \frac{b}{w_2}
$$

This is a straight line with slope $-w_1 / w_2$.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **$\mathbf{w} = (3, 4)$, $b = -10$**

$x_2 = -0.75\,x_1 + 2.5$. The line meets the axes at $x_2 = 2.5$ and at $x_1 = 3.33$.

On one side $z > 0$ and the output is 1. On the other side $z < 0$ and the output is 0.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_line.svg" style="display:block;margin:0 auto;width:100%;">

</div>

</div>

<!--
Speaker: the neuron cuts the plane in two with a straight line. This is all it
can do, and the last section of the lecture is about a case where one cut is
not enough. (~2 min)
-->

---
hideInToc: true
---

# The Weight Vector Is the **Normal**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## ⊥ **$\mathbf{w}$ is perpendicular to the line**

Take two points $\mathbf{p}$ and $\mathbf{q}$ on the line:

$$
\begin{aligned}
\mathbf{w} \cdot \mathbf{p} + b &= 0 \\
\mathbf{w} \cdot \mathbf{q} + b &= 0 \\
\text{subtract:}\quad \mathbf{w} \cdot (\mathbf{p} - \mathbf{q}) &= 0
\end{aligned}
$$

$\mathbf{p} - \mathbf{q}$ is a direction along the line. Its dot product with $\mathbf{w}$ is zero, so $\mathbf{w}$ is perpendicular to the line.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ➡️ **$\mathbf{w}$ points to the side of class 1**

A step along $\mathbf{w}$ from $\mathbf{x}$ to $\mathbf{x} + t\,\mathbf{w}$ changes $z$ by $t\,\mathbf{w} \cdot \mathbf{w} = t\,\lVert \mathbf{w} \rVert^2$, which is positive.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_line.svg" style="display:block;margin:0 auto;width:100%;">

</div>

</div>

<!--
Speaker: check it on the picture. Along the line, 4 to the right means 3 down:
the direction (4, -3). Its dot product with (3, 4) is 12 - 12 = 0. (~2 min)
-->

---
hideInToc: true
---

# The **Distance** of a Point from the Boundary

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 📏 **Derivation**

Go from the point $\mathbf{x}$ straight to the line, to $\mathbf{x}_0$. The way is along the unit vector $\mathbf{w} / \lVert \mathbf{w} \rVert$, with a length $d$:

$$
\mathbf{x} = \mathbf{x}_0 + d\,\frac{\mathbf{w}}{\lVert \mathbf{w} \rVert}
$$

Take the dot product with $\mathbf{w}$, add $b$, and use $\mathbf{w} \cdot \mathbf{x}_0 + b = 0$:

$$
\mathbf{w} \cdot \mathbf{x} + b = d\,\lVert \mathbf{w} \rVert \quad\Longrightarrow\quad d = \frac{z}{\lVert \mathbf{w} \rVert}
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **$\mathbf{x} = (4, 2)$**

$z = 12 + 8 - 10 = 10$ and $\lVert \mathbf{w} \rVert = \sqrt{9 + 16} = 5$, so $d = 2$. For $(1, 0.5)$: $z = -5$ and $d = -1$, on the other side.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_line.svg" style="display:block;margin:0 auto;width:100%;">

</div>

</div>

<!--
Speaker: z is the distance from the line, in units of the length of w, with a
sign that says which side. The origin has z = b = -10, so it lies 2 from the
line on the side of class 0. (~3 min)
-->

---
hideInToc: true
---

# What $\mathbf{w}$ and $b$ **Do**

<img class="fig" src="/figures/viz_perceptron_wb.svg" style="display:block;margin:0 auto;max-height:245px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

The **direction** of $\mathbf{w}$ sets the direction of the line.

</div>

<div class="card card-secondary card-glass pad-compact">

$b$ shifts the line without turning it. The line lies $\lvert b \rvert / \lVert \mathbf{w} \rVert$ from the origin.

</div>

<div class="card card-accent card-glass pad-compact">

Multiplying $\mathbf{w}$ and $b$ by 2 leaves the line where it is. Every $z$ doubles.

</div>

</div>

<div class="note-text mt-sm">

With $n$ inputs the neuron has $n + 1$ parameters, and the boundary $z = 0$ is a plane or a hyperplane. $\mathbf{w}$ is still its normal and $z / \lVert \mathbf{w} \rVert$ the distance.

</div>

<!--
Speaker: the third panel matters later. The line fixes the weights only up to a
common factor. The step ignores that factor. The sigmoid will not. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Rosenblatt's **Learning Rule**

So far the weights were set by hand. The rule of 1958 finds them from labelled examples, one point at a time.

<!--
Speaker: the section has three parts. The rule and why it moves the line the
right way. One complete run by hand. Then the theorem that says when the run
ends. (~1 min)
-->

---
hideInToc: true
---

# The **Rule**

<div class="card card-info card-glass pad-compact mt-sm">

Take the points one after another. For each point compute $\hat{y}$, then change the weights:

$$
\mathbf{w} \leftarrow \mathbf{w} + \eta\,(y - \hat{y})\,\mathbf{x} \qquad\qquad b \leftarrow b + \eta\,(y - \hat{y})
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔀 **Three cases**

| $y$ | $\hat{y}$ | $y - \hat{y}$ | What happens |
| --- | --- | --- | --- |
| equal | | 0 | nothing |
| 1 | 0 | +1 | $\eta\,\mathbf{x}$ is added to $\mathbf{w}$, $\eta$ to $b$ |
| 0 | 1 | −1 | $\eta\,\mathbf{x}$ is subtracted, $\eta$ from $b$ |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✅ **Why this is the right direction**

Compute $z$ for the same point with the new weights:

$$
\begin{aligned}
z_{\text{new}} &= \bigl(\mathbf{w} + \eta\,(y - \hat{y})\,\mathbf{x}\bigr) \cdot \mathbf{x} + b + \eta\,(y - \hat{y}) \\
&= z + \eta\,(y - \hat{y})\,\bigl(\lVert \mathbf{x} \rVert^2 + 1\bigr)
\end{aligned}
$$

$z$ was too small: it rises. $z$ was too large: it falls.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

One pass through all points is an **epoch**. One update need not make its point right, and it can make another point wrong. The passes are repeated until a whole epoch goes by without an update.

</div>

<!--
Speaker: derive the right card on the board. The bracket is never negative,
so the sign of the change is the sign of y minus y-hat. With eta = 1 and the
point (1, 1) the change of z is 2 + 1 = 3. (~3 min)
-->

---
hideInToc: true
---

# AND by the Rule: Epochs **1 and 2**

<div class="note-text mt-sm">

Start: $\mathbf{w} = (0, 0)$, $b = 0$, $\eta = 1$. Order of the points: (0, 0), (0, 1), (1, 0), (1, 1). Targets: 0, 0, 0, 1.

</div>

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Step | $\mathbf{x}$ | $y$ | $\mathbf{w}$ before | $b$ before | $z$ | $\hat{y}$ | $y - \hat{y}$ | $\mathbf{w}$ after | $b$ after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | (0, 0) | 0 | (0, 0) | 0 | 0 | 0 | 0 | (0, 0) | 0 |
| 2 | (0, 1) | 0 | (0, 0) | 0 | 0 | 0 | 0 | (0, 0) | 0 |
| 3 | (1, 0) | 0 | (0, 0) | 0 | 0 | 0 | 0 | (0, 0) | 0 |
| 4 | (1, 1) | 1 | (0, 0) | 0 | 0 | 0 | **+1** | **(1, 1)** | **1** |
| 5 | (0, 0) | 0 | (1, 1) | 1 | 1 | 1 | **−1** | **(1, 1)** | **0** |
| 6 | (0, 1) | 0 | (1, 1) | 0 | 1 | 1 | **−1** | **(1, 0)** | **−1** |
| 7 | (1, 0) | 0 | (1, 0) | −1 | 0 | 0 | 0 | (1, 0) | −1 |
| 8 | (1, 1) | 1 | (1, 0) | −1 | 0 | 0 | **+1** | **(2, 1)** | **0** |

</div>

<div class="card card-info card-glass pad-compact mt-md">

Step 4 makes (1, 1) right: $z$ goes from 0 to $0 + (2 + 1) = 3$. It also makes the other three points wrong, and epoch 2 has to repair that.

</div>

<!--
Speaker: do steps 1 to 6 on the board with the room, each number said aloud.
With all weights zero the neuron says 0 for everything, so the three points of
class 0 are right by accident. (~4 min)
-->

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

---
hideInToc: true
---

# The Ten Updates as **Lines**

<img class="fig" src="/figures/viz_perceptron_and_run.svg" style="display:block;margin:0 auto;max-height:325px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

Each panel shows the line **after** one update. The red ring marks the point that was wrong and caused it. The shaded side is where $\hat{y} = 1$.

</div>

<div class="card card-warning card-glass pad-compact">

⚠️ In the last panel the point (1, 0) lies exactly on the line: $z = 0$. The rule stops as soon as no point is wrong. It does not look for a line with room to spare.

</div>

</div>

<!--
Speaker: panel 1 has every point on the positive side: the line is outside the
square. Follow the line as it turns and shifts until the corner (1, 1) is alone
on its side. (~2 min)
-->

---
hideInToc: true
---

# The Rule in **Python**

<div class="note-text mt-sm">

`w @ x` is the dot product of two arrays. The output is the table of the last three slides, one line per epoch.

</div>

```py {monaco-run} {autorun:false}
import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])                    # AND
w, b, eta = np.zeros(2), 0.0, 1.0
for epoch in range(1, 7):
    updates = 0
    for x, target in zip(X, y):
        y_hat = int(w @ x + b > 0)            # the neuron
        w = w + eta * (target - y_hat) * x    # the rule
        b = b + eta * (target - y_hat)
        updates += int(y_hat != target)
    print("epoch", epoch, " w", w, " b", b, " updates", updates)
```

<!--
Speaker: run it. Six lines of output, one per epoch: 1, 3, 3, 2, 1 and 0
updates, and at the end w [2. 1.] and b -2.0. Then change y to [0, 1, 1, 1],
which is OR, and run again: four updates, w [1. 1.] and b 0.0. The two lines
marked "the rule" are the formula of the slide The Rule, nothing more. (~3 min)
-->

---
hideInToc: true
---

# Linearly **Separable**

<img class="fig" src="/figures/viz_perceptron_separable.svg" style="display:block;margin:0 auto;max-height:265px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📖 **Definition**

A set of labelled points is **linearly separable** if some $\mathbf{w}$ and $b$ give $z_i > 0$ for every point with $y_i = 1$ and $z_i < 0$ for every point with $y_i = 0$. In the plane: a straight line with all of class 1 on one side and all of class 0 on the other.

</div>

<div class="card card-secondary card-glass pad-compact">

## ↔️ **The margin $\gamma$**

The distance of the closest point from a separating line. For the line on the left it is 0.92. The 200 points on the right are not separable: the best line found leaves 15 on the wrong side.

</div>

</div>

<!--
Speaker: AND and OR are separable. The four points were separated by hand
earlier. The data of this lecture are not: the clouds overlap. The margin
measures how much room a separable set leaves. (~2 min)
-->

---
hideInToc: true
---

# The Perceptron **Convergence Theorem**

<div class="card card-info card-glass pad-compact mt-sm">

Write the bias as a weight on a constant input 1: $\tilde{\mathbf{x}} = (1, x_1, x_2)$ and $\tilde{\mathbf{w}} = (b, w_1, w_2)$ give $z = \tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}}$. Write the targets as signs: $t_i = 2 y_i - 1$ is $+1$ or $-1$.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📜 **Assumed**

1. The training set is finite
2. It is separable with a margin: there is a vector $\tilde{\mathbf{w}}^*$ of length 1 and a number $\gamma > 0$ with $t_i\,(\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{x}}_i) \ge \gamma$ for every point
3. No point is longer than $R$: $\lVert \tilde{\mathbf{x}}_i \rVert \le R$
4. The rule starts from $\tilde{\mathbf{w}} = 0$

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Then**

The rule makes at most

$$
k \le \frac{R^2}{\gamma^2}
$$

updates, in any order of the points and for any $\eta > 0$. After the last update every point is classified correctly.

</div>

</div>

<div class="note-text mt-sm">

Bounded is the number of **updates**. The theorem is silent on sets that are not separable. This form of the bound is due to A. Novikoff, 1962.

</div>

<!--
Speaker: read the four assumptions slowly. The theorem counts mistakes, not
epochs and not seconds. A wide margin and short points give a small bound. The
next three slides are the idea of the proof. (~3 min)
-->

---
hideInToc: true
---

# Proof, Part 1: Each Update Turns $\tilde{\mathbf{w}}$ **Towards $\tilde{\mathbf{w}}^*$**

<div class="card card-info card-glass pad-compact mt-sm">

An update happens only at a point that is wrong, and there $y - \hat{y} = t$. So every update is $\;\tilde{\mathbf{w}} \leftarrow \tilde{\mathbf{w}} + \eta\,t\,\tilde{\mathbf{x}}$.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **One update**

Take the dot product with $\tilde{\mathbf{w}}^*$:

$$
\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}}_{\text{new}} = \tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}} + \eta\,t\,(\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{x}})
$$

By assumption 2 the last bracket times $t$ is at least $\gamma$:

$$
\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}}_{\text{new}} \ge \tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}} + \eta\,\gamma
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **After $k$ updates**

The start is $\tilde{\mathbf{w}} = 0$, and each update adds at least $\eta\,\gamma$:

$$
\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}}_k \ge k\,\eta\,\gamma
$$

The part of $\tilde{\mathbf{w}}$ that points along the solution grows at least in proportion to the number of updates.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**In the AND run**, with $\tilde{\mathbf{w}}^* = (-3, 2, 2) / \sqrt{17}$, $\gamma = 0.243$ and $\eta = 1$: after the first update $\tilde{\mathbf{w}} = (1, 1, 1)$ and $\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}} = 1 / \sqrt{17} = 0.243$. After the tenth $\tilde{\mathbf{w}} = (-2, 2, 1)$ and $\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}} = 12 / \sqrt{17} = 2.91$, above $10\,\gamma = 2.43$.

</div>

<!--
Speaker: check y - y-hat = t for the two wrong cases. Target 1 and output 0
give +1. Target 0 and output 1 give -1. The solution vector w-star is not
known to the rule. It appears only in the proof. (~3 min)
-->

---
hideInToc: true
---

# Proof, Part 2: The Length Grows **Slowly**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **One update**

The squared length after an update:

$$
\lVert \tilde{\mathbf{w}}_{\text{new}} \rVert^2 = \lVert \tilde{\mathbf{w}} \rVert^2 + 2\,\eta\,t\,(\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}}) + \eta^2\,\lVert \tilde{\mathbf{x}} \rVert^2
$$

The point was wrong, so $t\,(\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}}) \le 0$: the middle term is not positive. By assumption 3 the last term is at most $\eta^2 R^2$:

$$
\lVert \tilde{\mathbf{w}}_{\text{new}} \rVert^2 \le \lVert \tilde{\mathbf{w}} \rVert^2 + \eta^2 R^2
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **After $k$ updates**

$$
\lVert \tilde{\mathbf{w}}_k \rVert^2 \le k\,\eta^2 R^2 \quad\Longrightarrow\quad \lVert \tilde{\mathbf{w}}_k \rVert \le \sqrt{k}\;\eta\,R
$$

The length grows at most like $\sqrt{k}$.

**Wrong means $t\,z \le 0$.** A point of class 1 is wrong when $z \le 0$, with $t = 1$. A point of class 0 is wrong when $z > 0$, with $t = -1$.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**In the AND run** the longest point is $(1, 1, 1)$, so $R^2 = 3$. After the first update $\lVert \tilde{\mathbf{w}} \rVert^2 = 3$, equal to the bound $1 \cdot 3$. After the tenth, $\tilde{\mathbf{w}} = (-2, 2, 1)$ has $\lVert \tilde{\mathbf{w}} \rVert^2 = 9$, below $10 \cdot 3 = 30$.

</div>

<!--
Speaker: the first line is (a + b) squared for vectors. The whole proof rests
on the sign of the middle term: the rule changes the weights only when the
point is on the wrong side, and exactly then the term cannot be positive.
(~3 min)
-->

---
hideInToc: true
---

# Proof, Part 3: The Two Bounds **Meet**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 🤝 **Combine**

A dot product is at most the product of the lengths, and $\tilde{\mathbf{w}}^*$ has length 1:

$$
k\,\eta\,\gamma \;\le\; \tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}}_k \;\le\; \lVert \tilde{\mathbf{w}}_k \rVert \;\le\; \sqrt{k}\;\eta\,R
$$

Divide the two ends by $\sqrt{k}\,\eta\,\gamma$:

$$
\sqrt{k} \le \frac{R}{\gamma} \quad\Longrightarrow\quad k \le \frac{R^2}{\gamma^2}
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **For AND**

$\gamma^2 = 1/17$ and $R^2 = 3$: the bound is $3 \cdot 17 = 51$ updates. The run needed 10.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_proof.svg" style="display:block;margin:0 auto;width:100%;">

<div class="note-text mt-sm">

The markers are the ten updates of the run, with $\eta = 1$. They stay between the two bounds.

</div>

</div>

</div>

<!--
Speaker: a quantity that grows like k cannot stay below one that grows like
the square root of k for ever. Where the two curves cross, the updates must
have ended. What is left out: that this w-star has the largest margin of all,
which was found numerically. Any separating w-star gives a valid bound. (~3 min)
-->

---
hideInToc: true
---

# What the Theorem Does **Not** Say

<img class="fig" src="/figures/viz_perceptron_rule_overlap.svg" style="display:block;margin:0 auto;max-height:290px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**Not separable: no end.** On the 200 points the rule makes 16 to 24 updates in every epoch, for 100 epochs.

</div>

<div class="card card-primary card-glass pad-compact">

**No best line.** The rule stops at the first line without errors. Which one depends on the start and the order.

</div>

<div class="card card-secondary card-glass pad-compact">

**No degree of belief.** The output is 0 or 1, as far from the line as next to it.

</div>

</div>

<!--
Speaker: the same rule, the points in a shuffled order, 100 epochs. After each
epoch between 14 and 26 points are on the wrong side, and the line of epoch 98
is not the line of epoch 100. Real data overlap. The next two sections replace
the rule by one that has an answer for this case. (~2 min)
-->

---
layout: section
hideInToc: true
---

# From the Step to the **Sigmoid**

Lecture 10 minimised a loss by following its slope. The step has no slope to follow. A smooth function in its place gives one, and turns the output into a probability.

<!--
Speaker: one change to the neuron, and everything of Lecture 10 becomes
available. (~1 min)
-->

---
hideInToc: true
---

# Gradient Descent Needs a **Slope**

<img class="fig" src="/figures/viz_perceptron_step_loss.svg" style="display:block;margin:0 auto;max-height:300px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**Counting errors.** Lecture 10: $\theta \leftarrow \theta - \eta\,\nabla(\text{loss})$. The number of errors changes only when the line crosses a point. Between the jumps its slope is zero, and a slope of zero gives no direction.

</div>

<div class="card card-success card-glass pad-compact">

**A smooth loss.** The curve on the right is computed on the same 200 points. It has a slope at every $b$, and one lowest point, at $b = -3.99$.

</div>

</div>

<!--
Speaker: both curves are along one parameter, the bias, with the weights fixed
at (2, 2). The left curve is what the step gives. The right curve is where this
section and the next are heading. (~2 min)
-->

---
hideInToc: true
---

# The **Sigmoid**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 〰️ **Definition**

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- Between 0 and 1 for every $z$
- $\sigma(0) = 0.5$
- $\sigma(-z) = 1 - \sigma(z)$
- For large $\lvert z \rvert$ it agrees with the step

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| $z$ | −4 | −2 | −1 | 0 | 1 | 2 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\sigma(z)$ | 0.018 | 0.119 | 0.269 | 0.5 | 0.731 | 0.881 | 0.982 |

</div>

<div class="note-text mt-sm">

In this lecture $\sigma$ is the sigmoid. It is not a standard deviation.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_sigmoid.svg" style="display:block;margin:0 auto;max-height:400px;">

</div>

</div>

<!--
Speaker: compute sigma of 2 on the board: e to the minus 2 is 0.135, and 1
over 1.135 is 0.881. The symmetry gives sigma of minus 2 as 0.119 without a
calculator. (~2 min)
-->

---
hideInToc: true
---

# The Derivative of the **Sigmoid**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Chain rule**

Write $\sigma = u^{-1}$ with $u = 1 + e^{-z}$:

$$
\begin{aligned}
\sigma'(z) &= -u^{-2} \cdot \frac{du}{dz} = -u^{-2} \cdot (-e^{-z}) \\[4pt]
&= \frac{e^{-z}}{(1 + e^{-z})^2} \\[4pt]
&= \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}}
\end{aligned}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **The second factor**

$$
1 - \sigma(z) = \frac{1 + e^{-z} - 1}{1 + e^{-z}} = \frac{e^{-z}}{1 + e^{-z}}
$$

So the derivative needs no exponential of its own:

$$
\sigma'(z) = \sigma(z)\,\bigl(1 - \sigma(z)\bigr)
$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$\sigma'(0) = 0.5 \cdot 0.5 = 0.25$, the largest value. $\sigma'(2) = 0.881 \cdot 0.119 = 0.105$. $\sigma'(4) = 0.018$. The slope is never zero, and it is small where the neuron is sure.

</div>

<!--
Speaker: do it on the board in these four lines. The result is used once, in
the gradient, where it cancels against another factor. (~3 min)
-->

---
hideInToc: true
---

# The Output Is a **Probability**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 🎲 **The model**

$$
\hat{y} = \sigma(\mathbf{w} \cdot \mathbf{x} + b) = P(y = 1 \mid \mathbf{x})
$$

The output is read as the probability that the point belongs to class 1. Class 0 has probability $1 - \hat{y}$.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 📐 **What $z$ means now**

Solve $\hat{y} = 1/(1 + e^{-z})$ for $z$:

$$
z = \ln \frac{\hat{y}}{1 - \hat{y}}
$$

$z$ is the logarithm of the odds. The model says that it is linear in the inputs. $\hat{y} > 0.5$ exactly when $z > 0$: the boundary is the same line as before.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_probmap.svg" style="display:block;margin:0 auto;max-height:400px;">

</div>

</div>

<!--
Speaker: on the line the neuron says 0.5. Since z is the distance times the
length of w, the lines of equal probability are parallel to the boundary. Here
the length of w is 3.08, so the output goes from 0.12 to 0.88 over a distance
of 4 / 3.08 = 1.3. Doubling w and b keeps the line and halves that distance:
with the sigmoid the common factor of the weights matters. Statisticians call
this model logistic regression. (~3 min)
-->

---
hideInToc: true
---

# Where the Sigmoid **Comes From**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 🔔 **Two Gaussian classes**

One input. Class 0 is Gaussian around $\mu_0$, class 1 around $\mu_1$, both of width 1 and equally frequent. Bayes' theorem of Lecture 09:

$$
P(1 \mid x) = \frac{p(x \mid 1)}{p(x \mid 1) + p(x \mid 0)} = \frac{1}{1 + \dfrac{p(x \mid 0)}{p(x \mid 1)}}
$$

The ratio of two Gaussians of equal width is

$$
\frac{p(x \mid 0)}{p(x \mid 1)} = e^{-\frac{(x - \mu_0)^2}{2} + \frac{(x - \mu_1)^2}{2}} = e^{-z}
$$

with $z = (\mu_1 - \mu_0)\,x - \tfrac{1}{2}(\mu_1^2 - \mu_0^2)$.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_posterior.svg" style="display:block;margin:0 auto;max-height:330px;">

<div class="card card-success card-glass pad-compact mt-sm">

The squares of $x$ cancel, so $z$ is linear in $x$ and $P(1 \mid x) = \sigma(z)$ exactly. For $\mu_0 = 0$, $\mu_1 = 2$: $z = 2x - 2$.

</div>

</div>

</div>

<!--
Speaker: the sigmoid is not an arbitrary smooth step. For two Gaussian clouds
of the same width it is the exact answer, with a weight equal to the distance
of the centres. The 200 points of this lecture are such clouds in two
dimensions: there the exact weights are (2, 2) and the bias is -4. (~3 min)
-->

---
layout: section
hideInToc: true
---

# The Loss: From Likelihood to **Cross-Entropy**

Lecture 10 turned the Gaussian likelihood into $\chi^2$. The same three steps, applied to labels that are 0 or 1, give the loss of the logistic neuron and its gradient.

<!--
Speaker: this is the centre of the lecture. Nothing in it is chosen for
convenience: the loss follows from the model, and the gradient follows from the
loss. (~1 min)
-->

---
hideInToc: true
---

# The Likelihood of **One Point**

<div class="card card-info card-glass pad-compact mt-sm">

The recipe of Lecture 10: write the likelihood of the data, take $-\ln$, minimise. For Gaussian errors it gave $\chi^2$. A label is not a number with a Gaussian error. It is one of two outcomes.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **The Bernoulli distribution**

A variable that is 1 with probability $\hat{y}$ and 0 with probability $1 - \hat{y}$. It is the binomial distribution of Lecture 09 with one trial.

Both cases in one formula:

$$
P(y) = \hat{y}^{\,y}\,(1 - \hat{y})^{1 - y}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Check both cases**

- $y = 1$: $\;\hat{y}^1 (1 - \hat{y})^0 = \hat{y}$
- $y = 0$: $\;\hat{y}^0 (1 - \hat{y})^1 = 1 - \hat{y}$

With $\hat{y} = 0.9$: a point of class 1 has probability 0.9, a point of class 0 has 0.1.

</div>

</div>

<div class="note-text mt-sm">

$P(y)$ is the probability that the neuron gives to the label the point really has. A good neuron makes it large for every point.

</div>

<!--
Speaker: the formula looks artificial and is only bookkeeping. Anything to the
power 0 is 1. Ask the room for P when y-hat is 0.2 and the label is 0: 0.8.
(~2 min)
-->

---
hideInToc: true
---

# The Likelihood of **All Points**

<div class="card card-primary card-glass pad-compact mt-sm">

**Step 1.** The points are independent, so the probabilities multiply. The likelihood is written $\mathcal{L}$ here, and $L$ is kept for the loss:

$$
\mathcal{L}(\mathbf{w}, b) = \prod_{i=1}^{N} \hat{y}_i^{\,y_i}\,(1 - \hat{y}_i)^{1 - y_i} \qquad \text{with } \hat{y}_i = \sigma(\mathbf{w} \cdot \mathbf{x}_i + b)
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

**Step 2.** The logarithm turns the product into a sum and the exponents into factors:

$$
-\ln \mathcal{L} = -\sum_{i=1}^{N} \Bigl[\, y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \Bigr]
$$

</div>

<div class="card card-success card-glass pad-compact mt-md">

**The loss** is this sum divided by $N$, the mean over the points. It is called the **cross-entropy**:

$$
L(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^{N} \Bigl[\, y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \Bigr]
$$

</div>

<!--
Speaker: step 3, minimising, takes the rest of the section. Dividing by N
does not move the minimum. It makes the loss of 200
points comparable with the loss of 2000. Of the two terms in the bracket, only
one is non-zero for each point. (~3 min)
-->

---
hideInToc: true
---

# What the Loss **Charges**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **One point**

$$
\ell = \begin{cases} -\ln \hat{y} & \text{if } y = 1 \\ -\ln (1 - \hat{y}) & \text{if } y = 0 \end{cases}
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

## 🔢 **A point of class 1**

| $\hat{y}$ | 0.99 | 0.9 | 0.5 | 0.1 | 0.01 |
| --- | --- | --- | --- | --- | --- |
| $\ell$ | 0.010 | 0.105 | 0.693 | 2.303 | 4.605 |

- Right and sure costs almost nothing
- Undecided costs $\ln 2 = 0.693$
- Wrong and sure costs most, without limit

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_cross_entropy.svg" style="display:block;margin:0 auto;width:100%;">

</div>

</div>

<!--
Speaker: every factor of 10 in the probability given to the true label adds
2.3 to the loss. A neuron that says 0.01 for a point of class 1 has claimed
that such a point occurs once in a hundred. (~2 min)
-->

---
hideInToc: true
---

# The Loss of Four Points, **by Hand**

<div class="note-text mt-sm">

A neuron with $\mathbf{w} = (1, 1)$ and $b = -2$, and four labelled points.

</div>

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| $\mathbf{x}$ | $y$ | $z = x_1 + x_2 - 2$ | $\hat{y} = \sigma(z)$ | $P(y)$ | $\ell = -\ln P(y)$ |
| --- | --- | --- | --- | --- | --- |
| (0, 0.5) | 0 | −1.5 | 0.182 | 0.818 | 0.201 |
| (1, 2) | 1 | 1 | 0.731 | 0.731 | 0.313 |
| (3, 1.5) | 1 | 2.5 | 0.924 | 0.924 | 0.079 |
| (0.5, 1) | 1 | −0.5 | 0.378 | 0.378 | 0.974 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

**Likelihood:** $0.818 \cdot 0.731 \cdot 0.924 \cdot 0.378 = 0.209$

**Loss:** $(0.201 + 0.313 + 0.079 + 0.974) / 4 = 0.392$

Check: $-\ln 0.209 = 1.568 = 4 \cdot 0.392$.

</div>

<div class="card card-info card-glass pad-compact">

The fourth point is on the wrong side of the line, and it alone gives 62 % of the loss. For the first point $P(y)$ is $1 - \hat{y}$, because its label is 0.

</div>

</div>

<!--
Speaker: let the room compute the row of (1, 2): z = 1, sigma of 1 is 0.731
from the table of the sigmoid, minus the logarithm is 0.313. With all weights
zero every y-hat would be 0.5 and the loss ln 2 = 0.693. (~3 min)
-->

---
hideInToc: true
---

# The Gradient, Part 1: The **Chain**

<div class="card card-info card-glass pad-compact mt-sm">

Gradient descent needs $\partial L / \partial w_1$, $\partial L / \partial w_2$ and $\partial L / \partial b$. The loss is a mean over the points, so it is enough to differentiate the loss $\ell$ of one point.

</div>

<div class="card card-primary card-glass pad-compact mt-md">

## 🔗 **Three functions, one inside the other**

$$
w_j \;\longrightarrow\; z = \mathbf{w} \cdot \mathbf{x} + b \;\longrightarrow\; \hat{y} = \sigma(z) \;\longrightarrow\; \ell = -\bigl[\, y \ln \hat{y} + (1 - y) \ln (1 - \hat{y}) \bigr]
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ⛓️ **The chain rule**

$$
\frac{\partial \ell}{\partial w_j} = \frac{\partial \ell}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w_j}
$$

Three factors, each the derivative of one arrow.

</div>

<!--
Speaker: a weight acts on the loss only through z, and z only through y-hat.
The same chain for the bias, with the last factor changed. (~2 min)
-->

---
hideInToc: true
---

# The Gradient, Part 2: The **Three Factors**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **Loss by output**

$$
\begin{aligned}
\frac{\partial \ell}{\partial \hat{y}} &= -\frac{y}{\hat{y}} + \frac{1 - y}{1 - \hat{y}} \\[6pt]
&= \frac{\hat{y} - y}{\hat{y}\,(1 - \hat{y})}
\end{aligned}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Output by sum**

The derivative of the sigmoid:

$$
\frac{\partial \hat{y}}{\partial z} = \hat{y}\,(1 - \hat{y})
$$

</div>

<div class="card card-accent card-glass pad-compact">

## 3️⃣ **Sum by weight**

$z = w_1 x_1 + w_2 x_2 + b$, so

$$
\frac{\partial z}{\partial w_j} = x_j \qquad \frac{\partial z}{\partial b} = 1
$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 🔍 **The first factor, term by term**

$\ell = -y \ln \hat{y} - (1 - y) \ln (1 - \hat{y})$, and the derivative of $\ln u$ is $1/u$.

- The first term gives $-y / \hat{y}$
- The second gives $-(1 - y) \cdot \dfrac{1}{1 - \hat{y}} \cdot (-1)$: the last factor is the derivative of $1 - \hat{y}$
- Over the common denominator the numerator is $-y\,(1 - \hat{y}) + (1 - y)\,\hat{y} = \hat{y} - y$

</div>

<!--
Speaker: the first factor is the only one with work in it. The second was
derived in the last section, and the third is read off the definition of z.
(~3 min)
-->

---
hideInToc: true
---

# The Gradient, Part 3: The **Product**

<div class="card card-primary card-glass pad-compact mt-sm">

Multiply the first two factors. The term $\hat{y}\,(1 - \hat{y})$ cancels:

$$
\frac{\partial \ell}{\partial z} = \frac{\hat{y} - y}{\hat{y}\,(1 - \hat{y})} \cdot \hat{y}\,(1 - \hat{y}) = \hat{y} - y
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🎯 **One point**

$$
\frac{\partial \ell}{\partial \mathbf{w}} = (\hat{y} - y)\,\mathbf{x} \qquad \frac{\partial \ell}{\partial b} = \hat{y} - y
$$

The error times the input.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **All $N$ points**

$$
\frac{\partial L}{\partial \mathbf{w}} = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)\,\mathbf{x}_i \qquad \frac{\partial L}{\partial b} = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)
$$

</div>

</div>

<div class="note-text mt-sm">

$\partial \ell / \partial \mathbf{w}$ is the vector of the derivatives by $w_1$ and $w_2$. With the squared error $\tfrac{1}{2}(\hat{y} - y)^2$ as the loss, the term $\hat{y}\,(1 - \hat{y})$ would not cancel: for $y = 1$ and $\hat{y} = 0.01$ the derivative by $z$ would be $-0.0098$ in place of $-0.99$.

</div>

<!--
Speaker: this is the result of the lecture. No logarithm and no exponential is
left in it. A point that the neuron has right, with y-hat close to y, hardly
moves the weights. A point it has wrong moves them most. (~3 min)
-->

---
hideInToc: true
---

# The Gradient, **Checked with Numbers**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **By the formula**

$\mathbf{w} = (0.5, -0.3)$, $b = 0.1$, one point $\mathbf{x} = (2, 1)$ with $y = 1$.

- $z = 1.0 - 0.3 + 0.1 = 0.8$
- $\hat{y} = \sigma(0.8) = 0.690$
- $\ell = -\ln 0.690 = 0.3711$
- $\hat{y} - y = -0.310$
- $\partial \ell / \partial \mathbf{w} = -0.310 \cdot (2, 1) = (-0.620, -0.310)$
- $\partial \ell / \partial b = -0.310$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔬 **By a small step**

Raise $w_1$ by 0.001 and compute the loss again:

$$
\frac{0.370481 - 0.371101}{0.001} = -0.620
$$

The formula and the difference quotient agree.

**One update with $\eta = 0.5$** gives $\mathbf{w} = (0.810, -0.145)$ and $b = 0.255$. Then $z = 1.730$ and $\hat{y} = 0.849$: the loss has fallen from 0.371 to 0.163.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A derivative worked out on paper is checked this way before it is trusted in a program: change one parameter a little, and compare the change of the loss with the formula.

</div>

<!--
Speaker: the gradient is negative in w1, so raising w1 lowers the loss, and
the update raises it: 0.5 minus 0.5 times -0.620 is 0.810. (~3 min)
-->

---
hideInToc: true
---

# The **Update Rule**

<div class="card card-success card-glass pad-compact mt-sm">

Gradient descent, $\mathbf{w} \leftarrow \mathbf{w} - \eta\,\partial \ell / \partial \mathbf{w}$, with the gradient just derived:

$$
\mathbf{w} \leftarrow \mathbf{w} + \eta\,(y - \hat{y})\,\mathbf{x} \qquad\qquad b \leftarrow b + \eta\,(y - \hat{y})
$$

</div>

<div class="card card-primary card-glass pad-compact mt-md table-compact">

| | **Output $\hat{y}$** | **Loss of one point** | **Update of $\mathbf{w}$** | **Which points move the weights** |
| --- | --- | --- | --- | --- |
| Straight-line fit, Lecture 10 | $\mathbf{w} \cdot \mathbf{x} + b$ | $\tfrac{1}{2}(\hat{y} - y)^2$ | $\eta\,(y - \hat{y})\,\mathbf{x}$ | all, in proportion to the residual |
| Perceptron, Rosenblatt | step of $z$ | none | $\eta\,(y - \hat{y})\,\mathbf{x}$ | only the wrong ones, each by the same amount |
| Logistic neuron | $\sigma(z)$ | cross-entropy | $\eta\,(y - \hat{y})\,\mathbf{x}$ | all, in proportion to the error in probability |

</div>

<div class="card card-info card-glass pad-compact mt-md">

The formula is Rosenblatt's, letter for letter. The difference is in $\hat{y}$: it is now a number between 0 and 1, so $y - \hat{y}$ is never exactly zero and every point pulls on the line.

</div>

<!--
Speaker: the first row is the least-squares line written in today's symbols,
with all errors equal. Its gradient is the residual times the input. Three
models, one update. (~2 min)
-->

---
hideInToc: true
---

# One **Minimum**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## ⌣ **The loss curves upward everywhere**

Differentiate $\partial \ell / \partial z = \hat{y} - y$ once more:

$$
\frac{\partial^2 \ell}{\partial z^2} = \hat{y}\,(1 - \hat{y}) > 0
$$

$z$ is linear in $\mathbf{w}$ and $b$, so the loss is a bowl in the parameters. It has no second valley in which gradient descent could end.

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ **Separable data: no minimum.** On AND the loss falls for as long as the loop runs: 0.035 after 1000 epochs with $\mathbf{w} = (6.0, 6.0)$, 0.0034 after 10 000 with $(10.7, 10.7)$. A larger $\mathbf{w}$ on the same line is always better.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_starts.svg" style="display:block;margin:0 auto;width:100%;">

<div class="note-text mt-sm">

The 200 points, three starting values, $\eta = 0.5$. All three runs end at the same loss, 0.1616.

</div>

</div>

</div>

<!--
Speaker: compare with the fits of Lecture 10 that depended on their starting
values. Here the start changes the way, never the end. The warning is the
third panel of the slide on w and b again: with a sigmoid, scaling the weights
sharpens the output, and on separable data sharper is always better. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Training in **NumPy**

The gradient is a mean over the points, and NumPy computes it for all points in one line. The whole training loop is a dozen lines.

<!--
Speaker: first the notation for all points at once, then the loop, then what
it does to the 200 points. (~1 min)
-->

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
-4.315. Change eta to 0.05 and run again: the loss at epoch 1000 is 0.1809,
not yet at the minimum. (~3 min)
-->

---
hideInToc: true
---

# The Loss **Falls**

<img class="fig" src="/figures/viz_perceptron_loss.svg" style="display:block;margin:0 auto;max-height:300px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Epoch | 0 | 10 | 100 | 200 | 1000 |
| --- | --- | --- | --- | --- | --- |
| Loss | 0.6931 | 0.3356 | 0.1806 | 0.1673 | 0.1616 |
| Correct | 50 % | 88 % | 92.5 % | 92 % | 92.5 % |

</div>

<div class="card card-secondary card-glass pad-compact">

**Why 0.6931 at the start.** With $\mathbf{w} = 0$ and $b = 0$ every $z$ is 0 and every $\hat{y}$ is 0.5. Each point costs $-\ln 0.5 = \ln 2 = 0.6931$.

</div>

</div>

<!--
Speaker: the loss falls at every epoch. The accuracy does not: it is 93.5 % at
epoch 50, 92.5 % at 100 and 92 % at 200. The loop minimises the loss, and the
accuracy only follows it roughly. (~2 min)
-->

---
hideInToc: true
---

# The Boundary **Moves**

<img class="fig" src="/figures/viz_perceptron_training.svg" style="display:block;margin:0 auto;max-height:330px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**After 1 update** the weights are $(0.259, 0.255)$ and the bias is still 0. The direction is nearly right at once. The line passes through the origin, the centre of class 0.

</div>

<div class="card card-secondary card-glass pad-compact">

**From then on** the bias falls, to −1.1 after 20 updates and −4.3 after 1000, and the line moves between the two clouds. The weights grow from 0.26 to 2.1 and 2.3.

</div>

</div>

<!--
Speaker: the first update is eta times the mean of (y - 0.5) x. That is one
eighth of the difference of the two class centres, so the first w already
points from one cloud to the other. The bias starts at zero because the two
classes have equal size. (~2 min)
-->

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

The neuron has recovered the rule that made the data, to within what 200 points allow. No rule can do better than 92.1 % here: the clouds overlap, and a point of class 1 that fell among class 0 cannot be told apart.

</div>

<!--
Speaker: 92.1 % is the probability that a Gaussian value lies less than the
square root of 2 above its mean: the centres are 2.83 apart, the line is half
way, 1.41 from each. The fitted weights differ from the exact ones as a fitted
slope differs from the true one: by the scatter of a finite sample. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Training in **Practice**

The loop works on these 200 points because their inputs are of order 1 and the learning rate suits them. Three things have to be decided for other data: the learning rate, the scale of the inputs, and the points on which the result is judged.

<!--
Speaker: nothing new is derived in this section. It is the same loop under
other conditions, each run and measured. (~1 min)
-->

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

---
hideInToc: true
---

# Inputs on **Different Scales**

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 📏 **The same points in other units**

Multiply $x_2$ by 100, as if metres were written in centimetres. The points and the classes are the same. The loop is not:

- $\eta = 0.5$: the loss is `nan` from the first epoch, and after 1000 epochs 74.5 % are correct
- $\eta = 0.0001$: stable, and after 1000 epochs the loss is 0.477, with 74.5 % correct

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔍 **Why**

$\partial L / \partial w_2$ is a mean of $(\hat{y}_i - y_i)\,x_{i2}$, so it is 100 times larger than before. One $\eta$ serves both weights: it is either too large for $w_2$ or too small for $w_1$ and $b$.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_scaling.svg" style="display:block;margin:0 auto;width:100%;">

<div class="note-text mt-sm">

The red curve is computed in a form that cannot overflow. Its values lie between 4 and 1100.

</div>

</div>

</div>

<!--
Speaker: no physics has changed, only the unit of one column. A method whose
result depends on the unit of a column needs a remedy, and the remedy is on
the next slide. (~2 min)
-->

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

---
hideInToc: true
---

# Train and **Test**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✂️ **Hold some points back**

The task was a rule for points that are not among the examples. So some examples are kept out of the training and used only to judge the result.

- **Training set**: 150 points, drawn at random. The loop sees only these
- **Test set**: the other 50. Used once, at the end
- The mean and standard deviation for standardising come from the training set alone

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐍 **In NumPy**

After the lines that make `X` and `y`:

```python
order = np.random.default_rng(11).permutation(200)
train, test = order[:150], order[150:]
m = X[train].mean(axis=0)
s = X[train].std(axis=0)
Z = (X - m) / s
```

The loop then runs on `Z[train]` and `y[train]`, 1000 epochs.

Measured: 140 of 150 training points correct, 93.3 %, and 46 of 50 test points, 92.0 %.

</div>

</div>

<!--
Speaker: permutation gives the numbers 0 to 199 in a random order, fixed by
the seed. An array of indices in square brackets selects those rows, like the
masks of Lecture 07. A model with three parameters cannot learn 150 points by
heart, so the two accuracies are close. (~3 min)
-->

---
hideInToc: true
---

# How Sure Is an **Accuracy**?

<img class="fig" src="/figures/viz_perceptron_split.svg" style="display:block;margin:0 auto;max-height:300px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**A count has an uncertainty.** Each test point is right or wrong: a binomial count, Lecture 09. With $p = 0.92$ and $N = 50$:

$$
\sqrt{p\,(1 - p) / N} = 0.038
$$

The test accuracy is 92 % ± 4 %.

</div>

<div class="card card-secondary card-glass pad-compact">

**Twenty splits** of the same 200 points, with the seeds 0 to 19, give test accuracies from 88 % to 98 %, with a mean of 93.6 %. The band is the binomial ±3.5 % around that mean. A difference of 2 % between two models on 50 test points says nothing.

</div>

</div>

<!--
Speaker: left, the split of the previous slide: the test points are drawn
large. Right, the same procedure with 20 seeds. An accuracy is a
measurement and is quoted with its uncertainty like any other. To halve the
uncertainty the test set must be four times as large. (~2 min)
-->

---
layout: section
hideInToc: true
---

# The Limit: **XOR**

One neuron draws one line. There is a problem of four points in which no single line is enough, and it can be shown in four lines of algebra.

<!--
Speaker: the last part of the argument. A proof that something is impossible,
then the smallest construction that makes it possible. (~1 min)
-->

---
hideInToc: true
---

# **XOR**

<div class="grid-2 mt-md gap-md">

<div>

<div class="card card-primary card-glass pad-compact table-compact">

## ⊕ **Exclusive or**

| $x_1$ | $x_2$ | AND | OR | XOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

XOR is 1 when exactly one input is 1: when the two inputs differ.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

In the plane the two points of class 1 lie on one diagonal of the square and the two points of class 0 on the other.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_xor_lines.svg" style="display:block;margin:0 auto;max-height:340px;">

<div class="note-text mt-sm">

Each line tried leaves at least one point on the wrong side. That is not yet a proof.

</div>

</div>

</div>

<!--
Speaker: let the room try to draw a line on paper for half a minute. Trying
lines shows nothing: there are infinitely many. The next slide settles it for
all of them at once. (~2 min)
-->

---
hideInToc: true
---

# No Line Exists: The **Four Inequalities**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📝 **What a neuron for XOR must satisfy**

| Point | Target | Needed | Condition |
| --- | --- | --- | --- |
| (0, 0) | 0 | $z \le 0$ | $b \le 0$ |
| (1, 0) | 1 | $z > 0$ | $w_1 + b > 0$ |
| (0, 1) | 1 | $z > 0$ | $w_2 + b > 0$ |
| (1, 1) | 0 | $z \le 0$ | $w_1 + w_2 + b \le 0$ |

</div>

<div class="card card-secondary card-glass pad-compact">

## ➕ **Add them in pairs**

The second and the third:

$$
w_1 + w_2 + 2b > 0
$$

The first and the fourth:

$$
w_1 + w_2 + 2b \le 0
$$

The same quantity would have to be positive and not positive.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

🚧 No numbers $w_1$, $w_2$, $b$ satisfy all four conditions: XOR is not linearly separable. Run on XOR, Rosenblatt's rule repeats the same four updates from epoch 3 on and never stops. The logistic neuron ends at $\mathbf{w} = 0$, $b = 0$: $\hat{y} = 0.5$ for every input, loss $\ln 2$.

</div>

<!--
Speaker: write the four conditions with the room: each is z for that point.
Then add. The result is about every possible line and does not depend on how
the neuron is trained. Both rules behave as their theory says: the theorem
assumed a separable set, and the one minimum of the cross-entropy is here the
neuron that knows nothing. (~3 min)
-->

---
hideInToc: true
---

# Two Lines **Solve It**

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

---
layout: section
hideInToc: true
---

# **History** in Three Dates

The unit of this lecture is nearly seventy years old. Three publications mark what was found, what was shown to be impossible, and what removed the obstacle.

<!--
Speaker: three dates, each with its source. (~1 min)
-->

---
hideInToc: true
---

# Three **Publications**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

## 1958 · **The perceptron**

F. Rosenblatt, *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*, Psychological Review 65, 386–408. A unit with adjustable weights that are found from examples: the rule of the third section.

</div>

<div class="card card-warning card-glass pad-compact">

## 1969 · **The limits**

M. Minsky and S. Papert, *Perceptrons: An Introduction to Computational Geometry*, MIT Press. A mathematical study of what a single layer of such units can and cannot compute. XOR, in general the parity of the inputs, is among the things it cannot.

</div>

<div class="card card-success card-glass pad-compact">

## 1986 · **Training hidden layers**

D. Rumelhart, G. Hinton and R. Williams, *Learning representations by back-propagating errors*, Nature 323, 533–536. Gradient descent for networks with hidden layers of smooth units, by the chain rule.

</div>

</div>

<!--
Speaker: Rosenblatt worked at the Cornell Aeronautical Laboratory. The
convergence bound of this lecture is from 1962, between the first two dates.
Seventeen years lie between the proof of the limit and the method that passed
it. (~2 min)
-->

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

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Compute $z = \mathbf{w} \cdot \mathbf{x} + b$, draw the line $z = 0$, and give the distance $z / \lVert \mathbf{w} \rVert$ of a point from it

</div>

<div class="card card-success card-glass pad-compact">

✅ Run Rosenblatt's rule by hand, and say what the convergence theorem assumes and what it bounds

</div>

<div class="card card-success card-glass pad-compact">

✅ Derive $\sigma' = \sigma\,(1 - \sigma)$, the cross-entropy from the Bernoulli likelihood, and the gradient $(\hat{y} - y)\,\mathbf{x}$

</div>

<div class="card card-success card-glass pad-compact">

✅ Write the training loop in NumPy, standardise the inputs, and quote a test accuracy with its uncertainty

</div>

<div class="card card-success card-glass pad-compact">

✅ Prove from four inequalities that one neuron cannot compute XOR

</div>

<div class="card card-success card-glass pad-compact">

✅ Build XOR from three neurons and check it for all four inputs

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🧭 **The numbers of this lecture**

AND: 10 updates, $\mathbf{w} = (2, 1)$, $b = -2$, against a bound of 51. The 200 points: loss from 0.6931 to 0.1616, 92.5 % correct, where the best possible is 92.1 % on average. XOR: weights $(1, 1)$ with biases $-0.5$ and $-1.5$, then $(1, -1)$ with $-0.5$.

</div>

<!--
Speaker: one neuron, fully understood: its geometry, two ways to train it,
where the second way comes from, and its limit. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="A neuron with a step has weights w = (2, −3) and bias b = 1. What are z and the output for the input x = (1, 2)?"
  :options="[
    'z = 9, output 1',
    'z = −3, output 0',
    'z = −4, output 0',
    'z = 3, output 1'
  ]"
  :correct="1"
  explanation="z = 2 · 1 + (−3) · 2 + 1 = 2 − 6 + 1 = −3. The step gives 1 only for z > 0, so the output is 0. Forgetting the bias gives −4."
/>

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

---
hideInToc: true
---

<MCQ
  question="Rosenblatt's rule with learning rate 1. The weights are w = (1, −1), b = 0. The next point is x = (0, 1) with target 1. What are the weights after this step?"
  :options="[
    'w = (1, −1), b = 0: the point is already right',
    'w = (1, −2), b = −1',
    'w = (1, 0), b = 0',
    'w = (1, 0), b = 1'
  ]"
  :correct="3"
  explanation="z = 1 · 0 + (−1) · 1 + 0 = −1, so the output is 0 and the target is 1: y − ŷ = +1. The rule adds x to w and 1 to b: w = (1, 0), b = 1. For the same point z is now 1."
/>

---
hideInToc: true
---

<MCQ
  question="A logistic neuron gives ŷ = 0.8 for a point whose label is 0. What is the cross-entropy loss of this point?"
  :options="[
    '1.609',
    '0.223',
    '0.8',
    '0.64'
  ]"
  :correct="0"
  explanation="For y = 0 the loss is −ln(1 − ŷ) = −ln 0.2 = 1.609. The value 0.223 is −ln 0.8, the loss if the label were 1. The neuron gave the true label a probability of 0.2."
/>

---
hideInToc: true
---

<MCQ
  question="For one point x = (2, −1) with label 1, a logistic neuron gives ŷ = 0.3. What is the gradient of the loss with respect to the weights?"
  :options="[
    '(1.4, −0.7)',
    '(0.6, −0.3)',
    '(−1.4, 0.7)',
    '(−0.7, −0.7)'
  ]"
  :correct="2"
  explanation="The gradient is (ŷ − y) x = (0.3 − 1) · (2, −1) = (−1.4, 0.7), and −0.7 with respect to the bias. Gradient descent subtracts it, so w1 rises and w2 falls, and z for this point rises."
/>

---
hideInToc: true
---

<MCQ
  question="XNOR is 1 when the two inputs are equal: for (0, 0) and (1, 1). Can a single neuron compute it?"
  :options="[
    'Yes, with negative weights',
    'No: it is XOR with the two classes exchanged, and the same four inequalities contradict each other',
    'Yes, if it is trained for enough epochs',
    'Only with a sigmoid in place of the step'
  ]"
  :correct="1"
  explanation="The conditions are b > 0, w1 + b ≤ 0, w2 + b ≤ 0 and w1 + w2 + b > 0. The middle two add to w1 + w2 + 2b ≤ 0, the outer two to w1 + w2 + 2b > 0. No weights exist, whatever the training and whatever the function after the sum."
/>
