# Seminar 6 · Git

**Paired lecture:** 06 Version Control with Git · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Who changed the mean?

The lecturer runs Part 2 from this page; in Part 3 the room works in pairs.
Everything is typed in the terminal of VS Code (zsh on macOS, Git Bash on
Windows; the same lines in both). A line that starts with `$` is typed without
the `$`; `...` stands for lines left out.

**If time runs short:** leave out section 6 (the conflict); Hint 3 of Part 3 gives the steps to resolve one.

??? info "Before the session"
    - **Room:** Git and Miniforge on every laptop (installed in Seminar 4;
      the [Setup](../setup.md) page for a laptop that missed it), internet,
      and a mailbox each student can open (GitHub sends a code).
    - **No file is handed out.** Two public repositories are cloned from
      their addresses:
        - [datasets/global-temp](https://github.com/datasets/global-temp),
          the yearly and monthly temperature of the Earth from NASA GISS
          (GISTEMP v4, public domain) and the Met Office (HadCRUT5, Open
          Government Licence v3), as a data package of datahub.io (CC BY
          4.0): 70 commits since 2015, 243 KiB;
        - [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project),
          the weather station of the lectures: seven commits by Smiltė and
          Tomas, data CC0, scripts MIT, 554 KiB.
    - **The outputs** come from runs on 10 November 2026 with Git 2.56.0.
      A bot adds a commit to `global-temp` on the first day of every month:
      a later clone has more commits on top, and `main` stands on a newer
      one. Sections 6 and 7 name the commits they start from by their ids,
      so their outputs stay as printed. The ids of both clones are the same
      on every laptop; commits made today get other ids on every laptop.
    - **Missing a tool?** Git and Miniforge: [Setup, steps
      2–4](../setup.md#shell); VS Code: [Setup, step 1](../setup.md#vscode).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.
    - **Page:** the **▶ Steps** button (bottom right) shows one step at a
      time; arrows or swipe to move, `Esc` to close.

---

## Part 1 · Set up { #part-1 }

### 1. Check Git, give it your name { #check }

<!-- 0:00 · 8 min -->

Every commit records a name and an e-mail. Set them once per laptop.

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

3. Your name as it should appear on every commit, and your e-mail: the one
   of your GitHub account, or the one you will sign up with in section 2.

    ```text
    $ git config --global user.name "Your Name"
    $ git config --global user.email "you@example.org"
    ```

4. The three settings of the lecture: the first branch of a new repository
   is called `main`, `git pull` joins two histories with a merge, and Git
   leaves line endings as they are. None prints anything.

    ```text
    $ git config --global init.defaultBranch main
    $ git config --global pull.rebase false
    $ git config --global core.autocrlf false
    ```

5. List what Git now knows. It prints the names in small letters.

    ```text
    $ git config --global --list
    user.name=Your Name
    user.email=you@example.org
    init.defaultbranch=main
    pull.rebase=false
    core.autocrlf=false
    ```

**Check:** your own name and e-mail in the list.

---

### 2. A GitHub account { #account }

<!-- 0:08 · 4 min -->

GitHub keeps a copy of a repository online; Part 3 ends there.

1. Open [github.com](https://github.com) > **Sign up**: the e-mail of
   section 1, a password and a username, then the code that GitHub e-mails
   you. The username is in the address of every repository you make. With
   an account already: **Sign in**.

**Check:** you are signed in on github.com and know your username.

---

### 3. A new folder for today's clones { #start }

<!-- 0:12 · 3 min -->

Both repositories of today are cloned into one new folder.

1. Make it and go into it.

    ```text
    $ mkdir ~/s06
    $ cd ~/s06
    $ pwd
    /Users/smilte/s06
    ```

2. **File** > **Open Folder...** > `s06` (in your home folder) > **Open**,
   then **View** > **Terminal**.

**Check:** the Explorer shows the empty folder `s06`, and the terminal is in it.

---

## Part 2 · Showcase { #part-2 }

The lecturer clones a real data repository, kept by people and since May 2026
also by a bot, and asks its history four questions; the room watches or types
along. Every block is typed as it stands.

### 4. Clone the global temperature data and read 1998 in four versions { #log }

<!-- 0:15 · 11 min -->

A clone brings every version of every file. `git log -- FILE` lists the commits that changed the file: who, when, and their message.

```text
$ cd ~/s06
$ git clone https://github.com/datasets/global-temp.git
Cloning into 'global-temp'...
...
Receiving objects: 100% (284/284), 242.56 KiB | 3.11 MiB/s, done.
...
$ cd global-temp
$ head -3 data/annual.csv
Source,Year,Mean
GCAG,1850,-0.4265
GCAG,1851,-0.2635
$ git rev-list --count HEAD
70
$ git log --format="%h %ad %an: %s" --date=short -- data/annual.csv
b90e8a3 2026-11-01 Automated commit: Automated commit
44571fe 2026-10-01 Automated commit: Automated commit
...
701a808 2026-05-14 Ola Rubaj: Fix data freshness: add missing entrypoint, bump HadCRUT5 to 5.1.0.0 (#17)
f5e1081 2024-10-04 gradedSystem: [update][m] Adding necessary changes to files
d92a358 2017-01-21 Soren Jones: add latest data
...
8aa154f 2015-01-22 Soren Jones: initial commit
$ git grep "GISTEMP,1998," 8aa154f d92a358 f5e1081 b90e8a3 -- data/annual.csv
8aa154f:data/annual.csv:GISTEMP,1998,0.61
d92a358:data/annual.csv:GISTEMP,1998,0.64
f5e1081:data/annual.csv:GISTEMP,1998,0.605
b90e8a3:data/annual.csv:GISTEMP,1998,0.6083
```

Your speed differs. `Mean` is in °C above or below the mean of a reference
period, 1951–1980 for NASA's rows, GISTEMP. `git grep` searches the file as it
was in each commit named.

**Notice:** 21 of the 70 commits changed `data/annual.csv`, and in four of them the row of 1998 reads 0.61, 0.64, 0.605 and 0.6083 °C.

**Ask the room:** a report of 2017 gives 1998 as 0.64 °C warmer than 1951–1980; the file says 0.6083 today. Which number is wrong?

??? note "Answer"
    Neither: each is right for its version of the data. NASA recomputes the
    whole record every month, with late reports and corrections from the
    stations, and in June 2019 moved to a larger collection of station data
    (GHCN version 4). A number in a report needs the id of the data it came
    from: `git show d92a358:data/annual.csv` gives back the file of January
    2017, byte for byte.

!!! warning "The terminal shows `:` or `(END)` and takes no commands"
    Git shows long output one screen at a time. Press `q`.

---

### 5. Find which commit moved the GCAG numbers, and why { #blame }

<!-- 0:26 · 9 min -->

`git log -S` lists the commits that added or removed a text; `git show` prints what a commit changed; `git blame` names the last commit of a line.

```text
$ git grep "GCAG,1880," d92a358 b90e8a3 -- data/annual.csv
d92a358:data/annual.csv:GCAG,1880,-0.1148
b90e8a3:data/annual.csv:GCAG,1880,-0.3032
$ git log -S "GCAG,1880,-0.1148" --oneline -- data/annual.csv
f5e1081 [update][m] Adding necessary changes to files
d92a358 add latest data
$ git log -S "hadcrut5" --oneline -- scripts/process.py
17a07be [update/polish][l] Updated scripts / added requirements.txt
$ git show 17a07be -- scripts/process.py | grep -e "cag/time-series" -e "^+GCAG_URL_annual"
-        self.base_url = 'http://www.ncdc.noaa.gov/cag/time-series/global'
+GCAG_URL_annual = 'https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.0.2.0/analysis/diagnostics/HadCRUT.5.0.2.0.analysis.summary_series.global.annual.csv'
$ git blame -L 8,8 scripts/process.py
701a808 (Ola Rubaj 2026-05-14 16:44:15 +0200 8) GCAG_URL_annual = 'https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.1.0.0/analysis/diagnostics/HadCRUT.5.1.0.0.analysis.summary_series.global.annual.csv'
```

GCAG is NOAA's series, *Climate at a Glance*. Its number for 1880 left the file
in `f5e1081`, which wrote the data again; the reason is in the script, changed
the same day in `17a07be`: since October 2024 the rows labelled GCAG come from
the Met Office's HadCRUT5, no longer from NOAA (`ncdc.noaa.gov/cag`). Neither
message says so.

**Notice:** NOAA measured from the mean of the 20th century, HadCRUT5 from the mean of 1961–1990, a period 0.12 °C warmer in NOAA's own rows of 2017: the same year now gets a lower number.

**Ask the room:** `git blame` names `701a808` for the line with the Met Office's address, `git log -S` names `17a07be`. Why two commits?

??? note "Answer"
    `blame` gives the last commit that changed a line: in May 2026 `701a808`
    changed this one again, from HadCRUT 5.0.2.0 to 5.1.0.0. `log -S` gives
    every commit that added or removed the text `hadcrut5`: `17a07be`
    brought it in. To find when a number first changed, search for the text;
    to find who wrote a line as it stands, blame it.

---

### 6. Merge the maintainers' fix of a line you also fixed: a conflict { #conflict }

<!-- 0:35 · 9 min -->

Git joins two branches by itself where they changed different lines, and stops where both changed the same line.

In November 2024, at `3cb5a07`, line 90 of `README.md` still sent readers to
NOAA for the GCAG rows. Fix it on a branch of your own made at that commit, then
merge `b90e8a3` (`main` on 10 November 2026), in which the maintainers fixed the
same line in May 2026.

```text
$ git switch -c gcag-link 3cb5a07
Switched to a new branch 'gcag-link'
$ sed -n 90,91p README.md
[gcag]: https://www.ncei.noaa.gov/node/6696
[hadcrut5]: https://www.metoffice.gov.uk/hadobs/hadcrut5/index.html
```

In VS Code, open `README.md` and give line 90 the address of line 91, so that it
reads `[gcag]: https://www.metoffice.gov.uk/hadobs/hadcrut5/index.html`. Save.

```text
$ git commit -am "Link the GCAG rows to HadCRUT5, their source"
[gcag-link b09bede] Link the GCAG rows to HadCRUT5, their source
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git merge --no-edit b90e8a3
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status --short
A  .gitattributes
M  .github/workflows/actions.yml
UU README.md
A  UPDATE_SCRIPT_MAINTENANCE_REPORT.md
M  data/annual.csv
M  data/monthly.csv
M  datapackage.json
M  scripts/process.py
```

Your ids differ. `README.md` now holds both versions of the line, at line 96:

```text
<<<<<<< HEAD
[gcag]: https://www.metoffice.gov.uk/hadobs/hadcrut5/index.html
=======
[gcag]: https://www.metoffice.gov.uk/hadobs/hadcrut5/
>>>>>>> b90e8a3
```

Over the `<<<<<<<` line VS Code offers **Accept Current Change** (yours),
**Accept Incoming Change** (`b90e8a3`) and **Accept Both Changes**. Click
**Accept Incoming Change**, save, then mark the file resolved and commit the
merge.

```text
$ git add README.md
$ git commit --no-edit
[gcag-link 86959a8] Merge commit 'b90e8a3' into gcag-link
$ git show --no-patch HEAD
commit 86959a80f1fa8be12caf4bc41263a5f5630db576 (HEAD -> gcag-link)
Merge: b09bede b90e8a3
Author: Your Name <you@example.org>
Date:   Tue Nov 10 21:32:00 2026 +0200

    Merge commit 'b90e8a3' into gcag-link

    # Conflicts:
    #       README.md
```

**Notice:** the changes of 16 commits in seven files came in by themselves (`A`, `M`); only the line that both sides changed (`UU`) waited for a person. The merge commit has two parents, yours and theirs.

**Ask the room:** had you typed exactly the maintainers' address, `https://www.metoffice.gov.uk/hadobs/hadcrut5/`, would the merge have stopped?

??? note "Answer"
    No. The same change on both sides is no conflict: Git takes it once.
    Git stops only where the two sides changed the same lines differently,
    and it never judges which of them is right: a person does.

---

### 7. Undo the November update with revert, then with reset { #revert }

<!-- 0:44 · 8 min -->

`git revert` undoes a commit with a new commit; `git reset --hard` moves the branch back, and the commits after that point leave it. Try both on a branch of your own.

```text
$ git switch -c undo b90e8a3
Switched to a new branch 'undo'
$ git revert --no-edit b90e8a3
[undo 2d1567c] Revert "Automated commit"
 Date: Tue Nov 10 21:40:00 2026 +0200
 2 files changed, 643 insertions(+), 643 deletions(-)
$ git log --oneline -3
2d1567c (HEAD -> undo) Revert "Automated commit"
b90e8a3 (origin/main, origin/HEAD, main) Automated commit
44571fe Automated commit
$ grep "GISTEMP,1998," data/annual.csv
GISTEMP,1998,0.6092
$ git reset --hard 44571fe
HEAD is now at 44571fe Automated commit
$ git log --oneline -3
44571fe (HEAD -> undo) Automated commit
c3fd761 Automated commit
bc6ef15 Automated commit
$ grep "GISTEMP,1998," data/annual.csv
GISTEMP,1998,0.6092
```

Your id and date of the revert differ. The November update changed 643 values of
NASA's rows, 116 of them yearly means, and added no month.

**Notice:** both leave October's numbers in the folder (1998: 0.6092). After `revert` the November update stays in the history with its undoing on top; after `reset` it is gone from the branch.

**Ask the room:** others have already pulled `b90e8a3` from GitHub. Which of the two can you push, and what would the other do to them?

??? note "Answer"
    The revert: the push adds one commit on top of theirs. After the reset
    the branch lacks `b90e8a3`, which GitHub has, so Git refuses the push;
    `git push --force` would remove the commit from GitHub, and everyone who
    pulled it would hold a history that GitHub no longer has. Reset only
    commits that nobody else has. An LLM asked to "undo a commit" may answer
    with `git reset --hard`: first ask whether the commit was pushed.

---

### 8. Library card: the Git commands of this page { #card }

<!-- 0:52 · 3 min -->

Every Git command of the examples and of the solution below, one line each.

| Command | What it does |
|--|--|
| `git clone URL` | a copy of the repository with its whole history, in a new folder |
| `git log --oneline`, `git log --format="%h %ad %an: %s" --date=short` | one line per commit, newest first; the second with date (`%ad`) and author (`%an`); `-- FILE` keeps the commits that changed FILE |
| `git rev-list --count HEAD` | the number of commits that lead to the current one |
| `git show ID -- FILE` | the commit, and what it changed in FILE: `-` the old line, `+` the new; `--stat` lists only the files, `--no-patch` leaves the changes out |
| `git show ID:FILE` | FILE as it was in commit ID |
| `git grep "TEXT" ID1 ID2 -- FILE` | the lines with TEXT in FILE, as it was in each commit |
| `git log -S "TEXT" --oneline -- FILE` | the commits that added or removed TEXT |
| `git blame -L 38,38 FILE` | the last commit that changed line 38, with its author and date |
| `git switch -c NAME ID`, `git switch main` | a new branch NAME at commit ID; back to `main` |
| `git commit -am "MESSAGE"` | stage every changed file that Git already tracks, and commit it |
| `git merge --no-edit NAME` | join branch NAME into the current branch, with Git's message |
| `git add FILE`, `git commit --no-edit` | after a conflict is settled in the editor: mark the file resolved, commit the merge (`git merge --abort` gives up the merge) |
| `git revert --no-edit ID` | a new commit that undoes commit ID |
| `git reset --hard ID` | the branch back to ID: later commits leave it, and so do edits not committed |
| `git remote -v`, `git remote remove origin` | where the clone pulls from and pushes to; forget that address |

---

## Part 3 · The problem { #part-3 }

### 9. Who changed the mean of the weather station, and how do you take it back? { #problem }

<!-- 0:55 · 50 min -->

The weather project of the lectures is a public repository, seven commits by
Smiltė and Tomas (data CC0, scripts MIT, as its README says):

```text
https://github.com/MindaugasSarpis/weather-project.git
```

Its `README.md` gives the mean temperature of 2016–2025 as 5.78 °C. The same
README says that `temp_c` is `-999`, the mark of a missing reading, in 120 rows
of `weather.csv`; without them the mean is 7.16 °C. Find who changed the number,
when and why, and take the change back so that the history keeps both.

Work in pairs, with any tools, an LLM too: the work is the idea and the checks, not the typing.

Clone it into `~/s06`:

```text
$ cd ~/s06
$ git clone https://github.com/MindaugasSarpis/weather-project.git
Cloning into 'weather-project'...
...
Resolving deltas: 100% (15/15), done.
```

Then **File** > **Open Folder...** > `s06` > `weather-project` > **Open**, and
**View** > **Terminal**: Source Control shows this repository alone.

1. **Predict**, before any command. Write down:
    - which number is the mean of the real temperatures, 5.78 or 7.16, and
      one line of arithmetic that links the two;
    - whether `git revert` of the commit that changed it will stop on a
      conflict: Smiltė's licence, the commit after it, also changed
      `README.md`;
    - for the second fix below: at which of the two files the merge will
      stop, and why.
2. **Solve.**
    - The commit that changed the mean: its id, author, date, message, and
      the lines it changed in each file.
    - Take it back with a new commit. Run `./scripts/rebuild.sh` and read
      `results/temp_c.txt`.
    - **A second fix, as an LLM writes it.** Give an LLM lines 38–39 of
      `README.md` and the last line of `scripts/rebuild.sh`, and ask for
      lines that leave the 120 rows out. On a branch `llm-fix` made at
      `0f19f54`, put its lines in place of the old ones and commit; then
      switch to `main` and merge `llm-fix` into it. Settle what stops.
    - Publish the repository to your GitHub, private: `git remote remove
      origin`, then **Publish Branch** in Source Control (VS Code asks you to
      sign in to GitHub: **Allow**, then **Continue** and **Authorize** in the
      browser), and **Publish to GitHub private repository**.
3. **Check the machine's work.**
    - Every id an LLM gives you: `git show --stat ID` must print that commit
      and the files it changed. An LLM that has not seen your terminal can
      name an id that does not exist.
    - By hand: count the rows of `-999` (`grep -c`) and redo the arithmetic.
      Does 5.78 come out of 7.16?
    - `git log --oneline`: are Tomas's commit and Smiltė's licence, `85e435e`
      and `0f19f54`, still in your history? `git status`: are
      `data/processed/` and `results/`, which `rebuild.sh` makes, kept out of
      your commits?
    - Your answers against your predictions; where they differ, why.
4. **Hand in.** The id of the commit that changed the mean, with its author,
   date and the reason its message gives; the mean in `results/temp_c.txt`
   after your fix, with the id of the commit `rebuild.sh` ran at; the address
   of your repository on GitHub; two sentences in your own words, ready to
   show.

!!! warning "`python: command not found` from `rebuild.sh`"
    The script runs Python from Miniforge: the prompt must start with
    `(base)`. Without it, see the [Setup page, step 4](../setup.md#terminal).

??? tip "Hint 1: finding the commit"
    `grep -n "5.78" README.md` gives the line; `git blame -L 38,38 README.md`
    the commit that last changed it; `git log -S "5.78" --oneline` every
    commit that added or removed the text; `git show ID` what one changed,
    file by file. As in section 5, the number is in one file and its cause
    in another: read every file the commit changed.

??? tip "Hint 2: taking it back"
    `git revert --no-edit ID`, as in section 7. `git reset --hard a9c513d`
    would also bring 7.16 back, and would take Smiltė's licence out of the
    history with Tomas's commit.

??? tip "Hint 3: the branch, the merge, the conflict"
    `git switch -c llm-fix 0f19f54` makes the branch and goes to it. Edit,
    `git commit -am "MESSAGE"`, `git switch main`, `git merge --no-edit
    llm-fix`. Where it stops, `README.md` holds both versions between
    `<<<<<<<` and `>>>>>>>`: click **Accept Current Change** or **Accept
    Incoming Change**, save, `git add README.md`, `git commit --no-edit`.

    Without an LLM, put these three lines in place of lines 38–39 of
    `README.md`:

    ```text
    Mean `temp_c`, 2016 to 2025: **7.16 °C**, over the 87 552 hours of
    `weather.csv` without the 120 rows of `-999`. The script writes it to
    `results/temp_c.txt`.
    ```

    and in the last line of `scripts/rebuild.sh` change `data/raw/weather.csv`
    back to `data/processed/weather_valid.csv`.

??? note "One solution"
    **The commit.** Line 38 holds the number; Tomas's commit changed it,
    and changed the script that computes it.

    ```text
    $ cd weather-project
    $ grep -n "5.78" README.md
    38:Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
    $ git blame -L 38,38 README.md
    85e435e (Tomas 2026-10-19 11:45:00 +0300 38) Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
    $ git log -S "5.78" --oneline
    85e435e Take the mean over all rows of weather.csv
    $ git show 85e435e -- scripts/rebuild.sh
    commit 85e435ef56fe4308debf88b5b2d546e4000bbce6
    Author: Tomas <tomas@example.org>
    Date:   Mon Oct 19 11:45:00 2026 +0300

        Take the mean over all rows of weather.csv

        The valid file leaves 120 hours out. The raw file has every hour.
    ...
    -python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
    +python scripts/column_stats.py data/raw/weather.csv temp_c > results/temp_c.txt
    $ grep -c ",-999," data/raw/weather.csv
    120
    ```

    By hand: each of the 120 rows adds −999 to the sum,
    (87 552 × 7.16 − 120 × 999) / 87 672 = 506 992 / 87 672 = 5.78.

    **Take it back, rebuild, keep the made files out.** The revert does not
    stop: the licence changed other lines of the README. Your ids and dates
    differ from here on.

    ```text
    $ git revert --no-edit 85e435e
    Auto-merging README.md
    [main 39ea1fe] Revert "Take the mean over all rows of weather.csv"
     Date: Tue Nov 10 22:05:00 2026 +0200
     2 files changed, 3 insertions(+), 3 deletions(-)
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    $ cat results/temp_c.txt
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    $ git status --short
    ?? data/processed/
    ?? results/
    $ printf "data/processed/\nresults/\n" > .gitignore
    $ git add .gitignore
    $ git commit -m "Leave out the files that rebuild.sh makes"
    [main 89c347c] Leave out the files that rebuild.sh makes
     1 file changed, 2 insertions(+)
     create mode 100644 .gitignore
    ```

    **The second fix and the merge.**

    ```text
    $ git switch -c llm-fix 0f19f54
    Switched to a new branch 'llm-fix'
    ```

    In `README.md` the three lines of Hint 3 in place of lines 38–39; in
    `scripts/rebuild.sh` `data/processed/weather_valid.csv` again. Save both.

    ```text
    $ git commit -am "Take the mean without the -999 rows"
    [llm-fix e0fbb0d] Take the mean without the -999 rows
     2 files changed, 4 insertions(+), 3 deletions(-)
    $ git switch main
    Switched to branch 'main'
    Your branch is ahead of 'origin/main' by 2 commits.
      (use "git push" to publish your local commits)
    $ git merge --no-edit llm-fix
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    $ git status --short
    UU README.md
    ```

    The merge stops at the README only: both fixes gave `rebuild.sh` the
    same line. In `README.md`:

    ```text
    <<<<<<< HEAD
    Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
    marked `-999` are left out. The script writes it to `results/temp_c.txt`.
    =======
    Mean `temp_c`, 2016 to 2025: **7.16 °C**, over the 87 552 hours of
    `weather.csv` without the 120 rows of `-999`. The script writes it to
    `results/temp_c.txt`.
    >>>>>>> llm-fix
    ```

    **Accept Current Change** (Smiltė's words, back by the revert), save.

    ```text
    $ git add README.md
    $ git commit --no-edit
    [main 36104a2] Merge branch 'llm-fix'
    $ git log --oneline --graph -6
    *   36104a2 (HEAD -> main) Merge branch 'llm-fix'
    |\
    | * e0fbb0d (llm-fix) Take the mean without the -999 rows
    * | 89c347c Leave out the files that rebuild.sh makes
    * | 39ea1fe Revert "Take the mean over all rows of weather.csv"
    |/
    * 0f19f54 (origin/main, origin/HEAD) Add a licence
    * 85e435e Take the mean over all rows of weather.csv
    ```

    **Publish.** The clone still points at the course repository, which
    only its owner can push to.

    ```text
    $ git remote remove origin
    ```

    **Publish Branch** in Source Control, **Publish to GitHub private
    repository**. Then:

    ```text
    $ git remote -v
    origin  https://github.com/your-username/weather-project.git (fetch)
    origin  https://github.com/your-username/weather-project.git (push)
    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

    **Hand in.** `85e435e`, Tomas, 19 October 2026: "The valid file leaves
    120 hours out. The raw file has every hour." After the revert `39ea1fe`,
    `results/temp_c.txt` says 7.15997 °C over 87 552 hours;
    `https://github.com/your-username/weather-project`. Tomas pointed the
    mean at the raw file to use every hour, but 120 of those hours are
    `-999`, the mark of a missing reading, and they pull the mean down by
    1.38 °C. The revert keeps his commit and its reason in the history and
    puts the correction on top of it.

**With your own project data:** if your project is a Git repository, which
commit last changed the number your report gives? `git log -S "THE NUMBER"`,
`git blame` on its line and `git show` of the commit: hand in its id, author,
date and reason, and say whether the message alone told you why. If the project
is not under Git yet, `git init` it, write a `.gitignore` for the files your
scripts make, commit, and publish it as a private repository.

---

## Part 4 · Show and discuss { #part-4 }

### 10. Three questions about the pairs' histories { #discuss }

<!-- 1:45 · 15 min -->

Two or three pairs show their repository on GitHub (**Commits**) and read their two sentences.

**Ask the room:** one pair followed an LLM that said `git reset --hard a9c513d`. What is missing from their repository?

??? note "Answer"
    In a fresh clone:

    ```text
    $ git reset --hard a9c513d
    HEAD is now at a9c513d Write the mean temperature into results and the README
    $ git status
    On branch main
    Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
      (use "git pull" to update your local branch)

    nothing to commit, working tree clean
    ```

    Tomas's commit and Smiltė's licence: `LICENSE` and the README's licence
    section went with the mistake. The README says 7.16 again, but the
    history no longer says who wrote 5.78 or why, and on a repository shared
    with others the push would be refused (section 7).

**Ask the room:** the merge of `llm-fix` stopped at `README.md`. Why not at `scripts/rebuild.sh`, which both fixes changed too?

??? note "Answer"
    Both fixes changed the line of `rebuild.sh` in the same way, back to
    `weather_valid.csv`, and the same change on both sides is taken once
    (section 6). In the README they used different words for the same
    number. A pair whose LLM changed the script in another way, for example
    to drop the `-999` rows inside the Python line, met a second conflict
    there.

**Ask the room:** every monthly commit of `global-temp` says `Automated commit`. What should the message of `b90e8a3` have said?

??? note "Answer"
    What changed and why, for example `GISTEMP revised by NASA: 116 of 146
    yearly means changed (1880: -0.1792 to -0.1725); HadCRUT5 unchanged`.
    Then `git log` answers "why did 1998 change?" without a diff. A bot can
    write that message as easily as a person can.

A result can be trusted when its history says which commit made it, who changed it and why; a mistake is taken back by a new commit, so that the history keeps both.

---

## Optional, if the room is fast { #optional }

### 11. Let Git find the commit: bisect { #bisect }

<!-- — · 10 min -->

`git bisect` halves the history, tests one commit at each step, and names the first commit that fails the test.

Mark `0f19f54` as bad and the first commit, `3e72263`, as good, and let Git run
a test that fails when the README says 5.78: `sh -c '...'` runs the test, and
`!` turns its result round.

```text
$ cd ~/s06/weather-project
$ git bisect start 0f19f54 3e72263
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[9f28b51be4d356315e48263d9037af025ee83553] Add the rebuild script
$ git bisect run sh -c '! grep -q "5.78" README.md'
running 'sh' '-c' ''\!' grep -q "5.78" README.md'
...
85e435ef56fe4308debf88b5b2d546e4000bbce6 is the first 'bad' commit
...
bisect found first 'bad' commit
$ git bisect reset
...
Switched to branch 'main'
...
```

**Ask the room:** three tests for six commits. How many would `global-temp`, with 70, need?

??? note "Answer"
    Seven: each test halves what is left, and 2⁷ = 128 is the first power
    of two above 70. A thousand commits take ten tests. With a test that
    runs the script and checks the mean, bisect finds a wrong number in
    any history, also when the commit's message does not mention it.

---

## Aims practised

- ♻️ **Reproducibility:** a number goes with the id of the data and the
  script that made it; any version of a file comes back by its id, byte for
  byte, and a mistake is undone by a commit that the history keeps.
- 🔧 **Tool-agnosticism:** the same lines in zsh on macOS and Git Bash on
  Windows; the Source Control view and GitHub show the same history.
- ⚙️ **Automation:** `git log -S`, `git blame` and `git bisect` search a
  history of any length; a bot commits the temperature data every month.
