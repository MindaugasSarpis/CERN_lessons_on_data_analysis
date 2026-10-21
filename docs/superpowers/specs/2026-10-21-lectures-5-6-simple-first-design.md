# Lectures 5 and 6: simple first, the inner workings for the curious

21 October 2026. Lecture 5 (Python Foundations) was delivered on 20 October;
Lecture 6 (Version Control with Git) is on 27 October and was released on
21 October in its first-principles form.

## Why

The lecturer, after Lecture 5 and on reading Lecture 6:

- "L5 was quite dry, just a bunch of python function not much story
  telling. Need to see how to make it a little bit more educational. Maybe
  compare with proprietary tools or smth"; "Classes - way too steep";
  "Why we need python, not excel."; "what's with the first 5 slides? I
  don't need them".
- On Lecture 6: "Now it looks very complicated from the start. I had this
  before: https://hsf-training.github.io/git-novice/aio.html I even had
  some pictures sourced and prepared. Could we first schematically show
  everything as here (or as the previous version of git lecture, but
  improved and coherent) and then towards the end the 'inner workings' but
  only for curious."
- On a terminal block of eight lines (the `git rm` slide): "this and similar
  ones are very difficult to read in a lecture. If we need them, use shiki
  magic move to show one line at a time, or something like that";
  then "reciprocate this to L5 as well", and "go ahead improve the
  slidedeck and deploy".

## Rules for both decks

1. **Simple and schematic first.** The main path shows what a tool does
   for the room, with pictures and one short example per step, before any
   internals. Each part starts from a need of the weather project.
2. **No walls of code or terminal output.** A block longer than about five
   lines is either cut to the lines that matter (`...` marks a cut) or
   built up with Shiki magic-move (` ````md magic-move ` around ` ```text `
   steps, as in Lecture 4, slide "Change Folder: cd"): one command and its
   answer per click, the earlier lines staying. Python runner blocks stay
   ≲10 lines (docs/python-runner-recipe.md).
3. **The inner workings go to the end, for the curious.** After the Recap
   and before `# Check **Yourself**`, a section slide `# For the **Curious**`
   opens the optional slides. `scripts/timing-report.mjs` counts that
   section and everything after it as 0 min, like the quizzes, so the main
   path alone must estimate in the deck's band. The main path must not need
   the section: a slide that used to argue from it says the one fact it
   needs in plain words.
4. **The opening goes straight to the problem.** No Learning Objectives
   slide, no table of parts. The cover stays.
5. Everything else in CLAUDE.md stays in force: self-contained decks, one
   note form, titles that pass the `writing-lecture-slides` test, outputs
   that were really printed (never invented), zero overflow, two shells.

## Lecture 6: Version Control with Git

The order of Software Carpentry's *Version Control with Git* (the HSF
copy the lecturer linked), with the figures already in
`lectures/content/public/figures/` from that lesson (CC BY 4.0, credited on
the slide): `play-changes.svg`, `versions.svg`, `merge.svg`,
`git-staging-area.svg`, `git-committing.svg`, `git-restore.svg`,
`git-freshly-made-github-repo.svg`, `github-repo-after-first-push.svg`,
`github-collaboration.svg`, plus `git_flow.svg` and the comic
`comic_version.jfif`. The deck before the first-principles rework used
them: `git show 518a793^:lectures/content/slides/05_Version_Control.md`.

Main path:

1. Why version control: the copies (`final_v2`, the comic); tracking
   changes, versions, merging as pictures; what Drive, Dropbox and Word keep
   against Git; where Git comes from (BitKeeper, 2005). The weather story
   stays as the thread, told without a terminal: Tomas sends back the export
   with line 2 changed from `6,3` to `6,4`, and nothing says who, when, why.
2. Setting up: Git's version, name and e-mail.
3. Tracking changes: the three areas as a picture first, then `git init`,
   `git status`, `git add`, `git commit`, each as the Source Control button
   and typed; the commit message; the modify-add-commit cycle.
4. History and undo: the diff, `git log`, restore an edit, revert a
   commit (and amend the last one).
5. What goes into a repository: which files, `.gitignore`, `.gitattributes`.
6. Remotes on GitHub: a remote as a picture; publish from VS Code and
   typed; clone; push and pull; collaborators.
7. Branches and conflicts: a branch, a merge, a conflict resolved in the
   editor; the whole picture (`git_flow.svg`); the daily workflow.
8. A result and its commit: the story's question answered from the history
   (`log`, `blame`, `show`), the revert, a tag. Then the Recap.

For the Curious: the model as it stands now (a name made from the content,
the blob header, the id of `weather.csv`, a folder as a tree, a commit as
text, the id of a commit, history as a graph, a branch as a 41-byte file).

Pull requests are not taught: the seminar will ask the room to make their
files appear in a course repository and let them find out what a pull
request is (lecturer, 21 Oct; the seminar is still to be designed).

## Lecture 5: Python Foundations

The thread is "why Python, not Excel". The same task is done the
spreadsheet way, the place where that breaks is shown, then Python does it.
Facts checked on 21 Oct 2026:

- `weather.csv` in a spreadsheet: `AVERAGE` over the 87 672 temperatures
  gives 5.78 (the 120 `-999` count), `AVERAGEIF(…;"<>-999")` gives 7.16.
  The spreadsheet gets the number; what it does not keep is the steps.
- The `.xls` format holds 65 536 rows. `weather.csv` has 87 673 lines: in
  `.xls` it would stop after 2023-06-23T14:00 and lose the last 22 137
  hours; the mean of what is left is 7.08 °C, not 7.16 (computed from the
  file). `.xlsx` holds 1 048 576 rows.
- Public Health England, October 2020: 15 841 positive Covid-19 cases of
  25 September to 2 October were left out of the daily figures, because
  the results were loaded into the old `.xls` format and the rows beyond
  its limit were dropped.
- Gene names: Excel turns `SEPT2` into the date 2-Sep and `MARCH1` into
  1-Mar. About one in five papers with Excel gene lists had such errors
  (Ziemann, Eren and El-Osta, Genome Biology, 2016: 704 of 3 597 papers);
  in 2020 the HUGO Gene Nomenclature Committee renamed 27 human genes
  (`SEPT2` → `SEPTIN2`, `MARCH1` → `MARCHF1`) rather than wait for Excel.
- Reinhart and Rogoff, 2010: an averaging formula covered rows 30 to 44
  instead of 49 and left out five countries (Australia, Austria, Belgium,
  Canada, Denmark). Herndon, Ash and Pollin found it in 2013; with this and
  two other choices corrected, the mean growth at a debt above 90 % of GDP
  is 2.2 %, not the published −0.1 %.

Changes:

- The opening goes straight to the spreadsheet problem; the quote, "What
  Happens When Python Runs", "The File of Today" and the table of parts go
  (the interpreter and the file's columns are said where Part 1 first
  needs them).
- Each part keeps its Python, with a spreadsheet contrast where it is
  natural, not on every slide. A closing table: what the spreadsheet and the
  script leave behind for the 7.16.
- Writing a class (`class Hour`, `__init__`, `self`, `is_missing()`, the
  coldest hour with `Hour` objects) moves to For the Curious. The main path
  keeps "every value is an object with methods" (`.split()`, `.append()`).
- Long blocks follow rule 2.

## Left to the builder

The exact slide order, titles, which existing slides are reused, cut or
parked (`lectures/content/parked/NN_*.md` with a header comment), and the
numbers on the lecture pages `lecture_5.md` and `lecture_6.md` (plan, skip
list, live moments), recounted after the rework.
