# Known ACC Confounders

Purpose: preserve the traps that can make a character or test look broken when the real cause is hidden state, layer interaction, or harness behavior.

## Major confounders

- Fresh thread vs imported prebuilt thread.
- Reminder parroting when reminder text is phrased too literally.
- Character lore URL not loaded into a thread yet.
- Post-generation rewrites from custom code.
- Reply length limits changing behavior.
- Thread role overrides silently changing behavior.
- Auto-open harness timing and race issues.
- Slash-looking pushed messages being mistaken for real slash-command execution.
- Site verification/browser gating during autonomous external testing.
- Summary/memory state changing long-thread behavior.
- Token budget / input crowding.
- Community folk models that collapse all fields into “just one prompt.”

## Practical rule

If a result looks surprisingly strong, check whether a hidden stronger layer or runtime effect could explain it.

If a result looks surprisingly weak, check whether the layer being tested actually loaded or was retrieved.

## Token budget / input crowding rule

Public/community explanations correctly warn that role, reminder, GWI, lore, memory, summaries, initial messages, and recent chat can all compete inside the model's input context.

This matters because a field can appear weak for more than one reason:

- it may be lower priority
- it may be crowded out
- it may be contradicted by recent context
- it may be summarized or stale
- it may not have been retrieved
- it may be present but too vague

Important correction:

```text
Everything contributes to the input, but fields do not behave identically under conflict.
```

Do not reduce ACC behavior to “it is all just one prompt.” Our marker tests show field placement still matters.

## Fresh/import rule

Do not compare imported prebuilt threads to fresh UI-created threads without labeling the import state.

Imported threads can contain pre-existing messages, custom data, overrides, shortcut snapshots, summary chain state, or stale context.

## Lore-loading rule

Before saying lore lost, check whether lore was actually present and retrieved.

Useful diagnostics:

- `loreIdsUsed`
- lore table rows
- character lorebook URLs
- thread lorebook ID
- `/lore` reload status

## Custom-code rule

Disable custom code for clean layer-precedence tests unless the test is specifically about runtime hooks.

If custom code is active, label the result as harness/runtime evidence, not pure startup-layer evidence.
