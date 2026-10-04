# 14: Concepts of Data Analysis

Lecture 13 closed the core of the course with a project that rebuilds itself
by one command. Lecture 14 is a further topic, given when there is time. It
uses no new tool. It looks back at two results the room has produced, g from
the pendulum table and the mass peak in the LHCb file, and asks what makes
such a number a result, how an honest analysis still goes wrong, and what
stands around an analysis: review, authorship, a plan for the data, personal
data and AI tools.

## What the lecture covers

1. **What an analysis is** — a question, evidence with its uncertainty, a
   decision. The same value of g with three uncertainties gives three
   verdicts. Comparing two numbers in units of σ. Statistical and
   systematic uncertainty: the mass peak lies 3.4σ below the world average
   in statistical uncertainty only, and that is no discovery. Four kinds of
   question: describe, explain, predict, decide.
2. **From question to decision** — a loop of seven steps, each taken for
   the pendulum and for the LHCb file: question, plan, data, model, result,
   checks, decision. The plan is written before the data is looked at.
3. **How analyses go wrong** — three ways that need no bug. Many looks:
   1 − 0.95ᵏ, twenty groups drawn by lot, stopping when it looks good, the
   750 GeV excess of 2015. Choosing the data after the result: the 36 ways
   of dropping two rows, 120 selections of rows. Reading a correlation as
   a cause: two columns of the LHCb file, a table that reverses, and what
   an experiment adds. The defence: decide before you look.
4. **Working with others** — what an author cannot see, the path of a
   result through an LHC collaboration, review and independent repetition,
   a checklist of twelve questions, a report with its review, a decision
   log.
5. **Research integrity** — the four principles of the European code,
   fabrication, falsification and plagiarism, what to do when a mistake is
   found, who is an author.
6. **The data management plan** — what it is, who asks for one, six
   headings, a plan on one page for the project folder of the course.
7. **Ethics and personal data** — what counts as personal data, why
   removing names is not enough, what the GDPR asks of a researcher, and
   four questions the law does not ask.
8. **AI tools in an analysis** — what the tool is, where it helps along
   the loop, verifying code with a known answer, verifying references and
   numbers, what never to paste, what to disclose.

## The two results the lecture uses

Both are the fits of Lecture 10, with the same choices.

| | Pendulum | LHCb file |
|--|--|--|
| Data | `pendulum.csv`, nine rows | `D0_KPi.csv`, 91 583 rows, 84 680 in the fit window |
| Model | T² = (4π²/g)·ℓ + b, with 0.1 s on each time of ten swings | A Gaussian on a straight line, 1820 to 1910 MeV/c², bins of 2 MeV/c² |
| Result | g = 9.84 ± 0.09 m/s² | peak at 1864.47 ± 0.10 MeV/c², width 7.65 ± 0.10 MeV/c² |
| Compared with | 9.81 m/s²: 0.4σ | 1864.84 ± 0.05 MeV/c² (Particle Data Group): 3.4σ |

Every other number on the slides is computed from these two files or from
a simulation with seed 14. `python figures/src/concepts.py --numbers`
prints them; `python figures/src/build.py --only concepts` redraws the ten
figures.

## The lecture in 90 minutes

The lecture is slides 1–65 and estimates about 126 min. Slides 66–72 are
the self-check quizzes and take no lecture time. In a 2-hour slot nothing
is skipped. For a 90-minute slot, skip the slides in the second table. To
jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–10 | What an analysis is: three parts, the uncertainty decides, statistical and systematic |
| 0:16 | 12–17, 19–20 | The loop, step by step, on the pendulum and the LHCb file |
| 0:32 | 21–25, 28–29, 31–32 | How analyses go wrong: many looks, selection after the result, correlation and cause |
| 0:50 | 33–35, 37–38 | Review: what the author cannot see, the checklist, a report reviewed |
| 1:00 | 41–43, 45 | Integrity, misconduct, who is an author |
| 1:06 | 47–49 | The data management plan |
| 1:12 | 52–55 | Personal data and the GDPR |
| 1:19 | 57, 60–63 | AI tools: verify, never paste, disclose |
| 1:29 | 65 | Recap |
| 1:31 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Four Kinds of Question | 11 | 2 min |
| 5 · The Result | 18 | 2 min |
| A Bump at 750 GeV, Dropping Two Rows | 26–27 | 4 min |
| Two Columns That Move Together | 30 | 2 min |
| Review and Repetition | 36 | 2 min |
| Writing a Review, A Decision Log | 39–40 | 4 min |
| When a Mistake Is Found | 44 | 2 min |
| Authorship: Roles and Problems | 46 | 2 min |
| A Plan on One Page, After the Project | 50–51 | 4 min |
| Beyond the Law | 56 | 2 min |
| What the Tool Is, Along the Loop | 58–59 | 4 min |
| Sources | 64 | 2 min |

- **Do not cut** slides 7–10. The step from "3.4σ" to "no discovery" is the
  centre of the first section, and the later sections return to it.
- **Do not cut** slides 23–25 and 28–29: one derivation, two demonstrations
  on the course files, and the defence.
- **Do not cut** slides 37–38 (the checklist and the reviewed report) and
  slide 49 (the six headings). The seminar uses both.
- **Slide 8** ends on a question: has this course found that the D⁰ mass is
  wrong? Let the room answer before slide 9.
- **Slide 23** is derived on the board: 0.95 for one quiet look, 0.95ᵏ for
  k of them.
- **Slide 31** (the table that reverses): let the room check one row of
  percentages by hand, then ask which treatment they would choose.
- **Slide 60** can be run live: the code prints `9.81`, `981.0` and
  `0.09809999999999999`.

## Rules that differ

The slides state what holds generally and say where rules differ. Before
the lecture, look up the local version of four of them and say it aloud:

- the code of academic ethics of the university (slide 42);
- whether doctoral students have to hand in a data management plan, and
  how long research data has to be kept (slides 48 and 51);
- who the data protection officer is, and when a student project needs the
  approval of an ethics committee (slides 55 and 56);
- what the university and this course allow for AI tools in graded work
  (slide 63).

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 66–72: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. An analyst tests 14 columns of pure noise and calls any result beyond
   2σ a finding. How likely is at least one finding?
   *About 51 %: 1 − 0.95¹⁴. All 14 stay quiet with probability 0.49.*
2. A group reports g = 9.90 ± 0.04 m/s². The reference is 9.81 m/s². What
   is the right reading?
   *2.25σ: no claim yet. A distance like this happens by chance about once
   in 40 cases, and a systematic effect is far more likely than a new
   value of g.*
3. Method A succeeds in 60 of 150 hard cases and 45 of 50 easy ones.
   Method B succeeds in 15 of 50 hard cases and 120 of 150 easy ones.
   Which statement holds?
   *A is better in hard cases (40 % against 30 %) and in easy ones (90 %
   against 80 %). B leads overall, 67.5 % against 52.5 %, because it got
   more easy cases.*
4. Who meets the conditions for authorship of a report on the pendulum
   measurement: the colleague who lent the stopwatch, the head of the
   department who has not read it, the student who took the data, revised
   the text, approved it and answers for it, or the language model that
   drafted the script?
   *The student. Authorship needs a contribution, work on the text,
   approval and accountability, all four.*
5. A table holds student number, year of birth and exam grade, without
   names. What is it under the GDPR?
   *Personal data. The university can link a student number to a person:
   the table is pseudonymised, not anonymous.*
6. Which of these can go into a public AI chat tool: a traceback from your
   own script on the public LHCb file, a table of grades with student
   numbers, a manuscript you were sent to referee, a script with your
   access token?
   *The traceback. The others are personal data, confidential work of
   someone else, and a secret.*

## Paired seminar

[Seminar 14 — Review an Analysis, Plan the Data](../seminars/seminar_14.md)
has four parts. The room first reviews a short report whose script does not
give the number in the report. Then each student rebuilds a neighbour's
project on their own laptop and reviews it with the twelve questions of
slide 37. The author answers every comment and fixes one. Last, each
student writes a data management plan of one page for their own dataset.

## Sources

- R. Feynman, *Cargo Cult Science*, Caltech commencement address, 1974.
- ISIS-2 Collaborative Group, *Lancet* 332 (1988) 349: the subgroups by
  star sign.
- C. R. Charig et al., *BMJ* 292 (1986) 879: the kidney-stone table.
- ATLAS Collaboration, *JHEP* 09 (2016) 001: the excess near 750 GeV,
  local and global significance.
- OPERA Collaboration, *JHEP* (2012): the neutrino velocity, final result.
- G. Miller, *Science* 314 (2006) 1856: the five retractions.
- L. Sweeney, *Simple Demographics Often Identify People Uniquely*, 2000.
  A. Narayanan and V. Shmatikov, *Robust De-anonymization of Large Sparse
  Datasets*, 2008.
- T. Vines et al., *Current Biology* 24 (2014) 94: data availability
  against the age of the article.
- ALLEA, *The European Code of Conduct for Research Integrity*, revised
  edition 2023.
- ICMJE, *Recommendations for the Conduct, Reporting, Editing, and
  Publication of Scholarly Work in Medical Journals*: authorship, AI
  tools.
- Science Europe, *Practical Guide to the International Alignment of
  Research Data Management*, 2021.
- Regulation (EU) 2016/679, the General Data Protection Regulation.
- European Commission, *Living guidelines on the responsible use of
  generative AI in research*, 2024.

## Take-aways

- An analysis is a question, evidence with its uncertainty, and a
  decision. A number without an uncertainty cannot be compared with
  anything.
- Two numbers are compared in units of σ, with both uncertainties. Beyond
  2σ happens by chance once in 22 cases, beyond 3σ once in 370.
- Statistical uncertainty falls as 1/√N. Systematic uncertainty does not.
  A result is value ± statistical ± systematic.
- The plan comes before the data, and the checks before the decision.
- With k looks at noise, the chance of at least one result beyond 2σ is
  1 − 0.95ᵏ: 64 % for twenty looks.
- Rows, thresholds and the number of measurements are fixed before the
  result is known, and written down with the date.
- A correlation is read as a cause only after chance, a common cause and
  selection are ruled out. An experiment sets the cause by hand.
- A review starts by rebuilding the work on another laptop. A comment says
  what was run and what came out.
- Fabrication, falsification and plagiarism are misconduct. An honest
  mistake is not. Hiding one is.
- An author has contributed, worked on the text, approved it and answers
  for it. A tool cannot be an author.
- A data management plan has six headings. For a small project it is one
  page.
- Data that can be linked to a person is personal data, with or without
  names. Ask the data protection officer before collecting it.
- Whatever an AI tool drafted is checked before it enters the report, and
  its use is stated. Personal data, other people's unpublished work and
  secrets are never pasted into it.
