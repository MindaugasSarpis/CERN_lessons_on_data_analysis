# slidev-videos Package (v0.1.0) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate `/home/mindaugas_wsl/slidev-videos` (= github.com/MindaugasSarpis/slidev-videos) with the reusable video pipeline: the `slidev-videos` Python CLI (outreach's `videos.py` behind a `videos.toml` config layer, plus `fetch`, `trim`, and `--repo`-aware gh calls), the `slidev-addon-videos` Slidev addon carrying the merged `VideoPlayer.vue`, a bundled shared-registry stub, tests, an example deck with a Playwright smoke, and CI — tagged `v0.1.0`.

**Architecture:** Lift-and-shift, not rewrite: `src/slidev_videos/pipeline.py` is a byte-copy of outreach `scripts/videos.py` at commit `20196d3`, then patched by an asserted script that swaps ONLY the config/paths layer (module constants → `_init_paths(project)` late-binding, `outreach.toml` walk → `videos.toml` walk, shared registry → bundled package data, bare `gh` → `--repo`-aware) and adds three features (course `fetch`, manifest `trim`, `build --quick` bug fix). `config.py` is the one new module. The addon is a single Vue component authored in this plan (outreach player + course `object-fit: cover` + prod-remotes-first + headmatter config). The example deck reaches the component through a `components/` symlink (the `addons:`-mechanism resolution is verified later, in the course-migration plan).

**Tech Stack:** Python ≥3.11 stdlib only (tomllib, dataclasses); pytest/unittest; Vue 3 SFC on `@slidev/client`; Slidev ^52; playwright-chromium for the example smoke; GitHub Actions.

**Spec:** `/home/mindaugas_wsl/CERN_lessons_on_data_analysis/docs/superpowers/specs/2026-09-01-video-pipeline-package-design.md` — §3 (repo layout), §4 (config model), §4.3 (`trim`), §6 (player), §9 (testing), §10 (error handling). The spec lives in the course repo; this plan lives beside it but ALL implementation commits go to `/home/mindaugas_wsl/slidev-videos` on branch `main`.

## Global Constraints

- Working repo: `/home/mindaugas_wsl/slidev-videos` (fresh scaffold, commit `fc2a434` = README + .gitignore). Commit per task on `main`; **push and tag only in the final task, after all gates**.
- Pipeline source of truth: `/home/mindaugas_wsl/outreach_talks/scripts/videos.py` at commit `20196d3` — copy it, never retype it. Behaviour parity except the config layer and the three named additions; no drive-by refactors.
- Names (exact): pip package `slidev-videos`, module `slidev_videos`, console script `slidev-videos`, npm package `slidev-addon-videos`, config file `videos.toml`, bundled registry `src/slidev_videos/shared.toml`, default shared source `MindaugasSarpis/slidev-videos@videos-shared`.
- `[project]` path defaults must reproduce outreach's talk layout exactly: `slides_dir="."`, `public_dir="public"`, `raw_dir="videos/raw"`, `hq_dir="videos/hq"`, `manifest="videos/manifest.toml"`; web tier dir = `<public_dir>/videos`, HQ link = `<public_dir>/videos-hq`.
- Defaults precedence (highest first): per-video `[[videos]]` → manifest `[defaults]` → project-root `videos.toml` `[defaults]` → ancestor `videos.toml` `[defaults]` (nearest ancestor wins over farther) → built-ins.
- The `.gitignore` blocks `*.mp4/*.mov/...` repo-wide — tests must never create video-named files outside tmp dirs, and the example deck's dummy clip name must not be committed (it is never created).
- Python: stdlib only at runtime; type hints as in the source file; `python3 -m pytest tests -q` green is the per-task gate.
- Every heredoc/patch uses assert-before-write; an anchor mismatch stops the task (report BLOCKED), never guess-edit.

---

## File structure

| File | Responsibility |
|---|---|
| `pyproject.toml` | pip packaging: name, entry point, package-data (`shared.toml`) |
| `src/slidev_videos/__init__.py` | version string only |
| `src/slidev_videos/config.py` | NEW: `videos.toml` discovery, `[project]` paths, ancestor `[defaults]` merge, repo-from-git, shared-source parsing |
| `src/slidev_videos/cli.py` | thin `main()` wrapper around `pipeline.main()` |
| `src/slidev_videos/pipeline.py` | the lifted outreach CLI (patched, see Task 2) |
| `src/slidev_videos/shared.toml` | bundled shared-registry stub (D3 fills the entries) |
| `tests/test_config.py` | config discovery/merge/paths/repo tests |
| `tests/test_clean_plan.py` | ported planner tests (byte-copy + header fix) |
| `tests/test_pipeline_patch.py` | trim args, gh `--repo` injection, fetch parser presence |
| `package.json` | the npm addon: name `slidev-addon-videos`, `files: ["components"]` |
| `components/VideoPlayer.vue` | the merged player (full text in Task 4) |
| `example/slides.md`, `example/package.json`, `example/components` (symlink) | buildable example deck + smoke target |
| `scripts/smoke-example.mjs` | Playwright smoke: component renders, headmatter config reached the chain |
| `.github/workflows/ci.yml` | pytest + example build + smoke |
| `README.md` | rewritten: install, videos.toml reference, day-to-day commands, new-course recipe |

---

### Task 1: Python package skeleton + `config.py` (TDD)

**Files:**
- Create: `pyproject.toml`, `src/slidev_videos/__init__.py`, `src/slidev_videos/cli.py`, `src/slidev_videos/shared.toml`, `src/slidev_videos/config.py`, `tests/test_config.py`

**Interfaces:**
- Produces: `config.load_project(cli_project: str | None) -> Project` where `Project` has attributes `root, slides_dir, public_dir, raw_dir, hq_dir, manifest: Path` and `defaults: dict`; `config.parse_shared(value) -> tuple[str, str] | None` (accepts `"owner/repo@tag"`, returns `(repo, tag)`; `False`/`""`/`None` → `None`); `config.shared_registry_path() -> Path`; `config.CONFIG_NAME = "videos.toml"`. Task 2's `_init_paths()` consumes `Project`.

- [ ] **Step 1: Write the failing tests**

```bash
mkdir -p tests src/slidev_videos
cat > tests/test_config.py <<'EOF'
"""config.py: videos.toml discovery, [project] paths, [defaults] merge chain."""
import subprocess
from pathlib import Path

import pytest

from slidev_videos import config


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def test_find_project_walks_up(tmp_path):
    write(tmp_path / "videos.toml", "[defaults]\n")
    deep = tmp_path / "a" / "b"
    deep.mkdir(parents=True)
    assert config.find_project(deep) == tmp_path


def test_find_project_missing_raises_systemexit(tmp_path):
    with pytest.raises(SystemExit) as e:
        config.find_project(tmp_path)
    assert "videos.toml" in str(e.value)


def test_project_paths_default_to_outreach_talk_layout(tmp_path):
    write(tmp_path / "videos.toml", "[defaults]\n")
    p = config.load_project(str(tmp_path))
    assert p.slides_dir == tmp_path
    assert p.public_dir == tmp_path / "public"
    assert p.raw_dir == tmp_path / "videos" / "raw"
    assert p.hq_dir == tmp_path / "videos" / "hq"
    assert p.manifest == tmp_path / "videos" / "manifest.toml"


def test_project_paths_overridable(tmp_path):
    write(tmp_path / "videos.toml", """
[project]
slides_dir = "lectures/content/slides"
public_dir = "lectures/content/public"
""")
    p = config.load_project(str(tmp_path))
    assert p.slides_dir == tmp_path / "lectures" / "content" / "slides"
    assert p.public_dir == tmp_path / "lectures" / "content" / "public"
    assert p.raw_dir == tmp_path / "videos" / "raw"  # untouched default


def test_defaults_merge_nearest_wins(tmp_path):
    write(tmp_path / "videos.toml", '[defaults]\nmax_size_mb = 100\nweb_long_edge_px = 1920\n')
    talk = tmp_path / "talks" / "T1"
    write(talk / "videos.toml", '[defaults]\nmax_size_mb = 300\n')
    p = config.load_project(str(talk))
    assert p.root == talk
    assert p.defaults["max_size_mb"] == 300          # nearest wins
    assert p.defaults["web_long_edge_px"] == 1920    # inherited from ancestor


def test_repo_from_git_remote(tmp_path):
    write(tmp_path / "videos.toml", "[defaults]\n")
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "remote", "add", "origin",
                    "https://github.com/SomeOwner/some-repo.git"], check=True)
    p = config.load_project(str(tmp_path))
    assert p.defaults["repo"] == "SomeOwner/some-repo"


def test_repo_explicit_beats_git(tmp_path):
    write(tmp_path / "videos.toml", '[defaults]\nrepo = "Explicit/repo"\n')
    p = config.load_project(str(tmp_path))
    assert p.defaults["repo"] == "Explicit/repo"


def test_shared_default_and_parse(tmp_path):
    write(tmp_path / "videos.toml", "[defaults]\n")
    p = config.load_project(str(tmp_path))
    assert p.defaults["shared"] == "MindaugasSarpis/slidev-videos@videos-shared"
    assert config.parse_shared(p.defaults["shared"]) == (
        "MindaugasSarpis/slidev-videos", "videos-shared")
    assert config.parse_shared(False) is None
    assert config.parse_shared("") is None


def test_shared_disable(tmp_path):
    write(tmp_path / "videos.toml", "[defaults]\nshared = false\n")
    p = config.load_project(str(tmp_path))
    assert config.parse_shared(p.defaults["shared"]) is None


def test_shared_registry_path_is_bundled_file():
    path = config.shared_registry_path()
    assert path.name == "shared.toml"
    assert path.is_file()
EOF
```

- [ ] **Step 2: Run to verify failure**

Run: `cd /home/mindaugas_wsl/slidev-videos && python3 -m pytest tests -q`
Expected: collection error — `ModuleNotFoundError: No module named 'slidev_videos'` (pytest itself must be available; if `python3 -m pytest` is missing, `pip install --user pytest` first and note it in the report).

- [ ] **Step 3: Write the packaging files and `config.py`**

```bash
cat > pyproject.toml <<'EOF'
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "slidev-videos"
version = "0.1.0"
description = "Release-hosted video pipeline CLI for Slidev decks (manifest-driven fetch/encode/publish/check)"
requires-python = ">=3.11"
license = { text = "MIT" }

[project.scripts]
slidev-videos = "slidev_videos.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
slidev_videos = ["shared.toml"]
EOF
cat > src/slidev_videos/__init__.py <<'EOF'
__version__ = "0.1.0"
EOF
cat > src/slidev_videos/cli.py <<'EOF'
"""Console entry point: `slidev-videos <subcommand>`."""
import sys


def main() -> None:
    from . import pipeline
    sys.exit(pipeline.main())
EOF
cat > src/slidev_videos/shared.toml <<'EOF'
# Shared clip registry for slidev-videos consumers.
#
# Entries are CERN/space B-roll and CGI sims shared by more than one deck,
# published on this repo's `videos-shared` GitHub Release (1080p H.264 web
# encodes). The initial 33-entry library lands with the shared-library
# encode pass (course spec §5.3); until then this stub keeps `check` and
# `pull --include-shared` well-defined (no shared names).
#
# Naming: lowercase snake_case, no resolution/codec suffixes; CDS clips keep
# their report-number digits (e.g. cern_footage_2022_013_001.mp4).

[defaults]
release_tag = "videos-shared"
repo        = "MindaugasSarpis/slidev-videos"
EOF
cat > src/slidev_videos/config.py <<'EOF'
"""Project discovery and configuration for slidev-videos.

A *project* is any directory tree with a `videos.toml` at its root. The
`[project]` table declares the layout (defaults reproduce the classic
talk layout); `[defaults]` feeds the pipeline and merges over the
`[defaults]` of every `videos.toml` found in ancestor directories
(nearest ancestor wins over farther ones; the project's own file wins
over all ancestors; a manifest's `[defaults]` — merged later by the
pipeline — wins over everything here).
"""
from __future__ import annotations

import re
import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path

CONFIG_NAME = "videos.toml"


@dataclass
class Project:
    root: Path
    slides_dir: Path
    public_dir: Path
    raw_dir: Path
    hq_dir: Path
    manifest: Path
    defaults: dict


def _read(path: Path) -> dict:
    try:
        with path.open("rb") as f:
            return tomllib.load(f)
    except OSError:
        return {}


def find_project(start: Path) -> Path:
    start = Path(start).resolve()
    for p in [start, *start.parents]:
        if (p / CONFIG_NAME).is_file():
            return p
    raise SystemExit(
        f"error: no {CONFIG_NAME} found from {start} upward — "
        f"create one at the project root (see the slidev-videos README)"
    )


def _ancestor_defaults(root: Path) -> dict:
    """[defaults] of every videos.toml strictly above root, nearest wins."""
    chain: list[dict] = []
    for p in root.parents:
        cfg = p / CONFIG_NAME
        if cfg.is_file():
            chain.append(_read(cfg).get("defaults", {}))
    merged: dict = {}
    for d in reversed(chain):   # farthest first, nearest overwrites
        merged.update(d)
    return merged


def repo_from_git(root: Path) -> str | None:
    try:
        url = subprocess.run(
            ["git", "-C", str(root), "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    m = re.search(r"github\.com[:/]([^/\s]+/[^/\s]+?)(?:\.git)?/?$", url)
    return m.group(1) if m else None


def parse_shared(value) -> tuple[str, str] | None:
    """'owner/repo@tag' -> (owner/repo, tag); false-y or malformed -> None."""
    if not value or not isinstance(value, str):
        return None
    repo, sep, tag = value.partition("@")
    if not sep or "/" not in repo or not tag:
        return None
    return repo, tag


def load_project(cli_project: str | None = None) -> Project:
    start = Path(cli_project) if cli_project else Path.cwd()
    root = find_project(start)
    data = _read(root / CONFIG_NAME)
    proj = data.get("project", {})
    defaults = {**_ancestor_defaults(root), **data.get("defaults", {})}
    defaults.setdefault("shared", "MindaugasSarpis/slidev-videos@videos-shared")
    if "repo" not in defaults:
        r = repo_from_git(root)
        if r:
            defaults["repo"] = r
    return Project(
        root=root,
        slides_dir=root / proj.get("slides_dir", "."),
        public_dir=root / proj.get("public_dir", "public"),
        raw_dir=root / proj.get("raw_dir", "videos/raw"),
        hq_dir=root / proj.get("hq_dir", "videos/hq"),
        manifest=root / proj.get("manifest", "videos/manifest.toml"),
        defaults=defaults,
    )


def shared_registry_path() -> Path:
    from importlib.resources import files
    return Path(str(files("slidev_videos") / "shared.toml"))
EOF
```

- [ ] **Step 4: Install editable and run the tests**

Run: `cd /home/mindaugas_wsl/slidev-videos && python3 -m pip install --user -e . -q && python3 -m pytest tests -q`
Expected: all `test_config.py` tests PASS. (If `pip install -e` is refused by the environment, `PYTHONPATH=src python3 -m pytest tests -q` is the fallback — note which was used.)

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml src tests
git commit -m "feat: python package skeleton + videos.toml config layer with tests"
```

---

### Task 2: Lift `pipeline.py` from outreach and patch the config layer (+ fetch, trim, --repo, build fix)

**Files:**
- Create: `src/slidev_videos/pipeline.py` (copied then patched), `tests/test_clean_plan.py` (copied then header-patched), `tests/test_pipeline_patch.py`
- Create then delete: `.patch-pipeline.py`

**Interfaces:**
- Consumes: `config.load_project`, `config.parse_shared`, `config.shared_registry_path`, `Project` (Task 1).
- Produces: `pipeline.main(argv=None) -> int` (used by `cli.main`); module globals `TALK, MANIFEST, RAW_DIR, WEB_DIR, HQ_DIR, HQ_LINK_DIR, SLIDES_DIR, GH_REPO_ARGS` bound by `_init_paths(project)`; `VideoEntry` gains `trim: tuple[str, str] | None = None`; `_hms("1:30") -> 90.0`.

- [ ] **Step 1: Copy the two source files at the pinned commit**

```bash
git -C /home/mindaugas_wsl/outreach_talks show 20196d3:scripts/videos.py > src/slidev_videos/pipeline.py
git -C /home/mindaugas_wsl/outreach_talks show 20196d3:scripts/tests/test_clean_plan.py > tests/test_clean_plan.py
wc -l src/slidev_videos/pipeline.py tests/test_clean_plan.py
```
Expected: ~1927 and ~136 lines.

- [ ] **Step 2: Write and run the asserted patch script**

The script below replaces the config layer and adds the three features. Every anchor is asserted with its exact count first; an `AssertionError` means the pinned copy drifted — report BLOCKED with the message.

```bash
cat > .patch-pipeline.py <<'EOF'
from pathlib import Path
P = Path('src/slidev_videos/pipeline.py'); s = P.read_text()
def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:70], s.count(old)); s = s.replace(old, new)

# (1) constants block -> late-bound globals + _init_paths()
rep('''# Talk root = current working directory (a talks/<name>/ dir in the monorepo).
# Monorepo root is located by walking up from TALK looking for outreach.toml.
TALK = Path.cwd().resolve()
MANIFEST = TALK / "videos" / "manifest.toml"
RAW_DIR = TALK / "videos" / "raw"
WEB_DIR = TALK / "public" / "videos"
HQ_DIR = TALK / "videos" / "hq"
HQ_LINK_DIR = TALK / "public" / "videos-hq"
SLIDES_DIR = TALK''',
'''# Project root and layout come from videos.toml (see config.py); main()
# resolves them via config.load_project() and binds these before dispatch.
from . import config as _config

TALK: Path = None          # project root
MANIFEST: Path = None
RAW_DIR: Path = None
WEB_DIR: Path = None       # <public_dir>/videos
HQ_DIR: Path = None
HQ_LINK_DIR: Path = None   # <public_dir>/videos-hq
SLIDES_DIR: Path = None
GH_REPO_ARGS: list[str] = []   # ["--repo", owner/repo] when configured
_PROJECT: "_config.Project" = None


def _init_paths(project: "_config.Project") -> None:
    global TALK, MANIFEST, RAW_DIR, WEB_DIR, HQ_DIR, HQ_LINK_DIR, SLIDES_DIR
    global GH_REPO_ARGS, _PROJECT
    _PROJECT = project
    TALK = project.root
    MANIFEST = project.manifest
    RAW_DIR = project.raw_dir
    WEB_DIR = project.public_dir / "videos"
    HQ_DIR = project.hq_dir
    HQ_LINK_DIR = project.public_dir / "videos-hq"
    SLIDES_DIR = project.slides_dir
    repo = project.defaults.get("repo")
    GH_REPO_ARGS = ["--repo", repo] if repo else []''')

# (2) monorepo-root walk -> videos.toml walk (name kept; 4 call sites live on)
rep('''def _find_monorepo_root(start: Path) -> Path | None:
    for p in [start, *start.parents]:
        if (p / "outreach.toml").exists():
            return p
    return None''',
'''def _find_monorepo_root(start: Path) -> Path | None:
    for p in [start, *start.parents]:
        if (p / _config.CONFIG_NAME).exists():
            return p
    return None''')

# (3) global defaults now come from the resolved project chain
rep('''def _load_global_defaults() -> dict:
    root = _find_monorepo_root(TALK)
    if not root:
        return {}
    global_cfg = root / "outreach.toml"
    try:
        with global_cfg.open("rb") as f:
            return tomllib.load(f).get("defaults", {})
    except OSError:
        return {}''',
'''def _load_global_defaults() -> dict:
    return dict(_PROJECT.defaults) if _PROJECT else {}''')

# (4) shared registry: bundled package data + [defaults].shared source
rep('''    root = _find_monorepo_root(TALK)
    if not root:
        return {}, []
    shared = root / "videos" / "shared.toml"
    if not shared.exists():
        return {}, []
    with shared.open("rb") as f:
        data = tomllib.load(f)
    defaults = {**_load_global_defaults(), **data.get("defaults", {})}
    return defaults, _videos_from_data(data)''',
'''    src = _config.parse_shared(_load_global_defaults().get("shared"))
    if src is None:
        return {}, []
    shared = _config.shared_registry_path()
    if not shared.exists():
        return {}, []
    with shared.open("rb") as f:
        data = tomllib.load(f)
    defaults = dict(data.get("defaults", {}))
    defaults["repo"], defaults["release_tag"] = src
    return defaults, _videos_from_data(data)''')

# (5) gh calls become --repo-aware. Shared-release reads may target another
# repo, so _remote_assets/_remote_asset_sizes gain a repo argument.
rep('''        ["gh", "release", "view", tag, "--json", "assets"],''',
    '''        ["gh", "release", "view", tag, *(["--repo", repo] if repo else GH_REPO_ARGS), "--json", "assets"],''')
rep('def _remote_assets(tag: str) -> dict[str, dict] | None:',
    'def _remote_assets(tag: str, repo: str | None = None) -> dict[str, dict] | None:')
rep('def _remote_asset_sizes(tag: str) -> dict[str, int] | None:',
    'def _remote_asset_sizes(tag: str, repo: str | None = None) -> dict[str, int] | None:')
rep('    assets = _remote_assets(tag)', '    assets = _remote_assets(tag, repo)')
rep('''        ["gh", "release", "view", tag], capture_output=True, text=True''',
    '''        ["gh", "release", "view", tag, *GH_REPO_ARGS], capture_output=True, text=True''')
rep('''            ["gh", "release", "create", tag,''',
    '''            ["gh", "release", "create", tag, *GH_REPO_ARGS,''')
rep('''        cmd = ["gh", "release", "upload", tag, *files, "--clobber"]''',
    '''        cmd = ["gh", "release", "upload", tag, *GH_REPO_ARGS, *files, "--clobber"]''')
rep('''                ["gh", "release", "delete-asset", tag, name, "--yes"]''',
    '''                ["gh", "release", "delete-asset", tag, *GH_REPO_ARGS, name, "--yes"]''')
rep('''def _pull_tier(
    videos: list[VideoEntry],
    dst_dir: Path,
    tag: str,
    force: bool,
    dry_run: bool,
    prune: bool = False,
    protected: set[str] | None = None,
) -> int:''',
'''def _pull_tier(
    videos: list[VideoEntry],
    dst_dir: Path,
    tag: str,
    force: bool,
    dry_run: bool,
    prune: bool = False,
    protected: set[str] | None = None,
    repo: str | None = None,   # shared releases may live on another repo
) -> int:''')
rep('''    remote_sizes = _remote_asset_sizes(tag)
''',
'''    remote_sizes = _remote_asset_sizes(tag, repo)
''')
rep('''        rc = subprocess.call([
            "gh", "release", "download", tag,
            "--pattern", name, "--dir", str(dst_dir), "--clobber",
        ])''',
'''        rc = subprocess.call([
            "gh", "release", "download", tag,
            *(["--repo", repo] if repo else GH_REPO_ARGS),
            "--pattern", name, "--dir", str(dst_dir), "--clobber",
        ])''')
rep('''    return _pull_tier(
        extra, WEB_DIR,
        tag=shared_tag,
        force=args.force, dry_run=args.dry_run, prune=False,
    )''',
'''    return _pull_tier(
        extra, WEB_DIR,
        tag=shared_tag,
        force=args.force, dry_run=args.dry_run, prune=False,
        repo=shared_defaults.get("repo"),
    )''')
rep('''            rc = _pull_tier(
                s_from_release, HQ_DIR,
                tag=s_tag,
                force=args.force, dry_run=args.dry_run, prune=False,
            )''',
'''            rc = _pull_tier(
                s_from_release, HQ_DIR,
                tag=s_tag,
                force=args.force, dry_run=args.dry_run, prune=False,
                repo=shared_defaults.get("repo"),
            )''')
rep('''        shared_assets = _remote_assets(shared_tag) if (shared_tag and has_gh) else None''',
'''        shared_assets = _remote_assets(shared_tag, shared_defaults.get("repo")) if (shared_tag and has_gh) else None''')
rep('''    root = _find_monorepo_root(TALK)
    if not root:
        print("error: not inside a monorepo (no outreach.toml found)", file=sys.stderr)
        return 2

    shared_path = root / "videos" / "shared.toml"''',
'''    root = TALK

    shared_path = _config.shared_registry_path()''')

# (6) VideoEntry gains trim; parse it in _videos_from_data
rep('''    loudnorm: bool | None = None''',
    '''    loudnorm: bool | None = None
    # Optional web-tier trim: ("start", "end") in seconds or M:SS; "" = open
    # end. Applied at encode (-ss input-side, -t duration output-side); the
    # remux profile cuts on keyframes.
    trim: tuple[str, str] | None = None''')
rep('''            loudnorm=v.get("loudnorm"),''',
    '''            loudnorm=v.get("loudnorm"),
            trim=tuple(v["trim"]) if v.get("trim") else None,''')

# (7) trim application in the web encode + a _hms helper
rep('''def _encode_one(entry: VideoEntry, force: bool, default_long_edge: int) -> tuple[VideoEntry, str, int, int]:''',
'''def _hms(t: str) -> float:
    """'90', '1:30' or '0:01:30' -> seconds."""
    parts = [float(x) for x in str(t).split(":")]
    out = 0.0
    for p in parts:
        out = out * 60 + p
    return out


def _trim_args(entry: VideoEntry) -> tuple[list[str], list[str]]:
    """(input-side, output-side) ffmpeg args for entry.trim.

    -ss before -i seeks fast; timestamps reset to 0 after an input seek, so
    the end point becomes an output-side -t duration. remux (-c copy) cuts on
    keyframes — documented; use a re-encode profile for frame-exact cuts.
    """
    if not entry.trim:
        return [], []
    start, end = entry.trim
    pre = ["-ss", str(start)] if str(start) else []
    if not str(end):
        return pre, []
    dur = _hms(end) - (_hms(start) if str(start) else 0.0)
    if dur <= 0:
        raise SystemExit(f"error: trim end <= start for {entry.name}")
    return pre, ["-t", f"{dur:.3f}"]


def _encode_one(entry: VideoEntry, force: bool, default_long_edge: int) -> tuple[VideoEntry, str, int, int]:''')
rep('''    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-nostdin", "-loglevel", "error",
        "-i", str(raw),
        *_profile_args(entry.profile, long_edge, encoder),
        *loudnorm,
        str(tmp),
    ]''',
'''    trim_in, trim_out = _trim_args(entry)
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-nostdin", "-loglevel", "error",
        *trim_in,
        "-i", str(raw),
        *_profile_args(entry.profile, long_edge, encoder),
        *trim_out,
        *loudnorm,
        str(tmp),
    ]''')

# (8) build --sync bug: the build subparser lacked --quick (outreach defect)
rep('''    p_build.add_argument("--dry-run", action="store_true", help="dry-run the sync step")''',
'''    p_build.add_argument("--dry-run", action="store_true", help="dry-run the sync step")
    p_build.add_argument("--quick", action="store_true", help="with --sync: compare by size+modtime instead of MD5")''')

# (9) fetch subcommand (lifted from the course CLI) + parser entry
rep('''# ---------------------------------------------------------------------------
# sync — pull raw files from Google Drive via rclone
# ---------------------------------------------------------------------------''',
'''# ---------------------------------------------------------------------------
# fetch — download a video from a URL (yt-dlp) into raw/ + manifest entry
# ---------------------------------------------------------------------------

def cmd_fetch(args: argparse.Namespace) -> int:
    if not shutil.which("yt-dlp"):
        print("error: yt-dlp not installed. https://github.com/yt-dlp/yt-dlp", file=sys.stderr)
        return 2
    name = args.name if args.name.endswith(".mp4") else f"{args.name}.mp4"
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw = RAW_DIR / name
    if raw.exists() and not args.force:
        print(f"  = {name}: already in raw/ (use --force to re-download)")
    else:
        # Prefer H.264 MP4 <=1080p so the default `remux` profile is a lossless
        # container rewrite (the platform's own encode is already web-friendly).
        fmt = ("bv*[ext=mp4][vcodec^=avc1][height<=1080]+ba[ext=m4a]"
               "/b[ext=mp4][height<=1080]/bv*[height<=1080]+ba/b")
        cmd = ["yt-dlp", "-f", fmt, "--merge-output-format", "mp4",
               "--no-playlist", "-o", str(raw), args.url]
        print(" ".join(cmd))
        if subprocess.call(cmd) != 0:
            return 1

    _, videos = load_manifest()
    if any(v.name == name for v in videos):
        print(f"  = {name}: already in manifest.toml")
        return 0
    used = ", ".join(json.dumps(u) for u in args.used_in)
    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(
            f"\\n[[videos]]\\n"
            f'name    = "{name}"\\n'
            f'profile = "{args.profile}"\\n'
            f"used_in = [{used}]\\n"
            f'notes   = "fetched from {args.url}"\\n'
        )
    print(f"  + manifest entry appended for {name} (profile {args.profile})")
    print(f"  next: slidev-videos encode --only {name} && slidev-videos publish --only {name}")
    return 0


# ---------------------------------------------------------------------------
# sync — pull raw files from Google Drive via rclone
# ---------------------------------------------------------------------------''')
rep('''    p_enc = sub.add_parser("encode", help="ffmpeg raw -> web")''',
'''    p_fetch = sub.add_parser("fetch", help="yt-dlp a URL into raw/ + append a manifest entry")
    p_fetch.add_argument("url")
    p_fetch.add_argument("--name", required=True, help="target file name (\\".mp4\\" appended if missing)")
    p_fetch.add_argument("--profile", default="remux")
    p_fetch.add_argument("--used-in", nargs="*", default=[], dest="used_in", metavar="LNN")
    p_fetch.add_argument("--force", action="store_true", help="re-download even if raw exists")
    p_fetch.set_defaults(func=cmd_fetch)

    p_enc = sub.add_parser("encode", help="ffmpeg raw -> web")''')

# (10) main(): global --project, resolve the project before dispatch
rep('''def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)''',
'''def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="slidev-videos", description=__doc__)
    parser.add_argument("--project", default=None,
                        help="project directory (default: walk up from cwd for videos.toml)")
    sub = parser.add_subparsers(dest="cmd", required=True)''')
rep('''    args = parser.parse_args(args_list)
    return args.func(args)''',
'''    args = parser.parse_args(args_list)
    _init_paths(_config.load_project(args.project))
    return args.func(args)''')

P.write_text(s)

# tests/test_clean_plan.py header: import from the package
T = Path('tests/test_clean_plan.py'); t = T.read_text()
old = '''import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from videos import LocalFile, VideoEntry, plan_clean, reclaimed_bytes  # noqa: E402'''
assert t.count(old) == 1
t = t.replace(old, '''import unittest

from slidev_videos.pipeline import LocalFile, VideoEntry, plan_clean, reclaimed_bytes''')
old2 = "        from videos import CleanCandidate"
assert t.count(old2) == 1
t = t.replace(old2, "        from slidev_videos.pipeline import CleanCandidate")
T.write_text(t)
print('patched ok')
EOF
python3 .patch-pipeline.py && rm .patch-pipeline.py
python3 -c "import ast; ast.parse(open('src/slidev_videos/pipeline.py').read()); print('pipeline parses')"
```
Expected: `patched ok` then `pipeline parses`.

- [ ] **Step 3: Write the patch-behaviour tests**

```bash
cat > tests/test_pipeline_patch.py <<'EOF'
"""Behaviour added by the config-layer patch: trim args, gh --repo, fetch parser."""
from pathlib import Path

import pytest

from slidev_videos import config, pipeline
from slidev_videos.pipeline import VideoEntry, _hms, _trim_args


def entry(**kw):
    return VideoEntry(name=kw.pop("name", "x.mp4"),
                      profile=kw.pop("profile", "standard"), used_in=[], **kw)


def test_hms():
    assert _hms("90") == 90.0
    assert _hms("1:30") == 90.0
    assert _hms("0:01:30") == 90.0


def test_trim_args_start_and_end():
    pre, out = _trim_args(entry(trim=("0:20", "1:50")))
    assert pre == ["-ss", "0:20"]
    assert out == ["-t", "90.000"]


def test_trim_args_open_end_and_none():
    assert _trim_args(entry(trim=("0:05", ""))) == (["-ss", "0:05"], [])
    assert _trim_args(entry()) == ([], [])


def test_trim_end_before_start_exits():
    with pytest.raises(SystemExit):
        _trim_args(entry(trim=("2:00", "1:00")))


def make_project(tmp_path, extra_defaults=""):
    (tmp_path / "videos.toml").write_text("[defaults]\n" + extra_defaults, encoding="utf-8")
    (tmp_path / "videos" ).mkdir(exist_ok=True)
    (tmp_path / "videos" / "manifest.toml").write_text("[defaults]\n", encoding="utf-8")
    return config.load_project(str(tmp_path))


def test_init_paths_binds_layout_and_repo(tmp_path):
    p = make_project(tmp_path, 'repo = "Owner/repo"\n')
    pipeline._init_paths(p)
    assert pipeline.TALK == tmp_path
    assert pipeline.WEB_DIR == tmp_path / "public" / "videos"
    assert pipeline.HQ_LINK_DIR == tmp_path / "public" / "videos-hq"
    assert pipeline.GH_REPO_ARGS == ["--repo", "Owner/repo"]


def test_load_manifest_inherits_project_defaults(tmp_path):
    p = make_project(tmp_path, 'max_size_mb = 123\n')
    pipeline._init_paths(p)
    defaults, videos = pipeline.load_manifest()
    assert defaults["max_size_mb"] == 123
    assert videos == []


def test_shared_manifest_reads_bundled_registry(tmp_path):
    p = make_project(tmp_path)   # default shared source
    pipeline._init_paths(p)
    shared_defaults, shared_videos = pipeline.load_shared_manifest()
    assert shared_defaults["release_tag"] == "videos-shared"
    assert shared_defaults["repo"] == "MindaugasSarpis/slidev-videos"
    assert shared_videos == []   # stub registry has no entries yet


def test_shared_disabled(tmp_path):
    p = make_project(tmp_path, "shared = false\n")
    pipeline._init_paths(p)
    assert pipeline.load_shared_manifest() == ({}, [])


def test_repo_threading_signatures():
    import inspect
    assert "repo" in inspect.signature(pipeline._remote_assets).parameters
    assert "repo" in inspect.signature(pipeline._remote_asset_sizes).parameters
    assert "repo" in inspect.signature(pipeline._pull_tier).parameters


def test_parser_has_fetch_and_project_and_build_quick(capsys):
    with pytest.raises(SystemExit):
        pipeline.main(["--help"])
    out = capsys.readouterr().out
    assert "fetch" in out and "--project" in out
    with pytest.raises(SystemExit):
        pipeline.main(["build", "--help"])
    assert "--quick" in capsys.readouterr().out
EOF
```

- [ ] **Step 4: Run the whole suite**

Run: `cd /home/mindaugas_wsl/slidev-videos && python3 -m pytest tests -q`
Expected: PASS — the ported `test_clean_plan.py` (12 tests) plus the new files, no skips. `pipeline.main(["--help"])` must NOT require a project (argparse exits before `_init_paths`).

- [ ] **Step 5: CLI smoke against a throwaway consumer project**

```bash
cd "$(mktemp -d)" && printf '[defaults]\n' > videos.toml && mkdir -p videos && printf '[defaults]\n' > videos/manifest.toml && printf 'slide with <VideoPlayer src="ghost.mp4" />\n' > deck.md
python3 -m slidev_videos.cli 2>/dev/null; python3 -c "import sys; from slidev_videos import pipeline; sys.exit(pipeline.main(['check']))"; echo "check exit=$? (expect 1: UNKNOWN REF ghost.mp4)"
cd /home/mindaugas_wsl/slidev-videos
```
Expected: check prints `UNKNOWN REF: ghost.mp4` and exits 1 — proving discovery, manifest load and the slide scan work end-to-end without outreach's layout.

- [ ] **Step 6: Commit**

```bash
git add src/slidev_videos/pipeline.py tests/test_clean_plan.py tests/test_pipeline_patch.py
git commit -m "feat: lift outreach pipeline behind the videos.toml config layer (+fetch, trim, --repo, build --quick)"
```

---

### Task 3: The addon — `package.json` + merged `VideoPlayer.vue` + example deck

**Files:**
- Create: `package.json` (repo root — replaces nothing; the scaffold has none), `components/VideoPlayer.vue`, `example/slides.md`, `example/package.json`, `example/components` (symlink → `../components`)

**Interfaces:**
- Consumes: nothing from Tasks 1–2 (independent surface).
- Produces: component props `src, fallback, loop, muted, controls, hq, volume, fit`; headmatter config contract `videos: { repo, release, shared, fit, hq }` with `VITE_VIDEO_REPO / VITE_VIDEO_RELEASE / VITE_VIDEO_SHARED_RELEASE / VITE_VIDEO_SHARED_REPO` as fallback; Task 4's smoke asserts the headmatter values reach the resolved chain.

- [ ] **Step 1: Root `package.json` (the npm addon) and example scaffolding**

```bash
cat > package.json <<'EOF'
{
  "name": "slidev-addon-videos",
  "version": "0.1.0",
  "type": "module",
  "description": "Slidev addon: full-bleed VideoPlayer streaming from GitHub Release assets with a local/remote fallback chain",
  "repository": { "type": "git", "url": "https://github.com/MindaugasSarpis/slidev-videos.git" },
  "license": "MIT",
  "keywords": ["slidev-addon", "video"],
  "files": ["components", "README.md"],
  "scripts": {
    "build:example": "slidev build example/slides.md --out dist --base /",
    "smoke": "node scripts/smoke-example.mjs"
  },
  "devDependencies": {
    "@slidev/cli": "^52.1.0",
    "@slidev/theme-default": "latest",
    "playwright-chromium": "^1.49.0"
  }
}
EOF
mkdir -p example scripts
ln -s ../components example/components
cat > example/slides.md <<'EOF'
---
theme: default
routerMode: hash
videos:
  repo: ExampleOwner/example-repo
  release: videos-example
  shared: false
  fit: cover
---

# slidev-addon-videos example

The next slide embeds `VideoPlayer` with a clip that does not exist —
the smoke test asserts the resolved URL came from the `videos:` headmatter.

---
hideInToc: true
---

<VideoPlayer src="clip_example.mp4" />

<!-- intentionally nonexistent: the chain must resolve to
     https://github.com/ExampleOwner/example-repo/releases/download/videos-example/clip_example.mp4 -->
EOF
cat > example/package.json <<'EOF'
{ "name": "slidev-videos-example", "private": true, "type": "module" }
EOF
```
Note: `example/slides.md` references `clip_example.mp4` as text only — no video file is ever created (the repo `.gitignore` bans committed video files).

- [ ] **Step 2: Write the merged component**

The full file. Provenance: outreach `components/VideoPlayer.vue` (chain, controls, look-ahead preload, slide-driven playback) merged with the course player's two behaviours (`object-fit: cover` default; production prefers remotes first because deploys strip local `videos/`), plus headmatter config and the `fit` prop. The inert `autoplay` prop is gone by design.

```bash
cat > components/VideoPlayer.vue <<'EOF'
<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useIsSlideActive, useNav, useSlideContext, configs } from '@slidev/client'

// Config resolution (headmatter beats env beats built-ins):
//   videos:                       VITE_VIDEO_REPO
//     repo: owner/repo            VITE_VIDEO_RELEASE
//     release: videos-web         VITE_VIDEO_SHARED_REPO + VITE_VIDEO_SHARED_RELEASE
//     shared: owner/repo@tag | false
//     fit: cover | contain
//     hq: false
const CFG = (configs && configs.videos) || {}
const ENV = import.meta.env
const REPO    = CFG.repo    || ENV.VITE_VIDEO_REPO    || ''
const RELEASE = CFG.release || ENV.VITE_VIDEO_RELEASE || 'videos'
function parseShared(v) {
  if (v === false || v === '') return null
  if (typeof v === 'string' && v.includes('@')) {
    const [repo, tag] = v.split('@')
    if (repo.includes('/') && tag) return { repo, tag }
    return null
  }
  return undefined // not configured here — try env, then default
}
let SHARED = parseShared(CFG.shared)
if (SHARED === undefined) {
  if (ENV.VITE_VIDEO_SHARED_RELEASE) {
    SHARED = { repo: ENV.VITE_VIDEO_SHARED_REPO || REPO, tag: ENV.VITE_VIDEO_SHARED_RELEASE }
  } else {
    SHARED = { repo: 'MindaugasSarpis/slidev-videos', tag: 'videos-shared' }
  }
}
const dl = (repo, tag) => repo ? `https://github.com/${repo}/releases/download/${tag}` : ''
const REMOTE_BASE        = dl(REPO, RELEASE)
const SHARED_REMOTE_BASE = SHARED ? dl(SHARED.repo, SHARED.tag) : ''
if (!REMOTE_BASE && !SHARED_REMOTE_BASE && typeof console !== 'undefined') {
  console.warn('[slidev-addon-videos] no repo configured (videos.repo headmatter or VITE_VIDEO_REPO) — only local files will play')
}

const props = defineProps({
  src:      { type: String, required: true },
  fallback: { type: String, default: '' },   // explicit URL override for the own-release step
  loop:     { type: Boolean, default: false },
  muted:    { type: Boolean, default: false },
  controls: { type: Boolean, default: true },
  // Prefer the local visually-lossless venue master (public/videos-hq/<src>)
  // when present. Falls through to the web tier automatically when absent.
  hq:       { type: Boolean, default: undefined },
  // Per-clip playback attenuation (0..1) — the live escape hatch for a clip
  // that plays hot despite loudness-normalized encodes.
  volume:   { type: Number, default: 1 },
  // cover = fill the frame edge-to-edge (default; crops non-16:9 slightly).
  // contain = letterbox instead of cropping (ultra-wide/portrait clips).
  fit:      { type: String, default: '' },
})
const effHq  = computed(() => props.hq === undefined ? (CFG.hq ?? true) : props.hq)
const effFit = computed(() => props.fit || CFG.fit || 'cover')

// Fallback chain. Deploys strip local videos/ (served from the release), so
// PROD probes the remotes first — a guaranteed local 404 only delays playback.
// DEV keeps local copies and probes them first (fast, offline).
const base = computed(() => import.meta.env.BASE_URL || '/')
const hqLocalSrc = computed(() => `${base.value}videos-hq/${props.src}`)
const webLocalSrc = computed(() => `${base.value}videos/${props.src}`)
const webRemoteSrc = computed(() => props.fallback || (REMOTE_BASE ? `${REMOTE_BASE}/${props.src}` : ''))
const sharedRemoteSrc = computed(() => SHARED_REMOTE_BASE ? `${SHARED_REMOTE_BASE}/${props.src}` : '')
const fallbackChain = computed(() => {
  const locals = effHq.value ? [hqLocalSrc.value, webLocalSrc.value] : [webLocalSrc.value]
  const remotes = [webRemoteSrc.value, sharedRemoteSrc.value]
  const chain = (import.meta.env.PROD ? [...remotes, ...locals] : [...locals, ...remotes])
    .filter(Boolean)
  return chain.filter((url, i) => i === 0 || url !== chain[i - 1])
})

const videoRef = ref(null)
const sourceRef = ref(null)
const currentSrc = ref(fallbackChain.value[0] || '')
const status = ref('idle')
const isActive = useIsSlideActive()
const hasBeenActive = ref(false)
const warmed = ref(false)

const mimeType = computed(() => {
  const ext = props.src.split('.').pop()?.toLowerCase()
  if (ext === 'webm') return 'video/webm'
  return 'video/mp4'
})

// --- Custom controls state ---
const playing = ref(false)
const currentTime = ref(0)
const duration = ref(0)
const isMuted = ref(true)
const progressPercent = computed(() => duration.value ? (currentTime.value / duration.value) * 100 : 0)
const controlsVisible = ref(false)

function formatTime(s) {
  if (!isFinite(s)) return '0:00'
  const m = Math.floor(s / 60)
  const sec = Math.floor(s % 60)
  return `${m}:${sec.toString().padStart(2, '0')}`
}

function onTimeUpdate() {
  const v = videoRef.value
  if (!v) return
  currentTime.value = v.currentTime
  duration.value = v.duration || 0
  playing.value = !v.paused
  isMuted.value = v.muted
}

function togglePlay() {
  const v = videoRef.value
  if (!v) return
  if (v.paused) v.play().catch(() => {})
  else v.pause()
  playing.value = !v.paused
}

function toggleMute() {
  const v = videoRef.value
  if (!v) return
  v.muted = !v.muted
  isMuted.value = v.muted
}

function seek(e) {
  const v = videoRef.value
  if (!v || !duration.value) return
  const rect = e.currentTarget.getBoundingClientRect()
  const ratio = (e.clientX - rect.left) / rect.width
  v.currentTime = ratio * duration.value
}

function showControls() { controlsVisible.value = true }
function hideControls() { controlsVisible.value = false }

// --- Fallback chain advance ---
let switching = false
function onError() {
  if (switching || (!hasBeenActive.value && !warmed.value)) return
  const chain = fallbackChain.value
  const idx = chain.indexOf(currentSrc.value)
  if (idx === -1 || idx === chain.length - 1) {
    status.value = 'error'
    return
  }
  switching = true
  status.value = 'loading'
  currentSrc.value = chain[idx + 1]
  nextTick(() => {
    videoRef.value?.load()
    switching = false
  })
}

function syncPlayback() {
  const video = videoRef.value
  if (!video) return
  if (isActive.value) {
    if (!hasBeenActive.value) {
      hasBeenActive.value = true
      if (!warmed.value) {
        status.value = 'loading'
        nextTick(() => videoRef.value?.load())
      }
    }
    video.currentTime = 0
    video.volume = Math.min(1, Math.max(0, props.volume))
    video.muted = true
    video.play().then(() => {
      if (!props.muted) video.muted = false
    }).catch(() => {})
  } else {
    video.pause()
    video.muted = true
    video.currentTime = 0
  }
}

watch(isActive, syncPlayback, { immediate: true })

function onLoaded() {
  status.value = 'ready'
  duration.value = videoRef.value?.duration || 0
  syncPlayback()
}

onMounted(() => {
  // <source> error events don't bubble to <video> on iOS Safari.
  sourceRef.value?.addEventListener('error', onError)
  syncPlayback()
})

// Look-ahead preload for upcoming slides' videos:
//  - PROD: warm the browser cache via <link rel="preload" as="video"> against
//    the most reliable remote (shared release when configured — the own
//    release may 404 for inherited clips).
//  - DEV: attach the <source> early and let the element buffer.
const PRELOAD_AHEAD = 3
const { currentPage } = useNav()
const { $page } = useSlideContext()

const isUpcoming = computed(() => {
  const here = $page?.value
  const now = currentPage?.value
  if (!here || !now) return false
  const distance = here - now
  return distance > 0 && distance <= PRELOAD_AHEAD
})

const shouldPreload = computed(() => import.meta.env.PROD && isUpcoming.value)

watch(() => import.meta.env.DEV && isUpcoming.value, (warm) => {
  if (!warm || warmed.value || hasBeenActive.value) return
  warmed.value = true
  status.value = 'loading'
  nextTick(() => videoRef.value?.load())
}, { immediate: true })

let preloadLink = null
function addPreload() {
  if (preloadLink || typeof document === 'undefined') return
  const url = sharedRemoteSrc.value || webRemoteSrc.value
  if (!url) return
  preloadLink = document.createElement('link')
  preloadLink.rel = 'preload'
  preloadLink.as = 'video'
  preloadLink.href = url
  preloadLink.type = mimeType.value
  document.head.appendChild(preloadLink)
}
function removePreload() {
  if (!preloadLink) return
  preloadLink.remove()
  preloadLink = null
}

watch(shouldPreload, (yes) => yes ? addPreload() : removePreload(), { immediate: true })
onUnmounted(removePreload)
</script>

<template>
  <div class="video-player" @mouseenter="controls && showControls()" @mouseleave="controls && hideControls()" @click="controls && togglePlay()">
    <div v-if="status === 'loading' || status === 'idle'" class="video-status">Loading video&hellip;</div>
    <div v-if="status === 'error'" class="video-status video-error">
      Video not available: <code>{{ src }}</code>
    </div>
    <video
      ref="videoRef"
      :loop="loop"
      muted
      playsinline
      webkit-playsinline
      :preload="warmed || hasBeenActive ? 'auto' : 'none'"
      :style="{ objectFit: effFit }"
      @loadeddata="onLoaded"
      @error="onError"
      @timeupdate="onTimeUpdate"
      @play="playing = true"
      @pause="playing = false"
      :class="{ 'video-ready': status === 'ready' }"
    >
      <source ref="sourceRef" :src="hasBeenActive || warmed ? currentSrc : ''" :type="mimeType" />
    </video>
    <div v-if="controls && status === 'ready'" class="custom-controls" :class="{ visible: controlsVisible }" @click.stop>
      <button class="ctrl-btn" @click="togglePlay">{{ playing ? '⏸' : '▶' }}</button>
      <span class="ctrl-time">{{ formatTime(currentTime) }} / {{ formatTime(duration) }}</span>
      <div class="ctrl-progress" @click="seek">
        <div class="ctrl-progress-fill" :style="{ width: progressPercent + '%' }"></div>
      </div>
      <button class="ctrl-btn" @click="toggleMute">{{ isMuted ? '🔇' : '🔊' }}</button>
    </div>
  </div>
</template>

<style scoped>
.video-player {
  position: absolute;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: black;
  cursor: pointer;
}
.video-player video {
  display: block;
  width: 100%;
  height: 100%;
  /* object-fit set inline from the `fit` prop / videos.fit config:
     cover (default) fills the frame edge-to-edge; contain letterboxes. */
  opacity: 0;
  pointer-events: none;
}
.video-player video.video-ready {
  opacity: 1;
  pointer-events: auto;
}
.video-status {
  position: absolute;
  padding: 2rem;
  opacity: 0.6;
  font-size: 0.9rem;
  color: white;
}
.video-error {
  color: #ef4444;
  opacity: 1;
}
.custom-controls {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 20px;
  background: linear-gradient(transparent, rgba(0,0,0,0.7));
  opacity: 0;
  transition: opacity 0.3s;
  cursor: default;
}
.custom-controls.visible { opacity: 1; }
.ctrl-btn {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
  padding: 4px 8px;
  line-height: 1;
}
.ctrl-btn:hover { opacity: 0.8; }
.ctrl-time {
  color: rgba(255,255,255,0.8);
  font-size: 18px;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  min-width: 120px;
}
.ctrl-progress {
  flex: 1;
  height: 8px;
  background: rgba(255,255,255,0.25);
  border-radius: 4px;
  cursor: pointer;
  position: relative;
}
.ctrl-progress-fill {
  height: 100%;
  background: white;
  border-radius: 4px;
  transition: width 0.1s linear;
}
</style>
EOF
```

- [ ] **Step 3: Install and build the example**

Run: `cd /home/mindaugas_wsl/slidev-videos && corepack enable 2>/dev/null; pnpm install --no-frozen-lockfile && pnpm build:example`
Expected: install succeeds (downloads the Chromium build for playwright-chromium), `slidev build` writes `dist/index.html`. A failed build here is a component compile error — report BLOCKED with the compiler output; do not simplify the component.

- [ ] **Step 4: Commit**

```bash
git add package.json pnpm-lock.yaml components example
git commit -m "feat: slidev-addon-videos player (merged outreach+course behaviours, headmatter config) + example deck"
```

---

### Task 4: Playwright smoke — headmatter config reaches the resolved chain

**Files:**
- Create: `scripts/smoke-example.mjs`

**Interfaces:**
- Consumes: `dist/` from `pnpm build:example`; the example headmatter values `ExampleOwner/example-repo` / `videos-example`.

- [ ] **Step 1: Write the smoke script**

```bash
cat > scripts/smoke-example.mjs <<'EOF'
// Serve dist/ and assert the VideoPlayer on slide 2 resolved its source URL
// from the `videos:` headmatter (custom-config passthrough — spec §6).
import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'
import { extname, join } from 'node:path'
import { chromium } from 'playwright-chromium'

const ROOT = new URL('../dist', import.meta.url).pathname
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.ico': 'image/x-icon' }
const server = createServer(async (req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname)
  if (p.endsWith('/')) p += 'index.html'
  try {
    const body = await readFile(join(ROOT, p))
    res.writeHead(200, { 'content-type': MIME[extname(p)] || 'application/octet-stream' })
    res.end(body)
  } catch {
    res.writeHead(404); res.end('not found')
  }
})
await new Promise((r) => server.listen(4180, r))

const expected = 'https://github.com/ExampleOwner/example-repo/releases/download/videos-example/clip_example.mp4'
let failures = 0
const check = (name, ok, detail = '') => {
  console.log(`${ok ? 'ok ' : 'FAIL'} ${name}${detail ? ` — ${detail}` : ''}`)
  if (!ok) failures++
}

const browser = await chromium.launch()
const page = await browser.newPage()
await page.goto('http://localhost:4180/#/2', { waitUntil: 'load' })
await page.waitForSelector('.video-player', { timeout: 15000 })
// Give the active-slide watcher a beat to attach the <source>.
await page.waitForFunction(() => {
  const s = document.querySelector('.video-player video source')
  return s && s.getAttribute('src')
}, null, { timeout: 15000 })
const src = await page.evaluate(() => document.querySelector('.video-player video source').getAttribute('src'))
check('component rendered', true)
check('headmatter videos: config reached the chain', src === expected, `src=${src}`)
// shared: false must keep the shared release out of the chain entirely.
const preloads = await page.evaluate(() => [...document.querySelectorAll('link[rel="preload"][as="video"]')].map(l => l.href))
check('no shared-release preload when shared: false', !preloads.some(u => u.includes('slidev-videos')), preloads.join(','))

await browser.close()
server.close()
if (failures) { console.error(`${failures} smoke failure(s)`); process.exit(1) }
console.log('SMOKE PASS')
EOF
```

- [ ] **Step 2: Run it**

Run: `cd /home/mindaugas_wsl/slidev-videos && pnpm smoke`
Expected: `ok headmatter videos: config reached the chain` and `SMOKE PASS`. **If the src assertion fails with a URL missing `ExampleOwner`** (i.e. `configs.videos` did not pass through), this is the spec's contingency: report DONE_WITH_CONCERNS stating exactly what `src` was — the controller decides the env-var fallback path. Do not silently switch mechanisms.

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke-example.mjs
git commit -m "test: playwright smoke — headmatter config reaches the player's resolved chain"
```

---

### Task 5: CI workflow + README

**Files:**
- Create: `.github/workflows/ci.yml`
- Rewrite: `README.md`

- [ ] **Step 1: CI**

```bash
mkdir -p .github/workflows
cat > .github/workflows/ci.yml <<'EOF'
name: ci
on:
  push: { branches: [main] }
  pull_request:
  workflow_dispatch:
jobs:
  python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -e . pytest
      - run: python -m pytest tests -q
  addon:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 10 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --no-frozen-lockfile
      - run: pnpm build:example
      - run: pnpm smoke
EOF
```

- [ ] **Step 2: Rewrite README.md** — replace the scaffold note wholesale:

```bash
cat > README.md <<'EOF'
# slidev-videos

Release-hosted video pipeline for Slidev decks, in one repo:

- **`slidev-videos`** (Python ≥3.11, stdlib only) — manifest-driven CLI:
  `fetch · sync · encode · encode-hq · publish · publish-hq · pull · pull-hq ·
  check · shared-check · clean · preflight · venue · build`. Web tier is
  1080p H.264 with EBU R128 loudness normalisation; clips are hosted as
  GitHub Release assets.
- **`slidev-addon-videos`** — the full-bleed `VideoPlayer` component with a
  local → own-release → shared-release fallback chain, slide-driven playback,
  look-ahead preload and custom controls.
- **The shared clip library** — `src/slidev_videos/shared.toml` (registry) +
  this repo's `videos-shared` Release (the encodes).

## Install (per consumer repo)

    pip install "slidev-videos @ git+https://github.com/MindaugasSarpis/slidev-videos@v0.1.0"
    pnpm add -D github:MindaugasSarpis/slidev-videos#v0.1.0

Enable the addon and configure the player in the deck headmatter:

    addons:
      - slidev-addon-videos
    videos:
      repo: You/your-course          # own release lives here
      release: videos-web
      shared: MindaugasSarpis/slidev-videos@videos-shared   # or false
      fit: cover                      # or contain

`VITE_VIDEO_REPO / VITE_VIDEO_RELEASE / VITE_VIDEO_SHARED_REPO /
VITE_VIDEO_SHARED_RELEASE` work as an env fallback for decks that prefer
`.env` files.

## videos.toml (project root)

    [project]                # optional — defaults are the classic talk layout
    slides_dir = "lectures/content/slides"
    public_dir = "lectures/content/public"

    [defaults]
    repo          = "You/your-course"   # default: origin remote
    release_tag   = "videos-web"
    source_remote = "gdrive:your/raws"  # for `sync`
    # web_long_edge_px = 1920, max_size_mb = 200, loudnorm = true, ...

Manifest (`videos/manifest.toml`) entries:

    [[videos]]
    name    = "clip.mp4"
    profile = "standard"          # remux | standard | standard-tight | silent-loop | high-motion
    used_in = ["L01"]
    trim    = ["0:20", "1:50"]    # optional; remux trims on keyframes
    notes   = "what it shows"

## Day to day

    slidev-videos fetch <url> --name Clip --used-in L05
    slidev-videos encode && slidev-videos publish
    slidev-videos check          # manifest vs slides vs raw/web
    slidev-videos preflight      # what will the deployed deck actually serve?
    slidev-videos pull           # restore local web copies from the release

Run from anywhere inside a project (`videos.toml` is found by walking up), or
pass `--project <dir>`.

## New course, three steps

1. `videos.toml` at the repo root (see above) + an empty `videos/manifest.toml`.
2. Install both packages, add the `addons:` and `videos:` headmatter.
3. Embed clips as `<VideoPlayer src="name.mp4" />` — shared-library names
   stream from this repo's `videos-shared` release with no further setup.

Design spec: `CERN_lessons_on_data_analysis/docs/superpowers/specs/2026-09-01-video-pipeline-package-design.md`.
EOF
```

- [ ] **Step 3: Commit**

```bash
git add .github README.md
git commit -m "chore: CI (pytest + example build + smoke) and real README"
```

---

### Task 6: Final gates, tag, push

- [ ] **Step 1: Full local gate battery**

```bash
cd /home/mindaugas_wsl/slidev-videos
python3 -m pytest tests -q
pnpm build:example && pnpm smoke
python3 -c "import sys; from slidev_videos import pipeline; sys.exit(pipeline.main(['--help']) or 0)" >/dev/null 2>&1; echo "help exit=$? (0 expected)"
git status --short
```
Expected: pytest all green; `SMOKE PASS`; help exit 0; working tree clean (`dist/`, `node_modules/` are ignored).

- [ ] **Step 2: Tag and push (main + tag)**

```bash
git tag v0.1.0
git push origin main v0.1.0
gh run watch --exit-status "$(gh run list --repo MindaugasSarpis/slidev-videos --limit 1 --json databaseId -q '.[0].databaseId')" | tail -3
```
Expected: push accepted; the `ci` workflow (both jobs) green. If CI fails on something environment-only (e.g. browser download), report the log excerpt — do not re-tag; fixes land as new commits and the tag moves only if the controller says so.

---

## Self-review against the spec

- §3 layout: every file in the spec's tree exists except `pipeline.py`'s split into `encode.py/publish.py/...` — the spec itself prescribes lift-and-shift with only the config layer new ("no behavior rewrite"); one `pipeline.py` module honours that and the spec's §3 note. `CHANGELOG.md` deferred to the first post-v0.1.0 change.
- §4.1/§4.2 discovery + precedence: Task 1 tests cover walk-up, nearest-wins ancestors, `[project]` overrides, repo-from-git, shared default/disable.
- §4.3 `trim`: Task 2 (7) with `-ss` input-side + `-t` duration output-side; the spec's literal "`-to` after input" is corrected to `-t end-start` because an input-side seek resets timestamps — same semantics, actually correct ffmpeg usage (ruling recorded in the ledger).
- §4.4 subcommands incl. `fetch`, `--project`: Task 2 (9)(10); outreach's `build --sync` crash fixed (8).
- §4.5 shared awareness: bundled registry + `parse_shared`; the shared release may live on ANOTHER repo, so `_pull_tier`/`_remote_assets`/`_remote_asset_sizes` gain a `repo` parameter threaded at the `pull --include-shared`, `pull-hq --include-shared` and `preflight` call sites; `shared-check` validates the bundled registry (its cross-talk scan over `talks/*` is vacuous outside a monorepo — acceptable). `check`/`clean` keep outreach logic against the bundled names (empty until D3 — tests assert the empty-stub behaviour).
- §6 player: merged component in Task 3 (chain order prod/dev, `fit`, headmatter config with env fallback, no `autoplay`, look-ahead preload, controls); Task 4 smoke verifies the config passthrough the spec flagged for implementation-time verification.
- §9 testing: config tests, ported planner tests, patch-behaviour tests, example build in CI, Playwright smoke. The ffmpeg `testsrc` encode smoke from §9 is NOT here — encoding real output is exercised in D3 (shared-library encode) where ffmpeg work happens for real; deferred deliberately.
- §10 errors: missing-binary messages retained from outreach; `find_project` failure message from Task 1; trim end<=start exits with a named error.
- Placeholder scan: no TBDs; every step carries runnable content.
- Type consistency: `Project` fields used by `_init_paths` match Task 1's dataclass; `parse_shared` return shape matches both consumers; smoke's expected URL matches the example headmatter.
