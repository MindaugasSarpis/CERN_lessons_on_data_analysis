# Seminar 5 — The Project Folder under Git

**Paired lecture:** 05 Version Control with Git · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student has the project folder under Git, with a
history of commits, a private copy on GitHub, and one merged branch.

The new tools are Git and GitHub. Each step is done in the Source Control
view of VS Code first and typed afterwards in the terminal of Seminar 4, as
in the lecture.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · A repository** · 35 min | | |
| 0:00 | [1. Check Git](#check) | `git config --global --list`, then `git hash-object` | Five settings, and `4a45f2be` on every laptop |
| 0:10 | [2. Create the repository](#init) | **Initialize Repository**, **+** on `README.md`, **Commit** | A first commit with the README |
| 0:20 | [3. Ignore, then commit the rest](#ignore) | `.gitignore`, then **+** on **Changes** | Three commits and a clean working folder |
| | **Part 2 · Changes, typed** · 30 min | | |
| 0:35 | [4. A change in Source Control](#change) | The diff of `report.md` | A diff read and committed |
| 0:45 | [5. The same, typed](#typed) | `git status`, `git diff`, `git add`, `git commit` | A commit made with four commands |
| 0:55 | [6. Undo](#undo) | **Discard Changes**, then `git commit --amend` | An edit discarded, a commit message corrected |
| | **Part 3 · A remote** · 25 min | | |
| 1:05 | [7. A GitHub account](#account) | `github.com`, **Sign up** | An account, signed in |
| 1:15 | [8. Publish and push](#publish) | **Publish Branch**, then `git push` | The project on GitHub, as a private repository |
| | **Part 4 · A branch and a merge** · 30 min | | |
| 1:30 | [9. A branch](#branch) | **Create new branch...** in the Status Bar | A change made on a branch and merged |
| 1:40 | [10. A conflict](#conflict) | `git merge wording` | A conflict resolved, a history with two lines |
| 1:55 | [11. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** leave out section 10, then section 9. No later
seminar uses a branch.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Commands are typed in the terminal of VS Code: `zsh` on macOS,
    **PowerShell 7** on Windows, as set up in Seminar 4. A line that starts
    with `git` is typed the same in both shells, so it stands once. Where a
    line differs, the step has a tab for **macOS** and one for **Windows**.
    The outputs were printed by `zsh`; Git prints the same lines in
    PowerShell 7. Keys are written for Windows, with macOS in brackets.

    Every commit has an id, such as `b7d67bc`. The ids on this page are those
    of one run of the steps. **Your ids differ**, and so do those of every
    student: a commit contains its author and its time. Blob ids of the same
    file are the same everywhere.

??? info "Before the session"
    For the room: the project folder as [Seminar 4](seminar_04.md) left it.
    The README has the line **Cleaned copy** with 97 bytes and the SHA-256,
    and a section **How to rebuild**. `data/raw` holds `D0_KPi.csv` and
    `pendulum.csv`, `data/processed` holds `pendulum.csv`,
    `pendulum_script.csv` and `D0_valid.csv`, and `data/checksums.txt` lists
    the raw files. `scripts` holds `hello.py`, `clean_pendulum.py` and
    `column_stats.py`, `results` holds `report.md` and `pendulum_plot.png`.
    Git installed in Seminar 4, with the name and e-mail set, and on Windows
    PowerShell 7 as the terminal of VS Code. A mailbox that can be opened in
    class, for the code that GitHub sends. No Python is needed.

    A student whose folder lacks the files of Seminar 4 goes on with what
    they have. Every step of this page works on the folder of
    [Seminar 1](seminar_01.md) alone. A student who has no folder at all
    downloads [`project_after_s1.zip`](../data/project_after_s1.zip), unpacks
    it, and opens `analysis-project` with **File** > **Open Folder...**. A
    student who missed Seminar 4 has no Git: they install it in section 1
    from the USB stick, as on
    [Install Python, Git and PowerShell 7](install_python_git.md), and follow
    a neighbour's screen meanwhile.

    For you:

    - A GitHub account of your own, and a project folder that is **not** a
      repository yet. If yours is one, delete its `.git` folder, and delete
      the repository `analysis-project` on GitHub.
    - Sections 8 to 10 done once on your own laptop. Section 8 depends on
      the sign-in of your system, and the first time takes longer.
    - The installers of Git and of PowerShell 7 on a USB stick, for a laptop
      that missed Seminar 4.
    - In VS Code, the terminal in the Panel and the Source Control view both
      visible: the room has to see that a button and a command do the same.
    - The lecture slide *Source Control and Commands* ready. It stays on the
      projector while the room works.

---

## Part 1 · A repository { #part-1 }

**0:00 to 0:35 · sections 1 to 3**

The room ends this part with the whole project in three commits, made with
the mouse. Nothing leaves the laptop yet.

---

### 1. Check Git { #check }

**0:00 · 10 min**

**Tell the room.** Git was installed in Seminar 4. Every commit carries a
name and an e-mail address, so Git has to know both. Three more settings
are made now, on every laptop, so that Git behaves the same in the whole
room. Then one command shows what the lecture derived: Git names a content
by a hash of its bytes.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**. The terminal is `zsh` on macOS and PowerShell 7 on
   Windows. Every line of this section starts with `git` and is typed the
   same in both.

2. Ask Git for its version, its name and its e-mail address.

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

!!! success "You should now see"
    Five settings, and the id `4a45f2be5e087d6b6dccd287fe1bfd36fe659aeb` on
    every laptop.

**Say it in these words.** Git for Windows comes with two settings of its
own: the first branch is named `master`, and `core.autocrlf` is `true`. The
lines of step 3 overrule both. With `true`, Git writes CRLF line endings
into every text file it puts into the working folder, for example in a
clone. `D0_KPi.csv` would grow from 3 926 142 to 4 017 726 bytes, one `0d`
more for each of its 91 584 lines, and the checksums of Seminar 4 would
fail, while `git status` still says that nothing changed. The lecture slide
*A Clone on Windows* shows it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `zsh: command not found: git`, or `The term 'git' is not recognized` | VS Code was open during the installation: close it with **File** > **Exit** (macOS `Cmd+Q`) and start it again. If Git is still missing, install it now from the USB stick, or work with a neighbour |
    | Windows: the terminal is **Git Bash**, its prompt ends in `$` | Not in this course. Close it with the bin icon at the top right of the Panel and open **Terminal** > **New Terminal**: PowerShell 7, as set in Seminar 4 |
    | The list of settings is longer | Other programs wrote settings too. The five lines have to be among them |
    | Another id for `D0_KPi.csv` | The file is not the one that was downloaded. Check it with `data/checksums.txt`, as in Seminar 4 |

---

### 2. Create the repository { #init }

**0:10 · 10 min**

**Tell the room.** A repository is the project folder together with a
hidden folder `.git` that holds every commit. It is made once. The first
commit holds one file, the README, so that the room sees the two steps of
every commit: stage, then commit.

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

    The answer is one line:

    ```text
    b7d67bc (HEAD -> main) Add the README
    ```

!!! success "You should now see"
    One line from `git log`, with seven digits of your own, and the other
    files still listed under **Changes**.

**Say it in these words.** The button made the folder `.git`. The **+**
copied the content of the README into the staging area. **Commit** wrote a
tree and a commit, and `main` is the name of that commit. Show the hidden
folder:

=== "macOS"

    ```text
    ls -a
    ```

    The list includes `.git`.

=== "Windows"

    ```text
    ls -Force
    ```

    The list includes `.git` with the mode `d--h-`: `h` for hidden. Plain
    `ls` leaves it out, and `ls -a` is refused with
    `the parameter name 'a' is ambiguous`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The view offers **Open Repository** in place of **Initialize Repository** | A folder above the project is a repository already, often the home folder. Do not open it. Call the lecturer |
    | A dialog: *There are no staged changes to commit* | Nothing was staged. Select **Cancel** and do step 3 |
    | A tab named `COMMIT_EDITMSG` opens | The message box was empty. Type the message into line 1 of that tab and select the check mark at its top right |
    | A dialog about `user.name` and `user.email` | Section 1, step 2 |
    | `git log` says `master` | The repository was made by a typed `git init` before section 1, step 3: Git for Windows and the Git of macOS then name the branch `master`. **Initialize Repository** names it `main` by itself. Type `git branch -m main` |

---

### 3. Ignore, then commit the rest { #ignore }

**0:20 · 15 min**

**Tell the room.** Not every file belongs in the repository.
`data/processed/D0_valid.csv` has 3.9 MB and is written by one command that
stands in the README. The command is kept and the file is left out. The file
`.gitignore` lists what Git has to leave out. It is a file of the project
and is committed like the others.

1. Go to the Explorer, select the empty area below the folders, then
   **New File**, and name it:

    ```text
    .gitignore
    ```

    The name begins with a dot and has no ending.

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

4. Stage `.gitignore` with its **+**, type the message and select
   **Commit**.

    ```text
    Add .gitignore
    ```

5. Move the mouse over the header **Changes** and select the **+** on that
   row. It stages every file at once. Read the list with the room:
   `D0_KPi.csv` is in it, `D0_valid.csv` is not.

6. Type the message and select **Commit**.

    ```text
    Add the data, the report and the scripts
    ```

7. Ask Git for the state of the folder.

    ```text
    git status
    ```

    ```text
    On branch main
    nothing to commit, working tree clean
    ```

8. Read the history.

    ```text
    git log --oneline
    ```

    ```text
    2f4088c (HEAD -> main) Add the data, the report and the scripts
    be1030d Add .gitignore
    b7d67bc Add the README
    ```

9. Ask which files were left out.

    ```text
    git status --ignored
    ```

    ```text
    Ignored files:
      (use "git add -f <file>..." to include in what will be committed)
            data/processed/D0_valid.csv
            data/processed/pendulum_script.csv
    ```

!!! success "You should now see"
    An empty **Changes** list, three commits, and the two ignored files named
    by `git status --ignored`.

**Say it in these words.** A file written by hand goes in, because nothing
can make it again. A file that a command writes may stay out, if the command
is in the repository. This command shows what the three commits cost, in
both shells:

```text
git count-objects -vH
```

```text
count: 22
size: 1.83 MiB
in-pack: 0
packs: 0
size-pack: 0 bytes
prune-packable: 0
garbage: 0
size-garbage: 0 bytes
```

22 objects, 3 commits, 8 trees and 11 blobs, take about 1.8 MiB for files
of 3.9 MB, because Git compresses. Windows prints 1.84 MiB.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The two files are still listed | A path in `.gitignore` is mistyped, or the file was saved as `.gitignore.txt` or inside a subfolder |
    | No ignored files at all | The folder has no files of Seminar 4. Go on: the steps work the same |
    | A student has put a dataset of their own into `data/raw`, and it has more than 50 MB | Add its path to `.gitignore` before step 5. GitHub refuses a file above 100 MB |
    | macOS: `.DS_Store` among the ignored files | Correct. The Finder makes it |
    | A file was committed that should stay out | `git rm --cached <file>`, add its path to `.gitignore`, commit both |

---

## Part 2 · Changes, typed { #part-2 }

**0:35 to 1:05 · sections 4 to 6**

The room changes a file, reads the change and commits it: once with the
mouse, once with four commands. Then two ways to take something back.

---

### 4. A change in Source Control { #change }

**0:35 · 10 min**

**Tell the room.** Git compares the working folder with the last commit. A
file that differs gets the letter `M`, and the diff shows what differs, line
by line. The diff is read before every commit: it is what the commit will
contain.

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

!!! success "You should now see"
    Four commits in the Graph, and the room can say what red and green mean
    in a diff.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | No `M` appears | The file was not saved. A dot on the tab means *not saved* |
    | The whole file is red and green | The line endings changed. Select `CRLF` or `LF` in the Status Bar and put back what it was |
    | Two columns in place of red above green | The window is wide. VS Code then shows the two versions side by side |

---

### 5. The same, typed { #typed }

**0:45 · 10 min**

**Tell the room.** Every button of the last section runs a Git command. The
room now types them. A typed command can be written down, repeated, and used
on a computer that has no VS Code.

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

4. Stage the file.

    ```text
    git add README.md
    ```

5. Look again. `git status` now says `Changes to be committed`.

    ```text
    git status
    ```

6. Commit.

    ```text
    git commit -m "Note when version control started"
    ```

    ```text
    [main 803abcb] Note when version control started
     1 file changed, 1 insertion(+)
    ```

7. Read the history.

    ```text
    git log --oneline
    ```

    ```text
    803abcb (HEAD -> main) Note when version control started
    59fe00c Name the pendulum in the report
    2f4088c Add the data, the report and the scripts
    be1030d Add .gitignore
    b7d67bc Add the README
    ```

!!! success "You should now see"
    Five commits, and after step 5 `git status` said
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
    | `dquote>` (zsh) or `>>` (PowerShell) at the start of the line | A quotation mark is missing. Press `Ctrl+C` and type the command again |
    | Windows: `warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it` | `core.autocrlf` is still `true`. Type the third line of section 1, step 3, and go on. The commit is fine |

---

### 6. Undo { #undo }

**0:55 · 10 min**

**Tell the room.** Two things go wrong every week: a file is damaged by an
edit that was not meant, and a commit gets a message with a mistake. Git
takes back both. The room damages the report on purpose.

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

    Stage it and commit it with the typing error, on purpose.

    ```text
    git add results/report.md
    git commit -m "Say who mesured"
    ```

5. Correct the message.

    ```text
    git commit --amend -m "Say who measured"
    ```

6. Read the last two commits.

    ```text
    git log --oneline -2
    ```

    ```text
    53f4ea5 (HEAD -> main) Say who measured
    803abcb Note when version control started
    ```

7. Look at the commit itself.

    ```text
    git cat-file -p HEAD
    ```

    ```text
    tree 757d50af6813e7a8ff793675df9d9b39dbeda5a2
    parent 803abcb95badf0458247a42238f3715d1b2fc28b
    author Mindaugas Sarpis <mindaugas.sarpis@cern.ch> 1792497300 +0300
    committer Mindaugas Sarpis <mindaugas.sarpis@cern.ch> 1792497360 +0300

    Say who measured
    ```

!!! success "You should now see"
    Six commits in `git log --oneline`, the last of them with the corrected
    message, and a table of nine rows in the report.

**Say it in these words.** Ask the room to compare the id of the commit
before and after step 5. It changed, from `6949f68` to `53f4ea5` in this
run: the message is part of the text that is hashed. That is why only a
commit that has not left the laptop is amended.

!!! warning "Watch for"
    A student discards an edit that was meant. Git has no copy of an edit
    that was never committed. `Ctrl+Z` in the editor brings it back as long
    as the tab is open.

---

## Part 3 · A remote { #part-3 }

**1:05 to 1:30 · sections 7 and 8**

The repository gets a second copy on GitHub. From here on the work survives
the loss of the laptop, and it can be fetched on another computer.

---

### 7. A GitHub account { #account }

**1:05 · 10 min**

**Tell the room.** GitHub is a hosting service for Git repositories. An
account is free. Its user name is public and part of every address, so it is
chosen like a file name: short, lowercase, without spaces, and fit to be
shown to an employer.

1. Everyone opens this address in the browser.

    ```text
    github.com
    ```

2. Ask who has an account. Those students select **Sign in** and help a
   neighbour. The others select **Sign up**.

3. They enter an e-mail address, a password and a user name. Advise an
   address that outlives the studies.

4. GitHub sends a code to that address. They type it in.

5. They stay on the free plan and skip the questions about a team.

!!! success "You should now see"
    On every laptop, a browser that is signed in to GitHub: the picture of
    the account is at the top right.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The code does not arrive | Look in the spam folder. Until it arrives the student follows on a neighbour's screen |
    | The user name is taken | Add the initial of the first name, or a number |
    | A student will not make an account | Sections 9 and 10 work without one. The student skips section 8 and the `git push` of section 10 |

---

### 8. Publish and push { #publish }

**1:15 · 15 min**

**Tell the room.** VS Code can create the repository on GitHub and send the
commits in one step. It signs in through the browser once and keeps the
sign-in. The repository is made **private**: only its owner sees it.

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
    ```

    ```text
    origin  https://github.com/<user>/analysis-project.git (fetch)
    origin  https://github.com/<user>/analysis-project.git (push)
    ```

6. Ask for the state.

    ```text
    git status
    ```

    ```text
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

7. Make one more commit, typed. Add this line at the end of the section
   **About** in `README.md` and save.

    ```text
    - **Repository:** private, on GitHub
    ```

    Stage, commit, and ask for the state.

    ```text
    git add README.md
    git commit -m "Say where the repository is"
    git status
    ```

    `git status` now says:

    ```text
    Your branch is ahead of 'origin/main' by 1 commit.
    ```

8. Send the commit, and reload the page in the browser.

    ```text
    git push
    ```

    The last line of the answer has two ids and the branch:

    ```text
    53f4ea5..ed3c15d  main -> main
    ```

    In the view the same step is the button **Sync Changes**.

!!! success "You should now see"
    The new line of the README in the browser, and
    `Your branch is up to date with 'origin/main'.` from `git status`.

**Say it in these words.** A push sends the objects the remote does not have
yet. Here that is one commit, one tree and one blob, 343 bytes in this run.
The data file is not sent again.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The browser does not return to VS Code | Select **Open Visual Studio Code** in the dialog of the browser, or copy the code it shows into VS Code |
    | `git push` asks for a user name and a password | The terminal is not the one inside VS Code. Press `Ctrl+C`, and push from the terminal of VS Code or with **Sync Changes** |
    | Windows: `git push` opens a window **Connect to GitHub** | Git Credential Manager, installed with Git, signs in once for typed commands. Select **Sign in with your browser** and confirm in the browser |
    | A name `analysis-project` exists already on the account | Choose another name in the list of step 3 |
    | The repository was published as public | On its page: **Settings**, at the bottom **Change visibility** |

---

## Part 4 · A branch and a merge { #part-4 }

**1:30 to 2:00 · sections 9 to 11**

A branch is a name for a commit. A second name lets work go on apart from
`main` until it is good. The room merges twice: once where Git has nothing
to decide, once where both branches changed the same line.

---

### 9. A branch { #branch }

**1:30 · 10 min**

**Tell the room.** The table of the report has the column names of the data
file as its header. A report needs words and units. The change is made on a
branch.

1. Select the branch name `main` at the left end of the Status Bar. A list
   opens at the top. Select **Create new branch...**, type the name and
   press Enter.

    ```text
    table-units
    ```

    The Status Bar now reads `table-units`.

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

6. Read the last three commits.

    ```text
    git log --oneline -3
    ```

    ```text
    01e155f (HEAD -> main, table-units) Write the units into the table header
    ed3c15d (origin/main) Say where the repository is
    53f4ea5 Say who measured
    ```

7. Delete the branch.

    ```text
    git branch -d table-units
    ```

    ```text
    Deleted branch table-units (was 01e155f).
    ```

!!! success "You should now see"
    `main` and `table-units` on the same commit in the log of step 6, one
    commit ahead of `origin/main`.

**Say it in these words.** This merge copied nothing. `main` had no commit
of its own, so Git moved the name `main` forward to the commit of the
branch. Deleting the branch deletes a name. The commit stays.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | After step 4 the header still has the units, and the file has the letter `M` | The change of step 2 was not committed, and Git carried it along to `main`. Go back to `table-units`, commit, and do step 4 again |
    | The list of step 5 is empty | The Status Bar still reads `table-units`. A branch is merged into the branch in use: do step 4 |

---

### 10. A conflict { #conflict }

**1:40 · 15 min**

**Tell the room.** Two branches now change the same line. Git cannot know
which text is meant. It writes both into the file and asks. This section is
typed, and the conflict is resolved in the editor.

1. Make a branch.

    ```text
    git switch -c wording
    ```

2. On it, change line 3 of `results/report.md` to the line below, and save.

    ```text
    Ten swings of a pendulum, timed for nine lengths.
    ```

    Commit it.

    ```text
    git add results/report.md
    git commit -m "Reword the first sentence"
    ```

3. Go back to `main`. Line 3 is the old sentence again.

    ```text
    git switch main
    ```

4. Change line 3 to the line below, and save.

    ```text
    Time of 10 swings of a pendulum for nine lengths from 20 cm to 100 cm.
    ```

    Commit it.

    ```text
    git add results/report.md
    git commit -m "Give the range of lengths"
    ```

5. Merge.

    ```text
    git merge wording
    ```

    ```text
    Auto-merging results/report.md
    CONFLICT (content): Merge conflict in results/report.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```

6. Look at `results/report.md` in the editor. Lines 3 to 7 are:

    ```text
    <<<<<<< HEAD
    Time of 10 swings of a pendulum for nine lengths from 20 cm to 100 cm.
    =======
    Ten swings of a pendulum, timed for nine lengths.
    >>>>>>> wording
    ```

    Above `=======` is the line of `main`, below it the line of `wording`.

7. Select **Accept Incoming Change** above the block. The markers go and
   the line of `wording` stays. Add the range to it by hand, so that it
   reads as below, and save.

    ```text
    Ten swings of a pendulum, timed for nine lengths from 20 cm to 100 cm.
    ```

8. In Source Control the file stands under **Merge Changes** with the sign
   `!`. Stage it with **+** and select **Continue**. The message
   `Merge branch 'wording'` is already filled in.

9. Look at the history.

    ```text
    git log --oneline --graph -5
    ```

    ```text
    *   5880f8b (HEAD -> main) Merge branch 'wording'
    |\
    | * 0a60f31 (wording) Reword the first sentence
    * | 6399829 Give the range of lengths
    |/
    * 01e155f Write the units into the table header
    * ed3c15d (origin/main) Say where the repository is
    ```

10. Delete the branch and push.

    ```text
    git branch -d wording
    git push
    ```

!!! success "You should now see"
    A history that splits and joins, eleven commits in `git log --oneline`,
    and in the browser the report with the new sentence.

**Say it in these words.** A conflict is not an error. Git reports that one
line was changed twice and leaves the decision to a person. Nothing is lost
before the decision, and `git merge --abort` goes back to the state before
the merge.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `Already up to date.` in step 5 | The branch `wording` has no commit of its own: the file was not saved before step 2 was committed, and Git said `nothing to commit`. Do step 2 again |
    | `merge: wording - not something we can merge` | The branch was never made. `git branch` lists the branches. Do steps 1 and 2 again |
    | The markers are committed | The file was staged before it was edited. Remove the markers, save, commit again |
    | No button **Continue** | Type `git commit --no-edit` |
    | `git push` is refused with `(fetch first)` | A commit was made on the GitHub page. `git pull --no-edit`, then push |

---

### 11. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

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

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Compute the id of the last commit again, from its text, as on the
  lecture slide *The Id of a Commit*. The line is the same in both shells.

    ```text
    git cat-file commit HEAD | git hash-object -t commit --stdin
    ```

    The answer is the full id of the last commit, the one `git log -1`
    shows: `5880f8b8c0c85c3d23926f4c46b4aac1716ce24d` in this run. The text
    goes from one `git` to the other through the pipe unchanged, in `zsh`
    and in PowerShell 7.

- Ask Git for the id of a two-letter text.

    ```text
    echo "hi" | git hash-object --stdin
    ```

    Ask which header Git put in front, and how many bytes it hashed.

    === "macOS"

        It prints `45b983be36b73c0788dc9cbcb76cbb80fc7bb057`. The header is
        `blob 3` and a zero byte: `hi` and a line break `0a` are three
        bytes, ten bytes in all.

    === "Windows"

        It prints `edf0effbb6851d0055229878b4bf0d7212167642`. PowerShell
        ends the text with `0d 0a`, so the header is `blob 4` and a zero
        byte, eleven bytes in all.

- Find out which commit last changed each of the first five lines of the
  report.

    ```text
    git blame -s -L 1,5 results/report.md
    ```

    The answer is three different ids: the commit that added the report
    for lines 1, 2 and 4, the merge commit for line 3, the commit of
    `table-units` for line 5.

- After section 8 or 10, mark the state with a tag, and push the tag.

    ```text
    git tag -a seminar-5 -m "State after Seminar 5"
    git push origin seminar-5
    ```

- If you have put a dataset of your own into `data/raw`, look at its size.

    === "macOS"

        ```text
        ls -l data/raw
        ```

    === "Windows"

        ```text
        ls data/raw
        ```

        The size in bytes is the column `Length`.

    If it has less than 50 MB, commit it. If it has more, add its path to
    `.gitignore` and write into the README where it comes from, how large it
    is and its SHA-256, as on the lecture slide *The README Says How to
    Fetch It*.

- Clone your repository into a second folder, `check`, beside the project
  folder, and rebuild what is missing. Take the address from
  `git remote -v`. These lines are the same in both shells.

    ```text
    cd ..
    ```

    ```text
    git clone <address> check
    ```

    ```text
    cd check
    ```

    ```text
    ls data/processed
    ```

    The answer is `pendulum.csv` alone: the two ignored files are not in
    the clone. Copy the two lines of your shell under **How to rebuild**
    out of the README and run them inside `check`. Then check the raw files
    against the list, as in Seminar 4, section 13.

    === "macOS"

        ```text
        shasum -a 256 -c data/checksums.txt
        ```

        Both raw files print `OK`.

    === "Windows"

        ```text
        Compare-Object (Get-Content data/checksums.txt) (Get-FileHash data/raw/*).Hash
        ```

        Nothing is printed: the hashes are the same.

    `git status` in `check` says `nothing to commit, working tree clean`:
    the rebuilt files are ignored. Go back and delete the clone.

    ```text
    cd ../analysis-project
    ```

    === "macOS"

        ```text
        rm -rf ../check
        ```

    === "Windows"

        ```text
        rm -r -Force ../check
        ```

        Without `-Force` PowerShell deletes the files and stops at
        `.git`, which is hidden and holds read-only objects.

- Set up an SSH key as on the lecture slide *SSH: the Alternative*, and
  change the address with `git remote set-url origin` and the address that
  begins with `git@github.com:`. `git push` then asks for no sign-in.

- Work in pairs. One invites the other on the GitHub page of the
  repository: **Settings** > **Collaborators**. The guest clones, makes a
  branch, pushes it and opens a pull request. The owner reads the diff and
  merges it.

- Do the first four levels of *Introduction Sequence* at
  [learngitbranching.js.org](https://learngitbranching.js.org/). They show
  commits, branches and merges as a moving picture.

## If students ask for more

| Topic | Week |
|--|--|
| Which Python files stay out of a repository | 6 (Python Foundations) |
| Data too large for a repository: Git LFS, DVC | 13 (Reproducible Workflows) |
| One command that rebuilds every ignored file | 13 (Reproducible Workflows) |
| Checks that run on every push | 13 (Reproducible Workflows) |

Leave out altogether, even if asked: Git Bash, `git rebase`,
`git reset --hard`, `git push --force`, submodules.

## Aims practised

♻️ every state of the project kept, with its reason · 🔧 the same commands in every editor and on every host · 📁 raw data in, rebuilt files out, by a written rule · ⚙️ a result tied to the commit that made it
