# 11: From Neurons to Language Models

Lecture 10 ended on one neuron and its limit: no single line separates the
four points of XOR. Lecture 11 goes from there to the language models that
write text, so that what a chat model does with a prompt is no longer a
black box. It opens on twelve true sentences about the weather station, one
per month, and five sentences that a program wrote after counting them,
three of them false. Two layers of neurons solve XOR; the chain rule trains
them, one step with numbers on a frost evening of the log. Then text becomes
numbers: words get ids, the simplest language model counts which word
follows which, and it writes fluent sentences that are often false, because
it sees one word of context. Words become vectors, softmax turns scores
into probabilities at a temperature, and attention weighs the earlier words
so that "july" decides the word after "in july it was". A large language
model is that loop with a very large network, pretrained on a very large
text and tuned on instructions. The last part draws the consequences for
prompting: give the context, an example, the format and the constraints;
ask for a test and run it; paste no personal data; say where a model was
used.

## What the lecture covers

1. **The question**: twelve sentences from the ten-year mean of each month
   (*in july it was warm .*), and five sentences a program wrote after
   counting them, three false.
2. **Two layers solve XOR**: XOR as "OR but not AND", two lines; a 2-2-1
   network of step neurons with nine weights set by hand; the four inputs
   pushed through it, on the slide and in Python; the hidden layer as a
   change of coordinates.
3. **Training a network**: a loss, one number for how wrong one answer
   is (−ln 0.3865 = 0.951); gradient descent needs a slope, so the step
   becomes a sigmoid; one evening of the log (12 April 2025, 2.0 °C at
   18:00, frost by 06:00) through two neurons; the chain rule, checked by a
   nudge; the backward pass one link at a time, with the whole chain as a
   picture; the nudge check of one derivative, the slope of the loss drawn;
   one step of gradient descent (ŷ from 0.386 to 0.692, the loss from 0.951
   to 0.369), and the same in Python; XOR learned from random weights, the
   hidden neurons ending near OR and AND; three of twelve random starts that
   stop on a plateau.
4. **Text as numbers**: the 20 words of the text as ids; which word follows
   which; next-word probabilities from counts (after "was": 3, 4, 2, 3 of
   12); the counting in Python, a dictionary of lists as `weather.group`;
   generating text by drawing; what the model wrote: 38 of 144 sentences
   true, and month by month only as often as the month's word follows
   "was"; one word of context is not enough, and a table of every context
   cannot be built.
5. **Words as vectors**: each month described by the weather words it came
   with in the 120 sentences of 2016–2025, twelve small bar charts; the dot
   product and the cosine, with numbers; the similarity of the twelve months
   as a picture, four seasons from the text alone; vectors in a language
   model are learned, a row of a table per token.
6. **Scores into probabilities**: softmax of three scores (0.659, 0.242,
   0.099), the sigmoid as softmax of two; a temperature, live: the scores
   dragged, *T* from 0.1 to 3, words drawn (0.864 at 0.5, 0.502 at 2); what
   the temperature does to text, with ten draws at each temperature.
7. **Context and attention**: which earlier word decides; attention as a
   weighted average with softmax weights (0.909 on "july", warm 0.932 in
   place of 0.25); where the scores come from, a dot product; the same in
   Python; attention in a large model, the transformer.
8. **A large language model**: the loop from a prompt to the next token;
   tokens, and a vocabulary of pieces built by counting pairs of letters in
   the twelve sentences; pretraining, the loss of Lecture 10 at every token (1.358 against
   0.069 on the twelve weather words); the number of parameters, from 4 to
   1.75 × 10¹¹; instruction tuning, and a chat as one text; what it is not:
   a database, a calculator, a view of your data, the same twice.
9. **Prompting, from how it works**: what a prompt gives the model; one
   request without and with context; a test with a known answer, which fails
   on a correct function because of a float; a question only the data can
   answer (22 352 hours below 0 °C); what to check and how; where a model
   helps in an analysis; what never to paste; saying where it was used;
   keeping the work reproducible.
10. **Wrap-up**: what an LLM does with a prompt, in five steps with the
    lecture's numbers; the recap.
11. **For the curious**, after the recap and outside the lecture time: why
    two layers without a bent function are one; backpropagation for the
    2-2-1 network in eight lines; the ten years as text; three dates (1948,
    1986, 2017). k-means, the ROC curve and cross-validation stay in the
    optional Lecture 16.

## The numbers of the lecture

Every number on the slides is computed by `figures/src/language.py`; run
`python figures/src/language.py` to print them all.

| Where | Result |
|--|--|
| The text | One sentence per month from its mean temperature, 2016–2025: below 0 °C cold, below 10 °C cool, below 15 °C mild, else warm. 12 sentences, 72 words, 20 different words |
| After "was" | cold 3, cool 4, mild 2, warm 3 of 12 |
| A drawn sentence is true | 38 / 144 = 0.264; 2655 of 10 000 draws |
| The tiny network, 12 April 2025 | *x* = 2.0, *y* = 1 (−3.8 °C at 06:00); *v* = −1, *c* = 1, *w* = 2, *b* = −1: ŷ = 0.386, loss 0.951; one step with η = 1: ŷ = 0.6915, loss 0.3689 |
| XOR from `random.Random(0)` | η = 2, 2000 steps: loss 0.696 → 0.003; all four right from step 205; 9 of 12 starts learn it |
| The month vectors, 120 sentences | January (9, 1, 0, 0), July (0, 0, 0, 10); cosine of January with February 0.994, with March 0.220, with July 0 |
| Softmax of (2.0, 1.0, 0.1) | *T* = 1: 0.659, 0.242, 0.099; *T* = 0.5: 0.864, 0.117, 0.019; *T* = 2: 0.502, 0.304, 0.194; ten draws from `random.Random(1)`: warm 10 times at *T* = 0.5, 5 times at *T* = 2 |
| Pieces counted in the twelve sentences | the most frequent pairs of letters: w + a 15 times, i + n 12, i + t 12, wa + s 12, c + o 7; after 8 merges `in`, `it`, `was`, `cool` are single pieces, `january` is still letters |
| Attention on "july it was" | scores 3, 0, 0; weights 0.909, 0.045, 0.045; warm 0.932 |
| Hours below 0 °C | 22 352 of 87 552 |

## The lecture, part by part

The lecture is slides 1–69 and estimates about 127 min (the speaker notes add
up to about 130), so in the two-hour slot **plan to skip the slides of the
second table** (about 16 min). Slides 70–74 are the optional section For
the Curious, and slides 75–83 the self-check quizzes; neither takes lecture
time. To jump, type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–3 | The question: twelve true sentences, five written by a program, three false |
| 4–9 | Two layers solve XOR: OR but not AND, the 2-2-1 network with weights set by hand, the four inputs on the slide and in Python, the change of coordinates |
| 10–21 | Training: the loss of one answer, a slope, one evening through two neurons, the chain rule, backward one link at a time, the nudge, one step, XOR learned from random weights, the trained network over every input (turned by hand) |
| 22–31 | Text as numbers: ids, the counts after each word, probabilities, the counting in Python, generating text, what the model wrote, the chance of the true word month by month, one word of context |
| 32–37 | Words as vectors: the months by their weather words, the dot product and the cosine, the twelve months as a picture, vectors in a language model |
| 38–42 | Softmax, the temperature live (drag the scores, *T* from 0.1 to 3, draw words), its effect on text |
| 43–49 | Context and attention: the word that decides, the weighted average, where the scores come from, attention in a large model |
| 50–56 | A large language model: the loop, tokens, pretraining, parameters, instruction tuning, what it is not |
| 57–66 | Prompting: what a prompt gives, without and with context, a test with a known answer, a question only the data can answer, what to check, where a model helps, what never to paste, saying where it was used, reproducibility |
| 67–69 | What an LLM does with a prompt; recap |

| Skip | Slides |
|--|--|
| Check one derivative by a nudge; the step in Python | 16, 18 |
| Not every start learns XOR | 21 |
| The chance of the true word, month by month | 30 |
| The dot product in Python | 36 |
| Softmax in Python | 41 |
| Where the scores come from | 46 |
| The number of parameters | 54 |
| Where an LLM helps in an analysis | 63 |

- **Do not cut** slide 3 (the question), slides 24–29 and 31 (the counting
  model, which answers it) or slide 45 (attention as a weighted average):
  slide 68 answers the opening with their numbers.
- **Do not cut** slides 56 and 58–60 (what a model is not, what a prompt
  gives, a prompt with context, the test) or 63–64 (what never to paste,
  saying where a model was used): the seminar applies them.
- **Slides 8, 18, 26, 28, 36, 41, 48 and 60** run Python in the browser,
  plain Python without libraries. The first run downloads the Python
  runtime, so run one block before the lecture. Slide 28 prints the five
  sentences of slide 3 (`random.seed(38)`); slide 60 shows a test that
  fails on a correct function, because 25.275 comes out as
  25.275000000000002.
- **Slide 20 is a figure in three dimensions** that works offline: the
  output of the trained network over every input. It turns by itself; drag
  to turn and tilt it; the buttons at its left switch between ŷ, h₁ and h₂
  and glide to two views (along the ridge, from above); a double-click goes
  back to the opening view. The audience window follows the presenter's.
- **Slide 40 is an interactive figure** that works offline: at *T* = 0.5
  read the row of warm (e⁴ = 54.60, Σ = 63.21, *p* = 0.864), press the
  chips 1, 2 and 3, drag the score of mild sideways, press "draw" or
  "×20". Use it on the projected window, not in the presenter view.
- **Slide 15** builds the backward pass in five clicks, one factor of the
  chain rule per click, and shows the whole chain on the sixth; **slide 45**
  the attention weights in three clicks, then the weighted average.
- **Slides 11, 14 and 39** step a formula per click, the numbers put in
  shown in the accent colour: the loss of 0.386, the chain rule at t = 1,
  the softmax of warm.
- **Slides 19 and 21** are the training of slide 17 repeated: nine weights,
  four points, 2000 steps; the hidden neurons it finds are an OR and an
  AND, the solution of slide 6.
- **Slides 70–74** (For the Curious) are for time left at the end or for
  students afterwards.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/11-neurons-to-language-models/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 75–83: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. A network computes *h*₁ = step(*x*₁ + *x*₂ − 0.5), *h*₂ = step(*x*₁ +
   *x*₂ − 1.5) and ŷ = step(*h*₁ − *h*₂ − 0.5). What is ŷ for the input
   (1, 1)?
   *0: z₁ = 1.5 and z₂ = 0.5, so both hidden neurons give 1, and
   1 − 1 − 0.5 = −0.5 gives 0. The AND neuron turns OR into XOR.*
2. *f* = *a*² and *a* = 3*t* + 1. What is d*f*/d*t* at *t* = 2?
   *42: a = 7, df/da = 2a = 14, da/dt = 3. A nudge to t = 2.001 gives
   (49.042009 − 49) / 0.001 = 42.009.*
3. In a text the word "was" is followed 3 times by cold, 4 times by cool,
   2 times by mild and 3 times by warm. What probability does a model that
   counts word pairs give to "mild" after "was"?
   *2 / 12 = 0.167.*
4. What is the dot product of **a** = (1, 2, 0) and **b** = (2, 0, 3)?
   *1 · 2 + 2 · 0 + 0 · 3 = 2: one number.*
5. Softmax turns the scores (2.0, 1.0, 0.1) into (0.659, 0.242, 0.099) at
   *T* = 1. What happens to the first probability at *T* = 0.5?
   *It rises to 0.864: the scores are doubled to (4, 2, 0.2), and the
   likely word becomes more likely.*
6. Two earlier words get the attention scores 2 and 0, and their vectors
   are (1, 0) and (0, 1). What is the weighted average?
   *(0.881, 0.119): softmax of (2, 0) gives the weights 0.881 and 0.119.*
7. A chat model gives you a reference with authors, journal, year and DOI.
   What follows from how the reply was made?
   *It is a likely continuation of the text and may not exist: open the DOI
   and read the paper. Asking again only draws again.*
8. A model wrote a correct function and the test `assert mean_valid(hours)
   == 25.275`, which gives an `AssertionError`. Why?
   *The mean comes out as 25.275000000000002: the decimals are not exact in
   binary. `round(mean_valid(hours), 3) == 25.275` passes. A test is code
   too, and is checked by running it.*

## Paired seminar

[Seminar 11 · A Language Model by Hand](../seminars/seminar_11.md) builds the counting model of the lecture on real text, in plain Python, in a new, empty folder (the `analysis` environment, no new package). The lecturer runs four scripts on 32 033 first names (makemore, MIT; US Social Security names of 2018) and 40 000 lines of Shakespeare: which letter follows which (after `q`, `u` 0.757), names drawn from the counts and their loss (2.454 against 3.296 blind), the same counts at three temperatures (as T goes to 0 the model writes the name `a`), and text from 1, 3 and 6 characters of context; the room asks a chat LLM the same and sets its answers beside the counts. Then pairs, with any tools and an LLM, predict and measure whether a longer context always guesses the next letter of new names better: best at 4 letters, 0.362 ± 0.003, worse beyond, where more contexts were never seen.

## Further reading

- **C. E. Shannon**, *A Mathematical Theory of Communication*, Bell System
  Technical Journal 27 (1948): English-like text, each word drawn by how
  often it follows the one before it in a book.
- **D. Rumelhart, G. Hinton, R. Williams**, *Learning representations by
  back-propagating errors*, Nature 323 (1986): the chain rule through the
  hidden layers.
- **A. Vaswani et al.**, *Attention Is All You Need* (2017): the transformer.
- **J. R. Firth**, *A Synopsis of Linguistic Theory, 1930–1955* (1957): the
  quote of slide 2.
- The optional Lecture 16 derives backpropagation for any number of hidden
  units, trains networks in NumPy and measures them (confusion matrix, ROC
  curve, cross-validation, leakage), and adds k-means.

## Take-aways

- A layer of neurons computes new coordinates; in them, one line separates
  what no line separated before. Without a bent function between the
  layers, two layers are one.
- Training is the step of Lectures 9 and 10 for every weight: the chain rule
  passes the error back one link at a time, and a nudge checks the result.
- A language model gives every possible next word a probability. The
  simplest one counts which word follows which; it writes grammatical text
  that is often false, because it sees one word of context.
- Words become vectors; the dot product and the cosine measure how alike two
  are. Words used alike get similar vectors, from text alone.
- Softmax turns scores into probabilities; the temperature sharpens or
  flattens them, which is why a reply can differ each time.
- Attention is a weighted average over the earlier words, with weights from
  softmax: it lets the word that decides count most.
- A large language model predicts the next token with a very large network,
  pretrained on a very large text and tuned on instructions. It is not a
  database, not a calculator, and has not seen your data.
- A prompt gives the context, an example, the format and the constraints.
  Every reply is checked: code by a test with a known answer, numbers by
  computing them, references by opening them. Personal data stay out, and
  the README says where a model was used.
