---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "File Handling and Directory Structure"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## File Handling and Directory Structure

---
hideInToc: true
layout: quote
---

# Good file management is the invisible foundation of every successful analysis. Name your files well, organise your directories, and your future self will thank you.

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

<div class="card card-warning card-glass pad-tight">

## 😵 **Common Issues**

- "I have no idea where I saved that file"

- "My file is gone!"

- "I have 10 files with the same name, which one is the right one?"

  - `final_final_v2.docx`,  `asdfasdf.docx`, `final.docx`

- "I have overwritten my file with the wrong version"

</div>

<div class="card card-success card-glass pad-tight">

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

- "I spilled tea on my laptop now my thesis is gone"

</div>

<div class="card card-success card-glass pad-tight">

## ✅ **How to Avoid**

- Follow the **here-near-far** strategy (covered below)

- Consider version control for text-based files (Git), so you can revert to an older version if needed

</div>

</div>

---
hideInToc: true
---

# Backup Strategy: Here — Near — Far

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💻 **Here**

Your **local device** — the working copy you use every day

- Laptop or desktop hard drive
- Fast access, but vulnerable to hardware failure, theft, or accidents

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔌 **Near**

A **local backup** in the same physical space

- External hard drive, USB stick, or NAS
- Protects against device failure
- Still at risk from fire, flood, or theft

</div>

<div class="card card-accent card-glass pad-tight">

## ☁️ **Far**

A **remote backup** in a different location

- Cloud storage (Google Drive, OneDrive, Dropbox)
- University-hosted storage or remote server
- Protects against site-level disasters

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

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

- "I have a mac so this probably won't work"

- "I opened this word file but it's all broken"

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

<div class="grid-2 mt-md gap-md">

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

- Track versions of a file by adding version information to end of the file name, e.g. filename_v2.xxx

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

- Use ISO 8601-formatted dates (YYYYMMDD or YYYY-MM-DD)

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

  - No separation: `filename.xxx`

- Camel case (the first letter of each section of text is capitalized): `FileName.xxx`

- Avoid special characters, such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " |

</div>

---
hideInToc: true
---

# File Naming: Documentation

<div class="card card-secondary card-glass pad-tight">

## 📝 **Write Down Your Naming Conventions**

- If the file is moved or shared, users will be able to identify the file from its file name

- File names should be 40-50 characters and conventions should only use alphanumeric characters, dashes, underscores

- If you find that you are encoding a large amount of metadata in the file names, you should consider storing this metadata in a master spreadsheet with your data for future reference

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

<div class="card card-info card-glass pad-compact mt-md">

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

<div class="card card-secondary card-glass pad-tight">

## 📊 **Organized by Analysis**

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

# Absolute vs Relative Paths

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📍 **Absolute Path**

Starts from the **root** of the filesystem — always points to the same location regardless of your current directory.

```bash
# macOS / Linux
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

💡 Use `pwd` to check where you are, then decide: **absolute** for scripts and configs, **relative** for interactive navigation.

</div>

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

<div class="card card-info card-glass pad-compact mt-md">

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

<div class="grid" style="grid-template-columns: 1fr 1fr; gap: 1rem; align-items: center;">

[<img src="/figures/RDM_Lifecycle.png" class="inline w-80"/>](https://datamanagement.hms.harvard.edu/)

<div>

<div class="card card-primary card-glass pad-compact">

- **Plan** → naming conventions & directory structure
- **Collect & Process** → consistent names, separate raw from processed
- **Analyse** → version-controlled project folders
- **Preserve & Share** → open formats, README, metadata

</div>

<div class="card card-info card-glass pad-compact mt-sm">

💡 Good file handling supports **every stage** of the research data lifecycle.

</div>

</div>

</div>

---