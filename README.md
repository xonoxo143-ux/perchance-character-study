# Perchance ACC Character Build + Foundation Lab

This repo is a Perchance ACC character-building and reverse-engineering lab.

Its goal is to build better Perchance characters by understanding the foundation: ACC layers, field behavior, export evidence, testing methods, and reusable construction patterns.

## Core idea

Better characters through foundation-level understanding.

```text
Build a character
→ notice failure
→ isolate the ACC layer
→ test the layer
→ update the foundation model
→ rebuild better
```

## Front room and lab

The repo has two major spaces:

```text
library/  = the front room: characters to inspect, sort, and use
lab docs  = the back room: research, testing, evidence, templates, and build rules
```

Start in `library/character-index.md` when looking for characters.

Use the lab folders when building, diagnosing, testing, or refining characters:

- `foundation/`
- `build-lane/`
- `docs/`
- `templates/`
- `source-material/`

## Character Library

The Character Library is the human-facing catalog.

It separates:

- `library/imported/` — characters imported from outside sources or copied material
- `library/made/` — characters built deliberately in this project
- `library/experiments/` — unstable builds, prototypes, and test characters

Every character should have an index entry explaining why it is here.

## Two equal lanes

### Build Lane

The Build Lane is for making characters that do not suck.

It contains practical guides, templates, examples, and diagnosis tools for building stronger ACC characters.

Use it when asking:

- What belongs in role/instruction?
- What belongs in reminder?
- What belongs in GWI?
- What belongs in lore?
- How do I avoid flatness, duplication, opener bias, cadence lock, or relationship over-weighting?

### Foundation Lane

The Foundation Lane is for understanding why characters work or fail.

It tracks ACC behavior, field interactions, layer precedence, export evidence, custom-code behavior, confounders, open tests, and documentation drift.

Use it when asking:

- Which layer is controlling this behavior?
- What is confirmed versus provisional?
- What does the export prove?
- What test would settle this?
- Is this character bad, or is a hidden ACC layer overpowering it?

## Re-anchoring rule

After a major merge, source import, failed test, surprising result, or scope mutation, pause and re-anchor before adding more structure.

Re-anchoring asks:

```text
What is the repo trying to do now?
What changed?
What evidence supports the change?
What risks did the change introduce?
What should not be touched yet?
What is the next smallest useful move?
```

Detailed protocol: `docs/RE_ANCHORING_PROTOCOL.md`.

## Source trust model

This repo separates source material from conclusions.

- `source-material/trusted/` — user-tested ACC evidence and compact snapshots.
- `source-material/salvage/` — recovered thread exports and messy-but-useful research remnants.
- `source-material/external/` — public repos, docs, gists, and comparison material.
- `foundation/` — derived working model of ACC mechanics.
- `build-lane/` — practical character-building guidance derived from the foundation.

## Current source priority

1. User-tested ACC cheat sheet and DB snapshot.
2. Salvaged thread export zip.
3. External Perchance/GitHub/SillyTavern references.

External repos are useful, but they do not outrank tested ACC behavior.

## First working rule

Do not treat a character failure as a prose problem until layer behavior has been checked.

A weak character may be weak because of bad writing. It may also be weak because role, reminder, GWI, lore, initial messages, memory, or custom code are fighting each other.

## Project status

This repo began from a copied Perchance URL-to-character generator reference. The original copied README is preserved at:

```text
source-material/external/copied-repo-readme.md
```

The repo is now being restructured into a dual-purpose ACC character build and foundation lab with a library front room.
