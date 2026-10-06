<!--
Slides taken out of Lecture 09 "Probability & Statistics". This file is not in
decks.json: it is not built, not gated and not deployed. To restore a slide,
move it back into lectures/content/slides/09_Probability_and_Statistics.md.
-->

<!--
Parked 2026-10-06 (storytelling pass). Stood between "Probability as a
Long-Run Frequency" and "The Frequency of a Six, Simulated" (old slide 7).
A tool detour between the definition and its demonstration: the seed and
integers(1, 7, n) are now explained in one note line on "The Frequency of a
Six, Simulated", whose runner is the first contact with default_rng in this
lecture (Lecture 08 already used default_rng(7)).
-->

---
hideInToc: true
---

# Random Numbers in **NumPy**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⌨️ **A generator with a seed**

```python
import numpy as np

rng = np.random.default_rng(1)
print(rng.random(3))            # in [0, 1)
print(rng.integers(1, 7, 10))   # a die
print(rng.normal(0, 1, 3))      # Gaussian
```

```text
[0.51182162 0.9504637  0.14415961]
[5 6 2 2 6 3 2 5 2 3]
[0.3645724  0.2941325  0.02842224]
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎰 **What the seed does**

- `default_rng(1)` makes a generator. The seed, here 1, fixes the whole sequence
- The same seed gives the same numbers in every run and on every laptop
- Another seed gives other numbers with the same properties
- The numbers come from a formula. For a simulation they behave as random ones

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **simulation** replaces the die by `rng.integers(1, 7, n)`: the lower end 1 is included, the upper end 7 is not. A million rolls take a few milliseconds. Every simulation in this lecture starts from a seeded generator, so each of its numbers can be reproduced.

</div>

<!--
Speaker: run the six lines live. Then run them again: the same numbers. Change
the seed to 2: other numbers. A result that depends on random numbers is
reproducible only if the seed is written down. (~2 min)
-->
