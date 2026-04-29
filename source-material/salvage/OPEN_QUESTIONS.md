# Open questions

Still worth testing.
Suggested method included for each.

## 1. Advanced reminder forms
### Question
Does reminder wording / authorship / order matter, or is raw reminder placement the main reason it wins?

### Suggested method
Fresh-thread marker bracket:
- plain reminder vs role
- AI-thought reminder vs role
- system-style vs AI-thought
- stacked order reversals

---

## 2. Character lore URL vs GWI
### Question
Does GWI beat character lore when lore actually loads?

### Suggested method
Fresh-thread pack with:
- lore URL only
- lore URL + GWI
- verify `loreIdsUsed`

---

## 3. Direct thread lore vs GWI
### Question
Does GWI beat manual thread lore, or does explicit `/lore` hold up better?

### Suggested method
Fresh thread
- add direct `/lore`
- then compare lore-only vs lore+GWI
- verify `loreIdsUsed`

---

## 4. Summary readiness: imported vs live-grown
### Question
Is the missing piece raw size, or live thread growth?

### Suggested method
Create one imported huge thread and one live-grown huge thread with the same kind of anchors.
Compare:
- `/sum`
- summary editor state
- summary rows
- `summariesUsed`

---

## 5. Memory / summary placement in the layer hierarchy
### Question
Where do summary / memory retrieval sit relative to reminder / role / lore?

### Suggested method
Once summary generation is working:
- load one fact only into summary/memory
- conflict it against one higher layer at a time
- inspect `summariesUsed`, `memoryQueriesUsed`

---

## 6. `/sys`, `/nar`, `/user` practical map
### Question
How different are these lanes in actual behavior contamination / persistence?

### Suggested method
Inject the same fact via:
- normal user message
- `/user`
- `/nar`
- `/sys`
then compare tone, obedience, persistence, and contamination of character voice.

---

## 7. `oc.generateText` return shape
### Question
Is the current live return an object, a string-like value, or something mixed?

### Suggested method
Tiny custom code:
- call `oc.generateText`
- log `typeof`
- log keys
- log raw value safely

---

## 8. Canonical streaming event name
### Question
Which event actually fires in the current live build:
- `MessageStreaming`
- `StreamingMessage`

### Suggested method
Register both.
Log whichever fires.

---

## 9. Character-state proof serialization
### Question
Can share-preserved fields hold test results?

### Suggested method
Sacrificial character:
- mutate `name` or `customData.PUBLIC` after a result
- export
- re-import
- compare with public share link

---

## 10. Host overwrite in complex-user builds
### Question
How much host framing is enough to drown out user identity before first reply?

### Suggested method
Same user build, same lorebook:
- weak host
- moderate host
- aggressive host
rate overwrite, wrongness, pronoun lock, and host-side diagnosis.

---

## 11. Example-dialogue cadence lock threshold
### Question
How much example dialogue is too much?

### Suggested method
Same character, same opener:
- no examples
- two-line examples
- heavy example block
compare tone anchor vs rhythm lock.

---

## 12. Literal-object constraint threshold
### Question
How strong does the role have to be before ACC stops anthropomorphizing an object?

### Suggested method
Three builds:
- weak “is a stapler”
- medium “literal stapler”
- hard “literal stapler, cannot talk”
same opener, same prompts.
