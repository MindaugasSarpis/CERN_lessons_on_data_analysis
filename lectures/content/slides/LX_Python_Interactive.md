---
background: ./background_default.jpg


theme: ./theme
drawings:
  persist: false

transition: fade
title: "Lecture 1: Course Orientation and Motivation"
layout: cover

class: text-left

addons:
  - slidev-addon-python-runner

# Optional configuration for this runner
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

# Lessons on **Data Analysis** from **CERN**

## Lecture X

### Workflow **Automation**

---

```py {monaco-run}
from termcolor import colored

print(colored("Hello, Slidev!", "blue"))
```

---