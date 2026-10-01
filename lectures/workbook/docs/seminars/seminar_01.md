# Seminar 1 — Get Started with VS Code and Markdown

**Paired lecture:** 02 Introduction to Data · **Format:** follow-along, from zero · **~120 min**
(90 min in class, 30 min at home)

The seminar has three parts, in this order.

1. **VS Code.** The room installs Visual Studio Code, learns the parts of its
   window and builds a project folder.
2. **Markdown.** The room writes a first document: the README of that folder.
3. **Both, on a data file.** A real data file is opened in VS Code, and the
   README records where the file came from.

It is the first hands-on session of the course and it starts from zero.
Today needs VS Code and a web browser. No Python, no Git, no terminal.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows and Linux, with macOS in brackets:
`Ctrl+S` (macOS `Cmd+S`).

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · VS Code** · 40 min | |
| 0:00 | [1. Install VS Code](#install) | VS Code running |
| 0:15 | [2. Open a folder](#open-folder) | The project folder open |
| 0:20 | [3. Explore the user interface](#interface) | Five regions named, the Command Palette used |
| 0:30 | [4. Create folders and a file](#folders) | The project skeleton and an empty README |
| | **Part 2 · Markdown** · 15 min | |
| 0:40 | [5. Write Markdown](#markdown) | A README with headings, a list, a table, a link |
| | **Part 3 · Both, on a data file** · 30 min | |
| 0:55 | [6. Look at a data file](#data-file) | The file in `data/raw/`, rows counted, seen in a spreadsheet |
| 1:15 | [7. Record where the data came from](#provenance) | A **Data** section in the README |
| 1:25 | [8. Wrap up](#wrap-up) | The homework known |

If time runs short, stop after Part 2. Part 3 then moves to the start of the
next session.

## Prerequisites

For the room: a laptop and a web browser. Nothing installed, no programming
experience.

For you, before the session:

- Your own VS Code looks like a fresh installation: default theme, Side Bar
  on the left, no `analysis-project` folder yet. You build it with the room.
- A USB stick with the VS Code installers for Windows and macOS and with
  `D0_KPi.csv`, in case the network fails.
- `D0_KPi.csv` opened once in the spreadsheet program on your laptop, so that
  you know which of the three outcomes in section 6 your computer shows.
- This page open on a second device, or printed.

At the start, ask who has written code before. Seat each of them next to
someone who has not. The rule for the experienced one: explain, never take
the keyboard.

## Part 1 · VS Code { #part-1 }

**0:00 to 0:40 · sections 1 to 4**

The room ends this part with VS Code installed and a project folder open in
it. Nothing is typed into a file yet.

## 1. Install VS Code { #install }

**0:00 · 15 min**

VS Code is a free editor for text and code. It looks and behaves the same on
Windows, macOS and Linux, so every screen in the room shows the same thing.
Everything done today by clicking can be done in any other editor.

1. Open `code.visualstudio.com` in a browser and select the **Download**
   button for your system.

2. Install it.

    - **Windows:** run the downloaded installer and keep every default.
    - **macOS:** open the downloaded file and drag **Visual Studio Code**
      into the **Applications** folder.

3. Start VS Code.

4. If a **Chat** panel is open on the right, close it with the **X** in its
   corner. It is not used today.

You should now see a window with a **Welcome** tab.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the installer asks for an administrator password | Take the **User Installer** from the download page. It needs none |
    | macOS: "cannot be opened because it is from an unidentified developer" | The file was opened from **Downloads**. Drag it to **Applications** first |
    | macOS: VS Code is gone after a restart | It was started from the downloaded archive. Drag it to **Applications** |
    | A university or work laptop blocks the installation | Use [vscode.dev](https://vscode.dev) in Chrome or Edge today. It can open a local folder. Install at home |
    | The download is slow | Pass round the USB stick |

## 2. Open a folder { #open-folder }

**0:15 · 5 min**

VS Code can open a single file, but it is made to work on a folder. That
folder is the project: everything that belongs to one piece of work lives in
it. For Excel users: a project folder is what a workbook is in Excel, except
that every sheet is a separate file.

1. In the file manager (File Explorer on Windows, Finder on macOS), create a
   folder named `analysis-project`, for example in **Documents**.

2. In VS Code select **File** > **Open Folder...** and pick
   `analysis-project`.

3. If a dialog asks whether you trust the authors, select
   **Yes, I trust the authors**.

You should now see the title `ANALYSIS-PROJECT` on the left, with nothing
under it.

## 3. Explore the user interface { #interface }

**0:20 · 10 min**

The window has five regions. Point at each one on the projector and name it.

```text
+---+-------------+------------------------------------+
|   |             |                                    |
| 1 |      2      |                 3                  |
|   |             |                                    |
|   |             +------------------------------------+
|   |             |                 4                  |
+---+-------------+------------------------------------+
|                          5                           |
+------------------------------------------------------+
```

| | Region | What it is for |
|--|--|--|
| 1 | Activity Bar | A column of icons. Each one switches what the Side Bar shows |
| 2 | Side Bar | The files of the project. This view is called the **Explorer** |
| 3 | Editor | The file you are working on. Several files open as tabs |
| 4 | Panel | Hidden at first. It holds the terminal, which is used in later weeks |
| 5 | Status Bar | Facts about the open file |

1. Select the icons of the Activity Bar one after another and watch the Side
   Bar change. Finish on the top icon, the **Explorer**.

2. Press `Ctrl+B` (macOS `Cmd+B`) twice. The Side Bar hides and comes back.

3. Press `Ctrl+Shift+P` (macOS `Cmd+Shift+P`). This is the
   **Command Palette**: a search box for everything VS Code can do.

4. Type `theme` and select **Preferences: Color Theme**. Move through the
   list with the arrow keys and press Enter on the theme you like.

5. Press `Ctrl+=` (macOS `Cmd+=`) to make everything larger and `Ctrl+-`
   (macOS `Cmd+-`) to make it smaller. Set your own zoom for the projector
   now.

You should now see your own theme, and the Explorer in the Side Bar.

!!! tip
    The Command Palette is the one shortcut worth memorising today. Every
    other action can be found through it by typing part of its name.

## 4. Create folders and a file { #folders }

**0:30 · 10 min**

A project has the same few folders every time. Files that were downloaded
are kept apart from everything that is made from them.

| Folder | What goes in |
|--|--|
| `data/raw` | Files exactly as downloaded. Never edited |
| `data/processed` | Cleaned versions, made later by scripts |
| `scripts` | Code |
| `results` | Figures and numbers that the code produces |

1. Move the mouse over the Side Bar. Four small icons appear next to the
   project name. Select **New Folder**, type `data` and press Enter.

2. Select `data`, then **New Folder**, and type `raw`.

    The Side Bar shows `data / raw` on one row. VS Code joins a folder with
    its only subfolder. The row splits in the next step.

3. Select the empty area below the folders, then **New Folder**, and type
   `data/processed`. A name with `/` creates the folder in the right place.

4. The room does this step alone: create `scripts` and `results` the same
   way.

5. Select the empty area again, then **New File**, and type `README.md`. The
   file opens in the Editor.

6. Right-click `README.md` and select **Reveal in File Explorer** (macOS
   **Reveal in Finder**). It is an ordinary file in an ordinary folder. VS
   Code only shows it.

You should now see this in the Side Bar. VS Code lists folders first, so
`README.md` is the last row.

```text
analysis-project/
|- data/
|  |- processed/
|  |- raw/
|- results/
|- scripts/
|- README.md
```

!!! warning "Watch for"
    A new folder that lands inside the folder that was selected. This is the
    most common slip of the session. Drag the folder onto the empty area of
    the Side Bar to move it out. To rename, select it and press `F2` (macOS
    `Enter`).

## Part 2 · Markdown { #part-2 }

**0:40 to 0:55 · section 5**

The room ends this part with a README that has a title, two sections, a
list, a table and a link, and with the preview open beside the text.

## 5. Write Markdown { #markdown }

**0:40 · 15 min**

Markdown is plain text with a few signs for structure: `#` starts a heading,
`-` starts a list item, `**` makes text bold. Any editor can open it, and it
can be read without any formatting at all. The file name ends in `.md`.

`README.md` is the first file anyone opens in a project. It says what the
project is and what is in it.

1. Type into `README.md`:

    ```text
    # Analysis Project

    Seminar exercises for the course
    *Best Research and Data Analysis Practices from CERN*.
    ```

2. Look at the tab of the file. A dot means *not saved*. Save with `Ctrl+S`
   (macOS `Cmd+S`). Then select **File** > **Auto Save**, so that saving
   cannot be forgotten.

3. Press `Ctrl+K`, release, then press `V` (macOS `Cmd+K`, then `V`). The
   preview opens beside the text: what you type is on the left, the
   formatted page on the right.

4. Add a section with a list. Each student fills in their own answers. The
   last line is the answer from the lecture's thought exercise.

    ```text
    ## About

    - **Author:** your name
    - **Started:** 2026-09-29
    - **Data I would like to look at:** one sentence
    ```

5. Add a section with a table.

    ```text
    ## Folders

    | Folder | What goes in |
    |--|--|
    | `data/raw` | files exactly as downloaded, never edited |
    | `data/processed` | cleaned versions, made later by scripts |
    | `scripts` | code |
    | `results` | figures and numbers that the code produces |
    ```

6. Add a link under the first paragraph.

    ```text
    The example data is from the [CERN Open Data Portal](https://opendata.cern.ch).
    ```

You should now see a formatted page on the right: one title, two sections, a
list with three items, a table with four rows, and a link that opens the
portal.

Leave this table on the projector while the room types:

| You type | You get |
|--|--|
| `# Title` | The title of the page |
| `## Section` | A section heading |
| `*text*` | Italic |
| `**text**` | Bold |
| `- item` | A list item |
| `` `text` `` | A file name or code |
| `[text](address)` | A link |
| `| a | b |` | A row of a table |

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | `#Title` stays plain text | The space after `#` is missing |
    | The list or the table runs into the paragraph above | The empty line before it is missing |
    | The table shows as text with `|` signs | The second line, `|--|--|`, is missing |

## Part 3 · Both, on a data file { #part-3 }

**0:55 to 1:25 · sections 6 and 7**

Section 6 uses VS Code from Part 1 to read a data file. Section 7 uses
Markdown from Part 2 to write down where the file came from.

## 6. Look at a data file { #data-file }

**0:55 · 20 min**

Everyone uses the same file, `D0_KPi.csv`, so that every screen in the room
shows the same thing. It is the file from the lecture's section
*A Dataset Up Close*. Students choose their own dataset at home.

1. Download [`D0_KPi.csv`](../data/D0_KPi.csv) with the browser. The file
   lands in **Downloads**.

2. Drag the file from **Downloads** onto the `raw` folder in the Side Bar.
   Do not rename it.

3. Select the file in the Side Bar to open it. Read line 1 and one line of
   numbers.

    | Question | Answer |
    |--|--|
    | What is written in line 1? | `M,PT,TAU,IPCHI2`: the four column names |
    | Which character separates the values? | The comma |
    | Which character is the decimal separator? | The point |

4. Press `Ctrl+End` (macOS `Cmd+↓`) to jump to the end, and read the line
   number on the left.

    VS Code numbers 91 585 lines. The last one is empty, because the file
    ends with a line break. That leaves 91 584 lines: one header line and
    **91 583 rows of data**.

5. Press `Ctrl+G` (the same key on macOS), type `5000` and press Enter. Line
   5000 begins with `1868.8636`.

6. Press `Ctrl+F` (macOS `Cmd+F`) and type `-100`. VS Code finds 49 places,
   all in the third column, `TAU`. In these rows the decay time could not be
   computed, and the file marks that with `-100`. This is how this file
   writes a missing value.

7. Open the same file in a spreadsheet program (Excel, LibreOffice, Numbers)
   **without saving anything**. Right-click the file in the Side Bar, select
   **Reveal in File Explorer** (macOS **Reveal in Finder**), and open it from
   there. A student without a spreadsheet program looks at a neighbour's
   screen.

    Ask who sees which of these:

    | On the screen | Reason |
    |--|--|
    | The whole line in column A, as one text | The spreadsheet expects `;` between values |
    | Four columns, but numbers turned into text or into wrong values | The spreadsheet expects `,` as the decimal separator |
    | Four correct columns | The computer is set to English regional settings |

8. Close the spreadsheet. If it asks whether to save, the answer is **No**.

You should now have `D0_KPi.csv` in `data/raw/`, and every student can say
the number of data rows and the four column names.

This comparison is the centre of the session. Say it in these words: the
file is the same on every laptop, and VS Code shows the same text on every
laptop. The spreadsheet shows an interpretation, and the interpretation
depends on the settings of the computer. Saving from the spreadsheet writes
that interpretation back into the file. That is why a file in `data/raw/` is
never edited and never saved from a spreadsheet.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The file is named `D0_KPi (1).csv` | It was downloaded twice. Delete both and download once |
    | Safari shows the numbers in a tab instead of saving | **File** > **Save As...** |
    | The file is not under `raw` | It was dropped onto another folder. Drag it again |
    | Someone saved from the spreadsheet | They download the file again |

## 7. Record where the data came from { #provenance }

**1:15 · 10 min**

A data file without a note on its origin cannot be checked by anyone,
including its owner six months later. The note goes into the README. It is
written in the Markdown from section 5.

1. Open [record 401](https://opendata.cern.ch/record/401) of the CERN Open
   Data Portal in the browser. Find the DOI and the licence on the page
   together with the room.

2. Add a **Data** section to `README.md`. The room types the labels and
   looks up the values. Filled in, the section reads:

    ```text
    ## Data

    - **Source:** CERN Open Data Portal, record 401
    - **Address:** https://opendata.cern.ch/record/401
    - **DOI:** 10.7483/OPENDATA.LHCb.E7EJ.JUWR
    - **Licence:** CC0
    - **Fetched:** 2026-09-29
    - **File:** `data/raw/D0_KPi.csv`, converted from the record's
      `MasterclassData.root` by the course's `root_to_csv.py`
    - **Size:** 3 926 142 bytes, 91 583 rows, 4 columns
    - **One row:** one candidate pair of a kaon and a pion from one collision
    ```

    The line **One row** is the one that needs thought. Give the room a
    minute before you show the answer.

3. Look up the size of the file in the file manager. Windows shows about
   3 835 KB and macOS about 3.9 MB. Both are 3 926 142 bytes: Windows counts
   in units of 1024, macOS in units of 1000.

4. Swap laptops with a neighbour. Using only the neighbour's README, could
   you find and download the same file? Tell them what was missing. This
   takes three minutes.

You should now see a **Data** section in the preview that a stranger could
follow.

The record holds `MasterclassData.root`, and the CSV is a converted copy. The
README names both, because the file in `data/raw/` is not the file a
stranger would download from the portal.

## 8. Wrap up { #wrap-up }

**1:25 · 5 min**

Put the three tasks of the next section on the projector and read them
aloud. Then:

- Say that an installation which fails at home is not a problem. Students
  bring the error message, a photo of the screen is enough, and it gets
  fixed at the start of the next session.
- Ask on the way out which step was hardest.

What the room has learned:

- VS Code works on a folder. The folder is the project.
- Markdown is plain text with a few signs for structure.
- The README says what is in the project and where each data file came from.
- A CSV file is plain text. VS Code shows the same text on every laptop.
- A spreadsheet shows an interpretation of the file, and the interpretation
  depends on the computer.
- A file in `data/raw/` is never edited.

## Next steps, at home

**30 min, before the next session**

1. **Choose a dataset of your own.** A table from a field you care about:
   weather, sport, prices, health, astronomy, your lab. Good places to look
   are the portals from the lecture (Eurostat, Copernicus, NASA, Zenodo,
   Kaggle) and the [Lithuanian open data portal](https://data.gov.lt). It
   should be a CSV file with at least a few hundred rows and at least one
   column of numbers.

2. Put it in `data/raw/` and add a second entry to the **Data** section of
   the README, with the same lines as in section 7.

3. Answer the five questions from the lecture for your file, in the README:
   how many rows and columns, what one row is, which columns are measured,
   derived or bookkeeping, the units, how missing values are marked.

4. Install Python and Git by following
   [Install Python and Git](install_python_git.md). Neither was needed
   today.

## Stretch goals

For students who already program and finish a section early. These need the
terminal and Python. Answers are given for the lecturer.

- Open the terminal with **Terminal** > **New Terminal** and compute the
  checksum of the file, a fingerprint that proves two copies are
  byte-identical. The answer is SHA-256 `25c3c972…c1505136` on every system.

    ```text
    Windows (PowerShell)   Get-FileHash data\raw\D0_KPi.csv -Algorithm SHA256
    macOS                  shasum -a 256 data/raw/D0_KPi.csv
    Linux, Git Bash        sha256sum data/raw/D0_KPi.csv
    ```

- Write `scripts/count_rows.py` that prints the number of data rows and the
  smallest and largest value of column `M`, without Pandas. The answer is
  91 583 rows, with `M` from 1766.2096 to 2453.6584.
- Download the record's original file `MasterclassData.root` and open it in
  VS Code. The file is binary, so VS Code declines to show it as text.
- Install the **Rainbow CSV** extension from the Extensions view of the
  Activity Bar and open `D0_KPi.csv` again. Each column gets its own colour.

## If students ask for more

Four parts of VS Code are kept for later weeks. If asked today, show it for
ten seconds and name the week.

| Part of VS Code | Week |
|--|--|
| The Status Bar: encoding, line endings | 3 (How Computers Work) |
| The terminal in the Panel | 4 (Command Line) |
| Source Control: saving and comparing versions | 6 (Git) |
| Extensions: Python, running a script | 7 (Python Foundations) |

Leave out altogether, even if asked: the debugger, settings sync, remote
development, AI assistants, Jupyter.

## Aims practised

♻️ provenance = reproducibility · 📁 raw data captured, untouched · 🔧 the same steps on every system
