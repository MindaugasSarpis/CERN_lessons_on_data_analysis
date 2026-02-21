# L8: Version Control with Git

---

## Overview

**Duration**: 90-120 minutes (lecture + hands-on)

**Prerequisites**: L3 (command line basics), L5 (Python — for understanding what files to track)

**Learning Objectives**:
- Explain why version control is essential for scientific work
- Initialise a git repository and make commits
- Use the staging area to control what goes into each commit
- Read diffs and logs to understand project history
- Push to and pull from a remote repository (GitHub)
- Create branches, merge them, and resolve conflicts
- Write a `.gitignore` and follow a daily git workflow

---

## Lecture Structure

### Part 1: Why Version Control? (10 min)
- The problem: `report_v2_final_FINAL_v3.docx`
- What version control gives you: history, collaboration, safety net
- Git = the standard (used at CERN, in industry, everywhere)
- Brief: Git vs GitHub (tool vs hosting platform)

### Part 2: First Steps (20 min)
- Configure git: `git config --global user.name` / `user.email`
- `git init` — create a repository
- `git status` — your most-used command
- The three states: working directory → staging area → repository
- `git add` → `git commit -m "message"`
- **Live demo**: Create a repo, add a Python script, commit it

### Part 3: Understanding History (15 min)
- `git log` and `git log --oneline --graph`
- `git diff` — reading changes (green = added, red = removed)
- `git diff --staged` — what's about to be committed
- Commit messages: imperative mood, short summary + optional body
- **Interactive**: Students make 3 commits with meaningful messages

### Part 4: Undoing Things (10 min)
- `git restore <file>` — discard working directory changes
- `git restore --staged <file>` — unstage a file
- `git revert <hash>` — undo a commit safely (creates new commit)
- `git reset --hard` — nuclear option (explain but discourage)
- Key message: git almost never loses data — if it's committed, it's recoverable

### Part 5: Ignoring Files (10 min)
- Why: data files, compiled code, secrets, OS files
- `.gitignore` syntax: patterns, wildcards, negation
- Show Python-specific `.gitignore` template
- Rule: track code and config, not data or outputs

### Part 6: Remotes & GitHub (15 min)
- SSH key setup (or HTTPS with token)
- `git remote add origin <url>`
- `git push -u origin main`
- `git pull` — always pull before starting work
- `git clone` — starting from an existing repo
- **Live demo**: Push to GitHub, show it in the browser

### Part 7: Branches & Merging (20 min)
- Why branch? Parallel development, experiments, features
- `git switch -c feature-branch`
- Work on branch, commit, `git switch main`, `git merge feature-branch`
- Merge conflicts: what they look like, how to resolve them
- `git branch -d feature-branch` — clean up
- **Live demo**: Create a conflict intentionally, resolve it together

---

## Teaching Tips

### Common Student Struggles

1. **"I committed to the wrong branch"**
   - Don't panic — git has solutions for everything
   - Show `git log` to verify where you are
   - For simple cases: cherry-pick or re-make the commit on the right branch

2. **"What's the staging area for?"**
   - Analogy: packing a suitcase. Staging = putting items on the bed to review. Commit = closing the suitcase.
   - It lets you commit part of your changes (e.g., fix A but not unfinished feature B)

3. **"I get merge conflicts and don't know what to do"**
   - Walk through conflict markers step-by-step: `<<<<<<<`, `=======`, `>>>>>>>`
   - "YOUR changes are on top, THEIR changes are on bottom"
   - Delete the markers, keep what you want, save, add, commit
   - Practice resolving 2-3 conflicts in class

4. **"SSH keys are confusing"**
   - Walk through step-by-step: `ssh-keygen`, copy public key, paste in GitHub settings
   - Have a backup plan: HTTPS with personal access token
   - Some students will need 1-on-1 help with this

5. **"I'm afraid of breaking something"**
   - If it's committed, it's safe — git doesn't lose committed data
   - Use `git status` constantly — it tells you what state you're in
   - Worst case: `git clone` a fresh copy

### Interactive Elements

- **Live demos are essential**: Students follow along on their machines
- **learngitbranching.js.org**: Send students here for visual practice
- **Pair exercise**: One student creates a repo, the other clones and contributes
- **Conflict resolution practice**: Give students a pre-made repo with conflicting branches

---

## Common Questions & Answers

**Q**: Git or GitHub?
**A**: Git is the tool (runs on your computer). GitHub is a hosting platform (stores repos online). You can use git without GitHub. GitLab and Bitbucket are alternatives to GitHub.

**Q**: How often should I commit?
**A**: Commit when you complete a logical unit of work. "Add data loading function" is good. "Did some stuff" is bad. Multiple small commits > one giant commit.

**Q**: Should I put data files in git?
**A**: Generally no. Git is for code, config, and documentation. Large data files belong in data storage (cloud drives, databases, git-lfs for special cases). Add data paths to `.gitignore`.

**Q**: Can I undo a `git push`?
**A**: Yes, with `git revert` (safe: creates a new commit that undoes the change). Never use `git push --force` on shared branches — it rewrites history others depend on.

**Q**: Do I need the command line, or can I use a GUI?
**A**: Learning the command line first gives you understanding. Once comfortable, GUIs (VS Code git panel, GitHub Desktop, GitKraken) are great for daily use. Most professionals use a mix.

---

## Key Reference Tables

### Git Command Cheat Sheet

| Command | What It Does |
|---------|-------------|
| `git init` | Create a new repository |
| `git status` | Show current state |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save staged changes |
| `git log --oneline` | Show commit history (compact) |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git restore <file>` | Discard changes in working directory |
| `git restore --staged <file>` | Unstage a file |
| `git revert <hash>` | Undo a commit (safely) |
| `git remote add origin <url>` | Connect to remote |
| `git push -u origin main` | Push to remote (first time) |
| `git push` | Push to remote (subsequent) |
| `git pull` | Fetch + merge from remote |
| `git clone <url>` | Copy a remote repository |
| `git switch -c <branch>` | Create and switch to new branch |
| `git switch main` | Switch to main branch |
| `git merge <branch>` | Merge branch into current branch |
| `git branch -d <branch>` | Delete a branch |

### Commit Message Best Practices

```
<type>: <short summary in imperative mood>

Optional longer description explaining WHY, not WHAT.
The diff shows WHAT changed — the message explains WHY.
```

Good examples:
- `Add data loading function for CSV files`
- `Fix off-by-one error in histogram binning`
- `Update README with installation instructions`

Bad examples:
- `fixed stuff`
- `WIP`
- `asdfgh`
- `final version`

### Python `.gitignore` Template

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/

# Virtual environments
venv/
.venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Data (track code, not data)
*.csv
*.h5
*.root
data/

# Jupyter
.ipynb_checkpoints/

# Secrets
.env
*.key
```

### Daily Workflow

```
1. git pull                    # Get latest changes
2. git switch -c my-feature    # Create a branch
3. (edit files)                # Do your work
4. git add file1.py file2.py   # Stage changes
5. git commit -m "Add feature" # Commit
6. git push -u origin my-feature  # Push branch
7. Open Pull Request on GitHub    # Request review
```

---

## Time Estimates

- Lecture (Parts 1-5): 65 min
- Live demos (throughout): 20 min
- Student hands-on (Parts 6-7): 25 min
- Q&A: 10 min
- **Total**: ~120 min

---

## Resources for Students

- [Learn Git Branching](https://learngitbranching.js.org/) — interactive visual tutorial
- [Pro Git book](https://git-scm.com/book/en/v2) (free online)
- [GitHub SSH key setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Oh My Git!](https://ohmygit.org/) — game-based git learning
- [git - the simple guide](https://rogerdudler.github.io/git-guide/)

---

## Assessment Ideas

- **Quiz**: "What does `git add` do?" / "Draw the three states of git"
- **Practical**: "Create a repository, make 3 commits, push to GitHub" — assessed on commit messages and history
- **Collaboration**: Pair exercise — contribute to each other's repositories via pull requests
- **Conflict resolution**: Resolve a pre-made merge conflict (provided as a repo with two branches)
