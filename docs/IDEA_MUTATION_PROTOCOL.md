# Idea Mutation Protocol

This repo expects ideas to evolve.

A changed idea is not automatically scope creep. It may be a refinement, side-grade, escalation, fork, or replacement.

## Core rule

Do not overwrite the trail.

When the project changes direction, record what changed, what stayed, why it changed, and what test or build should happen next.

## Mutation types

- **Refinement** — same idea, cleaner version.
- **Side-grade** — different approach in the same lane.
- **Escalation** — bigger or more advanced version of the same lane.
- **Fork** — related branch worth preserving separately.
- **Replacement** — old idea no longer leads; new idea becomes active.
- **Parked** — useful but not active.
- **Rejected** — not worth using under current evidence.

## Lane classification

Every major mutation should be classified as one of:

- **Build Lane** — character construction, examples, templates, quality.
- **Foundation Lane** — ACC mechanics, testing, exports, layer behavior.
- **Bridge** — turns foundation findings into build patterns.
- **Parked Mutation** — preserved but inactive.
- **Rejected Assumption** — not safe to build on.

## Mutation note format

```text
Mutation ID:
Previous idea:
New idea:
Type:
Lane:
What changed:
What stayed:
Why it changed:
Evidence or trigger:
Risk:
Next test/build:
Status:
```

## Diagnostic question

Before accepting a mutation, ask:

```text
Is this a genuinely better idea, or did an ACC layer interaction make the old idea look broken?
```

This matters because a character can seem weak when the real issue is reminder bloat, GWI domination, opener bias, lore not loading, thread overrides, or import-state contamination.

## Parking rule

Do not delete strange ideas too early.

If an idea is not active but might become useful, move it to `archive/parked-ideas.md` or a mutation note instead of burying it in chat.
