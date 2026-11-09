---
layout: cover
title: "From Neurons to Language Models"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## From Neurons to Language Models

##### <span class="aims-badge">🔧 tool-agnostic · 📁 data & files · ♻️ reproducibility</span>

<!--
**Ask:** who asked a chat model something this week? What did it do with the question?
**Say:** from the neuron of Lecture 10 to a model that writes text, every step with numbers; then what that means for how to prompt one and how to check its answer.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# You shall know a word by the **company it keeps**!
J. R. Firth, *A Synopsis of Linguistic Theory, 1930–1955* (1957)

---
hideInToc: true
---

# What a Program Wrote from Twelve **Sentences**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The station's months, in words**

```text
in january it was cold .
in february it was cold .
in march it was cool .
...
in july it was warm .
...
in december it was cold .
```

One sentence per month, the word from its mean temperature, 2016–2025: below 0 °C cold, below 10 °C cool, below 15 °C mild, else warm. July: 18.5 °C.

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## 🖨️ **A program that counted them wrote**

```text
in november it was warm .     false
in july it was cold .         false
in february it was cold .     true
in june it was cold .         false
in august it was warm .       true
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ All twelve sentences it read are true. Where do the false ones come from? And what does a chat model do with a prompt?

</div>

</div>

</div>

<!--
**Say:** ten years of the station as twelve short sentences: January's mean is −3.9 °C, so “cold”; July's 18.5 °C, so “warm”. A program read only these twelve lines and then wrote five sentences of its own.
**Ask:** where do the false ones come from? A bug, chance, something else? Keep the guesses.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Two Layers Solve **XOR**

One neuron draws one line. A layer of neurons in between draws more.

<!--
**Say:** a language model is a network of neurons. First, what two layers can compute that one neuron cannot.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# XOR Is OR but Not **AND**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact table-compact">

| $x_1$ | $x_2$ | OR | AND | XOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

<div class="note-text mt-sm">

No single line separates the two triangles from the two circles. Two lines do: the triangles lie above OR's line and below AND's.

</div>

</div>

<img class="fig" src="/figures/viz_language_xor_strip.svg">

</div>

<!--
**Say:** one neuron is one line, w·x + b = 0, and Lecture 10 ended on it: no line computes XOR. XOR is 1 when exactly one input is 1: “OR, but not AND”.
**Ask:** which neuron of Lecture 10 draws the pink line? The OR neuron: weights 1 and 1, bias −0.5.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# A 2-2-1 Network, Weights Set by **Hand**

<div class="card card-info card-glass pad-compact mt-sm">

🧠 Each circle is one neuron: $z = w_1 x_1 + w_2 x_2 + b$, then a step: 1 if $z > 0$, else 0. The output neuron takes $h_1$ and $h_2$ as its inputs. Nine numbers.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_xor_network.svg">

<!--
**Say:** two inputs, two neurons in between, one output: a 2-2-1 network. The middle layer is called hidden: its outputs are neither the inputs nor the answer. Three numbers per neuron, nine in all, set by hand.
**If asked:** the output neuron computes “h1 and not h2”: weight 1 on h1, −1 on h2, bias −0.5.
(~2 min)
-->

---
hideInToc: true
---

# The Four Inputs, Pushed **Through**

<div class="card card-info card-glass pad-compact mt-sm">

🧮 $h_1$, OR: $\;z_1 = x_1 + x_2 - 0.5$ $\qquad$ $h_2$, AND: $\;z_2 = x_1 + x_2 - 1.5$ $\qquad$ output: $\;z = h_1 - h_2 - 0.5$

</div>

<div class="card card-primary card-glass pad-compact mt-md">

| $x_1$ | $x_2$ | $z_1$ | $h_1$ | $z_2$ | $h_2$ | $z$ | $\hat{y}$ | XOR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | −0.5 | 0 | −1.5 | 0 | −0.5 | **0** | 0 |
| 0 | 1 | 0.5 | 1 | −0.5 | 0 | 0.5 | **1** | 1 |
| 1 | 0 | 0.5 | 1 | −0.5 | 0 | 0.5 | **1** | 1 |
| 1 | 1 | 1.5 | 1 | 0.5 | 1 | −0.5 | **0** | 0 |

</div>

<!--
**Do:** one row at a time, left to right. (1, 1): z1 = 1.5 and z2 = 0.5, both hidden neurons give 1, and 1 − 1 − 0.5 = −0.5 gives 0.
**Ask:** which hidden neuron turns (1, 1) into 0? AND: it fires only there.
(~3 min)
-->

---
hideInToc: true
---

# The Network in **Python**

```py {monaco-run} {autorun:false}
def step(z):
    return 1 if z > 0 else 0

def network(x1, x2):
    h1 = step(1 * x1 + 1 * x2 - 0.5)     # OR
    h2 = step(1 * x1 + 1 * x2 - 1.5)     # AND
    return step(1 * h1 - 1 * h2 - 0.5)   # OR, but not AND

for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(x1, x2, network(x1, x2))       # 0 0 0, 0 1 1, 1 0 1, 1 1 0
```

<!--
**Do:** press ▶: the last column is 0, 1, 1, 0. Then change −1.5 to −0.5 in h2 and run again: h2 becomes a second OR, and every output is 0.
**Say:** the network is the function of one neuron, called three times.
**If asked:** `1 if z > 0 else 0` is an if on one line; `for x1, x2 in ...` takes the two numbers of each pair.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Hidden Layer Changes the **Coordinates**

<div class="card card-success card-glass pad-compact mt-sm">

🔀 The output neuron sees $(h_1, h_2)$, not $(x_1, x_2)$: both $(0, 1)$ and $(1, 0)$ become $(1, 0)$. Three points, and one line separates them.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_xor_hidden.svg">

<!--
**Say:** the one idea to keep from this section: a layer computes new coordinates, and in the new coordinates a line is enough. A large network stacks many layers, each giving the next one coordinates in which its task is easier.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Training a **Network**

Nine weights set by hand work for XOR. For data, gradient descent finds them, through every layer.

<!--
**Say:** the weights of a language model are found the same way as the line of Lecture 9 and the neuron of Lecture 10; one new tool, the chain rule, carries the slope through the layers.
(~0.5 min)
-->

---
hideInToc: true
---

# Gradient Descent Needs a **Slope**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ⬇️ **One step, for every weight and bias** $\theta$

$$
\theta \leftarrow \theta - \eta\,\frac{\partial\,\text{loss}}{\partial \theta}
$$

$\eta$ is the step size. A weight moves against the slope of the loss.

</div>

<div class="card card-warning card-glass pad-compact">

## 📐 **The step function**

Flat on both sides of 0: its slope is 0. A small change of a weight changes nothing, or flips the output from 0 to 1.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md table-compact">

## 📈 **The sigmoid $1/(1 + e^{-z})$ has a slope everywhere:** $\text{sigmoid}(z)\,(1 - \text{sigmoid}(z))$

| $z$ | −1 | 0 | 2 |
| --- | --- | --- | --- |
| $\text{sigmoid}(z)$ | 0.269 | 0.500 | 0.881 |
| slope | 0.197 | 0.250 | 0.105 |

</div>

<!--
**Say:** the update rule of Lectures 9 and 10. A network that is to be trained uses the sigmoid of Lecture 10 in every neuron, so that every weight has a slope.
**If asked:** large networks mostly use max(0, z) or a smooth version of it; it has a slope wherever z > 0.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# One Evening Through Two **Neurons**

<div class="card card-info card-glass pad-compact mt-sm">

🌡️ 12 April 2025: 2.0 °C at 18:00, −3.8 °C at 06:00 the next morning: frost, $y = 1$. Weights $v = -1$, $c = 1$, $w = 2$, $b = -1$. The network says 0.386.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_tiny_forward.svg">

<!--
**Say:** the smallest network with a hidden neuron: the temperature at 18:00 in, the probability of frost by 06:00 out, the question of Lecture 10 with one input.
**Do:** read the values left to right: u = −1 · 2.0 + 1 = −1.0; h = sigmoid(−1.0) = 0.269; z = 2 · 0.269 − 1 = −0.462; ŷ = sigmoid(−0.462) = 0.386; the loss −ln 0.386 = 0.951.
**If asked:** for y = 1 the cross-entropy of Lecture 10, −[y ln ŷ + (1 − y) ln(1 − ŷ)], is −ln ŷ. The four starting weights are round numbers; training starts from small random ones.
(~3 min)
-->

---
hideInToc: true
---

# The Chain **Rule**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔗 **A function of a function**

If $f$ depends on $a$, and $a$ on $t$:

$$
\frac{df}{dt} = \frac{df}{da} \cdot \frac{da}{dt}
$$

$f = a^2$ with $a = 3t + 1$, at $t = 1$: $a = 4$, $\;df/da = 2a = 8$, $\;da/dt = 3$, so $df/dt = 24$.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔬 **Checked by a nudge**

$t = 1.001$: $\;a = 4.003$, $\;f = 16.024009$

$$
\frac{16.024009 - 16}{0.001} = 24.009
$$

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔗 In the network the loss depends on $v$ through a chain, $v \to u \to h \to z \to \hat{y} \to \text{loss}$: one factor for each link.

</div>

<!--
**Say:** the derivative of Lecture 9 and its check by a small nudge, for a function inside a function: multiply the slopes of the links.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Backward, One Link at a **Time**

<div class="card card-primary card-glass pad-compact mt-sm">

## ↩️ **Backpropagation: the error at the output, passed back link by link**

<v-clicks>

- Output, loss $-\ln \hat{y}$: $\;\delta = \partial\,\text{loss} / \partial z = -\tfrac{1}{\hat{y}}\,\hat{y}\,(1 - \hat{y}) = \hat{y} - y = 0.386 - 1 = -0.614$
- Its weight and bias: $\;\partial\,\text{loss} / \partial w = \delta\,h = -0.614 \cdot 0.269 = -0.165$, $\;\;\partial\,\text{loss} / \partial b = \delta = -0.614$
- Back to the hidden neuron, $z = wh + b$: $\;\partial\,\text{loss} / \partial h = \delta\,w = -0.614 \cdot 2 = -1.227$
- Through its sigmoid: $\;\partial\,\text{loss} / \partial u = \partial\,\text{loss} / \partial h \cdot h\,(1 - h) = -1.227 \cdot 0.197 = -0.241$
- Its weight and bias, $u = vx + c$: $\;\partial\,\text{loss} / \partial v = -0.241 \cdot 2.0 = -0.482$, $\;\;\partial\,\text{loss} / \partial c = -0.241$

</v-clicks>

</div>

<img v-click class="fig fig-fill mt-sm" src="/figures/viz_language_tiny_backward.svg">

<!--
**Do:** one click per line; each line is one factor of the chain rule, multiplied onto the line before. The last click shows the whole chain: values above, derivatives below.
**Say:** the backward pass uses only the values of the forward pass: h = 0.269 and ŷ = 0.386. A network of a million weights is done the same way, one layer back at a time. All four weight derivatives are negative: raising any of the four numbers raises ŷ towards 1.
(~4 min)
-->

---
hideInToc: true
class: fill
---

# Check One Derivative by a **Nudge**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔬 **Two forward passes**

```text
v = -0.999    loss = 0.9501829
v = -1.001    loss = 0.9511479

slope = -0.0009650 / 0.002 = -0.4825
```

The backward pass gave $\partial\,\text{loss} / \partial v = -0.4825$.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⏱️ **What each way costs**

- **Nudging:** two forward passes per parameter: 8 here, $2 \times 10^{9}$ for a network of $10^{9}$ parameters
- **Backpropagation:** one forward and one backward pass for all of them

</div>

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_nudge.svg">

<!--
**Say:** every derivation gets this check before it is trusted, the check of Lecture 9. The picture: the loss of the evening for every v, the other three weights fixed; the derivative is the slope of the curve at v = −1, and it says that a larger v lowers the loss.
(~2 min)
-->

---
hideInToc: true
---

# One Step of Gradient **Descent**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

| | before | $\partial\,\text{loss} / \partial \theta$ | after, $\eta = 1$ |
| --- | --- | --- | --- |
| $v$ | −1 | −0.4825 | −0.5175 |
| $c$ | 1 | −0.2412 | 1.2412 |
| $w$ | 2 | −0.1650 | 2.1650 |
| $b$ | −1 | −0.6135 | −0.3865 |

</div>

<div class="card card-success card-glass pad-compact">

## 📉 **The same evening, the new weights**

$u = -0.5175 \cdot 2.0 + 1.2412 = 0.2062$

$h = \text{sigmoid}(0.2062) = 0.5514$

$z = 2.1650 \cdot 0.5514 - 0.3865 = 0.8073$

$\hat{y} = \text{sigmoid}(0.8073) =$ **0.6915**, up from 0.3865

$\text{loss} = -\ln 0.6915 =$ **0.3689**, down from 0.9507

</div>

</div>

<div class="note-text mt-md">Training repeats this step for every evening, thousands of times.</div>

<!--
**Say:** after = before − η × derivative, row by row, then the forward pass with the new weights, line by line on the right.
**Ask:** which number moved most, and why? b, because its derivative is δ itself.
(~2 min)
-->

---
hideInToc: true
---

# The Step in **Python**

```py {monaco-run} {autorun:false}
import math
def sigmoid(z):
    return 1 / (1 + math.exp(-z))
x, y = 2.0, 1                            # 18:00 on 12 April 2025; frost by 06:00
v, c, w, b = -1.0, 1.0, 2.0, -1.0
h = sigmoid(v * x + c)                   # forward
y_hat = sigmoid(w * h + b)
delta = y_hat - y                        # backward
du = delta * w * h * (1 - h)
v, c, w, b = v - du * x, c - du, w - delta * h, b - delta    # one step, eta = 1
h = sigmoid(v * x + c)
print(round(y_hat, 3), round(sigmoid(w * h + b), 3))         # 0.386 0.692
```

<!--
**Say:** the five slides before, in eleven lines: forward, backward, one step, forward again.
**Do:** ▶; then repeat the four lines from `delta` to the second `h` a few times: ŷ climbs towards 1.
**If asked:** `v, c, w, b = ...` computes all four new values from the old ones first, then assigns them.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# XOR Learned from Random **Weights**

<div class="card card-success card-glass pad-compact mt-sm">

🏋️ The 2-2-1 network with sigmoids, nine weights drawn at random, 2000 steps on the four points: loss 0.696 → 0.003. The hidden neurons it found: $h_1$ = 0.03, 0.98, 0.98, 1.00, an OR; $h_2$ = 0.00, 0.05, 0.05, 0.94, an AND.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_xor_training.svg">

<!--
**Say:** the step of the evening, for nine weights and four points at a time, 2000 times. Nobody told it about OR and AND: it found the hand-set solution by itself, with larger weights.
**If asked:** the step size was η = 2, on the mean loss of the four points; from step 205 on, all four outputs are on the right side of 0.5.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# Not Every Start Learns **XOR**

<div class="card card-warning card-glass pad-compact mt-sm">

🎲 The same network and steps from twelve random starts: nine reach a loss near 0; three stop on a plateau, with one or two outputs left near 0.5 or 0.67.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_xor_starts.svg">

<!--
**Say:** gradient descent goes downhill from where it starts; a flat stretch, or a dip that is not the lowest, can hold it. Large networks are built and started so that this happens rarely, and their training is watched on text they were not trained on.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Text as **Numbers**

A language model gives every possible next word a probability. The simplest one counts.

<!--
**Say:** back to the twelve sentences and the five the program wrote.
(~0.5 min)
-->

---
hideInToc: true
---

# Words Become **Ids**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🔢 **The 20 words of the twelve sentences, numbered as they first appear**

```text
in 0           january 1      it 2           was 3          cold 4
. 5            february 6     march 7        cool 8         april 9
may 10         mild 11        june 12        warm 13        july 14
august 15      september 16   october 17     november 18    december 19
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📄 **A sentence as ids**

```text
in  july  it  was  warm  .
 0   14    2    3    13  5
```

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **A name, not a quantity**

14 − 1 = 13 says nothing about July and January. Ids only tell the words apart.

</div>

</div>

<!--
**Say:** a program stores text as numbers. The first step of every language model is a numbered list of its words, its vocabulary.
**If asked:** the list of a large model has tens of thousands of entries or more: words, pieces of words, signs.
(~2 min)
-->

---
hideInToc: true
---

# Count Which Word Follows **Which**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **The twelve sentences, 72 words**

```text
in january it was cold .
in february it was cold .
in march it was cool .
in april it was cool .
in may it was mild .
in june it was warm .
in july it was warm .
in august it was warm .
in september it was mild .
in october it was cool .
in november it was cool .
in december it was cold .
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **What comes right after each word**

| after | comes | times |
| --- | --- | --- |
| in | each month | 1 each |
| a month | it | 1 |
| it | was | 12 |
| was | cold, cool, mild, warm | **3, 4, 2, 3** |
| cold, cool, mild, warm | . | 12 |
| . | in | 11 |

</div>

</div>

<!--
**Do:** count the row of “was” with the room: cold after January, February, December; cool after March, April, October, November; mild after May, September; warm after June, July, August.
**Say:** only two rows offer a choice: after “in”, which month; after “was”, which weather word.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Next-Word Probabilities from **Counts**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

$$
P(b \mid a) = \frac{\text{count}(a\ b)}{\text{count}(a)}
$$

After “was”:

- cold: 3/12 = 0.250
- cool: 4/12 = 0.333
- mild: 2/12 = 0.167
- warm: 3/12 = 0.250

A table of such rows is a **language model**: a word in, a probability for each next word out.

</div>

<img class="fig" src="/figures/viz_language_next_word.svg">

</div>

<!--
**Say:** the probability by counting of Lecture 8: the hours with frost after an hour with frost, now the words “warm” after the word “was”.
**Ask:** what does the model say after “it”? “was”, with probability 1: twelve of twelve.
(~2 min)
-->

---
hideInToc: true
---

# Count the Pairs in **Python**

```py {monaco-run} {autorun:false}
text = """in january it was cold . in february it was cold . in march it was cool . in april it was cool .
in may it was mild . in june it was warm . in july it was warm . in august it was warm .
in september it was mild . in october it was cool . in november it was cool . in december it was cold ."""
words = text.split()                       # 72 words
follow = {}                                # word -> the words that came right after it
for i in range(len(words) - 1):
    if words[i] not in follow:
        follow[words[i]] = []
    follow[words[i]].append(words[i + 1])
print(follow["was"])                       # ['cold', 'cold', 'cool', 'cool', 'mild', ...]
print(follow["was"].count("warm") / 12)    # 0.25
```

<!--
**Say:** a dictionary of lists, as `weather.group` builds one: a key the first time it turns up gets an empty list, then every word that follows it is appended.
**Do:** ▶, then print `follow[“it”]` and `follow[“in”]`.
**If asked:** `split()` cuts a text at every space and line break; `range(len(words) - 1)` runs over every word but the last, which has nothing after it.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Generating **Text**

<div class="card card-info card-glass pad-compact mt-sm">

🎲 Draw the next word from the row of the last word, append it, repeat until “.”. From “in july it was”, the model writes “warm” with probability 3/12: three sentences in four are false.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_tree.svg">

<!--
**Say:** after “in” one of twelve months, then “it” and “was” with certainty, then one of four weather words by its count. The probability of a whole sentence is the product of its steps: from “in”, “in july it was warm .” has 1/12 · 1 · 1 · 3/12 = 1/48.
(~2 min)
-->

---
hideInToc: true
---

# Draw Five **Sentences**

```py {monaco-run} {autorun:false}
import random
months = ("january february march april may june july "
          "august september october november december").split()
after_was = ("cold cold cool cool mild warm "
             "warm warm mild cool cool cold").split()    # the row of "was"
random.seed(38)                           # the same draws every run
for n in range(5):
    month = random.choice(months)         # after "in": 1/12 each
    word = random.choice(after_was)       # after "was": 3, 4, 2, 3 of 12
    print("in", month, "it was", word, ".")
```

<!--
**Say:** the two rows that offer a choice, drawn from. `random.choice` picks one element of a list, each equally likely, so “cool”, which stands in the list four times, comes out with 4/12.
**Do:** ▶: the five sentences of the opening slide. Then remove `random.seed(38)` and run it a few times.
(~2 min)
-->

---
hideInToc: true
---

# What the Model **Wrote**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖨️ **Five sentences, seed 38**

```text
in november it was warm .     false
in july it was cold .         false
in february it was cold .     true
in june it was cold .         false
in august it was warm .       true
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔢 **How often a sentence is true**

The month is drawn first, the word without looking at it:

$$
\frac{1}{12} \cdot \frac{3 \cdot 3 + 4 \cdot 4 + 2 \cdot 2 + 3 \cdot 3}{12} = \frac{38}{144} = 0.264
$$

Of 10 000 sentences drawn: 2655 true.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Every sentence is grammatical, and 74 % are false. The counts hold which word follows which, not which month was warm.

</div>

<!--
**Say:** the three cold months each get “cold” with 3/12, the four cool ones “cool” with 4/12, and so on, each month with probability 1/12.
**Ask:** the guesses of the opening slide: a bug? No: the model does exactly what it was built to do, continue the text with likely words.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# The Chance of the True Word, Month by **Month**

<div class="card card-info card-glass pad-compact mt-sm">

📊 Each month gets its true word only as often as that word follows “was”: 2/12 for May and September, 4/12 for the cool months. The dots: the share in the 10 000 drawn sentences.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_true_by_month.svg">

<!--
**Say:** the month does not matter to the model at all: what it writes after “was” is the same for July as for January. Only the counts of the weather words decide.
(~1 min)
-->

---
hideInToc: true
---

# One Word of Context Is Not **Enough**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **The word that decides is further back**

```text
in  july  it  was  ___
    ^^^^           the word that decides
              ^^^  the word the model sees
```

After the three words “july it was”, the text holds one continuation: warm.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📈 **A row for every context**

| context | 20 words | 50 000 tokens |
| --- | --- | --- |
| 1 word | 20 | 50 000 |
| 2 words | 400 | $2.5 \times 10^{9}$ |
| 3 words | 8000 | $1.25 \times 10^{14}$ |
| 10 words | $1.0 \times 10^{13}$ | $9.8 \times 10^{46}$ |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 No table holds $10^{47}$ rows, and most contexts never occur in any text. A network computes the probabilities instead, from numbers for each word.

</div>

<!--
**Say:** counting three words back would fix our twelve sentences, but the number of possible contexts is the vocabulary to the power of the context length. A model must generalise: what it learned about one context has to carry over to similar ones.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Words as **Vectors**

A network computes with numbers. Each word becomes a list of numbers that says how it is used.

<!--
**Say:** Firth's quote of the second slide.
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# Each Month by Its Weather **Words**

<div class="card card-info card-glass pad-compact mt-sm">

📄 The same sentence for each of the 120 months of 2016–2025. Each month becomes a **vector**, a list of four numbers: how often each weather word came with it. January = (9, 1, 0, 0), July = (0, 0, 0, 10).

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_month_vectors.svg">

<!--
**Say:** January came with “cold” in nine Januaries out of ten; January 2018, at 0.2 °C, was “cool”. July was warm in all ten. Months used alike get similar vectors, from the text alone.
**Ask:** which month's vector looks most like January's? December, (9, 1, 0, 0), exactly the same; then February.
(~2 min)
-->

---
hideInToc: true
---

# Similarity as a Dot **Product**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ✖️ **Multiply and add**

$$
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 + a_4 b_4
$$

- january · february = 9 · 10 + 1 · 0 = 90
- january · march = 9 · 1 + 1 · 9 = 18
- january · july = 0

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Divided by the lengths: the cosine**

$$
\cos = \frac{\mathbf{a} \cdot \mathbf{b}}{\lVert\mathbf{a}\rVert\,\lVert\mathbf{b}\rVert}, \qquad \lVert\mathbf{a}\rVert = \sqrt{\mathbf{a} \cdot \mathbf{a}}
$$

- ‖january‖ = √82 = 9.055, ‖february‖ = 10
- january, february: 90 / 90.55 = **0.994**
- january, march: 18 / 82 = **0.220**
- january, july: **0**

</div>

</div>

<!--
**Say:** the dot product grows when two vectors have large numbers in the same places. Dividing by the lengths gives the cosine of the angle between them: 1 for the same direction, 0 for nothing in common.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# The Twelve Months by Their **Vectors**

<div class="fig-fill grid-side mt-sm">

<div class="card card-success card-glass pad-compact">

🗓️ The cosine of every pair of months. Four groups appear, from the words alone:

- December to February
- March, April, October, November
- May and September
- June to August

</div>

<img class="fig" src="/figures/viz_language_similarity.svg">

</div>

<!--
**Say:** nobody told the program which months are alike: it read 120 sentences. A language model learns its vectors from the company words keep in its text, in the same spirit.
**If asked:** August is 0.97 like July, 0.24 like May: two of its ten months were mild.
(~2 min)
-->

---
hideInToc: true
---

# The Dot Product in **Python**

```py {monaco-run} {autorun:false}
import math

def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total

january, march, july = [9, 1, 0, 0], [1, 9, 0, 0], [0, 0, 0, 10]
print(dot(january, march), dot(january, july))                          # 18 0
print(dot(january, march) / math.sqrt(dot(january, january) * dot(march, march)))  # 0.2195...
```

<!--
**Do:** ▶; then compute the cosine of January and February: february = [10, 0, 0, 0] gives 0.994.
**If asked:** the length of a vector is the square root of its dot product with itself.
(~2 min)
-->

---
hideInToc: true
---

# Vectors in a Language **Model**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Hundreds to thousands of numbers**

Every token of the vocabulary has its vector, not four counts.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **A row of a table**

The token's id picks its row of a table of vectors: the first layer of the network.

</div>

<div class="card card-accent card-glass pad-compact">

## 🏋️ **Learned, not counted**

The numbers are weights, found by gradient descent with the rest of the network.

</div>

<div class="card card-success card-glass pad-compact">

## 🧭 **Measured by the dot product**

Tokens used alike end up with similar vectors, as the months did here.

</div>

</div>

<!--
**Say:** the four counts per month were chosen by hand. In a language model nobody chooses what the numbers mean: they are whatever makes the next word most likely, and words that keep the same company end up close.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Scores into **Probabilities**

A network ends in one score for each possible next word. Softmax turns the scores into probabilities.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# **Softmax**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Scores to probabilities**

$$
p_i = \frac{e^{s_i}}{e^{s_1} + e^{s_2} + \dots + e^{s_K}}
$$

Every $p_i$ is positive, together they make 1, and a larger score gets a larger probability.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🧮 **Three scores**

| word | $s$ | $e^{s}$ | $p$ |
| --- | --- | --- | --- |
| warm | 2.0 | 7.389 | **0.659** |
| mild | 1.0 | 2.718 | **0.242** |
| cool | 0.1 | 1.105 | **0.099** |
| sum | | 11.213 | 1 |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📈 With two scores, softmax is the sigmoid: $(2, 0)$ gives $e^{2} / (e^{2} + e^{0}) = 0.881 = \text{sigmoid}(2)$.

</div>

<!--
**Say:** e to the power of a score is always positive; dividing by the sum makes the numbers add to 1.
**Do:** 7.389 / 11.213 = 0.659, row by row.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# Softmax with a **Temperature**

<div class="card card-primary card-glass pad-compact mt-sm">

🌡️ The scores divided by $T$ first: $T = 0.5$ doubles them, $T = 2$ halves them. Drag a score, move $T$, press “draw”.

</div>

<SoftmaxTemperature class="fig-fill mt-sm" prompt="in july it was" :words="['warm', 'mild', 'cool']" :scores="[2.0, 1.0, 0.1]" :t="0.5" />

<!--
**Do:** at T = 0.5 read the row of warm: s/T = 4, e⁴ = 54.60, Σ = 63.21, p = 0.864. Press the chip 1: warm 0.659, the slide before; the chip 2: warm 0.502, cool up from 0.019 to 0.194; the chip 3: 0.445, 0.319, 0.236. Press 0.1, then ×20: warm, 1.000 to three decimals. At T = 1 drag the score of mild from 1.0 to 2.0: warm and mild 0.465 each.
(~3 min)
-->

---
hideInToc: true
---

# Softmax in **Python**

```py {monaco-run} {autorun:false}
import math
def softmax(scores, T):
    e = []
    for s in scores:
        e.append(math.exp(s / T))
    p = []
    for x in e:
        p.append(round(x / sum(e), 3))
    return p
print(softmax([2.0, 1.0, 0.1], 1))      # [0.659, 0.242, 0.099]
print(softmax([2.0, 1.0, 0.1], 0.5))    # [0.864, 0.117, 0.019]
```

<!--
**Do:** ▶; then try T = 2 and T = 0.1.
**Ask:** at T = 0.1, how likely is warm? 1.0 to three decimals: e to the 20 against e to the 10 and e to the 1.
(~2 min)
-->

---
hideInToc: true
---

# What the Temperature Does to **Text**

<div class="grid-2 mt-sm gap-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

❄️ **Low $T$:** almost always the most likely word: the same text on every run

</div>

<div class="card card-warning card-glass pad-compact">

🔥 **High $T$:** unlikely words more often: more varied text, and more mistakes

</div>

<div class="card card-info card-glass pad-compact">

🎲 **A chat model** draws each word of its reply this way: the same prompt can get a different reply

</div>

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎲 **Ten draws after “in july it was”**

```text
T = 0.5   warm warm warm warm warm
          warm warm warm warm warm

T = 2     cool warm mild warm warm
          mild warm cool cool warm
```

Warm 10 times of 10 at $T = 0.5$, 5 times at $T = 2$.

</div>

</div>

<!--
**Say:** drawing is why a reply cannot be repeated exactly, and why a result must never depend on one chat. The draws on the right use the softmax probabilities of warm, 0.864 at T = 0.5 and 0.502 at T = 2 (random.Random(1)).
**If asked:** programs that call a model can set T; a chat app chooses it itself.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Context and **Attention**

The next word depends on words further back. Attention gives each of them a weight.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# Which Earlier Word **Decides**

<div class="card card-info card-glass pad-compact mt-sm">

❓ “in july it was ___”: the counting model sees “was” and says warm 0.25. The word that decides is “july”.

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📄 **What each word says about the weather word**

| word | cold | cool | mild | warm |
| --- | --- | --- | --- | --- |
| july | 0 | 0 | 0 | 1 |
| it | 0.250 | 0.333 | 0.167 | 0.250 |
| was | 0.250 | 0.333 | 0.167 | 0.250 |

</div>

<div class="card card-secondary card-glass pad-compact">

## ⚖️ **Weigh them**

In the twelve sentences “july” always comes with warm; “it” and “was” come with every weather word. A model needs a weight for each earlier word: large for “july”, small for the rest.

</div>

</div>

<!--
**Say:** the rows of the table are vectors of what each word tells about the next weather word, from the twelve sentences: the row of “was” is the probability row of the counting model.
(~2 min)
-->

---
hideInToc: true
---

# Attention: a Weighted **Average**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚖️ **Weights from scores, by softmax**

$$
a_i = \frac{e^{s_i}}{\sum_j e^{s_j}}, \qquad \mathbf{c} = a_1 \mathbf{v}_1 + a_2 \mathbf{v}_2 + a_3 \mathbf{v}_3
$$

<v-clicks>

- scores $s$: july 3, it 0, was 0
- $e^{s}$: 20.09, 1, 1; sum 22.09
- weights $a$: **0.909**, 0.045, 0.045

</v-clicks>

</div>

<div class="card card-secondary card-glass pad-compact" v-click>

## ➕ **The weighted average of the rows**

$0.909 \cdot (0, 0, 0, 1)$

$+\ 0.045 \cdot (0.25, 0.333, 0.167, 0.25)$

$+\ 0.045 \cdot (0.25, 0.333, 0.167, 0.25)$

$=\ (0.023,\ 0.030,\ 0.015,\ \mathbf{0.932})$

</div>

</div>

<div class="note-text mt-md">Warm: 0.25 from "was" alone, 0.932 with the weights.</div>

<!--
**Say:** the scores say how much each earlier word matters for the next one; softmax turns them into weights that add to 1; the result is the average of the words' vectors, each counted by its weight.
(~4 min)
-->

---
hideInToc: true
class: fill
---

# Where the Scores Come **From**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔎 **A dot product**

“was” looks for $\mathbf{q} = (3, 0)$; each earlier word offers its $\mathbf{k}$:

| word | $\mathbf{k}$ | score $\mathbf{q} \cdot \mathbf{k}$ |
| --- | --- | --- |
| july | (1, 0) | **3** |
| it | (0, 1) | **0** |
| was | (0, 1) | **0** |

<div class="note-text mt-sm">

In a trained model $\mathbf{q}$ and $\mathbf{k}$ are learned; here they are set by hand, as the XOR weights were.

</div>

</div>

<img class="fig" src="/figures/viz_language_qk.svg">

</div>

<!--
**Say:** the first coordinate stands for “is a month”, the second for “is not”. The word that needs a month gives a large score to the word that is one.
**If asked:** large models also divide each score by the square root of the number of entries in the vectors before softmax, so that long vectors do not give huge scores.
(~2 min)
-->

---
hideInToc: true
class: fill
---

# The Next Word with and without **Attention**

<div class="card card-success card-glass pad-compact mt-sm">

🎯 From “was” back over the words before it: 0.909 on “july”. Warm rises from 0.25 to 0.932.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_attention.svg">

<!--
**Say:** the weights in pictures on the left, the two predictions on the right. The model that looks back writes “in july it was warm” 93 times in 100.
(~1 min)
-->

---
hideInToc: true
---

# Attention in **Python**

```py {monaco-run} {autorun:false}
import math
total = math.exp(3) + math.exp(0) + math.exp(0)
weights = []
for s in [3, 0, 0]:                                 # scores of july, it, was
    weights.append(math.exp(s) / total)
print(weights)                                      # [0.909..., 0.045..., 0.045...]
july, was = [0, 0, 0, 1], [3/12, 4/12, 2/12, 3/12]  # it has the vector of was
for k in range(4):                                  # cold, cool, mild, warm
    c = weights[0] * july[k] + weights[1] * was[k] + weights[2] * was[k]
    print(round(c, 3))                              # 0.023 0.03 0.015 0.932
```

<!--
**Do:** ▶; then set the score of july to 1 and run again: warm falls to 0.40.
**Say:** three lines of softmax, then the weighted average, one weather word at a time.
(~2 min)
-->

---
hideInToc: true
---

# Attention in a Large **Model**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔁 **In every layer**

Each token weighs every token before it, and itself, in every layer of the network.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Learned scores**

Dot products of learned vectors; the weights come from softmax, as here.

</div>

<div class="card card-accent card-glass pad-compact">

## 👥 **Many weightings at once**

Several side by side in each layer, and dozens of layers in a row.

</div>

<div class="card card-info card-glass pad-compact">

## 📏 **A long context**

Thousands of tokens and more. The arrangement is called a **transformer** (Vaswani et al., 2017).

</div>

</div>

<!--
**Say:** the three words and the weight of 0.909 are the idea; a large model does the same over its whole context, in every layer, with weights it has learned.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# A Large Language **Model**

An LLM: the same next-word prediction, with a network in place of the table, learned from a very large text.

<!--
(~0.5 min)
-->

---
hideInToc: true
class: fill
---

# From a Prompt to the Next **Token**

<div class="card card-info card-glass pad-compact mt-sm">

🔁 One token per pass: the prompt's tokens, their vectors, layers of attention and neurons, a score for every token of the vocabulary, softmax at $T$, a draw. The token is appended, and the next pass begins.

</div>

<img class="fig fig-fill mt-sm" src="/figures/viz_language_llm.svg">

<!--
**Say:** every box is a part of this lecture: ids, vectors, attention, neurons, softmax, the draw. A large language model, an LLM, is this loop with a very large network.
(~2 min)
-->

---
hideInToc: true
---

# What a Token **Is**

<div class="grid-2 mt-sm gap-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-compact">

✂️ Text is cut into tokens: frequent words whole, rare words in pieces, signs and spaces too

</div>

<div class="card card-secondary card-glass pad-compact">

📚 A vocabulary has tens of thousands of tokens or more, each with an id and a learned vector

</div>

<div class="card card-warning card-glass pad-compact">

🔢 A number is one or more tokens of digits: “87552” is a piece of text to the model, not a quantity

</div>

</div>

<div class="card card-accent card-glass pad-compact table-compact">

## 🧮 **A vocabulary of pieces, counted**

From letters, merge the most frequent pair of neighbours, again and again. In the twelve sentences:

| merge | pair | times |
| --- | --- | --- |
| 1 | w + a | 15 |
| 2 | i + n | 12 |
| 3 | i + t | 12 |
| 4 | wa + s | 12 |
| 5 | c + o | 7 |

After 8 merges `in`, `it`, `was`, `cool` are tokens; `january` is still j·a·n·u·a·r·y.

</div>

</div>

<!--
**Say:** a vocabulary of pieces is itself made by counting pairs, the same counting as the word pairs: the pair met most often becomes one symbol. Built on a very large text, frequent words end up whole, rare ones in pieces, and any text, in any language, can still be written.
**If asked:** the merges after the fifth: l + d (5 times), co + o (4), coo + l (4).
(~1 min)
-->

---
hideInToc: true
---

# **Pretraining**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📉 **The loss, at every token**

$$
\text{loss} = -\ln p\,(\text{the token that came next})
$$

averaged over all tokens of the text.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **The twelve weather words**

| model | $p$ (warm) after “in july it was” | mean loss |
| --- | --- | --- |
| sees “was” | 0.250 | 1.358 |
| attention | 0.932 | 0.069 |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🏋️ Pretraining is gradient descent on this mean, over a very large text: books, web pages, program code. Every weight moves as $v$, $c$, $w$ and $b$ did.

</div>

<!--
**Say:** −ln 0.25 = 1.386 for July; averaged over the twelve weather words, 1.358 for the counting model and 0.069 for the one that weighs the month. Lower is better: the loss says which model predicts the text.
(~3 min)
-->

---
hideInToc: true
class: fill
---

# The Number of **Parameters**

<div class="fig-fill grid-side mt-sm">

<div class="card card-primary card-glass pad-compact">

🔢 Weights, biases and vectors. The tiny network of the frost evening: 4. XOR: 9. GPT-2 (2019): $1.5 \times 10^{9}$. GPT-3 (2020): $1.75 \times 10^{11}$, as their papers state.

The step is the same for all of them.

</div>

<img class="fig" src="/figures/viz_language_sizes.svg">

</div>

<!--
**Say:** the sizes of newer models are often not published. What was computed by hand for four numbers is computed for 10 to the 11: a forward pass, a loss, a backward pass, a step.
**If asked:** GPT-2: Radford et al., 2019; GPT-3: Brown et al., 2020.
(~1 min)
-->

---
hideInToc: true
---

# Instruction **Tuning**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📚 **After pretraining**

The model continues text. A question may be continued with more questions, as on an exam sheet.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗣️ **Then tuning**

More training on examples of instructions with good answers, and on people's choices between two answers. Then a question is followed by an answer.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

## 💬 **A chat is one text, continued token by token**

```text
<the provider's instructions>
user:        What does word_for(0) return?
assistant:   ___   drawn token by token, given all the text above
```

</div>

<!--
**Say:** tuning changes which continuations are likely, not how the reply is made: the reply is still drawn token by token, and the whole conversation is the context.
**If asked:** a new chat does not see an old one, unless the service keeps notes between chats; a very long chat may lose its oldest parts.
(~2 min)
-->

---
hideInToc: true
---

# What an LLM Is **Not**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 🗄️ **Not a database**

No table of facts inside. A fact comes out as a likely continuation, like “in july it was cold”.

</div>

<div class="card card-warning card-glass pad-compact">

## 🧮 **Not a calculator**

Digits are tokens, predicted like words. A number in a reply is checked by computing it.

</div>

<div class="card card-warning card-glass pad-compact">

## 📂 **Not looking at your data**

It knows your file only if the file is in the prompt, and nothing after its training text unless a tool fetches it.

</div>

<div class="card card-warning card-glass pad-compact">

## 🎲 **Not the same twice**

The reply is drawn at a temperature. Asked again, it may differ.

</div>

</div>

<!--
**Say:** each card follows from the loop of this lecture, not from experience with one product. A wrong answer comes in the same fluent style as a right one: the style says nothing about the truth.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Prompting, from How It **Works**

The reply depends on the training and on the prompt. The prompt is the part you write.

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# What a Prompt Gives the **Model**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📋 **Context**

What the data are: the file, the columns, the units, −999 for a missing hour. The model has seen none of it.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **An example**

One input with the answer you want. The reply continues the pattern, as the counts continued the sentences.

</div>

<div class="card card-accent card-glass pad-compact">

## 📐 **The format**

A function with a docstring, a table, a list. The likely next tokens follow it.

</div>

<div class="card card-success card-glass pad-compact">

## 🚧 **Constraints**

Plain Python, no pandas, at most ten lines. Each one rules out likely but wrong continuations.

</div>

</div>

<!--
**Say:** each card follows from next-token prediction: the reply is the likely text after the prompt, so whatever the prompt leaves open is filled with what is likely in general, not what is true for your data.
(~3 min)
-->

---
hideInToc: true
---

# A Prompt Without and With **Context**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 🚫 **Without**

```text
write code for the mean temperature
```

Which file, which column, which language, what about −999? Every gap is filled with a likely guess.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **With context, example, format, constraints**

```text
In my weather log, -999 marks an hour without
a temperature. Write a Python function
mean_valid(temps) that returns the mean of a
list of temperatures, leaving out -999.
Plain Python, no libraries, with a docstring.
Then a test with assert: the six hours of
2019-07-21 20:00 to 2019-07-22 01:00,
[27.3, 25.6, 24.6, 23.6, -999, -999],
must give 25.275.
```

</div>

</div>

<!--
**Say:** the second prompt gives the context (−999), the format (a function with a docstring), the constraints (plain Python) and an example with its answer, which becomes the test.
**Ask:** where does 25.275 come from? (27.3 + 25.6 + 24.6 + 23.6) / 4, computed without the code.
(~2 min)
-->

---
hideInToc: true
---

# A Test with a Known **Answer**

```py {monaco-run} {autorun:false}
def mean_valid(temps):
    """The mean of the temperatures that are not -999."""
    valid = []
    for t in temps:
        if t != -999:
            valid.append(t)
    return sum(valid) / len(valid)
hours = [27.3, 25.6, 24.6, 23.6, -999, -999]   # 2019-07-21, 20:00 to 01:00
print(mean_valid(hours))                       # 25.275000000000002
print(mean_valid(hours) == 25.275)             # False
print(round(mean_valid(hours), 3) == 25.275)   # True
```

<div class="note-text mt-md">

The test fails on a correct function: the float is rounded. Run every test, the model's and your own, before trusting it.

</div>

<!--
**Say:** whoever wrote the function, the test with a known answer checks it. A test written by a model is code too: here `==` on a float fails, and the run shows it; the repair compares the rounded value.
**Do:** ▶; then change `-999` to `-99` in the `if` and run again: the mean becomes −316.15, and the test catches it.
(~3 min)
-->

---
hideInToc: true
---

# A Question Only the Data Can **Answer**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## 💬 **Asked in a chat, without the file**

```text
How many hours of my weather log
are below 0 °C?
```

The model has not seen the file. A number in its reply is a likely-looking guess.

</div>

<div class="card card-success card-glass pad-compact">

## 🐍 **Computed from the file**

```python
temps = weather.temps("data/raw/weather.csv")
count = 0
for t in temps:
    if t < 0:
        count = count + 1
print(count, len(temps))
```

```text
22352 87552
```

</div>

</div>

<!--
**Say:** a statement about your data is computed from the data. A model can help write these six lines; the number comes from running them.
**If asked:** `weather.temps` is the function of Lecture 5: every temperature that is not −999.
(~2 min)
-->

---
hideInToc: true
---

# What to Check, and **How**

<div class="card card-primary card-glass pad-compact mt-sm">

| The reply gives | Check it by |
| --- | --- |
| A reference | opening it: does it exist, with these authors, and does it say this? |
| A number, a constant, a formula | the source, or your own calculation |
| Code | running it on a case whose answer you know |
| A statement about your data | computing it from the data |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Use only what you have checked. The tool helps most where you know enough to check its reply.

</div>

<!--
**Say:** every row is a check this course has practised on its own results; each takes minutes.
(~2 min)
-->

---
hideInToc: true
---

# Where an LLM Helps in an **Analysis**

<div class="card card-primary card-glass pad-compact mt-sm">

| Step | A reasonable use | The risk |
| --- | --- | --- |
| Plan | a list of what could be measured | it does not know what you need to decide |
| Code | a traceback explained; a first version of a function; a test | code that runs and computes the wrong thing |
| Checks | checks you did not think of | twenty variants in a minute, and the one that looks best is kept |
| Writing | the language of your own text | claims and references that are not in your results |

</div>

<div class="note-text mt-md">The order of the work stays: the plan first, the checks before the conclusion.</div>

<!--
**Say:** the tool speeds up each step; it does not change their order.
**Ask:** which row fits your project this week?
(~2 min)
-->

---
hideInToc: true
---

# What Never to **Paste**

<div class="card card-info card-glass pad-compact mt-sm">

📡 What you type is sent to the computers of the company that runs the model. Whether it is kept or used for training depends on the service and its terms.

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

🔒 **Personal data:** names, grades, health, addresses

</div>

<div class="card card-warning card-glass pad-compact">

📄 **Work that is not yours alone:** a colleague's unpublished results, a paper you review

</div>

<div class="card card-warning card-glass pad-compact">

🔑 **Secrets:** passwords, access tokens, keys

</div>

<div class="card card-warning card-glass pad-compact">

📜 **Restricted data:** under a licence or an agreement that forbids passing it on

</div>

</div>

<div class="note-text mt-md">Fine to paste: your own code, an error message, public data.</div>

<!--
**Say:** read the terms: on many free accounts what you type may be kept and used to train later models. If you do not know what happens to the text, treat the chat as public.
(~2 min)
-->

---
hideInToc: true
---

# Say Where an LLM Was **Used**

<div class="grid-3 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖊️ **Not an author**

A tool cannot answer for the work.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🙋 **You answer**

For every sentence, number and line of code, whoever drafted it.

</div>

<div class="card card-accent card-glass pad-compact">

## 📝 **Use is stated**

Which tool, when, for what, and what was checked.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

## 📄 **In the README**

```text
## Use of AI tools
mean_valid in scripts/clean.py was drafted with <tool> on 15 December 2026
and checked with a test: the six hours of 21 July 2019 give 25.275.
The text of this README is my own.
```

</div>

<!--
**Say:** journals, funders and universities agree on these three points; they differ on the rest, such as what is allowed in graded work, so ask before you hand something in.
(~2 min)
-->

---
hideInToc: true
---

# Keep the Work **Reproducible**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact">

♻️ A chat cannot be run again with the same output: what it produced goes into a script in the project folder

</div>

<div class="card card-secondary card-glass pad-compact">

🧪 Code from a chat is treated like all code: committed with Git, run from a clean start, tested on a known answer

</div>

<div class="card card-accent card-glass pad-compact">

📝 The README says which tool was used, when, and for what: provenance, like the source of a data file

</div>

<div class="card card-success card-glass pad-compact">

🗣️ You can explain every line you hand in

</div>

</div>

<!--
**Say:** the four aims of the course hold for this tool as for any other. The last card is the test: a line you cannot explain is not yet yours.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Wrap-up**

<!--
(~0.5 min)
-->

---
hideInToc: true
---

# What an LLM Does with a **Prompt**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

1\. Cuts the prompt into tokens with ids: “in july it was” → 0, 14, 2, 3

</div>

<div class="card card-secondary card-glass pad-compact">

2\. Gives each token its vector of learned numbers

</div>

<div class="card card-accent card-glass pad-compact">

3\. Mixes the vectors by attention, layer after layer: 0.909 on “july”

</div>

<div class="card card-info card-glass pad-compact">

4\. Scores every token of the vocabulary, softmax at a temperature: warm 0.932

</div>

<div class="card card-success card-glass pad-compact">

5\. Draws one token, appends it, and runs again; trained by the step of the frost evening on a very large text, then tuned on instructions

</div>

</div>

<!--
**Say:** the answer to the opening slide. The counting program wrote “in july it was cold” because it saw one word; a large model sees the whole prompt, and still writes the likely text, not the checked one.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Push the four inputs of **XOR** through a 2-2-1 network

</div>

<div class="card card-success card-glass pad-compact">

✅ Take one step of **gradient descent** through two neurons with the chain rule, and check a derivative by a nudge

</div>

<div class="card card-success card-glass pad-compact">

✅ Build a **language model** by counting word pairs, and generate text from it

</div>

<div class="card card-success card-glass pad-compact">

✅ Compare words as **vectors** with the dot product and the cosine

</div>

<div class="card card-success card-glass pad-compact">

✅ Turn scores into probabilities with **softmax** at a temperature, and weights into an **attention** average

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a **prompt** with context, an example, a format and constraints; test the reply; paste no personal data; state the use

</div>

</div>

<!--
**Say:** one line per card, each with its number from today: 0, 1, 1, 0; 0.951 to 0.369; 3 of 12; 0.994; 0.864; 25.275.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

The derivations behind the main path, and where the ideas come from.

<!--
**Say:** optional, for time left at the end or for after the lecture.
(~0.5 min)
-->

---
hideInToc: true
---

# Without the Step, Two Layers Are **One**

<div class="card card-primary card-glass pad-compact mt-sm">

## ➖ **Leave the step out of the hidden layer:** $h_1 = z_1$, $h_2 = z_2$

$$
\begin{aligned}
z &= h_1 - h_2 - 0.5 = (x_1 + x_2 - 0.5) - (x_1 + x_2 - 1.5) - 0.5 \\
  &= 0 \cdot x_1 + 0 \cdot x_2 + 0.5
\end{aligned}
$$

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ All four inputs give $z = 0.5$, so $\hat{y} = 1$. A weighted sum of weighted sums is a weighted sum: without a bent function between the layers, any number of layers draws one line.

</div>

<!--
**Say:** this is why every neuron of a network has its step, sigmoid or max(0, z) after the sum.
-->

---
hideInToc: true
---

# Backpropagation for the 2-2-1 **Network**

<div class="card card-primary card-glass pad-compact mt-sm table-compact">

| | Forward: the values | | Backward: the derivatives |
| --- | --- | --- | --- |
| 1 | $u_j = v_{j1}\,x_1 + v_{j2}\,x_2 + c_j$ | 5 | $\delta = \hat{y} - y$ |
| 2 | $h_j = \text{sigmoid}(u_j)$ | 6 | $\partial\,\text{loss} / \partial w_j = \delta\,h_j$, $\;\partial\,\text{loss} / \partial b = \delta$ |
| 3 | $z = w_1 h_1 + w_2 h_2 + b$ | 7 | $\delta_j = \delta\,w_j\,h_j\,(1 - h_j)$ |
| 4 | $\hat{y} = \text{sigmoid}(z)$ | 8 | $\partial\,\text{loss} / \partial v_{ji} = \delta_j\,x_i$, $\;\partial\,\text{loss} / \partial c_j = \delta_j$ |

</div>

<div class="note-text mt-md">

Lines 5 to 8 are the evening's five steps with an index: $j$ counts the hidden neurons, $i$ the inputs. The XOR network was trained with these eight lines, the mean over the four points, $\eta = 2$.

</div>

<!--
**Say:** each backward line is one factor of the chain rule; δ_j is the error passed back to hidden neuron j.
-->

---
hideInToc: true
---

# The Ten Years as **Text**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **120 sentences, one per month of 2016–2025**

```text
in january it was cold .
in february it was cold .
...
in december it was cold .
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🔢 **After “was”**

| word | times | $P$ |
| --- | --- | --- |
| cold | 29 | 0.242 |
| cool | 40 | 0.333 |
| mild | 22 | 0.183 |
| warm | 29 | 0.242 |

</div>

</div>

<!--
**Say:** the month vectors of the section Words as Vectors were counted in these 120 sentences. The counting model of the ten years still writes “in july it was cold” 24 times in 100.
-->

---
hideInToc: true
---

# Three **Dates**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

## 1948 · **Text from word pairs**

C. E. Shannon, *A Mathematical Theory of Communication*: English-like text, each word drawn by how often it follows the one before it in a book.

</div>

<div class="card card-secondary card-glass pad-compact">

## 1986 · **Training hidden layers**

D. Rumelhart, G. Hinton, R. Williams, *Learning representations by back-propagating errors*: the chain rule through every layer.

</div>

<div class="card card-success card-glass pad-compact">

## 2017 · **Attention**

A. Vaswani et al., *Attention Is All You Need*: the transformer, the arrangement of today's language models.

</div>

</div>

<!--
**Say:** the counting model of this lecture is Shannon's, the step through the layers is from 1986, and the weighting of the earlier words from 2017.
-->

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
  question="A network computes h1 = step(x1 + x2 − 0.5), h2 = step(x1 + x2 − 1.5) and ŷ = step(h1 − h2 − 0.5). What is ŷ for the input (1, 1)?"
  :options="[
    '1, because both hidden neurons give 1',
    '0, because h1 − h2 − 0.5 = 1 − 1 − 0.5 = −0.5',
    '0.5, half way between the classes',
    '1, because x1 + x2 = 2 is larger than every bias'
  ]"
  :correct="1"
  explanation="z1 = 1.5 and z2 = 0.5, so h1 = 1 and h2 = 1. The output neuron gets 1 − 1 − 0.5 = −0.5, and the step gives 0. The AND neuron h2 turns OR into XOR."
/>

---
hideInToc: true
---

<MCQ
  question="f = a² and a = 3t + 1. What is df/dt at t = 2?"
  :options="[
    '42',
    '14',
    '6',
    '49'
  ]"
  :correct="0"
  explanation="At t = 2, a = 7. By the chain rule df/dt = df/da · da/dt = 2a · 3 = 14 · 3 = 42. A nudge checks it: at t = 2.001, f = 7.003² = 49.042009, and 0.042009 / 0.001 = 42.009."
/>

---
hideInToc: true
---

<MCQ
  question="In a text the word 'was' is followed 3 times by cold, 4 times by cool, 2 times by mild and 3 times by warm. What probability does a model that counts word pairs give to 'mild' after 'was'?"
  :options="[
    '0.25, one of four words',
    '0.167, 2 of 12',
    '0.5, mild or not',
    '2, the number of times'
  ]"
  :correct="1"
  explanation="P(mild | was) = count(was mild) / count(was) = 2 / 12 = 0.167. The four probabilities, 0.25, 0.333, 0.167 and 0.25, add up to 1."
/>

---
hideInToc: true
---

<MCQ
  question="What is the dot product of a = (1, 2, 0) and b = (2, 0, 3)?"
  :options="[
    '(2, 0, 0)',
    '5',
    '2',
    '0'
  ]"
  :correct="2"
  explanation="a · b = 1 · 2 + 2 · 0 + 0 · 3 = 2. A dot product is one number: the products of the matching entries, added up."
/>

---
hideInToc: true
---

<MCQ
  question="Softmax turns the scores (2.0, 1.0, 0.1) into (0.659, 0.242, 0.099) at T = 1. What happens to the first probability at T = 0.5?"
  :options="[
    'It falls to 0.330: half of 0.659',
    'It stays 0.659: T changes only the order',
    'It rises to 0.864: the scores are doubled and spread apart',
    'It becomes 1: T below 1 always picks the top word'
  ]"
  :correct="2"
  explanation="Dividing by T = 0.5 doubles the scores to (4, 2, 0.2): e⁴ = 54.598, e² = 7.389, e⁰·² = 1.221, sum 63.209, and 54.598 / 63.209 = 0.864. A lower temperature makes the likely word more likely."
/>

---
hideInToc: true
---

<MCQ
  question="Two earlier words get the attention scores 2 and 0. Their vectors are (1, 0) and (0, 1). What is the weighted average?"
  :options="[
    '(1, 0): only the higher score counts',
    '(0.5, 0.5): an average gives each word half',
    '(2, 0): the scores times the vectors',
    '(0.881, 0.119): softmax weights times the vectors'
  ]"
  :correct="3"
  explanation="Softmax of (2, 0): e² / (e² + 1) = 0.881 and 1 / (e² + 1) = 0.119. The average is 0.881 · (1, 0) + 0.119 · (0, 1) = (0.881, 0.119)."
/>

---
hideInToc: true
---

<MCQ
  question="A chat model gives you a reference with authors, journal, year and DOI. What follows from how the reply was made?"
  :options="[
    'It exists: a model only repeats what it has read',
    'It is a likely continuation of the text, so it may not exist: open the DOI and read the paper',
    'It exists if the model is large enough',
    'It exists if the same reference comes back when you ask again'
  ]"
  :correct="1"
  explanation="The reply is drawn token by token from likely continuations; nothing in it compares a reference with a library. A reference that looks right can be invented, and asking again only draws again. Opening it is the check."
/>

---
hideInToc: true
---

<MCQ
  question="A model wrote a correct function and the test `assert mean_valid(hours) == 25.275`. Running it gives an AssertionError. Why?"
  :options="[
    'The function is wrong, since the test fails',
    'The mean is 25.275000000000002 as a float, and == compares every digit; compare the rounded value',
    'assert works only with integers',
    'Tests written by a model cannot be run'
  ]"
  :correct="1"
  explanation="27.3, 25.6, 24.6 and 23.6 are not exact in binary, and their mean comes out as 25.275000000000002. round(mean_valid(hours), 3) == 25.275 passes. A test is code too: it is checked by running it."
/>
