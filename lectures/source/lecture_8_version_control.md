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

### **Version Control** using Git

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

- ### Rather than saving multiple copies of the same file, we can track changes.
- ###  Word processors and other software have some changes-tracking functionality but it is limited (no synchronous editing, no change history, etc.).
- ### `git` is an open-source version control system that is used to track changes in files.

![](./resources/git/play-changes.svg)

---
layout: image-right
image: ./resources/git/versions.svg
backgroundSize: contain
---

# Different Versions 

- ### An eddit to a file might overwrite some of the content in the previous version.
- ### This *divergences* may arrise while working alone, but they are really common when multiple people are working on the same file.

---
layout: image-right
image: ./resources/git/merge.svg
backgroundSize: contain
---

# Merging 

- ### `git` has great functionality for merging different versions of the same file.
- ### If the previous content is not overwritten, or deleted, merge just combines the changes into one file.
- ### If changes over-write each other a so-called **merge conflict** arises.

---
layout: two-cols
---

# Using `git` for the first time 

- ### The user name and email address need to configured.

```bash
git config --global user.name "Mindaugas Sarpis"
git config --global user.email "mindaugas.sarpis@cern.ch"
```

- ### Check the configuration with:

```bash
git config --list
```

- ### Edit the configuration with:
  
```bash
git config --global --edit
```

- ### Open configuration help:
   
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

- ### `git` has a staging area where files are placed to track the changes made to them.  

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
 
- ### Changes to files can be viewed with:
  ```bash
  git diff
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

# Committing Changes

- ### Files are committed to the repository from the staging area with:

  ```bash
  git commit -m "A message describing the changes"
  ```
- ### Commit is a snapshot of the repository at a given time.

- ### Only changes to files are tracked, not the directories themselves. 
- ### It's best to keep the commits small and focused on a single change.
- ### The commit message should be descriptive and concise.
- ### The commit message should be in the present tense.
  

::right::
![](./resources/git/git-committing.svg)

---
layout: two-cols
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
::right::

![](./resources/git/git-restore.svg)

- ### A new commit reverting the changes can be made with:
  ```bash
  git revert < hash >
  ```

- ### The entire repository can be restored to the last commit with deleting the changes:

  ```bash
  git reset --hard < hash >
  ```

---
layout: image
image: ./resources/git/git_staging.svg
backgroundSize: contain
---

---
layout: two-cols
---

# Ignoring Files and Directories 

- ### There might be files that you don't want to track with `git`.

  - #### Temporary files
  - #### Output files 
  - #### Files with sensitive information
  - #### Large files

- ### These files can be ignored by creating a `.gitignore` file in the repository.

::right:: 

```bash {*}{maxHeight:'400px'}
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
layout: two-cols
---

# Git Remotes

- ### One of the most powerful features of `git` is the ability to work with remote repositories.
- ### Remote repositories are copies of the repository that are stored on a server.
- ### Using one of the remote providers (GitHub, GitLab, Bitbucket, etc.) you can store your repository in the cloud.
- ### This enables collaboration with other people and provides a backup of your work.
::right::

![](./resources/git/git-freshly-made-github-repo.svg)

---
layout: image
image: 
backgroundSize: contain
---

---

---

![](./resources/git/git-restore.svg)


---

![](./resources/git/github-collaboration.svg)

---

![](./resources/git/github-repo-after-first-push.svg)
