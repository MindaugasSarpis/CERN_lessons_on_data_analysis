# Seminar 4 · Command Line

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** What was the mean temperature of the evening the sensor
failed? Every student installs Git and Python with a package manager, types
six hours of the station's log into `weather.csv`, finds its two `-999`
rows with `grep` and keeps the other four, gets the mean temperature,
25.275 °C, and writes a script that makes every result again.

Everything is typed in the terminal of VS Code: `zsh` on macOS, Git Bash on
Windows, the data too, from this page. The lines are the same in both; only
the installs and the checksum command differ. In the blocks, a line that
starts with `$` is typed (a Mac shows `%`), and every other line is what
comes back.

Further reading: [The Unix Shell, Software Carpentry](https://swcarpentry.github.io/shell-novice/),
the lessons this seminar follows in spirit, on other data.

**If time runs short:** the Tasks and section 14 can go; never cut sections
10 to 13 and 15: they give the answer, the script and the README.

??? info "Before the session"
    - **Room:** internet for the installs, and laptops on which students can
      install programs (macOS asks for the laptop's password, Windows for an
      administrator's **Yes**). The session needs no file and nothing from
      any other seminar.
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

<!-- 0:00 · 14 min -->

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
        permission. Then close the PowerShell window.

5. macOS only: let conda set up `zsh`, so that every new terminal finds
   Python (Windows does this in section 2, in Git Bash). Then close the
   Terminal window.

    ```text
    $ conda init zsh
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

**Check:** Git and Miniforge installed.

!!! warning "No password, or no administrator's **Yes**"
    The laptop is managed by the university or an employer. The student
    pairs with a neighbour today.

---

### 2. VS Code's terminal and conda { #shell }

<!-- 0:14 · 6 min -->

The **terminal** is the window; the **shell** is the program in it that reads each line: `zsh` on macOS, Git Bash on Windows.

1. Open VS Code, with no folder: the project folder is made in section 4.
2. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). Type and choose:

    ```text
    Terminal: Select Default Profile
    ```

    Take **zsh** (macOS) or **Git Bash** (Windows).

3. Command Palette again:

    ```text
    Terminal: Create New Terminal
    ```

    With no folder open, it starts in your home folder.

4. Windows only: let conda set up Git Bash. Then close the terminal (the
   bin icon of the Panel) and open a new one: **Terminal: Create New
   Terminal** in the Command Palette.

    ```text
    $ ~/miniforge3/Scripts/conda.exe init bash
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

5. Check the shell.

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

6. Check conda and Python. `python` is the name on both systems.

    ```text
    $ conda --version
    conda 26.7.2
    $ python --version
    Python 3.14.7
    ```

**Check:** `(base)` in the prompt: conda's first environment, with Python in it.

!!! warning "`python: command not found`, or no `(base)` in the prompt"
    conda is not set up in this shell: run `conda init zsh` (macOS) or
    `~/miniforge3/Scripts/conda.exe init bash` (Windows) again, then quit
    VS Code (**File** > **Exit**, macOS `Cmd+Q`) and start it again.

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

2. The first folder of `PATH`, the one conda's `(base)` put in front. A
   pipe, `|`, hands the output of one command to the next: `tr` turns each
   `:` into a line break, `head -n 1` keeps the first line.

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

<!-- 0:28 to 0:52 -->

A typed line names a program, its options and the files it works on.

---

### 4. Read the prompt, make the project folder: `pwd`, `mkdir`, `cd` { #terminal }

<!-- 0:28 · 8 min -->

The shell always works in one folder, the **working directory**; a new terminal starts in the home folder, `~`.

1. Read the prompt aloud: the conda environment, who, where (`~`), and the
   sign that it waits (`%` in zsh, `$` in Git Bash).

    === "macOS"

        ```text
        (base) smilte@MacBook-Air ~ %
        ```

    === "Windows"

        ```text
        (base)
        smilte@LAPTOP MINGW64 ~
        $
        ```

2. Where am I.

    ```text
    $ pwd
    /c/Users/smilte
    ```

    macOS: `/Users/smilte`.

3. Make the project folder and go into it.

    ```text
    $ mkdir weather-s04
    $ cd weather-s04
    $ pwd
    /c/Users/smilte/weather-s04
    ```

4. Its four folders, in one line. `-p` makes `data` on the way to
   `data/raw`, and says nothing if a folder is already there.

    ```text
    $ mkdir -p data/raw data/processed scripts results
    $ ls
    data  results  scripts
    ```

5. Into `data`, look, back up one level.

    ```text
    $ cd data
    $ ls
    processed  raw
    $ cd ..
    ```

6. Open the folder in VS Code: **File** > **Open Folder...** >
   `weather-s04` (in your home folder) > **Open**, and answer **Yes, I
   trust the authors**. The window starts again; open a terminal:
   **Terminal: Create New Terminal** in the Command Palette.

**Check:** the prompt names `weather-s04`; the Side Bar shows `data`, `results` and `scripts`.

---

### 5. Write the log into a file, read and count it { #count }

<!-- 0:36 · 8 min -->

Six hours of the station's log, the evening its temperature sensor failed, 21 to 22 July 2019; the station's full log has 87 672 such rows, 2016 to 2025.

1. Write the file from the terminal: `<<'EOF'` gives `cat` the lines typed
   next, up to `EOF`, and `>` sends what `cat` prints into the file, new or
   overwritten. While it reads, the shell answers `>` (zsh: `heredoc>`).

    ```text
    $ cat > data/raw/weather.csv <<'EOF'
    > time,temp_c,humidity_pct,wind_ms
    > 2019-07-21T20:00,27.3,63,4.5
    > 2019-07-21T21:00,25.6,65,4.0
    > 2019-07-21T22:00,24.6,68,3.5
    > 2019-07-21T23:00,23.6,74,3.4
    > 2019-07-22T00:00,-999,76,3.2
    > 2019-07-22T01:00,-999,81,3.0
    > EOF
    ```

    Nothing comes back. A typo: type the block again.

2. The first three lines.

    ```text
    $ head -n 3 data/raw/weather.csv
    time,temp_c,humidity_pct,wind_ms
    2019-07-21T20:00,27.3,63,4.5
    2019-07-21T21:00,25.6,65,4.0
    ```

3. The last two: the hours the sensor was down, marked `-999`.

    ```text
    $ tail -n 2 data/raw/weather.csv
    2019-07-22T00:00,-999,76,3.2
    2019-07-22T01:00,-999,81,3.0
    ```

4. The number of lines.

    ```text
    $ wc -l data/raw/weather.csv
    7 data/raw/weather.csv
    ```

5. The number of bytes.

    ```text
    $ wc -c data/raw/weather.csv
    207 data/raw/weather.csv
    ```

    The header is 32 characters, each hour 28, and every line ends with one
    byte, LF: 33 + 6 × 29 = 207.

**Check:** 7 lines (a header and 6 hours), 207 bytes.

---

### 6. Write the export, count both files { #files }

<!-- 0:44 · 8 min -->

The daily mean temperatures of 1 to 9 October 2025 as a spreadsheet exported them: `;` between the values, a decimal comma, a row number `nr` in front and a mean line at the end.

1. Write it from the terminal: `cat`, the lines, `EOF`.

    ```text
    $ cat > data/raw/daily_export.csv <<'EOF'
    > nr;date;temp_c
    > 1;2025-10-01;6,3
    > 2;2025-10-02;5,0
    > 3;2025-10-03;5,6
    > 4;2025-10-04;7,0
    > 5;2025-10-05;9,4
    > 6;2025-10-06;10,4
    > 7;2025-10-07;9,2
    > 8;2025-10-08;9,0
    > 9;2025-10-09;9,8
    > ;mean;7,97
    > EOF
    ```

2. What is in `data/raw` now.

    ```text
    $ ls data/raw
    daily_export.csv  weather.csv
    ```

3. The lines of both files. `*` stands for any text, so `data/raw/*.csv`
   names both; `wc` adds a total line.

    ```text
    $ wc -l data/raw/*.csv
     11 data/raw/daily_export.csv
      7 data/raw/weather.csv
     18 total
    ```

4. Their bytes.

    ```text
    $ wc -c data/raw/*.csv
    180 data/raw/daily_export.csv
    207 data/raw/weather.csv
    387 total
    ```

**Check:** two files in `data/raw`, also in the Side Bar: 11 and 7 lines.

!!! question "Task: a backup of `data/raw`"
    1. Make a folder `backup`, copy both CSV files of `data/raw` into it
       with one `cp`, rename `backup/daily_export.csv` to
       `export_copy.csv`, list `backup`, then delete the folder.
    2. Which line of the export is not a day? Print it with one command.

??? success "Answer"
    1. `mv` renames when the target is a new name. `rm -r` deletes a folder
       with everything in it, and there is no Trash: read the line before
       `Enter`.

        ```text
        $ mkdir backup
        $ cp data/raw/*.csv backup/
        $ mv backup/daily_export.csv backup/export_copy.csv
        $ ls backup
        export_copy.csv  weather.csv
        $ rm -r backup
        ```

    2. The last one, the spreadsheet's mean.

        ```text
        $ tail -n 1 data/raw/daily_export.csv
        ;mean;7,97
        ```

---

## Part 3 · Search inside files: `grep` { #part-3 }

<!-- 0:52 to 1:12 -->

`grep` prints the lines of a file that hold a text.

---

### 7. Lines that hold a text { #grep }

<!-- 0:52 · 5 min -->

`grep` prints the lines of a file that hold a text: first the text in quotes, then the file. The commas around `-999` make it match the whole value only.

1. The matching lines.

    ```text
    $ grep ',-999,' data/raw/weather.csv
    2019-07-22T00:00,-999,76,3.2
    2019-07-22T01:00,-999,81,3.0
    ```

2. Count them: `-c`.

    ```text
    $ grep -c ',-999,' data/raw/weather.csv
    2
    ```

3. With line numbers, `-n`: the failure starts on line 6, at midnight.

    ```text
    $ grep -n ',-999,' data/raw/weather.csv
    6:2019-07-22T00:00,-999,76,3.2
    7:2019-07-22T01:00,-999,81,3.0
    ```

**Check:** 2 rows marked `-999`, lines 6 and 7.

---

### 8. Keep the other lines: `grep -v` { #valid }

<!-- 0:57 · 5 min -->

`-v` keeps the lines without the text; `>` writes them into a file instead of onto the screen.

1. Every line without `,-999,`.

    ```text
    $ grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
    ```

2. Read it.

    ```text
    $ cat data/processed/weather_valid.csv
    time,temp_c,humidity_pct,wind_ms
    2019-07-21T20:00,27.3,63,4.5
    2019-07-21T21:00,25.6,65,4.0
    2019-07-21T22:00,24.6,68,3.5
    2019-07-21T23:00,23.6,74,3.4
    ```

3. Count its lines: 7 − 2 = 5.

    ```text
    $ wc -l data/processed/weather_valid.csv
    5 data/processed/weather_valid.csv
    ```

4. No mark left.

    ```text
    $ grep -c ',-999,' data/processed/weather_valid.csv
    0
    ```

5. Its size: 207 − 2 × 29 = 149.

    ```text
    $ wc -c data/processed/weather_valid.csv
    149 data/processed/weather_valid.csv
    ```

**Check:** `weather_valid.csv`, 5 lines; `data/raw` untouched.

---

### 9. A pattern for a measured temperature: `grep -E` { #regex }

<!-- 1:02 · 10 min -->

A **regular expression** describes a kind of text, not one fixed text. `-E` lets `grep` read `+` and `?` as signs.

1. The hours of 22 July: `^` is the start of the line.

    ```text
    $ grep -c '^2019-07-22T' data/raw/weather.csv
    2
    ```

    Both marked? The pipe, `|`, hands these lines to a second `grep`, which
    counts the ones without the mark.

    ```text
    $ grep '^2019-07-22T' data/raw/weather.csv | grep -vc ',-999,'
    0
    ```

2. A measured temperature, between commas: `-?` a minus or none, `[0-9]+`
   one or more digits, `\.` a point (a bare `.` fits any character),
   `[0-9]` one digit.

    ```text
    $ grep -cE ',-?[0-9]+\.[0-9],' data/raw/weather.csv
    4
    ```

    Only `temp_c` has a point and a comma after it.

3. The lines that do not fit, with their numbers: `-v` and `-n` together.

    ```text
    $ grep -vnE ',-?[0-9]+\.[0-9],' data/raw/weather.csv
    1:time,temp_c,humidity_pct,wind_ms
    6:2019-07-22T00:00,-999,76,3.2
    7:2019-07-22T01:00,-999,81,3.0
    ```

    The header and the two marks: `-999` is the only mark. A typo such as
    `23,6` for `23.6` would show here too, with its line number.

**Check:** 4 hours fit a measured temperature; the 3 lines that do not are the header and the 2 marks of 22 July.

!!! question "Task: questions to the log"
    1. How many hours had 25 °C or more?
    2. Which hours had a humidity of 70 % or more?
    3. On which line is 23:00?

??? success "Answer"
    1. Two, 20:00 and 21:00. `[5-9]` is one digit of 5 to 9; `temp_c` is
       the only column with a point and a comma after it.

        ```text
        $ grep -cE ',2[5-9]\.[0-9],' data/raw/weather.csv
        2
        ```

    2. 23:00, 00:00 and 01:00. `humidity_pct` is the only column with two
       digits and no point between its commas.

        ```text
        $ grep -E ',[7-9][0-9],' data/raw/weather.csv
        2019-07-21T23:00,23.6,74,3.4
        2019-07-22T00:00,-999,76,3.2
        2019-07-22T01:00,-999,81,3.0
        ```

    3. Line 5.

        ```text
        $ grep -n 'T23:00' data/raw/weather.csv
        5:2019-07-21T23:00,23.6,74,3.4
        ```

---

## Part 4 · The mean by `awk`, the export by a pipe { #part-4 }

<!-- 1:12 to 1:31 -->

A checksum shows that two programs made the same bytes; `awk` computes the mean.

---

### 10. Keep the measured rows a second way, compare by checksum { #checksum }

<!-- 1:12 · 6 min -->

A SHA-256 checksum is 64 hex digits computed from every byte: the same bytes give the same digits on every laptop.

1. The checksum of `data/processed/weather_valid.csv`, the file `grep -v`
   made in section 8.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/weather_valid.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/weather_valid.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

2. The same rows by another program, `awk`. `-F,` splits each line at the
   commas, `$2` is field 2, and `awk` prints the lines for which the test is
   true: `!=` is "not equal". The header passes: `temp_c` is not `-999`.

    ```text
    $ awk -F, '$2 != -999' data/raw/weather.csv
    time,temp_c,humidity_pct,wind_ms
    2019-07-21T20:00,27.3,63,4.5
    2019-07-21T21:00,25.6,65,4.0
    2019-07-21T22:00,24.6,68,3.5
    2019-07-21T23:00,23.6,74,3.4
    ```

3. Into a second file.

    ```text
    $ awk -F, '$2 != -999' data/raw/weather.csv > data/processed/weather_awk.csv
    ```

4. Both checksums.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/weather_*.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_awk.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/weather_*.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_awk.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

5. The same 149 bytes from two programs. Delete the second copy.

    ```text
    $ rm data/processed/weather_awk.csv
    ```

**Check:** `d029d87a…9061d6a` on every laptop in the room; other digits mean a typo in `weather.csv`: compare it line by line with the six hours of section 5.

---

### 11. The mean, with and without the `-999` rows: `awk` { #python }

<!-- 1:18 · 5 min -->

`awk` also computes: a program in `{ }` runs on every line it selects, one in `END { }` once, after the last line.

1. Field 2 of every line.

    ```text
    $ awk -F, '{ print $2 }' data/raw/weather.csv
    temp_c
    27.3
    25.6
    24.6
    23.6
    -999
    -999
    ```

2. The mean over the raw log. `NR` is the line number, so `NR > 1` leaves
   out the header; `s += $2` adds field 2 to `s`, `n++` adds one to `n`;
   at the end it prints the count and the sum over the count.

    ```text
    $ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/raw/weather.csv
    6 -316.15
    ```

3. Over the valid rows: `↑` brings the line back, change the file.

    ```text
    $ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/processed/weather_valid.csv
    4 25.275
    ```

**Check:** 25.275 °C, (27.3 + 25.6 + 24.6 + 23.6) / 4 = 101.1 / 4; −316.15 counts −999 as a temperature: (101.1 − 1 998) / 6.

---

### 12. Clean the export by one line: `grep -v`, `tr`, `cut` { #export }

<!-- 1:23 · 8 min -->

The four edits of a hand repair as one pipe: the mean line out, `,` to `.`, `;` to `,`, the column `nr` out.

1. The mean line out: `^;` is a `;` at the start of the line.

    ```text
    $ grep -v '^;' data/raw/daily_export.csv | tail -n 2
    8;2025-10-08;9,0
    9;2025-10-09;9,8
    ```

2. Two signs swapped. `tr ',;' '.,'` replaces each character of the first
   set by the one in the same place of the second, both in one pass: one
   after the other, every `;` turned into `,` would then become `.` too.

    ```text
    $ grep -v '^;' data/raw/daily_export.csv | tr ',;' '.,' | head -n 3
    nr,date,temp_c
    1,2025-10-01,6.3
    2,2025-10-02,5.0
    ```

3. The column `nr` out: `cut -d, -f2-` keeps field 2 to the end.

    ```text
    $ grep -v '^;' data/raw/daily_export.csv | tr ',;' '.,' | cut -d, -f2- | head -n 3
    date,temp_c
    2025-10-01,6.3
    2025-10-02,5.0
    ```

4. Into the file, and its size. `↑`, then replace `| head -n 3` by
   `> data/processed/daily.csv`.

    ```text
    $ grep -v '^;' data/raw/daily_export.csv | tr ',;' '.,' | cut -d, -f2- > data/processed/daily.csv
    $ wc -l data/processed/daily.csv
    10 data/processed/daily.csv
    $ wc -c data/processed/daily.csv
    148 data/processed/daily.csv
    ```

    The header and its LF are 12 bytes, eight days like `2025-10-01,6.3`
    15 each, `2025-10-06,10.4` 16: 12 + 8 × 15 + 16 = 148.

**Check:** `data/processed/daily.csv`, 10 lines, 148 bytes.

!!! question "Task: the other columns"
    1. The mean `humidity_pct` over the raw log and over `weather_valid.csv`.
       Which one is right?
    2. The mean `wind_ms`.
    3. The mean of the nine days in `data/processed/daily.csv`. Does it match
       the export's last line?

??? success "Answer"
    1. 71.1667 over the raw log (6 rows), 67.5 over the valid rows (4). The
       raw one is right: in the 2 marked hours only the thermometer was
       down, so their humidity was measured. Field 3 is `$3`.

        ```text
        $ awk -F, 'NR > 1 { s += $3; n++ } END { print n, s / n }' data/raw/weather.csv
        6 71.1667
        $ awk -F, 'NR > 1 { s += $3; n++ } END { print n, s / n }' data/processed/weather_valid.csv
        4 67.5
        ```

    2. 3.6 m/s.

        ```text
        $ awk -F, 'NR > 1 { s += $4; n++ } END { print n, s / n }' data/raw/weather.csv
        6 3.6
        ```

    3. 7.96667, the 7,97 of the spreadsheet before rounding: 71.7 / 9.

        ```text
        $ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/processed/daily.csv
        9 7.96667
        ```

---

## Part 5 · A script for every result { #part-5 }

<!-- 1:31 to 2:00 -->

A script repeats every step of today; `set -e` stops it at the first failure.

---

### 13. One script makes it all again { #script }

<!-- 1:31 · 9 min -->

The lines of today in one file: one command makes `data/processed` and `results` again.

1. In the Side Bar, click `scripts`, **New File**:

    ```text
    rebuild.sh
    ```

2. Windows: the Status Bar says `CRLF`; click it and choose `LF`.
3. Type the six lines and save. Line 1 names the program that runs the
   file; `set -e` stops it at the first error. Lines 4 to 6 are the
   `grep -v` of section 8, the export pipe of section 12 and the `awk` mean
   of section 11.

    ```text
    #!/usr/bin/env bash
    set -e
    mkdir -p data/processed results
    grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
    grep -v '^;' data/raw/daily_export.csv | tr ',;' '.,' | cut -d, -f2- > data/processed/daily.csv
    awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/processed/weather_valid.csv > results/temp_c.txt
    ```

4. macOS only: mark the file as a program that may run.

    ```text
    $ chmod +x scripts/rebuild.sh
    ```

5. Delete everything the script makes. `rm -r` deletes a folder with
   everything in it, and there is no Trash.

    ```text
    $ rm -r data/processed results
    ```

6. Run it. `./` says "this folder": the shell does not search it. Nothing
   comes back: every result goes into a file.

    ```text
    $ ./scripts/rebuild.sh
    ```

7. What it made, and the result.

    ```text
    $ ls data/processed results
    data/processed:
    daily.csv  weather_valid.csv

    results:
    temp_c.txt
    $ cat results/temp_c.txt
    4 25.275
    ```

8. The checksum of the new `weather_valid.csv`: still `d029d87a…9061d6a`,
   the bytes the typed `grep -v` line made.

    === "macOS"

        ```text
        $ shasum -a 256 data/processed/weather_valid.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

    === "Windows"

        ```text
        $ sha256sum data/processed/weather_valid.csv
        d029d87add61a7e6b3fe0cef506b761e796da323a5e503af79077f0cc9061d6a  data/processed/weather_valid.csv
        ```

**Check:** `4 25.275` in `results/temp_c.txt`, made by one line.

!!! warning "`$'\r': command not found` or `set: -: invalid option`"
    The script was saved with CRLF: click `CRLF` in the Status Bar, choose
    `LF`, save, run again.

---

### 14. Stop at the first error { #stop }

<!-- 1:40 · 6 min -->

`set -e` ends a script at the first line that fails, before a later line works on a broken file.

1. In line 4 of `scripts/rebuild.sh`, change `data/raw/weather.csv` to
   `data/raw/wether.csv` and save.
2. Run it, then ask for its status: `0` is success.

    ```text
    $ ./scripts/rebuild.sh
    grep: data/raw/wether.csv: No such file or directory
    $ echo $?
    2
    ```

    It stopped at line 4; lines 5 and 6 did not run. The `>` had already
    emptied the file it writes:

    ```text
    $ wc -c data/processed/weather_valid.csv
    0 data/processed/weather_valid.csv
    ```

3. Put `weather.csv` back in line 4, save, and run the script again.

    ```text
    $ ./scripts/rebuild.sh
    $ wc -c data/processed/weather_valid.csv
    149 data/processed/weather_valid.csv
    ```

**Check:** the script runs to the end again; `weather_valid.csv` has 149 bytes.

---

### 15. The README: result and how to rebuild { #readme }

<!-- 1:46 · 10 min -->

The README says what the folder holds, what the result is and which line makes it.

1. In the Side Bar, click an empty place under the folders, then the
   **New File** icon at its top:

    ```text
    README.md
    ```

2. Type it and save. The command line is indented by four spaces.

    ```text
    # Weather Station

    Six hours of the station's hourly log, from 21 July 2019, 20:00, to 22
    July, 01:00, and the daily mean temperatures of 1 to 9 October 2025.

    ## Data

    - `data/raw/weather.csv`: one row per hour; `temp_c` is `-999` while the
      temperature sensor was down.
    - `data/raw/daily_export.csv`: a spreadsheet's export, with `;` between
      the values and a decimal comma.

    ## Result

    Mean `temp_c`: **25.275 °C**, over the 4 measured hours; the 2 hours
    marked `-999` are left out. `results/temp_c.txt` holds the hours and the
    mean.

    ## How to rebuild

    In the project folder, in zsh on macOS or Git Bash on Windows:

        ./scripts/rebuild.sh

    It writes `data/processed/weather_valid.csv`, `weather.csv` without the
    rows marked `-999`, and `data/processed/daily.csv`, the cleaned export.
    ```

3. Check the headings.

    ```text
    $ grep -n '^## ' README.md
    6:## Data
    13:## Result
    19:## How to rebuild
    ```

    Your line numbers may differ.

**Check:** three sections: Data, Result, How to rebuild.

!!! question "Task: the script also writes the number of marked rows"
    Add one line to `scripts/rebuild.sh` that writes `missing 2` into
    `results/missing.txt`, with the 2 counted by `grep`, not typed. Run
    the script and show the file. (`$( )` puts the output of a command into
    a line.)

??? success "Answer"
    The last line of `scripts/rebuild.sh`:

    ```text
    echo "missing $(grep -c ',-999,' data/raw/weather.csv)" > results/missing.txt
    ```

    ```text
    $ ./scripts/rebuild.sh
    $ cat results/missing.txt
    missing 2
    ```

    The shell runs the command inside `$( )` first and puts its output,
    `2`, into the text before `echo` runs. If the station sends a new log
    with more marks, the file follows by itself.

---

### 16. Wrap up { #wrap-up }

<!-- 1:56 · 4 min -->

The answer to today's question, made again by one command; then today's commands.

1. Run the script once more and read its result: 25.275 °C, the mean
   temperature of the evening the sensor failed, over the 4 hours it
   measured.

    ```text
    $ ./scripts/rebuild.sh
    $ cat results/temp_c.txt
    4 25.275
    ```

2. The commands for programs, folders and files, one row at a time.

    | To | Type |
    |--|--|
    | install, list, remove a program | `brew install`, `brew list`, `brew uninstall` · `winget install --id`, `winget list`, `winget uninstall` |
    | where am I, what is here, a new folder | `pwd`, `ls`, `cd`, `mkdir -p` |
    | a file from typed lines | `cat > FILE <<'EOF'`, the lines, `EOF` |
    | read, count | `head -n 3`, `tail -n 2`, `wc -l`, `wc -c` |
    | copy, move, delete | `cp`, `mv`, `rm -r` |

3. The commands for rows, the mean and the script.

    | To | Type |
    |--|--|
    | lines with a text, or without | `grep`, `-c`, `-n`, `-v` |
    | lines of a kind | `grep -E '^…'`, `[0-9]+`, `-?`, `\.` |
    | swap characters, keep columns | `tr ',;' '.,'`, `cut -d, -f2-` |
    | rows by a test, a mean | `awk -F, '$2 != -999'`, `awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }'` |
    | a checksum | `shasum -a 256 FILE` · `sha256sum FILE` |
    | everything again, stop at an error | `./scripts/rebuild.sh`, `set -e`, `echo $?` |

---

## Optional, if the room goes fast { #optional }

---

### 17. Files by name and kind { #find }

<!-- — · 5 min -->

`find` goes through a folder and every folder inside it, and prints each file that passes its tests; `.` is the folder you are in.

1. Every CSV file of the project. `-name` tests the name; the quotes keep
   the shell from reading `*` itself. `find` prints in the order of the
   disk; `sort` puts the lines in order.

    ```text
    $ find . -name '*.csv' | sort
    ./data/processed/daily.csv
    ./data/processed/weather_valid.csv
    ./data/raw/daily_export.csv
    ./data/raw/weather.csv
    ```

2. Every file: `-type f` keeps files, not folders.

    ```text
    $ find . -type f | sort
    ./data/processed/daily.csv
    ./data/processed/weather_valid.csv
    ./data/raw/daily_export.csv
    ./data/raw/weather.csv
    ./README.md
    ./results/temp_c.txt
    ./scripts/rebuild.sh
    ```

    macOS puts `./README.md` first. The script makes the files in
    `data/processed` and `results` again; the other four are the ones to
    keep.

**Check:** two raw files, the script, the README, and in `data/processed` and `results` what the script makes.

---

### 18. Files by size; search inside every file { #find-size }

<!-- — · 7 min -->

`-size` tests the size of a file; `-exec` runs a command on the files found.

1. Files over 150 bytes: `c` after the number means bytes, `+` more than.

    ```text
    $ find . -type f -size +150c | sort
    ./data/raw/daily_export.csv
    ./data/raw/weather.csv
    ./README.md
    ./scripts/rebuild.sh
    ```

    macOS puts `./README.md` first.

2. Which files hold `-999`? `-exec grep -l` runs `grep -l` on the files
   found, and it prints only the names of files with a match; `--` says
   that `-999` is the text, not an option.

    ```text
    $ find . -type f -exec grep -l -- '-999' {} + | sort
    ./data/raw/weather.csv
    ./README.md
    ./scripts/rebuild.sh
    ```

    The log, the README and the script; nothing the script made.

**Check:** `-999` stands in the raw log, the README and the script, and in nothing in `data/processed` or `results`.

!!! question "Task: find the small files"
    1. Which files are smaller than 150 bytes?
    2. Every file whose name starts with `weather`.
    3. Which files mention `temp_c`?

??? success "Answer"
    1. `-size -150c`: fewer than 150 bytes. The files the script makes:
       `weather_valid.csv` has 149, `daily.csv` 148 (and
       `results/missing.txt`, if the script writes it).

        ```text
        $ find . -type f -size -150c | sort
        ./data/processed/daily.csv
        ./data/processed/weather_valid.csv
        ./results/temp_c.txt
        ```

    2. `*` after the name: any text, or none.

        ```text
        $ find . -name 'weather*' | sort
        ./data/processed/weather_valid.csv
        ./data/raw/weather.csv
        ```

    3. Six. `results/temp_c.txt` is not among them: it has `temp_c` in its
       name, not in its text; the README and the script name that file.

        ```text
        $ find . -type f -exec grep -l 'temp_c' {} + | sort
        ./data/processed/daily.csv
        ./data/processed/weather_valid.csv
        ./data/raw/daily_export.csv
        ./data/raw/weather.csv
        ./README.md
        ./scripts/rebuild.sh
        ```

---

### 19. A list of checksums { #list }

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
   and check again.

    ```text
    $ shasum -a 256 -c data/checksums.txt
    data/raw/daily_export.csv: FAILED
    data/raw/weather.csv: OK
    shasum: WARNING: 1 computed checksum did NOT match
    ```

    Git Bash's `sha256sum` starts the last line with `sha256sum:`.

4. Change `6,4` back to `6,3`, save, check: two `OK`.

**Check:** the raw files match the list again.

---

### 20. Rows per day { #years }

<!-- — · 5 min -->

`tail -n +2` prints from line 2 on; `cut -c1-10` keeps the first ten characters, the date; `uniq -c` counts equal lines next to each other.

1. Count the rows of each day.

    ```text
    $ tail -n +2 data/raw/weather.csv | cut -c1-10 | uniq -c
          4 2019-07-21
          2 2019-07-22
    ```

    macOS pads the counts with fewer spaces.

**Check:** 4 + 2 = 6 hours, the two of 22 July both marked.

---

### 21. A conda environment for the project { #environment }

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

### 22. Advanced tasks { #advanced }

<!-- — · 20 min -->

Harder questions to the same files, each solved with the commands of today.

!!! question "Task: the coldest and the warmest measured hour"
    `sort` puts lines in order. Find its options for a comma between the
    columns (`-t`), for sorting by the second column only (`-k2,2`), as
    numbers (`-n`) and backwards (`-r`), and print the coldest and the
    warmest hour of `weather_valid.csv`. `tail -n +2` leaves out the header.

??? success "Answer"
    ```text
    $ tail -n +2 data/processed/weather_valid.csv | sort -t, -k2,2 -n | head -n 1
    2019-07-21T23:00,23.6,74,3.4
    $ tail -n +2 data/processed/weather_valid.csv | sort -t, -k2,2 -n -r | head -n 1
    2019-07-21T20:00,27.3,63,4.5
    ```

    With the header, `sort -n` reads `temp_c` as 0 and puts it first. On
    `data/raw/weather.csv` the coldest line would be a mark of −999: the
    reason for `weather_valid.csv`.

!!! question "Task: a failure inside a pipe"
    In line 5 of `scripts/rebuild.sh`, change `daily_export.csv` to
    `daily_exprt.csv`. Run the script and ask for its status. Did `set -e`
    stop it? What is in `daily.csv`? Then add the line `set -o pipefail`
    under `set -e`, run it again, and put `daily_export.csv` back.

??? success "Answer"
    ```text
    $ ./scripts/rebuild.sh
    grep: data/raw/daily_exprt.csv: No such file or directory
    $ echo $?
    0
    $ wc -c data/processed/daily.csv
    0 data/processed/daily.csv
    ```

    The status of a pipe is the status of its last command, `cut`, which
    read nothing and ended well: the script ran to the end and left an
    empty `daily.csv`. With `set -o pipefail` a pipe fails when any of its
    commands fails:

    ```text
    $ ./scripts/rebuild.sh
    grep: data/raw/daily_exprt.csv: No such file or directory
    $ echo $?
    2
    ```

---

## Aims practised

- ⚙️ **Automation:** the cleaning and the mean are lines in
  `scripts/rebuild.sh`; one command makes every result again, and `set -e`
  stops it at the first failure.
- ♻️ **Reproducibility:** `grep -v`, `awk` and the script give the same
  checksum; the README states the result and the line that makes it.
- 🔧 **Tool-agnostic:** the same `grep` and `awk` lines in zsh and Git
  Bash; programs installed and removed by a package manager.
