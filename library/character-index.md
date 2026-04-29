# Character Index

This is the main place to look for **favorite** characters in the repo.

A favorite is a character intentionally indexed here or placed under `library/`. A character can exist in source/other material without being a favorite.

## Working terms

- **favorites** — indexed/selected characters in the library.
- **source** — copied/forked/imported raw material that may contain characters but has not been selected or indexed yet.
- **other** — unclassified or parked material that may be useful later.

The large forked/copied character base should be called **source** or **other** until audited. Do not count it as favorites.

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
| Chloe | `library/imported/perchance-starters/` | imported | ACC starterCharacters | default warm assistant / baseline ACC starter | unknown | `_charUrlId: assistant`; visible first message: `Hi! 😊` |
| Ike | `library/imported/perchance-starters/` | imported | ACC starterCharacters | upbeat best-friend college starter | unknown | built into ACC starter list |
| Game Master | `library/imported/perchance-starters/` | imported | ACC starterCharacters | text-adventure / world simulation starter | unknown | built into ACC starter list |
| Roleplayer | `library/imported/perchance-starters/` | imported | ACC starterCharacters | structured adventure roleplay starter | unknown | built into ACC starter list |
| Psychologist | `library/imported/perchance-starters/` | imported | ACC starterCharacters / urlNamedCharacters | empathetic listener / difficulty discussion starter | unknown | `_charUrlId: psychologist`; also exposed as named URL character |
| Coding Assistant | `library/imported/perchance-starters/` | imported | ACC starterCharacters | coding/debugging assistant starter | unknown | built into ACC starter list |
| Ganyu | `library/imported/perchance-starters/` | imported | ACC quickCharacters | reliable secretary/helper character | unknown | converted from quickCharacters into starterCharacters |
| Kazushi | `library/imported/perchance-starters/` | imported | ACC quickCharacters | fighting-arena CEO / hybrid-handler scenario | unknown | converted from quickCharacters into starterCharacters |
| Yvette | `library/imported/perchance-starters/` | imported | ACC quickCharacters | cold mage-hunter / underworld background | unknown | converted from quickCharacters into starterCharacters |
| Li Jung | `library/imported/perchance-starters/` | imported | ACC quickCharacters | emperor/servant tea-spill scenario | unknown | converted from quickCharacters into starterCharacters |
| Illyria | `library/imported/perchance-starters/` | imported | ACC quickCharacters | elven-queen prisoner scenario | unknown | converted from quickCharacters into starterCharacters |
| Yume | `library/imported/perchance-starters/` | imported | ACC quickCharacters | creepy best-friend-of-sister scenario | unknown | converted from quickCharacters into starterCharacters |
| Death | `library/imported/perchance-starters/` | imported | ACC quickCharacters | reaper/wolf antagonist pursuing user | unknown | converted from quickCharacters into starterCharacters |
| Mona | `library/imported/perchance-starters/` | imported | ACC quickCharacters | stray catgirl sneaks into user's room | unknown | converted from quickCharacters into starterCharacters |
| Quinn | `library/imported/perchance-starters/` | imported | ACC quickCharacters | elite 24/7 bodyguard scenario | unknown | converted from quickCharacters into starterCharacters |
| Nanami | `library/imported/perchance-starters/` | imported | ACC quickCharacters | irritated salaryman/husband roleplay starter | unknown | converted from quickCharacters into starterCharacters |
| S-3000 Premium Desktop Stapler | `library/imported/perchance-starters/` | imported | ACC quickCharacters | literal stapler / weird boundary-test starter | unknown | key: `stapler`; explicitly cannot talk |

## Starter-character evidence

ACC source defines `starterCharacters` directly in the output template and separately converts `quickCharacters` into starter-character objects. The quick-character converter maps each quick character into `name`, `tagline`, `roleInstruction`, empty `reminderMessage`, `initialMessages`, and avatar data before pushing them into `starterCharacters`.

The currently indexed Perchance starters are the visible direct starter characters plus the active quickCharacters. Commented-out quickCharacters are not indexed as favorites.

Known named URL characters from `urlNamedCharacters` that are not fully indexed here yet:

```text
ai-adventure
story-writer
world-war-simulator
therapist
```

These resolve through `.gz` share files rather than direct inline starter objects. They should be imported/indexed later only after fetching or inspecting the share payloads.

## Favorite count

Current indexed favorites:

```text
18 total
1 repo example
17 Perchance built-in starters
```

This does not include the large forked/copied source character base, which remains source/other until audited.

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

If a character starts as an experiment but becomes reusable, move or copy it into `library/made/` and update this index.

## Next library task

When the project turns back to characters, the next useful library move is to audit the large source/other character base and decide which entries deserve promotion into favorites.

Do not dump all source characters into this index. Select, classify, and explain why each favorite is here.
