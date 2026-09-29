"""MkDocs hook: a numbered list keeps the number it starts with.

Python-Markdown renders every ordered list from 1, whatever number the source
begins with. The seminar briefs number their steps across sections (Part B
starts at step 4) and refer to steps by number, so the number on the page has
to be the number in the source.

The `sane_lists` extension would do the same, but it also stops a bullet from
continuing a numbered list, which changes how the older pages render.
"""

from markdown.blockprocessors import OListProcessor
from markdown.extensions import Extension


class StartOListProcessor(OListProcessor):
    LAZY_OL = False


class KeepListStart(Extension):
    def extendMarkdown(self, md):
        # Same name and priority as the built-in processor, which it replaces.
        md.parser.blockprocessors.register(StartOListProcessor(md.parser), "olist", 40)


def on_config(config):
    config.markdown_extensions.append(KeepListStart())
    return config
