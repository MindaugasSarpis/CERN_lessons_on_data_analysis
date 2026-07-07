# Seminar 6 — Branch, Break, Merge: Collaborate in Git ⚡

**Paired lecture:** 06 Version Control with Git · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

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
5. Break something on purpose, then practice the three levels of "undo" from
   the lecture on it: `git diff` to see the damage, `git restore <file>` to
   discard an uncommitted change, and (after committing a typo'd message)
   `git commit --amend` to fix it. Note which one you'd reach for in each case.

## Stretch goals
- Pair up: push to a shared GitHub repo, open a pull request, review each other's.
- Use `git log --oneline --graph --all` to see your branch history.
- Set up SSH key auth (`ssh-keygen`, add the public key to your GitHub
  account) instead of HTTPS, and clone your own repo fresh over SSH to confirm
  it works without typing a password.

## Wrap-up (last 10 min)
- Confirm a clean tree: `git status` should read "nothing to commit, working
  tree clean" and `git branch` should show only `main`, with the feature
  branch merged and deleted.
- Re-clone your own repo into a scratch folder (`git clone . /tmp/check`) and
  re-run `explore.sh` there — proof the *history*, not just your working copy,
  holds the whole project.
- Note one lesson in the README: the Git command you now trust most, and the
  one you're still wary of.

## Solution notes (instructor)
The conflict is the learning moment — everyone should resolve one. Reinforce the
git-vs-manual-copies MCQ from the lecture: Git separates *the current file* from
*its history*. In the 120-minute slot, protect time for task 4 — timebox tasks
1–3 to ~40 minutes even if the `.gitignore` isn't perfect, so every group reaches
and resolves a genuine conflict before the stretch goals.

## Aims practised
♻️ full navigable history · 🔧 the standard tool everywhere · ⚙️ a repeatable workflow
