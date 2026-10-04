# 5: Version Control with Git

Lecture 4 made the terminal a place where a step is written down and
repeated, and it ended with a README that says how every file of the project
is made. Lecture 5 adds time: every state the project goes through is kept,
with who changed what, when and why. The tool is Git. The lecture first
builds what Git stores, from the hash of Lecture 3, and then gives the
commands, each one in the Source Control view of VS Code and typed.

## What the lecture covers

1. **Why** — copies with names like `final_v2`; what a version control
   system records; two lines of work that are joined; a check that Git is
   installed, and three settings typed on every laptop.
2. **The model** — what has to be kept; a name computed from the content
   with `git hash-object`; the same number computed without Git, as the
   SHA-1 of a header and the bytes; the id of the data file, the same on
   every laptop; a folder as a list (tree); a commit as a text with a tree,
   a parent, an author and a message; the id of a commit computed by hand;
   history as a graph; a branch as a file of 41 bytes; the three areas.
3. **First commits** — the Source Control view; `git init`; `git status`
   and the letters `U`, `A`, `M`, `D`, `!`; stage and commit; the commit
   message.
4. **Data in a repository** — which files go in; why a file of 3.9 MB fits
   and one of 3 GB does not, with measured sizes; `.gitignore`; the README
   says how to fetch what is left out.
5. **Changes and history** — the diff in the view and typed; `git log`,
   the Graph and the Timeline; `git show` and `git blame`.
6. **Undoing** — `git restore` for an edit, `--amend` for the last commit,
   `git revert` for an older one.
7. **Remotes** — what a remote is; a GitHub account; publishing from VS
   Code; `git remote`, `git push`, `git clone`, `git pull`; SSH as the
   alternative to HTTPS.
8. **Branches and merging** — creating a branch; a fast-forward merge; two
   branches that both changed; a conflict, resolved in the editor and
   typed; ahead and behind.
9. **Working with others** — pull requests, the review loop, giving and
   receiving review, issues, forks, GitLab at CERN.
10. **Tags and stash**, the usual error messages, the whole picture, and a
    table of every step in Source Control and typed.

## The lecture in 90 minutes

The lecture is slides 1–67 and estimates about 130 min. Slides 68–77 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–5, 7 | Copies and versions, the check of Git, three settings |
| 0:10 | 8–18 | The model: blob, tree, commit, branch, three areas |
| 0:33 | 19–23, 25 | The first commit, in Source Control and typed |
| 0:44 | 26–31 | Data in a repository, `.gitignore`, the README |
| 0:56 | 32–35 | A diff, the history |
| 1:03 | 37, 38, 40 | Undoing: restore and revert |
| 1:08 | 41–46 | A remote, a GitHub account, push, clone, pull |
| 1:20 | 48–53 | A branch, a merge, a conflict |
| 1:31 | 67 | Recap |
| 1:33 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Two Lines of Work, Joined | 6 | 2 min |
| The Letters in Source Control | 24 | 2 min |
| show and blame | 36 | 2 min |
| Correct the Last Commit: amend. The seminar does it | 39 | 2 min |
| SSH: the Alternative | 47 | 2 min |
| Resolve It, Typed; Ahead and Behind | 54–55 | 4 min |
| Working with Others | 56–60 | 10 min |
| Tags & Stash | 61–63 | 5 min |
| When Git Says No, The Whole Picture | 64–65 | 5 min |
| Source Control and Commands: on the projector during the seminar | 66 | 2 min |

- **Do not cut** slides 9–17 (the model). Each of them needs the one before
  it, and slides 28, 39, 42 and 54 argue from it.
- **Slide 7 is typed by the room.** The three settings have to be on every
  laptop before the seminar. Without `core.autocrlf false`, Git for Windows
  writes CRLF line endings into every file it puts into the working folder:
  a clone then holds a `D0_KPi.csv` of 4 017 726 bytes in place of
  3 926 142, and its checksum fails.
- **Slides 10–12 are done live** in the terminal. They need no repository.
  Let the room type the first command of slide 12 in their project folder
  and read the first digits aloud: `4a45f2be` on every laptop.
- **Slides 13–17 show a repository that exists already.** Either read them
  from the slide, or keep a second copy of your project that has three
  commits and type the commands there with its ids.
- **Slides 20–23, 29, 33, 38, 44, 49 and 53 are done live** in VS Code, in
  the Source Control view. After each, type the command of the slide in the
  terminal and let the room compare.
- **Slide 44 needs your GitHub sign-in.** Do it once before the lecture on
  the laptop you present from, and delete the repository `analysis-project`
  on GitHub afterwards.
- **Slide 43**: students without an account create one during the break.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/05-version-control/`.

## The outputs on the slides

Every command on the slides was run in a scratch repository, and the
output is copied from the terminal. The project in it is the folder as it
stood after Seminar 3, with `scripts/hello.py` from the homework. The room's
folder has more files after Seminar 4, so its lists are longer.

- **Blob ids are the same for everyone.** `D0_KPi.csv` is
  `4a45f2be5e087d6b6dccd287fe1bfd36fe659aeb` on every laptop.
- **Commit ids differ.** A commit contains its author and its time. The ids
  on the slides belong to commits dated 20 October 2026 with the lecturer's
  name. Your live demo gives other ids.
- **The address in the push and clone outputs** was put in by hand. The
  commands ran against a repository in a local folder, and the line that
  begins with `To` showed its path. The other lines are as printed.
- **The pictures of VS Code** are from version 1.139 with the theme Dark
  Modern, on macOS. The box for the message reads `Ctrl+Enter` on Windows.
- **A Git that prints 64 digits.** Git 3.0 is announced to make SHA-256 the
  hash of new repositories. If a student's `git hash-object` prints 64 hex
  digits, the recipe of slide 11 holds with `shasum -a 256` (Git Bash:
  `sha256sum`): `echo "hello"` then gives `2cf8d83d…6db9ebb4`. In such a
  repository a branch is also no longer a file under `.git/refs/heads`:
  use `git rev-parse main` for slide 17.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 68–77: nine quiz slides for students to try afterwards. The same
questions, with their answers:

1. A student keeps `analysis.py`, `analysis_v2.py`, `analysis_final.py` and
   `analysis_final_REAL.py` side by side. What does Git give that these
   copies do not?
   *One file with its full history: what changed, when, and why.*
2. `echo "hi" | git hash-object --stdin` prints an id. Which bytes did Git
   hash?
   *The word `blob`, a space, the digit 3 and a zero byte, then `h`, `i` and
   a line break: nine bytes. The id is
   `45b983be36b73c0788dc9cbcb76cbb80fc7bb057` on every computer.*
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
   *`init.defaultBranch` is not set there, so Git uses its old default
   name. `git branch -m main` renames the branch.*
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

- Git names a content by the SHA-1 of a short header and its bytes. The
  same bytes have the same id on every computer, and a content is stored
  once.
- A tree is the list of a folder. A commit is a text that names a tree, a
  parent, an author, a time and a reason. Its id fixes the whole project
  and the whole history before it.
- A branch is a name for a commit. A new commit moves the name.
- A commit is made in two steps: stage, then commit. One commit has one
  purpose, and its message says what it does.
- Small raw data goes into the repository. Large data and files that a
  command can make again stay out, by `.gitignore`, and the README says how
  to fetch or rebuild them.
- The diff is read before every commit.
- `git restore` takes back an edit, `--amend` corrects the last commit
  before it is pushed, `git revert` takes back a commit by a new one.
- A remote is a second copy of the repository. Pull before you start, push
  when you stop.
- A conflict means that one line was changed twice. A person decides.
- A result that leaves the project carries the id or the tag of its commit.
