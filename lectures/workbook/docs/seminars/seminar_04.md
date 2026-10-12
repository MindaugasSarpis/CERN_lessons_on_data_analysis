# Seminar 4 — Work on Files from the Shell

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student builds a project folder with typed
commands, finds the broken week in two years of bicycle counts, writes a
clean copy and a short README, and gets the same checksum as everyone else
in the room.

The tool is the terminal of VS Code: `zsh` on macOS, **PowerShell 7** on
Windows. The room starts from the four commands it knows (`pwd`, `ls`, `cd`,
`clear`); every other command is typed here for the first time, in the order
of Lecture 04.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · The shell, ready** · 14 min | | |
| 0:00 | [1. Start the installs](#installs) | `winget install …`, `git --version`, python.org | Installs running, the Python installer in **Downloads** |
| 0:06 | [2. The terminal of VS Code](#shell) | **Select Default Profile**, the version line | `7` or `/bin/zsh` |
| | **Part 2 · Find your way** · 21 min | | |
| 0:14 | [3. Where you are](#where) | `pwd`, `ls`, `cd`, `Tab`, `↑` | The prompt read aloud, part by part |
| 0:22 | [4. A folder of your own](#folder) | `mkdir` five times | `bike-project` with four folders, open in VS Code |
| 0:28 | [5. The files, moved in](#files) | `mv ~/Downloads/…` | Two data files and two scripts in place |
| | **Part 3 · Look at the files** · 17 min | | |
| 0:35 | [6. Read and count](#count) | `head`, `wc`, `Get-Content`, `Get-Item` | 35 089 lines, 900 314 bytes |
| 0:44 | [7. Copy, rename, delete](#copy) | `cp`, `mv`, `rm`, `*` | A backup made and removed again |
| | **Part 4 · Pipes and filters** · 19 min | | |
| 0:52 | [8. The ends of a column](#sort) | `sort -n`, `Sort-Object` | `9999` at the top: a mark, not a count |
| 1:01 | [9. Count the mark, keep the rest](#grep) | `grep`, `uniq -c`, `Select-String`, `>` | 168 rows, one broken week, `bikes_valid.csv` |
| | **Part 5 · A program, a checksum, the README** · 31 min | | |
| 1:11 | [10. Python, and a program someone else wrote](#python) | The Python installer, `clean_export.py` | `monthly.csv`, 12 rows |
| 1:20 | [11. A mean, with and without the mark](#mean) | `column_stats.py` twice | 86.3 and 38.6 bicycles per hour |
| 1:25 | [12. One checksum in the room](#checksum) | `shasum -a 256`, `Get-FileHash` | `2c68aad2…` and `ea4ce2ce…` on every laptop |
| 1:31 | [13. The README](#readme) | `README.md` and its preview | Columns, the mark, how to rebuild |
| 1:38 | [14. Wrap up](#wrap-up) | `git config`, the list of the day | Git knows each name |
| | **Optional, if the room is fast** | | |
| — | [15. Output into a file, byte by byte](#bytes) | `>`, `>>`, `hexdump -C`, `Format-Hex` | 22 bytes on a Mac, 24 on Windows |
| — | [16. Patterns](#regex) | The `.*` button, `grep -E`, `Select-String` | 12 rows, then 8 lines with four digits |
| — | [17. An environment for the project](#environment) | `python -m venv .venv`, `pip install numpy` | `(.venv)` in the prompt, `requirements.txt` |
| — | [18. A list of checksums](#list) | `shasum -a 256 -c`, `Compare-Object` | `OK` twice, then one digit caught |
| — | [19. Test the README](#readme-test) | Delete, paste, measure | The two files back, the same checksum |

**If time runs short:** leave out the last step of section 9 (text against
number) and section 13 becomes the three lines of **How to rebuild** only;
never cut sections 10 to 12, whose files and numbers are the result of the
day.

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
    **Windows** (PowerShell 7). Where they agree, the line stands once. The
    user on the page is called `ada`; the home folder is `/Users/ada` on a
    Mac and `C:\Users\ada` on Windows. Keys are written for Windows, with
    macOS in brackets.

??? info "Before the session (5 minutes)"
    For the room: a laptop on which the student can install programs, with
    VS Code. Nothing else: the page starts from an empty folder.

    For you:

    - Put the five files of the next box on a USB stick, with the
      installers listed on
      [Install Python, Git and PowerShell 7](install_python_git.md) if the
      network of the room is slow.
    - Skim sections 8 and 9 once: they hold the one surprise of the day,
      the value `9999`. Let the room find it; do not announce it.

??? info "Files for this seminar"
    The files are generated for the course: the city and its two bicycle
    counters are made up, and the counts behave like real ones (rush hours,
    weekends, winter, rain). A browser saves each file in **Downloads**
    under the name in the second column; section 5 moves them into the
    project folder with typed commands.

    | File | Saved as | Moved into | What it is |
    |--|--|--|--|
    | [`bikes_hourly.csv`](../data/bikes_hourly.csv){ download="bikes.csv" } | `bikes.csv` | `data/raw` | Two counters, one row per counter and hour, 2024 and 2025: 35 088 rows, 900 314 bytes |
    | [`bikes_monthly_export.csv`](../data/bikes_monthly_export.csv){ download="monthly_export.csv" } | `monthly_export.csv` | `data/raw` | Bicycles per day on the bridge, each month of 2025, as a spreadsheet exported it: 233 bytes |
    | [`cli_clean_export.py`](../data/cli_clean_export.py){ download="clean_export.py" } | `clean_export.py` | `scripts` | A program that cleans such an export |
    | [`cli_column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" } | `column_stats.py` | `scripts` | A program that prints rows, smallest, largest and mean of one column |
    | [`bikes_project.zip`](../data/bikes_project.zip) | `bikes_project.zip` | unpack it | The finished folder `bike-project`, for a student who lost a step |
    | [`bikes_README.txt`](../data/bikes_README.txt){ download="README.md" } | `README.md` | compare only | The README of section 13 |

    The files were made by [`bikes_files.py`](../data/bikes_files.py).

---

## Part 1 · The shell, ready { #part-1 }

**0:00 to 0:14 · sections 1 and 2**

The slow installs start first. Then every laptop gets the shell of the
course in the terminal of VS Code: `zsh` on a Mac, PowerShell 7 on Windows.
[Install Python, Git and PowerShell 7](install_python_git.md) has the same
installs per system, with every error message, for helpers at a laptop.

---

### 1. Start the installs { #installs }

**0:00 · 6 min**

**Tell the room.** Three programs come today: a shell that is the same on
every Windows laptop, Python, which runs programs, and Git, which is used
next week. When the whole room downloads at once the network is slow, so
everything starts now and runs while we work.

1. Open VS Code. Select **Terminal** > **New Terminal**. A panel opens at
   the bottom with a prompt.

2. Start the shell and Git.

    === "macOS"

        Check which shell the terminal runs:

        ```text
        echo $SHELL
        ```

        ```text
        /bin/zsh
        ```

        Then ask for Git:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. It takes 5 to 15 minutes. If the
        line prints `git version 2.…` instead, Git is already there.

    === "Windows"

        The terminal that opens is Windows PowerShell 5.1, the one built
        into Windows. `winget`, the program that installs other programs,
        comes with it. Install PowerShell 7:

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

        Each ends with `Successfully installed`. Let them run.

3. In the browser, download the Python installer. Do not run it yet:
   section 10 needs it.

    === "macOS"

        Open the address below and select **Download Python 3.14.…**:

        ```text
        python.org/downloads
        ```

    === "Windows"

        Open the address below. Under the newest **Python 3.14** select
        **Download Windows installer (64-bit)**:

        ```text
        python.org/downloads/windows
        ```

!!! success "You should now see"
    On macOS `/bin/zsh` and the developer tools installing. On Windows
    `winget` at work, then `Successfully installed` twice. On both, the
    Python installer in **Downloads**.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `echo $SHELL` prints `/bin/bash`, or Terminal says *The default interactive shell is now zsh* | Type `chsh -s /bin/zsh`, then the laptop's password (nothing shows while typing) and `Enter`. Quit VS Code with `Cmd+Q` and start it again |
    | Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
    | Windows: `winget` is not recognized | Install `PowerShell-7.6.6-win-x64.msi` and Git for Windows from the USB stick, with every default |
    | An installer asks for an administrator password the student does not have | The laptop is managed by the university or an employer. The student pairs with a neighbour today |
    | VS Code runs in the browser (`vscode.dev`) | It has no terminal. The student pairs with a neighbour today |

---

### 2. The terminal of VS Code { #shell }

**0:06 · 8 min**

**Tell the room.** Three words. The **terminal** is the window that shows
text. The **shell** is the program inside it that reads what you type and
runs it: `zsh` on a Mac, PowerShell on Windows. The **prompt** is the line
where the shell waits. Windows has two PowerShells; VS Code is told once
to open the new one, 7.

1. **Windows only**, when `winget` has finished. Press `Ctrl+Shift+P` and
   type:

    ```text
    default profile
    ```

    Select **Terminal: Select Default Profile**, then **PowerShell**. Not
    **Windows PowerShell**: that is 5.1.

2. Close the open terminal with the bin icon at the top right of the
   panel. Select **Terminal** > **New Terminal**. Check the shell:

    === "macOS"

        ```text
        echo $SHELL
        ```

        ```text
        /bin/zsh
        ```

    === "Windows"

        ```text
        $PSVersionTable.PSVersion.Major
        ```

        ```text
        7
        ```

        The name at the top right of the panel reads `pwsh`.

3. Read the prompt aloud, part by part.

    === "macOS"

        ```text
        ada@MacBook-Air ~ %
        ```

        The user, the computer, the folder the shell is in (`~` is the home
        folder), and `%`: the shell waits.

    === "Windows"

        ```text
        PS C:\Users\ada>
        ```

        `PS`, the folder the shell is in, and `>`: the shell waits.

4. Type a first command and read the answer. The shell runs it, prints,
   and shows the prompt again.

    ```text
    echo hello
    ```

    ```text
    hello
    ```

!!! success "You should now see"
    `/bin/zsh` or `7`, the prompt read aloud, and `hello` on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the version line prints `5` | The old terminal is still open, or **Windows PowerShell** was chosen. Step 1 again, then a new terminal. If PowerShell 7 is still installing, go on in 5.1: most lines of today work there too |
    | Windows: **PowerShell** is missing from the list | PowerShell 7 is not installed yet, or VS Code started before it was. Quit VS Code with **File** > **Exit**, start it again, step 1 again |
    | The list offers **Git Bash** | Not in this course. Take **PowerShell** |

---

## Part 2 · Find your way { #part-2 }

**0:14 to 0:35 · sections 3 to 5**

The room moves between folders by typed commands, builds a project folder
of its own, and moves the downloaded files into it.

---

### 3. Where you are { #where }

**0:14 · 8 min**

**Tell the room.** The shell is always in one folder, the **working
directory**. The prompt shows it, `pwd` prints it in full, `ls` lists what
is in it, and `cd` changes it. A path that starts at the top of the disk is
**absolute**; one that starts at the working directory is **relative**.

1. Print the working directory.

    ```text
    pwd
    ```

    === "macOS"

        ```text
        /Users/ada
        ```

    === "Windows"

        ```text
        Path
        ----
        C:\Users\ada
        ```

    An absolute path: from the top of the disk, `/` or `C:\`, down to the
    home folder.

2. List what is in it.

    ```text
    ls
    ```

    The folders of the home folder: `Desktop`, `Documents`, `Downloads` and
    more. PowerShell prints a table; the names are in the column **Name**.

3. Go into **Downloads** with a relative path, and look. Type `cd Dow`,
   then press `Tab`: the shell completes the name.

    ```text
    cd Downloads
    ```

    ```text
    pwd
    ```

    The prompt now shows `Downloads`, and `pwd` ends in `Downloads`.

4. Go back up one level, then check.

    ```text
    cd ..
    ```

    ```text
    pwd
    ```

    `..` is the folder above. `cd ~` goes to the home folder from anywhere.

5. Press `↑` twice: the earlier commands come back, ready to run again.
   Press `Esc` (macOS `Ctrl+C`) to leave the line empty. Then empty the
   panel:

    ```text
    clear
    ```

!!! success "You should now see"
    `pwd` printing the home folder again, and an empty panel with the
    prompt at the top.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `cd: no such file or directory: downloads` | Names are spelled exactly, also the capital `D`. `Tab` spells them right |
    | `Tab` adds nothing | No name starts with what was typed. Check the letters before the `Tab` |
    | Windows: `Tab` writes `.\Downloads\` | PowerShell's spelling of the same path. It works |
    | Windows: the home folder has no **Documents**, only **OneDrive** | Fine: today's folder goes into the home folder itself, not into Documents |

---

### 4. A folder of your own { #folder }

**0:22 · 6 min**

**Tell the room.** `mkdir` makes a folder. Today's project gets the layout
of every project of the course: raw data that is never changed, processed
data that commands make from it, scripts, and results. Five short lines,
the same in both shells. `↑` brings back the last line, so only its end is
retyped.

1. In the home folder, make the project folder and go into it.

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
   `bike-project` in the home folder, **Open**. Then **Terminal** > **New
   Terminal**.

!!! success "You should now see"
    The four folders in the Side Bar of VS Code, and a prompt that ends in
    `bike-project`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `mkdir: data/raw: No such file or directory` | `data` has to exist first. `mkdir data`, then the line again |
    | `mkdir: bike-project: File exists`, or PowerShell: `An item with the specified name … already exists` | The folder is there from an earlier try. `cd bike-project` and go on |
    | A folder named `Data` or `bike project` | Names are small letters with no spaces. Delete it in the Side Bar and make it again |
    | The prompt of the new terminal shows the home folder | VS Code has no folder open. Step 4 again |

---

### 5. The files, moved in { #files }

**0:28 · 7 min**

**Tell the room.** The browser saves into **Downloads**. `mv` moves a file:
first where it is, then where it goes. `~/Downloads/bikes.csv` is the same
path in both shells. Press `Tab` after a few letters of each name: a name
that `Tab` completed has no typing mistake in it.

1. Download the four files of the box **Files for this seminar** at the top
   of this page: `bikes.csv`, `monthly_export.csv`, `clean_export.py`,
   `column_stats.py`. Do not open them.

2. Move them in, one line each.

    ```text
    mv ~/Downloads/bikes.csv data/raw/
    ```

    ```text
    mv ~/Downloads/monthly_export.csv data/raw/
    ```

    ```text
    mv ~/Downloads/clean_export.py scripts/
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
    bikes.csv          monthly_export.csv
    ```

    ```text
    ls scripts
    ```

    ```text
    clean_export.py    column_stats.py
    ```

!!! success "You should now see"
    Two files in `data/raw` and two in `scripts`, in the terminal and in
    the Side Bar.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory`, or PowerShell: `Cannot find path` | The name in **Downloads** differs. `ls ~/Downloads` shows how it is spelled |
    | A file named `bikes (1).csv` | It was downloaded twice. Move it and rename it in one line: `mv ~/Downloads/"bikes (1).csv" data/raw/bikes.csv`. The quotes hold a name with spaces together |
    | The browser opened the file instead of saving it | Go back and right-click the link, **Save Link As...** |

---

## Part 3 · Look at the files { #part-3 }

**0:35 to 0:52 · sections 6 and 7**

The room reads the two data files and measures them, then copies, renames
and deletes, safely, in a folder made for it.

---

### 6. Read and count { #count }

**0:35 · 9 min**

**Tell the room.** A command has parts: the **program** first, then
**options** that say how, then **arguments** that say what to work on.
`head -n 3 data/raw/bikes.csv`: the program `head`, the option `-n 3`, the
argument, a path. The file has thousands of lines; nobody opens it to
count them.

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

3. The small file, whole. `cat` prints a file in both shells.

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

    A spreadsheet with European settings wrote this: `;` between the
    values, a decimal comma, a column `nr`, and the mean at the end.

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

    900 314 bytes over 35 089 lines is about 26 bytes a line: the line
    `2024-01-01T00:00,bridge,2` has 25 characters and one line break.

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
        Get-Content: Cannot find path 'C:\Users\ada\bike-project\data\raw\bike.csv' because it does not exist.
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
    | macOS: the manual page fills the panel | `Space` goes on, `q` leaves |

---

### 7. Copy, rename, delete { #copy }

**0:44 · 8 min**

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
    cp data/raw/monthly_export.csv backup/
    ```

2. Rename the copy with `mv`: first the old name, then the new one.

    ```text
    mv backup/monthly_export.csv backup/export_copy.csv
    ```

3. Copy a whole folder: `-r` copies everything in it.

    ```text
    cp -r data backup/
    ```

    ```text
    ls backup
    ```

    ```text
    data            export_copy.csv
    ```

4. A wildcard: every CSV file in `data/raw`.

    ```text
    ls data/raw/*.csv
    ```

    ```text
    data/raw/bikes.csv              data/raw/monthly_export.csv
    ```

    PowerShell prints the two names in its table.

5. Delete the copy, then the whole backup folder. Say the name aloud before
   pressing `Enter`.

    ```text
    rm backup/export_copy.csv
    ```

    ```text
    rm -r backup
    ```

    ```text
    ls
    ```

    ```text
    data    results scripts
    ```

!!! success "You should now see"
    The project folder as it was: `data`, `results`, `scripts`, with nothing
    lost from `data/raw`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `cp: data is a directory (not copied).` | A folder needs `-r` |
    | Windows: `cp data backup2` made an empty folder `backup2` | Without `-r` PowerShell copies the folder alone, not what is in it. `rm backup2`, then with `-r` |
    | macOS: `rm: backup: is a directory` | A folder needs `rm -r` |
    | Windows: `rm backup` asks *The item at … has children …* | `N` and `Enter`, then `rm -r backup` |
    | Something in `data/raw` was deleted | Move it in again from **Downloads**, or download it again |

---

## Part 4 · Pipes and filters { #part-4 }

**0:52 to 1:11 · sections 8 and 9**

So far each command printed its answer. Now the answer of one command
becomes the input of the next, with `|`, and the last answer goes into a
file, with `>`. The room asks the large file one question: what is the
busiest hour?

---

### 8. The ends of a column { #sort }

**0:52 · 9 min**

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

5. The other end, for completeness.

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

### 9. Count the mark, keep the rest { #grep }

**1:01 · 10 min**

**Tell the room.** `grep` and `Select-String` keep the lines that contain a
text. `,9999$` means: a comma, 9999, and then the end of the line. They can
count those lines, show them, or keep every line *without* them, and `>`
sends the result into a file instead of onto the screen.

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
    hours, 7 × 24 = 168. One broken week.

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
    week has rows; their count is the mark.

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

## Part 5 · A program, a checksum, the README { #part-5 }

**1:11 to 1:42 · sections 10 to 14**

Python arrives and runs two programs someone else wrote. A checksum shows
that a file is the same on every laptop, and the README writes down what
was done, as lines anyone can run again.

---

### 10. Python, and a program someone else wrote { #python }

**1:11 · 9 min**

**Tell the room.** A program is a file. To run a Python program, the shell
needs Python, and finds it in the folders listed in `PATH`. On Windows one
box in the installer adds Python's folder to that list. After the install,
VS Code is restarted, so that its terminal reads the new list.

1. Ask the shell for Python before the install.

    === "macOS"

        ```text
        python3 --version
        ```

        Either `Python 3.9.6`, the copy that came with the developer tools
        of section 1, or, while those are still installing, a note about
        them. Both are fine: the installer below brings its own Python.

    === "Windows"

        ```text
        python --version
        ```

        ```text
        Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
        ```

        A stand-in of Windows answered, not Python.

2. Run the installer that section 1 downloaded.

    === "macOS"

        Open `python-3.14.…-macos11.pkg` in **Downloads** and keep every
        default.

    === "Windows"

        Open `python-3.14.…-amd64.exe` in **Downloads**. On the first
        screen tick **Add python.exe to PATH** at the bottom, then select
        **Install Now**, and **Close** at the end.

3. Quit VS Code with **File** > **Exit** (macOS `Cmd+Q`) and start it again.
   It opens `bike-project`. Open a new terminal and ask again.

    === "macOS"

        ```text
        python3 --version
        ```

    === "Windows"

        ```text
        python --version
        ```

    ```text
    Python 3.14.…
    ```

4. Run the cleaning program on the export: the program, the file to run,
   then two paths for the program: the file it reads and the file it
   writes.

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

5. Look at what it wrote.

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

    Four edits: the mean line is gone, the decimal comma became a point,
    `;` became `,`, and the column `nr` is gone. Open
    `scripts/clean_export.py` in VS Code and find the four in its eight-line
    `clean` function; nobody has to understand the rest today.

!!! success "You should now see"
    `Python 3.14.…`, and `monthly.csv` with 12 rows in `data/processed`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: still `Python was not found` | Either **Add python.exe to PATH** was not ticked (run the installer again, **Modify**, **Next**, tick **Add Python to environment variables**, **Install**) or VS Code was not quit and started again. Never install from the Store. Until it works, `py` runs in place of `python` |
    | macOS: `python3 --version` still prints `Python 3.9.6` | The installer has not finished, or the terminal is old. Quit VS Code with `Cmd+Q` and start it again |
    | macOS: `zsh: command not found: python` | On macOS the program is `python3` |
    | `no file data/raw/monthly_export.csv` | The terminal is not in `bike-project`, or the file is not in `data/raw`. `pwd`, then `ls data/raw` |

---

### 11. A mean, with and without the mark { #mean }

**1:20 · 5 min**

**Tell the room.** A second program prints the number of rows, the
smallest and largest value and the mean of one column. It counts every
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

3. The cleaned export: its mean is the mean line the spreadsheet wrote.

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

!!! success "You should now see"
    86.2712 and 38.5811, and 1182.04, on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `no column per_day … the columns are: nr;month;per_day` | That is the raw export: with `;` between the values, the program sees one column. Give it the cleaned file |
    | `no column Bikes` | Column names are exact: `bikes` |

---

### 12. One checksum in the room { #checksum }

**1:25 · 6 min**

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

2. The file the program wrote.

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

    The same on a Mac and on Windows: the program ends every line with the
    same byte on every system.

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

    Same rows, different checksums. PowerShell on Windows ends each line it
    writes with two bytes, CRLF, where zsh writes one, LF: 34 921 bytes
    more, 930 699 against 895 778. Section 15 shows the two bytes.

!!! success "You should now see"
    `2c68aad2…` and `ea4ce2ce…` on every laptop, and two checksums for
    `bikes_valid.csv`, one per system.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Another checksum for `bikes.csv` | The file is not the downloaded one: it was opened and saved, or the download broke. Download it again |
    | Windows: a table with `Algorithm`, `Hash`, `Path` | The brackets and `.Hash` were left out. The hash is the middle column |

---

### 13. The README { #readme }

**1:31 · 7 min**

**Tell the room.** The README is the first file a stranger opens. It says
what the data is, what each column means, which value marks a missing one,
and how every file in `data/processed` is made again: the lines that ran
today, copied from the terminal, not retyped from memory.

1. In the Side Bar, select **New File** at the top level of `bike-project`
   and name it `README.md`. Open the preview beside it: `Ctrl+K`, then `V`
   (macOS `Cmd+K`, then `V`).

2. Type the first part:

    ```text
    # Bike Counters

    Two bicycle counters of a city, one on a bridge and one on a park path:
    how many bicycles passed in each hour of 2024 and 2025.

    ## Data

    - `data/raw/bikes.csv`: one row per counter and hour, 35 088 rows.
      Generated for the course; the city and its counters are made up.
    - `data/raw/monthly_export.csv`: the mean number of bicycles per day on the
      bridge, for each month of 2025, exported from a spreadsheet.

    ## Columns of `bikes.csv`

    | Column | Meaning | Unit |
    |--|--|--|
    | `time` | start of the hour | YYYY-MM-DDTHH:MM |
    | `counter` | `bridge` or `park` | none |
    | `bikes` | bicycles that passed in that hour | bicycles |

    Missing value: `bikes` is `9999` in 168 rows, the park counter from
    2025-03-10 to 2025-03-16, while it was broken.
    ```

3. Add **How to rebuild**. Copy each command from the terminal: press `↑`
   until it comes back, select it with the mouse, copy, paste. Your shell's
   lines are enough.

    ```text
    ## How to rebuild

    Run in the project folder: zsh on macOS, PowerShell 7 on Windows.

    1. `data/processed/monthly.csv`, 189 bytes, SHA-256 `ea4ce2ce…19396ef6`:
       - zsh: `python3 scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv`
       - PowerShell: `python scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv`
    2. `data/processed/bikes_valid.csv`, `bikes.csv` without the 168 rows marked `9999`:
       - zsh: `grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv`
       - PowerShell: `Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv`
    ```

4. Save with `Ctrl+S` (macOS `Cmd+S`).

!!! success "You should now see"
    In the preview: a title, a table of three columns, the line about
    `9999`, and **How to rebuild** with the size and the checksum of
    `monthly.csv`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as plain text | The line of dashes under the header is missing, or the empty line before the table |
    | The preview does not open | Click into the README first, then `Ctrl+K`, `V` |
    | The checksum in the README was typed by hand | Copy it from the terminal instead: one wrong character and it names another file |

---

### 14. Wrap up { #wrap-up }

**1:38 · 4 min**

**Tell the room.** Git keeps versions of files, from next week on. It
writes a name and an address into every version, so it is told both once,
now. Nothing is printed, which is correct.

1. Check that Git is installed, then tell it who you are, with your own
   name and address.

    ```text
    git --version
    ```

    ```text
    git config --global user.name "Ada Lovelace"
    ```

    ```text
    git config --global user.email "ada@example.com"
    ```

2. Read the list of the day with the room:

    - The shell runs in the terminal; the prompt shows the working
      directory; `pwd`, `ls`, `cd` move around; `Tab` and `↑` save typing.
    - A command is a program, options and arguments. A path is absolute or
      relative.
    - `head`, `tail`, `cat`, `wc`, `cp`, `mv`, `rm`, `mkdir`, `*`.
    - `|` joins filters, `>` writes a file. Sort a column and look at both
      ends.
    - `9999` was a mark, not a count: 168 rows, one broken week, a mean
      more than doubled.
    - A program someone else wrote runs with one line; a checksum shows that
      two files hold the same bytes; the README holds the lines that make
      every processed file again.

!!! success "You should now see"
    `git version 2.…` on every laptop, and the folder `bike-project` with a
    README, two raw files, two processed files and two scripts.

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

### 15. Output into a file, byte by byte { #bytes }

**— · 8 min**

**Tell the room.** `>` makes a file, or empties one that exists, and writes
into it; `>>` adds at its end. Section 12 found that the two shells wrote
the same rows with different bytes. Here are the bytes.

1. Two lines into a note.

    ```text
    echo "counted by me" > results/note.txt
    ```

    ```text
    echo "checked" >> results/note.txt
    ```

    ```text
    cat results/note.txt
    ```

    ```text
    counted by me
    checked
    ```

2. Its size.

    === "macOS"

        ```text
        wc -c results/note.txt
        ```

        ```text
              22 results/note.txt
        ```

    === "Windows"

        ```text
        (Get-Item results/note.txt).Length
        ```

        ```text
        24
        ```

    `counted by me` has 13 characters and `checked` has 7: 20. The Mac adds
    one byte per line, 22. Windows adds two, 24.

3. The bytes themselves.

    === "macOS"

        ```text
        hexdump -C results/note.txt
        ```

        ```text
        00000000  63 6f 75 6e 74 65 64 20  62 79 20 6d 65 0a 63 68  |counted by me.ch|
        00000010  65 63 6b 65 64 0a                                 |ecked.|
        00000016
        ```

    === "Windows"

        ```text
        Format-Hex results/note.txt
        ```

        ```text
           Label: C:\Users\ada\bike-project\results\note.txt

                  Offset Bytes                                           Ascii
                         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
                  ------ ----------------------------------------------- -----
        0000000000000000 63 6F 75 6E 74 65 64 20 62 79 20 6D 65 0D 0A 63 counted by me��c
        0000000000000010 68 65 63 6B 65 64 0D 0A                         hecked��
        ```

    Every character is one byte: `63` is `c`, `20` a space. The line ends
    in `0a` (LF) on the Mac and in `0D 0A` (CRLF) on Windows.

!!! success "You should now see"
    22 or 24 bytes, and the line ends found in the hex view.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The note holds one line | The second line used `>` and emptied the file. Both lines again, `>>` the second time |

---

### 16. Patterns { #regex }

**— · 10 min**

**Tell the room.** A **regular expression** describes a kind of text:
`[0-9]` is any digit, `+` means one or more of what stands before it, `^`
is the start of a line, `{4}` exactly four. The same patterns work in the
Find box of VS Code and in the shell.

1. Open `data/raw/monthly_export.csv`. Press `Ctrl+F` (macOS `Cmd+F`) and
   switch on the button `.*` at the right end of the box. Type the three
   patterns below one after the other, and read the count of matches:

    ```text
    [0-9]+
    ```

    ```text
    [0-9]+;
    ```

    ```text
    ^[0-9]+;
    ```

    62 matches (every number), then 24 (a number before a `;`), then 12:
    the row number at the start of each row.

2. Close the file without saving. The same pattern in the shell, counting
   lines:

    === "macOS"

        ```text
        grep -E -c '^[0-9]+;' data/raw/monthly_export.csv
        ```

    === "Windows"

        ```text
        (Select-String '^[0-9]+;' data/raw/monthly_export.csv).Count
        ```

    ```text
    12
    ```

3. The months with 1000 bicycles a day or more: four digits between `;` and
   the decimal comma.

    === "macOS"

        ```text
        grep -E ';[0-9]{4},' data/raw/monthly_export.csv
        ```

    === "Windows"

        ```text
        Select-String ';[0-9]{4},' data/raw/monthly_export.csv -Raw
        ```

    ```text
    4;2025-04;1360,6
    5;2025-05;1676,5
    6;2025-06;1945,5
    7;2025-07;1927,5
    8;2025-08;1860,8
    9;2025-09;1453,2
    10;2025-10;1187,0
    ;mean;1182,04
    ```

    April to October, and the mean line, which fits the pattern too. A
    pattern finds what it describes, not what was meant.

!!! success "You should now see"
    12 in the Find box and in the shell, then eight lines.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The Find box counts 0 for `[0-9]+` | The `.*` button is off |
    | zsh: `grep -c '^[0-9]+;'` prints 0 | Without `-E`, grep reads `+` as a plain plus sign |
    | The file was changed | Close it without saving. Files in `data/raw` are never edited |

---

### 17. An environment for the project { #environment }

**— · 12 min**

**Tell the room.** `pip` installs Python packages. Installed into the
Python of the laptop, a package is shared by every project, and an upgrade
for one can break another. A **virtual environment** is a Python of the
project's own, in the folder `.venv`. Activating it puts its folder at the
front of `PATH`, so `python` means this one.

1. Where the shell finds Python now.

    === "macOS"

        ```text
        which python3
        ```

        ```text
        /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
        ```

    === "Windows"

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\ada\AppData\Local\Programs\Python\Python314\python.exe
        ```

2. Make the environment and switch it on.

    === "macOS"

        ```text
        python3 -m venv .venv
        ```

        ```text
        source .venv/bin/activate
        ```

        ```text
        which python
        ```

        ```text
        /Users/ada/bike-project/.venv/bin/python
        ```

    === "Windows"

        ```text
        python -m venv .venv
        ```

        ```text
        .venv\Scripts\Activate.ps1
        ```

        ```text
        (Get-Command python).Source
        ```

        ```text
        C:\Users\ada\bike-project\.venv\Scripts\python.exe
        ```

    The prompt now starts with `(.venv)`. From here the line is the same in
    both shells: `python`.

3. The environment is empty. Fill it.

    ```text
    python -m pip list
    ```

    ```text
    Package Version
    ------- -------
    pip     26.2.1
    ```

    ```text
    python -m pip install numpy
    ```

    ```text
    Successfully installed numpy-2.5.4
    ```

    ```text
    python -c "import numpy; print(numpy.__version__)"
    ```

    ```text
    2.5.4
    ```

4. Write the list down, so that another laptop installs the same versions.

    ```text
    python -m pip freeze > requirements.txt
    ```

    ```text
    cat requirements.txt
    ```

    ```text
    numpy==2.5.4
    ```

5. Switch it off.

    ```text
    deactivate
    ```

!!! success "You should now see"
    `(.venv)` in the prompt while it was on, and `requirements.txt` with one
    line. On another laptop, three lines make the same environment: make
    `.venv`, activate it, `python -m pip install -r requirements.txt`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `… cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1. Switch to PowerShell 7 (section 2), or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |
    | Other version numbers | A newer pip or numpy was released. Fine |
    | `.venv` shows in the Side Bar with many files | Correct. It is made again from `requirements.txt` and never edited by hand |

---

### 18. A list of checksums { #list }

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
        data/raw/monthly_export.csv: OK
        ```

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
    `data/raw/monthly_export.csv` inside `bike-copy` in the home folder,
    change `312,2` to `312,3`, save and close it.

4. Test the copy.

    === "macOS"

        ```text
        shasum -a 256 -c data/checksums.txt
        ```

        ```text
        data/raw/bikes.csv: OK
        data/raw/monthly_export.csv: FAILED
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
        F160398B59D8590C513D04D14EE517E2641B4DFAC5F7C748C61AAD98B1FADBA8 =>
        29C90DBD687848423E35817747F4858ADD6D748118C7F52D07CD3A836E9901DE <=
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
    `OK` twice for the project, and the one changed file caught in the
    copy.

---

### 19. Test the README { #readme-test }

**— · 6 min**

**Tell the room.** A README is tested the way a stranger would use it:
delete what it says can be made again, run its lines, and measure.

1. Delete the two processed files.

    ```text
    rm data/processed/monthly.csv
    ```

    ```text
    rm data/processed/bikes_valid.csv
    ```

2. Open the preview of `README.md`, copy the two lines of your shell from
   **How to rebuild** and paste them into the terminal, one at a time.

3. Measure.

    === "macOS"

        ```text
        shasum -a 256 data/processed/monthly.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/monthly.csv).Hash
        ```

    The checksum in the README: `ea4ce2ce…19396ef6`.

!!! success "You should now see"
    Both files back in `data/processed`, and the checksum the README
    promises.

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
- Write a second line into **How to rebuild** for the busiest hour of
  section 9, and test it.

## If students ask for more

- `less FILE` on a Mac and `Get-Content FILE | more` in PowerShell show a
  long file one screen at a time: `Space` goes on, `q` leaves.
- `history` lists the commands typed in this terminal, in both shells.
- `Ctrl+R` searches the earlier commands as you type.

## Aims practised

- 🔧 **Tool-agnostic:** the same work in two shells, and in VS Code.
- ♻️ **Reproducible:** a README whose lines make every processed file
  again, checked by a checksum.
- ⚙️ **Automation:** typed lines and two programs in place of clicks.
- 📁 **Data & files:** a project folder, raw data that is only read, a mark
  for missing values found and removed.
