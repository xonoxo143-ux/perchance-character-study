# Roadmap

## Mission

Build better Perchance ACC characters through foundation-level understanding.

This repo should support both hands-on character construction and reverse-engineering of ACC behavior.

## Phase 1 — Stabilize the lab structure

Goal: make the repo coherent before adding more examples or external sources.

Tasks:

- Preserve copied-source material.
- Add source trust model.
- Add Build Lane and Foundation Lane folders.
- Import trusted ACC sources.
- Import salvage material.
- Add first workflow docs.

Success condition:

- A new reader can tell what the repo is for within one minute.
- Tested findings are separated from theories and external references.

## Phase 2 — Derive the foundation model

Goal: convert trusted sources into practical ACC mechanics docs.

Tasks:

- Fill `foundation/layer-precedence-map.md`.
- Fill `foundation/field-behavior-map.md`.
- Fill `foundation/import-export-notes.md`.
- Fill `foundation/known-confounders.md`.
- Fill `foundation/open-test-matrix.md`.

Success condition:

- Every major ACC claim has a confidence label: High, Medium, Provisional, Untested, or Rejected.

## Phase 3 — Build practical character patterns

Goal: turn mechanics into better characters.

Tasks:

- Create role/reminder/GWI split guidance.
- Create lorebook design guidance.
- Create opener and initial-message guidance.
- Create failure diagnosis guide.
- Add minimal/full/experimental examples.

Success condition:

- A character can be drafted from the templates without re-learning the entire foundation model.

## Phase 4 — External comparison

Goal: study outside Perchance-compatible formats without letting them dominate the repo.

Tasks:

- Audit copied Perchance URL-to-character generator source.
- Study SillyTavern Perchance import behavior.
- Compare public character-card patterns against ACC-specific findings.

Success condition:

- External references are mapped to ACC behavior rather than copied blindly.

## Phase 5 — Test harnesses and advanced tooling

Goal: support controlled testing and repeatable evidence collection.

Tasks:

- Collect ACC custom-code harnesses.
- Build test-case templates.
- Track exports and proof fields.
- Explore portable result serialization.

Success condition:

- Future tests are easier to run, compare, and preserve.
