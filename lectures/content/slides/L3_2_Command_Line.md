---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Command Line Interfaces"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 3:

## Command Line Interfaces

---
hideInToc: true
---

# Command Line Interfaces (CLI)

- ## **Text-based** communication with the computer

- ## **Efficient** for repeatable tasks and automation

  - ### Can easily chain commands, redirect input/output, and script workflows

- ## Accessible across **Windows**, **macOS**, and **Linux**

- ## Forms the backbone of **data engineering** and **scientific computing**

---
hideInToc: true
---

# Why Learn the CLI?

- ## **Speed:** execute complex workflows faster than with a mouse

- ## **Automation:** script repetitive steps and share them openly

- ## **Remote work:** manage servers and clusters without a GUI

- ## **Transparency:** commands document exactly what happened

- ## **Composability:** small tools can be chained into powerful pipelines

---
hideInToc: true
---

# Shell Fundamentals

## Shells

```bash
PowerShell
bash / zsh
fish
```

- Provide the environment that interprets your commands
- Offer history, auto-completion, variables, and scripting features

## Prompt Structure

```bash
user@machine:path $
PS C:\Users\You>
```
---
hideInToc: true
---

# Basic Command Anatomy

```
command -options arguments
```

- `command`: the program to run
- `options`: tweak behavior, usually start with `-` or `--`
- `arguments`: the objects being acted on

## Built-ins vs Executables

- Shell provides built-in commands (`cd`, `Set-Location`)
- External executables live in directories listed in `$PATH` / `$Env:Path`

---
hideInToc: true
layout: two-cols
---

## Navigating the Filesystem

<div style="max-width: 320px;">

### PowerShell
```bash
Get-Location
Set-Location Documents
Get-ChildItem
```

</div>

<div style="max-width: 320px;">

### macOS & Linux
```bash
pwd
cd Documents
ls
```

</div>

::right::

## Key Concepts

- Directories are **hierarchical**
- `..` means "go up one level"
- Tab completion reduces typing
- Use history (`↑`) to rerun previous commands

---
hideInToc: true
layout: two-cols
---

## Inspecting Files

<div style="max-width: 320px;">

### PowerShell
```bash
Get-Content README.md
Select-String "analysis" *.txt
```

</div>

<div style="max-width: 320px;">

### macOS & Linux
```bash
cat README.md
rg "analysis" *.txt
```

</div>

::right::

## Practical Uses

- Preview configuration or log files quickly
- Search large codebases without opening an editor
- Combine with redirection (`>`) to save filtered output

---
hideInToc: true
layout: two-cols
---

## Creating and Editing

<div style="max-width: 320px;">

### PowerShell
```bash
New-Item notes.txt -ItemType File
Add-Content notes.txt "Result: 42"
notepad notes.txt
```

</div>

<div style="max-width: 320px;">

### macOS & Linux
```bash
touch notes.txt
echo "Result: 42" >> notes.txt
nano notes.txt
```

</div>

::right::

## Versioning & Collaboration

- Pair the CLI with `git` to track work precisely
- Editors like `nano`, `vim`, or IDE CLIs let you modify files without leaving the terminal
- Script file creation to keep project structure consistent

---
hideInToc: true
layout: two-cols
---

## Working with Processes

<div style="max-width: 320px;">

### PowerShell
```bash
Get-Process python
Stop-Process -Name python
Start-Job -ScriptBlock { python script.py }
```

</div>

<div style="max-width: 320px;">

### macOS & Linux
```bash
ps aux | grep python
killall python
nohup python script.py &
```

</div>

::right::

## Why It Matters

- Monitor long-running analyses
- Run jobs in the background while continuing to work
- Integrate into schedulers or workflow engines

---
hideInToc: true
layout: two-cols-header
---

# Combining Commands

## PowerShell Pipeline

```bash
Get-ChildItem *.csv |
  Where-Object { $_.Length -gt 1MB } |
  Sort-Object Length -Descending
```

## Save Results

```bash
... | Out-File large_files.txt
```

## UNIX Pipeline

```bash
ls -lh *.csv \
  | awk '$5+0 > 1 {print $9, $5}' \
  | sort -k2hr
```

## Save Results

```bash
... > large_files.txt
```

- Pipelines let each tool focus on one job
- Reuse the same pattern across projects with minimal edits

---
hideInToc: true
layout: two-cols
---

## Getting Help

<div style="max-width: 320px;">

### PowerShell
```bash
Get-Command *csv*
Get-Help Get-Content -Examples
```

</div>

<div style="max-width: 320px;">

### macOS & Linux
```bash
apropos csv
man cat
```

</div>

::right::

## Learning Faster

- Use `--help` or `/?` flags for quick summaries
- Explore interactive help (`Get-Help -Online`, `tldr command`)
- Build a personal cheatsheet for frequent tasks

---
hideInToc: true
---

# Best Practices

- ## Keep commands **small** and **composable**

- ## Use **aliases** sparingly—prefer readable scripts

- ## Store reusable commands in **scripts** under version control

- ## Document workflows in README files with **copy-paste** commands

- ## Practice regularly to build muscle memory

---
hideInToc: true
---

# Demo Challenge

- ## Create a new project folder **from the CLI**

- ## Create a `README.md` with your plan

- ## Share the exact commands you used

---
layout: statement
hideInToc: true
---

# The CLI is your multiplier—start small, automate often, and watch productivity compound.
