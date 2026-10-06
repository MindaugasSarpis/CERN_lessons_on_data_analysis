# Seminar 14 — Review an Analysis, Plan the Data

**Paired lecture:** 14 Concepts of Data Analysis · **Format:** follow-along, then in pairs · **~120 min**
in class

**Today's goal:** every student rebuilds and reviews a neighbour's project,
answers the review of their own, and writes a data management plan of one
page.

No new tool is needed. The session uses the project folder as it stands
after Seminar 13, the terminal of VS Code and GitHub.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · A review, together** · 30 min | | |
| 0:00 | [1. Read the report, run the script](#run) | `python scripts/fit_g_example.py` | An error message, and the first comment |
| 0:10 | [2. Compare the numbers](#compare) | The two lines that remove rows | 9.84 ± 0.09 against the 9.81 of the report |
| 0:20 | [3. Write the review](#write) | `review_example.md` | `review_example.md` with six comments |
| | **Part 2 · A review, in pairs** · 45 min | | |
| 0:30 | [4. Get the neighbour's project](#clone) | **Git: Clone** | The neighbour's folder on your own laptop |
| 0:40 | [5. Rebuild it](#rebuild) | `python run_all.py` | Their numbers rebuilt, or the place where it stopped |
| 0:55 | [6. Twelve questions](#questions) | The table of twelve questions | `review.md`, sent to the author |
| | **Part 3 · The answer** · 15 min | | |
| 1:15 | [7. Answer the review](#answer) | **Answer:** under a comment, then `git push` | Every comment answered, one fix committed |
| | **Part 4 · A plan for the data** · 25 min | | |
| 1:30 | [8. Six headings](#dmp) | `DMP.md` with six headings | `DMP.md` filled in and committed |
| 1:55 | [9. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** do Part 1 as a demonstration in 15 minutes, with the
room watching and not typing. Part 3 stays in class.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops. In Part 2 the pairs work on
      their own and you walk through the room.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Commands are typed in the terminal of VS Code, in the project folder:
    `zsh` on macOS, PowerShell 7 on Windows. Keys are written for Windows,
    with macOS in brackets. Where a step differs between systems, it has a
    tab for each: `python3` on macOS, `python` on Windows.

??? info "Before the session"
    For the room: the project folder as it stands after Seminar 13, with a
    README, `data/raw`, `data/processed/pendulum.csv`, scripts,
    `requirements.txt` and `run_all.py`; Python and Git from
    [Seminar 4](seminar_04.md); and the project pushed to its remote
    repository ([Seminar 5](seminar_05.md), [Seminar 13](seminar_13.md)).
    A student without a working project reviews in a group of three. No
    student needs a dataset of their own: section 8 is written for the
    course files.

    For you:

    - [`concepts_fit_g.py`](../data/concepts_fit_g.py) downloaded, and
      sections 1 to 3 done once on your own laptop.
    - The twelve questions of the lecture on a second screen or printed:
      they are repeated in [section 6](#questions).
    - Pairs decided. Seat students next to someone whose project they have
      not seen.

??? info "Files for this seminar"
    A browser saves the file under the name in the second column.

    | File | Saved as | What it is |
    |--|--|--|
    | [`concepts_fit_g.py`](../data/concepts_fit_g.py){ download="fit_g_example.py" } | `fit_g_example.py` | Section 1: the script of the report, which reads a file from the author's desktop |

---

## Part 1 · A review, together { #part-1 }

**0:00 to 0:30 · sections 1 to 3**

A report of six lines and a script of thirty. The room does what a reviewer
does: run it, compare, write down what was found.

---

### 1. Read the report, run the script { #run }

**0:00 · 10 min**

**Tell the room.** A review starts by running the work, not by reading it.
The first thing a reviewer learns is whether the analysis runs anywhere but
on the author's laptop.

1. Show the report on the projector. It is all there is.

    ```text
    # Pendulum report

    ## Result

    The rows at 20 cm and 80 cm were outliers and were removed.

    g = 9.81 m/s², in excellent agreement with the expected value.

    ![The fit](fit.png)
    ```

2. Download
   [`concepts_fit_g.py`](../data/concepts_fit_g.py){ download="fit_g_example.py" }
   and drag it onto the `scripts` folder. It is named:

    ```text
    fit_g_example.py
    ```

3. Run it from the project folder.

    === "macOS"

        ```text
        python3 scripts/fit_g_example.py
        ```

    === "Windows"

        ```text
        python scripts/fit_g_example.py
        ```

4. Read the last line of the traceback with the room.

    ```text
    FileNotFoundError: C:/Users/student/Desktop/pendulum.csv not found.
    ```

5. Open the script and find the line with that path. Replace the path by
   the one below and save.

    ```text
    data/processed/pendulum.csv
    ```

!!! success "You should now see"
    The script open in the Editor with the corrected path, and the room can
    say the first review comment: the script reads a file from the author's
    desktop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No module named numpy` | The environment of Seminar 13 is not active: the prompt does not start with `(.venv)`. Activate it with `source .venv/bin/activate` (Windows `.venv\Scripts\Activate.ps1`) and run the line again |
    | `can't open file ... fit_g_example.py` | The terminal is not in the project folder, or the file is still in **Downloads** |

---

### 2. Compare the numbers { #compare }

**0:10 · 10 min**

**Tell the room.** Now the script runs. The question is whether it gives
what the report says. A reviewer compares number by number and writes down
both.

1. Run the script again. It prints:

    ```text
    rows   9
    slope  4.010 +- 0.037 s^2/m
    g      9.84 +- 0.09 m/s^2
    pulls  0.12 0.39 -0.93 0.36 -0.52 0.57 -0.38 0.77 -0.39
    ```

2. Ask the room what differs from the report. Three things: the report
   says 9.81 and the script 9.84; the report has no uncertainty; the report
   speaks of removed rows and the script uses all nine.

3. Find the pulls of the two rows the report calls outliers. The rows are
   in the order of the table: 20 cm is the first, 80 cm the seventh. Their
   pulls are 0.12 and −0.38. The largest in the table is −0.93.

4. Check the report's claim. Add two lines below the line that reads the
   file, save, and run again.

    ```text
    keep = (data[:, 0] != 20) & (data[:, 0] != 80)
    data = data[keep]
    ```

    The script now prints:

    ```text
    rows   7
    slope  4.023 +- 0.050 s^2/m
    g      9.81 +- 0.12 m/s^2
    pulls  0.50 -0.88 0.36 -0.56 0.50 0.64 -0.55
    ```

5. Ask whether any script writes `fit.png`. None does: the report shows a
   figure that cannot be rebuilt.

!!! success "You should now see"
    `g      9.81 +- 0.12 m/s^2` in the terminal, and the room can say why the
    report's 9.81 could not be rebuilt from the script as it was handed out.

**Say it in these words.** The 9.81 is real, and it took two lines that the
author never showed. Nothing made those two rows outliers. They were the
two whose removal gave the expected value.

---

### 3. Write the review { #write }

**0:20 · 10 min**

**Tell the room.** A review is a list of comments that the author can act
on. Each comment says what was run and what came out, and is marked as
*must fix*, *suggestion* or *question*.

1. Create a file in the project folder named:

    ```text
    review_example.md
    ```

2. Type the heading and the first comment with the room.

    ```text
    # Review of the pendulum report

    Run on Windows 11, Python 3.13, 2026-12-29.

    1. **Must fix.** `fit_g_example.py` reads
       `C:/Users/student/Desktop/pendulum.csv`. On my laptop:
       FileNotFoundError. With `data/processed/pendulum.csv` it runs.
    ```

3. The room writes the other comments alone, for five minutes.

4. Collect them on the projector. A complete review has these six.

    | | Mark | Comment |
    |--|--|--|
    | 1 | Must fix | The path points to the author's desktop |
    | 2 | Must fix | The script gives 9.84 ± 0.09 from nine rows. The report says 9.81. The script removes no row |
    | 3 | Must fix | With the two rows removed I get 9.81 ± 0.12. Their pulls were 0.12 and −0.38, the largest in the table is −0.93. Why are they outliers? |
    | 4 | Must fix | The report gives no uncertainty |
    | 5 | Must fix | The report shows `fit.png`. No script makes it |
    | 6 | Question | *Excellent agreement*, at ± 0.12? |

5. Delete `scripts/fit_g_example.py`: right-click it in the Side Bar and
   select **Delete**. Keep `review_example.md` as a model for the next part.

!!! success "You should now see"
    A `review_example.md` with at least four of the six comments on every
    laptop.

!!! warning "Watch for"
    Comments about the author ("careless", "did not think"). A comment is
    about the work: what was run, what came out, what is missing.

---

## Part 2 · A review, in pairs { #part-2 }

**0:30 to 1:15 · sections 4 to 6**

Each student is now reviewer of one project and author of another. The
reviewer works on their own laptop and does not ask the author anything
before the review is written. A question the reviewer has to ask is a line
missing from the README.

---

### 4. Get the neighbour's project { #clone }

**0:30 · 10 min**

**Tell the room.** The reviewer needs the project as a stranger would get
it: from the remote repository, into an empty folder.

1. The author opens the repository on GitHub, then **Settings** >
   **Collaborators** > **Add people**, and enters the reviewer's user name.
   The reviewer accepts the invitation: it arrives by e-mail and under
   **Notifications**.

2. The reviewer copies the address of the repository from the green
   **Code** button, the one that starts with `https://`.

3. The reviewer opens a new window of VS Code, presses `Ctrl+Shift+P`
   (macOS `Cmd+Shift+P`) and types:

    ```text
    Git: Clone
    ```

    Paste the address and choose a folder outside your own project, for
    example **Documents**.

4. When VS Code asks, select **Open**. The neighbour's project is open.

!!! success "You should now see"
    The neighbour's files in the Side Bar, and their `README.md` in the
    Editor.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `Repository not found` | The invitation is not accepted yet. Open the link in the e-mail |
    | The author has no remote repository | The author compresses the project folder without `.venv` and passes it on a USB stick. The reviewer unpacks it into **Documents** |
    | The cloned folder has no data | Large or raw data is kept out of the repository. The README has to say how to fetch it: that is question 1 |

---

### 5. Rebuild it { #rebuild }

**0:40 · 15 min**

**Tell the room.** The reviewer follows the neighbour's README, and nothing
else. The aim is to get the numbers of the report out of the files of the
repository.

1. Read `README.md` from top to bottom before typing anything.

2. Do what it says to set up: fetch the data, create the environment,
   install the packages. Write down every step that the README did not
   give and that had to be guessed.

3. Run the command that rebuilds the analysis. In a project that followed
   Seminar 13 it is:

    === "macOS"

        ```text
        python3 run_all.py
        ```

    === "Windows"

        ```text
        python run_all.py
        ```

4. Open the report and compare its numbers and figures with what was just
   built. Write down each number in both versions.

5. Stop after 15 minutes, wherever you are. A rebuild that did not finish
   in 15 minutes is a finding, and the review says where it stopped.

!!! success "You should now see"
    One of two things: the neighbour's numbers rebuilt on your laptop, or a
    note that names the step where the rebuild stopped and the message on
    the screen.

Walk through the room during this section. Do not repair anything. When a
pair wants to talk, remind them: the reviewer writes the question down.

---

### 6. Twelve questions { #questions }

**0:55 · 20 min**

**Tell the room.** This is the checklist of the lecture. Each question is
answered with *yes*, *no* or *could not tell*, and every *no* becomes a
comment.

1. Create a file in the neighbour's project folder named:

    ```text
    review.md
    ```

    Its first line says who reviewed, on which system and when.

2. Answer the twelve questions in order.

    | | Question |
    |--|--|
    | | **Rebuild** |
    | 1 | Does the README say where the data came from? |
    | 2 | Does one command rebuild every number and figure on my laptop? |
    | 3 | Do the rebuilt numbers equal those in the report? |
    | | **Data** |
    | 4 | Is `data/raw` untouched? |
    | 5 | Is every removed or changed row listed, with a reason? |
    | 6 | Are the columns and their units written down? |
    | | **Method** |
    | 7 | Is the question stated, and was it fixed before the result? |
    | 8 | Does every result have an uncertainty, and is its kind named? |
    | 9 | Is there a check that could have failed? |
    | | **Report** |
    | 10 | Do the figures have axis labels with units? |
    | 11 | Does the conclusion claim no more than the numbers support? |
    | 12 | Are sources, data and tools named? |

3. Write the comments below the answers, in the form of
   `review_example.md`: a number, a mark, what was run, what came out.

4. Add one thing that is done well. A review that lists only faults is
   read less carefully.

5. Send `review.md` to the author: commit it and push, or pass the file.

!!! success "You should now see"
    A `review.md` with twelve answers, at least three comments and one thing
    done well, and the author has it.

!!! warning "Watch for"
    | In the review | What to say |
    |--|--|
    | "Looks good" with twelve times *yes* | Ask which command was run for question 2 and which numbers were compared for question 3 |
    | Comments on taste: variable names, colours | Mark them *suggestion*, and keep them few |
    | The reviewer repaired the neighbour's script | A reviewer reports. The author repairs |

---

## Part 3 · The answer { #part-3 }

**1:15 to 1:30 · section 7**

Each student is now the author again, with the review of their own project.

---

### 7. Answer the review { #answer }

**1:15 · 15 min**

**Tell the room.** The author now has a list of comments from someone who
ran the work. Every comment gets an answer in writing. There are two kinds
of answer: changed, with the commit, or not changed, with the reason.

1. Open the `review.md` you received in your own project. If it came by a
   push, fetch it first with **Pull** in the Source Control view.

2. Under each comment write one line that starts with **Answer:**.

    ```text
    2. **Must fix.** README does not say how to create the environment.
       **Answer:** changed. Added the three commands to the README.
    ```

3. Fix one *must fix* comment now. Choose the one that stopped the
   rebuild, if there was one.

4. Commit the fix together with the answered `review.md`, and push.

    ```text
    git add -A
    ```

    ```text
    git commit -m "Answer the review; README says how to rebuild"
    ```

    ```text
    git push
    ```

5. Tell the reviewer in one sentence what was changed, and say thank you.

!!! success "You should now see"
    A commit on the remote repository that holds `review.md` with an answer
    under every comment.

---

## Part 4 · A plan for the data { #part-4 }

**1:30 to 1:55 · section 8**

The project now has a reviewed analysis. The last part writes down what
happens to its data.

---

### 8. Six headings { #dmp }

**1:30 · 25 min**

**Tell the room.** A data management plan says what data a project has and
what happens to it, during the project and after. Funders ask for one. For
a project of this size it is one page, and most of its content is already
in the README. The plan is filled in for the course files on the projector,
and the room types it with you.

1. Create a file in the project folder named:

    ```text
    DMP.md
    ```

    Type the six headings.

    ```text
    # Data management plan

    ## 1 Data
    ## 2 Documentation
    ## 3 Storage and backup
    ## 4 Legal and ethical questions
    ## 5 Sharing and preservation
    ## 6 Responsibilities
    ```

2. Fill in heading 1 with the room. The sizes are measured, not guessed:

    === "macOS"

        ```text
        ls -l data/raw data/processed
        ```

    === "Windows"

        ```text
        Get-ChildItem data/raw, data/processed
        ```

        The sizes in bytes stand in the column `Length`.

    ```text
    ## 1 Data
    - `pendulum.csv`: 9 rows, own measurement, 97 bytes
    - `D0_KPi.csv`: 91 583 rows, 3 926 142 bytes, reused from
      CERN Open Data record 401
    ```

3. Fill in headings 2 to 6 on the projector, one line each, asking the
   room for every answer.

    ```text
    ## 2 Documentation
    README.md: source, DOI, columns, units, every change made.

    ## 3 Storage and backup
    Laptop, private repository on GitHub, external disk (weekly).

    ## 4 Legal and ethical questions
    No personal data. Record 401: CC0. Own measurement: CC BY 4.0.

    ## 5 Sharing and preservation
    At the end: code and pendulum.csv to Zenodo, with a DOI.
    D0_KPi.csv is not uploaded again: the README says how to fetch it.

    ## 6 Responsibilities
    The author. No cost.
    ```

4. For ten minutes each student makes the plan true for their own project:
   heading 3 names the places where their copies really are, heading 6 their
   own name. A student who has a dataset of their own adds it under heading
   1 and answers heading 4 for it first: does it hold data about people, and
   under which licence was it obtained?

5. Swap with the neighbour of Part 2 for two minutes. The neighbour marks
   every line that they could not act on.

6. Commit `DMP.md`.

    ```text
    git add DMP.md
    ```

    ```text
    git commit -m "Add a data management plan"
    ```

!!! success "You should now see"
    A `DMP.md` with six filled headings, committed, on every laptop.

!!! warning "Watch for"
    | In the plan | What to say |
    |--|--|
    | "Backup: GitHub" as the only copy | Data that is kept out of the repository is then on one disk only. Name a second place |
    | "No personal data" for a survey, a list of users or a set of photos | Go back to the table of the lecture: can a person be singled out? If yes, the plan needs a line on who may see the data and when it is deleted |
    | No licence | Open the record the data came from and read it. If there is none, write "licence unknown: not to be passed on" |

---

### 9. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask which of the twelve questions got the most *no*.
In most rooms it is question 2.

- A review starts by running the work on another laptop.
- A comment says what was run and what came out, and is marked *must fix*,
  *suggestion* or *question*.
- A number in a report that the scripts do not produce cannot be reviewed.
- Rows are removed for a reason written down before the result is known.
- The author answers every comment: changed, or not changed and why.
- A data management plan has six headings, and for a small project it is
  one page.

---

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- In how many ways can two of the nine rows be removed, and between which
  values does g then lie? Write a loop over all pairs. The answer is 36
  ways, with g from 9.76 to 9.91.
- Test `fit_g_example.py` on data with a known answer, as in the lecture:
  lengths 20, 40, 60, 80 and 100 cm, and the time of ten swings computed
  from g = 9.81. The answer is `g      9.81`.
- Compute the checksum of the neighbour's copy of `D0_KPi.csv` and compare
  it with the one in their README, as in
  [Seminar 4](seminar_04.md#checksum): `shasum -a 256 data/raw/D0_KPi.csv`
  on macOS, `(Get-FileHash data/raw/D0_KPi.csv).Hash` on Windows. The
  answer is `25c3c972…c1505136` (Windows `25C3C972…C1505136`) if the file
  is unchanged.
- Send the review as an issue on the neighbour's repository on GitHub:
  **Issues** > **New issue**, one issue per *must fix* comment. The author
  closes each issue with the commit that fixes it.
- Fix a second *must fix* comment of the review you received, and push.
- Add a file `DECISIONS.md` to your project with the three most important
  choices of your analysis: the date, the decision, the reason, and what
  the alternative gave.
- Find out how long your institution asks research data to be kept, and
  add it to heading 5 of `DMP.md`.

## If students ask for more

| Topic | Where |
|--|--|
| A template for a longer plan | The funder's own template, or the tools DMPonline and Argos |
| Fixing the plan of an analysis in public before the data is seen | Preregistration, for example on the Open Science Framework |
| Whether a student project needs approval by an ethics committee | The rules of the institution. They differ: ask the supervisor |
| What applies to a student project whose data is about people | The data protection officer of the institution |
| Rules for AI tools in a thesis | The rules of the university and of the journal. They differ: ask before handing in |

## Aims practised

♻️ an analysis rebuilt on a second laptop · 📁 a plan for where the data lives and what happens to it · 🔧 a review that depends on no tool but the project folder
