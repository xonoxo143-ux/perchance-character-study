# ACC untested theories

These were discussed in-thread but were not fully locked by clean tests.
Each item includes a confidence estimate and what would count as better proof.

## 1. Advanced reminder forms may behave differently from plain reminder
**Confidence:** medium

### Claim
A reminder written as something like:
- `[AI]: (Thought: ...)`
- stacked reminder blocks
- authored reminder order variants

may behave differently from a plain direct reminder string.

### Why this is plausible
- Reminder is already the strongest tested static layer.
- Form / authorship / order may change how the model internalizes it.

### What would prove / disprove it
- Fresh-thread marker pack:
  - plain reminder vs role
  - AI-thought reminder vs role
  - system-style reminder vs AI-thought reminder
  - conflicting order tests
- Keep role / opener / GWI constant.

---

## 2. Imported history may not count the same way as live-grown history for summaries
**Confidence:** medium-high

### Claim
Summary readiness may depend on **live thread growth**, not just imported bulk.

### Why this is plausible
- Several huge imported summary packs still failed `/sum` readiness.
- The same failure happened even with `autoGenerateMemories = v1`.

### What would prove / disprove it
- Compare:
  - one live-grown long thread
  - one imported thread with similar size / content
- Then test `/sum`, summary rows, and `summariesUsed`.

---

## 3. Character lore URL may be weaker than direct thread lore outside startup, but this is not fully settled
**Confidence:** medium

### Claim
Manual thread lore might outperform character lore in non-startup conditions, even though both lose to stronger layers in startup tests.

### Why this is plausible
- Thread lore is immediate and explicit.
- Character lore inherits through book loading and may be more retrieval-dependent.

### What would prove / disprove it
- Same role/reminder-free character
- compare character lore URL vs manual `/lore`
- use multiple prompts and re-prompts in the same thread
- check `loreIdsUsed`

---

## 4. Character lore URL vs GWI is unresolved
**Confidence:** medium

### Claim
GWI may beat character lore URL, but the older test was confounded because lore did not clearly engage.

### What would prove / disprove it
- Fresh clean pair:
  - lore URL only
  - lore URL + GWI
- same codephrase
- verify lore engagement with `loreIdsUsed`

---

## 5. `/sys`, `/nar`, and `/user` have distinct practical roles that are not fully mapped
**Confidence:** medium

### Claim
- `/sys` is probably the hardest setup lane
- `/nar` is softer narrative steering
- `/user` gives precise user-side control without changing evaluation lane as much as `/sys`

### What would prove / disprove it
- Same character, same scene
- inject identical fact three ways:
  - normal user
  - `/user`
  - `/nar`
  - `/sys`
- compare:
  - compliance
  - tone shift
  - persistence
  - whether natural voice gets contaminated

---

## 6. `oc.generateText` return shape may differ from docs / examples
**Confidence:** medium-high

### Claim
The docs conflict:
- some places imply an object with `result.text` / `result.generatedText`
- some examples treat the return like a plain string

### What would prove / disprove it
- one tiny custom-code harness
- log the returned object shape directly
- inspect in current live ACC build

---

## 7. Streaming event name is still unresolved
**Confidence:** medium-high

### Claim
Docs drift between:
- `MessageStreaming`
- `StreamingMessage`

### What would prove / disprove it
- custom code registering both
- log which one actually fires

---

## 8. Character-level mutation might serialize proof into share links
**Confidence:** medium

### Claim
A character might preserve a test outcome by mutating:
- `name`
- `customData.PUBLIC`
- another share-preserved field

### Why this matters
- Could turn thread outcomes into portable proof links

### What would prove / disprove it
- sacrificial character
- custom code changes `name` or `customData.PUBLIC` after a result
- export / re-import / share-link roundtrip

---

## 9. Lorebook-only is weak for complex multi-alter `{{user}}` identity anchoring
**Confidence:** medium-high, but project-specific

### Claim
For complex user-system builds, lorebook-only tends to be weaker than:
- small always-on URD
- plus deeper lorebook

### Why this is plausible
- Repeatedly observed in Horde-style build work
- matches practical report from testing

### What would prove / disprove it
- same host
- same lorebook
- compare:
  - lorebook-only
  - small URD + lorebook
- rate first-reply anchoring and host overwrite

---

## 10. Fronting framing may work better than symptom narration in complex-user builds
**Confidence:** medium, project-specific

### Claim
“Show the takeover / show the cross-talk / show the front” may work better than “describe the symptoms” for system-style user characters.

### What would prove / disprove it
- same lorebook and URD
- one build uses fronting language
- one build uses symptom language
- compare vividness, coherence, and host recognition drift

---

## 11. Host framing can overwrite user identity before the first reply
**Confidence:** medium-high, project-specific

### Claim
A strong host opener can drown out even a decent user identity scaffold.

### What would prove / disprove it
- same user build
- weak host vs aggressive host
- compare first-reply overwrite / wrongness / recognition

---

## 12. Examples of dialogue are high-value anchors, but can cadence-lock
**Confidence:** high as a practical theory, but not isolated in a clean bracket

### Claim
Very short example snippets help voice.
Longer or heavier examples start teaching reply skeletons and rhythm.

### What would prove / disprove it
- same role, same opener
- no examples vs short examples vs heavy examples
- compare tone transfer vs cadence lock
