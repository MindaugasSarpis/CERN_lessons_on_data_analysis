# Week 2 — Lecturer's Brief (29 September)

**Session:** 90 min lecture (02 Introduction to Data) + 90 min seminar
([Seminar 2](seminar_02.md): the first hands-on session, from scratch).

This page is the run-of-show for the person at the front. Students are welcome to
read it. The day before, go through the
[checklist](#c-checklist-before-the-session) at the end of the page.

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
| What Each Flavour Is Used For | 18 | 2 min |
| Data at Work (two slides) + Common Threads | 20–22 | 7 min |
| ALICE, quark–gluon plasma clip | 35–36 | 4 min |
| Quiz: what does 5 sigma mean? | 44 | 4 min |
| Quiz: why not record it all? | 49 | 3 min |
| Working with the Data | 50 | 2 min |
| Beyond Physics (whole section, with its quiz) | 52–55 | 9 min |

That leaves about 90 minutes, including the 5-minute thought exercise on
slide 19. If you run late, skip From Events to Petabytes (slide 47) next: the
data-flow clip before it shows the same chain.

Three detector fly-ins stay in: ATLAS (33), CMS (34), ALICE (37), two and a
half minutes together. They are silent, so talk over them. The ALICE slide is
skipped; say what ALICE studies while its fly-in plays. The LHCb clip (39,
0:47) stays in too: it is the detector the example file comes from.

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

!!! abstract "Overview"
    **Time:** 90 min · **Student brief:** [Seminar 2](seminar_02.md)

    **Questions**

    - Where does a project live on my computer?
    - What is inside a data file?
    - How do I write down where a file came from?

    **Objectives.** At the end a student can:

    - open a folder in VS Code and name the five regions of the window;
    - build the project folder and write a `README.md`;
    - open a CSV file as text and count its rows;
    - say why a spreadsheet shows the same file differently on two laptops;
    - write a **Data** section: source, DOI, licence, date, file.

| Clock | Block | Brief | Steps | Students end with |
|--|--|--|--|--|
| 0:00 | [1. Install and open VS Code](#block-1) | Part A | 1–3 | VS Code running |
| 0:15 | [2. The tour](#block-2) | Part B | 4–7 | The layout known, a folder open |
| 0:35 | [3. Build the project folder](#block-3) | Part C | 8–14 | The skeleton and a README |
| 0:50 | [4. A data file, in VS Code and in Excel](#block-4) | Part D | 15–20 | The file in `data/raw/`, rows counted |
| 1:15 | [5. Where it came from](#block-5) | Part E | 21–23 | A **Data** section in the README |
| 1:25 | [6. Wrap-up and homework](#block-6) | Part F | 24–27 | Knowing what to do before next week |

### How to read these notes

- **This page is enough to run the session.** Every step of the student brief
  is repeated here under the same number. Step 17 here is step 17 there.
- **Show** is what you do on the projector. **Say** is the point to make.
  **Watch for** is the usual slip at that step.
- **Check ✔** closes every block. Ask for hands: "who sees this?" Go on when
  about four in five have it. The rest get help from a neighbour while you
  continue.
- **Tour stop** marks the seven stops of the VS Code tour. Each one is taught
  at the step where students first need it: stops 1–3 in block 2, stops 4–6
  in block 3, stop 7 in block 4.

### How to run a mixed room

- **One step at a time, on the projector.** Do the step, say what the screen
  should show, wait.
- **Pair by experience.** Ask who has programmed before and seat them next to
  someone who has not. The rule for the experienced one: explain, never take
  the keyboard.
- **Fast students go to the stretch goals** ([answers below](#fast-students)).
  They do not go ahead in the main brief.
- **Name things as you click them.** Excel users know folders, files and
  tables. New today are only: the project folder as the unit of work, plain
  text as the format, and the README.
- **Optional, from the Carpentries:** two sticky notes for each student. Green
  on the laptop lid means "done", red means "stuck". You see the state of the
  room without asking.

---

### Block 1 — Install and open VS Code { #block-1 }

!!! abstract "0:00–0:15 · brief part A · steps 1–3"
    Students end with VS Code running.

**Before step 1.** Ask who has programmed before. Seat each of them next to
someone who has not.

1. **Download VS Code.**

    **Show:** the address `code.visualstudio.com`, large, on the projector.
    Students download the version for their system.

    **Say,** while it downloads: today needs one program and a browser.
    Everything done today by clicking can be done in any editor, or by typing
    commands.

2. **Install it.** Walk round the room while it installs.

    - Windows: run the downloaded installer and keep every default.
    - macOS: open the downloaded file and drag *Visual Studio Code* into the
      *Applications* folder.

3. **Start VS Code.**

!!! success "Check ✔"
    A window opens with a *Welcome* tab.

!!! warning "If it does not work"
    | Symptom | Fix |
    |--|--|
    | Windows: the installer asks for an administrator password | Choose the **User Installer** from the download page; it needs none |
    | macOS: "cannot be opened because it is from an unidentified developer" | The file was opened from *Downloads*; drag it to *Applications* first |
    | macOS: VS Code runs but disappears after a restart | It was started from the downloaded archive; drag it to *Applications* |
    | A university or work laptop blocks the installation | Use [vscode.dev](https://vscode.dev) in the browser today (it can open a local folder in Chrome and Edge), and install at home |
    | Slow network | Pass round a USB stick with both installers |

---

### Block 2 — The tour { #block-2 }

!!! abstract "0:15–0:35 · brief part B · steps 4–7 · tour stops 1–3"
    Students end with the layout known and a folder open.

**Before step 4.** Project your own VS Code and zoom in with `Ctrl` `+` /
`Cmd` `+`. Students repeat each step on their own laptop.

4. **Create the project folder.** *Tour stop 1: open a folder, not a file.*

    **Show:** in the file manager (File Explorer on Windows, Finder on macOS)
    create a folder named `analysis-project`, for example in *Documents*.

5. **Open the folder in VS Code.**

    **Show:** *File → Open Folder…*, pick `analysis-project`. Answer
    **Yes, I trust the authors**.

    **Say:** VS Code works on a folder. That folder is the project. For Excel
    users: a project folder is to this course what a workbook is to Excel,
    except that every sheet is a separate file.

6. **Name the five regions.** *Tour stop 2.*

    **Show:** point at each region and name it.

    | Region | Where | What it is for |
    |--|--|--|
    | Activity Bar | far left, icons | switches what the Side Bar shows |
    | Side Bar | left | Explorer, Search, Source Control, Extensions |
    | Editor | centre | the files, in tabs |
    | Panel | bottom, hidden at first | Terminal, Problems, Output |
    | Status Bar | bottom edge | facts about the open file and the project |

    `Ctrl+B` / `Cmd+B` hides and shows the Side Bar. Students press it twice.

7. **Open the Command Palette.** *Tour stop 3.*

    **Show:** `Ctrl+Shift+P` / `Cmd+Shift+P`. Type `theme`, choose
    *Preferences: Color Theme*, pick a theme.

    **Say:** every action in VS Code is listed here and can be found by typing
    part of its name. This is the one shortcut worth memorising today.
    Everything else can be found through it.

!!! success "Check ✔"
    The Side Bar shows the title `ANALYSIS-PROJECT` and nothing under it.

Block 2 has time to spare and block 3 is tight. Start block 3 as soon as the
check passes.

---

### Block 3 — Build the project folder { #block-3 }

!!! abstract "0:35–0:50 · brief part C · steps 8–14 · tour stops 4–6"
    Students end with the folder skeleton and a README.

Steps 8 and 9 are done together on the projector. Step 10 students do alone.

8. **Create the folder `data`.** *Tour stop 4: the Explorer.*

    **Show:** move the mouse over the Side Bar. Four small icons appear next
    to the project name. Click **New Folder**, type `data`, press Enter.

9. **Create `raw` inside `data`.**

    **Show:** click on `data`, then **New Folder**, type `raw`.

    **Show** on the new folder: `F2` / `Enter` renames it. Right-click →
    *Reveal in File Explorer* / *Reveal in Finder* opens it in the file
    manager.

    **Say:** it is an ordinary folder on disk. VS Code only shows it.

    **Watch for:** the Side Bar now shows `data / raw` on one row. VS Code
    joins a folder with its only subfolder. The row splits into a normal tree
    when `data` gets its second subfolder in step 10.

10. **Students alone: `data/processed`, `scripts`, `results`.**

    **Say** what each folder is for, one sentence each:

    | Folder | What goes in |
    |--|--|
    | `data/raw` | files exactly as downloaded; never edited |
    | `data/processed` | cleaned versions, made later by scripts |
    | `scripts` | code |
    | `results` | figures and numbers that the code produces |

    **Watch for:** a new folder that lands inside the folder that was
    selected. This is the most common slip of the session. Show how to click
    the empty area of the Side Bar first, and how to drag a folder out again.
    The way that always works: click the empty area, **New Folder**, type the
    whole path `data/processed`.

11. **Create `README.md`.**

    **Show:** click the empty area, then **New File**, type `README.md`.

12. **Type the first lines.** *Tour stop 5: editing and saving.*

    ```text
    # Analysis Project

    Seminar exercises for the course.
    ```

13. **Save.**

    **Show:** the dot on the tab means *not saved*. `Ctrl+S` / `Cmd+S`. Then
    switch on *File → Auto Save*.

    **Say:** Excel users expect a Save dialog with a file type. Here a file is
    only ever its own text.

14. **Look at the preview.** *Tour stop 6: Markdown preview.*

    **Show:** `Ctrl+Shift+V` / `Cmd+Shift+V` opens the README as a formatted
    page. On the projector use `Ctrl+K` `V` / `Cmd+K` `V`: the preview opens
    beside the text and the room sees both. Type a second `#` heading and
    watch the preview follow.

    **Say,** one sentence only: `#` makes a heading.

!!! success "Check ✔"
    The project contains exactly this. Walk the rows and check.

    ```text
    analysis-project/
    |- README.md
    |- data/
    |  |- processed/
    |  |- raw/
    |- results/
    |- scripts/
    ```

    VS Code lists folders before files, so in the Side Bar `README.md` is the
    last row.

---

### Block 4 — A data file, in VS Code and in Excel { #block-4 }

!!! abstract "0:50–1:15 · brief part D · steps 15–20 · tour stop 7"
    Students end with the file in `data/raw/` and its rows counted.

**Say:** everyone uses the same file, `D0_KPi.csv`, so that every screen in
the room shows the same thing. It is the file from the lecture's section
"A Dataset Up Close". You choose your own dataset at home.

15. **Download `D0_KPi.csv`.** The link is in step 15 of the brief. The file
    lands in *Downloads*.

    **Watch for:** a browser that renames a second download to
    `D0_KPi (1).csv`. Safari showing the text in a tab instead of saving it:
    *File → Save As*.

16. **Drag the file onto `raw`** in the Side Bar. Do not rename it.

    **Watch for:** the file dropped onto the wrong folder. Drag it again.

17. **Open the file and read it.** *Tour stop 7: moving in a long file.*

    **Show:** click the file in the Side Bar. `Ctrl+End` / `Cmd+↓` jumps to
    the end. `Ctrl+F` / `Cmd+F` finds text.

    Students answer on paper:

    | Question | Answer |
    |--|--|
    | What is written in line 1? | `M,PT,TAU,IPCHI2`, the four column names |
    | Which character separates the values? | The comma |
    | How many lines does the file have? | 91 584: one header line and 91 583 rows of data |

    **Watch for:** the answer 91 585. The file ends with a line break, so
    VS Code numbers one more line, and that line is empty. The last line with
    numbers in it is 91 584.

18. **Jump to line 5000.**

    **Show:** `Ctrl+G`, type `5000`, press Enter. The key is `Ctrl` on macOS
    too. Line 5000 begins with `1868.8636`.

19. **Open the same file in a spreadsheet, without saving anything.** Excel,
    LibreOffice or Numbers.

    **Show:** right-click the file in the Side Bar → *Reveal in File
    Explorer* / *Reveal in Finder*, then open it from there. A student
    without a spreadsheet program looks at a neighbour's screen.

    This comparison is the centre of the session. A computer set to
    Lithuanian, or to most European regional settings, expects `;` between
    values and `,` as the decimal separator. The file uses `,` between values
    and `.` as the decimal point. A student sees one of three things:

    | On the screen | Reason |
    |--|--|
    | Everything in column A, the whole line as one text | The spreadsheet waits for `;` |
    | Four columns, but numbers turned into text or into wrong values | The decimal point is not understood |
    | Four correct columns | English regional settings |

    **Ask** who sees which.

    **Say:** the file is the same on every laptop, and VS Code shows the same
    text on every laptop. The spreadsheet shows an interpretation that
    depends on the computer. Saving from the spreadsheet would write that
    interpretation back into the file. That is why `data/raw/` is never
    opened for editing.

20. **Close the spreadsheet.** If it asks whether to save, the answer is
    **No**.

    **Watch for:** someone who saved. They download the file again.

!!! success "Check ✔"
    Every student can say the number of data rows, 91 583, and the four
    column names.

---

### Block 5 — Where it came from { #block-5 }

!!! abstract "1:15–1:25 · brief part E · steps 21–23"
    Students end with a **Data** section in the README.

21. **Add a Data section to the README.**

    **Show:** open [record 401](https://opendata.cern.ch/record/401) on the
    projector. Find the DOI and the licence together with the room. Filled
    in, the section reads:

    ```text
    ## Data

    Source:   CERN Open Data Portal, record 401
    DOI:      10.7483/OPENDATA.LHCb.E7EJ.JUWR
    Licence:  CC0
    Fetched:  2026-09-29
    File:     data/raw/D0_KPi.csv — converted from the record's
              MasterclassData.root by the course's root_to_csv.py
    One row:  one candidate pair of a kaon and a pion from one collision
    ```

    The line "One row" is the one that needs thought. Give it a minute
    before you show the answer.

    **Say:** the record's file is `MasterclassData.root`, and the CSV is a
    converted copy. The README names both, because the file in `data/raw/`
    is not the file a stranger would download from the portal.

22. **Add the file size and the number of data rows:** 3 926 142 bytes,
    91 583 rows.

    **Watch for:** two different sizes in the room. Windows shows about
    3 835 KB, macOS about 3.9 MB. Both are 3 926 142 bytes: Windows counts in
    units of 1024, macOS in units of 1000.

23. **Swap laptops with a neighbour.** Using only the neighbour's README,
    could you find and download the same file? Tell them what was missing.
    This takes three minutes and is worth keeping.

!!! success "Check ✔"
    The README has a **Data** section that a stranger could follow.

---

### Block 6 — Wrap-up and homework { #block-6 }

!!! abstract "1:25–1:30 · brief part F · steps 24–27"
    Students leave knowing what to do before next week.

Read part F of the brief aloud. Three things are due before next week:

| Due | Brief |
|--|--|
| A dataset of their own in `data/raw/`, with its entry in the README | steps 24–25 |
| The five questions from the lecture, answered for that file | step 26 |
| Python and Git installed | step 27, [Seminar 1](seminar_01.md) |

**Say:** an installation that fails is not a problem. Bring the error
message; a photo of the screen is enough. It gets fixed at the start of the
next session.

**Ask** on the way out: which step was hardest?

!!! tip "Key points"
    - VS Code works on a folder. The folder is the project.
    - A CSV file is plain text. VS Code shows the same text on every laptop.
    - A spreadsheet shows an interpretation of the file, and the
      interpretation depends on the computer.
    - A file in `data/raw/` is never edited and never saved from a
      spreadsheet.
    - The README says where each file came from.

---

### Fast students { #fast-students }

Send them to the stretch goals at the end of the brief. These need the
terminal and Python.

| Stretch goal | Answer |
|--|--|
| Checksum of `D0_KPi.csv` | SHA-256 `25c3c972…c1505136`, the same on every system |
| `scripts/count_rows.py` | 91 583 rows; `M` runs from 1766.2096 to 2453.6584 |
| The value `-100` | Column `TAU`, 49 rows. It marks an invalid decay time |
| `MasterclassData.root` opened in VS Code | The file is binary, so VS Code declines to show it as text |

### If students ask for more

Four tour stops are not part of today's tour. If asked, show it for ten
seconds and move on.

| Stop | Topic |
|--|--|
| 8. The Status Bar: encoding, line endings | How Computers Work |
| 9. The terminal panel, `` Ctrl+` `` | Command Line |
| 10. Extensions: Python, running a script with ▶ | Python Foundations |
| 11. Source Control: staging, committing, comparing versions | Git |

Leave out altogether, even if asked: debugging, multi-root workspaces, settings
sync, remote development, AI assistants, Jupyter.

### Why start with VS Code

- It looks and behaves the same on Windows and macOS. The terminal does not:
  PowerShell and zsh differ in exactly the commands beginners need first.
- Files, editor, terminal and Git sit in one window. When the terminal and Git
  arrive in later weeks, they arrive inside a place students already know.
- It lets the first session be about *data and where it came from* rather than
  about typing commands.

The risk is that VS Code becomes "the tool" and the course's tool-agnostic aim
gets lost. That is why step 1 says it out loud: everything done today by
clicking can be done in any editor, or by typing commands.

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
- This page open on a second device or printed. The reference values for the
  file are in blocks 4 and 5.
- Optional: sticky notes in two colours, two for each student.
