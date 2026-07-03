# Seminar 1 — Set Up Your Toolkit & First Repo

**Paired lecture:** 01 Orientation & Data in Your Life · **Format:** hands-on · **~90 min**

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
   mkdir -p dimuon-analysis/{data/raw,data/processed,scripts,results}
   cd dimuon-analysis
   printf "# Dimuon Analysis\n\nCourse running project.\n" > README.md
   ```
3. Open the folder in VS Code (`code .`) and look around the Explorer.
4. Verify Python works: create `scripts/hello.py` with `print("ready")` and run it.

## Stretch goals
- Add a `.gitignore` (even empty for now) and a `results/.gitkeep`.
- Set your Git identity: `git config --global user.name` / `user.email`.

## Solution notes (instructor)
The point is a *clean start*, not content. Circulate to fix install issues
(PATH, `python` vs `python3`, VS Code `code` command). Everyone should end with an
identical folder structure — this consistency pays off in every later seminar.

## Aims practised
📁 organised from line one · 🔧 the same tools on every OS
