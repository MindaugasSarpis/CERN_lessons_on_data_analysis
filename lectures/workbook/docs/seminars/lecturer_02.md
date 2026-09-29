# Week 2 — Lecturer's Brief (29 September)

**Session:** 90 min lecture (02 Introduction to Data) + 90 min seminar
([Seminar 2](seminar_02.md): the first hands-on session, from scratch).

This page is the run-of-show for the person at the front. Students are welcome to
read it.

Shortcuts are written **Windows / Linux** first, then **macOS**.

---

## A. The lecture in 90 minutes

The deck is sized for a 2-hour slot (about 129 min as written, 62 slides). It
runs in this order: data in everyday life, kinds of data, open data and
provenance, then CERN as the case study, then the example file up close.

For 90 minutes, skip the slides below; type the slide number and press Enter to
jump. Almost all cuts fall in the CERN case study, so the fundamentals stay
whole.

| Skip | Slides | Saves |
|--|--|--|
| Quiz: the lifecycle | 10 | 3 min |
| Where Each Flavour Shows Up Later | 18 | 2 min |
| Data at Work (two slides) + Common Threads | 20–22 | 7 min |
| ALICE, quark–gluon plasma clip | 35–36 | 4 min |
| LHCb film clip | 40 | 2 min |
| Quiz: what does 5 sigma mean? | 44 | 4 min |
| Quiz: why not record it all? | 49 | 3 min |
| Careers at CERN, Working with the Data | 50–51 | 4 min |
| Beyond Physics (whole section, with its quiz) | 52–55 | 9 min |

That leaves about 90 minutes, including the 5-minute thought exercise on
slide 19. If you run late, skip From Events to Petabytes (slide 47) next: the
data-flow clip before it shows the same chain.

The four detector fly-ins stay in: ATLAS (33), CMS (34), ALICE (37), LHCb (39),
three and a half minutes together. They are silent, so talk over them. The
ALICE slide is skipped; say what ALICE studies while its fly-in plays.

The data-flow clip (46, 2:51, music) stays in as well: accelerator chain,
detectors, trigger, data centre, grid. It stands in for the skipped Beyond
Physics section, which is where the grid is otherwise introduced.

**Do not cut** slides 11–17 (kinds of data, tables, files), 23–30 (open data and
provenance) or 56–61 (the example file). The seminar uses every one of them.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–9 | Data in your life, what data is, the lifecycle |
| 0:16 | 11–19 | Kinds of data, variables, tables, files, thought exercise |
| 0:33 | 23–30 | Open data and provenance |
| 0:50 | 31–48 | CERN case study: the four detectors, the D⁰, the data flow, the trigger |
| 1:14 | 56–62 | The example file up close, recap |
| 1:30 | | Move to the seminar |

Ask students to keep their thought-exercise answer (slide 19): it is their
starting point for choosing a dataset at home this week.

Slide 17 (One Table, Three Files) sets up the seminar's central comparison, the
same CSV opened in VS Code and in a spreadsheet. Do not rush it.

---

## B. The seminar in 90 minutes

This is the first hands-on session of the course and it starts from zero.
Assume nothing is installed and nobody has opened a terminal. The room is
mixed: some students have written Python, some have only used Excel.

**Today needs only VS Code and a browser.** No Python, no Git, no terminal.
Those are installed at home ([Seminar 1](seminar_01.md)) and arrive one at a
time in the coming weeks.

| Clock | Block | Brief | Students end with |
|--|--|--|--|
| 0:00 | 1. Install and open VS Code | Part A | VS Code running |
| 0:15 | 2. The tour, followed along | Part B | The layout known, a folder open |
| 0:35 | 3. Build the project folder | Part C | The skeleton and a README |
| 0:50 | 4. A data file, in VS Code and in Excel | Part D | The file in `data/raw/`, rows counted |
| 1:15 | 5. Where it came from | Part E | A **Data** section in the README |
| 1:25 | 6. Wrap-up and homework | Part F | Knowing what to do before next week |

### How to run a mixed room

- **One step at a time, on the projector.** Do the step, say what the screen
  should show, wait. Move on when about four in five are there; the rest get
  help from a neighbour while you continue.
- **Pair by experience.** Ask who has programmed before and seat them next to
  someone who has not. The rule for the experienced one: explain, never take
  the keyboard.
- **The ✔ checks in the brief are the rhythm.** At each one ask for hands:
  "who sees this?"
- **Fast students go to the stretch goals**, which need the terminal and
  Python. They do not go ahead in the main brief.
- **Name things as you click them.** Excel users know folders, files and
  tables. New today are only: the project folder as the unit of work, plain
  text as the format, and the README.

### Why start with VS Code

- It looks and behaves the same on Windows and macOS. The terminal does not:
  PowerShell and zsh differ in exactly the commands beginners need first.
- Files, editor, terminal and Git sit in one window. When the terminal and Git
  arrive in later weeks, they arrive inside a place students already know.
- It lets the first session be about *data and where it came from* rather than
  about typing commands.

The risk is that VS Code becomes "the tool" and the course's tool-agnostic aim
gets lost. Say it once out loud: everything done today by clicking can be done
in any editor, and from Lecture 4 on we will also do it by typing.

### Block 1 — install and open VS Code (15 min)

Put the address on the projector: `code.visualstudio.com`. Walk round while it
downloads.

| Symptom | Fix |
|--|--|
| Windows: installer asks for an administrator password | Choose the **User Installer** from the download page; it needs none |
| macOS: "cannot be opened because it is from an unidentified developer" | The file was opened from *Downloads*; drag it to *Applications* first |
| macOS: VS Code runs but disappears after a restart | It was started from the downloaded archive; drag it to *Applications* |
| University or work laptop blocks installation | Use [vscode.dev](https://vscode.dev) in the browser today (it can open a local folder in Chrome and Edge), and install at home |
| Slow network | Pass round a USB stick with both installers |

### Block 2 — the tour (20 min)

Project your own VS Code, zoomed in (`Ctrl` `+` / `Cmd` `+`). Students repeat
each step. Seven stops today; four more are kept for later weeks.

**1. Open a folder, not a file.** Students create `analysis-project` in their
file manager, then *File → Open Folder…*. Answer "Yes, I trust the authors".
The point to make: VS Code works on a **folder**. That folder is the project.
For Excel users: a project folder is to this course what a workbook is to
Excel, except that every sheet is a separate file.

**2. The five regions.** Point at each and name it:

| Region | Where | What it is for |
|--|--|--|
| Activity Bar | far left, icons | switches what the Side Bar shows |
| Side Bar | left | Explorer, Search, Source Control, Extensions |
| Editor | centre | the files, in tabs |
| Panel | bottom | Terminal, Problems, Output |
| Status Bar | bottom edge | facts about the open file and the project |

`Ctrl+B` / `Cmd+B` hides and shows the Side Bar.

**3. The Command Palette.** `Ctrl+Shift+P` / `Cmd+Shift+P`. Every action in VS
Code is listed here and can be found by typing part of its name. Demonstrate
with *Preferences: Color Theme*. Tell them this is the one shortcut worth
memorising today; everything else can be found through it.

**4. Explorer.** New File and New Folder buttons at the top of the Side Bar.
Rename with `F2` / `Enter`. Right-click → *Reveal in File Explorer* / *Reveal
in Finder*, to show that it is an ordinary folder on disk. The most common
slip: a new folder lands inside the folder that was selected. Show how to
click the empty area first, and how to drag a folder out again.

**5. Editing and saving.** The dot on the tab means unsaved. `Ctrl+S` /
`Cmd+S`. Then *File → Auto Save*. Excel users expect a Save dialog with a file
type; here a file is only ever its own text.

**6. Markdown preview.** With `README.md` open: `Ctrl+Shift+V` /
`Cmd+Shift+V`. Type a `#` heading and watch the preview follow. One sentence
only: `#` makes a heading, the rest is Lecture 5.

**7. Moving in a long file.** `Ctrl+F` / `Cmd+F` finds text, `Ctrl+G` jumps to
a line number, `Ctrl+End` / `Cmd+↓` jumps to the end. They need these three in
block 4.

Kept for later weeks; if asked today, show it for ten seconds and name the week:

| Stop | Week |
|--|--|
| 8. The Status Bar: encoding, line endings | 3 (How Computers Work) |
| 9. The terminal panel, `` Ctrl+` `` | 4 (Command Line) |
| 10. Extensions: Python, running a script with ▶ | 7 (Python Foundations) |
| 11. Source Control: staging, committing, comparing versions | 6 (Git) |

Leave out altogether, even if asked: debugging, multi-root workspaces, settings
sync, remote development, AI assistants, Jupyter.

### Block 3 — build the project folder (15 min)

Follow part C of the brief. Build `data` and `data/raw` together on the
projector, then let students do `data/processed`, `scripts` and `results`
alone. Say what each folder is for in one sentence:

| Folder | What goes in |
|--|--|
| `data/raw` | files exactly as downloaded; never edited |
| `data/processed` | cleaned versions, made later by scripts |
| `scripts` | code |
| `results` | figures and numbers that the code produces |

Check the ✔ tree at the end of part C by walking the rows.

### Block 4 — a data file, in VS Code and in Excel (25 min)

Follow part D. Everyone uses the same file, `D0_KPi.csv`, so that every screen
in the room shows the same thing. This is the file from the lecture's "A
Dataset Up Close" section; students choose their own dataset at home.

| Step | Watch for |
|--|--|
| Download | Browsers that rename a second download to `D0_KPi (1).csv`; Safari showing the text in a tab instead of saving (File → Save As) |
| Drag into `raw` | Dropped onto the wrong folder; drag it again |
| Open in VS Code | 91 584 lines. Line 1 is the header, so 91 583 rows of data |
| Open in Excel | See below |

**The Excel comparison is the centre of the session.** On a computer set to
Lithuanian (or most European) regional settings, Excel expects `;` between
values and `,` as the decimal separator. This file uses `,` between values and
`.` as the decimal point. Depending on the settings students will see one of:

- everything in column A, the whole line as one text;
- four columns, but numbers turned into text or into wrong values;
- four correct columns (English regional settings).

Ask who sees which. Then make the point: the file is the same on every
laptop, and VS Code shows the same text on every laptop. The spreadsheet shows
an interpretation that depends on the computer. Saving from the spreadsheet
would write that interpretation back into the file. That is why `data/raw/` is
never opened for editing.

Make sure nobody saves. If someone did, they download the file again.

### Block 5 — where it came from (10 min)

Follow part E. Open [record 401](https://opendata.cern.ch/record/401) on the
projector and find the DOI and the licence together. The "One row" line is the
one that needs thought; expected answer: one candidate pair of a kaon and a
pion from one collision.

The record's file is `MasterclassData.root`, and the CSV is a converted copy.
Say so plainly: the README has to name both, because the file in `data/raw/`
is not the file a stranger would download from the portal.

The laptop swap in step 23 takes three minutes and is worth keeping.

### Block 6 — wrap-up and homework (5 min)

Read part F aloud. Three things are due before next week: a dataset of their
own in `data/raw/`, the five questions answered, Python and Git installed.
Tell them that an installation which fails is not a problem: they bring the
error message and it gets fixed at the start of the next session.

### The weeks after this one

One new tool or idea per week, each arriving inside VS Code. Nothing is used
before the session that introduces it.

| Session | New today | Still by clicking |
|--|--|--|
| 29 Sep | VS Code, project folder, README, provenance | everything |
| Next | The file as text: encoding, separators, size. First three terminal commands: `pwd`, `ls`, `cd` | creating and moving files |
| Then | Terminal: make, copy, move, delete; running a Python script that is handed out | editing |
| Then | Markdown: the README as a real document | |
| Then | Git from the Source Control view first, then the same steps typed | |
| Then | Python, from the first line: variables, a loop, reading the data file | |

The published briefs for Seminars 3–16 were written for an earlier plan. They
assume bash commands that do not exist in PowerShell and a data file with
columns the real one does not have. Each needs rewriting in the style of the
Seminar 2 brief before its week.

---

## C. Checklist before the session

- Local copy running: `node scripts/serve-local.mjs 8123`, then
  `http://localhost:8123/02-intro-to-data/`.
- Your own VS Code reset to what a fresh installation looks like: default
  theme, Side Bar on the left, no unrelated extensions in view, zoom raised,
  and no `analysis-project` folder yet, so that you build it with them.
- A USB stick with the VS Code installers for Windows and macOS and with
  `D0_KPi.csv`, in case the network fails.
- A spreadsheet program on your laptop for the comparison in block 4. Try it
  beforehand so that you know which of the three outcomes your own computer
  shows.
- Reference values for the file are in the instructor notes at the end of the
  [Seminar 2 brief](seminar_02.md).
