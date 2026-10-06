# 5: Version Control with Git

Lecture 4 ended with a README that holds the size and the SHA-256 of the
cleaned pendulum table, so the checksum says which copy of the table the
README means. Lecture 5 opens on two copies of that table, saved on 13 and on
20 October: the checksum says that they differ, `git diff` says which line,
and nothing in either folder says who changed it, when, or why. The tool that
keeps that third answer is Git. The lecture first builds what Git stores, from
the checksums of Lecture 4, and then gives the commands, each one in the
Source Control view of VS Code and typed. It closes on the same three
questions, answered from the history of the project.

## What the lecture covers

1. **Two copies of the table** — two copies of `pendulum.csv` with 97 bytes
   each and two checksums; `git diff --no-index` finds line 2, `9.02`
   against `9.03`; the third question, who, when and why, stays open. Copies
   with names like `final_v2`, and what a version control system records.
2. **The model** — what has to be kept; a name computed from the content
   with `git hash-object`, and why the same line gives another id in
   PowerShell (`0d 0a`); the header `blob <size>` and a zero byte; the id of
   the data file, the same on every laptop; a folder as a list, set beside
   the `data/checksums.txt` of Lecture 4; lists inside lists; a commit as a
   text with a tree, a parent, an author and a message; the id of a commit,
   computed again by `git hash-object`; history as a graph; a branch as a
   file of 41 bytes; the three areas.
3. **First commits** — the check of Git, three settings; the Source Control
   view; `git init`; `git status` and the letters `U`, `A`, `M`, `D`, `!`;
   stage and commit; the commit message.
4. **Data in a repository** — which files go in; why a file of 3.9 MB fits
   and one of 3 GB does not, with measured sizes; a `.gitignore` for the two
   files that the README's lines make again; the README says how to fetch
   the original ROOT file.
5. **Changes and history** — the diff in the view and typed; `git log`, the
   Graph and the Timeline; `git show` and `git blame`.
6. **Undoing** — `git restore` for an edit; the change `9.02` to `9.03`
   committed, `--amend` for its message, `git revert` to take it back;
   `git stash`.
7. **Remotes** — what a remote is; a GitHub account; publishing from VS
   Code; `git remote`, `git push`, `git clone`, `git pull`; one table with
   two line endings; a clone on Windows with `core.autocrlf true`; SSH as the
   alternative to HTTPS.
8. **Branches and merging** — creating a branch; a fast-forward merge; two
   branches that both changed; a conflict, resolved in the editor and
   typed; ahead and behind; the usual error messages; a table of every step
   in Source Control and typed.
9. **Working with others** — pull requests, the review loop, giving and
   receiving review, issues, forks, GitLab at CERN.
10. **A result and its commit** — a tag; the three questions of the start,
    answered from `git log`.

## The lecture in 90 minutes

The lecture is slides 1–71 and estimates about 142 min. Slides 72–81 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | Two copies of the table, the three questions |
| 0:12 | 8–19 | The model: blob, tree, commit, branch, three areas |
| 0:38 | 20, 21, 23, 25 | The check of Git, three settings, the first commit |
| 0:47 | 28, 29, 31, 32 | Data in a repository, `.gitignore` |
| 0:54 | 34, 37 | The history |
| 0:57 | 39, 41, 42 | The `9.03` change, amended and reverted: who, when and why |
| 1:01 | 44, 45, 47–49 | A remote, publish, push, clone, pull |
| 1:11 | 50, 51 | One table with two line endings, a clone on Windows |
| 1:16 | 53–58 | A branch, a merge, a conflict |
| 1:27 | 68–70 | A tag; the three questions, answered |
| 1:32 | 71 | Recap |
| 1:33 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Source Control in VS Code: say it while doing slide 23 | 22 | 1 min |
| What Git Sees, The Letters, The Commit Message | 24, 26, 27 | 5 min |
| 3.9 MB Fits; the README says how to fetch | 30, 33 | 5 min |
| The diff in the view and typed; show and blame | 35, 36, 38 | 7 min |
| restore; stash. The seminar does restore | 40, 43 | 4 min |
| A GitHub Account: students create one in the break | 46 | 2 min |
| SSH: the Alternative | 52 | 2 min |
| Resolve It, Typed; Ahead and Behind; When Git Says No | 59–61 | 6 min |
| Source Control and Commands: on the projector during the seminar | 62 | 2 min |
| Working with Others | 63–67 | 9 min |

- **The third question is answered by about minute 60**, at slides 41–42:
  the change of line 2 is a commit with an author, a time and a message,
  and the revert that took it back is another.
- **Do not cut slide 70**, *The Three Questions, Answered*. It closes the
  lecture on the question of slides 4–5.
- **Do not cut** slides 9–19 (the model). Each of them needs the one before
  it, and slides 30, 41, 45 and 59 argue from it.
- **Slides 4–5 need two folders** next to the project: `13oct/` with the
  cleaned `pendulum.csv` and `20oct/` with the same file with line 2 changed
  to `20,9.03`. Both have 97 bytes.
- **Slides 10–12 are done live** in the terminal. They need no repository.
  Type slide 10 in zsh and in PowerShell if both are at hand: `ce01…` and
  `ef04…`. Let the room type the line of slide 12 in their project folder and
  read the first digits aloud: `4a45f2be` in both shells.
- **Slides 13–18 show a repository that exists already.** Either read them
  from the slide, or keep a second copy of your project that has three
  commits and type the commands there with its ids.
- **Slide 21 is typed by the room.** The three settings have to be on every
  laptop before the seminar. Git for Windows comes with `core.autocrlf true`;
  slide 51 shows what that does to the data file.
- **Slides 23, 25, 31, 35, 40, 47, 54 and 58 are done live** in VS Code, in
  the Source Control view. After each, type the command of the slide in the
  terminal and let the room compare.
- **Slides 41–42 are the change of the opening.** Edit line 2 of
  `data/processed/pendulum.csv` to `20,9.03`, commit it with the typo, amend,
  then revert it.
- **Slide 47 needs your GitHub sign-in.** Do it once before the lecture on
  the laptop you present from, and delete the repository `analysis-project`
  on GitHub afterwards.
- **Slide 46**: students without an account create one during the break.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/05-version-control/`.

## The outputs on the slides

Every command on the slides was run in a scratch repository, and the output
is copied from the terminal. The project in it is the folder as it stands
after Seminar 4: `README.md` with the size and the SHA-256 of the table,
`data/raw/D0_KPi.csv` and `data/raw/pendulum.csv`, `data/processed/` with
`pendulum.csv`, `pendulum_script.csv` and `D0_valid.csv`,
`data/checksums.txt`, `scripts/hello.py`, `scripts/clean_pendulum.py` and
`scripts/column_stats.py`, and `results/` with the report and the plot. The
git lines are the same in zsh and in PowerShell; where the output differs,
both shells were run.

- **Blob ids are the same for everyone.** `D0_KPi.csv` is
  `4a45f2be5e087d6b6dccd287fe1bfd36fe659aeb` on every laptop, in both shells,
  and the tree of `data/raw` is `dba72972…`.
- **Commit ids differ.** A commit contains its author and its time. The ids
  on the slides belong to commits dated 20 October 2026 with the lecturer's
  name. Your live demo gives other ids. The tree and commit ids from
  `01fb5c2` on also depend on the exact bytes of every committed file, such
  as the handed-out `clean_pendulum.py`.
- **The address in the push and clone outputs** was put in by hand. The
  commands ran against a repository in a local folder, and the line that
  begins with `To` showed its path. The other lines are as printed.
- **The Windows outputs** (slides 4, 10, 51) are from a Windows laptop with
  PowerShell 7.6 and Git 2.51.0.windows.1 as installed, whose system
  configuration sets `core.autocrlf true` and `init.defaultBranch master`.
- **Compressed sizes** (1 906 370 bytes for the blob, 1.68 MiB for the first
  push, 2.0 MB for `.git`) are those of Git for Windows. A Git built with
  another zlib, as on some Linux systems, gives about 1.81 MB for the blob.
- **The pictures of VS Code** are from version 1.139 with the theme Dark
  Modern, on macOS. The box for the message reads `Ctrl+Enter` on Windows.
- **A Git that prints 64 digits.** Git 3.0 is announced to make SHA-256 the
  hash of new repositories. If a student's `git hash-object` prints 64 hex
  digits, the header of slide 11 is hashed with SHA-256 in place of SHA-1:
  `echo "hello"` in zsh then gives `2cf8d83d…6db9ebb4`. In such a repository
  a branch is also no longer a file under `.git/refs/heads`: use
  `git rev-parse main` for slide 18.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 72–81: nine quiz slides for students to try afterwards. The same
questions, with their answers:

1. A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and
   `analysis_final_REAL.py` side by side. What does Git give that these
   copies do not?
   *One file with its full history: what changed, when, and why.*
2. In zsh, `echo "hi" | git hash-object --stdin` prints an id. Which bytes
   did Git hash?
   *The word `blob`, a space, the digit 3 and a zero byte, then `h`, `i` and
   a line break: ten bytes. The id is
   `45b983be36b73c0788dc9cbcb76cbb80fc7bb057` on every Mac. PowerShell on
   Windows sends `h`, `i`, `0d`, `0a`: the header says `blob 4`, eleven
   bytes are hashed, and the id is
   `edf0effbb6851d0055229878b4bf0d7212167642`.*
3. A repository has 40 commits. A data file of 3 926 142 bytes was added in
   the first one and never changed. How often is its content stored?
   *Once. The content has one id, and each of the 40 trees names it.*
4. `git cat-file -p` of a commit prints two lines that begin with `parent`.
   What kind of commit is it?
   *A merge. It joins two histories.*
5. The message of your last commit has a typing error, and the commit is
   not pushed. What is the clean correction?
   *`git commit --amend -m` with the corrected message. The id changes,
   because the message is part of the hashed text.*
6. On a new computer `git init` is followed by `git status`, which says
   `On branch master`. Why?
   *`init.defaultBranch` is not set to `main` there, so Git uses `master`:
   its old default name, which Git for Windows also writes into its own
   configuration. `git branch -m main` renames the branch.*
7. Your branch corrects a plot, renames three functions and adds a script,
   three things that have nothing to do with each other. How do you open
   the pull request?
   *As three requests, one for each change.*
8. You want to correct a fault in a package whose repository you may read
   and not write. Which way works?
   *Fork it, commit on a branch of the fork, open a pull request to the
   original.*
9. An edit is half done when a fault on `main` has to be corrected at once.
   What do you do?
   *`git stash`, correct the fault and commit it, then `git stash pop`.*

## Paired seminar

[Seminar 5 — The Project Folder under Git](../seminars/seminar_05.md) puts
the project folder of the course under Git. The room makes the first commits
in the Source Control view, writes a `.gitignore` for the two files that a
command of the README can make again, and repeats the steps typed. Each
student creates a GitHub account, publishes the repository as a private one
and pushes to it. The session ends with a branch, a merge and one conflict.

## Take-aways

- A checksum says that two copies differ, and `git diff` says which line.
  Who changed it, when and why is kept only by a history.
- Git names a content by the SHA-1 of a short header and its bytes. The
  same bytes have the same id on every computer, and a content is stored
  once. A line ending is one of the bytes: `0a` and `0d 0a` give two ids.
- A tree is the list of a folder, like the list of checksums of Lecture 4. A
  commit is a text that names a tree, a parent, an author, a time and a
  reason. Its id is a checksum of the whole project and of every version
  before it.
- A branch is a name for a commit. A new commit moves the name.
- A commit is made in two steps: stage, then commit. One commit has one
  purpose, and its message says what it does.
- Small raw data goes into the repository. Large data and files that a
  command can make again stay out, by `.gitignore`, and the README says how
  to fetch or rebuild them.
- `core.autocrlf false` keeps the bytes of every file. With `true`, a clone
  on Windows adds a `0d` to every line, and the checksums of Lecture 4 fail
  while `git status` reports no change.
- `git restore` takes back an edit, `--amend` corrects the last commit
  before it is pushed, `git revert` takes back a commit by a new one.
- A remote is a second copy of the repository. Pull before you start, push
  when you stop.
- A conflict means that one line was changed twice. A person decides.
- A result that leaves the project carries the id or the tag of its commit.
