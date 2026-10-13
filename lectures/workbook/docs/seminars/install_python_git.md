# Install Python, Git and PowerShell 7

**Format:** in class, [Seminar 4](seminar_04.md), sections 1 and 2 · about 20 min

**This page is the reference for the installs of Seminar 4**, for a helper at
a laptop: the same steps as the seminar, then every check and the usual
failures.

| Program | What it is | Installed by |
|--|--|--|
| PowerShell 7 (`pwsh`) | the shell of the course, on macOS and Windows | Homebrew · `winget` |
| Git | keeps the versions of a project, from Seminar 5 | Homebrew · `winget` |
| Miniforge | Python with **conda**, which installs packages into environments; packages from **conda-forge** only | Homebrew · `winget` |

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
`winget`. One line at a time.

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

    4. The three programs. `powershell` asks for the password again.

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

    5. Let conda set up PowerShell.

        ```text
        conda init powershell
        ```

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

    6. Quit Terminal: `Cmd+Q`.

=== "Windows"

    1. Windows key, type `powershell`, `Enter`: Windows PowerShell 5.1.
    2. The three programs.

        ```text
        winget install --id Microsoft.PowerShell -e
        ```

        ```text
        winget install --id Git.Git -e
        ```

        ```text
        winget install --id CondaForge.Miniforge3 -e
        ```

        Each ends with `Successfully installed`. Answer `Y` to the source
        agreements, **Yes** when Windows asks for permission.

    3. Let conda set up PowerShell. Miniforge is in your user folder,
       `C:\Users\smilte\miniforge3`, and not yet on `PATH`.

        ```text
        & "$HOME\miniforge3\Scripts\conda.exe" init powershell
        ```

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

    4. Close the window.

`conda init powershell` writes a few lines into `profile.ps1`, a script that
PowerShell runs whenever it starts: they switch on conda's `base`
environment, shown as `(base)` before the prompt.

---

## 2. Make PowerShell 7 the terminal of VS Code { #profile }

1. Start VS Code, **File** > **Open Folder...** > `weather-project`.
2. Command Palette, `Ctrl+Shift+P` (macOS `Cmd+Shift+P`):

    ```text
    Terminal: Select Default Profile
    ```

    Take **pwsh** (macOS) or **PowerShell** (Windows). Not **zsh**,
    **bash**, **Windows PowerShell**, **Git Bash** or **Command Prompt**.

3. Command Palette again:

    ```text
    Terminal: Create New Terminal
    ```

    The top right of the Panel says `pwsh`; the prompt starts with
    `(base) PS`.

---

## 3. Check the programs { #check }

In the terminal of VS Code. The lines are the same on both systems.

1. The shell.

    ```text
    $PSVersionTable.PSVersion
    ```

    ```text
    Major  Minor  Patch  PreReleaseLabel BuildLabel
    -----  -----  -----  --------------- ----------
    7      6      6
    ```

    Any 7.4 or newer is fine.

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

5. Where Python comes from.

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

**Check:** four version lines, and a Python inside Miniforge's folder.

---

## If something does not work { #troubleshooting }

| What you see | What to do |
|--|--|
| The terminal of VS Code says `zsh` or `powershell`, or `$PSVersionTable.PSVersion` starts with `5` | Section 2 again: take **pwsh** / **PowerShell**, then a new terminal |
| **pwsh** or **PowerShell** is not in the profile list | VS Code was open during the install. Quit it (**File** > **Exit**, macOS `Cmd+Q`) and start it again |
| No `(base)` before the prompt, `conda` not recognized | `conda init powershell` did not run (section 1). Run it, then quit VS Code and start it again |
| Windows: `Python was not found; run without arguments to install from the Microsoft Store, …` | A stand-in of Windows answered, not Python: conda is not on in this terminal. See the row above. Do not install Python from the Store |
| Windows: the same message with `(base)` before the prompt | **Settings** > **Apps** > **Advanced app settings** > **App execution aliases**: switch off **App Installer** `python.exe` and `python3.exe`. Restart VS Code |
| Windows: `… profile.ps1 cannot be loaded because running scripts is disabled on this system` | The terminal is Windows PowerShell 5.1: section 2. Or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, answer `Y`, open a new terminal |
| `git`, `pwsh` or `conda` not recognized right after installing | Quit VS Code and start it again; closing the terminal is not enough |
| macOS: `zsh: command not found: brew` | The **Next steps** lines of Homebrew were not run. Run them, or open a new Terminal window |
| macOS: `zsh: command not found: conda` in Terminal.app | Homebrew's folder is not on `PATH` yet: the row above, then `conda init powershell` again |
| macOS: `xcode-select: note: No developer tools were found, requesting install.` | The developer tools are being installed. Wait for their window to finish, then run the Homebrew line again |
| Windows: `winget` is not recognized | Update **App Installer** in the Microsoft Store, then a new Windows PowerShell window |
| Windows: `winget` asks about the source agreements | Type `Y`, `Enter` |
| Windows: `… miniforge3\Scripts\conda.exe` not found | Miniforge went elsewhere. `Get-ChildItem $HOME -Filter miniforge3`; or open **Miniforge Prompt** from Start and run `conda init powershell` there |
| An installer asks for a password or an administrator's **Yes** the student does not have | The laptop is managed by the university or an employer. Pair with a neighbour today |
| VS Code runs in the browser (`vscode.dev`) | It has no terminal. Pair with a neighbour today |
| A download stalls | Wait, or try the line again; Homebrew and `winget` go on where they stopped |

## Aims practised

- 🔧 **Tool-agnostic:** the same shell and the same check lines on every
  laptop.
- ⚙️ **Automation:** programs installed, updated and removed by typed lines.
