# Perchance ACC Cheat Sheet

## Tested behaviors, practical traps, and rebuild rules

This cheat sheet is for **Perchance AI Character Chat (ACC)** only.
It focuses on things that are poorly documented, easy to misdiagnose, or only become obvious after testing.

---

## 1. Start with the right mental model

ACC behavior usually comes from **layer interaction**, not one isolated field.

- **Role / Instruction** = who `{{char}}` is
- **Reminder** = short near-reply nudge
- **Initial Messages** = early scene and response seeding
- **Lorebook** = supporting context
- **GWI** = prose / pacing / style layer
- **Live thread context** = recent momentum, summaries, memories, retrieved lore

A lot of ACC problems are really **overlap problems**.

---

## 2. What matters more than people think

### Initial messages can overpower a good character
**Finding:** A long, authored opener can make a solid character feel scripted, repetitive, or overcommitted to one dynamic.

**Why it matters:** People often rewrite the character when the real problem is the opening seed.

**Test first:** Shorten the opener and remove prewritten `{{user}}` turns before touching the role block.

**Do not assume:** Bad early replies do not automatically mean the core character is bad.

### Example dialogue can teach a response skeleton, not just tone
**Finding:** Dialogue examples can lock a character into a repeated rhythm or argumentative shape, not just word choice.

**Why it matters:** The character may sound correct but still feel too samey.

**Test first:** Remove only the example lines and reuse the same prompts.

**Do not assume:** Example dialogue is not a harmless flavor add-on.

### GWI can quietly dominate prose
**Finding:** A built-in writing style can add strong narrative sheen, pacing habits, or theatrical flavor even when the character spec itself is fine.

**Why it matters:** You can misdiagnose a prose problem as a character problem.

**Test first:** Swap only the GWI to a short neutral Custom instruction.

**Do not assume:** The role block is not automatically the source of all prose behavior.

### Reminder is stronger when shorter
**Finding:** Reminder works better as a small correction or persistent nudge than as a second full instruction block.

**Why it matters:** An overstuffed reminder can make the character feel supervised, distracted, or rigid.

**Test first:** Cut the reminder down before rewriting the whole character.

**Do not assume:** A stronger reminder is not always a better reminder.

### Layer duplication creates hidden rigidity
**Finding:** If the same idea is reinforced in role, reminder, opener, lore, and user framing, the build can become narrow without obviously breaking.

**Why it matters:** The character may look strong on paper but feel trapped in one lane in practice.

**Test first:** Reduce duplication before changing core identity.

**Do not assume:** More reinforcement does not always mean more stability.

---

## 3. What causes false diagnoses

### “The character is bad”
Sometimes true, often false.

Common hidden causes:
- opener is over-authored
- example dialogue is overtraining cadence
- GWI is imposing the wrong prose lane
- reminder is too long
- one relationship is overweighted across too many layers

### “The lorebook is broken”
Often overstated.

Common alternatives:
- role block and lore are contradicting each other
- lore is doing identity work it should not be doing
- retrieval cues are weak
- the real issue is scene momentum, not lore failure

### “The model is forgetting”
Possible, but not the only explanation.

Common alternatives:
- opener bleed
- summary compression
- exact-detail drift instead of full forgetting
- runtime context prioritizing recent tone over older facts

### “The character is too obsessed with `{{user}}`”
Sometimes structural, sometimes test contamination.

Check first:
- were prompts being delivered as `{{user}}` framing reality?
- did the opener pre-bias the relationship?
- is that relationship reinforced in too many layers?

---

## 4. Proven ACC testing rules

### Test one variable at a time
If you change opener, reminder, GWI, and role all at once, you learn almost nothing.

Good test sequence:
1. Keep a control
2. Change one thing
3. Reuse the same prompts
4. Compare behavior, not just vibes

### Use the same prompts when possible
If the test prompt changes, the comparison gets weaker.

### Separate setup tools from evaluation tools
A tool that is good for setting conditions is not automatically good for judging natural character behavior.

### Do not let smart criticism skip testing
Use criticism to generate **test targets**, not conclusions.

---

## 5. Slash-command reality check

### Normal typing
Best baseline for testing how `{{char}}` naturally responds to `{{user}}`.

### `/user`
Controlled `{{user}}` input. Useful when you want precision without changing lanes.

### `/ai`
Useful when you explicitly want `{{char}}` to continue from their own side. Good for some tests, but still not identical to ordinary play.

### `/sys`
Best used for hard scene-state control and test conditions.

Use it for:
- setting scene facts
- overriding stale state
- forcing a test condition

Do not rely on it as the main test for natural character voice.

### `/nar`
Treat as softer narrative steering, not a separate engine.

Practical rule:
- `/sys` = hard setup
- `/nar` = softer setup
- neither is the cleanest voice-evaluation lane

---

## 6. Common ACC traps

### Over-authored opener
**Symptoms:** inherited-feeling replies, user puppeting, narrow early tone, repeated scene gravity.

**First fix:** shorten it, remove extra user turns, seed less.

### Example dialogue overload
**Symptoms:** quote-like replies, repeated argument shape, strong but narrow voice.

**First fix:** remove example dialogue before rewriting the whole character.

### Role block doing too many jobs
**Symptoms:** character feels stiff, prose feels controlled in the wrong way, scenes feel over-managed.

**First fix:** move support material out of role and keep role focused on identity and behavior.

### Reminder becoming a second role block
**Symptoms:** forced-feeling replies, too many visible guardrails, character feels aware of constraints.

**First fix:** shorten the reminder drastically.

### One relationship dominating everything
**Symptoms:** character always orbits the same person, broader world collapses when that person is present, all scenes bend back to the same dynamic.

**First fix:** reduce duplication of that relationship across layers.

### Misreading `/sys`
**Symptoms:** outputs are longer, more scene-like, or differently constrained than normal play.

**First fix:** use `/sys` for setup only and judge character quality with normal prompts.

---

## 7. What to try first when something feels off

### Too stiff
Try:
1. shorten opener
2. remove example dialogue
3. shorten reminder
4. test Custom GWI

### Too samey
Try:
1. remove cadence/example lines
2. reduce repeated anti-failure rules
3. test whether GWI is imposing the rhythm

### Too ornate / too cinematic
Try:
1. switch off built-in RP style
2. use a neutral Custom GWI
3. keep opener minimal

### Too user-focused
Try:
1. remove prewritten `{{user}}` lines from opener
2. reduce relationship repetition across layers
3. test scenes where `{{user}}` is present but not central

### Ignores broader story when one dynamic is active
Try:
1. test a world/mission scene without rewriting identity
2. see whether the build is over-seeded for one relationship
3. cut duplicate framing before touching lore

### Weird runtime naming / labels
Try:
1. de-author the opener
2. test clean user prompts
3. check whether the issue is intermittent before assuming it is hardcoded

Do not assume a weird label must literally exist in the JSON.

---

## 8. Practical field-use rules

### Role / Instruction
Use for:
- identity
- decision style
- voice tendencies
- relationship posture

Do not use it for:
- full encyclopedic lore
- all scene law
- massive anti-failure lists

### Reminder
Use for:
- one or two persistent corrections
- temporary state
- one strong voice nudge

Do not use it for the whole character philosophy.

### Initial Messages
Use for:
- opening state
- opening lane
- first-turn temperature

Do not use them for a mini screenplay or heavy scripting of `{{user}}`.

### Lorebook
Use for:
- world support
- side systems
- supporting facts

Do not use it for the entire soul of the character.

### GWI
Use for:
- prose lane
- pacing
- verbosity habits
- overall style

Do not use it for defining the entire character.

---

## 9. What to keep unresolved on purpose

Some things should stay open until tested in the exact context that matters:
- exact placeholder/runtime fallback behavior
- exact RP1 vs RP2 differences in every use case
- perfect token-length sweet spot
- exact long-thread continuity limits under every memory setting

A good cheat sheet should not pretend to know more than it knows.

---

## 10. Working method

Use this order:
1. Identify the symptom
2. Identify the likely overlapping layers
3. Change one variable
4. Reuse the same prompt
5. Compare outputs
6. Keep the smallest successful fix

That method matters more than any single rule in this sheet.

---

## 11. Short version

If a character feels wrong in ACC, test these before rewriting them:
- shorten the opener
- remove example dialogue
- shorten the reminder
- test neutral Custom GWI
- reduce duplication across layers
- stop using `/sys` as your main voice-quality test

That set of checks will solve more problems than most full rewrites.
