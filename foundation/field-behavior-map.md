# ACC Field Behavior Map

Purpose: map Perchance ACC fields by practical behavior, best use, common misuse, symptoms, and test/fix approach.

## Field map

| Field / layer | Best use | Common misuse | Symptoms when misused | First fix/test |
|---|---|---|---|---|
| Role / Instruction | Core identity, stance, behavior, relationship frame | Giant lore dump or vague personality adjectives | Generic character, flattened behavior, inconsistent priorities | Rewrite into compact behavioral law; test against GWI/reminder conflicts |
| Reminder | Short near-response guardrail | Second full role block, literal token instruction, bloat | Parroting, overconstraint, stiffness, reminder dominating everything | Shorten reminder before rewriting role |
| GWI | Whole-chat writing rules, style, formatting, broad experience | Character identity or relationship control | Character ignores identity or style fights role | Move identity to role; leave prose/style in GWI |
| Initial Messages | Startup state, opening lane, seed context | Mini-screenplay, over-authored relationship, long canon dump | Opener bias, inherited-feeling replies, narrow first-turn behavior | Shorten opener; test fresh thread with same first user prompt |
| System Initial Message | Strong startup instruction | Long-term identity replacement | First reply obeys, later behavior drifts or conflicts | Use only for startup scaffolding; role handles identity |
| Character Lore URL | Shared lore for new threads | Core identity anchor | Lore feels ignored under role/reminder pressure | Check lore loaded; inspect `loreIdsUsed`; move critical identity upward |
| Direct Thread Lore | Thread-specific lore | Treating custom-code slash-looking message as real lore execution | Lore not actually created; AI treats slash text as visible context | Use real `/lore` editor/command; inspect export lore rows/ids |
| User role / description | User identity, relationship position, speaking assumptions | Overdetermining the user or forcing relationship | Character assumes too much, locks user into role | Keep user role small unless roleplay needs heavy framing |
| Custom code | Runtime hooks, rendering, harnesses, controlled automation | Hidden behavior that masks prompt-field results | Results cannot be attributed to fields cleanly | Disable code for layer tests; label harness tests separately |
| Memory / summaries | Long-thread recall and compression | Assuming summaries are neutral or always present | Behavior changes after long chat; retrieval seems inconsistent | Check summary/memory fields in export |
| Thread overrides | Per-thread role/reminder/user/system changes | Forgetting they exist | Base character seems to behave differently per thread | Inspect thread row overrides before diagnosing |

## Build principle

Each layer should have one job.

If the same instruction appears in role, reminder, GWI, opener, and lore, the character may seem strong at first but become brittle, repetitive, or overpowered by the wrong layer.

## Diagnosis shortcut

When a character fails, test in this order:

1. Is reminder too strong or too bloated?
2. Is role/instruction clear enough?
3. Is GWI carrying identity by mistake?
4. Is opener/initial message biasing the reply?
5. Is lore actually loaded and retrieved?
6. Are thread overrides active?
7. Is custom code rewriting or injecting behavior?
8. Are summaries/memory influencing the turn?

## Field confidence

This map should be updated with confidence labels as more tests are added.
