# Character Index

This is the main place to look for characters in the repo.

## Status labels

- **imported** — came from outside material or copied source.
- **made** — built deliberately in this project.
- **experimental** — prototype, test build, or unstable character.
- **parked** — useful later, not active.
- **retired** — no longer recommended.

## Quality labels

- **unknown** — not evaluated yet.
- **rough** — known issues; useful mainly for study.
- **workable** — usable but needs improvement.
- **strong** — performs well under normal use.
- **reference** — especially useful as a pattern or standard.

## Character table

| Name | Folder | Status | Source | Purpose | Quality | Notes |
|---|---|---:|---|---|---:|---|
| Marker Minimal | `examples/minimal-character.example.jsonc` | experimental | repo starter | smallest clean layer split example | rough | starter example, not a finished character |

## Intake rule

When adding a character, add an entry here first or in the same commit.

Minimum entry:

```text
Name:
Folder/file:
Status:
Source:
Purpose:
Quality:
Notes:
```

## Decision rule

If a character is mainly useful to play or inspect, it belongs in `library/`.

If a character is mainly useful as evidence for a platform behavior test, it belongs in `source-material/` or `examples/` until promoted.
