# ACC Layer Precedence Map

Purpose: track which Perchance ACC layers appear to control behavior under tested conditions.

This file is a working model, not a universal law. Every claim should keep its confidence label.

## Current best-supported static/startup hierarchy

```text
Reminder > Role / Instruction > System Initial Message > GWI
```

## Confirmed or strongly supported pairwise results

| Relationship | Confidence | Notes |
|---|---:|---|
| Reminder > Role / Instruction | High | Reminder is a hidden near-response layer and is hard for the AI to ignore. |
| Role / Instruction > GWI | High | Role is stronger for character identity than general whole-chat writing rules. |
| System Initial > GWI | High | Instructive system initial messages can strongly control first reply on fresh threads. |
| Role / Instruction > System Initial | High | Role won in direct tested setup. |
| Reminder > System Initial | High | Reminder remained dominant. |
| Reminder > GWI | High | Reminder beat whole-chat writing instructions. |
| Full-conflict reminder dominance | Medium | Directionally strong, but one major test produced reminder-parroting malformed output. |

## Lore placement

Current best-supported lore results:

| Relationship | Confidence | Notes |
|---|---:|---|
| System Initial > Character Lore URL | High | Tested on fresh thread first reply. |
| Role > Character Lore URL | High | Role beat character lore URL. |
| Reminder > Character Lore URL | High | Reminder beat character lore URL. |
| Role > Direct Thread Lore | High | Role beat direct thread lore. |
| Reminder > Direct Thread Lore | High | Reminder beat direct thread lore. |

## Not fully placed yet

- Direct thread lore vs system initial.
- Direct thread lore vs GWI.
- Character lore URL vs GWI.
- Direct thread lore vs character lore URL in clean setup.
- Summary/memory placement versus reminder/role/lore.

## Runtime hierarchy notes

| Relationship | Confidence | Notes |
|---|---:|---|
| Thread role override > base character role | High | Thread override can dominate base character role. |
| Reminder > thread role override | High | Reminder still beat thread role override in tested setup. |
| Reminder > `/ai` instruction | High | Simple head-to-head showed reminder dominance. |
| `/ai` under heavy conflict is mixed/unstable | High | Treat as runtime tool, not reliable final authority under conflict. |
| Reminder > hidden injected system instruction | Provisional | Narrow result in corrected C13-style harness. Useful but not generalized. |

## Practical build implications

- Put core identity in role/instruction.
- Keep reminder short and sharp; it is powerful and can distort behavior.
- Use GWI for broad writing/style rules, not identity.
- Use system initial messages for startup scaffolding, not long-term identity.
- Use lore for self-contained retrievable support material, not the core behavior spine.
- Check thread overrides before diagnosing a character as broken.

## Testing reminder

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
```
