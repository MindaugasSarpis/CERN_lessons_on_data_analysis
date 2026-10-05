---
layout: cover
title: "Lecture X: Python Interactive (template)"

# Deck-level config (theme, colorSchema, addons, routerMode) lives ONLY in the
# generated entry (scripts/gen-entries.mjs). A lecture's cover frontmatter is
# just `layout` + `title` — plus this `python:` block on runner decks, which
# slidev-addon-python-runner reads from slide 1 (= this cover).
python:
  # Install packages from PyPI. Default: []
  installs: ["cowsay"]

  # Code executed to set up the environment. Default: ""
  prelude: |
    GREETING_FROM_PRELUDE = "Hello, Slidev!"

  # Automatically load the imported builtin packages. Default: true
  loadPackagesFromImports: true

  # Disable annoying warning from `pandas`. Default: true
  suppressDeprecationWarnings: true

  # Always reload the Python environment when the code changes. Default: false
  alwaysReload: false

  # Options passed to `loadPyodide`. Default: {}
  loadPyodideOptions: {}

---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Lecture X

### Workflow **Automation**

---

<!-- Runner block style: docs/python-runner-recipe.md. Print every result,
put its value in a trailing comment, keep lines inside the editor, ≲10 lines,
self-contained, room under the block for the output. Check with
`pnpm qa:runners --only <slug>`. -->

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
```

---

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🧮 **Half-width runner**

In a `grid-2` card a line holds about 50 characters.

</div>

<div class="card card-warning pad-tight">

```py {monaco-run} {autorun:false}
import numpy as np
a = np.array([127], dtype=np.int8)
print(a + 1)  # [-128]: int8 wraps
```

</div>

</div>

---