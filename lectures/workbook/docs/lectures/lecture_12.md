# L12: Reproducible Workflows & Automation

---

## Overview

**Duration**: ~120 minutes (2 h slot)

**Prerequisites**: L1-L11 (especially L8 on Git)

**Learning Objectives**:
- Structure analysis projects professionally
- Use command-line arguments (argparse)
- Manage dependencies with virtual environments
- Write configuration files (YAML)
- Automate workflows with Makefiles
- Set up CI/CD with GitHub Actions
- Understand Docker basics (optional/advanced)

---

## Lecture Structure

### Part 1: Why Reproducibility Matters (10 min)
- The reproducibility crisis in science
- "Works on my machine" problem
- Benefits: faster iteration, easier collaboration, career skills
- Show before/after: chaotic notebook vs professional workflow

### Part 2: Project Structure (15 min)
- Anatomy of well-organized project
- Separation of concerns: data, code, config, results
- Never modify raw data!
- Directory structure best practices

### Part 3: Command-Line Arguments (20 min)
- Why hardcoded values are bad
- Introduce argparse
- **Live demo**: Convert hardcoded script to CLI tool
- Show help messages, required vs optional args

### Part 4: Configuration Files (15 min)
- When config files are better than args
- YAML syntax and structure
- Loading config in Python
- Combining argparse + config files

### Part 5: Virtual Environments (15 min)
- The dependency problem
- Creating venv and conda environments
- requirements.txt best practices
- Documenting Python version

### Part 6: Automation with Make (15 min)
- Why Makefiles?
- Basic syntax (targets, dependencies, commands)
- **Live demo**: Create Makefile for analysis pipeline
- Running: `make all`, `make clean`, `make test`

### Part 7: CI/CD with GitHub Actions (10 min)
- What is CI/CD?
- Basic GitHub Actions workflow
- Automatically run tests on push
- (Optional) Auto-run analysis pipeline

### Part 8: Best Practices Summary (5 min)
- Reproducibility checklist
- README template
- .gitignore essentials

---

## Teaching Tips

### Common Student Struggles

1. **"This seems like a lot of overhead for simple analysis!"**
   - Start small, add one thing at a time
   - Show long-term payoff (6 months later, can still run it!)
   - Emphasize: "Future you" will thank present you
   - Cost upfront, massive savings later

2. **"My Makefile isn't working!"**
   - **Must use TAB, not spaces!** (Most common error)
   - Check file paths (relative vs absolute)
   - Use `make -n` to dry-run and see commands

3. **"Virtual environments are confusing"**
   - Analogize: separate toolboxes for different projects
   - Show `pip list` before and after activation
   - Emphasize: prevents "it worked yesterday" syndrome

4. **"Do I really need all of this?"**
   - For one-off script: maybe not
   - For analysis you'll publish: absolutely!
   - For collaboration: essential
   - Show real-world example of paper retraction due to irreproducible analysis

### Interactive Elements

- **Before/after challenge**: Show messy project, have students identify problems
- **Pair programming**: One writes config file, other writes loading code
- **Makefile race**: Who can create working Makefile first?
- **Debug session**: Intentionally break things, troubleshoot together

### Hands-On Exercises

**Exercise 1** (Warm-up): Add argparse to existing script
```python
# Take hardcoded script from L10
# Add --input, --output, --bins arguments
# Test with different values
```

**Exercise 2** (Core): Create project structure
```bash
# Start with messy directory
# Reorganize into proper structure
# Add README, requirements.txt, .gitignore
# Create Makefile
```

**Exercise 3** (Advanced): Full workflow automation
- Multi-step analysis (preprocess → fit → plot)
- Config file for all parameters
- Makefile that runs entire pipeline
- GitHub Actions to test on push

---

## Common Questions & Answers

**Q**: Isn't this just software engineering, not data analysis?
**A**: Modern data analysis **is** software engineering! Computational reproducibility is as important as experimental reproducibility.

**Q**: Can't I just use Jupyter notebooks?
**A**: Notebooks are great for exploration, but scripts are better for reproducibility. Use both! Explore in notebooks, productionize as scripts.

**Q**: My collaborator doesn't know Git/Make/etc. What do I do?
**A**: Write clear README. Provide simple commands. Consider this a teaching opportunity!

**Q**: Should I commit generated results to Git?
**A**: Generally no (they should be reproducible!). Exception: small, important results for papers. Use Git LFS for large files.

**Q**: What if my analysis takes 24 hours to run?
**A**: Cache intermediate results. Makefiles help here! Only rerun what changed. Consider workflow managers (Snakemake, Nextflow) for very complex pipelines.

---

## Key Code Snippets

### argparse template
```python
import argparse

parser = argparse.ArgumentParser(description='Analysis script')
parser.add_argument('--input', required=True, help='Input CSV file')
parser.add_argument('--output', default='results.png', help='Output file')
parser.add_argument('--bins', type=int, default=50, help='Number of bins')
args = parser.parse_args()

# Use: python script.py --input data.csv --bins 100
```

### YAML config
```yaml
# config.yaml
data:
  input_file: "data/sample.csv"
  output_dir: "results/"

model:
  bins: 50
  range: [0, 15]
```

```python
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)
n_bins = config['model']['bins']
```

### Basic Makefile
```makefile
.PHONY: all clean test

all: results/plot.png

results/plot.png: data/clean.csv scripts/plot.py
	python scripts/plot.py --input data/clean.csv --output results/plot.png

clean:
	rm -rf results/*

test:
	pytest tests/
```

### GitHub Actions
```yaml
name: Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - run: pip install -r requirements.txt
    - run: pytest tests/
```

---

## Demonstrations

### Demo 1: Argparse in Action (5 min)
Start with hardcoded script:
```python
# analyze.py (before)
df = pd.read_csv('data.csv')
plt.hist(df['energy'], bins=50)
```

Transform to CLI tool:
```python
# analyze.py (after)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--bins', type=int, default=50)
args = parser.parse_args()

df = pd.read_csv(args.input)
plt.hist(df['energy'], bins=args.bins)
```

Show usage:
```bash
python analyze.py --help
python analyze.py --input data.csv
python analyze.py --input data.csv --bins 100
```

### Demo 2: Makefile Workflow (10 min)
Create analysis pipeline:
1. Preprocess data
2. Fit model
3. Generate plot

Write Makefile:
```makefile
all: results/final_plot.png

data/clean.csv: data/raw.csv scripts/preprocess.py
	python scripts/preprocess.py

results/fit.json: data/clean.csv scripts/fit.py
	python scripts/fit.py

results/final_plot.png: results/fit.json scripts/plot.py
	python scripts/plot.py

clean:
	rm -rf data/clean.csv results/*
```

Show:
- `make all` (runs everything)
- Modify one script
- `make all` again (only reruns affected steps!)
- `make clean && make all` (full rebuild)

---

## Time Estimates

- Motivation: 10 min
- Project structure: 15 min
- argparse: 20 min
- Config files: 15 min
- Virtual envs: 15 min
- Makefiles: 15 min
- GitHub Actions: 10 min
- Student exercises: 40 min
- **Total**: 140 min

---

## Resources for Students

- [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
- [YAML specification](https://yaml.org/)
- [GNU Make tutorial](https://makefiletutorial.com/)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [The Turing Way](https://the-turing-way.netlify.app/) - handbook on reproducible research
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) - project template

---

## Assessment Ideas

- **Project audit**: Students evaluate their own/peer's project structure
- **Reproducibility test**: Try to run classmate's analysis on your machine
- **Refactoring challenge**: Take messy code, make it reproducible
- **Final project requirement**: Must have proper structure, README, requirements.txt, and run with one command

---

## Extension Activities

For advanced students:
- Introduce Snakemake or Nextflow (workflow managers)
- Docker containerization (full environment isolation)
- Pre-commit hooks (automatic code formatting, linting)
- Documentation generation with Sphinx
- Code review practices on GitHub

---

## Key Messages to Emphasize

1. **Reproducibility is not optional** - it's fundamental to science
2. **Start small** - don't implement everything at once
3. **Future you is a collaborator** - write code for them
4. **Good structure saves time** - upfront cost, long-term benefit
5. **These are career skills** - industry values this highly
6. **Document everything** - README is not optional

---

## Homework / Project Integration

**Suggested assignment**:
"Take your L10 fitting code and L11 data processing code. Restructure into proper project with:
- Clear directory structure
- Command-line arguments
- Config file
- requirements.txt
- README with setup instructions
- Makefile
- Working on classmate's computer

Due: Next week. Will be evaluated on reproducibility!"
