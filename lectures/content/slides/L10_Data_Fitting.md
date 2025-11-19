---
mermaid: true
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Data Fitting"
layout: cover

addons:
  - slidev-addon-python-runner

python:
  installs: ["numpy", "matplotlib", "scipy"]
  prelude: |
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    import warnings
    warnings.filterwarnings('ignore')
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Data Fitting

---
hideInToc: true
layout: quote
---

# Data fitting is how we extract quantitative knowledge from measurements—turning noisy observations into precise parameter estimates with well-understood uncertainties.

---
layout: section
hideInToc: true
---

# What is **Data Fitting?**

---
hideInToc: true
---

# The Fundamental Problem

<div class="card card-info pad-tight mt-md">

## **Definition**

**Data fitting** is the process of finding parameter values $\theta$ such that a model $f(x; \theta)$ best describes observed data $(x_i, y_i)$.

$$\text{Data} \xrightarrow{\text{fitting}} \text{Parameter estimates } \hat{\theta} \pm \text{uncertainties}$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **What we have**

- Measurements $(x_i, y_i)$ with uncertainties
- A theoretical model $f(x; \theta)$
- Prior knowledge about subject

</div>

<div class="card card-secondary pad-tight">

## **What we want**

- Best-fit parameter values $\hat{\theta}$
- Uncertainties on parameters
- Assessment of fit quality
- Confidence in our model

</div>

</div>

---
hideInToc: true
---

# The Data Fitting Workflow

```mermaid {scale: 0.9}
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#0f1f3d', 'primaryBorderColor': '#60a5fa', 'primaryTextColor': '#e2e8f0', 'secondaryColor': '#102b4c', 'lineColor': '#5eead4', 'fontFamily': 'Inter, system-ui, sans-serif'}, 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'useMaxWidth': true, 'nodeSpacing': 40, 'rankSpacing': 45}}}%%
flowchart LR
    Data["📊 Data<br/>(xᵢ, yᵢ)"]:::input --> Model["📐 Model<br/>f(x; θ)"]:::process
    Model --> Fit["⚙️ Fit<br/>minimize χ²"]:::process
    Fit --> Params["🎯 Parameters<br/>θ̂ ± σ"]:::output
    Params --> Validate["✓ Validate<br/>residuals, χ²/dof"]:::check
    Validate -->|Good| Report["📝 Report"]:::output
    Validate -->|Bad| Model

    classDef input fill:#133661,stroke:#5eead4,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef process fill:#0f4c81,stroke:#93c5fd,stroke-width:2px,color:#e2e8f0,rx:12px,ry:12px
    classDef output fill:#155e75,stroke:#5eead4,stroke-width:2.5px,color:#e0f2fe,rx:14px,ry:14px
    classDef check fill:#0b2540,stroke:#fcd34d,stroke-width:2px,color:#fef3c7,rx:12px,ry:12px
```

<div class="card card-accent pad-tight mt-md">

**Key insight**: Fitting is iterative. If diagnostics reveal problems, refine the model and repeat.

</div>

---
layout: section
hideInToc: true
---

# Mathematical **Models**

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **Definition**

A **mathematical model** is a function $f(x; \theta)$ that describes the relationship between independent variable(s) $x$ and dependent variable $y$:

$$y = f(x; \theta) + \varepsilon$$

where $\varepsilon$ represents random measurement errors.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Components**

- **Functional form**: theory-motivated shape
- **Parameters $\theta$**: unknown quantities to estimate
- **Error term $\varepsilon$**: accounts for noise/uncertainty

</div>

<div class="card card-secondary pad-tight">

## **Examples**

- Linear: $y = mx + b$
- Exponential decay: $y = A e^{-\lambda t}$
- Gaussian peak: $y = A e^{-(x-\mu)^2/2\sigma^2}$
- Polynomial: $y = \sum a_n x^n$

</div>

</div>

---
hideInToc: true
---

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### 📐 **Mechanistic**

Based on physical principles

- First-principles derivation
- Parameters have physical meaning
- Preferred in physics

**Example**: Decay rate from quantum mechanics

</div>

<div class="card card-secondary pad-tight">

### 📈 **Empirical**

Based on observed patterns

- Data-driven functional form
- May lack physical interpretation
- Useful for interpolation

**Example**: Polynomial fit to calibration data

</div>

<div class="card card-info pad-tight">

### 🔀 **Hybrid**

Combines both approaches

- Physical model + corrections
- Systematic effects modeled empirically
- Common in practice

**Example**: Signal (Gaussian) + background (empirical)

</div>

</div>

<div class="card card-warning pad-tight mt-md">

**Important**: The choice of model should be guided by knowledge of the subject, not just by what fits best. A good fit with a wrong model gives wrong answers!

</div>

---
hideInToc: true
---

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **What parameters represent**

Parameters $\theta$ are the unknowns we want to determine:

- **Physical quantities**: mass, lifetime, cross-section
- **Shape descriptors**: width, amplitude, position
- **Nuisance parameters**: background level, resolution

Each parameter has:
- A true (unknown) value
- An estimated value $\hat{\theta}$
- An uncertainty $\sigma_{\hat{\theta}}$

</div>

<div class="card card-accent pad-tight">

## **Example: Gaussian + Exponential**

$$f(x) = A \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}} + N \cdot e^{-x/\lambda}$$

| Parameter | Meaning |
|-----------|---------|
| $A$ | Signal amplitude |
| $\mu$ | Signal position (mass) |
| $\sigma$ | Signal width (resolution) |
| $N$ | Background normalization |
| $\lambda$ | Background decay scale |

</div>

</div>

---
layout: section
hideInToc: true
---

# Parameter **Estimation**

---
hideInToc: true
---

# The Estimation Problem

<div class="card card-info pad-tight mt-md">

## **Goal**

Given data and a model, find the parameter values $\hat{\theta}$ that make the model best describe the data.

"Best" means: **maximize agreement** between model predictions and observations.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **The Challenge**

- Data contains random noise
- Multiple parameter combinations might seem plausible
- Need principled way to choose "best"
- Must quantify uncertainty in our estimates

</div>

<div class="card card-secondary pad-tight">

## **Solution: Optimization**

Define a **cost function** measuring disagreement:

$$\text{Cost}(\theta) = \text{how bad is this } \theta?$$

Then minimize it:

$$\hat{\theta} = \arg\min_\theta \text{Cost}(\theta)$$

</div>

</div>

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **Sum of Squared Residuals**

The most common approach: minimize the sum of squared differences between data and model:

$$S(\theta) = \sum_{i=1}^{n} \left[ y_i - f(x_i; \theta) \right]^2$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Intuition**

- Residual $r_i = y_i - f(x_i; \theta)$
- Squaring removes sign (positive/negative equally bad)
- Large errors penalized more heavily
- Leads to smooth optimization landscape

</div>

<div class="card card-accent pad-tight">

## **Connection to MLE**

If errors are Gaussian:
$$\varepsilon_i \sim N(0, \sigma^2)$$

Then **least squares = maximum likelihood**

This is why least squares is so widely used.

</div>

</div>

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **Weighted Least Squares**

If data points have different uncertainties $\sigma_i$, weight them accordingly:

$$\chi^2(\theta) = \sum_{i=1}^{n} \frac{\left[ y_i - f(x_i; \theta) \right]^2}{\sigma_i^2}$$

Points with smaller uncertainties contribute more to the fit.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Physical interpretation**

- $\sigma_i$ = uncertainty on point $i$
- Precise measurements ($\sigma_i$ small) → large weight
- Imprecise measurements → small weight
- This is the **chi-squared statistic**

</div>

<div class="card card-warning pad-tight">

## **Common case: Poisson data**

For histogram bin counts $n_i$:

$$\sigma_i = \sqrt{n_i}$$

</div>

</div>

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">

## **The Covariance Matrix**

The fit produces not just $\hat{\theta}$ but also the **covariance matrix** $\mathbf{C}$:

$$C_{ij} = \text{Cov}(\hat{\theta}_i, \hat{\theta}_j)$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Diagonal elements**

$$C_{ii} = \text{Var}(\hat{\theta}_i) = \sigma_i^2$$

**Parameter uncertainties:**

$$\sigma_i = \sqrt{C_{ii}}$$

Report results as: $\hat{\theta}_i \pm \sigma_i$

</div>

<div class="card card-secondary pad-tight">

## **Off-diagonal elements**

$$C_{ij} = \text{Cov}(\hat{\theta}_i, \hat{\theta}_j)$$

**Correlations between parameters:**

$$\rho_{ij} = \frac{C_{ij}}{\sigma_i \sigma_j}$$

Important for error propagation!

</div>

</div>

---
hideInToc: true
layout: image
image: /covariance_matrix_1.png
backgroundSize: contain
---

---
hideInToc: true
layout: image
image: /covariance_matrix_2.png
backgroundSize: contain
---

---
hideInToc: true
---

<div class="card card-info pad-tight mt-md">


`scipy.optimize.curve_fit` performs nonlinear least squares fitting:

```python
popt, pcov = curve_fit(model, x_data, y_data, p0=initial_guess)
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Inputs**

- `model`: function $f(x, \theta_1, \theta_2, ...)$
- `x_data`, `y_data`: your measurements
- `p0`: initial parameter guess
- `sigma`: uncertainties (optional)
- `bounds`: parameter limits (optional)

</div>

<div class="card card-secondary pad-tight">

## **Outputs**

- `popt`: optimal parameters $\hat{\theta}$
- `pcov`: covariance matrix

**Uncertainties:**
```python
errors = np.sqrt(np.diag(pcov))
```

</div>

</div>

<div class="card card-accent pad-tight mt-md">

Under the hood: uses Levenberg-Marquardt algorithm—a hybrid of gradient descent and Gauss-Newton methods.

</div>

---
hideInToc: true
---

<div class="card card-warning pad-tight mt-md">

## **The Local Minimum Problem**

Nonlinear fitting is an optimization problem. Poor initial guesses can lead to:

- Convergence to **local** (not global) minimum
- Fit failure or nonsensical results
- Very slow convergence

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Good practice**

1. **Visualize data first**
2. Estimate parameters by eye
3. Use physical constraints
4. Try multiple starting points

</div>

<div class="card card-info pad-tight">

For a Gaussian peak:
- `mean` ≈ position of maximum
- `sigma` ≈ half-width at half-max
- `amplitude` ≈ peak height

</div>

</div>

---
hideInToc: true
---

# Constraining Parameters

<div class="card card-info pad-tight mt-md">

## **Physical Constraints**

Real parameters often have physical bounds (e.g., $\sigma > 0$, mass positive):

```python
bounds = (
    [0, 0, 0.01, 0, 0.1],      # Lower bounds
    [np.inf, 15, 5, np.inf, 10]  # Upper bounds
)
popt, pcov = curve_fit(model, x, y, p0=p0, bounds=bounds)
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Benefits**

- Prevents unphysical solutions
- Can speed up convergence
- Incorporates prior knowledge

</div>

<div class="card card-warning pad-tight">

## **Caution**

- If optimal is at boundary → may indicate model problems
- Very tight bounds can bias results
- Check if bounds are affecting your fit

</div>

</div>

---
hideInToc: true
---

# Residual Analysis

<div class="card card-info pad-tight mt-md">

## **Definition**

**Residual** = observed − predicted: $r_i = y_i - f(x_i; \hat{\theta})$

Residuals reveal how well the model captures the data structure.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success pad-tight">

## ✅ **Good Fit**

- Randomly scattered around zero
- No visible patterns or trends
- Approximately Gaussian distributed
- Size consistent with uncertainties

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Problems Indicated**

- **Trends**: model missing structure
- **Outliers**: bad data or wrong model
- **Heteroscedasticity**: uncertainty varies
- **Periodicity**: missing periodic component

</div>

</div>

---
hideInToc: true
---

# Standardized Residuals

<div class="card card-info pad-tight mt-md">

## **Pull Distribution**

Standardize residuals by their uncertainties:

$$\text{pull}_i = \frac{y_i - f(x_i; \hat{\theta})}{\sigma_i}$$

If model is correct and uncertainties accurate: pulls ~ $N(0, 1)$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### **Mean**
Should be ≈ 0

Non-zero → systematic bias

</div>

<div class="card card-secondary pad-tight">

### **Width**
Should be ≈ 1

> 1 → underestimated errors
< 1 → overestimated errors

</div>

<div class="card card-accent pad-tight">

### **Shape**
Should be Gaussian

Non-Gaussian → model problems

</div>

</div>

---
hideInToc: true
---

# Visualizing Fit Quality

<div class="card card-info pad-tight mt-md">

## **Standard Plot Structure**

A complete fit visualization includes:

1. **Upper panel**: Data with error bars + fitted model + components
2. **Lower panel**: Residuals or pulls

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **What to include**

- Data points with error bars
- Total fit (solid line)
- Individual components (dashed)
- Clear legend and labels
- Axis labels with units

</div>

<div class="card card-secondary pad-tight">

## **Residual panel**

- Same x-axis as main plot
- Zero line clearly marked
- Error bars on residuals
- Smaller height (ratio ~3:1)

**Alternative**: Show pulls instead

</div>

</div>

---
layout: section
hideInToc: true
---

# Goodness-of-Fit: **χ²**

---
hideInToc: true
---

# The Chi-Squared Statistic

<div class="card card-info pad-tight mt-md">

## **Definition**

$$\chi^2 = \sum_{i=1}^{n} \frac{(y_i - f(x_i; \hat{\theta}))^2}{\sigma_i^2}$$

Sum of squared standardized residuals—measures total disagreement weighted by uncertainties.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Properties**

- $\chi^2 \geq 0$ always
- Smaller = better fit
- Expectation: $E[\chi^2] \approx \text{dof}$
- Distribution is known (for testing)

</div>

<div class="card card-secondary pad-tight">

## **Degrees of Freedom**

$$\text{dof} = n - p$$

- $n$ = number of data points
- $p$ = number of fitted parameters

Accounts for "freedom used up" by fitting.

</div>

</div>

---
hideInToc: true
---

# Reduced Chi-Squared

<div class="card card-info pad-tight mt-md">

## **The Key Diagnostic**

$$\chi^2_\nu = \frac{\chi^2}{\text{dof}} = \frac{\chi^2}{n - p}$$

The reduced chi-squared should be **approximately 1** for a good fit.

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-success pad-tight">

### ✅ **χ²/dof ≈ 1**

Good fit

Model describes data well, uncertainties are correct

</div>

<div class="card card-warning pad-tight">

### ⚠️ **χ²/dof >> 1**

Poor fit

Model missing structure, or uncertainties underestimated

</div>

<div class="card card-accent pad-tight">

### 🔍 **χ²/dof << 1**

Suspicious

Uncertainties overestimated, or too many parameters

</div>

</div>

---
hideInToc: true
---

# Interpreting χ² Results

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **When χ²/dof is large**

Possible causes:
1. Wrong model (missing terms)
2. Systematic effects not included
3. Uncertainties too small
4. Outliers in data

**Action**: Check residuals for patterns, reconsider model

</div>

<div class="card card-secondary pad-tight">

## **When χ²/dof is small**

Possible causes:
1. Uncertainties overestimated
2. Too many free parameters
3. Fitting noise (overfitting)

**Action**: Review uncertainty estimation, simplify model

</div>

</div>

<div class="card card-warning pad-tight mt-md">

**Important**: χ² alone doesn't tell you the model is correct—only that residuals are consistent with assumed uncertainties. Always combine with visual inspection!

</div>

---
hideInToc: true
---

# p-value from χ²

<div class="card card-info pad-tight mt-md">

## **Statistical Test**

The p-value answers: "If the model is correct, what's the probability of getting a χ² this large or larger?"

$$p = P(\chi^2 > \chi^2_{\text{obs}} \mid H_0)$$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Interpretation**

- $p > 0.05$: no evidence against model
- $p < 0.05$: model may be inadequate
- $p \ll 0.001$: strong evidence of misfit

**But**: p-values are often misinterpreted. Focus on χ²/dof and residuals.

</div>

<div class="card card-accent pad-tight">

## **Calculation**

```python
from scipy.stats import chi2

p_value = 1 - chi2.cdf(chi_squared, dof)
# or equivalently:
p_value = chi2.sf(chi_squared, dof)
```

</div>

</div>

---
layout: section
hideInToc: true
---

# Common **Issues**

---
hideInToc: true
---

# When Fits Go Wrong

<div class="grid-2 mt-md gap-md">

<div class="card card-warning pad-tight">

## **Convergence Failure**

Fit doesn't converge or gives errors

**Causes:**
- Poor initial guess
- Model incompatible with data
- Numerical issues (overflow, divide by zero)

**Solutions:**
- Better starting point
- Check model at p0 visually
- Add parameter bounds

</div>

<div class="card card-warning pad-tight">

## **Unreasonable Results**

Parameters have wrong sign or magnitude

**Causes:**
- Local minimum
- Correlated parameters
- Wrong model functional form

**Solutions:**
- Multiple starting points
- Reparameterize model
- Simplify or change model

</div>

</div>

---
hideInToc: true
---

# Common Pitfalls

<div class="grid-2 mt-md gap-md" style="margin-top: 0;">

<div class="stack-tight">

<div class="card card-warning pad-tight">

## ⚠️ **Empty Bins**

**Problem**: $\sigma_i = \sqrt{0}$ → division by zero

**Solution**: Exclude empty bins or use $\sigma_i = 1$

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Overfitting**

**Problem**: Model fits noise, not signal

**Solution**: Use simplest model that explains data

</div>

</div>

<div class="stack-tight">

<div class="card card-warning pad-tight">

## ⚠️ **Ignoring Correlations**

**Problem**: Parameters often correlated

**Solution**: Use full covariance for error propagation

</div>

<div class="card card-warning pad-tight">

## ⚠️ **Extrapolation**

**Problem**: Model unreliable outside data range

**Solution**: Only predict within fitted domain

</div>

</div>

</div>

---
hideInToc: true
---

# Model Comparison

<div class="card card-info pad-tight mt-md">

## **Which Model is Better?**

When comparing nested models (e.g., with/without a component), use:

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Likelihood Ratio Test**

$$\Delta \chi^2 = \chi^2_{\text{simple}} - \chi^2_{\text{complex}}$$

Compare to χ² distribution with Δdof degrees of freedom.

Large $\Delta \chi^2$ → complex model significantly better

</div>

<div class="card card-secondary pad-tight">

## **Information Criteria**

**AIC**: $2p - 2\ln(L)$

**BIC**: $p\ln(n) - 2\ln(L)$

Lower is better. Automatically penalize complexity.

</div>

</div>

<div class="card card-accent pad-tight mt-md">

**Occam's razor**: Prefer simpler models unless data strongly favor complexity.

</div>

---
layout: section
hideInToc: true
---

# Best **Practices**

---
hideInToc: true
---

# The Complete Workflow

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Before Fitting**

1. **Visualize data** - look for patterns, outliers
2. **Choose model** - based on physics, not convenience
3. **Estimate parameters** - reasonable starting point
4. **Define uncertainties** - how precise are measurements?

</div>

<div class="card card-secondary pad-tight">

## **After Fitting**

1. **Check convergence** - did fit succeed?
2. **Examine residuals** - patterns = problems
3. **Calculate χ²/dof** - is fit quality acceptable?
4. **Report results** - parameters ± uncertainties
5. **Document** - make it reproducible

</div>

</div>

---
hideInToc: true
---

# Do's and Don'ts

<div class="grid-2 mt-md gap-md">

<div class="card card-success pad-tight">

## ✅ **Do**

- Visualize data **before** fitting
- Use physically motivated models
- Report uncertainties with results
- Check residuals for patterns
- Calculate and report χ²/dof
- Document your analysis
- Use multiple starting points

</div>

<div class="card card-warning pad-tight">

## ❌ **Don't**

- Fit without looking at data
- Use arbitrary functional forms
- Report parameters without uncertainties
- Skip residual analysis
- Cherry-pick "good" fits
- Overfit with too many parameters
- Extrapolate far beyond data range

</div>

</div>

---
layout: section
hideInToc: true
---

# Real-World **Applications**

---
hideInToc: true
---

# Example: Higgs Boson Discovery

<div class="card card-accent pad-tight mt-md">

## **CERN 2012: Same Techniques!**

The Higgs boson was discovered using exactly these fitting methods.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **The Analysis**

1. Data: millions of LHC collisions
2. Signal: Higgs → γγ (two photons)
3. Background: smooth combinatorics
4. Model: Gaussian + polynomial
5. Fit: extract mass and signal yield
6. Result: 5σ significance at ~125 GeV

</div>

<div class="card card-info pad-tight">

## **What They Did**

- χ² minimization (weighted)
- Systematic uncertainty estimation
- Model comparison tests
- Background-only hypothesis tests
- Signal significance calculation

**Same concepts, larger scale!**

</div>

</div>

---
hideInToc: true
---

# Beyond Physics

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### 🧬 **Biology**

- Growth curves
- Enzyme kinetics
- Population dynamics

</div>

<div class="card card-secondary pad-tight">

### 💊 **Medicine**

- Dose-response
- Pharmacokinetics
- Survival analysis

</div>

<div class="card card-info pad-tight">

### 🌍 **Climate**

- Temperature trends
- CO₂ models
- Sea level rise

</div>

<div class="card card-success pad-tight">

### 💰 **Economics**

- Regression models
- Time series
- Demand forecasting

</div>

<div class="card card-accent pad-tight">

### 🏭 **Engineering**

- Calibration
- Signal processing
- Quality control

</div>

<div class="card card-warning pad-tight">

### 🤖 **Machine Learning**

Same principles!
- Cost function = χ²
- Parameters = weights
- Optimization = training

</div>

</div>

---
hideInToc: true
---

# Fitting vs Machine Learning

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## **Traditional Fitting**

- Explicit model: $y = f(x; \theta)$
- Physics-based form
- Few parameters (5-10)
- Interpretable
- Requires domain knowledge

</div>

<div class="card card-secondary pad-tight">

## **Machine Learning**

- Flexible model (neural network)
- Data-driven form
- Many parameters (millions)
- Less interpretable
- Requires lots of data

</div>

</div>

<div class="card card-accent pad-tight mt-md">

**Both are parameter estimation problems.** ML is fitting with very complex, flexible models. Understanding fitting makes you better at ML.

</div>

---
hideInToc: true
---

# Key Takeaways

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

### 📐 **Models**

Mathematical functions with parameters that describe data

Choose based on physics, not just fit quality

</div>

<div class="card card-secondary pad-tight">

### 🎯 **Fitting**

Find parameters that minimize disagreement (χ²)

Get uncertainties from covariance matrix

</div>

<div class="card card-info pad-tight">

### ✓ **Validation**

Always check residuals and χ²/dof

A good fit isn't enough—must make physical sense

</div>

</div>

<div class="card card-accent pad-tight mt-md">

## **The Big Picture**

Fitting connects theory to data. It's how we extract quantitative knowledge from measurements—used everywhere from particle physics to machine learning.

</div>

