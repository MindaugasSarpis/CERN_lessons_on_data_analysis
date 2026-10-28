#!/usr/bin/env node
/**
 * gen-review.mjs — emit <out>/ataskaita/index.html: one unlisted page (in
 * Lithuanian) with everything the university's Edukacinių kompetencijų centras
 * asked for in the report on the educational initiative (2025-10-30 –
 * 2026-10-30): every lecture deck, drafts included, their PDFs, the workbook,
 * the lecturer's material, the self-check questions, the code and the
 * literature. Nothing links to it from the landing page or the workbook, and
 * it carries `noindex`, so students keep the weekly release.
 *
 * Draft decks are built by build-all.mjs (--review) into <out>/ataskaita/<slug>/;
 * released decks link to their normal <prefix>/<slug>/. The PDFs are assets of
 * the GitHub release REVIEW_TAG (made once, by hand, from `slidev export` and
 * the workbook printed to PDF).
 *
 * Exported as genReview(); runnable standalone:
 *   node scripts/gen-review.mjs [--out dist] [--base <prefix>]
 */
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const REVIEW_DIR = 'ataskaita';
const REPO = 'https://github.com/MindaugasSarpis/CERN_lessons_on_data_analysis';
const REVIEW_TAG = 'ataskaita-2026-10-30';
const PDF = `${REPO}/releases/download/${REVIEW_TAG}`;
const SITE = 'https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis';

// The ten topics of the application (2025-10-28, section 4.2) and the lectures
// that carry each of them now.
const PLANNED = {
  '01-orientation': 'Įvadas ir supažindinimas su CERN',
  '02-intro-to-data': 'Darbas su bylomis; duomenų analizės projekto organizavimas',
  '03-how-computers-work': 'Kompiuterių mokslo pagrindai',
  '04-command-line-and-files': 'Darbas su bylomis; duomenų analizės projekto organizavimas',
  '05-python-foundations': 'Greitasis Python programavimo kursas; analizės moduliarizavimas',
  '06-version-control': 'Versijų kontrolė',
  '07-python-for-data-and-numpy': 'Greitasis Python programavimo kursas',
  '08-data-visualisation': 'Pagrindinės duomenų analizės mokslo idėjos',
  '09-probability-and-statistics': 'Pagrindinės duomenų analizės mokslo idėjos',
  '10-data-fitting': 'Pagrindinės duomenų analizės mokslo idėjos',
  '11-the-perceptron': 'papildoma tema',
  '12-pandas-and-data-cleaning': 'papildoma tema',
  '13-reproducible-workflows': 'Duomenų analizės srautai – automatizavimas; analizės moduliarizavimas',
  '14-concepts-of-data-analysis': 'Pagrindinės duomenų analizės mokslo idėjos',
  '15-computing-infrastructure': 'Supažindinimas su įprasta ir CERN kompiuterių infrastruktūra',
  '16-machine-learning': 'papildoma tema',
};

const LITERATURE = [
  ['Kursai, kuriais remtasi', [
    'Harvard CS50, <em>Introduction to Computer Science</em>, cs50.harvard.edu',
    'MIT, <em>The Missing Semester of Your CS Education</em>, missing.csail.mit.edu',
    'Software Carpentry, <em>The Unix Shell</em> ir <em>Version Control with Git</em>, software-carpentry.org',
    'HEP Software Foundation, <em>Analysis Essentials</em>, hsf-training.github.io/analysis-essentials',
    'The Turing Way Community, <em>The Turing Way: Guide for Reproducible Research</em>, book.the-turing-way.org',
  ]],
  ['Įrankiai (oficiali dokumentacija)', [
    'S. Chacon, B. Straub, <em>Pro Git</em>, git-scm.com/book',
    '<em>The Python Tutorial</em> ir standartinės bibliotekos dokumentacija, docs.python.org/3',
    'NumPy, Matplotlib, pandas, scikit-learn, conda ir VS Code dokumentacija',
  ]],
  ['Duomenys ir jų vizualizavimas', [
    'C. O. Wilke, <em>Fundamentals of Data Visualization</em>, O’Reilly, 2019, clauswilke.com/dataviz',
    'W. S. Cleveland, <em>The Elements of Graphing Data</em>, Hobart Press, 1994',
    'E. R. Tufte, <em>The Visual Display of Quantitative Information</em>, Graphics Press, 1983',
    'A. Cairo, <em>The Truthful Art</em>, New Riders, 2016',
    'H. Wickham, <em>Tidy Data</em>, Journal of Statistical Software 59 (10), 2014',
    'M. D. Wilkinson et al., <em>The FAIR Guiding Principles for scientific data management and stewardship</em>, Scientific Data 3, 160018 (2016)',
  ]],
  ['Statistika, modelio derinimas, mašininis mokymasis', [
    'J. R. Taylor, <em>An Introduction to Error Analysis</em>, University Science Books, 1997',
    'R. J. Barlow, <em>Statistics: A Guide to the Use of Statistical Methods in the Physical Sciences</em>, Wiley, 1989',
    'G. Cowan, <em>Statistical Data Analysis</em>, Oxford University Press, 1998',
    'J. K. Blitzstein, J. Hwang, <em>Introduction to Probability</em>, CRC Press, 2019',
    'F. Rosenblatt, <em>The Perceptron</em>, Psychological Review 65 (6), 386 (1958)',
    'D. Rumelhart, G. Hinton, R. Williams, <em>Learning representations by back-propagating errors</em>, Nature 323, 533 (1986)',
    'M. Nielsen, <em>Neural Networks and Deep Learning</em>, 2015, neuralnetworksanddeeplearning.com',
    'G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor, <em>An Introduction to Statistical Learning with Applications in Python</em>, Springer, 2023',
  ]],
  ['Mokslinio darbo praktika (paskaitų pavyzdžiai)', [
    'M. Ziemann, Y. Eren, A. El-Osta, <em>Gene name errors are widespread in the scientific literature</em>, Genome Biology 17, 177 (2016)',
    'T. Herndon, M. Ash, R. Pollin, <em>Does high public debt consistently stifle economic growth?</em>, Cambridge Journal of Economics 38, 257 (2014)',
    'ALLEA, <em>The European Code of Conduct for Research Integrity</em>, 2023',
    'R. Feynman, <em>Cargo Cult Science</em>, 1974',
  ]],
];

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const a = (href, text) => `<a href="${esc(href)}">${text}</a>`;

export async function genReview(manifest, outDir, prefix = '') {
  const base = prefix.replace(/\/$/, '');
  const rows = manifest.decks.map((d, i) => {
    const n = String(i + 1).padStart(2, '0');
    const html = d.draft ? `${base}/${REVIEW_DIR}/${d.slug}/` : `${base}/${d.slug}/`;
    const status = d.draft ? 'rengiama, skelbiama pagal tvarkaraštį' : 'paskelbta studentams';
    return `<tr><td class="num">${n}</td><td>${a(html, esc(d.title))}${d.optional ? ' <span class="dim">(papildoma)</span>' : ''}</td>`
      + `<td>${a(`${PDF}/${d.slug}.pdf`, 'PDF')}</td><td class="dim">${esc(PLANNED[d.slug] || '')}</td><td class="dim">${status}</td></tr>`;
  }).join('\n');
  const lecturePages = manifest.decks.map((d, i) =>
    a(`${base}/workbook/lectures/lecture_${i + 1}/`, String(i + 1))).join(' · ');
  const lit = LITERATURE.map(([h, items]) => `<h3>${h}</h3><ul>${items.map((x) => `<li>${x}</li>`).join('')}</ul>`).join('\n');

  const html = `<!doctype html>
<html lang="lt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Parengta medžiaga</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Space+Mono&display=swap">
<style>
:root { --bg:#050507; --fg:#f2f5f9; --fg-2:#c3ccd8; --dim:#8b97a6; --accent:#7dd3fc; --hair:rgba(139,151,166,.18); --panel:rgba(255,255,255,.018); }
* { box-sizing: border-box; }
body { margin: 0; background: radial-gradient(1100px 700px at 78% -8%, rgba(125,211,252,.07), transparent 62%), var(--bg); color: var(--fg);
  font: 16px/1.55 'Space Grotesk', system-ui, sans-serif; }
main { max-width: 1060px; margin: 0 auto; padding: 48px 16px 72px; }
.kicker { font: 12px/1 'Space Mono', monospace; letter-spacing: .14em; text-transform: uppercase; color: var(--dim); }
h1 { font-size: clamp(28px, 4.5vw, 44px); line-height: 1.1; margin: 14px 0 16px; font-weight: 600; }
h2 { font-size: 22px; margin: 44px 0 6px; font-weight: 600; }
h2 .n { color: var(--accent); font: 14px 'Space Mono', monospace; margin-right: 10px; }
h3 { font-size: 16px; margin: 22px 0 6px; color: var(--fg-2); font-weight: 500; }
p { color: var(--fg-2); max-width: 760px; }
a { color: var(--accent); text-decoration: none; border-bottom: 1px solid rgba(125,211,252,.3); }
a:hover { border-bottom-color: var(--accent); }
.dim { color: var(--dim); }
.panel { border: 1px solid var(--hair); background: var(--panel); border-radius: 10px; padding: 18px 20px; margin-top: 14px; }
.wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th { text-align: left; font: 11px 'Space Mono', monospace; letter-spacing: .1em; text-transform: uppercase; color: var(--dim); padding: 8px 10px; border-bottom: 1px solid var(--hair); }
td { padding: 8px 10px; border-bottom: 1px solid var(--hair); vertical-align: top; }
td.num { font-family: 'Space Mono', monospace; color: var(--dim); }
ul { padding-left: 20px; color: var(--fg-2); } li { margin: 4px 0; }
.files li a { font-weight: 500; }
footer { margin-top: 56px; color: var(--dim); font-size: 13px; border-top: 1px solid var(--hair); padding-top: 16px; }
</style>
</head>
<body>
<main>
<div class="kicker">Vilniaus universitetas · Fizikos fakultetas · Edukacinė iniciatyva 2025-10-30 – 2026-10-30</div>
<h1>CERN duomenų analizės dalyko modernizavimas ir metodinės bei išliekamosios medžiagos paruošimas</h1>
<p>Visa iniciatyvos metu parengta medžiaga vienoje vietoje: interaktyvios paskaitų skaidrės ir jų PDF, interaktyvus konspektas (pratybų sąsiuvinis), dėstytojo medžiaga, savikontrolės klausimai, kodas ir literatūra. Kurso medžiaga parengta anglų kalba. Iniciatyvos vadovas – dr. Mindaugas Šarpis.</p>
<p class="dim">Studentams paskaitos skelbiamos kas savaitę ${a(`${base}/`, 'kurso puslapyje')}; čia matomos ir dar neskelbtos paskaitos. PDF failai – 2026-10-30 būsenos kopija, HTML versijos atnaujinamos po kiekvieno užsiėmimo.</p>

<h2><span class="n">1</span>Interaktyvios paskaitų skaidrės: 16 temų</h2>
<p>Kiekviena paskaita – atskiras tinklalapis (Slidev): Python kodas paleidžiamas skaidrėje, rodomi CERN vaizdo įrašai, paskaitos pabaigoje – savikontrolės klausimai. Klavišas <code>O</code> rodo visas paskaitos skaidres vienu metu. Paraiškoje planuota 10 temų (apie 330 skaidrių); parengta 16 paskaitų, apie 1 200 skaidrių.</p>
<div class="panel wrap"><table>
<tr><th>Nr.</th><th>Paskaita</th><th>PDF</th><th>Paraiškos tema</th><th>Būsena</th></tr>
${rows}
</table></div>

<h2><span class="n">2</span>Interaktyvus konspektas (MkDocs)</h2>
<p>Pratybų sąsiuvinis: 16 paskaitų puslapių (planas pagal skaidrių numerius, ką praleisti, savikontrolės klausimai su atsakymais, pagrindinės mintys) ir 15 seminarų po 2 val. trumpais žingsniais, kiekvienoje dalyje – užduotis su paslėptu atsakymu. Mygtukas „▶ Steps“ seminaro puslapyje rodo po vieną žingsnį per visą ekraną.</p>
<div class="panel"><ul class="files">
<li>${a(`${base}/workbook/`, 'Pratybų sąsiuvinis (HTML)')}</li>
<li>${a(`${PDF}/pratybu-sasiuvinis.pdf`, 'Pratybų sąsiuvinis (PDF)')} <span class="dim">– visi puslapiai, atsakymai atskleisti</span></li>
<li>Paskaitų puslapiai: ${lecturePages}</li>
<li>${a(`${base}/workbook/seminars/overview/`, 'Seminarų apžvalga')} ir ${a(`${base}/workbook/setup/`, 'programų diegimas')}</li>
</ul></div>

<h2><span class="n">3</span>Dėstytojo medžiaga</h2>
<div class="panel"><ul class="files">
<li>${a(`${PDF}/kalbetojo-pastabos.pdf`, 'Kalbėtojo pastabos (PDF)')} <span class="dim">– prie kiekvienos skaidrės: ką daryti, sakyti, klausti ir kiek minučių</span></li>
<li>${a(`${REPO}/blob/main/docs/delivery-log.md`, 'Dėstymo žurnalas')} <span class="dim">– po kiekvieno užsiėmimo: kas planuota, kas įvyko, ką pakeista</span></li>
<li>${a(`${REPO}/blob/main/docs/superpowers/specs/2026-10-04-course-rework-first-principles-design.md`, 'Kurso struktūra ir paskaitų standartas')}</li>
<li>${a(`${REPO}/blob/main/docs/seminar-page-recipe.md`, 'Seminaro puslapio sandara')} ir ${a(`${REPO}/blob/main/docs/python-runner-recipe.md`, 'Python kodo skaidrėse taisyklės')}</li>
<li>Pateikimo režimas: paskaitos adresas + <code>/presenter/</code> (pvz., ${a(`${base}/01-orientation/#/presenter/1`, 'Paskaita 1')}) rodo dėstytojui pastabas, laikmatį ir kitą skaidrę</li>
</ul></div>

<h2><span class="n">4</span>Savikontrolės klausimai ir kodas</h2>
<div class="panel"><ul class="files">
<li>${a(`${PDF}/savikontroles-klausimai.pdf`, 'Savikontrolės klausimai su atsakymais (PDF)')} <span class="dim">– visų paskaitų klausimai, pažymėtas teisingas atsakymas ir paaiškinimas</span></li>
<li>${a(REPO, 'Visa kurso medžiaga su pakeitimų istorija (GitHub)')}</li>
<li>${a('https://github.com/MindaugasSarpis/weather-project', 'Pavyzdinis projektas: meteorologinės stoties duomenys')} <span class="dim">– vieša Git repozitorija ir kiekvieno seminaro pradinis aplankas</span></li>
<li>${a(`${REPO}/tree/main/figures/src`, 'Paveikslų scenarijai (Python)')}, ${a(`${REPO}/tree/main/misc/weather_repo`, 'pavyzdinio projekto generavimas')}, ${a(`${REPO}/tree/main/misc/exams`, 'vertinimo scenarijai')}</li>
<li>${a(`${REPO}/tree/main/scripts`, 'Automatinė patikra')} <span class="dim">– pakeitimas paskelbiamas tik tada, kai visos skaidrės telpa ekrane ir paskaita telpa į 2 val.</span></li>
</ul></div>

<h2><span class="n">5</span>Literatūra</h2>
<div class="panel">${lit}</div>

<footer>Sugeneruota ${new Date().toISOString().slice(0, 10)} iš ${a(REPO, 'kurso repozitorijos')} · ${a(`${SITE}/`, 'kurso puslapis')}</footer>
</main>
</body>
</html>
`;
  await mkdir(join(outDir, REVIEW_DIR), { recursive: true });
  await writeFile(join(outDir, REVIEW_DIR, 'index.html'), html);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
  const argv = process.argv.slice(2);
  const opt = (name, def) => { const i = argv.indexOf(name); return i > -1 ? argv[i + 1] : def; };
  const manifest = JSON.parse(await readFile(join(ROOT, 'lectures', 'content', 'decks.json'), 'utf8'));
  await genReview(manifest, resolve(ROOT, opt('--out', 'dist')), opt('--base', ''));
  console.log(`✓ ${REVIEW_DIR}/index.html`);
}
