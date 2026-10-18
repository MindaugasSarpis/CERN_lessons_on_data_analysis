# Seminar 4 · Command Line

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** What is the mean temperature of ten years? Every student installs Git and Python with a package
manager, searches `weather.csv` with `grep` and the project folder with
`find`, gets the mean temperature, 7.16 °C, and writes a script that makes
every result again.

Everything is typed in the terminal of VS Code: `zsh` on macOS, Git Bash on
Windows. The lines are the same in both; only the installs and the checksum
command differ. In the blocks, a line that starts with `$` is typed (a Mac
shows `%`), and every other line is what comes back.

Further reading: [The Unix Shell, Software Carpentry](https://swcarpentry.github.io/shell-novice/),
the lessons this seminar follows in spirit, on other data.

**If time runs short:** the Task of Part 4 can go; never cut sections 12 to
15: they give the answer and the script.

??? info "Before the session"
    - **Room:** internet, and laptops on which students can install programs
      (macOS asks for the laptop's password, Windows for an administrator's
      **Yes**). Today's folder is `weather-s04.zip` on the Releases page of
      [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project/releases);
      the session needs nothing from any other seminar.
    - **You:** nothing to prepare.
      [Install Python and Git](install_python_git.md) has every error
      message of the installs, for helpers.
    - **Outputs** are from Git Bash, user `smilte`. On macOS paths start
      with `/Users/smilte` instead of `/c/Users/smilte`, and `wc` puts spaces
      in front of its numbers.

---

## Part 1 · Install with a package manager { #part-1 }

<!-- 0:00 to 0:28 -->

A package manager fetches a program, puts it in one known folder and on `PATH`, and later updates or removes it.

---

### 1. Install the tools { #installs }

<!-- 0:00 · 12 min -->

Git keeps the versions of a project, from Seminar 6; Miniforge is Python with conda. VS Code stays closed.

1. Open the system's terminal.

    === "macOS"

        `Cmd+Space`, type `Terminal`, `Enter`. Its shell is `zsh`.

    === "Windows"

        Windows key, type `powershell`, `Enter`. Only the two install lines
        are typed here; from section 2 on, the course works in Git Bash.

2. macOS only: install the package manager **Homebrew** (Windows has its
   own, `winget`, built in). Type the laptop's password when asked: nothing
   shows while typing. It may install the developer tools of macOS first,
   which takes a while.

    ```text
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

    At the end it prints **Next steps**: copy the lines it lists there,
    paste them, `Enter`.

3. Check the package manager: one version line.

    === "macOS"

        ```text
        $ brew --version
        Homebrew …
        ```

    === "Windows"

        ```text
        $ winget --version
        v1.…
        ```

4. Install Git and Miniforge, one line at a time.

    === "macOS"

        ```text
        $ brew install git
        $ brew install --cask miniforge
        ```

        The second ends with `🍺  miniforge was successfully installed!`

    === "Windows"

        ```text
        $ winget install --id Git.Git -e
        $ winget install --id CondaForge.Miniforge3 -e
        ```

        Each ends with `Successfully installed`. Answer `Y` if winget asks
        about the source agreements, **Yes** if Windows asks for
        permission.

5. macOS only: let conda set up `zsh`, so that every new terminal finds
   Python. (Windows does this in section 2, in Git Bash.)

    ```text
    $ conda init zsh
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

6. Close the terminal window.

**Check:** Git and Miniforge installed.

!!! warning "No password, or no administrator's **Yes**"
    The laptop is managed by the university or an employer. The student
    pairs with a neighbour today.

---

### 2. Today's folder, VS Code's terminal and conda { #shell }

<!-- 0:12 · 8 min -->

Today's folder holds the weather project: the station's log, the export and its hand-repaired copy, a README, and two programs that arrived with the data. The **terminal** is the window; the **shell** is the program in it that reads each line: `zsh` on macOS, Git Bash on Windows.

1. On the Releases page (`github.com/MindaugasSarpis/weather-project/releases`),
   under **Assets**, click `weather-s04.zip`, and unpack it into your home
   folder.

    === "macOS"

        In Finder, open **Downloads** and double-click `weather-s04.zip`.
        Select the new folder `weather-s04`, press `Cmd+C`, then
        `Cmd+Shift+H` (your home folder), then `Cmd+V`.

    === "Windows"

        In File Explorer, open **Downloads**, right-click
        `weather-s04.zip` > **Extract All...** > **Browse...**, choose
        `C:\Users\` and your name, **Select Folder**, **Extract**.

2. Open VS Code: **File** > **Open Folder...** > `weather-s04` (in your
   home folder) > **Open**, and answer **Yes, I trust the authors**.
3. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). Type and choose:

    ```text
    Terminal: Select Default Profile
    ```

    Take **zsh** (macOS) or **Git Bash** (Windows).

4. Command Palette again:

    ```text
    Terminal: Create New Terminal
    ```

5. Windows only: let conda set up Git Bash. Then close the terminal (the
   bin icon of the Panel) and open a new one, as in step 4.

    ```text
    $ ~/miniforge3/Scripts/conda.exe init bash
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

6. Check the shell.

    === "macOS"

        ```text
        $ echo $SHELL
        /bin/zsh
        ```

    === "Windows"

        ```text
        $ echo $SHELL
        /usr/bin/bash
        ```

7. Check conda and Python. `python` is the name on both systems.

    ```text
    $ conda --version
    conda 26.7.2
    $ python --version
    Python 3.14.7
    ```

**Check:** `(base)` in the prompt: conda's first environment, with Python in it.

!!! warning "`python: command not found`, or no `(base)` in the prompt"
    conda is not set up in this shell: step 5 (Windows) or section 1, step 5
    (macOS) again, then quit VS Code (**File** > **Exit**, macOS `Cmd+Q`)
    and start it again.

---

### 3. Where the programs landed { #packages }

<!-- 0:20 · 8 min -->

The shell finds a program by searching the folders of `PATH`, in order.

1. Where `git` and `python` are.

    === "macOS"

        ```text
        $ which git python
        /opt/homebrew/bin/git
        /opt/homebrew/Caskroom/miniforge/base/bin/python
        ```

    === "Windows"

        ```text
        $ which git python
        /mingw64/bin/git
        /c/Users/smilte/miniforge3/python
        ```

2. The first folder of `PATH`, the one conda's `(base)` put in front. `tr`
   turns each `:` into a line break.

    === "macOS"

        ```text
        $ echo $PATH | tr ':' '\n' | head -n 1
        /opt/homebrew/Caskroom/miniforge/base/bin
        ```

    === "Windows"

        ```text
        $ echo $PATH | tr ':' '\n' | head -n 1
        /c/Users/smilte/miniforge3
        ```

3. What the package manager has installed, and what is out of date.

    === "macOS"

        ```text
        $ brew list
        $ brew outdated
        ```

    === "Windows"

        ```text
        $ winget list --id Git.Git
        $ winget upgrade
        ```

    A package is a program with its version, the packages it needs, and
    where it came from; `brew info git` or `winget show --id Git.Git` prints
    them.

**Check:** everyone can say in which folder their `git` lives.

!!! question "Task: install, use and remove a program"
    `jq` is a small program for JSON files. Install it with your package
    manager, print its version, uninstall it, and show that the shell no
    longer finds it.

??? success "Answer"
    === "macOS"

        ```text
        $ brew install jq
        $ jq --version
        $ brew uninstall jq
        ```

    === "Windows"

        ```text
        $ winget install --id jqlang.jq -e
        ```

        Quit VS Code (**File** > **Exit**) and start it again: it reads the
        new `PATH` when it starts. Then:

        ```text
        $ jq --version
        $ winget uninstall --id jqlang.jq -e
        ```

    `jq --version` prints its version, `jq-1.8.2` or newer. After the
    uninstall, `command -v jq` prints nothing, and `echo $?` prints `1`: not
    found.

---

## Part 2 · Around the project { #part-2 }

<!-- 0:28 to 0:45 -->

A typed line names a program, its options and the files it works on.

---

### 4. Read the prompt: `pwd`, `ls`, `cd` { #terminal }

<!-- 0:28 · 6 min -->

The shell always works in one folder, the **working directory**.

1. Read the prompt aloud: the conda environment, who, where, and the sign
   that it waits (`%` in zsh, `$` in Git Bash).

    === "macOS"

        ```text
        (base) smilte@MacBook-Air weather-s04 %
        ```

    === "Windows"

        ```text
        (base)
        smilte@LAPTOP MINGW64 ~/weather-s04
        $
        ```

2. Where am I.

    ```text
    $ pwd
    /c/Users/smilte/weather-s04
    ```

    macOS: `/Users/smilte/weather-s04`.

3. What is here.

    ```text
    $ ls
    data  incoming  README.md  results  scripts
    ```

    macOS puts `README.md` first: it sorts capitals before small letters.

4. Into `data`, look, back up one level.

    ```text
    $ cd data
    $ ls
    processed  raw
    $ cd ..
    ```

**Check:** the prompt names `weather-s04` again.

---

### 5. Read and count the log { #count }

<!-- 0:34 · 5 min -->

The first lines, the last lines and the size of the log, by command.

1. The first three lines.

    ```text
    $ head -n 3 data/raw/weather.csv
    time,temp_c,humidity_pct,wind_ms
    2016-01-01T00:00,-4.4,93,2.5
    2016-01-01T01:00,-4.8,95,2.6
    ```

2. The last two.

    ```text
    $ tail -n 2 data/raw/weather.csv
    2025-12-31T22:00,-9.9,98,4.1
    2025-12-31T23:00,-11.3,100,4.2
    ```

3. The number of lines.

    ```text
    $ wc -l data/raw/weather.csv
    87673 data/raw/weather.csv
    ```

4. The number of bytes.

    ```text
    $ wc -c data/raw/weather.csv
    2515215 data/raw/weather.csv
    ```

**Check:** 87 673 lines (a header and 87 672 hours), 2 515 215 bytes.

---

### 6. The scripts arrive { #files }

<!-- 0:39 · 6 min -->

Two programs came with the data, in the folder `incoming`; they go into `scripts`.

1. Look into `incoming`.

    ```text
    $ ls incoming
    clean_export.py  column_stats.py
    ```

2. Copy both into `scripts`. `*` stands for any text.

    ```text
    $ cp incoming/*.py scripts/
    $ ls scripts
    clean_export.py  column_stats.py
    ```

3. Delete `incoming`. No Trash: read the line before `Enter`.

    ```text
    $ rm -r incoming
    $ ls
    data  README.md  results  scripts
    ```

**Check:** two `.py` files in `scripts`, also in the Side Bar.

!!! question "Task: the export, counted and copied"
    1. How many lines and bytes have `data/raw/daily_export.csv` and
       `data/processed/daily.csv`? One line for each count.
    2. Make a folder `backup`, copy `daily.csv` into it, rename the copy to
       `daily_copy.csv`, list `backup`, then delete the folder.

??? success "Answer"
    1. `wc` takes several files and adds a total line.

        ```text
        $ wc -l data/raw/daily_export.csv data/processed/daily.csv
         11 data/raw/daily_export.csv
         10 data/processed/daily.csv
         21 total
        $ wc -c data/raw/daily_export.csv data/processed/daily.csv
        180 data/raw/daily_export.csv
        148 data/processed/daily.csv
        328 total
        ```

    2. Five lines; `mv` renames when the target is a new name.

        ```text
        $ mkdir backup
        $ cp data/processed/daily.csv backup/
        $ mv backup/daily.csv backup/daily_copy.csv
        $ ls backup
        daily_copy.csv
        $ rm -r backup
        ```

---

## Part 3 · Search inside files: `grep` { #part-3 }

<!-- 0:45 to 1:15 -->

`grep` prints the lines of a file that hold a text.

---

### 7. Lines that hold a text { #grep }

<!-- 0:45 · 10 min -->

First the text in quotes, then the file. The commas around `-999` make sure the whole value is `-999`.

1. The matching lines, the first three of them: `|` hands the output of
   `grep` to `head`.

    ```text
    $ grep ',-999,' data/raw/weather.csv | head -n 3
    2019-07-22T00:00,-999,76,3.2
    2019-07-22T01:00,-999,81,3.0
    2019-07-22T02:00,-999,80,3.4
    ```

2. Count them: `-c`.

    ```text
    $ grep -c ',-999,' data/raw/weather.csv
    120
    ```

3. With line numbers, the last one: `-n`.

    ```text
    $ grep -n ',-999,' data/raw/weather.csv | tail -n 1
    31273:2019-07-26T23:00,-999,66,1.9
    ```

    The first is line 31 154. 31 273 − 31 154 + 1 = 120 lines in a row: five
    days of 24 hours.

4. Upper and lower case. Every line has a capital `T` between date and hour.

    ```text
    $ grep -c 't' data/raw/weather.csv
    1
    $ grep -ci 't' data/raw/weather.csv
    87673
    ```

    `grep` tells `t` from `T`; `-i` ignores case. Only the header has a small
    `t`.

**Check:** 120 rows marked `-999`, lines 31 154 to 31 273.

---

### 8. Keep the other lines: `grep -v` { #valid }

<!-- 0:55 · 7 min -->

`-v` keeps the lines without the text; `>` writes them into a file.

1. Every line without `,-999,`.

    ```text
    $ grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
    ```

2. Count its lines.

    ```text
    $ wc -l data/processed/weather_valid.csv
    87553 data/processed/weather_valid.csv
    ```

    87 673 − 120 = 87 553.

3. No mark left.

    ```text
    $ grep -c ',-999,' data/processed/weather_valid.csv
    0
    ```

4. Its size.

    ```text
    $ wc -c data/processed/weather_valid.csv
    2511735 data/processed/weather_valid.csv
    ```

    The same bytes on both systems: `grep` copies each line as it is.

**Check:** `weather_valid.csv`, 87 553 lines; `data/raw` untouched.

---

### 9. Patterns: `grep -E` { #regex }

<!-- 1:02 · 13 min -->

A **regular expression** describes a kind of text, not one fixed text. `-E` lets `grep` read `+`, `|` and `( )`.

| Sign | Means |
|--|--|
| `^` | the start of the line |
| `[0-9]` | one digit; `[2-6]` one of 2 to 6 |
| `+` | one or more of what stands before |
| `.` | any one character; `\.` a point itself |
| `.*` | anything, or nothing |

1. A date range: the hours of 22 to 26 July 2019.

    ```text
    $ grep -c '^2019-07-2[2-6]T' data/raw/weather.csv
    120
    ```

    The same 120: every hour of those five days is marked. Check by a
    pipe: of those lines, how many lack the mark?

    ```text
    $ grep '^2019-07-2[2-6]T' data/raw/weather.csv | grep -vc ',-999,'
    0
    ```

2. A year.

    ```text
    $ grep -c '^2024-' data/raw/weather.csv
    8784
    ```

    366 days × 24 hours: 2024 is a leap year.

3. Below freezing. A minus after a comma finds too much:

    ```text
    $ grep -c ',-' data/raw/weather.csv
    22472
    ```

    A minus, digits, a point, one digit, a comma:

    ```text
    $ grep -cE ',-[0-9]+\.[0-9],' data/raw/weather.csv
    22352
    ```

    22 472 − 22 352 = 120: the `-999` rows have no point.

4. Two months: `(01|02)` means `01` or `02`.

    ```text
    $ grep -cE '^2016-(01|02)-' data/raw/weather.csv
    1440
    ```

    (31 + 29) × 24 = 1 440.

**Check:** 120, 8 784, 22 352.

!!! question "Task: questions to the log"
    1. How many hours had 30 °C or more?
    2. How many hours of 2025 were below freezing?
    3. On which line is 29 February 2020, 00:00?
    4. When was the coldest hour, −16.3 °C?

??? success "Answer"
    1. 86. `temp_c` is the only column with a point and a comma after it.

        ```text
        $ grep -cE ',3[0-9]\.[0-9],' data/raw/weather.csv
        86
        ```

    2. 2 677.

        ```text
        $ grep -cE '^2025-.*,-[0-9]+\.[0-9],' data/raw/weather.csv
        2677
        ```

    3. Line 36 482.

        ```text
        $ grep -n '^2020-02-29T00' data/raw/weather.csv
        36482:2020-02-29T00:00,-3.7,89,3.5
        ```

    4. 7 January 2025, 05:00.

        ```text
        $ grep -n ',-16\.3,' data/raw/weather.csv
        79063:2025-01-07T05:00,-16.3,100,3.3
        ```

---

## Part 4 · Find files: `find` { #part-4 }

<!-- 1:15 to 1:30 -->

`find` goes through a folder and every folder below it, and prints each file that passes its tests. `.` is the folder you are in.

---

### 10. Files by name and kind { #find }

<!-- 1:15 · 7 min -->

`-name` tests the name, `-type f` keeps files, `-type d` folders. `find` prints in the order of the disk; `sort` puts the lines in order.

1. Every CSV file of the project. The quotes keep the shell from reading
   `*` itself.

    ```text
    $ find . -name '*.csv' | sort
    ./data/processed/daily.csv
    ./data/processed/weather_valid.csv
    ./data/raw/daily_export.csv
    ./data/raw/weather.csv
    ```

2. Every folder.

    ```text
    $ find . -type d | sort
    .
    ./data
    ./data/processed
    ./data/raw
    ./results
    ./scripts
    ```

3. Every file.

    ```text
    $ find . -type f | sort
    ./data/processed/daily.csv
    ./data/processed/weather_valid.csv
    ./data/raw/daily_export.csv
    ./data/raw/weather.csv
    ./README.md
    ./results/daily.md
    ./scripts/clean_export.py
    ./scripts/column_stats.py
    ```

    macOS puts `./README.md` first.

**Check:** eight files, the same as in the Side Bar.

---

### 11. Files by size and time; search them all { #find-size }

<!-- 1:22 · 8 min -->

`-size` and `-mmin` test size and age; `-exec` runs a command on the files found.

1. Files over 1 MB.

    ```text
    $ find . -type f -size +1M
    ./data/raw/weather.csv
    ./data/processed/weather_valid.csv
    ```

2. Files changed in the last 60 minutes (`-mtime -1`: in the last day).

    ```text
    $ find . -type f -mmin -60
    ./data/processed/weather_valid.csv
    ./scripts/column_stats.py
    ./scripts/clean_export.py
    ```

    The file of section 8 and the two copies of section 6.

3. Which files hold `-999`? `-exec grep -l` runs `grep` on the files found;
   `-l` prints only the names of files with a match. `--` tells `grep` that
   `-999` is the text, not an option.

    ```text
    $ find . -type f -exec grep -l -- '-999' {} +
    ./README.md
    ./data/raw/weather.csv
    ./scripts/column_stats.py
    ```

**Check:** `-999` stands in the README, the raw log and a script's
description, and not in `weather_valid.csv`.

!!! question "Task: find the small files"
    1. Which files are smaller than 1 000 bytes? (`c` after a number means
       bytes.)
    2. Every `.py` file.
    3. Which files mention `temp_c`?

??? success "Answer"
    1. `-size -1000c`: fewer than 1 000 bytes.

        ```text
        $ find . -type f -size -1000c
        ./data/raw/daily_export.csv
        ./data/processed/daily.csv
        ./results/daily.md
        ```

    2. A name test alone finds files and folders; no folder ends in `.py`.

        ```text
        $ find . -name '*.py'
        ./scripts/column_stats.py
        ./scripts/clean_export.py
        ```

    3. Every data file, the README, `results/daily.md` and one script.

        ```text
        $ find . -type f -exec grep -l 'temp_c' {} + | sort
        ./data/processed/daily.csv
        ./data/processed/weather_valid.csv
        ./data/raw/daily_export.csv
        ./data/raw/weather.csv
        ./README.md
        ./results/daily.md
        ./scripts/column_stats.py
        ```

---

## Part 5 · The mean, made by one command { #part-5 }

<!-- 1:30 to 2:00 -->

A script repeats the cleaning; a checksum shows that it made the same bytes as the hand repair.

---

### 12. Compare the script's file with yours: a checksum { #checksum }

<!-- 1:30 · 6 min -->

A SHA-256 checksum is 64 hex digits computed from every byte: the same bytes give the same digits on every laptop.

1. The checksum of `data/processed/daily.csv`, the export repaired by hand
   in a text editor.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/daily.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/daily.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        ```

2. Keep it under another name.

    ```text
    $ mv data/processed/daily.csv data/processed/daily_hand.csv
    ```

3. Let the script make the four edits: `python`, then the script, then the
   file it reads and the file it writes.

    ```text
    $ python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    9 rows written to data/processed/daily.csv
    ```

4. Both checksums.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/daily*.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily_hand.csv
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/daily*.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily.csv
        33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d  data/processed/daily_hand.csv
        ```

5. The same 148 bytes. Delete the hand-made copy.

    ```text
    $ rm data/processed/daily_hand.csv
    ```

**Check:** `33fe5e77…f705483d` on every laptop in the room.

---

### 13. The mean, with and without the `-999` rows { #python }

<!-- 1:36 · 4 min -->

`column_stats.py` prints the rows, the smallest, the largest and the mean of one column.

1. Over the raw log.

    ```text
    $ python scripts/column_stats.py data/raw/weather.csv temp_c
    file    data/raw/weather.csv
    column  temp_c
    rows    87672
    min     -999.0
    max     32.4
    mean    5.7828
    ```

2. Over the valid rows.

    ```text
    $ python scripts/column_stats.py data/processed/weather_valid.csv temp_c
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

**Check:** 7.16 °C, the mean of Lecture 1; 5.78 counts −999 as a temperature.

---

### 14. One script makes it all again { #script }

<!-- 1:40 · 9 min -->

The lines of today in one file: one command makes `data/processed` and `results` again.

1. In the Side Bar, click `scripts`, **New File**:

    ```text
    rebuild.sh
    ```

2. Windows: the Status Bar says `CRLF`; click it and choose `LF`.
3. Type the six lines and save. Line 1 names the program that runs the
   file; `set -e` stops it at the first error.

    ```text
    #!/usr/bin/env bash
    set -e
    mkdir -p data/processed results
    grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
    python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
    ```

4. macOS only: mark the file as a program that may run.

    ```text
    $ chmod +x scripts/rebuild.sh
    ```

5. Delete everything the script makes.

    ```text
    $ rm -r data/processed
    ```

6. Run it. `./` says "this folder": the shell does not search it.

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    ```

7. What it made, and the result.

    ```text
    $ ls data/processed results
    data/processed:
    daily.csv  weather_valid.csv

    results:
    daily.md  temp_c.txt
    $ cat results/temp_c.txt
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

**Check:** `mean 7.15997` in `results/temp_c.txt`, made by one line.

!!! warning "`$'\r': command not found` or `set: -: invalid option`"
    The script was saved with CRLF: step 2, save, run again.

---

### 15. The README: result and how to rebuild { #readme }

<!-- 1:49 · 6 min -->

The README says what the result is and which line makes it.

1. In `README.md`, delete the item **Cleaned copy** of the Data list: the
   script makes that file now.
2. At the end of the README, add two sections. The command line is indented
   by four spaces.

    ```text
    ## Result

    Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
    marked `-999` are left out. The script writes it to `results/temp_c.txt`.

    ## How to rebuild

    In the project folder, in zsh on macOS or Git Bash on Windows, with Python
    from Miniforge; the script needs no package beyond it.

        ./scripts/rebuild.sh

    It writes `data/processed/weather_valid.csv`, `weather.csv` without the
    120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
    cleaned export (148 bytes).
    ```

3. Check the headings.

    ```text
    $ grep -n '^## ' README.md
    6:## Folders
    15:## Data
    24:## Columns of `weather.csv`
    36:## Result
    41:## How to rebuild
    ```

    Your line numbers may differ.

**Check:** five sections, and no **Cleaned copy** line.

!!! question "Task: the other columns"
    1. The mean `humidity_pct` over the raw log and over `weather_valid.csv`.
       Which one is right?
    2. The mean `wind_ms`.

??? success "Answer"
    1. 79.0974 over the raw log (87 672 rows), 79.1172 over the valid rows
       (87 552). The raw one is right: in the 120 marked hours only the
       thermometer was down, so their humidity was measured.

        ```text
        $ python scripts/column_stats.py data/raw/weather.csv humidity_pct
        file    data/raw/weather.csv
        column  humidity_pct
        rows    87672
        min     34.0
        max     100.0
        mean    79.0974
        ```

    2. 3.50352 m/s.

        ```text
        $ python scripts/column_stats.py data/raw/weather.csv wind_ms
        file    data/raw/weather.csv
        column  wind_ms
        rows    87672
        min     0.0
        max     12.0
        mean    3.50352
        ```

---

### 16. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->


| To | Type |
|--|--|
| install, list, remove a program | `brew install`, `brew list`, `brew uninstall` · `winget install --id`, `winget list`, `winget uninstall` |
| where am I, what is here | `pwd`, `ls`, `cd` |
| read, count | `head -n 3`, `tail -n 2`, `wc -l`, `wc -c` |
| copy, move, delete | `cp`, `mv`, `rm -r` |
| lines with a text, or without | `grep`, `-c`, `-n`, `-i`, `-v`, `-E` |
| files by name, kind, size, age | `find . -name '*.csv'`, `-type f`, `-size +1M`, `-mmin -60` |
| a checksum | `shasum -a 256 FILE` · `sha256sum FILE` |
| everything again | `./scripts/rebuild.sh` |

---

## Optional, if the room goes fast { #optional }

---

### 17. Stop at the first error { #stop }

<!-- — · 5 min -->

Without `set -e` a script runs on after a failed line and hides the failure.

1. In `scripts/rebuild.sh`, change `daily_export.csv` to `daily_exprt.csv`
   and save.
2. Run it, then ask for its status: `0` is success.

    ```text
    $ ./scripts/rebuild.sh
    no file data/raw/daily_exprt.csv
    $ echo $?
    1
    ```

    It stopped at line 5; line 6 did not run.

3. Put `daily_export.csv` back and save.

**Check:** the script runs to the end again.

---

### 18. A list of checksums { #list }

<!-- — · 5 min -->

Written once when the raw files arrive, checked after every copy. Windows: `sha256sum` for `shasum -a 256`.

1. The checksums of `data/raw`, into a file.

    ```text
    $ shasum -a 256 data/raw/* > data/checksums.txt
    ```

2. Check them: `-c` computes each again and compares.

    ```text
    $ shasum -a 256 -c data/checksums.txt
    data/raw/daily_export.csv: OK
    data/raw/weather.csv: OK
    ```

3. In VS Code, change `6,3` to `6,4` in `data/raw/daily_export.csv`, save,
   check again.

    ```text
    data/raw/daily_export.csv: FAILED
    data/raw/weather.csv: OK
    sha256sum: WARNING: 1 computed checksum did NOT match
    ```

    macOS starts the last line with `shasum:`.

4. Change `6,4` back to `6,3`, save, check: two `OK`.

**Check:** the raw files match the list again.

---

### 19. Rows per year { #years }

<!-- — · 5 min -->

`cut -c1-4` keeps the first four characters, the year; `uniq -c` counts equal lines next to each other.

1. Count the rows of each year.

    ```text
    $ cut -c1-4 data/raw/weather.csv | uniq -c
          1 time
       8784 2016
       8760 2017
       8760 2018
       8760 2019
       8784 2020
       8760 2021
       8760 2022
       8760 2023
       8784 2024
       8760 2025
    ```

**Check:** three leap years of 8 784 hours, seven of 8 760: 87 672.

---

### 20. A conda environment for the project { #environment }

<!-- — · 10 min -->

One environment per project: its own Python and packages, written down in `environment.yml`.

1. Make it and switch it on.

    ```text
    $ conda create -n s04 python=3.14 -y
    $ conda activate s04
    ```

    The prompt starts with `(s04)`.

2. Its own Python.

    ```text
    $ which python
    ```

    === "macOS"

        ```text
        /opt/homebrew/Caskroom/miniforge/base/envs/s04/bin/python
        ```

    === "Windows"

        ```text
        /c/Users/smilte/miniforge3/envs/s04/python
        ```

3. Write it down.

    ```text
    $ conda env export --from-history > environment.yml
    ```

    Open `environment.yml`, delete its last line, `prefix: ...`, and save.

    ```text
    name: s04
    channels:
      - conda-forge
    dependencies:
      - python=3.14
    ```

4. Back to `base`.

    ```text
    $ conda deactivate
    ```

**Check:** `environment.yml` in the project folder.

---

### 21. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions to the same files, each solved by joining the commands of today with `|`.

!!! question "Task: the cold hours of 2025, month by month"
    How many hours of 2025 were at −10 °C or colder, and in which months?
    Use `grep -E`, then `cut` and `uniq -c` (section 19) on the matching
    lines.

??? success "Answer"
    `-1[0-9]\.[0-9]` is a minus, a 1, one more digit, a point and a digit:
    −10.0 to −19.9. `cut -c1-7` keeps the year and the month.

    ```text
    $ grep -cE '^2025-.*,-1[0-9]\.[0-9],' data/raw/weather.csv
    322
    $ grep -E '^2025-.*,-1[0-9]\.[0-9],' data/raw/weather.csv | cut -c1-7 | uniq -c
        103 2025-01
         86 2025-02
        133 2025-12
    ```

    322 = 103 + 86 + 133: January, February and December, none in March.
    macOS pads the counts with fewer spaces.

!!! question "Task: the three warmest and the three coldest hours"
    `sort` puts lines in order. Find its options for a comma between the
    columns (`-t`), for sorting by the second column only (`-k2,2`), as
    numbers (`-n`) and backwards (`-r`), and print the three warmest and
    the three coldest hours of `weather_valid.csv`.

??? success "Answer"
    ```text
    $ sort -t, -k2,2 -n -r data/processed/weather_valid.csv | head -n 3
    2018-06-18T15:00,32.4,52,3.1
    2018-06-18T16:00,32.3,53,2.4
    2019-06-14T13:00,32.2,63,6.0
    $ sort -t, -k2,2 -n data/processed/weather_valid.csv | head -n 3
    2025-01-07T05:00,-16.3,100,3.3
    2025-01-07T03:00,-16.1,100,3.0
    2025-01-07T06:00,-16.1,100,3.9
    ```

    Without `-n`, `sort` compares characters, and `-16.3` would sort
    after `-1.0`. On `data/raw/weather.csv` the coldest lines would be the
    120 marks of −999: the reason for `weather_valid.csv`.

!!! question "Task: the script also writes the number of marked rows"
    Add one line to `scripts/rebuild.sh` that writes `missing 120` into
    `results/missing.txt`, with the 120 counted by `grep`, not typed. Run
    the script and show the file. (`$( )` puts the output of a command into
    a line.)

??? success "Answer"
    The last line of `scripts/rebuild.sh`:

    ```text
    echo "missing $(grep -c ',-999,' data/raw/weather.csv)" > results/missing.txt
    ```

    ```text
    $ ./scripts/rebuild.sh
    9 rows written to data/processed/daily.csv
    $ cat results/missing.txt
    missing 120
    ```

    The shell runs the command inside `$( )` first and puts its output,
    `120`, into the text before `echo` runs. If the station sends a new log
    with more marks, the file follows by itself.

---

## Aims practised

- ⚙️ **Automation:** the searches, the cleaning and the mean are lines in
  `scripts/rebuild.sh`; one command makes every result again.
- ♻️ **Reproducibility:** the hand repair and the script give the same
  checksum; the README states the result and the line that makes it.
- 🔧 **Tool-agnostic:** the same `grep`, `find` and `python` lines in zsh and
  Git Bash; programs installed and removed by a package manager.
