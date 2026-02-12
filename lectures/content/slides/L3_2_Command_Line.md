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

## Command Line Interfaces

---
hideInToc: true
layout: quote
---

# The command line is the universal interface to computing. Master it once, and you gain **speed**, **automation**, and the ability to work on any machine—from a laptop to a supercomputer cluster.

---
hideInToc: true
---

# Command Line Interfaces (CLI)

<div class="grid-2 mt-md gap-md">

<div class="card card-info pad-tight">

## 💻 **What is the CLI?**

- **Text-based** communication with the computer
- **Efficient** for repeatable tasks and automation
  - Can easily chain commands, redirect input/output, and script workflows

</div>

<div class="card card-primary pad-tight">

## 🌍 **Where does it run?**

- Accessible across **Windows**, **macOS**, and **Linux**
- Forms the backbone of **data engineering** and **scientific computing**

</div>

</div>

---
hideInToc: true
---

# Why Learn the CLI?

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## ⚡ **Speed**

Execute complex workflows faster than with a mouse

</div>

<div class="card card-secondary pad-tight">

## 🔄 **Automation**

Script repetitive steps and share them openly

</div>

<div class="card card-accent pad-tight">

## 🌐 **Remote Work**

Manage servers and clusters without a GUI

</div>

<div class="card card-info pad-tight">

## 📝 **Transparency**

Commands document exactly what happened

</div>

<div class="card card-success pad-tight">

## 🔗 **Composability**

Small tools can be chained into powerful pipelines

</div>

</div>

---
hideInToc: true
---

# Shell Fundamentals

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🐚 **Shells**

```bash
PowerShell
bash / zsh
fish
```

- Provide the environment that interprets your commands
- Offer history, auto-completion, variables, and scripting features

</div>

<div class="card card-secondary pad-tight">

## 📍 **Prompt Structure**

```bash
user@machine:path $
PS C:\Users\You>
```

<div class="note-text mt-sm">The prompt tells you who you are, where you are, and that the shell is ready for input.</div>

</div>

</div>

---
hideInToc: true
---

# Basic Command Anatomy

<div class="card card-info pad-tight mt-md">

## 🔧 **Structure**

```
command -options arguments
```

- `command`: the program to run
- `options`: tweak behavior, usually start with `-` or `--`
- `arguments`: the objects being acted on

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🏗️ **Built-ins**

Shell provides built-in commands (`cd`, `Set-Location`)

</div>

<div class="card card-secondary pad-tight">

## 📦 **Executables**

External executables live in directories listed in `$PATH` / `$Env:Path`

</div>

</div>

---
hideInToc: true
---

# Navigating the Filesystem

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell**

```bash
Get-Location
Set-Location Documents
Get-ChildItem
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
pwd
cd Documents
ls
```

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## 🔑 **Key Concepts**

- Directories are **hierarchical**
- `..` means "go up one level"
- Tab completion reduces typing
- Use history (`↑`) to rerun previous commands

</div>

---
hideInToc: true
---

# Inspecting Files

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell**

```bash
Get-Content README.md
Select-String "analysis" *.txt
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
cat README.md
rg "analysis" *.txt
```

</div>

</div>

<div class="card card-info pad-tight mt-md">

## 🔍 **Practical Uses**

- Preview configuration or log files quickly
- Search large codebases without opening an editor
- Combine with redirection (`>`) to save filtered output

</div>

---
hideInToc: true
---

# Creating and Editing

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell**

```bash
New-Item notes.txt -ItemType File
Add-Content notes.txt "Result: 42"
notepad notes.txt
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
touch notes.txt
echo "Result: 42" >> notes.txt
nano notes.txt
```

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## 🔀 **Versioning & Collaboration**

- Pair the CLI with `git` to track work precisely
- Editors like `nano`, `vim`, or IDE CLIs let you modify files without leaving the terminal
- Script file creation to keep project structure consistent

</div>

---
hideInToc: true
---

# Working with Processes

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell**

```bash
Get-Process python
Stop-Process -Name python
Start-Job -ScriptBlock { python script.py }
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
ps aux | grep python
killall python
nohup python script.py &
```

</div>

</div>

<div class="card card-warning pad-tight mt-md">

## ⚙️ **Why It Matters**

- Monitor long-running analyses
- Run jobs in the background while continuing to work
- Integrate into schedulers or workflow engines

</div>

---
hideInToc: true
---

# Combining Commands

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell Pipeline**

```bash
Get-ChildItem *.csv |
  Where-Object { $_.Length -gt 1MB } |
  Sort-Object Length -Descending
```

**Save Results:**

```bash
... | Out-File large_files.txt
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **UNIX Pipeline**

```bash
ls -lh *.csv \
  | awk '$5+0 > 1 {print $9, $5}' \
  | sort -k2hr
```

**Save Results:**

```bash
... > large_files.txt
```

</div>

</div>

<div class="card card-info pad-tight mt-md">

<div class="note-text">

**Key insight:** Pipelines let each tool focus on one job. Reuse the same pattern across projects with minimal edits.

</div>

</div>

---
hideInToc: true
---

# Getting Help

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🪟 **PowerShell**

```bash
Get-Command *csv*
Get-Help Get-Content -Examples
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
apropos csv
man cat
```

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## 📚 **Learning Faster**

- Use `--help` or `/?` flags for quick summaries
- Explore interactive help (`Get-Help -Online`, `tldr command`)
- Build a personal cheatsheet for frequent tasks

</div>

---
hideInToc: true
---

# Best Practices

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 🧩 **Keep commands small and composable**

</div>

<div class="card card-secondary pad-tight">

## 📖 **Use aliases sparingly—prefer readable scripts**

</div>

<div class="card card-info pad-tight">

## 📁 **Store reusable commands in scripts under version control**

</div>

<div class="card card-success pad-tight">

## 📋 **Document workflows in README files with copy-paste commands**

</div>

<div class="card card-accent pad-tight">

## 💪 **Practice regularly to build muscle memory**

</div>

</div>

---
hideInToc: true
---

# Demo Challenge

<div class="stack-tight mt-md">

<div class="card card-primary pad-tight">

## 📁 **Create a new project folder from the CLI**

</div>

<div class="card card-secondary pad-tight">

## 📝 **Create a `README.md` with your plan**

</div>

<div class="card card-accent pad-tight">

## 🔗 **Share the exact commands you used**

</div>

</div>

---
layout: statement
hideInToc: true
---

# The CLI is your multiplier—start small, automate often, and watch productivity compound.
