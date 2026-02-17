---
background: /background_intro.jpg

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

# Data analysis and Artificial Intelligence

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

<img src="/file_naming_comic.png" class="inline w-40" />

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
layout: iframe
hideInToc: true
url: https://datacarpentry.github.io/rr-organization1/01-file-naming/index.html
---

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

Choose the structure that best fits your workflow — either is valid as long as it is consistent. We'll navigate these structures from the command line in the next lecture.

</div>

---
layout: center
hideInToc: true
---

<div class="card card-info pad-compact">

## 🔄 **Research Data Management Lifecycle**

The RDM lifecycle shows how data flows through planning, collection, processing, analysis, preservation, and sharing — good file handling supports every stage.

</div>

[<img src="/RDM_Lifecycle.png" class="inline w-120"/>](https://datamanagement.hms.harvard.edu/)

---
