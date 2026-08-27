---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Command Line Interfaces"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Command Line & File Handling

##### <span class="aims-badge">⚙️ automation · 📁 data & files · 🔧 tool-agnostic</span>

<!--
Speaker: this is the workhorse lecture — the CLI and file handling. Two aims meet
here: automation and efficient work with data. By the end they can drive a
machine with no GUI and keep a project tidy. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The command line is the universal interface to computing. Master it once, and you gain **speed**, **automation**, and the ability to work on any machine—from a laptop to a supercomputer cluster.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧭 **Navigate** and inspect files entirely from the command line

</div>

<div class="card card-secondary card-glass pad-compact">

🔗 Chain small tools with **pipes** and **redirection** to answer questions

</div>

<div class="card card-accent card-glass pad-compact">

✳️ Match many files at once with **wildcards** — safely

</div>

<div class="card card-success card-glass pad-compact">

🏷️ Name files with consistent, sortable **conventions**

</div>

<div class="card card-info card-glass pad-compact">

⚙️ Turn repeated commands into a **shell script** — variables and a `for` loop

</div>

<div class="card card-warning card-glass pad-compact">

📁 Organise a project — raw vs **processed** data, plus a README

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. The paired Seminar 4 is where
they organise the seminar project folder and inspect the dataset from the shell —
today builds the toolkit and the habits. (~1 min)
-->

---
hideInToc: true
---

# The Command Line: What and **Why**

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight reveal-scale">

## 💻 **What is the CLI?**

- **Text-based** communication with the computer
- Chain commands, redirect input/output, script whole workflows
- Runs on **Windows**, **macOS**, and **Linux** — the backbone of scientific computing

</div>

<div class="card card-primary card-glass pad-tight reveal-scale">

## 🎯 **Why learn it?**

- ⚡ **Speed** — complex workflows faster than with a mouse
- 🔄 **Automation** — script repetitive steps and share them
- 🌐 **Remote work** — servers and clusters have no GUI
- 📝 **Transparency** — commands document exactly what happened

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

💡 Every tool in this lecture exists on every machine you will ever be given an account on — a laptop, a lab PC, or a computing-cluster node.

</div>

---
layout: section
hideInToc: true
---

# CLI **Foundations**

<!--
Speaker: ground them before commands — a shell interprets text, the prompt shows
where you are, and every command is verb-options-arguments. Everything that
follows is a variation on this pattern. (~1 min)
-->

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

<!--
Speaker: the verbs they'll use hourly — navigate, inspect, match, find. Show the
PowerShell/UNIX pairing so no one feels shut out by their OS; the concepts are
identical across shells. (~1 min)
-->

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
- Combine with redirection (`>`, coming up in Power Tools) to save filtered output

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
echo "Result: 42" >> notes.txt   # >> appends — see Power Tools
```

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🧭 **Beyond the Basics**

- Editors like `nano`, `vim`, or IDE CLIs let you modify files without leaving the terminal
- Script file creation to keep project structure consistent
- **File naming conventions** and directory structure are coming up later **in this lecture**; pairing the CLI with `git` (version control), **Markdown**, and **VS Code** each get their own lecture soon after

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

<!--
Speaker: the payoff — pipes compose small tools into real answers. Linger on the
error-count pipeline; watching four tiny commands answer a real question is what
converts sceptics. (~2 min)
-->

---
hideInToc: true
---

# Pipes and Redirection

<div class="card card-primary card-glass pad-tight mt-md glow">

## 🔗 **The Pipe Operator `|`**

The pipe sends the **output** of one command as **input** to another, letting you chain tools together.

```bash
grep "error" data.csv | wc -l     # how many lines mention "error"?
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

<div class="card card-primary card-glass pad-compact reveal-left">

1️⃣ `grep "ERROR" log.txt` — keep only the error lines

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

2️⃣ `… | sort` — identical sensor names become neighbours

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

3️⃣ `… | uniq -c` — collapse repeats into `count name`

</div>

<div class="card card-success card-glass pad-compact reveal-left">

4️⃣ `… | sort -nr | head -3` — numerically, biggest first, top three

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

```bash
grep "ERROR" log.txt | sort | uniq -c | sort -nr | head -3
```

💡 Four small tools, one question answered — **no programming required.**

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
find . -name "*.csv" -size +1M -exec du -h {} + \
  | sort -rh > large_files.txt
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 Pipelines let each tool focus on one job. Reuse the same pattern across projects with minimal edits.

*These examples show the power of pipelines — don't worry if the syntax looks unfamiliar; you'll pick up these tools as the course goes on.*

</div>

<!--
Speaker: if someone asks "why not just ls -l | awk?" — ls -l columns are not a
stable format to parse; filenames with spaces or locale settings silently break
naive awk/cut scripts. find … -exec du asks the filesystem directly. (~1 min)
-->

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
python analyse.py       # run it
echo $?                 # its exit code: 0 = ok, else failed
python analyse.py || echo "failed!"   # || = fallback on failure
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
layout: section
hideInToc: true
---

# The Shell as a **Data Tool**

<!--
Speaker: the pitch of this section is one sentence — long before Python, the
shell already answers real questions about a dataset. Same small tools as
before, now pointed at a CSV of detector events. This is the bridge to the
seminar dataset. (~1 min)
-->

---
hideInToc: true
---

# Meet the Dataset: `events.csv`

<div class="card card-info card-glass pad-compact mt-sm">

🔬 One line per recorded event from a detector — a **CSV**: comma-separated columns, first line names them.

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 👀 **First peek**

```bash
head -4 events.csv
```

```text
time,detector,energy,status
09:00:01,ECAL,148.9,OK
09:00:02,MUON,3.1,ERROR
09:00:02,VELO,12.4,OK
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Plain text is the shell's home turf — every tool from the last section works on this file **unchanged**.

</div>

---
hideInToc: true
---

# How Big Is It? `wc`, `head`, `tail`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📏 **Count with `wc`**

```bash
wc -l events.csv   # lines = events + header
wc -l *.csv        # every CSV at once
```

- `-l` lines, `-w` words, `-c` bytes

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔭 **Peek with `head` / `tail`**

```bash
head -20 events.csv   # first 20 lines
tail -5 events.csv    # last 5 lines
tail -f run.log       # follow a growing log
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 None of these load the whole file — inspecting a 10 GB file is instant, where a spreadsheet program would freeze.

</div>

---
hideInToc: true
---

# Columns with `cut`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✂️ **Pick columns**

```bash
cut -d, -f2 events.csv     # detector column
cut -d, -f2,4 events.csv   # detector + status
```

- `-d,` — the delimiter between columns
- `-f` — which field number(s) to keep

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **Which detectors exist?**

```bash
cut -d, -f2 events.csv | sort | uniq
```

```text
ECAL
HCAL
MUON
VELO
detector
```

<div class="note-text mt-sm">⚠️ The header line is just data to the shell — skip it with <code>tail -n +2 events.csv | cut …</code></div>

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `uniq` only collapses **adjacent** duplicates — that is why `sort` always comes before it.

</div>

---
hideInToc: true
---

# `sort` Does Numbers Too — If You Ask

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **Lexical by default**

```bash
sort energies.txt
```

```text
104.2
11.8
9.3
```

Character by character, `104…` sorts before `11…` — wrong for numbers.

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **Numeric, by column**

```bash
sort -n energies.txt         # numeric
sort -t, -k3 -n events.csv   # by CSV column 3
```

- `-t,` delimiter · `-k3` sort key · `-n` numeric · `-r` reverse

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 `sort -t, -k3 -nr events.csv | head -5` is already data analysis: **the five highest-energy events**, one line.

</div>

---
hideInToc: true
---

# Worked Pipeline (1/2): Build It Up

<div class="card card-info card-glass pad-compact mt-sm">

🧪 **Question:** how many events did each detector record? Same pattern as the ERROR pipeline — the new ingredient is `cut`.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

1️⃣ `cut -d, -f2 events.csv` — keep only the detector column

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

2️⃣ `… | sort` — identical detectors become neighbours

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

3️⃣ `… | uniq -c` — collapse each run into `count detector`

</div>

<div class="card card-success card-glass pad-compact reveal-left">

4️⃣ `… | sort -nr` — biggest counts first

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md reveal-up">

```text
    512 ECAL
    356 VELO
    214 HCAL
     88 MUON
```

💡 Run the pipeline **after every stage** — watch the data change shape.

</div>

---
hideInToc: true
---

# Worked Pipeline (2/2): Keep the Answer

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💾 **Save the result**

```bash
cut -d, -f2 events.csv | sort \
  | uniq -c | sort -nr > detector_counts.txt
```

- `>` captures the answer into a file
- rerunnable — the command *is* the documentation

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔀 **Vary the question**

```bash
grep ",ERROR" events.csv | cut -d, -f2 \
  | sort | uniq -c | sort -nr
```

- swap the first stage, keep the rest: now it counts **error** events per detector

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md glow">

🏆 **The shell is your first data-analysis tool** — you filtered, grouped, and ranked a dataset with zero programming.

</div>

<!--
Speaker: pause here. Filtering, grouping, ranking — that is groupby before they
have ever heard the word. When pandas arrives in a later lecture, point back to
this slide. (~2 min)
-->

---
hideInToc: true
---

<MCQ
  question="runs.txt contains six lines: alpha, beta, alpha, gamma, alpha, beta. What does `sort runs.txt | uniq -c | sort -nr | head -1` print?"
  :options="[
    '3 alpha',
    'alpha 3',
    '1 gamma',
    '6 runs.txt'
  ]"
  :correct="0"
  explanation="sort groups the identical lines together, uniq -c rewrites each group as count-then-value (count first!), sort -nr puts the largest count on top, and head -1 keeps only that line. alpha appears three times, so the output is `3 alpha`."
/>

---
layout: section
hideInToc: true
---

# Searching the Data **Tree**

<!--
Speaker: they met find and grep as single commands. This section upgrades both
into questions you ask a whole directory tree — the daily bread of anyone
managing run data. (~1 min)
-->

---
hideInToc: true
---

# `grep` Beyond the First Match

<div class="card card-info card-glass pad-compact mt-sm">

You know `grep pattern file`. Four flags turn it from *show me matches* into *answer my question*.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🚩 **The flags**

```bash
grep -i "error" run.log   # ignore case
grep -n "ERROR" run.log   # show line numbers
grep -c "ERROR" run.log   # just COUNT matches
grep -l "ERROR" *.log     # just LIST matching files
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **In practice**

```bash
grep -c "ERROR" *.log
```

```text
run_041.log:0
run_042.log:17
run_043.log:2
```

An error count **per file** — one command.

</div>

</div>

---
hideInToc: true
---

# Context: What Happened Around the Match?

<div class="card card-info card-glass pad-compact mt-sm">

🔎 An error line rarely explains itself — the cause is usually a few lines **earlier** in the log.

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 🩺 **`-B` before, `-A` after, `-C` both**

```bash
grep -B2 -A1 "ERROR" run_042.log
```

```text
09:14:55 sensor_3 temp 71C
09:14:56 sensor_3 temp 84C
09:14:57 sensor_3 ERROR overheat
09:14:58 sensor_3 shutdown
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Two lines of context turn *there was an error* into *sensor 3 overheated over two seconds* — diagnosis without opening an editor.

</div>

---
hideInToc: true
---

# `find` Acts, Not Just Lists: `-exec`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⚙️ **The pattern**

```bash
find data/ -name "*.log" -exec wc -l {} +
```

- `{}` — placeholder for the found files
- `+` — pass many files per call

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **Select, then act**

```bash
# line counts for CSVs changed this week
find data/ -name "*.csv" -mtime -7 \
  -exec wc -l {} +
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 The selection tests stack — `-name`, `-size`, `-mtime` combine into a **query language for your filesystem**, and `-exec` is its verb.

</div>

---
hideInToc: true
---

# Case Study: Audit a Season of Runs

<div class="card card-info card-glass pad-compact mt-sm">

📦 `data/raw/` holds hundreds of run logs. Your supervisor asks: **which of last week's runs had errors — and how many is that?**

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

1️⃣ `find data/raw -name "run_*.log" -mtime -7` — last week's runs

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

2️⃣ `… -exec grep -l "ERROR" {} +` — keep only those containing errors

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

3️⃣ `… | wc -l` — count the survivors

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

```bash
find data/raw -name "run_*.log" -mtime -7 -exec grep -l "ERROR" {} + | wc -l
```

💡 A tree-wide audit in one line — 📁 this is what *efficient work with files* means.

</div>

---
layout: section
hideInToc: true
---

# Your First Shell **Script**

<!--
Speaker: the automation payoff, and the rule of the whole course in miniature.
If you typed it twice, script it. Ten minutes here saves them hours every month
for the rest of their careers. (~1 min)
-->

---
hideInToc: true
---

# If You Typed It Twice, Script It

<div class="card card-accent card-glass pad-compact mt-sm glow">

⚙️ A **script** is just your commands saved in a file — typed once, run forever. This is the automation aim in its smallest form.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📝 **Anatomy**

```bash
#!/usr/bin/env bash
# count_events.sh — events per detector
cut -d, -f2 events.csv | sort | uniq -c
```

- line 1 is the **shebang** — which interpreter runs this file

</div>

<div class="card card-secondary card-glass pad-tight">

## ▶️ **Make it runnable**

```bash
chmod +x count_events.sh   # once: mark executable
./count_events.sh          # run it
```

- `./` means *the one right here*, not something on `$PATH`

</div>

</div>

---
hideInToc: true
---

# Script Building Block 1: Variables

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🏷️ **Define and use**

```bash
DATA_DIR="data/raw"
PATTERN="ERROR"
grep -c "$PATTERN" "$DATA_DIR"/run_042.log
```

- no spaces around `=`
- `$NAME` inserts the value

</div>

<div class="card card-warning card-glass pad-tight">

## 🛡️ **Quote your variables**

```bash
rm "$OLD_FILE"   # safe with spaces
rm $OLD_FILE     # "my data.csv" becomes TWO arguments!
```

Unquoted variables split on spaces — the classic script bug.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 Variables gather everything you might change — paths, patterns, thresholds — at the **top** of the script, in one visible place.

</div>

---
hideInToc: true
---

# Script Building Block 2: The `for` Loop

<div class="card card-info card-glass pad-compact mt-sm">

🔁 Wildcards give you the file list; `for` runs the same body **once per file**.

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 🔂 **The shape**

```bash
for f in data/raw/run_*.log; do
  echo "== $f"
  grep -c "ERROR" "$f"
done
```

- `$f` holds the current filename on each pass

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Ten files or ten thousand — the loop doesn't care. This is the moment the CLI stops being *typing fast* and becomes **automation**.

</div>

---
hideInToc: true
---

# Putting It Together: `error_report.sh`

<div class="card card-primary card-glass pad-tight mt-sm">

## 📜 **The whole script**

```bash
#!/usr/bin/env bash
# error_report.sh — ERROR count per run log
DATA_DIR="data/raw"
mkdir -p results

for f in "$DATA_DIR"/run_*.log; do
  n=$(grep -c "ERROR" "$f")
  echo "$f,$n"
done > results/error_report.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🆕 **One new trick**

`$( … )` — **command substitution**: run the command, keep its output in a variable

</div>

<div class="card card-success card-glass pad-compact">

## ♻️ **Why it matters**

Delete the report, rerun the script, get it back — ready for version control later in the course

</div>

</div>

---
hideInToc: true
---

# Teaser: `xargs` — the Loop You Don't Write

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🚀 **One-liner power**

```bash
find data/raw -name "*.csv" | xargs wc -l
# names with spaces: find -print0 | xargs -0
```

`xargs` reads names from the pipe and hands them to the command as **arguments** — a for-loop compressed into a word.

</div>

<div class="card card-secondary card-glass pad-tight">

## 🗺️ **Where this road leads**

- today — a script and a loop
- soon — your scripts under **version control**
- later in the course — whole **pipelines** rerun with one command

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

⚙️ You don't need `xargs` yet — recognise it in the wild, and remember the shell can always go one step further.

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

<div class="card card-primary card-glass pad-compact reveal-left">

🧩 Keep commands small and composable

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

📖 Use aliases sparingly — prefer readable scripts

</div>

<div class="card card-info card-glass pad-compact reveal-left">

📁 Store reusable commands in scripts under version control

</div>

<div class="card card-success card-glass pad-compact reveal-left">

📋 Document workflows in README files with copy-paste commands

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

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

# Part 1 in One **Slide**

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-up">

🧭 **Navigate** — `pwd` / `cd` / `ls` ↔ `Get-Location` / `Set-Location` / `Get-ChildItem`

</div>

<div class="card card-secondary card-glass pad-compact reveal-up">

🔍 **Inspect** — `cat` / `grep` ↔ `Get-Content` / `Select-String` · match many files with `*.csv`, `run_?.log`

</div>

<div class="card card-accent card-glass pad-compact reveal-up">

📝 **Create** — `mkdir` / `touch` / `echo` ↔ `New-Item` / `Add-Content`

</div>

<div class="card card-info card-glass pad-compact reveal-up">

🔗 **Combine** — pipe with `|`, overwrite with `>`, append with `>>`, continue only on success with `&&`

</div>

<div class="card card-success card-glass pad-compact reveal-up">

📊 **Analyse** — `cut` / `sort` / `uniq -c` / `wc` — filter, group, and rank a CSV with zero programming

</div>

<div class="card card-warning card-glass pad-compact reveal-up">

⚙️ **Automate** — `find -exec`, `for f in …; do … done`, `#!/usr/bin/env bash` — if you typed it twice, script it

</div>

</div>

<!--
Speaker: one beat per row — this is the whole first half. If a row does not ring
a bell, that is the section to revisit before the seminar. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Part 2 — From Commands to **Files**

<!--
Speaker: now that they can drive the CLI, the second half is about what the CLI
drives — files and folders that stay organised, backed up, and readable by
someone else. Start with the pain: everyone has lived the chaos slide. (~1 min)
-->

---
hideInToc: true
---

# Two Ways to Lose Your **Work**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight reveal-scale">

## 😵 **File chaos**

- "I have no idea where I saved that file"
- "Which one is the right one?" — `final_final_v2.docx`, `asdfasdf.docx`, `final.docx`
- "I overwrote my file with the wrong version"

</div>

<div class="card card-warning card-glass pad-tight reveal-scale">

## 💥 **No backups**

- "I accidentally deleted my file"
- "My computer crashed and I lost everything"
- "I spilled tea on my laptop — now my thesis is gone"

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md reveal-up">

## ✅ **How to avoid both**

- A consistent **folder structure** and descriptive, versioned **filenames** *(this lecture)*
- **Version control** (Git) for text files — revert to any older version *(later in the course)*
- Copies at three distances — **here, near, far** *(next slide)*

</div>

---
hideInToc: true
---

# Backup Strategy: <span class="gradient-text">Here — Near — Far</span>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-scale">

## 💻 **Here**

Your **local device** — the working copy you use every day

- Laptop or desktop hard drive
- Fast access, but vulnerable to hardware failure, theft, or accidents

</div>

<div class="card card-secondary card-glass pad-tight reveal-scale">

## 🔌 **Near**

A **local backup** in the same physical space

- External hard drive, USB stick, or NAS
- Protects against device failure
- Still at risk from fire, flood, or theft

</div>

<div class="card card-accent card-glass pad-tight reveal-scale">

## ☁️ **Far**

A **remote backup** in a different location

- Cloud storage (Google Drive, OneDrive, Dropbox)
- University-hosted storage or remote server
- Protects against site-level disasters

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up">

💡 A solid backup plan keeps copies at **all three distances**. If any one fails, the others still have you covered.

</div>

---
hideInToc: true
---

# Compatibility Issues

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 🔌 **Common Issues**

- "I can't open this file"

- "This only works on my old laptop"

- "I have a Mac, so this probably won't work"

- "I opened this Word file but it's all broken"

- "The script was running ok but now I get errors"

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **How to Avoid**

- Prefer **open-source** software and file formats

- Choose **cross-platform** tools (cloud-based or multi-OS)

- Later in the course you'll **pin versions** so it works everywhere

- Track changes with **version control** (Git)

- Agree on software and formats with **collaborators** upfront

</div>

</div>

---
layout: section
hideInToc: true
---

# File **Naming**

<!--
Speaker: pivot from commands to discipline. A good filename is sortable and
self-describing; bad ones cost hours later. Tie this back to the file-chaos
slide they just laughed at. (~1 min)
-->

---
hideInToc: true
---

# File Naming: Plan the **Metadata**

<div class="note-text">Comic: <a href="https://xkcd.com/1459/">xkcd 1459</a> · guidance in this section adapted from <a href="https://datamanagement.hms.harvard.edu/">Harvard Medical School's Research Data Management</a>.</div>

<div class="flex gap-md mt-sm items-start">

<div class="flex-1">

<div class="grid-2 gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧠 **Think Ahead**

- Which group of files does this convention cover?
- Different file sets may use different conventions
- Check for established conventions in your discipline or group

</div>

<div class="card card-info card-glass pad-compact">

## 🏷️ **Identify the Metadata**

- Experiment conditions, type of data
- Researcher initials, lab or location
- Project or experiment acronym
- Date or date range
- Run number or sample ID

</div>

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🔤 **Abbreviate & Encode**

- Keep only what you sort or search by; encode categories as short codes (`raw`, `cal`)
- **Document the codes** — a code nobody can decode is noise

</div>

</div>

<img src="/figures/file_naming_comic.png" class="w-40 shrink-0" />

</div>

---
hideInToc: true
---

# File Naming: Versioning & **Ordering**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔢 **Use Versioning**

- Mark the current version at the **end** of the name: `report_v02.docx`
- Zero-pad numbers (`v01` … `v10`) so they sort correctly
- Or use the version date in ISO 8601: `YYYY-MM-DD`

</div>

<div class="card card-accent card-glass pad-tight">

## 🔍 **Make Files Sortable & Searchable**

- Decide how you will sort and search — that metadata goes **first** in the name
- Default ordering is alphabetical, numerical, or chronological
- Put the date **first** when chronology matters — ISO dates sort correctly in a plain listing

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

## 🧪 **`ls` already shows them in order**

```text
2026-03-14_run042_calib_v01.csv
2026-03-14_run042_calib_v02.csv
2026-03-15_run043_calib_v01.csv
```

</div>

---
hideInToc: true
---

# File Naming: Separators & **Documentation**

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

## ✂️ **Separate the Elements**

- Dashes `file-name.xxx`, underscores `file_name.xxx`, or CamelCase `FileName.xxx`
- 🚫 No separation: `filename.xxx` — avoid
- No spaces, and no special characters: `~ ! @ # $ % ^ & * ( ) ; : < > ? , [ ] { } ' " |`

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **Write the Convention Down**

- Documented conventions let anyone identify a moved or shared file from its name alone
- At most 40–50 characters; only alphanumerics, dashes, and underscores
- Encoding a lot of metadata? Move it to a master spreadsheet next to the data — **next slide**

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A space in a filename is a bug waiting to happen: `rm my data.csv` deletes `my` and `data.csv`, not `my data.csv`.

</div>

---
hideInToc: true
---

# When Names Aren't Enough: Sidecar Metadata

<div class="card card-info card-glass pad-compact mt-sm">

🏷️ A filename holds three or four facts at most. The rest — instrument settings, units, operator, conditions — belongs in a **metadata file that travels with the data**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📑 **The sidecar pattern**

```text
data/
├── 2026-03-14_run042.csv
├── 2026-03-14_run042_README.txt
└── samples_master.csv
```

One description file per dataset — or one master table describing every file.

</div>

<div class="card card-secondary card-glass pad-tight">

## ✍️ **What goes in it**

- **Units** for every column *(the classic silent killer)*
- Instrument + settings used
- Date, operator, location
- Known issues ("sensor 3 drifted after 14:00")

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Rule of thumb: if a fact is needed to **interpret** the numbers, it must be stored **next to** the numbers — not in your memory or an old email.

</div>

---
hideInToc: true
---

# File Naming Cheatsheet

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ❌ **Bad**

```
final_FINAL_v2 (1).docx
data.csv
Copy of analysis.py
Figure 1 (final).png
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Good**

```
thesis_draft_v03_2026-02-20.docx
experiment_alpha_raw_001.csv
analysis_v02.py
fig01_mass_spectrum.png
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md glow">

💡 **Recipe:** `project_description_version.ext` — descriptive, no spaces or special characters — and put an ISO date **first** (`2026-02-20_thesis_draft_v03.docx`) when files must sort by time.

</div>

---
layout: section
hideInToc: true
---

# Directory **Structure**

---
hideInToc: true
---

# Organising Your Directories

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📁 **Organised by File Type**

```text
├── Data/
│   ├── Processed/
│   └── Raw/
└── Results/
    ├── Figure1.tif
    ├── Figure2.tif
    └── Models/
        └── Model1/
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **Organised by Analysis**

```text
├── Figure1/
│   ├── Data/
│   └── Results/
│       └── Figure1.tif
└── Figure2/
    ├── Data/
    └── Results/
        └── Figure2.tif
```

</div>

</div>

<div class="note-text mt-sm">

Choose the structure that best fits your workflow — either is valid as long as it is consistent. Build either one with the commands from Part 1 (`mkdir`, `ls`, `cd`) to create and navigate these structures.

</div>

---
hideInToc: true
---

# Raw Data Is <span class="gradient-text">Read-Only</span>

<div class="card card-warning card-glass pad-tight mt-md glow">

## 🔒 **The one rule that saves projects**

**Never edit a raw data file.** Not to fix a typo, not to delete an obvious outlier, not "just this once."

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-scale">

## 📥 **`data/raw/`**

- Exactly as collected or downloaded
- Treat as **untouchable** — your only link back to reality
- If it changes, every result becomes unverifiable

</div>

<div class="card card-success card-glass pad-tight reveal-scale">

## ⚙️ **`data/processed/`**

- Everything derived from raw — **by a script**
- Safe to delete at any time: rerun the script and it comes back
- Corrections live in **code**, where they are visible and repeatable

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up">

💡 Test yourself: could you delete everything *except* `data/raw/` and the scripts, and rebuild the project? If yes, your structure is right.

</div>

---
hideInToc: true
---

# The README: Your Project's Front Page

<div class="card card-info card-glass pad-compact mt-sm">

📄 A `README` is a plain-text file at the project root that tells a stranger — including **you, six months from now** — what this project is and how to use it.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📋 **A minimal README records**

- What the project is (one paragraph)
- Where the data **came from** (provenance, dates, units)
- How to **regenerate** the results, step by step
- Who to contact

</div>

<div class="card card-secondary card-glass pad-tight">

## 🧪 **Example skeleton**

```text
my_project/
├── README.md   <- you are here
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
└── results/
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Writing READMEs gets much nicer with **Markdown** — covered in its own lecture shortly.

</div>

---
hideInToc: true
---

# Absolute vs Relative Paths

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📍 **Absolute Path**

Starts from the **root** of the filesystem — always points to the same location regardless of your current directory.

```bash
# Linux (macOS: /Users/alice/...)
/home/alice/projects/data/results.csv

# Windows
C:\Users\Alice\projects\data\results.csv
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 📎 **Relative Path**

Starts from your **current directory** — shorter, but meaning changes as you move around.

```bash
# If you are in /home/alice/projects
cd data
cat results.csv

# Go up one level, then into another folder
cd ../notes
ls
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 In scripts, prefer paths **relative to the project root** — the project then works on any machine and for any collaborator. Absolute paths belong only in machine-specific configuration (and never in shared code).

</div>

---
hideInToc: true
---

# Try at Home: Build a Project **Skeleton**

<div class="card card-info card-glass pad-compact mt-md">

## 🏠 **Ten minutes, no file manager allowed**

Create this structure from the command line, then write your plan for a project of your choice into the README:

```bash
mkdir -p my_project/data/raw \
         my_project/data/processed \
         my_project/results
touch my_project/README.md
ls -R my_project
```

</div>

<div class="card card-success card-glass pad-compact mt-sm">

💡 `-p` creates parent directories automatically. Try `tree my_project` if you have `tree` installed.

💡 **Bonus:** drop a few `sensor_A OK` / `sensor_B ERROR` lines into `my_project/data/raw/run042.log`, then reuse the earlier pipeline: `grep ERROR my_project/data/raw/run042.log | sort | uniq -c | sort -nr`

🔗 **Keep the exact commands you used** — paste them into the README as its first "how to rebuild this" section.

</div>

---
hideInToc: true
---

<MCQ
  question="Why do shared projects usually prefer relative paths (data/raw/run42.csv) over absolute paths (/Users/alice/proj/data/raw/run42.csv)?"
  :options="[
    'Relative paths are faster for the OS to resolve',
    'Absolute paths are not supported on Linux',
    'Relative paths make the project portable — it still works when someone clones it elsewhere',
    'Relative paths automatically encrypt the file location'
  ]"
  :correct="2"
  explanation="Absolute paths tie a project to one machine and user; relative-to-project-root paths keep it self-contained and portable — a ♻️ reproducibility win."
/>

---
hideInToc: true
---

# Exercise: Fix This Mess (1/2)

<div class="card card-warning card-glass pad-tight mt-md">

## 😵 **The Problem**

A colleague shared their project with you. Here's what you received:

```
Desktop/
├── final_FINAL_v2.docx
├── data (1).csv
├── Copy of data.csv
├── analysis.py
├── analysis_old.py
├── analysis_NEW_USE_THIS.py
├── plot.png
├── plot2.png
├── Figure 1 (final).png
└── notes.txt
```

</div>

<div class="card card-info card-glass pad-compact mt-md" v-click>

💡 **Spot the issues:** spaces in filenames, duplicate data files, no versioning, no folder structure, unclear which script is current, vague figure names.

</div>

---
hideInToc: true
---

# Exercise: Fix This Mess (2/2)

<div class="card card-success card-glass pad-tight mt-md">

## ✅ **Your Task** (10 min, with a partner)

1. Design a proper **directory structure** using `mkdir -p`
2. **Rename** every file following the conventions we just covered
3. Draft a **README.md** describing the project and its contents
4. Decide which files belong in **version control** and which don't

</div>

<div class="card card-primary card-glass pad-tight mt-md">

## 💡 **Hints**

- Separate `data/`, `scripts/`, `results/`, and `docs/` folders
- Use ISO dates or version numbers: `analysis_v01.py`, `analysis_v02.py`
- Raw data files should never be modified — keep originals in `data/raw/`
- Figures need descriptive names: what does "plot2" actually show?

</div>

---
hideInToc: true
---

# Archiving: Freeze What You Publish

<div class="card card-info card-glass pad-compact mt-sm">

📦 When a thesis chapter, paper, or report goes out, **freeze the exact state** of the data and code that produced it.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🗜️ **Bundle** — one archive: data + scripts + README (`thesis_ch3_2026-07-03.zip`)

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

🔐 **Fingerprint** — store a checksum next to it, so corruption or tampering is detectable *(you met checksums and SHA-256 in Lecture 3)*

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🏛️ **Deposit** — university repository or a service like Zenodo, which gives your archive a permanent citable identifier (a **DOI**)

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

💡 "Which exact version of the data made Figure 3?" — with an archive, that question has an answer years later.

</div>

---
hideInToc: true
---

# Putting It All Together: The Research Data <span class="gradient-text">Lifecycle</span>

<div class="grid" style="grid-template-columns: 1fr 1fr; gap: 1rem; align-items: center;">

[<img src="/figures/RDM_Lifecycle.png" class="inline w-70"/>](https://datamanagement.hms.harvard.edu/)

<div>

<div class="card card-primary card-glass pad-compact reveal-left">

- **Plan** → naming conventions & directory structure
- **Collect & Process** → consistent names, separate raw from processed
- **Analyse** → version-controlled project folders
- **Preserve & Share** → open formats, README, metadata

</div>

<div class="card card-info card-glass pad-compact mt-sm reveal-left">

💡 Good file handling supports **every stage** of the research data lifecycle.

</div>

</div>

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ **Navigate** and inspect files from the command line

</div>

<div class="card card-success card-glass pad-compact">

✅ Chain tools with **pipes** and **redirection**

</div>

<div class="card card-success card-glass pad-compact">

✅ Name files with sortable, consistent **conventions**

</div>

<div class="card card-success card-glass pad-compact">

✅ Structure a project — raw vs **processed**, plus a README

</div>

<div class="card card-success card-glass pad-compact">

✅ Match many files safely with **wildcards** — and turn a pipeline into a rerunnable **script**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 4 tie-in**

Organise the seminar dataset into raw/ vs processed/ folders with clean filenames, and inspect it entirely from the command line.

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each card. The seminar
tie-in makes the payoff concrete: they leave here and immediately give the seminar
folder a clean structure and drive it from the shell — then their own project. (~1 min)
-->

---
layout: quote
hideInToc: true
---

# The CLI is your multiplier—start small, automate often, and watch productivity compound.
