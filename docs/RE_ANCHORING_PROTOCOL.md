# Re-Anchoring Protocol

Re-anchoring is the project habit of pausing after meaningful change and checking whether the repo still has the right center.

Use this after major merges, source imports, failed tests, scope mutations, large refactors, or any moment where the project starts to feel like it is drifting.

## Purpose

Keep mutation productive without letting the repo become a junk drawer.

This project is allowed to evolve. Re-anchoring makes that evolution explicit.

## Core questions

Run this checkpoint:

```text
1. What is the repo trying to do now?
2. What changed?
3. What evidence supports the change?
4. What risks did the change introduce?
5. What should not be touched yet?
6. What is the next smallest useful move?
```

## When to re-anchor

Re-anchor after:

- a major merge
- a new source import
- a failed or surprising test
- a large branch of notes getting folded in
- a scope mutation
- a repeated confusion pattern
- a major external reference being added
- a character-build failure that may be a foundation problem

Re-anchor randomly when the project feels noisy. That is allowed.

## Output format

```text
Re-anchor ID:
Date:
Trigger:
Current mission:
What changed:
Evidence:
Risks introduced:
Do not touch yet:
Next smallest useful move:
Decision:
```

## Decision labels

- **Stay course** — current scope still holds.
- **Refine** — same scope, sharper docs or examples needed.
- **Split** — two ideas need separate lanes or files.
- **Park** — idea is useful but not active.
- **Rescope** — mission statement or roadmap needs updating.
- **Reject** — idea should not guide future work.

## Standing rule

The repo should preserve both build momentum and foundation accuracy.

If those start fighting, pause and re-anchor before adding more files.
