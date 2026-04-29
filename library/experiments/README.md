# Experimental Characters

Use this folder for unstable builds, prototypes, test characters, and weird constructions.

Experiments are allowed to be ugly if they teach something.

## Examples

- layer-precedence test characters
- opener-bias tests
- reminder-parroting tests
- lore retrieval tests
- weird role constraints
- custom-code harness characters

## Rule

Experiments should not be mistaken for recommended characters.

Every experiment should state what it is testing.

## Suggested layout

```text
library/experiments/characters/
  experiment-name/
    character.jsonc
    test-notes.md
```

## Test notes template

```text
Experiment:
Question:
Fields being tested:
Setup:
Prompt:
Expected:
Actual:
Confidence:
Promote to foundation? yes/no
Promote to build pattern? yes/no
```
