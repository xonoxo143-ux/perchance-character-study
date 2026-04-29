# Mutation log

How the project goal evolved across the thread.

## Phase 1 — brute-force precedence bracket
### Previous idea
General ACC uncertainty:
- role?
- reminder?
- GWI?
- initial?
- lore?
What actually wins?

### New idea
Build clean marker-token test packs and stop guessing.

### What changed
- started using hard tokens like `REM-BLUE`, `INSTR-RED`, `INIT-GREEN`
- moved from vibes to controlled brackets

### What stayed the same
- goal was still practical ACC understanding, not abstract theory

### Why it mattered
This created the first real precedence map.

---

## Phase 2 — startup confounder discovered
### Previous idea
Imported packs were assumed to be “good enough” for startup tests.

### New idea
Fresh-thread vs imported-prebuilt is a major confounder.

### What changed
- earlier results were re-audited
- fresh-thread testing became the cleaner startup lane

### What stayed the same
- still mapping the same layers

### Why it mattered
Several results flipped or became cleaner only after this distinction.

---

## Phase 3 — startup sanity and lore placement
### Previous idea
Lore existed, but its actual place in the hierarchy was unclear.

### New idea
Split lore testing into:
- character lorebook URL
- direct thread lore via `/lore`

### What changed
- startup sanity pack
- fresh lore bracket
- direct thread lore bracket
- explicit use of `loreIdsUsed` to confirm lore engagement

### What stayed the same
- same bracket logic, same marker-token style

### Why it mattered
This stopped “lore lost” from being confused with “lore never loaded.”

---

## Phase 4 — automation / harness lane
### Previous idea
Everything was being hand-driven.

### New idea
Use custom code to reduce repetitive manual work.

### What changed
- auto-open harnesses
- one-time seed-on-open behavior
- fake slash-lore tests

### What stayed the same
- still trying to preserve clean evidence

### Why it mattered
This created useful lab tooling, but also revealed a new parser confounder:
visible slash-looking text is not the same as real command execution.

---

## Phase 5 — proof hardening and KB building
### Previous idea
Results were living too much in chat memory.

### New idea
Make a working KB / DB snapshot and export-schema notes.

### What changed
- glossary
- scoreboard
- challenge passes
- export JSON structure appendix
- harder separation of confirmed vs provisional

### What stayed the same
- goal remained practical continuity, not a polished tutorial

### Why it mattered
The thread became handoff-able instead of fragile.

---

## Phase 6 — summary / memory branch
### Previous idea
Summaries might be easy to force with imported bloat.

### New idea
Imported size alone may not answer the question.

### What changed
- summary bloat packs
- memories-enabled packs
- `/sum` parser test
- imported-vs-live-growth theory emerged

### What stayed the same
- still working from controlled artifacts and export proof

### Why it mattered
This moved summaries from “just brute-force it” to “needs a different test design.”

---

## Phase 7 — project-specific build heuristics were folded in
### Previous idea
Keep only pure ACC mechanics.

### New idea
Preserve useful Horde / complex-`{{user}}` lessons too, but label them clearly as project-specific.

### What changed
- small URD + deeper lorebook pattern
- fronting vs symptom narration note
- host overwrite / pronoun lock / secrecy spectacle notes

### What stayed the same
- separation between confirmed ACC mechanics and theory remained important

### Why it mattered
The repo became useful not only for layer precedence, but for actual complex character construction.

---

## Phase 8 — checkpoint / repo export
### Previous idea
Use the chat itself as the notebook.

### New idea
Export the useful knowledge into a structured zip for a separate repo.

### What changed
- this handoff bundle exists
- practical notes are separated from theory
- examples are bundled

### What stayed the same
- do not invent certainty
- preserve messy but useful details instead of deleting them

### Why it mattered
Another assistant can continue the work without re-reading the whole thread.
