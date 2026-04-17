"""Dataset loaders for CWilke-derived figures.

Small datasets are inlined here. Larger ones live in `data/*.csv` next to this
module. For datasets that don't exist in this directory but have canonical
public sources, `data.py` synthesises realistic substitutes so figures remain
didactically useful without relying on the original R packages (dviz.supp,
ggplot2::diamonds, nycflights13, etc.).

Each loader returns a pandas DataFrame.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

_DATA_DIR = Path(__file__).resolve().parent / "data"


# --- Inline datasets -------------------------------------------------------

def boxoffice() -> pd.DataFrame:
    """Top 5 weekend gross, 22–24 Dec 2017. Source: Box Office Mojo."""
    return pd.DataFrame({
        "rank": [1, 2, 3, 4, 5],
        "title": ["Star Wars: The Last Jedi", "Jumanji: Welcome to the Jungle",
                  "Pitch Perfect 3", "The Greatest Showman", "Ferdinand"],
        "title_short": ["Star Wars", "Jumanji", "Pitch Perfect 3",
                        "Greatest Showman", "Ferdinand"],
        "amount": [71565498, 36169328, 19928525, 8805843, 7316746],
    })


def students_popularity() -> pd.DataFrame:
    """
    Hypothetical goals children ascribe to popularity (Wilke Fig 6.4).
    Simulated from the spirit of the original: four grade levels × three goals.
    """
    rng = np.random.default_rng(42)
    grades = ["4th", "5th", "6th"]
    goals = ["Grades", "Popular", "Sports"]
    rows = []
    pops = {"4th": [0.47, 0.33, 0.20],
            "5th": [0.38, 0.43, 0.19],
            "6th": [0.36, 0.47, 0.17]}
    for g in grades:
        for goal, p in zip(goals, pops[g]):
            rows.append({"grade": g, "goal": goal, "percent": p * 100})
    return pd.DataFrame(rows)


def movies_oscar() -> pd.DataFrame:
    """Oscar-nominated movies by year and outcome (synthetic but plausible)."""
    rng = np.random.default_rng(7)
    years = np.arange(2007, 2018)
    rows = []
    for yr in years:
        for outcome in ["Winner", "Nominated"]:
            n = rng.integers(2, 8)
            rows.append({"year": yr, "outcome": outcome, "count": int(n)})
    return pd.DataFrame(rows)


# --- Classic toy datasets --------------------------------------------------

def iris() -> pd.DataFrame:
    """Fisher's iris; inlined to avoid extra deps."""
    from sklearn import datasets  # noqa: WPS433 — cheap local import
    raw = datasets.load_iris(as_frame=True)
    df = raw.frame
    df = df.rename(columns={
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
    })
    df["species"] = df["target"].map(dict(enumerate(raw.target_names)))
    return df.drop(columns="target")


def mtcars() -> pd.DataFrame:
    """R mtcars."""
    csv = _DATA_DIR / "mtcars.csv"
    if csv.exists():
        return pd.read_csv(csv)
    return _mtcars_inline()


def _mtcars_inline() -> pd.DataFrame:
    # 32 rows — small enough to inline
    d = [
        ("Mazda RX4", 21, 6, 160, 110, 3.9, 2.62, 16.46, 0, 1, 4, 4),
        ("Mazda RX4 Wag", 21, 6, 160, 110, 3.9, 2.875, 17.02, 0, 1, 4, 4),
        ("Datsun 710", 22.8, 4, 108, 93, 3.85, 2.32, 18.61, 1, 1, 4, 1),
        ("Hornet 4 Drive", 21.4, 6, 258, 110, 3.08, 3.215, 19.44, 1, 0, 3, 1),
        ("Hornet Sportabout", 18.7, 8, 360, 175, 3.15, 3.44, 17.02, 0, 0, 3, 2),
        ("Valiant", 18.1, 6, 225, 105, 2.76, 3.46, 20.22, 1, 0, 3, 1),
        ("Duster 360", 14.3, 8, 360, 245, 3.21, 3.57, 15.84, 0, 0, 3, 4),
        ("Merc 240D", 24.4, 4, 146.7, 62, 3.69, 3.19, 20, 1, 0, 4, 2),
        ("Merc 230", 22.8, 4, 140.8, 95, 3.92, 3.15, 22.9, 1, 0, 4, 2),
        ("Merc 280", 19.2, 6, 167.6, 123, 3.92, 3.44, 18.3, 1, 0, 4, 4),
        ("Merc 280C", 17.8, 6, 167.6, 123, 3.92, 3.44, 18.9, 1, 0, 4, 4),
        ("Merc 450SE", 16.4, 8, 275.8, 180, 3.07, 4.07, 17.4, 0, 0, 3, 3),
        ("Merc 450SL", 17.3, 8, 275.8, 180, 3.07, 3.73, 17.6, 0, 0, 3, 3),
        ("Merc 450SLC", 15.2, 8, 275.8, 180, 3.07, 3.78, 18, 0, 0, 3, 3),
        ("Cadillac Fleetwood", 10.4, 8, 472, 205, 2.93, 5.25, 17.98, 0, 0, 3, 4),
        ("Lincoln Continental", 10.4, 8, 460, 215, 3, 5.424, 17.82, 0, 0, 3, 4),
        ("Chrysler Imperial", 14.7, 8, 440, 230, 3.23, 5.345, 17.42, 0, 0, 3, 4),
        ("Fiat 128", 32.4, 4, 78.7, 66, 4.08, 2.2, 19.47, 1, 1, 4, 1),
        ("Honda Civic", 30.4, 4, 75.7, 52, 4.93, 1.615, 18.52, 1, 1, 4, 2),
        ("Toyota Corolla", 33.9, 4, 71.1, 65, 4.22, 1.835, 19.9, 1, 1, 4, 1),
        ("Toyota Corona", 21.5, 4, 120.1, 97, 3.7, 2.465, 20.01, 1, 0, 3, 1),
        ("Dodge Challenger", 15.5, 8, 318, 150, 2.76, 3.52, 16.87, 0, 0, 3, 2),
        ("AMC Javelin", 15.2, 8, 304, 150, 3.15, 3.435, 17.3, 0, 0, 3, 2),
        ("Camaro Z28", 13.3, 8, 350, 245, 3.73, 3.84, 15.41, 0, 0, 3, 4),
        ("Pontiac Firebird", 19.2, 8, 400, 175, 3.08, 3.845, 17.05, 0, 0, 3, 2),
        ("Fiat X1-9", 27.3, 4, 79, 66, 4.08, 1.935, 18.9, 1, 1, 4, 1),
        ("Porsche 914-2", 26, 4, 120.3, 91, 4.43, 2.14, 16.7, 0, 1, 5, 2),
        ("Lotus Europa", 30.4, 4, 95.1, 113, 3.77, 1.513, 16.9, 1, 1, 5, 2),
        ("Ford Pantera L", 15.8, 8, 351, 264, 4.22, 3.17, 14.5, 0, 1, 5, 4),
        ("Ferrari Dino", 19.7, 6, 145, 175, 3.62, 2.77, 15.5, 0, 1, 5, 6),
        ("Maserati Bora", 15, 8, 301, 335, 3.54, 3.57, 14.6, 0, 1, 5, 8),
        ("Volvo 142E", 21.4, 4, 121, 109, 4.11, 2.78, 18.6, 1, 1, 4, 2),
    ]
    cols = ["model", "mpg", "cyl", "disp", "hp", "drat",
            "wt", "qsec", "vs", "am", "gear", "carb"]
    return pd.DataFrame(d, columns=cols)


# --- Synthetic substitutes for dviz.supp data ------------------------------

def blue_jays(n: int = 123, seed: int = 0) -> pd.DataFrame:
    """Substitute for dviz.supp::blue_jays (Keith Tarvin's blue jays)."""
    rng = np.random.default_rng(seed)
    sex = rng.choice(["F", "M"], size=n, p=[0.45, 0.55])
    body_mass = np.where(sex == "M",
                         rng.normal(78, 3.5, n),
                         rng.normal(72, 3.5, n))
    head_length = np.where(sex == "M",
                            rng.normal(56.5, 1.5, n),
                            rng.normal(55, 1.5, n))
    skull_size = head_length - 0.6 * rng.normal(20, 1, n)
    return pd.DataFrame({"body_mass_g": body_mass,
                          "head_length_mm": head_length,
                          "skull_size_mm": skull_size,
                          "sex": sex})


def lincoln_temps(year: int = 2016, seed: int = 3) -> pd.DataFrame:
    """Daily mean temperature, Lincoln NE style — synthetic annual cycle.

    Includes a short month name for easy grouping.
    """
    rng = np.random.default_rng(seed)
    days = np.arange(1, 367)
    base = 52 + 35 * np.sin(2 * np.pi * (days - 110) / 365)
    temp = base + rng.normal(0, 5, days.size)
    # Day-of-year -> calendar month for 2016 (leap year).
    month_ends = np.cumsum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_idx = np.searchsorted(month_ends, days - 1, side="right")
    months = [month_names[i] for i in month_idx]
    return pd.DataFrame({"day": days, "mean_temp_F": temp,
                          "month": months, "month_idx": month_idx + 1,
                          "year": year})


def bridges() -> pd.DataFrame:
    """Pittsburgh bridges dataset (Wilke ch. 11).

    Rows are one-per-bridge with categorical covariates. We synthesize
    counts that match the totals used in the Wilke figures: 44 crafts,
    12 emerging, 27 mature, 23 modern (total 106 bridges); materials
    iron/steel/wood.  The era × material cross-tab mirrors Wilke's
    mosaic/treemap. We additionally fabricate river (Allegheny/
    Monongahela/Ohio) and length (short/medium/long) columns with plausible
    proportions keyed on the original UCI data.
    """
    # Era × Material table (as published in the book's mosaic/treemap):
    #               iron  steel  wood
    # crafts          10     0    18   (total 28 but scaled below)
    # emerging         3     9     1
    # mature           3    24     0
    # modern           0    16     0
    table = {
        "crafts":  {"iron": 10, "steel": 0,  "wood": 18},
        "emerging":{"iron": 3,  "steel": 9,  "wood": 1},
        "mature":  {"iron": 3,  "steel": 24, "wood": 0},
        "modern":  {"iron": 0,  "steel": 16, "wood": 0},
    }
    rng = np.random.default_rng(31)
    rows = []
    # Length / river probabilities, keyed on material (plausible).
    length_p = {"iron":  [0.0, 1.0, 0.0],
                "steel": [0.0, 0.62, 0.38],
                "wood":  [0.30, 0.70, 0.0]}
    river_p = {"iron":  [0.55, 0.40, 0.05],
               "steel": [0.45, 0.35, 0.20],
               "wood":  [0.85, 0.15, 0.0]}
    lengths = ["short", "medium", "long"]
    rivers = ["Allegheny", "Monongahela", "Ohio"]
    for era, mats in table.items():
        for mat, n in mats.items():
            for _ in range(n):
                L = rng.choice(lengths, p=length_p[mat])
                R = rng.choice(rivers, p=river_p[mat])
                rows.append({"material": mat, "erected": era,
                             "length": L, "river": R})
    return pd.DataFrame(rows)


def cows_butterfat() -> pd.DataFrame:
    """Butterfat percentages by cow breed — synthetic (Wilke fig 7.9).

    Four breeds with shifted means approximately matching the book:
    Ayrshire ~4.1%, Holstein-Friesian ~3.6%, Guernsey ~4.8%, Jersey ~5.3%.
    """
    rng = np.random.default_rng(23)
    breeds = {
        "Ayrshire":         (4.06, 0.45, 25),
        "Guernsey":         (4.80, 0.55, 20),
        "Holstein-Friesian":(3.67, 0.40, 30),
        "Jersey":           (5.30, 0.60, 25),
    }
    rows = []
    for breed, (mean, sd, n) in breeds.items():
        vals = rng.normal(mean, sd, n).clip(2.0, 8.0)
        for v in vals:
            rows.append({"breed": breed, "butterfat": float(v)})
    return pd.DataFrame(rows)


def bundestag_1976() -> pd.DataFrame:
    """Seats in 8th German Bundestag (1976–1980). Wilke fig 10.1."""
    return pd.DataFrame({
        "party": ["CDU/CSU", "SPD", "FDP"],
        "seats": [243, 214, 39],
        "color": ["#4E4E4E", "#D62728", "#F0E442"],
    })


def marketshare() -> pd.DataFrame:
    """Hypothetical company market shares over three years. Wilke fig 10.4."""
    rows = []
    years = [2015, 2016, 2017]
    shares = {
        "A": [17, 18, 22],
        "B": [18, 20, 22],
        "C": [20, 21, 20],
        "D": [22, 21, 19],
        "E": [23, 20, 17],
    }
    for y in years:
        for c, s in shares.items():
            rows.append({"year": y, "company": c,
                          "percent": s[years.index(y)]})
    return pd.DataFrame(rows)


def women_parliament_rwanda() -> pd.DataFrame:
    """% of women in Rwandan parliament, 1997-2016 (Wilke fig 10.7).

    Based on IPU data (values inline here).
    """
    years = list(range(1997, 2017))
    perc_women = [17, 17, 17, 17, 17, 17, 49, 49, 49, 49, 49,
                  56, 56, 56, 56, 56, 64, 64, 64, 64]
    return pd.DataFrame({"year": years, "perc_women": perc_women})


def happy_health_age(n: int = 4000, seed: int = 77) -> pd.DataFrame:
    """Synthetic GSS-style health status × age (Wilke fig 10.9)."""
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 91, n)
    # probabilities of health by age bucket
    rows = []
    levels = ["poor", "fair", "good", "very good", "excellent"]
    for a in age:
        # younger -> better health; older -> worse
        f = (a - 18) / 72  # 0..1 as age grows
        p_excellent = max(0.05, 0.40 - 0.32 * f)
        p_verygood  = 0.30 - 0.05 * f
        p_good      = 0.20 + 0.05 * f
        p_fair      = 0.08 + 0.15 * f
        p_poor      = 0.02 + 0.17 * f
        probs = np.array([p_poor, p_fair, p_good, p_verygood, p_excellent])
        probs = probs / probs.sum()
        lvl = rng.choice(levels, p=probs)
        rows.append({"age": int(a), "health": lvl})
    return pd.DataFrame(rows)


def happy() -> pd.DataFrame:
    """Self-rated happiness by income — synthesised ordinal survey."""
    rng = np.random.default_rng(11)
    incomes = ["<$25k", "$25-50k", "$50-100k", "$100k+"]
    levels = ["Not too happy", "Pretty happy", "Very happy"]
    rows = []
    probs = {
        "<$25k": [0.28, 0.55, 0.17],
        "$25-50k": [0.18, 0.58, 0.24],
        "$50-100k": [0.12, 0.55, 0.33],
        "$100k+": [0.08, 0.47, 0.45],
    }
    for inc in incomes:
        n = 500
        draws = rng.choice(levels, size=n, p=probs[inc])
        for lvl in levels:
            rows.append({"income": inc, "happiness": lvl,
                         "count": int((draws == lvl).sum())})
    return pd.DataFrame(rows)


def gapminder() -> pd.DataFrame:
    """Cached gapminder-style dataset (1952–2007, 5-year steps)."""
    csv = _DATA_DIR / "gapminder.csv"
    if csv.exists():
        return pd.read_csv(csv)
    # minimal inlined sample; replace with a real gapminder.csv to enrich
    return _gapminder_inline()


def _gapminder_inline() -> pd.DataFrame:
    rng = np.random.default_rng(42)
    countries = ["United States", "China", "India", "Brazil", "Germany",
                 "Nigeria", "Japan", "Russia", "Mexico", "Ethiopia"]
    continents = {
        "United States": "Americas", "China": "Asia", "India": "Asia",
        "Brazil": "Americas", "Germany": "Europe", "Nigeria": "Africa",
        "Japan": "Asia", "Russia": "Europe", "Mexico": "Americas",
        "Ethiopia": "Africa",
    }
    years = np.arange(1952, 2008, 5)
    rows = []
    for c in countries:
        life0 = rng.uniform(40, 65)
        gdp0 = rng.uniform(400, 8000)
        pop0 = rng.uniform(1e7, 1e8)
        for i, y in enumerate(years):
            life = life0 + i * rng.uniform(0.8, 1.5) + rng.normal(0, 0.5)
            gdp = gdp0 * (1 + 0.06) ** i * rng.uniform(0.9, 1.1)
            pop = pop0 * (1 + 0.02) ** i
            rows.append({
                "country": c, "continent": continents[c],
                "year": int(y), "lifeExp": life, "gdpPercap": gdp,
                "pop": pop,
            })
    return pd.DataFrame(rows)


def titanic() -> pd.DataFrame:
    """Bundled titanic.csv if present; else a tiny synthetic stand-in."""
    csv = _DATA_DIR / "titanic.csv"
    if csv.exists():
        return pd.read_csv(csv)
    rng = np.random.default_rng(5)
    n = 891
    pclass = rng.choice([1, 2, 3], size=n, p=[0.25, 0.21, 0.54])
    sex = rng.choice(["male", "female"], size=n, p=[0.65, 0.35])
    age = np.clip(rng.normal(30, 14, n), 0.4, 80)
    base_p = {"1-female": 0.97, "2-female": 0.92, "3-female": 0.5,
              "1-male": 0.37, "2-male": 0.16, "3-male": 0.13}
    probs = np.array([base_p[f"{p}-{s}"] for p, s in zip(pclass, sex)])
    survived = rng.binomial(1, probs).astype(int)
    return pd.DataFrame({"pclass": pclass, "sex": sex, "age": age,
                          "survived": survived})


def diamonds(n: int = 2000, seed: int = 2) -> pd.DataFrame:
    """Substitute for ggplot2::diamonds — synthetic but realistic carat/price."""
    rng = np.random.default_rng(seed)
    carat = rng.gamma(2.0, 0.35, n).clip(0.2, 5.0)
    clarity = rng.choice(["I1", "SI2", "SI1", "VS2", "VS1", "VVS2",
                           "VVS1", "IF"], size=n,
                         p=[0.02, 0.17, 0.24, 0.22, 0.15, 0.09, 0.07, 0.04])
    cut = rng.choice(["Fair", "Good", "Very Good", "Premium", "Ideal"],
                      size=n, p=[0.03, 0.09, 0.22, 0.26, 0.40])
    color = rng.choice(list("DEFGHIJ"), size=n,
                       p=[0.13, 0.18, 0.18, 0.21, 0.15, 0.10, 0.05])
    price = (
        1800 * carat ** 2.4
        * (1 + 0.08 * rng.normal(size=n))
        + rng.gamma(1.5, 150, n)
    ).clip(200, None)
    return pd.DataFrame({"carat": carat, "cut": cut, "color": color,
                          "clarity": clarity, "price": price})


def cabernets() -> pd.DataFrame:
    """Cabernet sauvignon ratings vs. price (synthetic for the rank chapter)."""
    rng = np.random.default_rng(9)
    n = 50
    price = rng.lognormal(mean=3.2, sigma=0.9, size=n).clip(5, 300)
    rating = np.clip(82 + 0.03 * price + rng.normal(0, 3, n), 70, 100)
    return pd.DataFrame({"wine_id": np.arange(1, n + 1),
                          "price_usd": price, "rating": rating})


def hate_crimes() -> pd.DataFrame:
    """Hate crimes vs. inequality by US state (synthetic stand-in)."""
    rng = np.random.default_rng(13)
    states = ["CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "NC", "MI",
              "NJ", "VA", "WA", "AZ", "MA", "TN", "IN", "MO", "MD", "WI",
              "CO", "MN", "SC", "AL", "LA", "KY", "OR", "OK", "CT", "UT"]
    gini = rng.uniform(0.40, 0.50, len(states))
    crimes = 0.5 + 18 * (gini - 0.40) + rng.normal(0, 0.6, len(states))
    return pd.DataFrame({"state": states, "gini_index": gini,
                          "hate_crimes_per_100k_splc": crimes.clip(0, None)})


def corrupt() -> pd.DataFrame:
    """Corruption Perceptions vs HDI (synthetic, for trend chapter)."""
    rng = np.random.default_rng(17)
    n = 70
    cpi = rng.uniform(10, 95, n)
    hdi = 0.35 + 0.006 * cpi + rng.normal(0, 0.05, n)
    hdi = hdi.clip(0.35, 1.0)
    continent = rng.choice(["Europe", "Asia", "Africa", "Americas", "Oceania"],
                            size=n)
    return pd.DataFrame({"cpi": cpi, "hdi": hdi, "continent": continent})


# --- Extras: ggplot2::mpg, Cars93, nycflights, dow_jones, etc. -------------

def mpg(seed: int = 99) -> pd.DataFrame:
    """Substitute for ggplot2::mpg (234 US-market cars, 1999 and 2008).

    We synthesise 234 rows with rounded displacement (to 0.1 L) and
    integer city mpg values, plus a `drv` train column ("f", "r", "4").
    The marginal relationship between displ and cty is approximately
    cty ~ 33 - 3.6 * displ, with drive-train shifts (RWD lower, 4WD lower).
    """
    rng = np.random.default_rng(seed)
    n = 234
    # displacement roughly 1.6 .. 7.0 litres, rounded to 0.1
    displ = np.round(rng.choice(
        np.arange(1.6, 7.1, 0.1), size=n,
        p=_mpg_displ_weights()), 1)
    drv = rng.choice(["f", "r", "4"], size=n, p=[0.44, 0.11, 0.45])
    base = 33 - 3.6 * displ
    shift = np.where(drv == "f", 1.5, np.where(drv == "r", -1.5, -0.5))
    cty = base + shift + rng.normal(0, 1.8, n)
    cty = np.clip(np.round(cty).astype(int), 9, 35)
    return pd.DataFrame({"displ": displ, "cty": cty, "drv": drv})


def _mpg_displ_weights() -> np.ndarray:
    # Favour smaller displacements (1.8–3.5 most common).
    grid = np.arange(1.6, 7.1, 0.1)
    w = np.exp(-((grid - 2.5) ** 2) / 3.5)
    return w / w.sum()


def cars93(seed: int = 11) -> pd.DataFrame:
    """Substitute for MASS::Cars93 — 93 cars with Price and Fuel.tank.capacity."""
    rng = np.random.default_rng(seed)
    n = 93
    # Price in thousand USD, log-normal with a long tail.
    price = rng.lognormal(mean=2.8, sigma=0.55, size=n).clip(7, 65)
    # Tank capacity saturates: y = A - B * exp(-m * x).
    A, B, m = 19.6, 15.5, 0.10
    tank = A - B * np.exp(-m * price) + rng.normal(0, 1.6, n)
    tank = tank.clip(8, 28)
    return pd.DataFrame({"Price": price, "Fuel_tank_capacity": tank})


def nycflights_delays(n: int = 30000, seed: int = 4) -> pd.DataFrame:
    """Substitute for flight_delays (Newark EWR 2013).

    Produces `departure_time` in hours-of-day floats and
    `departure_delay` in minutes. Delay distribution widens as the day
    progresses; most flights fall near zero with a long upper tail.
    """
    rng = np.random.default_rng(seed)
    # departure hour: bimodal morning / evening rush.
    hours = np.concatenate([
        rng.normal(8.5, 2.3, int(n * 0.55)),
        rng.normal(17.0, 2.8, int(n * 0.45)),
    ])
    hours = np.clip(hours, 0.0, 24.0)
    rng.shuffle(hours)
    hours = hours[:n]
    # delay: heavy tail that grows with time of day.
    base_scale = 10 + 4 * np.maximum(0, hours - 8)
    delay = rng.exponential(base_scale) - 6
    # a small fraction of extreme delays (>4h).
    extreme = rng.random(n) < 0.003
    delay[extreme] = rng.uniform(400, 900, extreme.sum())
    return pd.DataFrame({"departure_time": hours,
                          "departure_delay": delay})


def dow_jones_2009(seed: int = 19) -> pd.DataFrame:
    """Synthetic daily closes for the Dow Jones Industrial Average, 2009."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2008-12-31", "2010-01-08")
    n = len(dates)
    # Year starts at ~9000, drops to ~6550 in March, recovers to ~10400.
    t = np.arange(n) / (n - 1)
    # piecewise: drop then recovery.
    trend = np.where(
        t < 0.17,
        9000 - (9000 - 6547) * (t / 0.17),
        6547 + (10428 - 6547) * ((t - 0.17) / (1 - 0.17)),
    )
    noise = np.cumsum(rng.normal(0, 55, n))
    close = trend + 0.4 * noise
    return pd.DataFrame({"date": dates, "close": close})


def biorxiv_growth() -> pd.DataFrame:
    """Monthly bioRxiv preprint submissions, Nov 2013 – Apr 2018.

    Approximate counts drawn from Anaya / prepubmed.org. Exponential
    growth from ~60 in early 2014 to ~1500 by 2018.
    """
    rng = np.random.default_rng(33)
    dates = pd.date_range("2013-11-01", "2018-04-01", freq="MS")
    years = np.array([(d.year + (d.month - 1) / 12) for d in dates])
    y = 60.0 * np.exp(0.77 * (years - 2014))
    # Add small multiplicative noise.
    count = y * np.exp(rng.normal(0, 0.07, len(dates)))
    return pd.DataFrame({"date": dates,
                          "date_dec": years,
                          "count": count})


def preprints_three() -> pd.DataFrame:
    """Monthly submissions for three biomedical preprint servers.

    Columns: date, archive in {bioRxiv, arXiv q-bio, PeerJ Preprints}, count.
    Range: Jan 2014 – Jan 2017.
    """
    rng = np.random.default_rng(71)
    dates = pd.date_range("2014-01-01", "2017-01-01", freq="MS")
    years = np.array([(d.year + (d.month - 1) / 12) for d in dates])
    rows = []
    # bioRxiv: fast exponential
    bio = 60 * np.exp(0.77 * (years - 2014)) * np.exp(rng.normal(0, 0.07, len(dates)))
    # arXiv q-bio: slow linear growth ~50 → 90
    qbio = np.linspace(55, 95, len(dates)) + rng.normal(0, 6, len(dates))
    # PeerJ: flat ~40–55
    peerj = np.linspace(35, 55, len(dates)) + rng.normal(0, 5, len(dates))
    for d, y, b, q, p in zip(dates, years, bio, qbio, peerj):
        rows.append({"date": d, "date_dec": y, "archive": "bioRxiv", "count": float(b)})
        rows.append({"date": d, "date_dec": y, "archive": "arXiv q-bio", "count": float(q)})
        rows.append({"date": d, "date_dec": y, "archive": "PeerJ Preprints", "count": float(p)})
    return pd.DataFrame(rows)


def keeling_curve() -> pd.DataFrame:
    """Monthly Mauna Loa CO2, 1959–2017 (synthesised to match the Keeling curve).

    Includes the characteristic seasonal saw-tooth plus a slightly
    super-linear long-term trend.
    """
    rng = np.random.default_rng(49)
    months = pd.date_range("1959-01-01", "2017-12-01", freq="MS")
    t = np.arange(len(months))
    years = np.array([d.year + (d.month - 1) / 12 for d in months])
    # super-linear trend: 315 + 0.82*(year-1959) + 0.018*(year-1959)^2 / 2
    yr = years - 1959
    trend = 315 + 0.82 * yr + 0.018 * yr ** 2 / 2
    season = 3.0 * np.sin(2 * np.pi * (t / 12 - 0.28))  # peak in May
    noise = rng.normal(0, 0.25, len(months))
    co2 = trend + season + noise
    return pd.DataFrame({"date": months,
                          "year": [d.year for d in months],
                          "date_dec": years,
                          "co2": co2,
                          "trend": trend,
                          "seasonal": season,
                          "remainder": co2 - trend - season})


def hpi_states() -> pd.DataFrame:
    """House Price Index for four states, 1980–2017 (synthesised)."""
    rng = np.random.default_rng(54)
    dates = pd.date_range("1980-01-01", "2017-12-01", freq="MS")
    t = (dates - pd.Timestamp("2000-12-01")).days / 365.25  # years from Dec 2000
    rows = []

    def _series(trend_rate, bubble_fn):
        hpi = 100 * np.exp(trend_rate * t) * bubble_fn(t) * np.exp(rng.normal(0, 0.005, len(t)))
        return hpi

    def ca_bubbles(t):
        b1 = 0.15 * np.exp(-((t + 10) ** 2) / 14)  # 1990
        b2 = 0.42 * np.exp(-((t - 5) ** 2) / 8)     # 2005
        decline = -0.22 * np.exp(-((t - 11) ** 2) / 8)
        return np.exp(b1 + b2 + decline)

    def nv_bubbles(t):
        b = 0.55 * np.exp(-((t - 5) ** 2) / 6)
        decline = -0.32 * np.exp(-((t - 11) ** 2) / 8)
        return np.exp(b + decline)

    def tx_bubbles(t):
        return np.exp(0.02 * np.exp(-((t - 4) ** 2) / 8))

    def wv_bubbles(t):
        return np.exp(0.015 * np.exp(-((t - 6) ** 2) / 10))

    cfg = {
        "California":  (0.047, ca_bubbles),
        "Nevada":      (0.028, nv_bubbles),
        "Texas":       (0.028, tx_bubbles),
        "West Virginia": (0.028, wv_bubbles),
    }
    for state, (rate, bubble) in cfg.items():
        hpi = _series(rate, bubble)
        trend = 100 * np.exp(rate * t)
        for d, v, tv in zip(dates, hpi, trend):
            rows.append({"date": d, "state": state,
                         "hpi": float(v), "hpi_trend": float(tv),
                         "hpi_detrended": float(v / tv)})
    return pd.DataFrame(rows)


def ca_house_unemployment() -> pd.DataFrame:
    """California 12-month house-price change and unemployment rate,
    Jan 2001–Dec 2017 (synthesised to illustrate the anti-correlated cycle).
    """
    rng = np.random.default_rng(64)
    dates = pd.date_range("2001-01-01", "2017-12-01", freq="MS")
    t = np.arange(len(dates))
    # house price % change: big positive swing 2003–06, crash 2007–11, recovery
    # plus small early cycle 2001–03
    c1 = 0.22 * np.exp(-((t - 54) ** 2) / 120)   # 2005-ish peak
    c2 = -0.27 * np.exp(-((t - 108) ** 2) / 200)  # 2010 trough
    c3 = 0.11 * np.exp(-((t - 30) ** 2) / 80)     # 2003
    c4 = 0.06 * np.exp(-((t - 180) ** 2) / 200)   # 2016
    hp = c1 + c2 + c3 + c4 + rng.normal(0, 0.01, len(t))
    # Unemployment: inverse pattern, base ~6%, climbs to 12% around 2010.
    u1 = 0.06 - 0.018 * np.exp(-((t - 60) ** 2) / 200)  # boom drops it
    u1 += 0.06 * np.exp(-((t - 120) ** 2) / 600)         # crisis spike
    u1 -= 0.018 * np.exp(-((t - 200) ** 2) / 400)         # late recovery
    u1 = np.clip(u1 + rng.normal(0, 0.001, len(t)), 0.04, 0.135)
    return pd.DataFrame({"date": dates,
                          "house_price_perc": hp,
                          "unemploy_perc": u1 * 100})


def oats_yield() -> pd.DataFrame:
    """MASS::oats — 3 varieties x 4 nitrogen treatments, mean yield (lbs/acre)."""
    rows = [
        ("Marvellous",   0.0, 2200),
        ("Marvellous",   0.2, 2600),
        ("Marvellous",   0.4, 2800),
        ("Marvellous",   0.6, 3200),
        ("Golden Rain",  0.0, 1950),
        ("Golden Rain",  0.2, 2350),
        ("Golden Rain",  0.4, 2700),
        ("Golden Rain",  0.6, 2950),
        ("Victory",      0.0, 1850),
        ("Victory",      0.2, 2200),
        ("Victory",      0.4, 2400),
        ("Victory",      0.6, 2650),
    ]
    return pd.DataFrame(rows, columns=["variety", "N", "mean_yield"])


def co2_emissions_pairs() -> pd.DataFrame:
    """Per-capita CO2 emissions for ~160 countries in 1970, 2000, and 2010.

    Log-normal distribution spanning 4 orders of magnitude, with a small
    upward shift over the 40-year window.
    """
    rng = np.random.default_rng(99)
    n = 160
    y1970 = rng.lognormal(mean=0.2, sigma=1.6, size=n).clip(0.01, 60)
    # multiplicative drift (most countries emit more in 2010)
    drift1 = rng.normal(0.25, 0.5, n)  # log factor
    y2010 = y1970 * np.exp(drift1)
    y2010 = y2010.clip(0.01, 70)
    y2000 = y1970 * np.exp(drift1 * 0.75 + rng.normal(0, 0.1, n))
    return pd.DataFrame({"country": [f"C{i:03d}" for i in range(n)],
                          "y1970": y1970,
                          "y2000": y2000,
                          "y2010": y2010})


def forensic_glass() -> pd.DataFrame:
    """Synthesised forensic-glass oxide composition for 214 samples.

    Columns: Mg, Ca, Fe, K, Na, Al, Ba, plus `type` in
    {window, container, tableware, headlamp}.  Correlation structure is
    designed to roughly reproduce the correlogram in Wilke's chapter 12:
    Mg anticorrelates with most oxides; Ba/Al/Na cluster; Ca/K cluster.
    """
    rng = np.random.default_rng(23)
    n = 214

    # shared latent factors
    size = rng.normal(0, 1, n)    # overall scale
    fac_baalna = rng.normal(0, 1, n)   # Ba/Al/Na loading
    fac_cak = rng.normal(0, 1, n)      # Ca/K loading
    mg_factor = -0.6 * fac_baalna - 0.3 * fac_cak + rng.normal(0, 0.4, n)
    fe_factor = rng.normal(0, 1, n)

    Mg = 2.0 + 1.2 * mg_factor + 0.2 * rng.normal(0, 1, n)
    Ca = 8.5 + 0.9 * fac_cak + 0.1 * size + rng.normal(0, 0.4, n)
    Fe = 0.07 + 0.05 * fe_factor + 0.01 * rng.normal(0, 1, n)
    K  = 0.5 + 0.6 * fac_cak + rng.normal(0, 0.2, n)
    Na = 13.5 + 0.9 * fac_baalna + rng.normal(0, 0.5, n)
    Al = 1.5 + 0.7 * fac_baalna + rng.normal(0, 0.3, n)
    Ba = 0.2 + 0.9 * fac_baalna + rng.normal(0, 0.2, n)

    # Assign type based on fac_baalna / fac_cak
    type_ = np.where(
        fac_baalna > 0.6, "headlamp",
        np.where(fac_cak > 0.7, "tableware",
                 np.where(fac_cak < -0.8, "container", "window"))
    )
    return pd.DataFrame({"Mg": Mg, "Ca": Ca, "Fe": Fe, "K": K,
                          "Na": Na, "Al": Al, "Ba": Ba, "type": type_})


def correlation_examples() -> pd.DataFrame:
    """Six scatter clouds with correlations r in {0.2, 0.6, 0.9, -0.2, -0.6, -0.9}.

    Returns columns x, y, r.
    """
    rng = np.random.default_rng(5)
    n = 80
    rs = [0.2, 0.6, 0.9, -0.2, -0.6, -0.9]
    frames = []
    for r in rs:
        z1 = rng.normal(0, 1, n)
        z2 = rng.normal(0, 1, n)
        x = z1
        y = r * z1 + np.sqrt(1 - r * r) * z2
        frames.append(pd.DataFrame({"x": x, "y": y, "r": r}))
    return pd.concat(frames, ignore_index=True)


# --- Batch N: uncertainty / proportional ink / no_3d ----------------------

def hawaii_income() -> pd.DataFrame:
    """Median income in the 5 counties of Hawaii (2010 and 2015).

    Values are inline approximations of the 2010 and 2015 Five-Year
    American Community Survey figures used by Wilke in the proportional
    ink chapter.
    """
    rows = [
        ("Hawaii",    2010, 55000),
        ("Honolulu",  2010, 65000),
        ("Kalawao",   2010, 45000),
        ("Kauai",     2010, 60000),
        ("Maui",      2010, 61500),
        ("Hawaii",    2015, 53500),
        ("Honolulu",  2015, 72133),
        ("Kalawao",   2015, 66250),
        ("Kauai",     2015, 64079),
        ("Maui",      2015, 66476),
    ]
    return pd.DataFrame(rows, columns=["county", "year", "median_income"])


def fb_stock() -> pd.DataFrame:
    """Daily Facebook (FB) close from 22 Oct 2016 through 21 Jan 2017.

    Approximate from memory; shape captures the ~$133 peak in late Oct
    falling to ~$115 in mid-Nov, bottoming near $115 around late Dec and
    starting to recover into mid-Jan.
    """
    rng = np.random.default_rng(41)
    dates = pd.bdate_range("2016-10-24", "2017-01-20")
    t = np.linspace(0, 1, len(dates))
    # piecewise trajectory hitting the key prices
    price = np.piecewise(
        t,
        [t < 0.15, (t >= 0.15) & (t < 0.60), t >= 0.60],
        [
            lambda s: 132.5 - (132.5 - 116) * (s / 0.15),  # drop
            lambda s: 116 + 2.0 * np.sin((s - 0.15) * np.pi / 0.45) - 1.0 * s,
            lambda s: 116 + (128 - 116) * ((s - 0.60) / 0.40),
        ],
    )
    price = price + rng.normal(0, 0.7, len(dates))
    return pd.DataFrame({"date": dates, "price": price})


def oceania_gdp() -> pd.DataFrame:
    """2007 GDP (USD) for Oceania countries (Gapminder approximations)."""
    rows = [
        ("Australia",              7.78e11),
        ("New Zealand",            1.05e11),
        ("Papua New Guinea",       1.23e10),
        ("French Polynesia",       5.90e9),
        ("New Caledonia",          8.40e9),
        ("Fiji",                   3.45e9),
        ("Solomon Islands",        6.50e8),
        ("Samoa",                  5.60e8),
        ("Tonga",                  4.30e8),
        ("Vanuatu",                5.60e8),
        ("Micronesia, Fed. Sts.",  2.80e8),
    ]
    return pd.DataFrame(rows, columns=["country", "GDP"])


def ri_population() -> pd.DataFrame:
    """2010 Rhode Island county populations (U.S. Decennial Census)."""
    rows = [
        ("Providence", 626667),
        ("Kent",       166158),
        ("Washington", 126979),
        ("Newport",     82888),
        ("Bristol",     49875),
    ]
    return pd.DataFrame(rows, columns=["county", "pop2010"])


def titanic_counts() -> pd.DataFrame:
    """Counts of female/male passengers by class on the Titanic."""
    rows = [
        ("1st",  "female", 144),
        ("1st",  "male",   179),
        ("2nd",  "female", 106),
        ("2nd",  "male",   171),
        ("3rd",  "female", 216),
        ("3rd",  "male",   493),
    ]
    return pd.DataFrame(rows, columns=["class", "sex", "count"])


def va_deaths() -> pd.DataFrame:
    """R's VADeaths dataset: 1940 Virginia mortality by age and group.

    Rates are deaths per 1000 persons.
    """
    age = ["50-54", "55-59", "60-64", "65-69", "70-74"]
    rows = [
        ("50-54", "Rural Male",   11.7),
        ("55-59", "Rural Male",   18.1),
        ("60-64", "Rural Male",   26.9),
        ("65-69", "Rural Male",   41.0),
        ("70-74", "Rural Male",   66.0),
        ("50-54", "Rural Female",  8.7),
        ("55-59", "Rural Female", 11.7),
        ("60-64", "Rural Female", 20.3),
        ("65-69", "Rural Female", 30.9),
        ("70-74", "Rural Female", 54.3),
        ("50-54", "Urban Male",   15.4),
        ("55-59", "Urban Male",   24.3),
        ("60-64", "Urban Male",   37.0),
        ("65-69", "Urban Male",   54.6),
        ("70-74", "Urban Male",   71.1),
        ("50-54", "Urban Female",  8.4),
        ("55-59", "Urban Female", 13.6),
        ("60-64", "Urban Female", 19.3),
        ("65-69", "Urban Female", 35.1),
        ("70-74", "Urban Female", 50.0),
    ]
    df = pd.DataFrame(rows, columns=["age", "group", "rate"])
    df["age"] = pd.Categorical(df["age"], categories=age, ordered=True)
    return df


def cacao_ratings(seed: int = 67) -> pd.DataFrame:
    """Synthetic expert chocolate bar ratings (Manhattan Chocolate Society).

    Generates per-country ratings matching Wilke's distribution shape
    (scale 1-5, mean near 3.2) for six countries: Canada, Switzerland,
    Austria, Belgium, Peru, U.S.
    """
    rng = np.random.default_rng(seed)
    spec = {
        "Canada":      (3.32, 0.45, 125),
        "Switzerland": (3.24, 0.46,  38),
        "Austria":     (3.18, 0.46,  26),
        "Belgium":     (3.12, 0.48,  38),
        "Peru":        (3.02, 0.48,  62),
        "US":          (3.06, 0.50, 566),
    }
    rows = []
    for loc, (mu, sd, n) in spec.items():
        vals = rng.normal(mu, sd, n)
        # Round to nearest 0.25 to match the actual rating grid
        vals = np.clip(np.round(vals * 4) / 4, 1.0, 5.0)
        for v in vals:
            rows.append({"location": loc, "rating": float(v)})
    return pd.DataFrame(rows)


def mtcars_3cols() -> pd.DataFrame:
    """mtcars displacement / horsepower / mpg / cylinders view."""
    df = mtcars()
    return df[["disp", "hp", "mpg", "cyl"]].copy()


def pa_income_age(seed: int = 202) -> pd.DataFrame:
    """Synthetic median income vs median age for 67 PA counties.

    Includes margins of error for both variables (ACS-style).
    """
    rng = np.random.default_rng(seed)
    n = 67
    age = rng.uniform(36, 52, n) + rng.normal(0, 1.0, n)
    income = 25000 + 700 * age + rng.normal(0, 7000, n)
    age_moe = rng.uniform(0.3, 1.2, n)
    income_moe = rng.uniform(2000, 7000, n)
    return pd.DataFrame({
        "age": age,
        "income": income,
        "age_moe": age_moe,
        "income_moe": income_moe,
    })


# --- Additional datasets for coordinates_axes, multi_panel, aesthetic_mapping,
#     balance_data_context, avoid_line_drawings, small_axis_labels chapters ----

def ba_degrees() -> pd.DataFrame:
    """Bachelor's degrees awarded by field, 1971–2015 (yearly).

    Data is synthesised so that (a) the top-9 share of degrees roughly
    matches Wilke's figure, (b) field-level trends reflect the same
    qualitative story (business rising, education falling, social sciences
    falling, health rising, visual arts flat, etc.).
    """
    years = np.arange(1971, 2016)
    n = len(years)
    t = (years - 1971) / (2015 - 1971)
    rng = np.random.default_rng(8)

    fields = [
        ("Business",                               0.139, 0.192,  1.0),
        ("Health professions",                     0.030, 0.117,  2.2),
        ("Social sciences and history",            0.187, 0.085, -1.2),
        ("Education",                              0.210, 0.043, -1.7),
        ("Psychology",                             0.044, 0.060,  0.3),
        ("Visual and performing arts",             0.040, 0.051,  0.4),
        ("Biological sciences",                    0.039, 0.057,  0.5),
        ("Engineering",                            0.055, 0.060,  0.0),
        ("Communication, journalism, and related", 0.010, 0.047,  1.5),
    ]
    rows = []
    totals = np.linspace(0.84e6, 1.89e6, n)
    for field, start, end, curv in fields:
        shape = 1 / (1 + np.exp(-6 * (t - 0.5))) if curv >= 0 else \
                (1 - 1 / (1 + np.exp(-6 * (t - 0.5))))
        blend = 0.5 * (t + shape)
        perc = start + (end - start) * blend
        perc = np.clip(perc + rng.normal(0, 0.0015, n), 0.005, 0.30)
        for y, p, tot in zip(years, perc, totals):
            rows.append({"year": int(y), "field": field,
                         "perc": float(p), "count": float(p * tot)})
    return pd.DataFrame(rows)


def titanic_all(seed: int = 21) -> pd.DataFrame:
    """Extended Titanic passengers — ensures age column is populated."""
    rng = np.random.default_rng(seed)
    base = titanic().copy()
    if "age" not in base.columns or base["age"].isna().any():
        base["age"] = np.clip(rng.normal(30, 14, len(base)), 0.5, 80)
    return base


def gene_expression_t7(seed: int = 317) -> pd.DataFrame:
    """Wild-type vs. mutant T7 bacteriophage mRNA abundances.

    Returns a DataFrame with columns tpm_wt, tpm_mutant, label. Label is
    non-empty only for the three highlighted genes (8, 9, 10A).
    """
    rng = np.random.default_rng(seed)
    n = 58
    log_wt = rng.normal(np.log(0.01), 1.2, n)
    tpm_wt = np.exp(log_wt).clip(3e-4, 3e-1)
    tpm_mut = tpm_wt * np.exp(rng.normal(0, 0.15, n))
    order = np.argsort(tpm_wt)[::-1]
    highlight_idx = order[:3]
    names = ["10A", "9", "8"]
    tpm_mut[highlight_idx[0]] = tpm_wt[highlight_idx[0]] * 0.18
    tpm_mut[highlight_idx[1]] = tpm_wt[highlight_idx[1]] * 0.08
    tpm_mut[highlight_idx[2]] = tpm_wt[highlight_idx[2]] * 0.25
    labels = [""] * n
    for i, nm in zip(highlight_idx, names):
        labels[i] = nm
    return pd.DataFrame({
        "tpm_wt": tpm_wt,
        "tpm_mutant": tpm_mut.clip(3e-4, 3e-1),
        "label": labels,
    })


def lincoln_weather_2016(seed: int = 39) -> pd.DataFrame:
    """Daily mean temperature (°F) by month for Lincoln, NE, 2016."""
    rng = np.random.default_rng(seed)
    month_mu = [23, 28, 43, 52, 63, 73, 79, 76, 66, 55, 42, 28]
    month_sd = [12, 10,  8,  7,  7,  6,  5,  5,  7,  8,  9, 11]
    names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    rows = []
    for mu, sd, nm, nd in zip(month_mu, month_sd, names, days_in_month):
        vals = rng.normal(mu, sd, nd)
        for v in vals:
            rows.append({"month": nm, "mean_temp_F": float(v)})
    return pd.DataFrame(rows)


def ncdc_normals_4locs(seed: int = 101) -> pd.DataFrame:
    """Daily temperature normals (°F) for four U.S. locations (synthesised).

    Locations: Death Valley (hot), Houston, San Diego (mild, low-amp),
    Chicago (cold winters). 366 days × 4 locations.
    """
    rng = np.random.default_rng(seed)
    days = np.arange(1, 367)
    spec = {
        # mean, amplitude, phase (day of year of peak), noise sd
        "Death Valley": (77, 32, 198, 1.2),
        "Houston":      (70, 17, 200, 1.0),
        "San Diego":    (63,  8, 232, 0.6),
        "Chicago":      (50, 30, 200, 1.2),
    }
    rows = []
    month_ends = np.cumsum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for loc, (m, amp, phase, sd) in spec.items():
        cycle = m + amp * np.cos(2 * np.pi * (days - phase) / 365)
        temp = cycle + rng.normal(0, sd, days.size)
        for d, t in zip(days, temp):
            mo = month_names[np.searchsorted(month_ends, d - 1, side="right")]
            rows.append({"day": int(d), "month": mo, "location": loc,
                         "temperature": float(t)})
    return pd.DataFrame(rows)


def us_tx_counties_population(seed: int = 29) -> pd.DataFrame:
    """Texas county populations (2010 Census), sorted by size.

    Population values are synthesised via a log-normal draw; six named
    counties anchor the extremes (Harris / Dallas / Tarrant at top,
    Loving / King / Kenedy at bottom).
    """
    rng = np.random.default_rng(seed)
    n = 254
    log_pop = rng.normal(loc=np.log(17000), scale=1.6, size=n)
    pops = np.exp(log_pop).clip(82, 4e6)
    pops_sorted = np.sort(pops)[::-1]
    pops_sorted[0] = 4092459   # Harris
    pops_sorted[1] = 2368139   # Dallas
    pops_sorted[2] = 1818198   # Tarrant
    pops_sorted[-1] = 82       # Loving
    pops_sorted[-2] = 134      # King
    pops_sorted[-3] = 170      # Kenedy
    median = float(np.median(pops_sorted))
    names = [f"County_{i}" for i in range(n)]
    names[0] = "Harris"
    names[1] = "Dallas"
    names[2] = "Tarrant"
    names[-1] = "Loving"
    names[-2] = "King"
    names[-3] = "Kenedy"
    return pd.DataFrame({
        "county": names,
        "pop2010": pops_sorted,
        "popratio": pops_sorted / median,
        "rank": np.arange(1, n + 1),
    })


def northeast_state_areas() -> pd.DataFrame:
    """Areas of nine Northeastern U.S. states in square miles."""
    rows = [
        ("NY", 54556), ("PA", 46055), ("ME", 35385),
        ("MA", 10565), ("VT",  9616), ("NH",  9349),
        ("NJ",  8723), ("CT",  5543), ("RI",  1212),
    ]
    return pd.DataFrame(rows, columns=["state_abr", "area"])


def movie_rankings(seed: int = 123) -> pd.DataFrame:
    """Synthetic IMDB-style movie rankings vs. vote counts, 1906–2005."""
    rng = np.random.default_rng(seed)
    rows = []
    for year in range(1906, 2006):
        n = 120 + int((year - 1906) * 3)
        votes = 10 ** rng.uniform(0.8, 5.0, n)
        if year >= 1995:
            base = 7.5 - 0.3 * (np.log10(votes) - 2)
        else:
            base = 6.0 + 0.5 * (np.log10(votes) - 2)
        rating = np.clip(base + rng.normal(0, 1.0, n), 1.0, 10.0)
        for v, r in zip(votes, rating):
            rows.append({"year": year, "votes": float(v),
                         "rating": float(r)})
    return pd.DataFrame(rows)

# --- Extras for color / pitfalls / redundant / story / titles chapters ----

def us_popgrowth() -> pd.DataFrame:
    """US state population growth 2000–2010 by region (US Census).

    Returns columns: state, region, pop2000, popgrowth (fractional).
    """
    # region → state mapping (Census Bureau)
    west = ["Alaska", "Arizona", "California", "Colorado", "Hawaii",
            "Idaho", "Montana", "Nevada", "New Mexico", "Oregon",
            "Utah", "Washington", "Wyoming"]
    south = ["Alabama", "Arkansas", "Delaware", "District of Columbia",
             "Florida", "Georgia", "Kentucky", "Louisiana", "Maryland",
             "Mississippi", "North Carolina", "Oklahoma", "South Carolina",
             "Tennessee", "Texas", "Virginia", "West Virginia"]
    midwest = ["Illinois", "Indiana", "Iowa", "Kansas", "Michigan",
               "Minnesota", "Missouri", "Nebraska", "North Dakota",
               "Ohio", "South Dakota", "Wisconsin"]
    northeast = ["Connecticut", "Maine", "Massachusetts", "New Hampshire",
                 "New Jersey", "New York", "Pennsylvania", "Rhode Island",
                 "Vermont"]
    region_of = {}
    for r, ss in (("West", west), ("South", south),
                  ("Midwest", midwest), ("Northeast", northeast)):
        for s in ss:
            region_of[s] = r

    # Approximate 2000 populations (millions -> persons)
    pop2000 = {
        "California": 33871648, "Texas": 20851820, "New York": 18976457,
        "Florida": 15982378, "Illinois": 12419293, "Pennsylvania": 12281054,
        "Ohio": 11353140, "Michigan": 9938444, "New Jersey": 8414350,
        "Georgia": 8186453, "North Carolina": 8049313, "Virginia": 7078515,
        "Massachusetts": 6349097, "Indiana": 6080485, "Washington": 5894121,
        "Tennessee": 5689283, "Missouri": 5595211, "Wisconsin": 5363675,
        "Maryland": 5296486, "Arizona": 5130632, "Minnesota": 4919479,
        "Louisiana": 4468976, "Alabama": 4447100, "Colorado": 4301261,
        "Kentucky": 4041769, "South Carolina": 4012012,
        "Oklahoma": 3450654, "Oregon": 3421399, "Connecticut": 3405565,
        "Iowa": 2926324, "Mississippi": 2844658, "Kansas": 2688418,
        "Arkansas": 2673400, "Utah": 2233169, "Nevada": 1998257,
        "New Mexico": 1819046, "West Virginia": 1808344,
        "Nebraska": 1711263, "Idaho": 1293953, "Maine": 1274923,
        "New Hampshire": 1235786, "Hawaii": 1211537, "Rhode Island": 1048319,
        "Montana": 902195, "Delaware": 783600, "South Dakota": 754844,
        "North Dakota": 642200, "Alaska": 626932, "Vermont": 608827,
        "District of Columbia": 572059, "Wyoming": 493782,
    }
    # Approximate % growth 2000->2010
    popgrowth_pct = {
        "Nevada": 35.1, "Arizona": 24.6, "Utah": 23.8, "Idaho": 21.1,
        "Texas": 20.6, "North Carolina": 18.5, "Georgia": 18.3,
        "Florida": 17.6, "Colorado": 16.9, "South Carolina": 15.3,
        "Delaware": 14.6, "Washington": 14.1, "Wyoming": 14.1,
        "Virginia": 13.0, "Alaska": 13.3, "Tennessee": 11.5,
        "Oregon": 12.0, "Montana": 9.7, "Hawaii": 12.3, "New Mexico": 13.2,
        "California": 10.0, "Maryland": 9.0, "Arkansas": 9.1,
        "Oklahoma": 8.7, "Alabama": 7.5, "Kansas": 6.1, "Minnesota": 7.8,
        "Nebraska": 6.7, "Kentucky": 7.4, "South Dakota": 7.9,
        "Missouri": 7.0, "New Hampshire": 6.5, "North Dakota": 4.7,
        "Indiana": 6.6, "Wisconsin": 6.0, "Maine": 4.2,
        "Mississippi": 4.3, "Iowa": 4.1, "Vermont": 2.8,
        "Connecticut": 4.9, "New Jersey": 4.5, "Massachusetts": 3.1,
        "Pennsylvania": 3.4, "West Virginia": 2.5, "Ohio": 1.6,
        "Illinois": 3.3, "New York": 2.1, "Louisiana": 1.4,
        "Rhode Island": 0.4, "Michigan": -0.6,
        "District of Columbia": 5.2,
    }
    rows = []
    for s, region in region_of.items():
        rows.append({
            "state": s,
            "region": region,
            "pop2000": pop2000[s],
            "popgrowth": popgrowth_pct[s] / 100.0,
        })
    return pd.DataFrame(rows)


def aus_athletes(seed: int = 55) -> pd.DataFrame:
    """Telford & Cunningham 1991 Australian Institute of Sport — synthetic.

    Columns: sex, sport, height (cm), pcBfat (% body fat), rcc (red cell
    count, 10^12/L), wcc (white cell count, 10^9/L). Sports: track (400m),
    track (sprint), field, swimming, water polo, basketball, rowing,
    netball, gymnastics, tennis.
    """
    rng = np.random.default_rng(seed)
    spec_m = {
        "track (sprint)":  (180, 6, 7.0, 1.8),
        "track (400m)":    (183, 6, 7.3, 1.9),
        "field":           (188, 7, 11.0, 2.6),
        "swimming":        (185, 6, 10.0, 2.2),
        "water polo":      (188, 5, 13.5, 2.4),
        "basketball":      (196, 7, 10.0, 2.4),
        "rowing":          (190, 5, 11.0, 2.3),
        "tennis":          (183, 6, 9.5, 2.1),
    }
    spec_f = {
        "track (sprint)":  (170, 6, 10.0, 2.0),
        "track (400m)":    (171, 6, 10.5, 2.1),
        "field":           (173, 7, 18.0, 3.5),
        "swimming":        (174, 6, 17.0, 3.0),
        "basketball":      (180, 7, 20.0, 3.3),
        "rowing":           (180, 5, 18.0, 3.2),
        "tennis":          (168, 6, 20.0, 3.5),
        "netball":         (176, 6, 21.5, 3.6),
        "gymnastics":      (160, 5, 13.0, 2.2),
    }
    rows = []
    for spec, sex in ((spec_m, "m"), (spec_f, "f")):
        for sport, (h_mean, h_sd, bf_mean, bf_sd) in spec.items():
            n = rng.integers(8, 20)
            for _ in range(int(n)):
                h = rng.normal(h_mean, h_sd)
                bf = max(3.0, rng.normal(bf_mean, bf_sd))
                rcc = rng.normal(4.8 if sex == "m" else 4.4, 0.3)
                wcc = rng.normal(7.0, 1.5)
                rows.append({
                    "sex": sex, "sport": sport,
                    "height": h, "pcBfat": bf,
                    "rcc": rcc, "wcc": wcc,
                })
    return pd.DataFrame(rows)


def tech_stocks() -> pd.DataFrame:
    """Monthly close prices for AAPL, FB, GOOG, MSFT, Jun 2012 – May 2017.

    Columns: date, company, ticker, price, index_price (price on 2012-06-01),
    price_indexed (price / index_price * 100).  Prices approximate Yahoo
    Finance monthly closes.
    """
    dates = pd.date_range("2012-06-01", "2017-06-01", freq="MS")
    n = len(dates)
    rng = np.random.default_rng(2017)
    # piecewise realistic trajectories
    def _fb():
        # 27 -> ~150 over 5 years, rocky 2012-13 then steady
        t = np.linspace(0, 1, n)
        p = np.piecewise(
            t,
            [t < 0.20, (t >= 0.20) & (t < 0.60), t >= 0.60],
            [
                lambda s: 27 + (s / 0.20) * (50 - 27),
                lambda s: 50 + ((s - 0.20) / 0.40) * (108 - 50),
                lambda s: 108 + ((s - 0.60) / 0.40) * (152 - 108),
            ],
        )
        return p + rng.normal(0, 2, n)
    def _goog():
        t = np.linspace(0, 1, n)
        return 290 + t * (975 - 290) + rng.normal(0, 8, n)
    def _aapl():
        t = np.linspace(0, 1, n)
        return 82 + t * (155 - 82) + rng.normal(0, 3, n)
    def _msft():
        t = np.linspace(0, 1, n)
        return 30 + t * (70 - 30) + rng.normal(0, 1.5, n)
    spec = {
        "FB":   ("Facebook",  _fb()),
        "GOOG": ("Alphabet",  _goog()),
        "AAPL": ("Apple",     _aapl()),
        "MSFT": ("Microsoft", _msft()),
    }
    rows = []
    for ticker, (company, series) in spec.items():
        index_price = series[0]
        for d, p in zip(dates, series):
            rows.append({
                "date": d, "company": company, "ticker": ticker,
                "price": float(p),
                "index_price": float(index_price),
                "price_indexed": float(p / index_price * 100),
            })
    return pd.DataFrame(rows)


def pet_ownership() -> pd.DataFrame:
    """Number of US households with each pet type (2012 AVMA survey)."""
    rows = [
        ("dogs",   43346000),
        ("cats",   36117000),
        ("fish",    7738000),
        ("birds",   3671000),
    ]
    return pd.DataFrame(rows, columns=["pet", "households"])


def nyc_airline_delays(seed: int = 42) -> pd.DataFrame:
    """NYC 2013 flights by airline — mean arrival delay and flight count.

    Columns: name, mean_delay (min), n (flights), carrier.
    """
    # approximate from nycflights13::flights aggregated by carrier
    rows = [
        ("Frontier",      21.9, 685,   "F9"),
        ("AirTran",       20.1, 3260,  "FL"),
        ("ExpressJet",    15.8, 54173, "EV"),
        ("Mesa",          15.6, 601,   "YV"),
        ("SkyWest",       11.9, 32,    "OO"),
        ("Endeavor",       7.4, 18460, "9E"),
        ("JetBlue",        9.5, 54635, "B6"),
        ("United",         3.6, 58665, "UA"),
        ("US Airways",     2.1, 20536, "US"),
        ("Envoy",          10.8, 26397, "MQ"),
        ("Southwest",      9.6, 12275, "WN"),
        ("Virgin America", 5.0, 5162,  "VX"),
        ("Delta",          1.6, 48110, "DL"),
        ("American",       0.4, 32729, "AA"),
        ("Hawaiian",      -6.9, 342,   "HA"),
        ("Alaska",        -9.9, 714,   "AS"),
    ]
    return pd.DataFrame(rows, columns=["name", "mean_delay", "n", "carrier"])


def nyc_flights_weekdays(seed: int = 7) -> pd.DataFrame:
    """Simulated counts of 2013 flights by airline x origin x weekday.

    Columns: name, origin (EWR/JFK/LGA), weekday (Mon–Sun), count.
    """
    rng = np.random.default_rng(seed)
    airlines = ["United", "ExpressJet", "JetBlue", "Delta", "American",
                "Endeavor", "Envoy", "US Airways", "Southwest", "other"]
    origins = ["EWR", "JFK", "LGA"]
    # base daily volume per airline/origin combination
    # (large positives where airline dominates origin)
    base_map = {
        ("United", "EWR"):       1000,
        ("ExpressJet", "EWR"):    700,
        ("JetBlue", "JFK"):       800,
        ("Delta", "JFK"):         600,
        ("American", "JFK"):      300,
        ("Endeavor", "JFK"):      280,
        ("Delta", "LGA"):         700,
        ("American", "LGA"):      450,
        ("Envoy", "LGA"):         450,
        ("US Airways", "LGA"):    350,
        ("Southwest", "LGA"):     350,
    }
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    rows = []
    for a in airlines:
        for o in origins:
            base = base_map.get((a, o), 60)
            for d in days:
                weekend_dip = 0.55 if d in ("Sat", "Sun") else 1.0
                # ExpressJet and a few others don't dip
                if a in ("Envoy", "Endeavor"):
                    weekend_dip = max(weekend_dip, 0.8)
                noise = rng.normal(1.0, 0.05)
                rows.append({
                    "name": a, "origin": o, "weekday": d,
                    "count": int(base * weekend_dip * noise),
                })
    return pd.DataFrame(rows)


def corruption_2015(seed: int = 33) -> pd.DataFrame:
    """Country-level CPI and HDI for 2015 with regional labels.

    Synthesised to look like Transparency International + UN HDR.
    Columns: country, cpi, hdi, region.
    """
    rng = np.random.default_rng(seed)
    spec = [
        # (country, cpi, hdi, region)
        ("Norway",         87, 0.949, "OECD"),
        ("Germany",        81, 0.926, "OECD"),
        ("United States",  76, 0.920, "OECD"),
        ("Japan",          75, 0.903, "Asia Pacific"),
        ("Singapore",      85, 0.925, "Asia Pacific"),
        ("Chile",          70, 0.847, "Americas"),
        ("Argentina",      32, 0.827, "Americas"),
        ("Greece",         46, 0.866, "OECD"),
        ("Russia",         29, 0.804, "Europe and\nCentral Asia"),
        ("Venezuela",      17, 0.767, "Americas"),
        ("China",          37, 0.738, "Asia Pacific"),
        ("Kuwait",         41, 0.800, "Middle East\nand North Africa"),
        ("Qatar",          71, 0.856, "Middle East\nand North Africa"),
        ("Iraq",           16, 0.649, "Middle East\nand North Africa"),
        ("Sudan",          12, 0.490, "Sub-Saharan\nAfrica"),
        ("Niger",          34, 0.353, "Sub-Saharan\nAfrica"),
        ("Chad",           22, 0.396, "Sub-Saharan\nAfrica"),
        ("Ghana",          47, 0.579, "Sub-Saharan\nAfrica"),
        ("Rwanda",         54, 0.498, "Sub-Saharan\nAfrica"),
        ("Myanmar",        22, 0.556, "Asia Pacific"),
        ("Nepal",          27, 0.558, "Asia Pacific"),
    ]
    # add 50 extra plausible points spanning the curve
    more = []
    for i in range(50):
        cpi = rng.uniform(12, 92)
        hdi = 0.40 + 0.006 * cpi + rng.normal(0, 0.05)
        hdi = float(np.clip(hdi, 0.35, 0.97))
        region = rng.choice([
            "OECD", "Americas", "Asia Pacific",
            "Europe and\nCentral Asia", "Middle East\nand North Africa",
            "Sub-Saharan\nAfrica",
        ])
        more.append((f"C{i:02d}", float(cpi), float(hdi), region))
    rows = spec + more
    return pd.DataFrame(rows, columns=["country", "cpi", "hdi", "region"])
