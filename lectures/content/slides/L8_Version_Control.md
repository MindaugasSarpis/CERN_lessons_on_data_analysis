---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Version Control"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Version Control

---
hideInToc: true
layout: quote
---

# Every file has a history. **Version control** lets you navigate that history, collaborate without conflict, and never lose work again.

---
hideInToc: true
---

# The Importance of Version Control

<div class="grid-2 gap-md mt-md">

<div class="card card-warning pad-tight">

## ⚠️ **The Problem**

- Even if working alone, many different versions of the same file will exist
- Some overwritten changes might be needed later
- A "versioned" file might be needed when implementing comments from supervisor / reviewers
- This holds true for written work, code and other files

</div>

<div>

<img src="/comic_version.jfif" style="max-height: 450px;">

</div>

</div>

---
hideInToc: true
---

# Tracking Changes (differences)

<div class="card card-info pad-tight mt-md">

## 🔍 **Why Track Changes?**

- Rather than saving multiple copies of the same file, we can track changes
- Word processors and other software have some change-tracking functionality but it is limited (no synchronous editing, no change history, etc.)
- `git` is an open-source version control system that is used to track changes in files

</div>

![](/play-changes.svg)

---
hideInToc: true
---

# Different Versions

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔀 **Diverging Histories**

- An edit to a file might overwrite some of the content in the previous version
- This *divergences* may arrise while working alone, but they are really common when multiple people are working on the same file

</div>

<div>

<img src="/versions.svg" style="max-height: 450px;">

</div>

</div>

---
hideInToc: true
---

# Merging

<div class="grid-2 gap-md mt-md">

<div class="card card-success pad-tight">

## 🔗 **Combining Changes**

- `git` has great functionality for merging different versions of the same file
- If the previous content is not overwritten, or deleted, merge just combines the changes into one file
- If changes over-write each other a so-called **merge conflict** arises

</div>

<div>

<img src="/merge.svg" style="max-height: 450px;">

</div>

</div>

---
hideInToc: true
---

# Using `git` for the first time

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## ⚙️ **Configuration**

- The user name and email address need to be configured.

```bash
git config --global user.name "Mindaugas Sarpis"
git config --global user.email "mindaugas.sarpis@cern.ch"
```

- Check the configuration with:

```bash
git config --list
```

- Edit the configuration with:

```bash
git config --global --edit
```

- Open configuration help:

```bash
git config --h
git config --help
```

</div>

<div class="card card-secondary pad-tight" style="font-size: 0.7em; overflow: auto; max-height: 475px;">

```bash
usage: git config [<options>]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    --worktree            use per-worktree config file
    -f, --file < file >     use given config file
    --blob < blob-id >      read config from given blob object

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
    --default < value >     with --get, use default value when missing entry
```

</div>

</div>

---
hideInToc: true
---

# Creating a new repository

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📂 **Initializing a Repository**

- A repository is initialized with the following command:

```bash
git init
```

- This command creates a new repository in the current directory.

- The repository is a hidden directory called `.git` that contains all the information changes tracked by `git`.

- You can check the status of the repository with:

```bash
git status
```

</div>

<div>

![](/git-staging-area.svg)

<div class="card card-secondary pad-compact mt-sm">

The repository is empty at this point and the output will be:

```bash
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

</div>

</div>

</div>

---
hideInToc: true
---

# Staging Area

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📋 **Adding Files to the Stage**

- `git` has a staging area where files are placed to track the changes made to them.

- To move a file to the staging area use:

```bash
git add <file>
```

- To move all files to the staging area use:

```bash
git add --all
```

- To unstage a file use:

```bash
git restore --staged <file>
```

- Changes to files can be viewed with:

```bash
git diff
```

</div>

<div>

![](/git-staging-area.svg)

<div class="card card-info pad-compact mt-sm">

When staged files are present, the output of `git status` will be:

```bash
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   < file >
```

</div>

</div>

</div>

---
hideInToc: true
---

# Committing Changes

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📸 **Creating Snapshots**

- Files are committed to the repository from the staging area with:

```bash
git commit -m "A message describing the changes"
```

- Commit is a snapshot of the repository at a given time

- Only changes to files are tracked, not the directories themselves

- It's best to keep the commits small and focused on a single change

- The commit message should be descriptive and concise

- The commit message should be in the present tense

</div>

<div>

![](/git-committing.svg)

</div>

</div>

---
hideInToc: true
---

# Restoring Changes

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## ↩️ **Undoing Changes**

- Changes to files can be restored to the last commit with:

  ```bash
  git restore < file >
  ```

- Changes to files can be restored to the last commit and the staging area with:

  ```bash
  git restore --staged < file >
  ```

- Changes to files from previous commits can be restored using the *hash* of the commit:

  ```bash
  git restore --source=<hash> < file >
  ```

- A new commit reverting the changes can be made with:

  ```bash
  git revert < hash >
  ```

</div>

<div>

![](/git-restore.svg)

<div class="card card-warning pad-compact mt-sm">

The entire repository can be restored to the last commit with deleting the changes:

```bash
git reset --hard < hash >
```

</div>

</div>

</div>

---
layout: image
image: /git_staging.svg
backgroundSize: contain
hideInToc: true
---

---
hideInToc: true
---

# Ignoring Files and Directories

<div class="grid-2 gap-md mt-md">

<div class="card card-warning pad-tight">

## 🚫 **What to Ignore**

- There might be files that you don't want to track with `git`

  - Temporary files

  - Output files

  - Files with sensitive information

  - Large files

- These files can be ignored by creating a `.gitignore` file in the repository

</div>

<div>

```bash {*}{maxHeight:'350px'}
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
```

</div>

</div>

---
layout: image-right
image: /git-freshly-made-github-repo.svg
backgroundSize: contain
hideInToc: true
---

# Git Remotes

- ### One of the most powerful features of `git` is the ability to work with remote repositories.
- ### Remote repositories are copies of the repository that are stored on a server.
- ### Using one of the remote providers (GitHub, GitLab, Bitbucket, etc.) you can store your repository in the cloud.
- ### This enables collaboration with other people and provides a backup of your work.

---
layout: image-right
image: /git-freshly-made-github-repo.svg
backgroundSize: contain
hideInToc: true
---

# Git Remotes

- ### The remote is created via the remote provider (GitHub, GitLab, Bitbucket, etc.).
- ### A remote URL needs to be added to the local repository with:

```bash
git remote add origin git@github.com:mygithub/myremote.git
```

- ### To check which remotes are added:

```bash
  git remote -v
```

---
layout: image-right
image: /github-repo-after-first-push.svg
backgroundSize: contain
hideInToc: true
---

# Push / Pull Operations

- ### Changes to the local repository can be pushed to the remote repository with:

```bash
git push origin main
```

- ### Changes to the remote repository can be pulled to the local repository with:

```bash
git pull
```

---
layout: image-right
image: /github-collaboration.svg
backgroundSize: contain
hideInToc: true
---

# Cloning Repositories

- ### A repository can be cloned from a remote repository with:

```bash
git clone < URL >
```

---
hideInToc: true
---

# Branches

<div class="card card-info pad-tight mt-md">

## 🌿 **Parallel Development**

- `git` has a powerful branching system that allows for multiple versions of the repository to be worked on simultaneously.
- The default branch is called `main`.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## ➕ **Create a Branch**

```bash
git branch < branch-name >
```

</div>

<div class="card card-secondary pad-tight">

## 🔄 **Switch Branches**

```bash
git checkout < branch-name >
```

</div>

</div>

---
layout: center
hideInToc: true
---

# [An interactive git playground](https://learngitbranching.js.org/)
