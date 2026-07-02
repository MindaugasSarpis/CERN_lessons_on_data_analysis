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
hideInToc: true
---

# Wildcards — Many Files at Once

<div class="card card-info card-glass pad-compact mt-sm glow">

## ✳️ **Patterns instead of names**

The shell expands a **pattern** into every matching filename *before* the command runs — the command just sees a list of files.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🃏 **The patterns**

- `*` — any number of characters: `*.csv`
- `?` — exactly one character: `run_?.log`
- `[ab]` — one character from a set: `fig[12].png`

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **In action**

```bash
ls *.csv            # all CSV files here
cp data_2026_*.csv backup/
rm run_?.log        # run_1.log, run_A.log …
```

Works the same in PowerShell for file arguments.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Wildcards + `rm` is the classic foot-gun: run `ls <pattern>` first to **see** what will match.

</div>

---
hideInToc: true
---

# Finding Files

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🪟 **PowerShell**

```powershell
Get-ChildItem -Recurse -Filter *.csv
Get-ChildItem -Recurse |
  Where-Object Length -gt 100MB
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🐧 **macOS & Linux**

```bash
find . -name "*.csv"
find . -size +100M
find . -mtime -7     # changed last 7 days
```

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 🔍 **`grep` finds text, `find` finds files**

- "Which file mentions `calibration`?" → `grep -r "calibration" .`
- "Where did that huge download go?" → `find ~ -size +1G`
- Both search **recursively** — the whole directory tree below you

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

# A Pipeline, Step by Step

<div class="card card-info card-glass pad-compact mt-sm">

🧪 **Question:** which detector reports the most errors? `log.txt` has one line per event: `sensor_A OK`, `sensor_B ERROR`, …

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left" v-click>

1️⃣ `grep "ERROR" log.txt` — keep only the error lines

</div>

<div class="card card-secondary card-glass pad-compact reveal-left" v-click>

2️⃣ `… | sort` — identical sensor names become neighbours

</div>

<div class="card card-accent card-glass pad-compact reveal-left" v-click>

3️⃣ `… | uniq -c` — collapse repeats into `count name`

</div>

<div class="card card-success card-glass pad-compact reveal-left" v-click>

4️⃣ `… | sort -nr | head -3` — numerically, biggest first, top three

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up" v-click>

```bash
grep "ERROR" log.txt | sort | uniq -c | sort -nr | head -3
```

💡 Four small tools, one question answered — **no programming required.**

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

<div class="note-text">

*Optional power-user detour — skim it on first contact and return when you have a long-running analysis to babysit.*

</div>

<div class="grid-2 mt-sm gap-md">

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

# Did It Work? Exit Codes & Chaining

<div class="card card-info card-glass pad-compact mt-sm">

🚦 Every command finishes with an invisible **exit code**: `0` = success, anything else = failure. The shell lets you build logic on top of it.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔗 **Chaining operators**

```bash
cmd1 && cmd2   # cmd2 only if cmd1 succeeded
cmd1 || cmd2   # cmd2 only if cmd1 FAILED
cmd1 ;  cmd2   # cmd2 regardless
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **In practice**

```bash
mkdir results && cd results
python analyse.py || echo "analysis failed!"
echo $?          # print last exit code
```

`$LASTEXITCODE` in PowerShell.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 `&&` is your safety belt: "only continue **if that worked**" — you'll see it in install instructions everywhere.

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

- `rm -rf` on the wrong directory — deleted **permanently**, no trash can *(modern `rm` refuses `/` itself, but `rm -rf ~` has no such guard)*
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

<MCQ
  question="A folder contains: run_1.log, run_12.log, run_A.log, notes.txt. What does `rm run_?.log` delete?"
  :options="[
    'All four files',
    'run_1.log, run_12.log and run_A.log',
    'run_1.log and run_A.log',
    'Nothing — ? is not a valid wildcard'
  ]"
  :correct="2"
  explanation="? matches exactly one character, so run_1.log and run_A.log match but run_12.log (two characters) and notes.txt do not. This is why you run `ls run_?.log` first — see the match list before deleting it."
/>

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
