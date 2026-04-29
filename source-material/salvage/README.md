# Perchance ACC character-study export

## What this repo is
This zip is a handoff pack for continuing Perchance **AI Character Chat (ACC)** study work without reopening the full thread.

It is not a polished guide.
It is a working research bundle.

The material here is split into:
- **confirmed findings** from direct tests or strong verification
- **untested / partial theories**
- **layer interaction notes**
- **character-building patterns**
- **failed or parked ideas**
- **open questions**
- **mutation log** showing how the project changed over time
- **examples** that can be reused directly

## What problem this thread was solving
The thread was trying to answer two linked questions:

1. **How ACC layers actually interact in practice**
   - role / instruction
   - reminder
   - GWI
   - system initial messages
   - AI initial messages
   - character lorebook URLs
   - direct thread lore via `/lore`
   - thread overrides
   - slash commands
   - custom code

2. **How to build better ACC characters without false diagnoses**
   - when the problem is really the opener, not the role
   - when lore is doing the wrong job
   - how duplication across layers flattens characters
   - how to structure complex user / host / system builds
   - how to test cleanly instead of vibes-only editing

## How to use this zip
Suggested order:

1. `ACC_CONFIRMED_FINDINGS.md`
2. `ACC_LAYER_BEHAVIOR_NOTES.md`
3. `CHARACTER_STRUCTURE_PATTERNS.md`
4. `FAILED_OR_REJECTED_IDEAS.md`
5. `OPEN_QUESTIONS.md`
6. `EXAMPLES/`

## Scope notes
- This pack focuses on **ACC / character study**, not the later off-topic AI-consciousness discussion.
- Some build notes are **project-specific** to the Horde / complex-`{{user}}` work. Those are labeled as such.
- Some earlier tests were later found to be confounded by **fresh-thread vs imported-thread** differences. Those are kept, but marked accordingly.

## Short caution list
- Do not merge confirmed behavior and theory.
- Do not use imported prebuilt threads as if they were fresh startup proofs.
- Do not assume slash-looking text pushed by custom code is a real slash command.
- Do not assume lore “lost” unless lore actually loaded / `loreIdsUsed` shows it engaged.
- Do not over-rewrite a role block when the real problem is opener / cadence / GWI / duplication.
