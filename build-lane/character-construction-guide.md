# Character Construction Guide

Purpose: turn ACC foundation findings into practical character-building decisions.

## Build principle

Build characters by assigning each ACC layer a clear job.

A strong character is not made by repeating the same idea everywhere. It is made by putting the right kind of information in the right layer.

## Recommended layer split

### Role / Instruction

Use for:

- core identity
- behavioral stance
- relationship to user
- reply-level invariants
- hard prohibitions

Avoid:

- long lore dumps
- too many examples
- vague adjectives with no behavioral consequence
- trying to define every scene or every possible action

### Reminder

Use for:

- short guardrail
- immediate reply discipline
- one or two critical anti-failure rules

Avoid:

- second full role block
- long hidden scripts
- literal phrases that can get parroted
- lore or worldbuilding

### GWI

Use for:

- prose style
- pacing
- formatting
- whole-chat writing preferences

Avoid:

- core identity
- user relationship
- character rules that should live in role

### Initial messages / opener

Use for:

- startup state
- immediate scene/context
- tone demonstration

Avoid:

- over-authoring the whole relationship
- writing the user's side too heavily
- long screenplay-style setups that lock the chat

### Lore

Use for:

- self-contained facts
- world details
- backstory chunks
- structures that do not need to be always-on

Avoid:

- core identity
- critical anti-failure rules
- facts that must affect every reply regardless of retrieval

## Minimal strong build pattern

```text
Role:
[NAME] is [specific identity].
They want [drive].
They relate to the user as [dynamic].
In replies, they remain [3-5 behavioral truths].
They must never become [failure states].

Reminder:
Stay in [core stance]. Do not [most common failure].

GWI:
Write in [style/pacing rules]. Keep replies [length/format].

Initial message:
Short scene or first line that starts the dynamic without locking it.

Lore:
Optional self-contained support facts.
```

## Failure-first rebuild method

When a character feels bad, do not rewrite everything.

1. Identify the failure.
2. Guess the controlling layer.
3. Change the smallest relevant layer.
4. Test with the same prompt.
5. If fixed, document the pattern.
6. If not, escalate to the next layer.

## Common fixes

| Symptom | Likely cause | First fix |
|---|---|---|
| scripted first replies | opener/initial messages too authored | shorten opener first |
| same rhythm every reply | example dialogue cadence lock | remove or reduce examples |
| too theatrical | GWI or opener style overpowering | neutralize GWI and retest |
| ignores core identity | role too weak or identity in lore | move identity into role |
| repeats hidden rule | reminder too literal | rewrite reminder as behavioral nudge |
| lore seems ignored | lore not retrieved or too weak | check `loreIdsUsed`; move critical facts upward |
| different per thread | thread override/import state | inspect thread rows/overrides |

## Build verdict format

```text
Character:
Goal:
Current problem:
Likely layer:
Smallest fix:
Test prompt:
Result:
Promote pattern? yes/no
```
