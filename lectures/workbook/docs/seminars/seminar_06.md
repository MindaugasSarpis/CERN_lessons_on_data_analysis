# Seminar 6 · Git

**Paired lecture:** 06 Version Control with Git · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Who changed the mean?

**Today's goal:** every student clones the weather project, finds the commit
that changed its mean temperature, takes it back, commits their own work and
pushes it to their own GitHub repository.

Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows; the lines are the same in both). In the blocks, a line that starts
with `$` is typed, every other line is what comes back, and `...` stands
for lines left out. The **Source Control** view (`Ctrl+Shift+G`, macOS `Cmd+Shift+G`) stays open and shows
each change.

**If time runs short:** stop after section 12; sections 13 to 16 are optional.

??? info "Before the session"
    - **Room:** Git and Miniforge on every laptop (installed in Seminar 4;
      the [Setup](../setup.md) page for a laptop that missed it), internet, and a mailbox each student can open (GitHub sends a
      code). Nothing from earlier seminars is needed: the clone and one zip
      bring every file.
    - **Missing a tool?** Git and Miniforge: [Setup, steps
      2–4](../setup.md#shell); your name for Git and a GitHub account:
      [Setup, step 6](../setup.md#github).
    - **You:** nothing to prepare. The repository
      [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project)
      is small (about 0.5 MB to download) and the same for everyone, so its
      ids on this page are the ids in the room. Ids of commits made today
      differ on every laptop.
    - **Page:** the **▶ Steps** button (bottom right) shows one step at a
      time; arrows or swipe to move, `Esc` to close.

---

## Part 1 · Git and the project { #part-1 }

<!-- 0:00 to 0:20 -->

**Git** keeps every saved state of a project. A folder together with that history is a **repository**.

Further reading: [Pro Git, chapter 2: Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository);
[HSF Analysis Essentials, Git](https://hsf-training.github.io/analysis-essentials/git/README.html).

---

### 1. Check Git, give it your name { #check }

<!-- 0:00 · 10 min -->

Every commit records a name and an e-mail. Set them once.

1. Open VS Code, then the terminal: **View** > **Terminal**. The prompt
   ends in `%` on a Mac (zsh) and `$` on Windows (Git Bash).

    ??? warning "Windows: the terminal shows `PS` (PowerShell)"
        `Ctrl+Shift+P` > **Terminal: Select Default Profile** > **Git Bash**.
        Close the terminal (bin icon) and open a new one. No **Git Bash** in
        the list: Git is missing, see step 2.

2. Check Git.

    ```text
    $ git --version
    git version 2.56.0
    ```

    Any version from 2.40 on is fine.

    ??? warning "`command not found: git`: install it"
        === "macOS"

            ```text
            $ brew install git
            ```

        === "Windows"

            In the Windows terminal (PowerShell), then restart VS Code and
            take **Git Bash** as in step 1:

            ```text
            winget install --id Git.Git -e
            ```

        Close the terminal and open a new one.

3. Your name, as it should appear on every commit.

    ```text
    $ git config --global user.name "Your Name"
    ```

4. Your e-mail: the one of your GitHub account, or the one you will sign
   up with today.

    ```text
    $ git config --global user.email "you@example.org"
    ```

5. The three settings of the lecture: the first branch of a new repository
   is called `main`, `git pull` joins two histories with a merge, and Git
   leaves line endings as they are. None prints anything.

    ```text
    $ git config --global init.defaultBranch main
    $ git config --global pull.rebase false
    $ git config --global core.autocrlf false
    ```

6. List what Git now knows.

    ```text
    $ git config --global --list
    user.name=Your Name
    user.email=you@example.org
    init.defaultbranch=main
    pull.rebase=false
    core.autocrlf=false
    ```

    Git prints the names in small letters: `init.defaultbranch` is the
    setting typed as `init.defaultBranch`.

**Check:** your own name and e-mail in the list.

---

### 2. Clone the weather project { #clone }

<!-- 0:10 · 10 min -->

`git clone` downloads a project with its whole history.

1. From the home folder, clone the project into a new folder,
   `weather-s06`: the name after the address names the folder.

    ```text
    $ cd ~
    $ git clone https://github.com/MindaugasSarpis/weather-project.git weather-s06
    Cloning into 'weather-s06'...
    remote: Enumerating objects: 37, done.
    remote: Counting objects: 100% (37/37), done.
    remote: Compressing objects: 100% (20/20), done.
    remote: Total 37 (delta 15), reused 37 (delta 15), pack-reused 0 (from 0)
    Receiving objects: 100% (37/37), 554.27 KiB | 4.43 MiB/s, done.
    Resolving deltas: 100% (15/15), done.
    ```

2. Open it: **File** > **Open Folder...** > `weather-s06` > **Open**.
   Answer **Yes, I trust the authors**.
3. Open the terminal again (**View** > **Terminal**). It starts in the
   project folder.

    ```text
    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

4. The history lives in a hidden folder, `.git`: `ls` leaves out names
   that start with a dot unless one is asked for by name, and `-d` names
   the folder instead of listing what is in it.

    ```text
    $ ls -d .git
    .git
    ```

    Without `.git` the folder is a plain folder again.

**Check:** the Explorer shows `data`, `scripts`, `.gitattributes`, `LICENSE`, `README.md`.

---

## Part 2 · Who changed the mean? { #part-2 }

<!-- 0:20 to 0:55 -->

Without the 120 rows of `-999`, the mean temperature is 7.16 °C. Open the clone's `README.md`: its **Result** says 5.78 °C. The history says who changed it, when and why.

---

### 3. Read the history: `git log` { #log }

<!-- 0:20 · 10 min -->

A commit is one saved state: id, author, date, message.

1. One line per commit, newest first.

    ```text
    $ git log --oneline
    0f19f54 (HEAD -> main, origin/main, origin/HEAD) Add a licence
    85e435e Take the mean over all rows of weather.csv
    a9c513d Write the mean temperature into results and the README
    9f28b51 Add the rebuild script
    96f2dc4 Describe the columns and the -999 rows
    2d282c7 Add the two scripts handed out with the data
    3e72263 Add the station's hourly log and the spreadsheet export
    ```

    The seven-character code is the commit's **id**. `HEAD -> main` marks
    where you are; `origin/main`, where GitHub was at the clone.

2. The last two commits in full.

    ```text
    $ git log -n 2
    commit 0f19f54e1b79db8133153f28d76be685862182b5 (HEAD -> main, origin/main, origin/HEAD)
    Author: Smiltė <smilte@example.org>
    Date:   Mon Oct 19 17:05:00 2026 +0300

        Add a licence

    commit 85e435ef56fe4308debf88b5b2d546e4000bbce6
    Author: Tomas <tomas@example.org>
    Date:   Mon Oct 19 11:45:00 2026 +0300

        Take the mean over all rows of weather.csv

        The valid file leaves 120 hours out. The raw file has every hour.
    ```

3. Only the commits that touched the raw data. `--` separates the
   options from the paths.

    ```text
    $ git log --oneline -- data/raw
    3e72263 Add the station's hourly log and the spreadsheet export
    ```

    The raw files are as they arrived: nobody changed them since.

4. In Source Control, open the **Graph** section: the same seven commits,
   newest at the top. Drawn the other way, oldest at the left:

    ```mermaid
    gitGraph
      commit id: "3e72263 data"
      commit id: "2d282c7 scripts"
      commit id: "96f2dc4 columns"
      commit id: "9f28b51 rebuild"
      commit id: "a9c513d 7.16"
      commit id: "85e435e Tomas" type: HIGHLIGHT
      commit id: "0f19f54 licence"
    ```

**Check:** seven commits, by Smiltė and Tomas; one commit for `data/raw`.

!!! warning "The terminal shows `:` or `(END)` and takes no commands"
    Git shows long output one screen at a time. Press `q`.

---

### 4. Find who wrote a line: `git blame` { #blame }

<!-- 0:30 · 10 min -->

`git blame` gives, for each line, the commit that wrote it.

1. The **Result** in `README.md` says 5.78 °C; without the 120 hours of
   `-999` the mean is 7.16 °C. Find the line with 5.78.

    ```text
    $ grep -n '5.78' README.md
    38:Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
    ```

2. Ask who wrote line 38. `blame` prints one more digit of the id.

    ```text
    $ git blame -L 38,38 README.md
    85e435ef (Tomas 2026-10-19 11:45:00 +0300 38) Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
    ```

3. Ask which commits added or removed the text `5.78`.

    ```text
    $ git log -S "5.78" --oneline
    85e435e Take the mean over all rows of weather.csv
    ```

**Check:** commit `85e435e`, Tomas, 19 October.

---

### 5. See what a commit changed: `git show` { #show }

<!-- 0:40 · 15 min -->

`git show` prints a commit and its changes: `-` is the old line, `+` the new.

1. The files it changed.

    ```text
    $ git show --stat 85e435e
    commit 85e435ef56fe4308debf88b5b2d546e4000bbce6
    Author: Tomas <tomas@example.org>
    Date:   Mon Oct 19 11:45:00 2026 +0300

        Take the mean over all rows of weather.csv

        The valid file leaves 120 hours out. The raw file has every hour.

     README.md          | 4 ++--
     scripts/rebuild.sh | 2 +-
     2 files changed, 3 insertions(+), 3 deletions(-)
    ```

2. The change in `rebuild.sh`.

    ```text
    $ git show 85e435e -- scripts/rebuild.sh
    ...
    @@ -3,4 +3,4 @@ set -e
     mkdir -p data/processed results
     grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
     python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    -python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
    +python scripts/column_stats.py data/raw/weather.csv temp_c > results/temp_c.txt
    ```

3. Count the rows that the raw file has and the valid file has not.

    ```text
    $ grep -c ',-999,' data/raw/weather.csv
    120
    ```

    Each adds −999 to the sum:
    (87 552 × 7.16 − 120 × 999) / 87 672 = 5.78.

**Check:** the mean now reads `data/raw/weather.csv`, with its 120 rows of
`-999`.

!!! question "Task: where did 7.16 come from, and is the data file the same as Smiltė's?"
    1. Find the commit that first wrote 7.16 into the README, and its day.
    2. Print `scripts/rebuild.sh` as it was in that commit.
    3. Ask Git for the id of `data/raw/weather.csv`, and compare it with
       your neighbour's.

??? success "Answer"
    1. `a9c513d`, 16 October: the older of the two lines.

        ```text
        $ git log -S "7.16" --oneline
        85e435e Take the mean over all rows of weather.csv
        a9c513d Write the mean temperature into results and the README
        ```

    2. The last line still reads `weather_valid.csv`.

        ```text
        $ git show a9c513d:scripts/rebuild.sh
        #!/usr/bin/env bash
        set -e
        mkdir -p data/processed results
        grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
        python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
        python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
        ```

    3. The same id on every laptop: Git names a file by a **hash** of its
       bytes, a 40-digit number that changes when a single byte changes, so
       equal ids mean equal bytes.

        ```text
        $ git hash-object data/raw/weather.csv
        f811f73d93226acc8a0c96562aef9f7825b85b0a
        ```

---

## Part 3 · Put it right { #part-3 }

<!-- 0:55 to 1:25 -->

Undo the change without losing the history, check the number against the script, then add your own work.

---

### 6. Take the commit back: `git revert` { #revert }

<!-- 0:55 · 10 min -->

`git revert` makes a new commit that undoes an old one. The history keeps both.

1. Revert Tomas's commit.

    ```text
    $ git revert 85e435e --no-edit
    Auto-merging README.md
    [main 32855d4] Revert "Take the mean over all rows of weather.csv"
     Date: Tue Oct 27 10:32:00 2026 +0200
     2 files changed, 3 insertions(+), 3 deletions(-)
    ```

    Your id and date differ.

2. Look at the history: Tomas's commit stays, and the new one undoes it.

    ```text
    $ git log --oneline -n 3
    32855d4 (HEAD -> main) Revert "Take the mean over all rows of weather.csv"
    0f19f54 (origin/main, origin/HEAD) Add a licence
    85e435e Take the mean over all rows of weather.csv
    ```

    ```mermaid
    gitGraph
      commit id: "a9c513d 7.16"
      commit id: "85e435e Tomas" type: HIGHLIGHT
      commit id: "0f19f54 licence"
      commit id: "32855d4 revert" type: REVERSE
    ```

3. In `README.md` the **Result** says 7.16 °C again. Smiltė's licence of
   `0f19f54` is still there.

**Check:** 7.16 in the README, eight commits.

---

### 7. Rebuild and check the mean { #rebuild }

<!-- 1:05 · 5 min -->

The README's number must come out of the script.

1. Run the rebuild script.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ```

2. Read the result.

    ```text
    $ cat results/temp_c.txt
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

3. Ask Git what is new: the two folders the script made.

    ```text
    $ git status
    On branch main
    Your branch is ahead of 'origin/main' by 1 commit.
      (use "git push" to publish your local commits)

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            data/processed/
            results/

    nothing added to commit but untracked files present (use "git add" to track)
    ```

**Check:** `mean 7.15997`, and two untracked folders.

!!! warning "`command not found: python`"
    Miniforge is missing (the [Setup](../setup.md) page). The script made
    `data/processed/weather_valid.csv` before it stopped; go on.

---

### 8. Leave made files out: `.gitignore` { #ignore }

<!-- 1:10 · 5 min -->

Files that programs make again at any time stay out of the history.

1. **File** > **New File...**, type `.gitignore`, press `Enter`. Write three
   lines and save: the two folders that `rebuild.sh` makes, and
   `__pycache__`, which Python makes when a script imports a module such as
   the `weather.py` of Seminar 5.

    ```text
    data/processed/
    results/
    __pycache__/
    ```

2. The two folders of the rebuild are gone from Source Control;
   `.gitignore` is there.

    ```text
    $ git status --short
    ?? .gitignore
    ```

3. Stage it, then commit it.

    ```text
    $ git add .gitignore
    $ git commit -m "Leave out the files that scripts make"
    [main bdde04f] Leave out the files that scripts make
     1 file changed, 3 insertions(+)
     create mode 100644 .gitignore
    ```

**Check:** `git status` ends with `nothing to commit, working tree clean`.

---

### 9. Commit the work of Seminar 5 { #commit }

<!-- 1:15 · 10 min -->

Copy, look at the change, stage, commit: the loop of every day.

1. Download `weather-s06.zip` from the
   [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**. It holds a folder `weather-s06` with the files of
   Seminar 5; unzipped into the home folder, they go into the clone, which
   has the same name.

    ```text
    $ unzip ~/Downloads/weather-s06.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s06.zip
       creating: /Users/smilte/weather-s06/notebooks/
      inflating: /Users/smilte/weather-s06/environment.yml
      inflating: /Users/smilte/weather-s06/notebooks/explore.ipynb
      inflating: /Users/smilte/weather-s06/scripts/coldest_hour.py
      inflating: /Users/smilte/weather-s06/scripts/hours.py
      inflating: /Users/smilte/weather-s06/scripts/mean_temp.py
      inflating: /Users/smilte/weather-s06/scripts/now.py
      inflating: /Users/smilte/weather-s06/scripts/weather.py
    ```

    Safari unpacks a zip by itself: then
    `cp -R ~/Downloads/weather-s06/. ~/weather-s06/` copies its files into
    the clone.

2. Run two of its scripts, written in Seminar 5 for six hours, on the
   clone's full log. To one decimal they agree with `results/temp_c.txt`
   (`mean 7.15997`, `min -16.3`).

    ```text
    $ python scripts/mean_temp.py
    87552 hours, mean 7.2 °C
    $ python scripts/coldest_hour.py
    coldest hour: 2025-01-07T05:00, -16.3 °C
    ```

3. What changed: seven new files, shown as untracked (`??`). The run made
   `scripts/__pycache__`; `.gitignore` keeps it out of the list.

    ```text
    $ git status --short
    ?? environment.yml
    ?? notebooks/
    ?? scripts/coldest_hour.py
    ?? scripts/hours.py
    ?? scripts/mean_temp.py
    ?? scripts/now.py
    ?? scripts/weather.py
    ```

4. In `README.md`, under the **Result** paragraph, write the two results
   as two lines and save.

    ```text
    Checked in Python, `scripts/mean_temp.py`: 7.2 °C over 87 552 hours.
    The coldest hour, `scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.
    ```

5. How the README changed. Also: click `README.md` in Source Control.

    ```text
    $ git diff
    diff --git a/README.md b/README.md
    index a74c2dc..2e5c394 100644
    --- a/README.md
    +++ b/README.md
    @@ -38,6 +38,9 @@ the temperature sensor was down.
     Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
     marked `-999` are left out. The script writes it to `results/temp_c.txt`.

    +Checked in Python, `scripts/mean_temp.py`: 7.2 °C over 87 552 hours.
    +The coldest hour, `scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.
    +
     ## How to rebuild

     In the project folder, in zsh on macOS or Git Bash on Windows, with Python
    ```

    `git diff` shows changed files only; new files have no old version yet.

6. Stage all of it, look again. `git add` puts the files in the staging
   area, the content of the next commit.

    ```mermaid
    flowchart LR
      W["working folder<br/>your files"] -- "git add" --> S["staging area<br/>the next commit"]
      S -- "git commit" --> R["repository<br/>the history"]
      R -- "git push" --> G["GitHub"]
      G -- "git pull" --> W
      R -- "git restore" --> W
    ```

    ```text
    $ git add scripts notebooks environment.yml README.md
    $ git status --short
    M  README.md
    A  environment.yml
    A  notebooks/explore.ipynb
    A  scripts/coldest_hour.py
    A  scripts/hours.py
    A  scripts/mean_temp.py
    A  scripts/now.py
    A  scripts/weather.py
    ```

7. Commit.

    ```text
    $ git commit -m "Add the Python work of Seminar 5"
    [main 335cde1] Add the Python work of Seminar 5
     8 files changed, 377 insertions(+)
     create mode 100644 environment.yml
     create mode 100644 notebooks/explore.ipynb
     create mode 100644 scripts/coldest_hour.py
     create mode 100644 scripts/hours.py
     create mode 100644 scripts/mean_temp.py
     create mode 100644 scripts/now.py
     create mode 100644 scripts/weather.py
    ```

    Your id differs.

**Check:** `git log --oneline` shows ten commits, three of them yours.

!!! question "Task: break the raw data, then repair it"
    In VS Code, delete line 2 of `data/raw/weather.csv` and save. Find the
    change with Git, then undo it with one command.

??? success "Answer"
    ```text
    $ git status --short
     M data/raw/weather.csv
    $ git diff --stat
     data/raw/weather.csv | 1 -
     1 file changed, 1 deletion(-)
    $ git restore data/raw/weather.csv
    ```

    `git status --short` prints nothing: the file has its committed bytes
    again.

---

## Part 4 · Your copy on GitHub { #part-4 }

<!-- 1:25 to 2:00 -->

A **remote** is another copy of the repository, here on GitHub: `git push` sends your commits there, `git pull` brings its commits here.

---

### 10. A GitHub account { #account }

<!-- 1:25 · 10 min -->

GitHub keeps a copy of the repository online.

1. Ask Git which e-mail your commits carry. Sign up with that one, and
   GitHub shows those commits as yours.

    ```text
    $ git config user.email
    you@example.org
    ```

2. Open [github.com](https://github.com) > **Sign up**: that e-mail, a
   password and a username, then the code that GitHub e-mails you. The
   username is in the address of every repository you make. With an
   account already: **Sign in**.

**Check:** you are signed in on github.com.

---

### 11. Publish, then push and pull { #publish }

<!-- 1:35 · 20 min -->

The clone still points at the course repository, which you cannot write to.

1. Where the clone points.

    ```text
    $ git remote -v
    origin  https://github.com/MindaugasSarpis/weather-project.git (fetch)
    origin  https://github.com/MindaugasSarpis/weather-project.git (push)
    ```

2. Remove that remote.

    ```text
    $ git remote remove origin
    ```

3. In Source Control, click **Publish Branch**. VS Code asks to sign in
   to GitHub: **Allow**, then **Continue** and **Authorize** in the
   browser, then back to VS Code.
4. VS Code proposes the folder's name, `weather-s06`: keep it, click
   **Publish to GitHub private repository**. VS Code sends the ten commits.
5. Where the clone points now.

    ```text
    $ git remote -v
    origin  https://github.com/your-username/weather-s06.git (fetch)
    origin  https://github.com/your-username/weather-s06.git (push)
    ```

6. Open `https://github.com/your-username/weather-s06`: the files, and
   **10 Commits**.

**Check:** your repository on GitHub, marked **Private**.

!!! question "Task: one change each way"
    1. On github.com, edit `README.md` (the pencil), add a line, click
       **Commit changes**. Bring that commit to your laptop.
    2. On your laptop, add another line to `README.md`, commit it, and send
       it to GitHub.

??? success "Answer"
    The ids below are from one run; yours differ.

    1. `git pull` brings the commit made on github.com.

        ```text
        $ git pull
        ...
        From https://github.com/your-username/weather-s06
           335cde1..1bc67f8  main       -> origin/main
        Updating 335cde1..1bc67f8
        Fast-forward
         README.md | 1 +
         1 file changed, 1 insertion(+)
        ```

    2. Stage, commit, push.

        ```text
        $ git add README.md
        $ git commit -m "Add a line"
        [main 415f809] Add a line
         1 file changed, 1 insertion(+)
        $ git push
        ...
        To https://github.com/your-username/weather-s06.git
           1bc67f8..415f809  main -> main
        ```

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

Who changed the mean, asked of the history once more; then today's commands.

1. Ask which commits added or removed the text `5.78`: Tomas's added it,
   your revert took it out. The first id is your revert's, so yours differs.

    ```text
    $ git log -S "5.78" --oneline
    32855d4 Revert "Take the mean over all rows of weather.csv"
    85e435e Take the mean over all rows of weather.csv
    ```

2. The room names the command for each row, then reads the right column.

    | To | Type |
    |--|--|
    | copy a project with its history | `git clone URL` |
    | see the history | `git log --oneline` |
    | find who wrote a line | `git blame -L 38,38 FILE` |
    | find the commits that added or removed a text | `git log -S "TEXT" --oneline` |
    | see a commit | `git show ID` |
    | undo a commit, keep the history | `git revert ID` |
    | undo an edit not yet committed | `git restore FILE` |
    | commit | `git status`, `git diff`, `git add FILE`, `git commit -m "…"` |
    | sync with GitHub | `git push`, `git pull` |

---

## Optional, if the room goes fast { #optional }

---

### 13. A branch and a merge { #branch }

<!-- — · 10 min -->

A branch is a second line of commits; merge brings it back. Your ids differ.

1. Make a branch and go to it.

    ```text
    $ git switch -c fahrenheit
    Switched to a new branch 'fahrenheit'
    ```

2. In `README.md`, under the line that ends with `results/temp_c.txt`,
   add a line and save: 7.16 × 9 / 5 + 32 = 44.89.

    ```text
    In Fahrenheit: 44.89 °F.
    ```

3. Commit all changed files at once.

    ```text
    $ git commit -am "Give the mean in Fahrenheit"
    [fahrenheit 917aa83] Give the mean in Fahrenheit
     1 file changed, 1 insertion(+)
    ```

4. Back to `main`: the line is gone from `README.md`.

    ```text
    $ git switch main
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    ```

5. Merge `fahrenheit` into `main`. `main` has no commit of its own since
   the branch began, so Git only moves it forward: a fast-forward.

    ```text
    $ git merge fahrenheit
    Updating 415f809..917aa83
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
    ```

6. Delete the branch name, push.

    ```text
    $ git branch -d fahrenheit
    Deleted branch fahrenheit (was 917aa83).
    $ git push
    ...
    To https://github.com/your-username/weather-s06.git
       415f809..917aa83  main -> main
    ```

**Check:** the Fahrenheit line in `README.md` on `main`.

---

### 14. A conflict { #conflict }

<!-- — · 15 min -->

Two branches change the same line; Git asks which to keep.

1. A branch, `wording`, that rewrites the Fahrenheit line.

    ```text
    $ git switch -c wording
    Switched to a new branch 'wording'
    ```

    Change the line to `In degrees Fahrenheit: 44.89.`, save.

    ```text
    $ git commit -am "Spell out the unit"
    [wording 925a396] Spell out the unit
     1 file changed, 1 insertion(+), 1 deletion(-)
    ```

2. On `main`, change the Fahrenheit line differently.

    ```text
    $ git switch main
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    ```

    Change the line to `In Fahrenheit: 44.9 °F.`, save.

    ```text
    $ git commit -am "Round the Fahrenheit mean to one decimal"
    [main 4f7a803] Round the Fahrenheit mean to one decimal
     1 file changed, 1 insertion(+), 1 deletion(-)
    ```

3. Merge `wording` into `main`. Both changed the same line, so Git stops.

    ```mermaid
    gitGraph
      commit id: "Fahrenheit"
      branch wording
      commit id: "Spell out the unit"
      checkout main
      commit id: "Round to 44.9"
      merge wording id: "merge"
    ```

    ```text
    $ git merge wording
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```

4. `README.md` now holds both lines.

    ```text
    <<<<<<< HEAD
    In Fahrenheit: 44.9 °F.
    =======
    In degrees Fahrenheit: 44.89.
    >>>>>>> wording
    ```

    Over the `<<<<<<< HEAD` line VS Code offers **Accept Current Change**
    (`main`), **Accept Incoming Change** (`wording`), **Accept Both
    Changes**. Click one, save.

5. Mark it resolved, commit the merge.

    ```text
    $ git add README.md
    $ git commit --no-edit
    [main ca806f8] Merge branch 'wording'
    ```

6. The history has two lines that join. Your ids differ.

    ```text
    $ git log --oneline --graph -n 5
    *   ca806f8 (HEAD -> main) Merge branch 'wording'
    |\
    | * 925a396 (wording) Spell out the unit
    * | 4f7a803 Round the Fahrenheit mean to one decimal
    |/
    * 917aa83 (origin/main) Give the mean in Fahrenheit
    * 415f809 Add a line
    ```

**Check:** no `<<<<<<<` left in `README.md`, `git status` clean.

---

### 15. Tag the result { #tag }

<!-- — · 5 min -->

A tag is a name for one commit that never moves: "the state that gave 7.16".

1. Tag the last commit.

    ```text
    $ git tag -a v1.0 -m "Mean 7.16 °C, checked"
    ```

2. Send the tag to GitHub; tags are not pushed by `git push` alone.

    ```text
    $ git push origin v1.0
    ...
    To https://github.com/your-username/weather-s06.git
     * [new tag]         v1.0 -> v1.0
    ```

**Check:** on GitHub, the branch menu has a **Tags** tab with `v1.0`.

---

### 16. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions about the same history, for a room that is done early. Each answer is folded under its task; the outputs are from a fresh clone, so your own commits come on top of them.

!!! question "Advanced task: let Git find the commit"
    `git bisect` finds the first commit with a property by halving the
    history, testing one commit at each step. Mark `0f19f54` as bad and the
    first commit, `3e72263`, as good, and let Git run a test that fails
    when the README says 5.78. How many commits does it test?

??? success "Answer"
    `sh -c '...'` runs the test; `!` turns its result round, so "5.78 found"
    counts as bad.

    ```text
    $ git bisect start 0f19f54 3e72263
    Bisecting: 2 revisions left to test after this (roughly 2 steps)
    [9f28b51be4d356315e48263d9037af025ee83553] Add the rebuild script
    $ git bisect run sh -c '! grep -q "5.78" README.md'
    ...
    85e435ef56fe4308debf88b5b2d546e4000bbce6 is the first bad commit
    ...
    $ git bisect reset
    ...
    Switched to branch 'main'
    ...
    ```

    Three tests for six commits; a thousand commits would take ten. With a
    test script that checks the mean, this finds a wrong number in any
    history.

!!! question "Advanced task: the life of one line"
    Show every version of README line 38, the mean, with the commit that
    wrote it, in one command.

??? success "Answer"
    `-L 38,38:FILE` follows a range of lines back through the history.

    ```text
    $ git log -L 38,38:README.md --oneline
    85e435e Take the mean over all rows of weather.csv
    ...
    -Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
    -marked `-999` are left out. The script writes it to `results/temp_c.txt`.
    +Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
    a9c513d Write the mean temperature into results and the README
    ...
    +Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
    +marked `-999` are left out. The script writes it to `results/temp_c.txt`.
    ```

    In your repository, your revert is the newest entry.

!!! question "Advanced task: who did what"
    How many commits did each person make, and which files did Tomas
    change? Use one command for each question.

??? success "Answer"
    ```text
    $ git shortlog -sn HEAD
         6  Smiltė
         1  Tomas
    $ git log --author=Tomas --stat --oneline
    85e435e Take the mean over all rows of weather.csv
     README.md          | 4 ++--
     scripts/rebuild.sh | 2 +-
     2 files changed, 3 insertions(+), 3 deletions(-)
    ```

    In your repository your own name has a line too. `--author` takes part
    of a name or e-mail.

---

## Aims practised

- ♻️ **Reproducibility:** the README's number is checked against the script
  that makes it, and the history says who changed what, when and why.
- 🔧 **Tool-agnostic:** the same lines in zsh on macOS and Git Bash on Windows;
  the Source Control view shows the same state.
- 📁 **Files:** made files stay out of the repository; raw data is restored
  from the history in one command.
