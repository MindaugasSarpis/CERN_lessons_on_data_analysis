# Seminar 1 — Get Started with VS Code and Markdown

**Paired lecture:** 02 Introduction to Data · **Format:** follow-along, from zero · **~120 min**
(90 min in class, 30 min at home)

!!! abstract "Overview"
    **Time:** 17:15–18:45, with 15 min in reserve until 19:00

    **Questions**

    - Where do the files of one piece of work live?
    - How do I write a document that any program can open?
    - How do I record what a data file holds and where it came from?

    **After this seminar, students can**

    - open a project folder in VS Code and find their way in its window
    - write a README in Markdown: headings, a list, a table, a link
    - make the same edit on several lines at once
    - record the columns and the origin of a data file
    - turn a Markdown file into slides

    **The room ends with:** a folder `analysis-project` that holds
    `D0_KPi.csv`, a README that describes it, and three slides.

    **Needs:** a laptop and a web browser. Nothing installed, no
    programming experience. No Python, no Git, no terminal.

You do each step on the projector, and the room repeats it. After each
block ask: who sees this? Go on when about four in five do. The rest get
help from a neighbour. Keys are written for Windows and Linux, with macOS in
brackets: `Ctrl+S` (macOS `Cmd+S`).

| Block | Clock | Min | The room ends with |
|--|--|--|--|
| [1. Install VS Code](#install) | 17:15 | 10 | VS Code running |
| [2. Open a folder](#open-folder) | 17:25 | 5 | The project folder open |
| [3. Explore the user interface](#interface) | 17:30 | 8 | Five regions named, the Command Palette used |
| [4. Create folders and a file](#folders) | 17:38 | 7 | The project skeleton and an empty README |
| [5. Write Markdown](#markdown) | 17:45 | 12 | A README with headings, a list, a table, a link |
| [6. Look at a data file](#data-file) | 17:57 | 15 | The file in `data/raw/`, rows counted, seen in a spreadsheet |
| [7. Edit with several cursors](#multi-cursor) | 18:12 | 8 | A **Columns** table in the README |
| [8. Record where the data came from](#provenance) | 18:20 | 8 | A **Data** section in the README |
| [9. Turn the README into slides](#marp) | 18:28 | 12 | Three slides, exported to `results/` |
| [10. Wrap up](#wrap-up) | 18:40 | 5 | The homework known |

Blocks 1 to 5 are about the tools. Blocks 6 to 9 are about the data file
and need about 45 minutes. If the first half runs long, stop after block 5
and open the next session with block 6.

??? note "Before the session"
    - Your own VS Code looks like a fresh installation: default theme, Side
      Bar on the left, no `analysis-project` folder yet. You build it with
      the room.
    - A USB stick with the VS Code installers for Windows and macOS and with
      `D0_KPi.csv`, in case the network fails.
    - `D0_KPi.csv` opened once in the spreadsheet program on your laptop, so
      that you know which of the three outcomes in block 6 your computer
      shows.
    - Ask who has written code before. Seat each of them next to someone
      who has not. The rule for the experienced one: explain, never take
      the keyboard.

## 1. Install VS Code { #install }

<p class="block-meta">17:15 · 10 min</p>

**Say.** VS Code is a free editor for text and code. It looks and behaves
the same on Windows, macOS and Linux, so every screen in the room shows the
same thing.

1. Open `code.visualstudio.com` in a browser and select the **Download**
   button for your system.
2. Install it.
    - **Windows:** run the downloaded installer and keep every default.
    - **macOS:** open the downloaded file and drag **Visual Studio Code**
      into the **Applications** folder.
3. Start VS Code.
4. If a **Chat** panel is open on the right, close it with the **X** in its
   corner. It is not used today.

**You should now see** a window with a **Welcome** tab.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: the installer asks for an administrator password | Take the **User Installer** from the download page. It needs none |
    | macOS: "cannot be opened because it is from an unidentified developer" | The file was opened from **Downloads**. Drag it to **Applications** first |
    | macOS: VS Code is gone after a restart | It was started from the downloaded archive. Drag it to **Applications** |
    | A university or work laptop blocks the installation | Use [vscode.dev](https://vscode.dev) in Chrome or Edge today. It can open a local folder. Install at home |
    | The download is slow | Pass round the USB stick |

## 2. Open a folder { #open-folder }

<p class="block-meta">17:25 · 5 min</p>

**Say.** VS Code can open a single file, but it is made to work on a
folder. That folder is the project: everything that belongs to one piece of
work lives in it. For Excel users: a project folder is what a workbook is in
Excel, except that every sheet is a separate file.

1. In the file manager (File Explorer on Windows, Finder on macOS), create a
   folder named `analysis-project`, for example in **Documents**.
2. In VS Code select **File** > **Open Folder...** and pick
   `analysis-project`.
3. If a dialog asks whether you trust the authors, select
   **Yes, I trust the authors**.

**You should now see** the title `ANALYSIS-PROJECT` on the left, with
nothing under it.

!!! success "Key points"
    - VS Code works on a folder. The folder is the project.

## 3. Explore the user interface { #interface }

<p class="block-meta">17:30 · 8 min</p>

**Say.** The window has five regions. Show only what the room uses today. A
tour of every menu is forgotten by the end of the session.

```text title="The window"
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
| 4 | Panel | Hidden at first. It holds the terminal, which is used from next week |
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

**You should now see** your own theme, and the Explorer in the Side Bar.

!!! success "Key points"
    - Five regions: Activity Bar, Side Bar, Editor, Panel, Status Bar.
    - The Command Palette is the one shortcut to memorise today. Every
      other action can be found through it by typing part of its name.

## 4. Create folders and a file { #folders }

<p class="block-meta">17:38 · 7 min</p>

**Say.** A project has the same few folders every time. Files that were
downloaded are kept apart from everything that is made from them.

| Folder | What goes in |
|--|--|
| `data/raw` | Files exactly as downloaded. Never edited |
| `data/processed` | Cleaned versions, made later by scripts |
| `scripts` | Code |
| `results` | Figures and numbers that the code produces |

1. Move the mouse over the Side Bar. Four small icons appear next to the
   project name. Select **New Folder**, type `data` and press Enter.
2. Select `data`, then **New Folder**, and type `raw`. The Side Bar shows
   `data / raw` on one row: VS Code joins a folder with its only subfolder.
3. Select the empty area below the folders, then **New Folder**, and type
   `data/processed`. A name with `/` creates the folder in the right place.
4. Select the empty area again, then **New File**, and type `README.md`. The
   file opens in the Editor.

!!! question "Exercise 4.1 · 2 min"
    Create the folders `scripts` and `results` in the same way.

??? success "Solution"
    ```text title="The Side Bar"
    analysis-project/
    |- data/
    |  |- processed/
    |  |- raw/
    |- results/
    |- scripts/
    |- README.md
    ```

    VS Code lists folders first, so `README.md` is the last row.

!!! warning "Watch for"
    A new folder that lands inside the folder that was selected. This is the
    most common slip of the session. Drag the folder onto the empty area of
    the Side Bar to move it out. To rename, select it and press `F2` (macOS
    `Enter`).

!!! success "Key points"
    - `data/raw` holds files as downloaded. They are never edited.
    - VS Code only shows the folder. It is an ordinary folder on the disk:
      right-click > **Reveal in File Explorer** (macOS **Reveal in
      Finder**).

## 5. Write Markdown { #markdown }

<p class="block-meta">17:45 · 12 min</p>

**Say.** Markdown is plain text with a few signs for structure. Any editor
can open it, and it can be read without any formatting at all.
`README.md` is the first file anyone opens in a project. It says what the
project is and what is in it.

```text title="Type into README.md"
# Analysis Project

Seminar exercises for the course
*Best Research and Data Analysis Practices from CERN*.

The example data is from the [CERN Open Data Portal](https://opendata.cern.ch).
```

1. Look at the tab of the file. A dot means *not saved*. Save with `Ctrl+S`
   (macOS `Cmd+S`). Then select **File** > **Auto Save**.
2. Press `Ctrl+K`, release, then press `V` (macOS `Cmd+K`, then `V`). The
   preview opens beside the text.

```text title="Type, with your own answers"
## About

- **Author:** your name
- **Started:** 2026-09-29
- **Data I would like to look at:** one sentence

## Folders

| Folder | What goes in |
|--|--|
| `data/raw` | files exactly as downloaded, never edited |
| `data/processed` | cleaned versions, made later by scripts |
| `scripts` | code |
| `results` | figures and numbers that the code produces |
```

**You should now see** a formatted page on the right: one title, two
sections, a list with three items, a table with four rows, and a link.

Leave this table on the projector while the room types.

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

!!! success "Key points"
    - Markdown is plain text with a few signs for structure.
    - The README says what the project is and what is in it.

## 6. Look at a data file { #data-file }

<p class="block-meta">17:57 · 15 min</p>

**Say.** Everyone uses the same file, `D0_KPi.csv`, so that every screen
shows the same thing. It is the example file of the lecture. Students
choose their own dataset at home.

1. Download [`D0_KPi.csv`](../data/D0_KPi.csv) with the browser. The file
   lands in **Downloads**.
2. Drag the file from **Downloads** onto the `raw` folder in the Side Bar.
   Do not rename it.
3. Select the file in the Side Bar to open it.

!!! question "Exercise 6.1 · 3 min"
    Read line 1 and one line of numbers. What is written in line 1? Which
    character separates the values? Which character is the decimal
    separator?

??? success "Solution"
    Line 1 is `M,PT,TAU,IPCHI2`: the four column names. The comma separates
    the values. The point is the decimal separator.

!!! question "Exercise 6.2 · 3 min"
    How many rows of data does the file hold? `Ctrl+End` (macOS `Cmd+↓`)
    jumps to the end.

??? success "Solution"
    VS Code numbers 91 585 lines. The last one is empty, because the file
    ends with a line break. That leaves 91 584 lines: one header line and
    **91 583 rows of data**.

!!! question "Exercise 6.3 · 3 min"
    Press `Ctrl+F` (macOS `Cmd+F`) and type `-100`. How many places does
    VS Code find, and in which column?

??? success "Solution"
    49 places, all in the third column, `TAU`. In these rows the decay
    time could not be computed, and the file marks that with `-100`. This
    is how this file writes a missing value.

**Then, together:** open the same file in a spreadsheet program (Excel,
LibreOffice, Numbers) **without saving anything**. Right-click the file in
the Side Bar, select **Reveal in File Explorer** (macOS **Reveal in
Finder**), and open it from there. Ask who sees which of these:

| On the screen | Reason |
|--|--|
| The whole line in column A, as one text | The spreadsheet expects `;` between values |
| Four columns, but numbers turned into text or into wrong values | The spreadsheet expects `,` as the decimal separator |
| Four correct columns | The computer is set to English regional settings |

Close the spreadsheet. If it asks whether to save, the answer is **No**.

**Say.** This comparison is the centre of the session. The file is the same
on every laptop, and VS Code shows the same text on every laptop. The
spreadsheet shows an interpretation, and the interpretation depends on the
settings of the computer. Saving from the spreadsheet writes that
interpretation back into the file.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The file is named `D0_KPi (1).csv` | It was downloaded twice. Delete both and download once |
    | Safari shows the numbers in a tab instead of saving | **File** > **Save As...** |
    | The file is not under `raw` | It was dropped onto another folder. Drag it again |
    | Someone saved from the spreadsheet | They download the file again |

!!! success "Key points"
    - A CSV file is plain text. VS Code shows the same text on every
      laptop.
    - A spreadsheet shows an interpretation of the file.
    - A file in `data/raw/` is never edited and never saved from a
      spreadsheet.

## 7. Edit with several cursors { #multi-cursor }

<p class="block-meta">18:12 · 8 min</p>

**Say.** The README does not yet say what the four columns are. The names
are already in the data file, so they are copied, not typed again. VS Code
can put a cursor on several lines at once, and whatever is typed goes to
all of them.

1. In `D0_KPi.csv`, select line 1 and copy it. In `README.md`, add a section
   and paste the line under it.

    ```text title="README.md"
    ## Columns

    M,PT,TAU,IPCHI2
    ```

2. Select the first comma of that line. Press `Ctrl+D` (macOS `Cmd+D`) two
   times. Each press selects the next comma, so three are selected.
3. Press Enter. Every comma becomes a line break. Press `Esc` to return to
   one cursor.
4. Select the four lines. Press `Shift+Alt+I` (macOS `Shift+Option+I`). A
   cursor blinks at the end of every line.
5. Type ` |  |  |`. Press `Home` and type `| `. Press `Esc`.

    ```text title="You should now see"
    | M |  |  |
    | PT |  |  |
    | TAU |  |  |
    | IPCHI2 |  |  |
    ```

!!! question "Exercise 7.1 · 3 min"
    Add the two lines of the table head above the rows. Fill in the
    meaning and the unit of each column from what the lecture said about
    the file.

??? success "Solution"
    ```text title="README.md"
    | Column | Meaning | Unit |
    |--|--|--|
    | M | mass of the kaon and the pion together | MeV/c² |
    | PT | momentum of the pair across the beam | MeV/c |
    | TAU | decay time; `-100` means not computed | ns |
    | IPCHI2 | how well the pair points back to the collision | none |
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `Ctrl+D` selected a whole word | Nothing was selected before the first press. Select the comma with the mouse, then press |
    | The text was typed on one line only | `Esc` was pressed too early, or a click removed the cursors. Undo with `Ctrl+Z` (macOS `Cmd+Z`) and repeat |
    | Linux: `Shift+Alt+I` does nothing | Open the Command Palette and type `cursors to line ends` |

!!! success "Key points"
    - `Ctrl+D` selects the next occurrence. `Shift+Alt+I` puts a cursor at
      the end of every selected line. `Alt` and a click adds a cursor
      anywhere.
    - The same keys work on four lines and on four hundred.
    - A name that is copied cannot be misspelt.

## 8. Record where the data came from { #provenance }

<p class="block-meta">18:20 · 8 min</p>

**Say.** A data file without a note on its origin cannot be checked by
anyone, including its owner six months later. The note goes into the
README.

1. Open [record 401](https://opendata.cern.ch/record/401) of the CERN Open
   Data Portal in the browser. Find the DOI and the licence on the page
   together with the room.
2. Add a **Data** section to `README.md`. The room types the labels and
   looks up the values.

```text title="README.md"
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

!!! question "Exercise 8.1 · 2 min"
    Swap laptops with a neighbour. Using only the neighbour's README,
    could you find and download the same file? Tell them what was missing.

??? success "Solution"
    A reader needs the address or the DOI of the record, the name of the
    file, and its size to check the download. The README names the record's
    file `MasterclassData.root` as well, because the CSV in `data/raw/` is
    a converted copy and not the file a stranger would download.

!!! tip "The size of the file"
    Windows shows about 3 835 KB and macOS about 3.9 MB. Both are
    3 926 142 bytes: Windows counts in units of 1024, macOS in units of
    1000.

!!! success "Key points"
    - The README says where each data file came from.
    - The line **One row** is the one that needs thought.

## 9. Turn the README into slides { #marp }

<p class="block-meta">18:28 · 12 min</p>

**Say.** The README is plain text, and plain text can be shown in more than
one way. Marp is an extension of VS Code that shows a Markdown file as
slides. The slides of this course are written the same way.

1. Select the **Extensions** icon in the Activity Bar, type `marp` and
   install **Marp for VS Code**.
2. Create a file `slides.md` next to `README.md`.

```text title="Type into slides.md"
---
marp: true
---

# D0_KPi.csv

A data file from the CERN Open Data Portal

---

## One row

One candidate pair of a kaon and a pion from one collision

---

## Where it came from
```

3. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`). It
   shows three slides. A line with `---` starts a new slide.

!!! question "Exercise 9.1 · 4 min"
    Copy the **Columns** table from `README.md` to the second slide, and
    the list of the **Data** section to the third. Then export the slides:
    Command Palette, `marp export`, **Marp: Export Slide Deck...**, type
    **HTML**, saved as `results/slides.html`.

??? success "Solution"
    `results/slides.html` opens in the browser and shows three slides: the
    name of the file, its columns, and where it came from. The table was
    written once, in block 7. It is now in the README and on a slide, and
    it was never retyped.

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | The preview shows an ordinary page, not slides | `marp: true` is missing, or the file does not begin with `---` |
    | A line of text turned into a large heading | The empty line between the text and `---` is missing |
    | Export to PDF fails | PDF needs Chrome, Edge or Firefox on the computer. HTML needs nothing |
    | [vscode.dev](https://vscode.dev) in the browser: no export | The preview works there. Export at home, after installing VS Code |

!!! success "Key points"
    - The same text can be a document and a set of slides. It is written
      once.
    - If a unit turns out to be wrong, it is corrected in the text and
      exported again.

## 10. Wrap up { #wrap-up }

<p class="block-meta">18:40 · 5 min</p>

Put the homework on the projector and read it aloud. Say that an
installation which fails at home is not a problem: students bring the error
message, a photo of the screen is enough. Ask on the way out which step was
hardest.

!!! success "Key points of the seminar"
    - VS Code works on a folder. The folder is the project.
    - Markdown is plain text with a few signs for structure.
    - The README says what is in the project and where each data file came
      from.
    - Several cursors make the same edit on many lines at once.
    - A CSV file is plain text. A spreadsheet shows an interpretation of
      it.
    - A file in `data/raw/` is never edited.

!!! example "Homework · 30 min"
    1. **Choose a dataset of your own.** A table from a field you care
       about: weather, sport, prices, health, astronomy, your lab. Good
       places to look are the portals from the lecture (Eurostat,
       Copernicus, NASA, Zenodo, Kaggle) and the
       [Lithuanian open data portal](https://data.gov.lt). It should be a
       CSV file with at least a few hundred rows and at least one column
       of numbers.
    2. Put it in `data/raw/`. Add a second entry to the **Data** section
       as in block 8, a **Columns** table as in block 7, and a fourth
       slide in `slides.md`.
    3. Answer the five questions from the lecture for your file, in the
       README: how many rows and columns, what one row is, which columns
       are measured, derived or bookkeeping, the units, how missing values
       are marked.
    4. Install Python and Git by following
       [Install Python and Git](install_python_git.md).

## Stretch goals

For students who already program and finish a block early. These need the
terminal and Python.

!!! question "Stretch 1"
    Open the terminal with **Terminal** > **New Terminal** and compute the
    checksum of the file, a fingerprint that proves two copies are
    byte-identical.

??? success "Solution"
    ```text
    Windows (PowerShell)   Get-FileHash data\raw\D0_KPi.csv -Algorithm SHA256
    macOS                  shasum -a 256 data/raw/D0_KPi.csv
    Linux, Git Bash        sha256sum data/raw/D0_KPi.csv
    ```

    SHA-256 `25c3c972…c1505136` on every system.

!!! question "Stretch 2"
    Write `scripts/count_rows.py` that prints the number of data rows and
    the smallest and largest value of column `M`, without Pandas.

??? success "Solution"
    91 583 rows, with `M` from 1766.2096 to 2453.6584.

!!! question "Stretch 3"
    Download the record's original file `MasterclassData.root` and open it
    in VS Code. What happens?

??? success "Solution"
    The file is binary, so VS Code declines to show it as text.

!!! question "Stretch 4"
    Install the **Rainbow CSV** extension and open `D0_KPi.csv` again.

??? success "Solution"
    Each column gets its own colour.

## If students ask for more

Four parts of VS Code are kept for later weeks. If asked today, show it for
ten seconds and name the week. Marp is the only extension installed today.

| Part of VS Code | Week |
|--|--|
| The terminal in the Panel | 3 (Command Line) |
| The Status Bar: encoding, line endings | 4 (How Computers Work) |
| Source Control: saving and comparing versions | Git |
| The Python extension, running a script | Python Foundations |

Leave out altogether, even if asked: the debugger, settings sync, remote
development, AI assistants, Jupyter.

## Aims practised

♻️ provenance = reproducibility · 📁 raw data captured, untouched · 🔧 the same steps on every system · ⚙️ one edit on many lines, one text in two forms
