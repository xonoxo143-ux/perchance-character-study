# Failed or rejected ideas

This file keeps the dead ends and partial dead ends.
Some are fully rejected.
Some are parked because they failed in the tested form.

## 1. Treating imported prebuilt threads as clean startup proofs
**Status:** rejected

### Why it failed
Earlier imported-thread results did not hold up cleanly against later fresh-thread tests.

### Practical consequence
- Startup claims now default to fresh-thread evidence.
- Imported threads are still useful for harnesses and bulk experiments.

---

## 2. Treating blank ACC as a neutral assistant baseline
**Status:** rejected

### Why it failed
Blank / near-blank tests produced:
- placeholders
- silence
- odd degenerate outputs
- or scene-first roleplay drift

### Practical consequence
A blank control is not automatically a trustworthy baseline for “what ACC naturally is.”

---

## 3. Using a giant opener to fix a weak build
**Status:** rejected as default strategy

### Why it failed
Over-authored openers can:
- overpower the role
- pre-bias the relationship
- lock scene cadence
- make the character feel scripted

### Practical consequence
Cut the opener before rewriting the whole build.

---

## 4. Treating example dialogue as harmless flavor
**Status:** rejected

### Why it failed
Examples teach:
- cadence
- reply skeleton
- argumentative shape
not just tone.

### Practical consequence
Keep examples tiny.

---

## 5. Using fake slash messages from custom code as real slash commands
**Status:** rejected

### Why it failed
Auto-pushed `/lore ...` changed output but did not create real lore rows or command-level proof.

### Practical consequence
Treat pushed slash-looking messages as visible-context injection unless proven otherwise.

---

## 6. Using public character/share links as chat-proof
**Status:** rejected

### Why it failed
Character/share links were not enough to prove thread-level outcomes.
The real evidence lived in the exported thread JSON.

---

## 7. Using `/sum <text>` like `/lore <text>`
**Status:** rejected

### Why it failed
`/sum SUMMARY-CYAN` behaved as normal message text across multiple characters.
No summary rows or summary usage fields were created.

---

## 8. Bigger imported bloat should eventually force summaries
**Status:** parked / failed in tested form

### Why it failed
Multiple huge imported packs still did not reach summary readiness, even with memories enabled.

### Why it is not fully dead
The failure could mean:
- threshold is much higher than expected
- imported history does not count like live-grown history

### Practical consequence
Do not keep brute-forcing bigger imported packs blindly.

---

## 9. AI-authored visible initial message should control the next reply
**Status:** rejected

### Why it failed
A visible AI starter appeared, but the next reply did not obey it like a hard command.

### Practical consequence
Separate:
- visible seed
- hard startup control

---

## 10. Lorebook-only is enough for complex user identity
**Status:** rejected for the Horde / complex-`{{user}}` project

### Why it failed
Observed-in-practice reports said lorebook-only was too weak under strong host framing.

### Practical consequence
Use a small always-on URD plus deeper lorebook instead.

---

## 11. Heavy secrecy rules create better hidden-system behavior
**Status:** rejected for the project-specific Horde work

### Why it failed
Over-restricting secrecy could make the model compensate with spectacle / cinematic wrongness instead of better subtle fronting.

---

## 12. Reminder should always be made stronger by adding more text
**Status:** rejected

### Why it failed
Long reminders:
- can be parroted
- can make the character feel supervised
- can create rigidity instead of stronger control

---

## 13. Agent-mode ACC proofing as a main lane
**Status:** parked

### Why it failed
Site verification / browser gating made autonomous proofing unreliable.

### Practical consequence
Agent mode may still be useful later, but it is not the stable main lane right now.
