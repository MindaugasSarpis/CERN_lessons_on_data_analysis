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

```py {monaco-run} {autorun:false}
from termcolor import colored

print(colored("Hello, Slidev!", "blue"))
```

---