# Roadmap

## Mission

Build better Perchance ACC characters through foundation-level understanding.

This repo should support both hands-on character construction and reverse-engineering of ACC behavior.

## Current structure model

The repo has a front room and a lab.

```text
library/  = front room: characters to inspect, sort, use, and evaluate
lab docs  = back room: foundation, build guides, evidence, templates, and source material
```

## Current status

The main structure is stable.

Completed:

- lab structure
- source trust model
- trusted source import
- salvage import
- re-anchoring protocol
- character library front room
- assistant workflow
- Role / Reminder / GWI guide
- Opener / Initial Messages guide
- Lorebook Design guide
- initial vertical-slice test matrix updates

Next useful work should be content refinement, character indexing, or a specific requested task. Avoid adding more structure unless re-anchoring shows a real need.

## Phase 1 — Stabilize the lab structure

Status: complete enough.

Goal: make the repo coherent before adding more examples or external sources.

Completed tasks:

- Preserve copied-source material.
- Add source trust model.
- Add Build Lane and Foundation Lane folders.
- Import trusted ACC sources.
- Import salvage material.
- Add first workflow docs.
- Add re-anchoring protocol.

Success condition:

- A new reader can tell what the repo is for within one minute.
- Tested findings are separated from theories and external references.

## Phase 2 — Add the Character Library front room

Status: complete enough.

Goal: create one obvious place to look for characters without digging through the lab.

Completed tasks:

- Add `library/README.md`.
- Add `library/character-index.md`.
- Add `library/imported/` for outside/copy-source characters.
- Add `library/made/` for characters built in this project.
- Add `library/experiments/` for tests and prototypes.
- Establish character intake rules.

Success condition:

- A user can find characters from the library index.
- Imported, made, and experimental characters are not mixed together.
- Every listed character has a reason for being in the repo.

## Phase 3 — Derive the foundation model

Status: active, first pass complete.

Goal: convert trusted sources into practical ACC mechanics docs.

Completed / started tasks:

- Tighten `foundation/layer-precedence-map.md`.
- Tighten `foundation/open-test-matrix.md` around the first build slices.
- Keep unresolved questions confidence-labeled.

Remaining candidates:

- Tighten `foundation/field-behavior-map.md`.
- Tighten `foundation/import-export-notes.md`.
- Tighten `foundation/known-confounders.md`.

Success condition:

- Every major ACC claim has a confidence label: High, Medium, Provisional, Untested, or Rejected.
- Open questions have runnable test designs.

## Phase 4 — Build practical character patterns

Status: active, first pass complete.

Goal: turn mechanics into better characters.

Completed tasks:

- Create role/reminder/GWI split guidance.
- Create opener and initial-message guidance.
- Create lorebook design guidance.
- Create failure diagnosis guide.

Remaining candidates:

- Add minimal/full/experimental examples.
- Add made-character build notes once actual characters are built.
- Start filling `library/character-index.md` beyond the starter example.

Success condition:

- A character can be drafted from the templates without re-learning the entire foundation model.

## Phase 5 — External comparison

Status: parked.

Goal: study outside Perchance-compatible formats without letting them dominate the repo.

Tasks:

- Audit copied Perchance URL-to-character generator source.
- Study SillyTavern Perchance import behavior.
- Compare public character-card patterns against ACC-specific findings.

Success condition:

- External references are mapped to ACC behavior rather than copied blindly.

## Phase 6 — Test harnesses and advanced tooling

Status: parked.

Goal: support controlled testing and repeatable evidence collection.

Tasks:

- Collect ACC custom-code harnesses.
- Build test-case templates.
- Track exports and proof fields.
- Explore portable result serialization.
- Park and later evaluate GitHub Pages / Perchance bridge ideas.

Success condition:

- Future tests are easier to run, compare, and preserve.
