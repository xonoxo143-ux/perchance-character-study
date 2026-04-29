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

### Tier 3 — External references

These include public GitHub repos, Perchance docs, gists, SillyTavern importer behavior, Hugging Face packs, and other public examples.

Use Tier 3 sources for:

- format comparison
- import/export mechanics
- tooling ideas
- outside examples
- compatibility notes

Rule:

> External references are useful, but they do not outrank tested ACC behavior.

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

## Interpretation rule

A character problem is not automatically a writing problem.

Before rewriting prose, check whether role, reminder, GWI, initial messages, lore, memory, custom code, or thread overrides are controlling the behavior.
