---
background: /figures/background_intro.jpg
class: text-left
colorSchema: dark
theme: ./theme
drawings:
  persist: false
transition: fade
title: "Real Data & Case Studies"
layout: cover
addons:
  - slidev-addon-python-runner
python:
  installs: ["numpy", "pandas", "matplotlib", "scipy"]
  prelude: |
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    import warnings
    warnings.filterwarnings('ignore')
  loadPackagesFromImports: true
  suppressDeprecationWarnings: true
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Real Data & Case Studies

---
layout: quote
hideInToc: true
---

# Synthetic data teaches you tools. Real data teaches you **judgment**. The gap between them is where data analysis truly begins.

---
hideInToc: true
---

# Motivation

<div class="card card-info pad-tight mt-md">

## 🌍 **From Textbook to Reality**

So far we've worked with clean, synthetic data. Real-world data is different:
- **Messy**: missing values, outliers, inconsistent formats
- **Large**: millions of rows, multiple files, various formats
- **Contextual**: you need domain knowledge to interpret it
- **Imperfect**: no ground truth, uncertain measurements

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

### 🎯 **This Lecture**
- Apply NumPy, Pandas, stats, and fitting to realistic scenarios
- Work through complete analysis workflows
- Practice the judgment calls real data demands

</div>

<div class="card card-secondary pad-tight">

### 🔧 **Skills You'll Use**
- Everything from L5 (Python), L6 (NumPy/Pandas/matplotlib)
- L9 (probability & statistics)
- L10 (data fitting)

</div>

</div>

---
layout: section
hideInToc: true
---

# Case Study 1: **Higgs** to Two Photons

---
hideInToc: true
---

# Example: Higgs to Two Photons Analysis

<div class="card card-info pad-tight mt-md">

## 📋 **Realistic Scenario**

You have data from a particle physics experiment looking for Higgs → γγ (two photons). Each event has:
- Two photon energies and directions
- Invariant mass (m<sub>γγ</sub>)
- Detector information
- Event quality flags

**Goal**: Identify Higgs signal around 125 GeV

</div>

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
n_sig, n_bkg = 300, 2000

signal_df = pd.DataFrame({'mass': np.random.normal(125, 1.5, n_sig), 'type': 'signal'})
background_df = pd.DataFrame({'mass': np.random.exponential(30, n_bkg) + 105, 'type': 'background'})

df = pd.concat([signal_df, background_df], ignore_index=True)
df = df[df['mass'] < 150]
print(f"Total events: {len(df)} (Signal: {n_sig}, Background: {n_bkg})")
print(df.head())
```

---
hideInToc: true
---

# Exploratory Data Analysis: Statistics

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]

print("Summary statistics by type:")
print(df.groupby('type')['mass'].describe())

print(f"\nEvents near Higgs mass (124-126 GeV): {len(df[(df['mass']>124) & (df['mass']<126)])}")
```

---
hideInToc: true
---

# Exploratory Data Analysis: Visualization

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
signal = pd.DataFrame({'mass': np.random.normal(125, 1.5, 300), 'type': 'signal'})
background = pd.DataFrame({'mass': np.random.exponential(30, 2000) + 105, 'type': 'background'})
df = pd.concat([signal, background], ignore_index=True)
df = df[df['mass'] < 150]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.hist(df['mass'], bins=50, range=(105, 150), edgecolor='white', alpha=0.7)
ax1.axvline(125, color='red', linestyle='--', label='Higgs mass')
ax1.set_xlabel('m$_{γγ}$ (GeV)'); ax1.set_ylabel('Events'); ax1.legend()

ax2.hist(df[df['type']=='background']['mass'], bins=50, range=(105,150), alpha=0.5, label='Bkg')
ax2.hist(df[df['type']=='signal']['mass'], bins=50, range=(105,150), alpha=0.7, label='Signal')
ax2.set_xlabel('m$_{γγ}$ (GeV)'); ax2.set_ylabel('Events'); ax2.legend()
plt.tight_layout()
plt.show()
```

---
hideInToc: true
---

# Data Filtering: Quality Cuts

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'mass': np.concatenate([np.random.normal(125, 1.5, 300),
                            np.random.exponential(30, 2000) + 105]),
    'photon1_E': np.random.uniform(40, 110, 2300),
    'photon2_E': np.random.uniform(35, 100, 2300),
    'detector_qual': np.random.choice(['good', 'bad'], 2300, p=[0.9, 0.1])
})
df = df[df['mass'] < 150]
print(f"Events before cuts: {len(df)}")

# Quality cut
df_qual = df[df['detector_qual'] == 'good']
print(f"After quality cut:  {len(df_qual)}")

# Energy cuts
df_cut = df_qual[(df_qual['photon1_E'] > 50) & (df_qual['photon2_E'] > 45)]
print(f"After energy cuts:  {len(df_cut)}")
```

---
hideInToc: true
---

# Data Filtering: Signal Region

```py {monaco-run}
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'mass': np.concatenate([np.random.normal(125, 1.5, 300),
                            np.random.exponential(30, 2000) + 105]),
    'photon1_E': np.random.uniform(40, 110, 2300),
    'photon2_E': np.random.uniform(35, 100, 2300),
    'detector_qual': np.random.choice(['good', 'bad'], 2300, p=[0.9, 0.1])
})
df = df[(df['mass'] < 150) & (df['detector_qual'] == 'good')]
df = df[(df['photon1_E'] > 50) & (df['photon2_E'] > 45)]

# Signal region (mass window around Higgs)
signal_region = df[(df['mass'] > 122) & (df['mass'] < 128)]
print(f"Events in signal region (122-128 GeV): {len(signal_region)}")

# Sideband regions (for background estimation)
sideband_low = df[(df['mass'] > 110) & (df['mass'] < 120)]
sideband_high = df[(df['mass'] > 130) & (df['mass'] < 140)]
print(f"Sideband events: {len(sideband_low) + len(sideband_high)}")
print(f"\nSignal region statistics:\n{signal_region['mass'].describe()}")
```

---
hideInToc: true
---

# Case Study 1: What We Practiced

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📋 **Analysis Steps**
1. Generated realistic signal + background data
2. Explored with `.describe()` and `.groupby()`
3. Visualized total and separated distributions
4. Applied quality cuts (detector, energy thresholds)
5. Defined signal region and sidebands

</div>

<div class="card card-secondary pad-tight">

## 💡 **Key Lessons**
- Always **visualize before cutting**
- Quality cuts reduce data but improve signal-to-noise
- **Sidebands** help estimate background in the signal region
- Real analyses at CERN follow exactly this workflow

</div>

</div>

---
layout: section
hideInToc: true
---

# Case Study 2: **Dimuon** Mass Spectrum

---
hideInToc: true
---

# CERN Open Data Portal

<div class="card card-accent pad-tight mt-md">

## 🌐 **Explore Real Particle Physics Data**

CERN provides open access to real experimental data from LHC experiments!

**URL**: [http://opendata.cern.ch](http://opendata.cern.ch)

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

### 📚 **Available Datasets**

- **CMS**: Proton-proton collisions (7, 8, 13 TeV)
- **ATLAS**: Limited open data releases
- **ALICE**: Heavy-ion collisions
- **LHCb**: B-physics data

Formats: CSV, ROOT, HDF5

</div>

<div class="card card-secondary pad-tight">

### 📈 **Example Analyses**

- Higgs → ZZ → 4 leptons
- W/Z boson production
- Top quark pair production
- Dimuon mass spectrum
- Jet physics

Full tutorials and documentation provided!

</div>

</div>

<div class="card card-info pad-tight mt-md">

**Your next step**: Download a real dataset and apply NumPy/Pandas skills! Example: Dimuon spectrum showing J/ψ, Υ resonances

</div>

---
hideInToc: true
---

# Example: CMS Dimuon Spectrum — Data

```py {monaco-run}
import pandas as pd
import numpy as np

# Simulated CMS dimuon data (real data: http://opendata.cern.ch/record/5200)
np.random.seed(42)
jpsi = np.random.normal(3.1, 0.1, 500)       # J/ψ peak (~3.1 GeV)
upsilon = np.random.normal(9.5, 0.2, 200)     # Υ peak (~9.5 GeV)
background = np.random.exponential(2.0, 2000)  # Continuum background

mass = np.concatenate([jpsi, upsilon, background])
df = pd.DataFrame({'dimuon_mass': mass[mass < 15]})

print(f"Total events: {len(df)}")
print(f"J/ψ region (2.8-3.4 GeV):    {len(df[(df['dimuon_mass']>2.8) & (df['dimuon_mass']<3.4)])}")
print(f"Υ region (9.0-10.5 GeV):     {len(df[(df['dimuon_mass']>9) & (df['dimuon_mass']<10.5)])}")
```

---
hideInToc: true
---

# Example: CMS Dimuon Spectrum — Plot

```py {monaco-run}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
jpsi = np.random.normal(3.1, 0.1, 500)
upsilon = np.random.normal(9.5, 0.2, 200)
background = np.random.exponential(2.0, 2000)
mass = np.concatenate([jpsi, upsilon, background])
df = pd.DataFrame({'dimuon_mass': mass[mass < 15]})

plt.figure(figsize=(10, 5))
plt.hist(df['dimuon_mass'], bins=100, range=(0, 15), edgecolor='white', linewidth=0.3)
plt.xlabel('Dimuon Mass (GeV/c²)', fontsize=12)
plt.ylabel('Events', fontsize=12)
plt.title('Dimuon Mass Spectrum (simulated CMS data)', fontsize=14)
plt.axvline(3.1, color='red', ls='--', label='J/ψ (3.1 GeV)', lw=1.5)
plt.axvline(9.5, color='green', ls='--', label='Υ (9.5 GeV)', lw=1.5)
plt.legend(); plt.grid(alpha=0.3); plt.yscale('log')
plt.tight_layout(); plt.show()
```

---
hideInToc: true
---

# Dimuon Analysis: Fitting a Peak

```py {monaco-run}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

np.random.seed(42)
jpsi = np.random.normal(3.1, 0.08, 500)
background = np.random.exponential(1.5, 2000)
mass = np.concatenate([jpsi, background])
mass = mass[(mass > 2.0) & (mass < 5.0)]

# Histogram the data
counts, bin_edges = np.histogram(mass, bins=60, range=(2.0, 5.0))
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
errors = np.sqrt(np.maximum(counts, 1))

# Fit: Gaussian signal + exponential background
def model(x, A, mu, sigma, N, lam):
    return A * np.exp(-0.5*((x-mu)/sigma)**2) + N * np.exp(-lam*x)

p0 = [80, 3.1, 0.1, 200, 0.5]
popt, pcov = curve_fit(model, bin_centers, counts, p0=p0, sigma=errors)
perr = np.sqrt(np.diag(pcov))

plt.figure(figsize=(10, 5))
plt.errorbar(bin_centers, counts, yerr=errors, fmt='ko', markersize=3, label='Data')
x_fit = np.linspace(2.0, 5.0, 200)
plt.plot(x_fit, model(x_fit, *popt), 'r-', linewidth=2, label='Fit (Gaussian + exp)')
plt.xlabel('Dimuon Mass (GeV/c²)')
plt.ylabel('Events')
plt.title(f'J/ψ Peak: mass = {popt[1]:.3f} ± {perr[1]:.3f} GeV')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---
layout: section
hideInToc: true
---

# Case Study 3: End-to-End **Workflow**

---
hideInToc: true
---

# Building a Complete Analysis

<div class="card card-info pad-tight mt-md">

## 🔄 **The Full Pipeline**

Every real analysis follows the same pattern — regardless of field:

</div>

<div class="stack-tight mt-md">

<div class="card card-primary pad-compact">

📥 **1. Load** — Read data from files, APIs, or databases

</div>

<div class="card card-secondary pad-compact">

🧹 **2. Clean** — Handle missing values, fix types, remove duplicates

</div>

<div class="card card-accent pad-compact">

🔍 **3. Explore** — Summary statistics, distributions, correlations

</div>

<div class="card card-info pad-compact">

📊 **4. Visualize** — Histograms, scatter plots, time series

</div>

<div class="card card-success pad-compact">

🧪 **5. Analyze** — Fit models, test hypotheses, quantify uncertainty

</div>

<div class="card card-warning pad-compact">

📢 **6. Communicate** — Clear plots, reproducible code, written summary

</div>

</div>

---
hideInToc: true
---

# Try It: Complete Pipeline

```py {monaco-run}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD: Simulate a "messy" dataset
np.random.seed(42)
n = 200
df = pd.DataFrame({
    'time': np.arange(n),
    'temperature': 20 + 0.05*np.arange(n) + np.random.normal(0, 1.5, n),
    'humidity': 60 - 0.02*np.arange(n) + np.random.normal(0, 3, n),
    'sensor': np.random.choice(['A', 'B', 'C'], n)
})
# Inject some NaN values (realistic!)
df.loc[np.random.choice(n, 10, replace=False), 'temperature'] = np.nan

# 2. CLEAN
print(f"Missing values:\n{df.isnull().sum()}\n")
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())

# 3. EXPLORE
print("Summary by sensor:")
print(df.groupby('sensor')[['temperature', 'humidity']].agg(['mean', 'std']).round(2))

# 4. VISUALIZE
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for sensor in ['A', 'B', 'C']:
    mask = df['sensor'] == sensor
    axes[0].scatter(df[mask]['time'], df[mask]['temperature'], alpha=0.5, s=10, label=sensor)
axes[0].set_xlabel('Time'); axes[0].set_ylabel('Temperature (°C)')
axes[0].set_title('Temperature Over Time'); axes[0].legend()

df['temperature'].hist(bins=25, ax=axes[1], edgecolor='white', alpha=0.7)
axes[1].set_xlabel('Temperature (°C)'); axes[1].set_ylabel('Count')
axes[1].set_title('Temperature Distribution')
plt.tight_layout(); plt.show()
```

---
layout: section
hideInToc: true
---

# Lessons **Learned**

---
hideInToc: true
---

# Real Data vs Textbook Data

<div class="grid-2 mt-md gap-md">

<div class="card card-warning pad-tight">

## ⚠️ **Textbook Data**
- Clean, no missing values
- Known distributions
- Clear signal
- Small datasets
- Perfect error bars

</div>

<div class="card card-success pad-tight">

## 🌍 **Real Data**
- Missing values, outliers
- Unknown distributions
- Signal buried in noise
- Large, multi-file datasets
- Uncertain uncertainties

</div>

</div>

<div class="card card-info pad-tight mt-md">

## 💡 **The Bridge**

The techniques are the same — fitting, statistics, visualization. What changes is the **judgment**: which outliers to keep, how to handle missing data, what model to choose. That judgment comes from **practice**.

</div>

---
hideInToc: true
---

# Key Takeaways

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🎯 **Analysis Workflow**

✅ Always start with exploration and visualization

✅ Clean data systematically, document every step

✅ Validate results with residuals and chi-squared

✅ Report uncertainties — a number without an error bar is incomplete

</div>

<div class="card card-secondary pad-tight">

## 🔗 **Connecting the Course**

- **L5**: Python gave you the language
- **L6**: NumPy/Pandas/matplotlib gave you the tools
- **L9**: Statistics gave you the theory
- **L10**: Fitting gave you the methods
- **This lecture**: Real data gave you the practice
- **L12**: Reproducibility ties it all together

</div>

</div>

---
hideInToc: true
layout: quote
---

# The best way to learn data analysis is to **do** data analysis. Take a real dataset — from CERN Open Data, your field, or your life — and run the full pipeline. You now have every tool you need.

---
hideInToc: true
layout: end
---

# Questions?

## Next lecture: **Reproducible Workflows & Automation**
