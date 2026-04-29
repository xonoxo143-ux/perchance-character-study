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

## Phase 1 — Stabilize the lab structure

Status: substantially complete.

Goal: make the repo coherent before adding more examples or external sources.

Tasks:

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

Status: active.

Goal: create one obvious place to look for characters without digging through the lab.

Tasks:

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

Goal: convert trusted sources into practical ACC mechanics docs.

Tasks:

- Tighten `foundation/layer-precedence-map.md`.
- Tighten `foundation/field-behavior-map.md`.
- Tighten `foundation/import-export-notes.md`.
- Tighten `foundation/known-confounders.md`.
- Tighten `foundation/open-test-matrix.md`.

Success condition:

- Every major ACC claim has a confidence label: High, Medium, Provisional, Untested, or Rejected.
- Open questions have runnable test designs.

## Phase 4 — Build practical character patterns

Goal: turn mechanics into better characters.

Tasks:

- Create role/reminder/GWI split guidance.
- Create lorebook design guidance.
- Create opener and initial-message guidance.
- Create failure diagnosis guide.
- Add minimal/full/experimental examples.

Success condition:

- A character can be drafted from the templates without re-learning the entire foundation model.

## Phase 5 — External comparison

Goal: study outside Perchance-compatible formats without letting them dominate the repo.

Tasks:

- Audit copied Perchance URL-to-character generator source.
- Study SillyTavern Perchance import behavior.
- Compare public character-card patterns against ACC-specific findings.

Success condition:

- External references are mapped to ACC behavior rather than copied blindly.

## Phase 6 — Test harnesses and advanced tooling

Goal: support controlled testing and repeatable evidence collection.

Tasks:

- Collect ACC custom-code harnesses.
- Build test-case templates.
- Track exports and proof fields.
- Explore portable result serialization.
- Park and later evaluate GitHub Pages / Perchance bridge ideas.

Success condition:

- Future tests are easier to run, compare, and preserve.
