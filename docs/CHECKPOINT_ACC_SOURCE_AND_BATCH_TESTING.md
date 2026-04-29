# Checkpoint — ACC Source Audit and Batch Testing

Status: parked.

Purpose: preserve where the project stopped before drifting further into model/API/source-code work.

## Current mission of the repo

Build better Perchance ACC characters through foundation-level understanding.

The repo has two working lanes:

```text
Build Lane      = practical character construction and diagnosis
Foundation Lane = ACC mechanics, evidence, tests, and source interpretation
```

## Why this checkpoint exists

The project temporarily shifted from character-building guides into a possible batch-testing/API investigation.

That investigation is now parked.

Do not continue it automatically unless the user explicitly resumes batch testing, API discovery, or ACC source analysis.

## Latest stable repo state before this checkpoint

Merged PRs before parking:

```text
#3 Role / Reminder / GWI foundation slice
#4 Opener / Initial Messages slice
#5 Lorebook / Lore Retrieval Design slice
#6 Navigation / consolidation pass
#7 Online docs vs tested ACC findings comparison
```

Current useful docs in main include:

```text
README.md
ROADMAP.md
SOURCE_TRUST_MODEL.md
docs/ASSISTANT_WORKFLOW.md
docs/RE_ANCHORING_PROTOCOL.md
docs/ONLINE_DOC_COMPARISON.md
foundation/layer-precedence-map.md
foundation/open-test-matrix.md
foundation/field-behavior-map.md
foundation/known-confounders.md
build-lane/role-reminder-gwi-split-guide.md
build-lane/opener-and-initial-message-guide.md
build-lane/lorebook-design-guide.md
```

## Uploaded files that triggered this checkpoint

The user provided ACC source/runtime evidence files in chat:

```text
AI Character Chat (online, free, no sign-up, unlimited).mhtml.mht
ai-character-chat-modelText.txt
ai-character-chat-outputTemplate.html
perchance-characters-export-2026-04-29.json.gz
```

Generated local audit artifacts in chat, not yet committed to repo:

```text
acc_source_audit_pass1.zip
ACC_SOURCE_AUDIT_REPORT_PASS1.md
ACC_SOURCE_SYMBOL_INDEX_PASS1.md
ACC_BRIDGE_FEASIBILITY_NOTES_PASS1.md
ACC_REPO_PATCH_CANDIDATES_PASS1.md

ACC_SOURCE_AUDIT_PLAN_UPDATED.md
acc_source_audit_plan_updated.zip

acc_source_audit_pass2a.zip
ACC_SOURCE_AUDIT_REPORT_PASS2A.md
ACC_SOURCE_SYMBOL_INDEX_PASS2A.md
ACC_BRIDGE_FEASIBILITY_NOTES_PASS2A.md
ACC_REPO_PATCH_CANDIDATES_PASS2A.md
```

These were created as working notes only. They were not reviewed deeply enough to promote wholesale into repo guidance.

## What was actually found

### Source-confirmed

```text
1. ACC imports and uses aiTextPlugin as the text-generation abstraction.
2. ACC imports textToImagePlugin, uploadPlugin, superFetch, and other Perchance plugins.
3. The stored ACC chat model label is `perchance-ai`.
4. The identifiable embedding model is `Xenova/bge-base-en-v1.5`.
5. The ACC app uses IndexedDB under `chatbot-ui-v1`.
6. The visible app/runtime includes DB stores for characters, threads, messages, lore, memories, summaries, and caches.
7. Character share links use gzipped JSON uploaded through `uploadPlugin` / `user.uploads.dev`.
8. Raw DB export uses CBOR + gzip and identifies as `ai-character-chat-db-raw-export-v1`.
9. The native send-button path eventually calls ACC's reply generation path and stores proof fields like lore/memory/summary usage on message rows.
```

### Source-suggested / interpreted

```text
1. ACC is app/plugin/local-DB based, not a simple public REST API wrapper.
2. The most realistic exact ACC batch path would require running inside Perchance or an equivalent Perchance/plugin context.
3. Raw aiTextPlugin calls are not equivalent to full ACC behavior because full ACC behavior depends on prompt assembly, character/thread state, lore, memory, summaries, initial messages, reminder, and other layers.
4. Outside-Perchance batch testing would likely need a surrogate model and ACC-like prompt assembly.
```

### Not proven

```text
1. A clean external ACC chat REST API.
2. The real backend LLM behind `perchance-ai`.
3. That Perchance uses GPT-4, DeepSeek, Llama, Qwen, Mistral, or any exact backend for ACC chat.
4. That Google/AI-search/community claims about model identity are verified.
5. That running the exact ACC HTML in Colab would reproduce Perchance's hidden plugin/backend behavior.
```

## Model identity conclusion

Current evidence says:

```text
Stored model label: perchance-ai
Embedding model: Xenova/bge-base-en-v1.5
Underlying chat model: unknown
```

Public/AI-search/community content points toward a modular, server-side, possibly rotating/open-weights model situation, with DeepSeek/Llama/Qwen/GPT-like hypotheses. Treat these as candidate families, not facts.

Do not spend more time chasing exact model identity unless new source/network evidence appears.

## Batch testing conclusion

Exact outside-Perchance ACC batch testing is not currently proven feasible.

The likely practical path is a batch generator / surrogate tester:

```text
ACC-like prompt assembly
+ configurable model backend
+ prompt set
+ character variants
+ output scoring
+ small real-ACC validation set
```

This would test character structure, not exact Perchance behavior.

Candidate backend families:

```text
DeepSeek-class
Qwen/Llama/Mistral roleplay-class
GPT-4-class API model
```

## Parked direction

The user chose to park improvements and batch-generator planning for now.

Do not continue with:

```text
- source-code archaeology
- model identity debates
- custom-code bridge work
- exact Perchance clone planning
- batch generator implementation
- repo restructuring
```

unless explicitly resumed.

## If resuming later

Start by asking which lane the user wants:

```text
A. Return to actual character-building/study.
B. Build an external batch generator / surrogate tester.
C. Continue ACC source audit for prompt assembly.
D. Parse ACC exports/share links.
E. Study/import public characters into the library.
```

If the user resumes batch testing, the best next step is not more model guessing. It is a compact spec:

```text
input format
ACC-like prompt assembly
backend adapter interface
output JSONL format
scoring rubric
small Perchance validation set
```

## Recovery prompt for a future assistant

Use this prompt if the chat is lost and another assistant needs to reconstruct the state:

```text
I want to export the useful knowledge from this Perchance ACC character-study thread into a structured repo checkpoint, not a loose summary.

Goal:
Capture every useful insight, tested behavior, failed theory, untested theory, character-structure idea, ACC-source finding, batch-testing idea, and parked direction from this thread so another assistant can continue the work without needing the full chat.

Important context:
The repo is `xonoxo143-ux/perchance-character-study`.
The mission is building better Perchance ACC characters through foundation-level understanding.
The user prefers re-anchoring after major changes, PR-based coherent slices, and no unnecessary structure expansion.
The latest stable repo already contains guides for Role/Reminder/GWI, Opener/Initial Messages, Lorebook Design, an open-test matrix, layer-precedence map, source trust model, and online-doc comparison.

Include these files if creating a zip/checkpoint:

1. README.md
- What this checkpoint is
- What problem we were solving
- How to use the checkpoint

2. ACC_CONFIRMED_FINDINGS.md
- Only things directly tested or strongly verified
- Include test/source condition when possible
- Include symptoms and outcomes

3. ACC_SOURCE_FINDINGS.md
- Findings from ACC MHTML/source/modelText/outputTemplate/export files
- Separate source-confirmed from interpretation
- Include what was already known vs what was new

4. ACC_UNTESTED_THEORIES.md
- Theories discussed but not fully tested
- Mark each confidence: low / medium / high
- Explain what would prove or disprove it

5. ACC_BATCH_TESTING_NOTES.md
- Why we wanted batch testing
- Why external exact ACC testing is not proven
- Candidate paths: external REST API, aiTextPlugin, native ACC path, custom-code harness, surrogate batch generator
- Current conclusion: build surrogate tester if resumed

6. ACC_LAYER_BEHAVIOR_NOTES.md
- Role/instruction, reminder, GWI, opener/initial messages, lore, memory/summaries, thread overrides
- Known risks: duplication, overpowering, flattening, cadence lock, relationship bias, opener bias, token crowding

7. CHARACTER_STRUCTURE_GUIDANCE.md
- Practical build rules from the repo
- How to split role/reminder/GWI/opener/lore
- What belongs where

8. OPEN_TESTS_AND_NEXT_MOVES.md
- Tests still worth running
- Batch-generator next step if resumed
- Character-building next step if resumed

9. REPO_STATE.md
- Recent merged PRs
- Current stable docs
- Parked work
- What not to continue automatically

Rules:
- Do not overstate model identity.
- Do not claim a clean external ACC API exists.
- Do not treat raw aiTextPlugin as equivalent to full ACC behavior.
- Do not turn source-code observations into behavior claims unless tested.
- Preserve uncertainty labels.
- Keep the checkpoint useful for a future assistant, not pretty.
```
