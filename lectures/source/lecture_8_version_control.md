---
marp: true
paginate: true

background: ./resources/global/background.jpg
# apply unocss classes to the current slide
class: text-left

drawings:
  persist: false

transition: fade
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture **8**

### **Version** Control using Git

---
layout: image-right
image: ./resources/git/comic_version.jfif
backgroundSize: contain
---

# The Importance of Version Control

- ### Even if working alone, many different version of the same file will exist. 
- ### Some overwritten changes might be needed later.
- ### A "versioned" file might be needed when implementing comments from supervisor / reviewers. 
- ### This hold true for written work, code and other files. 
  
---

# Tracking Changes (differences)  

- ## Rather than saving multiple copies of the same file, we can track changes.
- ## git is an open-source version control system that is used to track changes in files.

![](./resources/git/play-changes.svg)

---
layout: image-right
image: ./resources/git/versions.svg
backgroundSize: contain
---

# Different Versions 

- An eddit to a file might overwrite some of the content in the previous version.
- This *divergences* may arrise while working alone, but they are really common when multiple people are working on the same file.

---
layout: image-right
image: ./resources/git/merge.svg
backgroundSize: contain
---

# Merging 

- ### `git` has great functionality for merging different versions of the same file.
- ### If the previous content is not overwritten, or deleted, merge just combines the changes into one file.

---
layout: two-cols
---

# When using `git` for the first time 

- ### You need to configure your user name and email address.

```bash
git config --global user.name "Mindaugas Sarpis"
git config --global user.email "mindaugas.sarpis@cern.ch"
```

- ### You can check the configuration with

```bash
git config --list
```

- ### You can open the help with
   
```bash
git config --h
git config --help
```

::right:: 

```bash {*}{maxHeight:'450px', maxWidth:'50px'}
usage: git config [<options>]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    --worktree            use per-worktree config file
    -f, --file <file>     use given config file
    --blob <blob-id>      read config from given blob object

Action
    --get                 get value: name [value-pattern]
    --get-all             get all values: key [value-pattern]
    --get-regexp          get values for regexp: name-regex [value-pattern]
    --get-urlmatch        get value specific for the URL: section[.var] URL
    --replace-all         replace all matching variables: name value [value-pattern]
    --add                 add a new variable: name value
    --unset               remove a variable: name [value-pattern]
    --unset-all           remove all matches: name [value-pattern]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    --fixed-value         use string equality when comparing values to 'value-pattern'
    -e, --edit            open an editor
    --get-color           find the color configured: slot [default]
    --get-colorbool       find the color setting: slot [stdout-is-tty]

Type
    -t, --type <type>     value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --null            terminate values with NUL byte
    --name-only           show variable names only
    --includes            respect include directives on lookup
    --show-origin         show origin of config (file, standard input, blob, command line)
    --show-scope          show scope of config (worktree, local, global, system, command)
    --default <value>     with --get, use default value when missing entry
```

---
layout: two-cols
---

# Creating a new repository

- ### A repository is initialized with the following command:

```bash
git init
```

- ### This command creates a new repository in the current directory. 

- ### The repository is a hidden directory called `.git` that contains all the information changes tracked by `git`.

- ### You can check the status of the repository with:

```bash
git status
```

::right::

![](./resources/git/git-staging-area.svg)

- ### The repository is empty at this point and the output will be:
    
```bash
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

---
layout: two-cols
---

# Staging Area

- ### `git` has a staging area where files are placed before they are committed to the repository.

- ###  To move a file to the staging area use: 
  
  ```bash
  git add <file>
  ```

- ### To move all files to the staging area use: 
  
  ```bash
  git add --all
  ```

- ### To unstage a file use: 
    
    ```bash
    git restore --staged <file>
    ```
 
::right::

![](./resources/git/git-staging-area.svg)

- ### When staged files are present, the output of `git status` will be:

```bash
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   <file>
```

---
layout: two-cols
---

- ### To commit the files in the staging area use:

  ```bash
  git commit -m "A message describing the changes"
  ```
- ### Any new changes to the files in the repository are now tracked by `git`.

- ### Changes to files can be viewed with:
  ```bash
  git diff
  ```
  
::right::
![](./resources/git/git-committing.svg)

---

![](./resources/git/git-freshly-made-github-repo.svg)

---

![](./resources/git/git-restore.svg)


---

![](./resources/git/github-collaboration.svg)

---

![](./resources/git/github-repo-after-first-push.svg)
