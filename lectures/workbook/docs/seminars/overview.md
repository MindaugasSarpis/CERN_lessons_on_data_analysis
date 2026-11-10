# The Seminars — How They Work

Every lecture from week 2 on is paired with a **hands-on seminar**. Week 1 is
lecture only. A page carries the number of its lecture, except Seminar 1,
which pairs with Lecture 2; there is no Seminar 2. Each seminar takes about
two hours (Seminar 5, the first Python, runs longer), all of it in class: there is no homework, and no session depends on
work done at home. The seminars practise the course's four aims:
🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data & files.

## One theme, one question per week

The lectures follow one project, a weather station with ten years of
hourly readings in `data/raw/weather.csv`. The seminars ask one question
per week about real weather and climate data that anyone can fetch: the
daily record of the Vilnius station since 1881, the weather of Vilnius
from a weather model, CO₂ at Mauna Loa, the temperature of the Earth.
Each question is answered by the end of the session.

- **Every seminar stands on its own.** It starts in a new, empty folder
  and hands out no file: the data is typed from the page or fetched by the
  code itself from an openly available data set at its public address
  (the real weather of Vilnius from the Open-Meteo archive, NOAA's Mauna
  Loa CO₂ table, and others, each with its source and licence). Missing a
  week costs nothing; nothing has to be carried over from an earlier
  session.
- **Seminar 5** is the first Python of the room and its first conda
  environment: the interpreter, a script in VS Code, a list and a loop over
  six typed hours; then scripts on Open-Meteo's forecast and NOAA's station
  files.
- **Seminar 6** is Git: the lecturer reads the history of a public data
  repository, `datasets/global-temp`; the room clones
  [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project)
  (about 0.5 MB), finds who changed its mean, takes the change back and
  publishes it to their own GitHub. Seminar 12's optional section uses Git
  again; the other seminars do not need it.
- **Weeks 8 to 12 share one conda environment, `analysis`.** Seminar 8
  creates it with one `conda create` line and adds pandas and Matplotlib;
  each later seminar adds the package of the week (`conda install`, then
  the file is written again). Whoever missed a week creates it with the
  line on that week's page.
- **One new tool per seminar from week 8:** pandas (8), NumPy (9), a class
  of your own (10), a language model in plain Python and an LLM (11),
  pytest (12). The lecture of the week gives the idea; the seminar shows
  the tool at work and then gives the room a problem to solve with it.
- **Your project:** from week 8, the problem of each seminar can be asked
  of your own file instead.
- **The terminal:** zsh on macOS and Git Bash on Windows, in the terminal
  of VS Code. They take the same commands, so a line typed on the projector
  is the line typed on every laptop.

## How a page works

A seminar has four parts. **Set up** makes the day's folder and, when
needed, the conda environment. In the **Showcase** the lecturer runs three
to five complete examples from the page, each on real data, with what to
notice and a question for the room; a table of the calls they used closes
it. Then **the problem**: one real question, worked on in pairs with any
tools, an LLM included. First a prediction, then the work, then checks that
no LLM can do for you (a number by hand, the units and the uncertainty read
off the result, the answer set against the prediction), and last one
figure or number with two sentences. Hints and a worked solution are
folded under it. In **Show and discuss** two or three pairs show their
answer. The **▶ Steps** button (bottom right) shows the page one step at a
time.

## The project folder

```text
weather-sNN/
|- README.md            # what this is, where the data came from, how to rebuild
|- environment.yml      # the conda environment (Seminar 5 on)
|- data/
|  |- raw/              # files exactly as received, never edited
|  |- processed/        # made from data/raw by commands and scripts
|- scripts/             # one script per step
|  |- rebuild.sh        # one command rebuilds everything
|  |- test_*.py         # checks of the results (pytest, Seminar 12)
|- results/             # numbers and figures the scripts produce
```

The same layout is a sound default for your own project.

**The golden rule:** you could delete `data/processed/` and `results/` and
rebuild both with one command.

## Seminars and your project

| | **The seminars** | **Your project** |
|--|--|--|
| What | One hands-on session per week on the weather project | One project of your own, developed across the semester |
| Topic | Set by the page | **Entirely your choice**: field, data, and form (analysis, app, dashboard, educational piece) |
| Continuity | Each seminar starts from an empty folder; its data is typed or fetched from a public address | Grows all term; the seminar skills are meant to be carried into it |
| Assessed | No | Yes: repository, one-page report, short video, final presentation (see Lecture 1) |

How much the two overlap is up to you: a seminar step can be repeated on
your own data, or your project can go somewhere else entirely.
