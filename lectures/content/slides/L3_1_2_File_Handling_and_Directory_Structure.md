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

# Lessons on **Data Analysis** from **CERN**

## File Handling and Directory Structure

---
layout: section
hideInToc: true
---

# **Common pitfalls in working with computers**

---
layout: two-cols-header
hideInToc: true
---

# **File management chaos**

::left::

## **Common issues:**

- ### "I have no idea where I saved that file"
  
- ### "My file is gone!"

- ### "I have 10 files with the same name, which one is the right one?"

  - ### `final_final_v2.docx`,  `asdfasdf.docx`, `asdfasdf.docx`

- ### "I have overwritten my file with the wrong version"

::right::

## **How to avoid:**

- ### Create a consistent folder structure

- ### Use descriptive filenames and version numbers

- ### Employ file tagging, search filters, or integrated version control systems like Git to help keep track of changes

---
layout: two-cols
hideInToc: true
---

## **No backups**

- ### "I lost all my data"

- ### "I accidentally deleted my file"

- ### "My computer crashed and I lost everything"

- ### "I spilled tea on my laptop now my thesis is gone"

::right::

## **How to avoid:**

- ### Use automatic cloud backup services (Dropbox, Google Drive, OneDrive).

- ### Keep external backups on physical drives, ensuring they’re in a separate location.

- ### Consider version control for text-based files (Git), so you can revert to an older version if needed.

---
layout: two-cols
hideInToc: true
---

## **Compatibility issues**

- ### "I can't open this file"
  
- ### "This only works on my old laptop"

- ### "I have a mac so this probably won't work"
  
- ### "I opened this word file but it's all broken"

- ### "The script was running ok but now I get errors"

::right::

##  **How to avoid:** 

- ### Use open-source software and file formats whenever possible

- ### Use cloud-based tools that work across different platforms

- ### Use virtual machines or containers to ensure compatibility

- ### Use version control to track changes and revert to a working version

- ### Use software that is actively maintained and updated

- ### Use software that is widely used and has a large user base

- ### Agree on software and file formats with collaborators

---
hideInToc: true
layout: two-cols-header
class: "pt-20"  # modifies spacing on the overall layout
---

# **File Naming Conventions**

::left::

- ## **Think about your files beforehand**

  - ### Identify what group of files your naming convention will cover

  - ### You can use different conventions for different file sets

  - ### Check for established file naming conventions in your discipline or group

::right::

<img src="/file_naming_comic.png" class="inline w-40" />

---
hideInToc: true
layout: two-cols
---

- ## **Identify metadata**

  - ### Experiment conditions

  - ### Type of data

  - ### Researcher name/initials

  - ### Lab name/location

  - ### Project or experiment name or acronym

  - ### Date or date range of experiment

  - ### Experiment number or sample ID

::right::

- ## **Abbreviate and encode metadata in the file name**

  - ### Decide what shortened information to keep
  
  - ### Standardize the categories and/or replace them with 2- or 3-letter codes

  - ### Be sure to document these codes

---
hideInToc: true
---

- ## **Use Versioning**

  - ### Use versioning to indicate the most current version of a file
  
  - ### Track versions of a file by adding version information to end of the file name, e.g. filename_v2.xxx
  
  - ### Use a version number (e.g. “v01” or “v02”)
  
  - ### Use the version date (use ISO 8601 format: YYYYMMDD or YYYY-MM-DD)

---
hideInToc: true
---

- ## **Ensure Files are Searchable**
  
  - ### Think about how you want to sort and search for your files in order to determine the order for the metadata in the file name
  
  - ### Decide what metadata should appear at the beginning
  
  - ### Use default ordering: alphabetically, numerically, or chronologically
  
  - ### Use ISO 8601-formatted dates (YYYYMMDD or YYYY-MM-DD)

---
hideInToc: true
---

- ## **Separate Metadata Elements**
  
  - ### Use dashes (-), underscores (_), or capitalize the first letter of each word

    - #### Dashes: file-name.xxx

    - #### Underscores: file_name.xxx

    - #### No separation: filename.xxx

  - ### Camel case (the first letter of each section of text is capitalized): FileName.xxx

  - ### Avoid special characters, such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " |

---
hideInToc: true
---

- ## **Write down your naming conventions**
  
  - ### If the file is moved or shared, users will be able to identify the file from its file name

  - ### File names should be 40-50 characters and conventions should only use alphanumeric characters, dashes, underscores

  - ### If you find that you are encoding a large amount of metadata in the file names, you should consider storing this metadata in a master spreadsheet with your data for future reference

---
layout: two-cols-header
hideInToc: true
class: "pt-30"  # modifies spacing on the overall layout
---

# **Two different file types**

::left::

- ## **Text File**

  - ### Human readable

  - ### Can be opened with any text editor

  - ### Generally larger

  - ### Usually config files, logs, or scripts

::right::

- ## **Binary File**

  - ### Not human readable

  - ### Requires specific software to open

  - ### Generally smaller

  - ### Usually images, videos, or executables

---
layout: iframe
hideInToc: true
url: https://datacarpentry.github.io/rr-organization1/01-file-naming/index.html
---

---
hideInToc: true
layout: two-cols-header
---

# **Directory Structure**

::left::

## Organized by File type

<div style="max-width: 300px;">

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

::right::

## Organized by Analysis

<div style="max-width: 300px; margin-top: 0px">

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

---
layout: center
hideInToc: true
---

[<img src="/RDM_Lifecycle.png" class="inline w-140"/>](https://datamanagement.hms.harvard.edu/)

---