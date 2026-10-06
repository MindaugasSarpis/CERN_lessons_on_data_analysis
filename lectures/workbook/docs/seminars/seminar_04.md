# Seminar 4 — Work on Files from the Shell

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every laptop has Python and Git, and every student
measures, searches and cleans the project's files by typed commands, and
ends with the same checksum for the cleaned table as everyone else in the
room, written into the README.

The tool is the terminal of VS Code: `zsh` on macOS, **PowerShell 7** on
Windows, side by side as on the slides of Lecture 04. Windows laptops install
PowerShell 7 in the first minutes. Python runs two handed-out scripts, and
Git is only told a name today.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Tools in place** · 25 min | | |
| 0:00 | [1. Start the downloads](#downloads) | `winget install …`, `git --version`, python.org | Three downloads running |
| 0:05 | [2. Bring the folder up to date](#folder) | The Side Bar against the list of files | Every file of the list, and the line **Cleaned copy** in the README |
| 0:12 | [3. Install Python and Git](#install) | The two installers, then VS Code restarted | Both installed |
| 0:19 | [4. PowerShell 7, and a first script](#shell) | **Select Default Profile**, `$PSVersionTable.PSVersion.Major` | `7`, two version lines, `ready` |
| | **Part 2 · The shell, named** · 10 min | | |
| 0:25 | [5. Name what you type](#terms) | The slide *Read the Prompt*, `pwd` | Prompt, program, option, argument, path named |
| | **Part 3 · A file as bytes, by command** · 20 min | | |
| 0:35 | [6. Count the bytes of a text](#bytes) | `wc -c`, `(Get-Item bytes.txt).Length`, the hex view | 3, 5, then 6 or 7 bytes, and `E0` |
| 0:49 | [7. The data file in bytes](#sizes) | `wc -c`, `wc -l` on `D0_KPi.csv` | 43 bytes per line, line 2 = 42 characters and one line break |
| | **Part 4 · The data file by command** · 30 min | | |
| 0:55 | [8. Three questions](#count) | The slide *Three Questions, Clicked and Typed* | 91 584, line 5000, 49 |
| 1:03 | [9. The ends of a column, and repeats](#sort) | `sort -n`, `uniq -c`, `Group-Object` | The four far masses, and the mark `-100.0` |
| 1:15 | [10. Keep lines: `D0_valid.csv`](#grep) | `grep -v`, `Select-String -NotMatch` | 91 535 lines, 3 924 368 or 4 015 903 bytes |
| | **Part 5 · A program, a checksum, the README** · 30 min | | |
| 1:25 | [11. Run a program someone else wrote](#script) | `clean_pendulum.py` | 9 rows, 97 bytes |
| 1:31 | [12. One checksum in the room](#checksum) | `shasum -a 256`, `Get-FileHash` | `fff0870b` on every laptop |
| 1:40 | [13. A list of checksums, and a mean](#list) | `data/checksums.txt`, `column_stats.py` | `OK` twice, two means |
| 1:47 | [14. Write it into the README](#readme) | `README.md` and its preview | Size and SHA-256, **How to rebuild** |
| 1:55 | [15. Wrap up](#wrap-up) | The list of what was learned | |
| | **Optional, if the room is fast** | | |
| — | [16. Regex in the Find box](#regex) | `Ctrl+H`, the button `.*` | The raw table cleaned again, `be05af03…` |
| — | [17. The same patterns in the shell](#grep-e) | `grep -E`, `Select-String` | Four far rows by line number |
| — | [18. Complete the README](#readme-more) | Columns and units, licence, the test | The README a stranger can use |

**If time runs short:** leave out steps 8 and 9 of section 6, and in
section 9 do only the low end of the mass column; never cut section 7,
which Seminar 6 refers back to, or sections 11 to 14, whose files Seminar 5
starts from.

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
    **Windows** (PowerShell 7). The outputs were printed by `zsh` and by
    PowerShell 7.6 on Windows, in a folder at
    `C:\Users\ada\Documents\analysis-project`. Dates, times and the user
    name differ on every laptop. Keys are written for Windows, with macOS in
    brackets.

??? info "Before the session"
    For the room: a laptop on which the student can install programs, and
    the project folder `analysis-project` in whatever state it is.
    Section 2 brings every folder to the same state.

    In 2026 the room comes in with less than the lecture assumed. Seminar 3
    ran as two hours of `pwd`, `ls`, `cd` and `clear` in the terminal VS Code
    opened, Windows PowerShell 5.1 on Windows, with nothing named and no byte
    work. Part 3 of Seminar 1, the cleaning of the pendulum table, was not
    done with the room, so many folders lack `data/processed/pendulum.csv`,
    `results` and the README line **Cleaned copy** that Lecture 04 opens
    on. Python and Git are on almost no laptop.

    For you:

    - The page done once on a Mac and once on a Windows laptop with
      PowerShell 7.
    - A USB stick with the installers, as listed on
      [Install Python, Git and PowerShell 7](install_python_git.md), and the
      files of the next box.
    - The lecture slides *Read the Prompt*, *Three Questions, Clicked and
      Typed* and *Which Copy? The README Says* ready to put on the
      projector.

??? info "Files for this seminar"
    A browser saves each file under the name in the second column. Drag it
    from **Downloads** onto the folder in the third.

    | File | Saved as | Goes into | What it is |
    |--|--|--|--|
    | [`project_after_s1.zip`](../data/project_after_s1.zip) | `project_after_s1.zip` | unpack it | The whole `analysis-project` folder, for a student whose folder lacks many files |
    | [`D0_KPi.csv`](../data/D0_KPi.csv){ download="D0_KPi.csv" } | `D0_KPi.csv` | `data/raw` | The LHCb file, 3 926 142 bytes |
    | [`pendulum_raw.csv`](../data/pendulum_raw.csv){ download="pendulum.csv" } | `pendulum.csv` | `data/raw` | The pendulum table as the lab partner sent it, 130 bytes |
    | [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | `data/processed` | The cleaned table, 97 bytes |
    | [`cli_clean_pendulum.py`](../data/cli_clean_pendulum.py){ download="clean_pendulum.py" } | `clean_pendulum.py` | `scripts` | Section 11: the four hand edits of Lecture 2, as a program |
    | [`cli_column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" } | `column_stats.py` | `scripts` | Section 13: rows, smallest, largest and mean of one column |
    | [`pendulum_report.txt`](../data/pendulum_report.txt){ download="report.md" } | `report.md` | `results` | The short report of Seminar 1. Seminar 5 edits it |
    | [`pendulum_plot.png`](../data/pendulum_plot.png){ download="pendulum_plot.png" } | `pendulum_plot.png` | `results` | The plot the report shows |
    | [`project_README_s1.txt`](../data/project_README_s1.txt){ download="README.md" } | `README.md` | compare only | The README of Seminar 1, with the line **Cleaned copy** at the end |
    | [`bytes_utf8.txt`](../data/bytes_utf8.txt){ download="bytes.txt" } | `bytes.txt` | compare only | Section 6: `abcą` and LF in UTF-8, 6 bytes |
    | [`bytes_1257.txt`](../data/bytes_1257.txt){ download="bytes_1257.txt" } | `bytes_1257.txt` | compare only | Section 6: the same text saved as Windows 1257, 5 bytes |
    | [`pendulum_crlf.csv`](../data/pendulum_crlf.csv){ download="pendulum_crlf.csv" } | `pendulum_crlf.csv` | compare only | Section 12: copy C of the lecture, CRLF, 107 bytes |

---

## Part 1 · Tools in place { #part-1 }

**0:00 to 0:25 · sections 1 to 4**

The slow downloads start first. While they run, the room brings its project
folder to the state Lecture 04 assumed. Then the programs are installed,
and every laptop ends the part with the same shell on its system and a
script that prints `ready`.
[Install Python, Git and PowerShell 7](install_python_git.md) has the same
steps per system, with every error message, for helpers at a laptop.

---

### 1. Start the downloads { #downloads }

**0:00 · 5 min**

**Tell the room.** Today every laptop gets the tools of the course: a
shell that is the same on every Windows laptop, Python, which runs programs,
and Git, which keeps versions from next week on. Downloads are slow when
the whole room downloads at once, so all of them start now.

1. Open VS Code on the project folder and select **Terminal** > **New
   Terminal**.

    === "macOS"

        Type:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. This takes 5 to 15 minutes. If
        the line prints `git version 2.…` instead, Git is already there.

    === "Windows"

        The terminal is Windows PowerShell 5.1, as in Seminar 3. Type:

        ```text
        winget install --id Microsoft.PowerShell --source winget
        ```

        `winget` downloads PowerShell 7 and installs it. It ends with
        `Successfully installed`. Let it run.

2. Start the browser downloads.

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

        Then open the address below and select **Download for Windows**, then
        the 64-bit **Git for Windows Setup**:

        ```text
        git-scm.com
        ```

!!! success "You should now see"
    On macOS the developer tools installing, and the Python installer in
    **Downloads**. On Windows `winget` at work in the terminal, and two
    installers downloading.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A download stalls | Copy the installer from the USB stick |
    | Windows: `winget` is not recognized, or ends in an error | Install `PowerShell-7.6.6-win-x64.msi` from the USB stick in section 3, with every default |
    | Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
    | An installer asks for an administrator password | The laptop is managed by the university or an employer. The student pairs with a neighbour today |
    | VS Code runs in the browser (`vscode.dev`) | The browser version has no terminal. The student pairs with a neighbour today |

---

### 2. Bring the folder up to date { #folder }

**0:05 · 7 min**

**Tell the room.** Lecture 04 started from a project folder with the raw
files, the cleaned table, and a README line that lists the four edits made
by hand. Many folders lack some of it. While the downloads run, every
folder gets the same files.

1. Compare the Side Bar with this list. Folder names are small letters.

    ```text
    analysis-project/
    ├─ README.md
    ├─ data/
    │  ├─ raw/         D0_KPi.csv  pendulum.csv
    │  └─ processed/   pendulum.csv
    ├─ scripts/        clean_pendulum.py  column_stats.py
    └─ results/        report.md  pendulum_plot.png
    ```

2. A folder that lacks most of it, or a student who was not in Seminar 1:
   download [`project_after_s1.zip`](../data/project_after_s1.zip), unpack
   it, and open the unpacked `analysis-project` with **File** > **Open
   Folder...**. It has everything but the two scripts.

3. A folder that lacks a single file: download it from the box **Files for
   this seminar** at the top of this page and drag it from **Downloads**
   onto its folder in the Side Bar. A missing folder is made with the
   **New Folder** icon of the Side Bar.

4. Everyone: download the two scripts into `scripts`. Do not open them yet.
   [`clean_pendulum.py`](../data/cli_clean_pendulum.py){ download="clean_pendulum.py" }
   and [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }.

5. Open `README.md`. The section **Data** ends with the line below. If it is
   missing, type it at the end of the section, and save.

    ```text
    - **Cleaned copy:** `data/processed/pendulum.csv`. Mean line deleted,
      `,` replaced by `.`, `;` replaced by `,`, column `nr` deleted
    ```

!!! success "You should now see"
    The tree of step 1 in the Side Bar, and the line **Cleaned copy** in the
    README, on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Folders named `Data`, `Results`, or a folder `Project` | Rename them with `F2` (macOS `Enter`) to the names of step 1. Move the files into `raw` and `processed` by dragging |
    | A file named `pendulum (1).csv` or `column_stats (1).py` | It was downloaded twice. Delete the copy and rename the file |
    | The zip opens as a folder inside **Downloads** | Unpack it first: Windows **Extract All...**, macOS double-click. Then open the unpacked `analysis-project` |
    | `D0_KPi.csv` was opened in Excel or Numbers and saved | It is no longer the file that was downloaded. Download it again |

---

### 3. Install Python and Git { #install }

**0:12 · 7 min**

**Tell the room.** An installer copies a program onto the disk and tells
the system where it is. That second part matters: the terminal finds a
program only in the folders listed in `PATH`, as Lecture 04 showed with
`Python was not found`. On Windows one box in the Python installer adds
Python to that list.

1. Install Python.

    === "macOS"

        Run the downloaded `python-3.14.…-macos11.pkg` and keep every
        default. Close the Finder window that opens at the end.

    === "Windows"

        Run `python-3.14.…-amd64.exe`. On the first screen tick **Add
        python.exe to PATH** at the bottom, then select **Install Now**, and
        **Close** at the end.

2. Install Git.

    === "macOS"

        Wait until the developer tools of section 1 have finished.

    === "Windows"

        Run `Git-2.…-64-bit.exe`. Keep every default: **Next** on each
        screen, then **Install** and **Finish**. If `winget` failed in
        section 1, install `PowerShell-7.6.6-win-x64.msi` from the USB stick
        now, with every default.

3. Close VS Code completely with **File** > **Exit** (macOS `Cmd+Q`) and start it
   again, so that it finds the new programs. It opens `analysis-project`
   again.

!!! success "You should now see"
    VS Code open on `analysis-project` after a restart, on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: **Add python.exe to PATH** was not ticked | Run the installer again, select **Modify**, **Next**, tick **Add Python to environment variables**, **Install** |
    | macOS: the developer tools take longer than 15 minutes | Go on with section 4 without `git --version`, and check it at the next break |

---

### 4. PowerShell 7, and a first script { #shell }

**0:19 · 6 min**

**Tell the room.** Windows has two PowerShells. Windows PowerShell 5.1 is
built in and was the terminal of Seminar 3. PowerShell 7 is the newer one,
the shell of the slides, and it runs on macOS and Linux as well. VS Code is
told once to open PowerShell 7. On macOS nothing changes: the shell is `zsh`.

1. **Windows only.** Press `Ctrl+Shift+P` and type:

    ```text
    default profile
    ```

    Select **Terminal: Select Default Profile**, then **PowerShell**. Not
    **Windows PowerShell**: that is 5.1.

2. Close the open terminal with the bin icon at the top right of the Panel,
   then select **Terminal** > **New Terminal**. Check the shell.

    === "macOS"

        ```text
        echo $ZSH_VERSION
        ```

        ```text
        5.9
        ```

    === "Windows"

        ```text
        $PSVersionTable.PSVersion.Major
        ```

        ```text
        7
        ```

        The name at the top right of the Panel reads `pwsh`.

3. Check Python and Git. Each prints one line: `Python 3.14.…` and
   `git version 2.…`.

    === "macOS"

        ```text
        python3 --version
        ```

        ```text
        git --version
        ```

    === "Windows"

        ```text
        python --version
        ```

        ```text
        git --version
        ```

4. Tell Git who you are, once per computer, with your own name and address.
   Seminar 5 needs both. Nothing is printed, which is correct.

    ```text
    git config --global user.name "Ada Lovelace"
    ```

    ```text
    git config --global user.email "ada@example.com"
    ```

5. In the Side Bar select the `scripts` folder, then **New File**, and name
   it `hello.py`. Type one line into it and save:

    ```text
    print("ready")
    ```

6. Run it.

    === "macOS"

        ```text
        python3 scripts/hello.py
        ```

    === "Windows"

        ```text
        python scripts/hello.py
        ```

    ```text
    ready
    ```

!!! success "You should now see"
    `5.9` or `7`, two version lines, and `ready`, on every laptop, in a
    terminal whose prompt shows the project folder.

From here on the terminal stays in the project folder. Every path on this
page starts there.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.` | A stand-in of Windows answered, not Python. Either Python is not installed, or PATH was not ticked (section 3, Watch for), or VS Code was not restarted. Never install from the Store. If it stays after all three: **Settings** > **Apps** > **Advanced app settings** > **App execution aliases**, switch off **App Installer** `python.exe` and `python3.exe`, restart VS Code. Until then `py` works in place of `python` |
    | Windows: the version check prints `5` | The old terminal is still open, or the wrong profile was chosen. Step 1 again: the right PowerShell is the one whose version check prints `7`. Close the terminal with the bin icon and open a new one |
    | Windows: **PowerShell** is missing from the list, or opens 5.1 | PowerShell 7 is not installed yet. Install the MSI from the USB stick, restart VS Code. Until then the student follows the PowerShell tab in 5.1: most commands work, and the page says where 5.1 differs |
    | `The term 'git' is not recognized`, or `python` the same | VS Code was open during the installation. Close it with **File** > **Exit** (macOS `Cmd+Q`) and start it again |
    | macOS: `zsh: command not found: python` | On macOS the program is `python3`, as in the macOS tab |
    | macOS: `python3 --version` prints `Python 3.9.6` | That is the Python of Apple's developer tools. The python.org installer has not run yet. Run it, then restart VS Code |
    | The prompt shows another folder than `analysis-project` | VS Code has a single file open. **File** > **Open Folder...** |
    | The list offers **Git Bash** | Not in this course. Take **PowerShell** |

---

## Part 2 · The shell, named { #part-2 }

**0:25 to 0:35 · section 5**

In Seminar 3 the room typed `pwd`, `ls`, `cd` and `clear` without names for
what it saw. Lecture 04 gave the names. The room types the same commands
again and names every part.

---

### 5. Name what you type { #terms }

**0:25 · 10 min**

**Tell the room.** The **terminal** is the window in the Panel. The
**shell** is the program in it that reads a line: `zsh` or PowerShell. The
**prompt** is what the shell writes when it waits. A **command** is a
**program**, then its **options**, which PowerShell calls **parameters**,
then its **arguments**: what to work on.

1. Put the slide *Read the Prompt* on the projector. Read your own prompt
   with the room, part by part.

    === "macOS"

        ```text
        ada@MacBook-Air analysis-project %
        ```

    === "Windows"

        ```text
        PS C:\Users\ada\Documents\analysis-project>
        ```

    | Part | Name | What it is |
    |--|--|--|
    | `ada@MacBook-Air` | user and computer | Written by `zsh`. PowerShell writes `PS` and no name |
    | `analysis-project`, or `C:\Users\…\analysis-project` | working directory | The folder the shell is in. `zsh` shows its last name, PowerShell the whole path |
    | `%` or `>` | the mark | The shell waits. Nobody types it |

2. Print the working directory as an **absolute path**, from the top of the
   disk down. The command is the same word in both shells.

    ```text
    pwd
    ```

    === "macOS"

        ```text
        /Users/ada/Documents/analysis-project
        ```

    === "Windows"

        ```text
        Path
        ----
        C:\Users\ada\Documents\analysis-project
        ```

    Every laptop prints another path: the user name differs.

3. Run a command with an option and an argument, and name its three parts.
   Put the slide *The Parts of a Command* on the projector.

    === "macOS"

        ```text
        head -n 2 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        Get-Content -Head 2 data/raw/D0_KPi.csv
        ```

    ```text
    M,PT,TAU,IPCHI2
    1880.649,3000.9534,0.00041271152,1299.1675
    ```

    | Part | macOS | Windows | Name |
    |--|--|--|--|
    | First word | `head` | `Get-Content` | program |
    | How to work | `-n 2` | `-Head 2` | option, in PowerShell a parameter |
    | What to work on | `data/raw/D0_KPi.csv` | `data/raw/D0_KPi.csv` | argument, a **relative path** |

4. Use a relative path from another folder. `..` is the folder above.
   These three lines are the same in both shells.

    ```text
    cd scripts
    ```

    ```text
    ls ../data/raw
    ```

    ```text
    cd ..
    ```

    === "macOS"

        ```text
        D0_KPi.csv	pendulum.csv
        ```

    === "Windows"

        ```text
            Directory: C:\Users\ada\Documents\analysis-project\data\raw

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        -a---          2026-10-06 11:07 PM        3926142 D0_KPi.csv
        -a---          2026-10-06 11:07 PM            130 pendulum.csv
        ```

        PowerShell's `ls` is a short name for `Get-ChildItem`, and it
        prints the size of each file in bytes.

5. Ask where `ls` comes from. Empty the Panel afterwards with `clear`, or
   `Ctrl+L`: nothing is deleted.

    === "macOS"

        ```text
        which ls cat cd
        ```

        ```text
        /bin/ls
        /bin/cat
        cd: shell built-in command
        ```

    === "Windows"

        ```text
        Get-Alias ls, cat, cd | Select-Object Name, Definition
        ```

        ```text
        Name Definition
        ---- ----------
        ls   Get-ChildItem
        cat  Get-Content
        cd   Set-Location
        ```

        The line of the slide *Terminal, Shell, Program*. `|` hands the
        answer to `Select-Object`, which keeps two columns.

!!! success "You should now see"
    `pwd` back in the project folder, and the room can name the parts of a
    prompt and of a command.

**Say it in these words.** A path that starts at the project folder, such
as `data/raw/D0_KPi.csv`, works on every laptop and in both shells. A path
that starts with `/Users/ada` or `C:\Users\ada` works on one.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `head: The term 'head' is not recognized as a name of a cmdlet, function, script file, or executable program.` | The macOS line was typed in PowerShell. Take the Windows tab |
    | macOS: `zsh: command not found: Get-Content` | The Windows line was typed in `zsh`. Take the macOS tab |
    | `cd: no such file or directory: scripts`, or `Set-Location: Cannot find path` | The terminal is not in the project folder. `pwd`, then `cd` into it |

---

## Part 3 · A file as bytes, by command { #part-3 }

**0:35 to 0:55 · sections 6 and 7**

The byte part of Seminar 3, now measured with the commands of Lecture 04:
`wc -c` and `Length` count the bytes of a file, `hexdump -C` and
`Format-Hex` show them.

??? note "Autumn 2026"
    This part is here because Seminar 3 of 2026 ran as a terminal session,
    and its byte part was not done. A year whose Seminar 3 covered the bytes
    in the Hex Editor skips Part 3 and gives its 20 minutes to the optional
    sections.

---

### 6. Count the bytes of a text { #bytes }

**0:35 · 14 min**

**Tell the room.** A file is a sequence of bytes. For plain English text one
character is one byte. Other letters take more, and a line break is a byte
too. Before each measurement, the room predicts the number. Lecture 3 gave
the reasons. Today a command measures them.

1. In the Side Bar select the empty area below the folders, then
   **New File**, and name it:

    ```text
    bytes.txt
    ```

2. Type into the file, without pressing Enter, and save with `Ctrl+S`
   (macOS `Cmd+S`):

    ```text
    abc
    ```

3. Count its bytes.

    === "macOS"

        ```text
        wc -c bytes.txt
        ```

        ```text
               3 bytes.txt
        ```

    === "Windows"

        ```text
        (Get-Item bytes.txt).Length
        ```

        ```text
        3
        ```

4. Show the bytes, two hex digits for each.

    === "macOS"

        ```text
        hexdump -C bytes.txt
        ```

        ```text
        00000000  61 62 63                                          |abc|
        00000003
        ```

    === "Windows"

        ```text
        Format-Hex bytes.txt
        ```

        ```text
           Label: C:\Users\ada\Documents\analysis-project\bytes.txt

                  Offset Bytes                                           Ascii
                         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
                  ------ ----------------------------------------------- -----
        0000000000000000 61 62 63                                        abc
        ```

    On the left the position of the first byte in the line, in the middle
    the bytes, on the right the same bytes as characters. Find `a` in the
    ASCII table of Lecture 3: 97, which is `61` in hex.

5. Add `ą` after the `c` and save. Ask the room for the number, then press
   `↑` to run both commands again: 5 bytes.

    === "macOS"

        ```text
        00000000  61 62 63 c4 85                                    |abc..|
        00000005
        ```

    === "Windows"

        ```text
        0000000000000000 61 62 63 C4 85                                  abcÄ�
        ```

    `ą` takes two bytes in UTF-8: `C4 85`. The right-hand column cannot
    show them as one letter.

6. Press Enter at the end of the line and save. Run both commands again,
   and ask who has 6 bytes and who has 7.

    === "macOS"

        ```text
        00000000  61 62 63 c4 85 0a                                 |abc...|
        00000006
        ```

    === "Windows"

        ```text
        0000000000000000 61 62 63 C4 85 0D 0A                            abcÄ���
        ```

7. Look at the right end of the Status Bar. It reads `LF` on macOS and
   `CRLF` on Windows: the line break `0A`, or `0D 0A`. Select it, choose
   **LF**, save, and measure again. Every laptop now has 6 bytes,
   `61 62 63 C4 85 0A`.

8. Read the same bytes with another table. Select `UTF-8` in the Status
   Bar, then **Reopen with Encoding**, and type:

    ```text
    1257
    ```

    Choose **Baltic (Windows 1257)**. The file reads `abcÄ…`. Measure
    again: still 6 bytes. Then **Reopen with Encoding**, **UTF-8**: `abcą`
    again.

9. Now change the bytes. Select `UTF-8`, then **Save with Encoding**,
   **Baltic (Windows 1257)**. Measure again: 5 bytes.

    === "macOS"

        ```text
        00000000  61 62 63 e0 0a                                    |abc..|
        00000005
        ```

    === "Windows"

        ```text
        0000000000000000 61 62 63 E0 0A                                  abcà�
        ```

    In that table `ą` is the single byte `E0`.

10. Delete the scratch file. `rm` is the same word in both shells, and
    prints nothing when it works.

    ```text
    rm bytes.txt
    ```

!!! success "You should now see"
    The same table on every laptop, and no `bytes.txt` in the Side Bar.

    | Text in the file | Bytes | Reason |
    |--|--|--|
    | `abc` | 3 | One byte for each of these letters |
    | `abcą` | 5 | `ą` takes two bytes in UTF-8 |
    | `abcą` and a line break | 6 or 7 | LF is one byte, CRLF is two |
    | `abcą` and LF, saved as Windows 1257 | 5 | `ą` is one byte, `E0`, in that table |

**Say it in these words.** Reopen reads the same bytes with another table
and is safe. Save writes other bytes. A file that shows `Ä…` was read with
the wrong table: it is reopened, not retyped.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The number does not change | The file was not saved. A dot on the tab means *not saved* |
    | One byte more than expected | A space or an extra line break. Look for `20` or a second `0A` in the hex view |
    | `No such file or directory`, or `Cannot find path` | `bytes.txt` was made inside a folder. Drag it onto the empty area below the folders |
    | Windows: `Format-Hex` prints `Path:` and no `Label:` | The terminal is Windows PowerShell 5.1. The bytes are the same. Section 4, step 1 |

---

### 7. The data file in bytes { #sizes }

**0:49 · 6 min**

**Tell the room.** `D0_KPi.csv` cannot be counted by hand, and it does not
need to be. Its size and its number of lines give the bytes per line, and
one line checks the result.

1. Count the bytes and the lines.

    === "macOS"

        ```text
        wc -c data/raw/D0_KPi.csv
        ```

        ```text
         3926142 data/raw/D0_KPi.csv
        ```

        ```text
        wc -l data/raw/D0_KPi.csv
        ```

        ```text
           91584 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/raw/D0_KPi.csv).Length
        ```

        ```text
        3926142
        ```

        ```text
        (Get-Content data/raw/D0_KPi.csv).Count
        ```

        ```text
        91584
        ```

2. Divide on the board: 3 926 142 / 91 584 is about 43 bytes per line.

3. Check it on line 2.

    === "macOS"

        ```text
        head -n 2 data/raw/D0_KPi.csv | tail -n 1 | wc -c
        ```

        ```text
              43
        ```

        43 bytes: 42 characters and the line break, which `wc -c` counts.

    === "Windows"

        ```text
        (Get-Content data/raw/D0_KPi.csv -Head 2)[1].Length
        ```

        ```text
        42
        ```

        42 characters. `Get-Content` drops the line break, so the line on
        disk has 43 bytes. `[1]` is line 2: PowerShell counts from 0.

    ```text
    1880.649,3000.9534,0.00041271152,1299.1675
    ```

!!! success "You should now see"
    Three numbers on the board: 3 926 142 bytes, 91 584 lines, about 43
    bytes per line, and line 2 as 42 characters and one line break.

The file is UTF-8 with LF line breaks, as the Status Bar of VS Code shows
for it, so every character is one byte and every line break one more.

!!! warning "Watch for"
    The size is not 3 926 142, or the Status Bar reads `CRLF` for this file.
    It was opened and saved by another program, and it is no longer the file
    that was downloaded. Download it again.

---

## Part 4 · The data file by command { #part-4 }

**0:55 to 1:25 · sections 8 to 10**

The room asks `D0_KPi.csv` the questions of Lecture 04, each with one typed
line. A line that joins programs with `|`, the pipe, is built stage by
stage: run it, read the output, press `↑`, add the next stage.

---

### 8. Three questions { #count }

**0:55 · 8 min**

**Tell the room.** Lecture 04 opened with three questions that VS Code
answers with clicks. A typed line answers them too, and the line can be
kept. Put the slide *Three Questions, Clicked and Typed* on the projector.

1. How many lines?

    === "macOS"

        ```text
        wc -l data/raw/D0_KPi.csv
        ```

        ```text
           91584 data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        (Get-Content data/raw/D0_KPi.csv).Count
        ```

        ```text
        91584
        ```

2. What is on line 5000? On macOS the first program hands 5000 lines to the
   second, which keeps the last. PowerShell counts lines from 0, so line
   5000 is number 4999.

    === "macOS"

        ```text
        head -n 5000 data/raw/D0_KPi.csv | tail -n 1
        ```

    === "Windows"

        ```text
        (Get-Content data/raw/D0_KPi.csv)[4999]
        ```

    ```text
    1868.8636,5537.248,0.0007151779,10.399748
    ```

3. How many rows have `-100`? The text stands in single quotes, with the
   comma in front.

    === "macOS"

        ```text
        grep -c ',-100' data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        (Select-String ',-100' data/raw/D0_KPi.csv).Count
        ```

    ```text
    49
    ```

4. Check one answer in VS Code: open the file, press `Ctrl+G` (the same
   keys on macOS) and type:

    ```text
    5000
    ```

    The cursor stands on the same line.

!!! success "You should now see"
    91 584, the line that begins with `1868.8636`, and 49, on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: the terminal waits and prints nothing | The text was typed as `-100` without the comma, and `grep` took it for an option. Press `Ctrl+C` |
    | Windows: line 5000 begins with another number | `[5000]` was typed. PowerShell counts from 0: `[4999]` |

---

### 9. The ends of a column, and repeats { #sort }

**1:03 · 12 min**

**Tell the room.** A wrong value usually sits at an end of a sorted column.
A measured value almost never occurs twice, so a value that occurs many
times is a mark. These are the first two checks of a new data file.

1. The low end of the mass column `M`: the header off, the column kept,
   ordered as numbers, the first two taken.

    === "macOS"

        ```text
        tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | sort -n | head -n 2
        ```

    === "Windows"

        ```text
        Import-Csv data/raw/D0_KPi.csv | Select-Object -ExpandProperty M | Sort-Object {[double]$_} | Select-Object -First 2
        ```

    ```text
    1766.2096
    1808.1385
    ```

2. Press `↑` and take the high end: `tail -n 2` in place of `head -n 2`, or
   `-Last 2` in place of `-First 2`.

    ```text
    1920.3453
    2453.6584
    ```

    The second value from each end lies much closer in than the first: one
    row at each end is far from all the others.

3. Count the repeats in the decay time `TAU`, field 3, and show the three
   most frequent values.

    === "macOS"

        ```text
        cut -d, -f3 data/raw/D0_KPi.csv | sort | uniq -c | sort -n | tail -n 3
        ```

        ```text
           2 0.0026546149
           2 0.0035111452
          49 -100.0
        ```

    === "Windows"

        ```text
        Import-Csv data/raw/D0_KPi.csv | Group-Object TAU -NoElement | Sort-Object Count | Select-Object -Last 3
        ```

        ```text
        Count Name
        ----- ----
            2 0.0001520892
            2 0.00017826671
           49 -100.0
        ```

    191 values occur twice, so the two shells list different ones before
    the 49.

!!! success "You should now see"
    The mass column from 1766.2096 to 2453.6584 on the board, and `-100.0`
    49 times: the mark for "no decay time", found without being told.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `uniq -c` prints thousands of lines of `1` | `sort` is missing before `uniq`. `uniq` only merges lines that stand next to each other |
    | `-n`, or the braces `{[double]$_}`, left out, and the same answer | Luck: every mass has four digits before the point, so text order is number order here. In a column with `20` and `100` it is not: as text `100` comes first (the slide *Order*). Keep them |
    | macOS: a sorted column with points looks wrong | The laptop's language reads the comma as the decimal sign. Write `LC_ALL=C sort -n` in place of `sort -n` |

---

### 10. Keep lines: `D0_valid.csv` { #grep }

**1:15 · 10 min**

**Tell the room.** The 49 marked rows are taken out by a typed line. The raw
file is read and stays as it is. The new file goes to `data/processed`, and
the line that made it says exactly what was done.

1. Show the first marked row with its line number.

    === "macOS"

        ```text
        grep -n ',-100' data/raw/D0_KPi.csv | head -n 1
        ```

        ```text
        343:1818.1002,2978.644,-100.0,9901.186
        ```

    === "Windows"

        ```text
        Select-String ',-100' data/raw/D0_KPi.csv | Select-Object -First 1
        ```

        ```text
        data\raw\D0_KPi.csv:343:1818.1002,2978.644,-100.0,9901.186
        ```

2. Write every line **without** the text into a new file. `>` sends the
   output into a file.

    === "macOS"

        ```text
        grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv
        ```

    === "Windows"

        ```text
        Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv
        ```

        `-Raw` passes on only the text of each line, without the file name
        and the line number.

3. Count its lines and its bytes.

    === "macOS"

        ```text
        wc -l data/processed/D0_valid.csv
        ```

        ```text
           91535 data/processed/D0_valid.csv
        ```

        ```text
        wc -c data/processed/D0_valid.csv
        ```

        ```text
         3924368 data/processed/D0_valid.csv
        ```

    === "Windows"

        ```text
        (Get-Content data/processed/D0_valid.csv).Count
        ```

        ```text
        91535
        ```

        ```text
        (Get-Item data/processed/D0_valid.csv).Length
        ```

        ```text
        4015903
        ```

4. Check the lines on the board: 91 584 − 49 = 91 535, the header and
   91 534 rows, in both shells. Then the bytes: 4 015 903 − 3 924 368 =
   91 535, one byte more for each line. Show where it is.

    === "macOS"

        ```text
        hexdump -C -n 32 data/processed/D0_valid.csv
        ```

        ```text
        00000000  4d 2c 50 54 2c 54 41 55  2c 49 50 43 48 49 32 0a  |M,PT,TAU,IPCHI2.|
        00000010  31 38 38 30 2e 36 34 39  2c 33 30 30 30 2e 39 35  |1880.649,3000.95|
        00000020
        ```

    === "Windows"

        ```text
        Format-Hex data/processed/D0_valid.csv -Count 32
        ```

        ```text
           Label: C:\Users\ada\Documents\analysis-project\data\processed\D0_valid.csv

                  Offset Bytes                                           Ascii
                         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
                  ------ ----------------------------------------------- -----
        0000000000000000 4D 2C 50 54 2C 54 41 55 2C 49 50 43 48 49 32 0D M,PT,TAU,IPCHI2�
        0000000000000010 0A 31 38 38 30 2E 36 34 39 2C 33 30 30 30 2E 39 �1880.649,3000.9
        ```

    PowerShell writes each line itself and ends it with CRLF, `0D 0A`. The
    raw file has LF. Same rows, other bytes.

!!! success "You should now see"
    `D0_valid.csv` in `data/processed`: 91 535 lines on every laptop,
    3 924 368 bytes on a Mac and 4 015 903 on Windows, and `D0_KPi.csv`
    unchanged at 3 926 142.

**Say it in these words.** The raw file was read and not changed. The new
file can be deleted and made again with one line. The two systems write the
same rows with different line breaks, so the two files will not have the
same checksum: section 12 comes back to it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `D0_valid.csv` is empty, or `D0_KPi.csv` is | The line had `> data/raw/...`, or the same file on both sides. `>` empties its file before anything is read. Download `D0_KPi.csv` again |
    | Windows: `A parameter cannot be found that matches parameter name 'Raw'.` | The terminal is Windows PowerShell 5.1, which has no `-Raw` here. Section 4, step 1. Delete the empty `D0_valid.csv` it left |
    | Windows: every line of the new file starts with `data\raw\D0_KPi.csv:` | `-Raw` is missing. Run the line again with it |

---

## Part 5 · A program, a checksum, the README { #part-5 }

**1:25 to 2:00 · sections 11 to 15**

The four hand edits of Lecture 2 are run as one typed line. A checksum then
shows that every laptop in the room wrote the same bytes, and the README
gets the size, the checksum and the lines that rebuild the files.

---

### 11. Run a program someone else wrote { #script }

**1:25 · 6 min**

**Tell the room.** Filters count, sort and keep lines. The four edits of
Lecture 2 take a program, and a program someone else wrote is run like any
other command: the program `python3` or `python`, its first argument the
script, then the file it reads and the file it writes.

1. Run the cleaning script.

    === "macOS"

        ```text
        python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
        ```

    ```text
    9 rows written to data/processed/pendulum_script.csv
    ```

2. Measure what it wrote.

    === "macOS"

        ```text
        wc -c data/processed/pendulum_script.csv
        ```

        ```text
              97 data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        (Get-Item data/processed/pendulum_script.csv).Length
        ```

        ```text
        97
        ```

3. Open `data/processed/pendulum_script.csv` in VS Code. It begins with
   `length_cm,t10_s` and `20,9.02`, and the Status Bar reads `LF` also on
   Windows: the script states its line break itself.

!!! success "You should now see"
    9 rows, and 97 bytes on every laptop, Mac and Windows alike.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `no file data/raw/pendulum.csv` | The raw table is missing or misnamed. Section 2 |
    | `can't open file ... scripts/clean_pendulum.py` | The script is not in `scripts`, or was saved as `clean_pendulum (1).py` |
    | A size other than 97 | The raw file differs from the lab partner's table. Compare it with [`pendulum_raw.csv`](../data/pendulum_raw.csv): 130 bytes |

---

### 12. One checksum in the room { #checksum }

**1:31 · 9 min**

**Tell the room.** Lecture 04 opened on four copies of the cleaned table,
97, 96, 107 and 105 bytes, that all look the same in VS Code. A checksum is
computed from every byte of a file: the same bytes always give the same 64
hex digits. The room now checks whether 30 laptops wrote the same file.

1. Compute the checksum of the file the script wrote.

    === "macOS"

        ```text
        shasum -a 256 data/processed/pendulum_script.csv
        ```

        ```text
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/pendulum_script.csv).Hash
        ```

        ```text
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        ```

        `Get-FileHash` writes the digits in upper case. `be05` and `BE05`
        are one number.

2. Read the last eight digits aloud, row by row: `fff0870b`. Ask who has
   other digits. One checksum in the whole room, on macOS and on Windows.

3. Now your own cleaned copy, next to the script's. The wildcard takes both
   files.

    === "macOS"

        ```text
        shasum -a 256 data/processed/pendulum*.csv
        ```

        ```text
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum.csv
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_script.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/pendulum*.csv).Hash
        ```

        ```text
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        ```

4. Put the slide *Which Copy? The README Says* on the projector. Each
   student finds their own `pendulum.csv` in the table, by its first eight
   digits.

    | Copy | Bytes | SHA-256 | What differs |
    |--|--|--|--|
    | A | 97 | `be05af03…fff0870b` | nothing: the script's file |
    | B | 96 | `139c90c8…18ddfe54` | no `0A` after the last line |
    | C | 107 | `c06d1344…f102106d` | CRLF |
    | D | 105 | `12c5c5ca…3afb291b` | CRLF, and no line break after the last line |
    | other | 97 or another size | other digits | a value or a character differs |

5. A copy that is not A is replaced by the script's file. The README will
   name A. `cp` is the same word in both shells, and replaces without
   asking.

    ```text
    cp data/processed/pendulum_script.csv data/processed/pendulum.csv
    ```

!!! success "You should now see"
    `be05af03…fff0870b` twice on every laptop.

**Say it in these words.** Same checksum, same bytes. The table cleaned by
hand and the table written by the script are one file when the checksums
agree. Size alone cannot tell A from a copy with one digit changed: the
checksum can.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `pendulum_script.csv` has other digits than `be05af03…` | The raw file or the script differs from the handed-out ones. Download both again and run section 11 again |
    | Windows: a table with `Algorithm`, `Hash` and `Path` | The round brackets and `.Hash` are missing. The digits are the same |

---

### 13. A list of checksums, and a mean { #list }

**1:40 · 7 min**

**Tell the room.** Lecture 2 said raw files are never edited. A list of
their checksums, written once, turns the rule into a test that runs in a
second. Then a second program computes what no filter can: a mean.

1. Write the list for `data/raw` and check it at once. The list stands in
   `data`, so that `data/raw/*` never includes it. Seminar 5 uses it.

    === "macOS"

        ```text
        shasum -a 256 data/raw/* > data/checksums.txt
        ```

        ```text
        shasum -a 256 -c data/checksums.txt
        ```

        ```text
        data/raw/D0_KPi.csv: OK
        data/raw/pendulum.csv: OK
        ```

    === "Windows"

        ```text
        (Get-FileHash data/raw/*).Hash | Set-Content data/checksums.txt
        ```

        ```text
        $list = Get-Content data/checksums.txt
        ```

        ```text
        $now = (Get-FileHash data/raw/*).Hash
        ```

        ```text
        Compare-Object $list $now
        ```

        `Compare-Object` prints only the lines that differ. Nothing means
        the same. `$list = …` keeps an output under a name for the next
        line.

2. Open `data/checksums.txt`. The line for `D0_KPi.csv` starts with
   `25c3c972`, or `25C3C972`, on every laptop.

3. Run the second handed-out script on the raw file, for the column `TAU`.

    === "macOS"

        ```text
        python3 scripts/column_stats.py data/raw/D0_KPi.csv TAU
        ```

    === "Windows"

        ```text
        python scripts/column_stats.py data/raw/D0_KPi.csv TAU
        ```

    ```text
    file    data/raw/D0_KPi.csv
    column  TAU
    rows    91583
    min     -100.0
    max     0.5787994
    mean    -0.0525221
    ```

4. Press `↑` and change the path to `data/processed/D0_valid.csv`.

    ```text
    file    data/processed/D0_valid.csv
    column  TAU
    rows    91534
    min     -0.13715266
    max     0.5787994
    mean    0.000981802
    ```

!!! success "You should now see"
    `OK` twice, or nothing from `Compare-Object`, and two means on the
    board: −0.0525 ns with the 49 marked rows, +0.00098 ns without them.

**Say it in these words.** 49 rows of 91 583 are 0.05% of the file:
49 × (−100) / 91 583 = −0.0535. They move the mean decay time to the wrong
sign. A mark for "no value" written as a number is counted as a number by
every program.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FAILED`, or `Compare-Object` prints two lines | A raw file changed after the list was written. If the list is seconds old, the file is open in a spreadsheet or was saved by one |
    | `no column tau in ...` | Column names are written as in the header: `TAU` |
    | macOS: `shasum: data/checksums.txt: no properly formatted SHA checksum lines found` | The list is empty, or was written by the Windows line. Run the first line of step 1 again |

---

### 14. Write it into the README { #readme }

**1:47 · 8 min**

**Tell the room.** The README said in words what was done to the pendulum
table. Now it names the copy it means, by size and checksum, and keeps the
lines that make the files of `data/processed`. These lines are the work,
not a story of it. Seminar 5 relies on them.

1. Open `README.md` and its preview with `Ctrl+K`, then `V` (macOS `Cmd+K`,
   then `V`). Change the line **Cleaned copy** to name the size and the
   checksum. Copy the 64 digits out of the terminal: select them and press
   `Ctrl+C` (macOS `Cmd+C`). Upper or lower case is the same number.

    ```text
    - **Cleaned copy:** `data/processed/pendulum.csv`, 97 bytes,
      SHA-256 `be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b`.
      Mean line deleted, `,` replaced by `.`, `;` replaced by `,`, column `nr` deleted
    ```

2. Add a section **How to rebuild** at the end of the README. Copy the
   lines from this page, or from the terminal history with `↑`, never from
   memory.

    ```text
    ## How to rebuild

    Run in the project folder: zsh on macOS, PowerShell 7 on Windows.

    1. The cleaned pendulum table, 97 bytes, SHA-256 `be05af03…fff0870b`:
       - zsh: `python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv`
       - PowerShell: `python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv`
    2. `D0_KPi.csv` without the 49 rows marked `-100`, 91 535 lines:
       - zsh: `grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv`
       - PowerShell: `Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv`
    ```

3. Save and read both parts in the preview.

!!! success "You should now see"
    In the preview: the line **Cleaned copy** with 97 bytes and the 64
    digits, and a section **How to rebuild** with two numbered steps, each
    with a line for each shell.

**Say it in these words.** The README may promise the checksum of the
pendulum table: the script writes the same 97 bytes on every system. For
`D0_valid.csv` it promises the lines, not the checksum, because each shell
writes its own line breaks.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The preview shows the list as one paragraph | An empty line is missing before `1.`, or the `-` lines are not indented by three spaces |
    | The checksum in the README ends in other digits | It was typed, not copied. Copy it again from the terminal |

---

### 15. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

- Python and Git are installed. On Windows the terminal is PowerShell 7, on
  macOS `zsh`. The ideas are the same in both, the words differ.
- The prompt shows the working directory. A command is a program, options
  (parameters) and arguments. A relative path works on every laptop.
- `wc -c` and `Length` count the bytes of a file, `hexdump -C` and
  `Format-Hex` show them. `ą` takes two bytes in UTF-8, a line break one or
  two.
- The ends of a sorted column and the count of repeated values found four
  far masses and the mark `-100.0` in 49 rows.
- Commands read from `data/raw` and write to `data/processed`. `>` empties
  the file it writes to.
- A program someone else wrote runs with one typed line: `python3` on
  macOS, `python` on Windows.
- One checksum, `be05af03…fff0870b`, in the whole room: the same 97 bytes
  on every laptop.
- The README names the copy by size and checksum, and keeps the lines that
  rebuild the files.

---

## Optional, if the room is fast { #optional }

Three sections for a room that is ahead of the clock. Each starts from files
the room already has. Do them in this order, and stop at 1:55 for the wrap
up.

---

### 16. Regex in the Find box { #regex }

**Optional · 12 min**

**Tell the room.** A regular expression describes a kind of text: a number,
a comma between two digits, a line that starts with a semicolon. The room
cleans the raw pendulum table a second time, on a copy, with four
replacements, and checks the result by its checksum.

1. Make a copy to work on, and open it in the editor. The line is the same
   in both shells.

    ```text
    cp data/raw/pendulum.csv data/processed/pendulum_regex.csv
    ```

2. Press `Ctrl+H` (macOS `Cmd+Option+F`). Switch on the button `.*` at the
   right end of the **Find** box, or press `Alt+R` (macOS `Cmd+Option+R`).

3. Build a pattern for the first column. Type each one into **Find** in
   place of the one before, and read the counter.

    ```text
    [0-9]+
    ```

    39 matches: every number.

    ```text
    [0-9]+;
    ```

    18: a number in front of a `;`.

    ```text
    ^[0-9]+;
    ```

    9: the first of them in a line, the row number.

    ```text
    ^(nr|[0-9]+);
    ```

    10: the row number, or `nr` in the header line.

4. Leave **Replace** empty and select **Replace All**. The first column is
   gone from the header and from the nine rows.

5. Type into **Find**:

    ```text
    ([0-9]),([0-9])
    ```

    The counter ends in `of 10`. Type into **Replace**:

    ```text
    $1.$2
    ```

    Select **Replace All**. Every decimal comma is now a point, and every
    semicolon is where it was.

6. Click in the line `;mean;15.14` and delete it with `Ctrl+Shift+K` (macOS
   `Cmd+Shift+K`).

7. Type into **Find**:

    ```text
    ;
    ```

    The counter ends in `of 10`. Type into **Replace**:

    ```text
    ,
    ```

    Select **Replace All**, close the boxes with `Esc` and save.

8. Compare the result with the cleaned table by its checksum.

    === "macOS"

        ```text
        shasum -a 256 data/processed/pendulum_regex.csv
        ```

        ```text
        be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_regex.csv
        ```

    === "Windows"

        ```text
        (Get-FileHash data/processed/pendulum_regex.csv).Hash
        ```

        ```text
        BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
        ```

9. Delete the copy. It was practice, and no line of the README makes it,
   so it would only be one more file for Git in Seminar 5.

    ```text
    rm data/processed/pendulum_regex.csv
    ```

!!! success "You should now see"
    `be05af03…fff0870b`: four replacements made the same 97 bytes as the
    hands in Lecture 2 and the script in section 11.

`([0-9]),([0-9])` fits a comma only between two digits, so it cannot touch
a comma that separates two values. That is why the order of the
replacements no longer matters.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The counter says `No results` for `[0-9]+` | The button `.*` is off |
    | `$1.$2` appears in the file as text | The button `.*` was switched off before **Replace All**. `Ctrl+Z`, switch it on, replace again |
    | Other digits than `be05af03` | Look at the file: a last line `100,20.01` without a line break gives 96 bytes, `CRLF` in the Status Bar gives 107 |

---

### 17. The same patterns in the shell { #grep-e }

**Optional · 10 min**

**Tell the room.** `grep -E` and `Select-String` read the same patterns as
the Find box. The pattern stands in single quotes, in both shells: without
them the shell reads `*`, `[`, `,` and `|` itself.

1. Count the lines of the raw table that have a decimal comma.

    === "macOS"

        ```text
        grep -cE '[0-9],[0-9]' data/raw/pendulum.csv
        ```

    === "Windows"

        ```text
        (Select-String '[0-9],[0-9]' data/raw/pendulum.csv).Count
        ```

    ```text
    10
    ```

2. Press `↑` and take the quotes away. macOS answers
   `zsh: no matches found: [0-9],[0-9]`. PowerShell prints `11`, a wrong
   number and no warning: it read the comma as a list of two patterns.

3. Count the lines that contain `1865`, then those that start with it.

    === "macOS"

        ```text
        grep -c 1865 data/raw/D0_KPi.csv
        ```

        ```text
        grep -c '^1865' data/raw/D0_KPi.csv
        ```

    === "Windows"

        ```text
        (Select-String 1865 data/raw/D0_KPi.csv).Count
        ```

        ```text
        (Select-String '^1865' data/raw/D0_KPi.csv).Count
        ```

    1986 and 1846. In 140 lines `1865` stands inside another number.

4. Find the rows outside 1810 to 1920, with their line numbers.

    === "macOS"

        ```text
        grep -nE '^(17|180|19[2-9]|2)' data/raw/D0_KPi.csv
        ```

        ```text
        10048:2453.6584,755.2686,0.2276815,1.0500937
        43608:1808.1385,3632.4104,0.06656479,11200.344
        67877:1920.3453,4999.695,0.00015124853,1.0319226
        89861:1766.2096,12493.022,0.0037266747,214.38336
        ```

    === "Windows"

        ```text
        Select-String '^(17|180|19[2-9]|2)' data/raw/D0_KPi.csv
        ```

        ```text
        data\raw\D0_KPi.csv:10048:2453.6584,755.2686,0.2276815,1.0500937
        data\raw\D0_KPi.csv:43608:1808.1385,3632.4104,0.06656479,11200.344
        data\raw\D0_KPi.csv:67877:1920.3453,4999.695,0.00015124853,1.0319226
        data\raw\D0_KPi.csv:89861:1766.2096,12493.022,0.0037266747,214.38336
        ```

5. The room does this step alone: the number of rows with a mass from 1850
   up to 1880. The answer is `grep -cE '^18[5-7]' data/raw/D0_KPi.csv`, or
   `(Select-String '^18[5-7]' data/raw/D0_KPi.csv).Count`: 41091, 45% of
   the rows.

!!! success "You should now see"
    Four lines with their numbers: the four far masses of section 9.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | A pattern with `\d` finds nothing on macOS | Not every `grep` reads `\d` as a digit. Write `[0-9]` |
    | `grep` and `Select-String` disagree on a file made in PowerShell | The file has CRLF. For `grep` the `0D` is the last character of the line, so a pattern that ends in `$` fits nothing. `D0_KPi.csv` has LF and is not affected |

---

### 18. Complete the README { #readme-more }

**Optional · 15 min**

**Tell the room.** A stranger with the README still asks what `TAU` is, in
which unit, and whether the scripts may be copied. Then the section **How
to rebuild** is tested the way a stranger would use it.

1. Add a section on the columns under **Data**. The names and the 49 come
   out of the file. The units do not: they are on the record page.

    ```text
    ## Columns of `D0_KPi.csv`

    | Column | Meaning | Unit |
    |--|--|--|
    | `M` | mass of the K⁻π⁺ pair | MeV/c² |
    | `PT` | transverse momentum | MeV/c |
    | `TAU` | decay time | ns |
    | `IPCHI2` | χ² of the impact parameter | none |

    Missing value: `TAU` is `-100.0` in 49 rows.
    ```

2. Add the licence. The data keeps the licence of its record. The scripts
   and the text are the student's own.

    ```text
    ## Licence

    Data: CC0, CERN Open Data Portal, record 401.
    Scripts and text: MIT, see `LICENSE`.
    ```

3. Test **How to rebuild**. Delete the two files it makes.

    === "macOS"

        ```text
        rm data/processed/pendulum_script.csv data/processed/D0_valid.csv
        ```

    === "Windows"

        ```text
        rm data/processed/pendulum_script.csv, data/processed/D0_valid.csv
        ```

4. Copy the two lines of your shell out of the preview, one at a time, and
   run them. Then measure what came back.

    === "macOS"

        ```text
        wc -c data/processed/*.csv
        ```

        ```text
         3924368 data/processed/D0_valid.csv
              97 data/processed/pendulum.csv
              97 data/processed/pendulum_script.csv
         3924562 total
        ```

    === "Windows"

        ```text
        Get-ChildItem data/processed | Select-Object Name, Length
        ```

        ```text
        Name                 Length
        ----                 ------
        D0_valid.csv        4015903
        pendulum_script.csv      97
        pendulum.csv             97
        ```

!!! success "You should now see"
    Two new sections in the preview, and the files of `data/processed` back
    with the sizes of sections 10 and 11.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as text with `|` signs | An empty line is missing before the table, or the line `|--|--|--|` is missing |
    | `rm` reports a missing file | It was deleted before. Go on with the next step |
    | Windows: `Remove-Item: A positional parameter cannot be found that accepts argument 'data/processed/D0_valid.csv'.` | The comma between the two paths is missing. Nothing was deleted. Run the line again with it |

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Look at the first eight bytes of the plot:
  `hexdump -C -n 8 results/pendulum_plot.png`, or
  `Format-Hex results/pendulum_plot.png -Count 8`. The answer is
  `89 50 4E 47 0D 0A 1A 0A`. The second to fourth bytes are `PNG` in ASCII:
  every PNG picture begins this way, whatever its name.
- Count how many different values `TAU` has:
  `tail -n +2 data/raw/D0_KPi.csv | cut -d, -f3 | sort | uniq | wc -l`, or
  `(Import-Csv data/raw/D0_KPi.csv | Group-Object TAU -NoElement).Count`.
  The answer is 91344 for 91 583 rows.
- Two rows write a number with an exponent. Find their line numbers with
  `grep -n 'e-' data/raw/D0_KPi.csv`, or
  `Select-String 'e-' data/raw/D0_KPi.csv`. The answer is lines 40769 and
  44745, with `1.3600341e-05` and `9.40878e-05` in the last column.
- After the marked rows are gone, three rows still have a negative decay
  time: `grep ',-0' data/raw/D0_KPi.csv`, or
  `Select-String ',-0' data/raw/D0_KPi.csv`. The answer is lines 22856,
  35320 and 42862, with `TAU` of −0.137, −0.059 and −0.098. They are not
  marks.
- Make a histogram of the mass in steps of 10 MeV/c²: the first three
  characters of each mass. `tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | cut -c1-3 | sort | uniq -c`,
  or `Import-Csv data/raw/D0_KPi.csv | Group-Object {$_.M.Substring(0,3)} -NoElement | Sort-Object Name`.
  The answer has 15 lines, with the peak `17496 186`: the D⁰, whose mass
  is 1865 MeV/c².
- Find every file of the project larger than 1 MB: `find . -size +1M`, or
  `Get-ChildItem -Recurse -File | Where-Object Length -gt 1MB | Select-Object Name, Length`.
  The answer is `D0_KPi.csv` and `D0_valid.csv`.
- Write the numbers of section 7 into the README as a section **File
  anatomy**, in the form of [Seminar 3, section 7](seminar_03.md#readme).
- Copy the project folder to a USB drive with the file manager, open the
  copy in VS Code, and run the check of section 13 inside it. Every line
  ends in `OK`, or `Compare-Object` prints nothing.
- A student with a dataset of their own runs the three questions of
  section 8 and the two ends of one numeric column on it.
- Add a file `LICENSE` to the project folder with the text of the MIT
  licence from [choosealicense.com](https://choosealicense.com/licenses/mit/),
  with the year and the student's name filled in.

## If students ask for more

| Topic | Week |
|--|--|
| Keeping older versions of the scripts and the README | 5 (Version Control with Git) |
| Writing a program like `clean_pendulum.py` or `column_stats.py` | 6 and 7 (Python) |
| Plotting the histogram of the mass | 8 (Data Visualisation) |
| Cleaning a table whose mark for "no value" is not known in advance | 12 (Pandas & Data Cleaning) |
| One command that rebuilds everything | 13 (Reproducible Workflows) |

Leave out altogether, even if asked: Git Bash, `awk`, `vim`, aliases of your own, the
shell's start-up files, remote login.

## Aims practised

⚙️ a step typed once and run again · 📁 a file measured in bytes, raw data read and never written · 🔧 one task in two shells, the same answer · ♻️ one checksum for the same file in the whole room
