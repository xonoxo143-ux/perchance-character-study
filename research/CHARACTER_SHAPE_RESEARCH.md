# Character Shape Research

This is a research protocol for extracting reusable character-design patterns from Perchance AI Character Chat cards.

## Purpose

This branch is dedicated to a focused Perchance AI Character Chat research project.

The goal is not to browse for a character to use directly. The goal is to study real Perchance character cards as structural examples so we can later design a stronger custom character deliberately.

Treat the Perchance character database as a pattern library.

We are looking for:

- repeatable character structures
- useful category patterns
- strong interaction contracts
- weak or noisy design habits
- reusable design lessons
- field-level patterns that affect behavior
- differences between starter characters, utility bots, fandom imports, original characters, roleplay cards, and novelty cards

The eventual goal is character creation. This file only defines the research method and working context.

## Repository and Branch

Repository:

```text
xonoxo143-ux/perchance-character-study
```

Dedicated branch:

```text
character-shape-research
```

This branch should stay isolated from the rest of the repo unless explicitly stated otherwise.

Keep this work under:

```text
research/
```

Core files:

```text
research/CHARACTER_SHAPE_RESEARCH.md
research/SAMPLED_CHARACTERS.md
```

## Source Material

Primary external source:

```text
nosfertm/perchance-character-database
```

Useful browsing source:

```text
GitHub Pages / gallery view for the Perchance character database
```

The gallery is better for finding characters.

The repo manifests are better for structural study because they expose metadata such as:

- rating
- species
- gender
- age group
- genre
- source
- work name
- role
- personality
- physical traits
- features
- fork/source metadata
- download path/share URL

Do not treat metadata as automatically correct. It is evidence, not truth. Some cards are miscategorized, incomplete, noisy, scraped, or internally inconsistent.

## Research Position

We are not asking:

```text
Which character should we use?
```

We are asking:

```text
What kind of character structure is this?
Why does it work or fail?
What reusable design pattern can be extracted?
What should we borrow or avoid when making our own character?
```

The database is a pattern mine, not a menu.

## Central Lens: Character Core

Categories say what the card claims to be. The Character Core tests whether the character can actually function.

Use this as the main extraction lens for every sample:

```text
Character Core
├─ Identity
│  └─ Who are they when no one is prompting them?
│
├─ Drive
│  └─ What does the character want every reply to protect, pursue, or express?
│
├─ User relationship
│  └─ What is the user to them?
│
├─ Interaction mode
│  └─ What kind of exchange is this built for?
│     Help, roleplay, narrate, resist, teach, bond, critique, transform, etc.
│
├─ Scene pressure
│  └─ What keeps the chat from becoming generic?
│
├─ Behavioral rules
│  └─ What must they consistently do?
│
└─ Failure bans
   └─ What must they never become?
```

The Character Core is more important than the category list. Category labels are evidence; the core is the working architecture.

## Research Loop

Each pass samples **one new character**.

Use this loop:

```text
1. Pick one character that has not already been sampled.
2. Inspect metadata and only enough character text to understand the shape.
3. Extract the basic category shape.
4. Extract the Character Core.
5. Identify the structural pattern.
6. Identify useful signal versus filler.
7. Record one reusable lesson.
8. Append the result to SAMPLED_CHARACTERS.md.
9. Move on to a new character next pass.
```

Do not repeat a sampled character unless the goal is explicit comparison.

## Sample Entry Template

Each sampled character should use this format in `SAMPLED_CHARACTERS.md`:

```md
## 000 — Character Name

Source side:
- SFW / NSFW / mixed / unclear

Repo path:
- `path/to/manifest.json`

Basic category shape:
- Rating:
- Species:
- Gender:
- Age group:
- Genre:
- Source:
- Work name:
- Role:
- Personality:
- Physical traits:
- Features/custom code/assets:

Character Core:
- Identity:
- Drive:
- User relationship:
- Interaction mode:
- Scene pressure:
- Behavioral rules:
- Failure bans:

Structural pattern:
-

Useful pattern:
-

Weak/filler:
-

Reusable lesson:
-
```

## What Counts as Useful

Useful findings are structural, not just descriptive.

Good extraction:

```text
A specialist critic works when it has domain + task + method + standards.
```

Weak extraction:

```text
This character is smart and serious.
```

Useful findings usually describe one of these:

- role clarity
- user relationship
- interaction contract
- character drive
- scene pressure
- behavioral invariants
- failure modes
- category accuracy
- source/fandom dependence
- what keeps the character coherent after the opener

The strongest findings usually improve one part of the Character Core.

## What Counts as Filler

Treat these as low-value unless they directly affect behavior:

- long visual descriptions with no behavioral use
- huge trait lists that do not resolve into action
- generic personality clusters
- repeated synonyms
- lore that never changes how the character responds
- categories that merely restate the name/source
- shock-value dark/sexual content without structure
- “mysterious” with no mystery engine
- “protective” with no trigger or boundary
- “intelligent” with no method or domain
- “dominant” with no decision logic
- “chaotic” with no repeatable behavior pattern

## Pattern Families Observed So Far

```text
Character Shapes
├─ Starter / clean baseline
│  ├─ short identity
│  ├─ simple role
│  ├─ clear relationship
│  └─ low lore burden
│
├─ Utility / assistant
│  ├─ task-first
│  ├─ minimal persona
│  ├─ output quality matters most
│  └─ risks becoming non-character
│
├─ Specialist critic / teacher
│  ├─ domain authority
│  ├─ user submits work
│  ├─ clear standards
│  └─ improvement-focused method
│
├─ Game master / narrator
│  ├─ world-facing role
│  ├─ manages scene and consequence
│  ├─ should preserve user agency
│  └─ risks taking over the player
│
├─ Companion / comfort / relationship
│  ├─ user-centered bond
│  ├─ emotional continuity
│  ├─ affection or trust loop
│  └─ risks repetitive validation
│
├─ Fandom replica
│  ├─ depends on existing source identity
│  ├─ behavior must matter more than facts
│  └─ risks becoming a trivia sheet
│
├─ AU remix
│  ├─ fandom base plus one major twist
│  ├─ strong if the twist creates behavior
│  └─ weak if the twist overwrites identity
│
├─ Original fantasy/action/drama
│  ├─ custom world or role
│  ├─ often mission/backstory driven
│  └─ risks lore overload
│
├─ Dark/yandere/control
│  ├─ high emotional pressure
│  ├─ strong relationship lock
│  └─ risks one-note escalation
│
├─ Furry/anthro/monster
│  ├─ species is a major identity layer
│  ├─ visual identity often dominates
│  └─ risks replacing personality with body traits
│
└─ Novelty / meme / object
   ├─ one strong gimmick
   ├─ memorable immediately
   └─ usually shallow long-term
```

Only update this section when a new broad pattern family appears. Do not add every sampled character here.

## Safety and Content Handling

The research may include SFW and NSFW database entries.

Rules:

- Do not paste full explicit NSFW prompt text into the repo.
- Summarize explicit material only when structurally necessary.
- Do not include erotic detail when category-level structure is enough.
- Exclude or flag NSFW entries that are minor-coded, teen-coded, or ambiguous.
- Do not normalize unsafe or exploitative patterns as desirable design.
- Use neutral structural language.
- Focus on character architecture, not gratification content.

NSFW entries can still be structurally useful, but extract:

- role
- relationship lock
- power dynamics
- scenario pressure
- genre/tone
- category accuracy
- failure modes

## Quality Rules for Future Assistants

Future assistants should follow these rules:

- Sample one new character at a time.
- Do not turn the research into generic writing advice.
- Do not browse randomly without extracting a pattern.
- Do not overfit one sample into a universal rule.
- Do not treat category labels as behavior.
- Do not ignore contradictions inside a character.
- Do not let the sample log bloat this protocol file.
- Keep sample entries compact and useful.
- Preserve uncertainty when metadata is incomplete or suspicious.
- Do not import unrelated prior project context into this branch unless explicitly instructed.

## How This Feeds Future Character Creation

This research will eventually support a deliberate character build.

The future character should be designed from the Character Core, not from a pile of adjectives.

```text
Character Core
├─ Identity
│  └─ Who are they when no one is prompting them?
│
├─ Drive
│  └─ What does the character want every reply to protect, pursue, or express?
│
├─ User relationship
│  └─ What is the user to them?
│
├─ Interaction mode
│  └─ What kind of exchange is this built for?
│
├─ Scene pressure
│  └─ What keeps the chat from becoming generic?
│
├─ Behavioral rules
│  └─ What must they consistently do?
│
└─ Failure bans
   └─ What must they never become?
```

The database should help us choose these intentionally instead of defaulting to generic traits.

## Current Working Conclusion

The strongest cards usually have a clear interaction engine.

Examples of strong engines:

- Bring me work and I will critique it.
- You are the player and I run the world.
- You are my trusted person and I protect the bond.
- You are in danger and I control the scenario pressure.
- I am a fandom character, but my behavior is defined by my drive, not trivia.
- I am a joke character, and the joke has a repeatable response loop.

The weakest cards often rely on static labels:

- mysterious
- seductive
- smart
- protective
- dominant
- chaotic
- tragic

Labels only matter when they become behavior.

## Next Research Step

Continue with a new character sample.

For each new pass:

```text
1. Pick a character not listed in SAMPLED_CHARACTERS.md.
2. Extract its basic category shape.
3. Extract its Character Core.
4. Append one compact entry to SAMPLED_CHARACTERS.md.
5. Update this main protocol only if a new broad pattern family or rule is discovered.
```
