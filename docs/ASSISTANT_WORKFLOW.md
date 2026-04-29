# Assistant Workflow

This repo is designed to be used by both the project owner and future assistant instances.

The project owner may not read every lab document. Treat the repo as a decision system: use it to stay grounded, diagnose ACC character behavior, and preserve progress without requiring the full chat history.

## First read order

When continuing this project, read in this order:

```text
1. README.md
2. library/character-index.md
3. SOURCE_TRUST_MODEL.md
4. docs/RE_ANCHORING_PROTOCOL.md
5. foundation/layer-precedence-map.md
6. foundation/field-behavior-map.md
7. build-lane/character-construction-guide.md
8. build-lane/failure-diagnosis-guide.md
9. foundation/open-test-matrix.md
```

Then inspect source material only when a claim needs evidence.

## Operating model

The repo has a front room and a lab.

```text
library/      = where characters are cataloged
foundation/   = how ACC behaves
build-lane/   = how to build better characters from that behavior
docs/         = workflow and project rules
templates/    = reusable forms
source-material/ = evidence and recovered material
```

## Default assistant loop

```text
Re-anchor
→ identify lane
→ inspect relevant docs
→ make smallest useful change
→ preserve evidence
→ update index/test/build docs as needed
```

## Lane selection

Use this decision rule:

- Character cataloging or selection → `library/`
- Character construction guidance → `build-lane/`
- ACC mechanics or layer behavior → `foundation/`
- Workflow rules → `docs/`
- Raw evidence → `source-material/`
- Reusable forms → `templates/`
- Later ideas not active yet → `docs/FUTURE_IDEAS.md`

## When diagnosing a character

Do not rewrite the whole character first.

Use this order:

```text
1. Identify the symptom.
2. Check likely controlling layer.
3. Check reminder before role if behavior feels over-constrained.
4. Check opener/initial messages if first replies feel scripted.
5. Check GWI if prose texture is wrong across characters.
6. Check lore retrieval before saying lore failed.
7. Check thread overrides/import state before blaming the build.
8. Make the smallest testable fix.
```

## When adding a character

Every character should have a reason to be here.

Update `library/character-index.md` when adding or promoting a character.

Classify it as:

- imported
- made
- experimental
- parked
- retired

## When adding a finding

Do not turn theory into guidance too early.

Use confidence labels:

- High
- Medium
- Provisional
- Untested
- Rejected
- Parked

If the finding came from an export or test, preserve enough evidence that another assistant can reconstruct the result.

## When the user has a new idea

Do not treat idea mutation as derailment by default.

Ask silently:

```text
Is this Build Lane, Foundation Lane, Bridge, Tooling, Future Idea, or Parked?
```

If it is useful but premature, put it in `docs/FUTURE_IDEAS.md` instead of expanding the repo immediately.

## Re-anchoring trigger

Re-anchor after:

- a merge
- a source import
- a failed test
- a surprising result
- a scope mutation
- a new tooling idea
- repeated confusion

Use `docs/RE_ANCHORING_PROTOCOL.md`.

## Hard rules

- Preserve raw evidence before rewriting conclusions.
- Do not let external examples outrank tested ACC behavior.
- Do not expand structure when an existing file can absorb the change.
- Do not claim a layer hierarchy without confidence labeling.
- Do not confuse character quality problems with ACC layer-control problems.
- Do not assume the project owner has read every doc.

## Useful final response style for this project

When giving next steps, prefer:

```text
Objective
Current state
Risk
Next smallest useful move
```

When a command/build/test fails, provide a compact checkpoint before continuing.
