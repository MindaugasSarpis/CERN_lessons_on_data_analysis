# Week 2 — Lecturer's Brief (29 September)

**Session:** 90 min lecture (02 Introduction to Data) + 90 min seminar
(VS Code tour, Seminar 1 check, [Seminar 2](seminar_02.md)).

This page is the run-of-show for the person at the front. Students are welcome to
read it: the VS Code tour in part B doubles as a reference.

Shortcuts are written **Windows / Linux** first, then **macOS**.

---

## A. The lecture in 90 minutes

The deck is sized for a 2-hour slot (about 115 min as written). For 90 minutes,
skip the slides below; type the slide number and press Enter to jump.

| Skip | Slides | Saves |
|--|--|--|
| Where Each Flavour Shows Up Later | 14 | 2 min |
| Data at Work (two slides) + Common Threads | 16–18 | 7 min |
| ATLAS clip, quark–gluon plasma clip | 21, 23 | 4 min |
| Quiz: why not record it all? | 33 | 3 min |
| Careers at CERN, A Day in the Data | 34–35 | 4 min |
| Beyond the Ring (whole section, with its quiz) | 36–39 | 9 min |

That leaves about 85 minutes, including the 5-minute thought exercise on slide 15.

**Do not cut** slides 40–53 (Open Data & Provenance, A Dataset Up Close). The
seminar uses every one of them. If you run late, drop the lifecycle quiz
(slide 10) and the LHCb clip (slide 25) before touching that part.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–15 | Data in your life, the four flavours, metadata, thought exercise |
| 0:27 | 19–26 | The four experiments, the D⁰ |
| 0:37 | 27–32 | Why data: the trigger, from events to petabytes |
| 0:52 | 40–47 | Open data and provenance |
| 1:09 | 48–54 | A dataset up close, recap |
| 1:25 | | Questions, move to the seminar |

Ask students to keep their thought-exercise answer (slide 15): it is their
starting point for choosing a dataset in the seminar.

---

## B. The seminar in 90 minutes

| Clock | Block | Students end with |
|--|--|--|
| 0:00 | 1. Who has what — setup triage | Everyone knows whether their tools work |
| 0:10 | 2. VS Code tour, followed along | The project folder open, the layout known |
| 0:40 | 3. Skeleton and first commit | Seminar 1 done, inside VS Code |
| 0:50 | 4. Seminar 2, tasks 1–5 | A dataset in `data/raw/`, provenance in the README |
| 1:20 | 5. Second commit and wrap-up | Two commits in the history |

Task 6 of Seminar 2 (the five questions) and the stretch goals are homework.

### Why start with VS Code

- It looks and behaves the same on Windows and macOS. The terminal does not:
  PowerShell and zsh differ in exactly the commands beginners need first.
- File Explorer, editor, terminal and Git sit in one window, so students see
  that a folder on disk, a file's text and a commit are the same thing seen
  three ways.
- It lets the first session be about *data and provenance* rather than about
  typing. The command line gets its own lecture in week 4, and by then the
  terminal panel is already a familiar place.

The risk is that VS Code becomes "the tool" and the course's tool-agnostic aim
gets lost. Say it once out loud: everything done today by clicking can be done
in any editor and any terminal, and from Lecture 4 on we will do it both ways.

### Block 1 — setup triage (10 min)

Ask for a show of hands, in this order:

1. VS Code opens.
2. `git --version` prints a number.
3. `python --version` (or `python3`, or `py` on Windows) prints a number.
4. Seminar 1 finished, first commit made.

Seat people with a gap next to someone without one. Do not fix installations
from the front; walk round during block 2's follow-along pauses and during
block 4. The usual problems:

| Symptom | Cause | Fix |
|--|--|--|
| Windows: `python` opens the Microsoft Store | Store alias, no real Python | Install from python.org with **Add python.exe to PATH** ticked; or use `py` |
| Windows: `git` not recognised after installing | Terminal opened before the install | Close and reopen VS Code |
| macOS: `git` opens an installer dialog | Xcode command-line tools missing | Accept it; takes a few minutes |
| macOS: `python` not found | Only `python3` exists | Use `python3` |
| macOS: `code` not found in the terminal | Shell command not installed | Command Palette → *Shell Command: Install 'code' command in PATH* |
| Commit fails: "configure your user.name and user.email" | Git identity not set | The two `git config` lines from Seminar 1, task 6 |
| Windows: downloaded file is `data.csv.txt` | File extensions hidden | File Explorer → View → Show → File name extensions |

Anyone still without Python or Git at 0:40 continues anyway: blocks 3–5 need
only VS Code, except the commit. They pair up for the commit and finish the
installation at home.

### Block 2 — the VS Code tour (30 min)

Project your own VS Code, zoomed in (`Ctrl` `+` / `Cmd` `+`). Students repeat each
step. Eleven stops, two to three minutes each.

**1. Open a folder, not a file.** *File → Open Folder…*, create
`analysis-project` and open it. Answer "Yes, I trust the authors". The point to
make: VS Code works on a **folder**; that folder is the project, and later the
Git repository. Students who did Seminar 1 open the folder they already have.

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
memorising today; the rest can be found through it.

**4. Explorer.** New File and New Folder buttons at the top of the Side Bar.
Build one folder together (`data`, then `raw` inside it). Rename with `F2` /
`Enter`. Drag a file from the desktop into a folder. Right-click → *Reveal in
File Explorer* / *Reveal in Finder* to show it is an ordinary folder on disk.

**5. Editing and saving.** Create `README.md`, type a title line. Point at the
dot on the tab: unsaved. `Ctrl+S` / `Cmd+S`. Then *File → Auto Save*, and
explain why it is worth switching on: most "my change did nothing" problems in
later weeks are unsaved files.

**6. Markdown preview.** With `README.md` open: `Ctrl+Shift+V` /
`Cmd+Shift+V`, or the split-preview icon at the top right of the editor. Type a
`#` heading, a `-` list and a `**bold**` word and watch the preview follow.
This is a preview of Lecture 5; today it is only so the README looks like a
document.

**7. Finding things.** `Ctrl+P` / `Cmd+P` opens a file by typing part of its
name. `Ctrl+F` / `Cmd+F` finds in the open file. `Ctrl+Shift+F` /
`Cmd+Shift+F` finds in every file of the project. `Ctrl+G` jumps to a line
number. They will use the last one on the data file.

**8. The Status Bar, read left to right.** Open any text file and read out:
line and column, spaces or tabs, **encoding** (UTF-8), **line endings** (LF on
macOS and Linux, often CRLF on Windows), language. Say that the encoding and
the line endings are metadata of the file, as in today's lecture, and that
Lecture 3 explains both. Windows and macOS students compare their line endings.

**9. The terminal panel.** `` Ctrl+` `` on every system, or *Terminal → New
Terminal*. It opens **inside the project folder**; show the path in the prompt.
Windows students see PowerShell, macOS students zsh. Run only commands that
behave the same in both:

```text
pwd
ls
git --version
python --version
```

The dropdown next to the `+` lists other shells; on Windows, Git Bash is
there if Git is installed. Do not go further: the command line is Lecture 4.

**10. Extensions.** `Ctrl+Shift+X` / `Cmd+Shift+X`. Install **Python**
(publisher Microsoft) together. Then create `scripts/hello.py` with
`print("ready")` and run it with the ▶ button at the top right. If VS Code asks
for an interpreter, *Python: Select Interpreter* in the Command Palette. Mention
**Rainbow CSV** as optional: it colours the columns of a CSV file.

**11. Source Control.** `Ctrl+Shift+G`. This is the last stop and leads into
block 3. Show only what the view is: a list of files that changed since the
last commit. Click a changed file to see the before/after comparison.

Things to leave out today, even if asked: debugging, workspaces and
multi-root folders, settings sync, remote development, AI assistants, Jupyter.
Note the question and come back to it in the week it belongs to.

### Block 3 — skeleton and first commit (10 min)

Students who finished Seminar 1 help a neighbour. Everyone else does
Seminar 1 tasks 2–6 in VS Code:

1. In Explorer, complete the skeleton: `data/raw`, `data/processed`, `scripts`,
   `results`, `README.md`. An empty folder is not tracked by Git, so add an
   empty file named `.gitkeep` to `data/raw`, `data/processed` and `results`.
2. Source Control view → **Initialize Repository**.
3. Type the message `Project skeleton`, press **Commit**. When asked whether to
   stage all changes, answer Yes.
4. If the commit is refused because no identity is set, run in the terminal
   panel, once per computer:

   ```text
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

Say what just happened in one sentence: Git stored a snapshot of the folder
that can be returned to. How and why is week 6.

### Block 4 — Seminar 2, tasks 1–5 (30 min)

Follow the [brief](seminar_02.md). Time per task:

| Task | Min | Watch for |
|--|--|--|
| 1. Choose a dataset | 10 | The time sink. At 0:58 anyone without a dataset takes the LHCb record 401 and swaps later |
| 2. Download into `data/raw/` | 5 | Files renamed by the browser (`data (1).csv`); Safari unzipping archives; files over ~50 MB |
| 3. **Data** section in the README | 7 | "Downloaded from the internet" is not a source; ask for the record's URL or DOI |
| 4. Size and row count | 3 | Row count is the last line number minus the header line |
| 5. Checksum | 5 | PowerShell prints upper case, macOS lower case; both are the same hash |

Useful demonstration for task 2: open `MasterclassData.root` in VS Code. It
refuses, because the file is binary. Then open `D0_KPi.csv`: 91,584 lines,
`Ctrl+G` to jump to any of them. That is the difference between a file a
person can read and one only a program can.

Datasets that cause trouble: anything behind a login, anything about
identifiable people, Excel files with several sheets (accept them, but the
student notes which sheet), files above 100 MB (take a smaller extract and say
so in the README).

### Block 5 — second commit and wrap-up (10 min)

1. Source Control view: the README shows as modified, the data file as new.
   Click the README to see the added **Data** section highlighted.
2. Small file with a licence that allows it: commit both. Large or restricted
   file: commit only the README, which says how to fetch the data.
3. Message `Add dataset + provenance`, **Commit**.
4. Ask two or three students to read their **Data** section aloud. The test
   from the brief: could a stranger fetch the same bytes from this text alone?

Homework: task 6 of Seminar 2 (the five questions for their file), and the
installation for anyone who still lacks Python or Git.

---

## C. Checklist before the session

- Local copy running: `node scripts/serve-local.mjs 8123`, then
  `http://localhost:8123/02-intro-to-data/`.
- Your own VS Code reset to something students will recognise: default theme
  or a plain dark one, extensions panel not full of unrelated tools, zoom
  raised, a clean empty folder to open.
- `MasterclassData.root` and `D0_KPi.csv` on a USB stick in case the network
  fails; both are also in the workbook under `data/`.
- Reference values for the LHCb fallback are in the instructor notes at the end
  of the [Seminar 2 brief](seminar_02.md).
