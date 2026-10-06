<!--
Parked slides from slides/07_Python_for_Data_and_NumPy.md.

This file is not in decks.json: it is not built, not gated and not deployed.
To put a slide back, move it into the lecture file.

Parked on 2026-10-06, in the storytelling pass (hook "guess the mean TAU"):
"Try It — Creating Arrays" stood after "`float32` and `float64` on the Data
File" and before "**Shape**: Rows and Columns", in the section `dtype` &
Shape. It answered none of the four questions of the lecture, and Seminar 7
does not use np.zeros, np.arange or np.linspace. The one linspace the deck
still uses ("Try It — Time Both") carries a comment.
-->

---
hideInToc: true
---

# Try It — **Creating Arrays**

```py {monaco-run} {autorun:false}
import numpy as np

print(np.array([20, 30, 40]))
print(np.zeros(4))
print(np.arange(20, 101, 10))
print(np.linspace(1815, 1915, 5))
print(np.zeros((2, 3)))
```

<div class="card card-info card-glass pad-compact mt-md">

`np.array` takes a list. `np.zeros(n)` gives *n* zeros to be filled later. `np.arange(start, stop, step)` counts like `range` and leaves the stop out. `np.linspace(start, stop, n)` gives *n* values at equal distances and includes both ends. `np.zeros((2, 3))` has two rows and three columns.

</div>

<!--
Speaker: run it, then ask for the nine lengths of the pendulum table in
metres: np.arange(20, 101, 10) / 100, or np.linspace(0.2, 1.0, 9). (~3 min)
-->

