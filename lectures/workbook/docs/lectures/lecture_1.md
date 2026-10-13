# 1: Orientation & Motivation

Lecture 1 opens on one file: ten years of hourly readings from a weather
station, 87 672 rows, with five days in July 2019 when the sensor was down
and the logger wrote `-999`. Smiltė averages every hour and reports a mean of 7.16 °C.
Ben takes the middle of each day and averages the days: 7.11 °C. Neither made
a mistake. The question of the lecture is: *I send you only 7.16. How do you
check it?* The answers the room gives sort into four piles, and the four piles
are the four aims of the course. The lecture answers the question again at the
end, then runs the film reel from the cosmos down to the LHCb detector.

## What the lecture covers

1. **Introductions**: a Google Earth pull-back from the Physics Faculty to the
   cosmos as the cold open, then a show of hands: your field, your operating
   system, whether you have written code before.
2. **The question**: the weather log as it arrived; two honest answers from
   the same file, 7.16 °C and 7.11 °C; and seven numbers from seven choices
   about it, from 7.03 to 7.29 when one year is left out, and 5.78 or 79.10
   after a slip.
3. **The four aims as the answer**: 🔧 tool-agnosticism, ♻️ reproducibility,
   ⚙️ automation, 📁 efficient work with data & files. Each comes with a
   before and after pair: a spreadsheet of the log against the CSV; a
   screenshot of 7.16 against the folder that made it; four edits by hand to
   the station's spreadsheet export against one script, and what the wrong
   order of two replacements does; a Desktop of copies against `data/raw`
   (180 bytes) and `data/processed` (148 bytes).
4. **How this course works**: the lecture and the seminar of each Tuesday, the
   schedule, the path of the course (VS Code and Markdown, files, the command
   line in zsh on macOS and Git Bash on Windows, with package managers and
   conda environments, Git, Python, then data analysis), the learning
   outcomes, what "done" means each week, habits that work.
5. **Seminars & your project**: the grade is one project of your own, graded
   on the four aims; what you hand in; open data and practice files; the
   finished project tree; delete `data/processed/` and `results/` and rebuild
   them with one command.
6. **How do you check 7.16?**: why CERN needs the same skills; Mariner 4's first picture
   of Mars, coloured by hand from 40 000 printed numbers and a key; and
   *What a Result Needs*, one line per aim, which answers the opening
   question.
7. **The reel**: from the cosmos to the quantum and into CERN, ending on the
   LHCb fly-through. Four slides on CERN (the organisation, the LHC, the
   accelerator chain, how a detector sees a collision) follow the closing
   film as extra material and are not delivered.

## The lecture in 90 minutes

The deck is slides 1–59 and estimates about 109 min, of which slides 55–59
(extra material after the closing film) are not delivered. Slides 60–65 are
the self-check quizzes and take no lecture time. The films run about 32 min
(slides 35–54) plus 4:42 for the cold open. To jump, type the slide number and
press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | Cover, cold open film, show of hands, the goal |
| 0:09 | 5–7 | The weather log; Smiltė's 7.16 and Ben's 7.11; seven numbers from one file |
| 0:19 | 8–14 | The four aims as the answer; one before and after pair per aim |
| 0:32 | 15–22 | How this course works |
| 0:41 | 23–28 | Seminars and your project, the project tree, delete and rebuild |
| 0:49 | 29–33 | How do you check 7.16? Why CERN, Mariner 4, **What a Result Needs**, what to bring |
| 0:56 | 34–54 | The reel, ending on the LHCb fly-through |
| 1:30 | | End |

| Skip | Slides | Saves |
|--|--|--|
| The Aims Reinforce Each Other | 14 | 2 min |
| Learning Outcomes | 19 | 1 min |
| Habits for This Course, What to Expect | 21–22 | 3 min |
| Open Data | 26 | 2 min |
| Why You Need These Skills | 30 | 2 min |

- **The notes are short on purpose.** Each slide's speaker note says what to
  **Do**, **Say** or **Ask**, and what to answer **If asked**, with the
  minutes it takes.
- **The hook is answered twice**: first at slide 8 (the four aims, about
  0:19), and in full at slide 32, *What a Result Needs* (about 0:53).
- **Do not cut** slides 5–8 (the question and the four aims) or slide 32
  (*What a Result Needs*, which answers it). If time runs short, cut from the
  skip list, never the closing slide.
- **Slide 6** (The Mean Temperature, Computed Two Ways): give the room two or three minutes
  and write their answers on the board; slide 8 sorts them into the four aims.
- **Slide 12** (The Same Edits in the Wrong Order): ask which replacement
  comes first before showing the two columns.
- All numbers on slides 5–13 and 32 were computed from
  [`weather.csv`](../data/weather.csv) and
  [`weather_daily_export.csv`](../data/weather_daily_export.csv). The
  `.xlsx` size was measured by writing the log with Python's `openpyxl` 3.1.5.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 60–65: five quiz slides for students to try afterwards. The same
questions, with their answers:

1. From the same file of hourly readings, Smiltė reports a mean of 7.16 °C and
   Ben 7.11 °C. What tells you which method a number came from?
   *The code that computed it, run on the file as it was received. A
   screenshot shows the number, not the choices behind it.*
2. You catch yourself repeating the same manual steps on your data every week.
   Writing a script to do it instead chiefly serves which of the four aims?
   *⚙️ Automation: do it once by hand, twice by script. It helps
   reproducibility too, but the direct target is automation.*
3. A colleague sends you a PDF of the final plot. What is the minimum you
   would need for the result to count as reproducible?
   *The raw data, the code, and a note of the environment it ran in, such as
   an `environment.yml`. A sharper picture or a promise changes nothing.*
4. It's week 5. You attend every lecture but skip the seminars because you
   "get the ideas already". Why is this the riskiest habit in this course?
   *The seminars are where an idea becomes a working skill, and the project is
   graded on skills.*
5. In a reproducible project, two folders can be deleted at any time and
   rebuilt with one command. Which two?
   *`data/processed/` and `results/`: they hold only what the scripts write.
   `data/raw/` cannot be made again, and the scripts with `run_all.py`,
   `config.json`, `environment.yml` and the README are the recipe.*

## Before the first seminar

Nothing has to be installed. The first session in class starts from zero and
needs only VS Code, which the room installs together. Git (with Git Bash on
Windows) and Python with conda through Miniforge are installed in class, at
the start of the seminar that first needs them. A laptop on which programs
can be installed is all that is needed: on a university or work laptop,
check that now.

## Paired seminar

None: week 1 is lecture only. The first session in class is
[Seminar 1](../seminars/seminar_01.md), in week 2.

## Take-aways

- A number on its own cannot be checked: the same file gives 7.16 or 7.11 by
  method, 7.03 to 7.29 when one year is left out, and 5.78 when the marks
  for a missing value are read as temperatures.
- To check a result you need the file as received, every step as code, the
  versions it ran on (an `environment.yml`), and formats anyone can open: the
  four aims.
- Once by hand, twice by script. Two replacements in the wrong order ruin the
  table; a script keeps the order.
- Delete `data/processed/` and `results/`, run one command, and the same
  files and the same numbers come back.
- The whole grade is one project of your own; the seminars teach the moves,
  the project is where you make them yours.
