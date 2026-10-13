# Install Python and Git

**Format:** in class, [Seminar 4](seminar_04.md), sections 1 and 2 · about 20 min

**This page is the reference for the installs of Seminar 4**, for a helper at
a laptop: the same steps as the seminar, then every check and the usual
failures.
The full walkthrough of everything the course needs, with WSL2 as an
optional way on Windows, is [Setup](../setup.md).

| Program | What it is | macOS | Windows |
|--|--|--|--|
| the shell | reads the typed lines | `zsh`, built in | Git Bash, comes with Git |
| Git | keeps the versions of a project, from Seminar 6 | Homebrew | `winget` |
| Miniforge | Python with **conda**, which installs packages into environments; packages from **conda-forge** only | Homebrew | `winget` |

A **package manager** fetches a program, puts it in one known folder and on
`PATH`, and later updates or removes it: **Homebrew** (`brew`) on macOS,
**`winget`** on Windows. VS Code stays closed until the installs are done, so
that it finds them when it starts.

??? info "For the lecturer: a slow network"
    Thirty laptops downloading at once make the room's network slow. Start
    section 1 first thing, and keep the two zips of Seminar 4,
    `weather-scripts.zip` and `weather-project-s1.zip`, from the Releases page
    of `github.com/MindaugasSarpis/weather-project` on a USB stick.

---

## 1. Install the tools { #install }

**macOS:** in Terminal.app. **Windows:** in Windows PowerShell, which has
`winget`; only these two lines are typed there. One line at a time.

=== "macOS"

    1. `Cmd+Space`, type `Terminal`, `Enter`.
    2. Install Homebrew.

        ```text
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

        Type the laptop's password (nothing shows while typing), then
        `Enter`. It may install the developer tools of macOS first, 5 to
        15 minutes.

    3. At the end Homebrew prints **Next steps**. Copy the lines listed
       there, paste them, `Enter`. Check:

        ```text
        brew --version
        ```

        A line that starts with `Homebrew`.

    4. Git and Miniforge.

        ```text
        brew install git
        ```

        ```text
        brew install --cask miniforge
        ```

        The second ends with `🍺  miniforge was successfully installed!`

    5. Let conda set up `zsh`.

        ```text
        conda init zsh
        ```

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

    6. Quit Terminal: `Cmd+Q`.

=== "Windows"

    1. Windows key, type `powershell`, `Enter`.
    2. Git (with Git Bash) and Miniforge.

        ```text
        winget install --id Git.Git -e
        ```

        ```text
        winget install --id CondaForge.Miniforge3 -e
        ```

        Each ends with `Successfully installed`. Answer `Y` to the source
        agreements, **Yes** when Windows asks for permission. Miniforge
        goes into your user folder, `C:\Users\smilte\miniforge3`.

    3. Close the window. conda is set up in Git Bash, in section 2.

`conda init` writes a few lines into the file the shell runs whenever it
starts (`~/.zshrc` on macOS, `~/.bash_profile` in Git Bash): they switch on
conda's `base` environment, shown as `(base)` in the prompt.

---

## 2. Make the shell the terminal of VS Code { #profile }

1. Start VS Code, **File** > **Open Folder...** > `weather-project`.
2. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`):

    ```text
    Terminal: Select Default Profile
    ```

    Take **zsh** (macOS) or **Git Bash** (Windows). Not **bash**,
    **PowerShell** or **Command Prompt**.

3. Command Palette again:

    ```text
    Terminal: Create New Terminal
    ```

4. Windows only: let conda set up Git Bash, then close the terminal (the bin
   icon of the Panel) and open a new one, as in step 3.

    ```text
    ~/miniforge3/Scripts/conda.exe init bash
    ```

    ```text
    ==> For changes to take effect, close and re-open your current shell. <==
    ```

The prompt now starts with `(base)`.

---

## 3. Check the programs { #check }

In the terminal of VS Code. The lines are the same on both systems.

1. The shell.

    ```text
    echo $SHELL
    ```

    === "macOS"

        ```text
        /bin/zsh
        ```

    === "Windows"

        ```text
        /usr/bin/bash
        ```

2. Git.

    ```text
    git --version
    ```

    ```text
    git version 2.56.0
    ```

    Any from 2.40 on is fine.

3. conda.

    ```text
    conda --version
    ```

    ```text
    conda 26.7.2
    ```

4. Python: `python` on both systems.

    ```text
    python --version
    ```

    ```text
    Python 3.14.7
    ```

5. Where they come from.

    ```text
    which git python
    ```

    === "macOS"

        ```text
        /opt/homebrew/bin/git
        /opt/homebrew/Caskroom/miniforge/base/bin/python
        ```

    === "Windows"

        ```text
        /mingw64/bin/git
        /c/Users/smilte/miniforge3/python
        ```

**Check:** four version lines, and a Python inside Miniforge's folder.

---

## If something does not work { #troubleshooting }

| What you see | What to do |
|--|--|
| Windows: the terminal of VS Code says `powershell`, or its prompt starts with `PS` | Section 2 again: take **Git Bash**, then a new terminal |
| macOS: `echo $SHELL` prints `/bin/bash` | `chsh -s /bin/zsh`, the laptop's password, then quit VS Code (`Cmd+Q`) and start it again |
| **Git Bash** is not in the profile list | VS Code was open during the install. Quit it (**File** > **Exit**) and start it again |
| No `(base)` in the prompt; `conda: command not found` | `conda init zsh` (macOS, section 1) or `~/miniforge3/Scripts/conda.exe init bash` (Git Bash, section 2) did not run. Run it, then a new terminal |
| `python: command not found`, or Windows: `Python was not found; run without arguments to install from the Microsoft Store, …` | conda is not on in this terminal: the row above. Do not install Python from the Store |
| Windows: the same message with `(base)` in the prompt | **Settings** > **Apps** > **Advanced app settings** > **App execution aliases**: switch off **App Installer** `python.exe` and `python3.exe`. Restart VS Code |
| `git` or `conda` not found right after installing | Quit VS Code and start it again; closing the terminal is not enough |
| macOS: `zsh: command not found: brew` | The **Next steps** lines of Homebrew were not run. Run them, or open a new Terminal window |
| macOS: `zsh: command not found: conda` in Terminal.app | The same: Homebrew's folder is not on `PATH` yet. Then `conda init zsh` again |
| macOS: `xcode-select: note: No developer tools were found, requesting install.` | The developer tools are being installed. Wait for their window to finish, then run the Homebrew line again |
| Windows: `winget` is not recognized | Update **App Installer** in the Microsoft Store, then a new PowerShell window |
| Windows: `winget` asks about the source agreements | Type `Y`, `Enter` |
| Windows: `~/miniforge3/Scripts/conda.exe: No such file or directory` | Miniforge went elsewhere: `ls ~ /c/ProgramData` and look for `miniforge3`; or open **Miniforge Prompt** from Start and run `conda init bash` there |
| An installer asks for a password or an administrator's **Yes** the student does not have | The laptop is managed by the university or an employer. Pair with a neighbour today |
| VS Code runs in the browser (`vscode.dev`) | It has no terminal. Pair with a neighbour today |
| A download stalls | Wait, or run the line again; Homebrew and `winget` go on where they stopped |

## Aims practised

- 🔧 **Tool-agnostic:** the same check lines in zsh and Git Bash on every
  laptop.
- ⚙️ **Automation:** programs installed, updated and removed by typed lines.
