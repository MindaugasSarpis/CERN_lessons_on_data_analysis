# Install Python, Git and PowerShell 7

**Format:** in class, [Seminar 4](seminar_04.md), Part 1 · about 20 min

**This page is the reference for Part 1 of Seminar 4.** The seminar page has
the same steps in the order the room does them. This page has them per
system, with every error message the room is likely to meet, so that a
helper at a laptop can look one up.

| Program | Windows | macOS | Needed from |
|--|--|--|--|
| A shell | PowerShell 7, installed today | `zsh`, built in | Seminar 4 |
| Python | from python.org, program name `python` | from python.org, program name `python3` | Seminar 4 (two handed-out scripts), Lecture 6 on |
| Git | Git for Windows | the developer tools of macOS | Seminar 5 |

Everything is installed in class, in Part 1 of Seminar 4.

??? info "For the lecturer: the USB stick"
    The network of the room is slow when 30 laptops download at once. Bring
    on a USB stick:

    - `PowerShell-7.6.6-win-x64.msi`, from the release page of PowerShell
      on GitHub (`github.com/PowerShell/PowerShell/releases`)
    - the Windows installer (64-bit) and the macOS installer of the current
      Python 3.14, from `python.org/downloads`
    - Git for Windows (64-bit), from `git-scm.com`
    - [`project_after_s1.zip`](../data/project_after_s1.zip),
      [`clean_pendulum.py`](../data/cli_clean_pendulum.py){ download="clean_pendulum.py" }
      and [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }

    The Git of macOS cannot go on a stick: it comes from Apple's servers
    when `git --version` is typed for the first time.

---

## 1. Start the downloads { #downloads }

Start everything slow first, then do something else while it runs.

=== "macOS"

    1. In VS Code select **Terminal** > **New Terminal** and type:

        ```text
        git --version
        ```

        A window asks to install the **command line developer tools**.
        Select **Install**, then **Agree**. The download takes 5 to 15
        minutes. Let it run. If the line prints `git version 2.…` instead,
        Git is already there.

    2. In the browser, open the address below and select
       **Download Python 3.14.…**.

        ```text
        python.org/downloads
        ```

=== "Windows"

    1. In VS Code select **Terminal** > **New Terminal**. This is Windows
       PowerShell 5.1, the terminal of Seminar 3. Install PowerShell 7 with
       one line:

        ```text
        winget install --id Microsoft.PowerShell --source winget
        ```

        `winget` downloads PowerShell 7 and installs it. It ends with
        `Successfully installed`. Let it run.

    2. In the browser, open the address below. Under the newest
       **Python 3.14** select **Download Windows installer (64-bit)**.

        ```text
        python.org/downloads/windows
        ```

    3. Open the address below and select **Download for Windows**, then the
       64-bit **Git for Windows Setup**.

        ```text
        git-scm.com
        ```


---

## 2. Install { #install }

=== "macOS"

    1. **Python.** Run the downloaded `python-3.14.…-macos11.pkg` and keep
       every default. At the end a Finder window opens: close it.

    2. **Git.** Wait until the developer tools have finished installing.

=== "Windows"

    1. **Python.** Run the downloaded `python-3.14.…-amd64.exe`. On the first
       screen tick **Add python.exe to PATH**, at the bottom. Then select
       **Install Now**, and **Close** at the end.

    2. **Git.** Run `Git-2.…-64-bit.exe`. Keep every default: select
       **Next** on each screen, then **Install**, then **Finish**.

    3. **PowerShell 7.** The `winget` line of step 1 ended with
       `Successfully installed`. If `winget` could not run, install
       `PowerShell-7.6.6-win-x64.msi` from the USB stick instead, with every
       default.

Then close VS Code completely, **File** > **Exit** (macOS `Cmd+Q`), and start it again,
so that it finds the new programs. Open `analysis-project` with **File** >
**Open Folder...** if it does not open by itself.

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

In the terminal of VS Code, in the project folder:

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

Each prints one line: `Python 3.14.…` and `git version 2.…`.

---

## 5. Tell Git who you are { #git-name }

Once per computer, with your own name and e-mail address. Seminar 5 writes
them into every version of the project. Both lines print nothing, which is
correct.

```text
git config --global user.name "Ada Lovelace"
```

```text
git config --global user.email "ada@example.com"
```

Check what Git has kept:

```text
git config --global --list
```

```text
user.name=Ada Lovelace
user.email=ada@example.com
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
| Windows: `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.` | Windows answers with a stand-in, not with Python. Python is not installed yet, or **Add python.exe to PATH** was not ticked. Run the installer again, select **Modify**, then **Next**, tick **Add Python to environment variables**, **Install**. Restart VS Code. Do not install from the Store |
| The same message after a correct installation | The stand-in comes first. Open **Settings** > **Apps** > **Advanced app settings** > **App execution aliases** and switch off the two **App Installer** entries `python.exe` and `python3.exe`. Restart VS Code. Until then, `py` works in place of `python` |
| `python` or `git`: `The term '…' is not recognized` right after installing | VS Code was open during the installation. Close it with **File** > **Exit** (macOS `Cmd+Q`) and start it again. Closing the terminal is not enough |
| Windows: `winget` is not recognized, or ends with an error | Install `PowerShell-7.6.6-win-x64.msi` from the USB stick, with every default |
| Windows: `winget` asks whether you agree to the source agreements | Type `Y` and `Enter` |
| Windows: an installer asks for an administrator password | The laptop is managed by the university or an employer. Pair with a neighbour for today, and ask the owner of the laptop to install the three programs |
| The laptop opens VS Code in the browser (`vscode.dev`) | The browser version has no terminal and cannot run Python. Pair with a neighbour for today |
| Windows: the version check prints `5` | The terminal is Windows PowerShell 5.1. Section 3 again: select the other PowerShell entry, close the old terminal, open a new one |
| Windows: **PowerShell** is not in the list, or is 5.1 | PowerShell 7 is not installed yet, or VS Code was open while it was installed. Restart VS Code, then select the profile again |
| macOS: `zsh: command not found: python` | Correct: on macOS the program is `python3`. Type `python3` everywhere this course writes `python` |
| macOS: `python3 --version` prints `Python 3.9.6` | That is the Python of Apple's developer tools. The python.org Python is not installed yet, or the terminal was opened before it was. Install it, then restart VS Code |
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
  shell, the Python version and the Git version that the checks printed.

## Aims practised

🔧 the same three tools on every laptop, checked by one typed line each
