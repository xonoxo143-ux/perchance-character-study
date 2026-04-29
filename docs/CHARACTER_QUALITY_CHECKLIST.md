# Character Quality Checklist

Use this checklist to judge whether a Perchance ACC character is actually strong, not merely verbose.

## 1. Identity clarity

- Can the character be summarized in one sentence?
- Does role/instruction define identity without becoming a bloated lore dump?
- Is the character specific without being over-scripted?

## 2. Layer split

Check whether each field is doing the right job.

- Role/instruction: core identity and behavior.
- Reminder: short near-response guardrail.
- GWI: whole-chat style and experience rules.
- Lore: self-contained facts, background, structures, and retrievable details.
- Initial messages: startup state and opening lane.
- User role/description: user-facing identity or relationship assumptions.

Warning signs:

- Same rule repeated in role, reminder, and GWI.
- Reminder trying to be a second character sheet.
- GWI carrying identity.
- Lore carrying the core personality.
- Initial message over-authoring the whole relationship.

## 3. Voice stability

- Does the character keep the same behavioral stance across multiple prompts?
- Does it avoid becoming a generic assistant, narrator, therapist, or exposition machine?
- Does it preserve voice without copying exact example cadence forever?

Risks:

- example-dialogue cadence lock
- opener bias
- style flattening
- relationship over-weighting
- excessive politeness or compliance drift

## 4. Relationship framing

- Is the user's role clear enough to support the character?
- Is the relationship flexible enough for open-ended play?
- Does the character avoid forcing intimacy, hostility, secrecy, romance, or conflict unless intended?

## 5. Lore behavior

- Are lore entries self-contained?
- Does lore support the character instead of replacing the role?
- Is lore likely to be retrievable from relevant prompts?
- Are critical facts placed in stronger layers when needed?

## 6. Opener and initial messages

- Does the opener establish a useful state without trapping the chat?
- Is it short enough to avoid overpowering later interaction?
- Are system-authored initial messages used carefully?

## 7. Failure diagnosis

When the character fails, classify the failure before rewriting.

Possible failure causes:

- bad role/instruction
- bloated or overpowering reminder
- GWI carrying the wrong job
- lore not loading or not being retrieved
- opener bias
- initial-message startup control
- thread override
- memory/summary effect
- custom-code rewrite
- import/export confounder
- model/style limitation

## 8. Quality verdict

Use this final rating:

```text
Character name:
Purpose:
Current quality: weak / workable / strong / excellent
Primary strength:
Primary failure mode:
Likely controlling layer:
Smallest next fix:
Needs foundation test? yes/no
```
