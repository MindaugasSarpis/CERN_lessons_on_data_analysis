# 5: Version Control with Git

Lecture 4 ended with a copy of the cleaned export that has the right size
and one digit changed, and only the checksum told it apart. Lecture 5 opens
on two copies of the raw export of the weather project, Smiltė's and the
one her colleague Tomas sent back: the checksum says that they differ,
`git diff` says which line, and nothing says who changed it, when, or why.
The lecture first builds what Git stores, from the checksums of Lecture 4,
then puts the weather project under Git one commit at a time, each step in
the Source Control view of VS Code and typed in PowerShell 7. It closes on
the same question, answered from the history: Tomas edited line 2 of a raw
file, the rebuilt file loses the checksum of the README, and a revert puts
it back.

## What the lecture covers

1. **Two copies of the export** — two copies of `daily_export.csv` with 180
   bytes each and two checksums; `git diff --no-index` finds line 2, `6,3`
   against `6,4`; who, when and why stays open. Copies named `final_v2`,
   and what a version control system records.
2. **The model** — what has to be kept; a name computed from the content
   with `git hash-object`, and why the same line gives another id on
   Windows (`0d 0a`); the header `blob <size>` and a zero byte; the id of
   `weather.csv`, `f811f73d`, the same on every laptop; a folder as a list,
   set beside `Get-FileHash`; the tree of the whole project; a commit as a
   text with a tree, a parent, an author and a message; one commit drawn as
   its objects; the id of a commit, computed again; history as a graph; a
   branch as a file of 41 bytes that a commit moves; the three areas.
3. **First commits** — the check of Git and three settings; the Source
   Control view; `git init`; `git status`; stage and commit; what
   `git status --short` says in each state; the commit message.
4. **Data in a repository** — which files go in; why `weather.csv` (2.5 MB)
   fits and a file of 3 GB does not, with measured sizes; `.gitignore` for
   `data/processed/`, which `rebuild.ps1` makes; `.gitattributes` with
   `* -text`, so a clone on Windows keeps the bytes; the rest committed.
5. **Changes and history** — the diff in the view and typed; `git log`;
   `git show` and `git blame`.
6. **Undoing** — `git restore` for an edit; `--amend` for a message with a
   typo; a commit that deletes the raw export and breaks the rebuild, taken
   back with `git revert`.
7. **Remotes** — what a remote is; a GitHub account; publishing from VS
   Code and typed; Tomas clones, the ignored folder comes back by the
   rebuild script; Tomas pushes a commit and Smiltė pulls it.
8. **Branches and merging** — a branch; a fast-forward merge; two branches
   that both changed the first paragraph; the conflict, resolved in the
   editor and typed; ahead and behind; the usual error messages; a table of
   every step in Source Control and typed.
9. **A result and its commit** — `git log -- data/raw` and `git blame` find
   Tomas's commit; `git show` read line by line answers who, when and why;
   the edit gives `daily.csv` the checksum of Lecture 4's changed copy; a
   revert restores `33fe5e77…`; a tag `v1.0`.

## The lecture in 90 minutes

The lecture is slides 1–68 and estimates about 135 min. Slides 69–77 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | Two copies of the export; what version control records |
| 0:10 | 8–20 | The model: blob, tree, commit, graph, branch, three areas |
| 0:35 | 22, 24–26, 28 | Settings, `git init`, `git status`, the first commit, the message |
| 0:44 | 30, 32–34 | Which files go in, `.gitignore`, `.gitattributes`, the rest |
| 0:52 | 36–39 | The diff, `log`, `show` and `blame` |
| 1:00 | 41–44 | restore, amend, a commit that breaks the rebuild, revert |
| 1:08 | 46, 48–51 | A remote, publish, push, clone, pull |
| 1:17 | 53–57 | A branch, a merge, a conflict |
| 1:25 | 62–68 | Who changed the export, the revert, the tag, the recap |
| 1:35 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Source Control in VS Code: say it while doing slide 24 | 23 | 2 min |
| What `git status --short` says in each state | 27 | 3 min |
| Which data files fit in a repository | 31 | 3 min |
| A GitHub account: the seminar creates them | 47 | 2 min |
| Resolve it, typed; ahead and behind | 58, 59 | 4 min |
| Common errors; the table of steps (on the projector in the seminar) | 60, 61 | 4 min |

- **Do not cut slides 62–66.** They answer the question of slides 4–5 from
  the history, with only commands the room has seen.
- **Do not cut slides 9–20** (the model). Each needs the one before it, and
  slides 31, 42, 44, 50 and 58 argue from it.
- **Slide 33** (`.gitattributes`) is short but matters on every Windows
  laptop: without it, the checksums of Lecture 4 fail after a clone.

## Live in the lecture

Six moments, each marked **Live:** in its slide's note, run in one folder,
in order. Each costs about a minute more than the slide alone; the minutes
above include it. If a line misbehaves, go to the slide: it has the output.
The commit ids and line counts on the laptop differ from the slides, which
come from the lecture's scratch repository (see below).

**Before the lecture.** Unzip [`weather_project.zip`](../data/weather_project.zip)
into a new folder, open `weather-project` in VS Code, open its terminal
(PowerShell 7) and make the font large. Check `git config --global user.name`
once.

| Slide | What to do | What the room sees |
|--|--|--|
| 10 | `"hello" | git hash-object --stdin` | `ce013625…` on a Mac, `ef0493b2…` on Windows |
| 12 | `git hash-object data/raw/weather.csv` | `f811f73d…`, on every laptop |
| 24 | Source Control: **Initialize Repository**; then `Get-ChildItem -Force -Name` | `.git` among the folders |
| 26 | **+** beside `README.md`, message "Add the README", **Commit** | `README.md` leaves the list; the Graph shows one commit |
| 36 | Add the three lines of the Result section to `README.md`, save, select the file in Source Control; then stage and commit it | The diff view: five green lines |
| 41 | Select one whole section of the README, delete it, save; `git diff --stat`; `git restore README.md` | The section comes back |

The Result section of slide 36:

```text
## Result

- **Mean air temperature, 2016 to 2025:** 7.16 °C
- **From:** `column_stats.py` on `data/processed/weather_valid.csv`, 87 552 hours
```

## The outputs on the slides

Every command on the slides ran in a scratch repository, and the output is
copied from the terminal: `bash misc/l05_scratch_repo/build.sh` makes it
again with the same ids (Git 2.56, PowerShell 7.6, on Linux; author and
committer dates fixed on 20 October 2026). The project in it is the weather
project as Lecture 4 leaves it: `README.md` with *How to rebuild*,
`data/raw/weather.csv` and `daily_export.csv`, `scripts/clean_export.py`,
`column_stats.py` and `rebuild.ps1`. Smiltė makes the commits; Tomas clones
the repository and pushes one.

- **Blob and tree ids are the same for everyone.** `weather.csv` is
  `f811f73d93226acc8a0c96562aef9f7825b85b0a` on every laptop, and the tree of
  `data/raw` is `ee85972a…`.
- **Commit ids differ.** A commit contains its author and its time.
- **The address in the push, clone and pull outputs** is put in by Git's
  `insteadOf`: the commands ran against a repository in a local folder.
  `smilte-example` stands for the user name; the transfer rate of the push
  is that of a local copy.
- **The Windows ids** of `hello` (`ef0493b2…`, slide 10) and `hi` (quiz 2)
  were measured with PowerShell 7.6 and Git for Windows 2.51, and computed
  again here from the bytes `0d 0a`. Everything else ran in PowerShell 7.6
  on Linux, which hands over the bytes a Mac does.
- **The pictures of VS Code** are from VS Code 1.140 (the web version run
  from the lecture's scratch folders), theme Dark Modern; the message box
  reads `Ctrl+Enter`, on macOS `Cmd+Enter`. *Initialize Repository*,
  *Publish Branch* and the branch picker are older pictures from macOS.
- **A Git that prints 64 digits.** Git 3.0 is announced to make SHA-256 the
  hash of new repositories. If a student's `git hash-object` prints 64 hex
  digits, the header is hashed with SHA-256 in place of SHA-1. In such a
  repository a branch is also no longer a file under `.git/refs/heads`: use
  `git rev-parse main` for slide 19.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 69–77: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and
   `analysis_final_REAL.py` side by side. What does Git give that these
   copies do not?
   *One file with its full history: what changed, when, and why.*
2. On a Mac, PowerShell runs `"hi" | git hash-object --stdin`. Which bytes
   does Git hash?
   *The word `blob`, a space, the digit 3 and a zero byte, then `h`, `i` and
   a line break: ten bytes. The id is
   `45b983be36b73c0788dc9cbcb76cbb80fc7bb057`. On Windows the line break is
   `0d 0a`, the header says `blob 4`, and the id is
   `edf0effbb6851d0055229878b4bf0d7212167642`.*
3. A repository has 40 commits. `weather.csv` (2 515 215 bytes) was added in
   the first one and never changed. How often is its content stored?
   *Once. The content has one id, and each of the 40 trees names it.
   Compressed it takes 722 938 bytes.*
4. `git cat-file -p` of a commit prints two lines that begin with `parent`.
   What kind of commit is it?
   *A merge. It joins two histories.*
5. The message of your last commit has a typing error, and the commit is
   not pushed. What is the clean correction?
   *`git commit --amend -m` with the corrected message. The id changes,
   because the message is part of the hashed text.*
6. A colleague pushed a commit that edits a raw data file, and you have
   pulled it. How do you take it back?
   *`git revert` with the id of that commit, then push. Every history stays
   as it is and gains one commit.*
7. After `git clone`, the folder `data/processed` is missing, and
   `.gitignore` lists `data/processed/`. Why, and what brings it back?
   *Git stores files, not folders, and the files in it were ignored.
   `./scripts/rebuild.ps1` makes the folder and its files again.*
8. On a new computer `git init` is followed by `git status`, which says
   `On branch master`. Why?
   *`init.defaultBranch` is not set to `main` there, so Git uses `master`,
   its old default name. `git branch -m main` renames the branch.*

## Paired seminar

[Seminar 5](../seminars/seminar_05.md) clones the weather project from
GitHub (`MindaugasSarpis/weather-project`) and works on its history: who
changed the mean temperature, when and why, found with `git log`,
`git blame` and `git show`, and taken back with `git revert`. The room then
leaves made files out with `.gitignore`, commits its own work, and
publishes the repository to a private one on each student's GitHub account.

## What left the deck

On 13 October 2026 the deck was cut to one line and moved to the weather
project. These slides are in `lectures/content/parked/05_Version_Control.md`:
the README that says how to fetch a file kept out of the repository,
`git stash`, line endings and a clone on Windows with `core.autocrlf true`
(now one slide, `.gitattributes`), SSH, and the section *Working with
Others* (pull requests, review, issues, forks, GitLab at CERN), with their
three quizzes.

## Take-aways

- A checksum says that two copies differ, and `git diff` says which line.
  Who changed it, when and why is kept only by a history.
- Git names a content by the SHA-1 of a short header and its bytes. The
  same bytes have the same id on every computer, and a content is stored
  once. A line ending is one of the bytes: `0a` and `0d 0a` give two ids.
- A tree is the list of a folder, like a list of checksums. A commit is a
  text that names a tree, a parent, an author, a time and a reason. Its id
  fixes the whole project and every version before it.
- A branch is a name for a commit. A new commit moves the name.
- A commit is made in two steps: stage, then commit. One commit has one
  purpose, and its message says what it does.
- Small raw data goes into the repository. Files a script makes again stay
  out by `.gitignore`; `* -text` in `.gitattributes` keeps the bytes of
  every file on every laptop.
- `git restore` takes back an edit, `--amend` corrects the last commit
  before it is pushed, `git revert` takes back a commit by a new one.
- A remote is a second copy of the repository. Pull before you start, push
  when you stop.
- A conflict means that the same lines were changed twice. A person
  decides.
- A result that leaves the project carries the id or the tag of its commit.
