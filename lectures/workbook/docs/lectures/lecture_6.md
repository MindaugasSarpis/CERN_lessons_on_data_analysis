# 6: Version Control with Git

Lecture 4 checked the raw export against a list of checksums: one digit
changed, and only `FAILED` told it apart. Lecture 6 opens on two copies of
the raw export of the weather project, Smiltė's and the one her colleague
Tomas sent back by e-mail: line 2 reads `6,3` in one and `6,4` in the
other, and nothing says who changed it, when, or why. The lecture first
shows what version control does, in pictures: changes recorded one after
another, two versions from one start, a merge. Then it puts the weather
project under Git one step at a time, and takes its time over the three
commands everything else rests on: `git add` puts a file into the next
commit, `git commit` keeps it in the history, `git push` sends the commits
to GitHub; one picture per command shows where the change is afterwards.
Each step is shown in the Source Control view of VS Code and typed in zsh
(macOS) or Git Bash (Windows). Then two ways to work together: Smiltė and
Tomas share one repository (a refused push, a pull, a conflict), and Rūta,
from another university, sends a change by a fork and a pull request. It
closes on the opening question, answered from the history. How Git stores
all this comes after the recap, in **For the Curious**, and a few more
commands in **More Commands**, for whoever wants them.

## What the lecture covers

1. **Copies and versions**: files named `final_v2`; two copies of
   `daily_export.csv` with 180 bytes each, side by side: line 2, `6,3`
   against `6,4`, and who, when and why stays open; a file as a sequence
   of changes, two versions from one start and a merge, as pictures; what
   Google Drive, Dropbox and Track Changes in Word keep, set against Git;
   where Git comes from.
2. **Setting up**: Git's version, the name and the e-mail written into
   every commit, and three settings.
3. **Tracking changes**: the four places a change passes (working folder,
   staging area, repository, GitHub) and the command between each two;
   the Source Control view; `git init`; `git status --short`; `git add`
   and `git commit`, one slide and one picture each; what a commit keeps
   and its id; the commit message.
4. **What goes into a repository**: which files go in; `.gitignore` for
   `data/processed/`; the rest committed, five files in one commit.
5. **Changes and history**: the diff in the view and typed; one change
   through its three steps, with what `git status --short` says after
   each; `git log`.
6. **Undoing**: `git restore` for an edit; a commit that deletes the raw
   export and breaks the rebuild, taken back with `git revert`; which undo
   for which case.
7. **Remotes**: a remote as a picture; a GitHub account; publishing from
   VS Code and typed; `git push`, and what it sends (commits only: a
   staged edit stays behind, `Everything up-to-date`); where the change is
   after each step, who sees it, and what a lost laptop takes with it.
8. **Working together**: two ways, as one picture. A shared repository:
   Smiltė invites Tomas, Tomas clones, pushes a commit and Smiltė pulls it;
   then both change the same two lines, Smiltė's push is refused, her
   `git pull` stops on a conflict, she resolves it in the editor, commits
   the merge and pushes. A fork and a pull request: Rūta forks the public
   repository, clones her fork, commits on a branch `ranges`, pushes it to
   the fork, opens pull request #1; Smiltė reviews and merges it on GitHub
   and pulls. The two ways side by side; a table of every step.
9. **A result and its commit**: `git log -- data/raw` and `git blame` find
   Tomas's commit; `git show` answers who, when and why.
10. **For the curious** (optional, after the recap): a name computed from
    the content, the blob, the tree, the commit as text, history as a
    graph, a branch as a file of 41 bytes.
11. **More commands** (optional): `--amend`; rebuilding what a clone
    lacks; the checksum the edit breaks, the revert that restores it and a
    tag `v1.0`; the map of every command; which data files fit, with
    measured sizes; `.gitattributes`; what `git status --short` says in
    each state; the usual error messages.

## The lecture, part by part

The lecture is slides 1–62. The minutes in the notes add up to about 134
for them, so in the two-hour slot **plan to skip the slides of the second
table** (about 119 min then). **Slides 63–84, For the Curious and More
Commands, are optional:** show them only if time is left, or leave them
for the room to read; the timing counts them as no lecture time. Slides
85–97 are the self-check quizzes and take no lecture time either. To
jump, type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–8 | Copies, two copies of the export, changes, versions and a merge as pictures; Drive, Dropbox and Word against Git; where Git comes from |
| 9–10 | Setting up: version, name, e-mail, three settings |
| 11–19 | The four places; Source Control; `git init`, `git status`; `git add`; `git commit`; what a commit keeps; the message |
| 20–23 | Which files go in, `.gitignore`, the rest |
| 24–28 | The diff, one change in three steps, `log` |
| 29–34 | restore, amend, a commit that breaks the rebuild, revert, which undo for which case |
| 35–41 | A remote, an account, publish, `git push` and what it sends, where the change is after each step |
| 42–51 | Two ways to work together; a shared repository: collaborator, clone, pull, a refused push, a conflict resolved |
| 52–58 | A fork and a pull request; the two ways side by side; every step |
| 59–62 | Who changed the export, read the commit, the recap |
| 63–74 | For the Curious (optional) |
| 75–84 | More Commands (optional) |

| Skip | Slides |
|--|--|
| Where Git comes from | 8 |
| Drive, Dropbox and Word against Git: ask the question of its note instead | 7 |
| Source Control in VS Code: say it while doing slide 14 | 13 |
| The same diff, typed | 26 |
| Publish to GitHub, typed: slide 38 publishes from VS Code | 39 |
| The table of every step: it is on the projector in the seminar | 58 |

- **Take your time over slides 12–17 and 40–41.** They are the answer to
  "what does add, commit, push do": each picture shows the four places
  and where the change is after one command. Ask the room, after each,
  where the README is now and who can see it.
- **Do not cut slides 47–51 or 52–57.** They are the two ways to work
  together. A refused push and a conflict are what every student meets in
  the first week of shared work; the fork and pull request is how they
  propose a change to anybody else's project.
- **Do not cut slides 60–61.** They answer the question of slide 4 from
  the history.
- **Nothing in slides 1–62 needs slides 63–84.**

## Live in the lecture

Six moments, run in one folder, in order. Each slide with a live moment
carries the tag **LIVE DEMO** in its lower right corner, and its note
begins with **Live:**. If a line misbehaves, go back to the slide: it has
the output. The commit ids on the laptop differ from the slides (a commit
contains its author and its time); the line counts are the same.

**Before the lecture.** Unzip [`weather_project_git.zip`](../data/weather_project_git.zip)
(1.1 MB) into a new folder: the weather project of the slides before
`git init`, with `rebuild.sh` and the two files it makes. Open
`weather-project` in VS Code, open the Source Control view and the
terminal (zsh on a Mac, Git Bash on Windows) and make the font large.

| Slide | Min | What to do | What the room sees |
|--|--|--|--|
| 10 | 3 | `git --version`, then `git config --global user.name` | The version and the name |
| 14 | 2 | Source Control: **Initialize Repository**; then `ls -a` | `.git` among the folders; 8 files under **Changes** |
| 16 | 3 | **+** beside `README.md`; then `git status --short` | `README.md` under **Staged Changes**; `A  README.md` |
| 17 | 3 | Message "Add the README", **Commit**; then `git status --short` | **Staged Changes** empty; `?? data/`, `?? scripts/` |
| 25 | 2 | Type the Result section below into `README.md` above `## Licence`, save, select the file in Source Control; then **+** and commit "Give the mean temperature in the README" | The diff view: five green lines |
| 30 | 2 | Select the section *Columns of `weather.csv`* (11 lines, down to *Missing value*), delete it, save; `git diff --stat`; `git restore README.md` | `11 deletions`, then the section comes back |

Slides 22–23 (`.gitignore`, the rest) are shown, not typed: on the laptop
the other seven files stay under **Changes** until the end, and that is
fine. For the same reason a `git status` typed at slide 30 lists `data/`
and `scripts/` as untracked instead of `working tree clean`: leave it to
the slide. Publishing (slide 38) and the whole of Working Together are
not live: they need GitHub sign-ins on the projector, and in the case of
the refused push two laptops.

The Result section of slide 25:

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
the repository, pushes a correction of the raw export and a reworded
paragraph that conflicts with Smiltė's; Rūta forks it and sends the column
ranges by a pull request.

- **A line `...` in a block** marks lines cut on the slide; long lines are
  cut at `…`. Blocks of more than about five lines grow one command per
  click (magic-move).
- **Git 2.56.0.** The script runs with Git 2.56.0 (conda-forge), the
  version the room installs; the live moments were replayed from
  `weather_project_git.zip`, which the same script writes. On 27 October
  2026 the story after Tomas's first push was rewritten (the shared
  repository, the fork): every commit up to `f2546ed` kept its id, the
  later ones are new.
- **GitHub, simulated.** The fork is a bare copy of the remote under the
  address `ruta-example/weather-project`, and the merge of pull request #1
  is a merge commit by Smiltė with GitHub as its committer and GitHub's
  default message, `Merge pull request #1 from ruta-example/ranges`. The
  lines `remote: Create a pull request for 'ranges' …` on slide 54 are
  printed by GitHub, not by a local remote, and were added as GitHub
  prints them.
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
- **The CRLF ids** of `hello` (`ef0493b2…`, slide 65) and `hi` (quiz 6)
  come from the bytes `0d 0a`, as a Windows program writes them; they were
  also measured on Windows with Git for Windows 2.51.
- **The pictures of VS Code** are from VS Code 1.140 (the web version run
  from the lecture's scratch folders), theme Dark Modern; the message box
  reads `Ctrl+Enter`, on macOS `Cmd+Enter`. *Initialize Repository*,
  *Publish Branch* and the branch picker are older pictures from macOS.
  The conflict on slide 50 is a picture of a merge of a branch; its
  incoming label was changed to Tomas's commit id, which a pull shows,
  and the Source Control panel was cut off.
- **The diagrams** are drawn by `figures/src/git.py` (`python3
  figures/src/build.py --only git`), in the course style, with the ids of
  the scratch repository: the opening pictures (slides 5, 6), the four
  places and add, commit, push (12, 16, 17, 40), commit the rest (23),
  restore (30), the remotes (36, 45), the two ways to work together (43),
  the refused push, the pull, the merge and the pull request (47, 48, 51,
  56), the objects, the history and a branch of For the Curious (71, 73,
  74) and the map of every command (80). Until 27 October the deck used
  Software Carpentry's figures (CC BY 4.0) and Mermaid drawings.
- **A Git that prints 64 digits.** Git 3.0 is announced to make SHA-256 the
  hash of new repositories. If a student's `git hash-object` prints 64 hex
  digits, the header is hashed with SHA-256 in place of SHA-1. In such a
  repository a branch is also no longer a file under `.git/refs/heads`: use
  `git rev-parse main` for slide 74.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 86–97: twelve quiz slides for students to try afterwards. Questions
6–8 are on For the Curious, 11 on More Commands. The same questions, with their answers:

1. You edit `README.md`, run `git add README.md`, edit the file again,
   save, and run `git commit`. What does the commit hold?
   *Only the first edit: the README as it was at `git add`. The second
   edit stays in the working folder: after the commit `git status` shows
   it as changed, not staged (before the commit, `MM README.md`), and a
   second `git add` stages it.*
2. `git commit` printed a new id, but your colleague sees nothing new on
   GitHub. Why?
   *The commit is in the repository on your laptop; `git push` sends it to
   GitHub, and your colleague gets it with `git pull`.*
3. `git push` answers `! [rejected] main -> main (fetch first)`. What do
   you do?
   *`git pull`, settle a conflict if there is one, then `git push` again.
   GitHub has a commit your laptop lacks, and a push may only add commits
   on top.*
4. The README of a public package you use gives a wrong unit. You do not
   know its authors. How do you propose the correction?
   *Fork it, commit the correction on a branch of the fork, push, and open
   a pull request. Only people with write access may push to the
   package's repository; the authors review the request and merge it.*

5. A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and
   `analysis_final_REAL.py` side by side. What does Git give that these
   copies do not?
   *One file with its full history: what changed, when, and why.*
6. In zsh or Git Bash, `echo "hi" | git hash-object --stdin` prints an id.
   Which bytes does Git hash?
   *The word `blob`, a space, the digit 3 and a zero byte, then `h`, `i` and
   a line break: ten bytes. The id is
   `45b983be36b73c0788dc9cbcb76cbb80fc7bb057` on every laptop. With a Windows line ending,
   `0d 0a`, the header says `blob 4`, and the id is
   `edf0effbb6851d0055229878b4bf0d7212167642`.*
7. A repository has 40 commits. `weather.csv` (2 515 215 bytes) was added in
   the first one and never changed. How often is its content stored?
   *Once. The content has one id, and each of the 40 trees names it.
   Compressed it takes 722 938 bytes.*
8. `git cat-file -p` of a commit prints two lines that begin with `parent`.
   What kind of commit is it?
   *A merge. It joins two histories.*
9. The message of your last commit has a typing error, and the commit is
   not pushed. What is the clean correction?
   *`git commit --amend -m` with the corrected message. The id changes:
   the corrected commit is a new commit, and the old one leaves the
   history.*
10. A colleague pushed a commit that edits a raw data file, and you have
   pulled it. How do you take it back?
   *`git revert` with the id of that commit, then push. Every history stays
   as it is and gains one commit.*
11. After `git clone`, the folder `data/processed` is missing, and
   `.gitignore` lists `data/processed/`. Why, and what brings it back?
   *Git stores files, not folders, and the files in it were ignored.
   `./scripts/rebuild.sh` makes the folder and its files again.*
12. On a new computer `git init` is followed by `git status`, which says
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
copies, the drawn three areas and the drawn remote (then replaced by
Software Carpentry figures), and *Read a Commit, Trace a Line* (`git show`
and `git blame` now come where they answer the opening question).

On 27 October 2026, after the first delivery ("too difficult"), the deck
was reworked around add, commit and push, one picture each, and around two
ways to work together. Branches on one laptop (a fast-forward merge of
`ranges`, a conflict between the branches `wording` and `main`) and
*Ahead and Behind* left the deck: the branch now comes with the fork, and
the conflict with a pull. Amend, rebuilding a clone, the revert of
Tomas's edit, the tag, the map of the commands, the data sizes,
`.gitattributes`, the status table and the error messages moved to More
Commands.

## Take-aways

- Two copies show that a line differs. Who changed it, when and why is
  kept only by a history.
- A commit keeps every staged file, the commit before it, who, when and
  why. Its id is a checksum of all of it: the same on every copy of the
  repository, and another id for any other content.
- `git add` puts a file, as it is saved at that moment, into the next
  commit; `git commit` keeps the staged files in the history, on the
  laptop; `git push` sends the commits to GitHub. Until the push nobody
  else sees anything, and a lost laptop takes it with it.
- One commit has one purpose, and its message says what it does.
- Small raw data goes into the repository. Files a script makes again stay
  out by `.gitignore`.
- `git restore` takes back an edit, `git revert` takes back a commit by a
  new one.
- A remote is a second copy of the repository. Pull before you start, push
  when you stop.
- Two ways to work together: a shared repository that everyone pushes to,
  or a fork and a pull request that the owner reviews and merges. A
  refused push means GitHub has a commit you lack: pull, then push. A
  conflict means that the same lines were changed twice; a person decides.
- A result that leaves the project carries the id of its commit.
- For the curious: Git names a content by the SHA-1 of a short header and
  its bytes, keeps a folder as a tree and a commit as a short text, and a
  branch is a name for one commit.
