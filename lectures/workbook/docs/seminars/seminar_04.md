# Seminar 4 — Work on Files from the Shell

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along, with a task for the room in every part · **~120 min**
in class

**The question of the day:** two counters, one on a bridge and one on a
park path, counted the bicycles that passed every hour of 2024 and 2025.
How many bicycles pass in an hour? Every student installs the tools, gets
the file and checks it, finds what is wrong in it, computes the answer,
and writes a script that makes every result again.

## Run sheet

One screen for the front of the room. Each line links to its section.
A **Task** is for the room alone; the answer is folded under it.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Install and set up** · 36 min | | |
| 0:00 | [1. Install the tools](#installs) | `winget install …`, the Miniforge installer, `conda init` | PowerShell 7, Git and Miniforge installed |
| 0:12 | [2. VS Code, its terminal and the shell](#shell) | The five regions, **Select Default Profile** | `(base)` in the prompt, `7` or `/bin/zsh`, `conda 26.7.2` |
| 0:18 | [3. Read the prompt; `pwd`, `ls`, `cd`](#terminal) | `pwd`, `ls`, `cd`, `Tab`, `↑` | The prompt read aloud, part by part |
| 0:25 | [4. Make the project folder with `mkdir`](#folder) | `mkdir` six times; **Task**: two paths | `bike-project` with its four folders |
| 0:32 | [5. Start the README](#readme-md) | `README.md` and its preview | A title, the question, the folders |
| | **Part 2 · Get the file and check it** · 22 min | | |
| 0:36 | [6. Move the downloaded files into the project](#files) | `mv ~/Downloads/…` | `bikes.csv` and `column_stats.py` in place |
| 0:40 | [7. Is it the right file? A checksum](#checksum) | `shasum -a 256`, `Get-FileHash` | `2c68aad2…` on every laptop |
| 0:44 | [8. Read `bikes.csv`, count its lines and bytes](#count) | `head`, `tail`, `wc`, two mistakes | 35 089 lines, 900 314 bytes |
| 0:52 | [9. The bytes of the first lines](#bytes) | `hexdump -C`, `Format-Hex`; **Task**: line ends | 19, 26 and 24 bytes; 877 219 if every count had one digit |
| | **Part 3 · Find what is wrong** · 23 min | | |
| 0:58 | [10. A pipe: sort the counts, read both ends](#sort) | `sort -n`, `Sort-Object` | `9999` at the top: the mark for a missing count |
| 1:06 | [11. Count the 9999 rows, find the broken week](#grep) | `grep -c`, `uniq -c`; **Task**: a line, empty hours | 168 rows, one week at the park |
| 1:15 | [12. Keep the valid rows in a new file](#valid) | `grep -v … >`, text against number | `bikes_valid.csv`, 34 921 lines |
| | **Part 4 · The answer** · 10 min | | |
| 1:21 | [13. The mean, with and without the 9999 rows](#python) | `column_stats.py` twice; **Task**: each counter | 86.3 and 38.6 bicycles per hour |
| | **Part 5 · Make it repeatable** · 25 min | | |
| 1:31 | [14. A script that makes the files again](#script) | `rebuild.sh`, `chmod +x`, `rm`; **Task**: two more files | One command remakes `data/processed` and `results` |
| 1:41 | [15. The script from the other system](#crlf) | A copy saved with CRLF | `bad interpreter` on a Mac; the PowerShell script runs with either line end |
| 1:48 | [16. The README: data, columns, how to rebuild](#readme) | `README.md` and its preview | The checksum, the columns, the mark, the script |
| 1:53 | [17. Wrap up](#wrap-up) | `git --version`, the list of the day | Git ready for next week |
| | **Optional, if the room is fast** | | |
| — | [18. A program that cleans an export](#clean) | `clean_export.py` | `monthly.csv`, `ea4ce2ce…` on every laptop |
| — | [19. Regular expressions in VS Code and the shell](#regex) | The `.*` button, `grep -E`, `Select-String` | 168, 4022, 37 |
| — | [20. A conda environment for the project](#environment) | `conda create`, `conda activate`, `conda install numpy` | `(bikes)` in the prompt, `environment.yml` |
| — | [21. A list of checksums](#list) | `shasum -a 256 -c`, `Compare-Object` | `OK`, then one digit caught |
| — | [22. Stop the script at the first error](#stop) | `set -e`, `$ErrorActionPreference` | A typo that stops the script |
| — | [23. Aliases, the prompt and the start-up file](#settings) | `alias`, `~/.zshrc`, `$PROFILE`, Oh My Zsh, Oh My Posh | A short prompt and `..` in every new terminal |

**If time runs short:** do sections 3 and 5 in three minutes each, show
section 9 and section 15 on the projector only, and shorten a Task to its
first question. Never cut sections 11 to 14: they hold the finding and the
answer of the day.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes the steps. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - A **Task** is for the room alone, with only the commands of that part.
      Give it three to five minutes, then ask a student to show the answer
      on the projector. The answer is folded under the task.
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
    - Skim sections 10 and 11: they hold the one surprise of the day, the
      value `9999`. Let the room find it; do not announce it.

??? info "Files for this seminar"
    A browser saves each file in **Downloads** under the name in the second
    column; the page moves it into the project folder with a typed command.

    | File | Saved as | Moved into | What it is |
    |--|--|--|--|
    | [`bikes_hourly.csv`](../data/bikes_hourly.csv){ download="bikes.csv" } | `bikes.csv` | `data/raw` | Section 6. Two counters, one row per counter and hour, 2024 and 2025: 35 088 rows, 900 314 bytes, SHA-256 `2c68aad2…e3808991` |
    | [`cli_column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" } | `column_stats.py` | `scripts` | Section 6. A program that prints rows, smallest, largest and mean of one column |
    | [`bikes_monthly_export.csv`](../data/bikes_monthly_export.csv){ download="monthly_export.csv" } | `monthly_export.csv` | `data/raw` | Optional section 18. Bicycles per day on the bridge, each month of 2025, as a spreadsheet exported it |
    | [`cli_clean_export.py`](../data/cli_clean_export.py){ download="clean_export.py" } | `clean_export.py` | `scripts` | Optional section 18. A program that cleans such an export |
    | [`bikes_project.zip`](../data/bikes_project.zip) | `bikes_project.zip` | unpack it | The folder `bike-project` at the end of section 17, both scripts in it, for a student who lost a step |
    | [`bikes_README.txt`](../data/bikes_README.txt){ download="README.md" } | `README.md` | compare only | The README of sections 5 and 16 |

    The bicycle files were made by [`bikes_files.py`](../data/bikes_files.py).

---

## Part 1 · Install and set up { #part-1 }

**0:00 to 0:36 · sections 1 to 5**

Everything the day needs is installed first, in the terminal the system
brings, while VS Code stays closed. Then VS Code starts, finds it all, and
the room builds the project folder from nothing. [Install Python, Git and
PowerShell 7](install_python_git.md) has the installs per system, with
every error message, for helpers at a laptop.

---

### 1. Install the tools { #installs }

**0:00 · 12 min**

**Tell the room.** Three programs come today. **PowerShell 7**, on Windows
only: a shell that is the same on every Windows laptop; a Mac has its
shell, `zsh`, built in. **Miniforge**: Python, and **conda**, a program
that installs packages and keeps each project's packages apart. **Git**,
which keeps versions of files from next week on. VS Code stays closed
until the installs are done, so that it finds them when it starts. Type
the lines exactly; every word of them comes back later today.

1. Close VS Code if it is open. Open the terminal of the system.

    === "macOS"

        Press `Cmd+Space`, type `Terminal`, press `Enter`. A window with a
        prompt opens. Ask for Git:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. They install on their own for
        5 to 15 minutes; go on meanwhile. If the line prints
        `git version 2.…` instead, Git is already there.

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

        It ends with `Successfully installed` too.

2. Install Miniforge.

    === "macOS"

        In the same window, go into **Downloads**, fetch the installer and
        run it:

        ```text
        cd ~/Downloads
        ```

        ```text
        curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
        ```

        `$(uname)` and `$(uname -m)` fill in the system and the chip of
        this Mac, so one line fits every Mac. A table counts the download
        up to `100`.

        ```text
        bash Miniforge3-$(uname)-$(uname -m).sh
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

        Select this link; the browser saves the installer in
        **Downloads**:
        [Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe).
        Not `winget`: the Miniforge it offers is from 2022.

        Open the installer in **Downloads**. Select **Next** and **I
        Agree**, choose **Just Me (recommended)**, and keep every other
        default: the folder `C:\Users\smilte\miniforge3`, the boxes as they
        are, **Install**, then **Finish**.

        Then press the Windows key, type `Miniforge Prompt` and press
        `Enter`. In the window that opens, let conda add its lines to the
        start-up files of PowerShell, so that every new terminal finds
        conda and Python:

        ```text
        conda init powershell
        ```

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

3. Close the terminal windows. On a Mac the developer tools go on
   installing on their own.

!!! success "You should now see"
    On macOS `Thank you for installing Miniforge3!`, and the developer
    tools installing. On Windows `Successfully installed` twice, and the
    last line of `conda init powershell`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
    | Windows: `winget` is not recognized | Install `PowerShell-7.6.6-win-x64.msi` and Git for Windows from the USB stick, with every default |
    | macOS: `curl: (6) Could not resolve host: github.com` | No network. Copy the Miniforge installer from the USB stick into **Downloads** and go on with `bash` |
    | macOS: `ERROR: File or directory already exists: '/Users/smilte/miniforge3'` | Miniforge is there already, from an earlier try. Go on with section 2 |
    | Windows: the browser asks whether to keep the installer | Select **Keep**. It comes from the release page of conda-forge on GitHub |
    | Windows: "Windows protected your PC" when the installer starts | Select **More info**, then **Run anyway** |
    | An installer asks for an administrator password the student does not have | The laptop is managed by the university or an employer. The student pairs with a neighbour today |
    | No VS Code on the laptop | Download it from `code.visualstudio.com` and install it with every default, now |

---

### 2. VS Code, its terminal and the shell { #shell }

**0:12 · 6 min**

**Tell the room.** VS Code is the editor of the course: files, Markdown and
the terminal in one window, in five regions. The **terminal** is the
window that shows text; the **shell** is the program inside it that reads
each line you type, runs it, prints the answer and waits: `zsh` on a Mac,
PowerShell 7 on Windows. Windows has two PowerShells, so VS Code is told
once to open 7.

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

3. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`): the **Command Palette**,
   where every command of VS Code can be found by name.

    === "macOS"

        Type `create new terminal` and select **Terminal: Create New
        Terminal**. The Panel opens at the bottom, with a prompt.

    === "Windows"

        Type `default profile` and select **Terminal: Select Default
        Profile**, then **PowerShell**. Not **Windows PowerShell**: that is
        5.1. Press `Ctrl+Shift+P` again, type `create new terminal` and
        select **Terminal: Create New Terminal**. The Panel opens at the
        bottom, with a prompt.

4. Check the shell.

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

5. Check conda.

    ```text
    conda --version
    ```

    ```text
    conda 26.7.2
    ```

    The prompt starts with `(base)`: conda's first environment, with
    Python in it, switched on in every new terminal.

!!! success "You should now see"
    A prompt that starts with `(base)`, `/bin/zsh` or `7`, and
    `conda 26.7.2`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `/bin/bash`, or Terminal says *The default interactive shell is now zsh* | Type `chsh -s /bin/zsh`, then the laptop's password (nothing shows while typing) and `Enter`. Quit VS Code with `Cmd+Q` and start it again |
    | macOS: no `(base)`, or `zsh: command not found: conda` | The last question of the installer was answered with `Enter`, which means no. Run `~/miniforge3/bin/conda init zsh`, then open a new terminal |
    | Windows: the version line prints `5` | **Windows PowerShell** was chosen. Step 3 again, then a new terminal |
    | Windows: **PowerShell** is missing from the list | VS Code started before PowerShell 7 was installed. Quit VS Code with **File** > **Exit**, start it again, step 3 again |
    | Windows: `conda : The term 'conda' is not recognized …`, and no `(base)` | `conda init powershell` was not run in the Miniforge Prompt (section 1, step 2), or VS Code started before it. Run it, then quit VS Code and start it again |
    | Windows: `… profile.ps1 cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1: step 3 again. Or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, answer `Y`, and open a new terminal |
    | The list offers **Git Bash** | Not in this course. Take **PowerShell** |
    | VS Code runs in the browser (`vscode.dev`) | It has no terminal. The student pairs with a neighbour today |

---

### 3. Read the prompt; `pwd`, `ls`, `cd` { #terminal }

**0:18 · 7 min**

**Tell the room.** The **prompt** is the line where the shell waits. The
shell is always in one folder, the **working directory**: the prompt shows
it, `pwd` prints it in full, `ls` lists what is in it, `cd` changes it.

1. Read the prompt aloud, part by part.

    === "macOS"

        ```text
        (base) smilte@MacBook-Air ~ %
        ```

        conda's environment, the user, the computer, the folder the shell
        is in (`~` is the home folder), and `%`: the shell waits.

    === "Windows"

        ```text
        (base) PS C:\Users\smilte>
        ```

        conda's environment, `PS`, the folder the shell is in, and `>`:
        the shell waits.

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

**0:25 · 7 min**

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

    PowerShell prints the same names in its table.

!!! success "You should now see"
    `data`, `results` and `scripts` in `bike-project`.

!!! question "Task: two paths to one folder"
    Go to the home folder. From there, list what is in the folder `data` of
    the project twice: once with a relative path, once with an absolute
    one. Then go back into `bike-project` with one `cd`.

??? note "Answer"
    ```text
    cd ~
    ```

    ```text
    ls bike-project/data
    ```

    === "macOS"

        ```text
        ls /Users/smilte/bike-project/data
        ```

    === "Windows"

        ```text
        ls C:\Users\smilte\bike-project\data
        ```

    ```text
    cd bike-project
    ```

    Both lists show `processed` and `raw`. The relative path starts at the
    working directory, the home folder; the absolute one at the top of the
    disk, so it works from anywhere. `cd ~/bike-project` also works from
    anywhere.

4. Open the folder in VS Code: **File** > **Open Folder...**, select
   `bike-project` in the home folder, **Open**. The window reloads. Then
   **Terminal** > **New Terminal**: the prompt ends in `bike-project`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `mkdir: data/raw: No such file or directory` | `data` has to exist first. `mkdir data`, then the line again |
    | `mkdir: bike-project: File exists`, or PowerShell: `An item with the specified name … already exists` | The folder is there from an earlier try. `cd bike-project` and go on |
    | A folder named `Data` or `bike project` | Delete it in the Side Bar and make it again: small letters, no spaces |
    | VS Code asks *Do you trust the authors of the files in this folder?* | **Yes, I trust the authors**: you made the folder yourself |

---

### 5. Start the README { #readme-md }

**0:32 · 4 min**

**Tell the room.** The README is the first file anyone opens in a project.
It is written in Markdown: plain text with a few signs, `#` for a heading,
`-` for a list item. Today it starts with the question; in section 16 it
gets what the files are and how to make them again.

1. In the Explorer, point at the line `BIKE-PROJECT` and select the
   **New File** icon. Name the file:

    ```text
    README.md
    ```

2. Type, or copy, this text into it:

    ```text
    # Bike Counters

    Two bicycle counters, one on a bridge and one on a park path, counted
    every hour of 2024 and 2025. How many bicycles pass in an hour?

    ## Folders

    - `data/raw`: files as they arrived, never edited
    - `data/processed`: files that commands make from `data/raw`
    - `scripts`: programs
    - `results`: numbers that the programs write
    ```

3. Open the preview beside it: `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

4. Save with `Ctrl+S` (macOS `Cmd+S`). The dot on the tab goes away: a dot
   means *not saved*.

!!! success "You should now see"
    In the preview: a large title, the question, and a heading **Folders**
    over a list of four items.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The list shows as one line | An empty line is missing before the first `-` |
    | The `#` shows in the preview | A space is missing after `#` |
    | The file is named `README.md.txt` or `readme.md` | Rename it in the Explorer with `F2` (macOS `Enter`) |

---

## Part 2 · Get the file and check it { #part-2 }

**0:36 to 0:58 · sections 6 to 9**

The counts come from a web page. Before anything is computed from them:
is it the file the page offers, how large is it, and what does one line of
it look like, byte by byte?

---

### 6. Move the downloaded files into the project { #files }

**0:36 · 4 min**

**Tell the room.** The browser saves into **Downloads**. `mv` moves a file:
first where it is, then where it goes. `~/Downloads/bikes.csv` is the same
path in both shells. Press `Tab` after a few letters of each name: a name
that `Tab` completed has no typing mistake in it.

1. Download the two files of the box **Files for this seminar** at the top
   of this page: `bikes.csv` and `column_stats.py`. Do not open them.

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
    bikes.csv
    ```

!!! success "You should now see"
    `bikes.csv` in `data/raw` and `column_stats.py` in `scripts`, in the
    terminal and in the Explorer.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory`, or PowerShell: `Cannot find path` | The name in **Downloads** differs. `ls ~/Downloads` shows how it is spelled |
    | A file named `bikes (1).csv` | It was downloaded twice. Move it and rename it in one line: `mv ~/Downloads/"bikes (1).csv" data/raw/bikes.csv`. The quotes hold a name with spaces together |
    | The browser opened the file instead of saving it | Go back and right-click the link, **Save Link As...** |

---

### 7. Is it the right file? A checksum { #checksum }

**0:40 · 4 min**

**Tell the room.** A **checksum** is a long number computed from every
byte of a file. Two files with the same bytes have the same checksum; one
byte changed gives a completely different one. The page gives the
checksum of `bikes.csv`, starting `2c68aad2`. Thirty laptops can check
that they hold that file by reading eight characters aloud.

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

2. Ask three students, one on Windows, to read the first eight characters:
   `2c68aad2`. The case of the letters does not matter.

!!! success "You should now see"
    `2c68aad2…e3808991` on every laptop: the same 900 314 bytes everywhere,
    so every number of today can be compared across the room.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Another checksum | The file is not the downloaded one: it was opened and saved, or the download broke. Download it again and move it in |
    | Windows: a table with `Algorithm`, `Hash`, `Path` | The brackets and `.Hash` were left out. The hash is the middle column |

---

### 8. Read `bikes.csv`, count its lines and bytes { #count }

**0:44 · 8 min**

**Tell the room.** A command has parts: the **program** first, then
**options** that say how, then **arguments** that say what to work on.
`head -n 3 data/raw/bikes.csv`: the program `head`, the option `-n 3`, the
argument, a path. Before we count, we predict.

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

3. Predict the number of lines with the room: 2024 had 366 days and 2025
   had 365, so 731 days of 24 hours, at two counters: 731 × 24 × 2 =
   35 088 rows, and the header makes 35 089 lines. Count them.

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

4. Its size in bytes.

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

5. Make two mistakes on purpose, and read what the shell says. A program
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

6. Help on a command. On macOS `q` leaves the manual page.

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
    | macOS: the manual page fills the Panel | `Space` goes on, `q` leaves |

---

### 9. The bytes of the first lines { #bytes }

**0:52 · 6 min**

**Tell the room.** A file is a row of bytes. In this file every character
is one byte: digits, letters, `-`, `:`, the comma. The end of a line is a
byte too, `0a`, called LF. A hex view shows each byte as a number of two
hex digits, 16 to a row, with the characters on the right.

1. The first 80 bytes.

    === "macOS"

        ```text
        hexdump -C -n 80 data/raw/bikes.csv
        ```

        ```text
        00000000  74 69 6d 65 2c 63 6f 75  6e 74 65 72 2c 62 69 6b  |time,counter,bik|
        00000010  65 73 0a 32 30 32 34 2d  30 31 2d 30 31 54 30 30  |es.2024-01-01T00|
        00000020  3a 30 30 2c 62 72 69 64  67 65 2c 32 0a 32 30 32  |:00,bridge,2.202|
        00000030  34 2d 30 31 2d 30 31 54  30 30 3a 30 30 2c 70 61  |4-01-01T00:00,pa|
        00000040  72 6b 2c 30 0a 32 30 32  34 2d 30 31 2d 30 31 54  |rk,0.2024-01-01T|
        00000050
        ```

    === "Windows"

        ```text
        Format-Hex data/raw/bikes.csv -Count 80
        ```

        ```text
           Label: C:\Users\smilte\bike-project\data\raw\bikes.csv

                  Offset Bytes                                           Ascii
                         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
                  ------ ----------------------------------------------- -----
        0000000000000000 74 69 6D 65 2C 63 6F 75 6E 74 65 72 2C 62 69 6B time,counter,bik
        0000000000000010 65 73 0A 32 30 32 34 2D 30 31 2D 30 31 54 30 30 es�2024-01-01T00
        0000000000000020 3A 30 30 2C 62 72 69 64 67 65 2C 32 0A 32 30 32 :00,bridge,2�202
        0000000000000030 34 2D 30 31 2D 30 31 54 30 30 3A 30 30 2C 70 61 4-01-01T00:00,pa
        0000000000000040 72 6B 2C 30 0A 32 30 32 34 2D 30 31 2D 30 31 54 rk,0�2024-01-01T
        ```

2. Read the first row with the room: `74 69 6d 65` is `time`, `2c` is the
   comma. The number on the left is the position of the first byte of the
   row, in hex: `00000010` is 16.

!!! success "You should now see"
    The same 80 bytes on every laptop, and `0a` where the characters on the
    right show a dot or a box.

!!! question "Task: where the lines end"
    1. Find the three `0a` in the hex view. How many bytes does each of the
       first three lines take? Check by counting the characters of each
       line.
    2. Half the 35 088 rows are `bridge` rows, half `park` rows. If every
       count had one digit, how many bytes would the file take? Why is it
       900 314?

??? note "Answer"
    1. The `0a` stand at positions 0x12 = 18, 0x2c = 2 × 16 + 12 = 44 and
       0x44 = 4 × 16 + 4 = 68, counting from 0. So the lines take 19, 26
       and 24 bytes: `time,counter,bikes` is 18 characters, the first row
       25, the second 23 (`park` is two letters shorter than `bridge`),
       and each line has its `0a`.
    2. 19 + 17 544 × 26 + 17 544 × 24 = 877 219 bytes. The file has 23 095
       bytes more: one for each digit after the first. 14 547 counts have
       two digits, 4 022 three, and 168 four:
       14 547 + 2 × 4 022 + 3 × 168 = 23 095.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `A parameter cannot be found that matches parameter name 'Count'` | The terminal is Windows PowerShell 5.1, whose `Format-Hex` has no `-Count`. Section 2, step 3 |
    | macOS: the hex view runs for pages | `-n 80` was left out. `Ctrl+C` stops it |

---

## Part 3 · Find what is wrong { #part-3 }

**0:58 to 1:21 · sections 10 to 12**

Nobody reads 35 088 counts by eye. Now the answer of one command becomes
the input of the next, with `|`, and the last answer goes into a file,
with `>`. Sorted, a column shows at its ends what does not belong.

---

### 10. A pipe: sort the counts, read both ends { #sort }

**0:58 · 8 min**

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

### 11. Count the 9999 rows, find the broken week { #grep }

**1:06 · 9 min**

**Tell the room.** `grep` and `Select-String` keep the lines that contain a
text. `,9999$` means: a comma, 9999, and then the end of the line. They can
count those lines or show them.

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

!!! success "You should now see"
    `168`, and one broken week at the park, from 10 to 16 March 2025.

!!! question "Task: a line and the empty hours"
    1. On which line of the file is the first hour of 2025 at the bridge?
       Work it out first, then print that line alone with a pipe.
    2. How many hours had no bicycle at all, at the park and at the bridge?

??? note "Answer"
    1. 2024 has 366 × 24 × 2 = 17 568 rows; after the header, the first
       row of 2025 is line 17 570.

        === "macOS"

            ```text
            head -n 17570 data/raw/bikes.csv | tail -n 1
            ```

        === "Windows"

            ```text
            Get-Content data/raw/bikes.csv -Head 17570 | Select-Object -Last 1
            ```

        ```text
        2025-01-01T00:00,bridge,4
        ```

    2. A comma, the counter, a comma, `0`, the end of the line:

        === "macOS"

            ```text
            grep -c ',park,0$' data/raw/bikes.csv
            ```

        === "Windows"

            ```text
            (Select-String ',park,0$' data/raw/bikes.csv).Count
            ```

        1372 at the park, and 576 with `bridge` in the line. Fewer
        bicycles use the park path, so more of its night hours stay empty.
        Without the `$`, `,park,0` would also count 0 at the start of a
        longer number, but no count starts with 0.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Someone typed `9999` alone and got 168 too | Here it gives the same count. The `,` and the `$` make sure that only a whole value 9999 at the end of a line counts |

---

### 12. Keep the valid rows in a new file { #valid }

**1:15 · 6 min**

**Tell the room.** `grep -v` and `Select-String -NotMatch` keep every line
*without* the text. `>` sends the result into a file instead of onto the
screen: it makes the file, or empties one that exists. The new file goes
into `data/processed`; `data/raw` is only read.

1. Keep every line without the mark.

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

2. Check the new file.

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

3. Now the busiest hour, twice: sorted as text, then as numbers.

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
    `bikes_valid.csv` with 34 921 lines in `data/processed`, and 803 as the
    busiest hour.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `bikes_valid.csv` is empty | The line read from the file it wrote to. Never `>` into the file that is read |
    | Windows: every line of the new file starts with `data\raw\bikes.csv:` | `-Raw` was left out. Run the line again with it |

---

## Part 4 · The answer { #part-4 }

**1:21 to 1:31 · section 13**

A program someone else wrote computes the mean, once on the raw file and
once on the valid rows.

---

### 13. The mean, with and without the 9999 rows { #python }

**1:21 · 10 min**

**Tell the room.** A program is a file. To run a Python program, the shell
needs Python, and finds it in the folders listed in `PATH`; conda put the
folder of `base` first in that list. `column_stats.py` prints the number of
rows, the smallest and largest value and the mean of one column. It counts
every value it finds, the mark too: it cannot know that 9999 means "no
count". Nobody has to read the program today.

1. Which Python answers?

    === "macOS"

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

2. The raw file: the program, the file to run, then two words for the
   program: the file it reads and the column. On Windows the first word is
   `python`.

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

3. The valid rows.

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

4. Work out the difference with the room: 168 × 9999 = 1 679 832 bicycles
   that never passed, spread over 35 088 rows, adds about 48 to every
   hour. One broken week in two years more than doubles the mean.

!!! success "You should now see"
    86.2712 and 38.5811 on every laptop. The answer to the question of the
    day: about 39 bicycles an hour.

!!! question "Task: each counter alone"
    What is the mean at the bridge alone, and at the park alone, without
    the broken week? Make one file per counter in `data/processed`, then
    run the program on each. A hint: `column_stats.py` needs the header
    line, and the header contains neither `bridge` nor `park`.

??? note "Answer"
    Keep every line *without* the other counter: the header stays.

    === "macOS"

        ```text
        grep -v ',park,' data/processed/bikes_valid.csv > data/processed/bridge.csv
        ```

        ```text
        grep -v ',bridge,' data/processed/bikes_valid.csv > data/processed/park.csv
        ```

    === "Windows"

        ```text
        Select-String ',park,' data/processed/bikes_valid.csv -NotMatch -Raw > data/processed/bridge.csv
        ```

        ```text
        Select-String ',bridge,' data/processed/bikes_valid.csv -NotMatch -Raw > data/processed/park.csv
        ```

    ```text
    python3 scripts/column_stats.py data/processed/bridge.csv bikes
    ```

    ```text
    file    data/processed/bridge.csv
    column  bikes
    rows    17544
    min     0.0
    max     803.0
    mean    49.6184
    ```

    ```text
    python3 scripts/column_stats.py data/processed/park.csv bikes
    ```

    ```text
    file    data/processed/park.csv
    column  bikes
    rows    17376
    min     0.0
    max     420.0
    mean    27.437
    ```

    About 50 an hour on the bridge, 27 on the park path. Check against the
    mean of both: (17 544 × 49.6184 + 17 376 × 27.437) / 34 920 = 38.58.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `Python 3.9.6`, and `which python3` prints `/usr/bin/python3` | conda is not on in this terminal: no `(base)` in the prompt. Section 2, Watch for |
    | Windows: `Python was not found; run without arguments to install from the Microsoft Store, …` | A stand-in of Windows answered, not Python: conda is not on in this terminal. Section 2, Watch for. Never install Python from the Store |
    | `no column Bikes` | Column names are exact: `bikes` |
    | Task: `no column bikes in data/processed/bridge.csv` | The header was lost: the line kept the rows *with* `bridge` (`grep` without `-v`). Keep the rows without `park` instead |

---

## Part 5 · Make it repeatable { #part-5 }

**1:31 to 1:56 · sections 14 to 17**

Every file in `data/processed` and `results` was made by a line typed
today. Written into a script, the lines run again with one command, on any
laptop. The README says what the files are and how to make them.

---

### 14. A script that makes the files again { #script }

**1:31 · 10 min**

**Tell the room.** A **script** is a text file of commands, run in order
as if they were typed. On a Mac its first line, `#!/bin/zsh`, names the
program that runs the file, and `chmod +x` allows the file to run as a
command. On Windows a file whose name ends in `.ps1` is a PowerShell
script. `./` in front of the name means "in this folder": the shell runs a
file only when it is given a path to it.

1. In the Explorer select the folder `scripts`, then **New File**.

    === "macOS"

        Name the file `rebuild.sh` and type, or copy, three lines, with
        `Enter` after the last. Save.

        ```text
        #!/bin/zsh
        grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv
        python3 scripts/column_stats.py data/processed/bikes_valid.csv bikes > results/bikes_stats.txt
        ```

    === "Windows"

        Name the file `rebuild.ps1` and type, or copy, two lines, with
        `Enter` after the last. Save.

        ```text
        Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv
        python scripts/column_stats.py data/processed/bikes_valid.csv bikes > results/bikes_stats.txt
        ```

    The lines of sections 12 and 13; the second sends its answer into
    `results` instead of onto the screen.

2. **macOS only.** Allow the file to run as a command.

    ```text
    chmod +x scripts/rebuild.sh
    ```

3. Delete the file the script makes, then run the script.

    ```text
    rm data/processed/bikes_valid.csv
    ```

    === "macOS"

        ```text
        ./scripts/rebuild.sh
        ```

    === "Windows"

        ```text
        ./scripts/rebuild.ps1
        ```

    Nothing is printed: both lines write into files.

4. Check what it made.

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

    ```text
    cat results/bikes_stats.txt
    ```

    ```text
    file    data/processed/bikes_valid.csv
    column  bikes
    rows    34920
    min     0.0
    max     803.0
    mean    38.5811
    ```

5. Compare a checksum with a neighbour on the other system.

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

    The rows are the same on both systems, the checksums are not.
    PowerShell on Windows ends each line it writes with two bytes, `0d 0a`
    (CRLF), where zsh writes `0a`: 34 921 bytes more, 930 699 against
    895 778.

!!! success "You should now see"
    `bikes_valid.csv` made again by one command, 34 921 lines, and the
    mean 38.5811 in `results/bikes_stats.txt`.

!!! question "Task: the script makes everything"
    Add the two files of the Task of section 13, `bridge.csv` and
    `park.csv`, and their means, `results/bridge_stats.txt` and
    `results/park_stats.txt`, to the script. Then delete everything in
    `data/processed` and in `results`, run the script, and list both
    folders.

??? note "Answer"
    Four lines at the end of the script, after the line that makes
    `bikes_valid.csv`, which they read:

    === "macOS"

        ```text
        grep -v ',park,' data/processed/bikes_valid.csv > data/processed/bridge.csv
        grep -v ',bridge,' data/processed/bikes_valid.csv > data/processed/park.csv
        python3 scripts/column_stats.py data/processed/bridge.csv bikes > results/bridge_stats.txt
        python3 scripts/column_stats.py data/processed/park.csv bikes > results/park_stats.txt
        ```

    === "Windows"

        ```text
        Select-String ',park,' data/processed/bikes_valid.csv -NotMatch -Raw > data/processed/bridge.csv
        Select-String ',bridge,' data/processed/bikes_valid.csv -NotMatch -Raw > data/processed/park.csv
        python scripts/column_stats.py data/processed/bridge.csv bikes > results/bridge_stats.txt
        python scripts/column_stats.py data/processed/park.csv bikes > results/park_stats.txt
        ```

    `*` stands for every name in a folder:

    ```text
    rm data/processed/*
    ```

    ```text
    rm results/*
    ```

    Then `./scripts/rebuild.sh` or `./scripts/rebuild.ps1`, `ls
    data/processed` and `ls results`: `bikes_valid.csv`, `bridge.csv`,
    `park.csv`, and `bikes_stats.txt`, `bridge_stats.txt`,
    `park_stats.txt`. `cat results/park_stats.txt` ends with `mean
    27.437`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: permission denied: ./scripts/rebuild.sh` | `chmod +x scripts/rebuild.sh` was skipped. Run it, then the script again |
    | `zsh: command not found: rebuild.sh`, or *not recognized* | The `./scripts/` in front is missing |
    | Windows: `… cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1: section 2, step 3. Or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |
    | macOS: `zsh: no matches found: results/*` | The folder is empty already. Go on |
    | `results/bikes_stats.txt` holds `no column bikes …` | `bikes_valid.csv` was empty or missing when the second line ran. Check the first line of the script against the page |

---

### 15. The script from the other system { #crlf }

**1:41 · 7 min**

**Tell the room.** Section 9 showed `0a` at the end of every line. VS Code
on Windows ends each line of a new file with two bytes, `0d 0a`: CRLF. The
Status Bar shows which. A script sent from a Windows laptop to a Mac
carries those bytes, and the Mac reads the `0d` as part of the line. Work
in pairs, one Mac and one Windows laptop; a room of one system watches the
projector for the other.

1. **Windows.** Open `scripts/rebuild.ps1`: the right end of the Status
   Bar reads `CRLF`. Show it to your Mac neighbour.

2. **macOS.** Make a copy of the script, as if the neighbour had written
   it, and give the copy Windows line ends: open
   `scripts/rebuild_win.sh`, select `LF` in the Status Bar, choose `CRLF`,
   save.

    ```text
    cp scripts/rebuild.sh scripts/rebuild_win.sh
    ```

    ```text
    hexdump -C -n 16 scripts/rebuild_win.sh
    ```

    ```text
    00000000  23 21 2f 62 69 6e 2f 7a  73 68 0d 0a 67 72 65 70  |#!/bin/zsh..grep|
    00000010
    ```

    ```text
    ./scripts/rebuild_win.sh
    ```

    ```text
    zsh: ./scripts/rebuild_win.sh: bad interpreter: /bin/zsh^M: no such file or directory
    ```

    `^M` is the byte `0d`. The Mac ends the first line at `0a` alone, so
    the name of the program is now `/bin/zsh` followed by `0d`, and no
    program has that name. The script does not run at all. Delete the
    copy:

    ```text
    rm scripts/rebuild_win.sh
    ```

3. **Windows.** Select `CRLF` in the Status Bar, choose `LF`, save, and
   run the script again:

    ```text
    ./scripts/rebuild.ps1
    ```

    Nothing is printed, and `bikes_valid.csv` is made again: PowerShell
    reads both line ends. To make VS Code write LF in every new file:
    `Ctrl+,`, search `eol`, set **Files: Eol** to `\n`.

!!! success "You should now see"
    On a Mac, `bad interpreter` for the copy with CRLF; on Windows, the
    script running with both line ends. A file that runs on one system
    can fail on another with no difference to see in the editor; the
    Status Bar shows it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: the copy still runs after choosing `CRLF` | The file was not saved after the switch |
    | macOS: `zsh: permission denied: ./scripts/rebuild_win.sh` | `cp` made the copy without the permission: `chmod +x scripts/rebuild_win.sh` |

---

### 16. The README: data, columns, how to rebuild { #readme }

**1:48 · 5 min**

**Tell the room.** A stranger who opens the project needs to know where
the data came from and which file it is, what each column means, which
value marks a missing one, and how every file in `data/processed` and
`results` is made again. The checksum is copied from the terminal, not
retyped.

1. Open `README.md` and its preview (`Ctrl+K`, then `V`). Add at the end,
   with the full checksum of section 7 pasted in place of the dots:

    ```text
    ## Data

    `data/raw/bikes.csv`: two bicycle counters, one row per counter and
    hour of 2024 and 2025, 35 088 rows, SHA-256 `2c68aad2…e3808991`.
    From [Seminar 4](https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis/workbook/seminars/seminar_04/)
    of the course workbook.

    | Column | Meaning | Unit |
    |--|--|--|
    | `time` | start of the hour | YYYY-MM-DDTHH:MM |
    | `counter` | `bridge` or `park` | none |
    | `bikes` | bicycles that passed in that hour | bicycles |

    Missing value: `bikes` is `9999` in 168 rows, the park counter from
    2025-03-10 to 2025-03-16, while it was broken.

    ## How to rebuild

    In the project folder: `./scripts/rebuild.sh` in zsh on macOS,
    `./scripts/rebuild.ps1` in PowerShell 7 on Windows. They make:

    - `data/processed/bikes_valid.csv`: `bikes.csv` without the rows
      marked `9999`, 34 921 lines
    - `results/bikes_stats.txt`: rows, smallest, largest and mean of
      `bikes` in it
    ```

2. If the Task of section 14 was done, add a line for each of the four
   files it makes. Save.

!!! success "You should now see"
    In the preview: **Data** with the checksum and a link, a table of three
    columns, the line about `9999`, and **How to rebuild** with the two
    scripts and what they make. The README gives no checksum for
    `bikes_valid.csv`: section 14 showed that it differs between macOS and
    Windows.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The table shows as plain text | The line of dashes under the header is missing, or the empty line before the table |
    | The checksum in the README was typed by hand | Copy it from the terminal instead: one wrong character and it names another file |

---

### 17. Wrap up { #wrap-up }

**1:53 · 3 min**

1. Git is needed next week. Check that it is there:

    ```text
    git --version
    ```

    ```text
    git version 2.…
    ```

2. Read the list of the day with the room:

    - Installs come first, in the system's terminal; VS Code starts after
      them and finds them. Its terminal runs `zsh` or PowerShell 7, with
      conda's `(base)` in the prompt.
    - The prompt shows the working directory; `pwd`, `ls`, `cd` move
      around, by relative or absolute paths; `Tab` and `↑` save typing.
    - A checksum shows that every laptop holds the same file.
    - A file is bytes: one per character here, and `0a` (LF) or `0d 0a`
      (CRLF) at the end of a line.
    - `|` joins filters, `>` writes a file. The sorted column showed `9999`
      at its top end: the mark for no count, in 168 rows, one week at the
      park. Counted as bicycles, it more than doubled the mean: 86.3
      against 38.6 an hour.
    - A script runs the day's lines again with one command; the README
      says what the files are and how to make them.

!!! success "You should now see"
    `git version 2.…` on every laptop, and the folder `bike-project` with a
    README, `bikes.csv`, `bikes_valid.csv`, `column_stats.py`, the rebuild
    script and `bikes_stats.txt`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `git: command not found`, or *not recognized* | The install of section 1 has not finished, or VS Code started before it did. Quit VS Code, start it again, `git --version` |
    | macOS: the developer tools are still installing | Let them finish after the session |

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
    ends every line with LF on every system. Add the line of step 3 to the
    rebuild script of section 14, and the file to **How to rebuild** in the
    README: `data/processed/monthly.csv`, 189 bytes, SHA-256
    `ea4ce2ce…19396ef6`.

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

**Tell the room.** Since section 1 every terminal starts in conda's
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
    | `conda: command not found`, or `The term 'conda' is not recognized` | conda is not on in this terminal: section 2, Watch for |
    | `EnvironmentNameNotFound: Could not find conda environment: bikez` | A typo, or `conda create` did not finish. `conda env list` shows the names |
    | `conda install numpy` ran with `(base)` in the prompt | numpy went into `base`. `conda remove numpy`, then `conda activate bikes` and install it again |
    | `environment.yml` still ends with `prefix:` | Delete that line and save |
    | Windows: `… cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1. Switch to PowerShell 7 (section 2, step 3), or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and answer `Y` |
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
        ```

        A second line, `monthly_export.csv: OK`, if section 18 was done.

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

### 22. Stop the script at the first error { #stop }

**— · 8 min**

**Tell the room.** A script runs on after a line fails, and its last line
decides what it reports. One typo can leave an empty file behind and a
wrong result in `results`, with nothing on the screen to say so. One line
on a Mac, two on Windows, make the script stop at the first error.

1. Put a typo into the first command of the script: `bike.csv` in place of
   `bikes.csv`. Save, run it, and ask for its status: `$?` holds the
   answer of the last command, `0` (`True`) when it worked.

    === "macOS"

        ```text
        ./scripts/rebuild.sh
        ```

        ```text
        grep: data/raw/bike.csv: No such file or directory
        ```

        ```text
        echo $?
        ```

        ```text
        1
        ```

    === "Windows"

        ```text
        ./scripts/rebuild.ps1
        ```

        ```text
        Select-String: C:\Users\smilte\bike-project\scripts\rebuild.ps1:1
        Line |
           1 |  Select-String ',9999$' data/raw/bike.csv -NotMatch -Raw > data/proces …
             |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             | Cannot find path 'C:\Users\smilte\bike-project\data\raw\bike.csv' because it does not exist.
        ```

        ```text
        $?
        ```

        ```text
        True
        ```

2. Look at what the script left behind.

    ```text
    cat results/bikes_stats.txt
    ```

    ```text
    no column bikes in data/processed/bikes_valid.csv
    the columns are:
    ```

    `>` emptied `bikes_valid.csv` before the first command failed, and the
    second command ran on the empty file. On Windows the script even
    reports `True`, because its last command worked.

3. Make it stop at the first error. Add as the second line:

    === "macOS"

        ```text
        set -e
        ```

    === "Windows"

        As the first two lines: the first stops at a failing PowerShell
        command, the second at a failing program such as `python`.

        ```text
        $ErrorActionPreference = 'Stop'
        $PSNativeCommandUseErrorActionPreference = $true
        ```

    Save and run it again.

    === "macOS"

        ```text
        grep: data/raw/bike.csv: No such file or directory
        ```

        ```text
        echo $?
        ```

        ```text
        2
        ```

    === "Windows"

        ```text
        Select-String: C:\Users\smilte\bike-project\scripts\rebuild.ps1:3
        Line |
           3 |  Select-String ',9999$' data/raw/bike.csv -NotMatch -Raw > data/proces …
             |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             | Cannot find path 'C:\Users\smilte\bike-project\data\raw\bike.csv' because it does not exist.
        ```

        ```text
        $?
        ```

        ```text
        False
        ```

    The script stopped at line 3 and reports the failure; the second
    command never ran.

4. Correct the typo, keep the new lines, and run the script once more:
   `bikes_valid.csv` has 34 921 lines again.

!!! success "You should now see"
    A script that reports `1` or `True` for a failed run, then `2` or
    `False` once it stops at the first error.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `set -e` as the first line, and `bad interpreter` | `#!/bin/zsh` must stay the first line |
    | `$?` prints `0` or `True` after the run | Another command ran in between. Run the script, then `$?` at once |

---

### 23. Aliases, the prompt and the start-up file { #settings }

**— · 12 min**

**Tell the room.** A shell runs a file of settings whenever it starts:
`~/.zshrc` for zsh, `$PROFILE` for PowerShell. conda's lines of section 1
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
        step 2 and conda's lines of section 1. Give conda its lines back
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
- How many bytes would `bikes.csv` take with CRLF at the end of every
  line? Predict it, then check on Windows with a copy saved by VS Code
  with `CRLF`: 900 314 + 35 089 = 935 403.
- How many counts have three digits? `grep -E -c ',[0-9]{3}$'` (section
  19) gives 4022; the Task of section 9 used it.

## If students ask for more

- `less FILE` on a Mac and `Get-Content FILE | more` in PowerShell show a
  long file one screen at a time: `Space` goes on, `q` leaves.
- `history` lists the commands typed in this terminal, in both shells.
- `Ctrl+R` searches the earlier commands as you type.
- `conda env remove -n bikes` deletes the environment of section 20;
  `conda env create -f environment.yml` makes it again.

## Aims practised

- 🔧 **Tool-agnostic:** the same work in two shells, and in VS Code.
- ♻️ **Reproducible:** a checksum that names the raw file, a README that
  says what each file is, and (section 20) an `environment.yml` from which
  any laptop makes the same environment.
- ⚙️ **Automation:** a script that makes every processed file and result
  again with one command.
- 📁 **Data & files:** a project folder from nothing, a file read byte by
  byte, raw data that is only read, a mark for missing values found and
  removed.
