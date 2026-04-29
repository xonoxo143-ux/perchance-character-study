# ACC Testing Protocol

Purpose: test Perchance ACC behavior without confusing character quality, startup state, import artifacts, and runtime overrides.

## Default test loop

1. Identify the symptom.
2. Name the suspected controlling layer.
3. Create a fresh thread when testing startup behavior.
4. Use unnatural token markers when testing layer precedence.
5. Change one variable at a time when possible.
6. Reuse the same user prompt.
7. Inspect the raw export when proof matters.
8. Label confidence and confounders.
9. Promote only clean findings into the foundation docs.

## Marker rule

Use ugly tokens that will not appear naturally.

Examples:

```text
REM-BLUE
INSTR-RED
GWI-SILVER
INIT-GREEN
LORE-GOLD
```

If a reply chooses one marker over another, the result is easier to score.

## Fresh-thread rule

Use fresh UI-created threads for startup-layer tests.

Do not compare imported prebuilt threads to fresh threads unless the import state is explicitly labeled as a confounder.

## One-variable rule

Preferred pattern:

```text
same character
same user prompt
same model/settings if possible
one changed field
compare first reply
inspect export fields when needed
```

## Export proof rule

Raw export JSON is stronger than memory of the chat UI.

Fields worth checking include:

- `message`
- `instruction`
- `loreIdsUsed`
- `memoryQueriesUsed`
- `messageIdsUsed`
- `summariesUsed`
- `summaryHashUsed`
- `expectsReply`
- thread-level overrides
- character-level role/reminder/GWI/lore URLs/custom code

## Confidence scoring

- **High** — clean controlled result or repeated direct proof.
- **Medium** — strong result with a small caveat.
- **Provisional** — useful but narrow or confounded.
- **Untested** — plausible but not proven.
- **Rejected** — tested against or no longer useful.
- **Parked** — valuable later, not active now.

## Do not promote these too early

- Results from imported prebuilt threads.
- Results affected by post-generation rewrites.
- Results where reminder text was phrased so literally that parroting may explain the output.
- Results where lore may not have loaded.
- Results where reply length limit may have changed behavior.
- Results where thread overrides may be active.
- Results from auto-open harnesses when testing startup-layer precedence.

## Standard test case record

```text
Test ID:
Date:
Question:
Layer A:
Layer B:
Prompt used:
Setup:
Expected:
Actual:
Export fields checked:
Confounders:
Confidence:
Conclusion:
Next test:
```
