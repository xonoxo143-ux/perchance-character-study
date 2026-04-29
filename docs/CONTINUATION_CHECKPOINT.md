# Continuation Checkpoint

Status: active continuity checkpoint.

Purpose: help future chats and future assistant instances continue the project without redoing the recent reasoning or confusing parked ideas with active work.

This checkpoint is not a simulator plan. It is not an ACC Layer Interpreter spec. It is a project-state and continuation document.

## Current repo mission

Build better Perchance ACC characters through foundation-level understanding.

The repo should help with:

```text
character construction
ACC layer diagnosis
source/evidence handling
character browsing and selection
recovering context after chat loss
```

## Current working terms

Use these terms consistently:

```text
favorites = indexed/selected characters in library/
source    = copied/forked/imported raw character material not selected yet
other     = unclassified or parked material that may be useful later
```

Important distinction:

```text
favorites are not all available characters.
source/other can contain thousands of characters without being favorites.
```

Current favorite count after PR #9:

```text
18 total
1 repo example
17 Perchance built-in starters
```

The large upstream/forked source character base remains source/other until audited and intentionally promoted.

## Recent merged PRs

```text
#3 Role / Reminder / GWI foundation slice
#4 Opener / Initial Messages slice
#5 Lorebook / Lore Retrieval Design slice
#6 Navigation / consolidation pass
#7 Online docs vs tested ACC findings comparison
#8 Parked ACC source/API/batch-testing checkpoint
#9 Favorites/source terminology + Perchance starter indexing
```

## Current repo state

The repo is stable enough to continue from without more restructuring.

Durable areas now exist for:

```text
library favorites
source trust model
assistant workflow
re-anchoring protocol
layer precedence
open tests
role/reminder/GWI guidance
opener/initial-message guidance
lorebook guidance
online-doc comparison
parked ACC source and batch-testing findings
```

## What just happened

The project briefly moved through several adjacent ideas:

1. Browsing the upstream/source character base.
2. Clarifying favorites versus source/other.
3. Indexing Perchance built-in starter characters.
4. Noting the S-3000 Premium Desktop Stapler as a useful weird-ontology character, without deep-diving it further.
5. Considering a future ACC Layer Interpreter idea.
6. Pulling back to preserve continuation state before the chat gets too large.

The important correction was that the user currently wants **continuation support**, not immediate simulator/interpreter work.

## Parked lanes

Do not continue these automatically.

### Batch testing / API / model identity

Parked by PR #8.

Current conclusion:

```text
Exact outside-Perchance ACC batch testing is not proven feasible.
The stored chat model label is `perchance-ai`.
The hidden backend model is unknown.
A surrogate batch generator may be useful later, but is not active now.
```

Do not resume model guessing, source archaeology, or batch-generator implementation unless the user explicitly asks.

### ACC Layer Interpreter idea

Parked idea, not active work.

Rough concept:

```text
Make ChatGPT interpret Perchance ACC fields as layered runtime pressures:
role, reminder, GWI, opener, lore, memory, summaries, user role, and thread state.
```

Useful later for quasi-accurate structural previews, but not exact Perchance cloning.

Do not write a full spec, project instructions, or simulator until the user explicitly resumes this lane.

### Source character browsing/indexing

Active only when the user asks to browse or inspect characters.

Current source-browsing frame:

```text
Start with SFW source characters.
Use manifest-only triage first.
Do not decode full character payloads unless a candidate is promising.
Do not promote source characters into favorites without a reason.
```

## Current useful character-source map

High-level SFW buckets observed from upstream/source manifests:

```text
original human / slice-of-life
fandom/canon characters
fantasy/supernatural beings
AI/tool characters
relationship-frame characters
abstract/weird ontology characters
novelty/custom-code characters
```

Good study targets tend to break the ordinary `person + role + relationship/scenario` pattern:

```text
AI-as-character
object-as-character
abstract concept/entity
game master / narrator
custom-code utility
strong antagonist
heavy fandom/lore character
opener-heavy relationship-lock character
```

## Continuation rules

When resuming the project, start with a re-anchor:

```text
What lane are we in?
What is the user actually asking for?
What is parked?
What should not be restarted?
What is the smallest useful next move?
```

Common lanes:

```text
A. Character browsing / favorites selection
B. Character construction / repair
C. ACC foundation testing
D. Source/evidence audit
E. Batch testing / API/model work
F. ACC Layer Interpreter idea
G. Repo continuity / checkpointing
```

If the user says they want continuation work, do not pivot into simulator/interpreter design.

## PR and repo-history rule

Future PRs should preserve why, not just what.

Each meaningful PR body should include:

```text
What changed
Why it changed
What evidence triggered it
What risk it prevents
What remains unresolved
What not to continue automatically
```

Commit messages can stay short. PR bodies and checkpoint docs carry the reasoning.

## What not to do by default

```text
Do not restart the ACC source audit.
Do not chase the Perchance hidden model identity.
Do not build a batch generator.
Do not write the ACC Layer Interpreter spec yet.
Do not dump all upstream/source characters into favorites.
Do not treat connector search misses as proof of absence when the repo is not indexed.
```

## Best next moves from here

Choose based on the user's next request:

```text
If browsing characters:
  continue SFW manifest-only triage from upstream/source.

If preserving context:
  update this checkpoint or create a narrow checkpoint PR.

If building characters:
  use build-lane guides and keep layer separation explicit.

If resuming Layer Interpreter:
  first create a small seed, not a full simulator.

If resuming batch testing:
  first write a compact spec, not code.
```

## Recovery prompt for future chat

Paste this if the chat is lost:

```text
Use the repo `xonoxo143-ux/perchance-character-study` as the active project context.
Start by reading:
1. README.md
2. docs/CONTINUATION_CHECKPOINT.md
3. docs/ASSISTANT_WORKFLOW.md
4. docs/CHECKPOINT_ACC_SOURCE_AND_BATCH_TESTING.md
5. library/character-index.md

Important terms:
- favorites = indexed/selected characters in library/
- source = copied/forked/imported raw character material not selected yet
- other = unclassified or parked material

Do not assume all source characters are favorites.
Do not restart batch testing, model identity work, ACC source archaeology, or ACC Layer Interpreter design unless I explicitly ask.
If I ask to browse characters, start with SFW source manifests and keep it shallow first.
If I ask for continuation, preserve project state and why-decisions, not new simulator work.
```
