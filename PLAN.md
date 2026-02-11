# Lecture Style Consistency & Visual Improvement Plan

## Reference Style (from L9, L10, L11, L12)

The target style has these elements:
- **Frontmatter**: `colorSchema: dark`, `background: /background_intro.jpg`, `mermaid: true` (if mermaid used)
- **Cover slide**: `# Dr. Mindaugas Šarpis` → `# Lessons on **Data Analysis** from **CERN**` → `## Lecture Title`
- **Quote slide** after cover: motivational/thematic quote
- **Motivation slide**: bullet list with `##` items explaining why the topic matters
- **Section breaks**: `layout: section` + `hideInToc: true` + `# Section **Name**` (key word bolded)
- **Content slides**: Use card system (`<div class="card card-X pad-tight">`) with emoji headers (`## 📊 **Title**`)
- **Layouts**: `grid-2`, `grid-3` with `gap-md mt-md` for multi-column content
- **Card colors**: `card-primary`, `card-secondary`, `card-accent`, `card-info`, `card-success`, `card-warning` used thematically
- **Padding**: `pad-tight` (most common), `pad-compact` for denser content
- **Note text**: `<div class="note-text">` for annotations/summaries
- **Emojis**: Every card header gets a relevant emoji: `## 🎯 **Purpose**`
- **No `hideInToc: true`** on regular content slides, only on section/quote/special slides

## Tasks

### Phase 1: Fix consistency in already-modified files (L1-L8)

- [x] **L1_Course_Orientation.md** - Review and ensure consistent frontmatter, emoji headers, card usage
- [x] **L3_1_1_Crash_Course_on_Computer_Science.md** - Remove `download: true` unless needed, ensure consistent style
- [x] **L3_1_2_File_Handling_and_Directory_Structure.md** - Review card/emoji consistency
- [x] **L3_2_Command_Line.md** - Review card/emoji consistency (already consistent, no changes needed)
- [x] **L3_3_Markdown.md** - Review card/emoji consistency (already consistent, no changes needed)
- [x] **L4_Computing_Infrastructure.md** - Review card/emoji consistency
- [x] **L5_Crash_Course_on_Python_Programming.md** - Review card/emoji consistency
- [x] **L6_Concepts_of_Data_Analysis.md** - Review; this is the largest file, check for over-styling
- [x] **L7_Data_Visualisation.md** - Review card/emoji consistency
- [x] **L8_Version_Control.md** - Add emoji headers (currently missing), improve card usage

### Phase 2: Skip L2 and LX (special cases)

- L2 is in-class only (3 slides, not examinable) - skip
- LX is a placeholder/template - skip

## Consistency Rules to Apply

1. **Frontmatter order**: background → class → colorSchema → theme → drawings → transition → title → layout
2. **Background**: Always `/background_intro.jpg` (not `./background_default.jpg`)
3. **Emoji format**: Always `## 📊 **Title**` (emoji outside bold)
4. **Card headers**: Every card should have an emoji + bold title
5. **Grid gaps**: Always `gap-md` with grids
6. **Margin top**: `mt-md` after slide titles before content divs
7. **Section slides**: `# Section **KeyWord**` format
8. **Quote slides**: After every cover slide, a thematic quote
9. **No empty lines** between `---` and frontmatter fields like `hideInToc`
10. **Consistent padding**: Use `pad-tight` as default, `pad-compact` only when content is dense

## How to Work

1. Read each file fully
2. Compare against the reference style rules above
3. Fix inconsistencies - focus on visual consistency, not content changes
4. After fixing each file, mark it as done by changing `[ ]` to `[x]`
5. Git commit after each file is done
6. When all Phase 1 tasks are `[x]`, output: <promise>STYLE COMPLETE</promise>
