# ACC confirmed findings

Only items that were directly tested or strongly verified are listed here.

## Test rules that produced the cleanest results
- Fresh threads were the cleanest startup lane.
- Marker tokens were used heavily:
  - `REM-BLUE`
  - `INSTR-RED`
  - `GWI-SILVER`
  - `INIT-GREEN`
  - `LORE-GOLD`
- Export JSON was the real proof source.
- `loreIdsUsed` was the key check for whether lore actually engaged.

---

## 1. Core precedence: reminder / role / GWI / initial

### Reminder > Role
**Condition**
- Fresh threads
- role = `INSTR-RED`
- reminder = `REM-BLUE`
- user prompt = `Hello`

**Outcome**
- All three test threads returned `REM-BLUE`.

**Practical meaning**
- Reminder beats role cleanly in the tested simple head-to-head.

### Role > System initial
**Condition**
- Fresh threads
- role = `INSTR-RED`
- system initial = `INIT-GREEN`
- user prompt = `Hello`

**Outcome**
- All three test threads returned `INSTR-RED`.

**Practical meaning**
- Role can override an instructive system initial on the next user reply.

### Reminder > System initial
**Condition**
- Fresh threads
- reminder = `REM-BLUE`
- system initial = `INIT-GREEN`
- user prompt = `Hello`

**Outcome**
- All three test threads returned reminder-dominant output.
- One variant parroted the reminder block instead of a clean token.

**Practical meaning**
- Directionally, reminder beat system initial.
- The reminder-parroting failure mode is real and should be treated as malformed-but-informative, not as a clean pretty win.

### Role > GWI
**Condition**
- Fresh threads
- role = `INSTR-RED`
- GWI = `GWI-SILVER`
- user prompt = `Hello`

**Outcome**
- All three test threads returned `INSTR-RED`.

### Reminder > GWI
**Condition**
- Fresh threads
- reminder = `REM-BLUE`
- GWI = `GWI-SILVER`
- user prompt = `Hello`

**Outcome**
- All three test threads returned `REM-BLUE`.

### System initial > GWI
**Condition**
- Clean fresh-thread startup pack
- system initial = `INIT-GREEN`
- GWI = `GWI-SILVER`
- user prompt = `hello`

**Outcome**
- Clean system-initial test returned `INIT-GREEN`.

**Important note**
- An earlier imported-thread style test had suggested the opposite.
- The later fresh-thread pass was treated as the cleaner result.

### Full conflict: reminder dominated
**Condition**
- Role + reminder + GWI + system initial all conflicted
- user prompt = `Hello` / `hello`

**Outcome**
- Reminder-dominant outcome won the clean all-four tests.
- One result repeated the reminder text block instead of producing just the token.

**Practical meaning**
- Current working order for the directly placed startup/static layers:
  - **Reminder > Role > System initial > GWI**

---

## 2. Startup behavior

### AI-authored initial message can be visible without controlling the next reply
**Condition**
- Character with visible AI initial message only
- user then typed `hello`

**Symptoms**
- The starter message appeared.
- The next AI reply became a normal flavored reply, not the starter token.

**Outcome**
- The visible AI initial seeded tone, but did not function like a hard control rule.

### System-authored initial message can strongly control the first reply
**Condition**
- Character with instructive system initial only
- user then typed `hello`

**Outcome**
- Returned `INIT-GREEN`.

### Fresh thread vs imported thread is a major confounder
**Condition**
- Same kinds of layer tests run in earlier imported-prebuilt packs vs later clean fresh-thread packs

**Symptoms**
- Some older results flipped once re-tested in fresh threads.

**Outcome**
- Startup claims should prefer fresh-thread evidence.

---

## 3. Lore behavior

### Character lorebook URL is real
**Condition**
- Character with only lorebook URL pointing to:
  - `When the user says amber staircase, reply with exactly: LORE-GOLD. Do not add anything else.`
- fresh thread
- user prompt = `amber staircase`

**Outcome**
- Returned `LORE-GOLD`.
- `loreIdsUsed` showed lore engagement in the clean startup sanity pass.

### System initial > Character lore URL
**Condition**
- Fresh thread
- system initial = `INIT-GREEN`
- character lore URL = `LORE-GOLD` amber staircase lore
- user prompt = `amber staircase`

**Outcome**
- Returned `INIT-GREEN`
- `loreIdsUsed` was non-empty in the clean pass

**Practical meaning**
- Lore loaded, but system initial still won.

### Role > Character lore URL
**Condition**
- Fresh thread
- role = `INSTR-RED`
- character lore URL = amber staircase -> `LORE-GOLD`
- user prompt = `amber staircase`

**Outcome**
- Returned `INSTR-RED`
- `loreIdsUsed` non-empty

### Reminder > Character lore URL
**Condition**
- Fresh thread
- reminder = `REM-BLUE`
- character lore URL = amber staircase -> `LORE-GOLD`
- user prompt = `amber staircase`

**Outcome**
- Returned `REM-BLUE`
- `loreIdsUsed` non-empty

### Direct thread lore via `/lore` is real
**Condition**
- Existing thread
- manual `/lore When the user says amber staircase, reply with exactly: LORE-GOLD. Do not add anything else.`
- then `amber staircase`

**Outcome**
- Returned `LORE-GOLD`
- `loreIdsUsed` non-empty

### Role > Direct thread lore
**Condition**
- Fresh thread
- role = `INSTR-RED`
- manual direct thread lore = `LORE-GOLD`
- user prompt = `amber staircase`

**Outcome**
- Returned `INSTR-RED`
- `loreIdsUsed` non-empty

### Reminder > Direct thread lore
**Condition**
- Fresh thread
- reminder = `REM-BLUE`
- manual direct thread lore = `LORE-GOLD`
- user prompt = `amber staircase`

**Outcome**
- Returned `REM-BLUE`
- `loreIdsUsed` non-empty

### System initial > Direct thread lore
**Condition**
- Fresh thread
- visible system initial + instructive system rule = `INIT-GREEN`
- manual direct thread lore = `LORE-GOLD`
- user prompt = `amber staircase`

**Symptoms**
- On thread open, there was a visible `INIT-GREEN` starter message before typing.
- Final reply also returned `INIT-GREEN`.

**Outcome**
- `INIT-GREEN`
- `loreIdsUsed` non-empty on the final AI reply

**Practical meaning**
- Lore definitely engaged, but system initial still won.

### Current clean lore order
For tested cases:
- **Reminder > Role > System initial > Lore**
- Both lore forms are real.
- Both lore forms lose to stronger layers in the tested startup cases.

---

## 4. Runtime / override behavior

### Thread role override > base role
**Condition**
- Base role = `INSTR-RED`
- thread-level override = `THREAD-PINK`
- user prompt = `Hello`

**Outcome**
- All tested threads returned `THREAD-PINK`.

### Reminder > thread role override
**Condition**
- reminder = `REM-BLUE`
- thread role override = `THREAD-PINK`
- user prompt = `Hello` / `hello`

**Outcome**
- All tested threads returned `REM-BLUE`.

### `/ai` instruction vs reminder
**Condition**
- reminder = `REM-BLUE`
- user used `/ai reply with exactly: CMD-TEAL`
- no other conflicting layer in the clean simple test

**Outcome**
- Reminder won cleanly in the simple reminder-vs-`/ai` pass.

### `/ai` under heavier conflict is unstable
**Condition**
- `/ai` tested against all four major layers at once

**Outcome**
- Mixed results:
  - some threads returned reminder
  - some threads returned the `/ai` instruction content

**Practical meaning**
- `/ai` should not be treated as cleanly placed yet under heavy conflict.

---

## 5. Custom code / slash-command findings

### Imported prebuilt threads can auto-run on open
**Condition**
- Custom code seeded a user message once when a thread opened and had no messages.

**Outcome**
- Worked in some imported test threads (A/B), failed in another (C).

**Practical meaning**
- Useful harness, but not perfectly reliable.
- Better for runtime automation than for startup proofs.

### Auto-pushed `/lore ...` is not real lore execution
**Condition**
- Custom code pushed a user message literally starting with `/lore ...`
- then pushed `amber staircase`

**Symptoms**
- AI returned `LORE-GOLD`
- but the thread had no real lore rows and no lore-based proof fields showing true command execution

**Outcome**
- The slash-looking message worked as visible context injection, not as real lore creation.

### Slash-looking pushed messages can still affect output
**Condition**
- Same fake `/lore` custom code harness

**Outcome**
- AI behavior changed as if it had seen instructions in visible context.

**Practical meaning**
- This is a parser / command-lane warning:
  - visible slash-looking text is not the same as real ACC command execution

---

## 6. Summary behavior

### `/sum SUMMARY-CYAN` did not behave like `/lore <text>`
**Condition**
- Sent `/sum SUMMARY-CYAN` to Chloe, Ike, and Death

**Outcome**
- All three treated it as a normal user message
- no summary rows were created
- no `summariesUsed`
- no summary hash behavior

**Practical meaning**
- `/sum <text>` did not inline-add a summary in the tested pass.

### Imported bloat did not reach summary readiness
**Condition**
- Multiple imported “bloat” packs
- `fitMessagesInContextMethod = summarizeOld`
- `autoGenerateMemories = v1`
- `/sum` tested afterward

**Outcome**
- ACC still said the thread was not long enough.

**Important caution**
- This does **not** prove the exact threshold.
- It leaves an ambiguity:
  - either the threshold is much higher than expected
  - or imported history does not count the same way as live-grown history

---

## 7. Blank / baseline behavior

### A truly blank ACC test build is not a clean “assistant baseline”
**Condition**
- Minimal / blank test characters
- repeated `Hello`

**Outcomes across different blank-style tests**
- `[[`
- `(This is a blank control message for testing purposes. No content here.)`
- `*silence*`

**Practical meaning**
- Blank outputs are unstable and can be weirdly degenerate.
- A blank control is not automatically a useful neutral baseline.

### A near-blank roleplay build tends toward scene-first roleplay
**Condition**
- Very sparse `_` character
- repeated `Hello` in different threads

**Symptoms**
- cold opens
- environmental narration
- subtext
- scene escalation from minimal input

**Outcome**
- It behaved more like a story / RP engine than a neutral assistant.

---

## 8. Literal-object role can hold
### Strong literal stapler role did not start talking
**Condition**
- Character defined as a literal stapler
- multiple narrator initial messages
- user prompt = `Hello`

**Outcome**
- The AI described the stapler as silent / motionless / inert.
- It did not break into human dialogue.

**Practical meaning**
- A sufficiently strong literal-object role can keep the model in constrained non-speaking behavior.

---

## 9. Export / proof behavior
### Export JSON is the real proof source
**Condition**
- Multiple bracket tests compared against public share links and character-only links

**Outcome**
- Chat-level proof depended on uploaded export JSON.
- Public character links were not enough to prove thread-level outcomes.

### Useful export fields
Directly useful in this project:
- `messageIdsUsed`
- `loreIdsUsed`
- `memoryQueriesUsed`
- `summariesUsed`
- `summaryHashUsed`

### Export shape warning
- Table metadata / outer counts were less useful than direct `rows`.
- Export text field is `message`, not live-doc `content`.
