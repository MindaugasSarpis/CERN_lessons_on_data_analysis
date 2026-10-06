<!--
Parked slides from slides/11_The_Perceptron.md, taken out on 2026-10-06.

"The Symbols of This Lecture" stood after "What Lecture 10 Built, and What
Changes", before the section slide "One Neuron". It was a glossary between
the question of the lecture and the neuron, and its dot-product example
(w = (2, -1), x = (3, 2)) is computed again on "Weighted Sum, Bias, Step".
Each symbol is now defined on the slide that first uses it.

"The Loss Falls" stood after "The Training Loop", before "The Boundary
Moves". Its table repeated the printed output of the runner on the slide
before; the "Why 0.6931" card and the remark on the accuracy are now in that
slide's speaker note. It left to keep the deck under 145 min after the
gradient check became a runner. This file is not
in decks.json: it is not built, not gated and not deployed. To put a slide
back, move it into the lecture file.
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
