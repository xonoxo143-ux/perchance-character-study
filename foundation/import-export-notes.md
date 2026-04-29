# Import / Export Notes

Purpose: track practical Perchance ACC export-reading rules and import/export pitfalls.

## Current export model

ACC exports are Dexie-style database exports.

Observed outer shape:

```text
formatName
formatVersion
data
```

Observed database payload shape:

```text
data.databaseName
data.databaseVersion
data.tables
data.data
```

Important rule:

> Match table metadata and payloads by `tableName` and inspect `rows` directly. Do not trust superficial table counts.

## Tables observed

- `characters`
- `threads`
- `messages`
- `misc`
- `summaries`
- `memories`
- `lore`
- `textEmbeddingCache`
- `textCompressionCache`

## Character rows

Useful fields:

- `name`
- `roleInstruction`
- `reminderMessage`
- `generalWritingInstructions`
- `initialMessages`
- `loreBookUrls`
- `customCode`
- `autoGenerateMemories`
- `modelName`
- `temperature`
- `maxTokensPerMessage`
- `shortcutButtons`
- `avatar`
- `scene`
- `userCharacter`
- `systemCharacter`
- `customData`
- `uuid`

Interpretation:

- character-level role/reminder/GWI live here
- lorebook URLs live here
- custom code lives here
- memory/summary settings live here

## Thread rows

Useful fields:

- `characterId`
- `userCharacter`
- `systemCharacter`
- `character`
- `customCodeWindow`
- `customData`
- `loreBookId`
- `shortcutButtons`
- `currentSummaryHashChain`

Interpretation:

- thread-level overrides can live here
- shortcut buttons may be snapshotted here
- summary-chain state may exist even when dedicated summary rows are empty

## Message rows

Useful fields:

- `message`
- `instruction`
- `hiddenFrom`
- `expectsReply`
- `variants`
- `loreIdsUsed`
- `summaryHashUsed`
- `summariesUsed`
- `memoryQueriesUsed`
- `messageIdsUsed`
- `customData`
- `wrapperStyle`

Important note:

> Exported message text is currently named `message`, not `content`.

This matters when translating between export rows and live custom-code examples.

## Proof fields

For lore tests:

- check `loreIdsUsed`
- check lore rows
- check character lore URLs
- check whether lore was reloaded into an existing thread

For memory/summary tests:

- check `memoryQueriesUsed`
- check `summariesUsed`
- check `summaryHashUsed`
- check thread-level summary-chain fields

For slash-command-looking behavior:

- a visible exported message beginning with `/...` is not proof that ACC executed a slash command
- custom-code-pushed slash text may act like normal user-visible context

## Import caution

Imported prebuilt threads are not clean startup tests.

They may contain:

- existing message history
- custom data
- thread overrides
- summary-chain state
- snapshotted shortcut buttons
- stale or missing lore state

Use fresh UI-created threads for startup proofs.
