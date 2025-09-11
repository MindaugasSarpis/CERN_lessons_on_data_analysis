---
marp: true
background: /intro_background.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 9: Version Control"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 9:

## Version Control

---
layout: two-cols
hideInToc: true
---

# The Importance of Version Control

- ### Even if working alone, many different versions of the same file will exist

- ### Some overwritten changes might be needed later

- ### A "versioned" file might be needed when implementing comments from supervisor / reviewers

- ### This hold true for written work, code and other files

::right::

<img src="/comic_version.jfif" style="max-height: 500px; margin-left: 30px">

---
hideInToc: true
---

# Tracking Changes (differences)

- ### Rather than saving multiple copies of the same file, we can track changes

- ### Word processors and other software have some change-tracking functionality but it is limited (no synchronous editing, no change history, etc.)

- ### `git` is an open-source version control system that is used to track changes in files

![](/play-changes.svg)

---
layout: two-cols
hideInToc: true
---

# Different Versions

- ### An eddit to a file might overwrite some of the content in the previous version

- ### This *divergences* may arrise while working alone, but they are really common when multiple people are working on the same file

::right::

<img src="/versions.svg" style="max-height: 500px; margin-left: 30px">

---
layout: two-cols
hideInToc: true
---

# Merging

- ### `git` has great functionality for merging different versions of the same file

- ### If the previous content is not overwritten, or deleted, merge just combines the changes into one file

- ### If changes over-write each other a so-called **merge conflict** arises

::right::

<img src="/merge.svg" style="max-height: 500px; margin-left: 30px">

---
layout: two-cols
hideInToc: true
---

# Using `git` for the first time 

- ### The user name and email address need to configured.

<div style="max-width: 350px">
```bash
git config --global user.name "Mindaugas Sarpis"
git config --global user.email "mindaugas.sarpis@cern.ch"
```
</div>

- ### Check the configuration with:

<div style="max-width: 350px">
```bash
git config --list
```
</div>

- ### Edit the configuration with:
  
<div style="max-width: 350px">
```bash
git config --global --edit
```
</div>

- ### Open configuration help:

<div style="max-width: 350px">
```bash
git config --h
git config --help
```
</div>

::right::

<div style="max-width: 450px; max-height: 475px; overflow: auto;">
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

---
layout: two-cols
hideInToc: true
---

# Creating a new repository

- ### A repository is initialized with the following command:

<div style="max-width: 350px">
```bash
git init
```
</div>

- ### This command creates a new repository in the current directory. 

- ### The repository is a hidden directory called `.git` that contains all the information changes tracked by `git`.

- ### You can check the status of the repository with:

<div style="max-width: 350px">
```bash
git status
```
</div>

::right::

![](/git-staging-area.svg)

- ### The repository is empty at this point and the output will be:

```bash
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

---
layout: two-cols
hideInToc: true
---

# Staging Area

- ### `git` has a staging area where files are placed to track the changes made to them.  

- ### To move a file to the staging area use: 
  
<div style="max-width: 350px">
```bash
git add <file>
```
</div>

- ### To move all files to the staging area use:
  
<div style="max-width: 350px">
```bash
git add --all
```
</div>

- ### To unstage a file use:
  
<div style="max-width: 350px">
```bash
git restore --staged <file>
```
</div>

- ### Changes to files can be viewed with:

<div style="max-width: 350px">
```bash
git diff
```
</div>

::right::

![](/git-staging-area.svg)

- ### When staged files are present, the output of `git status` will be:

```bash
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   < file >
```

---
layout: two-cols
hideInToc: true
---

# Committing Changes

- ### Files are committed to the repository from the staging area with:

<div style="max-width: 375px">
```bash
git commit -m "A message describing the changes"
```
</div>

- ### Commit is a snapshot of the repository at a given time

- ### Only changes to files are tracked, not the directories themselves

- ### It's best to keep the commits small and focused on a single change

- ### The commit message should be descriptive and concise

- ### The commit message should be in the present tense
  
::right::
![](/git-committing.svg)

---
layout: two-cols
hideInToc: true
---

# Restoring Changes

- ### Changes to files can be restored to the last commit with:

  ```bash
  git restore < file >
  ```

- ### Changes to files can be restored to the last commit and the staging area with:

  ```bash
  git restore --staged < file >
  ```

- ### Changes to files from previous commits can be restored using the *hash* of the commit:

  ```bash
  git restore --source=<hash> < file >
  ```

- ### A new commit reverting the changes can be made with:

  ```bash
  git revert < hash >
  ```

::right::

![](/git-restore.svg)

&nbsp;

- ### The entire repository can be restored to the last commit with deleting the changes:

  ```bash
  git reset --hard < hash >
  ```

---
layout: image
image: /git_staging.svg
backgroundSize: contain
hideInToc: true
---

---
layout: two-cols
hideInToc: true
---

# Ignoring Files and Directories 

- ### There might be files that you don't want to track with `git`

  - #### Temporary files

  - #### Output files

  - #### Files with sensitive information

  - #### Large files

- ### These files can be ignored by creating a `.gitignore` file in the repository

::right::

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

- ### `git` has a powerful branching system that allows for multiple versions of the repository to be worked on simultaneously.
- ### The default branch is called `main`.
- ### A new branch can be created with:

```bash
git branch < branch-name >
```

- ### The branch can be switched with:

```bash
git checkout < branch-name >
```

---
hideInToc: true
---

# [An interactive git playground](https://learngitbranching.js.org/)