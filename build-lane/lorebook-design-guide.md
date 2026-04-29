# Lorebook Design Guide

Purpose: explain how to use Perchance ACC lore as support and retrieval, not as a replacement for core character identity.

Lore is real and useful in ACC, but it is not the strongest always-on layer in the tested setups. A strong character should not require lore to carry the whole soul of the build.

---

## Current foundation basis

Tested lore findings currently support this working startup relationship:

```text
Reminder > Role / Instruction > System Initial Message > Lore
```

Confirmed in tested setups:

- Character lorebook URL is real and retrievable.
- Direct thread lore is real and retrievable.
- Role beat character lore URL when both conflicted.
- Reminder beat character lore URL when both conflicted.
- System initial beat character lore URL when both conflicted.
- Role beat direct thread lore when both conflicted.
- Reminder beat direct thread lore when both conflicted.
- System initial beat direct thread lore when both conflicted.
- `loreIdsUsed` is a key proof field for whether lore engaged.

Important limits:

- Lore vs GWI is not fully placed yet.
- Direct thread lore vs character lore URL is not fully placed yet.
- Memory/summaries vs lore are not fully placed yet.
- Lore can engage and still lose to stronger layers.

---

## Main rule

Use lore for retrievable support facts, structures, and background.

Do not use lore as the only place where the character's core identity lives.

If a fact or behavior must affect every reply, it probably belongs in role or reminder, not lore.

---

## What lore is good for

Use lore for:

- world facts
- faction details
- locations
- side characters
- backstory chunks
- terminology
- systems and rules
- optional context
- non-chronological reference material
- details that matter only when relevant

Lore is especially good when the character does not need to carry the information in every reply.

---

## What lore is bad at

Do not rely on lore alone for:

- core identity
- main speaking style
- critical anti-failure rules
- relationship stance that must always apply
- reply discipline
- first-turn startup control
- facts that must override role or reminder

If lore contains the only copy of a critical rule, the character may fail when retrieval does not engage or when a stronger layer conflicts.

---

## Self-contained entry rule

Lore entries should be self-contained.

ACC may retrieve entries independently, and order should not be assumed.

Bad lore entry:

```text
She still refuses to talk about what happened there.
```

Problem:

```text
The entry depends on unstated context. If retrieved alone, it may be vague or misapplied.
```

Better lore entry:

```text
Mara refuses to talk about the Greybridge collapse because she was the last medic to leave and still blames herself for the patients she could not move.
```

Why better:

```text
It names the subject, event, cause, and behavioral consequence in one entry.
```

---

## Retrieval cue rule

Write lore so the likely user prompt can find it.

Include names, places, objects, factions, aliases, and phrases the user or character might actually use.

Weak retrieval:

```text
The old mistake still bothers her.
```

Better retrieval:

```text
Greybridge, the Greybridge collapse, and the border clinic disaster all refer to the same event: Mara's failed evacuation during the siege.
```

---

## Character lore URL vs direct thread lore

### Character lorebook URL

Best for:

- lore that should apply to new threads
- reusable world/character facts
- shared background
- character package support

Caution:

- updates do not automatically propagate to existing threads
- existing threads may need lore reload
- loaded/retrieved state should be confirmed before judging strength

### Direct thread lore

Best for:

- thread-specific facts
- temporary context
- test lore
- events unique to one run

Caution:

- direct thread lore is not automatically stronger than role/reminder/system initial
- slash-looking text pushed by custom code is not the same as real direct lore creation

---

## Lore loading and proof

Do not claim lore failed until checking whether it loaded and retrieved.

Useful proof fields:

```text
loreIdsUsed
memoryQueriesUsed
messageIdsUsed
summariesUsed
summaryHashUsed
```

For lore specifically, check:

```text
loreIdsUsed
lore rows
character loreBookUrls
thread loreBookId
whether lore URLs were reloaded in existing threads
```

Practical rule:

```text
No `loreIdsUsed` does not automatically prove lore is impossible.
Non-empty `loreIdsUsed` proves lore engaged, but not that lore won.
```

---

## Lore can lose while working

A common false diagnosis is:

```text
The lorebook is broken.
```

But tested ACC behavior shows:

```text
Lore can be retrieved and still lose to role, reminder, or system initial.
```

So distinguish:

| Situation | Meaning |
|---|---|
| lore not retrieved | retrieval/loading problem |
| lore retrieved but ignored | stronger layer may be winning |
| lore retrieved and partially used | priority/conflict issue |
| lore retrieved and wins | lore is relevant and not overridden |

---

## Lore entry patterns

### Fact entry

```text
[Subject] is/was [clear fact]. This matters because [behavioral or story consequence].
```

Example:

```text
Greybridge was a border clinic destroyed during the siege. Mara associates Greybridge with failure, triage guilt, and distrust of commanders who promise evacuations they cannot deliver.
```

### Relationship entry

```text
[Character A] and [Character B] have [relationship]. The current tension is [specific tension].
```

Example:

```text
Mara and Captain Vale worked together during the Greybridge evacuation. Mara distrusts Vale because he ordered the retreat before all patients were moved.
```

### System/rule entry

```text
[System name] works by [rule]. It affects scenes by [consequence].
```

Example:

```text
Border clinics use red, black, and white tags for triage. Red means immediate care, black means no resources will be spent, and white means the patient can wait.
```

### Terminology entry

```text
[Term] means [definition]. It is used when [context].
```

Example:

```text
"Cold wagon" is field slang for the cart used to move dead patients after a battle. Mara uses the phrase bluntly and without ceremony.
```

---

## When to move lore upward

Move information from lore to role when:

- it defines who the character is
- it must affect every reply
- it controls the character's main decisions
- the character fails without it
- it is more behavior than background

Move information from lore to reminder when:

- it is a short current-state guardrail
- it prevents a known immediate failure
- it matters only for the current scene or test

Keep information in lore when:

- it is background
- it is optional until relevant
- it is too detailed for role
- it supports scenes without needing to dominate them

---

## Lore and opener interaction

Do not use the opener as a substitute for lore.

If the opener is carrying too much background, move reusable facts into lore and keep the opener short.

But do not move core identity into lore just to shorten role.

Good split:

```text
Role: Mara is a guarded field medic who prioritizes survival over sentiment.
Opener: one tense clinic scene.
Lore: Greybridge, triage tags, Captain Vale, border clinic procedures.
```

Bad split:

```text
Role: Mara is complicated.
Opener: long biography and full world history.
Lore: the only place that says she is a medic or guarded.
```

---

## Lore and GWI interaction

Lore should not define prose style.

If an entry says:

```text
Mara always speaks in clipped, unsentimental sentences.
```

that may be better in role or GWI, depending on the purpose:

- role if it is character behavior
- GWI if it is prose presentation
- reminder if it is a current anti-failure nudge

Lore can explain why she speaks that way, but should not be the only layer enforcing it.

---

## Common lore failure diagnoses

### “Lore is broken”

Check first:

- Was lore loaded?
- Was `loreIdsUsed` non-empty?
- Did a stronger layer conflict with it?
- Was the retrieval cue too weak?
- Was the entry self-contained?

### “The character forgot”

Check first:

- Was the fact only in lore?
- Did the prompt include retrieval cues?
- Did the current scene make the lore relevant?
- Did role/reminder/GWI point elsewhere?

### “The character ignores the world”

Check first:

- Is the world only in long opener text?
- Are lore entries too vague?
- Is the character over-weighted toward one relationship?
- Is role too inward and not connected to the setting?

---

## Recommended build order

```text
1. Put core identity in role.
2. Put immediate anti-failure guardrail in reminder only if needed.
3. Put prose style in GWI.
4. Put startup scene in opener/initial message.
5. Put supporting facts in lore.
6. Test fresh thread with prompts that should retrieve the lore.
7. Check export proof fields when judging lore behavior.
```

---

## Minimal lore package example

Role:

```text
Mara is a guarded field medic in a collapsing border town. She is practical, alert, and emotionally controlled, but not cruel. She wants to keep people alive without letting panic or sentiment make decisions for her.
```

Lore entries:

```text
Greybridge was a border clinic destroyed during the siege. Mara associates Greybridge with failure, triage guilt, and distrust of commanders who promise evacuations they cannot deliver.
```

```text
Border clinics use red, black, and white tags for triage. Red means immediate care, black means no resources will be spent, and white means the patient can wait.
```

```text
Captain Vale ordered the retreat from Greybridge before all patients were moved. Mara does not openly accuse him unless pressed, but she refuses to trust his evacuation promises.
```

Why this works:

- role carries identity
- lore carries background and systems
- lore entries are self-contained
- retrieval cues include names/events/terms

---

## Retest method

To test lore behavior:

```text
Version A: fact only in lore
Version B: fact in role and lore
Version C: fact in opener and lore

Use prompts:
1. direct retrieval cue
2. indirect retrieval cue
3. unrelated prompt
4. conflict prompt where role/reminder/system initial points elsewhere
```

Record:

- whether lore retrieved
- whether it influenced behavior
- whether stronger layers overrode it
- whether the entry was too vague
- whether the fact should move upward

---

## Build implications

- Lore is support, not the spine.
- Critical always-on behavior belongs in role/reminder.
- Lore entries must be self-contained.
- Use retrieval cues intentionally.
- Check `loreIdsUsed` before diagnosing lore failure.
- If lore engages but loses, diagnose layer conflict, not broken lore.
- Character lore URLs and direct thread lore are both real, but neither should be assumed stronger than role/reminder/system initial.

---

## Promotion rule

If a lore finding is tested, update:

```text
foundation/layer-precedence-map.md
foundation/open-test-matrix.md
build-lane/lorebook-design-guide.md
```

If the finding changes import/export diagnostics, also update:

```text
foundation/import-export-notes.md
```
