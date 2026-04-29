# Online Doc Comparison

Purpose: compare public Perchance ACC documentation/community notes against this repo's tested findings.

This file is a comparison layer, not the source of truth. Public docs can explain intended mechanics. Local ACC tests and exports explain observed behavior under conflict.

## Source trust ranking

| Source type | Use | Trust level |
|---|---|---:|
| User-tested ACC exports and snapshots | Observed behavior, precedence, proof fields | Highest for ACC behavior |
| Dev-like documentation / Rentry guides | Intended mechanics and field semantics | High for intended mechanics |
| Public guide mirrors and community guides | Workflow hints and broad descriptions | Medium |
| Lemmy / Reddit community posts | Folk models, edge cases, bug reports, custom-code examples | Low to Medium |
| Public character examples | Pattern study and anti-pattern discovery | Low until tested in ACC |

## Core interpretation rule

```text
Online docs explain what a feature is supposed to do.
Our tests explain what happened when layers conflicted.
```

When they disagree, do not immediately discard either side.

Classify the mismatch as one of:

- intended mechanic versus observed behavior
- normal use versus conflict test
- fresh-thread versus existing-thread state
- documented feature versus untested implementation detail
- community folk model versus export-backed evidence

## What lines up cleanly

| Topic | Online docs say | Repo finding | Verdict |
|---|---|---|---|
| Role / instruction defines character | Role/instruction tells the AI how to speak and behave. | Role carries identity and beat GWI/system initial in tested conflicts. | Aligned. |
| Keep role concise; use lore for lots of info | Docs recommend concise role and lorebooks for larger character/world info. | Build guides warn against role-as-lore-dump and place support facts in lore. | Aligned. |
| Reminder is short, hidden, near-response, powerful | Reminder is placed near the next response and should be much shorter than role. | Reminder tested above role, GWI, system initial, thread role override, and `/ai` in several setups. | Strongly aligned. |
| Long reminders can disrupt behavior | Docs warn long reminders can distract/disrupt the AI. | Repo warns about rigidity, parroting, and reminder-as-role. | Aligned. |
| Role/reminder edits affect existing threads | Docs say instruction/reminder are character-level and update existing threads. | Repo treats these as character-level fields, not one-thread-only state. | Aligned. |
| Initial messages are normal messages and can be summarized | Docs distinguish initial messages from instruction/reminder summarization behavior. | Opener guide treats initial messages as startup context, not permanent identity. | Aligned. |
| Lorebook URLs may need reload in existing threads | Public guide material says existing threads may need lore reload. | Lore guide warns existing threads may need reload and proof checks. | Aligned. |
| Custom-code message hooks exist | Public examples show `oc.thread.on("MessageAdded", ...)`. | Repo treats hooks as real runtime tools but separates harness findings from startup hierarchy. | Aligned. |

## What this repo adds beyond public docs

| Area | Public docs usually cover | Repo adds |
|---|---|---|
| Layer precedence | Field purpose and broad placement. | Tested order: `Reminder > Role / Instruction > System Initial > GWI` in conflict setups. |
| Lore behavior | Lore exists, can be loaded, and supports context. | Lore can retrieve and still lose to stronger layers; `loreIdsUsed` proves engagement, not victory. |
| Initial-message distinction | Initial messages set tone/context. | AI starter and system initial behaved differently in tested setups. |
| Runtime overrides | Commands and custom code exist. | Thread role override beat base role, but reminder beat thread role override. |
| Slash-looking injected messages | Slash commands exist. | Custom-code-pushed slash-looking text can affect output as visible context without proving real command execution. |
| Testing discipline | Tips and examples. | Marker-token tests, proof fields, confounder labels, and promotion rules. |

## Public-doc points to absorb carefully

| Public-doc point | Why useful | Repo action |
|---|---|---|
| Plain role text is equivalent to `[SYSTEM]: ...` role text. | Explains why role behaves as a strong system-authored identity field. | Add to field behavior notes as documented mechanics. |
| Advanced instruction/reminder messages can use `[SYSTEM]`, `[AI]`, `[USER]`. | Useful for advanced formatting and testing. | Add as documented but not fully precedence-tested. |
| Reminder can be authored as `[AI]: (Thought: ...)`. | Docs say this can prevent AI from replying to the reminder as if it were a user/system message. | Keep as open test: does it reduce parroting or change precedence? |
| Token budget / input crowding matters. | Long role, lore, summaries, memories, messages, and reminders may compete. | Add as known confounder. |
| Group/multi-character replies may use main character lore/memory. | Important later for group chats. | Park as future test until group-chat work matters. |

## Public-doc claims that should not be over-promoted yet

### “Everything is one input” folk model

Useful but incomplete.

It is true that role, reminder, GWI, lore, memory, summaries, and messages all contribute to the model context. But tested ACC behavior shows placement still matters under conflict.

Do not collapse all fields into “just prompt text.”

### Reminder authored as internal thought

Public docs recommend `[AI]: (Thought: ...)` reminder style.

Do not assume it is stronger or safer until tested. Current repo position:

```text
Documented mechanic, untested behavior difference.
```

### Public character examples

Public characters are useful for pattern study, but they are not proof of ACC field behavior.

## Open tests created from online comparison

- Plain role text vs explicit `[SYSTEM]` role text.
- Plain reminder vs `[SYSTEM]` reminder.
- Plain reminder vs `[AI]: (Thought: ...)` reminder.
- Whether `[AI]: (Thought: ...)` reduces reminder parroting.
- Token crowding and layer effectiveness.
- Existing-thread lore URL reload behavior.
- Group chat / main-character lore and custom-code behavior.

## Working conclusion

The online docs do not undermine the repo's findings.

They mostly explain intended field mechanics. The repo adds tested behavior, priority order, and diagnosis rules.

Use both, but keep tested ACC evidence above public examples and community folk models when making build rules.
