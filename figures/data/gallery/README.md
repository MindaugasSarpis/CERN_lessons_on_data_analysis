# Raw data of Lecture 7's gallery figures

`figures/src/interactive_l07_gallery_data.py` reads these two files and writes
`lectures/content/public/data/l07_gapminder.json` (BubbleChart) and
`l07_volcano.json` (TurningSurface). Both files are kept byte for byte as
downloaded on 9 November 2026.

| File | What it holds | Source | Licence |
|--|--|--|--|
| `gapminder.csv` | 1704 rows: country, continent, year (1952 to 2007, every 5 years), life expectancy at birth (years), population, GDP per person (US$, inflation-adjusted); 142 countries | <https://vincentarelbundock.github.io/Rdatasets/csv/gapminder/gapminder.csv> (Rdatasets), the `gapminder` R package by Jennifer Bryan, <https://github.com/jennybc/gapminder> | the data: Gapminder Foundation, <https://www.gapminder.org/data/>, CC BY 4.0; the excerpt (R package): CC0 |
| `volcano.csv` | Maunga Whau (Mt Eden), Auckland: 87 x 61 heights in metres on a 10 m x 10 m grid (columns `V1` to `V61`); digitised from a topographic map by Ross Ihaka | <https://vincentarelbundock.github.io/Rdatasets/csv/datasets/volcano.csv> (Rdatasets), R's `datasets` package (`volcano`) | part of R: GPL-2 \| GPL-3 |

R's documentation of `volcano`: "These data should not be regarded as accurate."
Its rows are grid lines 10 m apart along x, its columns along y, as
`image(volcano)` draws them.

## The classics: `figures/src/gallery.py`

`figures/src/gallery.py` reads these four files and draws
`viz_gallery_minard.svg` and `viz_gallery_nightingale.svg`
(`python figures/src/gallery.py` prints every number the slides state).
They are kept byte for byte as downloaded from Rdatasets on 9 November 2026.
All four come from the R package HistData (Michael Friendly et al., CRAN,
<https://cran.r-project.org/package=HistData>, licence GPL-2 | GPL-3),
mirrored as CSV by Rdatasets (Vincent Arel-Bundock,
<https://vincentarelbundock.github.io/Rdatasets/>). The numbers themselves are
historical records (the campaign of 1812, the deaths of 1854 to 1856), long out of copyright.

| File | What it holds | Source |
|--|--|--|
| `Minard.troops.csv` | 51 rows: longitude, latitude, survivors, direction (A advance, R retreat) and group (1 to 3) along the path of Napoleon's army in Russia, 1812, as Minard drew it (1869) | <https://vincentarelbundock.github.io/Rdatasets/csv/HistData/Minard.troops.csv>; transcribed by Lee Wilkinson for *The Grammar of Graphics* |
| `Minard.cities.csv` | 20 towns with longitude and latitude, in Minard's spelling | <https://vincentarelbundock.github.io/Rdatasets/csv/HistData/Minard.cities.csv> |
| `Minard.temp.csv` | 9 temperatures on the retreat (degrees Réaumur, as Minard gave them), their longitude, date and days since the reading before; one date is empty and follows from `days` (14 Nov + 10 = 24 Nov) | <https://vincentarelbundock.github.io/Rdatasets/csv/HistData/Minard.temp.csv> |
| `Nightingale.csv` | 24 months, April 1854 to March 1856: the army's average strength and the deaths from preventable (zymotic) disease, wounds and other causes, with annual rates per 1000 | <https://vincentarelbundock.github.io/Rdatasets/csv/HistData/Nightingale.csv>; from Pearson and Short (2007), *Understanding Uncertainty: Mathematics of the Coxcomb* |

HistData's documentation dates Minard's campaign 1815; it was 1812.
