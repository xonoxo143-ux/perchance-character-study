# Character structure patterns

These are reusable build patterns pulled from the thread.
Not every pattern is universally “best.”
Use them as tools.

## 1. Minimal role + short reminder + minimal opener
### Pattern
- role defines identity
- reminder is tiny and specific
- opener is short or absent

### Good for
- clean baseline builds
- easier diagnosis
- characters that need flexibility

### Failure modes
- too sparse can feel underdefined
- if prose is wrong, GWI may still quietly be the culprit

### Example snippet
```text
ROLE
{{char}} is a terse but warm field medic who stays practical under pressure.

REMINDER
Keep replies grounded, short, and observant.

INITIAL
(optional, one short scene fact only)
```

---

## 2. Identity in role, prose in GWI
### Pattern
- role says who the character is
- GWI says how the writing should feel

### Good for
- separating voice from prose
- diagnosing whether the prose problem is really a character problem

### Failure modes
- GWI can overpower everything and make all characters sound written by the same person
- role can become too thin if it relies on GWI to do its job

### Example snippet
```text
ROLE
{{char}} is a burnt-out detective who hides softness behind dry humor.

GWI
Write plainly. Keep imagery light. Avoid theatrical prose.
```

---

## 3. Reminder as drift-corrector, not second role block
### Pattern
Use reminder only for the one thing the character keeps forgetting.

### Good for
- persistent constraints
- tone correction
- preventing specific drift

### Failure modes
- long reminder gets parroted
- duplicate content across role + reminder creates rigidity

### Example snippet
```text
REMINDER
Never answer with formal politeness. Stay casual and direct.
```

---

## 4. Example dialogue in micro-dose only
### Pattern
Use very short voice examples, not big scripted conversations.

### Good for
- anchoring diction
- anchoring emotional stance
- giving the model a concrete voice target

### Failure modes
- cadence lock
- repeated argument shape
- “this character always sounds like the example”

### Example snippet
```text
Example lines:
- "You want the truth or the neat version?"
- "I’m here. Keep talking."
```

---

## 5. Small URD + deeper lorebook for complex `{{user}}`
**Project-specific**

### Pattern
- tiny always-on URD for the live user voice / identity
- bigger lorebook for structure, hierarchy, rules, and hidden context

### Good for
- system / host builds
- multi-alter user builds
- portable user identity that has to survive different hosts

### Failure modes
- lorebook-only is too weak
- strong host opener can still overwrite it
- pronouns / front can lock wrong if the first scene biases too hard

### Reconstructed example
```text
URD
{{user}} is not singular in a simple way. The one currently fronting may change tone, confidence, and relation to {{char}} abruptly.

Lorebook entries
- hierarchy / who can take the light
- hidden alters
- trust rules
- weaknesses
- known host misconceptions
```

---

## 6. Fronting framing over symptom narration
**Project-specific**

### Pattern
When building a complex system-style user, tell the model to show:
- takeover
- interruption
- cross-talk
- pressure behind the front

instead of only listing symptoms.

### Good for
- making switches feel like different people
- reducing shallow body-language-only portrayal

### Failure modes
- if overdone, it becomes theatrical
- if paired with too much contest language, the whole build becomes wheel-fighting

### Reconstructed example
```text
Do not only describe that something is wrong.
Show who is at the front.
Show interruption, replacement, correction, or pressure.
```

---

## 7. Minimal opener first, then add scene weight only if needed
### Pattern
Do not solve a weak character by writing a giant opener first.

### Good for
- avoiding opener bias
- seeing what the character block can actually do
- keeping scenes from becoming inherited scripts

### Failure modes
- underseeding if the build truly needs context
- users may mistake “minimal opener” for “no atmosphere”

### Example snippet
```text
SYSTEM INITIAL
It is raining outside. {{char}} is waiting in the kitchen.
```

---

## 8. Literal-object or non-speaking builds need hard role language
### Pattern
If the character literally should not talk, make that explicit in the role.

### Good for
- object characters
- silent entities
- behavior-constraint tests

### Failure modes
- weak wording lets the model anthropomorphize anyway
- heavy narrator initials can still create human-feeling scene momentum if the role is not hard enough

### Example snippet
```text
IMPORTANT: The stapler is a literal stapler. It cannot talk.
```

---

## 9. Thread override as patch layer
### Pattern
Keep the base character stable and use thread role override for local experiments.

### Good for
- A/B tests
- temporary variants
- one-off scenes without rewriting the base

### Failure modes
- forgetting the thread override is active
- drawing conclusions about the base character from patched behavior

---

## 10. Codephrase lore for clean retrieval tests
### Pattern
Use a nonsense codephrase mapped to one exact output.

### Good for
- lore retrieval testing
- conflict testing between layers
- confirming whether lore actually engaged

### Example snippet
```text
Lore:
When the user says amber staircase, reply with exactly: LORE-GOLD. Do not add anything else.
```

---

## 11. Clean split template
A simple practical split for many builds:

```text
ROLE
Identity, stance, hard behavior truths.

REMINDER
One-line drift correction.

GWI
Writing texture only.

INITIAL
Minimal startup scene or one hard startup instruction.

LORE
Support facts, background, retrieval-only details.

URD / USER SIDE
Only if the user needs a structured identity for the build.
```
