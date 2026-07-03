# Seminar 6 — Branch, Break, Merge: Collaborate in Git ⚡

**Paired lecture:** 06 Version Control with Git · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** the whole project under version control,
> with a feature branch made and merged.

## Goal
Put the project under Git, experience branching and a merge (including a conflict),
and adopt a daily workflow.

## Prerequisites
Seminars 1–5. Git installed and configured.

## Tasks
1. `git init` in the project. Write a `.gitignore` (ignore large derived files in
   `processed/`, `results/`, `__pycache__/`, virtual envs — **keep `raw/` if the
   file is small enough, else document how to fetch it**).
2. Commit the skeleton, README, and scripts with clear messages.
3. Create a branch (`git switch -c add-explore`), add or improve `scripts/explore.sh`,
   commit, switch back to `main`, and `git merge` it.
4. **Provoke a merge conflict** on purpose (edit the same README line on two
   branches) and resolve it. Note what the markers mean.

## Stretch goals
- Pair up: push to a shared GitHub repo, open a pull request, review each other's.
- Use `git log --oneline --graph --all` to see your branch history.

## Solution notes (instructor)
The conflict is the learning moment — everyone should resolve one. Reinforce the
git-vs-manual-copies MCQ from the lecture: Git separates *the current file* from
*its history*.

## Aims practised
♻️ full navigable history · 🔧 the standard tool everywhere · ⚙️ a repeatable workflow
