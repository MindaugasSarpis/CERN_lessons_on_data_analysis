# Seminar 1 — Set Up Your Toolkit & First Repo

**Paired lecture:** 01 Orientation & Data in Your Life · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **Running project — this session adds:** an empty project repository with the
> standard skeleton and your first commit.

## Goal
Leave the room with a working environment (terminal, Python, VS Code, Git) and an
initialised project you'll grow all course long.

## Prerequisites
A laptop with internet access. Nothing installed yet — that's what today is for.

## Tasks
1. Open a terminal and confirm each tool, installing any that are missing:
   `python --version` (or `python3`), `git --version`, `code --version`.
2. Create the project folder and skeleton:
   ```bash
   mkdir -p analysis-project/{data/raw,data/processed,scripts,results}
   cd analysis-project
   printf "# Analysis Project\n\nCourse running project.\n" > README.md
   ```
3. Open the folder in VS Code (`code .`) and look around the Explorer.
4. Verify Python works: create `scripts/hello.py` with `print("ready")` and run it.
5. Make the tools talk to each other: run `scripts/hello.py` from the VS Code
   *integrated* terminal, then extend it to report your setup:
   ```python
   import sys, platform
   print(platform.system(), sys.version.split()[0])
   ```
6. Make your **first commit** — a recipe for now, demystified in week 6:
   ```bash
   git init
   git config user.name "Your Name"       # once per machine: add --global
   git config user.email "you@example.com"
   git add -A
   git commit -m "Project skeleton"
   ```

## Stretch goals
- Add a `.gitignore` (even empty for now) and a `results/.gitkeep`.
- Set your Git identity: `git config --global user.name` / `user.email`.
- Install the VS Code Python and Markdown extensions and confirm `hello.py` gets
  syntax highlighting and linting.
- Add an **Environment** note to `README.md`: OS, Python version, and how you
  installed each tool — future-you will thank you.

## Wrap-up (last 10 min)
- Compare your tree against the skeleton in the
  [running-project overview](running-project.md) — it should match exactly.
- Re-run `python scripts/hello.py` in a *fresh* terminal to prove the setup
  survives a restart, then check `git log` shows your first commit.
- Add one line to `README.md`: the setup step that surprised you most.

## Solution notes (instructor)
The point is a *clean start*, not content. Circulate to fix install issues
(PATH, `python` vs `python3`, VS Code `code` command). Everyone should end with an
identical folder structure — this consistency pays off in every later seminar.
In the 120-minute slot, timebox installs (task 1) to ~30 minutes and help
stragglers individually while the room moves on — everyone must reach the first
commit in task 6.

## Aims practised
📁 organised from line one · 🔧 the same tools on every OS
