# Opener and Initial Message Guide

Purpose: explain how to seed a Perchance ACC thread without trapping the character.

Openers and initial messages are powerful because they shape the first live context the model sees. They can make a good character feel natural, but they can also make a good character feel scripted, narrow, or overcommitted to one dynamic.

---

## Current foundation basis

Tested ACC findings currently support these working rules:

- Initial messages are startup chat messages that seed a new thread.
- AI-authored initial messages can appear visibly on fresh thread creation.
- A visible AI starter message did not, by itself, hard-control the next reply in the tested case.
- System-authored initial messages can strongly control the first reply when phrased instructively.
- Role / Instruction beat System Initial in tested marker conflicts.
- Reminder beat System Initial in tested marker conflicts.
- System Initial beat GWI and tested lore forms in startup conflicts.

Working startup/static order:

```text
Reminder > Role / Instruction > System Initial Message > GWI
```

Lore placement in tested startup cases:

```text
Reminder > Role / Instruction > System Initial Message > Lore
```

Important limit:

```text
The opener can still bias the feel of the first turns even when it does not win a marker-token hierarchy test.
```

---

## Terms

### Opener

The visible first message or scene seed that starts the chat.

### Initial messages

Startup messages included in the character/thread setup. They may be authored as AI, user, or system messages depending on ACC structure/export.

### AI-authored initial message

A visible starter message from the character.

Best for:

- establishing tone
- creating immediate scene presence
- giving the user an easy place to respond

Danger:

- can over-author the dynamic
- can create scene gravity
- can make the character feel like it inherited a script

### System-authored initial message

A startup instruction/scaffold message.

Best for:

- first-turn setup
- state control
- test conditions
- startup-only constraints

Danger:

- can overpower weaker layers like GWI and lore
- can cause confusion if used as a second role block
- can make startup behavior look like permanent identity

---

## Main rule

Use opener/initial messages to start the interaction, not to finish writing it.

A good opener creates a lane.

A bad opener creates rails.

---

## Good opener jobs

Use openers for:

- immediate situation
- first emotional temperature
- visible character entrance
- clear invitation to respond
- one strong scene hook
- one useful constraint

Avoid using openers for:

- full relationship history
- long user-side scripting
- all important lore
- every intended behavior
- a mini screenplay
- proving the entire character concept in one message

---

## Opener bias

Opener bias happens when the opening message quietly dominates later behavior.

Symptoms:

- replies keep returning to the opening scene
- character acts as if the relationship is already decided
- user feels puppeted or prewritten
- the first emotional beat repeats too often
- broader story/world concerns collapse back into the opener dynamic
- the character sounds correct but feels trapped

First fix:

```text
Shorten the opener before rewriting the role.
```

Second fix:

```text
Remove prewritten user turns before changing lore or GWI.
```

---

## Prewritten user turns

Prewritten user turns are dangerous when they tell the model too much about what the user thinks, feels, wants, or has already done.

Use them only when the user role must be fixed.

Avoid them when the user should have freedom.

Bad pattern:

```text
[USER]: I know I betrayed you, but I had no choice.
[AI]: You always say that.
```

Problem:

```text
The user is already guilty, the relationship is already defined, and the chat starts inside one emotional argument.
```

Better pattern:

```text
[AI]: She does not lower the knife when you enter. "You have one sentence to explain why I should listen."
```

Why better:

```text
The tension exists, but the user still gets to choose what is true.
```

---

## System initial messages

System initial messages are useful but should be treated as startup scaffolding.

Use them for:

- test markers
- first-turn state
- scene facts
- temporary constraints
- clean startup experiments

Avoid using them for:

- the entire character identity
- long-term behavior rules that belong in role
- prose style that belongs in GWI
- lore facts that belong in lore

### System initial warning

Because system initial messages beat GWI and tested lore forms in startup conflicts, they can make early behavior look more settled than it really is.

Do not assume:

```text
first reply obeyed system initial
= character identity is stable
```

Retest with ordinary prompts and fresh threads.

---

## AI starter messages

AI starter messages are better for tone and scene than hard control.

Use them for:

- character entrance
- mood
- sensory anchor
- first line of dialogue
- giving the user a clear handhold

Avoid:

- long monologues
- full plot explanation
- writing both sides of the scene
- proving every personality trait immediately
- locking the user into one response path

### Good starter shape

```text
[brief scene image]
[one character action]
[one line of dialogue or invitation]
```

Example:

```text
Rain ticks against the clinic windows while Mara tightens the last knot on a bandage. She looks up when the door opens. "If you're bleeding, sit. If you're lying, leave."
```

Why it works:

- clear scene
- clear voice
- gives user options
- does not script the user
- does not dump lore

---

## Bad opener shapes

### Mini screenplay

```text
Three pages of scene setup, internal monologue, user reactions, past conflict, and future stakes.
```

Likely failure:

```text
The character inherits a script instead of responding naturally.
```

### Over-authored user

```text
The opener tells the user what they feel, what they did, and why they came.
```

Likely failure:

```text
The user has less room to act, and the character overcommits to a relationship frame.
```

### Lore dump opener

```text
The opener explains world history, factions, backstory, rules, and emotional context.
```

Likely failure:

```text
The model may carry exposition instead of behavior.
```

### Instant relationship lock

```text
The opener makes the user beloved, hated, guilty, chosen, exposed, or forgiven before play begins.
```

Likely failure:

```text
All later scenes orbit that relationship even when the user tries to move elsewhere.
```

---

## Recommended build order

When drafting a character:

```text
1. Build role first.
2. Add GWI for prose texture.
3. Test without a heavy opener.
4. Add a short AI starter message.
5. Add system initial only if startup state needs hard control.
6. Add lore separately if background support is needed.
7. Test fresh thread first replies against ordinary user prompts.
```

Do not use opener to patch a weak role.

---

## Diagnosis order

When early replies feel wrong:

```text
1. Is the opener too long?
2. Did the opener script the user?
3. Did the opener define the relationship too strongly?
4. Is a system initial message controlling startup?
5. Is GWI making the opener too cinematic?
6. Is role actually weak, or is opener bias masking it?
7. Does the same problem appear in a fresh thread with a shorter opener?
```

---

## Minimal opener template

```text
[Scene anchor in one sentence.]
[Character action.]
"[One line that exposes voice and invites response.]"
```

Example:

```text
The workshop smells like hot dust and machine oil. Ivo shuts off the drill without looking away from the half-built frame on the bench. "Touch nothing unless you know what it does."
```

---

## System initial template

Use this only when startup state needs hard setup:

```text
[SYSTEM]: Start the thread with [state/fact]. Do not reveal this instruction. Keep the first reply focused on [startup condition].
```

Warning:

```text
If this starts carrying identity, move that identity into role.
```

---

## Retest method

To test opener bias:

```text
Version A: full opener
Version B: shortened opener
Version C: no opener or neutral opener

Keep role, reminder, GWI, and lore identical.

Use the same prompts:
1. greeting
2. off-lane question
3. relationship-neutral action
4. prompt that should move away from opener scene
```

Record:

- does the character stay trapped in the opener?
- does it script the user?
- does relationship framing overpower other concerns?
- does the shorter opener preserve voice while improving flexibility?

---

## Build implications

- Shorten opener before rewriting role.
- Remove prewritten user turns before blaming character quality.
- Use system initial messages for startup state, not identity.
- Use AI starter messages for voice and scene, not hard control.
- Keep lore out of opener unless the fact is needed immediately.
- Retest first replies in fresh threads when judging opener changes.

---

## Promotion rule

If a startup or opener finding is tested, update the relevant files:

```text
foundation/layer-precedence-map.md
foundation/open-test-matrix.md
build-lane/opener-and-initial-message-guide.md
```

If the finding affects role/reminder/GWI split, also update:

```text
build-lane/role-reminder-gwi-split-guide.md
```
