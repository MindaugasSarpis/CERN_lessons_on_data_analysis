# Seminar 1 — Install Your Toolkit

**Paired lecture:** 01 Orientation & Motivation · **Format:** at home, after the first hands-on session · **~120 min**

> **Week 1 had no seminar.** The first session in class is
> [Seminar 2](seminar_02.md), which needs only VS Code. Do this brief at home
> afterwards, before **6 October**. Bring any error message you could not
> solve: a photo of the screen is enough.

**Suggested timing:** 0:00 Python · 0:40 Git · 1:10 check in VS Code · 1:40 notes in the README

> **This session builds:** a laptop with Python and Git installed, checked from
> inside VS Code.

## Goal
Have the three tools of the course working: VS Code (done in Seminar 2),
Python and Git.

## Prerequisites
[Seminar 2](seminar_02.md): VS Code installed, the `analysis-project` folder.

## Tasks
1. **Install Python** from [python.org/downloads](https://www.python.org/downloads/).
    - **Windows:** on the first screen of the installer tick
      **Add python.exe to PATH**, then *Install Now*.
    - **macOS:** run the downloaded installer and keep every default.
2. **Install Git** from [git-scm.com](https://git-scm.com).
    - **Windows:** run the installer and keep every default.
    - **macOS:** open the *Terminal* app, type `git --version` and press Enter.
      If Git is missing, macOS offers to install it; accept.
3. Close VS Code completely and start it again, so that it notices the new
   programs. Open your `analysis-project` folder.
4. Open the terminal inside VS Code: **Terminal → New Terminal**. A panel
   appears at the bottom. Type each line and press Enter:

    ```text
    python --version
    git --version
    ```

    Each prints a version number. If `python` is not found, try `python3`
    (macOS) or `py` (Windows).
5. In the Side Bar, create the file `scripts/hello.py` with one line:

    ```python
    print("ready")
    ```

    Run it from the terminal with `python scripts/hello.py`. It prints `ready`.
6. Tell Git who you are, once per computer. In the terminal:

    ```text
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```

    Nothing is printed; that is correct. Git itself starts in week 6.

## Stretch goals
- In VS Code open the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`) and
  install **Python** (publisher Microsoft). Open `hello.py` again: the code is
  now coloured, and a ▶ button at the top right runs it.
- Extend `hello.py` to report your setup:

    ```python
    import sys, platform
    print(platform.system(), sys.version.split()[0])
    ```

- Add an **Environment** note to `README.md`: your operating system, the
  Python version, and how you installed each tool.
- Install the **Rainbow CSV** extension and open your data file again.

## Wrap-up (last 10 min)
- Close VS Code, open it again, and re-run `python scripts/hello.py` to confirm
  that the setup survives a restart.
- Add one line to `README.md`: the installation step that surprised you most.

## If something does not work

| What you see | What to do |
|--|--|
| Windows: typing `python` opens the Microsoft Store | Python is not installed yet, or PATH was not ticked. Run the installer again, choose *Modify*, tick **Add python.exe to PATH**. Or use `py` |
| `git` or `python` "is not recognized" right after installing | Close VS Code and open it again |
| macOS: `python` not found | Use `python3` everywhere this course says `python` |
| macOS: a dialog about "command line developer tools" | Click *Install*; it takes a few minutes |

## Solution notes (instructor)
In 2026 this brief is homework after the first hands-on session (29 September)
and is checked by show of hands at the start of the next one. Nothing in
Seminar 2 depends on it. The first commit that used to close this brief has
moved to the Git week, where it is explained rather than recited.

## Aims practised
🔧 the same tools on every OS
