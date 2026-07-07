# L12: Practical Data Fitting in Python

---

## Overview

**Duration**: ~120 minutes (2 h slot)

**Prerequisites**: L11 (Probability & Statistics), L7-L8 (Python basics)

**Learning Objectives**:
- Apply MLE and χ² concepts from L11 to real fitting problems
- Use `scipy.optimize.curve_fit` for parameter estimation
- Compute and interpret uncertainties from covariance matrices
- Perform residual analysis and goodness-of-fit tests
- Bridge theory (L11) to practice (real code)

---

## Lecture Structure

### Part 1: Workflow Overview (15 min)
- Recap L11: MLE, least squares, χ² statistic
- Show complete workflow diagram (data → fit → evaluate)
- Emphasize: "L11 was theory, L12 is implementation"
- Interactive: Ask students where they struggled with L11 concepts

### Part 2: Data Generation (15 min)
- Why synthetic data first (known truth, reproducibility)
- Generate Gaussian signal + exponential background
- **Live demo**: Run `1_generator.py` from `misc/python/stable/analysis_example/`
- Discuss random seeds and reproducibility

### Part 3: Model Fitting with scipy (30 min)
- Introduce `curve_fit` and its connection to MLE
- **Live coding**: Step through fitting example
- Show how to define model function
- Discuss initial parameter guesses (common failure point!)
- Extract parameters and uncertainties from covariance matrix

### Part 4: Residuals & Goodness-of-Fit (20 min)
- Calculate and plot residuals
- Interpret χ²/dof values (good fit ≈ 1)
- Common patterns in residuals (systematic deviations = model issues)

### Part 5: Practical Considerations (10 min)
- What to do when fits fail
- Parameter constraints and bounds
- Weighted fitting
- Model comparison

---

## Teaching Tips

### Common Student Struggles

1. **"My fit doesn't converge!"**
   - Check initial guess (plot model with initial parameters first!)
   - Check data range vs model domain
   - Try simpler model first, then add complexity

2. **"What's a good initial guess?"**
   - Visualize data first
   - Use domain knowledge (e.g., peak location ≈ mean)
   - Order of magnitude is usually enough

3. **"How do I interpret the covariance matrix?"**
   - Diagonal = variances (uncertainties squared)
   - Off-diagonal = correlations (often ignored at first)
   - Use `np.sqrt(np.diag(pcov))` for errors

4. **"Is χ²/dof = 1.2 good or bad?"**
   - ≈1 is good, 0.8-1.3 acceptable
   - >>1 suggests underfitting (model too simple)
   - <<1 suggests overestimated errors or overfitting

### Interactive Elements

- **Live coding**: Essential! Walk through fitting example step-by-step
- **Debugging together**: Intentionally break the code, fix it live
- **Parameter exploration**: Change initial guesses, show when it fails
- **Ask students**: "What do you expect this χ²/dof value to tell us?"

### Hands-On Exercises

**Exercise 1** (Easy): Fit simple Gaussian to data
```python
# Generate pure Gaussian data
data = np.random.normal(5, 1, 1000)
# Students fit and extract mean ± error
```

**Exercise 2** (Medium): Modify background model
- Change exponential → polynomial background
- Compare χ²/dof values

**Exercise 3** (Advanced): Real CERN Open Data
- Download dimuon spectrum from opendata.cern.ch
- Fit J/ψ peak (Gaussian) + background

---

## Common Questions & Answers

**Q**: Why use histograms instead of raw data points?
**A**: For large datasets (millions of events), fitting histograms is faster. Also natural for counting experiments (Poisson statistics).

**Q**: When should I use weighted fitting?
**A**: When data points have different uncertainties. For histograms, weights = 1/√counts (Poisson).

**Q**: Can curve_fit fit anything?
**A**: Only works for **linear least squares** problems (linear in parameters). For more complex cases, use `scipy.optimize.minimize`.

**Q**: How do I know if my model is good?
**A**: 1) χ²/dof ≈ 1, 2) Residuals randomly scattered, 3) Physically meaningful parameters, 4) Visual inspection!

---

## Key Code Snippets

### Basic fitting template
```python
from scipy.optimize import curve_fit

def model(x, a, b, c):
    return a * np.exp(-((x - b) / c)**2)

# Fit
popt, pcov = curve_fit(model, x_data, y_data, p0=[1, 0, 1])
errors = np.sqrt(np.diag(pcov))

print(f"Parameter b = {popt[1]:.3f} ± {errors[1]:.3f}")
```

### Chi-squared calculation
```python
fitted = model(x_data, *popt)
residuals = y_data - fitted
chi2 = np.sum((residuals / uncertainties)**2)
dof = len(x_data) - len(popt)
chi2_reduced = chi2 / dof
```

---

## Time Estimates

- Lecture: 60 min
- Live demos: 20 min
- Student exercises: 30 min
- Q&A: 10 min
- **Total**: 120 min

---

## Resources for Students

- [SciPy curve_fit documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- Glen Cowan, *Statistical Data Analysis* (Chapter 7: Parameter Estimation)
- Scripts in `misc/python/stable/analysis_example/`

---

## Assessment Ideas

- **Quiz question**: "What does χ²/dof = 3.5 suggest about your fit?"
- **Practical exam**: "Fit this dataset and report parameters with uncertainties"
- **Project component**: Include fitting in final project with proper uncertainty reporting
