# Seminar 4 · Command Line

**Paired lecture:** 04 Command Line & File Handling · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** Does Vilnius have fewer frost days a year than in 1961–1990?

Part 1 installs the tools; the lecturer runs Part 2 from this page and the
room types along; in Part 3 the room works in pairs. Everything is typed in
the terminal of VS Code: `zsh` on macOS, Git Bash on Windows. The lines are
the same in both; only the installs differ. A line that starts with `$` is
typed without the `$` (a Mac shows `%`), every other line is what comes
back, and `...` stands for lines left out.

**If time runs short:** leave out section 6 (sorting by a column); its calls are on the library card.

??? info "Before the session"
    - **Room:** internet for the installs, and laptops on which students can
      install programs (macOS asks for the laptop's password, Windows for an
      administrator's **Yes**). Nothing from another seminar is needed.
      Part 1 is longer than in later seminars: Git and Miniforge are
      installed in it.
    - **You:** [Install Python and Git](install_python_git.md) has every
      error message of the installs, for helpers.
    - **No file is handed out.** Section 4 fetches one public file, 0.8 MB
      packed and 6.4 MB unpacked: the daily record of the Vilnius weather
      station since 1881, one line per day and quantity, from NOAA NCEI's
      GHCN-Daily (`by_station/LH000026730.csv.gz`). Its columns are named in
      NCEI's [readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme-by_station.txt).
    - **Terms:** GHCN-Daily, NOAA NCEI, "for free and unrestricted use in
      research, education, and other non-commercial activities" (WMO
      Resolution 40); cite Menne et al. 2012, *Global Historical Climatology
      Network - Daily (GHCN-Daily)*, Version 3.35, NOAA NCDC,
      [doi:10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ), accessed
      10 November 2026.
    - **The numbers** come from runs on 10 November 2026. NCEI updates the
      file daily; the station's last day so far is 24 August 2025. If NCEI
      adds days, what is counted over the whole file changes (sections 4, 5
      and 7, the checksum, the years since 2010 in the solution); the
      numbers for 1961–1990 and 1991–2020 stay.
    - **Outputs** were printed by zsh with the GNU tools, which Git Bash
      has too. The tools of macOS pad the numbers of `wc` and `uniq -c` with
      other numbers of spaces. Paths are shown for a Mac
      (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.
    - **Keys** are written for Windows, macOS in brackets.

---

## Part 1 · Set up { #part-1 }

<!-- Part 1: 0:00 to 0:27, longer than the 15 min of later seminars: the installs of Git and Miniforge -->

### 1. Install Git and Miniforge { #installs }

<!-- 0:00 · 14 min -->

A package manager fetches a program, puts it in one known folder and on `PATH`, and later updates or removes it. Git keeps the versions of a project (Seminar 6); Miniforge is Python with conda. VS Code stays closed.

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

**Check:** Git and Miniforge installed, no red error at the end of a line.

!!! warning "No password, or no administrator's **Yes**"
    The laptop is managed by the university or an employer. The student
    pairs with a neighbour today.

---

### 2. The shell in VS Code, and where the programs are { #shell }

<!-- 0:14 · 7 min -->

The **terminal** is the window; the **shell** is the program in it that reads each line; it finds a program by searching the folders of `PATH`, in order.

1. Open VS Code, with no folder: the folder for today is made in section 3.
2. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). Type and choose
   `Terminal: Select Default Profile`, and take **zsh** (macOS) or
   **Git Bash** (Windows). Then, from the Command Palette again,
   `Terminal: Create New Terminal`.
3. Windows only: let conda set up Git Bash. Then close the terminal (the
   bin icon of the Panel) and open a new one: `Terminal: Create New
   Terminal` in the Command Palette.

    ```text
    $ ~/miniforge3/Scripts/conda.exe init bash
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

4. Ask the shell which shell it is, and the two programs for their
   versions. `python` is the name on both systems.

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

    ```text
    $ git --version
    git version 2.56.0
    $ python --version
    Python 3.14.10
    ```

    Your versions may differ.

5. Where the shell found them: the first folder of `PATH` that holds each.
   conda put its own folder, shown as `(base)`, in front.

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

**Check:** `(base)` at the start of the prompt, and a version from `git` and from `python`.

!!! warning "`python: command not found`, or no `(base)` in the prompt"
    conda is not set up in this shell: run `conda init zsh` (macOS) or
    `~/miniforge3/Scripts/conda.exe init bash` (Windows) again, then quit
    VS Code (**File** > **Exit**, macOS `Cmd+Q`) and start it again.

---

### 3. A folder for today { #folder }

<!-- 0:21 · 6 min -->

The shell always works in one folder, the working directory; a new terminal starts in your home folder, `~`.

1. Where am I.

    ```text
    $ pwd
    /Users/smilte
    ```

2. Make today's folder, go into it, and make the folders of a project in
   it: `data/raw` for files as they arrive, `results`, `scripts`. `-p`
   makes `data` on the way to `data/raw`.

    ```text
    $ mkdir weather-s04
    $ cd weather-s04
    $ mkdir -p data/raw results scripts
    $ ls
    data  results  scripts
    ```

3. **File** > **Open Folder...** > `weather-s04` (in your home folder) >
   **Open**, and answer **Yes, I trust the authors**. The window starts
   again; open a terminal: `Terminal: Create New Terminal` in the Command
   Palette.

**Check:** the prompt names `weather-s04`; the Explorer shows `data`, `results` and `scripts`.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs the lines of sections 4 to 7; the room types along. Section 4 fetches one file, and the later sections read it.

### 4. 145 years of Vilnius in one file: fetch it, look at both ends, count { #fetch }

<!-- 0:27 · 8 min -->

Before any calculation, look at the first and the last lines of a file, and count them.

1. Fetch the file into `data/raw`, and count its bytes. `curl` downloads an
   address; `-o` names the file it writes. Your speeds and times differ.

    ```text
    $ curl -o data/raw/vilnius.csv.gz https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/LH000026730.csv.gz
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  816k  100  816k    0     0   588k      0  0:00:01  0:00:01 --:--:--  588k
    $ wc -c data/raw/vilnius.csv.gz
    835602 data/raw/vilnius.csv.gz
    ```

2. Unpack it: `gunzip` replaces `vilnius.csv.gz` by `vilnius.csv`.

    ```text
    $ gunzip data/raw/vilnius.csv.gz
    $ ls data/raw
    vilnius.csv
    $ wc -c data/raw/vilnius.csv
    6370258 data/raw/vilnius.csv
    ```

3. The first and the last lines, and the number of lines.

    ```text
    $ head -n 3 data/raw/vilnius.csv
    LH000026730,18810101,PRCP,0,,,r,
    LH000026730,18810102,PRCP,0,,,r,
    LH000026730,18810103,PRCP,0,,,r,
    $ tail -n 3 data/raw/vilnius.csv
    LH000026730,20250822,TAVG,152,H,,S,
    LH000026730,20250823,TAVG,127,H,,S,
    LH000026730,20250824,TAVG,118,H,,S,
    $ wc -l data/raw/vilnius.csv
    185061 data/raw/vilnius.csv
    ```

    One line is one quantity on one day: the station, the date as
    YYYYMMDD, the quantity, its value, three flags, a time. The file has
    no header; NCEI's readme names the columns.

**Notice:** 835 602 bytes packed, 6 370 258 unpacked: lines that repeat this much pack to about an eighth of their size.

**Ask the room:** 1 January 1881 to 24 August 2025 is 52 831 days. With five quantities a day, how many lines would the file have, and why does it have 185 061?

??? note "Answer"
    5 × 52 831 = 264 155. Not every quantity was measured on every day:
    the lowest and the highest temperature start in 1890 and 1900, the snow
    depth in 1973, and some days are missing. Section 5 counts them.

---

### 5. What the file holds, and which days are missing: `cut`, `sort`, `uniq -c` { #count }

<!-- 0:35 · 8 min -->

Count every kind of line, then count the days of each year against the calendar: 365, or 366.

1. Field 3, the quantity, of every line; `sort` puts equal lines next to
   each other, and `uniq -c` prints each once, with its count.

    ```text
    $ cut -d, -f3 data/raw/vilnius.csv | sort | uniq -c
      44102 PRCP
       3901 SNWD
      50814 TAVG
      42719 TMAX
      43525 TMIN
    ```

    | Quantity | What it is | Unit |
    |--|--|--|
    | `PRCP` | rain and snow of the day | tenths of mm |
    | `SNWD` | depth of the snow on the ground | mm |
    | `TAVG` | mean temperature of the day | tenths of °C |
    | `TMAX`, `TMIN` | highest and lowest temperature of the day | tenths of °C |

2. The daily mean, `TAVG`: 12 is 1.2 °C.

    ```text
    $ grep ',TAVG,' data/raw/vilnius.csv | head -n 3
    LH000026730,18810101,TAVG,12,,,r,
    LH000026730,18810102,TAVG,-8,,,r,
    LH000026730,18810103,TAVG,16,,,r,
    ```

3. The days of each year: characters 13 to 16 of a line are its year.

    ```text
    $ grep ',TAVG,' data/raw/vilnius.csv | cut -c13-16 | uniq -c | head -n 3
        365 1881
        365 1882
         59 1883
    ```

4. The shortest years first: `sort -n` sorts the lines as numbers. Then
   the months of 1883: in the pattern, `.` stands for any one character.

    ```text
    $ grep ',TAVG,' data/raw/vilnius.csv | cut -c13-16 | uniq -c | sort -n | head -n 6
         59 1883
        212 1915
        212 1941
        213 1920
        236 2025
        294 1884
    $ grep ',1883....,TAVG,' data/raw/vilnius.csv | cut -c13-18 | uniq -c
         31 188301
         28 188302
    ```

**Notice:** 1883 has January and February only; 1915 and 1941 stop at the end of July (German troops took Vilnius in September 1915 and in June 1941); 1920 lacks July to November; 2025 stops on 24 August.

**Ask the room:** the 59 days of 1883 have a mean of −5.6 °C. Was 1883 the coldest year in Vilnius?

??? note "Answer"
    Nobody can tell from this file: it holds the two coldest months of
    1883 and nothing else. A mean of a year needs its 365 days. Count what
    a number rests on before comparing it.

---

### 6. The coldest nights on record: sort by a column, as numbers { #sort }

<!-- 0:43 · 7 min -->

`sort` orders by a column only when it is told the separator, the column, and that the column holds numbers.

1. The lowest temperatures, `TMIN`, sorted by field 4 as numbers, the
   first three lines.

    ```text
    $ grep ',TMIN,' data/raw/vilnius.csv | sort -k4,4n | head -n 3
    LH000026730,18900101,TMIN,-95,,,r,
    LH000026730,18900102,TMIN,-60,,,r,
    LH000026730,18900103,TMIN,-58,,,r,
    ```

    Not sorted by temperature: without `-t,` sort looks for fields between
    spaces, finds no field 4, and orders the whole lines instead, by date.

2. With the separator, `-t,`.

    ```text
    $ grep ',TMIN,' data/raw/vilnius.csv | sort -t, -k4,4n | head -n 3
    LH000026730,19400110,TMIN,-372,,,r,
    LH000026730,19400117,TMIN,-372,,,r,
    LH000026730,19400116,TMIN,-362,,,r,
    ```

3. Every night at −30 °C or colder, counted by year. `awk -F,` splits a
   line at the commas; it prints the lines for which the test is true:
   `$3` is field 3, `&&` is "and".

    ```text
    $ awk -F, '$3 == "TMIN" && $4 <= -300' data/raw/vilnius.csv | cut -c13-16 | uniq -c
          1 1893
          5 1929
         10 1940
          1 1941
          1 1942
          2 1950
          3 1954
          3 1956
          1 1978
          1 1987
    ```

**Notice:** −372 is −37.2 °C, on 10 and 17 January 1940; 28 nights reached −30 °C or colder, the last in 1987.

**Ask the room:** the first command answered "−9.5 °C, 1 January 1890". What in its output shows that it is not the coldest night?

??? note "Answer"
    The lines under it: −6.0 and −5.8 °C are warmer, so the output is not
    in order. One line of output proves nothing; read three. And a coldest
    night of −9.5 °C in 145 years, where the days of January average
    −5 °C, is not plausible.

---

### 7. One script makes the table again: a loop, `set -e`, a checksum { #script }

<!-- 0:50 · 9 min -->

A script holds every line from the address to the result; two runs that give the same checksum gave the same bytes.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `months.sh`, `Enter`. Windows: the Status Bar says `CRLF`; click it and
   choose `LF`. Type the lines and save (`Ctrl+S`, macOS `Cmd+S`).

    ```bash title="scripts/months.sh"
    #!/usr/bin/env bash
    # The mean temperature of each month in Vilnius, 1881 to 2025:
    # GHCN-Daily, NOAA NCEI; TAVG is the daily mean in tenths of °C.
    set -e
    STATION=LH000026730
    URL=https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/$STATION.csv.gz
    mkdir -p data/raw results
    curl -fsS -o data/raw/vilnius.csv.gz "$URL"
    gunzip -f data/raw/vilnius.csv.gz
    for month in 01 02 03 04 05 06 07 08 09 10 11 12; do
      grep ",....$month..,TAVG," data/raw/vilnius.csv |
        awk -F, -v m="$month" '{ s += $4; n++ }
          END { printf "%s %5d days %6.2f °C\n", m, n, s / n / 10 }'
    done > results/months.txt
    cat results/months.txt
    ```

    `set -e` stops the script at the first line that fails. The loop runs
    the `grep` and `awk` lines once for each month: the shell puts `01`,
    `02`, … in place of `$month`. `> results/months.txt` writes what the
    whole loop prints into one file.

2. Run it with `bash`.

    ```text
    $ bash scripts/months.sh
    01  4339 days  -5.15 °C
    02  3977 days  -4.44 °C
    03  4355 days  -0.53 °C
    04  4197 days   6.30 °C
    05  4368 days  12.84 °C
    06  4230 days  16.27 °C
    07  4339 days  18.11 °C
    08  4270 days  16.87 °C
    09  4110 days  12.23 °C
    10  4247 days   6.67 °C
    11  4106 days   1.29 °C
    12  4276 days  -2.87 °C
    ```

3. The checksum of the table, a second run, the checksum again: the same
   64 digits, on every laptop that ran the same lines on the same file.

    === "macOS"

        ```text
        $ shasum -a 256 results/months.txt
        46454a41447fb1071cb737f86830a37c0da3b250e9d0df334d9154c8cd156a04  results/months.txt
        $ bash scripts/months.sh > /dev/null
        $ shasum -a 256 results/months.txt
        46454a41447fb1071cb737f86830a37c0da3b250e9d0df334d9154c8cd156a04  results/months.txt
        ```

    === "Windows"

        ```text
        $ sha256sum results/months.txt
        46454a41447fb1071cb737f86830a37c0da3b250e9d0df334d9154c8cd156a04  results/months.txt
        $ bash scripts/months.sh > /dev/null
        $ sha256sum results/months.txt
        46454a41447fb1071cb737f86830a37c0da3b250e9d0df334d9154c8cd156a04  results/months.txt
        ```

    `> /dev/null` throws the printed table away: only the file counts here.

**Notice:** each line prints the days its mean rests on: January 4 339 of the 4 495 in the calendar of 1881–2025 (145 × 31); the gaps of section 5 are missing from every month.

**Ask the room:** delete the line `set -e`, change one letter of the address, and run the script. What does it print?

??? note "Answer"
    The same table. `curl` fails (`curl: (22) The requested URL returned
    error: 404`), `gunzip` finds no file, and the loop reads the
    `vilnius.csv` of the run before: a result that looks right and comes
    from an old file. With `set -e` the script stops at `curl`, and
    `echo $?` prints `22`. Put both lines back.

---

### 8. Library card: the commands of this page { #card }

<!-- 0:59 · 2 min -->

Every command of the showcase and of the solution below, one line each.

| Command | What it does |
|--|--|
| `curl -o FILE URL` | downloads an address into FILE; in a script `-fsS`: fail on an error page, print only errors |
| `gunzip FILE.gz` | unpacks FILE.gz into FILE; `-f` overwrites FILE |
| `head -n 3 FILE`, `tail -n 3 FILE` | the first, the last three lines |
| `wc -l FILE`, `wc -c FILE` | the number of lines, of bytes |
| `cut -d, -f3`, `cut -c13-16` | field 3 between commas; characters 13 to 16 |
| `sort`, `sort -n` | lines in order, as text, as numbers |
| `sort -t, -k4,4n` | lines in order of field 4 between commas, as numbers |
| `uniq -c` | each run of equal lines once, with its count |
| `grep ',TAVG,' FILE`, `grep -c` | the lines that hold a text; their count |
| `grep ',1883....,TAVG,'` | a pattern: `.` is any one character |
| `awk -F, '$3 == "TMIN" && $4 < 0'` | the lines whose field 3 is `TMIN` and field 4 below 0 |
| `awk -F, '{ s += $4; n++ } END { print n, s / n }'` | the count and the mean of field 4 |
| `awk 'BEGIN { print 4071 / 30 }'` | arithmetic with decimals |
| `A \| B` | the output of A is the input of B |
| `for m in 01 02; do ... $m ...; done` | the lines between `do` and `done`, once for each value |
| `> FILE` | the output into FILE, emptied first |
| `bash FILE.sh`, `set -e` | run a script; stop it at the first failing line |
| `shasum -a 256 FILE` · `sha256sum FILE` | the checksum of a file (macOS · Git Bash) |

---

## Part 3 · The problem { #part-3 }

### 9. Does Vilnius have fewer frost days than in 1961–1990? { #problem }

<!-- 1:01 · 45 min -->

A frost day is a day whose lowest temperature, `TMIN`, is below 0 °C.
Weather services describe a climate by thirty years; 1961–1990 and
1991–2020 are the two periods they use. The data: `data/raw/vilnius.csv`
of section 4 (GHCN-Daily, NOAA NCEI; terms under "Before the session").

Work in pairs, with any tools, an LLM too: the work is the idea and the checks, not the typing. The answer comes from the shell alone: no spreadsheet, no Python.

1. **Predict**, before any command. How many frost days a year did
   Vilnius have in 1961–1990, and how many in 1991–2020? One reason.
   Write it down.
2. **Solve.** The frost days a year in each period.
3. **Check the machine's work.**
    - By hand: the five `TMIN` lines of 1 to 5 January 1961,
      `grep ',TMIN,' data/raw/vilnius.csv | grep ',1961010' | head -n 5`.
      How many are frost days? Run your test on the same five lines.
    - The sample size: how many `TMIN` lines does each period have?
      Thirty years have 10 957 days (1961–1990) and 10 958 (1991–2020).
    - The unit: tenths of °C. Is `< 0` right for "below 0 °C"? Which test
      would "below −10 °C" need?
    - Set the answer against your prediction; where they differ, say
      which was wrong, and why.
4. **Hand in.** The frost days a year in each period, the number of days
   each count rests on, and two sentences in your own words, ready to
   show.

??? tip "Hint 1: one period in awk"
    `awk` compares the date as a number: `$2 >= 19610101 && $2 <= 19901231`
    keeps 1961–1990. Add `$3 == "TMIN"` and `$4 < 0`, and count the lines
    with `wc -l`.

??? tip "Hint 2: what each count rests on"
    Count the `TMIN` lines of each year, as section 5 counted `TAVG`:
    `grep ',TMIN,' data/raw/vilnius.csv | cut -c13-16 | uniq -c`. Read the
    last twenty years.

??? tip "Hint 3: a fair comparison"
    Compare only years that have all their days, or turn each count into a
    share: frost days ÷ days with a `TMIN`, times 365.25 days a year.

??? note "One solution"
    By hand, 1 to 5 January 1961: −2.8, −1.7, −2.0, −1.4 and 0.0 °C. Four
    frost days: 0.0 is not below 0.

    ```text
    $ grep ',TMIN,' data/raw/vilnius.csv | grep ',1961010' | head -n 5 | awk -F, '$4 < 0' | wc -l
    4
    ```

    The two periods: the `TMIN` lines, then the frost days among them.

    ```text
    $ awk -F, '$3 == "TMIN" && $2 >= 19610101 && $2 <= 19901231' data/raw/vilnius.csv | wc -l
    10957
    $ awk -F, '$3 == "TMIN" && $4 < 0 && $2 >= 19610101 && $2 <= 19901231' data/raw/vilnius.csv | wc -l
    4071
    $ awk -F, '$3 == "TMIN" && $2 >= 19910101 && $2 <= 20201231' data/raw/vilnius.csv | wc -l
    8280
    $ awk -F, '$3 == "TMIN" && $4 < 0 && $2 >= 19910101 && $2 <= 20201231' data/raw/vilnius.csv | wc -l
    2805
    ```

    1991–2020 has a `TMIN` for 8 280 of its 10 958 days. Which years are
    short:

    ```text
    $ grep ',TMIN,' data/raw/vilnius.csv | cut -c13-16 | uniq -c | tail -n 17
        365 2009
        114 2010
         98 2011
        131 2012
        135 2013
        132 2014
        128 2015
        123 2016
        139 2017
        125 2018
        122 2019
         93 2020
        127 2021
        105 2022
         43 2023
        129 2024
        110 2025
    ```

    Since 2010 the file has a `TMIN` for about one day in three. The years
    with all their days, 1991–2009:

    ```text
    $ awk -F, '$3 == "TMIN" && $2 >= 19910101 && $2 <= 20091231' data/raw/vilnius.csv | wc -l
    6940
    $ awk -F, '$3 == "TMIN" && $4 < 0 && $2 >= 19910101 && $2 <= 20091231' data/raw/vilnius.csv | wc -l
    2385
    $ awk 'BEGIN { print 4071 / 30, 2805 / 30, 2385 / 19, 2805 / 8280 * 365.25 }'
    135.7 93.5 125.526 123.735
    ```

    | Period | `TMIN` lines | Frost days | Frost days a year |
    |--|--|--|--|
    | 1961–1990 | 10 957 of 10 957 | 4 071 | 135.7 |
    | 1991–2020, lines counted | 8 280 of 10 958 | 2 805 | 93.5 |
    | 1991–2009, all days | 6 940 of 6 940 | 2 385 | 125.5 |
    | 1991–2020, share × 365.25 | 8 280 of 10 958 | 2 805 | 123.7 |

    Vilnius had 135.7 frost days a year in 1961–1990, and about 124 to 126
    in 1991–2020: some 10 to 12 fewer. Counting the lines gives 93.5,
    because since 2010 two days in three have no `TMIN` in the file and
    count as days without frost.

**With your own project data:** a count of events in your own files (days
above a limit, failed runs, records of one kind) in two periods: first the
number of records in each period, then the events, then the events per
record.

---

## Part 4 · Show and discuss { #part-4 }

### 10. Three questions about the pairs' counts { #discuss }

<!-- 1:46 · 14 min -->

Two or three pairs show their numbers and read their two sentences.

**Ask the room:** one pair found 42 fewer frost days a year, another 10. Which is right, and what did the first pair count?

??? note "Answer"
    The second. 93.5 divides the frost days of 1991–2020 by thirty years,
    but the file has a `TMIN` for 8 280 of their 10 958 days; the 2 678
    missing days count as days without frost. The first pair counted the
    lines of the file, not the frost.

**Ask the room:** why compare thirty years with thirty years, and not 1961 with 2020?

??? note "Answer"
    Frost days change more from one year to the next than between the
    periods: from 77 in 1990 to 159 in 1965 and 1980, within 1961–2009.
    One pair of single years can show a rise or a fall; thirty years
    average most of that out.

**Ask the room:** the share, frost days ÷ days with a `TMIN`, assumes something about the missing days. What, and how would you check it?

??? note "Answer"
    That the missing days are like the measured ones, spread over the
    year. Counted by month, the `TMIN` lines of 2010 to 2025 are spread
    evenly, from 122 (February) to 185 (April). Had the missing days all
    been in winter, the share would come out too low.

A count compares two periods only when both rest on the same days: count the records first, then the events.

---

## Optional, if the room is fast { #optional }

### 11. Days with a mean below 0 °C: does a second column agree? { #tavg }

<!-- — · 10 min -->

`TAVG`, the mean of the day, has nearly every day of both periods. Predict,
solve, check the machine's work, hand in, as in section 9: the days a year
with a mean below 0 °C in 1961–1990 and in 1991–2020.

??? note "One solution"
    ```text
    $ awk -F, '$3 == "TAVG" && $2 >= 19610101 && $2 <= 19901231' data/raw/vilnius.csv | wc -l
    10955
    $ awk -F, '$3 == "TAVG" && $4 < 0 && $2 >= 19610101 && $2 <= 19901231' data/raw/vilnius.csv | wc -l
    2934
    $ awk -F, '$3 == "TAVG" && $2 >= 19910101 && $2 <= 20201231' data/raw/vilnius.csv | wc -l
    10956
    $ awk -F, '$3 == "TAVG" && $4 < 0 && $2 >= 19910101 && $2 <= 20201231' data/raw/vilnius.csv | wc -l
    2527
    $ awk 'BEGIN { print 2934 / 30, 2527 / 30 }'
    97.8 84.2333
    ```

    Two days are missing in each period. 97.8 days a year with a mean
    below 0 °C in 1961–1990, 84.2 in 1991–2020: 14 fewer, the same
    direction as the frost days, and nothing like 42.

---

## Aims practised

- ⚙️ **Automation:** `scripts/months.sh` fetches the file and makes the
  table with one command; `set -e` stops it at the first failing line.
- ♻️ **Reproducibility:** a second run gives the same checksum; every
  number on this page comes from a typed line that anyone can run again on
  the public file.
- 🔧 **Tool-agnostic:** the same lines in zsh and Git Bash; programs
  installed by a package manager; a file of 185 061 lines read without
  opening it.
