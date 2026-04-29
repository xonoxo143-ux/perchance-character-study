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

### Lore / retrieval placement

| Test ID | Question | Status | Predicted result | Why it matters |
|---|---|---:|---|---|
| ACC-LAYER-002 | Direct thread lore vs GWI | Open | Unknown | Completes lore placement against style layer. |
| ACC-LAYER-003 | Character lore URL vs GWI | Open | Unknown | Completes character lore URL placement against style layer. |
| ACC-LAYER-004 | Direct thread lore vs character lore URL | Open | Direct thread lore may be more immediate | Clarifies conflict resolution between lore sources. |
| ACC-MEM-001 | Memory/summary placement versus role/reminder/lore | Open | Likely weaker than reminder, variable retrieval | Needed before treating long-thread behavior as simple forgetting or simple hierarchy. |

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
