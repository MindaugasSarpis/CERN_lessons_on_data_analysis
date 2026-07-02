---
background: /figures/background_intro.jpg

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

# Data Analysis and Artificial Intelligence

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

<div class="card card-info card-glass pad-tight">

## 💻 **What is the CLI?**

- **Text-based** communication with the computer
- **Efficient** for repeatable tasks and automation
  - Can easily chain commands, redirect input/output, and script workflows

</div>

<div class="card card-primary card-glass pad-tight">

## 🌍 **Where does it run?**

- Accessible across **Windows**, **macOS**, and **Linux**
- Forms the backbone of **data engineering** and **scientific computing**

</div>

</div>

---
hideInToc: true
---

# Why Learn the <span class="gradient-text">CLI</span>?

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale" v-click>

⚡ **Speed** — complex workflows faster than with a mouse

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale" v-click>

🔄 **Automation** — script repetitive steps and share them

</div>

<div class="card card-accent card-glass pad-compact reveal-scale" v-click>

🌐 **Remote Work** — manage servers and clusters without a GUI

</div>

<div class="card card-info card-glass pad-compact reveal-scale" v-click>

📝 **Transparency** — commands document exactly what happened

</div>

</div>

---
layout: section
hideInToc: true
---

# CLI **Foundations**

---
hideInToc: true
---

# Shell Fundamentals

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🐚 **Shells**

```text
PowerShell
bash / zsh
fish
```

- Provide the environment that interprets your commands
- Offer history, auto-completion, variables, and scripting features

</div>

<div class="card card-secondary card-glass pad-tight">

## 📍 **Prompt Structure**

```sh
user@machine:path $
```

```powershell
PS C:\Users\You>
```

<div class="note-text mt-sm">The prompt tells you who you are, where you are, and that the shell is ready for input.</div>

</div>

</div>

---
hideInToc: true
---

# Basic Command Anatomy

<div class="card card-info card-glass pad-tight mt-md">

## 🔧 **Structure**

```
command -options arguments
```

- `command`: the program to run
- `options`: tweak behavior, usually start with `-` or `--`
- `arguments`: the objects being acted on

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🏗️ **Built-ins**

The shell provides built-in commands (`cd`, `Set-Location`)

</div>

<div class="card card-secondary card-glass pad-tight">

## 📦 **Executables**

External executables live in directories listed in `$PATH` / `$Env:Path`

</div>

</div>

---
layout: section
hideInToc: true
---

# Everyday **Commands**

---
hideInToc: true
---

# Navigating the Filesystem

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
Get-Location
Set-Location Documents
Get-ChildItem
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
pwd
cd Documents
ls
```

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

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

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
Get-Content README.md
Select-String "analysis" *.txt
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
cat README.md
grep "analysis" *.txt
```

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 🔍 **Practical Uses**

- Preview configuration or log files quickly
- Search large codebases without opening an editor
- Combine with redirection (`>`, next slide) to save filtered output

</div>

---
layout: section
hideInToc: true
---

# Power **Tools**

---
hideInToc: true
---

# Pipes and Redirection

<div class="card card-primary card-glass pad-tight mt-md glow">

## 🔗 **The Pipe Operator `|`**

The pipe sends the **output** of one command as **input** to another, letting you chain tools together.

```bash
cat data.csv | grep "error"       # filter lines containing "error"
ls -l | sort -k5 -n               # list files sorted by size
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-tight">

## 📤 **Overwrite with `>`**

Writes command output to a file, **replacing** any existing content.

```bash
echo "Hello" > notes.txt
```

</div>

<div class="card card-accent card-glass pad-tight">

## 📎 **Append with `>>`**

Adds command output to the **end** of a file without erasing it.

```bash
echo "Another line" >> notes.txt
```

</div>

</div>

---
hideInToc: true
---

# Creating and Editing

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
New-Item project -ItemType Directory
New-Item notes.txt -ItemType File
Add-Content notes.txt "Result: 42"
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
mkdir project
touch notes.txt
echo "Result: 42" >> notes.txt
```

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🧭 **Beyond the Basics**

- Editors like `nano`, `vim`, or IDE CLIs let you modify files without leaving the terminal
- Script file creation to keep project structure consistent
- Coming up later in the course: pairing the CLI with `git` (version control, covered in its own lecture), **file naming conventions**, **Markdown** for documentation, and **VS Code** as your IDE

</div>

---
hideInToc: true
---

# Working with Processes

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
Get-Process firefox
Stop-Process -Name firefox
Start-Job -ScriptBlock { ./long_task.ps1 }
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
ps aux | grep firefox
killall firefox
nohup ./long_task.sh &
```

</div>

</div>

<div class="card card-warning card-glass pad-tight mt-md">

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

<div class="card card-primary card-glass pad-compact">

## 🪟 **PowerShell Pipeline**

```powershell
Get-ChildItem *.csv |
  Where-Object { $_.Length -gt 1MB } |
  Sort-Object Length -Descending |
  Out-File large_files.txt
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐧 **UNIX Pipeline**

```bash
# $5 = size in bytes, $9 = filename; 1 MB = 1048576 bytes
ls -l *.csv | awk '$5 > 1048576 {print $9, $5}' \
  | sort -k2,2nr > large_files.txt
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 Pipelines let each tool focus on one job. Reuse the same pattern across projects with minimal edits.

*These examples show the power of pipelines — don't worry if the syntax looks unfamiliar; you'll pick up these tools as the course goes on.*

</div>

---
hideInToc: true
---

# Getting Help

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
Get-Command *csv*
Get-Help Get-Content -Examples
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
apropos csv
man cat
```

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 📚 **Learning Faster**

- Use `--help`, `--version`, or `/?` flags for quick summaries
- Explore interactive help (`Get-Help -Online`, `tldr command`)
- Build a personal cheatsheet for frequent tasks

</div>

---
layout: section
hideInToc: true
---

# Working **Safely**

---
hideInToc: true
---

# Common CLI Mistakes

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **Dangerous**

- `rm -rf /` — deletes your entire system
- Running commands in the **wrong directory**
- Overwriting files with `>` instead of appending with `>>`
- Copy-pasting commands from the internet without reading them

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **Safe Habits**

- Always `pwd` before destructive operations
- Use `ls` to verify targets before `rm`
- Try `--dry-run` flags when available
- Read `man` pages for unfamiliar commands

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 **Rule of thumb:** if a command can't be undone, double-check before pressing Enter.

</div>

---
hideInToc: true
---

# Best Practices

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left" v-click>

🧩 Keep commands small and composable

</div>

<div class="card card-secondary card-glass pad-compact reveal-left" v-click>

📖 Use aliases sparingly — prefer readable scripts

</div>

<div class="card card-info card-glass pad-compact reveal-left" v-click>

📁 Store reusable commands in scripts under version control

</div>

<div class="card card-success card-glass pad-compact reveal-left" v-click>

📋 Document workflows in README files with copy-paste commands

</div>

<div class="card card-accent card-glass pad-compact reveal-left" v-click>

💪 Practice regularly to build muscle memory

</div>

</div>

---
hideInToc: true
---

# Key <span class="gradient-text">Takeaways</span>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-up" v-click>

🧭 **Navigate** — `pwd` / `cd` / `ls` ↔ `Get-Location` / `Set-Location` / `Get-ChildItem`

</div>

<div class="card card-secondary card-glass pad-compact reveal-up" v-click>

🔍 **Inspect** — `cat` / `grep` ↔ `Get-Content` / `Select-String`

</div>

<div class="card card-accent card-glass pad-compact reveal-up" v-click>

📝 **Create** — `mkdir` / `touch` / `echo` ↔ `New-Item` / `Add-Content`

</div>

<div class="card card-info card-glass pad-compact reveal-up" v-click>

🔗 **Combine** — pipe with `|`, overwrite with `>`, append with `>>` — the same symbols work in both shells

</div>

</div>

---
hideInToc: true
---

# Demo Challenge

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-tight">

## 📁 **Create a new project folder from the CLI**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **Create a `README.md` with your plan**

</div>

<div class="card card-accent card-glass pad-tight">

## 🔗 **Share the exact commands you used**

</div>

</div>

---
layout: quote
hideInToc: true
---

# The CLI is your multiplier—start small, automate often, and watch productivity compound.

---
disabled: true
---
