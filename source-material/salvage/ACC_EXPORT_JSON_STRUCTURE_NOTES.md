# ACC export / JSON structure notes

This is a practical appendix, not a guarantee that the schema will never drift.

## Top-level shape
Observed export shape:
- `formatName`
- `formatVersion`
- `data`

Common observed values:
- `formatName = "dexie"`
- `formatVersion = 1`

## `data` shape
Inside `data`:
- `databaseName`
- `databaseVersion`
- `tables`
- `data`

Important:
- `tables` is metadata
- `data` is the parallel list of actual table payloads
- match by `tableName` or position, not by assuming a keyed dict

## Observed tables
- `characters`
- `threads`
- `messages`
- `misc`
- `summaries`
- `memories`
- `lore`
- `textEmbeddingCache`
- `textCompressionCache`

## Character fields that mattered in this project
- `name`
- `roleInstruction`
- `reminderMessage`
- `generalWritingInstructions`
- `initialMessages`
- `fitMessagesInContextMethod`
- `autoGenerateMemories`
- `loreBookUrls`
- `customCode`
- `shortcutButtons`
- `avatar`
- `scene`
- `customData`

## Thread fields that mattered
- `name`
- `characterId`
- `character` (thread-level overrides live here)
- `customData`
- `userMessagesSentHistory`
- `shortcutButtons`
- `currentSummaryHashChain`
- `loreBookId`

## Message fields that mattered
- `message`  ← exported text field
- `characterId`
- `hiddenFrom`
- `expectsReply`
- `instruction`
- `loreIdsUsed`
- `summaryHashUsed`
- `summariesUsed`
- `summariesEndingHere`
- `memoriesEndingHere`
- `memoryIdBatchesUsed`
- `memoryQueriesUsed`
- `messageIdsUsed`
- `wrapperStyle`
- `customData`

## Important practical note
Live docs / custom code talk about message `content`.
Exports use message `message`.

Do not mix those up.

## Proof fields worth checking
For this repo the most useful proof fields were:
- `loreIdsUsed`
- `messageIdsUsed`
- `memoryQueriesUsed`
- `summariesUsed`
- `summaryHashUsed`

## Reading rules
- Trust `rows`, not outer table counts.
- Uploaded raw export JSON is the real chat/thread proof source.
- Public character links are not enough for thread outcomes.
- A slash-looking visible message in export is **not** proof that ACC executed it as a real command.
