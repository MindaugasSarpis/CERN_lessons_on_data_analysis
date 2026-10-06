# 16: Machine Learning & AI

Lecture 11 built one neuron, trained it by gradient descent, and ended with a
network of three neurons that computes XOR, its nine numbers set by hand.
Lecture 16 finds such numbers from data. It derives the gradient for a
network with one hidden layer, trains that network, and then asks what every
trained model has to answer: how good it is on rows it has not seen, and how
that is measured. The last part applies both to large language models.

The lecture belongs to the further topics of the course. It is given when
there is time, and it needs Lectures 09 to 11.

## What the lecture covers

1. **From one neuron to a network** — a hidden layer of sigmoid neurons; the
   forward pass in symbols and by hand for one point; why two layers without
   a function in between are one neuron.
2. **Backpropagation** — nine derivatives are needed and three are known;
   the chain rule; four steps from the loss back to the hidden weights, each
   with numbers; the whole pass as eight lines; the check by nudging one
   weight; one step of gradient descent; all points at once in NumPy.
3. **Training on XOR** — the training loop with its seed; the loss and the
   four outputs; what the network found, compared with the hand-set weights;
   30 of 100 seeds fail, and why; what helps.
4. **Train, validation, test** — a two-class file of 600 rows; three sets
   for three jobs; the loop as a function; one line per hidden unit;
   overfitting in a network; the choice by validation and the test, once.
5. **Measuring a classifier** — the confusion matrix; accuracy, precision,
   recall; a rare class; the threshold as a choice; the ROC curve by hand,
   and its area as a count of pairs.
6. **Cross-validation & leakage** — five folds; three forms of leakage; a
   leak in the LHCb file.
7. **Learning without labels** — k-means, run by hand for two iterations on
   six points; why it stops; where it misleads.
8. **scikit-learn** — what was built by hand, packaged; its results checked
   against the hand versions; a default that fails.
9. **Large language models** — softmax; a language model made by hand from
   four sentences; what a large one is; what follows for research: what to
   verify, what to disclose, what not to paste.

## Notation

The output neuron keeps the letters of Lecture 11: weights $w_j$, bias $b$,
weighted sum $z$, output $\hat{y}$. The hidden layer has letters of its own:
weights $v_{ji}$ (to hidden unit $j$ from input $i$), biases $c_j$, weighted
sums $u_j$ and outputs $h_j = \sigma(u_j)$. In code these are `V`, `c`, `w`,
`b`. Lecture 11 wrote `W1`, `b1`, `w2`, `b2` for its hand-set network.

## The lecture in 90 minutes

The lecture is slides 1–66 and estimates about 139 min. Slides 67–73 are the
self-check quizzes and take no lecture time. In a 2-hour slot, skip the
section on k-means or the one on scikit-learn. For a 90-minute slot, skip
the slides in the second table. To jump, type the slide number and press
Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–4 | Where Lecture 11 stopped |
| 0:06 | 5–7 | The hidden layer, the forward pass by hand |
| 0:11 | 9–16, 19 | Backpropagation: the four steps, the whole pass, the loop in NumPy |
| 0:31 | 20–25 | Training on XOR, the seeds that fail |
| 0:44 | 27–33 | The two-class file, three sets, hidden units, overfitting, the test |
| 0:59 | 34–36, 38 | Confusion matrix, precision and recall, the threshold |
| 1:07 | 42, 44–45 | Leakage, and the leak in the LHCb file |
| 1:13 | 56, 58, 60–64 | Language models: by hand, what they are, verify, disclose |
| 1:29 | 66 | Recap |
| 1:31 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Without the Sigmoid, Two Layers Are One | 8 | 3 min |
| The Check: Nudge One Weight; One Step of Gradient Descent | 17–18 | 4 min |
| What Helps | 26 | 2 min |
| When Accuracy Misleads | 37 | 2 min |
| The ROC curve by hand, its area, the ROC of the test rows | 39–41 | 7 min |
| Cross-Validation | 43 | 2 min |
| Learning Without Labels, the whole section | 46–51 | 11 min |
| scikit-learn, the whole section. Seminar 16 does it in its section 8 | 52–55 | 8 min |
| From Two Classes to Many | 57 | 3 min |
| Generating Text. Show its output on slide 60 | 59 | 4 min |
| Keeping the Work Reproducible | 65 | 2 min |

- **Do not cut** slides 12–16 (the four steps and the whole pass), 21–25
  (the training run and the seeds that fail) or 28–33 (the split, the
  network on the file, the test). The seminar types this code and repeats
  these numbers.
- **Slides 7 and 12–18 are one worked example.** The nine weights and the
  point of slide 7 are used on every one of them. Write the weights on the
  board at slide 7 and leave them there.
- **Slide 21** (The Training Loop in NumPy) is run live: the play button at
  the top right of the code. It prints six lines, from a loss of 0.6935 to
  0.0021. Change the seed to 1 and run again to see a run that fails:
  slide 25 takes that run apart.
- **Slide 59** (Generating Text) is run live. It prints the list after `a`
  and five sentences.
- **Slide 33**: before showing the test result, ask the room which row of
  the table it would choose and why the training loss cannot make the
  choice.
- **Slide 45** needs the file of the course, `D0_KPi.csv`. The run takes
  about a minute and is not done live.

## Where the numbers come from

Every number on the slides is printed by one script, and the figures are
drawn by the same file:

```text
python figures/src/ml.py                    all numbers of the lecture
python figures/src/build.py --only ml       the figures viz_ml_*.svg
```

The script needs NumPy, and scikit-learn for the checks of slides 54 and 55
(version 1.7.2 was used). The two-class file is
[`ml_two_class.csv`](../data/ml_two_class.csv): 600 rows, made by
[`ml_two_class.py`](../data/ml_two_class.py) with seed 16. The split of the
lecture uses seed 0, and so do the starting weights of every network unless
a slide names another seed.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 67–73: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. A network has 3 inputs, one hidden layer of 5 units and 1 output unit.
   How many parameters does it have?
   *26. The hidden layer has 5 · 3 weights and 5 biases, the output unit 5
   weights and 1 bias.*
2. The error at the output is δ = 0.2. A hidden unit has the output weight
   w = −3 and the value h = 0.9. What is its error?
   *δ · w · h · (1 − h) = 0.2 · (−3) · 0.9 · 0.1 = −0.054.*
3. A classifier gives TP = 30, FP = 10, FN = 20, TN = 140. What are its
   precision and recall?
   *Precision 30/40 = 0.75, recall 30/50 = 0.60. The accuracy is 0.85.*
4. Three rows of class 1 score 0.8, 0.5 and 0.3. Two rows of class 0 score
   0.6 and 0.2. What is the area under the ROC curve?
   *4 of the 6 pairs are in order: 0.67.*
5. A network with 400 hidden units is right for 100 % of its 500 training
   rows and for 71 % of 500 unseen rows. What is the reading?
   *Overfitting. Use fewer hidden units or stop earlier, and choose with
   validation rows. A leak would raise the result on the unseen rows too.*
6. A language model gives a reference with authors, journal, year and pages
   for a statement in your report. What is established?
   *Nothing yet. The reference has to be found and read: a likely
   continuation of a request for a reference is a line that looks like
   one.*

## Paired seminar

[Seminar 16 — A Small Network, Measured](../seminars/seminar_16.md) is a
follow-along session on the two-class file. The room loads and plots it,
splits it with a seed, trains the neuron of Lecture 11 and then the network
of this lecture as two functions, chooses the number of hidden units with
the validation rows, uses the test rows once, counts the confusion matrix by
hand, checks it with scikit-learn, and writes the result into the README.

## Further reading

- D. Rumelhart, G. Hinton, R. Williams, *Learning representations by
  back-propagating errors*, Nature 323, 533–536 (1986). Four pages: the
  derivation of this lecture for any number of layers.
- M. Nielsen, *Neural Networks and Deep Learning* (2015), free at
  neuralnetworksanddeeplearning.com. Chapter 2 derives backpropagation step
  by step.
- G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor, *An Introduction
  to Statistical Learning with Applications in Python* (2023), free at
  statlearning.com. Validation, cross-validation, classification.
- The user guide of scikit-learn, at scikit-learn.org.

## Slides that left the deck

The deck before this rework is in the history of the repository
(`git show cc65310:lectures/content/slides/16_Machine_Learning_and_AI.md`).
Its perceptron and first classifier are now Lecture 11. Not kept: the
regression section, which repeated Lecture 10; the slides on features from
momentum columns, which the data file does not have; the random forest; the
slides on the trigger, flavour tagging, model cards and bias.

## Take-aways

- A network with one hidden layer is the neuron of Lecture 11 fed by other
  neurons. Without a function between the layers it collapses into one
  neuron.
- Backpropagation is the chain rule, applied from the loss backwards. The
  error of a hidden unit is $\delta_j = \delta\,w_j\,h_j(1 - h_j)$, and the
  derivative for a weight is the error of its unit times its input.
- One forward and one backward pass give all derivatives. Nudging a weight
  gives one, and is the test of the code.
- Training starts from random weights and can end in a flat region. State
  the seed, run several, and expect some to fail.
- Training rows fit the weights, validation rows choose the model, test rows
  are used once. A number taken from the data comes from the training rows.
- The training loss always prefers the larger model. Overfitting shows as a
  validation loss that rises while the training loss falls.
- An accuracy hides the kind of error. Precision is TP / (TP + FP), recall
  is TP / (TP + FN), and the cut between them is a choice.
- The area under the ROC curve is the share of pairs, one row of each class,
  that the scores put in the right order.
- A result that is much better than expected is checked for a leak before it
  is believed.
- k-means returns $k$ groups whether the data have groups or not, and its
  result depends on the start.
- A packaged function is compared with the hand version the first time it
  is used. A default setting is a choice someone else made.
- A language model writes a likely continuation of a text. Nothing in it
  compares the output with a source: references, numbers and code are
  checked by the person who uses them, and the use is disclosed.
