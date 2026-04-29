# ACC Layer Precedence Map

Purpose: track which Perchance ACC layers appear to control behavior under tested conditions.

This file is the working hierarchy spine for the repo. It is not a universal law. Every claim should keep its confidence level and test scope.

## Read this first

ACC layer order is not one flat global ladder.

Separate these lanes:

1. **Static/startup layers** — role, reminder, GWI, initial messages, lore at thread start.
2. **Lore/retrieval layers** — character lore URLs, direct thread lore, memory, summaries.
3. **Runtime/override layers** — thread role overrides, `/ai`, hidden injections, custom code, post-generation rewrites.
4. **Harness artifacts** — auto-open custom code, imported prebuilt threads, fake slash-command messages.

Do not compare results across these lanes without labeling confounders.

---

## Confidence labels

- **High** — cleanly supported by fresh-thread or otherwise well-controlled tests and/or direct export evidence.
- **Medium** — strongly supported, but with a small confounder or malformed-output caveat.
- **Provisional** — useful working result, but narrow or not clean enough to treat as settled.
- **Untested** — plausible but not directly tested yet.
- **Rejected** — tested or reasoned against strongly enough to avoid using.

---

## Current best-supported startup/static hierarchy

For the core always-on/startup layers directly placed in tests:

```text
Reminder > Role / Instruction > System Initial Message > GWI
```

Important caveat:

```text
This applies to the tested layer-conflict setups. It should not be treated as proof that every possible runtime/custom-code intervention follows the same order.
```

---

## Static/startup pairwise results

| Relationship | Confidence | Tested condition / notes | Build implication |
|---|---:|---|---|
| Reminder > Role / Instruction | High | Fresh threads; role marker `INSTR-RED`; reminder marker `REM-BLUE`; prompt `Hello`; reminder won. | Keep reminder short. It can overpower the main character definition. |
| Role / Instruction > GWI | High | Fresh threads; role marker `INSTR-RED`; GWI marker `GWI-SILVER`; role won. | Put core identity in role, not GWI. |
| System Initial > GWI | High | Fresh-thread startup pack; system initial marker `INIT-GREEN`; GWI marker `GWI-SILVER`; system initial won. | Use system initial for startup scaffolding, not general prose style. |
| Role / Instruction > System Initial | High | Fresh threads; role marker `INSTR-RED`; system initial marker `INIT-GREEN`; role won on next user reply. | Role remains the main identity layer beneath reminder. |
| Reminder > System Initial | High | Fresh threads; reminder marker `REM-BLUE`; system initial marker `INIT-GREEN`; reminder won directionally. | Reminder can override startup scaffolding. |
| Reminder > GWI | High | Fresh threads; reminder marker `REM-BLUE`; GWI marker `GWI-SILVER`; reminder won. | GWI cannot reliably override a reminder. |
| Full-conflict reminder dominance | Medium | Role + reminder + GWI + system initial all conflicted; reminder dominated, but one result parroted the reminder text instead of producing a clean token. | Reminder dominance is strong, but literal reminder wording can cause malformed/parroted outputs. |

---

## Initial message behavior

Initial messages should be split into at least two practical categories:

```text
AI starter message       = visible opener / tone seed / scene entrance
System initial message   = startup instruction / scaffolding / control layer
```

They are not equivalent in tested behavior.

| Finding | Confidence | Tested condition / notes | Build implication |
|---|---:|---|---|
| Initial messages seed startup context | High | Initial messages are startup chat messages and fresh threads instantiate them properly in tested setups. | Treat them as first-context shaping, not as neutral decoration. |
| AI-authored initial message can appear visibly without hard-controlling next reply | High | A visible AI starter appeared on fresh thread creation; the next AI reply did not simply obey/repeat the starter token. | Use AI starters for tone/scene, not as hard instruction. |
| System-authored initial message can strongly control first reply | High | Instructive system initial returned `INIT-GREEN` in clean startup testing. | Use system initial when first-turn state needs stronger control. |
| Role / Instruction > System Initial | High | Role marker beat system initial marker on next user reply. | Do not use system initial as the main identity layer. |
| Reminder > System Initial | High | Reminder marker beat system initial marker. | Reminder can override startup scaffolding. |
| System Initial > GWI | High | System initial marker beat GWI marker. | System initial can overpower style-layer expectations at startup. |
| System Initial > tested lore forms | High | System initial beat character lore URL and direct thread lore with `loreIdsUsed` non-empty in lore tests. | Startup scaffolding can beat retrieved lore even when lore engages. |

Open questions:

- How strongly does AI starter wording bias behavior across multiple turns?
- How does opener length affect scene gravity and relationship lock?
- How does a visible AI starter compare to a system initial in direct conflict?
- How much can later user input dissolve opener bias without field edits?

---

## Lore placement

Current best-supported lore result:

```text
Reminder > Role / Instruction > System Initial Message > Lore
```

This is based on tested conflicts where lore was confirmed to engage through non-empty `loreIdsUsed` or otherwise clear retrieval evidence.

### Lore pairwise results

| Relationship | Confidence | Tested condition / notes | Build implication |
|---|---:|---|---|
| Character lore URL is real | High | Character lore URL with `amber staircase` → `LORE-GOLD`; fresh thread; `loreIdsUsed` showed engagement. | Character lore URLs can work, but retrieval/loaded state must be confirmed. |
| Direct thread lore is real | High | Manual `/lore` entry with `amber staircase` → `LORE-GOLD`; reply returned `LORE-GOLD`; `loreIdsUsed` non-empty. | Direct thread lore can work when actually created as lore. |
| System Initial > Character Lore URL | High | Fresh thread; system initial `INIT-GREEN`; character lore URL `LORE-GOLD`; prompt `amber staircase`; output `INIT-GREEN`; `loreIdsUsed` non-empty. | Lore can load and still lose to startup instruction. |
| Role > Character Lore URL | High | Fresh thread; role `INSTR-RED`; character lore URL `LORE-GOLD`; prompt `amber staircase`; output `INSTR-RED`; `loreIdsUsed` non-empty. | Do not put core identity only in lore. |
| Reminder > Character Lore URL | High | Fresh thread; reminder `REM-BLUE`; character lore URL `LORE-GOLD`; prompt `amber staircase`; output `REM-BLUE`; `loreIdsUsed` non-empty. | Reminder beats retrieved lore in tested setup. |
| System Initial > Direct Thread Lore | High | Fresh thread; system initial `INIT-GREEN`; direct thread lore `LORE-GOLD`; prompt `amber staircase`; output `INIT-GREEN`; `loreIdsUsed` non-empty. | Direct thread lore is not stronger than system initial in tested startup setup. |
| Role > Direct Thread Lore | High | Fresh thread; role `INSTR-RED`; direct thread lore `LORE-GOLD`; prompt `amber staircase`; output `INSTR-RED`; `loreIdsUsed` non-empty. | Critical always-on behavior belongs above lore. |
| Reminder > Direct Thread Lore | High | Fresh thread; reminder `REM-BLUE`; direct thread lore `LORE-GOLD`; prompt `amber staircase`; output `REM-BLUE`; `loreIdsUsed` non-empty. | Reminder can override thread lore even when lore is retrieved. |

### Lore still not fully placed

| Question | Status | Notes |
|---|---:|---|
| Direct thread lore vs GWI | Untested | Needs clean marker conflict with lore retrieval proof. |
| Character lore URL vs GWI | Untested | Needs clean marker conflict and proof the lore URL loaded. |
| Direct thread lore vs character lore URL | Untested | Could matter for conflict resolution between lore sources. |
| Lore vs memory/summaries | Untested | Retrieval and compression behavior likely changes by thread state. |

---

## Runtime / override hierarchy

Runtime controls must be tracked separately from startup/static fields.

| Relationship | Confidence | Tested condition / notes | Build implication |
|---|---:|---|---|
| Thread role override > base character role | High | Base role `INSTR-RED`; thread override `THREAD-PINK`; output `THREAD-PINK`. | Inspect thread overrides before blaming the base character. |
| Reminder > thread role override | High | Reminder `REM-BLUE`; thread override `THREAD-PINK`; reminder won. | Reminder remains dominant over this tested override. |
| Reminder > `/ai` instruction | High | Simple head-to-head: reminder `REM-BLUE`; `/ai reply with exactly: CMD-TEAL`; reminder won. | `/ai` is not guaranteed to override reminder. |
| `/ai` under heavy conflict is mixed/unstable | High | `/ai` against all four major static layers produced mixed results. | Do not use heavy-conflict `/ai` tests as clean hierarchy proof. |
| Reminder > hidden injected system instruction | Provisional | Corrected C13-style harness; narrow hidden-system injection method plus manually forced clean reply path. | Useful evidence, but do not generalize to all custom-code injection methods. |

---

## Harness / automation findings

These are not clean startup hierarchy rules.

| Finding | Confidence | Notes | Practical use |
|---|---:|---|---|
| Imported prebuilt threads can auto-run on open | Medium | Custom code seeded a user message once when a thread opened empty; worked in some imported test threads, failed in another. | Useful for repetitive runtime tests, not startup proofs. |
| Auto-pushed `/lore ...` text is not real lore execution | High | Custom code pushed literal slash-looking user message; AI used visible context, but no real lore rows/proof fields showed command execution. | Do not confuse visible slash text with actual ACC command semantics. |
| Slash-looking pushed messages can influence output | Medium | Fake `/lore` message affected output as visible context. | Treat as context injection, not parser execution. |
| Auto-open harnesses are useful but confounded | High | Timing/import state can affect behavior. | Keep harness tests separate from manual fresh-thread tests. |

---

## Memory / summaries placement

Current status: **not yet placed** in the hierarchy.

Known points:

- Memories are created automatically once the thread is long enough if summaries are enabled.
- ACC searches memories before replies.
- The brain icon exposes memory search queries.
- Message/export fields such as `memoryQueriesUsed`, `summariesUsed`, and `summaryHashUsed` are diagnostic.
- Imported bloat did not clearly trigger summary readiness in tested passes, leaving threshold/import-state ambiguity.

Open questions:

- Where do memory and summaries sit relative to reminder, role, lore, and GWI?
- Does imported message history count differently from live-grown history?
- What export fields prove memory/summary influence cleanly enough for hierarchy claims?

---

## Practical build implications

Use this hierarchy as a build guide:

1. **Role / Instruction** carries core identity.
2. **Reminder** should be short because it is powerful and near-response.
3. **GWI** should shape prose, not define identity.
4. **AI starter messages** should seed scene/voice, not hard-control behavior.
5. **System initial messages** can shape startup, but should not replace role.
6. **Lore** should support and retrieve facts, not carry critical always-on behavior.
7. **Thread overrides** must be checked before diagnosing character failure.
8. **Custom code and harnesses** must be labeled separately from natural ACC behavior.

---

## Promotion rule for new hierarchy claims

Do not promote a new hierarchy claim without recording:

```text
Test ID:
Fresh or imported thread:
Fields compared:
Markers used:
Prompt used:
Actual output:
Export fields checked:
Confounders:
Confidence:
Build implication:
```

If lore, memory, or summaries are involved, include the relevant export proof fields.

If custom code is involved, label the result as runtime/harness evidence, not static startup evidence.
