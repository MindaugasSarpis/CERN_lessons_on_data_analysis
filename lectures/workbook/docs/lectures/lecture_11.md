# 11: The Perceptron

Lecture 10 fitted a number: it wrote the likelihood of the data, took its
logarithm times −2, got χ² plus a constant, and minimised it in closed form or by gradient
descent. Lecture 11 applies the same three steps to a label that is 0 or 1.
The model is one artificial neuron. The lecture builds it completely: what
it computes, two ways to train it, where its loss comes from, and the one
problem it cannot solve.

## What the lecture covers

1. **From a number to a class** — the data of the lecture, 200 generated
   points with two inputs and a label; a threshold on one input is right for
   177 of them, a line for 185, and the question of the lecture is how that
   line was found; a fit and a classification side by side as the plan.
2. **One neuron** — the weighted sum, the bias and the step; AND, OR and NOT
   with weights set by hand, and XOR left open as a puzzle; the decision
   boundary *z* = 0 is a line; the
   weight vector is its normal; the distance of a point from it is
   *z* / ‖**w**‖; what turning **w**, changing *b* and scaling both do.
3. **Rosenblatt's learning rule** — the rule and why it moves *z* the right
   way; the AND gate worked through in 24 steps and 10 updates; the same in
   Python; linearly separable sets and the margin; the perceptron convergence
   theorem with its four assumptions and the bound *R*²/γ²; the idea of the
   proof in three slides; what the theorem does not say.
4. **From the step to the sigmoid** — counting errors has no slope; the
   sigmoid and its derivative σ(1 − σ), derived; the output as a probability
   and *z* as the logarithm of the odds; the sigmoid as the exact answer for
   two Gaussian classes.
5. **The loss: from likelihood to cross-entropy** — the Bernoulli likelihood
   of one point and of all points; its negative logarithm is the
   cross-entropy; the loss of four points by hand; the gradient by the chain
   rule in three parts, (ŷ − *y*) **x**; the gradient checked against a
   difference quotient in Python; the update rule beside Rosenblatt's and the
   straight-line fit, which answers why his rule has the form it has; one
   minimum.
6. **Training in NumPy** — the loop read line by line against the formulas;
   the loop run on the 200 points, which finds the line of 185 from the
   opening; the boundary moving; the weights against the exact ones of the
   generator.
7. **Training in practice** — the learning rate; inputs on different scales
   and standardising; a training and a test set; the uncertainty of an
   accuracy.
8. **The limit: XOR** — the puzzle of the gates slide settled: four
   inequalities that no weights satisfy; two lines
   and a third neuron; the 2-2-1 network verified for all four inputs; the
   hidden layer as a change of coordinates; what is missing.
9. **History in three dates** — 1958, 1969, 1986, each with its source, and
   what the press expected of the 1958 machine; what a modern network keeps
   of this unit.

## The numbers of the lecture

Every number on the slides was computed. The ones the room meets again in
the seminar:

| Where | Result |
|--|--|
| AND by Rosenblatt's rule, from zero weights, η = 1, points in the order (0,0), (0,1), (1,0), (1,1) | 10 updates in 5 epochs, then **w** = (2, 1), *b* = −2. The bound of the theorem is 51 |
| The same rule on the 200 overlapping points | 16 to 24 updates in every epoch, for 100 epochs |
| The logistic neuron on the 200 points, η = 0.5, 1000 epochs | loss from 0.6931 to 0.1616, 185 of 200 correct (92.5 %), **w** = (2.10, 2.26), *b* = −4.31 |
| The best possible rule for these data | **w** = (2, 2), *b* = −4, right for 92.1 % of new points on average |
| 150 training and 50 test points | 93.3 % and 92.0 %; the test accuracy is 92 % ± 4 % |
| XOR by three step neurons | hidden weights (1, 1) with biases −0.5 and −1.5, output weights (1, −1) with bias −0.5 |

## The lecture in 90 minutes

The lecture is slides 1–67 and estimates about 143 min. Slides 68–74 are the
self-check quizzes and take no lecture time. In a 2-hour slot nothing is
skipped. For a 90-minute slot, skip the slides in the second table. To jump,
type the slide number and press Enter.

The lecture opens on a question, slide 6: a threshold on one input is right
for 177 of the 200 points, a line for 185, so how was the line found? The plan
reaches the answer at about minute 60: the training loop of slide 47 prints
185 of 200, and slide 49 names it as the line of slide 6.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | The data, the question of the lecture, a fit and a classification |
| 0:10 | 8–13 | The neuron, AND and OR, the XOR puzzle, the boundary, its normal, the distance |
| 0:23 | 15–17, 27 | Rosenblatt's rule, AND for two epochs, what the rule cannot do |
| 0:33 | 28, 30–32 | The sigmoid, its derivative, the output as a probability |
| 0:42 | 34–36, 39–41, 43 | Likelihood, cross-entropy, the gradient, the update rule |
| 0:58 | 45, 47, 49 | The training loop, run: the line of slide 6 found |
| 1:05 | 50, 53 | Standardising the inputs |
| 1:09 | 56–61 | XOR: the puzzle settled, two lines, the network verified |
| 1:22 | 65, 67 | Three publications, Recap |
| 1:25 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| What **w** and *b* Do | 14 | 2 min |
| AND, epochs 3 to 6, and the ten updates as lines | 18–20 | 7 min |
| The Rule in Python | 21 | 3 min |
| Linearly separable, the theorem and its proof | 22–26 | 14 min |
| Gradient Descent Needs a Slope | 29 | 2 min |
| Where the Sigmoid Comes From | 33 | 3 min |
| What the Loss Charges, The Loss of Four Points | 37–38 | 5 min |
| The Gradient, Checked with Numbers | 42 | 3 min |
| One Minimum | 44 | 3 min |
| Reading the Loop, The Boundary Moves | 46, 48 | 5 min |
| The Learning Rate, Inputs on Different Scales | 51–52 | 4 min |
| Train and Test, How Sure Is an Accuracy? | 54–55 | 5 min |
| The Hidden Layer Changes the Coordinates, What Is Missing | 62–63 | 4 min |
| The History section slide, What a Modern Network Keeps | 64, 66 | 3 min |

- **Do not cut** slide 6 (the question of the lecture), slides 11–13 (the
  boundary, its normal, the distance), 16–17 (the rule and its first two
  epochs), 35–36 and 39–41 (the likelihood, the loss, the gradient), 47 and
  49 (the loop that finds the line of slide 6, and what it means), 58–61
  (XOR) or the closing slide 67 (Recap), whose bottom card answers slide 6.
- **Slide 10 sets a puzzle**: find **w** and *b* for XOR. One minute,
  collect two or three attempts, check one row of each aloud, and leave it
  open. Slides 57–58 settle it.
- **Slides 17–19 are done with the room.** Steps 1 to 6 on the board, each
  number said aloud. In the 90-minute plan the run stops after epoch 2: say
  its end, ten updates and then **w** = (2, 1), *b* = −2.
- **Slide 27** (What the Theorem Does Not Say): say aloud that Rosenblatt
  wrote his rule down and did not derive it. Slide 43 derives it from the
  Bernoulli likelihood.
- **Slides 21, 42, 47 and 61 run Python in the browser.** Select the play
  button at the top right of the code. The first run on a slide loads Python
  and takes some seconds. Run each once before the session.
- **Slide 21** (The Rule in Python): after the run, change `y` to
  `[0, 1, 1, 1]` and run again: OR, four updates, `w [1. 1.]  b 0.0`.
- **Slide 47** (The Training Loop): after the run, set `eta` to `0.05` and
  to `20`. This replaces slide 51 in the 90-minute plan.
- **Slides 24–26** (the proof): if they are skipped, say what the theorem
  bounds, the number of updates, and that slide 27 shows what happens
  without its assumption.
- **Slides 52 and 54–55** are repeated in the seminar on its own file:
  the loop that prints `nan`, the split, the uncertainty of the accuracy.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 68–74: six quiz slides for students to try afterwards. The same
questions, with their answers:

1. A neuron with a step has **w** = (2, −3) and *b* = 1. What are *z* and
   the output for **x** = (1, 2)?
   *z = 2 − 6 + 1 = −3, so the output is 0.*
2. A neuron has **w** = (6, 8) and *b* = −5. How far is **x** = (2, 1) from
   its boundary?
   *z = 15 and ‖**w**‖ = 10, so the distance is 1.5, on the side of class 1.*
3. Rosenblatt's rule with η = 1. The weights are **w** = (1, −1), *b* = 0,
   and the next point is **x** = (0, 1) with target 1. What are the weights
   after this step?
   *z = −1, the output is 0, the error is +1. The rule adds the point:
   **w** = (1, 0), b = 1.*
4. A logistic neuron gives ŷ = 0.8 for a point with label 0. What is its
   cross-entropy loss?
   *−ln(1 − 0.8) = −ln 0.2 = 1.609.*
5. For **x** = (2, −1) with label 1 a logistic neuron gives ŷ = 0.3. What
   is the gradient of the loss with respect to the weights?
   *(ŷ − y) **x** = −0.7 · (2, −1) = (−1.4, 0.7).*
6. XNOR is 1 when the two inputs are equal. Can one neuron compute it?
   *No. The conditions are b > 0, w₁ + b ≤ 0, w₂ + b ≤ 0 and
   w₁ + w₂ + b > 0. The middle two add to w₁ + w₂ + 2b ≤ 0, the outer two
   to w₁ + w₂ + 2b > 0.*

## Paired seminar

[Seminar 11 — A Perceptron from an Empty File](../seminars/seminar_11.md)
starts from an empty script. The room reads a file of 300 labelled points,
plots it, and sets the weights of a neuron by hand. It writes Rosenblatt's
rule and checks it against the AND table of the lecture. It then writes the
sigmoid, the loss and the training loop, sees the loop fail on inputs of
different scales, standardises them, and measures the result on 75 points
that were held back: 67 correct, 89 % ± 4 %.

## Take-aways

- A neuron computes *z* = **w** · **x** + *b* and compares it with zero. Its
  decision boundary is the line *z* = 0, **w** is the normal of that line,
  and *z* / ‖**w**‖ is the distance of a point from it.
- Rosenblatt's rule changes the weights only at a point that is wrong, by
  the error times the input. On a linearly separable set it stops after at
  most *R*²/γ² updates. On any other set it never stops.
- The sigmoid turns *z* into a probability, and its derivative is
  σ(1 − σ).
- The loss is not chosen. It is the negative logarithm of the Bernoulli
  likelihood, as χ² was, up to a factor 2 and a constant, that of the
  Gaussian likelihood.
- The gradient of the cross-entropy is the error times the input,
  (ŷ − *y*) **x**. The update has the same form as Rosenblatt's rule and as
  the gradient of a least-squares line.
- The training loop is four lines of NumPy: the outputs, the loss, the step
  in **w**, the step in *b*.
- Inputs are standardised before training, with the mean and standard
  deviation of the training set. Those two numbers per column belong to the
  model.
- A result is judged on points that were held back, and an accuracy on *N*
  points has the binomial uncertainty √(*p*(1 − *p*)/*N*).
- One neuron draws one line. XOR needs two lines, and a hidden layer of two
  neurons supplies them: it gives the output neuron new coordinates in
  which one line is enough.
