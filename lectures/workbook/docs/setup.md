# Setup

Everything the course needs on a laptop, step by step. The seminars install
the same things in class (VS Code in [Seminar 1](seminars/seminar_01.md),
the rest in [Seminar 4](seminars/seminar_04.md)); this page is for doing it
before, or catching up after.

| Program | What it is for | First used |
|--|--|--|
| **VS Code** | the editor, with a terminal inside | Seminar 1 |
| **the shell** | reads typed commands: zsh on macOS, Git Bash on Windows | Seminar 4 |
| **Git** | keeps the versions of a project | Seminar 6 |
| **Miniforge** | Python with **conda**, which installs packages into environments | Seminar 4 |
| **a GitHub account** | a copy of your project online | Seminar 6 |

**Windows: two ways.** **Git Bash** comes with Git and is what the seminars
show; take it if unsure. **WSL2** runs a real Linux (Ubuntu) inside Windows,
the same system as research clusters; it is optional and takes longer to set
up. Pick one and follow its tab all the way.

About 30 minutes (Windows with WSL2: 45), most of it downloading. Keep VS
Code closed until step 4.

---

## 1. VS Code { #vscode }

=== "macOS"

    1. Download from [code.visualstudio.com](https://code.visualstudio.com),
       open the zip, drag **Visual Studio Code** into **Applications**.
    2. Open it once from **Applications**, then quit it.

=== "Windows · Git Bash"

    1. Download the **User Installer** from
       [code.visualstudio.com](https://code.visualstudio.com) and run it.
    2. Keep **Add to PATH** ticked. Finish, then close VS Code.

=== "Windows · WSL2"

    1. Download the **User Installer** from
       [code.visualstudio.com](https://code.visualstudio.com) and run it.
    2. Keep **Add to PATH** ticked. Finish, then close VS Code.

**Check:** VS Code opens and closes.

---

## 2. The package manager and the shell { #shell }

A **package manager** downloads a program, puts it in one known place, and
later updates or removes it.

=== "macOS"

    The shell is **zsh**, built in. The package manager is **Homebrew**.

    1. `Cmd+Space`, type `Terminal`, `Enter`.
    2. Install Homebrew; type the laptop's password when asked (nothing
       shows while typing).

        ```text
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

    3. At the end it prints **Next steps**: copy those lines, paste them,
       `Enter`.
    4. Check.

        ```text
        brew --version
        ```

        A line that starts with `Homebrew`.

=== "Windows · Git Bash"

    The package manager is **winget**, built into Windows 10 and 11. Git Bash
    arrives with Git in step 3.

    1. `Start`, type `PowerShell`, `Enter`. Only steps 2 and 3 are typed
       here.
    2. Check winget.

        ```text
        winget --version
        ```

        A line such as `v1.11.430`. Missing: install **App Installer** from
        the Microsoft Store.

=== "Windows · WSL2"

    WSL2 runs Ubuntu inside Windows. Its shell is **bash**, its package
    manager **apt**. Needs Windows 10 (2004 or later) or 11, and an
    administrator account.

    1. `Start`, type `PowerShell`, right-click **Run as administrator**.
    2. Install WSL2 with Ubuntu.

        ```text
        wsl --install
        ```

    3. Restart Windows when it asks. Ubuntu then opens by itself (or:
       `Start` > **Ubuntu**) and asks for a **user name** and a
       **password**: small letters, no spaces; the password shows nothing
       while typing. Keep it: `sudo` asks for it.
    4. Check, in PowerShell.

        ```text
        wsl -l -v
        ```

        ```text
          NAME      STATE           VERSION
        * Ubuntu    Running         2
        ```

    5. In Ubuntu, update the package list.

        ```text
        sudo apt update
        ```

**Check:** `brew --version`, `winget --version` or `wsl -l -v` answers.

---

## 3. Git and Miniforge { #git-python }

=== "macOS"

    In Terminal:

    1. Git.

        ```text
        brew install git
        ```

    2. Miniforge.

        ```text
        brew install --cask miniforge
        ```

    3. Let zsh find conda, then close Terminal.

        ```text
        conda init zsh
        ```

=== "Windows · Git Bash"

    In the PowerShell window of step 2:

    1. Git, with Git Bash. Accept the questions; the defaults are right.

        ```text
        winget install --id Git.Git -e
        ```

    2. Miniforge.

        ```text
        winget install --id CondaForge.Miniforge3 -e
        ```

    3. Close PowerShell. The rest happens in VS Code (step 4).

=== "Windows · WSL2"

    In Ubuntu:

    1. Git (Ubuntu usually has it; this makes sure).

        ```text
        sudo apt install -y git unzip
        ```

    2. Download the Miniforge installer for Linux.

        ```text
        curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
        ```

    3. Install it into `~/miniforge3`, without questions.

        ```text
        bash Miniforge3-$(uname)-$(uname -m).sh -b
        ```

    4. Let bash find conda, then close Ubuntu.

        ```text
        ~/miniforge3/bin/conda init bash
        ```

**Check:** no red error at the end of each line.

---

## 4. The terminal of VS Code { #terminal }

=== "macOS"

    1. Open VS Code, then **View** > **Terminal**. The panel names `zsh`.
    2. The prompt starts with `(base)`: conda is ready.

=== "Windows · Git Bash"

    1. Open VS Code. `Ctrl+Shift+P`, type **Terminal: Select Default
       Profile**, `Enter`, take **Git Bash**.
    2. **View** > **Terminal**. The panel names `bash`.
    3. Let Git Bash find conda.

        ```text
        ~/miniforge3/Scripts/conda.exe init bash
        ```

    4. Close the terminal (bin icon), open a new one. The prompt starts
       with `(base)`.

=== "Windows · WSL2"

    1. Open VS Code. **Extensions** (`Ctrl+Shift+X`), search **WSL**,
       install the one by Microsoft.
    2. `Ctrl+Shift+P`, type **WSL: Connect to WSL**, `Enter`. A new window
       opens; the bottom-left corner says **WSL: Ubuntu**.
    3. **View** > **Terminal**. It is bash in Ubuntu; the prompt starts
       with `(base)`.
    4. Always open course folders from this window (**File** > **Open
       Folder...**), and keep them in the Linux home folder (`~`), not under
       `/mnt/c`: that is much faster.

**Check:** a terminal in VS Code with `(base)` at the start of the prompt.

---

## 5. Check everything { #check }

In the terminal of VS Code. The lines are the same on every system.

1. Git.

    ```text
    git --version
    ```

    A line such as `git version 2.51.0`.

2. conda.

    ```text
    conda --version
    ```

    A line such as `conda 26.7.2`.

3. Python, from Miniforge.

    ```text
    python --version
    ```

    A line such as `Python 3.14.7`.

4. Which Python runs.

    ```text
    which python
    ```

    | System | The path contains |
    |--|--|
    | macOS | `miniforge` |
    | Windows · Git Bash | `/c/Users/<you>/miniforge3/python` |
    | Windows · WSL2 | `/home/<you>/miniforge3/bin/python` |

**Check:** four answers, none `command not found`.

---

## 6. Git: your name, and a GitHub account { #github }

1. Your name and e-mail, as they will appear on every commit.

    ```text
    git config --global user.name "Your Name"
    ```

    ```text
    git config --global user.email "you@example.org"
    ```

2. Let `git pull` join two histories with a merge.

    ```text
    git config --global pull.rebase false
    ```

3. [github.com](https://github.com) > **Sign up**, with the same e-mail. The
   username is in the address of every repository you make.

**Check:** `git config --global --list` shows your name and e-mail; you can
sign in on github.com.

On WSL2, Git in Ubuntu and Git for Windows are two programs with two
settings; set them in Ubuntu.

---

## 7. Two VS Code extensions { #extensions }

**Extensions** (`Ctrl+Shift+X`, macOS `Cmd+Shift+X`). On WSL2, install them
in the **WSL: Ubuntu** window.

1. **Python** (by Microsoft): runs and checks Python files, from Seminar 5.
2. **Hex Editor** (by Microsoft): shows a file as bytes, Seminar 3.

**Check:** both listed under **Installed**.

---

## If something does not work { #troubleshooting }

| On the screen | What to do |
|--|--|
| `conda: command not found`, no `(base)` | The `conda init` line of step 3 (macOS, WSL2) or step 4 (Git Bash) did not run. Run it, then a new terminal |
| `python: command not found`, or Python from Microsoft Store opens (Windows) | **Settings** > **Apps** > **Advanced app settings** > **App execution aliases**: switch off `python.exe` and `python3.exe`. New terminal |
| macOS: `zsh: command not found: brew` | The **Next steps** lines of Homebrew were not run: step 2.3 |
| Windows: no **Git Bash** in **Select Default Profile** | Git is missing or VS Code was open during the install: step 3, then restart VS Code |
| Windows: `~/miniforge3/Scripts/conda.exe: No such file or directory` | Miniforge went elsewhere: `ls ~ /c/ProgramData`, find `miniforge3`, use that path |
| `wsl --install` says virtualisation is off | Switch on **Virtualization** (Intel VT-x or AMD-V) in the laptop's BIOS/UEFI, or use Git Bash instead |
| WSL2: a file downloaded in Windows is needed in Ubuntu | `cp /mnt/c/Users/<you>/Downloads/FILE ~` |
| No administrator rights | macOS and Git Bash work without; WSL2 needs them |

Not tried on every laptop: the exact Homebrew, winget and WSL screens, and
the version numbers, which change with each release.
