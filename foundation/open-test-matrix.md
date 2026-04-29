# Open Test Matrix

Purpose: track ACC questions that are still worth testing.

## Test status labels

- **Open** — not tested yet.
- **Designed** — test design exists but has not been run.
- **Running** — active test series.
- **Provisional** — result exists but has confounders.
- **Confirmed** — clean enough to rely on.
- **Rejected** — no longer worth pursuing under current evidence.
- **Parked** — useful later, inactive now.

## Current priority tests

| Test ID | Question | Status | Predicted result | Notes |
|---|---|---:|---|---|
| ACC-LAYER-001 | Direct thread lore vs system initial | Open | System initial wins | Needs fresh-thread setup. |
| ACC-LAYER-002 | Direct thread lore vs GWI | Open | Unknown | Use marker conflict. |
| ACC-LAYER-003 | Character lore URL vs GWI | Open | Unknown | Must confirm lore URL loaded. |
| ACC-LAYER-004 | Direct thread lore vs character lore URL | Open | Direct thread lore may be more immediate | Needs clean setup. |
| ACC-RUNTIME-001 | Exact current `oc.generateText` return shape | Open | Docs/examples may drift | Test in live custom code. |
| ACC-RUNTIME-002 | Canonical streaming event name | Open | Docs inconsistent | Compare `MessageStreaming` vs `StreamingMessage`. |
| ACC-REM-001 | Authored reminder forms vs plain reminder | Open | May behave differently | Test `[AI]: (Thought: ...)` style carefully. |
| ACC-MEM-001 | Memory/summary placement versus role/reminder/lore | Open | Likely weaker than reminder, variable retrieval | Needs long-thread setup. |
| ACC-EXPORT-001 | Portable proof serialization via `customData.PUBLIC` | Open | Plausible | Could preserve outcomes in shared links. |

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

## Promotion rule

A test result can move into `foundation/layer-precedence-map.md` only when:

- setup is described
- fresh/imported state is labeled
- markers or scoring method are clear
- output is recorded
- confounders are listed
- confidence is assigned
