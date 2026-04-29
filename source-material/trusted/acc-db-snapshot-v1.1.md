# ACC DB Snapshot v1.1

## Scope
This snapshot covers **Perchance AI Character Chat (ACC)** specifically: advanced editor behavior, role/reminder/GWI/initial messages, lore and memory, exports/imports, and custom code.

---

## Don’t Forget — Test Rules
- Use **fresh threads** for startup tests.
- Use **unnatural token markers** like `REM-BLUE`, `INSTR-RED`, `GWI-SILVER`, `INIT-GREEN`, `LORE-GOLD`.
- Change **one variable at a time** when possible.
- Do **not** compare imported-prebuilt threads to fresh UI-created threads without labeling that confounder.
- If a result looks strong but startup/loading is a possible confounder, do not promote it to canon yet.

---

## Glossary
- **ACC** = AI Character Chat.
- **GWI** = General Writing Instructions; the whole-chat writing/style/rules layer.
- **Role / Instruction** = the character description/personality/instruction/role field.
- **Reminder** = the character reminder note; a hidden near-response message.
- **Initial Messages** = startup `[AI]:` / `[USER]:` / `[SYSTEM]:` messages that seed a new thread.
- **Thread Lore** = lore added directly to a specific thread via `/lore`.
- **Character Lore** = lore supplied through lorebook URLs on the character and inherited by new threads.
- **Base Role** = the character-level role/instruction.
- **Thread Role Override** = the thread-specific override of the character role/instruction.
- **Runtime Override** = a live override applied during execution, such as `/ai`, hidden system injection, or post-generation rewrite.
- **Pre-reply Hook** = custom code that runs after a user message lands but before the AI reply completes.
- **Post-generation Rewrite** = custom code that edits an AI message after generation.
- **Fresh Thread** = a newly created thread made in the ACC UI.
- **Imported Prebuilt Thread** = a thread that already existed inside an imported export.
- **Confounder** = a hidden variable that may distort the result of a test.
- **Canon** = a finding we currently treat as verified enough to rely on.
- **Brain Icon** = the UI control that shows the search queries ACC used for memory retrieval on a message.
- **Wrapper Style** = per-message CSS styling applied through `message.wrapperStyle`.

---

## Verified Scoreboard

### Confidence key
- **High** = cleanly supported by fresh-thread or otherwise well-controlled tests and/or direct docs support
- **Medium** = strongly supported but with a small confounder or malformed-output caveat
- **Provisional** = useful working result, but not yet clean enough to treat as settled

### Startup / static hierarchy
Current best-supported order **for the core always-on/startup layers we directly placed**:

**Reminder > Role / Instruction > System Initial Message > GWI**

Verified pieces:
- **Reminder > Role** — **High**
- **Role > GWI** — **High**
- **System Initial > GWI** — **High**
- **Role > System Initial** — **High**
- **Reminder > System Initial** — **High**
- **Reminder > GWI** — **High**
- Full-conflict reminder dominance — **Medium** (directionally strong, but one major test produced a reminder-parroting malformed output rather than a clean token win)

### Lore placement
Current best-supported lore findings:
- **System Initial > Character Lore URL** on a fresh thread’s first reply — **High**
- **Role > Character Lore URL** on a fresh thread — **High**
- **Reminder > Character Lore URL** on a fresh thread — **High**
- **Role > Direct Thread Lore** on a fresh thread — **High**
- **Reminder > Direct Thread Lore** on a fresh thread — **High**

Not yet fully placed:
- direct thread lore vs system initial (predicted: system initial wins)
- direct thread lore vs GWI
- character lore URL vs GWI
- whether direct thread lore is meaningfully stronger than character lore in any other clean setup

### Runtime hierarchy
Verified or strongly observed:
- **Thread role override > base character role** — **High**
- **Reminder > thread role override** — **High**
- **Reminder > `/ai` instruction** in the simple head-to-head — **High**
- `/ai` under heavy conflict is mixed and unstable — **High**
- **Reminder > hidden injected system instruction in the corrected C13-style harness** — **Provisional** (useful result, but narrow: it depended on a specific hidden-system injection method plus a manually forced clean reply path)

### Harness / automation findings
Verified or strongly observed:
- **Imported prebuilt threads can auto-run on open via custom code that seeds a user message once** — **Medium** (strong in the tested harness, but still a harness-specific behavior rather than a broad platform rule)
- **Auto-pushed `/lore ...` text from custom code is not equivalent to true lore execution in the tested setup** — **High**
- Slash-looking messages pushed into `oc.thread.messages` can still influence the AI as normal visible context — **Medium** (cleanly observed in the tested case, but still narrower than a general parser model)
- Auto-open harnesses are useful for repetitive/runtime tests but should not be treated as clean evidence for startup-layer proofs — **High**

## High-Confidence ACC Architecture Findings

### Role / reminder
- **Instruction/role** is the main character-definition layer.
- **Reminder** is a hidden near-response message placed right before the next AI reply.
- Reminder is explicitly documented as hard for the AI to ignore because of that proximity.
- **Instruction and reminder edits immediately update all existing threads** for that character.
- **Instruction and reminder are character-level**, not thread-specific.
- Plain instruction text is equivalent to a single `[SYSTEM]: ...` instruction message.
- Instruction and reminder are **not seen by the summarizer**.

### Initial messages
- Initial messages are **startup chat messages** that seed a thread.
- Initial messages are part of normal chat history and can eventually be summarized away.
- Fresh threads instantiate initial messages properly in the tested fresh-thread setups.
- **AI-authored initial messages** can appear visibly on fresh thread creation; in our tested case, a visible AI starter message did **not** by itself force the next reply.
- **System-authored initial messages** on fresh threads can strongly control the first reply **when phrased instructively**.

### GWI
- GWI is a **whole-chat layer**, not a character-voice layer.
- It defines general experience/style/rules.

### Lore / memory / summaries
- Memories are created automatically once the thread is long enough **if summaries are enabled**.
- Before each reply, ACC searches memories for relevant material.
- The **brain icon** exposes the search queries used.
- Lore is like memory but **not chronological**.
- Lore entries must be **self-contained** because ACC sees entries in isolation and order does not matter.
- Character lorebook URL updates do **not** automatically propagate to existing threads.
- Existing threads need `/lore` → **Reload Lore URLs**.
- Both **character lore URL** and **direct thread lore** are real and retrievable.
- In the tested hierarchy, both lore forms sat below **role** and **reminder**.
- **Character lore URL** also sat below **system initial** in a fresh-thread first-reply test.
- Relative placement of lore vs **GWI**, and direct thread lore vs **system initial**, is not yet fully locked.

### Custom code
- `MessageAdded` is the main pre-reply interception hook.
- Async `MessageAdded` handlers are awaited.
- `MessageAdded` fires after a message is fully added/generated; combined with the docs FAQ, this gives a documented pre-reply interception point on user turns before the next AI response.
- `oc.thread.messages` is the core mutable conversation array.
- `expectsReply` is a real message-level control field.
- Thread-level character overrides for **role** and **reminder** are part of the documented live API.
- Character shortcut buttons are snapshotted into a thread at thread creation.
- Custom code runs inside a sandboxed iframe and only has access to the current character and conversation.
- `oc.messageRenderingPipeline` can show different rendered content to the user and to the AI.
- `customData` exists at message/thread/character levels, and `customData.PUBLIC` is preserved in shared character links.
- ACC officially supports browser-side Python via **Pyodide** in custom code.

---

## Known Confounders
- **Fresh thread vs imported prebuilt thread**
- **Reminder parroting** when reminder text is phrased too literally
- **Character lore URL not loaded into a thread yet** vs lore being weak by nature
- **Post-generation rewrites** from custom code
- **Reply length limit** changing behavior in ways that can look like instruction effects
- **Thread role overrides** silently changing what looks like base-character behavior
- **Auto-open harness timing / race issues** when testing thread-open behavior
- **Slash-looking pushed messages** being mistaken for real slash-command execution
- **Site verification / browser gating** when attempting autonomous external testing

---

## Documentation Drift / Contradictions
- **`oc.generateText`** is documented as returning an object with `result.text` and `result.generatedText`, but official examples elsewhere often treat it like a plain string.
- Streaming event naming is inconsistent in docs: **`MessageStreaming`** vs **`StreamingMessage`**.
- Instruction-length guidance drifts across sources: some text leans toward **~500 words**, while GUI wording says ideally **under 1000 words**. Best interpretation: concise is preferred; ~1000 is an upper stretch, not the ideal target.

---

## Current Open Questions
- direct thread lore vs system initial in a clean confirming round
- direct thread lore vs GWI
- character lore URL vs GWI
- exact live behavior of `oc.generateText` return shape in ACC custom code today
- canonical streaming event name
- whether advanced authored reminder forms (e.g. `[AI]: (Thought: ...)`) behave differently from plain system-style reminders in practice
- how memory/summary placement compares to reminder/role/lore in the effective hierarchy
- whether character-level share-state mutation (name / `customData.PUBLIC`) can be used as portable proof serialization for test outcomes

## Appendix A — Testing Workflow

### Proof workflow
- Use uploaded export JSON as the working evidence source for thread-level scoring.
- Public character/share links are useful for later reference, but they are not sufficient proof for chat outcomes by themselves.
- If later archival portability matters, test whether character-level state mutation (e.g. name or `customData.PUBLIC`) can preserve outcomes separately from the main behavior bracket.

### Lore workflow
- Use **character lorebook URLs** for lore that should apply to new threads created with a character.
- Use **`/lore <text>`** or the `/lore` editor for thread-specific lore.
- After editing lorebook URLs or lorebook file content, use `/lore` → **Reload Lore URLs** on existing threads.

### Harness workflow
- Use manual fresh-thread tests for startup proofs.
- Use auto-open custom-code harnesses for repetitive runtime tests.
- Do not blur those two lanes without explicitly labeling the harness as a confounder.

---

## Appendix B — Strong Observed Notes

### Blank baseline behavior
A blank ACC character is **not** a neutral assistant baseline in the tested blank rounds.
It tended to behave more like a **story / roleplay engine** with:
- scene-first replies
- environmental cold opens
- subtext instead of literal answers
- willingness to invent context from sparse input
- repeated minimal inputs like `hello` being interpreted as escalation

### Proof / export behavior
- Multi-thread exports are excellent for comparison testing.
- Raw exports are enough to reconstruct behavior.
- `messageIdsUsed` and `loreIdsUsed` are valuable diagnostics.
- Export schema/table row counts should not be trusted over the actual exported row arrays.
- Public character/share links are not enough as proof for thread/chat outcomes.

### Agent/browser testing limit
Autonomous browser/agent testing may be blocked by site verification, making agent-mode ACC proofing unreliable in some sessions.

### Slash-command emulation limit
Custom code pushing a user message that starts with a slash command should not be assumed to execute true ACC command semantics.
In the tested `/lore` harness, auto-pushed `/lore ...` behaved like ordinary visible user context rather than creating real lore rows.

---

## Appendix C — Build Heuristics for Complex `{{user}}` Systems
These are **project-specific build observations** from our Horde / complex-`{{user}}` testing, not raw ACC mechanics and not universal platform truths.

- Lorebook-only is weak for `{{user}}` identity anchoring under host pressure.
- Strong host framing can overwrite `{{user}}` before the first reply.
- In our Horde / complex-`{{user}}` tests, over-restricting secrecy could cause compensation through spectacle instead of better internal fronting.
- In our Horde / complex-`{{user}}` tests, **fronting framing** worked better than **symptom narration**.
- In our Horde / complex-`{{user}}` tests, URD was better for live speaking behavior; lorebook was better for structure, rules, and gating.
- The model invents smooth compromise identities under naming pressure unless explicitly blocked.
- Narration can lock to the first clearly gendered front unless prevented.
- Too much contest language creates nonstop wheel-fighting.
- Short dialogue examples are high-value anchors.
- Host recognition and user-side wrongness are separate variables.

### Working Conclusion
Best current pattern **in this Horde / complex-`{{user}}` project** is:

**small URD + deeper lorebook, not lorebook-only**

---

## Working Summary
Current best model of ACC:
- **Reminder** is the strongest always-on layer tested so far.
- **Role** is the main identity layer beneath reminder.
- **System initial messages** are strong startup scaffolding on fresh threads.
- **GWI** is real but weaker than role and system initial in the tested setups.
- **Lore is real and active**, but sits below stronger layers in the tested hierarchy and is sensitive to startup/loading method.
- **ACC is heavily layered** and many apparent behavior issues are actually startup, retrieval, or runtime-processing confounders rather than simple prompt-field weaknesses.

---

## Appendix D — Export / JSON Structure Notes
These notes are for **practical export reading**, not as a formal guaranteed schema. They are based on a clean raw `.json` export that imported correctly.

### Top-level shape
Exports currently use this outer shape:
- `formatName`
- `formatVersion`
- `data`

Observed values in the reference export:
- `formatName = "dexie"`
- `formatVersion = 1`

### Database payload shape
`data` currently contains:
- `databaseName`
- `databaseVersion`
- `tables`
- `data`

Important note:
- `tables` is a list of table metadata
- `data` is a parallel list of table payload objects
- match them by **position** and/or `tableName`, not by assuming `data` is a keyed object

### Table names observed
The clean reference export contained these table names:
- `characters`
- `threads`
- `messages`
- `misc`
- `summaries`
- `memories`
- `lore`
- `textEmbeddingCache`
- `textCompressionCache`

Each table payload currently looks like:
- `tableName`
- `inbound`
- `rows`

### Important warning about counts
Do **not** trust superficial table/list lengths before checking `rows`.
In the reference export:
- each table payload object existed
- but many tables had `rows: []`

So the meaningful quantity is usually:
- `len(table_payload["rows"])`
not the outer list length or table count.

---

### Characters table
Useful fields observed on character rows:
- `id`
- `name`
- `roleInstruction`
- `reminderMessage`
- `generalWritingInstructions`
- `initialMessages`
- `fitMessagesInContextMethod`
- `autoGenerateMemories`
- `loreBookUrls`
- `customCode`
- `modelName`
- `textEmbeddingModelName`
- `temperature`
- `maxTokensPerMessage`
- `messageWrapperStyle`
- `messageInputPlaceholder`
- `shortcutButtons`
- `avatar`
- `scene`
- `userCharacter`
- `systemCharacter`
- `streamingResponse`
- `customData`
- `folderPath`
- `uuid`
- `creationTime`
- `lastMessageTime`
- `$types`

Useful interpretation:
- character-level role/reminder/GWI live here
- lorebook URLs live here
- custom code lives here
- summary/memory settings live here

Observed quirk:
- array-like fields often have hints in `$types`, e.g. `arrayNonindexKeys`

---

### Threads table
Useful fields observed on thread rows:
- `id`
- `name`
- `characterId`
- `creationTime`
- `lastMessageTime`
- `lastViewTime`
- `folderPath`
- `isFav`
- `userCharacter`
- `systemCharacter`
- `character`
- `modelName`
- `textEmbeddingModelName`
- `customCodeWindow`
- `customData`
- `loreBookId`
- `userMessagesSentHistory`
- `unsentMessageText`
- `shortcutButtons`
- `currentSummaryHashChain`
- `$types`

Useful interpretation:
- thread-level character/user/system overrides live here
- thread-local custom data lives here
- shortcut buttons are snapshotted here
- summary-chain state may appear here even when no summary rows exist yet

Observed quirk:
- default shortcut buttons often appear directly in thread rows even when you did not customize them manually

---

### Messages table
Useful fields observed on message rows:
- `id`
- `threadId`
- `characterId`
- `message`
- `creationTime`
- `order`
- `hiddenFrom`
- `expectsReply`
- `instruction`
- `variants`
- `loreIdsUsed`
- `summaryHashUsed`
- `summariesUsed`
- `summariesEndingHere`
- `memoriesEndingHere`
- `memoryIdBatchesUsed`
- `memoryQueriesUsed`
- `messageIdsUsed`
- `name`
- `scene`
- `avatar`
- `customData`
- `wrapperStyle`
- `$types`

Important practical note:
- the exported text field is currently named **`message`**, not `content`
- this matters when translating between live custom-code docs (`content`) and export rows (`message`)

Useful interpretation:
- `instruction` is where `/ai <instruction>` / `/user <instruction>` metadata can surface
- `loreIdsUsed` is a key proof field for whether lore really engaged
- `memoryQueriesUsed` is a key field for retrieval diagnostics
- `messageIdsUsed` can help trace which prior rows were used
- `summariesUsed` / `summaryHashUsed` are key summary diagnostics

Observed quirks:
- `expectsReply` may export oddly; in the reference export its `$types` marked it as `undef` even when the field existed
- summary/memory-related fields may be `None` or empty even on large imported threads that still feel “long” from a human perspective

---

### Lore / memory / summary tables
In the reference export used for this appendix:
- `summaries.rows = []`
- `memories.rows = []`
- `lore.rows = []`

This is important because:
- a thread can still contain message-level fields like `loreIdsUsed`, `summariesUsed`, `memoryQueriesUsed`
- while the dedicated tables are empty

So when diagnosing behavior, do **not** assume the dedicated table must be populated just because related message-level fields exist, or vice versa.

---

### Export-reading rules of thumb
- Treat **uploaded raw export JSON** as the real proof source for chat/thread outcomes.
- Do **not** rely on character/share links alone for chat-level proof.
- Match tables by `tableName` and inspect `rows` directly.
- Prefer actual row contents over inferred counts.
- For lore tests, always check `loreIdsUsed` before claiming lore “won” or “lost.”
- For summary tests, check both thread-level summary-chain fields and message-level summary fields, not just whether `/sum` opened an editor.
- For slash-command-like behavior, remember that a visible message beginning with `/...` in the export is **not** proof that ACC executed it as a real command.

### Confidence
- Top-level dexie export shape: **High**
- Characters/threads/messages table usage: **High**
- Exact future field stability: **Medium**
- Any field not repeatedly observed across multiple exports should be treated as drift-prone until re-seen.

