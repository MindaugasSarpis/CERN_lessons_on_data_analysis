---
layout: cover
title: "Machine Learning & AI"
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

## Machine Learning & AI

##### <span class="aims-badge">🔧 tool-agnostic · ♻️ reproducibility</span>

<!--
Speaker: this lecture continues Lecture 11. That lecture ended with a network
of three neurons whose nine numbers were set by hand. Today the numbers are
found by gradient descent, and then the result is measured. (~1 min)
-->

---
layout: quote
hideInToc: true
---

# “The procedure repeatedly adjusts the weights of the connections in the network so as to **minimize a measure of the difference** between the actual output vector of the net and the desired output vector.”

Rumelhart, Hinton and Williams, *Learning representations by back-propagating errors*, Nature 323 (1986)

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧮 Write the **forward pass** of a network with one hidden layer and count its parameters

</div>

<div class="card card-secondary card-glass pad-compact">

🔗 Derive **backpropagation** for one hidden layer by the chain rule, and check a derivative with numbers

</div>

<div class="card card-accent card-glass pad-compact">

🏋️ Train a small network in NumPy, and explain why a run can fail

</div>

<div class="card card-success card-glass pad-compact">

🔒 Use **training, validation and test** rows for their three jobs, and recognise overfitting and leakage

</div>

<div class="card card-info card-glass pad-compact">

📊 Compute **accuracy, precision, recall** and the area under the ROC curve from counts

</div>

<div class="card card-warning card-glass pad-compact">

🧠 Say what a **large language model** computes, and what to verify, to disclose and to keep out of it

</div>

</div>

<!--
Speaker: the first half is one derivation and one training run. The second
half is how any trained model is measured. The last part applies both to the
language models everyone uses. (~1 min)
-->

---
hideInToc: true
---

# Where Lecture 11 **Stopped**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧠 **One neuron, trained**

- $z = \mathbf{w} \cdot \mathbf{x} + b$ and $\hat{y} = \sigma(z)$
- Loss: $L = -\bigl[\,y \ln \hat{y} + (1 - y) \ln (1 - \hat{y})\,\bigr]$
- Gradient: $\dfrac{\partial L}{\partial \mathbf{w}} = (\hat{y} - y)\,\mathbf{x}$ and $\dfrac{\partial L}{\partial b} = \hat{y} - y$
- Update: $\mathbf{w} \leftarrow \mathbf{w} - \eta\,\dfrac{\partial L}{\partial \mathbf{w}}$

</div>

<div class="card card-secondary card-glass pad-compact">

## ✋ **XOR, with nine numbers set by hand**

- $h_1$: weights (1, 1), bias −0.5. It computes OR
- $h_2$: weights (1, 1), bias −1.5. It computes AND
- Output: weights (1, −1), bias −0.5, on $h_1$ and $h_2$
- One neuron cannot compute XOR. These three can

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

For data, nobody can set the weights by hand. This lecture finds them by gradient descent. That needs the derivative of the loss with respect to a weight of the hidden layer. Then the network is trained on XOR and on a file of 600 rows, and the result is measured on rows it has not seen.

</div>

<!--
Speaker: everything on the left was derived in Lecture 11 and is used today
without a new derivation. The right card is the network of its last section.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# From One Neuron to a **Network**

The forward pass of a network with one hidden layer, in symbols and in numbers.

---
hideInToc: true
---

# A Hidden Layer of **Sigmoid Neurons**

<div class="grid-2 mt-sm gap-md">

<img class="fig" src="/figures/viz_ml_network.svg" style="display:block;margin:0 auto;max-height:215px;">

<div class="card card-primary card-glass pad-compact">

## ➡️ **The forward pass**

$$
u_j = v_{j1}\,x_1 + v_{j2}\,x_2 + c_j \qquad h_j = \sigma(u_j)
$$

$$
z = w_1 h_1 + w_2 h_2 + b \qquad \hat{y} = \sigma(z)
$$

Nine parameters: 6 in the hidden layer, 3 in the output neuron. A layer of $m$ neurons with $n$ inputs has $m \cdot n$ weights and $m$ biases.

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

**Every unit is a sigmoid neuron.** The step of the hand-set network is gone, so every unit has a slope. The output neuron is the neuron of Lecture 11 with $h_1$, $h_2$ as its inputs. It keeps the letters $w$, $b$ and $z$.

</div>

<div class="card card-info card-glass pad-compact">

**The hidden layer gets its own letters.** $v_{ji}$ is the weight to hidden unit $j$ from input $i$, $c_j$ its bias, $u_j$ its weighted sum. In the code of Lecture 11 these arrays were `W1`, `b1`, `w2`, `b2`. Here they are `V`, `c`, `w`, `b`.

</div>

</div>

<!--
Speaker: nine symbols for nine numbers. The index j counts hidden units, the
index i counts inputs. The loss is unchanged: the cross-entropy of y hat and y.
Let the room count a 2-3-1 network with the rule: 9 plus 4 is 13. (~3 min)
-->

---
hideInToc: true
---

# The Forward Pass **by Hand**

<div class="card card-secondary card-glass pad-compact mt-sm">

```text
hidden unit 1:  v1 = ( 0.5, -0.3)   c1 = 0.1        output:  w = (0.7, -0.6)   b = 0.1
hidden unit 2:  v2 = (-0.4,  0.8)   c2 = 0.2        point:   x = (1, 0)        y = 1
```

</div>

<div class="card card-primary card-glass pad-compact mt-md">

## 🔢 **Layer by layer**

```text
u1 =  0.5 · 1 - 0.3 · 0 + 0.1 =  0.6        h1 = σ( 0.6) = 0.6457
u2 = -0.4 · 1 + 0.8 · 0 + 0.2 = -0.2        h2 = σ(-0.2) = 0.4502
z  =  0.7 · 0.6457 - 0.6 · 0.4502 + 0.1 = 0.2819
ŷ  =  σ(0.2819) = 0.570
L  = -ln 0.570  = 0.562
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

The target is 1 and the output is 0.570. For a point with $y = 1$ the loss is $-\ln \hat{y}$, here 0.562. These nine weights and this one point are used until the end of the next section.

</div>

<!--
Speaker: the weights are round numbers chosen for the arithmetic, not trained
ones. Sigma of 0.6 is 1 over 1 plus e to the minus 0.6. (~3 min)
-->

---
hideInToc: true
---

# Without the Sigmoid, Two Layers Are **One**

<div class="card card-primary card-glass pad-compact mt-sm">

## ➖ **Leave the sigmoid out of the hidden layer**

Then $h_j = u_j$, and the weighted sum of the output neuron is

$$
z = w_1 u_1 + w_2 u_2 + b = (w_1 v_{11} + w_2 v_{21})\,x_1 + (w_1 v_{12} + w_2 v_{22})\,x_2 + (w_1 c_1 + w_2 c_2 + b)
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **With the weights of the last slide**

```text
0.7 · 0.5    - 0.6 · (-0.4) =  0.59
0.7 · (-0.3) - 0.6 · 0.8    = -0.69
0.7 · 0.1    - 0.6 · 0.2 + 0.1 = 0.05
```

$z = 0.59\,x_1 - 0.69\,x_2 + 0.05$

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **One neuron again**

A weighted sum of weighted sums is a weighted sum. Three neurons have collapsed into one with the weights (0.59, −0.69) and the bias 0.05, and one neuron cannot compute XOR.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The function between two layers must not be a straight line. The sigmoid is one choice. $\max(0, z)$ is another.

</div>

<!--
Speaker: this is why the function after the sum matters. A network of any
depth without it draws one line. (~2 min)
-->

---
layout: section
hideInToc: true
---

# **Backpropagation**

The derivative of the loss with respect to every weight of the network, by the chain rule.

---
hideInToc: true
---

# Nine **Derivatives**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⬇️ **One derivative per parameter**

Gradient descent changes each parameter $\theta$ against the slope of the loss:

$$
\theta \leftarrow \theta - \eta\,\frac{\partial L}{\partial \theta}
$$

Here $\theta$ is each of $v_{11}, v_{12}, v_{21}, v_{22}, c_1, c_2, w_1, w_2, b$.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Three are known**

The output neuron is the neuron of Lecture 11 with the inputs $h_j$:

$$
\frac{\partial L}{\partial w_j} = (\hat{y} - y)\,h_j \qquad \frac{\partial L}{\partial b} = \hat{y} - y
$$

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

## ❓ **Six are missing**

$v_{11}$ does not appear in the loss. The loss depends on it through a chain: $v_{11} \to u_1 \to h_1 \to z \to \hat{y} \to L$. A change of $v_{11}$ changes $u_1$, that changes $h_1$, and so on to the loss.

</div>

<!--
Speaker: point at the chain on the network drawing two slides back. Each arrow
is one function, and each function has a derivative that is already known.
(~2 min)
-->

---
hideInToc: true
---

# The Chain **Rule**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔗 **Two functions in a row**

If $f$ depends on $a$, and $a$ depends on $t$:

$$
\frac{df}{dt} = \frac{df}{da} \cdot \frac{da}{dt}
$$

Example: $f = a^2$ with $a = 3t + 1$. At $t = 1$: $a = 4$, $\frac{df}{da} = 2a = 8$, $\frac{da}{dt} = 3$. So $\frac{df}{dt} = 24$.

Check: $f(1.001) = 4.003^2 = 16.024009$. The slope is $0.024009 / 0.001 = 24.009$.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📉 **The slope of the sigmoid**

From Lecture 11, with $h = \sigma(u)$: $\;\sigma'(u) = h\,(1 - h)$

| $h$ | $h\,(1 - h)$ |
| --- | --- |
| 0.5 | 0.25 |
| 0.9 | 0.09 |
| 0.99 | 0.0099 |
| 0.999 | 0.000999 |

A unit with $h$ close to 0 or 1 is **saturated**: its slope is nearly zero.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Lecture 11 applied the chain rule through one neuron. A network needs one more factor for every layer between a weight and the loss.

</div>

<!--
Speaker: the two tools of this section. The numeric check of the example is
the same check that is applied to the network six slides on. (~3 min)
-->

---
hideInToc: true
---

# Step 1: The Error at the **Output**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 1️⃣ **From $L$ to $z$**

Lecture 11 multiplied $\partial L / \partial \hat{y}$ by $\partial \hat{y} / \partial z$ and found

$$
\delta = \frac{\partial L}{\partial z} = \hat{y} - y
$$

$\delta$ is the **error** of the output neuron. Since $z = w_1 h_1 + w_2 h_2 + b$:

$$
\frac{\partial L}{\partial w_j} = \delta\,h_j \qquad \frac{\partial L}{\partial b} = \delta
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **With the numbers**

```text
δ      = 0.570 - 1       = -0.430
∂L/∂w1 = -0.430 · 0.6457 = -0.278
∂L/∂w2 = -0.430 · 0.4502 = -0.194
∂L/∂b  =                   -0.430
```

All three are negative. Raising $w_1$, $w_2$ or $b$ raises the output, which is below its target, and so lowers the loss.

</div>

</div>

<img class="fig" src="/figures/viz_ml_backprop_step1.svg" style="display:block;margin:0.8rem auto 0;max-height:150px;">

<!--
Speaker: nothing new yet. This is the result of Lecture 11 with h in the place
of x. The letter delta is new: it is the quantity that will be passed back.
(~2 min)
-->

---
hideInToc: true
---

# Step 2: Back to the **Hidden Outputs**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 2️⃣ **From $z$ to $h_j$**

$z = w_1 h_1 + w_2 h_2 + b$, so $\partial z / \partial h_j = w_j$. By the chain rule:

$$
\frac{\partial L}{\partial h_j} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial h_j} = \delta\,w_j
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **With the numbers**

```text
∂L/∂h1 = -0.430 ·   0.7  = -0.301
∂L/∂h2 = -0.430 · (-0.6) = +0.258
```

A larger $h_1$ would lower the loss. A larger $h_2$ would raise it, because $w_2$ is negative.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The error $\delta$ goes back along each connection and is multiplied by the weight of that connection. This step gives the method its name: **backpropagation** of the error.

</div>

<img class="fig" src="/figures/viz_ml_backprop_step2.svg" style="display:block;margin:0.8rem auto 0;max-height:165px;">

<!--
Speaker: h is not a parameter, so nothing is updated here. The derivative with
respect to h is an intermediate result, needed for the next step. (~2 min)
-->

---
hideInToc: true
---

# Step 3: Through the **Sigmoid**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 3️⃣ **From $h_j$ to $u_j$**

$h_j = \sigma(u_j)$, so $\partial h_j / \partial u_j = h_j\,(1 - h_j)$. One more factor:

$$
\delta_j = \frac{\partial L}{\partial u_j} = \delta\,w_j\,h_j\,(1 - h_j)
$$

$\delta_j$ is the error of hidden unit $j$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **With the numbers**

```text
h1 (1 - h1) = 0.6457 · 0.3543 = 0.2288
h2 (1 - h2) = 0.4502 · 0.5498 = 0.2475
δ1 = -0.301 · 0.2288 = -0.0689
δ2 = +0.258 · 0.2475 = +0.0639
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The factor $h_j\,(1 - h_j)$ is at most 0.25. A saturated hidden unit, with $h_j$ near 0 or 1, passes almost no error back. This matters in the training runs of the next section.

</div>

<img class="fig" src="/figures/viz_ml_backprop_step3.svg" style="display:block;margin:0.8rem auto 0;max-height:160px;">

<!--
Speaker: the target of the output was given by the data. The error of a hidden
unit is computed from the output error: this is what Rosenblatt's rule could
not supply. (~2 min)
-->

---
hideInToc: true
---

# Step 4: The Hidden **Weights**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 4️⃣ **From $u_j$ to $v_{ji}$ and $c_j$**

$u_j = v_{j1}\,x_1 + v_{j2}\,x_2 + c_j$, so $\partial u_j / \partial v_{ji} = x_i$ and $\partial u_j / \partial c_j = 1$:

$$
\frac{\partial L}{\partial v_{ji}} = \delta_j\,x_i \qquad \frac{\partial L}{\partial c_j} = \delta_j
$$

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **With $\mathbf{x} = (1, 0)$**

| | weight on $x_1$ | weight on $x_2$ | bias |
| --- | --- | --- | --- |
| unit 1 | −0.0689 | 0 | −0.0689 |
| unit 2 | +0.0639 | 0 | +0.0639 |

The weights on $x_2$ get no change from this point. $x_2 = 0$ took no part in the output.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

The form is the one of Lecture 11: **the error of a unit times the input of the weight**. For the output neuron that is $\delta\,h_j$. For hidden unit $j$ it is $\delta_j\,x_i$.

</div>

<img class="fig" src="/figures/viz_ml_backprop_step4.svg" style="display:block;margin:0.8rem auto 0;max-height:150px;">

<!--
Speaker: six derivatives from two numbers, delta 1 and delta 2. With these six
and the three of step 1 all nine are known. (~2 min)
-->

---
hideInToc: true
---

# The Whole Pass, **Forward and Backward**

<img class="fig" src="/figures/viz_ml_backprop.svg" style="display:block;margin:0 auto;max-height:205px;">

<div class="card card-primary card-glass pad-compact mt-md table-compact">

| | Forward: the values | | Backward: the derivatives |
| --- | --- | --- | --- |
| 1 | $u_j = v_{j1}\,x_1 + v_{j2}\,x_2 + c_j$ | 5 | $\delta = \hat{y} - y$ |
| 2 | $h_j = \sigma(u_j)$ | 6 | $\partial L / \partial w_j = \delta\,h_j$ and $\partial L / \partial b = \delta$ |
| 3 | $z = w_1 h_1 + w_2 h_2 + b$ | 7 | $\delta_j = \delta\,w_j\,h_j\,(1 - h_j)$ |
| 4 | $\hat{y} = \sigma(z)$ | 8 | $\partial L / \partial v_{ji} = \delta_j\,x_i$ and $\partial L / \partial c_j = \delta_j$ |

</div>

<div class="note-text mt-sm">

The backward pass uses the values of the forward pass, $h_j$ and $\hat{y}$. These eight lines are the whole method for one hidden layer.

</div>

<!--
Speaker: blue numbers above each circle are the forward values, orange numbers
below are the derivatives of the loss with respect to that quantity. Read the
figure once from left to right and once from right to left. (~3 min)
-->

---
hideInToc: true
---

# The Check: Nudge One **Weight**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔬 **A derivative is a slope**

Set $v_{11}$ to 0.501 and to 0.499 and run the forward pass twice:

```text
v11 = 0.501    L = 0.5620463
v11 = 0.499    L = 0.5621841
slope = -0.0001378 / 0.002 = -0.0689
```

| Parameter | Slope from two passes | Backpropagation |
| --- | --- | --- |
| $v_{11}$ | −0.0689 | −0.0689 |
| $w_2$ | −0.1936 | −0.1936 |
| $c_2$ | +0.0639 | +0.0639 |

</div>

<div class="card card-secondary card-glass pad-compact">

## ⏱️ **What each way costs**

- By nudging: two forward passes for each parameter. That is 18 passes for 9 parameters and 2 000 000 passes for a million
- By backpropagation: one forward and one backward pass for all parameters, whatever their number

The nudge tests the code. Backpropagation trains the network.

</div>

</div>

<!--
Speaker: Lecture 11 checked its gradient in the same way. A new derivation
always gets this check before it is trusted. (~3 min)
-->

---
hideInToc: true
---

# One Step of **Gradient Descent**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Parameter | Before | Derivative | After, $\eta = 1$ |
| --- | --- | --- | --- |
| $v_{11}$ | 0.5 | −0.0689 | 0.5689 |
| $v_{12}$ | −0.3 | 0 | −0.3 |
| $c_1$ | 0.1 | −0.0689 | 0.1689 |
| $v_{21}$ | −0.4 | +0.0639 | −0.4639 |
| $v_{22}$ | 0.8 | 0 | 0.8 |
| $c_2$ | 0.2 | +0.0639 | 0.1361 |
| $w_1$ | 0.7 | −0.2776 | 0.9776 |
| $w_2$ | −0.6 | −0.1936 | −0.4064 |
| $b$ | 0.1 | −0.4300 | 0.5300 |

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## 📉 **The forward pass again**

With the new weights the output for the same point is 0.735, up from 0.570. The loss is 0.308, down from 0.562.

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every parameter moved against its own derivative, by $\eta$ times its size. This was one step for one point. Training does it for all points, thousands of times.

</div>

</div>

</div>

<!--
Speaker: after = before minus eta times derivative, row by row. Ask which
parameter moved most and why: b, because its input is always 1. (~2 min)
-->

---
hideInToc: true
---

# All Points at Once, in **NumPy**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Line of the loop | Formula | Shape, $N$ points and $H$ hidden units |
| --- | --- | --- |
| `h = sigma(X @ V.T + c)` | $h_j = \sigma(v_{j1}\,x_1 + v_{j2}\,x_2 + c_j)$ | $N \times H$ |
| `y_hat = sigma(h @ w + b)` | $\hat{y} = \sigma(w_1 h_1 + \dots + w_H h_H + b)$ | $N$ |
| `d = (y_hat - y) / len(y)` | $\delta = \hat{y} - y$, divided by $N$ | $N$ |
| `dh = np.outer(d, w) * h * (1 - h)` | $\delta_j = \delta\,w_j\,h_j\,(1 - h_j)$ | $N \times H$ |
| `w = w - eta * h.T @ d` | $w_j \leftarrow w_j - \eta \sum \delta\,h_j$ | $H$ |
| `V = V - eta * dh.T @ X` | $v_{ji} \leftarrow v_{ji} - \eta \sum \delta_j\,x_i$ | $H \times 2$ |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

**The loss of a dataset** is the mean of the losses of its points, as in Lecture 11. Its gradient is the mean of the gradients of the points. That is the division by $N$ in the third line, and the sums run over the points.

</div>

<div class="card card-info card-glass pad-compact">

`V` has one row per hidden unit. `np.outer(d, w)` is the table of all products $\delta \cdot w_j$: one row per point, one column per hidden unit. The biases are updated with `d.sum()` and `dh.sum(axis=0)`.

</div>

</div>

<!--
Speaker: six lines for the eight lines of the summary slide. X.T and @ were
read in Lecture 11: X.T @ something is a sum over the points. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Training on **XOR**

The nine numbers that Lecture 11 set by hand, found by gradient descent.

---
hideInToc: true
---

# The Training Loop in **NumPy**

```py {monaco-run} {autorun:false, outputHeight:'4.8rem'}
import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
def sigma(z):
    return 1 / (1 + np.exp(-z))
rng = np.random.default_rng(0)                   # the seed
V, c = rng.normal(0, 1, (2, 2)), np.zeros(2)     # hidden layer
w, b, eta = rng.normal(0, 1, 2), 0.0, 1.0        # output neuron
for epoch in range(5001):
    h = sigma(X @ V.T + c)                       # forward
    y_hat = sigma(h @ w + b)
    if epoch % 1000 == 0:
        loss = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        print(epoch, round(loss, 4), y_hat.round(3))
    d = (y_hat - y) / 4                          # backward
    dh = np.outer(d, w) * h * (1 - h)
    w, b = w - eta * h.T @ d, b - eta * d.sum()  # update
    V, c = V - eta * dh.T @ X, c - eta * dh.sum(axis=0)
```

<!--
Speaker: run it. Six lines appear: the epoch, the loss, the four outputs.
Measured: 0.6935 at epoch 0, 0.0219 at 1000, 0.0021 at 5000, with the outputs
0.003 0.998 0.998 0.002. The weights start as random numbers with mean 0 and
standard deviation 1, the biases at 0. The seed fixes the random numbers, so
that every run gives these values. (~4 min)
-->

---
hideInToc: true
---

# The Loss and the Four **Outputs**

<img class="fig" src="/figures/viz_ml_xor_training.svg" style="display:block;margin:0 auto;max-height:240px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

```text
epoch   loss     (0,0)  (0,1)  (1,0)  (1,1)
    0   0.6935   0.478  0.485  0.488  0.495
 1000   0.0219   0.025  0.980  0.980  0.022
 5000   0.0021   0.003  0.998  0.998  0.002
```

</div>

<div class="card card-info card-glass pad-compact">

The loss starts at $\ln 2 = 0.693$, the loss of four outputs of 0.5. After 300 epochs it is still 0.666. Then the two hidden units take different lines: 0.339 after 500 epochs, 0.022 after 1000.

</div>

</div>

<!--
Speaker: the flat start is typical. While both hidden units give nearly the
same value for all four points, the output neuron has nothing to work with.
(~2 min)
-->

---
hideInToc: true
---

# What the Network **Found**

<img class="fig" src="/figures/viz_ml_xor_learned.svg" style="display:block;margin:0 auto;max-height:265px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Seed 0 | Weights | Bias | High for |
| --- | --- | --- | --- |
| $h_1$ | (5.77, 5.77) | −8.82 | (1, 1) only: AND |
| $h_2$ | (7.57, 7.56) | −3.48 | all but (0, 0): OR |
| output | (−14.22, 13.42) | −6.30 | $h_2$ and not $h_1$ |

</div>

<div class="card card-success card-glass pad-compact">

The run found the split that was set by hand, OR and AND, with the units in the other order. Its lines are $x_1 + x_2 = 1.53$ and $0.46$; by hand they were 1.5 and 0.5. Seed 2 ends elsewhere: one unit is high for (0, 1) only, the other for (1, 0) only. Both networks compute XOR. The weights that solve a problem are not unique.

</div>

</div>

<!--
Speaker: left panel, the two hidden units as lines in the plane of the inputs.
Right panel, where the four points land in the plane of h1 and h2, and the
line of the output neuron. The picture of Lecture 11, now with trained weights.
(~3 min)
-->

---
hideInToc: true
---

# Not Every Run **Succeeds**

<img class="fig" src="/figures/viz_ml_xor_seeds.svg" style="display:block;margin:0 auto;max-height:235px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Network | Seeds 0 to 99 with a loss below 0.01 after 5000 epochs |
| --- | --- |
| 2-2-1 | 70 |
| 2-3-1 | 96 |
| 2-4-1 | 99 |

</div>

<div class="card card-warning card-glass pad-compact">

Of the 30 runs of the 2-2-1 network that fail, 27 end at a loss near 0.35 and 3 near 0.48. After 20 000 epochs one more seed has succeeded. The other 29 have not moved. Seed 1 is still at 0.347 after 200 000 epochs.

</div>

</div>

<!--
Speaker: same code, same data, same learning rate. Only the starting weights
differ. Three runs in ten end with a network that does not compute XOR, and
more epochs do not help. (~2 min)
-->

---
hideInToc: true
---

# Why a Run Gets **Stuck**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🧱 **Seed 1 after 5000 epochs**

| Input | $h_1$ | $h_2$ | $\hat{y}$ | $y$ |
| --- | --- | --- | --- | --- |
| (0, 0) | 0.118 | 0.036 | 0.002 | 0 |
| (0, 1) | 1.000 | 0.000 | 0.499 | 1 |
| (1, 0) | 0.969 | 0.840 | 0.999 | 1 |
| (1, 1) | 1.000 | 0.000 | 0.501 | 0 |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Read it with the four steps**

- (0, 1) and (1, 1) have the same hidden values. The output neuron cannot tell them apart and gives both 0.5
- Their errors are −0.5 and +0.5 at the same $h$. In $\sum \delta\,h_j$ they cancel
- Both hidden units are saturated for these two points: $h_j\,(1 - h_j) = 0$, and no error reaches the hidden weights

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

All nine derivatives are zero to three decimals, and the loss stays near $(\ln 2 + \ln 2)/4 = 0.347$. The loss of one neuron has one minimum (Lecture 11). The loss of a network has flat regions where the gradient vanishes and the loss is not at its lowest. Gradient descent stops wherever the gradient is zero.

</div>

<!--
Speaker: step 3 of the derivation predicted this. The factor h times 1 minus h
is the gate through which the error has to pass. (~3 min)
-->

---
hideInToc: true
---

# What **Helps**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **Several starts, more units**

- Run several seeds and keep the run with the lowest loss
- Add hidden units. 96 of 100 seeds succeed with three units and 99 with four: a spare unit can take the line that a saturated unit has lost
- State the seed with the result. A run that cannot be repeated cannot be checked

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚖️ **Why the start is random**

- All weights 0: every derivative is 0, and the loss stays at 0.693
- All weights 0.5: both hidden units get the same derivatives in every epoch and stay equal. After 5000 epochs both have the weights (8.225, 8.225). The outputs are 0.003, 0.666, 0.666, 0.667 and the loss is 0.479
- Two equal units draw one line. Random starting values make the units differ

</div>

</div>

<!--
Speaker: both runs on the right were computed with the loop of this section
and other starting values. The second one ends where three of the hundred
seeds ended. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Train, Validation, **Test**

XOR has four points, and all four were used for training. Data has rows the model has not seen.

---
hideInToc: true
---

# A Two-Class **File**

<div class="grid-2 mt-sm gap-md">

<img class="fig" src="/figures/viz_ml_two_class.svg" style="display:block;margin:0 auto;max-height:390px;">

<div>

<div class="card card-primary card-glass pad-compact">

## 📄 **`ml_two_class.csv`**

```text
x1,x2,label
6.974,28.38,0
5.062,14.85,0
...
```

600 rows: two measured quantities and a label, 300 rows of each class. The data are simulated with a fixed seed. Class 1 is a cloud, class 0 a ring around it, and they overlap where they meet.

</div>

<div class="card card-warning card-glass pad-compact mt-md">

No straight line separates a cloud from the ring around it. The neuron of Lecture 11, trained on this file, is right for 65 % of its training rows. A guess is right for 50 %.

</div>

</div>

</div>

<!--
Speaker: the file and the script that makes it are on the page of this lecture
in the workbook. x1 is near 5 and x2 near 30: the two columns have different
scales. (~2 min)
-->

---
hideInToc: true
---

# Three Sets, Three **Jobs**

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏋️ **Training**, 360 rows

Gradient descent fits the weights to these rows.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎚️ **Validation**, 120 rows

They decide what gradient descent does not: the number of hidden units, $\eta$, the number of epochs.

</div>

<div class="card card-success card-glass pad-compact">

## 🎓 **Test**, 120 rows

Used once, at the end, for the number that is reported.

</div>

</div>

```python
rng = np.random.default_rng(0)
idx = rng.permutation(len(y))            # the 600 row numbers, shuffled
train, val, test = idx[:360], idx[360:480], idx[480:]
mu, sd = X[train].mean(axis=0), X[train].std(axis=0)
Z = (X - mu) / sd                        # scaled with the training rows
```

<div class="card card-info card-glass pad-compact mt-sm">

Lecture 11 split the rows into training and test and standardised the inputs. The middle set is new. A choice made by looking at a set is fitted to that set, so the rows that pick the model cannot also grade it. The mean (5.04, 28.96) and the standard deviation (1.09, 10.67) come from the training rows only.

</div>

<!--
Speaker: the split is by a seeded shuffle, so that it can be repeated. Without
the shuffle a file sorted by class would put one class into the test rows.
(~3 min)
-->

---
hideInToc: true
---

# The Loop as a **Function**

```python
def fit(X, y, H, seed=0, eta=1.0, epochs=5000):
    rng = np.random.default_rng(seed)
    V, c = rng.normal(0, 1, (H, 2)), np.zeros(H)     # H hidden units
    w, b = rng.normal(0, 1, H), 0.0
    for epoch in range(epochs):
        h = sigma(X @ V.T + c)
        y_hat = sigma(h @ w + b)
        d = (y_hat - y) / len(y)                     # N rows
        dh = np.outer(d, w) * h * (1 - h)
        w, b = w - eta * h.T @ d, b - eta * d.sum()
        V, c = V - eta * dh.T @ X, c - eta * dh.sum(axis=0)
    return V, c, w, b

def predict(p, X):
    V, c, w, b = p
    return sigma(sigma(X @ V.T + c) @ w + b)

p = fit(Z[train], y[train], H=4)
print(np.mean((predict(p, Z[train]) > 0.5) == y[train]))    # 0.9555...
```

<div class="note-text mt-sm">

The loop of the XOR slide with three changes: `H` hidden units, `len(y)` rows, and the nine or more numbers returned as `p`. With four hidden units, 344 of the 360 training rows are right.

</div>

<!--
Speaker: nothing in the mathematics changed between four points and 360 rows.
The training takes less than a second. (~2 min)
-->

---
hideInToc: true
---

# One Line per **Hidden Unit**

<img class="fig" src="/figures/viz_ml_hidden_units.svg" style="display:block;margin:0 auto;max-height:250px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**One or two units** cannot close a region. One line cuts the plane in two, two lines give a wedge. The model is too simple for the data: it **underfits**.

</div>

<div class="card card-success card-glass pad-compact">

**Three units** are three lines, and three lines enclose a triangle. The sigmoid rounds its corners. The validation accuracy jumps from 0.742 to 0.900.

</div>

<div class="card card-info card-glass pad-compact">

**Four units** follow the cloud a little better: 0.917. The white curve is where $\hat{y} = 0.5$. The points are the training rows, in the scaled coordinates.

</div>

</div>

<!--
Speaker: the same fit function with H from 1 to 4, seed 0 each time. The
shaded region is where the network answers class 1. (~3 min)
-->

---
hideInToc: true
---

# Overfitting in a **Network**

<img class="fig" src="/figures/viz_ml_overfit_network.svg" style="display:block;margin:0 auto;max-height:255px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**60 training rows, 20 hidden units, 81 parameters.** After 30 000 epochs the training loss is 0.0016 and all 60 rows are right. The validation loss was lowest after 410 epochs, at 0.280, and has risen to 1.79. The validation accuracy fell from 0.850 to 0.825.

</div>

<div class="card card-success card-glass pad-compact">

**The boundary bends around single rows.** Three remedies: more training rows, fewer hidden units, or stopping where the validation loss is lowest. The third is called early stopping, and the number of epochs is then one more choice made by the validation rows.

</div>

</div>

<!--
Speaker: the same fit function on the first 60 training rows with H = 20. The
white curve fits every training point, including the orange ones that sit
inside the cloud by chance. (~3 min)
-->

---
hideInToc: true
---

# Choose with Validation, Report with **Test**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Hidden units | Parameters | Loss, training | Loss, validation | Accuracy, validation |
| --- | --- | --- | --- | --- |
| 1 | 5 | 0.570 | 0.639 | 0.617 |
| 2 | 9 | 0.398 | 0.626 | 0.742 |
| 3 | 13 | 0.138 | 0.233 | 0.900 |
| 4 | 17 | 0.123 | **0.209** | 0.917 |
| 8 | 33 | 0.118 | 0.219 | 0.908 |
| 16 | 65 | 0.114 | 0.226 | 0.917 |

The training loss falls with every added unit. The validation loss is lowest at four units: that is the choice. The training loss could not have made it, because it always prefers the larger network.

</div>

<div class="card card-success card-glass pad-compact">

## 🎓 **The test rows, once**

The 2-4-1 network on the 120 test rows: 114 right, an accuracy of 0.950. Its uncertainty, as in Lecture 11:

$$
\sqrt{\frac{0.95 \cdot 0.05}{120}} = 0.020
$$

The result is $0.95 \pm 0.02$. The validation rows gave 110 of 120. A difference of 4 rows is inside the uncertainty.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

**What “once” means.** No choice is made after the test rows have been looked at. If the test result leads to a change of the model, the test rows have become validation rows, and the number is no longer a test. And 120 rows cannot show a difference of 0.01: for an uncertainty of 0.01 at this accuracy, $0.95 \cdot 0.05 / 0.01^2 = 475$ test rows are needed.

</div>

<!--
Speaker: six trainings, each about half a second. The validation rows were not
used by gradient descent, but they have now been used by us. The test rows are
the only rows that neither gradient descent nor we have used for anything.
That is what makes the number honest. (~4 min)
-->

---
layout: section
hideInToc: true
---

# Measuring a **Classifier**

One number hides which kind of error was made.

---
hideInToc: true
---

# The Confusion **Matrix**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **The 120 test rows**

| | Predicted 1 | Predicted 0 | Rows |
| --- | --- | --- | --- |
| **Class 1** | 53 true positives, TP | 4 false negatives, FN | 57 |
| **Class 0** | 2 false positives, FP | 61 true negatives, TN | 63 |

Accuracy counts the diagonal: 53 + 61 = 114 of 120.

</div>

<div class="card card-info card-glass pad-compact">

## ❌ **Two kinds of error**

- **False negative**: a row of class 1 that the network called 0. Four were missed
- **False positive**: a row of class 0 that the network called 1. Two were let in

</div>

</div>

```python
score = predict(p, Z[test])              # 120 outputs between 0 and 1
pred = score > 0.5                       # the decision
t = y[test] == 1                         # the truth
TP, FP = np.sum(pred & t), np.sum(pred & ~t)
FN, TN = np.sum(~pred & t), np.sum(~pred & ~t)
print(TP, FP, FN, TN)                    # 53 2 4 61
```

<!--
Speaker: four counts from two masks. The sign ~ turns True into False.
"Positive" means the class the question is about, here class 1. (~3 min)
-->

---
hideInToc: true
---

# Accuracy, Precision, **Recall**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **Accuracy**

Of all rows, the share that was decided correctly.

$$
\frac{TP + TN}{N} = \frac{114}{120} = 0.950
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔬 **Precision**

Of the rows called 1, the share that are 1.

$$
\frac{TP}{TP + FP} = \frac{53}{55} = 0.964
$$

</div>

<div class="card card-accent card-glass pad-compact">

## 🕸️ **Recall**, the true-positive rate

Of the rows that are 1, the share that was found.

$$
\frac{TP}{TP + FN} = \frac{53}{57} = 0.930
$$

</div>

<div class="card card-info card-glass pad-compact">

## 🚪 **False-positive rate**

Of the rows that are 0, the share called 1.

$$
\frac{FP}{FP + TN} = \frac{2}{63} = 0.032
$$

</div>

</div>

<div class="note-text mt-sm">

In particle physics the recall is the signal efficiency and the precision is the purity of the selected sample.

</div>

<!--
Speaker: precision reads the matrix along a column, recall and the
false-positive rate along a row. Have the room compute the four from the
counts before showing them. (~3 min)
-->

---
hideInToc: true
---

# When Accuracy **Misleads**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

## 🔎 **100 signal rows among 100 000**

| Classifier | TP | FP | Accuracy | Recall | Precision |
| --- | --- | --- | --- | --- | --- |
| always answers 0 | 0 | 0 | 0.9990 | 0 | not defined |
| recall 0.90, false-positive rate 0.01 | 90 | 999 | 0.9899 | 0.90 | 0.083 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

```text
FP        = 0.01 · 99 900        = 999
precision = 90 / (90 + 999)      = 0.083
accuracy  = (90 + 98 901) / 100 000 = 0.9899
```

</div>

<div class="card card-warning card-glass pad-compact">

The classifier that finds 90 of the 100 has the lower accuracy. Of the 1089 rows it calls signal, 999 are not. A false-positive rate of 1 % is large when the other class is a thousand times bigger.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Before reading an accuracy, compute what the rule “always the larger class” achieves. In the two-class file that is 0.525. Here it is 0.999.

</div>

<!--
Speaker: this is the situation of most searches in physics: the wanted class
is rare. Accuracy is then the wrong number to report. (~3 min)
-->

---
hideInToc: true
---

# The Threshold Is a **Choice**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Cut on $\hat{y}$ | TP | FP | FN | TN | Precision | Recall |
| --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 57 | 19 | 0 | 44 | 0.750 | 1.000 |
| 0.5 | 53 | 2 | 4 | 61 | 0.964 | 0.930 |
| 0.9 | 48 | 1 | 9 | 62 | 0.980 | 0.842 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔬 **A false alarm is expensive**

Raise the cut. A claimed discovery that is none costs more than a missed candidate: precision counts.

</div>

<div class="card card-accent card-glass pad-compact">

## 🕸️ **A miss is expensive**

Lower the cut. The trigger of Lecture 02 drops an event for ever, and a later step can still remove what was let in: recall counts.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The network gives a number between 0 and 1. The cut that turns it into a decision is set by a person, from what each kind of error costs. One network has a whole table of precisions and recalls, one row per cut.

</div>

<!--
Speaker: the same network and the same 120 test rows in all three lines. Only
the 0.5 in the line pred = score > 0.5 was changed. (~2 min)
-->

---
hideInToc: true
---

# The ROC Curve **by Hand**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| Cut lowered to | This row is | True-positive rate | False-positive rate |
| --- | --- | --- | --- |
| 0.9 | class 1 | 1/4 | 0 |
| 0.8 | class 1 | 2/4 | 0 |
| 0.7 | class 0 | 2/4 | 1/4 |
| 0.6 | class 1 | 3/4 | 1/4 |
| 0.4 | class 1 | 4/4 | 1/4 |
| 0.3 | class 0 | 4/4 | 2/4 |
| 0.2 | class 0 | 4/4 | 3/4 |
| 0.1 | class 0 | 4/4 | 4/4 |

</div>

<img class="fig" src="/figures/viz_ml_roc_by_hand.svg" style="display:block;margin:0 auto;max-height:300px;">

</div>

<div class="card card-info card-glass pad-compact mt-md">

Eight rows, sorted by their score. The cut is lowered past one row at a time: a row of class 1 moves the curve up by 1/4, a row of class 0 moves it right by 1/4. The curve of all cuts is the **ROC curve**.

The area under the steps is $\tfrac{1}{4} \cdot \tfrac{2}{4} + \tfrac{3}{4} \cdot 1 = 0.875$.

</div>

<!--
Speaker: ROC stands for receiver operating characteristic; the name comes
from radar receivers. Draw the steps on the board from
the table, one row at a time, before showing the figure. (~3 min)
-->

---
hideInToc: true
---

# What the Area **Means**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Count the pairs**

Take one row of class 1 and one row of class 0. The pair is **in order** if the row of class 1 has the higher score.

- There are 4 · 4 = 16 pairs
- 0.9 and 0.8 are above all four scores of class 0: 8 pairs
- 0.6 and 0.4 are above three of them, and below 0.7: 6 pairs
- 14 of 16 pairs are in order: 0.875

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **The area under the curve, AUC**

It is the probability that a random row of class 1 gets a higher score than a random row of class 0.

- 1 means that every pair is in order
- 0.5 is what scores without information give: the diagonal

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Why the two numbers agree: every step to the right belongs to one row of class 0, and the height of the curve at that step is the share of class-1 rows with a higher score. Adding the columns counts the pairs.

</div>

```python
s1, s0 = score[t], score[~t]                 # the scores of the two classes, test rows
pairs = s1[:, None] > s0[None, :]            # 57 x 63 comparisons
print(pairs.size, pairs.sum(), pairs.mean().round(4))        # 3591 3558 0.9908
```

<!--
Speaker: 0.875 twice, once as an area and once as a count. The count is the
definition that can be explained to anyone. The three lines of code count the
pairs for the 120 test rows of the network: s1[:, None] turns the 57 scores
into a column, so that the comparison gives a table of 57 by 63. (~3 min)
-->

---
hideInToc: true
---

# The ROC of the **Test Rows**

<img class="fig" src="/figures/viz_ml_roc_curve.svg" style="display:block;margin:0 auto;max-height:255px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**Three models, one test set.** For the 2-4-1 network there are 57 · 63 = 3591 pairs, and 3558 are in order: an AUC of 0.991. Two hidden units give 0.773. One neuron gives 0.438, no better than the 0.5 of random scores.

</div>

<div class="card card-info card-glass pad-compact">

**What the AUC does and does not say.** It needs no cut, and it does not change with the share of the two classes, because each rate is measured inside one class. It says how well the scores order the rows. It does not say where to cut.

</div>

</div>

<!--
Speaker: the three dots on the blue curve are the cuts 0.1, 0.5 and 0.9 of the
table two slides back. The histogram on the left shows why the curve is so
close to the corner: the two classes get very different scores. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Cross-Validation & **Leakage**

How sure the measured number is, and how it can be wrong without anyone noticing.

---
hideInToc: true
---

# Cross-**Validation**

<img class="fig" src="/figures/viz_ml_cross_validation.svg" style="display:block;margin:0 auto;max-height:215px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**One validation set** of 120 rows gave 0.917, with an uncertainty of 0.025. It cannot tell 4 hidden units from 8, and another shuffle would give another number.

</div>

<div class="card card-primary card-glass pad-compact">

**Five folds.** Each of the 480 rows is held out once. The five accuracies have the mean 0.935 and the standard deviation 0.019: a result and its spread.

</div>

<div class="card card-info card-glass pad-compact">

**The cost** is five trainings. The scaling is redone in every run from the four training folds. The 120 test rows stay out of all of it.

</div>

</div>

<!--
Speaker: cross-validation replaces the single validation set when rows are
few. The spread of the five numbers is the first thing to look at when two
models are compared. (~3 min)
-->

---
hideInToc: true
---

# Data **Leakage**

<div class="card card-warning card-glass pad-compact mt-sm">

## 💧 **The model has seen what it will not have when it is used**

A leak makes the measured accuracy higher than the accuracy in use. No error message appears, and the test rows often cannot show it.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **The label in an input**

An input was computed from the label, or the label from an input.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔓 **Test rows in a choice**

The scaling constants, the number of hidden units or the cut were set while the test rows were part of the data.

</div>

<div class="card card-accent card-glass pad-compact">

## 👯 **One object on both sides**

Duplicate rows, several candidates from one collision or repeated measurements of one sample are split between training and test.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

**Three habits against it.** Split first: every number taken from the data, a mean, a cut, a number of units, comes from the training or the validation rows. Split by object: all rows of one collision or one sample go to the same side. Ask of every input whether it is known at the time the model is used.

</div>

<!--
Speaker: three forms, in the order of how often they are found. The
standardisation of this lecture followed the first habit: mu and sd came from
the training rows. The next slide is the first form, on the file of this
course. (~3 min)
-->

---
hideInToc: true
---

# A Leak in the **LHCb File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎯 **The task**

`D0_KPi.csv`. The label is 1 if `M` lies between 1845 and 1885 MeV/c², the region of the D⁰ peak, and 0 otherwise. The inputs are the logarithms of `PT`, `TAU` and `IPCHI2`, standardised.

The 91 531 rows with `TAU` above 0 are used: 73 224 for training and 18 307 for testing. The larger class has 53.2 % of the test rows.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📊 **Accuracy on the test rows**

| Inputs | One neuron | Network, 4 hidden units |
| --- | --- | --- |
| `PT`, `TAU`, `IPCHI2` | 0.601 | 0.629 |
| the same and `M` | 0.603 | **0.999** |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

With `M` among the inputs the network is right for 99.9 % of the test rows. It has learned the two cuts on `M` that define the label, and nothing about the candidates. The test rows cannot reveal this: they contain `M` too. The single neuron gains nothing from `M`, because an interval is not linearly separable. The honest result is 0.629 against 0.532: the three columns say little about where `M` falls. A result this much better than expected is checked before it is believed: leave out one input at a time and see which one carries it.

</div>

<!--
Speaker: the fit function of this lecture with three and with four inputs,
seed 0. The label is itself rough: the peak region also holds background.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Learning Without **Labels**

Rows without a label, and one method that groups them.

---
hideInToc: true
---

# No Labels: **Clustering**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **Supervised**

Everything so far. Every training row came with its label $y$, and the loss compared $\hat{y}$ with it.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **Unsupervised**

There are only the inputs. The question changes from “which class is this row?” to “which rows belong together?”

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 🎯 **k-means**

Choose the number of groups $k$ and $k$ starting centres. Then repeat two steps until nothing changes:

1. **Assign** every point to the nearest centre
2. **Update** every centre to the mean of its points

The quantity it lowers is $J$, the sum of the squared distances of all points to their centres.

</div>

<!--
Speaker: there is no y hat and no gradient here. The method is older and
simpler than a network, and it is the standard first look at unlabelled rows.
(~2 min)
-->

---
hideInToc: true
---

# k-means by Hand: **Iteration 1**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 1️⃣ **Assign**

| Point | $d^2$ to (1, 3) | $d^2$ to (2, 1) | Group |
| --- | --- | --- | --- |
| A (1, 3) | 0 | 5 | 1 |
| B (2, 1) | 5 | 0 | 2 |
| C (3, 2) | 5 | 2 | 2 |
| D (6, 8) | 50 | 65 | 1 |
| E (5, 8) | 41 | 58 | 1 |
| F (4, 5) | 13 | 20 | 1 |

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Update**

```text
centre 1 = mean of A, D, E, F
         = (16/4, 24/4) = (4, 6)
centre 2 = mean of B, C
         = (5/2, 3/2)   = (2.5, 1.5)
```

One distance in full, D to (1, 3): $5^2 + 5^2 = 50$.

With the new centres, $J = 18 + 8 + 5 + 1 + 0.5 + 0.5 = 33$.

</div>

</div>

<div class="note-text mt-sm">

Six points, $k = 2$, and the centres start on A and B. $d^2$ is the squared distance: the difference in the first coordinate squared plus the difference in the second squared.

</div>

<!--
Speaker: A stays with its own centre, and D, E and F are nearer to A than to
B, so the first group is A with the three far points. (~3 min)
-->

---
hideInToc: true
---

# k-means by Hand: **Iteration 2**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 1️⃣ **Assign**

| Point | $d^2$ to (4, 6) | $d^2$ to (2.5, 1.5) | Group |
| --- | --- | --- | --- |
| A (1, 3) | 18 | 4.5 | **2** |
| B (2, 1) | 29 | 0.5 | 2 |
| C (3, 2) | 17 | 0.5 | 2 |
| D (6, 8) | 8 | 54.5 | 1 |
| E (5, 8) | 5 | 48.5 | 1 |
| F (4, 5) | 1 | 14.5 | 1 |

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Update**

```text
centre 1 = mean of D, E, F
         = (15/3, 21/3) = (5, 7)
centre 2 = mean of A, B, C
         = (6/3, 6/3)   = (2, 2)
```

A has changed its group. Now $J = 2 + 1 + 5 + 2 + 1 + 1 = 12$.

A third iteration assigns every point as before. The centres stay, and the method has finished.

</div>

</div>

<!--
Speaker: the centre of the first group moved away from A when D, E and F
pulled it up, and A found the other centre nearer. (~2 min)
-->

---
hideInToc: true
---

# Why It **Stops**

<img class="fig" src="/figures/viz_ml_kmeans_by_hand.svg" style="display:block;margin:0 auto;max-height:260px;">

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**Neither step can raise $J$.** The first gives every point its nearest centre, so no distance grows. The second moves each centre to the mean, and the mean is the point with the smallest sum of squared distances. The same fact made the sample mean the best estimate in Lecture 09.

</div>

<div class="card card-success card-glass pad-compact">

**$J$ went 33, 12, 12.** A quantity that never rises and cannot fall below zero must stop changing. There are only finitely many ways to split six points into two groups, so the method always ends.

</div>

</div>

<!--
Speaker: crosses are the centres, the dashed arrows show how each centre moved
in that iteration, colours are the groups. (~2 min)
-->

---
hideInToc: true
---

# Where k-means **Misleads**

<img class="fig" src="/figures/viz_ml_kmeans.svg" style="display:block;margin:0 auto;max-height:225px;">

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**The start decides.** Of the 15 pairs of starting points among A to F, 9 end at $J = 12$ and 6 at $J = 14.25$, with F in the wrong group. Run several starts and keep the smallest $J$.

</div>

<div class="card card-primary card-glass pad-compact">

**It always returns $k$ groups**, whether the data have groups or not. In the right panel one cloud is split in two. $k$ is chosen by a person.

</div>

<div class="card card-info card-glass pad-compact">

**Distances mix the units.** Without standardising, the column with the largest numbers decides the groups.

</div>

</div>

<!--
Speaker: the figure is k-means in ten lines of NumPy on 300 simulated points:
two clouds on the left, one cloud on the right. The first card is the lesson
of the XOR seeds again: a method that descends from a starting point ends in
the valley it started in. (~2 min)
-->

---
layout: section
hideInToc: true
---

# **scikit-learn**

A Python package that holds what was built by hand in this lecture and the one before.

---
hideInToc: true
---

# What Was Built by Hand, **Packaged**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| By hand | In scikit-learn |
| --- | --- |
| shuffle and slice | `train_test_split` |
| `(X - mu) / sd` | `StandardScaler` |
| the neuron of Lecture 11 | `LogisticRegression` |
| the network of this lecture | `MLPClassifier` |
| counting TP, FP, FN, TN | `confusion_matrix` |
| precision and recall | `precision_score`, `recall_score` |
| counting pairs | `roc_auc_score` |
| five folds | `cross_val_score` |
| assign and update | `KMeans` |

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **Install and import**

```text
python -m pip install scikit-learn
```

The same line in zsh and in PowerShell, with the environment of Lecture 13 active. The package is imported under the name `sklearn`. The numbers of this section were made with version 1.7.2.

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every model has the same two calls: `fit(X, y)` trains and `predict(X)` answers. Exchanging one model for another changes one line.

</div>

</div>

</div>

<!--
Speaker: nothing in the right column is new. Each name is a tested, faster
version of something the room has written or computed by hand. (~2 min)
-->

---
hideInToc: true
---

# Checked Against the **Hand Version**

```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_auc_score
print(confusion_matrix(y[test], pred))                  # [[61  2]
                                                        #  [ 4 53]]
print(round(precision_score(y[test], pred), 4))         # 0.9636
print(round(recall_score(y[test], pred), 4))            # 0.9298
print(round(roc_auc_score(y[test], score), 4))          # 0.9908
```

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**The same counts**, in another order. scikit-learn puts class 0 first: TN is top left, TP bottom right. Precision 53/55, recall 53/57 and the AUC 3558/3591 agree to four decimals.

</div>

<div class="card card-secondary card-glass pad-compact">

**The neuron.** `LogisticRegression(penalty=None)` on the three LHCb inputs gives the weights (0.344, 0.472, −0.590) and the bias 0.184. The loop of Lecture 11 gives the same, and both reach 0.601.

</div>

<div class="card card-accent card-glass pad-compact">

**k-means.** `KMeans` started on A and B ends with the centres (5, 7) and (2, 2) and $J = 12$, as by hand.

</div>

</div>

<!--
Speaker: pred and score are the arrays of the confusion-matrix slide. Where a
hand version exists, the first use of a packaged function is a comparison with
it. (~3 min)
-->

---
hideInToc: true
---

# A Default Is a **Choice** Too

```python
from sklearn.neural_network import MLPClassifier
for solver in ("adam", "lbfgs"):
    net = MLPClassifier(hidden_layer_sizes=(4,), activation="logistic",
                        solver=solver, random_state=0, max_iter=5000)
    net.fit(Z[train], y[train])
    print(solver, net.n_iter_, round(net.loss_, 3), net.score(Z[test], y[test]))
```

```text
adam 213 0.684 0.48333333333333334
lbfgs 476 0.122 0.9416666666666667
```

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**`adam` is the default.** It stopped after 213 passes at a loss of 0.684, close to $\ln 2$. Its rule is to stop when the loss improves by less than 0.0001 in ten passes in a row, and its steps were that small. The network had not started to learn: 48 % on the test rows.

</div>

<div class="card card-success card-glass pad-compact">

**`lbfgs`** follows the same gradient in another way and reaches a loss of 0.122 and 113 of the 120 test rows. By hand: 0.123 and 114. Without the hand version, 48 % would look like a property of the data.

</div>

</div>

<!--
Speaker: the same network, the same rows. The first line of output is what a
user gets who types the shortest possible call. Write the version of the
package next to a result. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Large Language **Models**

A very large network, trained by gradient descent to predict the next piece of text.

---
hideInToc: true
---

# From Two Classes to **Many**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Softmax**

A network with $K$ output units gives $K$ numbers $z_1 \ldots z_K$. They become probabilities by

$$
p_k = \frac{e^{z_k}}{e^{z_1} + \dots + e^{z_K}}
$$

For $z = (2.0,\ 1.0,\ 0.1)$: $p = (0.659,\ 0.242,\ 0.099)$. They add up to 1.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **For two classes: the sigmoid**

$$
p_1 = \frac{e^{z_1}}{e^{z_1} + e^{z_2}} = \frac{1}{1 + e^{-(z_1 - z_2)}}
$$

That is $\sigma(z_1 - z_2)$. The loss is the one of Lecture 11, $L = -\ln p$ of the class that is true. In the example: 0.417 if the first class is true, 2.317 if the third is.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Nothing else changes. The error at output $k$ is again output minus target: $p_k - 1$ for the true class and $p_k$ for the others. Backpropagation carries it through the layers.

</div>

<!--
Speaker: divide numerator and denominator of p1 by e to the z1 to get the
middle form. A network that chooses among ten digits or fifty thousand words
ends in this function. (~3 min)
-->

---
hideInToc: true
---

# A Language Model **by Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The training text**

```text
the kaon has a mass of 494 MeV .
the pion has a mass of 140 MeV .
the D0 has a mass of 1865 MeV .
the pendulum has a length of 60 cm .
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **What follows each word**

| After | Next word | Probability |
| --- | --- | --- |
| `the` | kaon, pion, D0, pendulum | 1/4 each |
| `has` | a | 1 |
| `a` | mass, length | 3/4, 1/4 |
| `of` | 494, 140, 1865, 60 | 1/4 each |
| `494`, `140`, `1865` | MeV | 1 |
| `60` | cm | 1 |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **language model** gives, for a piece of text, the probability of each possible next word. This one looks at the last word only, and its probabilities are counts from four sentences. Text is produced by drawing a next word, appending it, and repeating.

</div>

<!--
Speaker: count the table with the room from the four sentences. After "a"
comes "mass" three times and "length" once. (~3 min)
-->

---
hideInToc: true
---

# Generating **Text**

```py {monaco-run} {autorun:false, outputHeight:'4.8rem'}
import numpy as np
text = """the kaon has a mass of 494 MeV .
the pion has a mass of 140 MeV .
the D0 has a mass of 1865 MeV .
the pendulum has a length of 60 cm ."""
words = text.split()
follow = {}                              # word -> the words seen after it
for a, b in zip(words, words[1:]):
    follow[a] = follow.get(a, []) + [b]
print(follow["a"])

rng = np.random.default_rng(0)
for n in range(5):
    w, out = "the", ["the"]
    while w != ".":
        w = str(rng.choice(follow[w]))   # draw the next word
        out.append(w)
    print(" ".join(out))
```

<!--
Speaker: the dictionary follow is the table of the last slide. zip pairs every
word with its successor. Drawing from the list of followers gives each word
with the probability of the table. Measured output on the next slide. (~3 min)
-->

---
hideInToc: true
---

# What the Model **Wrote**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖨️ **Five sentences, seed 0**

```text
the pendulum has a mass of 140 MeV .
the kaon has a mass of 1865 MeV .
the D0 has a length of 1865 MeV .
the D0 has a length of 140 MeV .
the D0 has a mass of 1865 MeV .
```

Only the last one is in the training text.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Count them**

The model can write 4 · 2 · 4 = 32 different sentences. 4 of them are in the text. The probability of writing one of those four:

$$
3 \cdot \tfrac{1}{4} \cdot \tfrac{3}{4} \cdot \tfrac{1}{4} + \tfrac{1}{4} \cdot \tfrac{1}{4} \cdot \tfrac{1}{4} = \tfrac{10}{64} = 16\,\%
$$

Of 10 000 sentences drawn with seed 0, 1617 were.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

Every sentence is grammatical, and every step in it is a continuation that occurs in the text. Five in six are false. The model was built to continue text. Nothing in it compares a sentence with a source.

</div>

<!--
Speaker: the first product is for kaon, pion and D0: the right noun, then
"mass", then the right number. The second is for the pendulum. (~3 min)
-->

---
hideInToc: true
---

# What a Large Language Model **Is**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧠 **The same task, a network for the table**

- The text is cut into **tokens**: words and pieces of words, each with a number. A vocabulary has tens of thousands of them
- Input: the tokens so far, thousands of them, not the last one only
- Output: one $z_k$ for every token of the vocabulary, turned into probabilities by softmax
- Loss: $-\ln p$ of the token that came next in the training text
- Training: gradient descent with backpropagation

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📏 **The size**

| Network | Parameters |
| --- | --- |
| XOR, this lecture | 9 |
| two-class file, this lecture | 17 |
| GPT-2, 2019 | 1.5 × 10⁹ |
| GPT-3, 2020 | 1.75 × 10¹¹ |

The training text is collected from the internet, from books and from program code. The arrangement of the layers is called a transformer (Vaswani et al., 2017).

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

What was derived for nine parameters is what is computed for $10^{11}$: a forward pass, a loss, a backward pass, a step of size $\eta$. Text is written as on the last slide: draw a token, append it, repeat.

</div>

<!--
Speaker: the two published sizes are from the papers of those models. Newer
models are larger, and their sizes are often not published. The principle on
this slide has not changed since 2017. (~3 min)
-->

---
hideInToc: true
---

# What Follows from **That**

<div class="stack-tight mt-md">

<div class="card card-warning card-glass pad-compact">

📝 **Plausible text, not checked facts.** The output is a likely continuation. A long context makes it right far more often than the table of four sentences. It is not always right, for the same reason: no step compares the output with a source

</div>

<div class="card card-primary card-glass pad-compact">

✍️ **Fluent in every case.** A wrong answer is written in the same confident style as a right one. The style carries no information about the truth

</div>

<div class="card card-secondary card-glass pad-compact">

🎲 **Not the same answer twice.** The next token is drawn at random from the probabilities, so the same question can get different answers

</div>

<div class="card card-accent card-glass pad-compact">

📅 **Nothing after the training text.** What was written or measured later is unknown to the model, unless it is in the text it is given

</div>

<div class="card card-info card-glass pad-compact">

🔍 **No view of your data or of the literature**, unless a tool around the model fetches a text. Then the fetched text can be checked, and what the model says about it still has to be

</div>

</div>

<!--
Speaker: five statements that follow from how the model is built, not from
experience with one product. They hold for every model of this kind. (~3 min)
-->

---
hideInToc: true
---

# What to **Verify**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| The model gives you | Check it by |
| --- | --- |
| A reference | Opening it. Does it exist, with these authors, and does it say this? An invented reference looks like a real one |
| A number, a constant, a formula | The source, or your own calculation |
| Code | Running it on a case whose answer you know, as with the nudged weight |
| A summary of a paper | Reading the parts of the paper that your argument rests on |
| A statement about your data | Computing it from the data |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Where it saves time**

Where the check is quick and the writing is slow: a first draft, the name of a function, the meaning of an error message, another wording of a paragraph.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **The limit**

What you cannot check, you cannot use. That needs the knowledge to do the check, so the tool helps most in a field you already know.

</div>

</div>

<!--
Speaker: the table is the practical content of this section. Every row is a
check that takes minutes and that this course has practised on its own
results. (~3 min)
-->

---
hideInToc: true
---

# What to Disclose, What Not to **Paste**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📣 **Disclose**

- Which tool, which version, when, and for what: wording, code, translation, a search
- Journals and universities have rules for this. Read the ones that apply before you submit
- A language model is not an author. The authors answer for every sentence, number and line of code, whoever drafted it (COPE position statement, 2023; ICMJE recommendations)

</div>

<div class="card card-warning card-glass pad-compact">

## 🚫 **Do not paste**

- Data or text of other people that is not published
- Personal data
- A manuscript or a proposal that you were given to review
- Passwords and access keys
- Anything under a confidentiality agreement

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

What is typed into an online service is sent to the computers of another organisation. Whether it is kept, and whether it is used for training, is set by the terms of that service. Read them, or use a tool that your institution provides.

</div>

<!--
Speaker: COPE is the Committee on Publication Ethics, ICMJE the International
Committee of Medical Journal Editors. Both state that an AI tool cannot be
listed as an author and that its use is to be declared. (~3 min)
-->

---
hideInToc: true
---

# Keeping the Work **Reproducible**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

♻️ A chat cannot be run again with the same output. No result may depend on one: what the model produced goes into a script or a text file in the project folder

</div>

<div class="card card-secondary card-glass pad-compact">

🧪 Code from a model is treated like all code in this course: under version control (Lecture 05), run from a clean start, with a test on a case whose answer is known (Lecture 13)

</div>

<div class="card card-accent card-glass pad-compact">

📝 The README says which tool was used for what, with the date. This is provenance, like the source of a data file (Lecture 02)

</div>

<div class="card card-success card-glass pad-compact">

🗣️ You can explain every line that you hand in

</div>

</div>

<!--
Speaker: the four aims of the course apply to this tool as to any other. The
last card is the test: if a line cannot be explained, it is not yet yours.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Compute the **forward pass** of a network with one hidden layer and count its parameters

</div>

<div class="card card-success card-glass pad-compact">

✅ Derive the eight lines of **backpropagation** and check a derivative by nudging a weight

</div>

<div class="card card-success card-glass pad-compact">

✅ Train a network in NumPy, state the **seed**, and say why a run gets stuck

</div>

<div class="card card-success card-glass pad-compact">

✅ Give **training, validation and test** rows their jobs, and see overfitting in two loss curves

</div>

<div class="card card-success card-glass pad-compact">

✅ Compute **precision, recall and the AUC** from counts, and find a leak

</div>

<div class="card card-success card-glass pad-compact">

✅ Run **k-means** by hand, and check a scikit-learn result against the hand version

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🧠 **One method, from 9 parameters to 10¹¹**

A forward pass, a loss, a backward pass, a step. A model trained this way is as good as its measurement on rows it has not seen. A language model trained this way writes likely text, and the checking stays with you.

</div>

<!--
Speaker: have the room nod along to each card. The last card joins the three
parts of the lecture: the method, the measurement, the tool. (~1 min)
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
  question="A network has 3 inputs, one hidden layer of 5 sigmoid units and 1 output unit. How many parameters does it have?"
  :options="[
    '15',
    '20',
    '26',
    '9'
  ]"
  :correct="2"
  explanation="The hidden layer has 5 · 3 = 15 weights and 5 biases, 20 parameters. The output unit has 5 weights and 1 bias, 6 parameters. Together 26."
/>

---
hideInToc: true
---

<MCQ
  question="In a backward pass the error at the output is δ = 0.2. A hidden unit has the output weight w = −3 and the value h = 0.9. What is the error of this hidden unit?"
  :options="[
    '−0.054',
    '−0.54',
    '+0.054',
    '−0.6'
  ]"
  :correct="0"
  explanation="The error of a hidden unit is δ · w · h · (1 − h) = 0.2 · (−3) · 0.9 · 0.1 = −0.054. The factor h (1 − h) = 0.09 is small because the unit is close to saturation."
/>

---
hideInToc: true
---

<MCQ
  question="A classifier is tested on 200 rows: TP = 30, FP = 10, FN = 20, TN = 140. What are its precision and its recall?"
  :options="[
    'Precision 0.60, recall 0.75',
    'Precision 0.75, recall 0.60',
    'Precision 0.85, recall 0.75',
    'Precision 0.75, recall 0.85'
  ]"
  :correct="1"
  explanation="Precision is TP / (TP + FP) = 30 / 40 = 0.75. Recall is TP / (TP + FN) = 30 / 50 = 0.60. The accuracy is (30 + 140) / 200 = 0.85, which is higher than both because most rows are of class 0."
/>

---
hideInToc: true
---

<MCQ
  question="Three rows of class 1 have the scores 0.8, 0.5 and 0.3. Two rows of class 0 have the scores 0.6 and 0.2. What is the area under the ROC curve?"
  :options="[
    '0.50',
    '0.67',
    '0.75',
    '0.83'
  ]"
  :correct="1"
  explanation="There are 3 · 2 = 6 pairs. In order are 0.8 above 0.6, 0.8 above 0.2, 0.5 above 0.2 and 0.3 above 0.2: four pairs. Out of order are 0.5 below 0.6 and 0.3 below 0.6. The area is 4 / 6 = 0.67."
/>

---
hideInToc: true
---

<MCQ
  question="A network with 400 hidden units is right for 100 % of its 500 training rows and for 71 % of 500 rows it has not seen. What is the most likely reading, and the first thing to do?"
  :options="[
    'Data leakage: remove the input that holds the label',
    'Too little training: run more epochs',
    'Overfitting: use fewer hidden units or stop earlier, and choose with validation rows',
    'The 500 unseen rows are too few for any conclusion'
  ]"
  :correct="2"
  explanation="A large gap between the training rows and unseen rows is the sign of overfitting: the network has fitted the noise of its training rows. A leak would raise the result on the unseen rows too. More epochs would widen the gap. With 500 rows the uncertainty of 0.71 is about 0.02, far smaller than the gap."
/>

---
hideInToc: true
---

<MCQ
  question="A language model gives you a reference for a statement in your report, with authors, journal, year and page numbers. What is established at this point?"
  :options="[
    'The reference exists, because the details are specific',
    'The reference exists, but it may not support the statement',
    'Nothing yet: the reference has to be found and read',
    'The statement is true if the model repeats the reference when asked again'
  ]"
  :correct="2"
  explanation="The model writes a likely continuation, and a likely continuation of a request for a reference is a line that looks like one. Specific details are part of looking like one. Asking again draws from the same probabilities. The check is to open the paper and read what it says."
/>
