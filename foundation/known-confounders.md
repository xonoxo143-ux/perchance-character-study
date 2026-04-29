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

## Practical rule

If a result looks surprisingly strong, check whether a hidden stronger layer or runtime effect could explain it.

If a result looks surprisingly weak, check whether the layer being tested actually loaded or was retrieved.

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
