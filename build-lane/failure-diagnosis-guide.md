# Failure Diagnosis Guide

Purpose: diagnose why a Perchance ACC character fails before rewriting it.

## First question

Is this a character-writing problem, or a layer-control problem?

Many ACC failures are caused by hidden or stronger layers, not by the character concept itself.

## Diagnosis order

### 1. Reminder

Check first because it is powerful and near-response.

Symptoms:

- character parrots a hidden phrase
- replies are rigid
- one rule dominates everything
- role seems ignored

Fix:

- shorten reminder
- remove literal tokens
- make it a compact guardrail

### 2. Role / Instruction

Symptoms:

- character is generic
- identity changes across turns
- motivation is vague
- relationship to user is unclear

Fix:

- define identity, drive, user dynamic, invariants, and failure states
- avoid lore bloat

### 3. Initial messages / opener

Symptoms:

- first replies feel scripted
- relationship feels pre-decided
- character keeps returning to the opener
- user feels over-authored

Fix:

- shorten opener
- remove prewritten user turns
- keep startup state but loosen the path

### 4. GWI

Symptoms:

- prose feels too theatrical, purple, flat, formal, or assistant-like
- all characters share the same writing texture
- character identity is fine but delivery feels wrong

Fix:

- neutralize GWI and retest
- move identity rules back to role

### 5. Lore

Symptoms:

- background facts vanish
- character knows lore only sometimes
- lore seems weaker than expected

Fix:

- make entries self-contained
- check retrieval fields
- move critical always-on behavior to role/reminder

### 6. Thread state / import state

Symptoms:

- same character acts differently in different threads
- imported thread behaves unlike fresh thread
- old behavior persists after edits

Fix:

- test in fresh thread
- inspect thread overrides
- label imported-thread confounders

### 7. Custom code

Symptoms:

- generated reply changes after appearing
- hidden messages seem to steer output
- slash-looking messages behave unexpectedly

Fix:

- disable custom code for clean tests
- separate runtime tests from startup-layer tests

### 8. Memory / summaries

Symptoms:

- long chats drift
- prior context appears or disappears unpredictably
- behavior changes after enough messages

Fix:

- inspect summary/memory fields
- test fresh short thread versus long thread

## Diagnosis record

```text
Character:
Symptom:
Prompt that caused it:
Suspected layer:
Evidence:
Smallest change:
Retest result:
Conclusion:
Next fix:
```

## Hard rule

Do not rewrite the whole character until the smallest likely layer fix has failed.
