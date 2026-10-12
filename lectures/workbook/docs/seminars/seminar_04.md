# Seminar 4 — Work on Files from the Shell

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student builds a project from an empty folder, with
VS Code, the terminal, a README and a small file measured byte by byte, then
finds the broken week in two years of bicycle counts and gets the same
checksum as everyone else in the room.

The first part revisits Seminars 1 and 3 from scratch, so nobody depends on
what they did then. The rest follows Lecture 04: the terminal of VS Code,
`zsh` on macOS and **PowerShell 7** on Windows, and two downloaded files.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Warm-up: from an empty folder** · 49 min | | |
| 0:00 | [1. Start the installs](#installs) | `winget install …`, `git --version`, the Miniforge download | Installs and downloads running in the background |
| 0:05 | [2. The five regions of VS Code](#vscode) | The five regions, `Ctrl+Shift+P` | The regions named, a terminal open |
| 0:11 | [3. Read the prompt; `pwd`, `ls`, `cd`](#terminal) | `pwd`, `ls`, `cd`, `Tab`, `↑`, `clear` | The prompt read aloud, part by part |
| 0:18 | [4. Make the project folder with `mkdir`](#folder) | `mkdir` six times, **Open Folder** | `bike-project` with its four folders |
| 0:24 | [5. A README in Markdown](#readme-md) | `README.md` and its preview | A title, a list, a table, a link |
| 0:31 | [6. Check the shell; PowerShell 7 in VS Code](#shell) | **Select Default Profile** | `7` or `/bin/zsh` |
| 0:34 | [7. Count the bytes of a small file; a script with CRLF](#bytes) | `counts.csv`, `wc -c`, `hexdump -C`, `Format-Hex`; `hello.sh` with CRLF | 39 bytes (42 with CRLF); a script that does not run on a Mac |
| | **Part 2 · Read, count and copy a large file** · 17 min | | |
| 0:49 | [8. Move the downloaded files into the project](#files) | `mv ~/Downloads/…` | `bikes.csv` and `column_stats.py` in place |
| 0:52 | [9. Read `bikes.csv`, count its lines and bytes](#count) | `head`, `wc -l`, `Get-Content`, `Get-Item` | 35 089 lines, 900 314 bytes |
| 1:00 | [10. Copy, rename, delete](#copy) | `cp`, `mv`, `rm`, `*` | A backup made and removed again |
| | **Part 3 · Pipes and filters** · 17 min | | |
| 1:06 | [11. A pipe: sort the counts, read both ends](#sort) | `sort -n`, `Sort-Object` | `9999` at the top: the mark for a missing count |
| 1:14 | [12. Count the 9999 rows, keep the others in a new file](#grep) | `grep`, `uniq -c`, `Select-String`, `>` | 168 rows, one broken week, `bikes_valid.csv` |
| | **Part 4 · Python, a checksum, the README** · 29 min | | |
| 1:23 | [13. Install Miniforge, run `column_stats.py`](#python) | The Miniforge installer, `conda init`, `column_stats.py` | `(base)` in the prompt, Python 3.14.7, the mean of `counts.csv`: 400 |
| 1:33 | [14. The mean with and without the 9999 rows](#mean) | `column_stats.py` twice | 86.3 and 38.6 bicycles per hour |
| 1:37 | [15. Compare checksums across the room](#checksum) | `shasum -a 256`, `Get-FileHash` | `2c68aad2…` on every laptop |
| 1:42 | [16. Data, columns and the rebuild line in the README](#readme) | `README.md` and its preview | Data, columns, the mark, one rebuild line |
| 1:48 | [17. Wrap up](#wrap-up) | `git config`, the list of the day | Git knows each name |
| | **Optional, if the room is fast** | | |
| — | [18. A program that cleans an export](#clean) | `clean_export.py` | `monthly.csv`, `ea4ce2ce…` on every laptop |
| — | [19. Regular expressions in VS Code and the shell](#regex) | The `.*` button, `grep -E`, `Select-String` | 168, 4022, 37 |
| — | [20. A conda environment for the project](#environment) | `conda create`, `conda activate`, `conda install numpy` | `(bikes)` in the prompt, `environment.yml` |
| — | [21. A list of checksums](#list) | `shasum -a 256 -c`, `Compare-Object` | `OK`, then one digit caught |
| — | [22. Test the README](#readme-test) | Delete, paste, count | `bikes_valid.csv` back, 34 921 lines |
| — | [23. Aliases, the prompt and the start-up file](#settings) | `alias`, `~/.zshrc`, `$PROFILE`, Oh My Zsh, Oh My Posh | A short prompt and `..` in every new terminal |

**If time runs short:** in the warm-up keep sections 3, 4 and 7 and do 2
and 5 in two minutes each; in section 7 show the script (steps 8 to 10) on
the projector only; in section 12 leave out the last step (text against
number). Never cut sections 13 to 15, whose numbers are the result
of the day.

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

    Every command stands alone in a block. It is typed as it stands and
    ended with `Enter`. The output follows in its own block. Where the two
    shells differ, the step has a tab for **macOS** (`zsh`) and one for
    **Windows** (PowerShell). Where they agree, the line stands once. The
    user on the page is called `smilte`; the home folder is `/Users/smilte` on a
    Mac and `C:\Users\smilte` on Windows. Keys are written for Windows, with
    macOS in brackets.

??? info "Before the session (5 minutes)"
    For the room: a laptop on which the student can install programs, with
    VS Code. A laptop without VS Code gets it from `code.visualstudio.com`
    in section 1, while the other installs run.

    For you:

    - Put the files of the next box on a USB stick, with the installers
      listed on [Install Python, Git and PowerShell 7](install_python_git.md)
      if the network of the room is slow.
    - Read section 7 once: the derivation of 39 and 42 bytes is the one
      piece of arithmetic of the warm-up.
    - Skim sections 11 and 12: they hold the one surprise of the day, the
      value `9999`. Let the room find it; do not announce it.

??? info "Files for this seminar"
    A browser saves each file in **Downloads** under the name in the second
    column; the page moves it into the project folder with a typed command.

    | File | Saved as | Moved into | What it is |
    |--|--|--|--|
    | [`bikes_hourly.csv`](../data/bikes_hourly.csv){ download="bikes.csv" } | `bikes.csv` | `data/raw` | Section 8. Two counters, one row per counter and hour, 2024 and 2025: 35 088 rows, 900 314 bytes |
    | [`cli_column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" } | `column_stats.py` | `scripts` | Section 8. A program that prints rows, smallest, largest and mean of one column |
    | [`bikes_monthly_export.csv`](../data/bikes_monthly_export.csv){ download="monthly_export.csv" } | `monthly_export.csv` | `data/raw` | Optional section 18. Bicycles per day on the bridge, each month of 2025, as a spreadsheet exported it |
    | [`cli_clean_export.py`](../data/cli_clean_export.py){ download="clean_export.py" } | `clean_export.py` | `scripts` | Optional section 18. A program that cleans such an export |
    | [`bikes_project.zip`](../data/bikes_project.zip) | `bikes_project.zip` | unpack it | The folder `bike-project` at the end of section 17, for a student who lost a step |
    | [`bikes_README.txt`](../data/bikes_README.txt){ download="README.md" } | `README.md` | compare only | The README of sections 5 and 16 |

    The bicycle files were made by [`bikes_files.py`](../data/bikes_files.py).
    `counts.csv` is not downloaded: every student types it in section 7.

---

## Part 1 · Warm-up: from an empty folder { #part-1 }

**0:00 to 0:49 · sections 1 to 7**

The slow installs start first and run while the room rebuilds, from
nothing, what Seminars 1 and 3 did: VS Code and its regions, the terminal,
a project folder, a README in Markdown, and one small file measured byte by
byte. [Install Python, Git and PowerShell 7](install_python_git.md) has the
installs per system, with every error message, for helpers at a laptop.

---

### 1. Start the installs { #installs }

**0:00 · 5 min**

**Tell the room.** Three programs come today: PowerShell 7 on Windows, a
shell that is the same on every Windows laptop; Miniforge, which brings
Python and conda, a program that installs packages and keeps each
project's packages apart; and Git, which is used next week. When the whole
room downloads at once the network is slow, so everything starts now and
runs in the background. Type the lines exactly; every word is explained in the next
twenty minutes.

1. Open a terminal of the system.

    === "macOS"

        Press `Cmd+Space`, type `Terminal`, press `Enter`. A window with a
        prompt opens. Ask for Git:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. It takes 5 to 15 minutes. If the
        line prints `git version 2.…` instead, Git is already there.

    === "Windows"

        Press the Windows key, type `powershell`, press `Enter`. A window
        with a prompt opens: Windows PowerShell 5.1, the one built into
        Windows. `winget`, a program that installs other programs, comes
        with it. Install PowerShell 7:

        ```text
        winget install --id Microsoft.PowerShell --source winget
        ```

        ```text
        Found PowerShell [Microsoft.PowerShell] Version 7.6.6
        ...
        Successfully installed
        ```

        Then Git, by the same kind of line:

        ```text
        winget install --id Git.Git --source winget
        ```

        Each ends with `Successfully installed`. Leave the window open.

2. Download the Miniforge installer. Do not run it yet: section 13 needs
   it.

    === "macOS"

        In the same Terminal window, go into **Downloads** and fetch the
        installer:

        ```text
        cd ~/Downloads
        ```

        ```text
        curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
        ```

        `$(uname)` and `$(uname -m)` fill in the system and the chip of
        this Mac, so one line fits every Mac. A table counts the download
        up to `100`.

    === "Windows"

        Select this link; the browser saves the installer in
        **Downloads**:
        [Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe).
        Not `winget`: the Miniforge it offers is from 2022.

!!! success "You should now see"
    On macOS the developer tools installing, and `curl` at `100`. On
    Windows `winget` at work, and the Miniforge installer in **Downloads**.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
    | macOS: `curl: (6) Could not resolve host: github.com` | No network. Copy the Miniforge installer from the USB stick into **Downloads** |
    | Windows: the browser asks whether to keep the installer | Select **Keep**. It comes from the release page of conda-forge on GitHub |
    | Windows: `winget` is not recognized | Install `PowerShell-7.6.6-win-x64.msi` and Git for Windows from the USB stick, with every default |
    | An installer asks for an administrator password the student does not have | The laptop is managed by the university or an employer. The student pairs with a neighbour today |
    | No VS Code on the laptop | Download it from `code.visualstudio.com` and install it with every default, now |

---

### 2. The five regions of VS Code { #vscode }

**0:05 · 6 min**

**Tell the room.** VS Code is the editor of the course: files, Markdown and
the terminal in one window. The window has five regions, and every step of
today names the region it happens in.

1. Open VS Code. If it opens a folder from before, select **File** >
   **Close Folder**: today starts from nothing.

2. Name the regions, pointing at each one on the projector.

    | | Region | What it is for |
    |--|--|--|
    | 1 | **Activity Bar** | The column of icons on the far left |
    | 2 | **Side Bar** | The files of the project: the **Explorer** |
    | 3 | **Editor** | The open files, one tab each |
    | 4 | **Panel** | At the bottom, hidden at first: the terminal |
    | 5 | **Status Bar** | The line at the bottom: facts about the open file |

3. Press `Ctrl+B` (macOS `Cmd+B`) twice. The Side Bar hides and comes back.

4. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`): the **Command Palette**,
   where every command of VS Code can be found by name. Type:

    ```text
    create new terminal
    ```

    Select **Terminal: Create New Terminal**. The Panel opens at the
    bottom, with a prompt.

!!! success "You should now see"
    The five regions named, and the Panel open with a prompt in it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | VS Code runs in the browser (`vscode.dev`) | It has no terminal. The student pairs with a neighbour today |
    | The Command Palette shows `>` and nothing else | Correct: the `>` means "commands". Type after it |

---

### 3. Read the prompt; `pwd`, `ls`, `cd` { #terminal }

**0:11 · 7 min**

**Tell the room.** The **terminal** is the window that shows
text: here, the Panel. The **shell** is the program inside it that reads
each line you type, runs it, prints the answer and waits: `zsh` on a Mac,
PowerShell on Windows. The **prompt** is the line where it waits. The shell
is always in one folder, the **working directory**: the prompt shows it,
`pwd` prints it in full, `ls` lists what is in it, `cd` changes it.

1. Read the prompt aloud, part by part.

    === "macOS"

        ```text
        smilte@MacBook-Air ~ %
        ```

        The user, the computer, the folder the shell is in (`~` is the home
        folder), and `%`: the shell waits.

    === "Windows"

        ```text
        PS C:\Users\smilte>
        ```

        `PS`, the folder the shell is in, and `>`: the shell waits. Until
        section 6 this is the built-in PowerShell 5.1; every line of the
        warm-up works in both.

2. A first command. The shell runs it, prints, and shows the prompt again.

    ```text
    echo hello
    ```

    ```text
    hello
    ```

3. Where am I?

    ```text
    pwd
    ```

    === "macOS"

        ```text
        /Users/smilte
        ```

    === "Windows"

        ```text
        Path
        ----
        C:\Users\smilte
        ```

    An **absolute** path: from the top of the disk, `/` or `C:\`, down to
    the home folder.

4. What is here?

    ```text
    ls
    ```

    The folders of the home folder: `Desktop`, `Documents`, `Downloads` and
    more. PowerShell prints a table; the names are in the column **Name**.

5. Go into **Downloads** with a **relative** path, one that starts at the
   working directory. Type `cd Dow`, then press `Tab`: the shell completes
   the name.

    ```text
    cd Downloads
    ```

    ```text
    pwd
    ```

    The prompt now shows `Downloads`, and `pwd` ends in `Downloads`.

6. Up one level, and check. `..` is the folder above; `cd ~` goes to the
   home folder from anywhere.

    ```text
    cd ..
    ```

    ```text
    pwd
    ```

7. Press `↑` twice: earlier commands come back, ready to run again. Press
   `Esc` (macOS `Ctrl+C`) to leave the line empty. Then empty the Panel:

    ```text
    clear
    ```

!!! success "You should now see"
    The home folder printed by `pwd`, and an empty Panel with the prompt at
    the top.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `cd: no such file or directory: downloads` | Names are spelled exactly, also the capital `D`. `Tab` spells them right |
    | `Tab` adds nothing | No name starts with what was typed. Check the letters before the `Tab` |
    | Windows: `Tab` writes `.\Downloads\` | PowerShell's spelling of the same path. It works |
    | Windows: the home folder has no **Documents**, only **OneDrive** | Fine: today's folder goes into the home folder itself |

---

### 4. Make the project folder with `mkdir` { #folder }

**0:18 · 6 min**

**Tell the room.** Every project of the course has the same layout: raw
data that is never changed, processed data that commands make from it,
scripts, and results. Names have small letters and no spaces, because a
space ends a word in a command. `mkdir` makes a folder; six short lines,
the same in both shells. `↑` brings back the last line, so only its end is
retyped.

1. In the home folder, make the project folder and go into it.

    ```text
    cd ~
    ```

    ```text
    mkdir bike-project
    ```

    ```text
    cd bike-project
    ```

2. Make its folders. After the second line, press `↑` and change only the
   last word.

    ```text
    mkdir data
    ```

    ```text
    mkdir data/raw
    ```

    ```text
    mkdir data/processed
    ```

    ```text
    mkdir scripts
    ```

    ```text
    mkdir results
    ```

    zsh prints nothing. PowerShell answers each line with a short table
    that names the new folder.

3. Look.

    ```text
    ls
    ```

    ```text
    data    results scripts
    ```

    ```text
    ls data
    ```

    ```text
    processed raw
    ```

    PowerShell prints the same names in its table.

4. Open the folder in VS Code: **File** > **Open Folder...**, select
   `bike-project` in the home folder, **Open**. The window reloads. Then
   **Terminal** > **New Terminal**.

!!! success "You should now see"
    The four folders in the Explorer, and a prompt that ends in
    `bike-project`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `mkdir: data/raw: No such file or directory` | `data` has to exist first. `mkdir data`, then the line again |
    | `mkdir: bike-project: File exists`, or PowerShell: `An item with the specified name … already exists` | The folder is there from an earlier try. `cd bike-project` and go on |
    | A folder named `Data` or `bike project` | Delete it in the Side Bar and make it again: small letters, no spaces |
    | VS Code asks *Do you trust the authors of the files in this folder?* | **Yes, I trust the authors**: you made the folder yourself |

---

### 5. A README in Markdown { #readme-md }

**0:24 · 7 min**

**Tell the room.** The README is the first file anyone opens in a project.
It is written in Markdown: plain text with a few signs, `#` for a heading,
`-` for a list item, `|` for a table, `[text](address)` for a link. The
preview shows how it looks.

1. In the Explorer, point at the line `BIKE-PROJECT` and select the
   **New File** icon. Name the file:

    ```text
    README.md
    ```

2. Type, or copy, this text into it:

    ```text
    # Bike Counters

    Practice project of Seminar 4: bicycle counts, read and checked with typed
    commands.

    ## Folders

    - `data/raw`: files as they arrived, never edited
    - `data/processed`: files that commands make from `data/raw`
    - `scripts`: programs
    - `results`: numbers and figures

    ## Two places

    | Place | Bicycles |
    |--|--|
    | Antakalnis | 412 |
    | Užupis | 388 |

    Course pages: [the workbook](https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis/workbook/)
    ```

3. Open the preview beside it: `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

4. Save with `Ctrl+S` (macOS `Cmd+S`). The dot on the tab goes away: a dot
   means *not saved*.

!!! success "You should now see"
    In the preview: a large title, a heading **Folders** over a list of
    four items, a table of two rows, and a link that opens the workbook.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The list shows as one line | An empty line is missing before the first `-` |
    | The table shows as plain text | The line of dashes under the header is missing, or the empty line before the table |
    | The `#` shows in the preview | A space is missing after `#` |
    | The file is named `README.md.txt` or `readme.md` | Rename it in the Explorer with `F2` (macOS `Enter`) |

---

### 6. Check the shell; PowerShell 7 in VS Code { #shell }

**0:31 · 3 min**

**Tell the room.** Windows has two PowerShells: 5.1, built in, and 7, the
one installed at the start, which also runs on macOS and Linux. VS Code is
told once to open 7. On a Mac the shell is `zsh`, built in; this step only
checks it.

1. Check the shell.

    === "macOS"

        ```text
        echo $SHELL
        ```

        ```text
        /bin/zsh
        ```

    === "Windows"

        In the PowerShell window of section 1, check that both installs
        printed `Successfully installed`, then close that window. In VS
        Code press `Ctrl+Shift+P` and type:

        ```text
        default profile
        ```

        Select **Terminal: Select Default Profile**, then **PowerShell**.
        Not **Windows PowerShell**: that is 5.1.

2. Close the terminal with the bin icon at the top right of the Panel, then
   **Terminal** > **New Terminal**.

    === "macOS"

        The name at the top right of the Panel reads `zsh`.

    === "Windows"

        ```text
        $PSVersionTable.PSVersion.Major
        ```

        ```text
        7
        ```

        The name at the top right of the Panel reads `pwsh`.

!!! success "You should now see"
    `/bin/zsh` or `7`, and a prompt that ends in `bike-project`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `/bin/bash`, or Terminal says *The default interactive shell is now zsh* | Type `chsh -s /bin/zsh`, then the laptop's password (nothing shows while typing) and `Enter`. Quit VS Code with `Cmd+Q` and start it again |
    | Windows: the version line prints `5` | **Windows PowerShell** was chosen, or the old terminal is still open. Step 1 again, then a new terminal |
    | Windows: **PowerShell** is missing from the list | PowerShell 7 is not installed yet, or VS Code started before it was. Quit VS Code with **File** > **Exit**, start it again, step 1 again. If it is still installing, go on in 5.1 and switch later |
    | The list offers **Git Bash** | Not in this course. Take **PowerShell** |

---

### 7. Count the bytes of a small file; a script with CRLF { #bytes }

**0:34 · 15 min**

**Tell the room.** A file is a row of bytes. A letter `a` to `z` is one
byte in UTF-8; a Lithuanian letter such as `ž` is two. The end of a line is
a byte too: `0A`, called LF, on a Mac; two bytes, `0D 0A`, called CRLF, in
what VS Code writes on Windows. We type a file of three lines, predict its
size, and let the shell measure it. Then a file of two lines shows what the
line ending does when a file goes from Windows to a Mac.

1. In the Explorer select the folder `raw` inside `data`, then the **New
   File** icon. Name the file:

    ```text
    counts.csv
    ```

2. Type, or copy, these three lines. Press `Enter` after the last line
   too, so that every line ends with a line break. Save.

    ```text
    place,bikes
    Antakalnis,412
    Užupis,388
    ```

3. Read the right end of the Status Bar: `UTF-8`, and `LF` on a Mac or
   `CRLF` on Windows.

4. Predict the size with the room. Count the characters:

    | Line | Characters |
    |--|--|
    | `place,bikes` | 11 |
    | `Antakalnis,412` | 14 |
    | `Užupis,388` | 10 |
    | together | 35 |

    `ž` takes two bytes, every other character one: 36 bytes. Three line
    ends: 3 × 1 = 3 bytes with LF, 3 × 2 = 6 with CRLF. So 39 bytes on a
    Mac, 42 on Windows.

5. Measure.

    === "macOS"

        ```text
        wc -c data/raw/counts.csv
        ```

        ```text
              39 data/raw/counts.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/raw/counts.csv).Length
        ```

        ```text
        42
        ```

6. Look at the bytes themselves.

    === "macOS"

        ```text
        hexdump -C data/raw/counts.csv
        ```

        ```text
        00000000  70 6c 61 63 65 2c 62 69  6b 65 73 0a 41 6e 74 61  |place,bikes.Anta|
        00000010  6b 61 6c 6e 69 73 2c 34  31 32 0a 55 c5 be 75 70  |kalnis,412.U..up|
        00000020  69 73 2c 33 38 38 0a                              |is,388.|
        00000027
        ```

        `c5 be` is `ž`: two bytes, two dots on the right. `0a` ends each
        line. The last line is the size in hex: 0x27 = 2 × 16 + 7 = 39.

    === "Windows"

        ```text
        Format-Hex data/raw/counts.csv
        ```

        ```text
           Label: C:\Users\smilte\bike-project\data\raw\counts.csv

                  Offset Bytes                                           Ascii
                         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
                  ------ ----------------------------------------------- -----
        0000000000000000 70 6C 61 63 65 2C 62 69 6B 65 73 0D 0A 41 6E 74 place,bikes��Ant
        0000000000000010 61 6B 61 6C 6E 69 73 2C 34 31 32 0D 0A 55 C5 BE akalnis,412��UÅ¾
        0000000000000020 75 70 69 73 2C 33 38 38 0D 0A                   upis,388��
        ```

        `C5 BE` is `ž`; PowerShell shows it on the right as `Å¾`, because
        it reads each byte alone. `0D 0A` ends each line.

7. **Windows only.** Select `CRLF` in the Status Bar, choose `LF`, save,
   and measure again:

    ```text
    (Get-Item data/raw/counts.csv).Length
    ```

    ```text
    39
    ```

    One byte less on each of the three lines. Now the file has the same
    bytes on every laptop in the room.

8. **A two-line script.** Work in pairs, one Mac and one Windows
   laptop; a room of one system watches the projector for the other. In
   the Explorer select the folder `scripts`, then **New File**.

    === "macOS"

        Name the file `hello.sh` and type two lines, with `Enter` after the
        second. Save.

        ```text
        #!/bin/zsh
        echo hello
        ```

        The first line names the program that runs the file. Allow the
        file to run as a command, then run it:

        ```text
        chmod +x scripts/hello.sh
        ```

        ```text
        ./scripts/hello.sh
        ```

        ```text
        hello
        ```

    === "Windows"

        Name the file `hello.ps1` and type one line. Save.

        ```text
        Write-Output hello
        ```

        Run it:

        ```text
        ./scripts/hello.ps1
        ```

        ```text
        hello
        ```

        The Status Bar shows `CRLF`: a new file on Windows gets the
        Windows line ending. Show it to your Mac neighbour.

9. **Switch the line ending and run it again.**

    === "macOS"

        Select `LF` in the Status Bar, choose `CRLF`, save. The file now
        has the bytes VS Code writes on Windows, as if your neighbour had
        sent it. Look at the bytes, then run it again:

        ```text
        hexdump -C scripts/hello.sh
        ```

        ```text
        00000000  23 21 2f 62 69 6e 2f 7a  73 68 0d 0a 65 63 68 6f  |#!/bin/zsh..echo|
        00000010  20 68 65 6c 6c 6f 0d 0a                           | hello..|
        00000018
        ```

        ```text
        ./scripts/hello.sh
        ```

        ```text
        zsh: ./scripts/hello.sh: bad interpreter: /bin/zsh^M: no such file or directory
        ```

        `^M` is the byte `0d`. The Mac ends the first line at `0a` alone,
        so the name of the program is now `/bin/zsh` followed by `0d`, and
        no program has that name. The file does not run at all.

    === "Windows"

        Select `CRLF` in the Status Bar, choose `LF`, save, and run it
        again:

        ```text
        ./scripts/hello.ps1
        ```

        ```text
        hello
        ```

        PowerShell reads both line endings. Look at your neighbour's
        screen: the same two bytes stop their file.

10. **Back to LF, then clean up.** On the Mac, select `CRLF` in the Status
    Bar, choose `LF`, save, and run `./scripts/hello.sh` again: `hello`.
    Then both delete the script, which the project does not need:

    === "macOS"

        ```text
        rm scripts/hello.sh
        ```

    === "Windows"

        ```text
        rm scripts/hello.ps1
        ```

    A file that runs on Windows can fail on a Mac with no difference to
    see in the editor; the Status Bar shows it. To make VS Code write LF
    in every new file on Windows: `Ctrl+,`, search `eol`, set **Files:
    Eol** to `\n`.

!!! success "You should now see"
    39 bytes on every laptop, and `c5 be` for `ž` in the hex view. On a
    Mac, `bad interpreter` for the script with CRLF and `hello` again with
    LF; on Windows, `hello` with both.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | 38 bytes on a Mac, 40 on Windows | No `Enter` after the last line. Add it and save |
    | 38 bytes on a Mac (41 on Windows), and no `c5 be` in the hex view | `Uzupis` was typed without `ž`. Copy the line from this page |
    | The size does not change after an edit | The file was not saved: a dot on the tab means *not saved* |
    | Windows: `Cannot find path` | The file is not in `data/raw`, or the terminal is not in `bike-project`. `pwd`, then `ls data/raw` |
    | macOS: `zsh: permission denied: ./scripts/hello.sh` | `chmod +x scripts/hello.sh` was skipped. Run it, then the script again |
    | macOS: still `hello` after choosing `CRLF` | The file was not saved after the switch |
    | Windows: `… cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1. Switch to PowerShell 7 (section 6), or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |

---

## Part 2 · Read, count and copy a large file { #part-2 }

**0:49 to 1:06 · sections 8 to 10**

Two files come from the web and are moved in by typed commands. The large
one has thousands of lines; nobody opens it to count them.

---

### 8. Move the downloaded files into the project { #files }

**0:49 · 3 min**

**Tell the room.** The browser saves into **Downloads**. `mv` moves a file:
first where it is, then where it goes. `~/Downloads/bikes.csv` is the same
path in both shells. Press `Tab` after a few letters of each name: a name
that `Tab` completed has no typing mistake in it.

1. Download the two core files of the box **Files for this seminar** at the
   top of this page: `bikes.csv` and `column_stats.py`. Do not open them.

2. Move them in.

    ```text
    mv ~/Downloads/bikes.csv data/raw/
    ```

    ```text
    mv ~/Downloads/column_stats.py scripts/
    ```

    A move prints nothing when it works.

3. Check.

    ```text
    ls data/raw
    ```

    ```text
    bikes.csv       counts.csv
    ```

!!! success "You should now see"
    `bikes.csv` next to `counts.csv` in `data/raw`, and `column_stats.py` in
    `scripts`, in the terminal and in the Explorer.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory`, or PowerShell: `Cannot find path` | The name in **Downloads** differs. `ls ~/Downloads` shows how it is spelled |
    | A file named `bikes (1).csv` | It was downloaded twice. Move it and rename it in one line: `mv ~/Downloads/"bikes (1).csv" data/raw/bikes.csv`. The quotes hold a name with spaces together |
    | The browser opened the file instead of saving it | Go back and right-click the link, **Save Link As...** |

---

### 9. Read `bikes.csv`, count its lines and bytes { #count }

**0:52 · 8 min**

**Tell the room.** A command has parts: the **program** first, then
**options** that say how, then **arguments** that say what to work on.
`head -n 3 data/raw/bikes.csv`: the program `head`, the option `-n 3`, the
argument, a path.

1. The first three lines.

    === "macOS"

        ```text
        head -n 3 data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        Get-Content data/raw/bikes.csv -Head 3
        ```

    ```text
    time,counter,bikes
    2024-01-01T00:00,bridge,2
    2024-01-01T00:00,park,0
    ```

    A header, then one row per counter and hour: the start of the hour, the
    counter, the number of bicycles that passed.

2. The last two lines.

    === "macOS"

        ```text
        tail -n 2 data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        Get-Content data/raw/bikes.csv -Tail 2
        ```

    ```text
    2025-12-31T23:00,bridge,4
    2025-12-31T23:00,park,1
    ```

3. `cat` prints a whole file, in both shells. The small one:

    ```text
    cat data/raw/counts.csv
    ```

    ```text
    place,bikes
    Antakalnis,412
    Užupis,388
    ```

4. Count the lines of the large file.

    === "macOS"

        ```text
        wc -l data/raw/bikes.csv
        ```

        ```text
           35089 data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Get-Content data/raw/bikes.csv).Count
        ```

        ```text
        35089
        ```

    Check it by hand: 2024 had 366 days and 2025 had 365, so 731 days of 24
    hours, at two counters: 731 × 24 × 2 = 35 088 rows, and the header
    makes 35 089 lines.

5. Its size in bytes.

    === "macOS"

        ```text
        wc -c data/raw/bikes.csv
        ```

        ```text
          900314 data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/raw/bikes.csv).Length
        ```

        ```text
        900314
        ```

    About 26 bytes a line, as in section 7: `2024-01-01T00:00,bridge,2` has 25
    characters, one byte each, and one line break.

6. Make two mistakes on purpose, and read what the shell says. A program
   that does not exist:

    === "macOS"

        ```text
        haed -n 3 data/raw/bikes.csv
        ```

        ```text
        zsh: command not found: haed
        ```

    === "Windows"

        ```text
        Gte-Content data/raw/bikes.csv -Head 3
        ```

        ```text
        Gte-Content: The term 'Gte-Content' is not recognized as a name of a cmdlet, function, script file, or executable program.
        Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
        ```

    A file that does not exist:

    === "macOS"

        ```text
        head -n 3 data/raw/bike.csv
        ```

        ```text
        head: data/raw/bike.csv: No such file or directory
        ```

    === "Windows"

        ```text
        Get-Content data/raw/bike.csv -Head 3
        ```

        ```text
        Get-Content: Cannot find path 'C:\Users\smilte\bike-project\data\raw\bike.csv' because it does not exist.
        ```

    The first word of the message names who complains: the shell, or the
    program that could not find the file.

7. Help on a command. On macOS `q` leaves the manual page.

    === "macOS"

        ```text
        man head
        ```

    === "Windows"

        ```text
        Get-Help Get-Content
        ```

        It prints the syntax and the short names (`cat`, `gc`, `type`). The
        full text comes after `Update-Help`, or online with
        `Get-Help Get-Content -Online`.

!!! success "You should now see"
    35 089 lines and 900 314 bytes for `bikes.csv`, on every laptop. Ask
    two students to read their numbers aloud.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `head` waits and prints nothing | The file name is missing, so `head` reads the keyboard. `Ctrl+C` stops it |
    | Windows: `A positional parameter cannot be found that accepts argument …` | A space in a path. Names today have no spaces; check the line |
    | A size other than 900 314 | The file was opened and saved in Excel or Numbers. Download it again and move it in |
    | macOS: the manual page fills the Panel | `Space` goes on, `q` leaves |

---

### 10. Copy, rename, delete { #copy }

**1:00 · 6 min**

**Tell the room.** `cp` copies, `mv` moves and renames, `rm` deletes. In
PowerShell the same short words work: they are short names of `Copy-Item`,
`Move-Item` and `Remove-Item`. A `*` stands for any characters in a name.
`rm` has no bin: what it deletes is gone. So we practise in a folder made
for it.

1. Make a backup folder and copy the small file into it.

    ```text
    mkdir backup
    ```

    ```text
    cp data/raw/counts.csv backup/
    ```

2. Rename the copy with `mv`: first the old name, then the new one.

    ```text
    mv backup/counts.csv backup/counts_copy.csv
    ```

3. Copy a whole folder: `-r` copies everything in it.

    ```text
    cp -r data backup/
    ```

    ```text
    ls backup
    ```

    ```text
    counts_copy.csv data
    ```

4. A wildcard: every CSV file in `data/raw`.

    ```text
    ls data/raw/*.csv
    ```

    ```text
    data/raw/bikes.csv      data/raw/counts.csv
    ```

    PowerShell prints the two names in its table.

5. Delete the copy, then the whole backup folder. Say the name aloud before
   pressing `Enter`.

    ```text
    rm backup/counts_copy.csv
    ```

    ```text
    rm -r backup
    ```

    ```text
    ls
    ```

    ```text
    README.md       data            results         scripts
    ```

!!! success "You should now see"
    The project folder as it was, with nothing lost from `data/raw`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `cp: data is a directory (not copied).` | A folder needs `-r` |
    | Windows: `cp data backup2` made an empty folder `backup2` | Without `-r` PowerShell copies the folder alone, not what is in it. `rm backup2`, then with `-r` |
    | macOS: `rm: backup: is a directory` | A folder needs `rm -r` |
    | Windows: `rm backup` asks *The item at … has children …* | `N` and `Enter`, then `rm -r backup` |
    | Something in `data/raw` was deleted | `counts.csv`: type it again (section 7). `bikes.csv`: download it again and move it in |

---

## Part 3 · Pipes and filters { #part-3 }

**1:06 to 1:23 · sections 11 and 12**

So far each command printed its answer. Now the answer of one command
becomes the input of the next, with `|`, and the last answer goes into a
file, with `>`. The question of this part is which hour had the most
bicycles.

---

### 11. A pipe: sort the counts, read both ends { #sort }

**1:06 · 8 min**

**Tell the room.** `A | B` is a **pipe**: what `A` prints goes into `B`,
not onto the screen. A program that reads, changes and passes on is a
**filter**. Sort a column and look at both ends: a wrong value is almost
always at an end.

1. A first pipe: the first three lines, and of those the last.

    === "macOS"

        ```text
        head -n 3 data/raw/bikes.csv | tail -n 1
        ```

    === "Windows"

        ```text
        Get-Content data/raw/bikes.csv -Head 3 | Select-Object -Last 1
        ```

    ```text
    2024-01-01T00:00,park,0
    ```

2. One column. zsh cuts at the commas and keeps field 3; PowerShell reads
   the header and takes the column by its name.

    === "macOS"

        ```text
        cut -d, -f3 data/raw/bikes.csv | head -n 4
        ```

        ```text
        bikes
        2
        0
        3
        ```

    === "Windows"

        ```text
        Import-Csv data/raw/bikes.csv | Select-Object -First 3
        ```

        ```text
        time             counter bikes
        ----             ------- -----
        2024-01-01T00:00 bridge  2
        2024-01-01T00:00 park    0
        2024-01-01T01:00 bridge  3
        ```

3. Sort the counts as numbers and look at the top end: the busiest hours.
   `tail -n +2` starts at line 2, so the header stays out.

    === "macOS"

        ```text
        tail -n +2 data/raw/bikes.csv | cut -d, -f3 | sort -n | tail -n 3
        ```

        ```text
        9999
        9999
        9999
        ```

    === "Windows"

        ```text
        Import-Csv data/raw/bikes.csv | Sort-Object {[double]$_.bikes} | Select-Object -Last 3
        ```

        ```text
        time             counter bikes
        ----             ------- -----
        2025-03-16T09:00 park    9999
        2025-03-15T22:00 park    9999
        2025-03-12T00:00 park    9999
        ```

        `{[double]$_.bikes}` sorts by the value as a number.

4. Ask the room: 9999 bicycles in one hour on a park path, almost three a
   second, at midnight in March? No. A value like this is a **mark**: the
   counter's way of writing "no count".

5. The three lowest counts.

    === "macOS"

        ```text
        tail -n +2 data/raw/bikes.csv | cut -d, -f3 | sort -n | head -n 3
        ```

    === "Windows"

        ```text
        Import-Csv data/raw/bikes.csv | Sort-Object {[double]$_.bikes} | Select-Object -First 3
        ```

    Zeros: hours at night with no bicycle. Those are real.

!!! success "You should now see"
    `9999` at the top of the column on every laptop, and the room agreeing
    that it is not a count.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The line waits and prints nothing | A file name is missing, or a quote is open. `Ctrl+C` and type the line again |
    | Windows: the three rows show other times | All three are `park` and `9999`; rows with the same value may come in another order |
    | `bikes` shows up among the numbers | The header was sorted with them. Start the pipe with `tail -n +2` |

---

### 12. Count the 9999 rows, keep the others in a new file { #grep }

**1:14 · 9 min**

**Tell the room.** `grep` and `Select-String` keep the lines that contain a
text. `,9999$` means: a comma, 9999, and then the end of the line. They can
count those lines, show them, or keep every line *without* them. `>` sends
the result into a file instead of onto the screen: it makes the file, or
empties one that exists.

1. How many rows carry the mark?

    === "macOS"

        ```text
        grep -c ',9999$' data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Select-String ',9999$' data/raw/bikes.csv).Count
        ```

    ```text
    168
    ```

2. The first and the last of them.

    === "macOS"

        ```text
        grep ',9999$' data/raw/bikes.csv | head -n 1
        ```

        ```text
        grep ',9999$' data/raw/bikes.csv | tail -n 1
        ```

    === "Windows"

        ```text
        Select-String ',9999$' data/raw/bikes.csv -Raw | Select-Object -First 1
        ```

        ```text
        Select-String ',9999$' data/raw/bikes.csv -Raw | Select-Object -Last 1
        ```

    ```text
    2025-03-10T00:00,park,9999
    2025-03-16T23:00,park,9999
    ```

    From Monday 10 March to Sunday 16 March 2025, at the park: 7 days of 24
    hours, 7 × 24 = 168, so all 168 marks fall in this one week.

3. Count the rows per counter: is any counter missing hours?

    === "macOS"

        ```text
        cut -d, -f2 data/raw/bikes.csv | sort | uniq -c
        ```

        ```text
        17544 bridge
           1 counter
        17544 park
        ```

        `uniq -c` counts equal lines that stand next to each other, so
        `sort` comes first. The `1 counter` is the header.

    === "Windows"

        ```text
        Import-Csv data/raw/bikes.csv | Group-Object counter -NoElement
        ```

        ```text
        Count Name
        ----- ----
        17544 bridge
        17544 park
        ```

    731 × 24 = 17 544: every hour is there at both counters. The broken
    week has its rows, with 9999 in their `bikes` column.

4. Keep every line without the mark, in a new file in `data/processed`.
   `data/raw` is only read.

    === "macOS"

        ```text
        grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv
        ```

    === "Windows"

        ```text
        Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv
        ```

        `-Raw` passes on the text of each line alone, without a file name
        and a line number in front.

5. Check the new file.

    === "macOS"

        ```text
        wc -l data/processed/bikes_valid.csv
        ```

        ```text
           34921 data/processed/bikes_valid.csv
        ```

    === "Windows"

        ```text
        (Get-Content data/processed/bikes_valid.csv).Count
        ```

        ```text
        34921
        ```

    35 089 − 168 = 34 921.

6. Now the busiest hour, twice: sorted as text, then as numbers.

    === "macOS"

        ```text
        tail -n +2 data/processed/bikes_valid.csv | cut -d, -f3 | sort | tail -n 1
        ```

        ```text
        99
        ```

        ```text
        tail -n +2 data/processed/bikes_valid.csv | cut -d, -f3 | sort -n | tail -n 1
        ```

        ```text
        803
        ```

    === "Windows"

        ```text
        Import-Csv data/processed/bikes_valid.csv | Sort-Object bikes | Select-Object -Last 1
        ```

        ```text
        time             counter bikes
        ----             ------- -----
        2024-09-03T18:00 park    99
        ```

        ```text
        Import-Csv data/processed/bikes_valid.csv | Sort-Object {[double]$_.bikes} | Select-Object -Last 1
        ```

        ```text
        time             counter bikes
        ----             ------- -----
        2024-06-28T08:00 bridge  803
        ```

    As text, `99` comes after `803`, because `9` comes after `8`, the way
    words are ordered in a dictionary. As numbers, 803 is the largest: 803
    bicycles on the bridge on Friday 28 June 2024 at 8:00.

!!! success "You should now see"
    `168`, one broken week at the park, and `bikes_valid.csv` with 34 921
    lines in `data/processed`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Someone typed `9999` alone and got 168 too | Here it gives the same count. The `,` and the `$` make sure that only a whole value 9999 at the end of a line counts, never a 9999 inside a longer number |
    | `bikes_valid.csv` is empty | The line read from the file it wrote to. Never `>` into the file that is read |
    | Windows: every line of the new file starts with `data\raw\bikes.csv:` | `-Raw` was left out. Run the line again with it |

---

## Part 4 · Python, a checksum, the README { #part-4 }

**1:23 to 1:52 · sections 13 to 17**

Python arrives and runs a program someone else wrote. A checksum shows that
a file is the same on every laptop, and the README writes down what was
done, as a line anyone can run again.

---

### 13. Install Miniforge, run `column_stats.py` { #python }

**1:23 · 10 min**

**Tell the room.** A program is a file. To run a Python program, the shell
needs Python, and finds it in the folders listed in `PATH`. Python comes
with **Miniforge**. It installs **conda**, a program that installs packages
and keeps them apart in **environments**, and a first environment, `base`,
with Python in it. The installer adds a few lines to a file the shell runs
whenever it starts, `~/.zshrc` on a Mac and `profile.ps1` on Windows, so
that every new terminal finds conda and Python. Then VS Code is
restarted, so that its terminal runs those lines.

1. Ask the shell for Python before the install.

    === "macOS"

        ```text
        python3 --version
        ```

        Either `Python 3.9.6`, the copy that came with the developer tools
        of section 1, or, while those are still installing, a note about
        them. Both are fine: Miniforge brings its own Python.

    === "Windows"

        ```text
        python --version
        ```

        ```text
        Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
        ```

        A stand-in of Windows answered, not Python.

2. Install Miniforge from the file that section 1 downloaded.

    === "macOS"

        In the terminal of VS Code:

        ```text
        bash ~/Downloads/Miniforge3-$(uname)-$(uname -m).sh
        ```

        The installer stops five times:

        | It prints | You type |
        |--|--|
        | `Please, press ENTER to continue` | `Enter` |
        | The licence, one screen at a time | `q`, which jumps to its end |
        | `Do you accept the license terms?` | `yes` |
        | `[/Users/smilte/miniforge3] >>>` | `Enter`: the folder is right |
        | `Proceed with initialization?` and `[no] >>>` | `yes`. The answer in brackets is the default, so `Enter` alone would say no |

        It ends with:

        ```text
        Thank you for installing Miniforge3!
        ```

    === "Windows"

        Open `Miniforge3-Windows-x86_64.exe` in **Downloads**. Select
        **Next** and **I Agree**, choose **Just Me (recommended)**, and keep
        every other default: the folder `C:\Users\smilte\miniforge3`, the
        boxes as they are, **Install**, then **Finish**.

        Then press the Windows key, type `Miniforge Prompt` and press
        `Enter`. In the window that opens, let conda add its lines to the
        profile scripts of PowerShell:

        ```text
        conda init powershell
        ```

        It lists the files it looked at and ends with:

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

        Close the Miniforge Prompt.

3. Quit VS Code with **File** > **Exit** (macOS `Cmd+Q`) and start it again.
   It opens `bike-project`. Open a new terminal: the prompt now starts with
   `(base)`, the environment conda switched on. Ask again.

    === "macOS"

        ```text
        conda --version
        ```

        ```text
        conda 26.7.2
        ```

        ```text
        python3 --version
        ```

        ```text
        Python 3.14.7
        ```

        ```text
        which python3
        ```

        ```text
        /Users/smilte/miniforge3/bin/python3
        ```

    === "Windows"

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

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\smilte\miniforge3\python.exe
        ```

    The folder of `base` now comes first in `PATH`, so the shell finds this
    Python before any other.

4. Run the program on the file you typed: the program, the file to run,
   then two words for the program: the file it reads and the column.

    === "macOS"

        ```text
        python3 scripts/column_stats.py data/raw/counts.csv bikes
        ```

    === "Windows"

        ```text
        python scripts/column_stats.py data/raw/counts.csv bikes
        ```

    ```text
    file    data/raw/counts.csv
    column  bikes
    rows    2
    min     388.0
    max     412.0
    mean    400
    ```

    Check it by hand: (412 + 388) / 2 = 400. Nobody has to read the program
    today; it was tested on a file whose answer we know.

!!! success "You should now see"
    `(base)` in the prompt, `Python 3.14.7`, and the mean 400 on every
    laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: no `(base)` in the new terminal, or `zsh: command not found: conda` | The last question of the installer was answered with `Enter`, which means no. Run `~/miniforge3/bin/conda init zsh`, then open a new terminal |
    | macOS: `bash: /Users/smilte/Downloads/Miniforge3-…: No such file or directory` | The download of section 1 did not finish. `ls ~/Downloads`, or copy the installer from the USB stick into **Downloads** |
    | macOS: `ERROR: File or directory already exists: '/Users/smilte/miniforge3'` | Miniforge is there already, from an earlier try. Go on with step 3 |
    | Windows: "Windows protected your PC" when the installer starts | Select **More info**, then **Run anyway** |
    | Windows: `conda : The term 'conda' is not recognized …`, and no `(base)` | `conda init powershell` was not run in the Miniforge Prompt, or VS Code was not quit and started again |
    | Windows: `… profile.ps1 cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1: switch to PowerShell 7 (section 6). Or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, answer `Y`, and open a new terminal |
    | Windows: still `Python was not found` | conda is not on in this terminal: there is no `(base)` in the prompt. See the two rows above. Never install Python from the Store |
    | `no column bikes in data/raw/counts.csv` | The header of `counts.csv` was typed differently. It must read `place,bikes` |

---

### 14. The mean with and without the 9999 rows { #mean }

**1:33 · 4 min**

**Tell the room.** The same program on the large file. It counts every
value it finds, the mark too: it cannot know that 9999 means "no count".

1. The raw file, then the clean one. The lines are the same in both shells,
   with `python` on Windows.

    ```text
    python3 scripts/column_stats.py data/raw/bikes.csv bikes
    ```

    ```text
    file    data/raw/bikes.csv
    column  bikes
    rows    35088
    min     0.0
    max     9999.0
    mean    86.2712
    ```

    ```text
    python3 scripts/column_stats.py data/processed/bikes_valid.csv bikes
    ```

    ```text
    file    data/processed/bikes_valid.csv
    column  bikes
    rows    34920
    min     0.0
    max     803.0
    mean    38.5811
    ```

2. Work out the difference with the room: 168 × 9999 = 1 679 832 bicycles
   that never passed, spread over 35 088 rows, adds about 48 to every
   hour. One broken week in two years more than doubles the mean.

!!! success "You should now see"
    86.2712 and 38.5811 on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `no column Bikes` | Column names are exact: `bikes` |

---

### 15. Compare checksums across the room { #checksum }

**1:37 · 5 min**

**Tell the room.** A **checksum** is a long number computed from every
byte of a file. Two files with the same bytes have the same checksum; one
byte changed gives a completely different one. Thirty laptops can check
that they hold the same file by reading eight characters aloud.

1. The checksum of the downloaded file.

    === "macOS"

        ```text
        shasum -a 256 data/raw/bikes.csv
        ```

        ```text
        2c68aad221bfb1cc8346625a842eca3897c3c39bba5cfc2fe7d27891e3808991  data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/raw/bikes.csv).Hash
        ```

        ```text
        2C68AAD221BFB1CC8346625A842ECA3897C3C39BBA5CFC2FE7D27891E3808991
        ```

    Ask three students, one on Windows, to read the first eight characters:
    `2c68aad2`. The case of the letters does not matter.

2. The file you typed. Thirty people typed it; are the bytes the same?

    === "macOS"

        ```text
        shasum -a 256 data/raw/counts.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/raw/counts.csv).Hash
        ```

    `d992afbf…` for the 39 bytes of section 7, on a Mac and on Windows. A
    laptop with another checksum typed one character differently, or kept
    CRLF: `c2d52752…` is the 42-byte file.

3. The file the shell wrote, with `>`.

    === "macOS"

        ```text
        shasum -a 256 data/processed/bikes_valid.csv
        ```

        ```text
        4a505f781fb717ed3433e042d43cc522fe7550cec40085ec741602773a2cd92a  data/processed/bikes_valid.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/bikes_valid.csv).Hash
        ```

        ```text
        8BD1459D4D008B89DB57AC1A902B0B9C6944275B1F4891F1C5205B641AA6AD31
        ```

    The rows are the same on both systems, the checksums are not. PowerShell
    on Windows ends each line it writes with CRLF, as VS Code did in section 7: 34 921 bytes more,
    930 699 against 895 778.

!!! success "You should now see"
    `2c68aad2…` on every laptop, `d992afbf…` on most, and two checksums for
    `bikes_valid.csv`, one per system.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Another checksum for `bikes.csv` | The file is not the downloaded one: it was opened and saved, or the download broke. Download it again |
    | Windows: a table with `Algorithm`, `Hash`, `Path` | The brackets and `.Hash` were left out. The hash is the middle column |

---

### 16. Data, columns and the rebuild line in the README { #readme }

**1:42 · 6 min**

**Tell the room.** The README of section 5 says what the project is. A
stranger also needs to know where the data came from, what each column
means, which value marks a missing one, and how every file in
`data/processed` is made again: the line that ran today, copied from the
terminal, not retyped from memory.

1. Open `README.md` and its preview (`Ctrl+K`, then `V`). Add at the end:

    ```text
    ## Data

    - `data/raw/counts.csv`: the two places above, typed by hand.
    - `data/raw/bikes.csv`: two bicycle counters, one row per counter and hour
      of 2024 and 2025, 35 088 rows, SHA-256 `2c68aad2…e3808991`. From the
      course workbook, Seminar 4.

    ## Columns of `bikes.csv`

    | Column | Meaning | Unit |
    |--|--|--|
    | `time` | start of the hour | YYYY-MM-DDTHH:MM |
    | `counter` | `bridge` or `park` | none |
    | `bikes` | bicycles that passed in that hour | bicycles |

    Missing value: `bikes` is `9999` in 168 rows, the park counter from
    2025-03-10 to 2025-03-16, while it was broken.

    ## How to rebuild

    Run in the project folder: zsh on macOS, PowerShell 7 on Windows.

    - `data/processed/bikes_valid.csv`: `bikes.csv` without the rows marked
      `9999`, 34 921 lines.
    ```

2. Under the last item, add the line of your shell. Press `↑` in the
   terminal until it comes back, select it with the mouse, copy, and paste
   it between backticks:

    ```text
      - zsh: `grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv`
      - PowerShell: `Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv`
    ```

3. Save with `Ctrl+S` (macOS `Cmd+S`).

!!! success "You should now see"
    In the preview: **Data** with the checksum of `bikes.csv`, a table of
    three columns, the line about `9999`, and **How to rebuild** with the
    line that made `bikes_valid.csv`. The README gives that line and no
    checksum for the file: section 15 showed that it differs between macOS
    and Windows.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The checksum in the README was typed by hand | Copy it from the terminal instead: one wrong character and it names another file |
    | The command shows without its `$` or with odd formatting | It must stand between backticks, as on this page |

---

### 17. Wrap up { #wrap-up }

**1:48 · 4 min**

**Tell the room.** Git keeps versions of files, from next week on. It
writes a name and an address into every version, so it is told both once,
now. Nothing is printed, which is correct.

1. Check that Git is installed, then tell it who you are, with your own
   name and address.

    ```text
    git --version
    ```

    ```text
    git config --global user.name "Smiltė"
    ```

    ```text
    git config --global user.email "smilte@example.com"
    ```

2. Read the list of the day with the room:

    - VS Code has five regions; the Command Palette finds any command.
    - The shell runs in the terminal; the prompt shows the working
      directory; `pwd`, `ls`, `cd` move around; `Tab` and `↑` save typing.
    - A file is bytes: `ž` is two of them, a line end one (LF) or two
      (CRLF).
    - A command is a program, options and arguments. `head`, `tail`, `cat`,
      `wc`, `cp`, `mv`, `rm`, `mkdir`, `*`.
    - `|` joins filters, `>` writes a file. The sorted column showed `9999`
      at its top end: the mark for no count, in 168 rows, one week of the
      park counter, and it more than doubled the mean.
    - Python comes with Miniforge, in conda's environment `base`, which
      every new terminal switches on: `(base)` in the prompt.
    - A program someone else wrote runs with one line; a checksum shows that
      two files hold the same bytes; the README holds the line that makes
      the processed file again.

!!! success "You should now see"
    `git version 2.…` on every laptop, and the folder `bike-project` with a
    README, two raw files, one processed file and one script.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `git: command not found`, or *not recognized* | The install of section 1 has not finished, or VS Code started before it did. Quit VS Code, start it again, `git --version` |
    | macOS: the developer tools are still installing | Let them finish after the session; `git config` can wait until next week |

---

## Optional, if the room is fast { #optional }

Each section stands on its own and takes about ten minutes. Take them in
any order.

---

### 18. A program that cleans an export { #clean }

**— · 10 min**

**Tell the room.** A spreadsheet with European settings exports a table
with `;` between the values and a decimal comma. Most programs read neither.
A second program someone else wrote makes four edits: it deletes the
summary line, turns the decimal comma into a point, turns `;` into `,`, and
deletes the column `nr`.

1. Download `monthly_export.csv` and `clean_export.py` from the box **Files
   for this seminar**, and move them in.

    ```text
    mv ~/Downloads/monthly_export.csv data/raw/
    ```

    ```text
    mv ~/Downloads/clean_export.py scripts/
    ```

2. Look at the export.

    ```text
    cat data/raw/monthly_export.csv
    ```

    ```text
    nr;month;per_day
    1;2025-01;312,2
    2;2025-02;480,3
    3;2025-03;756,7
    4;2025-04;1360,6
    5;2025-05;1676,5
    6;2025-06;1945,5
    7;2025-07;1927,5
    8;2025-08;1860,8
    9;2025-09;1453,2
    10;2025-10;1187,0
    11;2025-11;792,0
    12;2025-12;432,2
    ;mean;1182,04
    ```

    Bicycles per day on the bridge, each month of 2025, and the mean at the
    end.

3. Clean it: the program, the file it reads, the file it writes.

    === "macOS"

        ```text
        python3 scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv
        ```

    === "Windows"

        ```text
        python scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv
        ```

    ```text
    12 rows written to data/processed/monthly.csv
    ```

4. Look at the result, then its mean.

    ```text
    cat data/processed/monthly.csv
    ```

    ```text
    month,per_day
    2025-01,312.2
    2025-02,480.3
    2025-03,756.7
    2025-04,1360.6
    2025-05,1676.5
    2025-06,1945.5
    2025-07,1927.5
    2025-08,1860.8
    2025-09,1453.2
    2025-10,1187.0
    2025-11,792.0
    2025-12,432.2
    ```

    ```text
    python3 scripts/column_stats.py data/processed/monthly.csv per_day
    ```

    ```text
    file    data/processed/monthly.csv
    column  per_day
    rows    12
    min     312.2
    max     1945.5
    mean    1182.04
    ```

    The mean line of the spreadsheet, 1182,04, computed again.

5. Its checksum.

    === "macOS"

        ```text
        shasum -a 256 data/processed/monthly.csv
        ```

        ```text
        ea4ce2cee1cb14872a6364966b6f53554c828030988cac813643803119396ef6  data/processed/monthly.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/monthly.csv).Hash
        ```

        ```text
        EA4CE2CEE1CB14872A6364966B6F53554C828030988CAC813643803119396EF6
        ```

    The same on a Mac and on Windows, unlike `bikes_valid.csv`: the program
    ends every line with LF on every system. Add it to **How to rebuild**:
    `data/processed/monthly.csv`, 189 bytes, SHA-256 `ea4ce2ce…19396ef6`,
    with the line of step 3.

!!! success "You should now see"
    `monthly.csv` with 12 rows, the mean 1182.04, and `ea4ce2ce…` on every
    laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `no column per_day … the columns are: nr;month;per_day` | That is the raw export: with `;` between the values, the program sees one column. Give it the cleaned file |
    | `no file data/raw/monthly_export.csv` | Step 1 was not done, or the file kept another name in **Downloads** |

---

### 19. Regular expressions in VS Code and the shell { #regex }

**— · 10 min**

**Tell the room.** A **regular expression** describes a kind of text:
`[0-9]` is any digit, `{3}` exactly three of what stands before it, `[5-9]`
one digit from 5 to 9, `$` the end of a line. The same patterns work in the
Find box of VS Code and in the shell.

1. Open `data/raw/bikes.csv`. Press `Ctrl+F` (macOS `Cmd+F`) and switch on
   the button `.*` at the right end of the box. Type the three patterns
   below one after the other, and read the count of matches:

    ```text
    ,9999$
    ```

    ```text
    ,[0-9]{3}$
    ```

    ```text
    ,[5-9][0-9]{2}$
    ```

    168: the broken week. 4022: hours with 100 to 999 bicycles. 37: hours
    with 500 or more. A value of 9999 has four digits after the comma, so
    the second pattern leaves it out.

2. Close the file without saving. The last pattern in the shell:

    === "macOS"

        ```text
        grep -E -c ',[5-9][0-9]{2}$' data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Select-String ',[5-9][0-9]{2}$' data/raw/bikes.csv).Count
        ```

    ```text
    37
    ```

3. How many mornings at 8:00 had 100 bicycles or more on the bridge?

    === "macOS"

        ```text
        grep -E -c 'T08:00,bridge,[0-9]{3}$' data/raw/bikes.csv
        ```

    === "Windows"

        ```text
        (Select-String 'T08:00,bridge,[0-9]{3}$' data/raw/bikes.csv).Count
        ```

    ```text
    386
    ```

    386 of the 731 mornings.

!!! success "You should now see"
    168, 4022 and 37 in the Find box, then 37 and 386 in the shell.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The Find box counts 0 | The `.*` button is off |
    | zsh: `grep -c ',[5-9][0-9]{2}$'` prints 0 | Without `-E`, grep reads `{2}` as plain text |
    | The file was changed | Close it without saving. Files in `data/raw` are never edited |

---

### 20. A conda environment for the project { #environment }

**— · 12 min**

**Tell the room.** Since section 13 every terminal starts in conda's
environment `base`: one Python, shared by everything on the laptop. A
package installed there is shared by every project, and an upgrade for one
can break another. An **environment** is a folder with a Python and
packages of its own. **Activating** it puts its folder at the front of
`PATH`, so that `python` means this one. The project keeps the list of what
is in it, `environment.yml`, and any laptop makes the same environment from
that list.

1. Where the shell finds Python now. The prompt starts with `(base)`.

    === "macOS"

        ```text
        which python3
        ```

        ```text
        /Users/smilte/miniforge3/bin/python3
        ```

    === "Windows"

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\smilte\miniforge3\python.exe
        ```

2. Make an environment for the project, with Python 3.14.

    ```text
    conda create -n bikes python=3.14
    ```

    conda shows its plan, the folder first, and asks before it installs:

    === "macOS"

        ```text
        ## Package Plan ##

          environment location: /Users/smilte/miniforge3/envs/bikes

          added / updated specs:
            - python=3.14
        ```

    === "Windows"

        ```text
        ## Package Plan ##

          environment location: C:\Users\smilte\miniforge3\envs\bikes

          added / updated specs:
            - python=3.14
        ```

    Below the plan comes the list of packages, Python and the libraries it
    needs, then `Proceed ([y]/n)?`. Press `Enter`. It ends with:

    ```text
    #     $ conda activate bikes
    ```

3. Switch it on.

    ```text
    conda activate bikes
    ```

    The prompt now starts with `(bikes)`.

    === "macOS"

        ```text
        which python
        ```

        ```text
        /Users/smilte/miniforge3/envs/bikes/bin/python
        ```

    === "Windows"

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\smilte\miniforge3\envs\bikes\python.exe
        ```

    From here the word is `python` in both shells.

4. The environment has Python and nothing else: numpy is missing. Install
   it.

    ```text
    python -c "import numpy"
    ```

    ```text
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
        import numpy
    ModuleNotFoundError: No module named 'numpy'
    ```

    ```text
    conda install numpy
    ```

    Press `Enter` at `Proceed ([y]/n)?`. numpy comes with the libraries it
    calls for its arithmetic.

    ```text
    python -c "import numpy; print(numpy.__version__)"
    ```

    ```text
    2.5.4
    ```

5. numpy went into `bikes` only. Switch back to `base`, ask, and switch on
   `bikes` again.

    ```text
    conda deactivate
    ```

    The prompt shows `(base)` again.

    === "macOS"

        ```text
        python3 -c "import numpy"
        ```

    === "Windows"

        ```text
        python -c "import numpy"
        ```

    ```text
    ModuleNotFoundError: No module named 'numpy'
    ```

    ```text
    conda activate bikes
    ```

6. Write the list down, so that another laptop makes the same environment.

    ```text
    conda env export --from-history -f environment.yml
    ```

    Open `environment.yml` in VS Code:

    ```text
    name: bikes
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - numpy
    prefix: /Users/smilte/miniforge3/envs/bikes
    ```

    `--from-history` writes what was asked for, not every library that
    came with it: those differ between a Mac and Windows. Two edits, then
    save:

    - Delete the last line, `prefix: …`. It names a folder on this laptop.
    - Change `- numpy` to `- numpy=2.5.4`. Without a version, the next
      laptop gets whatever numpy is newest that day.

7. List the environments, then switch `bikes` off.

    ```text
    conda env list
    ```

    === "macOS"

        ```text
        # conda environments:
        #
        # * -> active
        # + -> frozen
        base                     /Users/smilte/miniforge3
        bikes                *   /Users/smilte/miniforge3/envs/bikes
        ```

    === "Windows"

        ```text
        # conda environments:
        #
        # * -> active
        # + -> frozen
        base                     C:\Users\smilte\miniforge3
        bikes                *   C:\Users\smilte\miniforge3\envs\bikes
        ```

    ```text
    conda deactivate
    ```

!!! success "You should now see"
    `(bikes)` in the prompt while it was on, numpy 2.5.4 in `bikes` and
    not in `base`, and `environment.yml` of six lines in the project. On
    another laptop one line makes the same environment from it:
    `conda env create -f environment.yml`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `conda: command not found`, or `The term 'conda' is not recognized` | conda is not on in this terminal: section 13, step 3 |
    | `EnvironmentNameNotFound: Could not find conda environment: bikez` | A typo, or `conda create` did not finish. `conda env list` shows the names |
    | `conda install numpy` ran with `(base)` in the prompt | numpy went into `base`. `conda remove numpy`, then `conda activate bikes` and install it again |
    | `environment.yml` still ends with `prefix:` | Delete that line and save |
    | Windows: `… cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1. Switch to PowerShell 7 (section 6), or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |
    | Other version numbers | A newer Python 3.14 or numpy was released. Fine |

---

### 21. A list of checksums { #list }

**— · 8 min**

**Tell the room.** The files in `data/raw` must never change. A list of
their checksums, written once, turns that rule into a test that takes a
second.

1. Write the list. It goes into `data`, not into `data/raw`, so that
   `data/raw/*` never includes it.

    === "macOS"

        ```text
        shasum -a 256 data/raw/* > data/checksums.txt
        ```

    === "Windows"

        ```text
        (Get-FileHash data/raw/*).Hash | Set-Content data/checksums.txt
        ```

2. Test it.

    === "macOS"

        ```text
        shasum -a 256 -c data/checksums.txt
        ```

        ```text
        data/raw/bikes.csv: OK
        data/raw/counts.csv: OK
        ```

        A third line, `monthly_export.csv: OK`, if section 18 was done.

    === "Windows"

        ```text
        $list = Get-Content data/checksums.txt
        ```

        ```text
        $now = (Get-FileHash data/raw/*).Hash
        ```

        ```text
        Compare-Object $list $now
        ```

        Nothing is printed: no line differs. `$list = …` keeps an answer
        under a name for the next line.

3. Change one digit, in a copy of the project, never in the project itself.
   Copy the folder and go into the copy:

    ```text
    cp -r ~/bike-project ~/bike-copy
    ```

    ```text
    cd ~/bike-copy
    ```

    In VS Code select **File** > **Open File...**, open
    `data/raw/bikes.csv` inside `bike-copy` in the home folder, change line
    2 from `2024-01-01T00:00,bridge,2` to `2024-01-01T00:00,bridge,3`, save
    and close it.

4. Test the copy.

    === "macOS"

        ```text
        shasum -a 256 -c data/checksums.txt
        ```

        ```text
        data/raw/bikes.csv: FAILED
        data/raw/counts.csv: OK
        shasum: WARNING: 1 computed checksum did NOT match
        ```

    === "Windows"

        ```text
        $now = (Get-FileHash data/raw/*).Hash
        ```

        ```text
        Compare-Object $list $now
        ```

        ```text
        InputObject                                                      SideIndicator
        -----------                                                      -------------
        E3BB52964625BDAAF5FCF377F2ED8CB0C63602B0B97DAC92669CBE54E4709348 =>
        2C68AAD221BFB1CC8346625A842ECA3897C3C39BBA5CFC2FE7D27891E3808991 <=
        ```

        `<=` is the checksum in the list, `=>` the one found now.

5. Go back and delete the copy.

    ```text
    cd ~/bike-project
    ```

    ```text
    rm -r ~/bike-copy
    ```

!!! success "You should now see"
    `OK` for every file of the project, and the one changed file caught in
    the copy: one digit out of 900 314 bytes.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: a file of `data/raw` has no `OK` line | It came into `data/raw` after the list was written, for example in section 18. `-c` checks only the files on the list: write the list again (step 1) |
    | Windows: a checksum with `=>` and none with `<=` before any change | The same: a file came in after the list was written. Write the list again (step 1) |
    | In the copy, `ls` shows a folder `bike-project` and no `data` | `bike-copy` was there from an earlier try, so the project went inside it. `cd ~`, `rm -r ~/bike-copy`, then step 3 again |

---

### 22. Test the README { #readme-test }

**— · 6 min**

**Tell the room.** A README is tested the way a stranger would use it:
delete what it says can be made again, run its line, and measure.

1. Delete the processed file.

    ```text
    rm data/processed/bikes_valid.csv
    ```

2. Open the preview of `README.md`, copy the line of your shell from **How
   to rebuild** and paste it into the terminal.

3. Count.

    === "macOS"

        ```text
        wc -l data/processed/bikes_valid.csv
        ```

    === "Windows"

        ```text
        (Get-Content data/processed/bikes_valid.csv).Count
        ```

    34 921 lines, the number the README states.

!!! success "You should now see"
    `bikes_valid.csv` back in `data/processed`, with the number of lines the
    README states.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The count says the file does not exist | The pasted line did not run. Press `Enter` after pasting |
    | Windows: the prompt shows `>>` and waits | The backticks came along: a backtick at the end of a line tells PowerShell the line goes on. `Ctrl+C`, then copy the line from the preview, not from the source |

---

### 23. Aliases, the prompt and the start-up file { #settings }

**— · 12 min**

**Tell the room.** A shell runs a file of settings whenever it starts:
`~/.zshrc` for zsh, `$PROFILE` for PowerShell. conda's lines of section 13
went into `~/.zshrc` on a Mac, and into `profile.ps1`, a file beside
`$PROFILE`, on Windows. What is written there comes back in every new
terminal. Nothing in this course needs more of it, and it stays on this
laptop: a README line always uses the full command.

1. Try an alias and a shorter prompt, for this terminal only.

    === "macOS"

        ```text
        alias ..='cd ..'
        ```

        ```text
        PROMPT='%1~ %# '
        ```

    === "Windows"

        ```text
        function .. { Set-Location .. }
        ```

        ```text
        function prompt { "$env:CONDA_PROMPT_MODIFIER$((Get-Item .).Name)> " }
        ```

        `$env:CONDA_PROMPT_MODIFIER` holds `(base) `, or the name of the
        environment that is on, so the prompt keeps showing it.

    Then go down and up again:

    ```text
    cd data
    ```

    ```text
    ..
    ```

    The prompt shows only the folder: `data %` and `bike-project %` on a
    Mac, `(base) data>` and `(base) bike-project>` on Windows. Close the
    terminal with the bin icon of the Panel and open a new one with `+`:
    both settings are gone.

2. Write them into the start-up file.

    === "macOS"

        ```text
        echo "alias ..='cd ..'" >> ~/.zshrc
        ```

        ```text
        echo "PROMPT='%1~ %# '" >> ~/.zshrc
        ```

        ```text
        tail -n 2 ~/.zshrc
        ```

        ```text
        alias ..='cd ..'
        PROMPT='%1~ %# '
        ```

    === "Windows"

        The folder of `$PROFILE` may not exist yet. This line makes it,
        and does nothing if it is there:

        ```text
        New-Item -Force -ItemType Directory (Split-Path $PROFILE) | Out-Null
        ```

        ```text
        Add-Content $PROFILE 'function .. { Set-Location .. }'
        ```

        ```text
        Add-Content $PROFILE 'function prompt { "$env:CONDA_PROMPT_MODIFIER$((Get-Item .).Name)> " }'
        ```

        ```text
        Get-Content $PROFILE
        ```

        ```text
        function .. { Set-Location .. }
        function prompt { "$env:CONDA_PROMPT_MODIFIER$((Get-Item .).Name)> " }
        ```

3. Open a new terminal with `+`. The short prompt is there, and `..` goes
   up one folder.

4. **Oh My Zsh or Oh My Posh.** Show it on the projector; the room may
   follow.

    === "macOS"

        Oh My Zsh is a collection of zsh settings, 371 plugins and 143
        prompt themes. It needs Git (section 1). It writes a new
        `~/.zshrc` and keeps the old one as `~/.zshrc.pre-oh-my-zsh`:

        ```text
        sh -c "$(curl -fsSL https://install.ohmyz.sh/)"
        ```

        A new zsh starts with the prompt `➜  bike-project`. The old
        `~/.zshrc` is now `~/.zshrc.pre-oh-my-zsh`, with the two lines of
        step 2 and conda's lines of section 13. Give conda its lines back
        in the new file, then open a new terminal:

        ```text
        ~/miniforge3/bin/conda init zsh
        ```

        The theme is set by the line `ZSH_THEME="robbyrussell"` in the new
        `~/.zshrc`. To go back: `uninstall_oh_my_zsh`, which puts the old
        file back.

    === "Windows"

        Oh My Posh sets the prompt of PowerShell from a theme:

        ```text
        winget install JanDeDobbeleer.OhMyPosh --source winget
        ```

        Open a new terminal, so that it finds the program, then:

        ```text
        Add-Content $PROFILE 'oh-my-posh init pwsh | Invoke-Expression'
        ```

        A new terminal shows its prompt; some symbols stay boxes until a
        Nerd Font is installed (ohmyposh.dev, **Fonts**). To go back:
        `notepad $PROFILE`, delete the last line, save.

!!! success "You should now see"
    A new terminal whose prompt shows only the folder, and `..` going up one
    folder.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: permission denied: ..` | The alias is missing. `tail -n 2 ~/.zshrc`, then step 2 again |
    | macOS: `(base)` is gone from the prompt | The new `PROMPT` replaced the prompt conda had set; in `~/.zshrc` it comes after conda's lines. conda still works, and `conda activate bikes` adds the name again: `(bikes) bike-project %` |
    | macOS, after Oh My Zsh: `zsh: command not found: conda` | conda's lines stayed in `~/.zshrc.pre-oh-my-zsh`. `~/miniforge3/bin/conda init zsh`, then a new terminal |
    | Windows: `Could not find a part of the path` | The folder line of step 2 was skipped. Run it, then the two `Add-Content` lines |
    | Windows: `… cannot be loaded because running scripts is disabled on this system` when a terminal opens | The profile is a script. Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |
    | A profile path under `OneDrive\Documents` | Correct: OneDrive keeps `Documents` there |

---

## Stretch goals

- The busiest hour at the park, without the broken week. On a Mac,
  `grep ',park,' data/processed/bikes_valid.csv | sort -t, -k3 -n | tail -n 1`:
  `-t,` splits at commas and `-k3` sorts by the third field. In PowerShell,
  `Import-Csv data/processed/bikes_valid.csv | Where-Object counter -eq park | Sort-Object {[double]$_.bikes} | Select-Object -Last 1`.
  Both give 420 bicycles, on 6 September 2024 at 8:00.
- How many hours with no bicycle at all are there at each counter?
  `grep -c ',park,0$' data/raw/bikes.csv` and the same for the bridge:
  1372 and 576.
- Add a third place to `counts.csv` and to the table of the README, predict
  the new size in bytes, and measure it.

## If students ask for more

- `less FILE` on a Mac and `Get-Content FILE | more` in PowerShell show a
  long file one screen at a time: `Space` goes on, `q` leaves.
- `history` lists the commands typed in this terminal, in both shells.
- `Ctrl+R` searches the earlier commands as you type.
- `conda env remove -n bikes` deletes the environment of section 20;
  `conda env create -f environment.yml` makes it again.

## Aims practised

- 🔧 **Tool-agnostic:** the same work in two shells, and in VS Code.
- ♻️ **Reproducible:** a README whose line makes the processed file again,
  a checksum that names the raw file, and (section 20) an `environment.yml`
  from which any laptop makes the same environment.
- ⚙️ **Automation:** typed lines and a program in place of clicks.
- 📁 **Data & files:** a project folder from nothing, a file read byte by
  byte, raw data that is only read, a mark for missing values found and
  removed.
