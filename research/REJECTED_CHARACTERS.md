# Rejected Characters

This file tracks characters inspected during Character Shape Research but not accepted into `SAMPLED_CHARACTERS.md`.

A rejected character is not necessarily bad. It only means the character did not add enough distinct structural value for the current research pass, was redundant with stronger samples, was too thin to study, or was not appropriate for this research purpose.

Rejected characters are still sampled characters. Accepted and rejected entries share the same global sample-number sequence.

The main protocol lives here:

```text
research/CHARACTER_SHAPE_RESEARCH.md
```

Accepted samples live here:

```text
research/SAMPLED_CHARACTERS.md
```

## Rules

- Add rejected characters only after they have been inspected.
- Keep entries compact.
- Do not paste full prompts.
- Do not include explicit NSFW details unless structurally necessary.
- Do not use this file to mock, rank, or shame creators.
- Never renumber accepted samples because of rejects.
- A rejected character may be revisited later if it becomes useful for comparison.
- Rejection means low research value for the current pass, not permanent worthlessness.
- Use the same global sample numbering as accepted samples.

## Rejection Reasons

Use one or more:

- Redundant with existing sample
- Too thin / insufficient structure
- No clear Character Core
- No useful interaction engine
- Mostly category/tag noise
- Misclassified or internally inconsistent
- Unsafe/problematic for this research purpose
- Too dependent on unavailable context
- Better saved for later comparison

## Entry Template

```md
## 000 — Character Name

Source side:
- SFW / NSFW / mixed / unclear

Repo path:
- `path/to/manifest.json`

Basic shape:
-

Reason rejected:
-

What, if anything, was still useful:
-

Could revisit if:
-
```

## Rejected Entries

## 011 — Bosnia Countryball

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Bosnia_Countryball by bmo12/manifest.json`

Basic shape:
- Meme / countryball character defined almost entirely by a hard language constraint: Bosnian only, no English.

Reason rejected:
- Too thin / insufficient structure
- No clear Character Core beyond a single constraint
- No useful interaction engine beyond language friction
- Mostly constraint behavior, not enough character architecture

What, if anything, was still useful:
- Shows that a hard constraint can shape every reply.
- Demonstrates the edge case of a “constraint-only micro-character.”
- Useful warning: a single rule can be memorable, but it is not enough for a durable character unless paired with goal, setting, relationship, or escalation.

Could revisit if:
- We later study language-locked characters, countryball/meme personas, or micro-characters built around one behavioral rule.
