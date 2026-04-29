# Source Trust Model

This repo is built around a strict distinction between evidence, interpretation, and experiments.

## Trust tiers

### Tier 1 — User-tested ACC sources

These are the highest-priority sources.

Examples:

- ACC cheat sheet
- ACC DB snapshot
- raw ACC exports personally tested by the repo owner

Use Tier 1 sources for:

- layer precedence
- field behavior
- export structure
- known confounders
- confirmed and provisional findings

Rule:

> Tier 1 can override public docs or external repo assumptions when the tested condition is clear.

### Tier 2 — Salvaged thread exports

These are useful but may contain messy context, partial theories, reconstructed examples, and parked ideas.

Use Tier 2 sources for:

- theory recovery
- failed ideas
- examples
- mutation history
- test candidates

Rule:

> Salvaged material must be sorted into confirmed, provisional, untested, failed, or parked before becoming guidance.

### Tier 3 — Dev-like public docs and intended mechanics

These include Perchance docs, Rentry guides, dev/community-maintained explanations, and public notes that describe how ACC fields are intended to work.

Use Tier 3 sources for:

- intended field semantics
- documented commands
- supported syntax
- expected reload/update behavior
- custom-code API examples

Rule:

> Public docs explain intended mechanics. They do not automatically prove observed behavior under conflict.

### Tier 4 — External references and public examples

These include public GitHub repos, gists, SillyTavern importer behavior, Hugging Face packs, public character cards, Reddit/Lemmy explanations, and other outside examples.

Use Tier 4 sources for:

- format comparison
- tooling ideas
- outside examples
- compatibility notes
- folk models and edge cases
- future test candidates

Rule:

> External references are useful, but they do not outrank tested ACC behavior.

## Online-doc comparison rule

When public docs and local tests appear to disagree, classify the difference before changing guidance.

Possible classifications:

- intended mechanic versus observed behavior
- normal use versus conflict test
- fresh-thread versus existing-thread state
- documented syntax versus untested behavior difference
- community folk model versus export-backed evidence

Main rule:

```text
Online docs explain what a feature is supposed to do.
Local tests explain what happened when layers conflicted.
```

Use `docs/ONLINE_DOC_COMPARISON.md` for detailed comparisons.

## Confidence labels

Use these labels whenever possible:

- **High** — cleanly supported by controlled tests and/or direct export evidence.
- **Medium** — strongly supported, but with a small confounder or narrower test condition.
- **Provisional** — useful working result, but not clean enough to treat as settled.
- **Untested** — plausible theory with no direct test yet.
- **Rejected** — tested or reasoned against strongly enough to avoid using.
- **Parked** — not active, but worth preserving.

## Evidence rules

- Prefer fresh-thread tests for startup behavior.
- Prefer raw export JSON for proof of chat outcomes.
- Use unnatural token markers when testing layer precedence.
- Change one variable at a time when possible.
- Label imported-thread versus fresh-thread confounds.
- Do not promote a result to canon if startup/loading/runtime confounders remain.
- Do not treat public examples as proof until reproduced in ACC.

## Interpretation rule

A character problem is not automatically a writing problem.

Before rewriting prose, check whether role, reminder, GWI, initial messages, lore, memory, custom code, or thread overrides are controlling the behavior.
