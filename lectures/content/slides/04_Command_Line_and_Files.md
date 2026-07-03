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

# Best Research and Data Analysis Practices from CERN

## Command Line & File Handling

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

---
layout: section
hideInToc: true
---

# Common Pitfalls in Working with **Computers**

---
hideInToc: true
---

# File Management Chaos

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight reveal-scale" v-click>

## 😵 **Common Issues**

- "I have no idea where I saved that file"

- "My file is gone!"

- "I have 10 files with the same name, which one is the right one?"

  - `final_final_v2.docx`, `asdfasdf.docx`, `final.docx`

- "I have overwritten my file with the wrong version"

</div>

<div class="card card-success card-glass pad-tight reveal-scale" v-click>

## ✅ **How to Avoid**

- Create a consistent folder structure

- Use descriptive filenames and version numbers

- Employ file tagging, search filters, or integrated version control systems like Git to help keep track of changes

</div>

</div>

---
hideInToc: true
---

# No Backups

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 💥 **Common Issues**

- "I lost all my data"

- "I accidentally deleted my file"

- "My computer crashed and I lost everything"

- "I spilled tea on my laptop — now my thesis is gone"

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **How to Avoid**

- Follow the **here-near-far** strategy (next slide)

- Consider version control for text-based files (Git), so you can revert to an older version if needed

</div>

</div>

---
hideInToc: true
---

# Backup Strategy: <span class="gradient-text">Here — Near — Far</span>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-scale" v-click>

## 💻 **Here**

Your **local device** — the working copy you use every day

- Laptop or desktop hard drive
- Fast access, but vulnerable to hardware failure, theft, or accidents

</div>

<div class="card card-secondary card-glass pad-tight reveal-scale" v-click>

## 🔌 **Near**

A **local backup** in the same physical space

- External hard drive, USB stick, or NAS
- Protects against device failure
- Still at risk from fire, flood, or theft

</div>

<div class="card card-accent card-glass pad-tight reveal-scale" v-click>

## ☁️ **Far**

A **remote backup** in a different location

- Cloud storage (Google Drive, OneDrive, Dropbox)
- University-hosted storage or remote server
- Protects against site-level disasters

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up" v-click>

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

- Pin versions with **virtual environments** or containers

- Track changes with **version control** (Git)

- Agree on software and formats with **collaborators** upfront

</div>

</div>

---
layout: section
hideInToc: true
---

# File **Naming**

---
hideInToc: true
---

# File Naming Conventions

<div class="note-text">

*The guidance in this section is adapted from [Harvard Medical School's Research Data Management](https://datamanagement.hms.harvard.edu/) best practices.*

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧠 **Think About Your Files Beforehand**

- Identify what group of files your naming convention will cover

- You can use different conventions for different file sets

- Check for established file naming conventions in your discipline or group

</div>

<div>

<img src="/figures/file_naming_comic.png" class="inline w-40" />

</div>

</div>

---
hideInToc: true
---

# File Naming: Metadata

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-tight">

## 🏷️ **Identify Metadata**

- Experiment conditions

- Type of data

- Researcher name/initials, lab name/location

- Project or experiment name or acronym

- Date or date range of experiment

- Experiment number or sample ID

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔤 **Abbreviate & Encode Metadata**

- Decide what shortened information to keep

- Standardize the categories and/or replace them with 2- or 3-letter codes

- Be sure to document these codes

</div>

</div>

---
hideInToc: true
---

# File Naming: Versioning

<div class="card card-primary card-glass pad-tight">

## 🔢 **Use Versioning**

- Use versioning to indicate the most current version of a file

- Track versions of a file by adding version information to the end of the file name, e.g. `filename_v2.xxx`

- Use a version number (e.g. "v01" or "v02")

- Use the version date (use ISO 8601 format: YYYYMMDD or YYYY-MM-DD)

</div>

---
hideInToc: true
---

# File Naming: Searchability

<div class="card card-accent card-glass pad-tight">

## 🔍 **Ensure Files are Searchable**

- Think about how you want to sort and search for your files in order to determine the order for the metadata in the file name

- Decide what metadata should appear at the beginning

- Use default ordering: alphabetically, numerically, or chronologically

- Put the date **first** when chronology matters — ISO 8601 dates sort correctly even in a plain alphabetical file listing

</div>

---
hideInToc: true
---

# File Naming: Separators

<div class="card card-info card-glass pad-tight">

## ✂️ **Separate Metadata Elements**

- Use dashes (-), underscores (_), or capitalize the first letter of each word

  - Dashes: `file-name.xxx`

  - Underscores: `file_name.xxx`

  - Camel case (the first letter of each section of text is capitalized): `FileName.xxx`

- 🚫 No separation: `filename.xxx` — avoid

- Avoid special characters, such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " |

</div>

---
hideInToc: true
---

# File Naming: Documentation

<div class="card card-secondary card-glass pad-tight">

## 📝 **Write Down Your Naming Conventions**

- With documented conventions, anyone receiving a moved or shared file can identify it from its name

- File names should be at most 40-50 characters, and conventions should only use alphanumeric characters, dashes, and underscores

- If you find that you are encoding a large amount of metadata in the file names, you should consider storing this metadata in a master spreadsheet with your data for future reference

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
|- 2026-03-14_run042.csv
|- 2026-03-14_run042_README.txt
|- samples_master.csv
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

💡 **Recipe:** `project_description_version_date.ext` — descriptive, sortable, no spaces or special characters.

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

```bash
|- Data/
|  |- Processed/
|  |- Raw/
|- Results/
|  |- Figure1.tif
|  |- Figure2.tif
|  |- Models/
|  |  |- Model1/
```

</div>

<div class="card card-secondary card-glass pad-tight">

## 📊 **Organised by Analysis**

```bash
|- Figure1/
|  |- Data/
|  |- Results/
|  |  |- Figure1.tif
|- Figure2/
|  |- Data/
|  |- Results/
|  |  |- Figure2.tif
```

</div>

</div>

<div class="note-text mt-sm">

Choose the structure that best fits your workflow — either is valid as long as it is consistent. Use the CLI commands from the Command Line lesson (`mkdir`, `ls`, `cd`) to create and navigate these structures.

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

<div class="card card-primary card-glass pad-tight reveal-scale" v-click>

## 📥 **`data/raw/`**

- Exactly as collected or downloaded
- Treat as **untouchable** — your only link back to reality
- If it changes, every result becomes unverifiable

</div>

<div class="card card-success card-glass pad-tight reveal-scale" v-click>

## ⚙️ **`data/processed/`**

- Everything derived from raw — **by a script**
- Safe to delete at any time: rerun the script and it comes back
- Corrections live in **code**, where they are visible and repeatable

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up" v-click>

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
|- README.md   <- you are here
|- data/raw/
|- data/processed/
|- scripts/
|- results/
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

# Try It: Build a Project Skeleton

<div class="card card-success card-glass pad-compact mt-md">

## 🧪 **CLI Exercise**

Create this structure from the command line — no file manager allowed!

```bash
mkdir -p my_project/data/raw \
         my_project/data/processed \
         my_project/results
touch my_project/README.md
ls -R my_project
```

</div>

<div class="card card-info card-glass pad-compact mt-sm">

💡 `-p` creates parent directories automatically. Try `tree my_project` if you have `tree` installed.

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
layout: center
hideInToc: true
---

# Archiving: Freeze What You Publish

<div class="card card-info card-glass pad-compact mt-sm">

📦 When a thesis chapter, paper, or report goes out, **freeze the exact state** of the data and code that produced it.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left" v-click>

🗜️ **Bundle** — one archive: data + scripts + README (`thesis_ch3_2026-07-03.zip`)

</div>

<div class="card card-secondary card-glass pad-compact reveal-left" v-click>

🔐 **Fingerprint** — store a checksum next to it, so corruption or tampering is detectable *(how checksums work: the Computer Science lecture)*

</div>

<div class="card card-accent card-glass pad-compact reveal-left" v-click>

🏛️ **Deposit** — university repository or a service like Zenodo, which gives your archive a permanent citable identifier (a **DOI**)

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up" v-click>

💡 "Which exact version of the data made Figure 3?" — with an archive, that question has an answer years later.

</div>

---
hideInToc: true
---

# Putting It All Together: The Research Data <span class="gradient-text">Lifecycle</span>

<div class="grid" style="grid-template-columns: 1fr 1fr; gap: 1rem; align-items: center;">

[<img src="/figures/RDM_Lifecycle.png" class="inline w-70"/>](https://datamanagement.hms.harvard.edu/)

<div>

<div class="card card-primary card-glass pad-compact reveal-left" v-click>

- **Plan** → naming conventions & directory structure
- **Collect & Process** → consistent names, separate raw from processed
- **Analyse** → version-controlled project folders
- **Preserve & Share** → open formats, README, metadata

</div>

<div class="card card-info card-glass pad-compact mt-sm reveal-left" v-click>

💡 Good file handling supports **every stage** of the research data lifecycle.

</div>

</div>

</div>

---
