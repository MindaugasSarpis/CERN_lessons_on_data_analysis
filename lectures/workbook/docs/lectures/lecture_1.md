# 1: Orientation & Motivation

Lecture 1 opens on a small table from a lab partner: nine lengths of a
pendulum and the time of ten swings at each. Ada works out *g* row by row and
averages: 9.80 m/s². Ben draws one line through all nine rows: 9.84 m/s².
Neither made a mistake. The question of the lecture is: *I send you only
9.84. How do you check it?* The answers the room gives sort into four piles,
and the four piles are the four aims of the course. The lecture closes on
that answer, then runs the film reel from the cosmos down to the LHCb
detector.

## What the lecture covers

1. **Introductions**: a Google Earth pull-back from the Physics Faculty to the
   cosmos as the cold open, then a show of hands: your field, your operating
   system, whether you have written code before.
2. **The question**: the pendulum table as it arrived (130 bytes, `;` between
   the fields, decimal commas, a numbering column and a mean line); two honest
   answers from the same nine rows, 9.80 and 9.84; and seven values of *g*
   from seven choices about the same file, from 9.79 to 9.88 when one row is
   left out, and 983.61 or 0.098 after a slip.
3. **The four aims as the answer**: 🔧 tool-agnosticism, ♻️ reproducibility,
   ⚙️ automation, 📁 efficient work with data & files. Each comes with a
   before/after pair counted on the pendulum file: about 5 000 bytes of `.xlsx`
   against 97 bytes of CSV; a screenshot of 9.84 against the folder that made
   it; four edits by hand (one line, 9 commas, 20 semicolons, one column)
   against one script, and what the wrong order of two replacements does; a
   Desktop of copies against `data/raw` (130 bytes) and `data/processed`
   (97 bytes).
4. **How this course works**: the lecture and the seminar of each Tuesday, the
   schedule, the learning outcomes, what "done" means each week, habits that
   work.
5. **Seminars & your project**: the grade is one project of your own, graded
   on the four aims; what you hand in; why real, open data; the pendulum table
   block by block through the course; the finished project tree (the one
   Lecture 13 builds); delete `data/processed/` and `results/` and rebuild them
   with one command.
6. **The answer**: why CERN needs the same skills; Mariner 4's first picture of
   Mars, coloured by hand from 40 000 printed numbers and a key; and *What a
   Result Needs*, one line per aim, which answers the opening question.
7. **The reel**: from the cosmos to the quantum and into CERN, ending on the
   LHCb fly-through. Four slides on CERN (the organisation, the LHC, the
   accelerator chain, how a detector sees a collision) follow the closing
   film as extra material and are not delivered.

## The lecture in 90 minutes

The deck is slides 1–57 and estimates about 112 min, of which slides 53–57
(extra material after the closing film) are not delivered. Slides 58–62 are
the self-check quizzes and take no lecture time. The films run about 32 min
(slides 33–52) plus 4:42 for the cold open. To jump, type the slide number and
press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–3 | Cover, cold open film, show of hands |
| 0:08 | 4–7 | The pendulum table; Ada's 9.80 and Ben's 9.84; seven numbers from one file |
| 0:18 | 8–14 | The four aims as the answer; the before/after pairs |
| 0:31 | 15–20 | How this course works |
| 0:39 | 21–27 | Seminars and your project, the project tree, delete and rebuild |
| 0:49 | 28–31 | Why CERN, Mariner 4, **What a Result Needs**, what to bring |
| 0:56 | 32–52 | The reel, ending on the LHCb fly-through |
| 1:30 | | End |

| Skip | Slides | Saves |
|--|--|--|
| The Aims Reinforce Each Other | 14 | 2 min |
| Learning Outcomes | 18 | 2 min |
| Habits That Work | 20 | 2 min |
| Why Real, Open Data | 24 | 2 min |
| Why You Need These Skills | 28 | 2 min |

- **The hook is answered twice**: first at slide 8 (the four aims, about
  0:18), and in full at slide 30, *What a Result Needs* (about 0:53).
- **Do not cut** slides 5–8 (the question and the four aims) or slide 30
  (*What a Result Needs*, which answers the question). If time runs short, cut
  from the skip list in the middle, never the closing slide.
- **Slide 6** (Two People, Two Answers): give the room two or three minutes
  and write their answers on the board; slide 8 sorts them into the four aims.
  No formula is needed. For questions: *g* = 4π²*L*/*T*², with *T* the time of
  one swing; Ben's line is *T*² against *L*, slope 4.014 s²/m.
- **Slide 12** (The Same Edits in the Wrong Order): ask which replacement
  comes first before showing the two columns.
- All numbers on slides 5–13 and 30 were computed from
  [`pendulum_raw.csv`](../data/pendulum_raw.csv) and
  [`pendulum.csv`](../data/pendulum.csv); the `.xlsx` size was measured by
  writing the table with Python's `openpyxl` 3.1.5 (4 993 to 5 007 bytes,
  depending on the install).

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 58–62: four quiz slides for students to try afterwards. The same
questions, with their answers:

1. You catch yourself repeating the same manual steps on your data every week.
   Writing a script to do it instead chiefly serves which of the four aims?
   *⚙️ Automation: do it once by hand, twice by script. It helps
   reproducibility too, but the direct target is automation.*
2. A colleague sends you a PDF of the final plot. What is the minimum you
   would need for the result to count as reproducible?
   *The raw data, the code, and a note of the environment it ran in. A
   sharper picture or a promise changes nothing.*
3. It's week 5. You attend every lecture but skip the seminars because you
   "get the ideas already". Why is this the riskiest habit in this course?
   *The seminars are where an idea becomes a working skill, and the project is
   graded on skills.*
4. In a reproducible project, two folders can be deleted at any time and
   rebuilt with one command. Which two?
   *`data/processed/` and `results/`: they hold only what the scripts write.
   `data/raw/` cannot be regenerated, and the scripts with `run_all.py`,
   `config.json`, `requirements.txt` and the README are the recipe.*

## Before the first seminar

Nothing has to be installed. The first session in class, on 29 September,
starts from zero and needs only VS Code, which the room installs together.
Python and Git, and PowerShell 7 on Windows, are installed in class, at the
start of Seminar 4. A laptop on which programs can be installed is all that is
needed: on a university or work laptop, check that now.

## Paired seminar

None: week 1 is lecture only. The first session in class is
[Seminar 1](../seminars/seminar_01.md), in week 2. Python and Git are
installed in class at the start of [Seminar 4](../seminars/seminar_04.md),
with the steps of [Install Python, Git and PowerShell 7](../seminars/install_python_git.md).

## Take-aways

- A number on its own cannot be checked: the same nine rows give 9.80, 9.81
  or 9.84 by method, and 9.79 to 9.88 when one row is left out.
- To check a result you need the file as received, every step as code, the
  versions it ran on, and formats anyone can open: the four aims.
- Once by hand, twice by script. Two replacements in the wrong order ruin the
  table; a script keeps the order.
- Delete `data/processed/` and `results/`, run one command, and the same
  97 bytes and the same 9.84 come back.
- The whole grade is one project of your own; the seminars teach the moves,
  the project is where you make them yours.
