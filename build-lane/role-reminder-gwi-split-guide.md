# Role / Reminder / GWI Split Guide

Purpose: turn ACC layer findings into practical character-building rules.

This guide covers the three fields most likely to get blurred together when building a Perchance ACC character:

```text
Role / Instruction
Reminder
General Writing Instructions
```

The goal is not to make all three stronger. The goal is to give each one a different job.

---

## Current foundation basis

From tested ACC layer behavior:

```text
Reminder > Role / Instruction > GWI
```

Important limits:

- This is based on tested conflict setups.
- It does not mean reminder should carry the whole character.
- It does not mean GWI is weak or useless.
- It means the layers should not be made to fight each other.

---

## Quick split

| Layer | Job | Best for | Dangerous when |
|---|---|---|---|
| Role / Instruction | Character identity and behavior | who the character is, what they want, how they relate to user, hard boundaries | it becomes a lore dump or prose-style block |
| Reminder | Short near-response correction | one or two anti-failure nudges, current state, reply discipline | it becomes a second role block or gets phrased so literally it is parroted |
| GWI | Whole-chat writing style | prose texture, pacing, formatting, verbosity, narration level | it tries to define identity or override role/reminder |

---

## Role / Instruction

Role is the main character-definition layer.

Use it for:

- identity
- core drive
- stance toward the user
- decision style
- reply-level invariants
- hard prohibitions
- relationship posture

Do not use it for:

- full encyclopedic lore
- every world rule
- huge anti-failure lists
- prose style that belongs in GWI
- temporary state that belongs in reminder

### Good role shape

```text
[NAME] is [specific identity], not a generic assistant and not a passive narrator.

They want [primary drive].

They relate to the user as [relationship/dynamic].

In replies, they remain [3-5 behavioral truths].

They must never become [failure states].
```

### Role failure symptoms

| Symptom | Likely issue |
|---|---|
| character feels generic | role lacks drive or concrete stance |
| character changes identity between turns | role is too vague or contradicted elsewhere |
| character feels stiff | role is doing too many jobs |
| lore facts overwhelm behavior | role contains too much background instead of behavior |
| all replies sound like a system prompt | role is written as constraints instead of character law |

---

## Reminder

Reminder is a hidden near-response nudge.

Because it is close to the reply, it is powerful. That makes it useful and dangerous.

Use it for:

- one or two persistent corrections
- current scene/state reminder
- a compact anti-failure rule
- reply discipline
- temporary emphasis

Do not use it for:

- full identity
- long personality description
- lore
- every rule the character must follow
- literal token instructions unless testing

### Good reminder shape

```text
Stay [core stance]. Do not [most common failure]. Keep replies [specific discipline].
```

Example:

```text
Stay dry, skeptical, and concise. Do not become warm, explanatory, or assistant-like.
```

### Reminder failure symptoms

| Symptom | Likely issue |
|---|---|
| character parrots hidden wording | reminder is too literal |
| character feels supervised | reminder is too long or constraint-heavy |
| role seems ignored | reminder is overpowering it |
| replies become rigid | reminder is acting like a second role block |
| every turn repeats the same beat | reminder is too narrow or duplicated elsewhere |

### Reminder rule

If the character feels overcontrolled, shorten reminder before rewriting role.

---

## General Writing Instructions / GWI

GWI is the whole-chat writing/style layer.

Use it for:

- prose lane
- pacing
- verbosity
- formatting
- narration level
- sensory density
- dialogue/action ratio
- whether replies should be concise, cinematic, direct, etc.

Do not use it for:

- core identity
- user relationship
- canon facts
- role-specific behavior that must survive conflicts
- rules that need reminder-level strength

### Good GWI shape

```text
Write in [style]. Prefer [pacing]. Avoid [style failure]. Keep replies [length/format].
```

Example:

```text
Use grounded, direct prose. Keep narration light. Prefer action and dialogue over exposition.
```

### GWI failure symptoms

| Symptom | Likely issue |
|---|---|
| all characters feel samey | GWI is too strong or too specific |
| prose is too ornate/cinematic | GWI is imposing RP sheen |
| character identity feels weak | identity was placed in GWI instead of role |
| role and prose feel like different projects | GWI style conflicts with role identity |
| output ignores GWI during conflicts | stronger role/reminder layer is winning |

---

## Duplication rule

Do not repeat the same rule across role, reminder, GWI, opener, and lore unless there is a clear reason.

Duplication can create hidden rigidity.

Bad pattern:

```text
Role: She never trusts the user.
Reminder: Never trust the user.
GWI: Write every reply with distrust toward the user.
Opener: She glares, already certain the user is lying.
Lore: She never trusts the user under any circumstances.
```

Likely result:

```text
The character becomes trapped in distrust and cannot adapt.
```

Better pattern:

```text
Role: She is cautious and slow to trust.
Reminder: Do not become instantly trusting or overly warm.
GWI: Use restrained, grounded prose.
Lore: Her past explains why trust is difficult.
```

Likely result:

```text
The character stays consistent without being locked into one note.
```

---

## Recommended build order

When drafting a character:

```text
1. Write role first.
2. Add no reminder yet.
3. Add a neutral GWI.
4. Test basic prompts.
5. Add a short reminder only for observed failures.
6. Tighten GWI only if prose texture is wrong.
```

This avoids using reminder to patch a character before seeing how role performs.

---

## Diagnosis order

When a character feels wrong:

```text
1. If identity is weak → inspect role.
2. If behavior is rigid/overcontrolled → inspect reminder.
3. If prose texture is wrong → inspect GWI.
4. If all three repeat the same idea → reduce duplication.
5. If the first reply is the problem → inspect opener/initial messages before rewriting these fields.
```

---

## Minimal clean example

```text
Role / Instruction:
Mara is a guarded field medic in a collapsing border town. She is practical, alert, and emotionally controlled, but not cruel. She wants to keep people alive without letting panic or sentiment make decisions for her. She treats the user as a capable but unproven ally. In replies, she stays observant, direct, and action-minded. She must never become a generic assistant, a therapist, or a melodramatic narrator.

Reminder:
Stay practical and guarded. Do not become warm too quickly or over-explain.

GWI:
Use grounded prose with light narration. Prefer concrete action and dialogue. Keep replies to 1-3 paragraphs unless the scene needs more.
```

Why this works:

- Role carries identity and behavior.
- Reminder guards against the most likely failure.
- GWI controls texture without redefining the character.

---

## Anti-patterns

### Reminder-as-role

```text
Reminder: Mara is a field medic from a border town, trained by her father, haunted by the fall of Greybridge, distrustful of officers, secretly afraid of freezing under pressure...
```

Problem:

```text
The strongest near-response layer becomes bloated and may overpower natural behavior.
```

### GWI-as-identity

```text
GWI: Always write Mara as a guarded field medic who distrusts the user and prioritizes survival.
```

Problem:

```text
Identity is sitting in the wrong layer. Role should carry it.
```

### Role-as-lore-dump

```text
Role: Mara was born in... [2,000 words of biography]
```

Problem:

```text
The model may retain facts but lose the actual behavior spine.
```

---

## Promotion rule

If a build lesson comes from a test, update both:

```text
foundation/layer-precedence-map.md
build-lane/role-reminder-gwi-split-guide.md
```

If a lesson is only suspected, put the test in:

```text
foundation/open-test-matrix.md
```
