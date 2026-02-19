---
background: /figures/background_intro.jpg
class: text-left
colorSchema: dark
theme: ./theme
drawings:
  persist: false
transition: fade
title: "Working with Your Computer"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Working with Your Computer

---
hideInToc: true
layout: quote
---

# Master your files, your terminal, and your documentation — these three skills underpin **everything** else in data analysis.

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

<div class="card card-warning pad-tight">

## 😵 **Common Issues**

- "I have no idea where I saved that file"

- "My file is gone!"

- "I have 10 files with the same name, which one is the right one?"

  - `final_final_v2.docx`,  `asdfasdf.docx`, `asdfasdf.docx`

- "I have overwritten my file with the wrong version"

</div>

<div class="card card-success pad-tight">

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

<div class="card card-warning pad-tight">

## 💥 **Common Issues**

- "I lost all my data"

- "I accidentally deleted my file"

- "My computer crashed and I lost everything"

- "I spilled tea on my laptop now my thesis is gone"

</div>

<div class="card card-success pad-tight">

## ✅ **How to Avoid**

- Use automatic cloud backup services (Dropbox, Google Drive, OneDrive)

- Keep external backups on physical drives, ensuring they're in a separate location

- Consider version control for text-based files (Git), so you can revert to an older version if needed

</div>

</div>

---
hideInToc: true
---

# Compatibility Issues

<div class="grid-2 mt-md gap-md">

<div class="card card-warning pad-tight">

## 🔌 **Common Issues**

- "I can't open this file"

- "This only works on my old laptop"

- "I have a mac so this probably won't work"

- "I opened this word file but it's all broken"

- "The script was running ok but now I get errors"

</div>

<div class="card card-success pad-tight">

## ✅ **How to Avoid**

- Use open-source software and file formats whenever possible

- Use cloud-based tools that work across different platforms

- Use virtual machines or containers to ensure compatibility

- Use version control to track changes and revert to a working version

- Use actively maintained software with a large user base

- Agree on software and file formats with collaborators

</div>

</div>

---
layout: section
hideInToc: true
---

# File **Naming** and Organisation

---
hideInToc: true
---

# File Naming Conventions

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

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

<div class="card card-info pad-tight">

## 🏷️ **Identify Metadata**

- Experiment conditions

- Type of data

- Researcher name/initials, lab name/location

- Project or experiment name or acronym

- Date or date range of experiment

- Experiment number or sample ID

</div>

<div class="card card-secondary pad-tight">

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

<div class="card card-primary pad-tight">

## 🔢 **Use Versioning**

- Use versioning to indicate the most current version of a file

- Track versions of a file by adding version information to end of the file name, e.g. filename_v2.xxx

- Use a version number (e.g. "v01" or "v02")

- Use the version date (use ISO 8601 format: YYYYMMDD or YYYY-MM-DD)

</div>

---
hideInToc: true
---

# File Naming: Searchability

<div class="card card-accent pad-tight">

## 🔍 **Ensure Files are Searchable**

- Think about how you want to sort and search for your files in order to determine the order for the metadata in the file name

- Decide what metadata should appear at the beginning

- Use default ordering: alphabetically, numerically, or chronologically

- Use ISO 8601-formatted dates (YYYYMMDD or YYYY-MM-DD)

</div>

---
hideInToc: true
---

# File Naming: Separators

<div class="card card-info pad-tight">

## ✂️ **Separate Metadata Elements**

- Use dashes (-), underscores (_), or capitalize the first letter of each word

  - Dashes: `file-name.xxx`

  - Underscores: `file_name.xxx`

  - No separation: `filename.xxx`

- Camel case (the first letter of each section of text is capitalized): `FileName.xxx`

- Avoid special characters, such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " |

</div>

---
hideInToc: true
---

# File Naming: Documentation

<div class="card card-secondary pad-tight">

## 📝 **Write Down Your Naming Conventions**

- If the file is moved or shared, users will be able to identify the file from its file name

- File names should be 40-50 characters and conventions should only use alphanumeric characters, dashes, underscores

- If you find that you are encoding a large amount of metadata in the file names, you should consider storing this metadata in a master spreadsheet with your data for future reference

</div>

---
hideInToc: true
---

# Two Different File Types

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📄 **Text File**

- Human readable

- Can be opened with any text editor

- Generally larger

- Usually config files, logs, or scripts

</div>

<div class="card card-secondary pad-tight">

## 💾 **Binary File**

- Not human readable

- Requires specific software to open

- Generally smaller

- Usually images, videos, or executables

</div>

</div>

---
hideInToc: true
---

# Directory Structure

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📁 **Organized by File Type**

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

<div class="card card-secondary pad-tight">

## 📊 **Organized by Analysis**

```bash
|- Figure1/
|  |- Data/
|  |- Results
|  |  |- Figure1.tif
|- Figure2/
|  |- Data/
|  |- Results/
|  |  |- Figure2.tif
```

</div>

</div>

<div class="note-text mt-sm">

Choose the structure that best fits your workflow — either is valid as long as it is consistent. We'll navigate these structures from the command line in the next section.

</div>

---
layout: section
hideInToc: true
---

# The Command **Line**

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

<div class="card card-primary pad-compact">

## ⚡ **Speed**

Execute complex workflows faster than with a mouse

</div>

<div class="card card-secondary pad-compact">

## 🔄 **Automation**

Script repetitive steps and share them openly

</div>

<div class="card card-accent pad-compact">

## 🌐 **Remote Work**

Manage servers and clusters without a GUI

</div>

<div class="card card-info pad-compact">

## 📝 **Transparency & Composability**

Commands document exactly what happened — and small tools can be chained into powerful pipelines

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
grep "analysis" *.txt
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
New-Item project -ItemType Directory
New-Item notes.txt -ItemType File
Add-Content notes.txt "Result: 42"
```

</div>

<div class="card card-secondary pad-tight">

## 🐧 **macOS & Linux**

```bash
mkdir project
touch notes.txt
echo "Result: 42" >> notes.txt
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

# Pipes and Redirection

<div class="card card-primary pad-tight mt-md">

## 🔗 **The Pipe Operator `|`**

The pipe sends the **output** of one command as **input** to another, letting you chain tools together.

```bash
cat data.csv | grep "error"       # filter lines containing "error"
ls -l | sort -k5 -n               # list files sorted by size
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary pad-tight">

## 📤 **Overwrite with `>`**

Writes command output to a file, **replacing** any existing content.

```bash
echo "Hello" > notes.txt
```

</div>

<div class="card card-accent pad-tight">

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
layout: section
hideInToc: true
---

# Writing with **Markdown**

---
hideInToc: true
---

# Markdown

<div class="card card-info pad-tight">

## 📝 **What is Markdown?**

- **Lightweight markup language** with plain text formatting syntax
- **Converts** plain text to **HTML**
- **Easy to read** and **write**
- **Simple** and **intuitive**

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🎯 **Purpose**

📄 Documentation • 📓 Notebooks • 🖥️ Presentations • 🌐 Websites • 📊 Scientific reports

</div>

<div class="card card-secondary pad-tight">

## 🔧 **Used In**

GitHub READMEs • Jupyter Notebooks • Slidev • Jekyll • Hugo • Obsidian • Notion

<div class="note-text mt-sm">Remember creating <code>README.md</code> from the CLI in our earlier lectures? That was Markdown!</div>

</div>

</div>

---
hideInToc: true
---

# Markdown Syntax: Headers & Emphasis

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Syntax**

```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

*Italic* or _Italic_
**Bold** or __Bold__
~~Strikethrough~~
```

<div class="note-text mt-sm">Use `#` for header levels. Combine emphasis: `***bold italic***`</div>

</div>

<div class="card card-secondary pad-compact">

## 👁️ **Rendered Output**

<p style="font-size: 1.6em; font-weight: bold; margin: 0.15em 0;"><code>#</code> Header 1 — largest</p>
<p style="font-size: 1.35em; font-weight: bold; margin: 0.15em 0;"><code>##</code> Header 2</p>
<p style="font-size: 1.15em; font-weight: bold; margin: 0.15em 0;"><code>###</code> Header 3</p>
<p style="font-size: 1.0em; font-weight: bold; margin: 0.15em 0;"><code>####</code> Header 4</p>
<p style="font-size: 0.9em; font-weight: bold; margin: 0.15em 0;"><code>#####</code> Header 5</p>
<p style="font-size: 0.8em; font-weight: bold; margin: 0.15em 0;"><code>######</code> Header 6 — smallest</p>

<div class="mt-sm">

## *Italic*

## **Bold**

## ~~Strikethrough~~

</div>

</div>

</div>

---
hideInToc: true
---

# Lists: Ordered, Unordered & Task Lists

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Syntax**

```
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

1. First
2. Second
3. Third

- [x] Task 1 (completed)
- [ ] Task 2 (pending)
- [ ] Task 3 (pending)
```

<div class="note-text mt-sm">Use `-`, `*`, or `+` for unordered lists. `[x]` marks tasks done. Indent with 2 or 4 spaces for nesting.</div>

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

<div class="mt-sm">

1. First
2. Second
3. Third

</div>

<div class="mt-sm">

- [x]  Task 1 (completed)
- [ ]  Task 2 (pending)
- [ ]  Task 3 (pending)

</div>

<div class="note-text mt-sm">Task lists are widely used in **GitHub Issues** and **Pull Requests** to track progress.</div>

</div>

</div>

---
hideInToc: true
---

# Links & Images

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔗 **Links**

```
[OpenAI](https://openai.com)
```

<div class="mt-sm">

## [OpenAI](https://openai.com)

</div>

</div>

<div class="card card-secondary pad-tight">

## 🖼️ **Images**

```
![Markdown Logo](https://upload.wikimedia.org/
wikipedia/commons/4/48/Markdown-mark.svg)
```

<div class="mt-sm">

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

</div>

</div>

</div>

---
hideInToc: true
---

# Code Blocks

<div class="card card-info pad-tight">

## 💻 **Inline Code**

```
Use `inline code` within a sentence.
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📦 **Code Block**

- Use triple backticks to create "```" a code block

```
  function hello() {
  console.log("Hello, world!");
  }
```

</div>

<div class="card card-accent pad-tight">

## 🎨 **Syntax Highlighting**

- Add the language name after the first set of backticks
- For example, `python`

```python
def hello():
    print("Hello, world!")
```

</div>

</div>

---
layout: section
hideInToc: true
---

# Putting It All **Together**

---
hideInToc: true
---

# Hands-On: Build a Project from Scratch

<div class="card card-info pad-tight mt-md">

## 🎯 **Challenge**

Using only the CLI, create a properly organized project with good naming and Markdown documentation.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

**1.** Create a project folder: `mkdir 2025_data_analysis_project`

</div>

<div class="card card-secondary pad-compact">

**2.** Create subfolders: `data/raw`, `data/processed`, `results`, `scripts`

</div>

<div class="card card-accent pad-compact">

**3.** Create a `README.md` with: a level-1 header, a description paragraph, and a list of folder contents

</div>

<div class="card card-success pad-compact">

**4.** Create `scripts/analysis_v01.py` with a comment: `# First analysis script`

</div>

<div class="card card-warning pad-compact">

**5.** Use `ls -R` (or `Get-ChildItem -Recurse`) to verify your structure

</div>

</div>

---
hideInToc: true
---

# Exercise: Fix This Mess

<div class="card card-warning pad-tight mt-md">

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

<div class="card card-success pad-tight mt-md">

## ✅ **Your Task**

With a partner, propose:

1. A proper **directory structure**
2. **Renamed files** following naming conventions
3. A **README.md** describing the project
4. Which files should go in **version control**

</div>

---
layout: statement
hideInToc: true
---

# The CLI is your multiplier—start small, automate often, and watch productivity compound.
