# 6: Version Control with Git

Lecture 4 checked the raw export against a list of checksums: one digit
changed, and only `FAILED` told it apart. Lecture 6 opens on two copies of
the raw export of the weather project, Smiltė's and the one her colleague
Tomas sent back by e-mail: line 2 reads `6,3` in one and `6,4` in the
other, and nothing says who changed it, when, or why. The lecture first
shows what version control does, as the pictures of Software Carpentry's
*Version Control with Git*: changes recorded one after another, two
versions from one start, a merge. Then it puts the weather project under
Git one commit at a time, each step in the Source Control view of VS Code
and typed in zsh (macOS) or Git Bash (Windows). It closes on the same
question, answered from the history: Tomas edited line 2 of a raw file, the
rebuilt file loses the checksum of the README, and a revert puts it back.
How Git stores all this (a name computed from the bytes, the blob, the
tree, the commit as text, a branch as a file) comes after the recap, in
**For the Curious**, for whoever wants it.

## What the lecture covers

1. **Copies and versions** — files named `final_v2`; two copies of
   `daily_export.csv` with 180 bytes each, side by side: line 2, `6,3`
   against `6,4`, and who, when and why stays open; a file as a sequence
   of changes, two versions from one start and a merge, as pictures; what
   Google Drive, Dropbox and Track Changes in Word keep, set against Git;
   where Git comes from: the Linux kernel lost its proprietary tool,
   BitKeeper, in April 2005, and Git's own first commit, of 7 April, still
   says who, when and why.
2. **Setting up** — Git's version, the name and the e-mail written into
   every commit, and three settings.
3. **Tracking changes** — the three areas as a picture; the Source Control
   view; `git init`; `git status --short`; stage and commit; what a commit
   keeps (every staged file, the commit before it, who and when, why) and
   its id, a checksum of all four; what `git status --short` says in each
   state; the commit message.
4. **What goes into a repository** — which files go in; why `weather.csv`
   (2.5 MB) fits and a file of 3 GB does not, with measured sizes;
   `.gitignore` for `data/processed/`, which `rebuild.sh` makes;
   `.gitattributes` with `* -text`, so a clone on Windows keeps the bytes;
   the rest committed, several files in one commit.
5. **Changes and history** — the diff in the view and typed; `git log`.
6. **Undoing** — `git restore` for an edit; `--amend` for a message with a
   typo; a commit that deletes the raw export and breaks the rebuild, taken
   back with `git revert`; which undo for which case.
7. **Remotes** — a remote as a picture; a GitHub account; publishing from
   VS Code and typed; Smiltė invites Tomas as a collaborator; Tomas clones,
   and the ignored folder comes back by the rebuild script; Tomas pushes a
   commit and Smiltė pulls it.
8. **Branches and merging** — a branch; a fast-forward merge; two branches
   that both changed the first paragraph; the conflict, resolved in the
   editor and typed; ahead and behind; the usual error messages; the
   commands between the four places, as one picture; a table of every step
   in Source Control and typed.
9. **A result and its commit** — `git log -- data/raw` and `git blame` find
   Tomas's commit; `git show`, built up line by line, answers who, when and
   why; the edit gives `daily.csv` a checksum other than the README's
   `33fe5e77…`; a revert restores `33fe5e77…`; a tag `v1.0`.
10. **For the curious** (optional, after the recap) — what has to be kept;
    a name computed from the content with `git hash-object`, the same on
    every laptop, and another id for `hello` with a Windows line ending
    (`0d 0a`); the header `blob <size>` and a zero byte; the id of
    `weather.csv`, `f811f73d`; a folder as a list, set beside
    `shasum -a 256`; the tree of the whole project; a commit as a text
    with a tree, a parent, an author and a message; one commit drawn as its
    objects; the id of a commit, computed again; history as a graph; a
    branch as a file of 41 bytes that a commit moves.

## The lecture, part by part

The lecture is slides 1–62; when time is short, skip the slides of the
second table. **Slides 63–74, For the Curious, are optional:** show them
only if time is left, or leave them for the room to read; the timing
counts them as no lecture time. Slides 75–83 are the self-check quizzes and
take no lecture time either. To jump, type the slide number and press
Enter.

| Slides | Part |
|--|--|
| 1–8 | Copies, two copies of the export, changes, versions and a merge as pictures; Drive, Dropbox and Word against Git; where Git comes from |
| 9–10 | Setting up: version, name, e-mail |
| 11–12, 14–17, 19 | The three areas, `git init`, `git status`, the first commit, what a commit keeps, the message |
| 20–21, 23–25 | Which files go in, `.gitignore`, `.gitattributes`, the rest |
| 26–29 | The diff, `log` |
| 30–35 | restore, amend, a commit that breaks the rebuild, revert, which undo for which case |
| 36–37, 39–44 | A remote, publish, a collaborator, clone, pull |
| 45–50, 54 | A branch, a merge, a conflict, the commands as one picture |
| 56–62 | Who changed the export, the revert, the tag, the recap |
| 63–74 | For the Curious (optional) |

| Skip | Slides |
|--|--|
| Source Control in VS Code: say it while doing slide 14 | 13 |
| What `git status --short` says in each state | 18 |
| Which data files fit in a repository | 22 |
| A GitHub account: the seminar creates them | 38 |
| Resolve it, typed; ahead and behind | 51, 52 |
| Common errors; the table of steps (on the projector in the seminar) | 53, 55 |

- **Do not cut slides 57–60.** They answer the question of slide 4 from
  the history, with commands the room has seen or that the slide itself
  explains (`git blame`, `git show`). The table on slide 58 has the
  questions of slide 4, answered.
- **Slide 17** (what a commit keeps) is the one fact of the model the
  main path needs: the id is a checksum of the files, the commit before,
  who, when and why. Slide 32 (amend: a corrected message gives a new id)
  and the remotes (the same commits under the same ids) rest on it.
- **Nothing in slides 1–62 needs slides 63–74.** For the Curious starts
  from the checksums of Lecture 4 and ends at a branch as a file of 41
  bytes; each of its slides needs the one before.
- **Slide 24** (`.gitattributes`) is short but matters on every Windows
  laptop: without it, the checksums of Lecture 4 fail after a clone.

## Live in the lecture

Five moments, each marked **Live:** in its slide's note, run in one folder,
in order. Each costs about a minute more than the slide alone; the minutes
above include it. If a line misbehaves, go to the slide: it has the output.
The commit ids and line counts on the laptop differ from the slides, which
come from the lecture's scratch repository (see below).

**Before the lecture.** Unzip [`weather_project.zip`](../data/weather_project.zip)
into a new folder, open `weather-project` in VS Code, open its terminal
(zsh on a Mac, Git Bash on Windows) and make the font large.

| Slide | What to do | What the room sees |
|--|--|--|
| 10 | `git --version`, then `git config --global user.name` | The version and the name |
| 14 | Source Control: **Initialize Repository**; then `ls -a` | `.git` among the folders |
| 16 | **+** beside `README.md`, message "Add the README", **Commit** | `README.md` leaves the list; the Graph shows one commit |
| 27 | Add the three lines of the Result section to `README.md`, save, select the file in Source Control; then stage and commit it | The diff view: five green lines |
| 31 | Select one whole section of the README, delete it, save; `git diff --stat`; `git restore README.md` | The section comes back |

The Result section of slide 27:

```text
## Result

- **Mean air temperature, 2016 to 2025:** 7.16 °C
- **From:** `column_stats.py` on `data/processed/weather_valid.csv`, 87 552 hours
```

If For the Curious is shown, its slides 65 and 67 have two more:
`echo "hello" | git hash-object --stdin` (`ce013625…` on every laptop) and
`git hash-object data/raw/weather.csv` (`f811f73d…`, on every laptop).

## The outputs on the slides

Every command on the slides ran in a scratch repository, and the output is
copied from the terminal: `bash misc/l05_scratch_repo/build.sh` makes it
again with the same ids (Git 2.56 and bash on Linux, whose GNU tools are
those of Git Bash; author and committer dates fixed on 20 October 2026).
The project in it is the weather project as Lecture 4 leaves it, with a
shorter `rebuild.sh`: `README.md` with *How to rebuild*,
`data/raw/weather.csv` and `daily_export.csv`, `scripts/clean_export.py`,
`column_stats.py` and `rebuild.sh`. Smiltė makes the commits; Tomas clones
the repository and pushes one.

- **A line `...` in a block** marks lines cut on the slide; long lines are
  cut at `…`. Blocks of more than about five lines grow one command per
  click (magic-move).
- **`git status --short` on slide 15** was run on 21 October 2026 in the
  same scratch repository, right after `git init` (Git 2.47); the rest of
  the outputs are from the build of 20 October.
- **Blob and tree ids are the same for everyone.** `weather.csv` is
  `f811f73d93226acc8a0c96562aef9f7825b85b0a` on every laptop, and the tree of
  `data/raw` is `ee85972a…`.
- **Commit ids differ.** A commit contains its author and its time.
- **The address in the push, clone and pull outputs** is put in by Git's
  `insteadOf`: the commands ran against a repository in a local folder.
  `smilte-example` stands for the user name; the transfer rate of the push
  is that of a local copy.
- **macOS outputs.** `shasum -a 256` was run as `sha256sum`, which prints
  the same; `ls` on a Mac lists `README.md` before `data`, as on the
  slide, while Git Bash may sort it after.
- **The CRLF ids** of `hello` (`ef0493b2…`, slide 65) and `hi` (quiz 2)
  come from the bytes `0d 0a`, as a Windows program writes them; they were
  also measured on Windows with Git for Windows 2.51.
- **The pictures of VS Code** are from VS Code 1.140 (the web version run
  from the lecture's scratch folders), theme Dark Modern; the message box
  reads `Ctrl+Enter`, on macOS `Cmd+Enter`. *Initialize Repository*,
  *Publish Branch* and the branch picker are older pictures from macOS.
- **The schematic figures** are from Software Carpentry's *Version Control
  with Git* (CC BY 4.0), credited on each slide: `play-changes`,
  `versions`, `merge`, `git-staging-area`, `git-committing`,
  `git-restore`. The three GitHub figures of slides 37 and 42 are
  copies of its `git-freshly-made-github-repo`,
  `github-repo-after-first-push` and `github-collaboration` with the
  weather project's names (`git-weather-remote-*.svg`). `git_flow.svg`
  on slide 54 is the course's own.
- **A Git that prints 64 digits.** Git 3.0 is announced to make SHA-256 the
  hash of new repositories. If a student's `git hash-object` prints 64 hex
  digits, the header is hashed with SHA-256 in place of SHA-1. In such a
  repository a branch is also no longer a file under `.git/refs/heads`: use
  `git rev-parse main` for slide 74.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 75–83: eight quiz slides for students to try afterwards. Questions 2
and 4 are on For the Curious. The same questions, with their answers:

1. A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and
   `analysis_final_REAL.py` side by side. What does Git give that these
   copies do not?
   *One file with its full history: what changed, when, and why.*
2. In zsh or Git Bash, `echo "hi" | git hash-object --stdin` prints an id.
   Which bytes does Git hash?
   *The word `blob`, a space, the digit 3 and a zero byte, then `h`, `i` and
   a line break: ten bytes. The id is
   `45b983be36b73c0788dc9cbcb76cbb80fc7bb057` on every laptop. With a Windows line ending,
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
   *`git commit --amend -m` with the corrected message. The id changes:
   the corrected commit is a new commit, and the old one leaves the
   history.*
6. A colleague pushed a commit that edits a raw data file, and you have
   pulled it. How do you take it back?
   *`git revert` with the id of that commit, then push. Every history stays
   as it is and gains one commit.*
7. After `git clone`, the folder `data/processed` is missing, and
   `.gitignore` lists `data/processed/`. Why, and what brings it back?
   *Git stores files, not folders, and the files in it were ignored.
   `./scripts/rebuild.sh` makes the folder and its files again.*
8. On a new computer `git init` is followed by `git status`, which says
   `On branch master`. Why?
   *`init.defaultBranch` is not set to `main` there, so Git uses `master`,
   its old default name. `git branch -m main` renames the branch.*

## Paired seminar

[Seminar 6](../seminars/seminar_06.md) clones the weather project from
GitHub (`MindaugasSarpis/weather-project`) and works on its history: who
changed the mean temperature, when and why, found with `git log`,
`git blame` and `git show`, and taken back with `git revert`. The room then
leaves made files out with `.gitignore`, commits its own work, and
publishes the repository to a private one on each student's GitHub account.

## What left the deck

On 13 October 2026 the deck was cut to one line and moved to the weather
project. These slides are in `lectures/content/parked/06_Version_Control.md`:
the README that says how to fetch a file kept out of the repository,
`git stash`, line endings and a clone on Windows with `core.autocrlf true`
(now one slide, `.gitattributes`), SSH, and the section *Working with
Others* (pull requests, review, issues, forks, GitLab at CERN), with their
three quizzes.

On 21 October 2026 the deck was reworked simple first: the model moved
from the start to For the Curious, and five slides were parked in the same
file: the opening with the two checksums, `git diff --no-index` on the two
copies, the drawn three areas and the drawn remote (now the Software
Carpentry figures), and *Read a Commit, Trace a Line* (`git show` and
`git blame` now come where they answer the opening question).

## Take-aways

- Two copies show that a line differs. Who changed it, when and why is
  kept only by a history.
- A commit keeps every staged file, the commit before it, who, when and
  why. Its id is a checksum of all of it: the same on every copy of the
  repository, and another id for any other content.
- A commit is made in two steps: stage, then commit. One commit has one
  purpose, and its message says what it does.
- Small raw data goes into the repository. Files a script makes again stay
  out by `.gitignore`; `* -text` in `.gitattributes` keeps the bytes of
  every file on every laptop.
- `git restore` takes back an edit, `--amend` corrects the last commit
  before it is pushed, `git revert` takes back a commit by a new one.
- A remote is a second copy of the repository. Pull before you start, push
  when you stop.
- A branch holds work that is tried apart from `main`. A conflict means
  that the same lines were changed twice; a person decides.
- A result that leaves the project carries the id or the tag of its commit.
- For the curious: Git names a content by the SHA-1 of a short header and
  its bytes, keeps a folder as a tree and a commit as a short text, and a
  branch is a name for one commit.
