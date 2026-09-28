# Seminar 2 — First Hands-On: VS Code, a Project Folder, a Dataset

**Paired lecture:** 02 Introduction to Data · **Format:** hands-on, from scratch · **~120 min**

**Suggested timing:** 90 min in class (parts A–E) · 30 min at home (part F)

> **This is the first hands-on session and it starts from zero.** You need a
> laptop and a web browser. You do not need programming experience, and you do
> not need anything installed beforehand. If you have only ever used Excel,
> this brief is written for you.

> **This session builds:** a project folder with a data file in `data/raw/` and
> a README that says where the file came from.

> **Windows and macOS.** Every step works on both. Where a key differs, it is
> written as `Ctrl` / `Cmd`: Windows and Linux use the first, macOS the second.

## Goal
Get comfortable in the one program we use all semester, put a real data file
into a tidy project folder, and write down **where it came from**.

## Prerequisites
None.

## Tasks

Each part ends with a ✔ check. If your screen does not match the check, ask a
neighbour or raise a hand before moving on.

### Part A — Install and open VS Code (15 min)

1. Go to [code.visualstudio.com](https://code.visualstudio.com) and download
   VS Code for your system.
2. Install it.
    - **Windows:** run the downloaded installer and keep every default.
    - **macOS:** open the downloaded file and drag *Visual Studio Code* into
      the *Applications* folder.
3. Start VS Code.

✔ A window opens with a *Welcome* tab.

### Part B — Find your way around (20 min)

4. Create a folder named `analysis-project` somewhere you will find it again,
   for example in *Documents*. Use your normal file manager (File Explorer on
   Windows, Finder on macOS).
5. In VS Code choose **File → Open Folder…** and pick `analysis-project`.
   If asked whether you trust the authors, answer **Yes**.
6. Find the five regions of the window:

    | Region | Where | What it is for |
    |--|--|--|
    | Activity Bar | far left, a column of icons | switches what the Side Bar shows |
    | Side Bar | left | the files of your project |
    | Editor | centre | the file you are working on |
    | Panel | bottom, hidden at first | the terminal, used in later weeks |
    | Status Bar | bottom edge | facts about the open file |

7. Press `Ctrl+Shift+P` / `Cmd+Shift+P`. This is the **Command Palette**: a
   search box for everything VS Code can do. Type `theme`, choose
   *Preferences: Color Theme*, and pick one you like.

✔ The Side Bar shows the title `ANALYSIS-PROJECT` and nothing under it.

### Part C — Build the project folder (15 min)

8. Move the mouse over the Side Bar. Four small icons appear next to the
   project name. Click **New Folder** and type `data`. Press Enter.
9. Click on `data`, then **New Folder** again, and type `raw`.
10. In the same way create `data/processed`, `scripts` and `results`.
    Click on the empty area of the Side Bar first, so that the new folder is
    created at the top level and not inside `data`.
11. Click on the empty area again, then **New File**, and type `README.md`.
12. The file opens in the Editor. Type:

    ```text
    # Analysis Project

    Seminar exercises for the course.
    ```

13. Look at the tab of the file: a dot means *not saved*. Save with `Ctrl+S` /
    `Cmd+S`. Then switch on **File → Auto Save**, so this cannot be forgotten.
14. Press `Ctrl+Shift+V` / `Cmd+Shift+V` to see the README as a formatted page.

✔ Your Side Bar shows exactly this:

```text
analysis-project/
|- README.md
|- data/
|  |- processed/
|  |- raw/
|- results/
|- scripts/
```

### Part D — Get a data file and look at it (25 min)

Everyone starts with the same file, the example from today's lecture. You
choose your own dataset in part F.

15. Download [`D0_KPi.csv`](../data/D0_KPi.csv) with your browser. It lands in
    your *Downloads* folder.
16. Drag the file from *Downloads* onto the `raw` folder in the VS Code Side
    Bar. Do **not** rename it.
17. Click the file in the Side Bar to open it. Answer on paper:
    - What is written in line 1?
    - Which character separates the values in a line?
    - How many lines does the file have? Press `Ctrl+End` / `Cmd+↓` to jump to
      the end and read the line number.
18. Press `Ctrl+G`, type `5000`, press Enter. You are at line 5000.
19. Now open the same file in Excel (or LibreOffice, or Numbers) **without
    saving anything**. Compare with VS Code:
    - Does each value sit in its own column, or is the whole line in column A?
    - Do the numbers look the same as in VS Code? Look at the decimal point.
20. Close the spreadsheet. If it asks whether to save, answer **No**.

✔ You know the number of data rows (lines minus the header line) and the four
column names.

> **Why two programs?** VS Code shows the file as it is: plain text. A
> spreadsheet shows its *interpretation* of the file, and may change numbers,
> dates and decimal separators when it saves. The file in `data/raw/` is never
> edited and never saved from a spreadsheet.

### Part E — Write down where it came from (15 min)

21. Open `README.md` and add a **Data** section. Fill in the lines from the
    record on the CERN Open Data Portal,
    [record 401](https://opendata.cern.ch/record/401):

    ```text
    ## Data

    Source:   CERN Open Data Portal, record 401
    DOI:      (copy it from the record page)
    Licence:  (copy it from the record page)
    Fetched:  (today's date, as YEAR-MONTH-DAY)
    File:     data/raw/D0_KPi.csv — converted from the record's
              MasterclassData.root by the course's root_to_csv.py
    One row:  (one sentence: what does one line of the file describe?)
    ```

22. Add the file's size (from your file manager) and the number of data rows
    you counted in step 17.
23. Swap laptops with a neighbour. Using only their README, could you find and
    download the same file? Tell them what was missing.

✔ Your README has a **Data** section that a stranger could follow.

### Part F — At home, before next week (30 min)

24. **Choose your own dataset.** Pick a table of data from a field you care
    about: weather, sport, prices, health, astronomy, your lab. Good places to
    look are the portals from the lecture (Eurostat, Copernicus, NASA, Zenodo,
    Kaggle) and the [Lithuanian open data portal](https://data.gov.lt). It
    should be a CSV file with at least a few hundred rows and at least one
    column of numbers.
25. Put it in `data/raw/` and add a second entry to the **Data** section of
    your README, with the same lines as in step 21.
26. Answer the five questions from the lecture for your file, in the README:
    how many rows and columns; what one row is; which columns are measured,
    derived or bookkeeping; the units; how missing values are marked.
27. Install Python and Git by following [Seminar 1](seminar_01.md). Neither
    was needed today; both are needed from week 4.

## Stretch goals

For those who already program. Do them in class if you finish early.

- Open the terminal with **Terminal → New Terminal** and compute the file's
  checksum, a fingerprint that proves two copies are byte-identical:

    ```text
    Windows (PowerShell)   Get-FileHash data\raw\D0_KPi.csv -Algorithm SHA256
    macOS                  shasum -a 256 data/raw/D0_KPi.csv
    Linux, Git Bash        sha256sum data/raw/D0_KPi.csv
    ```

  Add it to the README and compare with a neighbour on the other system.
- Write `scripts/count_rows.py` that prints the number of data rows and the
  smallest and largest value of column `M`, without Pandas.
- One column contains the value `-100` in a few dozen rows. Which column, and
  what could it mean?
- Download the record's original file `MasterclassData.root` and try to open it
  in VS Code. What happens, and why?

## Wrap-up (last 5 min)
- Look at your project folder in the normal file manager: it is an ordinary
  folder, and VS Code only showed it to you.
- Say in one sentence what "provenance" means.
- Note which step was hardest; tell the lecturer on the way out.

## Solution notes (instructor)
The run-of-show, the VS Code tour and the list of common problems are in the
[lecturer's brief](lecturer_02.md). Reference values: `D0_KPi.csv` has
91 583 data rows + 1 header line, four columns (`M`, `PT`, `TAU`, `IPCHI2`),
3 926 142 bytes, SHA-256 `25c3c972…c1505136`. Record 401: DOI
`10.7483/OPENDATA.LHCb.E7EJ.JUWR`, licence CC0. The `-100` values are in `TAU`
(49 rows) and mark an invalid decay time. `MasterclassData.root` is binary, so
VS Code declines to show it as text.

## Aims practised
♻️ provenance = reproducibility · 📁 raw data captured, untouched · 🔧 the same steps on every system
