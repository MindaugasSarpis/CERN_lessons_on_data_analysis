# Install Python, Git and PowerShell 7

**Format:** in class, [Seminar 4](seminar_04.md), sections 1, 6 and 13 · about 20 min

**This page is the reference for the installs of Seminar 4.** The seminar page has
the same steps in the order the room does them. This page has them per
system, with every error message the room is likely to meet, so that a
helper at a laptop can look one up.

| Program | Windows | macOS | Needed from |
|--|--|--|--|
| A shell | PowerShell 7, installed today | `zsh`, built in | Seminar 4 |
| Python | from Miniforge, with conda; program name `python` | from Miniforge, with conda; program name `python3` | Seminar 4 (two handed-out scripts), Lecture 6 on |
| Git | Git for Windows | the developer tools of macOS | Seminar 5 |

**Miniforge** installs **conda**, a program that installs packages and keeps
them apart in environments, and a first environment, `base`, with Python in
it. Its packages come from **conda-forge**, a free collection kept by
volunteers. Every terminal that knows conda shows `(base)` before its
prompt.

Everything is installed in class, in Seminar 4: the installs of PowerShell 7
and Git and the download of Miniforge start in section 1, VS Code switches
to PowerShell 7 in section 6, and Miniforge is installed in section 13,
where the first script needs Python.

??? info "For the lecturer: the USB stick"
    The network of the room is slow when 30 laptops download at once. Bring
    on a USB stick:

    - `PowerShell-7.6.6-win-x64.msi`, from the release page of PowerShell
      on GitHub (`github.com/PowerShell/PowerShell/releases`)
    - the three Miniforge installers, from
      `github.com/conda-forge/miniforge/releases/latest`, with these exact
      names: `Miniforge3-Darwin-arm64.sh` (a Mac with an Apple chip),
      `Miniforge3-Darwin-x86_64.sh` (a Mac with an Intel chip) and
      `Miniforge3-Windows-x86_64.exe`. The install line of a Mac expects
      the name of its own chip
    - Git for Windows (64-bit), from `git-scm.com`
    - the two files of Seminar 4: [`bikes_hourly.csv`](../data/bikes_hourly.csv){ download="bikes.csv" }
      and [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" };
      for its optional section 18,
      [`bikes_monthly_export.csv`](../data/bikes_monthly_export.csv){ download="monthly_export.csv" }
      and [`clean_export.py`](../data/cli_clean_export.py){ download="clean_export.py" };
      and the fallback [`bikes_project.zip`](../data/bikes_project.zip)

    The Git of macOS cannot go on a stick: it comes from Apple's servers
    when `git --version` is typed for the first time.

---

## 1. Start the downloads { #downloads }

Start everything slow first, then do something else while it runs.

=== "macOS"

    1. Press `Cmd+Space`, type `Terminal` and press `Enter` (the terminal
       of VS Code works too). Ask for Git:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. The download takes 5 to 15
        minutes. Let it run. If the line prints `git version 2.…` instead,
        Git is already there.

    2. In the same terminal, fetch the Miniforge installer into
       **Downloads**:

        ```text
        cd ~/Downloads
        ```

        ```text
        curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
        ```

        `$(uname)` and `$(uname -m)` fill in `Darwin` and the chip, `arm64`
        or `x86_64`. A table counts the download up to `100`.

=== "Windows"

    1. Press the Windows key, type `powershell` and press `Enter`: Windows
       PowerShell 5.1, built into Windows. `winget`, a program that
       installs other programs, comes with it. Install PowerShell 7, then
       Git:

        ```text
        winget install --id Microsoft.PowerShell --source winget
        ```

        ```text
        winget install --id Git.Git --source winget
        ```

        Each ends with `Successfully installed`. Let them run.

    2. In the browser, open the address below. The browser saves
       `Miniforge3-Windows-x86_64.exe` in **Downloads**.

        ```text
        github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
        ```

        Not `winget`: the Miniforge it offers is from 2022.


---

## 2. Install { #install }

=== "macOS"

    1. **Miniforge.** In the terminal of VS Code:

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

        The last answer lets the installer add a few lines to `~/.zshrc`,
        the file `zsh` runs whenever it starts, so that every new terminal
        finds conda. It ends with `Thank you for installing Miniforge3!`

    2. **Git.** Wait until the developer tools have finished installing.

=== "Windows"

    1. **Miniforge.** Run `Miniforge3-Windows-x86_64.exe` from
       **Downloads**. Select **Next** and **I Agree**, choose **Just Me
       (recommended)**, and keep every other default: the folder
       `C:\Users\smilte\miniforge3`, the boxes as they are, **Install**, then
       **Finish**. No administrator password is needed.

    2. **conda in PowerShell.** Press the Windows key, type
       `Miniforge Prompt` and press `Enter`. In the window that opens:

        ```text
        conda init powershell
        ```

        It adds a few lines to `profile.ps1`, a script every PowerShell
        runs when it starts, in `Documents\PowerShell` and in
        `Documents\WindowsPowerShell`. It ends with:

        ```text
        ==> For changes to take effect, close and re-open your current shell. <==
        ```

        Close the Miniforge Prompt.

    3. **PowerShell 7 and Git.** The two `winget` lines of step 1 ended
       with `Successfully installed`. If `winget` could not run, install
       `PowerShell-7.6.6-win-x64.msi` and Git for Windows from the USB stick
       instead: every default, **Next** on each screen, then **Install**
       and **Finish**.

Then close VS Code completely, **File** > **Exit** (macOS `Cmd+Q`), and start
it again, so that its terminal runs the new start-up lines and finds the new
programs. Open `bike-project` with **File** > **Open Folder...** if it does
not open by itself.

---

## 3. Make PowerShell 7 the terminal (Windows only) { #profile }

VS Code lists the shells it found under the `+` of the Panel. After the
installation it knows two PowerShells:

| Name in VS Code | What it is | Its version check prints |
|--|--|--|
| **PowerShell** | PowerShell 7, the shell of this course | `7` |
| **Windows PowerShell** | Windows PowerShell 5.1, built into Windows | `5` |

1. Press `Ctrl+Shift+P` and type:

    ```text
    default profile
    ```

    Select **Terminal: Select Default Profile**, then **PowerShell**.

2. Close the open terminal with the bin icon at the top right of the Panel.
   Select **Terminal** > **New Terminal**. The name at the top right of the
   Panel reads `pwsh`.

3. Check the version:

    ```text
    $PSVersionTable.PSVersion.Major
    ```

    ```text
    7
    ```

If it prints `5`, the terminal is still Windows PowerShell 5.1. Select the
default profile again and take the other PowerShell entry: the right one is
the one whose version check prints `7`. The list also shows **Git Bash**
and **Command Prompt**. They are not used in this course.

---

## 4. Check the programs { #check }

In a new terminal of VS Code, in the project folder. The prompt starts with
`(base)`.

=== "macOS"

    ```text
    conda --version
    ```

    ```text
    python3 --version
    ```

    ```text
    git --version
    ```

=== "Windows"

    ```text
    conda --version
    ```

    ```text
    python --version
    ```

    ```text
    git --version
    ```

Each prints one line: `conda 26.7.2`, `Python 3.14.7` and `git version 2.…`.

---

## 5. Tell Git who you are { #git-name }

Once per computer, with your own name and e-mail address. Seminar 5 writes
them into every version of the project. Both lines print nothing, which is
correct.

```text
git config --global user.name "Smiltė"
```

```text
git config --global user.email "smilte@example.com"
```

Check what Git has kept:

```text
git config --global --list
```

```text
user.name=Smiltė
user.email=smilte@example.com
```

---

## 6. A first script { #hello }

1. In the Side Bar select the `scripts` folder, then **New File**, and name
   it `hello.py`. Type one line into it and save:

    ```text
    print("ready")
    ```

2. Run it from the project folder.

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

A laptop that prints `ready` is ready for the course.

---

## If something does not work { #troubleshooting }

| What you see | What it means, and what to do |
|--|--|
| No `(base)` before the prompt of a new terminal | conda was not added to the start-up file of the shell. macOS: `~/miniforge3/bin/conda init zsh`. Windows: `conda init powershell` in the Miniforge Prompt. Then quit VS Code and start it again |
| macOS: `zsh: command not found: conda` | The same: the last question of the installer was answered with `Enter`, which means no. `~/miniforge3/bin/conda init zsh`, then a new terminal |
| Windows: `conda : The term 'conda' is not recognized …` | `conda init powershell` was not run in the Miniforge Prompt, or VS Code was open during the install. Run it, then quit VS Code and start it again |
| Windows: `… profile.ps1 cannot be loaded because running scripts is disabled on this system` | The script that conda added cannot run. In Windows PowerShell 5.1 that is the default: switch to PowerShell 7 (section 3). Or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, answer `Y`, and open a new terminal |
| Windows: `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.` | Windows answers with a stand-in, not with Python: conda is not on in this terminal. See the rows above. Do not install Python from the Store |
| Windows: the same message with `(base)` before the prompt | The stand-in comes first. Open **Settings** > **Apps** > **Advanced app settings** > **App execution aliases** and switch off the two **App Installer** entries `python.exe` and `python3.exe`. Restart VS Code |
| Windows: "Windows protected your PC" when the Miniforge installer starts | Select **More info**, then **Run anyway** |
| `git`: `The term '…' is not recognized` or `command not found` right after installing | VS Code was open during the installation. Close it with **File** > **Exit** (macOS `Cmd+Q`) and start it again. Closing the terminal is not enough |
| Windows: `winget` is not recognized, or ends with an error | Install `PowerShell-7.6.6-win-x64.msi` and Git for Windows from the USB stick, with every default |
| Windows: `(base)` shows in Windows PowerShell but not in PowerShell 7 | `conda init powershell` ran before PowerShell 7 was installed, so it found only 5.1. Run it again in the Miniforge Prompt, then restart VS Code |
| Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
| Windows: an installer asks for an administrator password | The laptop is managed by the university or an employer. Miniforge (**Just Me**) needs none; for PowerShell 7 and Git, pair with a neighbour today and ask the owner of the laptop to install them |
| The laptop opens VS Code in the browser (`vscode.dev`) | The browser version has no terminal and cannot run Python. Pair with a neighbour for today |
| Windows: the version check prints `5` | The terminal is Windows PowerShell 5.1. Section 3 again: select the other PowerShell entry, close the old terminal, open a new one |
| Windows: **PowerShell** is not in the list, or is 5.1 | PowerShell 7 is not installed yet, or VS Code was open while it was installed. Restart VS Code, then select the profile again |
| macOS: `python3 --version` prints `Python 3.9.6` | That is the Python of Apple's developer tools: conda is not on in this terminal. See the first row |
| macOS: `bash: /Users/smilte/Downloads/Miniforge3-…: No such file or directory` | The download did not finish, or the file has another name. `ls ~/Downloads`; from the USB stick, take the file whose name ends in the chip of this Mac (`uname -m` prints it) |
| macOS: `ERROR: File or directory already exists: '/Users/smilte/miniforge3'` | Miniforge is installed already, from an earlier try. Skip to the check of section 4 |
| macOS: `curl: (6) Could not resolve host: github.com` | No network. Copy the installer from the USB stick into **Downloads** |
| macOS: `xcode-select: note: No developer tools were found, requesting install.` | Correct: the developer tools are being installed. Wait for their window to finish, then type `git --version` again |
| A download stalls | Copy the installer from the USB stick |

---

## Stretch goals

For a laptop that is ready early.

- In VS Code open the Extensions view (`Ctrl+Shift+X`, macOS
  `Cmd+Shift+X`) and install **Python**, published by Microsoft. Open
  `hello.py` again: the code is coloured, and a ▶ button at the top right
  runs it.
- Make `hello.py` report the setup, and run it again:

    ```text
    import sys, platform
    print(platform.system(), sys.version.split()[0])
    ```

- Add an **Environment** section to `README.md`: the operating system, the
  shell, and the conda, Python and Git versions that the checks printed.

## Aims practised

🔧 the same three tools on every laptop, checked by one typed line each
