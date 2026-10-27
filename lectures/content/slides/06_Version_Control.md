---
layout: cover
title: "Version Control with Git"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Version Control

##### <span class="aims-badge">♻️ reproducibility · 🔧 tool-agnostic</span>

---
hideInToc: true
layout: quote
---

# **Version control** keeps every state a project went through, with who changed what, when and why.

<!--
**Say:** read the line, then go straight to the copies.
(~1 min)
-->

---
hideInToc: true
---

# Versions Kept as **Copies**

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-tight">

## ⚠️ **What goes wrong**

- A file that changes gets copied: `report_final.md`, `report_final_v2.md`, `report_final_v2_corrected.md`
- No copy says who changed a line, when, or why
- Two copies edited on the same day have to be joined by hand
- A change that turned out wrong can be taken back only if the older copy was kept

</div>

<div>

<img src="/figures/comic_version.jfif" style="max-height: 415px;">

</div>

</div>

<!--
**Do:** a show of hands: who has files named final, final_v2, final_corrected?
**Say:** a copy keeps the bytes and the name. Who, when and why live in somebody's memory.
(~2 min)
-->

---
hideInToc: true
---

# Two Copies of the **Export**

<div class="card card-info card-glass pad-compact mt-sm">

Smiltė keeps `data/raw/daily_export.csv` of the weather project: the daily mean temperatures of 1 to 9 October 2025. Her colleague Tomas sends his copy back by e-mail. Both files have 180 bytes.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **Smiltė's copy, lines 1 to 4**

```text
nr;date;temp_c
1;2025-10-01;6,3
2;2025-10-02;5,0
3;2025-10-03;5,6
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Tomas's copy, lines 1 to 4**

```text
nr;date;temp_c
1;2025-10-01;6,4
2;2025-10-02;5,0
3;2025-10-03;5,6
```

</div>

</div>

<div class="card card-warning card-glass pad-compact table-compact mt-md">

| Question | What the two files say |
| --- | --- |
| Do they differ? | Yes, in line 2, 1 October: `6,3` against `6,4` |
| Who changed it, when, and why? | Nothing in either file |

</div>

<!--
**Ask:** which copy is the file as it came from the station? Was 6,4 read off a paper log, or typed by mistake?
**If asked:** the checksums of Lecture 4, `9d849815…` and `13fbcae6…`, say that the two files differ, not where.
(~3 min)
-->

---
hideInToc: true
---

# A File as a Sequence of **Changes**

<div class="card card-primary card-glass pad-compact mt-sm">

A version control system records every change of a file, one after another, each with who made it, when, and why. Any earlier version can be brought back, and nothing is copied by hand.

</div>

<img src="/figures/git_changes.svg" style="max-width:100%;display:block;margin:1.2rem auto 0;max-height:215px;">

<!--
**Say:** three versions of the export from left to right, each with who, when and why. The middle one is Tomas's 6,4 of the two copies; the third takes it back. Every step can be brought back.
(~2 min)
-->

---
hideInToc: true
---

# How a Merge Joins Two **Versions**

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🔀 **Two versions from one start**

<img src="/figures/git_versions.svg" style="max-width:100%;display:block;margin:0 auto;max-height:250px;">

</div>

<div class="card card-success card-glass pad-compact">

## 🔗 **A merge joins them**

<img src="/figures/git_merge.svg" style="max-width:100%;display:block;margin:0 auto;max-height:250px;">

</div>

</div>

<div class="note-text mt-sm">Changes to different lines are joined without help. Changes to the same line are a <strong>conflict</strong>: Git shows both, and a person decides.</div>

<!--
**Say:** Smiltė and Tomas change the same export on the same day. With copies, someone joins the two by hand; Git joins them line by line.
(~2 min)
-->

---
hideInToc: true
---

# What Drive, Dropbox and Word **Keep**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | Google Drive, Dropbox | Track Changes in Word | Git |
| --- | --- | --- | --- |
| Versions of | Each file on its own | One document | The whole project at once |
| Kept for | Drive 30 days, Dropbox 30 to 365 | Until a change is accepted | For good |
| Who and when | Yes | Yes | Yes |
| Why | Nothing | A comment, if someone writes one | A message with every commit |
| Two editors, one file | Dropbox makes a *conflicted copy* | Both edits marked in one file | A merge, line by line |
| Which files | Any | Word documents | Any; line by line for text |

</div>

<!--
**Ask:** who has brought back an old version from Drive or Dropbox? How far back could it go?
**Say:** each tool on the left keeps a history of something. Git keeps one history of the whole project, with a reason for every step, and that column is what this lecture builds.
**If asked:** Drive deletes a version of an uploaded file after 30 days or 100 newer versions, unless it is marked **Keep forever**; Dropbox keeps 30 days on Basic and Plus, 180 or 365 on the business plans. Google Docs has its own history, per document.
(~3 min)
-->

---
hideInToc: true
---

# Where Git Comes **From**

<div class="card card-warning card-glass pad-compact mt-sm">

## 📅 **BitKeeper, 2002 to 2005**

- 2002: the Linux kernel keeps its history in BitKeeper, a proprietary tool, free of charge for the kernel's developers
- April 2005: the company withdraws the free version
- 3 April: Linus Torvalds starts Git. 7 April: its first commit, below. 16 June: kernel 2.6.12 is released from Git

</div>

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash: the first commit, in a clone of Git**

```text
$ git log --reverse | head -5
commit e83c5163316f89bfbde7d9ab23ca2e25604af290
Author: Linus Torvalds <torvalds@ppc970.osdl.org>
Date:   Thu Apr 7 15:13:13 2005 -0700

    Initial revision of "git", the information manager from hell
```

</div>

<!--
**Say:** the kernel's history sat in a tool its developers did not own. Git is free, and every copy holds the whole history: 21 years on, its first commit still says who, when and why, under the same id in every copy.
**If asked:** BitKeeper was free on one condition, no work on a competing tool; it became open source in 2016. Git's own history had 82 542 commits on 19 October 2026.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Setting **Up**

Git writes a name and an e-mail address into every commit.

<!--
**Say:** Git was installed in Seminar 4. Before the first commit it has to know who is committing.
(~1 min)
-->

---
hideInToc: true
class: live
---

# Check Git and Its **Settings**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git --version
git version 2.56.0
```
```text
$ git --version
git version 2.56.0
$ git config --global user.name
Smiltė
```
```text
$ git --version
git version 2.56.0
$ git config --global user.name
Smiltė
$ git config --global user.email
smilte@example.org
```
````

Your version differs. Git for Windows prints `2.56.0.windows.1`, Apple's Git ends in `(Apple Git-…)`.

</div>

<div class="card card-secondary card-glass pad-compact">

## ➕ **Three more settings**

```text
$ git config --global init.defaultBranch main
$ git config --global pull.rebase false
$ git config --global core.autocrlf false
```

Type them now, once per laptop; none prints anything. They make Git name things and behave as on these slides, on a Mac and on Windows alike.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ An empty answer means the setting is missing: `git config --global user.name "Your Name"`, and the same for `user.email`. Both are written into every commit.

</div>

<!--
**Live:** `git --version`, then `git config --global user.name`, in the terminal of VS Code.
**Ask:** hands up, who gets a version number? Who gets a name?
**Say:** the three lines on the right are typed now, on every laptop. Git for Windows comes with master and with core.autocrlf true.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Tracking **Changes**

The weather project of Lecture 4 goes into a repository, one commit at a time.

<!--
**Say:** each step once in the Source Control view and once typed: the button and the command are the same thing.
(~1 min)
-->

---
hideInToc: true
---

# Where a Change Goes: add, commit, push

<img src="/figures/git_places.svg" style="max-width:100%;display:block;margin:0.4rem auto 0;max-height:205px;">

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📋 **`git add`**

Copies a file, as it is saved now, into the **staging area**: the list of what the next commit will hold.

</div>

<div class="card card-primary card-glass pad-compact">

## 🗄️ **`git commit`**

Keeps everything staged as one version, a **commit**, in the folder `.git`: the history.

</div>

<div class="card card-primary card-glass pad-compact">

## ☁️ **`git push`**

Sends the commits to a copy of the repository on a server, GitHub, where others can fetch them.

</div>

</div>

<!--
**Say:** a change passes four places, from left to right, one command per step. The first three are on the laptop: until `git push`, nobody else sees anything.
**If asked:** the staging area is also called the *index*. It lets one commit hold one purpose: stage what belongs together, leave the rest for the next commit.
(~3 min)
-->

---
hideInToc: true
---

# Source Control in **VS Code**

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 2fr 3fr;">

<div class="text-center">

<img src="/figures/git_vscode_init.png" style="max-height: 400px; display: inline-block; border-radius: 6px; border: 1px solid var(--hair);">

</div>

<div class="card card-primary card-glass pad-tight">

## 🧭 **Two ways to the same Git**

- The **Source Control** view is the third icon of the Activity Bar: `Ctrl+Shift+G` (macOS `Cmd+Shift+G`)
- VS Code runs the Git that is installed. Every button of the view runs a Git command
- The same commands are typed in the terminal: **Terminal** > **New Terminal**
- Another editor has other buttons. The commands are the same everywhere 🔧

</div>

</div>

<!--
**Do:** open the weather project in VS Code, then the Source Control view.
(~2 min)
-->

---
hideInToc: true
class: live
---

# Create the **Repository**

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 2fr 3fr;">

<div class="card card-primary card-glass pad-compact">

## 🖱️ **In Source Control**

Select **Initialize Repository**. The view then lists every file of the folder under **Changes**.

</div>

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Typed**

```text
$ git init
Initialized empty Git repository in /Users/smilte/weather-project/.git/
$ ls -a
.  ..  .git  README.md  data  results  scripts
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

A **repository** is the project folder together with its `.git` folder. All commits are in `.git`. It is made once per project.

</div>

<div class="card card-warning card-glass pad-compact">

⚠️ Deleting `.git` deletes the history and leaves the files. Never make a repository inside another one, and never in the home folder.

</div>

</div>

<!--
**Live:** with `weather-project` (from `weather_project_git.zip`) open in VS Code, Source Control: select **Initialize Repository**, then `ls -a` in the terminal: the button made this one folder.
**If asked:** `-a` shows names that begin with a dot, which `ls` hides. Git Bash may list `README.md` after `data`.
(~2 min)
-->

---
hideInToc: true
---

# What Git Sees: `git status`

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 2fr 3fr;">

<div class="text-center">

<img src="/figures/git_weather_changes.png" style="max-height: 360px; display: inline-block; border-radius: 6px; border: 1px solid var(--hair);">

</div>

<div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ git status --short
?? README.md
?? data/
?? scripts/
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

`U` in the view and `??` in the terminal say the same: the file is **untracked**, Git sees it and has no version of it. The terminal names a folder once; `results` is empty and not listed.

</div>

</div>

</div>

<div class="note-text mt-sm">Without <code>--short</code>, <code>git status</code> says the same in sentences, with a hint for the next command. It changes nothing.</div>

<!--
**Ask:** count the files in the view: 8. Which two did a script make? `daily.csv` and `weather_valid.csv`.
**If asked:** the long form starts `On branch main`, `No commits yet`, and lists the three names under `Untracked files:`.
(~2 min)
-->

---
hideInToc: true
class: live
---

# Choose What Goes into the Next Commit: **add**

<img src="/figures/git_add.svg" style="max-width:100%;display:block;margin:0.2rem auto 0;max-height:185px;">

<div class="grid-2 gap-md mt-sm">

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Typed**

```text
$ git add README.md
$ git status --short
A  README.md
?? data/
?? scripts/
```

</div>

<div class="card card-primary card-glass pad-compact">

## 🖱️ **In Source Control**

**+** beside `README.md` moves it to **Staged Changes**, and its letter turns to `A`, *added*. The file stays in the folder as it was. `git add` prints nothing.

</div>

</div>

<div class="note-text mt-sm">The staging area holds the file as it was at <code>git add</code>. An edit saved after it is not in the copy: add the file again.</div>

<!--
**Live:** in Source Control, **+** beside `README.md`; then `git status --short` in the terminal.
**Say:** nothing is in the history yet, and nothing has left the laptop. `add` only chooses what the next commit holds.
(~3 min)
-->

---
hideInToc: true
class: live
---

# Keep It in the History: **commit**

<img src="/figures/git_commit.svg" style="max-width:100%;display:block;margin:0.2rem auto 0;max-height:185px;">

<div class="grid-2 gap-md mt-sm" style="grid-template-columns: 3fr 2fr;">

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Typed**

```text
$ git commit -m "Add the README"
[main (root-commit) c08a1c7] Add the README
 1 file changed, 49 insertions(+)
...
$ git status --short
?? data/
?? scripts/
```

</div>

<div class="card card-primary card-glass pad-compact">

## 🔎 **Reading the answer**

`main`: the **branch**, the line of commits this one starts (*root-commit*: the first). `c08a1c7`: the first digits of the commit's **id**. The staging area now equals the commit. In the view: message, then **Commit**.

</div>

</div>

<!--
**Live:** type "Add the README" in the message box of Source Control, then **Commit** (or `Ctrl+Enter`, macOS `Cmd+Enter`). The other seven files stay under Changes.
**Say:** from now on this README can always be brought back, even if the file is deleted. The two folders are still untracked: they wait for their own commit.
(~3 min)
-->

---
hideInToc: true
---

# What a Commit **Keeps**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| A commit keeps | In `c08a1c7`, the first commit |
| --- | --- |
| Every file of the staging area, complete | `README.md`, 49 lines |
| The commit before it | None: it is the first, the *root-commit* |
| Who, and when | Smiltė, 20 October 2026, 10:15 |
| Why | The message, *Add the README* |

</div>

<div class="card card-info card-glass pad-compact mt-md">

The **id**, `c08a1c73cb29ed8ed399f19e74f14996d05636d4`, is a checksum of all four. The same commit has the same id on every copy of the repository; another file, message or time gives another id.

</div>

<!--
**Say:** a commit is a complete picture of the staged files, with a pointer to the commit before it. Git shows it as the change from that one.
**If asked:** Git stores the four as a short text and hashes it; the slides For the Curious show that text.
(~2 min)
-->

---
hideInToc: true
---

# The Commit **Message**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## ✍️ **Rules**

- One commit has one purpose. Two changes that do not belong together are two commits
- The first line has at most about 50 characters
- It says what the commit does, as an instruction: *Add*, *Give*, *Remove*
- The reason goes below an empty line, when the first line does not give it

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔎 **Examples**

❌ `update`

❌ `fixed stuff`

❌ `final version`

✅ `Add the README`

✅ `Give the mean temperature in the README`

✅ `Mark the 120 hours of -999 in the README`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The message is read months later, by someone who sees one line per commit and nothing else.

</div>

<!--
**If asked:** "Add the data and the scripts" is one purpose: the scripts read the data, and neither works alone.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# What Goes into a **Repository**

The project holds raw data, scripts, and files that a script makes again. Not all of them belong in a repository.

<!--
**Say:** Git was made for text written by people, and the project has data files. Which go in, which stay out, and what the README then has to say.
(~1 min)
-->

---
hideInToc: true
---

# Which Files Go **In**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| File | In the repository | Reason |
| --- | --- | --- |
| `README.md`, the scripts | Yes | Written by hand. Nothing can make them again |
| Small raw data: `weather.csv`, 2.5 MB | Yes | The project is complete in one piece |
| Large raw data: one file of 3 GB | No | Too large for Git and for the host |
| `data/processed/*`, made by `rebuild.sh` | No | The script is in the repository and makes them again |
| `.DS_Store`, `Thumbs.db` | No | Made by the operating system, of no use to anyone |
| Passwords and access keys | Never | A pushed commit stays readable for good |

</div>

<div class="card card-info card-glass pad-compact mt-md">

`weather_valid.csv` has 2 511 735 bytes and would fit. It stays out because one line of `rebuild.sh` makes it again. The README promises its 87 553 lines, so a rebuilt copy can be checked.

</div>

<!--
**Ask:** where does `daily.csv` go? Out: the script writes it, and the README gives its checksum, 33fe5e77…
(~2 min)
-->

---
hideInToc: true
---

# The File **`.gitignore`**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`.gitignore`, in the project folder**

```text
# made by the operating system
.DS_Store
Thumbs.db

# made by scripts/rebuild.sh
data/processed/
```

One pattern per line, and `#` starts a comment. `*.tmp` is every file ending in `.tmp`. `data/processed/` is the whole folder.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ git add .gitignore
$ git commit -m "Add .gitignore"
[main e3f4e26] Add .gitignore
 1 file changed, 6 insertions(+)
...
```

🖱️ In the view: right-click a file, **Add to .gitignore**.

</div>

</div>

<div class="note-text mt-sm"><code>.gitignore</code> is a file of the project and is committed. It acts only on files that Git does not track yet.</div>

<!--
**Ask:** after this commit, how many files are left under Changes? Five: the two in `data/processed` are gone from the list.
(~3 min)
-->

---
hideInToc: true
---

# Commit the **Rest**

<div class="grid-2 gap-md mt-sm" style="align-items:start;">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git add .
$ git status --short --ignored
A  data/raw/daily_export.csv
A  data/raw/weather.csv
A  scripts/clean_export.py
A  scripts/column_stats.py
A  scripts/rebuild.sh
!! data/processed/
```
```text
$ git add .
$ git status --short --ignored
A  data/raw/daily_export.csv
A  data/raw/weather.csv
A  scripts/clean_export.py
A  scripts/column_stats.py
A  scripts/rebuild.sh
!! data/processed/
$ git commit -m "Add the data and the scripts"
[main a9f65a6] Add the data and the scripts
 5 files changed, 87798 insertions(+)
...
```
````

</div>

<div>

<img src="/figures/git_commit_rest.svg" style="max-width:100%;display:block;margin:0 auto;max-height:260px;">

<div class="card card-secondary card-glass pad-compact mt-sm">

- `git add .` stages everything in the present folder that is not ignored: the **+** on the **Changes** header
- Read the list before the commit: `!!` marks the ignored folder
- One purpose, one commit: the scripts read the data
- 87 673 of the 87 798 new lines are `weather.csv`

</div>

</div>

</div>

<!--
**Do:** stop after `git status` and let the room check the list against the Explorer.
**Say:** five files staged, one commit, as in the picture.
**If asked:** the commit also prints one `create mode` line per file; they are cut here.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Changes & **History**

A file changes, and the history says what changed, when and why.

<!--
**Say:** from here on, every change goes the same way: edit, read the diff, stage, commit.
(~1 min)
-->

---
hideInToc: true
class: live
---

# A Change, Seen as a **Diff**

<div class="text-center mt-sm">

<img src="/figures/git_weather_diff.png" style="max-height: 200px; display: inline-block; border-radius: 6px; border: 1px solid var(--hair);">

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🖱️ **In Source Control**

Smiltė adds a section **Result** to the README with the mean of Lecture 4. The file gets the letter `M`. Select it and the **diff view** opens: green lines are new, red lines gone.

</div>

<div class="card card-secondary card-glass pad-compact">

## 👀 **Read it before every commit**

The diff is what the commit will contain. It also shows an edit that was not meant: a deleted line, a stray character.

</div>

</div>

<!--
**Live:** in `README.md`, above `## Licence`, type the section below, save, select the file in Source Control; then **+** and commit: *Give the mean temperature in the README*.
`## Result` / empty line / `- **Mean air temperature, 2016 to 2025:** 7.16 °C` / `` - **From:** `column_stats.py` on `data/processed/weather_valid.csv`, 87 552 hours `` / empty line.
**If asked:** a wide window shows the two versions side by side, a narrow one line under line as here.
(~2 min)
-->

---
hideInToc: true
---

# The Same Diff, **Typed**

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ git diff
...
+## Result
+
+- **Mean air temperature, 2016 to 2025:** 7.16 °C
+- **From:** `column_stats.py` on `data/processed/…
+
 ## Licence
...
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔎 **Reading it**

- `+` a line that came
- `-` a line that went
- a space: an unchanged line, shown so the change can be found
- `...` marks lines cut on this slide

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Then the cycle closes as for every change: `git add README.md`, `git commit -m "Give the mean temperature in the README"`. The new commit is `15505c4`.

</div>

<!--
**Say:** the commit was made live on the slide before; here only the typed `git diff`. `git diff` compares the working folder with the staging area; after `git add` it prints nothing, and `git diff --staged` shows what will be committed.
**If asked:** the cut lines are a header with the two file names and `@@ -43,6 +43,11 @@`: six lines from line 43 before, eleven after.
(~3 min)
-->

---
hideInToc: true
---

# One Change, Three Steps

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Step | Working folder | Staging area | Repository | `git status` says |
| --- | --- | --- | --- | --- |
| Edit `README.md`, save | README with **Result** | as the last commit | last commit `a9f65a6` | *Changes not staged for commit* |
| `git add README.md` | the same | README with **Result** | `a9f65a6` | *Changes to be committed* |
| `git commit -m "…"` | the same | as the new commit | new commit `15505c4` | *nothing to commit* |

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

The staging area always holds the next commit. After a commit it equals that commit, until the next `git add`.

</div>

<div class="card card-info card-glass pad-compact">

Every change of the project goes this way: edit, read the diff, add, commit. `git status` says at any moment which step a file is at.

</div>

</div>

<!--
**Ask:** after the commit, can Tomas see the new Result section? No: it is in the repository on Smiltė's laptop only.
(~3 min)
-->

---
hideInToc: true
---

# Reading the History: **log**

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ git log --oneline
15505c4 (HEAD -> main) Give the mean temperature in the README
a9f65a6 Add the data and the scripts
ef28e40 Keep the committed bytes of every file on checkout
e3f4e26 Add .gitignore
c08a1c7 Add the README
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

- One line per commit, newest first: the id, then the message
- `(HEAD -> main)` marks the commit the working folder is at, the newest of the branch `main`
- `ef28e40` adds `.gitattributes`, a setting file shown under More Commands

</div>

<div class="card card-info card-glass pad-compact">

- `git log` without `--oneline` adds the author and the date of each commit
- The **Graph** at the bottom of Source Control lists the same commits

</div>

</div>

<!--
**Ask:** which commit made the README say 7.16? The newest.
**If asked:** a list longer than the window ends in a colon: the arrow keys scroll, q leaves. `ef28e40` adds `.gitattributes`, which keeps every checkout byte for byte as committed (For the Curious).
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Undoing**

A change can be wrong. How it is taken back depends on how far it got.

<!--
**Say:** three cases, by how far the change got: an edit in the working folder, the last commit, an older commit.
(~1 min)
-->

---
hideInToc: true
class: live
---

# Undo an Edit: **restore**

<div class="grid-2 gap-md mt-sm">

<div>

<img src="/figures/git_restore.svg" style="max-width:100%;display:block;margin:0 auto;max-height:215px;">

<div class="card card-primary card-glass pad-compact mt-sm">

In the view, the bent arrow beside a changed file is **Discard Changes**: the file goes back to its last commit, or to its last `git add`. **−** beside a staged file unstages it; the edit stays.

</div>

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git diff --stat
 README.md | 11 -----------
 1 file changed, 11 deletions(-)
```
```text
$ git diff --stat
 README.md | 11 -----------
 1 file changed, 11 deletions(-)
$ git restore README.md
```
```text
$ git diff --stat
 README.md | 11 -----------
 1 file changed, 11 deletions(-)
$ git restore README.md
$ git status
On branch main
nothing to commit, working tree clean
```
````

`git restore --staged README.md` unstages.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ An edit that was never committed and is discarded is gone. Git has no copy of it. Read the diff first.

</div>

<!--
**Live:** in the README select the section *Columns of `weather.csv`*, down to the line *Missing value*, delete it, save; `git diff --stat` (11 deletions); `git restore README.md`.
**Say:** this undo works after the editor was closed.
**If asked:** `git restore --source=<id> <file>` brings one file back as it was in an older commit.
(~2 min)
-->

---
hideInToc: true
---

# Correct the Last Commit: **amend**

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git add LICENSE
$ git commit -m "Add teh LICENSE named in the README"
[main c2422af] Add teh LICENSE named in the README
...
```
```text
$ git add LICENSE
$ git commit -m "Add teh LICENSE named in the README"
[main c2422af] Add teh LICENSE named in the README
...
$ git commit --amend -m "Add the LICENSE named in the README"
[main 2eab6b2] Add the LICENSE named in the README
...
```
```text
$ git add LICENSE
$ git commit -m "Add teh LICENSE named in the README"
[main c2422af] Add teh LICENSE named in the README
...
$ git commit --amend -m "Add the LICENSE named in the README"
[main 2eab6b2] Add the LICENSE named in the README
...
$ git log --oneline -2
2eab6b2 (HEAD -> main) Add the LICENSE named in the README
15505c4 Give the mean temperature in the README
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔁 **A new commit replaces the old**

The README names a file `LICENSE` that did not exist yet: Smiltė saves the MIT licence text under that name. `--amend` makes a new commit with the corrected message, `2eab6b2`, and `c2422af` leaves the history.

In the view: the arrow on **Commit**, then **Commit (Amend)**.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Amend only a commit that has not been pushed. A commit that others may already have is corrected by a new commit.

</div>

<!--
**Say:** the id is computed from the whole commit, message included, so a corrected commit is another commit with another id.
**If asked:** the MIT text is copied from choosealicense.com, with the year and the name.
(~2 min)
-->

---
hideInToc: true
---

# A Commit That Breaks the **Rebuild**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git rm data/raw/daily_export.csv
rm 'data/raw/daily_export.csv'
```
```text
$ git rm data/raw/daily_export.csv
rm 'data/raw/daily_export.csv'
$ git commit -m "Remove the raw export, daily.csv replaces it"
[main 172f06a] Remove the raw export, daily.csv replaces it
...
```
```text
$ git rm data/raw/daily_export.csv
rm 'data/raw/daily_export.csv'
$ git commit -m "Remove the raw export, daily.csv replaces it"
[main 172f06a] Remove the raw export, daily.csv replaces it
...
$ ./scripts/rebuild.sh
no file data/raw/daily_export.csv
```
```text
$ git rm data/raw/daily_export.csv
rm 'data/raw/daily_export.csv'
$ git commit -m "Remove the raw export, daily.csv replaces it"
[main 172f06a] Remove the raw export, daily.csv replaces it
...
$ ./scripts/rebuild.sh
no file data/raw/daily_export.csv
$ echo $?
1
```
````

</div>

<div class="card card-warning card-glass pad-compact mt-md">

`git rm` deletes the file and stages the deletion. The commit looked tidy: `daily.csv` holds the same nine values. Then the rebuild stops with status 1, because the script reads the raw export. Raw files are never deleted.

</div>

<!--
**Ask:** the commit is made. What now: copy the file back from an e-mail, or ask Git?
**If asked:** status 1 comes from the Python line, the last line of `rebuild.sh`: `clean_export.py` finds no input file.
(~2 min)
-->

---
hideInToc: true
---

# Take Back a Commit: **revert**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git revert --no-edit 172f06a
[main 2eb3b1c] Revert "Remove the raw export, daily.csv replaces it"
...
```
```text
$ git revert --no-edit 172f06a
[main 2eb3b1c] Revert "Remove the raw export, daily.csv replaces it"
...
$ git log --oneline -3
2eb3b1c (HEAD -> main) Revert "Remove the raw export, daily.csv replaces it"
172f06a Remove the raw export, daily.csv replaces it
2eab6b2 Add the LICENSE named in the README
```
```text
$ git revert --no-edit 172f06a
[main 2eb3b1c] Revert "Remove the raw export, daily.csv replaces it"
...
$ git log --oneline -3
2eb3b1c (HEAD -> main) Revert "Remove the raw export, daily.csv replaces it"
172f06a Remove the raw export, daily.csv replaces it
2eab6b2 Add the LICENSE named in the README
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
```
````

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## ↩️ **A commit that does the opposite**

`revert` adds a commit with the reverse change. Nothing leaves the history, so it is safe for pushed commits. `--no-edit` keeps the proposed message.

</div>

<!--
**Say:** the history keeps both the mistake and its correction, with the reason in each message.
(~2 min)
-->

---
hideInToc: true
---

# Choose the Undo by How Far the Change **Got**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| How far the change got | Typed | In Source Control |
| --- | --- | --- |
| Edited, not staged | `git restore <file>` | **Discard Changes** |
| Staged, not committed | `git restore --staged <file>` | **−** beside the file |
| The last commit, not pushed | `git commit --amend` | **Commit (Amend)** |
| Any commit, pushed or not | `git revert <id>` | No button: typed |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Only the first row loses work: an edit that was never committed has no copy in Git. Every other row keeps what was committed.

</div>

<!--
**Ask:** Tomas pushed a commit last week that was wrong. Which row? The last: revert.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# **Remotes**

Every commit so far lives in one `.git` folder on one laptop.

<!--
**Say:** a remote is the same history on a server.
(~1 min)
-->

---
hideInToc: true
---

# A Remote Is a Second **Copy**

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🆕 **A new, empty repository on GitHub**

<img src="/figures/git_remote_empty.svg" style="max-width:100%;display:block;margin:0 auto;max-height:260px;">

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬆️ **After the first push**

<img src="/figures/git_remote_pushed.svg" style="max-width:100%;display:block;margin:0 auto;max-height:260px;">

</div>

</div>

<div class="note-text mt-sm">A <strong>remote</strong> is the same repository on another computer, with the same commits under the same ids. GitHub, GitLab and Bitbucket keep remotes reachable; <code>origin</code> is the usual name of the first.</div>

<!--
**Say:** on the left Smiltė's laptop, on the right GitHub. `git push` sends the commits GitHub lacks; `git pull` fetches the ones the laptop lacks. What is there already is not sent again.
**Ask:** what is a remote for? A copy of the project outside the laptop, the same project on a second computer, work with other people on one history.
(~2 min)
-->

---
hideInToc: true
---

# A GitHub **Account**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🪪 **Create it once**

1. Open `github.com` and select **Sign up**
2. Enter an e-mail address, a password and a user name
3. Type in the code that GitHub sends to that address
4. Stay on the free plan. It allows private and public repositories without limit

</div>

<div class="card card-secondary card-glass pad-tight">

## 🤔 **Choose with care**

- The user name is public and part of every address: `github.com/<user>/<repository>`
- Use an e-mail address that you keep after your studies
- A **private** repository is seen by you and those you invite, a **public** one by everyone
- The e-mail of `git config` is in every commit, readable in a public repository

</div>

</div>

<!--
**Ask:** who has an account already? The others create one in the seminar; it takes three minutes and the mailbox.
(~2 min)
-->

---
hideInToc: true
---

# Publish from **VS Code**

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 2fr 3fr;">

<div class="text-center">

<img src="/figures/git_vscode_publish.png" style="max-height: 170px; display: inline-block; border-radius: 6px; border: 1px solid var(--hair);">

</div>

<div class="card card-primary card-glass pad-compact">

## 🖱️ **In Source Control**

1. When everything is committed, the button reads **Publish Branch**. Select it
2. VS Code asks: *The extension 'GitHub' wants to sign in using GitHub.* Select **Allow**, sign in in the browser and return
3. Choose **Publish to GitHub private repository**
4. **Open on GitHub** shows the project in the browser, with the README as its front page

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

From now on the button reads **Sync Changes**: it sends your new commits and brings the others' new commits.

</div>

<!--
**Say:** the four steps of the card; on GitHub the project shows its files, the README as its front page, and the commits with the same ids as in the terminal.
(~3 min)
-->

---
hideInToc: true
---

# Publish to GitHub, **Typed**

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🌐 **On `github.com` first**

**New repository**, the name `weather-project`, **Private**, no README, **Create repository**. `remote add` gives the new repository's address the short name `origin`; `push -u` sends `main` the first time. Later a plain `git push` is enough.

</div>

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ git remote add origin https://github.com/smilte-example/weather-project.git
$ git push -u origin main
...
To https://github.com/smilte-example/weather-project.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

</div>

<!--
**Say:** the first push asks for the GitHub sign-in; in the terminal of VS Code it goes through the browser.
**Ask:** push again at once, with nothing new. How much is sent? Nothing: `git push` answers `Everything up-to-date`.
**If asked:** the cut lines count what is sent: 30 objects, 554 KiB for eight commits and the data.
(~3 min)
-->

---
hideInToc: true
---

# Send the Commits to GitHub: **push**

<img src="/figures/git_push.svg" style="max-width:100%;display:block;margin:0.2rem auto 0;max-height:185px;">

<div class="grid-2 gap-md mt-sm">

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **A staged edit, then a push**

```text
$ git status --short
M  README.md
$ git push
Everything up-to-date
```

The edit is staged, not committed: `push` sends commits only.

</div>

<div class="card card-primary card-glass pad-compact">

## 📦 **What the first push sent**

- The 8 commits GitHub lacked, under the same ids
- The files of those commits, compressed: 554 KiB
- Nothing of the working folder or the staging area, no ignored file

</div>

</div>

<!--
**Say:** `push` copies commits from the repository on the laptop to the one on GitHub. A later push sends only the commits GitHub lacks.
**If asked:** the staged edit was one line, "Draft: the wind column.", taken back with `git restore --staged README.md`, then `git restore README.md`.
(~3 min)
-->

---
hideInToc: true
---

# Where the Change Is After Each Step

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| After | The change is in | Who sees it | If the laptop is lost |
| --- | --- | --- | --- |
| Saving the file | the working folder | you | gone |
| `git add` | also the staging area | you | gone |
| `git commit` | also the repository, `.git`, with who, when and why | you | gone |
| `git push` | also the repository on GitHub | everyone with access | kept on GitHub |

</div>

<div class="card card-info card-glass pad-compact mt-md">

Commit whenever one step of work is done, push when you stop for the day: then the history is on two computers.

</div>

<!--
**Ask:** which step makes a change safe from a lost laptop? Only the push. Which makes it possible to bring back? The commit.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Working **Together**

Two ways to share one history: everyone pushes to one repository, or each works in a fork and asks.

<!--
**Say:** Tomas works with Smiltė every day: he gets write access. Rūta, at another university, does not: she forks.
(~1 min)
-->

---
hideInToc: true
---

# Two Ways to Work Together

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🤝 **One shared repository**

<img src="/figures/git_ways_shared.svg" style="max-width:100%;display:block;margin:0.3rem auto 0;max-height:205px;">

Both push to it. For a group that works together every day: a lab, a thesis with its supervisor.

</div>

<div class="card card-primary card-glass pad-compact">

## 🍴 **Fork and pull request**

<img src="/figures/git_ways_fork.svg" style="max-width:100%;display:block;margin:0.3rem auto 0;max-height:205px;">

Rūta pushes to her copy and asks; Smiltė merges. For anyone else: open-source projects, ROOT and NumPy among them.

</div>

</div>

<div class="note-text mt-sm"><code>clone</code>: the first copy, down. <code>pull</code>: the others' new commits, down. <code>push</code>: your commits, up.</div>

<!--
**Say:** on the left, two people push to one repository. On the right, Rūta's commits reach Smiltė's repository only when Smiltė accepts them.
(~2 min)
-->

---
hideInToc: true
---

# Invite a **Collaborator**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🤝 **On `github.com`, in Smiltė's repository**

1. **Settings**, then **Collaborators** in the list on the left
2. **Add people**, type Tomas's user name, select him
3. GitHub sends Tomas an invitation; he accepts it in the e-mail or on GitHub

</div>

<div class="card card-secondary card-glass pad-tight">

## ✍️ **What Tomas may do then**

- See the private repository and clone it
- Push his commits to it, as Smiltė does
- Anyone not invited does not see a private repository at all

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A collaborator writes to the same history. Every commit still carries its author, so the history says which of the two made each change.

</div>

<!--
**Say:** Smiltė and Tomas now share one repository on GitHub, and each has a copy on the laptop.
**If asked:** the free plan allows any number of collaborators, on private repositories too.
(~2 min)
-->

---
hideInToc: true
---

# Clone on a Second **Computer**

<img src="/figures/git_remote_clone.svg" style="max-width:100%;display:block;margin:0.3rem auto 0;max-height:185px;">

<div class="grid-2 gap-md mt-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 📥 **Tomas clones the project**

````md magic-move
```text
$ git clone https://github.com/smilte-example/weather-project.git
Cloning into 'weather-project'...
...
```
```text
$ git clone https://github.com/smilte-example/weather-project.git
Cloning into 'weather-project'...
...
$ cd weather-project
$ git log --oneline -1
2eb3b1c (HEAD -> main, origin/main, origin/HEAD) Revert "Remove …"
```
````

</div>

<div class="card card-info card-glass pad-compact">

The clone has every commit, under the same ids, and every committed file. Tomas commits in it as on any repository, and his pushes reach Smiltė's repository on GitHub.

</div>

</div>

<!--
**Say:** the picture is the whole setup: Smiltė's laptop, GitHub, Tomas's laptop, each with the same history.
**If asked:** `origin/HEAD` is the remote's default branch, recorded by the clone. The last line is cut with … here.
(~3 min)
-->

---
hideInToc: true
---

# Pull: Fetch What Is **New**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Tomas changes line 2 of the export to 6,4, commits, pushes**

```text
$ git add data/raw/daily_export.csv
$ git commit -m "Correct 1 October to 6,4" -m "The station's paper log says 6,4 for 1 October 2025."
[main f2546ed] Correct 1 October to 6,4
...
$ git push
...
   2eb3b1c..f2546ed  main -> main
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## ⬇️ **Smiltė pulls**

```text
$ git pull
...
Fast-forward
 data/raw/daily_export.csv | 2 +-
...
```

</div>

<div class="note-text mt-sm">A second <code>-m</code> adds the why below the first line. <code>git pull</code> brings Tomas's commit to Smiltė's laptop and into her files. Pull before you start to work, push when you stop.</div>

<!--
**Say:** a second `-m` gives the message a body, below an empty line: the reason. `2eb3b1c..f2546ed` is the old and the new last commit.
**Ask:** this is the change of the two copies at the start. Should a raw file change at all? No: `data/raw` holds the files as they arrived; a value from the paper log goes into the README, with its source.
(~3 min)
-->

---
hideInToc: true
---

# Both Commit, the Second Push Is **Refused**

<div class="card card-info card-glass pad-compact mt-sm">

Tomas rewords lines 3 and 4 of the README, commits `7abaa0d` and pushes. Smiltė has not pulled since; she rewrites the same two lines.

</div>

<div class="grid-2 gap-md mt-sm" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 💻 **Smiltė**

```text
$ git add README.md
$ git commit -m "Give the number of hours in the first paragraph"
[main 94dccdc] Give the number of hours in the first paragraph
...
$ git push
To https://github.com/smilte-example/weather-project.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '…'
...
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔀 **The two histories**

<img src="/figures/git_refused.svg" style="max-width:100%;display:block;margin:0.4rem auto 0;">

</div>

</div>

<div class="note-text mt-sm">A push may only add commits on top of what GitHub has. It never throws away Tomas's commit: first <code>git pull</code>, then push.</div>

<!--
**Say:** nothing is broken and nothing is lost. Git refuses: GitHub's `main` has a commit this laptop lacks, and pushing would drop it.
**If asked:** the cut lines are hints; the fourth says to use `git pull` before pushing again.
(~3 min)
-->

---
hideInToc: true
---

# Pull Fetches Tomas's Commit and **Merges**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Smiltė**

```text
$ git pull --no-edit
...
From https://github.com/smilte-example/weather-project
   f2546ed..7abaa0d  main       -> origin/main
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

</div>

<img src="/figures/git_pull.svg" style="max-width:100%;display:block;margin:0.6rem auto 0;max-height:150px;">

<div class="note-text mt-sm">Changes to different lines Git joins by itself, and the push goes through. Here both changed lines 3 and 4: a <strong>conflict</strong>. <code>--no-edit</code> keeps the proposed message, without an editor.</div>

<!--
**Say:** most pulls end without a question. A conflict means two people changed the same lines, and Git will not guess which text is meant.
**If asked:** without a conflict the answer says `Merge made by the 'ort' strategy.`, then the files changed.
(~3 min)
-->

---
hideInToc: true
---

# A Merge **Conflict**

<div class="card card-warning card-glass pad-compact mt-md">

```text
$ git status --short
UU README.md
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 📄 **`README.md` now**

<pre class="slidev-code conflict-block"><code># Weather Station

&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
The hourly log of one weather station, 2016 to 2025, 87 672 hours, and a
table of daily mean temperatures typed into a spreadsheet from it.
=======
Ten years of hourly readings from one weather station, and the daily
means of nine days of October 2025, typed into a spreadsheet from them.
&gt;&gt;&gt;&gt;&gt;&gt;&gt; 7abaa0dce0209145f5c805bb6c19e75d601ff051</code></pre>

Above `=======` Smiltė's lines (`HEAD`, her own commit), below Tomas's, named by his commit's id. Nothing is lost, and nothing is decided.

</div>

<!--
**Say:** a conflict is no error. Git writes both versions into the file and asks a person. `UU` means changed by both, not merged yet.
(~2 min)
-->

---
hideInToc: true
---

# Resolve It in the **Editor**

<div class="text-center mt-sm">

<img src="/figures/git_weather_conflict.png" style="max-height: 230px; display: inline-block; border-radius: 6px; border: 1px solid var(--hair);">

</div>

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

**1.** In Source Control the file stands under **Merge Changes**, marked `!`. Open it.

</div>

<div class="card card-secondary card-glass pad-compact">

**2.** Above the block: **Accept Current Change**, **Accept Incoming Change**, **Accept Both Changes**. Or edit the lines. The markers must go.

</div>

<div class="card card-success card-glass pad-compact">

**3.** **+** stages the file. **Continue** makes the merge commit; its message is already filled in.

</div>

</div>

<!--
**Say:** here Tomas's lines are accepted and "87 672 hours" is added by hand. The result has something of both, the usual case.
(~2 min)
-->

---
hideInToc: true
---

# Resolve, Commit, Push

<div class="card card-secondary card-glass pad-compact mt-sm">

## 📄 **`README.md` after the edit: both versions joined, no marker left**

```text
Ten years of hourly readings from one weather station, 87 672 hours, and
the daily means of nine days of October 2025, typed into a spreadsheet
from them.
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

```text
$ git add README.md
$ git commit --no-edit
[main 6dd93ad] Merge branch 'main' of https://…
$ git push
...
   7abaa0d..6dd93ad  main -> main
```

</div>

<div class="card card-info card-glass pad-compact">

## 🔀 **The history now**

<img src="/figures/git_merged.svg" style="max-width:100%;display:block;margin:0.3rem auto 0;max-height:150px;">

</div>

</div>

<!--
**Say:** `git add` tells Git the conflict is settled, the commit closes the merge. A merge commit has two commits before it: the two lines that join in the graph. Now the push goes through, and Tomas gets the merge with his next pull.
**If asked:** the first line of the message is `Merge branch 'main' of https://github.com/smilte-example/weather-project`; below it Git lists the file that had the conflict. `git log --oneline --graph` draws the same history with `*`, `|` and `/`. `git merge --abort` puts everything back as before the pull.
(~3 min)
-->

---
hideInToc: true
---

# Fork: Your Own Copy on **GitHub**

<div class="card card-info card-glass pad-compact mt-sm">

Smiltė's repository is public since her report came out. Rūta, at another university, has the range of every column and wants it in the README. She may read the repository, not push to it.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🍴 **On `github.com/smilte-example/weather-project`**

1. **Fork**, at the top right of the page
2. Owner: her own account; the name stays `weather-project`
3. **Create fork**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📂 **`github.com/ruta-example/weather-project`**

- Every commit of Smiltė's, under the same ids
- Rūta may push to it, and nobody else has to agree
- Its page reads *forked from smilte-example/weather-project*

</div>

</div>

<!--
**Say:** a fork is a clone that GitHub makes, on GitHub, under Rūta's name. Smiltė's repository does not change and is not asked.
**If asked:** Settings, then **Change visibility** at the bottom of the General page, makes a private repository public.
(~2 min)
-->

---
hideInToc: true
---

# Clone the Fork, Make a **Branch**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **Rūta**

````md magic-move
```text
$ git clone https://github.com/ruta-example/weather-project.git
Cloning into 'weather-project'...
...
```
```text
$ git clone https://github.com/ruta-example/weather-project.git
Cloning into 'weather-project'...
...
$ cd weather-project
$ git switch -c ranges
Switched to a new branch 'ranges'
```
````

</div>

<div class="card card-secondary card-glass pad-compact">

## 🖱️ **In VS Code**

<img src="/figures/git_vscode_branch.png" style="width:100%; border-radius: 6px; border: 1px solid var(--hair);">

The branch name at the left of the Status Bar, then **Create new branch...**, `ranges`, Enter.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **branch** is a separate line of commits. A pull request proposes one branch, so Rūta's commits go to `ranges` and her `main` stays equal to Smiltė's.

</div>

<!--
**Say:** Rūta clones her fork, not Smiltė's repository: `origin` is then the fork, the one repository she may push to.
**If asked:** `git branch` lists the branches and marks the one in use with `*`.
(~2 min)
-->

---
hideInToc: true
---

# Commit on the Branch, Push It to the **Fork**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Rūta, after adding a column Range to the README's table of columns**

```text
$ git add README.md
$ git commit -m "Give the range of each column"
[ranges 6e10712] Give the range of each column
 1 file changed, 6 insertions(+), 6 deletions(-)
$ git push -u origin ranges
...
remote: Create a pull request for 'ranges' on GitHub by visiting:
remote:      https://github.com/ruta-example/weather-project/pull/new/ranges
...
 * [new branch]      ranges -> ranges
branch 'ranges' set up to track 'origin/ranges'.
```

</div>

<div class="note-text mt-sm">Here <code>origin</code> is Rūta's fork, the one repository she may push to. <code>-u origin ranges</code> sends the new branch there. Lines that begin with <code>remote:</code> are written by GitHub.</div>

<!--
**Say:** nothing has reached Smiltė yet. The commit is in Rūta's fork, on the branch `ranges`.
**If asked:** the ranges, -16.3 to 32.4 °C, 34 to 100 % and 0.0 to 12.0 m/s, are the minimum and maximum of the valid rows.
(~2 min)
-->

---
hideInToc: true
---

# Open a Pull **Request**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-tight">

## 🌐 **On `github.com`, as Rūta**

1. The yellow banner *ranges had recent pushes*: **Compare & pull request**
2. Check the line: `smilte-example/weather-project`, `main` ← `ruta-example/weather-project`, `ranges`
3. Title: the commit message. Below it: what changed and why
4. **Create pull request**

</div>

<div class="card card-secondary card-glass pad-tight">

## 📨 **What Smiltė receives**

- Pull request **#1** in her repository: merge `ranges` of the fork into `main`
- Its tabs: **Conversation**, **Commits**, **Checks**, **Files changed** (the diff)
- A commit Rūta pushes to `ranges` later joins the request

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **pull request** asks the owner to take a branch in. Nobody types `git pull` for it: discussion, review and the merge happen on its page on GitHub.

</div>

<!--
**Say:** the arrow `←` reads "into ← from": into Smiltė's `main`, from Rūta's `ranges`.
**If asked:** GitHub also offers **Allow edits from maintainers** (on a fork with workflows: *Allow edits and access to secrets by maintainers*): Smiltė may then push small fixes to Rūta's branch herself.
(~3 min)
-->

---
hideInToc: true
---

# Review and Merge the Pull **Request**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🔎 **On `github.com`, as Smiltė**

**Pull requests**, then **#1**. **Files changed** shows the diff: a comment on a line, or **Review changes**, **Approve**, **Submit review**. At the bottom of **Conversation**: **Merge pull request**, then **Confirm merge**.

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 💻 **Then on Smiltė's laptop**

```text
$ git pull
...
Fast-forward
 README.md | 12 ++++++------
...
```

<img src="/figures/git_pr_merged.svg" style="max-width:100%;display:block;margin:0.6rem auto 0;max-height:120px;">

</div>

<!--
**Say:** GitHub made the merge commit `2c8f8b0`, with Smiltė as author; `6e10712` keeps Rūta as its author. Smiltė's `git pull` only moves `main` forward: a fast-forward.
**If asked:** Rūta updates her fork with **Sync fork**, then **Update branch** on its page, and on her laptop `git switch main`, then `git pull`. Smiltė may also refuse: **Close pull request**, with a comment that says why.
(~3 min)
-->

---
hideInToc: true
---

# A Shared Repository or a **Fork**

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| | Shared repository | Fork and pull request |
| --- | --- | --- |
| Who pushes to Smiltė's repository | Smiltė and every collaborator she invited | Smiltė and her collaborators. Rūta pushes to her fork |
| How a change arrives | `git push` | A pull request, merged by someone who may push |
| Read by someone else before `main` changes | Only if the group agrees on it | Always: the request waits |
| For | A lab, a thesis, a course team | Anyone else: open source, another group |

</div>

<div class="card card-info card-glass pad-compact mt-md">

Inside a shared repository the same review works: push a branch, open a pull request from it into `main`. Many groups never push to `main` directly.

</div>

<!--
**Ask:** you find a wrong unit in the README of a package you use. Which way? A fork and a pull request: you cannot push there.
(~2 min)
-->

---
hideInToc: true
---

# Every Step, in Source Control and **Typed**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Step | In Source Control | Typed |
| --- | --- | --- |
| Create the repository | **Initialize Repository** | `git init` |
| See what changed | The **Changes** list. Select a file for its diff | `git status`, `git diff` |
| Stage, unstage | **+**, **−** | `git add <file>`, `git restore --staged <file>` |
| Commit | Message, then **Commit** | `git commit -m "…"` |
| Discard an edit | **Discard Changes** | `git restore <file>` |
| Read the history | **Graph** | `git log --oneline` |
| Take back a commit | No button: typed | `git revert <id>` |
| Send and fetch | **Sync Changes** | `git push`, `git pull` |
| New branch | Branch name in the Status Bar | `git switch -c <name>` |
| Propose a change | On `github.com`: **Fork**, **Compare & pull request** | `git push -u origin <branch>`, then on `github.com` |

</div>

<div class="note-text mt-sm">A working day: pull, edit, read the diff, stage, commit with a message that says why, push.</div>

<!--
**Say:** the left column is what the room clicks, the right what it types; both run the same Git.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# A Result and Its **Commit**

The question of the two copies, answered from the history alone.

<!--
**Say:** back to the start: one line of the raw export differs. Who changed it, when, and why?
(~1 min)
-->

---
hideInToc: true
---

# Who Changed the Raw **Export**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git log --oneline -- data/raw
f2546ed Correct 1 October to 6,4
2eb3b1c Revert "Remove the raw export, daily.csv replaces it"
172f06a Remove the raw export, daily.csv replaces it
a9f65a6 Add the data and the scripts
```
```text
$ git log --oneline -- data/raw
f2546ed Correct 1 October to 6,4
2eb3b1c Revert "Remove the raw export, daily.csv replaces it"
172f06a Remove the raw export, daily.csv replaces it
a9f65a6 Add the data and the scripts
$ git blame -L 2,2 data/raw/daily_export.csv
f2546ed (Tomas 2026-10-20 11:30:00 +0300 2) 1;2025-10-01;6,4
```
````

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 📜 **`git log -- data/raw`**

Only the commits that changed something in `data/raw`. A folder of files that are never edited should have one: the commit that added them. Here it has four.

</div>

<div class="card card-info card-glass pad-compact">

## 🔎 **`git blame -L 2,2`**

For each line, the commit that last changed it, with its author and time. Line 2 of the export, `6,4`, comes from `f2546ed`, by Tomas, at 11:30.

</div>

</div>

<!--
**Ask:** which of these four changed line 2? The newest: the other three added the file, deleted it and brought it back.
**If asked:** in VS Code the Status Bar shows the author and age of the commit behind the line the cursor is in.
(~3 min)
-->

---
hideInToc: true
---

# Read Tomas's Commit **Line by Line**

<div class="grid-2 gap-md mt-sm" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git show f2546ed
commit f2546ed4cd7ed6d64259cacbd6d0d6e2532203ca
Author: Tomas <tomas@example.org>
Date:   Tue Oct 20 11:30:00 2026 +0300
...
```
```text
$ git show f2546ed
commit f2546ed4cd7ed6d64259cacbd6d0d6e2532203ca
Author: Tomas <tomas@example.org>
Date:   Tue Oct 20 11:30:00 2026 +0300

    Correct 1 October to 6,4

    The station's paper log says 6,4 for 1 October 2025.
...
```
```text
$ git show f2546ed
commit f2546ed4cd7ed6d64259cacbd6d0d6e2532203ca
Author: Tomas <tomas@example.org>
Date:   Tue Oct 20 11:30:00 2026 +0300

    Correct 1 October to 6,4

    The station's paper log says 6,4 for 1 October 2025.
...
 nr;date;temp_c
-1;2025-10-01;6,3
+1;2025-10-01;6,4
...
```
````

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 🧾 **The questions of the start**

| Question | Answer |
| --- | --- |
| Which line? | Line 2, `6,3` to `6,4` |
| Who? | Tomas |
| When? | 20 October, 11:30 |
| Why? | The paper log, in the message body |

</div>

</div>

<!--
**Do:** point at the table of "Two Copies of the Export", slide 4, then at Author, Date and the message here.
**Say:** `git show` prints one commit: who, when, the message, then the diff of what it changed. The cut lines are the diff's header and the lines around the change.
(~3 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Say what a history keeps that copies do not: who, when and **why**

</div>

<div class="card card-success card-glass pad-compact">

✅ Say where `git add`, `git commit` and `git push` put a change, and who sees it then

</div>

<div class="card card-success card-glass pad-compact">

✅ Keep made files out with `.gitignore`

</div>

<div class="card card-success card-glass pad-compact">

✅ Read a **diff** and the history, and undo an edit or a commit

</div>

<div class="card card-success card-glass pad-compact">

✅ Share one repository: clone, pull, push, and resolve a **conflict**

</div>

<div class="card card-success card-glass pad-compact">

✅ Propose a change to someone else's project: a **fork** and a **pull request**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **A result and its commit**

A number that leaves the project carries the id of the commit that made it. With the id, the files behind the result come back exactly.

</div>

<!--
**Do:** go through the six cards; let the room nod or object.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# For the **Curious**

How Git keeps every version: under a name computed from its bytes.

<!--
**Say:** shown only if time is left, or read after the lecture. Nothing before this slide needs it.
(~1 min)
-->

---
hideInToc: true
---

# What Has to Be **Kept**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **One version of the project**

- The bytes of every file
- The path of every file, such as `data/raw/weather.csv`
- Which version came before it
- Who made it, when, and why

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗂️ **The obvious way: copy the folder**

```text
weather-project_2026-10-13/
weather-project_2026-10-20/
weather-project_2026-10-20_fixed/
```

The folder holds 5.03 MB, nearly all of it the four data files. Fifteen copies take 75.5 MB, with the same data in each.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Git keeps the same four things and stores each content once. The tool is a checksum, as in Lecture 4: a short number computed from all the bytes of a content.

</div>

<!--
**Say:** a copied folder has the first two items and loses the last two. The two copies of the export were exactly this case.
**If asked:** 2 515 215 + 180 bytes in `data/raw`, 2 511 735 + 148 in `data/processed`; 15 × 5 032 295 bytes = 75.5 MB.
(~2 min)
-->

---
hideInToc: true
class: live
---

# A Name Made from the **Content**

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ echo "hello" | git hash-object --stdin
ce013625030ba8dba906f756967f9e9ca394464a
$ echo "hallo" | git hash-object --stdin
4cf5aa5f9a644263dbe3d6e78bcbef45487a802c
$ printf "hello\r\n" | git hash-object --stdin
ef0493b275aa2080237f676d2ef6559246f56636
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

## 📏 **What the number is**

- 40 hex digits are 160 bits. The hash is **SHA-1**, an older relative of the SHA-256 of Lecture 4, which has 64 digits
- One changed letter changes the whole number
- Git calls the number the **id** of the content, and stores the content under it

</div>

<div class="card card-warning card-glass pad-compact">

## 🔀 **The same word, another ending**

`printf` writes `hello` with `\r\n`, the line ending of Windows programs: `ef0493b2…`. The word is the same, so the bytes that reached Git must differ.

</div>

</div>

<!--
**Live:** `echo "hello" | git hash-object --stdin` on the lecture laptop.
**Ask:** read the first four digits to your neighbour: ce01 on every laptop, Mac or Windows.
(~3 min)
-->

---
hideInToc: true
---

# What Git **Hashes**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
62 6c 6f 62 20 36 00 68 65 6c 6c 6f 0a          echo: 13 bytes
b  l  o  b     6     h  e  l  l  o  LF

62 6c 6f 62 20 37 00 68 65 6c 6c 6f 0d 0a       printf "hello\r\n": 14 bytes
b  l  o  b     7     h  e  l  l  o  CR LF
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 🧾 **A header, then the bytes**

The header is the word `blob`, a space, the number of bytes as decimal text, and one zero byte. A **blob** is Git's word for the content of a file. The id is the SHA-1 of the header and the content together.

</div>

<div class="card card-accent card-glass pad-compact">

## ↩️ **Where the 7 comes from**

`echo` ends the text with `0a`: 6 bytes. `printf` was told to write `0d 0a`, the ending a Windows program such as Notepad writes: 7 bytes. Other bytes, so another id.

</div>

</div>

<div class="note-text mt-sm">Read the bytes with the ASCII table of Lecture 3: 62 is b, 20 the space, 36 the digit 6, 37 the digit 7.</div>

<!--
**Say:** the id is no secret of Git. It is a SHA-1 of bytes that can be written down; the size in the header is 6 or 7.
(~3 min)
-->

---
hideInToc: true
class: live
---

# The Data File Has an **Id**

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash: the same id on every laptop**

```text
$ git hash-object data/raw/weather.csv
f811f73d93226acc8a0c96562aef9f7825b85b0a
$ shasum -a 256 data/raw/weather.csv
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 💻 **Bytes as they are**

Git hashes `blob 2515215`, a zero byte, then the 2 515 215 bytes of the file. A file is read as it is, so nothing is added. A copy under another name has the same id: name and date are not hashed.

</div>

<div class="card card-success card-glass pad-compact">

## 🗜️ **Stored once, compressed**

`git add` keeps the blob in `.git/objects/f8/`, in a file named by the other 38 digits. That file has 722 938 bytes: Git compresses with DEFLATE, the method of zip.

</div>

</div>

<!--
**Live:** `git hash-object data/raw/weather.csv` in the project folder.
**Ask:** read the first six digits aloud: f811f7 on every laptop. A laptop with another number has another file.
**Say:** the SHA-256 of Lecture 4 is another function of the same bytes.
(~2 min)
-->

---
hideInToc: true
---

# A Folder Is a **List**

<div class="card card-secondary card-glass pad-compact mt-sm">

## 📋 **The checksums of `data/raw`, as in Lecture 4**

```text
$ shasum -a 256 data/raw/*
9d849815d88eceb18366ee66ac72f26b72e195bea8bb20aa9a1474372513bbdb  data/raw/daily_export.csv
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
```

</div>

<div class="card card-primary card-glass pad-compact mt-md">

## 🌳 **The list Git keeps for `data/raw`**

```text
$ git cat-file -p ee85972a
100644 blob 0799b86b8920dc0305f14957ed806fbaa6b29107    daily_export.csv
100644 blob f811f73d93226acc8a0c96562aef9f7825b85b0a    weather.csv
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

Git's list of a folder is a **tree**: one line per file, a mode, the kind, the blob id and the name. `100644 blob` is an ordinary file. The tree is itself content, so it has an id of its own: `ee85972a…`.

</div>

<!--
**Say:** both lists hold one hash and one name per file, in the order of the names. Git adds the mode and the kind.
**If asked:** `git cat-file -p` prints any object in readable form. The `data/raw` tree is the same on every laptop with the same two files.
(~2 min)
-->

---
hideInToc: true
---

# The Tree of the Whole **Project**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ git cat-file -p b9c01664
100644 blob f6a280d35eb8d7399aca4d204531729eb933e40e    .gitattributes
100644 blob 3febadb2ecf24b916a6e8b06b61a44ac77965e79    .gitignore
100644 blob 5b35420e27065df77187c89dd7602163cf8a2e80    README.md
040000 tree d87619c94923e48458c24349ca078fdf304b68e5    data
040000 tree d824278b278d8646a317896458a16a1b99f5b734    scripts
$ git cat-file -p d87619c9
040000 tree ee85972aa77240166e830bd65e5514b032637fd5    raw
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 📂 **A subfolder is a tree**

A line `040000 tree` names the list of a subfolder. The top list names `data`, and `data` names `raw`, the list of the slide before.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔗 **One id for the whole project**

Change one byte of `weather.csv`: its blob id changes, so the list of `raw` changes, then `data`, then the top list. `b9c01664` fixes every byte and every name.

</div>

</div>

<!--
**Say:** `data/processed` has no line here: `.gitignore` keeps it out. An empty folder has no entry either.
(~2 min)
-->

---
hideInToc: true
---

# A **Commit**

<div class="card card-primary card-glass pad-compact mt-md">

```text
$ git cat-file -p a9f65a6
tree b9c0166494b823a041989ceb23623d62173d923d
parent ef28e402d742c44c8c0a708e035794228ec32a2e
author Smiltė <smilte@example.org> 1792481100 +0300
committer Smiltė <smilte@example.org> 1792481100 +0300

Add the data and the scripts
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

- `tree`: the snapshot, as the id of the top list
- `parent`: the commit that came before
- `author`: who, and when. 1 792 481 100 seconds after 1 January 1970 is 20 October 2026, 10:25, at UTC+3

</div>

<div class="card card-info card-glass pad-compact">

The last line is the message: why. A commit is these 233 bytes of text. It holds no file and no difference between files. It points to a complete snapshot.

</div>

</div>

<!--
**Say:** the four things of "What Has to Be Kept" are all here: bytes and paths through the tree, the version before through the parent, who, when and why in the text itself.
(~2 min)
-->

---
hideInToc: true
---

# One Commit, Drawn

<div class="mt-sm" style="display: flex; justify-content: center;">

<img src="/figures/git_commit_tree.svg" style="max-width:100%;display:block;margin:0 auto;max-height:330px;">

</div>

<div class="note-text mt-sm">Every arrow is an id written inside the object it starts from. <code>.gitattributes</code> and the two Python scripts are left out of the drawing.</div>

<!--
**Say:** follow one path from the commit to `weather.csv`: four ids, each computed from the one below it.
**Ask:** which boxes get a new id if one byte of `weather.csv` changes? All on the path to it, and the commit.
(~3 min)
-->

---
hideInToc: true
---

# The Id of a **Commit**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ git cat-file -s a9f65a6
233
$ git cat-file commit a9f65a6 | git hash-object -t commit --stdin
a9f65a6cc855739979919aae1a861f1a0bc8d58e
```

The recipe of the blob, with `commit 233` and a zero byte as the header.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 🔒 **What the id fixes**

The hashed text holds the id of the tree and the id of the parent. So one commit id fixes every file of this version and every version before it.

</div>

<div class="card card-accent card-glass pad-compact">

## 📌 **Consequences**

- An old version cannot be changed unnoticed: every later id would change
- A corrected message gives another id: `--amend` makes a new commit
- The same files committed by two people give one tree and two commit ids: name and time differ

</div>

</div>

<!--
**Say:** -s prints the size, -t commit puts the word commit in the header. Seven digits are enough to name a commit.
**If asked:** 233 bytes for 231 characters: the ė of Smiltė takes two bytes in UTF-8, and it appears twice.
(~3 min)
-->

---
hideInToc: true
---

# History Is a **Graph**

<div class="mt-sm" style="display: flex; justify-content: center;">

<img src="/figures/git_history.svg" style="max-width:100%;display:block;margin:0 auto;max-height:180px;">

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

Every commit names its parent. The first has none, a merge has two. The arrows point back in time: from one commit the whole past can be reached, and nothing that came after it.

</div>

<div class="card card-secondary card-glass pad-compact">

Each commit has its own tree, a complete snapshot. Snapshots share every blob that did not change: `README.md` is blob `5b35420e…` in all four.

</div>

</div>

<!--
**Say:** the four commits of Tracking Changes, each naming the one before it.
(~2 min)
-->

---
hideInToc: true
---

# A Branch Is a Name for a **Commit**

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **A file of 41 bytes**

```text
$ cat .git/HEAD
ref: refs/heads/main
$ cat .git/refs/heads/main
a9f65a6cc855739979919aae1a861f1a0bc8d58e
```

<img src="/figures/git_branch_a.svg" style="max-width:100%;display:block;margin:0.6rem auto 0;max-height:110px;">

</div>

<div class="card card-secondary card-glass pad-compact">

## ➡️ **A commit moves the name**

```text
$ git add README.md
$ git commit -m "Give the mean temperature in the README"
[main 15505c4] Give the mean temperature in the README
...
$ cat .git/refs/heads/main
15505c482d25129590a630d023046267f7abb020
```

<img src="/figures/git_branch_b.svg" style="max-width:100%;display:block;margin:0.6rem auto 0;max-height:110px;">

</div>

</div>

<div class="note-text mt-sm"><code>HEAD</code> says which branch is in use. A second branch is a second file of 41 bytes: no file of the project is copied.</div>

<!--
**Do:** on the board, draw the four commits, write "main" beside the newest, and move it when you draw a fifth.
**Say:** the word branch suggests a line of commits. What Git stores is one name on one commit.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# More **Commands**

Rebuild a clone, take back Tomas's edit and name the version, the map of every command, and a few details.

<!--
**Say:** shown only if time is left, or read after the lecture.
(~1 min)
-->

---
hideInToc: true
---

# Rebuild What the Clone **Lacks**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash, in Tomas's clone**

````md magic-move
```text
$ ls data
raw
```
```text
$ ls data
raw
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
```
```text
$ ls data
raw
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ ls data
processed  raw
```
````

</div>

<div class="card card-info card-glass pad-compact">

## ♻️ **The ignored folder comes back**

`data/processed` is not in the clone: Git stores files, not folders, and this folder was ignored. Line 3 of `rebuild.sh`, `mkdir -p data/processed`, makes the folder; the next two lines fill it.

</div>

</div>

<!--
**Ask:** where do the two made files come from on Tomas's laptop? From the raw files and the script, both in the repository.
(~2 min)
-->

---
hideInToc: true
---

# The Edit Changes the **Result**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ shasum -a 256 data/processed/daily.csv
58709abc8e3c698e4dd32feb2dae7db128d29138c6c1883d1f08f46fb40d36b1  data/processed/daily.csv
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-compact">

## ❌ **Not the promised file**

The README promises `daily.csv` with SHA-256 `33fe5e77…f705483d`. With `6,4` the rebuild gives `58709abc…fb40d36b`: the cleaned copy of the export with `6,4`.

</div>

<div class="card card-info card-glass pad-compact">

## 📁 **Where the paper log belongs**

`data/raw` holds the files as they arrived. A value from another source goes into the README, as a note with its source, and the raw file stays as it came.

</div>

</div>

<!--
**Say:** Tomas may well be right about the paper log. The fault is the place: a raw file edited in place breaks the checksum and hides what the station sent.
(~2 min)
-->

---
hideInToc: true
---

# Take It Back and **Check**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git revert --no-edit f2546ed
[main 4119ca1] Revert "Correct 1 October to 6,4"
...
```
```text
$ git revert --no-edit f2546ed
[main 4119ca1] Revert "Correct 1 October to 6,4"
...
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ shasum -a 256 data/processed/daily.csv
33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
```
```text
$ git revert --no-edit f2546ed
[main 4119ca1] Revert "Correct 1 October to 6,4"
...
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ shasum -a 256 data/processed/daily.csv
33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
$ git push
...
   2c8f8b0..4119ca1  main -> main
```
````

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ Tomas's commit stays in the history, with its reason, and so does the revert. The rebuilt file has the checksum of the README again.

</div>

<!--
**Say:** revert, not amend: the commit was pushed and Tomas has it. Amend would give Smiltė and Tomas two different histories.
(~2 min)
-->

---
hideInToc: true
---

# A Tag Names a **Version**

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ git tag -a v1.0 -m "Data as received; mean 7.16 °C"
```
```text
$ git tag -a v1.0 -m "Data as received; mean 7.16 °C"
$ git log --oneline -2
4119ca1 (HEAD -> main, tag: v1.0, origin/main, origin/HEAD) Revert "Correct 1 October to 6,4"
2c8f8b0 Merge pull request #1 from ruta-example/ranges
```
```text
$ git tag -a v1.0 -m "Data as received; mean 7.16 °C"
$ git log --oneline -2
4119ca1 (HEAD -> main, tag: v1.0, origin/main, origin/HEAD) Revert "Correct 1 October to 6,4"
2c8f8b0 Merge pull request #1 from ruta-example/ranges
$ git push origin v1.0
...
 * [new tag]         v1.0 -> v1.0
```
````

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

## 🏷️ **A name that does not move**

A branch name moves with every commit. The tag `v1.0` stays on `4119ca1`. `-a` stores who set it, when, and a message. A tag is pushed by its name.

</div>

<div class="card card-success card-glass pad-compact">

## ♻️ **Which files made this number?**

Tag the commit behind every result that leaves the project: a mean in an e-mail, a figure in a thesis. `git switch --detach v1.0` brings those files back (`git status` then says `HEAD detached at v1.0`), `git switch main` returns.

</div>

</div>

<!--
**Say:** the 7.16 of Lecture 1, sent as one number, now comes with a name that fixes every file behind it.
(~2 min)
-->

---
hideInToc: true
---

# Where Each Command Moves a **Change**

<div class="mt-sm" style="display: flex; justify-content: center;">

<img src="/figures/git_flow.svg" style="max-height: 360px; max-width: 100%;">

</div>

<div class="note-text mt-sm"><code>git pull</code> is two steps: <code>git fetch</code> brings the new commits from the remote into the repository, <code>git merge</code> joins them with the branch in use and so into the files.</div>

<!--
**Say:** one map of the lecture: the working folder, the staging area, the repository on the laptop, the remote. `add` and `commit` go right, `push` crosses to GitHub, `pull` comes back: `fetch` brings the commits, `merge` puts them into the files.
**Ask:** where on this map is `git restore`? From the staging area back to the working folder; with nothing staged, that is the last commit.
**If asked:** `git commit -a` stages every tracked file and commits in one step. Other books call the staging area the *index*.
(~2 min)
-->

---
hideInToc: true
---

# Which Data Files Fit in a **Repository**

<div class="grid-2 gap-md mt-md">

<div class="card card-success card-glass pad-tight">

## ✅ **`weather.csv`, 2 515 215 bytes**

- Git keeps each content once, compressed: 722 938 bytes
- By the end of this lecture: 15 commits, and `.git` takes 0.77 MB. The data file never changed, so it was kept once
- Fifteen copies of the folder, one per commit, would take 75.5 MB
- The first push sent 554 KiB

</div>

<div class="card card-warning card-glass pad-tight">

## ❌ **One file of 3 GB**

- GitHub refuses a file above 100 MB and warns above 50 MB
- A changed line gives a second version of the whole file
- Every copy of the repository carries every version of every file
- A commit cannot be removed later without rewriting every commit after it

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A file that stays out is still on the disk. Git is told to ignore it, and the README says where it comes from or which script makes it.

</div>

<!--
**Say:** the numbers on the left are measured on the lecture project. Each commit names the one before it, so taking one out changes every commit after it.
**If asked:** the folder holds 5.03 MB; fifteen copies are 15 × 5 032 295 bytes = 75.5 MB.
(~3 min)
-->

---
hideInToc: true
---

# The Same Bytes on Every Laptop: **`.gitattributes`**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`.gitattributes`**

```text
# Check out every file with the bytes it was committed with:
# no CRLF line endings on Windows, the same checksums on every laptop.
* -text
```

```text
$ git add .gitattributes
$ git commit -m "Keep the committed bytes of every file on checkout"
[main ef28e40] Keep the committed bytes of every file on checkout
...
```

</div>

<div class="card card-warning card-glass pad-compact">

## 🪟 **Without it, on Windows**

`core.autocrlf false` acts only on the laptop where it was typed. Git for Windows comes with `true`, and there a clone gets `0d 0a` at the end of each of the 87 673 lines of `weather.csv`: 87 673 bytes more, and `sha256sum` no longer gives `3f1ad06d…`.

`* -text` says: no file of this project is text to convert. It travels with the repository, on every laptop that clones it.

</div>

</div>

<!--
**Say:** Smiltė committed this file right after `.gitignore`, as `ef28e40`. The global setting acts on one laptop; this file acts on every clone.
**If asked:** `git status` stays clean even with the extra bytes, because Git takes the `0d` out again when it reads. Only the checksum shows it.
(~3 min)
-->

---
hideInToc: true
---

# What `git status --short` Says in Each **State**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| State of the file | `git status --short` | Letter in the view |
| --- | --- | --- |
| New, Git has no version of it | <code style="white-space: pre">?? .gitignore</code> | `U` |
| New and staged | <code style="white-space: pre">A  data/raw/weather.csv</code> | `A` under **Staged Changes** |
| Changed since the last commit, not staged | <code style="white-space: pre"> M README.md</code> | `M` |
| Changed and staged | <code style="white-space: pre">M  README.md</code> | `M` under **Staged Changes** |
| Deleted with `git rm`, staged | <code style="white-space: pre">D  data/raw/daily_export.csv</code> | `D` under **Staged Changes** |
| Changed by both, a merge stopped | <code style="white-space: pre">UU README.md</code> | `!` |
| Ignored, shown with `--ignored` | <code style="white-space: pre">!! data/processed/</code> | not listed |

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-secondary card-glass pad-compact">

Two columns before the name: the left one is the staging area, the right one the working folder. `M` on the left is staged, `M` on the right is not.

</div>

<div class="card card-info card-glass pad-compact">

A file with no letter is as in the last commit. The Status Bar shows `main*` with changes, `main+` with staged ones, `main!` during a conflict.

</div>

</div>

<!--
**Say:** every state of the lecture in one table, with the letter the view shows. Read the two columns before the file name: left the staging area, right the working folder.
(~3 min)
-->

---
hideInToc: true
---

# Common Git Errors and Their **Fixes**

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-compact">

```text
fatal: not a git repository (or any of
the parent directories): .git
```

The terminal is not in the project folder. `pwd` says where it is, and `cd` goes to the project.

</div>

<div class="card card-warning card-glass pad-compact">

```text
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '…'
```

The remote has a commit that this laptop lacks. Fetch and merge it with <code style="white-space: nowrap;">git pull --no-edit</code>, then push again.

</div>

<div class="card card-warning card-glass pad-compact">

```text
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each,
respectively.
```

`git status` after such a fetch. Both sides have a commit of their own. The same pull joins them.

</div>

<div class="card card-warning card-glass pad-compact">

A screen full of `~` signs: Git opened the editor Vim for a message. Type `:q!` and press Enter. After `git commit` that stops the commit: commit again with `-m`. After `git merge` or `git pull` it keeps the proposed message.

</div>

</div>

<div class="note-text mt-sm">Read the last lines of a long answer first: Git usually names the command that helps.</div>

<!--
**Say:** these four cover most of what stops a beginner. None of them means that anything is lost.
**If asked:** the editor depends on the choice made when Git was installed; on a Mac it is Vim.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="You edit `README.md`, run `git add README.md`, edit the file again, save, and run `git commit`. What does the commit hold?"
  :options="[
    'Both edits',
    'Only the first edit: the README as it was at git add',
    'Only the second edit',
    'Nothing: the file changed after git add'
  ]"
  :correct="1"
  explanation="git add copies the file as it is at that moment into the staging area, and git commit keeps the staging area. The second edit stays in the working folder: after the commit git status shows it as changed, not staged, and a second git add stages it."
/>

---
hideInToc: true
---

<MCQ
  question="`git commit` printed a new id, but your colleague sees nothing new on GitHub. Why?"
  :options="[
    'GitHub shows a commit only on the next day',
    'The commit is in the repository on your laptop; git push sends it to GitHub',
    'The staging area was not empty',
    'Your colleague has to clone the repository again'
  ]"
  :correct="1"
  explanation="add and commit act on the laptop only. git push sends the commits that GitHub lacks; your colleague then gets them with git pull."
/>

---
hideInToc: true
---

<MCQ
  question="`git push` answers `! [rejected] main -> main (fetch first)`. What do you do?"
  :options="[
    'git pull, settle a conflict if there is one, then git push again',
    'Delete the folder and clone the repository again',
    'git commit --amend, then git push',
    'Wait until the colleague who pushed has gone home'
  ]"
  :correct="0"
  explanation="GitHub has a commit that your laptop lacks, and a push may only add commits on top. git pull fetches it and merges it with yours; then the push goes through. Nothing is lost on either side."
/>

---
hideInToc: true
---

<MCQ
  question="The README of a public package you use gives a wrong unit. You do not know its authors. How do you propose the correction?"
  :options="[
    'Clone it and push the correction to its main',
    'Fork it, commit the correction on a branch of the fork, push, and open a pull request',
    'Ask to be invited as a collaborator first',
    'Edit the file on GitHub without an account'
  ]"
  :correct="1"
  explanation="Only people with write access may push to the package's repository. A fork is a copy you may push to; the pull request asks the authors to merge your branch, and they review it first."
/>

---
hideInToc: true
---

<MCQ
  question="A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and `analysis_final_REAL.py` side by side. What does Git give that these copies do not?"
  :options="[
    'Smaller files on the disk',
    'A faster program',
    'A conversion of the script into Markdown',
    'One file with its full history: what changed, when, and why'
  ]"
  :correct="3"
  explanation="Git keeps the present file apart from its history. Renamed copies mix the two, and none of them says what changed or why."
/>

---
hideInToc: true
---

<MCQ
  question="In zsh or Git Bash, `echo &quot;hi&quot; | git hash-object --stdin` prints an id. Which bytes does Git hash?"
  :options="[
    'The two letters h and i',
    'The word blob, a space, the digit 3, a zero byte, then h, i and a line break',
    'The word blob, a space, the digit 2, a zero byte, then h and i',
    'The name of the file and its date, then the letters'
  ]"
  :correct="1"
  explanation="echo hands h, i and a line break to git: three bytes. Git puts the header blob 3 and a zero byte in front and hashes all ten bytes: 45b983be36b73c0788dc9cbcb76cbb80fc7bb057, on every laptop. With a Windows line ending, 0d 0a, the header says blob 4 and the id is edf0effbb6851d0055229878b4bf0d7212167642."
/>

---
hideInToc: true
---

<MCQ
  question="A repository has 40 commits. `weather.csv` (2 515 215 bytes) was added in the first commit and never changed. How often is its content stored in `.git`?"
  :options="[
    '40 times, once per commit',
    'Once',
    'Never: Git stores only differences',
    'Twice: in the first commit and in the newest'
  ]"
  :correct="1"
  explanation="The content has one SHA-1, so it is one blob. Each of the 40 trees names that blob by its id. Compressed it takes 722 938 bytes."
/>

---
hideInToc: true
---

<MCQ
  question="`git cat-file -p` of a commit prints two lines that begin with `parent`. What kind of commit is it?"
  :options="[
    'The first commit of the repository',
    'A commit that was amended',
    'A merge: it joins two histories',
    'A commit that exists on two computers'
  ]"
  :correct="2"
  explanation="An ordinary commit has one parent and the first commit has none. A merge commit names the two commits it joins, so both histories can be reached from it."
/>

---
hideInToc: true
---

<MCQ
  question="The message of your last commit has a typing error. The commit is not pushed. What is the clean correction?"
  :options="[
    'git commit --amend -m with the corrected message',
    'git revert of the commit, then the same commit again',
    'git reset --hard and all the work once more',
    'Nothing can change a commit message'
  ]"
  :correct="0"
  explanation="For a commit that exists on one computer only, --amend replaces it with a corrected one. The id changes: the corrected commit is a new commit, and the old one leaves the history. After a push the commit may be on other computers, and then a new commit is the correction."
/>

---
hideInToc: true
---

<MCQ
  question="A colleague pushed a commit that edits a raw data file. You have pulled it. How do you take it back?"
  :options="[
    'git revert with the id of that commit, then push',
    'git commit --amend, then push',
    'Delete the commit on the GitHub website',
    'Copy the old file from an e-mail over the new one'
  ]"
  :correct="0"
  explanation="The commit is on the remote and on the colleague's laptop. git revert adds a commit with the reverse change, so every history stays the same and gains one commit. Amend would rewrite a commit others already have, and a copied file loses the reason."
/>

---
hideInToc: true
---

<MCQ
  question="After `git clone`, the folder `data/processed` is missing. `.gitignore` lists `data/processed/`. Why, and what brings it back?"
  :options="[
    'The clone failed: clone again',
    'Git stores files, not folders, and the files in it were ignored; the rebuild script makes them',
    'GitHub deletes folders larger than 1 MB',
    'The folder is hidden: ls -a shows it'
  ]"
  :correct="1"
  explanation="Ignored files were never committed, and an empty folder has no entry in a tree. ./scripts/rebuild.sh makes the folder and writes daily.csv and weather_valid.csv again."
/>

---
hideInToc: true
---

<MCQ
  question="On a new computer `git init` is followed by `git status`, and it says: On branch master. Why?"
  :options="[
    'Git found an old project and changed it',
    'init.defaultBranch is not set on this computer, so Git uses its old default name',
    'master is required as soon as there is more than one branch',
    'git status says master until the first commit exists'
  ]"
  :correct="1"
  explanation="A new repository gets the branch name main only when init.defaultBranch says so. Git for Windows even writes master into its own system settings. One line sets it for all later repositories: git config --global init.defaultBranch main. The branch of an existing repository is renamed with git branch -m main."
/>
