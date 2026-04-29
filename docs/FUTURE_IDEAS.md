# Future Ideas

This file parks useful ideas that should not disrupt the current restructure/refinement work.

A parked idea is not rejected. It is preserved until the repo spine is stable enough to evaluate it properly.

## GitHub Pages character browser

Idea:

Build a GitHub Pages front end for browsing the Character Library.

Possible features:

- list imported, made, and experimental characters
- show character metadata from `library/character-index.md` or a generated JSON index
- link to character files and build notes
- filter by status, quality, source, and purpose

Why later:

The library structure should stabilize before building a browser on top of it.

## Perchance ACC bridge / output intake

Idea:

Find a way to give an assistant direct access to ACC chat outputs without requiring a full export zip every time.

Possible paths:

- standardized manual paste format
- export zip parser
- browser bookmarklet
- Perchance custom-code export helper
- GitHub Pages intake page
- share-link or `customData.PUBLIC` proof serialization

Why later:

Direct API or bridge work may involve browser sandboxing, CORS, Perchance internal behavior, session state, and unstable undocumented surfaces.

First safer target:

Create a standard intake format that can capture:

```text
character/settings
prompt
reply
thread state
export proof fields if available
screenshots or notes
```

## Direct Perchance API exploration

Idea:

Investigate whether Perchance exposes usable APIs or share-link mechanisms for character or chat transfer.

Why later:

Do not build the repo around undocumented behavior until the internal lab model and library structure are stable.

## Character index automation

Idea:

Automatically generate `library/character-index.md` from per-character metadata files.

Why later:

Manual indexing is simpler until character volume gets large.

## Rule

Before promoting any future idea, re-anchor first:

```text
Does this help build better ACC characters through foundation-level understanding?
Does this belong in Build Lane, Foundation Lane, Library, Tooling, or Parking?
What is the smallest useful version?
```
