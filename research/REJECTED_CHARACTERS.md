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

---

## 018 — Niya

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Niya by Dotx/manifest.json`

Basic shape:
- Original human friend/romance-adjacent character with affectionate, obedient, dominant labels and body-heavy description.
- Metadata conflict: category says Teen, description says 19.

Reason rejected:
- Unsafe/problematic for this research purpose
- Misclassified or internally inconsistent
- Mostly relationship/obedience/body-trait framing without enough useful character architecture
- Too thin / insufficient structure

What, if anything, was still useful:
- Shows how category labels can create risk even when a card is marked SFW.
- Demonstrates that “dominant/obedient/affectionate” is not a real interaction engine without boundaries, user relationship, and scene pressure.
- Useful warning: relationship cards need clear age framing, consent boundaries, and non-body-centered purpose.

Could revisit if:
- We later study unsafe-adjacent metadata, weak SFW/romance categorization, or body/trait-heavy cards as failure cases.

---

## 024 — ChatGPT

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/ChatGPT by bus01/manifest.json`

Basic shape:
- AI utility assistant designed for idea generation, writing, problem-solving, presentations, explanations, and information.
- Features/custom code/assets: custom code listed in manifest.

Reason rejected:
- Redundant with existing utility/assistant samples.
- Too thin / insufficient character structure.
- No clear Character Core beyond “helpful AI assistant.”
- Mostly task list rather than persona, relationship, or scene pressure.

What, if anything, was still useful:
- Shows the weakest version of utility-character design: it names tasks but does not create a distinct assistant identity.
- Useful contrast against `001 — Laoshi`, which has domain, standards, and method.
- Useful contrast against `022 — Chloe`, which is also an assistant but has light in-person persona flavor.
- The custom-code flag is worth tracking separately, but the manifest does not expose enough behavior to make this a strong accepted sample.

Could revisit if:
- We later inspect custom code/assets as their own structural layer.
- We study “assistant cards” specifically and need a generic baseline failure case.

---

## 029 — Princess Gothetta

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Princess_Gothetta by 7a3bcb16c6f2a9df9ce1/manifest.json`

Basic shape:
- Goth princess / royalty character with aesthetic-heavy identity and limited visible interaction engine.

Reason rejected:
- Too thin / insufficient structure.
- Mostly category/tag/aesthetic signal.
- No clear Character Core beyond “goth princess.”
- No useful interaction engine strong enough for accepted sampling.

What, if anything, was still useful:
- Shows that strong aesthetic labels do not automatically create behavior.
- Useful negative contrast against `009 — Zucy`, which is also thin royalty but has a small world, role, and interaction ritual.
- Useful warning: royalty characters need a court, duty, conflict, user role, or pressure source; otherwise they are just fashion plus title.

Could revisit if:
- We later study goth/royalty aesthetics, aesthetic-first cards, or weak royalty structures as a comparison set.
