---
layout: cover
title: "Classification and the Perceptron"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Classification and the Perceptron

##### <span class="aims-badge">🔧 tool-agnostic · ⚙️ automation · ♻️ reproducibility</span>

<!--
**Say:** one question, will it freeze tonight, and one artificial neuron that answers it: what it computes, how it learns from ten years of evenings, how sure its answer is, and what it cannot do.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be **conscious of its existence**.
The New York Times, 8 July 1958, on Frank Rosenblatt's perceptron

<!--
**Say:** what Rosenblatt showed that day was one artificial neuron. It draws one straight line.
(~0.5 min)
-->

---
hideInToc: true
---

# Will It Freeze **Tonight**?

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📅 **8 December, 18:00, in the weather log**

| Year | 18:00 | Humidity | 06:00 next day |
|--|--|--|--|
| 2016 | 0.7 °C | 76 % | −2.1 °C |
| 2017 | 3.1 °C | 79 % | +1.3 °C |
| 2018 | −3.9 °C | 81 % | −7.1 °C |
| 2019 | −2.6 °C | 75 % | −4.7 °C |
| 2020 | 1.6 °C | 75 % | −3.2 °C |
| 2021 | 1.2 °C | 67 % | −1.6 °C |
| 2022 | −2.7 °C | 80 % | −6.0 °C |
| 2023 | 1.1 °C | 79 % | −1.9 °C |
| 2024 | −0.2 °C | 82 % | −3.4 °C |

</div>

<div>

<div class="card card-warning card-glass pad-compact">

## ❓ **2025: 2.6 °C and 85 % at 18:00**

Below 0 °C by 06:00?

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

✅ 06:00 on 9 December 2025: **−2.0 °C**, frost.

</div>

<div class="card card-info card-glass pad-compact mt-md">

📊 The log holds **3646** such evenings, 2016 to 2025. **1229** were followed by frost.

</div>

</div>

</div>

<!--
**Ask:** hands up for frost, hands up for no frost. Eight of the nine earlier years froze; 2017, at 3.1 °C, did not, and 2025 is warmer than all the others but 2017.
**Say:** after the click: it froze. The lecture builds a rule from all 3646 evenings that gives this answer, and says how sure it is.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The 3646 Evenings of the **Log**

<div class="card card-primary card-glass pad-compact mt-sm">

📈 Each evening is a point: $x_1$ the temperature at 18:00, $x_2$ the humidity at 18:00 as a fraction (85 % → 0.85); its colour, the next morning. From 0 to 6 °C the two clouds overlap: 824 evenings, 568 of them with frost.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_evenings.svg">

<!--
**Say:** an evening is 18:00 of one day beside 06:00 of the next: 3652 pairs, and the six that touch the 120 missing hours of July 2019 are left out.
**Ask:** where would you draw the border between the colours?
**If asked:** the warmest evening followed by frost was 7.8 °C (30 September 2017), the coldest without frost −0.4 °C (15 February 2016).
(~2 min)
-->

---
layout: section
hideInToc: true
---

# From a Number to a **Class**

A mean and a slope are numbers. Frost or no frost is a class: 1 or 0.

<!--
**Say:** Lectures 8 and 9 estimated numbers; today's answer is one of two labels, and every idea of those lectures comes back: counting, a likelihood, a loss, a slope, a step downhill.
(~0.5 min)
-->

---
hideInToc: true
---

# One Evening as **Numbers**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌡️ **Inputs**

Temperature at 18:00: $x_1 = 2.6$ °C

Humidity at 18:00: $x_2 = 0.85$

Together: $x = (2.6,\ 0.85)$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🏷️ **Label**

$y = 1$: below 0 °C at 06:00, frost

$y = 0$: no frost

8 Dec 2025: $y = 1$

</div>

<div class="card card-accent card-glass pad-compact">

## 🎯 **Output**

$\hat{y}$: what a rule says, 1 or 0

Right when $\hat{y} = y$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **classifier** turns the inputs into a class. Its **accuracy**: the share of evenings with $\hat{y} = y$.

</div>

<!--
**Say:** the hat marks what the rule says; $y$ without a hat is what happened. One letter, one meaning, for the whole lecture.
**If asked:** the humidity is written as a fraction so that both inputs are numbers of a few units or less; with 85 in place of 0.85 the learning rule of this lecture fails (For the Curious).
(~1.5 min)
-->

---
hideInToc: true
---

# Every Evening as One **Row**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📋 **The first and the last rows**

`[date, temperature, humidity, frost]`

```text
['2016-01-01', -4.5, 85.0, 1]
['2016-01-02', -2.6, 82.0, 1]
...
['2025-12-29', -6.6, 85.0, 1]
['2025-12-30', -9.7, 93.0, 1]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔗 **Made from `weather.csv`**

- 18:00 of each day beside 06:00 of the next
- 3652 pairs; 6 touch the −999 hours of July 2019
- **3646** rows: 1229 with $y = 1$, 2417 with $y = 0$

</div>

</div>

<!--
**Say:** the hourly log of Lectures 5 and 7, read twice a day: the evening as the inputs, the next morning as the label.
**If asked:** the last row is the evening of 30 December 2025; 31 December has no next morning in the log.
(~1.5 min)
-->

---
hideInToc: true
---

# The Baseline: **Never Frost**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **A rule that ignores the inputs**

$\hat{y} = 0$ on every evening. It is right on every evening without frost:

$$
\frac{2417}{3646} = 66.3\,\%
$$

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **The number to beat**

"Always frost" is right on 1229, 33.7 %.

A rule that is right 66 % of the time has learned nothing about frost.

</div>

</div>

<!--
**Ask:** a forecaster says "I am right two times in three". Good?
**Say:** two evenings in three have no frost: "never frost" already scores 66.3 %. Every rule of the lecture is compared with it.
(~1.5 min)
-->

---
hideInToc: true
class: fill
---

# A Threshold on the **Temperature**

<div class="card card-success card-glass pad-compact mt-sm">

📊 The rule "frost if $x_1 < c$", scored for every $c$ from −6 to 14 °C in steps of 0.1 °C: best below 3.8 °C, right on 3490 of 3646 evenings, 95.7 %.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_threshold.svg">

<!--
**Say:** left, the temperatures of the frost evenings and of the others; their overlap is where any threshold errs. Right, each threshold scored by counting.
**Ask:** why does the curve fall on both sides? Too low a threshold misses frosts; too high a threshold calls frosts that do not come.
**If asked:** below 2 °C is right on 91.6 %, below 0 °C on 84.1 %.
(~2 min)
-->

---
hideInToc: true
---

# Score a Threshold on Ten Evenings, **Live**

```py {monaco-run} {autorun:false}
# 8 December 2016 to 2025: [temperature at 18:00, frost at 06:00]
evenings = [[0.7, 1], [3.1, 0], [-3.9, 1], [-2.6, 1], [1.6, 1],
            [1.2, 1], [-2.7, 1], [1.1, 1], [-0.2, 1], [2.6, 1]]
c = 3.8                              # <-- try 3, 2, 0
right = 0
for e in evenings:
    if e[0] < c:
        guess = 1
    else:
        guess = 0
    if guess == e[1]:
        right = right + 1
print(right, "of", len(evenings))    # 9 of 10
```

<!--
**Do:** run it with 3.8, then 3, 2 and 0: 9, 10, 9 and 5 of 10.
**Ask:** on these ten evenings 3 °C is best. Why not use 3 °C? Ten evenings choose the number that fits them; 3646 evenings choose 3.8 °C.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# One **Neuron**

A weighted sum of the inputs, a bias and a step. The threshold rule is one of them.

<!--
**Say:** three numbers decide what a neuron says; in this section they are set by hand.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Weighted Sum, Bias, **Step**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **The weighted sum**

$$
z = w_1 x_1 + w_2 x_2 + b
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪜 **The step**

$$
\hat{y} = \text{step}(z) = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{if } z \le 0 \end{cases}
$$

</div>

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_unit.svg">

<!--
**Say:** a weight $w_1$, $w_2$ for each input and a bias $b$: three numbers. With the step this unit is Rosenblatt's perceptron.
**If asked:** $w_1 x_1 + w_2 x_2$ is often written short as $w \cdot x$, the dot product. At exactly $z = 0$ the output here is 0; some books choose 1.
(~2 min)
-->

---
hideInToc: true
---

# 8 December 2025 Through the **Neuron**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚙️ **The threshold rule as a neuron**

$w_1 = -1$, $w_2 = 0$, $b = 3.8$:

$$
z = 3.8 - x_1 > 0 \quad\text{exactly when}\quad x_1 < 3.8
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **$x = (2.6,\ 0.85)$**

<FormulaSteps steps="
  z = w_1 x_1 + w_2 x_2 + b
  = (-1)(2.6) + (0)(0.85) + 3.8
  = -2.6 + 0 + 3.8
  = 1.2
" />

</div>

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

✅ $\hat{y} = \text{step}(1.2) = 1$: frost. At 06:00 −2.0 °C, so $y = 1$: right. On all 3646 evenings this neuron is right 3490 times, as the rule.

</div>

<!--
**Do:** click through: the numbers in place of the letters, each product, the sum; the last click, the step and what happened.
**Say:** the humidity has weight 0, so this neuron does not look at it: it is the rule "below 3.8 °C".
(~2 min)
-->

---
hideInToc: true
---

# The Neuron in **Python**

```py {monaco-run} {autorun:false}
def predict(x, w, b):
    z = w[0] * x[0] + w[1] * x[1] + b
    if z > 0:
        return 1
    return 0

w = [-1.0, 0.0]                      # the rule "below 3.8 °C"
b = 3.8
print(predict([2.6, 0.85], w, b))    # 8 Dec 2025, 1: frost came
print(predict([2.8, 0.81], w, b))    # 7 Dec 2025, 1: none came
print(predict([5.4, 0.75], w, b))    # 1 Nov 2024, 0: frost came
```

<div class="note-text mt-sm">Inputs in a list <code>x</code>, the weights in a list <code>w</code>: <code>x[0]</code> is the temperature, <code>x[1]</code> the humidity. The last two evenings lie near 4 °C, where the clouds overlap: the neuron is wrong on both.</div>

<!--
**Do:** run it; then set `w = [-1.0, 4.0]` and `b = 0.6` and run again: 1, 1, 0.
**Say:** three numbers and five lines of Python are the whole model so far.
(~2 min)
-->

---
hideInToc: true
---

# Where the Output **Changes**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Solve $z = 0$ for $x_1$**

$$
w_1 x_1 + w_2 x_2 + b = 0 \;\Longrightarrow\; x_1 = -\frac{b + w_2 x_2}{w_1}
$$

A straight line in the plane of $x_1$ and $x_2$: the **decision boundary**.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **A weight on the humidity: $w = (-1, 4)$, $b = 0.6$**

<v-clicks>

- $x_2 = 0.5$: $x_1 = -(0.6 + 2.0)/(-1) = 2.6$ °C
- $x_2 = 1.0$: $x_1 = -(0.6 + 4.0)/(-1) = 4.6$ °C
- 8 Dec 2025: $z = -2.6 + 3.4 + 0.6 = 1.4$, frost

</v-clicks>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$w_1$ and $w_2$ set the direction of the line, $b$ shifts it. With $w_2 = 0$ it stands upright, at $x_1 = 3.8$ °C.

</div>

<!--
**Say:** this neuron says frost below 2.6 °C on a dry evening and below 4.6 °C on a humid one.
**Ask:** what happens to the line if $w_1$, $w_2$ and $b$ are all doubled? Nothing: $z = 0$ at the same places.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Decision Boundary Is a **Line**

<div class="card card-info card-glass pad-compact mt-sm">

📐 Drag $w_1$, $w_2$ and $b$; tap an evening. Upright at 3.8 °C: 3490 of 3646 right; tilted, $w = (-1, 4)$ and $b = 0.6$: 3494, the humidity moves four evenings.

</div>

<PerceptronPlayground class="fig-fill mt-sm" />

<!--
**Do:** it opens on w = (−1, 0), b = 3.8 and 8 Dec 2025: z = 1.2, frost; the line stands at 3.8 °C, 3490 right, 95.7 %. Press never frost: 66.3 %, the baseline. Press reset.
**Do:** tilt it: click the w₂ slider and press PageUp four times (4.00); click b, PageDown three times and ↓ twice (0.6): 3494 right, 95.8 %. Then tap 6 Dec 2025, the ringed point near 1 °C: frost said, none came.
**Say:** whatever its three numbers, a neuron cuts the plane in two with a straight line; tilting it moves four evenings of 3646.
**Ask:** can any line put every cyan point on one side and every orange point on the other? No: the clouds overlap.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# One Neuron Computes **AND** and **OR**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact table-compact">

## 🔌 **$w = (1, 1)$, inputs 0 or 1**

| $x_1$ | $x_2$ | $z$, $b = -1.5$ | AND | $z$, $b = -0.5$ | OR |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | −1.5 | 0 | −0.5 | 0 |
| 0 | 1 | −0.5 | 0 | 0.5 | 1 |
| 1 | 0 | −0.5 | 0 | 0.5 | 1 |
| 1 | 1 | 0.5 | 1 | 1.5 | 1 |

The bias sets how large $x_1 + x_2$ must be.

</div>

<div class="card card-warning card-glass pad-compact mt-md">

🧩 **XOR** is 1 when the inputs differ: (0, 1) and (1, 0). Find $w_1$, $w_2$ and $b$.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_gates.svg">

</div>

</div>

<!--
**Say:** the truth tables of Lecture 3, computed by a weighted sum and a threshold. The same weights give both gates; only the bias differs.
**Do:** one minute for the XOR puzzle; collect two or three attempts and check one row of each aloud. Every attempt gets a row wrong. Leave it open.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Rosenblatt's Learning **Rule**

The weights so far were set by hand. The rule of 1958 finds them from labelled examples, one at a time.

<!--
**Say:** the rule, one update with the numbers of a real evening, one pass over AND, then the rule on ten years of evenings.
(~0.5 min)
-->

---
hideInToc: true
---

# Why Not Try Every **Line**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **One number: 201 tries**

The threshold was found by trying every $c$ from −6 to 14 °C in steps of 0.1: 201 values, each scored on 3646 evenings.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💥 **Three numbers: 8 million lines**

<v-clicks>

- $w_1$, $w_2$, $b$ on the same grid: $201^3 = 8\,120\,601$ lines
- each scored on 3646 evenings: $3.0 \times 10^{10}$ values of $z$
- ten numbers: $201^{10} = 1.1 \times 10^{23}$ lines

</v-clicks>

</div>

</div>

<div v-click class="card card-success card-glass pad-compact mt-md">

✅ A learning rule never looks at most lines: it starts somewhere and moves the numbers a little, evening by evening, where the errors point.

</div>

<!--
**Say:** three numbers already take about half an hour of plain Python on a laptop; ten would outlast the universe. A network has thousands of numbers, a language model billions.
(~2 min)
-->

---
hideInToc: true
---

# The **Rule**

<div class="card card-info card-glass pad-compact mt-sm">

Take the evenings in turn. For each, compute $\hat{y}$; then change the numbers by the error $y - \hat{y}$, with a **learning rate** $\eta$:

$$
w_1 \leftarrow w_1 + \eta\,(y - \hat{y})\,x_1 \qquad w_2 \leftarrow w_2 + \eta\,(y - \hat{y})\,x_2 \qquad b \leftarrow b + \eta\,(y - \hat{y})
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔀 **Three cases**

| $y$ | $\hat{y}$ | $y - \hat{y}$ | the numbers |
| --- | --- | --- | --- |
| equal | | 0 | stay |
| 1 | 0 | +1 | $w$ gains $\eta\,x$, $b$ gains $\eta$ |
| 0 | 1 | −1 | $w$ loses $\eta\,x$, $b$ loses $\eta$ |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✅ **$z$ moves the right way**

For the same evening, after the update:

$$
z_{\text{new}} = z + \eta\,(y - \hat{y})\,(x_1^2 + x_2^2 + 1)
$$

The bracket is positive: a frost evening called "no frost" gets a larger $z$.

</div>

</div>

<!--
**Say:** only a wrong evening changes anything. One pass over all evenings is an **epoch**.
**If asked:** $\eta$ is the learning rate of Lecture 9's gradient descent. Started from zero weights, this rule draws the same lines for every $\eta$: each number is a multiple of $\eta$. With $\eta = 1$ it adds or subtracts $x$ itself.
(~3 min)
-->

---
hideInToc: true
---

# One Update, with **Numbers**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📅 **1 January 2016, the first evening**

$x = (-4.5,\ 0.85)$; 06:00: −8.3 °C, so $y = 1$.

Start: $w = (0, 0)$, $b = 0$, $\eta = 1$.

</div>

<div class="card card-secondary card-glass pad-compact">

<v-clicks>

- $z = 0 \cdot (-4.5) + 0 \cdot 0.85 + 0 = 0$, so $\hat{y} = 0$: wrong
- $y - \hat{y} = +1$: $x$ is added to $w$, 1 to $b$
- $w = (-4.5,\ 0.85)$, $b = 1$
- $z_{\text{new}} = 20.25 + 0.72 + 1 = 21.97$: frost, right

</v-clicks>

</div>

</div>

<div v-click class="card card-warning card-glass pad-compact mt-md">

⚠️ One update need not be enough: on 10 January 2016, $x = (1.5,\ 0.89)$ with frost, $z$ rises from −4.99 to −0.95, still "no frost".

</div>

<!--
**Do:** click through, each number said aloud.
**Say:** $z_{\text{new}} = z + (x_1^2 + x_2^2 + 1) = 0 + 20.25 + 0.72 + 1$: the formula of the slide before. On 10 January the bracket is 4.04, too small to lift $z$ from −4.99 past 0.
(~2 min)
-->

---
hideInToc: true
---

# AND by the Rule: Epochs **1 and 2**

<div class="note-text mt-sm">

Start: $w = (0, 0)$, $b = 0$, $\eta = 1$. The points in the order (0, 0), (0, 1), (1, 0), (1, 1); the labels 0, 0, 0, 1.

</div>

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| Step | $x$ | $y$ | $w$ before | $b$ before | $z$ | $\hat{y}$ | $y - \hat{y}$ | $w$ after | $b$ after |
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

Step 4 makes (1, 1) right and the three other points wrong; epoch 2 repairs two of them. Four more epochs end at $w = (2, 1)$, $b = -2$: ten updates in all.

</div>

<!--
**Do:** steps 1 to 6 on the board with the room, each number said aloud; then let the room do 7 and 8.
**Say:** with all numbers zero the neuron says 0 everywhere, so the three points of class 0 are right by accident.
(~4 min)
-->

---
hideInToc: true
class: fill
---

# The Ten Updates as **Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

✏️ The line after each update; the red ring marks the point that was wrong. After the tenth, epoch 6 changes nothing: $w = (2, 1)$, $b = -2$ computes AND.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_and_run.svg">

<!--
**Say:** in panel 1 every point is on the frost side: the line is outside the square. It turns and shifts until the corner (1, 1) is alone on its side.
**Say:** the result is not the hand-set $w = (1, 1)$, $b = -1.5$: many lines separate these four points, and the rule stops at the first one it reaches. In the last panel (1, 0) lies exactly on the line, $z = 0$.
(~2 min)
-->

---
hideInToc: true
class: runner-side
---

# The Rule in Python, **Live**

```py {monaco-run} {autorun:false}
def predict(x, w, b):
    if w[0] * x[0] + w[1] * x[1] + b > 0:
        return 1
    return 0

xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
ys = [0, 0, 0, 1]                    # AND
w = [0, 0]
b = 0
for epoch in range(1, 7):
    for i in range(4):
        error = ys[i] - predict(xs[i], w, b)
        w[0] = w[0] + error * xs[i][0]
        w[1] = w[1] + error * xs[i][1]
        b = b + error
    print("epoch", epoch, " w", w, " b", b)
```

<!--
**Do:** run it: after epoch 1 `w [1, 1]`, `b 1`; after epochs 5 and 6 `w [2, 1]`, `b -2`.
**Do:** change `ys` to `[0, 1, 1, 1]`, OR, and run again: from epoch 3 on `w [1, 1]`, `b 0`.
**Say:** the three lines in the inner loop are the rule of the slide, nothing more. `range(1, 7)` counts 1 to 6, `range(4)` 0 to 3.
(~2 min)
-->

---
hideInToc: true
---

# Linearly **Separable**

<div class="card card-info card-glass pad-compact mt-sm">

📖 Labelled points are **linearly separable** when some line has every point of class 1 on one side and every point of class 0 on the other.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **AND: yes**

$w = (1, 1)$, $b = -1.5$ puts (1, 1) alone on its side. On separable points the rule stops after a finite number of updates: the **convergence theorem** (Novikoff, 1962).

</div>

<div class="card card-warning card-glass pad-compact">

## 🚫 **The evenings: no**

A frost evening at 7.8 °C (30 Sep 2017), an evening without frost at −0.4 °C (15 Feb 2016), and 824 evenings between 0 and 6 °C of both kinds.

</div>

</div>

<!--
**Say:** the theorem also says how many updates at most; its proof, three lines of vectors, is for the curious.
**Ask:** with frost and no frost mixed at every temperature from 0 to 6 °C, can a line have all frost evenings on one side? No line can.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Rule on 2551 Evenings Never **Stops**

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ The evenings of 2016 to 2022, in the order of the log, from zero weights. After each pass: 95.2 %, 33.3 %, 92.3 %, 88.6 %, 95.2 % right. In 30 epochs every pass makes 158 to 176 updates.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_rule_evenings.svg">

<!--
**Say:** the clouds overlap: no line has every evening on its side, so some evening is always wrong and the rule always moves. After epoch 2 the line has left the clouds: every evening is "frost", 33.3 %, worse than "never frost".
**If asked:** when one line does separate the classes, the rule stops after a finite number of updates: the convergence theorem, with its proof, for the curious.
(~2 min)
-->

---
hideInToc: true
---

# What the Rule Does Not **Give**

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔁 **An end**

On overlapping classes it never stops. Where it is stopped decides the line: 95.2 % after the first pass, 33.3 % after the second.

</div>

<div class="card card-primary card-glass pad-compact">

## 📏 **A best line**

On separable points it stops at the first line without errors: for AND, $(2, 1)$ and −2, a line that touches (1, 0).

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎲 **How sure**

The output is 1 or 0: an evening at 3.7 °C and one at −10 °C both get 1.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Rosenblatt wrote the rule down; he did not derive it. Why the error times the input?

</div>

<!--
**Say:** three gaps, and one question. A smooth output in place of the step closes all three and answers the question.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# From the Step to the **Sigmoid**

A smooth output: a probability, a loss with a slope everywhere, and an update that follows from it.

<!--
**Say:** one change to the neuron, and the method of Lecture 9 applies: a likelihood, a loss, its slope, a step downhill.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Counting Errors Gives No **Slope**

<div class="card card-info card-glass pad-compact mt-sm">

📉 With $w = (-1, 0)$ the bias $b$ is the threshold. Wrong evenings: flat between jumps, no slope to follow. The cross-entropy: a slope at every $b$, lowest at $b = 3.97$.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_step_loss.svg">

<!--
**Say:** Lecture 9 moved a parameter against the slope of its loss. A staircase has no slope: between two jumps a small change of $b$ changes nothing.
**If asked:** the inset zooms into 2.5 to 5 °C: the count jumps only where an evening's temperature lies, and is flat in between.
(~2 min)
-->

---
hideInToc: true
---

# Frost by Counting, per **Degree**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **All 3646 evenings, by the temperature at 18:00**

| 18:00 | Evenings | Frost | Share |
| --- | --- | --- | --- |
| −1 to 0 °C | 152 | 151 | 0.99 |
| 0 to 1 °C | 156 | 151 | 0.97 |
| 1 to 2 °C | 148 | 139 | 0.94 |
| 2 to 3 °C | 155 | 134 | 0.86 |
| 3 to 4 °C | 134 | 83 | 0.62 |
| 4 to 5 °C | 121 | 39 | 0.32 |
| 5 to 6 °C | 110 | 22 | 0.20 |
| 6 to 7 °C | 98 | 10 | 0.10 |
| 7 to 8 °C | 105 | 2 | 0.02 |

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## 📉 **No jump at 3.8 °C**

The share falls smoothly, from 0.99 to 0.02 over eight degrees. Between 3 and 4 °C, 83 of 134 evenings froze: P(frost) = 0.62.

</div>

<div class="card card-info card-glass pad-compact mt-md">

A step says 1 or 0. The evenings say "62 % of the time".

</div>

</div>

</div>

<!--
**Say:** the conditional probability of Lecture 8, by counting: P(frost | 3 to 4 °C) = 83/134. A smooth curve through these shares is what the neuron should give.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The **Sigmoid**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 〰️ **A smooth step**

$$
\text{sigmoid}(z) = \frac{1}{1 + e^{-z}}
$$

- between 0 and 1 for every $z$
- $\text{sigmoid}(0) = 0.5$
- far from 0, the step

</div>

<div class="card card-secondary card-glass pad-compact mt-md table-compact">

| $z$ | −4 | −2 | −1 | 0 | 1 | 2 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sigmoid | 0.018 | 0.119 | 0.269 | 0.5 | 0.731 | 0.881 | 0.982 |

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_sigmoid.svg">

</div>

</div>

<!--
**Do:** compute sigmoid(1.2) on the board: $e^{-1.2} = 0.301$, and $1/1.301 = 0.769$.
**Say:** σ is the standard deviation in this course, so the sigmoid keeps its name in the formulas.
(~2 min)
-->

---
hideInToc: true
---

# The Output Is a **Probability**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **The logistic neuron**

$$
\hat{y} = \text{sigmoid}(w_1 x_1 + w_2 x_2 + b)
$$

$\hat{y}$ is read as P(frost | $x$). Above 0.5 exactly when $z > 0$: the same line as the step.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **$w = (-1, 0)$, $b = 3.8$, December 2025**

<v-clicks>

- 6 Dec, 1.1 °C: $z = 2.7$, $\hat{y} = 0.94$
- 7 Dec, 2.8 °C: $z = 1.0$, $\hat{y} = 0.73$
- 8 Dec, 2.6 °C: $z = 1.2$, $\hat{y} = 0.77$
- 9 Dec, 0.4 °C: $z = 3.4$, $\hat{y} = 0.97$

</v-clicks>

</div>

</div>

<div v-click class="card card-info card-glass pad-compact mt-md">

06:00 the next morning: +0.4 °C after the 6th and +0.1 °C after the 7th, no frost; −2.0 °C after the 8th and −4.8 °C after the 9th, frost.

</div>

<!--
**Say:** the step said 1 for all four. The sigmoid says how sure: 0.94 for the 6th, which did not freeze.
**If asked:** P(frost | $x$) reads "the probability of frost given the inputs", as the conditional probabilities counted in Lecture 8. Statisticians call this model logistic regression.
(~2 min)
-->

---
hideInToc: true
---

# The Probability of What **Happened**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🎲 **One evening: frost with probability $\hat{y}$**

$$
P(y) = \hat{y}^{\,y}\,(1 - \hat{y})^{\,1 - y}
$$

- $y = 1$: $\hat{y}^1 (1 - \hat{y})^0 = \hat{y}$
- $y = 0$: $\hat{y}^0 (1 - \hat{y})^1 = 1 - \hat{y}$

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **6 to 9 December 2025**

| Evening | $\hat{y}$ | $y$ | $P(y)$ |
| --- | --- | --- | --- |
| 6 Dec | 0.937 | 0 | 0.063 |
| 7 Dec | 0.731 | 0 | 0.269 |
| 8 Dec | 0.769 | 1 | 0.769 |
| 9 Dec | 0.968 | 1 | 0.968 |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

$P(y)$ is the probability the neuron gave to what really happened. A good neuron makes it large on every evening.

</div>

<!--
**Say:** the formula is bookkeeping: anything to the power 0 is 1, so only one of the two factors is left.
**If asked:** a variable that is 1 with probability $\hat{y}$ and 0 otherwise is a Bernoulli variable, a coin with a bias.
(~2 min)
-->

---
hideInToc: true
---

# From the Likelihood to the **Loss**

<div class="card card-primary card-glass pad-compact mt-sm">

**The likelihood.** Taken as independent, the evenings' probabilities multiply:

$$
L = \prod_{i=1}^{N} P(y_i)
$$

Four evenings: $L = 0.063 \cdot 0.269 \cdot 0.769 \cdot 0.968 = 0.0126$.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

**The loss.** Minus the logarithm of $L$, per evening: the product becomes a sum, the **cross-entropy**:

$$
\text{loss} = -\frac{1}{N} \ln L = -\frac{1}{N} \sum_{i=1}^{N} \ln P(y_i)
$$

Four evenings: $(2.765 + 1.313 + 0.263 + 0.033)/4 = 1.094$.

</div>

<div class="card card-success card-glass pad-compact mt-md">

The largest likelihood is the smallest loss: the numbers that make what happened most probable.

</div>

<!--
**Say:** Lecture 9 took the same steps with the Gaussian and arrived at χ². ∏ is the product, as ∑ is the sum.
**Say:** the logarithm turns the product into a sum, $\ln(ab) = \ln a + \ln b$. At the start of training, 2551 factors of 0.5 make $10^{-768}$, too small for a float, whose smallest is about $10^{-308}$; the sum of logarithms is −1768.
**If asked:** neighbouring evenings are alike (Lecture 8), so "independent" is an assumption; it makes the numbers less certain, not the line wrong.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# What the Loss **Charges**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **A frost evening, $y = 1$**

| $\hat{y}$ | 0.99 | 0.9 | 0.5 | 0.1 | 0.01 |
| --- | --- | --- | --- | --- | --- |
| $-\ln \hat{y}$ | 0.010 | 0.105 | 0.693 | 2.303 | 4.605 |

</div>

<div class="stack-tight">

<div class="card card-success card-glass pad-compact">

✅ Right and sure: almost nothing

</div>

<div class="card card-secondary card-glass pad-compact">

⚖️ Undecided, 0.5: $\ln 2 = 0.693$

</div>

<div class="card card-warning card-glass pad-compact">

⚠️ Wrong and sure: the most, without limit

</div>

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_cross_entropy.svg">

</div>

</div>

<!--
**Say:** the 6th costs 2.77: the neuron was 94 % sure of frost, and none came. Every factor of 10 lost in the probability of what happened adds 2.3 to the loss.
(~2 min)
-->

---
hideInToc: true
---

# The Loss of Four Evenings, **Live**

```py {monaco-run} {autorun:false}
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# 6 to 9 December 2025: [temperature, humidity, frost]
evenings = [[1.1, 0.65, 0], [2.8, 0.81, 0], [2.6, 0.85, 1], [0.4, 0.86, 1]]
w = [-1.0, 0.0]
b = 3.8                                   # <-- try 3.0
total = 0
for e in evenings:
    y_hat = sigmoid(w[0] * e[0] + w[1] * e[1] + b)
    if e[2] == 1:
        total = total - math.log(y_hat)
    else:
        total = total - math.log(1 - y_hat)
print(round(total / len(evenings), 3))    # 1.094
```

<!--
**Do:** run it: 1.094. Then `b = 3.0`: 0.856, a lower loss. The two evenings without frost wanted a lower threshold.
**Say:** `math.log` is the natural logarithm, ln; `math.exp(-z)` is $e^{-z}$.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **Gradient**

The slope of the loss in each number, and a step downhill.

<!--
**Say:** the derivative of Lecture 9, now in three numbers at once.
(~0.5 min)
-->

---
hideInToc: true
---

# The Slope of the Loss: $(\hat{y} - y)\,x$

<div class="card card-primary card-glass pad-compact mt-sm">

For one evening, the loss $-\ln P(y)$ changes with each number as

$$
\frac{\partial\,\text{loss}}{\partial w_1} = (\hat{y} - y)\,x_1 \qquad \frac{\partial\,\text{loss}}{\partial w_2} = (\hat{y} - y)\,x_2 \qquad \frac{\partial\,\text{loss}}{\partial b} = \hat{y} - y
$$

The error times the input.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **8 Dec 2025, $w = (-1, 0)$, $b = 3.8$**

$\hat{y} - y = 0.769 - 1 = -0.231$

<v-clicks>

- $\partial\,\text{loss}/\partial w_1 = -0.231 \cdot 2.6 = -0.602$
- $\partial\,\text{loss}/\partial w_2 = -0.231 \cdot 0.85 = -0.197$
- $\partial\,\text{loss}/\partial b = -0.231$

</v-clicks>

</div>

<div class="card card-accent card-glass pad-compact">

## 🧭 **What the signs say**

All three are negative: raising $w_1$, $w_2$ or $b$ lowers this evening's loss.

An evening the neuron has right and sure, $\hat{y} \approx y$, hardly pulls; one it has wrong and sure pulls most.

</div>

</div>

<!--
**Say:** $\partial$ is the derivative of Lecture 9 with the other numbers held fixed. No logarithm and no exponential is left in the result.
**If asked:** the derivation, by the chain rule through $z$ and the sigmoid, is in the section for the curious.
(~3 min)
-->

---
hideInToc: true
---

# The Slope, Checked with a **Nudge**

```py {monaco-run} {autorun:false}
import math

def loss(w1):                         # 8 Dec 2025: x = (2.6, 0.85), y = 1
    z = w1 * 2.6 + 0.0 * 0.85 + 3.8
    return -math.log(1 / (1 + math.exp(-z)))

print(round((loss(-1.0 + 0.001) - loss(-1.0)) / 0.001, 4))   # -0.6012
y_hat = 1 / (1 + math.exp(-1.2))
print(round((y_hat - 1) * 2.6, 4))                           # -0.6018
```

<div class="note-text mt-sm">

Raise $w_1$ by 0.001 and compute the loss again: it changes by −0.6012 per unit of $w_1$. The formula gives −0.6018. A slope worked out on paper is checked this way before a program trusts it.

</div>

<!--
**Do:** run it; then change the nudge to 0.0001 in both places: the two numbers agree to more digits.
**Say:** the small difference is the bend of the loss over the step of 0.001.
(~2 min)
-->

---
hideInToc: true
---

# One Step **Downhill**

<div class="card card-info card-glass pad-compact mt-sm">

Each number moves against its slope, $\eta$ times the slope:

$$
w_1 \leftarrow w_1 - \eta\,(\hat{y} - y)\,x_1 \qquad w_2 \leftarrow w_2 - \eta\,(\hat{y} - y)\,x_2 \qquad b \leftarrow b - \eta\,(\hat{y} - y)
$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **8 Dec 2025, $\eta = 0.1$**

<v-clicks>

- $w_1 = -1 - 0.1 \cdot (-0.602) = -0.940$
- $w_2 = 0 - 0.1 \cdot (-0.197) = 0.020$
- $b = 3.8 - 0.1 \cdot (-0.231) = 3.823$

</v-clicks>

</div>

<div class="card card-success card-glass pad-compact">

## 📉 **The same evening again**

<v-clicks>

- $z = -0.940 \cdot 2.6 + 0.020 \cdot 0.85 + 3.823 = 1.396$
- $\hat{y} = 0.802$, up from 0.769
- loss 0.221, down from 0.263

</v-clicks>

</div>

</div>

<!--
**Do:** click through the three new numbers, then the evening again.
**Say:** the humidity, ignored so far, gets its first weight from this one evening.
**If asked:** the same step raises the loss of the two evenings without frost, 6 and 7 December; the next steps, on them, pull back. Over many evenings the line settles where the pulls balance.
(~2 min)
-->

---
hideInToc: true
---

# The Mean Slope over Four **Evenings**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

## 🔢 **$w = (-1, 0)$, $b = 3.8$: each evening's slope, then the mean**

| Evening | $y$ | $\hat{y} - y$ | $(\hat{y} - y)\,x_1$ | $(\hat{y} - y)\,x_2$ |
| --- | --- | --- | --- | --- |
| 6 Dec, 1.1 °C, 0.65 | 0 | 0.937 | 1.031 | 0.609 |
| 7 Dec, 2.8 °C, 0.81 | 0 | 0.731 | 2.047 | 0.592 |
| 8 Dec, 2.6 °C, 0.85 | 1 | −0.231 | −0.602 | −0.197 |
| 9 Dec, 0.4 °C, 0.86 | 1 | −0.032 | −0.013 | −0.028 |
| **Mean** | | **0.351** | **0.616** | **0.244** |

</div>

<div class="card card-success card-glass pad-compact mt-md">

📉 The mean is the slope of the loss of all four. One step, $\eta = 0.1$: $w = (-1.062,\ -0.024)$, $b = 3.765$; the loss of the four falls from 1.094 to 1.040.

</div>

<!--
**Say:** the two evenings without frost pull the threshold down, the two with frost pull it up; the mean decides. This is Lecture 9's way: one step per pass, from the mean slope of all points.
**If asked:** after the step the 6th has ŷ = 0.93 and the 7th 0.68: both a little closer to 0.
(~2 min)
-->

---
hideInToc: true
---

# Rosenblatt's Rule Follows from the **Loss**

<div class="card card-success card-glass pad-compact mt-sm">

Downhill, $-\eta\,(\hat{y} - y)\,x$, is $+\eta\,(y - \hat{y})\,x$: Rosenblatt's rule, letter for letter.

</div>

<div class="card card-primary card-glass pad-compact mt-md table-compact">

| Model | Output $\hat{y}$ | Loss of one point | Update of $w_1$ | Who moves the line |
| --- | --- | --- | --- | --- |
| Straight line, least squares | $w_1 x_1 + b$ | $\tfrac{1}{2}(\hat{y} - y)^2$ | $\eta\,(y - \hat{y})\,x_1$ | every point, by its residual |
| Rosenblatt, 1958 | $\text{step}(z)$ | none | $\eta\,(y - \hat{y})\,x_1$ | only wrong points, all by the same amount |
| Logistic neuron | $\text{sigmoid}(z)$ | $-\ln P(y)$ | $\eta\,(y - \hat{y})\,x_1$ | every point, by its error in probability |

</div>

<div class="card card-info card-glass pad-compact mt-md">

The answer to "why the error times the input": it is the slope of the loss. With the sigmoid, $y - \hat{y}$ is never exactly 0, so every evening pulls a little.

</div>

<!--
**Say:** the first row is the straight line of Lecture 9 in today's letters: the slope of the squared residual is the residual times the input. Three models, one update.
**If asked:** the squared residual with a sigmoid output would give the slope an extra factor $\hat{y}(1 - \hat{y})$: a sure and wrong evening would hardly pull.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Loss Has One Lowest **Point**

<div class="fig-fill grid-side mt-sm">

<div class="card card-info card-glass pad-compact">

⌣ The loss of the 2551 training evenings for every $w_1$ and $b$, with $w_2 = 0$: one bowl, no second valley. Its lowest point, $w_1 = -1.05$, $b = 4.17$, is the threshold $4.17 / 1.05 = 3.97$ °C.

Downhill from any start ends there.

</div>

<img class="fig" src="/figures/viz_perceptron_bowl.svg">

</div>

<!--
**Say:** contour lines, as on a map: each joins the numbers with the same loss. The threshold neuron, the square, sits near the bottom: loss 0.1086 against 0.1080 at the lowest point.
**If asked:** the loss curves upward in every direction, so a step downhill never ends in a false valley. Networks with hidden layers lose this.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Train and **Test**

A rule is scored on evenings it has not seen.

<!--
**Say:** the update of the last section, run over seven years of evenings, and scored on three others.
(~0.5 min)
-->

---
hideInToc: true
---

# Train on 2016–2022, Test on **2023–2025**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏋️ **Training: 2016 to 2022**

2551 evenings, 850 of them with frost. The numbers $w_1$, $w_2$, $b$ are learned from these alone.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧪 **Test: 2023 to 2025**

1095 evenings, 379 with frost. Used once, at the end, to score the result.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

✂️ Split by years, not evening by evening at random: neighbouring evenings are alike, and a test evening would have its own yesterday among the training evenings.

</div>

<!--
**Ask:** why not score on the training evenings? A rule can fit the evenings it has seen; the question is the next winter.
**Say:** the threshold 3.8 °C was found on all evenings, the test years included. Chosen on the training years alone it is again 3.8 °C: 95.6 % there.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Five Passes over the Training **Evenings**

<div class="card card-primary card-glass pad-compact mt-sm">

📉 The update after each evening, $\eta = 0.01$, from zero, in the order of the log. The loss falls from ln 2 = 0.693 to 0.130 after one pass and to 0.110 after five; right on 95.5 % of the training evenings.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_training.svg">

<!--
**Say:** from zero numbers every $\hat{y}$ is 0.5 and each evening costs ln 2. After five passes $w = (-0.877, 1.704)$, $b = 2.227$: frost below 3.5 °C at humidity 0.5 and below 4.5 °C at 1.0. More passes hardly move the line: 0.1085 after twenty.
**If asked:** the update after each evening is Rosenblatt's way; the mean of the slopes over all evenings, one step per pass, is Lecture 9's way. Both go downhill.
(~2 min)
-->

---
hideInToc: true
---

# The Training Loop in Plain **Python**

```python {all|4|5-7|all}
for epoch in range(5):
    for i in range(len(xs)):
        x = xs[i]
        error = ys[i] - sigmoid(w[0] * x[0] + w[1] * x[1] + b)
        w[0] = w[0] + 0.01 * error * x[0]
        w[1] = w[1] + 0.01 * error * x[1]
        b = b + 0.01 * error
```

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

| After epoch | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Loss | 0.693 | 0.130 | 0.117 | 0.113 | 0.111 | 0.110 |
| Right | 66.7 % | 95.5 % | 95.6 % | 95.5 % | 95.5 % | 95.5 % |

</div>

<div class="card card-info card-glass pad-compact">

The step's `predict` became a `sigmoid`, and each change is $\eta = 0.01$ times as large. `xs`: the 2551 training evenings as $[x_1, x_2]$; `ys`: their labels.

</div>

</div>

<!--
**Say:** the AND runner, line for line: `predict` in the error line became the sigmoid, and each change is multiplied by η = 0.01. Seven lines train the neuron.
**Say:** epoch 0 is the start: every ŷ = 0.5, so "never frost" by the 0.5 cut, 66.7 % of the training evenings.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# P(frost) from the Trained **Neuron**

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

🎲 The trained neuron at humidity 0.85: P(frost) 0.94 at 1 °C, 0.74 at 3 °C, 0.33 at 5 °C.

8 December 2025, 2.6 °C: **0.80**.

The dots count the test evenings: the share with frost per 1 °C, with its ±.

</div>

<img class="fig" src="/figures/viz_perceptron_probability.svg">

</div>

<!--
**Say:** the neuron's curve against counting, as Lecture 8 counted probabilities: it runs through the shares within their ±, on evenings it never saw.
**Ask:** at 0.80, do you cover the plants tonight?
(~2 min)
-->

---
hideInToc: true
---

# Tonight's Evening Through the Neuron, **Live**

```py {monaco-run} {autorun:false}
import math
w = [-0.877, 1.704]           # learned from the evenings of 2016 to 2022
b = 2.227
temp = 2.6                    # <-- tonight at 18:00, °C
humidity = 0.85               # <-- tonight at 18:00, 0 to 1
z = w[0] * temp + w[1] * humidity + b
print(round(z, 3), round(1 / (1 + math.exp(-z)), 2))   # 1.395 0.8
```

<div class="note-text mt-sm">Three numbers learned from seven years of evenings, and one evening's two inputs: the whole forecast.</div>

<!--
**Do:** type this evening's 18:00 temperature and humidity (from any weather service), then ▶.
**Ask:** frost or not, and how sure? Check tomorrow at 06:00.
(~2 min)
-->

---
hideInToc: true
---

# How Sure Is an **Accuracy**?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **A share of $N$ evenings**

Each test evening is right or wrong. The standard error of a share $p$ of $N$:

$$
\sqrt{\frac{p\,(1 - p)}{N}} = \sqrt{\frac{0.961 \cdot 0.039}{1095}} = 0.006
$$

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **The logistic neuron, 2023 to 2025**

1052 of 1095 test evenings right:

$$
96.1 \pm 0.6\,\%
$$

"Never frost" on the same evenings: 716, 65.4 ± 1.4 %.

</div>

</div>

<!--
**Say:** an accuracy is a measurement and is quoted with its ± like any other. $p(1 - p)$ is the variance of a 0-or-1 value.
**Say:** to halve the ±, the test set must be four times as large.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Four Rules on the Test **Years**

<div class="card card-info card-glass pad-compact mt-sm">

🏁 The 1095 evenings of 2023 to 2025. The three rules that use the temperature differ by less than their ±; the neuron and the threshold rule agree on 1087 evenings.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_test.svg">

<!--
**Say:** the neuron learned the threshold rule: its line stands near 4 °C, nearly upright. Bars from zero, as in Lecture 7.
**If asked:** a neuron with the temperature alone learns the threshold 3.93 °C and is also right on 1052: the humidity adds nothing these evenings can show.
(~2 min)
-->

---
hideInToc: true
---

# Accuracy on Seen and Unseen **Evenings**

<div class="card card-primary card-glass pad-compact mt-sm">

| Rule | Numbers it keeps | 2016–2022, seen | 2023–2025, unseen |
| --- | --- | --- | --- |
| Logistic neuron | 3 | 95.5 % | 96.1 % |
| Frost if most years froze on that date | 366 | 91.9 % | 89.5 % |
| Frost if the nearest training evening froze | 7653 | 98.8 % | 93.1 % |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The rule that keeps every training evening scores best on those and worse on new ones. Only unseen evenings tell how good a rule is.

</div>

<!--
**Say:** the nearest-evening rule keeps all 2551 evenings, three numbers each, and answers like the most similar one. On its own evenings it is nearly always right; on 2023 to 2025 it is worse than three numbers.
**If asked:** the date rule keeps one answer for each of the 366 dates of the year.
(~2 min)
-->

---
hideInToc: true
---

# Missed Frosts and False **Alarms**

<div class="card card-primary card-glass pad-compact mt-sm">

The 379 frost evenings and 716 others of 2023 to 2025, with "frost" said when $\hat{y}$ is above a cut:

| Cut on $\hat{y}$ | Frosts caught | Frosts missed | False alarms | Right |
| --- | --- | --- | --- | --- |
| 0.5 | 361 | 18 | 25 | 96.1 % |
| 0.3 | 369 | 10 | 52 | 94.3 % |
| 0.2 | 374 | 5 | 68 | 93.3 % |

</div>

<div class="card card-success card-glass pad-compact mt-md">

🌱 A gardener who loses the plants to a missed frost takes 0.2: a quarter of the misses, nearly three times the alarms, a lower accuracy. The cut is a choice of which error costs more.

</div>

<!--
**Ask:** which cut would a road service choose, which a gardener?
**Say:** one accuracy hides two kinds of error; the probability lets each user choose.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# A Model as an **Object**

Three numbers, and two things done with them: predict and fit.

<!--
**Say:** the trained neuron is three numbers; a program that uses it needs those numbers and two functions. Python keeps them together in an object.
(~0.5 min)
-->

---
hideInToc: true
---

# What a Model Holds and **Does**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🗃️ **It holds its numbers**

$w_1 = -0.877$, $w_2 = 1.704$, $b = 2.227$: the whole trained logistic neuron.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **It does two things**

- **predict**: inputs in, 0 or 1 out
- **fit**: evenings and labels in, its numbers change

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧩 Values kept together with the functions that use them form an **object**; its type is a **class**. A `str` keeps its text and has `split`; a `list` keeps its values and has `append`.

</div>

<!--
**Say:** Lecture 5 called `line.split(",")` a method: a function that belongs to the value before the dot. A model is the same idea with numbers inside.
**If asked:** Lecture 5's section for the curious wrote a class `Hour`, with a time, a temperature and a method `is_missing()`.
(~2 min)
-->

---
hideInToc: true
---

# The Same Code as a Class: `Perceptron`

<div class="code-beside mt-sm">

````md magic-move {lines: true}
```py
def predict(x, w, b):
    z = w[0] * x[0] + w[1] * x[1] + b
    if z > 0:
        return 1
    return 0
```
```py
class Perceptron:
    def __init__(self):
        self.w = [0.0, 0.0]
        self.b = 0.0
```
```py {6-10}
class Perceptron:
    def __init__(self):
        self.w = [0.0, 0.0]
        self.b = 0.0

    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if z > 0:
            return 1
        return 0
```
```py {12-18}
class Perceptron:
    def __init__(self):
        self.w = [0.0, 0.0]
        self.b = 0.0

    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if z > 0:
            return 1
        return 0

    def fit(self, xs, ys, epochs):
        for epoch in range(epochs):
            for i in range(len(xs)):
                error = ys[i] - self.predict(xs[i])
                self.w[0] = self.w[0] + error * xs[i][0]
                self.w[1] = self.w[1] + error * xs[i][1]
                self.b = self.b + error
```
````

<div class="card card-info card-glass pad-compact">

- `Perceptron()` makes an object and runs `__init__` once
- `self` is that object; `self.w` keeps a value in it
- a `def` inside the class is a **method**: `predict` reads `self.w`, `fit` changes it

</div>

</div>

<style>
.code-beside { display: grid; grid-template-columns: minmax(0, 1.75fr) minmax(0, 1fr); gap: var(--gap-md); align-items: start; }
</style>

<!--
**Do:** four steps: the function of the slide before; the class with its two numbers; `predict` moved in, `w` and `b` now `self.w` and `self.b`; `fit`, the loop of the AND runner.
**Say:** nothing new is computed: the same lines, with the numbers kept in the object instead of passed around.
(~3 min)
-->

---
hideInToc: true
class: runner-side
---

# Fit and Predict, **Live**

```py {monaco-run} {autorun:false}
class Perceptron:
    def __init__(self):
        self.w = [0, 0]
        self.b = 0
    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if z > 0:
            return 1
        return 0
    def fit(self, xs, ys, epochs):
        for epoch in range(epochs):
            for i in range(len(xs)):
                error = ys[i] - self.predict(xs[i])
                self.w[0] = self.w[0] + error * xs[i][0]
                self.w[1] = self.w[1] + error * xs[i][1]
                self.b = self.b + error

xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
model = Perceptron()
model.fit(xs, [0, 0, 0, 1], 6)       # AND, six epochs
print(model.w, model.b)              # [2, 1] -2
print(model.predict([1, 1]))         # 1
```

<!--
**Do:** run it: `[2, 1] -2`, the numbers of the table by hand, and 1 for (1, 1).
**Do:** add `other = Perceptron()` and `print(other.w)`: `[0, 0]`. Each object keeps its own numbers.
**Say:** fit on the 2551 training evenings, five passes, the same class gives $w = (-1.2, 1.09)$, $b = 3$, and 95.5 % on the test years.
(~2 min)
-->

---
hideInToc: true
---

# Why the Numbers Live in the **Object**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 👯 **Two models, side by side**

`frost = Perceptron()` and `gate = Perceptron()` each keep their own `w` and `b`: one trained on the evenings, one on AND.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧳 **Nothing to carry**

`model.predict(x)` needs only the evening: the numbers travel with the model.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔄 **Change inside, same calls**

Training with the sigmoid changes the inside of `fit`. Code that calls `fit` and `predict` stays as it is.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every model of a machine-learning library is such an object, with the same two calls: fit on training data, predict on new data.

</div>

<!--
**Say:** this is why the libraries of the seminars are built from classes: a model is numbers plus methods.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The Limit: **XOR**

Four points that no single line separates.

<!--
**Say:** back to the puzzle of the gates slide.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# **XOR**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact table-compact">

## ⊕ **Exclusive or**

| $x_1$ | $x_2$ | AND | OR | XOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

Class 1 lies on one diagonal of the square, class 0 on the other. Each line tried leaves a point on the wrong side; that is not yet a proof.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_xor_lines.svg">

</div>

</div>

<!--
**Say:** every attempt of the room at the puzzle left a point on the wrong side. Trying lines proves nothing: there are infinitely many.
(~2 min)
-->

---
hideInToc: true
---

# No Line Exists: Four **Inequalities**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📝 **What a neuron for XOR needs**

| Point | Label | Needed | Condition |
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

The same number cannot be both.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

🚧 No $w_1$, $w_2$, $b$ satisfy all four: XOR is not **linearly separable**. One neuron draws one line.

</div>

<!--
**Do:** write the four conditions with the room: each is $z$ of that point. Then add.
**Say:** the result holds for every line and every way of training.
(~3 min)
-->

---
hideInToc: true
---

# What the Two Rules Do on **XOR**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔁 **Rosenblatt's rule**

From zero: 2, 3, then 4 updates in every epoch, the same four for ever. The convergence theorem assumes a separating line; there is none.

</div>

<div class="card card-secondary card-glass pad-compact">

## 〰️ **The logistic neuron**

The lowest loss is at $w = (0, 0)$, $b = 0$: $\hat{y} = 0.5$ for all four points, loss $\ln 2 = 0.693$. The best one line can do is to know nothing.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Both behave as their mathematics says. A second line, and a neuron that combines two, solve XOR.

</div>

<!--
**Say:** from any start the logistic neuron ends at zero: by symmetry, any tilt helps two points and hurts the other two by as much.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Wrap-up**

The answer for 8 December 2025, and how sure it is.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# Will It Freeze Tonight: the **Answers**

<div class="card card-primary card-glass pad-compact mt-sm">

| Rule | Learned from | Test evenings right, 2023–2025 | 8 Dec 2025: 2.6 °C, 0.85 |
| --- | --- | --- | --- |
| Never frost | nothing | 65.4 ± 1.4 % | no frost |
| Frost below 3.8 °C | every threshold, tried on 2016–2022 | 96.1 ± 0.6 % | frost |
| Rosenblatt's rule, 5 epochs | 2016–2022 | 95.5 ± 0.6 % | frost, $z = 0.81$ |
| Logistic neuron, 5 passes | 2016–2022 | 96.1 ± 0.6 % | frost, P = 0.80 |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ 06:00 on 9 December 2025: −2.0 °C. Every rule that looks at the temperature said frost; the logistic neuron also said how sure.

</div>

<!--
**Say:** the opening question in the room's own numbers.
**Ask:** point at each row: which slide did it come from?
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Score a classifier against the **baseline** "never frost" and a **threshold** rule

</div>

<div class="card card-success card-glass pad-compact">

✅ Push an evening through a **neuron**, $z = w_1 x_1 + w_2 x_2 + b$, and draw its **line**

</div>

<div class="card card-success card-glass pad-compact">

✅ Apply **Rosenblatt's rule** by hand, and say why it never stops on overlapping classes

</div>

<div class="card card-success card-glass pad-compact">

✅ Turn $z$ into a probability with the **sigmoid**, and the likelihood into the **cross-entropy**

</div>

<div class="card card-success card-glass pad-compact">

✅ Take a step downhill with $(\hat{y} - y)\,x$, and quote a **test accuracy** with its ±

</div>

<div class="card card-success card-glass pad-compact">

✅ Keep a model's numbers in an **object** with `fit` and `predict`, and show that no line computes **XOR**

</div>

</div>

<!--
**Say:** one card per section of the lecture, each with its numbers from the weather log.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

When the rule stops, the distance from the line, the slope by the chain rule, where the sigmoid comes from, and three dates.

<!--
**Say:** optional, for time left at the end or for after the lecture.
(~0.5 min)
-->

---
hideInToc: true
---

# The Perceptron Convergence **Theorem**

<div class="card card-info card-glass pad-compact mt-sm">

Write the bias as a weight on a constant input 1: $\tilde{x} = (1, x_1, x_2)$ and $\tilde{w} = (b, w_1, w_2)$ give $z = \tilde{w} \cdot \tilde{x}$. Write the labels as signs: $t = 2y - 1$ is $+1$ or $-1$.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📜 **Assumed**

1. The training set is finite
2. It is separable with a margin: some $\tilde{w}^*$ of length 1 and some $\gamma > 0$ give $t_i\,(\tilde{w}^* \cdot \tilde{x}_i) \ge \gamma$ for every point
3. No point is longer than $R$: $\lVert \tilde{x}_i \rVert \le R$
4. The rule starts from $\tilde{w} = 0$

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Then**

The rule makes at most

$$
k \le \frac{R^2}{\gamma^2}
$$

updates, in any order of the points and for any $\eta > 0$. After the last one every point is right.

</div>

</div>

<div class="note-text mt-sm">

The theorem bounds the number of updates, not epochs, and says nothing about classes that overlap. This form of the bound is A. Novikoff's, 1962.

</div>

---
hideInToc: true
---

# Proof, Part 1: Each Update Turns $\tilde{w}$ Towards $\tilde{w}^*$

<div class="card card-info card-glass pad-compact mt-sm">

An update happens only at a wrong point, and there $y - \hat{y} = t$. So every update is $\tilde{w} \leftarrow \tilde{w} + \eta\,t\,\tilde{x}$.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📈 **One update**

The dot product with $\tilde{w}^*$, and assumption 2:

$$
\begin{aligned}
\tilde{w}^* \cdot \tilde{w}_{\text{new}} &= \tilde{w}^* \cdot \tilde{w} + \eta\,t\,(\tilde{w}^* \cdot \tilde{x}) \\
&\ge \tilde{w}^* \cdot \tilde{w} + \eta\,\gamma
\end{aligned}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **After $k$ updates**

From $\tilde{w} = 0$, each update adds at least $\eta\,\gamma$:

$$
\tilde{w}^* \cdot \tilde{w}_k \ge k\,\eta\,\gamma
$$

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**AND**, with $\tilde{w}^* = (-3, 2, 2)/\sqrt{17}$, $\gamma = 1/\sqrt{17} = 0.243$, $\eta = 1$: after the tenth update $\tilde{w} = (-2, 2, 1)$ and $\tilde{w}^* \cdot \tilde{w} = 12/\sqrt{17} = 2.91$, above $10\,\gamma = 2.43$.

</div>

---
hideInToc: true
---

# Proof, Part 2: The Length Grows **Slowly**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **One update**

$$
\begin{aligned}
\lVert \tilde{w}_{\text{new}} \rVert^2 &= \lVert \tilde{w} \rVert^2 + 2\,\eta\,t\,(\tilde{w} \cdot \tilde{x}) \\
&\quad + \eta^2\,\lVert \tilde{x} \rVert^2 \\
&\le \lVert \tilde{w} \rVert^2 + \eta^2 R^2
\end{aligned}
$$

The point was wrong, so $t\,(\tilde{w} \cdot \tilde{x}) \le 0$: the middle term is not positive.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **After $k$ updates**

$$
\begin{aligned}
\lVert \tilde{w}_k \rVert^2 &\le k\,\eta^2 R^2 \\
\lVert \tilde{w}_k \rVert &\le \sqrt{k}\;\eta\,R
\end{aligned}
$$

The length grows at most like $\sqrt{k}$.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

**AND**: the longest point is $(1, 1, 1)$, $R^2 = 3$. After the tenth update $\tilde{w} = (-2, 2, 1)$ has $\lVert \tilde{w} \rVert^2 = 9$, below $10 \cdot 3 = 30$.

</div>

---
hideInToc: true
class: fill
---

# Proof, Part 3: The Two Bounds **Meet**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 🤝 **Combine**

A dot product is at most the product of the lengths, and $\tilde{w}^*$ has length 1:

$$
k\,\eta\,\gamma \le \tilde{w}^* \cdot \tilde{w}_k \le \lVert \tilde{w}_k \rVert \le \sqrt{k}\;\eta\,R
$$

so $\sqrt{k} \le R/\gamma$, and $k \le R^2/\gamma^2$.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔢 **AND**

$\gamma^2 = 1/17$, $R^2 = 3$: at most $3 \cdot 17 = 51$ updates. The run needed 10.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_proof.svg">

</div>

</div>

---
hideInToc: true
class: fill
---

# $w$ Stands at a Right Angle to the **Line**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## ⊥ **Two points $q_1$, $q_2$ on the line**

$$
\begin{aligned}
w \cdot q_1 + b &= 0 \\
w \cdot q_2 + b &= 0 \\
\text{subtract:}\quad w \cdot (q_1 - q_2) &= 0
\end{aligned}
$$

$q_1 - q_2$ runs along the line, so $w$ is at a right angle to it.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ➡️ **$w$ points to the side of class 1**

A step from $x$ to $x + s\,w$ changes $z$ by $s\,\lVert w \rVert^2$, which is positive.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_line.svg">

</div>

</div>

---
hideInToc: true
---

# The **Distance** of a Point from the Line

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📏 **Derivation**

From $x$ straight to the line, to $x_0$, along $w/\lVert w \rVert$, a length $d$:

$$
x = x_0 + d\,\frac{w}{\lVert w \rVert}
$$

Dot product with $w$, add $b$, use $w \cdot x_0 + b = 0$:

$$
z = d\,\lVert w \rVert \quad\Longrightarrow\quad d = \frac{z}{\lVert w \rVert}
$$

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **$w = (3, 4)$, $b = -10$**

$x = (4, 2)$: $z = 12 + 8 - 10 = 10$ and $\lVert w \rVert = \sqrt{9 + 16} = 5$, so $d = 2$.

$x = (1, 0.5)$: $z = -5$ and $d = -1$, on the other side.

8 Dec 2025 under the trained neuron: $z = 1.395$, $\lVert w \rVert = 1.917$, $d = 0.73$.

</div>

</div>

---
hideInToc: true
class: fill
---

# What $w$ and $b$ **Do**

<div class="card card-info card-glass pad-compact mt-sm">

The direction of $w$ sets the direction of the line; $b$ shifts it, to $\lvert b \rvert / \lVert w \rVert$ from the origin; $w$ and $b$ times 2 leave it where it is, and double every $z$.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_perceptron_wb.svg">

---
hideInToc: true
class: fill
---

# The Slope of the **Sigmoid**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## ✏️ **Chain rule, $u = 1 + e^{-z}$**

$$
\begin{aligned}
\frac{d}{dz}\,u^{-1} &= -u^{-2} \cdot (-e^{-z}) \\[4pt]
&= \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} \\[4pt]
&= \text{sigmoid}(z)\,\bigl(1 - \text{sigmoid}(z)\bigr)
\end{aligned}
$$

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

At $z = 0$: $0.5 \cdot 0.5 = 0.25$, the largest. At $z = 2$: $0.881 \cdot 0.119 = 0.105$. Never zero; small where the neuron is sure.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_sigmoid_slope.svg">

</div>

</div>

---
hideInToc: true
---

# The Slope of the Loss by the **Chain Rule**

<div class="card card-primary card-glass pad-compact mt-sm">

$$
w_1 \;\to\; z \;\to\; \hat{y} = \text{sigmoid}(z) \;\to\; \text{loss} = -\bigl[\,y \ln \hat{y} + (1 - y) \ln (1 - \hat{y})\bigr]
$$

so

$$
\frac{\partial\,\text{loss}}{\partial w_1} = \frac{\partial\,\text{loss}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w_1}
$$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📉 **Loss by output**

$$
\begin{aligned}
&-\frac{y}{\hat{y}} + \frac{1 - y}{1 - \hat{y}} \\[4pt]
&= \frac{\hat{y} - y}{\hat{y}\,(1 - \hat{y})}
\end{aligned}
$$

</div>

<div class="card card-accent card-glass pad-compact">

## 〰️ **Output by sum**

$$
\hat{y}\,(1 - \hat{y})
$$

the slope of the sigmoid

</div>

<div class="card card-info card-glass pad-compact">

## ➕ **Sum by weight**

$$
\frac{\partial z}{\partial w_1} = x_1, \quad \frac{\partial z}{\partial b} = 1
$$

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

The product: $\hat{y}\,(1 - \hat{y})$ cancels, and $\partial\,\text{loss}/\partial w_1 = (\hat{y} - y)\,x_1$. With the squared residual $\tfrac{1}{2}(\hat{y} - y)^2$ it would not cancel: for $y = 1$, $\hat{y} = 0.01$ the slope by $z$ would be −0.0098 in place of −0.99.

</div>

---
hideInToc: true
---

# $z$ Is the Logarithm of the **Odds**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📐 **Solve $\hat{y} = 1/(1 + e^{-z})$ for $z$**

$$
z = \ln \frac{\hat{y}}{1 - \hat{y}}
$$

$\hat{y}/(1 - \hat{y})$ is the **odds** of frost. The model says: the log-odds are a straight function of the inputs.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **The trained neuron**

8 Dec 2025: $\hat{y} = 0.80$, odds $0.80/0.20 = 4$, $\ln 4 = 1.39 = z$.

One degree warmer: $z$ falls by $w_1 = 0.877$, the odds by a factor $e^{0.877} = 2.4$.

</div>

</div>

---
hideInToc: true
class: fill
---

# Where the Sigmoid **Comes From**

<div class="fig-fill grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">

## 🔔 **Two Gaussian classes**

One input; class 0 Gaussian around $\mu_0$, class 1 around $\mu_1$, both of width 1, equally frequent. Bayes' rule:

$$
P(1 \mid x) = \frac{p(x \mid 1)}{p(x \mid 1) + p(x \mid 0)} = \frac{1}{1 + e^{-z}}
$$

with $z = (\mu_1 - \mu_0)\,x - \tfrac{1}{2}(\mu_1^2 - \mu_0^2)$: the squares of $x$ cancel, $z$ is a straight function of $x$.

</div>

<div class="card card-success card-glass pad-compact mt-md">

For $\mu_0 = 0$, $\mu_1 = 2$: $z = 2x - 2$.

</div>

</div>

<div>

<img class="fig" src="/figures/viz_perceptron_posterior.svg">

</div>

</div>

---
hideInToc: true
class: fill
---

# Humidity in Percent: the Rule **Fails**

<div class="fig-fill grid-side mt-sm">

<div class="card card-warning card-glass pad-compact">

⚠️ The same rule with $x_2 = 85$ in place of 0.85. One update changes $w_2$ by about 80 and $b$ by 1: $w_2 x_2$ outgrows everything, and after every epoch the neuron says frost on every evening, 33.3 %. The fraction keeps the inputs and the bias on similar scales.

</div>

<img class="fig" src="/figures/viz_perceptron_percent.svg">

</div>

---
hideInToc: true
---

# **History** in Three Dates

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

## 1958 · **The perceptron**

F. Rosenblatt, *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*, Psychological Review 65, 386–408. Weights found from examples by the rule of this lecture; the press of the quote at the start. It drew one line.

</div>

<div class="card card-warning card-glass pad-compact">

## 1969 · **The limits**

M. Minsky and S. Papert, *Perceptrons*, MIT Press: what one layer of such units can and cannot compute. XOR, and in general the parity of the inputs, it cannot.

</div>

<div class="card card-success card-glass pad-compact">

## 1986 · **Training hidden layers**

D. Rumelhart, G. Hinton and R. Williams, *Learning representations by back-propagating errors*, Nature 323, 533–536: the slope of the loss by the chain rule, through layers of smooth units.

</div>

</div>

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it.

---
hideInToc: true
---

<MCQ
  question="A neuron with a step has w1 = 2, w2 = −3 and b = 1. What are z and the output for the input x = (1, 2)?"
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
  question="Of 1000 test evenings, 900 had no frost. A classifier is right on 890 of them. What does this say?"
  :options="[
    'It is good: 89 % right',
    'It is worse than the rule never frost, which is right on 900',
    'Nothing, without the training accuracy',
    'It is right on 890 of the 100 frost evenings'
  ]"
  :correct="1"
  explanation="Never frost is right on every evening without frost: 900 of 1000, 90 %. A classifier at 89 % does worse than a rule that ignores its inputs. The baseline comes before any accuracy is praised."
/>

---
hideInToc: true
---

<MCQ
  question="Rosenblatt's rule with learning rate 1. The numbers are w = (1, −1), b = 0. The next point is x = (0, 1) with label 1. What are the numbers after this step?"
  :options="[
    'w = (1, −1), b = 0: the point is already right',
    'w = (1, −2), b = −1',
    'w = (1, 0), b = 0',
    'w = (1, 0), b = 1'
  ]"
  :correct="3"
  explanation="z = 1 · 0 + (−1) · 1 + 0 = −1, so the output is 0 and the label is 1: y − ŷ = +1. The rule adds x to w and 1 to b: w = (1, 0), b = 1. For the same point z is now 1."
/>

---
hideInToc: true
---

<MCQ
  question="A logistic neuron gives ŷ = 0.8 for an evening without frost (y = 0). What is the cross-entropy loss of this evening?"
  :options="[
    '1.609',
    '0.223',
    '0.8',
    '0.64'
  ]"
  :correct="0"
  explanation="For y = 0 the loss is −ln(1 − ŷ) = −ln 0.2 = 1.609. The value 0.223 is −ln 0.8, the loss had the frost come. The neuron gave what happened a probability of 0.2."
/>

---
hideInToc: true
---

<MCQ
  question="One evening has x = (2, −1) and label y = 1, and a logistic neuron gives ŷ = 0.3. What is the slope of its loss in w1 and w2?"
  :options="[
    '(1.4, −0.7)',
    '(0.6, −0.3)',
    '(−1.4, 0.7)',
    '(−0.7, −0.7)'
  ]"
  :correct="2"
  explanation="The slope is (ŷ − y) x = (0.3 − 1) · (2, −1) = (−1.4, 0.7), and −0.7 in b. A step downhill subtracts it: w1 rises, w2 falls, and z of this evening rises."
/>

---
hideInToc: true
---

<MCQ
  question="A rule is right on 900 of 1000 test evenings. What is its accuracy with its standard error?"
  :options="[
    '90.0 ± 0.9 %',
    '90.0 ± 9 %',
    '90.0 ± 0.09 %',
    '90.0 ± 3 %'
  ]"
  :correct="0"
  explanation="The standard error of a share p of N is the square root of p(1 − p)/N: the square root of 0.9 · 0.1 / 1000 is 0.0095, so 90.0 ± 0.9 %. A second rule at 90.5 % on the same evenings is not shown to be better."
/>

---
hideInToc: true
---

<MCQ
  question="After `model = Perceptron()` and `model.fit(xs, ys, 5)`, what has `fit` changed?"
  :options="[
    'The lists xs and ys',
    'model.w and model.b, the numbers the object holds',
    'Nothing: fit returns new numbers, which have to be stored',
    'The class Perceptron, for every model made from it'
  ]"
  :correct="1"
  explanation="fit runs the rule over the examples and changes self.w and self.b, the numbers of this one object. Another Perceptron() keeps its own numbers, and predict uses the ones of the object before the dot."
/>

---
hideInToc: true
---

<MCQ
  question="XNOR is 1 when the two inputs are equal: for (0, 0) and (1, 1). Can a single neuron compute it?"
  :options="[
    'Yes, with negative weights',
    'No: it is XOR with the labels exchanged, and the same four inequalities contradict each other',
    'Yes, if it is trained for enough epochs',
    'Only with a sigmoid in place of the step'
  ]"
  :correct="1"
  explanation="The conditions are b > 0, w1 + b ≤ 0, w2 + b ≤ 0 and w1 + w2 + b > 0. The middle two add to w1 + w2 + 2b ≤ 0, the outer two to w1 + w2 + 2b > 0. No numbers exist, whatever the training and whatever the function after the sum."
/>
