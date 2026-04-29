# ACC layer behavior notes

This file is about **practical interaction**, not formal theory.
It mixes direct tests with strong observed patterns.
Project-specific notes are labeled.

## Layer shorthand
- **Role / Instruction** = who `{{char}}` is
- **Reminder** = near-reply corrective nudge
- **GWI** = prose / pacing / global style lane
- **URD** = user role / description
- **Opener / Initial messages** = startup seed
- **Scenario** = scene framing
- **Character lore** = lorebook URLs inherited by new threads
- **Thread lore** = `/lore` added directly to a thread

---

## 1. Role / instruction
### What it seems to do
- Main identity lane.
- Stronger than GWI.
- Stronger than system initial in tested fresh-thread head-to-head.
- Can be overridden at the thread level.

### What it is good for
- defining who the character is
- behavioral stance
- hard character constraints
- literal-object constraints when needed

### Risks
- doing too many jobs at once
- carrying prose instructions that belong in GWI
- becoming a prose blob instead of an identity block
- duplication with reminder / opener / lore that creates rigidity

### Failure symptoms
- stiffness
- flattening
- overmanaged scenes
- “good on paper, narrow in play”

---

## 2. Reminder
### What it seems to do
- Strongest tested static layer.
- Beats role, GWI, and system initial in clean head-to-head tests.
- Also beats thread role override in runtime tests.

### What it is good for
- short persistent correction
- keeping one hard rule alive
- drift prevention
- high-priority reply-shaping

### Risks
- overstuffed reminder becomes a second role block
- literal wording can be parroted back instead of followed cleanly
- too many repeated ideas across layers can make the build feel supervised

### Practical rule
- shorter reminder is usually better

### Failure symptoms
- rigidity
- weird self-awareness
- reminder-text parroting
- overcompliance that feels unnatural

---

## 3. GWI
### What it seems to do
- Global prose / style / pacing lane
- weaker than role and reminder in the tested hierarchy
- not an identity layer

### What it is good for
- prose texture
- pacing
- formatting habits
- narrative sheen
- broad output style

### Risks
- can quietly dominate prose while role still looks “correct”
- can be misdiagnosed as a character problem
- can cadence-lock all characters in the same way

### Failure symptoms
- every character feels like the same writer
- too cinematic / too ornate / too polished
- role seems fine but prose is wrong

---

## 4. URD / user role / description
**Project-specific note**

### What it seems to do
In complex system / host work, URD looked like the best place to tune:
- live speaking behavior
- front-facing user identity
- ongoing interaction feel

Lorebook looked better for:
- structure
- hierarchy
- weaknesses
- gating
- support facts

### Risks
- too much user-side structure can become performative or obvious
- lorebook-only user identity can be too weak under host pressure

---

## 5. Scenario / opener / startup seed
### What it seems to do
- Sets early lane and momentum
- Can pre-bias relationship, tone, and expected scene shape
- Can overpower a decent role block if over-authored

### Important direct finding
- visible AI initial message did **not** function like a hard command
- instructive system initial **did**

### Practical meaning
There is a real difference between:
- “visible starter message”
- and “hard instructive startup seed”

### Risks
- opener bias
- relationship bias
- cadence lock from authored first-turn structure
- inherited-feeling scenes
- user puppeting if too many user turns are prewritten

### Failure symptoms
- replies feel precommitted
- character always bends toward one dynamic
- early scene gravity never loosens

---

## 6. Initial messages
### AI-authored initials
- good for visible seed / tone
- not proven to be hard control by themselves

### System-authored initials
- strong startup control when phrased instructively
- still weaker than role and reminder in tested fresh-thread conflicts

### Risks
- stacked initials can feel like a hidden script
- too much authored startup material can lock scene rhythm

---

## 7. Lore
### What it seems to do
- factual support / retrieval lane
- both character lore URL and direct thread lore are real
- both are weaker than role and reminder in tested startup cases
- character lore also lost to system initial in a fresh-thread test
- direct thread lore also lost to system initial in a fresh-thread test

### Character lore vs thread lore
**Character lore**
- inherited by new threads
- needs reload on existing threads after edits
- better for reusable background context

**Thread lore**
- explicit per-thread injection
- good for test control and thread-local facts

### Practical rule
Lore should be written as **self-contained entries**.
Do not assume order will matter.

### Risks
- using lore to do identity work it is too weak to carry
- blaming lore for failures caused by opener / role / host pressure
- forgetting to verify lore actually loaded

### Failure symptoms
- lore “loses” but `loreIdsUsed` is empty
- lore is technically present but never becomes retrievable
- character lore edited, existing thread not reloaded

---

## 8. Thread overrides and runtime layers
### Confirmed
- thread role override > base role
- reminder > thread role override

### Practical meaning
Thread override is a real patch lane.
Useful for per-thread experiments and temporary control.

### Risks
- forgetting you changed the thread layer and then misreading behavior as “base character behavior”

---

## 9. Slash commands and command-lane warnings
### Useful practical split
- normal typing = best natural baseline
- `/ai` = explicit AI-side continuation / instruction
- `/user` = controlled user-side input
- `/nar` = softer narrative steering
- `/sys` = hardest setup lane
- `/lore` = real lore lane when typed / used through the UI

### Important warning
A slash-looking message pushed by custom code into `oc.thread.messages` is **not** automatically a real slash command.

### Proven example
- fake pushed `/lore ...` changed output
- but did **not** create real lore rows
- therefore: visible-context injection, not real command execution

---

## 10. Known ACC risks to watch
### Duplication
Same idea repeated in:
- role
- reminder
- opener
- lore
- relationship framing

can create hidden rigidity.

### Overpowering
A long opener or strong startup scene can overpower the character block.

### Flattening
Too many reinforcements of one trait or dynamic makes the character narrow.

### Cadence lock
Example dialogue and heavy prose guidance can teach a rhythm, not just tone.

### Relationship bias
One relationship repeated everywhere becomes the whole build.

### Opener bias
The first scene / first dynamic becomes “the character” unless reduced.

### Host framing overwrite
**Project-specific**
A strong host can drown out user identity before the first real turn.

### Pronoun / front lock
**Project-specific**
Once a clearly gendered front appears first, narration can lock that in too hard if not guarded.

### Secrecy spectacle
**Project-specific**
Over-restricting inner-state disclosure can cause the model to compensate with cinematic wrongness instead of better fronting.

### Wheel-fighting
**Project-specific**
Too much contest language can make the system a nonstop struggle instead of one front in control with pressure behind it.

---

## 11. Clean working picture
The best-supported startup/static picture from this thread is:

**Reminder > Role > System initial > Lore > GWI**

Use that as a practical starting map, not as an untouchable law.
If a result matters, retest in a fresh thread with marker tokens.
