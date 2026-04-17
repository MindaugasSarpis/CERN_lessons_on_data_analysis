"""Same 3D scatters without depth cues — unintelligible (Wilke fig 26.4)."""

from __future__ import annotations

from cwilke.chapters.no_3d_jitter.mtcars_3d import render as _render


def render() -> None:
    _render(axes=False, name="mtcars_3d_no_axes")


if __name__ == "__main__":
    render()
