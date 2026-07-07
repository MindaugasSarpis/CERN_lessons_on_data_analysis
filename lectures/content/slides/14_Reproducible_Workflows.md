---
mermaid: true
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Reproducible Workflows & Automation"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Reproducible Workflows & Automation

##### <span class="aims-badge">♻️ reproducibility · ⚙️ automation</span>

<!--
Speaker: open on the pain — an analysis you cannot rerun six months later. Today
turns ad-hoc scripts into a pipeline anyone can rebuild. Serves the ♻️ + ⚙️
aims. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Science requires **reproducibility**. Good computing practices transform ad-hoc analysis scripts into professional, automated workflows that others (and future you) can understand, verify, and extend.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

📁 Structure an analysis project — separate **data, code, and config**

</div>

<div class="card card-secondary card-glass pad-compact">

⌨️ Parameterise scripts with **argparse** and readable **YAML config files**

</div>

<div class="card card-success card-glass pad-compact">

📦 Isolate dependencies in **virtual environments** with pinned versions

</div>

<div class="card card-warning card-glass pad-compact">

⚙️ Automate the pipeline with a **Makefile** so `make all` rebuilds everything

</div>

<div class="card card-accent card-glass pad-compact">

🧪 Test analysis code with **pytest** — pure functions, fixtures, regression tests

</div>

<div class="card card-info card-glass pad-compact">

🔄 Let **CI and pre-commit hooks** run those checks on every push, automatically

</div>

<div class="card card-primary card-glass pad-compact">

🗃️ Version **data**, not just code — checksums, manifests, immutable raw files

</div>

<div class="card card-secondary card-glass pad-compact">

🌍 Publish data that is **FAIR** — findable, accessible, interoperable, reusable

</div>

</div>

<!--
Speaker: frame these as promises, not a syllabus. Today is the "why + how" of
reproducible workflows; Seminar 14 is where their own project gets a pinned
environment and a Makefile. (~1 min)
-->

---
hideInToc: true
---

# Motivation

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## **The Reproducibility Crisis**

Results cannot be reproduced because:
- Code is lost or undocumented
- Dependencies are unclear
- Analysis steps are manual
- Data processing is not tracked

</div>

<div class="card card-success card-glass pad-tight">

## **Benefits of Good Practices**

- Faster iteration & collaboration
- Reliable, verifiable results
- Publication-ready code
- Career-ready skills

**Goal**: Reproducible in 5 years (or 5 hours!)

</div>

</div>

---
layout: section
hideInToc: true
---

# From **Scripts** to **Workflows**

<!--
Speaker: the arc of the whole lecture — notebook to script to modular code to an
automated pipeline. Everything that follows moves one step along this path.
(~1 min)
-->

---
hideInToc: true
---

# The Evolution of Your Analysis

<div style="display: flex; justify-content: center; align-items: center; height: 80%;">

```mermaid{scale: 1}
%%{init: {'theme': 'dark', 'themeVariables': {
  'primaryColor': '#0f1f3d',
  'primaryBorderColor': '#60a5fa',
  'primaryTextColor': '#e2e8f0',
  'secondaryColor': '#102b4c',
  'lineColor': '#5eead4',
  'fontFamily': 'Inter, Segoe UI, sans-serif',
  'fontSize': '18px'
}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': false, 'nodeSpacing': 10, 'rankSpacing': 80}}}%%
flowchart LR
    A["📓 Jupyter<br/>Notebook"]:::stage1 --> B["📜 Python<br/>Script"]:::stage2
    B --> C["📦 Modular <br/>Code"]:::stage3
    C --> D["⚙️ Automated<br/>Pipeline"]:::stage4
    D --> E["🚀 Production<br/>System"]:::stage5

    classDef stage1 fill:#0f4c81,stroke:#93c5fd,stroke-width:3px,color:#e2e8f0,rx:14px,ry:14px
    classDef stage2 fill:#155e75,stroke:#5eead4,stroke-width:3px,color:#e2e8f0,rx:14px,ry:14px
    classDef stage3 fill:#1c3d5a,stroke:#34d399,stroke-width:3px,color:#d1fae5,rx:14px,ry:14px
    classDef stage4 fill:#1e3a5f,stroke:#fbbf24,stroke-width:3px,color:#fef3c7,rx:14px,ry:14px
    classDef stage5 fill:#0b2540,stroke:#f472b6,stroke-width:3px,color:#fce7f3,rx:14px,ry:14px
```

</div>

---
hideInToc: true
---

# Anatomy of a Well-Structured Project

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight" style="font-family: monospace; font-size: 0.7em; line-height: 1.5;">

```text
my_analysis/
├── README.md
├── requirements.txt
├── config/
│   └── analysis_config.yaml
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── fitting.py
│   └── plotting.py
├── scripts/
│   ├── 1_preprocess.py
│   ├── 2_fit_model.py
│   └── 3_make_plots.py
├── notebooks/
├── tests/
├── results/
└── .gitignore
```

</div>

<div style="display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.85em;">

<div class="card card-info card-glass pad-compact">📄 <strong>Root</strong> — README, requirements, config</div>

<div class="card card-secondary card-glass pad-compact">📁 <strong>data/</strong> — raw (immutable) → processed</div>

<div class="card card-success card-glass pad-compact">📁 <strong>src/</strong> — Reusable modules & functions</div>

<div class="card card-warning card-glass pad-compact">📁 <strong>scripts/</strong> — Numbered execution steps</div>

<div class="card card-accent card-glass pad-compact">📁 <strong>notebooks/</strong> — Exploration only</div>

<div class="card card-info card-glass pad-compact">📁 <strong>tests/</strong> + <strong>results/</strong> — Tests & outputs</div>

</div>

</div>

---
hideInToc: true
---

# Key Principles

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **1. Separation of Concerns**

- **Data**: Raw vs processed (never modify raw!)
- **Code**: Reusable functions vs scripts
- **Config**: Parameters separate from code

</div>

<div class="card card-secondary card-glass pad-tight">

## **2. Clear Dependencies**

- Document required packages with versions
- Use virtual environments
- Pin critical dependencies

</div>

<div class="card card-info card-glass pad-tight">

## **3. Self-Documentation**

- README explains what & how
- Code comments explain why
- Docstrings for functions

</div>

<div class="card card-accent card-glass pad-tight">

## **4. Automation**

- Scripts run without intervention
- Results are reproducible
- Tests validate correctness

</div>

</div>

---
layout: section
hideInToc: true
---

# Command-Line **Arguments**

---
hideInToc: true
---

# Why Command-Line Arguments?

<div class="card card-warning card-glass pad-tight mt-md">

## **Problem: Hardcoded Values**

```python
# Bad: hardcoded file paths and parameters
df = pd.read_csv('data.csv')
model_fit(df, n_bins=50, range_min=0, range_max=15)
```

**Issues**: Can't easily change parameters, not reusable, manual editing required

</div>

<div class="card card-success card-glass pad-tight mt-md">

## **Solution: Command-Line Arguments**

```bash
python fit_model.py --input data.csv --bins 50 --range 0 15
python fit_model.py --input new_data.csv --bins 100 --range 5 20
```

**Benefits**: Flexible, scriptable, no code changes needed

</div>

---
hideInToc: true
---

# argparse: Python's Standard Tool

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Key Features**

- `required=True` for mandatory args
- `default=value` for optional args
- `type=int/float/str` for type conversion
- `nargs=2` for multiple values
- `action='store_true'` for flags
- `help='...'` for documentation

</div>

<div class="card card-secondary card-glass pad-tight">

## **Common Argument Types**

```python
--input file.csv      # required string
--output results.csv  # optional with default
--bins 50             # integer
--range 0 15          # two floats
--verbose             # boolean flag
```

</div>

</div>

---
hideInToc: true
---

# Script Structure with argparse

<div class="card card-info card-glass pad-tight mt-md">

## **Typical Script Pattern**

```python
import argparse

parser = argparse.ArgumentParser(description='...')
parser.add_argument('--input', required=True, help='...')
# ... more arguments ...
args = parser.parse_args()

data = load_data(args.input)
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### **Benefits**

- Flexible parameters
- Self-documenting (`--help`)
- Scriptable (batch processing)
- No code changes needed

</div>

<div class="card card-secondary card-glass pad-tight">

### **Tips**

- Use meaningful names
- Provide defaults
- Add help messages
- Validate inputs

</div>

</div>

---
layout: section
hideInToc: true
---

# Configuration **Files**

---
hideInToc: true
---

<div class="card card-info card-glass pad-tight mt-md">

## **When Command-Line Args Get Unwieldy**

Dozens of parameters → use configuration files instead!

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

### ❌ **Too Many Arguments**

```bash
python analyze.py \
  --input data.csv --bins 50 \
  --signal-mean 5.0 --bg-scale 2.0 \
  --fit-method mle --output results.png \
  --verbose --save-params params.json
```

Unreadable, error-prone!

</div>

<div class="card card-success card-glass pad-tight">

### ✅ **Config File**

```bash
python analyze.py --config analysis_config.yaml
```

```yaml
input: data.csv
bins: 50
signal: { mean: 5.0, sigma: 1.0 }
background: { scale: 2.0 }
fit_method: mle
output: results.png
```

</div>

</div>

---
hideInToc: true
---

# YAML Configuration Files

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-tight">

## **YAML: Human-Readable Config**

- Easy to read and write
- Hierarchical structure
- Comments with `#`
- Standard for config files

<strong>Basic syntax:</strong>

```yaml
key: value          # string
count: 42           # number
enabled: true       # boolean
items: [1, 2, 3]    # list
```

</div>

<div class="card card-secondary card-glass pad-tight" style="font-size: 0.7em;">

```yaml
# config.yaml
data:
  input_file: "data/raw/sample.csv"
  output_dir: "results/"

histogram:
  bins: 50
  range: [0, 15]

model:
  signal: { mean: 5.0, sigma: 1.0 }
  background: { scale: 2.0 }

fitting:
  method: "mle"
  tolerance: 1.0e-6   # decimal point → parsed as a float, not a string
```

</div>

</div>

---
hideInToc: true
---

# Loading Config in Python

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Basic Loading**

```python
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Access nested values
n_bins = config['histogram']['bins']
```

</div>

<div class="card card-secondary card-glass pad-tight">

## **Best Practices**

- Use `yaml.safe_load()` (not `load()`)
- Validate required fields exist
- Check value types and ranges
- Provide sensible defaults
- Handle missing files gracefully

</div>

</div>

<div class="card card-warning card-glass pad-tight mt-md" style="display: flex; gap: 2rem; align-items: center;">

<div>

**Why `safe_load()`?** — `yaml.load()` can execute arbitrary code (e.g., `!!python/object/apply:os.system`)

</div>

<div style="font-size: 0.9em;">

`safe_load()` only parses: `str` | `int` | `float` | `bool` | `list` | `dict` | `None`

</div>

</div>

---
hideInToc: true
---

# Combining argparse + Config Files

<div class="card card-info card-glass pad-compact mt-sm">

## **The Pattern**

Config file provides defaults; command-line arguments can override specific values.

```bash
# Use config defaults
python analyze.py --config analysis.yaml

# Override specific values
python analyze.py --config analysis.yaml --input new_data.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

### **Config File For**

- Default values
- Complex nested settings
- Documentation (comments)
- Experiment configurations

</div>

<div class="card card-secondary card-glass pad-tight">

### **CLI Args For**

- Required inputs/outputs
- Quick overrides
- Batch processing
- Scripting workflows

</div>

</div>

<div class="note-text mt-sm">

💡 **Groundwork**: build this CLI/config habit now — the running project leans on it later (Seminar 14 itself jumps straight to a pinned environment + Makefile). *See the demo for a complete implementation with validation.*

</div>

---
layout: section
hideInToc: true
---

# Virtual Environments & **Dependencies**

<!--
Speaker: "it works on my machine" is a reproducibility bug. Isolated, pinned
environments are the fix — this is the ♻️ aim in practice. (~1 min)
-->

---
hideInToc: true
---

# The Dependency Problem

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## **"It Works on My Machine!"**

- You develop with NumPy 1.24, Matplotlib 3.7
- Collaborator has different versions
- Code breaks with mysterious errors
- 6 months later: can't reproduce your own results

**Root cause**: Unmanaged dependencies

</div>

<div class="card card-success card-glass pad-tight">

## **Solution: Virtual Environments**

Isolated Python environments with pinned versions

- Each project has its own environment
- Document exact versions
- No conflicts between projects

</div>

</div>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## **Option 1: venv (built-in)**

```bash
# Create environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages
pip install numpy pandas matplotlib

# Deactivate
deactivate
```

**Pros**: Built into Python, simple

**Cons**: Only Python packages

</div>

<div class="card card-secondary card-glass pad-tight">

## **Option 2: conda**

```bash
# Create environment
conda create -n myenv python=3.11

# Activate
conda activate myenv

# Install packages
conda install numpy pandas matplotlib
# or: pip install ...

# Deactivate
conda deactivate
```

**Pros**: Handles non-Python deps (C libs, etc.), popular in science

**Cons**: Heavier, slower

  * Use `mamba` if too slow.

</div>

</div>

---
hideInToc: true
---

# requirements.txt

<div class="grid-2 mt-sm gap-md">

<div style="display: flex; flex-direction: column; gap: 0.8rem;">

<div class="card card-info card-glass pad-compact">

**The Package List** — Simple text file listing required packages with version constraints

</div>

<div class="card card-primary card-glass pad-compact">

**Version syntax:**
- `==2.0.3` — exact version
- `>=1.24.0` — minimum version
- `>=1.24,<2.0` — version range

</div>

<div class="card card-warning card-glass pad-compact">

**Tip**: `pip freeze` includes transitive deps. Better to manually list direct dependencies only.

</div>

</div>

<div>

```bash
# requirements.txt
numpy>=1.24.0,<2.0.0
pandas==2.0.3
matplotlib>=3.7.0
scipy>=1.11.0
pyyaml>=6.0
```

```bash
# Install all requirements
pip install -r requirements.txt

# Generate from current env
pip freeze > requirements.txt
```

</div>

</div>

---
hideInToc: true
---

# Modern Tooling: uv & pyproject.toml

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚡ **uv — fast, lockfile-based**

One Rust-based tool for **environments *and* dependencies**, resolving in milliseconds — the emerging 2026 standard for scientific Python.

```bash
uv init my_analysis        # project + pyproject.toml
uv add numpy pandas        # resolve, install, lock
uv run python analysis.py  # run inside the env
```

`uv.lock` pins exact versions for a byte-identical rebuild. **pixi** plays the same role in the conda world.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **pyproject.toml (PEP 621)**

One declarative file for project metadata *and* dependencies — the modern replacement for a scattered `requirements.txt` + `setup.py`.

```toml
[project]
name = "my_analysis"
requires-python = ">=3.11"
dependencies = [
  "numpy>=1.24",
  "pandas>=2.0",
]
```

Read by `uv`, `pip`, and build tools alike. ♻️

</div>

</div>

---
hideInToc: true
---

# environment.yml

<div class="grid-2 mt-sm gap-md">

<div style="display: flex; flex-direction: column; gap: 0.8rem;">

<div class="card card-info card-glass pad-compact">
<strong>Conda Alternative</strong> — Env name, channels, Python version, mix conda + pip
</div>

<div class="card card-success card-glass pad-compact">
<strong>Commands:</strong> <br>
<code>conda env create -f</code> <br>
 <code>conda env update -f</code> <br>
 <code>conda env export ></code>
</div>

</div>

<div style="font-size: 0.85em;">

```yaml
name: my_analysis
channels:
  - conda-forge
dependencies:
  - python=3.11
  - numpy>=1.24
  - pandas>=2.0
  - matplotlib>=3.7
  - pip:
      - some-pip-package
```

</div>

</div>

---
hideInToc: true
---

# Best Practices: Dependencies

<div class="grid-2 mt-sm gap-md">

<div class="card card-success card-glass pad-compact">
<strong>Do</strong>

- Use virtual environments for every project
- Document dependencies with version constraints
- Test on fresh environment before sharing
- Add <code>venv/</code>, <code>.conda/</code> to .gitignore
</div>

<div class="card card-warning card-glass pad-compact">
<strong>Don't</strong>

- Install packages globally
- Use <code>pip freeze</code> output blindly
- Pin every package to exact version
- Commit virtual environment to git
</div>

</div>

---
layout: section
hideInToc: true
---

# Automation with **Makefiles**

<!--
Speaker: this is the payoff — one command runs the whole pipeline and only
rebuilds what changed. Make is the ⚙️ aim made concrete. (~1 min)
-->

---
hideInToc: true
---

# Why Makefiles?

<div class="grid-2 mt-sm gap-md">

<div>

<div class="card card-primary card-glass pad-compact">
<strong>Automate Your Workflow</strong>

Instead of running multiple commands manually, run: <code>make all</code>
</div>

<div class="card card-info card-glass pad-compact mt-sm">
<strong>Benefits:</strong> One-command execution, tracks dependencies, only reruns what changed, documents workflow
</div>

</div>

<div class="card card-secondary card-glass pad-compact">
<strong>Common Uses</strong>

- Run analysis pipeline
- Run tests
- Generate figures
- Build documentation
- Clean temporary files
</div>

</div>

---
hideInToc: true
---

# Basic Makefile Syntax

<div class="grid-2 mt-sm gap-md">

<div style="font-size: 0.82em;">

```makefile
# Makefile for analysis pipeline

# Main target - runs full pipeline
all: results/plot.png

# Plot depends on clean data and script
results/plot.png: data/clean.csv scripts/plot.py
	python scripts/plot.py

# Clean data depends on raw data
data/clean.csv: data/raw.csv scripts/clean.py
	python scripts/clean.py

# Utility targets (don't create files)
.PHONY: all clean

clean:
	rm -rf results/* data/clean.csv
```

</div>

<div>

<div class="card card-info card-glass pad-compact">
<strong>Key Concepts</strong>

- <strong>Target</strong>: File to create
- <strong>Dependencies</strong>: Files it needs
- <strong>Command</strong>: How to build (TAB!)
- <strong>Phony</strong>: Non-file targets
</div>

<div class="card card-success card-glass pad-compact mt-sm">
<strong>Usage</strong>

<code>make all</code> — run pipeline<br>
<code>make clean</code> — remove outputs
</div>

<div class="card card-info card-glass pad-compact mt-sm">
📚 <strong>When pipelines outgrow Make</strong> — reach for a data-science DAG runner: <strong>Snakemake</strong> (Python rules, wildcards, cluster/conda support) or <strong>targets</strong> (R). Same idea, more power — but start with Make.
</div>

</div>

</div>

---
hideInToc: true
---

# Using the Makefile

```bash
make all          # run the entire pipeline
make clean; make all   # wipe and rebuild
make test         # run tests   ·   make help
```

**Smart rebuilding**:
```bash
# First run: builds everything
make all

# Edit only the plotting script
vim scripts/3_make_plots.py

# Second run: only regenerates plot (skips preprocessing and fitting!)
make all
```

<div class="card card-accent card-glass pad-tight mt-sm">

Make checks file timestamps. If dependencies are newer than target, it rebuilds. Otherwise, it skips!

</div>

---
hideInToc: true
---

# Make vs Snakemake vs a Plain Script

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📜 **Plain script**

One `run_all.sh` calling every step in order.

**Good for**: a linear 2–3 step pipeline, one contributor.

**Weak on**: always reruns everything — no dependency tracking.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔧 **Make**

Tracks file timestamps; reruns only stale targets.

**Good for**: most single-analysis pipelines — portable, `make` is everywhere.

**Weak on**: branching workflows, parameter sweeps.

</div>

<div class="card card-accent card-glass pad-compact">

## 🐍 **Snakemake**

Python-native rules, wildcards, cluster & conda support.

**Good for**: many samples/parameters, HPC submission.

**Weak on**: overkill for one small analysis.

</div>

</div>

<div class="note-text mt-sm">

💡 What matters: **dependency tracking**, **partial re-runs**, and **portability** 🔧. Start with a script; add Make when reruns waste time; add Snakemake when parameters multiply.

</div>

---
layout: section
hideInToc: true
---

# Continuous Integration with **GitHub Actions**

<!--
Speaker: CI runs your tests and pipeline automatically on every push — the
machine enforces reproducibility so you do not have to remember. (~1 min)
-->

---
hideInToc: true
---

# DataOps & automation

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## ⏱️ Schedule data pipelines with orchestration tools

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔄 Leverage CI/CD for tests, linting, deployment

</div>

<div class="card card-accent card-glass pad-tight">

## 📐 Parameterise workflows for reproducibility

</div>

<div class="card card-info card-glass pad-tight">

## 📡 Monitor pipelines for latency, failures, data drift

</div>

</div>

---
hideInToc: true
---

# Testing your analysis

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🧪 Unit tests for data transforms & calculations

</div>

<div class="card card-secondary card-glass pad-tight">

## ✅ Data validation (great expectations, pydantic, pandera)

</div>

<div class="card card-accent card-glass pad-tight">

## 📊 Statistical tests to confirm assumptions

</div>

<div class="card card-info card-glass pad-tight">

## 📂 Golden datasets & regression tests for dashboards

</div>

<div class="card card-success card-glass pad-tight">

## 👁️ Peer review before results leave the team

</div>

</div>

---
hideInToc: true
---

# From "It Looked Fine" to a Test

<div class="card card-warning card-glass pad-tight mt-md">

## 😬 **"I ran it and the plot looked fine"**

That is not evidence — a silent off-by-one in a selection cut can shift a peak by 10 MeV and still "look fine" on a busy histogram. A **test** checks a known number, every time, automatically.

</div>

<div class="card card-info card-glass pad-tight mt-sm">

## 🎯 **What we test**

A small, pure analysis function — not a plot, not a whole script. Something with one clear right answer for a known input.

</div>

---
hideInToc: true
---

# Your First pytest Test

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-tight">

## **The function**

```python
# src/selection.py
def is_signal_region(mass):
    """True if mass sits in the D0 window."""
    return 1.80 < mass < 1.93
```

</div>

<div class="card card-secondary card-glass pad-tight">

## **The test**

```python
# tests/test_selection.py
from src.selection import is_signal_region

def test_accepts_known_peak():
    assert is_signal_region(1.865)

def test_rejects_sideband():
    assert not is_signal_region(2.5)
```

</div>

</div>

<div class="note-text mt-sm">

One `assert` per fact you know must hold. Name the test after the behaviour it checks, not the function.

</div>

---
hideInToc: true
---

# Testing Edge Cases

<div class="card card-info card-glass pad-tight mt-md">

## 🧪 **Beyond the happy path**

Real data is messy — a good test suite checks the cases that break code silently.

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

### **Empty input**

```python
def test_empty_returns_empty():
    result = select(np.array([]))
    assert len(result) == 0
```

</div>

<div class="card card-accent card-glass pad-compact">

### **NaN values**

Append to `tests/test_selection.py` (add `import numpy as np` at the top):

```python
def test_nan_is_rejected():
    assert not is_signal_region(np.nan)
```

</div>

</div>

<div class="note-text mt-sm">

If a function silently returns `True` for `NaN` or crashes on an empty array, you want to know **before** it corrupts a fit — not after.

</div>

---
hideInToc: true
---

# Running pytest & Reading the Output

<span class="def-sub">A collaborator "tidies up" the cut to `return not (mass < 1.80 or mass > 1.93)` — identical to the original for every real number. Run the tests:</span>

<div class="card card-primary card-glass pad-tight mt-sm">

```bash
$ pytest tests/ -v
tests/test_selection.py::test_accepts_known_peak PASSED
tests/test_selection.py::test_rejects_sideband PASSED
tests/test_selection.py::test_nan_is_rejected FAILED

=============== FAILURES ===============
    def test_nan_is_rejected():
>       assert not is_signal_region(np.nan)
E       assert not True
E        +  where True = is_signal_region(nan)
tests/test_selection.py:12: AssertionError
====== 1 failed, 2 passed in 0.05s ======
```

</div>

<div class="note-text mt-sm">

For `NaN`, **both** comparisons are `False`, so the rewrite returns `True` — two forms identical for every normal number diverge on `NaN`. Each line is one test; the traceback names the exact failing `assert`. *(Output trimmed to the interesting lines.)*

</div>

---
hideInToc: true
---

# What (Not) to Test in an Analysis

<div class="grid-2 mt-sm gap-md">

<div class="card card-success card-glass pad-tight">

## ✅ **Worth testing**

- Selection cuts (mass windows, quality flags)
- Unit conversions & physical constants
- Data-loading edge cases (empty file, missing column)
- Fit-result sanity (parameter in a physical range)

</div>

<div class="card card-warning card-glass pad-tight">

## ❌ **Not worth testing**

- Exact pixel colours or figure DPI
- Wording of axis labels or titles
- Anything that changes every run by design (timestamps)

</div>

</div>

<div class="note-text mt-sm">

Rule of thumb: test **logic with a right answer**, not **appearance with a taste**.

</div>

---
hideInToc: true
---

<MCQ
  question="Which of these is most worth writing a unit test for?"
  :options="[
    'The exact shade of blue used in a histogram',
    'A signal-region selection cut that must accept 1.865 GeV and reject 2.5 GeV',
    'The DPI setting used when saving a PNG',
    'The wording of an axis label'
  ]"
  :correct="1"
  explanation="Tests are for logic with a right answer — selection cuts, unit conversions, edge cases. Plot styling is a visual choice, not a correctness question."
/>

---
hideInToc: true
---

# What is CI/CD?

<div class="card card-info card-glass pad-compact">
<strong>Continuous Integration / Deployment</strong> — Automatically run tasks when you push code: tests, style checks, build docs, run pipeline. <strong>Benefits:</strong> Catch errors early, ensure reproducibility.
</div>

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#0f1f3d', 'primaryBorderColor': '#60a5fa', 'primaryTextColor': '#e2e8f0', 'lineColor': '#5eead4'}, 'flowchart': {'curve': 'basis'}}}%%
flowchart LR
    A[Push Code]:::action --> B[GitHub Actions]:::process
    B --> C[Tests]:::step
    B --> D[Style]:::step
    C --> E{Pass?}:::decision
    D --> E
    E -->|Yes| F[Success]:::success
    E -->|No| G[Fail]:::fail

    classDef action fill:#0f4c81,stroke:#93c5fd,color:#e2e8f0
    classDef process fill:#155e75,stroke:#5eead4,color:#e2e8f0
    classDef step fill:#1c3d5a,stroke:#34d399,color:#d1fae5
    classDef decision fill:#0b2540,stroke:#fcd34d,color:#fef3c7
    classDef success fill:#134e4a,stroke:#34d399,color:#d1fae5
    classDef fail fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

---
hideInToc: true
---

# GitHub Actions: Basic Workflow

<div class="grid-2 mt-sm gap-md">

<div style="font-size: 0.78em;">

```yaml
# .github/workflows/test.yml
name: Run Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - run: pip install -r requirements.txt
    - run: pytest tests/ -v
```

</div>

<div>

<div class="card card-info card-glass pad-compact">
<strong>Key Parts</strong>

- <strong>on:</strong> When to trigger (push, PR)
- <strong>runs-on:</strong> VM type (ubuntu)
- <strong>steps:</strong> Sequential actions
- <strong>uses:</strong> Pre-built actions
- <strong>run:</strong> Shell commands
</div>

<div class="card card-success card-glass pad-compact mt-sm">
Every push/PR now automatically runs your tests!
</div>

</div>

</div>

---
hideInToc: true
---

# Advanced: Analysis Pipeline

<div class="grid-2 mt-sm gap-md">

<div style="font-size: 0.75em;">

```yaml
name: Analysis Pipeline
on:
  push:
    branches: [main]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - run: pip install -r requirements.txt
    - run: make all
    - uses: actions/upload-artifact@v4
      with:
        name: results
        path: results/
```

</div>

<div>

<div class="card card-info card-glass pad-compact">
<strong>Pipeline Steps</strong>

1. Checkout code
2. Setup Python
3. Install dependencies
4. Run analysis (<code>make all</code>)
5. Upload results as artifact
</div>

<div class="card card-accent card-glass pad-compact mt-sm">
<strong>Optional:</strong> Auto-commit results back to repo, send notifications, deploy to web
</div>

</div>

</div>

---
layout: section
hideInToc: true
---

# Pre-commit **Hooks**

<!--
Speaker: the seatbelt you stop noticing — checks run locally, before a commit
lands, so bad formatting or an accidental notebook output never even reaches
CI. (~1 min)
-->

---
hideInToc: true
---

# What Runs Before You Even Push

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🎨 **Formatter** (black, ruff format) — rewrites code to one house style, no debate

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔍 **Linter** (ruff, flake8) — flags unused imports, undefined names, obvious bugs

</div>

<div class="card card-accent card-glass pad-tight">

## 📓 **Notebook-output stripper** (nbstripout) — clears cell outputs so diffs stay readable

</div>

<div class="card card-info card-glass pad-tight">

## 🚫 **Big-file / secret guards** — block an accidental `data.root` or `.env` commit

</div>

</div>

---
hideInToc: true
---

# A Minimal `.pre-commit-config.yaml`

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/kynan/nbstripout
    rev: 0.7.1
    hooks:
      - id: nbstripout
```

</div>

<div class="stack-tight">

<div class="card card-info card-glass pad-compact">

**Install once**: `pre-commit install`

</div>

<div class="card card-success card-glass pad-compact">

**Every commit**: hooks run automatically — a failing hook blocks the commit until you fix it

</div>

</div>

</div>

<div class="note-text mt-sm">

Same tools the course already uses (formatting, notebook cleanliness) — now enforced automatically, so conventions hold even under deadline pressure. ⚙️ The `rev:` pin (required!) is the reproducibility guarantee: every collaborator runs exactly the same hook version. ♻️

</div>

---
layout: section
hideInToc: true
---

# Versioning **Data**

<!--
Speaker: git is for code. Data needs a different trick — the on-ramp to the
FAIR + provenance discussion that follows. (~1 min)
-->

---
hideInToc: true
---

# Why Git Chokes on Data

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **The problem**

Git stores every version of every file, forever. A 2 GB ROOT file changed 10 times means **20 GB** in `.git/` — clones become huge and slow.

</div>

<div class="card card-success card-glass pad-tight">

## 💡 **The idea**

Store the data **once**, content-addressed by its hash. Git tracks a tiny **pointer file** instead — the data itself lives outside the repo.

</div>

</div>

---
hideInToc: true
---

# A Pointer File, Not the Data

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

**What git actually stores** — `sample.csv.dvc`:

```yaml
outs:
  - md5: 8f14e45fceea167a5a36dedd4bea2543
    path: sample.csv
    size: 2147483648
```

</div>

<div class="card card-secondary card-glass pad-compact">

**What happens**

`dvc pull` fetches the real file from remote storage using that hash — the repo stays small, the data stays exact.

</div>

</div>

<div class="note-text mt-sm">

Same principle behind Git LFS and content-addressed storage generally: **the hash *is* the identity** — change one byte and everyone notices. 📁

</div>

---
hideInToc: true
---

# Data Versioning: The Toolbox

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🗃️ **DVC**

Git-native; pairs a pointer file with any remote (S3, GDrive, SSH).

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **Git LFS**

Simpler, GitHub-integrated; swaps large files for pointers transparently.

</div>

<div class="card card-accent card-glass pad-compact">

## 🏛️ **Zenodo DOIs**

For a **finished** dataset: upload once, get a permanent, citable identifier.

</div>

</div>

<div class="note-text mt-sm">

Teaser only — pick one when a project's data actually outgrows git. The DOI idea reappears next: it's the **F** in FAIR.

</div>

---
layout: section
hideInToc: true
---

# **FAIR** Principles

<!--
Speaker: FAIR = Findable, Accessible, Interoperable, Reusable. Frame it as the
standard that lets a stranger reuse your data a decade later — then show CERN
Open Data as living proof it works at petabyte scale. (~1 min)
-->

---
layout: quote
hideInToc: true
---

## The first step in **(re)using data** is to find them. **Metadata** and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services — a core component of the FAIRification process.

<div class="note-text" style="text-align: right; margin-top: 1.5rem;">— GO FAIR, after Wilkinson et al. (2016), <em>Scientific Data</em></div>

---
hideInToc: true
---

# **Findable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🏷️ **F1.** (Meta)data are assigned a globally **unique** and persistent **identifier**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **F2.** Data are described with **rich metadata**

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 **F3.** Metadata explicitly **include the identifier** of the data they describe

</div>

<div class="card card-info card-glass pad-tight">

## 🔍 **F4.** (Meta)data are registered or indexed in a **searchable resource**

</div>

</div>

---
hideInToc: true
---

# **Accessible** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🌐 **A1.** (Meta)data are retrievable by their identifier using a standardised communications protocol

</div>

<div class="card card-secondary card-glass pad-tight">

## 📖 **A1.1** The protocol is **open**, free, and universally implementable

</div>

<div class="card card-accent card-glass pad-tight">

## 🔐 **A1.2** The protocol allows for **authentication** and **authorisation** where necessary

</div>

<div class="card card-info card-glass pad-tight">

## 📂 **A2.** Metadata are accessible even when the data are no longer available

</div>

</div>

---
hideInToc: true
---

# **Interoperable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🗣️ **I1.** (Meta)data use a formal, accessible, shared, and broadly applicable **language for knowledge representation**

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔗 **I2.** (Meta)data use vocabularies that follow **FAIR principles**

</div>

<div class="card card-accent card-glass pad-tight">

## 📎 **I3.** (Meta)data include **qualified references** to other (meta)data

</div>

</div>

---
hideInToc: true
---

# Interoperability · **what breaks it vs. what fixes it**

<span class="def-sub">"I just shared the CSV" is not interoperability. The machine — and the next analyst — still needs to know what every column means and in what units.</span>

<div class="grid-2 gap-md mt-md tidy-cards">

<div class="card card-warning card-glass pad-compact">

## ❌ **Proprietary format**

`.xlsx` with merged cells, macros, embedded plots. Only opens cleanly in one tool, parses poorly everywhere else.

**Fix:** CSV / Parquet / HDF5 — open, typed, streamable.

</div>

<div class="card card-warning card-glass pad-compact">

## ❌ **Missing units**

A column `mass` with values `[72, 68, 75]`. Kilograms? Pounds? Per event? No one can tell.

**Fix:** units in the column name (`mass_kg`) or a sidecar schema file.

</div>

<div class="card card-warning card-glass pad-compact">

## ❌ **Undocumented codes**

`status` column with values `{1, 2, 3, 9}` and no legend. The meaning lives in someone's head.

**Fix:** a README mapping each code + a controlled vocabulary (ICD, MeSH, PDG, …).

</div>

<div class="card card-warning card-glass pad-compact">

## ❌ **Opaque timestamps**

`ts = 1712937600` — seconds? milliseconds? Which timezone? From when?

**Fix:** ISO 8601 strings with explicit offset (`2024-04-12T14:00:00+02:00`).

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

## 💡 **Rule of thumb**

A dataset is interoperable when a stranger, with no access to you, can correctly merge it with their own data **without guessing.**

</div>

---
hideInToc: true
---

# **Reusable** data

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📋 **R1.** (Meta)data are **richly described** with a plurality of accurate and relevant attributes

</div>

<div class="card card-secondary card-glass pad-tight">

## 📜 **R1.1.** (Meta)data are released with a clear and **accessible** data usage **license**

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 **R1.2.** (Meta)data are associated with detailed **provenance**

</div>

<div class="card card-info card-glass pad-tight">

## 🏛️ **R1.3.** (Meta)data meet **domain-relevant community standards**

</div>

</div>

---
hideInToc: true
---

# FAIR in practice

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 🏷️ Assign DOIs or persistent IDs through catalogues

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 Publish rich metadata schemas (Dublin Core, DataCite, schema.org)

</div>

<div class="card card-accent card-glass pad-tight">

## 🌐 Provide API/documentation for programmatic access

</div>

<div class="card card-info card-glass pad-tight">

## 📖 Reuse domain ontologies and controlled vocabularies

</div>

<div class="card card-success card-glass pad-tight">

## 🔄 Capture provenance with tools like REANA, DVC, Quilt

</div>

</div>

---
hideInToc: true
---

# FAIR worked example — a CERN Open Data record

<div class="card card-info card-glass pad-compact mt-sm">

<div class="note-text">

An LHCb research-grade dataset on opendata.cern.ch — annotated against each FAIR pillar.

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="stack-tight">

<div class="card card-primary card-glass pad-tight">

## 🔍 **Findable**

DOI `10.7483/OPENDATA.LHCB.…`, title, keywords, indexed on Google Dataset Search

</div>

<div class="card card-secondary card-glass pad-tight">

## 🌐 **Accessible**

HTTPS download + XRootD streaming, free, no login required; metadata stays online if files are retired

</div>

</div>

<div class="stack-tight">

<div class="card card-accent card-glass pad-tight">

## 🔗 **Interoperable**

ROOT / AOD format with published schema, HEP-specific vocabularies, links to detector & simulation records

</div>

<div class="card card-success card-glass pad-tight">

## ♻️ **Reusable**

CC0 licence, full provenance (run conditions, software version), validated example analyses in containers

</div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

<div class="note-text">

#### 🎯 Every FAIR principle is concretely visible — that's why CERN data can be reanalysed a decade later

</div>

</div>

---
layout: section
hideInToc: true
---

# Best Practices **Summary**

---
hideInToc: true
---

# Reproducible Analysis Checklist (1/2)

<div class="card card-success card-glass pad-tight mt-md">

## ✅ **Essential Practices**

<div class="grid-2 mt-sm gap-md">

<div>

- [ ]  Use version control (Git)
- [ ]  Document dependencies (requirements.txt)
- [ ]  Use virtual environments
- [ ]  Write README with setup instructions
- [ ]  Separate raw and processed data

</div>

<div>

- [ ]  Use config files for parameters
- [ ]  Never commit generated files
- [ ]  Add .gitignore
- [ ]  Test on clean environment

</div>

</div>

</div>

---
hideInToc: true
---

# Reproducible Analysis Checklist (2/2)

<div class="card card-info card-glass pad-tight mt-md">

## 🚀 **Advanced Practices**

<div class="grid-2 mt-sm gap-md">

<div>

- [ ]  Modular code (functions/classes)
- [ ]  Command-line arguments (argparse)
- [ ]  Automated pipeline (Make/Snakemake)
- [ ]  Unit tests (pytest)
- [ ]  CI/CD (GitHub Actions)

</div>

<div>

- [ ]  Docker container (optional)
- [ ]  Logging instead of print()
- [ ]  Code style checking (black, ruff)
- [ ]  Documentation (Sphinx)

</div>

</div>

</div>

---
hideInToc: true
---

# Example README.md

<div class="grid-2 mt-sm gap-md">

<div class="card card-info card-glass pad-compact">
<strong>README Essentials</strong>

- Title & description
- Setup instructions
- How to run analysis
- Project structure
- Input/output files
- Dependencies
- Citation & license
</div>

<div style="font-size: 0.75em;">

```markdown
# D0 Lifetime Analysis
LHCb Open Data: D0 → K-π+ decay.

## Setup
    git clone ... && cd d0-lifetime
    python -m venv venv
    pip install -r requirements.txt

## Usage
    make all    # Full analysis pipeline
    make test   # Run unit tests
    make clean  # Remove outputs

## Structure
    data/       # Input ROOT files
    results/    # Plots and fits
    src/        # Analysis scripts
```

</div>

</div>

---
hideInToc: true
---

# Version Control: .gitignore

<div class="grid grid-cols-2 gap-4">
<div>

<div class="card card-warning card-glass pad-tight">

**Never commit**:
- Large data files (use Git LFS or external storage)
- Generated results (should be reproducible!)
- Virtual environments
- OS-specific files
- Credentials/secrets

</div>

</div>
<div class="overflow-y-auto max-h-85">

```bash
# .gitignore for data analysis project

# Data (too large, or stored elsewhere)
data/raw/*.csv
data/raw/*.root
data/processed/

# Generated results
results/
*.png
*.pdf
figures/

# Virtual environments
venv/
env/
.conda/

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Secrets
.env
credentials.json
*.key

# Logs
*.log
logs/
```

</div>
</div>

---
layout: section
hideInToc: true
---

# Docker: **Containerization** (Optional/Advanced)

---
hideInToc: true
---

# Why Docker?

<div class="grid grid-cols-2 gap-4">
<div>

<div class="card card-info card-glass pad-tight">

**Ultimate Reproducibility**

**Virtual environments** handle Python packages. **Docker containers** handle *everything*:
- Operating system
- System libraries
- Python + packages
- Your code

**Result**: "It works on my machine" → "It works everywhere"

</div>

</div>
<div>

<div class="card card-primary card-glass pad-tight">

**Use Cases**
- Share analysis with exact environment
- Run on HPC clusters
- Deploy to production
- Archive for long-term reproducibility

</div>

<div class="card card-secondary card-glass pad-tight mt-2">

**When to Use**
- Complex dependencies (ROOT, GEANT4)
- Collaboration with diverse systems
- Production deployment
- Long-term preservation

</div>

</div>
</div>

---
hideInToc: true
---

# Basic Dockerfile

<div class="grid grid-cols-2 gap-4">
<div>

```dockerfile
# Dockerfile - Analysis environment
FROM python:3.11-slim
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command
CMD ["python", "scripts/run_analysis.py"]
```

</div>
<div>

```bash
# Build container
docker build -t my-analysis .

# Run analysis in container
docker run my-analysis

# Interactive session
docker run -it my-analysis /bin/bash

# Mount local data
docker run -v $(pwd)/data:/app/data my-analysis
```

<div class="card card-accent card-glass pad-tight mt-2">

**Note**: Start with virtual environments, add Docker when needed.

</div>

</div>
</div>

---
layout: section
hideInToc: true
---

# Real-World **Example**

---
hideInToc: true
---

# Putting It All Together: From Chaos to Order

<div class="grid grid-cols-2 gap-4">

<div class="card card-warning card-glass pad-tight">

**Before**

```text
analysis_final_FINAL_v3.ipynb
data.csv
fit_attempt2_working.py
plot_results_old.py
results_oct22_updated.png
untitled.py
```

- Unclear what to run
- Can't reproduce results

</div>

<div class="card card-success card-glass pad-tight">

**After**

```text
my_analysis/
├── README.md
├── requirements.txt
├── Makefile
├── config/analysis.yaml
├── scripts/
│   ├── 1_preprocess.py
│   ├── 2_fit.py
│   └── 3_plot.py
```

- Clear workflow (`make all`)
- Reproducible & tested

</div>

</div>

---
hideInToc: true
---

# Workflow Execution

<div class="grid grid-cols-2 gap-4">
<div>

```bash
# First-time setup (once)
git clone https://github.com/username/analysis.git
cd analysis
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run analysis (any time)
make all

# Run tests
make test

# Clean and rerun
make clean && make all
```

</div>
<div>

```bash
# Output:
# Step 1/3: Preprocessing data...
# Step 2/3: Fitting model...
#   Fitted mean: 5.021 ± 0.015
#   Chi-squared/dof: 1.03
# Step 3/3: Generating plots...
# ✅ Analysis complete! Results in results/

# Push results
git add results/fit_params.csv
git commit -m "Update fit results"
git push
```

<div class="card card-accent card-glass pad-tight mt-2">

**One command** runs everything. **Anyone** can reproduce your results!

</div>

</div>
</div>

---
hideInToc: true
---

# Benefits in Practice

<div class="grid grid-cols-3 gap-4">

<div class="card card-primary card-glass pad-tight">

**For You**

- Faster iteration
- Easier to modify
- Less debugging
- Confidence in results
- Easy to revisit old work

</div>

<div class="card card-secondary card-glass pad-tight">

**For Collaborators**

- Easy onboarding
- Clear workflow
- Reproducible results
- Parallel work (no conflicts)
- Review-friendly code

</div>

<div class="card card-info card-glass pad-tight">

**For Science**

- Reproducible research
- Transparent methods
- Easier peer review
- Reusable by others
- Career-ready skills

</div>

</div>

---
hideInToc: true
---

<MCQ
  question="What makes a data-analysis workflow 'scriptable' rather than 'non-scriptable'?"
  :options="[
    'It is written by hand in a lab notebook',
    'Every step can be expressed as code or commands and re-run from scratch to reproduce the same results',
    'It relies on clicking through menus in a graphical application',
    'It can only be run once, then discarded'
  ]"
  :correct="1"
  explanation="Scriptable workflows are reproducible and shareable; GUI point-and-click ones leave no reliable record and are hard to replay or verify — the ♻️ and ⚙️ aims in one idea."
/>

---
hideInToc: true
---

# The Course So Far

<div class="grid-3 mt-sm gap-md" style="font-size: 0.74em;">

<div class="card card-primary card-glass pad-compact">

**A · Foundations & Tooling** (01–06)
- Computers, files, the command line
- Markdown, VS Code, Git

</div>

<div class="card card-secondary card-glass pad-compact">

**B · Programming** (07–08)
- Python foundations
- Python for data & files

</div>

<div class="card card-info card-glass pad-compact">

**C · Data Analysis Core** (09–12)
- Concepts, visualisation
- Probability, statistics, fitting

</div>

<div class="card card-success card-glass pad-compact">

**D · Practical Data Work** (13–14)
- NumPy & Pandas
- ⭐ Reproducible workflows *(here)*

</div>

<div class="card card-warning card-glass pad-compact">

**E · Advanced** *(optional)* (15–16)
- Computing infrastructure & HPC
- Machine learning & AI

</div>

<div class="card card-accent card-glass pad-compact">

**The four aims, all along**
- 🔧 agnostic · ♻️ reproducible
- ⚙️ automated · 📁 organised data

</div>

</div>

<div class="note-text mt-sm" style="text-align:center;">

Everything today — config files, environments, Make, CI — is the **♻️ + ⚙️ aims made concrete**: an analysis anyone can rebuild with one command.

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Structure a project and separate **raw data, code, and config**

</div>

<div class="card card-success card-glass pad-compact">

✅ Parameterise runs with **argparse** and **YAML config files**

</div>

<div class="card card-success card-glass pad-compact">

✅ Pin dependencies in a reproducible **virtual environment**

</div>

<div class="card card-success card-glass pad-compact">

✅ Automate the pipeline so **`make all`** rebuilds every result

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 14 tie-in**

make your whole pipeline rebuild with one command — a pinned environment plus a Makefile so `make all` reproduces every result.

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each card. The tie-in
makes it concrete: in Seminar 14 their own analysis becomes one-command
reproducible. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Start small. Don't try to implement everything at once. Add one improvement per project: argparse this week, Makefile next week, tests the following. Incrementally build good habits.
