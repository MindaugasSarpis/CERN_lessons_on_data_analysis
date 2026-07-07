# L11: Probability & Statistics

---

## Overview

**Duration**: ~120 minutes (2 h slot)

**Prerequisites**: L7-L8 (Python basics), L9 (Concepts of Data Analysis), basic algebra

**Learning Objectives**:
- State and apply the axioms of probability
- Compute conditional probabilities and apply Bayes' theorem
- Distinguish between discrete and continuous random variables
- Compute and interpret descriptive statistics (mean, median, variance, std dev)
- Identify and describe common probability distributions (Binomial, Poisson, Normal)
- Explain the Central Limit Theorem and its practical implications
- Understand the basics of estimation (point estimates, confidence intervals, MLE)

---

## Lecture Structure

### Part 1: Foundations of Probability (20 min)
- What is probability? Frequentist vs Bayesian interpretation
- Experiment, sample space, event
- Kolmogorov axioms (non-negativity, normalisation, countable additivity)
- Derived rules: complement, addition, multiplication
- Worked example: dice problems

### Part 2: Conditional Probability & Bayes (20 min)
- Conditional probability P(A|B) = P(A∩B)/P(B)
- Independence: P(A∩B) = P(A)·P(B)
- Bayes' theorem: prior × likelihood / evidence = posterior
- Medical test example (sensitivity, specificity, false positives)
- Tree diagrams for visualising conditional probability

### Part 3: Random Variables & Distributions (20 min)
- Discrete vs continuous random variables
- PMF (probability mass function) and PDF (probability density function)
- CDF (cumulative distribution function)
- Key distributions overview: Bernoulli, Binomial, Poisson, Uniform, Exponential, Normal

### Part 4: Descriptive Statistics (15 min)
- Central tendency: mean, median, mode — when to use which
- Spread: range, variance, standard deviation
- Population vs sample statistics, Bessel's correction (N−1)
- Expectation and variance: definitions and properties

### Part 5: The Normal Distribution & CLT (20 min)
- Normal distribution: PDF, parameters (μ, σ)
- Standard normal and Z-transformation
- The 68-95-99.7 rule
- CERN's 5σ discovery threshold (why 5 sigma?)
- Central Limit Theorem: averages of any distribution → Normal
- Standard error = σ/√n

### Part 6: Estimation & Connection to Fitting (15 min)
- Point estimation: what makes a good estimator?
- Maximum Likelihood Estimation (MLE) — concept and normal mean example
- Interval estimation: confidence intervals (interpret carefully!)
- Connection to L12: least squares = MLE for normally distributed errors
- Chi-squared statistic preview

### Part 7: Pitfalls & Practical Advice (10 min)
- Common mistakes: confusing probability and statistics, p-hacking, misinterpreting CIs
- Practical advice: always visualise first, check assumptions, report uncertainties
- Preview: L12 applies these concepts to real fitting problems

---

## Teaching Tips

### Common Student Struggles

1. **"What's the difference between probability and statistics?"**
   - Probability: given a model → predict outcomes (deductive)
   - Statistics: given data → infer the model (inductive)
   - "Probability goes forward (model → data), statistics goes backward (data → model)"

2. **Bayes' theorem confusion**
   - Students mix up P(A|B) and P(B|A)
   - Use the medical test example repeatedly — it's intuitive
   - Draw the tree diagram every time
   - Ask: "Given a positive test, what's the probability of actually being sick?"

3. **"Why N−1 instead of N?"**
   - Intuition: the sample mean is already estimated from the data, so one degree of freedom is "used up"
   - Analogy: if you have 3 numbers that must average to 5, only 2 are free to vary
   - Show numerically: sample variance with N underestimates true variance

4. **PDF doesn't give probability**
   - P(X = exactly 3.000...) = 0 for continuous variables
   - PDF values can be > 1 (they're densities, not probabilities)
   - Probability = area under the curve: P(a < X < b) = ∫f(x)dx

5. **"What does 5 sigma mean?"**
   - σ = standard deviation. 5σ = 5 standard deviations from expected
   - P(fluctuation ≥ 5σ) ≈ 1 in 3.5 million — extremely unlikely to be chance
   - CERN chose this high threshold because they search across many channels

### Interactive Elements

- **Dice simulation**: Roll dice (physically or digitally), build histogram, observe CLT
- **Medical test Bayes'**: Walk through with specific numbers, let students compute
- **Distribution matching**: Show data histograms, students guess the distribution
- **Python demo**: Generate random samples, compute statistics, plot distributions

---

## Common Questions & Answers

**Q**: Why do we need both mean and median?
**A**: Mean is sensitive to outliers, median is not. For symmetric data, they're similar. For skewed data (e.g., income distribution), median is more representative. Always report both for important datasets.

**Q**: What's the difference between standard deviation and standard error?
**A**: Standard deviation (σ) measures the spread of individual data points. Standard error (σ/√n) measures the uncertainty of the mean estimate. As you collect more data (larger n), the standard error shrinks but σ stays the same.

**Q**: When do I use Poisson vs Binomial?
**A**: Binomial: fixed number of trials, each with success/failure. Poisson: counting events in a fixed interval (time, area, volume) when events are rare and independent. Poisson is the limit of Binomial when n→∞ and p→0 with np=λ.

**Q**: What's a confidence interval, really?
**A**: A 95% CI means: if we repeated this experiment many times, 95% of the computed intervals would contain the true value. It does NOT mean "there's a 95% probability the true value is in this interval" (that's the Bayesian credible interval).

**Q**: Why does CERN require 5 sigma and not 3?
**A**: The look-elsewhere effect: when you search across many mass bins and channels, random fluctuations happen more often than you'd expect from a single test. 5σ accounts for this by requiring overwhelming evidence.

---

## Key Reference Tables

### Common Probability Distributions

| Distribution | Type | Parameters | Mean | Variance | When to Use |
|-------------|------|-----------|------|----------|-------------|
| **Bernoulli** | Discrete | p | p | p(1−p) | Single yes/no trial |
| **Binomial** | Discrete | n, p | np | np(1−p) | Fixed trials, count successes |
| **Poisson** | Discrete | λ | λ | λ | Count events in fixed interval |
| **Uniform** | Continuous | a, b | (a+b)/2 | (b−a)²/12 | Equal probability in range |
| **Exponential** | Continuous | λ | 1/λ | 1/λ² | Time between events |
| **Normal** | Continuous | μ, σ | μ | σ² | "Bell curve", CLT limit |

### Probability Rules Quick Reference

| Rule | Formula |
|------|---------|
| Complement | P(A') = 1 − P(A) |
| Addition (general) | P(A∪B) = P(A) + P(B) − P(A∩B) |
| Addition (mutually exclusive) | P(A∪B) = P(A) + P(B) |
| Multiplication (general) | P(A∩B) = P(A) · P(B\|A) |
| Multiplication (independent) | P(A∩B) = P(A) · P(B) |
| Conditional | P(A\|B) = P(A∩B) / P(B) |
| Bayes' theorem | P(A\|B) = P(B\|A) · P(A) / P(B) |

### The 68-95-99.7 Rule

```
          68.3%
       ┌────┴────┐
  ──┬──┤         ├──┬──
    │  μ-σ     μ+σ  │
    │                │
    └── 95.4% ───────┘
    │                │
    └── 99.7% ───────┘
   μ-3σ            μ+3σ
```

| Range | Probability | Meaning |
|-------|------------|---------|
| μ ± 1σ | 68.3% | About 2/3 of data |
| μ ± 2σ | 95.4% | About 19/20 of data |
| μ ± 3σ | 99.7% | Almost all data |
| μ ± 5σ | 99.99994% | CERN discovery threshold |

### Descriptive Statistics Summary

| Statistic | Formula | Sensitive to Outliers? |
|-----------|---------|----------------------|
| Mean | Σxᵢ/n | Yes |
| Median | Middle value when sorted | No |
| Mode | Most frequent value | No |
| Variance | Σ(xᵢ−x̄)²/(n−1) | Yes |
| Std Dev | √variance | Yes |
| Range | max − min | Very |
| IQR | Q3 − Q1 | No |

---

## Time Estimates

- Lecture (Parts 1-6): 110 min
- Worked examples and demos: 20 min
- Practice problems: 10 min
- Q&A: 10 min
- **Total**: ~150 min

---

## Resources for Students

- [3Blue1Brown — Bayes' theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM) (excellent visual explanation)
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive probability visualisations
- Glen Cowan, *Statistical Data Analysis* (Chapters 1-5)
- [Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)
- [CERN 5-sigma explainer](https://www.symmetrymagazine.org/article/five-sigma)

---

## Assessment Ideas

- **Quiz**: "A medical test has 99% sensitivity and 95% specificity. If 1% of the population has the disease, what's the probability a positive test is correct?" (Bayes' theorem)
- **Computation**: "Given this dataset, compute mean, median, std dev, and 95% CI for the mean"
- **Distribution identification**: "Classify these 5 scenarios by distribution type"
- **Conceptual**: "Explain in your own words what the Central Limit Theorem says and why it matters for data analysis"
- **Python exercise**: "Generate 1000 samples from a Poisson distribution, plot the histogram, overlay the theoretical PMF"
