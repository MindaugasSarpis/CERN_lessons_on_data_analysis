# Seminar 4 — What Is the Mean Temperature of Ten Years? PowerShell on the Weather Project

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student installs PowerShell 7, Git and Python with a
package manager, searches `weather.csv` and the project folder by command,
gets the mean temperature, 7.16 °C, and writes a script that makes every
result again.

Everything is typed in the terminal of VS Code, in PowerShell 7, the same on
macOS and Windows. Only the installs of section 1 differ by system.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · Install with a package manager** · 28 min | | |
| 0:00 | [1. Install the tools](#installs) | `brew install`, `winget install` | PowerShell 7, Git, Miniforge |
| 0:12 | [2. VS Code opens PowerShell 7](#shell) | **Select Default Profile** | `(base) PS`, `7`, `conda 26.7.2` |
| 0:20 | [3. Where the programs landed](#packages) | `(Get-Command git).Source` | each program's folder, `PATH` |
| | **Part 2 · Around the project** · 17 min | | |
| 0:28 | [4. Read the prompt: `pwd`, `Get-ChildItem`, `cd`](#terminal) | `Get-ChildItem -Name` | the folders by name |
| 0:34 | [5. Read and count the log](#count) | `(Get-Content data/raw/weather.csv).Count` | 87 673 lines, 2 515 215 bytes |
| 0:39 | [6. The scripts arrive](#files) | `Copy-Item ~/weather-scripts/*.py scripts` | two scripts in `scripts` |
| | **Part 3 · Search inside files: `Select-String`** · 30 min | | |
| 0:45 | [7. Lines that hold a text](#grep) | `Select-String ',-999,' data/raw/weather.csv` | 120 rows, lines 31 154 to 31 273 |
| 0:55 | [8. Keep the other lines: `-NotMatch`](#valid) | `... -NotMatch -Raw > ...` | `weather_valid.csv`, 87 553 lines |
| 1:02 | [9. Patterns: regular expressions](#regex) | `'^2019-07-2[2-6]T'` | 120, 8 784, 22 352 |
| | **Part 4 · Find files: `Get-ChildItem`** · 15 min | | |
| 1:15 | [10. Files by name and kind](#find) | `Get-ChildItem -Recurse -Filter *.csv` | the four CSV files |
| 1:22 | [11. Files by size and time; search them all](#find-size) | `Where-Object Length -gt 1MB` | two large files; where `-999` stands |
| | **Part 5 · The mean, made by one command** · 25 min | | |
| 1:30 | [12. The script against your hand: a checksum](#checksum) | `Get-FileHash` | `33FE5E77…F705483D` twice |
| 1:36 | [13. The mean, with and without the `-999` rows](#python) | `python scripts/column_stats.py` | 5.7828 and 7.15997 |
| 1:40 | [14. One script makes it all again](#script) | `./scripts/rebuild.ps1` | `results/temp_c.txt` |
| 1:49 | [15. The README: result and how to rebuild](#readme) | `## Result` | the README of the course |
| 1:55 | [16. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [17. Stop at the first error](#stop) | `daily_exprt.csv` | the script stops |
| — | [18. A list of checksums](#list) | `Compare-Object` | one changed file caught |
| — | [19. Rows per year](#years) | `Group-Object` | 8 784 or 8 760 a year |
| — | [20. A conda environment for the project](#environment) | `conda create -n weather` | `environment.yml` |

**If time runs short:** the Task of Part 4 can go; never cut sections 12 to
15: they give the answer and the script.

??? info "Before the session"
    - **Room:** internet, and laptops on which students can install programs
      (macOS asks for the laptop's password, Windows for an administrator's
      **Yes**). Each student has `weather-project` from Seminars 1 and 3;
      section 2 has the zip for anyone without it.
    - **You:** nothing to prepare. The two zips are on the Releases page of
      [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project/releases).
      [Install Python, Git and PowerShell 7](install_python_git.md) has
      every error message of the installs, for helpers.
    - **Outputs** are from macOS, user `smilte`. On Windows paths start with
      `C:\Users\smilte` and use `\`.

---

## Part 1 · Install with a package manager { #part-1 }

**0:00 to 0:28** · A package manager fetches a program, puts it in one known folder and on `PATH`, and later updates or removes it.

---

### 1. Install the tools { #installs }

**0:00 · 12 min** · Three programs: PowerShell 7, the shell of the course; Git, from Seminar 5; Miniforge, Python with conda. VS Code stays closed.

1. Open the system's terminal.

    === "macOS"

        `Cmd+Space`, type `Terminal`, `Enter`. Its shell is `zsh`, used only
        for these installs.

    === "Windows"

        Windows key, type `powershell`, `Enter`: Windows PowerShell 5.1,
        with the package manager `winget` built in.

2. macOS only: install the package manager **Homebrew**.

    === "macOS"

        ```text
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

        Type the laptop's password (nothing shows while typing), then
        `Enter` to continue. It may install the developer tools of macOS
        first (5 to 15 minutes). At the end it prints **Next steps**: copy
        the lines it lists there, paste them, `Enter`.

        ```text
        brew --version
        ```

        A line that starts with `Homebrew`.

    === "Windows"

        Nothing to do: `winget` is there.

        ```text
        winget --version
        ```

3. Install the three programs, one line at a time.

    === "macOS"

        ```text
        brew install --cask powershell
        ```

        ```text
        brew install git
        ```

        ```text
        brew install --cask miniforge
        ```

        Each ends with a line like `🍺  powershell was successfully installed!`

    === "Windows"

        ```text
        winget install --id Microsoft.PowerShell -e
        ```

        ```text
        winget install --id Git.Git -e
        ```

        ```text
        winget install --id CondaForge.Miniforge3 -e
        ```

        Each ends with `Successfully installed`. Answer `Y` if winget asks
        about the source agreements, **Yes** if Windows asks for
        permission.

4. Let conda set up PowerShell, so that every new PowerShell finds Python.

    === "macOS"

        ```text
        conda init powershell
        ```

    === "Windows"

        ```text
        & "$HOME\miniforge3\Scripts\conda.exe" init powershell
        ```

    ```text
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

5. Close the terminal window.

**Check:** three programs installed, and conda's last line.

!!! warning "No password, or no administrator's **Yes**"
    The laptop is managed by the university or an employer. The student
    pairs with a neighbour today.

---

### 2. VS Code opens PowerShell 7 { #shell }

**0:12 · 8 min** · The **terminal** is the window; the **shell** is the program in it that reads each line; from today it is PowerShell 7 on both systems.

1. Open VS Code: **File** > **Open Folder...** > `weather-project` (in your
   home folder) > **Open**.
2. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). Type and choose:

    ```text
    Terminal: Select Default Profile
    ```

    Take **pwsh** (macOS) or **PowerShell** (Windows). Not **zsh**, not
    **Windows PowerShell**.

3. Command Palette again:

    ```text
    Terminal: Create New Terminal
    ```

    The Panel opens at the bottom; its top right says `pwsh`.

4. Check the shell.

    ```text
    $PSVersionTable.PSVersion.Major
    ```

    ```text
    7
    ```

5. Check conda and Python.

    ```text
    conda --version
    ```

    ```text
    conda 26.7.2
    ```

    ```text
    python --version
    ```

    ```text
    Python 3.14.7
    ```

    `python` is the name on both systems.

**Check:** the prompt starts with `(base) PS`.

??? warning "No `weather-project` from Seminars 1 and 3"
    Download `weather-project-s1.zip` from the Releases page
    (`github.com/MindaugasSarpis/weather-project/releases`, under
    **Assets**). In the terminal of VS Code:

    ```text
    Expand-Archive ~/Downloads/weather-project-s1.zip -DestinationPath ~
    ```

    Then step 1 again.

!!! warning "`Python was not found` (Windows), or no `(base)` in the prompt"
    conda is not set up in this PowerShell: section 1, step 4 again, then
    quit VS Code (**File** > **Exit**, macOS `Cmd+Q`) and start it again.

---

### 3. Where the programs landed { #packages }

**0:20 · 8 min** · The shell finds a program by searching the folders of `PATH`, in order.

1. Where `git` is.

    ```text
    (Get-Command git).Source
    ```

    === "macOS"

        ```text
        /opt/homebrew/bin/git
        ```

    === "Windows"

        ```text
        C:\Program Files\Git\cmd\git.exe
        ```

2. Where `python` is.

    ```text
    (Get-Command python).Source
    ```

    === "macOS"

        ```text
        /opt/homebrew/Caskroom/miniforge/base/bin/python
        ```

    === "Windows"

        ```text
        C:\Users\smilte\miniforge3\python.exe
        ```

3. The first folder of `PATH`: the one conda's `(base)` put in front.

    ```text
    $env:PATH -split [IO.Path]::PathSeparator | Select-Object -First 1
    ```

    === "macOS"

        ```text
        /opt/homebrew/Caskroom/miniforge/base/bin
        ```

    === "Windows"

        ```text
        C:\Users\smilte\miniforge3
        ```

4. What the package manager has installed, and what is out of date.

    === "macOS"

        ```text
        brew list
        ```

        ```text
        brew outdated
        ```

    === "Windows"

        ```text
        winget list --id Git.Git
        ```

        ```text
        winget upgrade
        ```

    A package is a program with its version, the packages it needs, and
    where it came from; `brew info git` or `winget show --id Git.Git` prints
    them.

**Check:** everyone can say in which folder their `git` lives.

!!! question "Task: install, use and remove a program"
    `jq` is a small program for JSON files. Install it with your package
    manager, print its version, uninstall it, and show that the shell no
    longer finds it.

??? note "Answer"
    === "macOS"

        ```text
        brew install jq
        ```

        ```text
        jq --version
        ```

        ```text
        brew uninstall jq
        ```

    === "Windows"

        ```text
        winget install --id jqlang.jq -e
        ```

        Quit VS Code (**File** > **Exit**) and start it again: it reads the
        new `PATH` when it starts. Then:

        ```text
        jq --version
        ```

        ```text
        winget uninstall --id jqlang.jq -e
        ```

    `jq --version` prints its version, `jq-1.8.2` or newer. After the
    uninstall:

    ```text
    Get-Command jq
    ```

    ```text
    Get-Command: The term 'jq' is not recognized as a name of a cmdlet, function, script file, or executable program.
    ```

---

## Part 2 · Around the project { #part-2 }

**0:28 to 0:45** · `pwd`, `cd` and `dir` work in PowerShell on both systems. `ls`, `cp`, `mv`, `rm` and `cat` run other programs on a Mac, so this page writes the full names: `Get-ChildItem`, `Copy-Item`, `Move-Item`, `Remove-Item`, `Get-Content`.

---

### 4. Read the prompt: `pwd`, `Get-ChildItem`, `cd` { #terminal }

**0:28 · 6 min** · The shell always works in one folder, the **working directory**.

1. Read the prompt aloud: the conda environment, `PS`, the folder, `>`.

    ```text
    (base) PS /Users/smilte/weather-project>
    ```

2. Where am I.

    ```text
    pwd
    ```

    ```text
    Path
    ----
    /Users/smilte/weather-project
    ```

3. What is here, names only.

    ```text
    Get-ChildItem -Name
    ```

    ```text
    data
    results
    scripts
    README.md
    ```

4. Into `data`, look, back up one level.

    ```text
    cd data
    ```

    ```text
    Get-ChildItem -Name
    ```

    ```text
    processed
    raw
    ```

    ```text
    cd ..
    ```

5. The raw files with their sizes.

    ```text
    Get-ChildItem data/raw
    ```

    ```text
    UnixMode         User Group         LastWriteTime         Size Name
    --------         ---- -----         -------------         ---- ----
    -rw-r--r--     smilte staff      10/13/2026 09:30          180 daily_export.csv
    -rw-r--r--     smilte staff      10/13/2026 09:30      2515215 weather.csv
    ```

    Windows shows the columns `Mode`, `LastWriteTime`, `Length`, `Name`.
    Your dates differ.

**Check:** the prompt ends in `weather-project>` again.

---

### 5. Read and count the log { #count }

**0:34 · 5 min** · The numbers of Seminars 1 and 3, by command.

1. The first three lines.

    ```text
    Get-Content data/raw/weather.csv -TotalCount 3
    ```

    ```text
    time,temp_c,humidity_pct,wind_ms
    2016-01-01T00:00,-4.4,93,2.5
    2016-01-01T01:00,-4.8,95,2.6
    ```

2. The last two.

    ```text
    Get-Content data/raw/weather.csv -Tail 2
    ```

    ```text
    2025-12-31T22:00,-9.9,98,4.1
    2025-12-31T23:00,-11.3,100,4.2
    ```

3. The number of lines.

    ```text
    (Get-Content data/raw/weather.csv).Count
    ```

    ```text
    87673
    ```

4. The size in bytes.

    ```text
    (Get-Item data/raw/weather.csv).Length
    ```

    ```text
    2515215
    ```

**Check:** 87 673 lines (a header and 87 672 hours), 2 515 215 bytes.

---

### 6. The scripts arrive { #files }

**0:39 · 6 min** · Two programs come with the data; they go into `scripts`.

1. On the Releases page (`github.com/MindaugasSarpis/weather-project/releases`),
   under **Assets**, click `weather-scripts.zip`.
2. Unpack it into the home folder.

    ```text
    Expand-Archive ~/Downloads/weather-scripts.zip -DestinationPath ~
    ```

    ```text
    Get-ChildItem ~/weather-scripts -Name
    ```

    ```text
    clean_export.py
    column_stats.py
    ```

3. Copy both into `scripts`. `*` stands for any text.

    ```text
    Copy-Item ~/weather-scripts/*.py scripts
    ```

    ```text
    Get-ChildItem scripts -Name
    ```

    ```text
    clean_export.py
    column_stats.py
    ```

4. Delete the unpacked folder. No Trash: check the name before `Enter`.

    ```text
    Remove-Item ~/weather-scripts -Recurse
    ```

**Check:** two `.py` files in `scripts`, also in the Side Bar.

!!! question "Task: the export, counted and copied"
    1. How many lines and bytes have `data/raw/daily_export.csv` and
       `data/processed/daily.csv`?
    2. Make a folder `backup`, copy `daily.csv` into it, rename the copy to
       `daily_copy.csv`, list `backup`, then delete the folder.

??? note "Answer"
    1. 11 lines and 180 bytes; 10 lines and 148 bytes.

        ```text
        (Get-Content data/raw/daily_export.csv).Count
        ```

        ```text
        (Get-Item data/processed/daily.csv).Length
        ```

    2. ```text
       New-Item -ItemType Directory backup
       ```

        ```text
        Copy-Item data/processed/daily.csv backup
        ```

        ```text
        Move-Item backup/daily.csv backup/daily_copy.csv
        ```

        ```text
        Get-ChildItem backup -Name
        ```

        ```text
        daily_copy.csv
        ```

        ```text
        Remove-Item backup -Recurse
        ```

---

## Part 3 · Search inside files: `Select-String` { #part-3 }

**0:45 to 1:15** · `Select-String` keeps the lines of a file that hold a text: the `grep` of PowerShell.

---

### 7. Lines that hold a text { #grep }

**0:45 · 10 min** · Each match is printed with its file and line number.

1. The full form: `-Pattern` is the text, `-Path` the file. The first three
   matches.

    ```text
    Select-String -Pattern ',-999,' -Path data/raw/weather.csv | Select-Object -First 3
    ```

    ```text
    data/raw/weather.csv:31154:2019-07-22T00:00,-999,76,3.2
    data/raw/weather.csv:31155:2019-07-22T01:00,-999,81,3.0
    data/raw/weather.csv:31156:2019-07-22T02:00,-999,80,3.4
    ```

    The commas around `-999` make sure the whole value is `-999`.

2. The short form, pattern first, file second; `.Count` counts the matches.

    ```text
    (Select-String ',-999,' data/raw/weather.csv).Count
    ```

    ```text
    120
    ```

3. The last match.

    ```text
    Select-String ',-999,' data/raw/weather.csv | Select-Object -Last 1
    ```

    ```text
    data/raw/weather.csv:31273:2019-07-26T23:00,-999,66,1.9
    ```

    31 273 − 31 154 + 1 = 120 lines in a row: five days of 24 hours.

4. Upper and lower case. Every line has a `T` between date and hour.

    ```text
    (Select-String 't' data/raw/weather.csv).Count
    ```

    ```text
    87673
    ```

    ```text
    (Select-String 't' data/raw/weather.csv -CaseSensitive).Count
    ```

    ```text
    1
    ```

    `Select-String` ignores case unless told `-CaseSensitive`: only the
    header has a small `t`.

**Check:** 120 rows marked `-999`, lines 31 154 to 31 273.

---

### 8. Keep the other lines: `-NotMatch` { #valid }

**0:55 · 7 min** · `-NotMatch` keeps the lines without the text; `>` writes them into a file.

1. Every line without `,-999,`. `-Raw` prints the line alone, without file
   name and number.

    ```text
    Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
    ```

2. Count its lines.

    ```text
    (Get-Content data/processed/weather_valid.csv).Count
    ```

    ```text
    87553
    ```

    87 673 − 120 = 87 553.

3. No mark left.

    ```text
    (Select-String ',-999,' data/processed/weather_valid.csv).Count
    ```

    ```text
    0
    ```

4. Its size.

    ```text
    (Get-Item data/processed/weather_valid.csv).Length
    ```

    ```text
    2511735
    ```

    Windows: 2 599 288. There `>` ends each line with CRLF, one byte more on
    each of 87 553 lines. The number of lines is the same.

**Check:** `weather_valid.csv`, 87 553 lines; `data/raw` untouched.

---

### 9. Patterns: regular expressions { #regex }

**1:02 · 13 min** · A **regular expression** describes a kind of text, not one fixed text. `Select-String` reads every pattern as one.

| Sign | Means |
|--|--|
| `^` | the start of the line |
| `[0-9]` | one digit; `[2-6]` one of 2 to 6 |
| `+` | one or more of what stands before |
| `.` | any one character; `\.` a point itself |
| `.*` | anything, or nothing |

1. A date range: the hours of 22 to 26 July 2019.

    ```text
    (Select-String '^2019-07-2[2-6]T' data/raw/weather.csv).Count
    ```

    ```text
    120
    ```

    The same 120: every hour of those five days is marked. Check:

    ```text
    (Select-String '^2019-07-2[2-6]T' data/raw/weather.csv | Select-String ',-999,' -NotMatch).Count
    ```

    ```text
    0
    ```

2. A year.

    ```text
    (Select-String '^2024-' data/raw/weather.csv).Count
    ```

    ```text
    8784
    ```

    366 days × 24 hours: 2024 is a leap year.

3. Below freezing. A minus after a comma finds too much:

    ```text
    (Select-String ',-' data/raw/weather.csv).Count
    ```

    ```text
    22472
    ```

    A minus, digits, a point, one digit, a comma:

    ```text
    (Select-String ',-[0-9]+\.[0-9],' data/raw/weather.csv).Count
    ```

    ```text
    22352
    ```

    22 472 − 22 352 = 120: the `-999` rows have no point.

**Check:** 120, 8 784, 22 352.

!!! question "Task: questions to the log"
    1. How many hours had 30 °C or more?
    2. How many hours of 2025 were below freezing?
    3. On which line is 29 February 2020, 00:00?
    4. When was the coldest hour, −16.3 °C?

??? note "Answer"
    1. 86. `temp_c` is the only column with a point and a comma after it.

        ```text
        (Select-String ',3[0-9]\.[0-9],' data/raw/weather.csv).Count
        ```

    2. 2 677.

        ```text
        (Select-String '^2025-.*,-[0-9]+\.[0-9],' data/raw/weather.csv).Count
        ```

    3. Line 36 482.

        ```text
        Select-String '^2020-02-29T00' data/raw/weather.csv
        ```

        ```text
        data/raw/weather.csv:36482:2020-02-29T00:00,-3.7,89,3.5
        ```

    4. 7 January 2025, 05:00.

        ```text
        Select-String ',-16\.3,' data/raw/weather.csv
        ```

        ```text
        data/raw/weather.csv:79063:2025-01-07T05:00,-16.3,100,3.3
        ```

---

## Part 4 · Find files: `Get-ChildItem` { #part-4 }

**1:15 to 1:30** · `Get-ChildItem -Recurse` goes through every folder below this one: the `find` of PowerShell.

---

### 10. Files by name and kind { #find }

**1:15 · 7 min** · `-Filter` picks names, `-File` and `-Directory` pick the kind, `-Name` prints paths only.

1. Every CSV file of the project.

    ```text
    Get-ChildItem -Recurse -Filter *.csv -Name
    ```

    ```text
    data/processed/daily.csv
    data/processed/weather_valid.csv
    data/raw/daily_export.csv
    data/raw/weather.csv
    ```

2. Every folder.

    ```text
    Get-ChildItem -Recurse -Directory -Name
    ```

    ```text
    data
    results
    scripts
    data/processed
    data/raw
    ```

3. Every file.

    ```text
    Get-ChildItem -Recurse -File -Name
    ```

    ```text
    README.md
    data/processed/daily.csv
    data/processed/weather_valid.csv
    data/raw/daily_export.csv
    data/raw/weather.csv
    results/daily.md
    scripts/clean_export.py
    scripts/column_stats.py
    ```

    `results/daily.md` is there if you made it in Seminar 1.

**Check:** eight files or seven, the same in the Side Bar.

---

### 11. Files by size and time; search them all { #find-size }

**1:22 · 8 min** · `Where-Object` keeps the files whose property passes a test; the pipe `|` hands the files on.

1. Files over 1 MB.

    ```text
    Get-ChildItem -Recurse -File | Where-Object Length -gt 1MB | Select-Object Name, Length
    ```

    ```text
    Name               Length
    ----               ------
    weather.csv       2515215
    weather_valid.csv 2511735
    ```

2. Files written in the last hour.

    ```text
    Get-ChildItem -Recurse -File | Where-Object LastWriteTime -gt (Get-Date).AddHours(-1) | Select-Object Name
    ```

    ```text
    Name
    ----
    weather_valid.csv
    ```

    `Copy-Item` kept the scripts' own dates, so only the file of section 8
    is new.

3. Search inside every file: `-List` stops at the first match in each.

    ```text
    Get-ChildItem -Recurse -File | Select-String '-999' -List | Select-Object Filename, LineNumber
    ```

    ```text
    Filename        LineNumber
    --------        ----------
    README.md               35
    weather.csv          31154
    column_stats.py         13
    ```

    The README line number is that of your own README.

**Check:** `-999` stands in the README, the raw log and a script's
description, and not in `weather_valid.csv`.

!!! question "Task: find the small files"
    1. Which files are smaller than 1 kB?
    2. Every `.py` file, with its size.
    3. Which files mention `temp_c`?

??? note "Answer"
    1. ```text
       Get-ChildItem -Recurse -File | Where-Object Length -lt 1KB | Select-Object Name, Length
       ```

        ```text
        Name             Length
        ----             ------
        daily_export.csv    180
        daily.csv           148
        daily.md            216
        ```

    2. ```text
       Get-ChildItem -Recurse -Filter *.py | Select-Object Name, Length
       ```

        ```text
        Name            Length
        ----            ------
        clean_export.py   1779
        column_stats.py   1577
        ```

    3. Every data file, the README and one script.

        ```text
        Get-ChildItem -Recurse -File | Select-String 'temp_c' -List | Select-Object Filename
        ```

---

## Part 5 · The mean, made by one command { #part-5 }

**1:30 to 2:00**

---

### 12. The script against your hand: a checksum { #checksum }

**1:30 · 6 min** · A SHA-256 checksum is 64 hex digits computed from every byte: the same bytes give the same digits on every laptop.

1. The checksum of the `daily.csv` you repaired by hand in Seminar 1.

    ```text
    (Get-FileHash data/processed/daily.csv).Hash
    ```

    ```text
    33FE5E77A97900B6E8F94776F266DA4D6E3C96590088D21BC9842987F705483D
    ```

2. Keep it under another name.

    ```text
    Move-Item data/processed/daily.csv data/processed/daily_hand.csv
    ```

3. Let the script make the four edits. On macOS and Windows it is
   `python`, then the script, then the file it reads and the file it writes.

    ```text
    python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    ```

    ```text
    9 rows written to data/processed/daily.csv
    ```

4. Both checksums.

    ```text
    Get-FileHash data/processed/daily*.csv | Select-Object Hash
    ```

    ```text
    Hash
    ----
    33FE5E77A97900B6E8F94776F266DA4D6E3C96590088D21BC9842987F705483D
    33FE5E77A97900B6E8F94776F266DA4D6E3C96590088D21BC9842987F705483D
    ```

5. The same 148 bytes. Delete the hand-made copy.

    ```text
    Remove-Item data/processed/daily_hand.csv
    ```

**Check:** `33FE5E77…F705483D` on every laptop in the room.

---

### 13. The mean, with and without the `-999` rows { #python }

**1:36 · 4 min** · `column_stats.py` prints the rows, the smallest, the largest and the mean of one column.

1. Over the raw log.

    ```text
    python scripts/column_stats.py data/raw/weather.csv temp_c
    ```

    ```text
    file    data/raw/weather.csv
    column  temp_c
    rows    87672
    min     -999.0
    max     32.4
    mean    5.7828
    ```

2. Over the valid rows.

    ```text
    python scripts/column_stats.py data/processed/weather_valid.csv temp_c
    ```

    ```text
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

**1:40 · 9 min** · The lines of today in one file: one command makes `data/processed` and `results` again.

1. In the Side Bar, click `scripts`, **New File**:

    ```text
    rebuild.ps1
    ```

2. Type the six lines and save. The first two make the script stop at the
   first error.

    ```text
    $ErrorActionPreference = 'Stop'
    $PSNativeCommandUseErrorActionPreference = $true
    New-Item -ItemType Directory -Force data/processed, results | Out-Null
    Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
    python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
    python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
    ```

3. Delete everything the script makes.

    ```text
    Remove-Item data/processed -Recurse
    ```

4. Run it. `./` says "in this folder".

    ```text
    ./scripts/rebuild.ps1
    ```

    ```text
    9 rows written to data/processed/daily.csv
    ```

5. What it made.

    ```text
    Get-ChildItem data/processed, results -Name
    ```

    ```text
    daily.csv
    weather_valid.csv
    daily.md
    temp_c.txt
    ```

6. The result.

    ```text
    Get-Content results/temp_c.txt
    ```

    ```text
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

**Check:** `mean 7.15997` in `results/temp_c.txt`, made by one line.

---

### 15. The README: result and how to rebuild { #readme }

**1:49 · 6 min** · The README says what the result is and which line makes it.

1. In `README.md`, delete the item **Cleaned copy** of the Data list: the
   script makes that file now.
2. At the end of the README, add two sections.

    ```text
    ## Result

    Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
    marked `-999` are left out. The script writes it to `results/temp_c.txt`.

    ## How to rebuild

    In the project folder, in PowerShell 7 on macOS or Windows, with Python from
    Miniforge; the script needs no package beyond it.

        ./scripts/rebuild.ps1

    It writes `data/processed/weather_valid.csv`, `weather.csv` without the
    120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
    cleaned export (148 bytes).
    ```

3. Check the headings.

    ```text
    Select-String '^## ' README.md
    ```

    ```text
    README.md:6:## Folders
    README.md:15:## Data
    README.md:24:## Columns of `weather.csv`
    README.md:36:## Result
    README.md:41:## How to rebuild
    ```

    Your line numbers may differ.

**Check:** five sections, and no **Cleaned copy** line.

!!! question "Task: the other columns"
    1. The mean `humidity_pct` over the raw log and over `weather_valid.csv`.
       Which one is right?
    2. The mean `wind_ms`.

??? note "Answer"
    1. 79.0974 over the raw log (87 672 rows), 79.1172 over the valid rows
       (87 552). The raw one is right: in the 120 marked hours only the
       thermometer was down, so their humidity was measured.

        ```text
        python scripts/column_stats.py data/raw/weather.csv humidity_pct
        ```

    2. 3.50352 m/s.

        ```text
        python scripts/column_stats.py data/raw/weather.csv wind_ms
        ```

---

### 16. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
| install, list, remove a program | `brew install`, `brew list`, `brew uninstall` · `winget install --id`, `winget list`, `winget uninstall` |
| where am I, what is here | `pwd`, `Get-ChildItem -Name` |
| read, count | `Get-Content -TotalCount 3`, `(Get-Content FILE).Count` |
| copy, move, delete | `Copy-Item`, `Move-Item`, `Remove-Item -Recurse` |
| lines with a text, or without | `Select-String 'TEXT' FILE`, `-NotMatch`, `-CaseSensitive` |
| files by name, size, time | `Get-ChildItem -Recurse -Filter`, `Where-Object Length -gt 1MB` |
| a checksum | `(Get-FileHash FILE).Hash` |
| everything again | `./scripts/rebuild.ps1` |

Seminar 5 clones the course's copy of this project with Git.

---

## Optional, if the room is fast { #optional }

---

### 17. Stop at the first error { #stop }

**— · 5 min** · Without its first two lines a script runs on after a failed line and hides the failure.

1. In `scripts/rebuild.ps1`, change `daily_export.csv` to `daily_exprt.csv`
   and save.
2. Run it.

    ```text
    ./scripts/rebuild.ps1
    ```

    ```text
    no file data/raw/daily_exprt.csv
    NativeCommandExitException: /Users/smilte/weather-project/scripts/rebuild.ps1:5
    Line |
       5 |  python scripts/clean_export.py data/raw/daily_exprt.csv data/processe …
         |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         | Program "python" ended with non-zero exit code: 1 (0x01).
    ```

    It stopped at line 5; line 6 did not run.

3. Put `daily_export.csv` back and save.

**Check:** the script runs to the end again.

---

### 18. A list of checksums { #list }

**— · 5 min** · Written once when the raw files arrive, checked after every copy.

1. The checksums of `data/raw`, into a file.

    ```text
    (Get-FileHash data/raw/*).Hash | Set-Content data/checksums.txt
    ```

2. Compare the list with the files now. Nothing printed: nothing changed.

    ```text
    Compare-Object (Get-Content data/checksums.txt) (Get-FileHash data/raw/*).Hash
    ```

3. In VS Code, change `6,3` to `6,4` in `data/raw/daily_export.csv`, save,
   compare again.

    ```text
    InputObject                                                      SideIndicator
    -----------                                                      -------------
    13FBCAE6A7A4D67EC30FDF3BEDC0B666209F7A4DC453EA72FF6DE7370FFD6AEE =>
    9D849815D88ECEB18366EE66AC72F26B72E195BEA8BB20AA9A1474372513BBDB <=
    ```

    `<=` is the line of the list, `=>` the file now.

4. Change `6,4` back to `6,3`, save, compare: nothing printed.

**Check:** the raw files match the list again.

---

### 19. Rows per year { #years }

**— · 5 min** · `Import-Csv` reads the columns; `Group-Object` counts rows by a key.

1. Group by the first four characters of `time`.

    ```text
    Import-Csv data/raw/weather.csv | Group-Object { $_.time.Substring(0,4) } -NoElement
    ```

    ```text
    Count Name
    ----- ----
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

**— · 10 min** · One environment per project: its own Python and packages, written down in `environment.yml`.

1. Make it and switch it on.

    ```text
    conda create -n weather python=3.14 -y
    ```

    ```text
    conda activate weather
    ```

    The prompt starts with `(weather)`.

2. Its own Python.

    ```text
    (Get-Command python).Source
    ```

    === "macOS"

        ```text
        /opt/homebrew/Caskroom/miniforge/base/envs/weather/bin/python
        ```

    === "Windows"

        ```text
        C:\Users\smilte\miniforge3\envs\weather\python.exe
        ```

3. Write it down.

    ```text
    conda env export --from-history > environment.yml
    ```

    Open `environment.yml`, delete its last line, `prefix: ...`, and save.

    ```text
    name: weather
    channels:
      - conda-forge
    dependencies:
      - python=3.14
    ```

4. Back to `base`.

    ```text
    conda deactivate
    ```

**Check:** `environment.yml` in the project folder.

---

## Aims practised

- ⚙️ **Automation:** the searches, the cleaning and the mean are lines in
  `scripts/rebuild.ps1`; one command makes every result again.
- ♻️ **Reproducibility:** the hand repair and the script give the same
  checksum; the README states the result and the line that makes it.
- 🔧 **Tool-agnostic:** one shell, PowerShell 7, with the same lines on macOS
  and Windows; programs installed and removed by a package manager.
