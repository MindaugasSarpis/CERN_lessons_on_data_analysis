---
background: /figures/background_intro.jpg

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

# Data Analysis and Artificial Intelligence

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

<img src="/figures/comic_version.jfif" style="max-height: 450px;">

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

![](/figures/play-changes.svg)

---
hideInToc: true
---

# Different Versions

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔀 **Diverging Histories**

- An edit to a file might overwrite some of the content in the previous version
- Such *divergence* may arise while working alone, but it is really common when multiple people are working on the same file

</div>

<div>

<img src="/figures/versions.svg" style="max-height: 450px;">

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

<img src="/figures/merge.svg" style="max-height: 450px;">

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

- Edit the configuration with:

```bash
git config --global --edit
```

- Open short help for any command:

```bash
git config --h
```

</div>

<div class="card card-info pad-tight">

## 🔍 **Checking Your Config**

- View all current settings with:

```bash
git config --list
```

- Example output:

```bash
user.name=Mindaugas Sarpis
user.email=mindaugas.sarpis@cern.ch
core.editor=vim
init.defaultbranch=main
color.ui=auto
pull.rebase=false
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

![](/figures/git-staging-area.svg)

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

# Staging Area — Adding Files

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

</div>

<div>

![](/figures/git-staging-area.svg)

<div class="card card-info pad-compact mt-sm">

When staged files are present, the output of `git status` will be:

```bash
On branch main
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

# Staging Area — Unstaging & Diffing

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔄 **Unstaging Files**

- To unstage a file use:

```bash
git restore --staged <file>
```

- This moves the file back to the working directory without discarding your changes.

</div>

<div class="card card-secondary pad-tight">

## 🔍 **Viewing Differences**

- Changes to files can be viewed with:

```bash
git diff
```

- To see differences of staged files:

```bash
git diff --staged
```

- To compare with a specific commit:

```bash
git diff <hash>
```

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

![](/figures/git-committing.svg)

</div>

</div>

---
hideInToc: true
---

# Viewing History

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 📜 **Git Log**

```bash
# Full history
git log

# Compact view (one line per commit)
git log --oneline

# Visual branch graph
git log --oneline --graph --all
```

</div>

<div class="card card-secondary pad-tight">

## ✍️ **Commit Message Best Practices**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning pad-compact">

❌ "fixed stuff"

❌ "update"

❌ "asdf"

</div>

<div class="card card-success pad-compact">

✅ "Add data validation for input CSV"

✅ "Fix off-by-one error in histogram bins"

✅ "Remove unused plot function"

</div>

</div>

</div>

</div>

---
hideInToc: true
---

# Restoring Files

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## ↩️ **Undo Working Directory Changes**

- Restore a file to the last committed version (discard uncommitted edits):

```bash
git restore < file >
```

- Unstage a file while keeping your edits:

```bash
git restore --staged < file >
```

</div>

<div>

![](/figures/git-restore.svg)

<div class="card card-info pad-compact mt-sm">

## 💡 **When to Use**

- `git restore <file>` — discard local edits
- `git restore --staged <file>` — unstage without losing changes

</div>

</div>

</div>

---
hideInToc: true
---

# Reset & Revert

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔙 **Restore from History**

- Restore a file from a previous commit using its *hash*:

```bash
git restore --source=<hash> < file >
```

- Create a **new commit** that undoes a previous one:

```bash
git revert < hash >
```

`git revert` is safe because it adds history rather than deleting it.

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Dangerous: Hard Reset**

`reset --hard` permanently deletes **all uncommitted changes**. Cannot be undone.

```bash
git reset --hard < hash >
```

- Use only when you truly want to throw away work
- Prefer `git revert` for undoing commits already shared with others

</div>

</div>

---
layout: image
image: /figures/git_staging.svg
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
image: /figures/git-freshly-made-github-repo.svg
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
image: /figures/git-freshly-made-github-repo.svg
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
hideInToc: true
---

# SSH Key Setup

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔑 **Why SSH?**

- `git@github.com:` remotes use SSH for authentication
- SSH keys let you push/pull without entering a password every time
- More secure than HTTPS with stored passwords

</div>

<div class="card card-secondary pad-tight">

## ⚙️ **Quick Setup**

```bash
# Generate a new SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add the key to the agent
ssh-add ~/.ssh/id_ed25519

# Copy the public key
cat ~/.ssh/id_ed25519.pub
```

Then add the public key to **GitHub > Settings > SSH and GPG keys**.

</div>

</div>

---
layout: image-right
image: /figures/github-repo-after-first-push.svg
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
image: /figures/github-collaboration.svg
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

## ➕ **Create & Switch**

```bash
# Create and switch in one command
git switch -c feature-name

# Or separately
git branch feature-name
git switch feature-name
```

</div>

<div class="card card-secondary pad-tight">

## 🔀 **Merge & Clean Up**

```bash
# Switch back to main
git switch main

# Merge the feature branch
git merge feature-name

# Delete merged branch
git branch -d feature-name
```

</div>

</div>

---
hideInToc: true
---

# Merge Conflicts — What They Look Like

<div class="card card-warning pad-tight mt-md">

## ⚠️ **When two branches change the same lines**

- If changes over-write each other a so-called **merge conflict** arises
- `git` marks the conflict in the file so you can decide which version to keep

</div>

<div class="card card-secondary pad-tight mt-md">

## 🔍 **Conflict Markers**

```text {*}{lines:false}
{{'<<<<<<< HEAD'}}
result = calculate_mean(data)
{{'======='}}
result = calculate_median(data)
{{'>>>>>>> feature-branch'}}
```

- Everything between `<<<<<<< HEAD` and `=======` is **your** version
- Everything between `=======` and `>>>>>>> feature-branch` is the **incoming** version

</div>

---
hideInToc: true
---

# Resolving Merge Conflicts

<div class="grid-2 gap-md mt-md">

<div class="card card-primary pad-tight">

## 🔧 **How to resolve**

1. Open the file and choose the correct version
2. Remove the conflict markers (`<<<<`, `====`, `>>>>`)
3. Stage and commit the resolved file

```bash
git add resolved_file.py
git commit -m "Resolve merge conflict"
```

</div>

<div class="card card-info pad-compact">

## 💡 **Tips**

- Conflicts are **normal** in collaborative work
- Pull frequently to minimize conflicts
- Communicate with teammates about shared files
- VS Code highlights conflicts with clickable options

</div>

</div>

---
hideInToc: true
---

# Typical Daily Workflow

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

1️⃣ `git pull` — get latest changes from remote

</div>

<div class="card card-secondary pad-compact">

2️⃣ `git switch -c my-feature` — create a branch for your work

</div>

<div class="card card-accent pad-compact">

3️⃣ *Make changes to files*

</div>

<div class="card card-info pad-compact">

4️⃣ `git add` + `git commit -m "descriptive message"` — save your work

</div>

<div class="card card-success pad-compact">

5️⃣ `git push origin my-feature` — share with remote

</div>

<div class="card card-warning pad-compact">

6️⃣ *Create a Pull Request on GitHub for code review*

</div>

</div>

---
layout: center
hideInToc: true
---

# [An interactive git playground](https://learngitbranching.js.org/)

---
hideInToc: true
---

# Looking Ahead

<div class="card card-info pad-tight mt-md">

## 🔗 **Git in the Bigger Picture**

Version control is one pillar of **reproducible research**. In **L12**, we combine git with:

- **Virtual environments** — isolate dependencies
- **Automated scripts** — one command runs the full analysis
- **CI/CD** — run tests and checks on every push

Together, these practices ensure that anyone can reproduce your results — from raw data to final figures.

</div>
