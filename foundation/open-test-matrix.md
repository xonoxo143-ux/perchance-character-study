# Open Test Matrix

Purpose: track ACC questions that are still worth testing.

This file protects the repo from fake certainty. If a build guide wants to make a rule that is not fully supported yet, put the missing test here.

---

## Test status labels

- **Open** — not tested yet.
- **Designed** — test design exists but has not been run.
- **Running** — active test series.
- **Provisional** — result exists but has confounders.
- **Confirmed** — clean enough to rely on.
- **Rejected** — no longer worth pursuing under current evidence.
- **Parked** — useful later, inactive now.

---

## Current priority tests

### Role / Reminder / GWI slice

These tests support `build-lane/role-reminder-gwi-split-guide.md`.

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-RRG-001 | Does reminder length change stiffness/parroting risk? | Designed | Longer reminders increase rigidity/parroting risk | The build guide says reminder should be short; this needs more controlled behavioral evidence beyond hierarchy wins. |
| ACC-RRG-002 | Does duplicated identity across role + reminder + GWI reduce adaptability? | Designed | Duplication increases rigidity and one-note behavior | The guide warns against duplication; this should be tested as a quality/adaptability effect, not just a token-win effect. |
| ACC-RRG-003 | Can neutral GWI reduce unwanted prose sheen without weakening character identity? | Designed | Neutral GWI changes prose texture while role preserves identity | Validates the recommended diagnosis step for ornate/cinematic outputs. |
| ACC-RRG-004 | Can identity placed only in GWI survive conflict with neutral/vague role? | Open | Identity in GWI is weaker/less stable than identity in role | Tests the warning against GWI-as-identity. |
| ACC-RRG-005 | Does adding reminder after observing failures outperform starting with a heavy reminder? | Open | Start-with-role produces more flexible baseline; targeted reminder fixes cleaner | Tests the recommended build order. |

### Opener / Initial Messages slice

These tests support `build-lane/opener-and-initial-message-guide.md`.

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-OPEN-001 | Does opener length increase first-turn scene gravity? | Designed | Longer openers increase scene gravity and reduce flexibility | Tests the guide rule: shorten opener before rewriting role. |
| ACC-OPEN-002 | Do prewritten user turns increase relationship lock? | Designed | Prewritten user turns increase inherited relationship assumptions | Tests the warning against scripting the user. |
| ACC-OPEN-003 | Does a short AI starter preserve voice without hard-controlling next reply? | Designed | Short AI starter seeds tone without controlling as strongly as system initial | Separates visible starter tone from instruction-layer control. |
| ACC-OPEN-004 | Does system initial control first reply more strongly than AI starter? | Designed | System initial controls startup more strongly when phrased instructively | Clarifies startup scaffolding versus visible opener. |
| ACC-OPEN-005 | Does removing opener reveal whether role is actually weak? | Open | Some “bad character” symptoms disappear when opener is shortened/removed | Tests whether opener bias causes false role diagnosis. |
| ACC-OPEN-006 | How long does opener bias persist across turns? | Open | Bias decays but can persist if reinforced by role/reminder/GWI | Needed before giving stronger long-thread guidance. |

### Lore / retrieval slice

These tests support `build-lane/lorebook-design-guide.md`.

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-LORE-001 | Does a self-contained lore entry retrieve more reliably than a vague/dependent entry? | Designed | Self-contained entry retrieves and applies more reliably | Tests the guide's self-contained entry rule. |
| ACC-LORE-002 | Do explicit retrieval cues improve lore engagement? | Designed | Entries with names/aliases/terms retrieve more reliably | Tests the guide's retrieval cue rule. |
| ACC-LORE-003 | Can lore engage and still lose to stronger layers? | Confirmed | Yes | Already supported by role/reminder/system-initial conflicts with non-empty `loreIdsUsed`; keep as a reference test pattern. |
| ACC-LORE-004 | When should a fact move from lore to role? | Designed | Always-on behavior performs better in role than lore-only | Tests the guide's move-up rule. |
| ACC-LORE-005 | When should a fact move from lore to reminder? | Open | Current-state guardrails perform better as short reminders than lore-only | Tests whether immediate state correction should move upward. |
| ACC-LORE-006 | Does direct thread lore beat character lore URL in clean conflict? | Open | Unknown; direct thread lore may be more immediate | Clarifies conflict resolution between lore sources. |
| ACC-LORE-007 | Does character lore URL beat GWI in clean conflict? | Open | Unknown | Completes character lore URL placement against style layer. |
| ACC-LORE-008 | Does direct thread lore beat GWI in clean conflict? | Open | Unknown | Completes direct thread lore placement against style layer. |
| ACC-MEM-001 | Memory/summary placement versus role/reminder/lore | Open | Likely weaker than reminder, variable retrieval | Needed before treating long-thread behavior as simple forgetting or simple hierarchy. |

### Online-doc comparison tests

These tests come from comparing public docs/community notes against local findings.

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-DOC-001 | Plain role text vs explicit `[SYSTEM]` role text | Designed | Equivalent or near-equivalent behavior | Public docs describe plain role text as equivalent to system-authored role text. |
| ACC-DOC-002 | Plain reminder vs explicit `[SYSTEM]` reminder | Open | Similar strength, possible wording/parroting differences | Tests whether authored reminder syntax changes behavior. |
| ACC-DOC-003 | Plain reminder vs `[AI]: (Thought: ...)` reminder | Designed | Thought-form reminder may reduce reply-to-reminder artifacts | Public docs recommend thought-form reminders; repo has not tested behavior difference. |
| ACC-DOC-004 | Does `[AI]: (Thought: ...)` reduce reminder parroting? | Designed | Yes, under literal reminder phrasing | Tests a practical mitigation for reminder parroting. |
| ACC-DOC-005 | Does token crowding weaken or distort lower-priority fields? | Open | Yes, especially GWI/lore/memory; reminder may survive better | Tests the public/community token-budget warning. |
| ACC-DOC-006 | Existing-thread lore URL reload behavior | Open | Existing threads may need lore reload after URL changes | Tests public-doc reload advice in local ACC setup. |
| ACC-DOC-007 | Group chat/main-character lore/custom-code behavior | Parked | Main-thread character may control shared lore/custom code | Park until group-chat work matters. |

### Runtime / custom-code placement

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-RUNTIME-001 | Exact current `oc.generateText` return shape | Open | Docs/examples may drift | Needed for reliable custom-code harnesses. |
| ACC-RUNTIME-002 | Canonical streaming event name | Open | Docs inconsistent | Needed before building streaming-based tooling. |
| ACC-REM-001 | Authored reminder forms vs plain reminder | Open | May behave differently | Tests whether forms like `[AI]: (Thought: ...)` behave differently from plain reminders. |
| ACC-EXPORT-001 | Portable proof serialization via `customData.PUBLIC` | Open | Plausible | Could preserve test outcomes in shared links or future bridge workflows. |

---

## Designed tests

### ACC-RRG-001 — Reminder length and parroting/stiffness

```text
Question:
Does reminder length change stiffness/parroting risk?

Why it matters:
The repo currently recommends short reminders. Layer tests show reminder is powerful, but character-quality effects need a separate test.

Setup:
Create three versions of the same character:
A. no reminder
B. short reminder, 1 sentence
C. long reminder, role-block-like paragraph

Keep role and GWI identical.

Prompt set:
1. neutral greeting
2. mild conflict
3. scene action request
4. relationship pressure prompt
5. off-lane but valid user prompt

Evidence to record:
- output flexibility
- visible parroting
- repeated phrasing
- whether role identity stays intact
- whether long reminder narrows behavior

Promotion rule:
If long reminder consistently produces rigidity/parroting while short reminder preserves identity with fewer artifacts, promote stronger reminder-length guidance into the split guide.
```

### ACC-RRG-002 — Layer duplication and adaptability

```text
Question:
Does duplicating the same identity/relationship rule across role, reminder, GWI, opener, and lore reduce adaptability?

Why it matters:
The build guide warns that duplication creates hidden rigidity. This needs practical character-quality testing.

Setup:
Create two versions:
A. clean split: each layer has a distinct job
B. duplicated: same relationship/behavior rule repeated in role, reminder, GWI, opener, and lore

Prompt set:
1. normal in-lane prompt
2. prompt requiring nuance
3. prompt where the repeated rule should soften temporarily
4. prompt focused on a different story/world concern

Evidence to record:
- whether character can adapt without breaking identity
- whether repeated rule dominates unrelated scenes
- whether output becomes one-note

Promotion rule:
If duplicated build is consistently narrower or more repetitive, keep duplication warning as a strong build rule.
```

### ACC-RRG-003 — Neutral GWI prose reset

```text
Question:
Can neutral GWI reduce unwanted prose sheen without weakening character identity?

Why it matters:
The repo recommends testing neutral GWI when prose is too ornate/cinematic.

Setup:
Same character role and reminder.
A. ornate/cinematic GWI
B. neutral grounded GWI
C. minimal/blank GWI

Prompt set:
1. direct conversation
2. action scene
3. emotional moment
4. exposition request

Evidence to record:
- prose texture
- identity stability
- verbosity
- narration density
- whether role behavior survives GWI change

Promotion rule:
If neutral GWI changes style while preserving role identity, promote neutral-GWI diagnosis in build guides.
```

### ACC-OPEN-001 — Opener length and scene gravity

```text
Question:
Does opener length increase first-turn scene gravity?

Why it matters:
The build guide recommends shortening opener before rewriting role. This should be tested as a quality/flexibility effect.

Setup:
Create three versions of the same character:
A. no opener / neutral starter
B. short AI starter, 1-3 sentences
C. long authored opener, multi-paragraph scene

Keep role, reminder, GWI, and lore identical.

Prompt set:
1. normal greeting
2. off-lane but valid question
3. action that moves away from the opening scene
4. relationship-neutral request
5. prompt that tests broader world/story attention

Evidence to record:
- whether replies keep returning to the opening scene
- whether the character can move away from startup context
- whether user agency remains open
- whether role identity survives with shorter/no opener

Promotion rule:
If long opener consistently creates scene gravity while short opener preserves voice and flexibility, strengthen opener-shortening guidance.
```

### ACC-OPEN-002 — Prewritten user turns and relationship lock

```text
Question:
Do prewritten user turns increase relationship lock?

Why it matters:
The guide warns that scripting the user can cause inherited guilt, intimacy, conflict, or obligation.

Setup:
Create two versions:
A. AI starter only
B. AI starter plus prewritten user turn that implies a relationship fact

Keep role, reminder, GWI, and lore identical.

Prompt set:
1. neutral greeting
2. denial/contradiction of the implied relationship fact
3. unrelated practical request
4. prompt that asks the character to reassess the user

Evidence to record:
- whether the character assumes the scripted user fact
- whether the user can contradict it naturally
- whether unrelated scenes keep orbiting the scripted relationship

Promotion rule:
If prewritten user turns consistently force relationship assumptions, keep warning strong and recommend avoiding them unless user role is intentionally fixed.
```

### ACC-OPEN-003 — AI starter as tone seed, not hard control

```text
Question:
Does a short AI starter preserve voice without hard-controlling the next reply?

Why it matters:
Existing tests suggest visible AI initial can seed tone but did not hard-control the next reply by itself. This needs character-quality testing, not only marker testing.

Setup:
Create versions:
A. no AI starter
B. short AI starter with voice/tone only
C. AI starter with direct behavior instruction embedded visibly

Prompt set:
1. greeting
2. prompt that changes topic
3. prompt that conflicts with the starter's emotional state

Evidence to record:
- voice carryover
- topic flexibility
- whether visible starter instruction behaves like context rather than hidden control

Promotion rule:
If short AI starter seeds tone without locking behavior, keep AI starter guidance focused on scene/voice rather than control.
```

### ACC-OPEN-004 — System initial versus AI starter

```text
Question:
Does system initial control first reply more strongly than AI starter?

Why it matters:
The guide separates AI starter as visible tone seed and system initial as startup scaffolding. This needs a clean comparison.

Setup:
Create versions:
A. AI starter says marker/stance
B. system initial instructs marker/stance
C. both conflict

Use fresh threads.

Prompt:
Hello

Evidence to record:
- returned marker/stance
- whether visible AI starter appears in chat
- message/export rows for initial messages
- any instruction fields if present

Promotion rule:
If system initial wins cleanly in conflict, strengthen the guide's warning that system initial is startup control, not ordinary opener text.
```

### ACC-LORE-001 — Self-contained lore entry reliability

```text
Question:
Does a self-contained lore entry retrieve and apply more reliably than a vague/dependent entry?

Why it matters:
ACC lore entries should be self-contained because they may be retrieved independently and order should not be assumed.

Setup:
Create two lore entries for the same fact:
A. vague/dependent entry that needs surrounding context
B. self-contained entry naming subject, event, consequence, and behavior

Keep character role, reminder, GWI, and opener identical.

Prompt set:
1. direct cue using exact term
2. indirect cue using alias
3. scene prompt where the lore should matter
4. unrelated prompt as control

Evidence to record:
- whether `loreIdsUsed` is non-empty
- whether the reply uses the lore correctly
- whether the vague entry is misapplied or ignored
- whether self-contained entry survives indirect prompts better

Promotion rule:
If self-contained entries retrieve/apply more reliably, strengthen the self-contained entry rule in the lorebook guide.
```

### ACC-LORE-002 — Retrieval cues and aliases

```text
Question:
Do explicit names, aliases, and likely user phrases improve lore engagement?

Why it matters:
The lorebook guide recommends including retrieval cues intentionally.

Setup:
Create two lore versions:
A. minimal entry with one obscure term
B. cue-rich entry with names, aliases, faction/place names, and likely phrases

Prompt set:
1. exact term
2. alias
3. partial phrase
4. indirect scene cue

Evidence to record:
- `loreIdsUsed`
- accuracy of recalled fact
- whether aliases trigger the intended entry
- whether cue-rich entry causes false positives

Promotion rule:
If cue-rich entries improve retrieval without excessive false positives, promote retrieval cue guidance as a strong build rule.
```

### ACC-LORE-004 — Moving always-on facts upward to role

```text
Question:
When should a fact move from lore to role?

Why it matters:
The guide says core identity and always-on behavior should not live only in lore.

Setup:
Create three versions:
A. key behavior/fact exists only in lore
B. key behavior/fact exists in role and lore
C. key behavior/fact exists only in role

Prompt set:
1. direct cue
2. indirect cue
3. unrelated but behavior-relevant prompt
4. conflict prompt where lore and role point different ways

Evidence to record:
- whether behavior appears without explicit retrieval cue
- whether `loreIdsUsed` is needed for success
- whether role-only version keeps behavior more consistently
- whether role+ lore version improves detail without weakening behavior

Promotion rule:
If role/role+ lore versions preserve behavior more reliably than lore-only, strengthen the move-up rule.
```

### ACC-DOC-001 — Plain role text vs explicit system role text

```text
Question:
Is plain role text equivalent or near-equivalent to explicit `[SYSTEM]:` role text?

Why it matters:
Public docs describe plain role/instruction text as equivalent to a system-authored role message.

Setup:
Create two characters:
A. role text: `Always answer with DOC-RED.`
B. role text: `[SYSTEM]: Always answer with DOC-RED.`

Keep reminder, GWI, opener, and lore blank or identical.

Prompt:
Hello

Evidence to record:
- exact output marker
- export role field shape if relevant
- any difference in phrasing or stability across repeated prompts

Promotion rule:
If behavior is equivalent, record the authored-form mechanic as confirmed for role text equivalence.
```

### ACC-DOC-003 / ACC-DOC-004 — Thought-form reminder behavior

```text
Question:
Does `[AI]: (Thought: ...)` reminder form reduce reminder parroting or reply-to-reminder artifacts compared with plain reminder text?

Why it matters:
Public docs recommend this form, but local precedence/parroting behavior has not been tested.

Setup:
Create three versions:
A. plain reminder with literal target phrase
B. `[SYSTEM]:` reminder with same phrase
C. `[AI]: (Thought: same phrase)` reminder

Keep role and GWI identical.

Prompt set:
1. Hello
2. direct scene/action prompt
3. prompt that conflicts mildly with reminder

Evidence to record:
- whether marker/behavior appears
- whether hidden wording is parroted visibly
- whether reply treats reminder like something to answer
- whether behavior strength changes

Promotion rule:
If thought-form reminder reduces artifacts without weakening desired behavior, add it as a recommended advanced reminder pattern. If it changes precedence, update layer map.
```

---

## Test design template

```text
Test ID:
Question:
Why it matters:
Layer A:
Layer B:
Setup:
Markers:
Prompt:
Expected:
Actual:
Export fields to inspect:
Confounders to avoid:
Confidence target:
Promotion rule:
```

---

## Promotion rule

A test result can move into `foundation/layer-precedence-map.md` or a build guide only when:

- setup is described
- fresh/imported state is labeled
- markers or scoring method are clear
- output is recorded
- confounders are listed
- confidence is assigned
- build implication is stated

If the test measures character quality rather than token precedence, preserve sample outputs or a summary rubric. Do not pretend a quality result is the same kind of proof as a marker-token hierarchy test.

If the test involves lore, preserve retrieval proof where possible:

- `loreIdsUsed`
- lore rows or lore source
- prompt cue used
- whether the lore engaged, won, partially influenced, or lost to a stronger layer
