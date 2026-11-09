# 10: Classification and the Perceptron

Lectures 8 and 9 estimated numbers from the weather log: a mean with its
uncertainty, a straight line fitted by least squares and by gradient
descent. Lecture 10 asks for a class instead of a number: will it freeze
tonight? Each evening of the log becomes one example, the temperature and
the humidity at 18:00 as the inputs and frost at 06:00 the next morning as
the label; 3646 evenings, 1229 of them followed by frost. The lecture
builds one artificial neuron that answers the question, and pushes the
numbers of real evenings through every expression: the weighted sum and
the step, the line it draws, Rosenblatt's rule of 1958, the sigmoid and the
cross-entropy from the likelihood, whose slope, (ŷ − y)·x, is Rosenblatt's
rule and the update of Lecture 9's straight line. Trained on 2016 to 2022,
the neuron is right on 96.1 ± 0.6 % of the evenings of 2023 to 2025, as
the threshold "below 3.8 °C" it rediscovers, against 65.4 % for "never
frost". A class `Perceptron` with the methods `predict` and `fit` holds
its numbers: object-oriented code enters the course here. The lecture
ends on what one neuron cannot do, XOR. No library is used on a slide;
the code is plain Python on lists.

## What the lecture covers

1. **The question** (slides 1–4): 8 December at 18:00 in the ten years of
   the log, nine of them followed by frost; 2.6 °C and 85 % in 2025, and
   frost at 06:00; the 3646 evenings as points of temperature and humidity,
   two clouds that overlap between 0 and 6 °C.
2. **From a number to a class** (5–10): inputs, label, output and
   accuracy; the list of evenings; the baseline "never frost", 66.3 %; a
   threshold on the temperature, best below 3.8 °C, 95.7 %, scored live on
   ten evenings.
3. **One neuron** (11–17): z = w₁x₁ + w₂x₂ + b and a step; the evening of
   8 December 2025 pushed through it; the neuron in five lines of Python;
   where the output changes, a straight line, and how its three numbers
   set it, moved by hand over all 3646 evenings (upright at 3.8 °C 3490
   right, tilted 3494); AND and OR from one neuron, and the XOR puzzle.
4. **Rosenblatt's rule** (18–27): why not try every line (8.1 million lines
   for three numbers); the rule and why it moves z the right way; one
   update with the numbers of 1 January 2016; AND by hand, epochs 1 and 2,
   and the ten updates as lines; the rule in Python, live; linearly
   separable; on 2551 evenings the rule never stops (95.2 %, 33.3 %,
   92.3 %, … after each pass); what it does not give.
5. **From the step to the sigmoid** (28–36): counting errors gives no
   slope; frost by counting, per degree (62 % of the evenings at 3 to
   4 °C); the sigmoid; the output as a probability for four evenings of
   December 2025; the Bernoulli probability of what happened; the
   likelihood and the loss, the cross-entropy, of the four (1.094); what
   the loss charges; the loss computed live.
6. **The gradient** (37–43): the slope of the loss, (ŷ − y)·x, with the
   numbers of 8 December 2025; checked with a nudge; one step downhill; the
   mean slope over four evenings; one update for three models (the line of
   Lecture 9, Rosenblatt's rule, the logistic neuron); the loss as one bowl.
7. **Train and test** (44–53): seven years to learn from, three to score;
   five passes over the training evenings (loss from 0.693 to 0.110);
   Rosenblatt's loop with one change, in plain Python; tonight with a
   probability, 0.80, and live with this evening's numbers; the ± of an
   accuracy; four rules on the test years; seen and unseen evenings (a rule
   that keeps every evening: 98.8 % seen, 93.1 % unseen); missed frosts and
   false alarms.
8. **A model as an object** (54–58): what a model holds and does; the same
   code as a class `Perceptron`, built one method at a time; fit and
   predict, live, on AND; why the numbers live in the object.
9. **The limit: XOR** (59–62): no line exists, by four inequalities; what
   the two rules do on XOR.
10. **Wrap-up** (63–65): the answers for 8 December 2025, every rule with
    its test accuracy; the recap.
11. **For the curious** (66–79), after the recap and outside the lecture
    time: the convergence theorem and its proof, checked on AND (at most 51
    updates, 10 needed); w at a right angle to the line, the distance of a
    point from it, what w and b do; the slope of the sigmoid and the
    gradient by the chain rule; z as the logarithm of the odds; where the
    sigmoid comes from (Bayes' rule for two Gaussian classes); the humidity
    in percent, on which the rule fails; history in three dates (1958,
    1969, 1986).

## The lecture, part by part

The main path is slides 1–65. **Plan to skip the slides of the second
table** to fit the two-hour slot; slides 66–79 (For the Curious) and
80–88 (the self-check quizzes) take no lecture time. To jump, type the
slide number and press Enter.

| Slides | Part |
|--|--|
| 1–4 | The question: 8 December in ten years, then the 3646 evenings as two overlapping clouds |
| 5–9 | Inputs, label and output; the list; the baseline never frost; the best threshold, 3.8 °C |
| 11–17 | The neuron, one evening through it, in Python, its line (live), AND and OR |
| 18, 20–22, 24–27 | Rosenblatt's rule, one update, AND by hand, the rule live, separable or not, the rule on the evenings and what it does not give |
| 28–40 | No slope in a count, frost by counting, the sigmoid, the probability, the likelihood and the cross-entropy, the gradient checked and one step |
| 42 | One update for three models |
| 44–46, 48–52 | Train and test, five passes, tonight with a probability, the ± of an accuracy, four rules, seen and unseen evenings |
| 54–58 | A model as an object: the class `Perceptron`, live |
| 59–65 | XOR, the answers, the recap |

| Skip | Slides |
|--|--|
| Score a threshold on ten evenings, live | 10 |
| Why not try every line | 19 |
| The ten updates of AND as lines | 23 |
| The mean slope over four evenings; the loss as a bowl | 41, 43 |
| Rosenblatt's loop with one change | 47 |
| Missed frosts and false alarms | 53 |

- **Do not cut** slides 3 and 64: the question and its answer. Slide 3
  asks for a show of hands before its click.
- **Do not cut** slides 21–22 (one update and AND by hand: do the steps on
  the board with the room), 33–34 (the likelihood and the loss), 38–40
  (the slope, its check and one step) or 55–57 (the class): Seminar 10
  builds the same class, `Perceptron`, with the same lines.
- **Slide 16 is an interactive figure** that works offline: the neuron on
  all 3646 evenings. It opens on "below 3.8 °C" (3490 right) with 8 December
  2025 pushed through z; press never frost (66.3 %) and reset, tilt the
  line with the keys (w₂ PageUp ×4, b PageDown ×3 and ↓ ×2: 3494 right),
  tap an evening to push it through z. Use it on the projected window, not
  in the presenter view.
- **Seven slides run Python in the browser**: 10, 14, 24, 36, 39, 49 and
  57. The first ▶ downloads the Python runtime, so run one block before
  the lecture. Slides 24 and 57 show the output beside the code. On slide
  49 type this evening's 18:00 temperature and humidity, from any weather
  service, and run: the neuron's probability of frost for tonight.
- **Clicks:** slide 3 holds the answer back for one click; slide 13 builds
  the sum one step per click; slides 15, 19, 21, 32, 38 and 40 add one line
  of numbers per click; slide 47
  highlights the code in steps; slide 56 builds the class one method per
  click.
- **Every figure fills its slide** and is drawn from the weather log by
  `figures/src/perceptron.py`, which also prints every number the slides
  state (`python figures/src/perceptron.py`); the evenings of slide 16 come
  from `figures/src/interactive_data.py`.
- **One symbol per meaning:** x₁, x₂ the inputs, y the label, ŷ the
  output, w₁, w₂ the weights, b the bias, z the weighted sum, η the
  learning rate, L the likelihood; the loss is written "loss", and the
  sigmoid "sigmoid", since σ is the standard deviation of Lecture 8.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/10-classification-and-the-perceptron/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 80–88: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A neuron with a step has w₁ = 2, w₂ = −3 and b = 1. What are z and the
   output for the input x = (1, 2)?
   *z = 2 · 1 + (−3) · 2 + 1 = −3, and the output is 0: the step gives 1
   only for z > 0. Forgetting the bias gives −4.*
2. Of 1000 test evenings, 900 had no frost. A classifier is right on 890
   of them. What does this say?
   *It is worse than the rule "never frost", which is right on 900. The
   baseline comes before any accuracy is praised.*
3. Rosenblatt's rule with learning rate 1. The numbers are w = (1, −1),
   b = 0. The next point is x = (0, 1) with label 1. What are the numbers
   after this step?
   *w = (1, 0), b = 1: z was −1, so the output was 0 and the error +1;
   the rule adds x to w and 1 to b.*
4. A logistic neuron gives ŷ = 0.8 for an evening without frost (y = 0).
   What is the cross-entropy loss of this evening?
   *−ln(1 − 0.8) = −ln 0.2 = 1.609. The value 0.223 would be the loss had
   the frost come.*
5. One evening has x = (2, −1) and label y = 1, and a logistic neuron gives
   ŷ = 0.3. What is the slope of its loss in w₁ and w₂?
   *(ŷ − y) x = (0.3 − 1) · (2, −1) = (−1.4, 0.7), and −0.7 in b.*
6. A rule is right on 900 of 1000 test evenings. What is its accuracy with
   its standard error?
   *90.0 ± 0.9 %: the square root of 0.9 · 0.1 / 1000 is 0.0095.*
7. After `model = Perceptron()` and `model.fit(xs, ys, 5)`, what has `fit`
   changed?
   *`model.w` and `model.b`, the numbers this object holds; another
   `Perceptron()` keeps its own.*
8. XNOR is 1 when the two inputs are equal. Can a single neuron compute
   it?
   *No: it is XOR with the labels exchanged, and the same four
   inequalities contradict each other, whatever the training.*

## Paired seminar

[Seminar 10 · A Class of Your Own](../seminars/seminar_10.md) works on the
same evenings in plain Python, for students who write code for the first
time: one evening through a function `predict`, every evening and the
accuracy (95.7 % for "below 3.8 °C"), one step of Rosenblatt's rule, the
loop over five epochs, and then the same lines as a class `Perceptron`,
one method at a time (`__init__`, `predict`, `fit`, `score`), which is
right on 95.5 ± 0.6 % of the evenings of 2023 to 2025. Optional: the
sigmoid in `fit` (the lecture's 96.1 %), and scikit-learn's `Perceptron`
and `LogisticRegression`, which take the same calls. The last part puts a
baseline and a threshold to a yes-or-no question about the student's own
data.

## Slides that left the deck

On 9 November 2026 the lecture moved from week 11 to week 10 and was
rebuilt on the weather log. Until then it was *The Perceptron*, on 200
points generated around (0, 0) and (2, 2), trained in NumPy. Parked slides
are in `lectures/content/parked/10_Classification_and_the_Perceptron.md`;
the deck before the rebuild can be read with
`git show 328aba2:lectures/content/slides/11_The_Perceptron.md`.

| Earlier slides | What happened | Reason |
|--|--|--|
| The goal quote; Learning Objectives | Parked | Preambles leave every lecture (9 Nov 2026); the deck opens on its question |
| A Classification Problem; Classify by a Threshold or by a Line | Replaced by slides 3–4 and 8–9 | The question is the room's own: the evenings of the weather log |
| The fit and the classification side by side | Parked; its last row is slide 42 | The likelihood steps are on slides 33–34 |
| AND, epochs 3 to 6 | Parked | One pass by hand and the ten updates as lines carry the run |
| The convergence theorem and its proof; the normal vector and the distance; what w and b do; the derivative of the sigmoid; the gradient in three parts; where the sigmoid comes from | Moved to For the Curious | A derivation on the main path ends in a number; proofs and long derivations wait until after the recap |
| Training in NumPy, Reading the Loop, The Training Loop | Parked; replaced by slide 47 | No library calls on a lecture slide: the same loop in plain Python |
| The learning rate; inputs on different scales; standardising | Parked; the scale of the inputs is slide 78 | The humidity as a fraction keeps the inputs on similar scales without standardising |
| Two lines separate XOR; a network of three neurons; the hidden layer; what is missing; what a modern network keeps | Parked, for Lecture 11 | Two layers are the opening of Lecture 11, From Neurons to Language Models |
| The quiz on the distance from the line | Parked | The distance is in For the Curious |

## Further reading

- **F. Rosenblatt**, *The Perceptron: A Probabilistic Model for Information
  Storage and Organization in the Brain*, Psychological Review 65,
  386–408 (1958): the rule of slides 20–22.
- **M. Minsky and S. Papert**, *Perceptrons*, MIT Press (1969): what one
  layer of such units cannot compute.
- **M. Nielsen**, *Neural Networks and Deep Learning*, free online
  (neuralnetworksanddeeplearning.com), chapter 1 (perceptrons and sigmoid
  neurons) and chapter 3 (the cross-entropy).
- **D. J. C. MacKay**, *Information Theory, Inference, and Learning
  Algorithms*, free online, chapter 39: the single neuron as a classifier.
- **C. M. Bishop**, *Pattern Recognition and Machine Learning*, chapter 4:
  the perceptron and logistic regression, with the convergence theorem.

## Take-aways

- A classifier is scored against the rule that ignores its inputs: "never
  frost" is right on 66.3 % of the evenings before anything is learned.
- A neuron computes z = w₁x₁ + w₂x₂ + b and says 1 when z > 0. Its
  boundary is a straight line; the threshold "below 3.8 °C" is the neuron
  w = (−1, 0), b = 3.8.
- Rosenblatt's rule adds the error times the input after each wrong
  example. It stops on classes that one line separates, and never on
  classes that overlap: there the line it ends on depends on when it is
  stopped.
- The sigmoid turns z into a probability. The probability of what
  happened, multiplied over the examples, is the likelihood; minus its
  logarithm per example is the cross-entropy, and its slope is
  (ŷ − y)·x, the error times the input.
- The same update trains the straight line of Lecture 9, Rosenblatt's
  perceptron and the logistic neuron; they differ in ŷ.
- A slope worked out on paper is checked with a nudge before it is
  trusted.
- A model is scored on data it has not seen, split so that no test example
  has its neighbours in training: here by years. An accuracy has a ± like
  any measured share, √(p(1 − p)/N).
- A rule that keeps every training example is nearly perfect on them and
  worse on new ones; three numbers cannot learn 2551 evenings by heart.
- One accuracy hides two kinds of error. The cut on the probability
  chooses between missed frosts and false alarms.
- A model is an object: its numbers inside, `fit` to change them,
  `predict` to use them. Every library model has the same two calls.
- One neuron draws one line, and no line computes XOR.
