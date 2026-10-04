# Seminar 5 — The Project Folder under Git

**Paired lecture:** 05 Version Control with Git · **Format:** follow-along · **~120 min**
in class, 30 min at home

The seminar has four parts, in this order.

1. **A repository.** The project folder gets a repository. The first commits
   are made in the Source Control view of VS Code, and a `.gitignore` keeps
   out the files that a command can make again.
2. **Changes, typed.** A change is read as a diff and committed, once in the
   view and once in the terminal. An edit and a commit are taken back.
3. **A remote.** Every student gets a GitHub account, publishes the
   repository as a private one and pushes a commit to it.
4. **A branch and a merge.** One merge that needs no decision, and one with
   a conflict that is resolved in the editor.

Each step is done in the Source Control view first and typed afterwards, as
in the lecture. The new tools of the session are Git and GitHub. Everything
else is VS Code and the terminal of Seminar 4. No Python is needed.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows, with macOS in brackets. Commands are the same
on every laptop: Windows types them in Git Bash, the terminal that VS Code
has opened since Seminar 4. Where a command differs between systems, both
forms are given.

Every commit has an id, such as `9672bf7`. The ids on this page are those of
one run of the steps. **Your ids differ**, and so do those of every student:
a commit contains its author and its time. Blob ids of the same file are the
same everywhere.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · A repository** · 35 min | |
| 0:00 | [1. Check Git](#check) | Five settings, and one id that is the same on every laptop |
| 0:10 | [2. Create the repository](#init) | A first commit with the README |
| 0:20 | [3. Ignore, then commit the rest](#ignore) | Three commits and a clean working folder |
| | **Part 2 · Changes, typed** · 30 min | |
| 0:35 | [4. A change in Source Control](#change) | A diff read and committed |
| 0:45 | [5. The same, typed](#typed) | A commit made with four commands |
| 0:55 | [6. Undo](#undo) | An edit discarded, a commit message corrected |
| | **Part 3 · A remote** · 25 min | |
| 1:05 | [7. A GitHub account](#account) | An account, signed in |
| 1:15 | [8. Publish and push](#publish) | The project on GitHub, as a private repository |
| | **Part 4 · A branch and a merge** · 30 min | |
| 1:30 | [9. A branch](#branch) | A change made on a branch and merged |
| 1:40 | [10. A conflict](#conflict) | A conflict resolved, a history with two lines |
| 1:55 | [11. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, do Parts 1 to 3 and go to the wrap-up. Part 4 then opens
the next session, or is done at home from this page.

## Prerequisites

For the room: the project folder as [Seminar 4](seminar_04.md) left it, with
`data/checksums.txt`, `scripts/clean_pendulum.sh`, `results/report.md` and a
README that has a section **How to rebuild**. Git installed and the name and
e-mail set, as in [Install Python and Git](install_python_git.md). A mailbox
that can be opened in class, for the code that GitHub sends.

For you, before the session:

- A GitHub account of your own, and a project folder that is **not** a
  repository yet. If yours is one, delete its `.git` folder, and delete the
  repository `analysis-project` on GitHub.
- Sections 8 to 10 done once on your own laptop. Section 8 depends on the
  sign-in of your system, and the first time takes longer.
- In VS Code, the terminal in the Panel and the Source Control view both
  visible: the room has to see that a button and a command do the same.
- The lecture slide *Source Control and Commands* ready. It stays on the
  projector while the room works.

## Part 1 · A repository { #part-1 }

**0:00 to 0:35 · sections 1 to 3**

The room ends this part with the whole project in three commits, made with
the mouse. Nothing leaves the laptop yet.

## 1. Check Git { #check }

**0:00 · 10 min**

Git was installed at home and told a name and an e-mail address. Three more
settings are made now, on every laptop, so that Git behaves the same in the
whole room. Then one command shows what the lecture derived: Git names a
content by a hash of its bytes.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**.

2. Ask Git for its version and for the two settings of the homework.

    ```text
    git --version
    git config --global user.name
    git config --global user.email
    ```

    Three lines come back: a version, a name, an address. An empty answer
    means the setting is missing. Set it now:

    ```text
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```

3. Type three more settings. None of them prints anything.

    ```text
    git config --global init.defaultBranch main
    git config --global pull.rebase false
    git config --global core.autocrlf false
    ```

    | Setting | What it does |
    |--|--|
    | `init.defaultBranch main` | The first branch of a new repository is named `main` |
    | `pull.rebase false` | `git pull` joins two histories by a merge |
    | `core.autocrlf false` | Git leaves line endings alone. Every file keeps its bytes |

4. Read the settings back.

    ```text
    git config --global --list
    ```

    ```text
    user.name=Mindaugas Sarpis
    user.email=mindaugas.sarpis@cern.ch
    init.defaultbranch=main
    pull.rebase=false
    core.autocrlf=false
    ```

5. Ask Git for the id of the data file.

    ```text
    git hash-object data/raw/D0_KPi.csv
    ```

    Read the first eight digits aloud: `4a45f2be`.

You should now see five settings, and the id
`4a45f2be5e087d6b6dccd287fe1bfd36fe659aeb` on every laptop.

Say why the third setting matters. Git for Windows is installed with
`core.autocrlf` switched on. It then writes CRLF line endings into every
text file it puts into the working folder. `D0_KPi.csv` would grow from
3 926 142 to 4 017 726 bytes, the checksums of Seminar 4 would fail, and
`clean_pendulum.sh` would stop with `command not found`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `git: command not found` | Git is not installed, or VS Code was open during the installation. Close VS Code and start it again |
    | Windows: the prompt ends in `>` | The terminal is PowerShell. Select **Git Bash** in the list beside the `+` of the Panel |
    | The list of settings is longer | Other programs wrote settings too. The five lines have to be among them |
    | Another id for `D0_KPi.csv` | The file is not the one that was downloaded. Check it with `data/checksums.txt`, as in Seminar 4 |

## 2. Create the repository { #init }

**0:10 · 10 min**

A repository is the project folder together with a hidden folder `.git` that
holds every commit. It is made once. The first commit holds one file, the
README, so that the room sees the two steps of every commit: stage, then
commit.

1. Press `Ctrl+Shift+G` (the same keys on macOS), or select the third icon
   of the Activity Bar. This is the **Source Control** view.

2. Select **Initialize Repository**. The view now lists every file of the
   project under **Changes**. Each has the letter `U`: Git sees the file and
   has no version of it.

3. Move the mouse over `README.md` and select the **+** on its row. The file
   moves to a new group, **Staged Changes**, and its letter turns to `A`.

4. Click into the box above the **Commit** button and type the message.

    ```text
    Add the README
    ```

5. Select **Commit**. `README.md` leaves the view. At the bottom of the
   view, under **Graph**, the commit appears with its message and your name.

6. Type in the terminal:

    ```text
    git log --oneline
    ```

    ```text
    9672bf7 (HEAD -> main) Add the README
    ```

You should now see one line from `git log`, with seven digits of your own,
and the other files still listed under **Changes**.

Say what happened in the terms of the lecture. The button made the folder
`.git`. The **+** copied the content of the README into the staging area.
**Commit** wrote a tree and a commit, and `main` is the name of that commit.
Show the folder: `ls -a` lists `.git`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The view offers **Open Repository** in place of **Initialize Repository** | A folder above the project is a repository already, often the home folder. Do not open it. Call the lecturer |
    | A dialog: *There are no staged changes to commit* | Nothing was staged. Select **Cancel** and do step 3 |
    | A tab named `COMMIT_EDITMSG` opens | The message box was empty. Type the message into line 1 of that tab and select the check mark at its top right |
    | A dialog about `user.name` and `user.email` | Section 1, step 2 |
    | `git log` says `master` | The repository was made before the setting of section 1. Type `git branch -m main` |

## 3. Ignore, then commit the rest { #ignore }

**0:20 · 15 min**

Not every file belongs in the repository. `data/processed/D0_valid.csv` has
3.9 MB and is written by one command that stands in the README. The command
is kept and the file is left out. The file `.gitignore` lists what Git has
to leave out. It is a file of the project and is committed like the others.

1. Go to the Explorer, select the empty area below the folders, then
   **New File**, and type `.gitignore`. The name begins with a dot and has
   no ending.

2. Type into the file and save.

    ```text
    # made by the operating system
    .DS_Store
    Thumbs.db

    # made by the commands in README.md
    data/processed/D0_valid.csv
    data/processed/pendulum_script.csv
    ```

3. Go back to Source Control. The two files of `data/processed` have left
   the list, and `.gitignore` is in it.

4. Stage `.gitignore` with its **+**, type the message `Add .gitignore` and
   select **Commit**.

5. Move the mouse over the header **Changes** and select the **+** on that
   row. It stages every file at once. Read the list with the room:
   `D0_KPi.csv` is in it, `D0_valid.csv` is not.

6. Type the message and select **Commit**.

    ```text
    Add the data, the report and the scripts
    ```

7. Type in the terminal:

    ```text
    git status
    git log --oneline
    git status --ignored
    ```

    ```text
    On branch main
    nothing to commit, working tree clean
    ```

    ```text
    2b37a62 (HEAD -> main) Add the data, the report and the scripts
    82e1b35 Add .gitignore
    9672bf7 Add the README
    ```

    ```text
    Ignored files:
      (use "git add -f <file>..." to include in what will be committed)
            data/processed/D0_valid.csv
            data/processed/pendulum_script.csv
    ```

You should now see an empty **Changes** list, three commits, and the two
ignored files named by `git status --ignored`.

Say the rule in these words: a file written by hand goes in, because nothing
can make it again. A file that a command writes may stay out, if the command
is in the repository. `du -sh .git` shows what the three commits cost:
about 2.0 MB for a project of 3.9 MB, because Git compresses.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The two files are still listed | A path in `.gitignore` is mistyped, or the file was saved as `.gitignore.txt` or inside a subfolder |
    | A student's own dataset in `data/raw` has more than 50 MB | Add its path to `.gitignore` before step 5. GitHub refuses a file above 100 MB |
    | macOS: `.DS_Store` among the ignored files | Correct. The Finder makes it |
    | A file was committed that should stay out | `git rm --cached <file>`, add its path to `.gitignore`, commit both |

## Part 2 · Changes, typed { #part-2 }

**0:35 to 1:05 · sections 4 to 6**

The room changes a file, reads the change and commits it: once with the
mouse, once with four commands. Then two ways to take something back.

## 4. A change in Source Control { #change }

**0:35 · 10 min**

Git compares the working folder with the last commit. A file that differs
gets the letter `M`, and the diff shows what differs, line by line. The diff
is read before every commit: it is what the commit will contain.

1. Open `results/report.md` and change the first sentence to:

    ```text
    Time of 10 swings of a pendulum for nine lengths.
    ```

    Save with `Ctrl+S` (macOS `Cmd+S`).

2. Go to Source Control. `report.md` stands under **Changes** with the
   letter `M`. Select it.

3. The **diff view** opens. The old line is red, the new line green, and
   the words that were added have a stronger green.

4. Stage the file with **+**, type the message and select **Commit**.

    ```text
    Name the pendulum in the report
    ```

5. Look at the **Graph**: four commits, the newest on top. Select the
   newest one, then the file under it. The same diff opens again.

You should now see four commits in the Graph, and the room can say what red
and green mean in a diff.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | No `M` appears | The file was not saved. A dot on the tab means *not saved* |
    | The whole file is red and green | The line endings changed. Select `CRLF` or `LF` in the Status Bar and put back what it was |
    | Two columns in place of red above green | The window is wide. VS Code then shows the two versions side by side |

## 5. The same, typed { #typed }

**0:45 · 10 min**

Every button of the last section runs a Git command. The room now types
them. A typed command can be written down, repeated, and used on a computer
that has no VS Code.

1. Open `README.md`. Under the line **Started** in the section **About**,
   add a line and save.

    ```text
    - **Under version control since:** 2026-10-20
    ```

2. Ask what changed.

    ```text
    git status
    ```

    ```text
    On branch main
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

3. Read the diff.

    ```text
    git diff
    ```

    The line with `+` in front is the new one. The lines without a sign
    around it are unchanged. If the output ends in a line with `:` or
    `(END)`, press `q`.

4. Stage, look again, commit.

    ```text
    git add README.md
    git status
    git commit -m "Note when version control started"
    ```

    ```text
    [main 2119c20] Note when version control started
     1 file changed, 1 insertion(+)
    ```

5. Read the history.

    ```text
    git log --oneline
    ```

    ```text
    2119c20 (HEAD -> main) Note when version control started
    3c3b3cd Name the pendulum in the report
    2b37a62 Add the data, the report and the scripts
    82e1b35 Add .gitignore
    9672bf7 Add the README
    ```

You should now see five commits, and after step 4 `git status` said
`Changes to be committed`.

Leave this table on the projector. It is the lecture slide
*Source Control and Commands*.

| In Source Control | Typed |
|--|--|
| The **Changes** list | `git status` |
| Select a changed file | `git diff` |
| **+** on a file | `git add <file>` |
| Message, then **Commit** | `git commit -m "…"` |
| **Graph** | `git log --oneline` |

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `fatal: not a git repository` | The terminal is not in the project folder. `pwd`, then `cd` |
    | The terminal fills with `~` signs | `git commit` was typed without `-m`, and Git opened the editor Vim. Type `:q!` and press Enter, then repeat with `-m` |
    | `dquote>` or `>` at the prompt | A quotation mark is missing. Press `Ctrl+C` and type the command again |

## 6. Undo { #undo }

**0:55 · 10 min**

Two things go wrong every week: a file is damaged by an edit that was not
meant, and a commit gets a message with a mistake. Git takes back both. The
room damages the report on purpose.

1. In `results/report.md` select the last five rows of the table, from
   `| 60 |` to `| 100 |`, delete them and save.

2. Ask Git how large the damage is.

    ```text
    git diff --stat
    ```

    ```text
     results/report.md | 5 -----
     1 file changed, 5 deletions(-)
    ```

3. In Source Control, move the mouse over `report.md` and select the bent
   arrow, **Discard Changes**. VS Code asks *Are you sure you want to
   discard changes in 'report.md'?* Select **Discard File**. The five rows
   are back. Typed, this is `git restore results/report.md`.

4. Now a commit with a mistake in its message. Add an empty line and this
   line at the end of `report.md`, and save.

    ```text
    Measured by a lab partner.
    ```

    ```text
    git add results/report.md
    git commit -m "Say who mesured"
    ```

5. Correct the message.

    ```text
    git commit --amend -m "Say who measured"
    git log --oneline -2
    ```

    ```text
    116be24 (HEAD -> main) Say who measured
    2119c20 Note when version control started
    ```

6. Look at the commit itself.

    ```text
    git cat-file -p HEAD
    ```

    ```text
    tree 4c2f32c77974c2430db09b2f84b34830eec30217
    parent 2119c20ad2c66b315d851f5ca8ad29a68ccf591c
    author Mindaugas Sarpis <mindaugas.sarpis@cern.ch> 1792497300 +0300
    committer Mindaugas Sarpis <mindaugas.sarpis@cern.ch> 1792497360 +0300

    Say who measured
    ```

You should now see six commits in `git log --oneline`, the last of them
with the corrected message, and a table of nine rows in the report.

Ask the room to compare the id of the commit before and after step 5. It
changed, from `e085933` to `116be24` in this run: the message is part of the
text that is hashed. That is why only a commit that has not left the laptop
is amended.

!!! warning "Watch for"
    A student discards an edit that was meant. Git has no copy of an edit
    that was never committed. `Ctrl+Z` in the editor brings it back as long
    as the tab is open.

## Part 3 · A remote { #part-3 }

**1:05 to 1:30 · sections 7 and 8**

The repository gets a second copy on GitHub. From here on the work survives
the loss of the laptop, and it can be fetched on another computer.

## 7. A GitHub account { #account }

**1:05 · 10 min**

GitHub is a hosting service for Git repositories. An account is free. Its
user name is public and part of every address, so it is chosen like a file
name: short, lowercase, without spaces, and fit to be shown to an employer.

1. Ask who has an account. Those students sign in at `github.com` in the
   browser and help a neighbour.

2. The others open `github.com` and select **Sign up**.

3. They enter an e-mail address, a password and a user name. Advise an
   address that outlives the studies.

4. GitHub sends a code to that address. They type it in.

5. They stay on the free plan and skip the questions about a team.

You should now see, on every laptop, a browser that is signed in to GitHub:
the picture of the account is at the top right.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The code does not arrive | Look in the spam folder. Until it arrives the student follows on a neighbour's screen |
    | The user name is taken | Add the initial of the first name, or a number |
    | A student will not make an account | Sections 8 to 10 work without one, except the publishing. The student skips section 8 |

## 8. Publish and push { #publish }

**1:15 · 15 min**

VS Code can create the repository on GitHub and send the commits in one
step. It signs in through the browser once and keeps the sign-in. The
repository is made **private**: only its owner sees it.

1. In Source Control the button now reads **Publish Branch**. Select it.

2. VS Code says *The extension 'GitHub' wants to sign in using GitHub*.
   Select **Allow**. The browser opens. Confirm there, and let the browser
   open VS Code again.

3. A list opens at the top of the window. Select
   **Publish to GitHub private repository**.

4. A note at the bottom right confirms the publishing. Select
   **Open on GitHub**. The browser shows the project: the folders, the
   number of commits, and the README as formatted text below them.

5. Ask Git where the remote is.

    ```text
    git remote -v
    git status
    ```

    ```text
    origin  https://github.com/<user>/analysis-project.git (fetch)
    origin  https://github.com/<user>/analysis-project.git (push)
    ```

    ```text
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

6. Make one more commit, typed. Add this line at the end of the section
   **About** in `README.md` and save.

    ```text
    - **Repository:** private, on GitHub
    ```

    ```text
    git add README.md
    git commit -m "Say where the repository is"
    git status
    ```

    `git status` now says
    `Your branch is ahead of 'origin/main' by 1 commit.`

7. Send the commit, and reload the page in the browser.

    ```text
    git push
    ```

    The last line of the answer has two ids and the branch:
    `116be24..e0f45a9  main -> main`. In the view the same step is the
    button **Sync Changes**.

You should now see the new line of the README in the browser, and
`Your branch is up to date with 'origin/main'.` from `git status`.

Say what a push sends: the objects the remote does not have yet. Here that
is one commit, one tree and one blob, 339 bytes in this run. The data file
is not sent again.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The browser does not return to VS Code | Select **Open Visual Studio Code** in the dialog of the browser, or copy the code it shows into VS Code |
    | `git push` asks for a user name and a password | The terminal is not the one inside VS Code. Press `Ctrl+C`, and push from the terminal of VS Code or with **Sync Changes** |
    | A name `analysis-project` exists already on the account | Choose another name in the list of step 3 |
    | The repository was published as public | On its page: **Settings**, at the bottom **Change visibility** |

## Part 4 · A branch and a merge { #part-4 }

**1:30 to 1:55 · sections 9 and 10**

A branch is a name for a commit. A second name lets work go on apart from
`main` until it is good. The room merges twice: once where Git has nothing
to decide, once where both branches changed the same line.

## 9. A branch { #branch }

**1:30 · 10 min**

The table of the report has the column names of the data file as its header.
A report needs words and units. The change is made on a branch.

1. Select the branch name `main` at the left end of the Status Bar. A list
   opens at the top. Select **Create new branch...**, type `table-units`
   and press Enter. The Status Bar now reads `table-units`.

2. In `results/report.md` replace the header line of the table and save.

    ```text
    | Length (cm) | Time of 10 swings (s) |
    ```

3. Stage and commit in Source Control, with the message:

    ```text
    Write the units into the table header
    ```

4. Select `table-units` in the Status Bar and select `main` in the list.
   Look at the report: the header is `| length_cm | t10_s |` again. The
   working folder now holds the snapshot of `main`.

5. Move the mouse over the header **Changes** and select **...** on that
   row, then **Branch** > **Merge...**, and select `table-units`. The
   header with the units is back.

6. Type in the terminal:

    ```text
    git log --oneline -3
    git branch -d table-units
    ```

    ```text
    6de9899 (HEAD -> main, table-units) Write the units into the table header
    e0f45a9 (origin/main) Say where the repository is
    116be24 Say who measured
    ```

    ```text
    Deleted branch table-units (was 6de9899).
    ```

You should now see `main` and `table-units` on the same commit in the log,
one commit ahead of `origin/main`.

Say that this merge copied nothing. `main` had no commit of its own, so Git
moved the name `main` forward to the commit of the branch. Deleting the
branch deletes a name. The commit stays.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | After step 4 the header still has the units, and the file has the letter `M` | The change of step 2 was not committed, and Git carried it along to `main`. Go back to `table-units`, commit, and do step 4 again |
    | The list of step 5 is empty | The Status Bar still reads `table-units`. A branch is merged into the branch in use: do step 4 |

## 10. A conflict { #conflict }

**1:40 · 15 min**

Two branches now change the same line. Git cannot know which text is meant.
It writes both into the file and asks. This section is typed, and the
conflict is resolved in the editor.

1. Make a branch and reword the first sentence of the report on it.

    ```text
    git switch -c wording
    ```

    Change line 3 of `results/report.md` to the line below, and save.

    ```text
    Ten swings of a pendulum, timed for nine lengths.
    ```

    ```text
    git add results/report.md
    git commit -m "Reword the first sentence"
    ```

2. Go back to `main`. Line 3 is the old sentence again.

    ```text
    git switch main
    ```

    Change line 3 to the line below, and save.

    ```text
    Time of 10 swings of a pendulum for nine lengths from 20 cm to 100 cm.
    ```

    ```text
    git add results/report.md
    git commit -m "Give the range of lengths"
    ```

3. Merge.

    ```text
    git merge wording
    ```

    ```text
    Auto-merging results/report.md
    CONFLICT (content): Merge conflict in results/report.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```

4. Look at `results/report.md` in the editor. Lines 3 to 7 are:

    ```text
    <<<<<<< HEAD
    Time of 10 swings of a pendulum for nine lengths from 20 cm to 100 cm.
    =======
    Ten swings of a pendulum, timed for nine lengths.
    >>>>>>> wording
    ```

    Above `=======` is the line of `main`, below it the line of `wording`.

5. Select **Accept Incoming Change** above the block. The markers go and
   the line of `wording` stays. Add the range to it by hand, so that it
   reads as below, and save.

    ```text
    Ten swings of a pendulum, timed for nine lengths from 20 cm to 100 cm.
    ```

6. In Source Control the file stands under **Merge Changes** with the sign
   `!`. Stage it with **+** and select **Continue**. The message
   `Merge branch 'wording'` is already filled in.

7. Look at the history, delete the branch and push.

    ```text
    git log --oneline --graph -5
    git branch -d wording
    git push
    ```

    ```text
    *   7ab6617 (HEAD -> main) Merge branch 'wording'
    |\
    | * 6685eb2 (wording) Reword the first sentence
    * | c0a3c3c Give the range of lengths
    |/
    * 6de9899 Write the units into the table header
    * e0f45a9 (origin/main) Say where the repository is
    ```

You should now see a history that splits and joins, eleven commits in
`git log --oneline`, and in the browser the report with the new sentence.

Say it in these words: a conflict is not an error. Git reports that one
line was changed twice and leaves the decision to a person. Nothing is lost
before the decision, and `git merge --abort` goes back to the state before
the merge.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `Already up to date.` in step 3 | The branch `wording` has no commit of its own: the file was not saved before step 1 was committed, and Git said `nothing to commit`. Do step 1 again |
    | `merge: wording - not something we can merge` | The branch was never made. `git branch` lists the branches. Do step 1 again |
    | The markers are committed | The file was staged before it was edited. Remove the markers, save, commit again |
    | No button **Continue** | Type `git commit --no-edit` |
    | `git push` is refused with `(fetch first)` | A commit was made on the GitHub page. `git pull --no-edit`, then push |

## 11. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- A repository is the project folder with its `.git` folder. It is made
  once.
- A commit is made in two steps: stage, then commit with a message that
  says what the commit does.
- `.gitignore` names the files that stay out. A file that a command can
  make again need not be stored, if the command is.
- The diff is read before every commit.
- An edit is discarded with `git restore`. The last commit is corrected
  with `--amend`, as long as it has not been pushed.
- A remote is a second copy. `git push` sends commits, `git pull` fetches
  them.
- A branch is a name for a commit. A merge joins two histories, and a
  conflict is settled by a person.
- Every button of the Source Control view runs a Git command.

## Next steps, at home

**30 min, before the next session**

1. Look at the size of your own dataset with `ls -l data/raw`. If it has
   less than 50 MB, commit it. If it has more, add its path to `.gitignore`
   and write into the README where it comes from, how large it is and its
   SHA-256, as on the lecture slide *The README Says How to Fetch It*.

2. Make at least three commits on your own files this week, each with one
   purpose and a message that says it. Push after each.

3. Mark the state after this seminar with a tag, and push the tag.

    ```text
    git tag -a seminar-5 -m "State after Seminar 5"
    git push origin seminar-5
    ```

4. Do the first four levels of *Introduction Sequence* at
   [learngitbranching.js.org](https://learngitbranching.js.org/). They
   show commits, branches and merges as a moving picture.

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Compute the id of the data file without Git. The answer is the id of
  section 1, `4a45f2be…fe659aeb`.

    ```text
    (printf 'blob 3926142\0'; cat data/raw/D0_KPi.csv) | shasum
    ```

    Git Bash and Linux have `sha1sum` in place of `shasum`.

- `echo "hi" | git hash-object --stdin` prints
  `45b983be36b73c0788dc9cbcb76cbb80fc7bb057`. Ask which header Git put in
  front. The answer is `blob 3` and a zero byte: `hi` and a line break are
  three bytes.
- Find out which commit last changed each of the first five lines of the
  report: `git blame -s results/report.md | head -5`. The answer is three
  different ids: the commit that added the report for lines 1, 2 and 4, the
  merge commit for line 3, the commit of `table-units` for line 5.
- Clone your repository into a second folder and rebuild what is missing.
  Take the address from `git remote -v`.

    ```text
    cd ..
    git clone <address> check
    ls check/data/processed
    ```

    The answer is `pendulum.csv` alone: the two ignored files are not in
    the clone. Run commands 1 and 2 of **How to rebuild** inside `check`,
    then the checksum test of command 3. Both raw files print `OK`. Delete
    `check` afterwards.
- Set up an SSH key as on the lecture slide *SSH: the Alternative*, and
  change the address with `git remote set-url origin` and the address that
  begins with `git@github.com:`. `git push` then asks for no sign-in.
- Work in pairs. One invites the other on the GitHub page of the
  repository: **Settings** > **Collaborators**. The guest clones, makes a
  branch, pushes it and opens a pull request. The owner reads the diff and
  merges it.

## If students ask for more

| Topic | Week |
|--|--|
| Which Python files stay out of a repository | 6 (Python Foundations) |
| Data too large for a repository: Git LFS, DVC | 13 (Reproducible Workflows) |
| One command that rebuilds every ignored file | 13 (Reproducible Workflows) |
| Checks that run on every push | 13 (Reproducible Workflows) |

Leave out altogether, even if asked: `git rebase`, `git reset --hard`,
`git push --force`, submodules.

## Aims practised

♻️ every state of the project kept, with its reason · 🔧 the same commands in every editor and on every host · 📁 raw data in, rebuilt files out, by a written rule · ⚙️ a result tied to the commit that made it
