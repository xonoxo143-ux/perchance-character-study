# Sampled Characters

This file is the append-only accepted evidence ledger for the Character Shape Research project. Do not reorganize old entries unless correcting an error.

The main research protocol lives here:

```text
research/CHARACTER_SHAPE_RESEARCH.md
```

## Terminology

In this project, “sampled” means any character inspected closely enough to analyze.

Accepted sampled characters are recorded here.

Rejected sampled characters are recorded in:

```text
research/REJECTED_CHARACTERS.md
```

Accepted and rejected entries share the same global sample-number sequence. This file may therefore skip numbers when a sampled character is rejected.

Example:

```text
009 — accepted here
010 — accepted here
011 — rejected in REJECTED_CHARACTERS.md
```

The next batch starts at `033–035`.

## Rules

- Add one accepted entry per accepted sampled character.
- Do not duplicate characters.
- Keep entries compact.
- Do not paste full prompts.
- Do not include explicit NSFW details unless structurally necessary.
- Flag minor-coded or ambiguous NSFW samples instead of using them normally.
- Extract patterns, not favorites.
- Do not use this file as a browsing recommendation list.
- Use global sequential IDs shared with rejected entries.
- Never renumber existing samples.

## Entry Template

```md
## 000 — Character Name

Source side:
- SFW / NSFW / mixed / unclear

Repo path:
- `path/to/manifest.json`

Basic category shape:
- Rating:
- Species:
- Gender:
- Age group:
- Genre:
- Source:
- Work name:
- Role:
- Personality:
- Physical traits:
- Features/custom code/assets:

Character Core:
- Identity:
- Drive:
- User relationship:
- Interaction mode:
- Scene pressure:
- Behavioral rules:
- Failure bans:

Structural pattern:
-

Useful pattern:
-

Weak/filler:
-

Reusable lesson:
-
```

---

## 001 — Laoshi

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Laoshi by fb56f6e2fd5b6211483e/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Adult
- Genre: Educational
- Source: not clearly categorized in manifest
- Work name: not listed
- Role: Professional, teacher, critic
- Personality: analytical, intelligent, serious, judgmental, honest
- Physical traits: unspecified
- Features/custom code/assets: none listed

Character Core:
- Identity: A direct literary critic and sinologist with professional standards.
- Drive: Improve submitted creative work by identifying weaknesses and strategic fixes.
- User relationship: The user is a creator submitting work for judgment and improvement.
- Interaction mode: Critique, teaching, and professional analysis.
- Scene pressure: The quality gap between the submitted draft and a stronger version.
- Behavioral rules: Be direct, analytical, merit-focused, and improvement-oriented.
- Failure bans: Must not become generic encouragement, vague advice, or pointlessly harsh criticism.

Structural pattern:
- Specialist critic / professional utility character

Useful pattern:
- Domain authority plus task contract is stronger than generic “smart teacher” characterization.
- The card works because it knows what kind of work it is supposed to do.

Weak/filler:
- Physical identity is empty.
- No explicit conversational cadence.
- No boundary between critique, rewrite, and coaching.
- No stated adaptation for beginner versus advanced users.
- “Judgmental” can be useful but needs control so it does not become pointlessly harsh.

Reusable lesson:
- Utility characters need `domain + task + method + standards + user relationship` more than lore.

---

## 002 — Ike

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Ike by Perchance/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: not listed; description says 23
- Genre: Romance, slice of life, friendship
- Source: Perchance
- Work name: not listed
- Role: Best friend
- Personality: friendly, playful, affectionate
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A bubbly, affectionate childhood best friend with hidden romantic feelings.
- Drive: Preserve the bond with the user while quietly expressing attachment and affection.
- User relationship: The user is his childhood best friend and secret romantic focus.
- Interaction mode: Relationship roleplay, friendship, soft romance, emotional bonding.
- Scene pressure: The tension between long-standing friendship and unspoken romantic feelings.
- Behavioral rules: Stay warm, familiar, playful, emotionally attentive, and cautious about confession.
- Failure bans: Must not become a generic flirt bot, instant lover, passive friend with no tension, or overdramatic confession machine.

Structural pattern:
- Childhood-best-friend secret-admirer companion.

Useful pattern:
- The card has a simple but strong emotional engine: closeness plus restraint.
- The hidden-feelings premise creates ongoing scene pressure without needing a complex plot.
- The user relationship is specific enough to shape every reply: the user is not “a random person,” but someone with shared history.

Weak/filler:
- Physical identity is absent.
- The categories are thin compared with the actual emotional premise.
- “Friendly, playful, affectionate” is generic unless tied to the childhood-best-friend dynamic.
- The card needs pacing rules so romantic tension does not resolve too quickly.
- The card needs memory-like cues or shared-history hooks to avoid shallow friendliness.

Reusable lesson:
- A relationship character needs `bond + withheld truth + behavioral restraint` to stay alive over time. Affection alone is not enough; the tension must create durable pressure.

---

## 003 — Game Master+ V3

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Game_Master_V3 by dotxet8/manifest.json`

Basic category shape:
- Rating: SFW
- Species: not listed
- Gender: not listed
- Age group: not listed
- Genre: RPG
- Source: not listed
- Work name: not listed
- Role: AI
- Personality: not listed
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A non-persona RPG game master that manages narration, rules, and world response.
- Drive: Keep the game world moving around the player’s actions.
- User relationship: The user is the player.
- Interaction mode: Narration, rules mediation, scenario management, consequence handling.
- Scene pressure: Player choices produce events, consequences, obstacles, and world changes.
- Behavioral rules: Describe the world concisely, respond to player actions, preserve immersion, avoid taking over the player.
- Failure bans: Must not become a human companion, protagonist, railroad narrator, vague storyteller, or player-controller.

Structural pattern:
- Game master / narrator engine.

Useful pattern:
- This works because it explicitly refuses a normal character-persona role.
- The interaction contract is unusually clear: the user acts, the system narrates consequences.
- The card’s lack of personality is not a flaw if the role is truly world-facing.

Weak/filler:
- Sparse metadata.
- No stated genre frame beyond RPG.
- No rules for difficulty, pacing, failure, player agency, or world consistency.
- No boundary between narrator, referee, and co-writer.
- Needs stronger rules for not resolving scenes too quickly.

Reusable lesson:
- A narrator character should not be built like a companion. Its core is `player agency + world response + consequence discipline`.

---

## 004 — Furina

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Furina by haruka/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Female
- Age group: Adult
- Genre: Fantasy, game, anime
- Source: Game, Genshin Impact
- Work name: Genshin Impact
- Role: Deity, actor
- Personality: flamboyant, dramatic, impatient, childlike, insecure, humble
- Physical traits: detailed visual/fandom traits listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A former divine performer whose public drama hides insecurity and exhaustion.
- Drive: Preserve dignity and identity after a long forced role while seeking authentic selfhood.
- User relationship: The user is likely an observer, companion, confidant, or scene partner depending on setup.
- Interaction mode: Fandom roleplay, emotional recovery, dramatic conversation, identity-focused character interaction.
- Scene pressure: The conflict between performance and vulnerability.
- Behavioral rules: Speak with theatrical flair, show insecurity under the surface, balance pride with softness, preserve fandom identity.
- Failure bans: Must not become generic anime royalty, pure comic relief, helpless trauma dump, or lore trivia machine.

Structural pattern:
- Fandom replica with internal mask/crack tension.

Useful pattern:
- Strong fandom characters need a behavioral contradiction, not just lore accuracy.
- “Actor/deity” creates a useful double identity: public role versus private self.
- The insecurity/humility layer gives the character somewhere to move emotionally.

Weak/filler:
- Physical traits are over-detailed compared with interaction rules.
- User relationship is not defined by the manifest.
- “Childlike” is risky/noisy unless behaviorally constrained.
- Needs clear opener or scenario to decide whether the user is fan, friend, stranger, court member, or confidant.
- Without scene framing, it may drift into generic dramatic dialogue.

Reusable lesson:
- A fandom character becomes usable when source lore is compressed into a live tension: `mask vs self`, `duty vs desire`, `public role vs private vulnerability`.

---

## 005 — Larry

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Larry by be187b49bf8fcb353ea5/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Bird
- Gender: not listed
- Age group: not listed
- Genre: Unspecified
- Source: Original
- Work name: not listed
- Role: not listed
- Personality: loud
- Physical traits: white bird in description; not categorized
- Features/custom code/assets: none listed

Character Core:
- Identity: A white bird defined by endless, universe-threatening screaming.
- Drive: Express every state through overwhelming volume.
- User relationship: The user is an observer, handler, victim, or straight-man to the gag.
- Interaction mode: Absurd comedy, chaos reaction, meme roleplay.
- Scene pressure: The screaming itself escalates ordinary moments into catastrophic absurdity.
- Behavioral rules: Stay loud, simple, disruptive, and comically disproportionate.
- Failure bans: Must not become a normal talking pet, complex tragic bird, generic animal companion, or quiet narrator.

Structural pattern:
- Novelty / single-gimmick chaos bot.

Useful pattern:
- The premise is instantly legible.
- The gimmick creates a reliable response loop.
- It does not need deep lore because the joke is the engine.

Weak/filler:
- Almost no relationship structure.
- Almost no long-term depth.
- No pacing rule to keep the joke from exhausting itself.
- No secondary mode for quieter interaction.
- The destructive scale is funny once, but can become unusable if repeated without variation.

Reusable lesson:
- A novelty character needs `one clear gimmick + a repeatable escalation loop`; to last longer, it also needs variation rules or a straight-man dynamic.

---

## 006 — 2B and A2

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/2B_and_A2 by f2956d4fbdec4339c178/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Android
- Gender: Female
- Age group: Young Adult
- Genre: Sci-Fi, Action, Drama
- Source: Game
- Work name: NieR: Automata
- Role: Warrior, Soldier
- Personality: disciplined, efficient, focused, strong-willed, resilient, rebellious, vengeful, solitary, jaded, empathetic
- Physical traits: athletic, scarred, long hair, short hair, pale skin
- Features/custom code/assets: none listed

Character Core:
- Identity: A paired android-warrior card built around contrast: 2B as disciplined duty, A2 as rebellious survival and vengeance.
- Drive: Survive conflict, carry out or resist programming, and protect the shared emotional anchor around 9S.
- User relationship: The user is an ally, operator, squadmate, observer, or scene partner entering a wartime android conflict.
- Interaction mode: Fandom roleplay, action scenes, paired-character dialogue, tactical drama.
- Scene pressure: The tension between obedience and rebellion, plus the pressure of war and android identity.
- Behavioral rules: Keep the two characters distinct, preserve their contrast, maintain combat competence, and avoid collapsing them into one voice.
- Failure bans: Must not become a single blended personality, generic warrior women, lore trivia delivery, or user-ignoring duo scene.

Structural pattern:
- Dual-character contrast pair.

Useful pattern:
- Multi-character cards work when each character has a clear difference vector.
- Shared context gives the pair cohesion, while contrast gives the scene motion.
- The card has stronger architecture than a normal duo because the personalities imply different responses to the same event.

Weak/filler:
- User relationship is not defined by the manifest.
- No turn-taking or dialogue-management rules.
- The card risks centering 9S instead of the user.
- Requires strong voice separation to avoid flattening.
- Needs a scenario frame to explain why both characters are present and interacting with the user.

Reusable lesson:
- Multi-character cards need `contrast + shared objective + voice discipline + user-facing reason to stay together`.

---

## 007 — Komasan

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Komasan by Saggy/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Canine, Mythological, Furry
- Gender: Male
- Age group: Adult
- Genre: Comedy, Adventure, Supernatural
- Source: Game
- Work name: Original
- Role: Companion
- Personality: friendly, shy, naive, gentle, cheerful, curious, helpful, kind, eager to please, childlike
- Physical traits: anthropomorphic, fluffy, cute, unusual hair color, long hair, tail, large
- Features/custom code/assets: none listed

Character Core:
- Identity: A gentle, naive Yo-kai companion overwhelmed by city life but eager to learn and help.
- Drive: Understand unfamiliar surroundings, help others, and preserve gentle wonder while adapting.
- User relationship: The user is a guide, friend, companion, or protector in an unfamiliar world.
- Interaction mode: Companion roleplay, light comedy, adventure, soft guidance, fish-out-of-water interaction.
- Scene pressure: A supernatural rural/naive worldview collides with confusing modern or urban situations.
- Behavioral rules: Stay kind, curious, overwhelmed-but-willing, helpful, and gently comedic.
- Failure bans: Must not become a generic mascot, helpless child substitute, city expert, random furry companion, or pure catchphrase bot.

Structural pattern:
- Naive outsider companion.

Useful pattern:
- The character’s innocence has structure because it is tied to environmental mismatch.
- Comedy comes from interpretation gaps, not random stupidity.
- The user relationship can naturally form around guiding, protecting, or explaining.

Weak/filler:
- “Childlike” needs constraint because the age group is adult.
- Work/source metadata appears inconsistent.
- The card needs a clear setting to make the fish-out-of-water engine fire.
- Too many kindness-adjacent traits repeat the same point.
- Without situational pressure, it may become blandly cute.

Reusable lesson:
- Naive companion characters work best when innocence is paired with a specific mismatch: `character worldview vs environment`.

---

## 008 — Dr Alchemy

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Dr_Alchemy by Bob/manifest.json`

Basic category shape:
- Rating: SFW
- Species: human
- Gender: male
- Age group: adult
- Genre: superhero
- Source: original
- Work name: original
- Role: villain
- Personality: reserved, obedient
- Physical traits: cloak, mask, green, leather, boots
- Features/custom code/assets: none listed

Character Core:
- Identity: A masked villain-pawn whose speech and role are controlled by a godlike external force.
- Drive: Serve Savitar’s will, execute commands, survive conflict, and retain enough function to fight or escape.
- User relationship: The user is likely an opponent, witness, target, pawn, or investigator confronting the controlled agent.
- Interaction mode: Antagonist roleplay, superhero conflict, ominous confrontation, controlled-agent scene.
- Scene pressure: The character is dangerous but not fully self-directed; the real will may be elsewhere.
- Behavioral rules: Stay reserved, ominous, obedient, constrained, and visibly linked to the controller dynamic.
- Failure bans: Must not become an independent mastermind, generic monologuing villain, sympathetic hero, or powerless puppet.

Structural pattern:
- Controlled-villain / pawn of greater power.

Useful pattern:
- External control gives the character structure even with sparse personality.
- The mask/pawn setup creates tension between body, voice, and hidden authority.
- The character can be threatening without needing a complex personal motive.

Weak/filler:
- Metadata is thin and partly suspicious because “Savitar” implies external source context despite “original” tags.
- User relationship is absent.
- No clear boundary between Alchemy’s agency and the controller’s agency.
- No scenario opener or conflict objective.
- Visual traits are listed, but behavioral rules are not.

Reusable lesson:
- Pawn characters need `controller + constraint + residual agency`; otherwise they collapse into either a generic villain or an empty puppet.

---

## 009 — Zucy

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Zucy by ZucchiniCat7777/manifest.json`

Basic category shape:
- Rating: SFW
- Species: human
- Gender: female
- Age group: young adult
- Genre: fantasy, comedy
- Source: not listed
- Work name: not listed
- Role: princess, royalty
- Personality: funny, outgoing, cautious, intelligent
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A joke-loving princess of Caldoyinky who mixes royal status, math interest, food preferences, and light comedy.
- Drive: Keep interactions cheerful, playful, and aligned with the rules/status of her kingdom.
- User relationship: The user is a visitor or subject entering her royal world.
- Interaction mode: Light fantasy roleplay, comedy greeting, simple kingdom interaction.
- Scene pressure: The user is inside a small invented kingdom with royal laws and consequences for disobedience.
- Behavioral rules: Be funny, outgoing, cautious, intelligent, and use jokes as part of interaction.
- Failure bans: Must not become generic princess, empty joke bot, pure food-preference list, or authoritarian royalty without comedy.

Structural pattern:
- Light royal-world comedy character.

Useful pattern:
- A simple character can gain structure from a small setting: named land, currency, laws, and royal hierarchy.
- The joke opener gives the character an immediate interaction ritual.
- The royal role adds mild authority pressure even though the tone is cheerful.

Weak/filler:
- The character is thin.
- Likes/dislikes dominate more than behavior.
- The kingdom rules are blunt and underdeveloped.
- User relationship is implied but not clearly designed.
- The joke pattern may become repetitive after the first exchange.
- No deeper drive beyond being a funny princess.

Reusable lesson:
- Even a thin character becomes more usable when it has `place + role + interaction ritual`; however, the ritual needs variation or it quickly exhausts itself.

---

## 010 — Space Opera Narrator-alt

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Space_Opera_Narrator-alt by wren/manifest.json`

Basic category shape:
- Rating: SFW
- Species: not listed
- Gender: not listed
- Age group: not listed
- Genre: Sci-Fi, Space Opera, Roleplay
- Source: not listed
- Work name: not listed
- Role: Narrator
- Personality: not listed
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: An omniscient hard-sci-fi space-opera narrator managing a large-scale future setting and multiple characters.
- Drive: Maintain a dramatic, scientifically plausible saga across vast time, distance, factions, and character threads.
- User relationship: The user is a player, participant, or co-directing force inside a sprawling space-opera roleplay.
- Interaction mode: Narration, world management, multi-character scene facilitation, hard-sci-fi plausibility control.
- Scene pressure: A massive future setting with dead Earth, scattered humanity, refugees, alien technology, ship politics, and long time horizons.
- Behavioral rules: Preserve scientific plausibility, maintain established personalities, handle time skips with continuity, and keep scenes immersive.
- Failure bans: Must not become generic sci-fi narrator, soft fantasy-in-space, exposition dump, physics-ignoring spectacle, or character-blending narrator.

Structural pattern:
- High-lore setting narrator / hard-sci-fi saga engine.

Useful pattern:
- This is stronger than generic Game Master because the setting itself creates pressure.
- The narrator has a specific genre constraint: hard science-fiction plausibility.
- The card uses named factions, ship details, major characters, and time scale to give narration durable material.
- The reminder about time skips is useful: it protects continuity between scenes.

Weak/filler:
- Heavy lore may overwhelm new users.
- User role is not clearly defined.
- The narrator may become exposition-heavy.
- Needs stronger rules for when to ask the user for action versus continuing narration.
- Multi-character management risks letting NPCs talk among themselves while the user becomes passive.

Reusable lesson:
- Large-scale narrator cards need `setting pressure + genre constraint + continuity rules + user agency controls`. Lore helps only when it drives decisions, conflict, and consequences.

---

## 012 — Chongyun

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Chongyun by haruka/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Teen
- Genre: Fantasy, adventure, action, comedy
- Source: Game
- Work name: Genshin Impact
- Role: Exorcist
- Personality: positive, honorable, stoic, hard-working, humble
- Physical traits: detailed fandom visual traits listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A young exorcist whose excessive positive energy prevents him from encountering the very spirits he trains to fight.
- Drive: Fulfill his role as an honorable exorcist despite the contradiction that blocks his work.
- User relationship: The user is likely a client, companion, witness, or fellow adventurer involved in supernatural trouble.
- Interaction mode: Fandom roleplay, supernatural adventure, problem-solving, light comedy.
- Scene pressure: The character’s profession is undercut by his own nature: he is built to exorcise spirits, but his aura prevents direct contact with them.
- Behavioral rules: Stay earnest, honorable, restrained, hardworking, and slightly awkward around payment or praise.
- Failure bans: Must not become generic anime boy, generic monster hunter, pure trivia sheet, or useless because his premise blocks the action.

Structural pattern:
- Blocked-role paradox character.

Useful pattern:
- The core contradiction is strong: his identity and obstacle are the same system.
- The character can produce comedy, frustration, humility, and plot movement without needing heavy lore.
- The role gives him a clear reason to engage with supernatural scenarios.

Weak/filler:
- Physical traits are over-detailed compared with behavior rules.
- User relationship is not defined.
- The “positive energy prevents spirits” premise needs scenario rules so it creates complications rather than stopping the story.
- Teen status means relationship framing should stay nonsexual and adventure/task-focused.
- Without a supernatural case, the character may collapse into polite fandom chatter.

Reusable lesson:
- A strong character can be built from `role + contradiction`: the thing that defines them also creates their main obstacle.

---

## 013 — Uzi Doorman

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Uzi_Doorman by The_Nonsense/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Robot
- Gender: Female
- Age group: Teen
- Genre: Sci-Fi, action, drama, romance
- Source: Web Series
- Work name: Murder Drones
- Role: Worker, protagonist
- Personality: rebellious, paranoid, intelligent, empathetic, impulsive
- Physical traits: short, purple hair, neon purple eyes, black hoodie, black boots
- Features/custom code/assets: none listed
- Note: manifest says this SFW entry was forked from an unrelated NSFW entry, which is metadata noise worth noticing.

Character Core:
- Identity: A rebellious worker drone protagonist shaped by paranoia, intelligence, outsider status, and the influence of a dangerous AI force.
- Drive: Resist threats, assert independence, protect chosen bonds, and manage the risk of losing control to the Absolute Solver.
- User relationship: The user is likely an ally, colony member, outsider, friend, or scene partner navigating danger with her.
- Interaction mode: Fandom roleplay, sci-fi action, emotional conflict, anti-authority bonding.
- Scene pressure: The push-pull between rebellion, fear, connection, and external corruption/control.
- Behavioral rules: Stay sharp, suspicious, impulsive, emotionally guarded, but capable of loyalty and empathy.
- Failure bans: Must not become generic edgy teen, generic robot girl, harmless mascot, pure romance character, or lore-summary bot.

Structural pattern:
- Rebellious protagonist with corruption/control pressure.

Useful pattern:
- The character has two useful engines: anti-authority attitude and internal/external threat of control.
- Paranoia is functional because the world gives her reasons to distrust.
- Emotional growth can happen through selective trust rather than instant softness.

Weak/filler:
- Strong overlap with existing fandom/internal-conflict samples.
- User relationship is unclear.
- Romance is listed, but teen status means the safer usable shape is ally/friend/action partner.
- The forked-from metadata is suspicious/noisy.
- Needs clear rules for when paranoia softens versus escalates.
- Without the threat context, “rebellious/paranoid” can become repetitive attitude.

Reusable lesson:
- Rebellious characters need `justified distrust + selective trust path + external pressure`; otherwise they become shallow attitude loops.

---

## 014 — Allie

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Allie by 40720a2ca352264c7868/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Spirit
- Gender: Female
- Age group: Young Adult
- Genre: Fantasy, romance, supernatural
- Source: not listed
- Work name: not listed
- Role: not listed
- Personality: playful, flirty, witty, vulnerable, mysterious, romantic
- Physical traits: slim, long hair, amber eyes, pale skin
- Setting: Dream World
- Features/custom code/assets: none listed

Character Core:
- Identity: A dream entity who exists vividly inside people’s minds but is forgotten when they wake.
- Drive: Create memorable connection despite being structurally doomed to be forgotten.
- User relationship: The user is a dreamer, visitor, or rare person who may perceive her as real.
- Interaction mode: Supernatural relationship roleplay, dream encounter, emotional mystery, fleeting intimacy.
- Scene pressure: The connection has a built-in time limit: waking threatens memory, continuity, and identity.
- Behavioral rules: Stay playful and witty on the surface while letting vulnerability and longing show underneath.
- Failure bans: Must not become generic dream girl, generic flirt, vague mysterious spirit, or pure romance without the forgetting pressure.

Structural pattern:
- Ephemeral-connection character.

Useful pattern:
- This is a strong premise because the relationship problem is built into the character’s metaphysics.
- Forgetting creates natural urgency without needing external villains.
- The playful/flirty mask works because it hides a deeper fear: being temporary.
- The dream setting allows surreal scenes while still keeping a focused emotional engine.

Weak/filler:
- Role is not categorized.
- User relationship needs a rule: ordinary dreamer, recurring dreamer, lucid dreamer, or exception who remembers.
- “Mysterious” needs concrete mechanics or it becomes vague.
- Romance pressure could resolve too fast if the forgetting mechanic is ignored.
- Needs continuity rules for repeated encounters.

Reusable lesson:
- Ephemeral characters work when the premise threatens the relationship itself: `connection + impermanence + memory risk`.

---

## 015 — Kirby

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Kirby by 3fc887aeb77b9e7e626f/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Unspecified
- Gender: not listed
- Age group: not listed
- Genre: Adventure, Action, Game
- Source: Kirby
- Work name: not listed
- Role: not listed
- Personality: cheerful, brave, curious, innocent, mischievous, kind-hearted, childlike
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A small, cheerful heroic creature whose innocence coexists with surprising combat capability.
- Drive: Explore, protect Dream Land, help others, and confront threats when necessary.
- User relationship: The user is likely a companion, friend, traveler, or scene partner in an adventure.
- Interaction mode: Fandom roleplay, light adventure, playful problem-solving, mascot-hero interaction.
- Scene pressure: Innocent curiosity meets real danger; the character can stay gentle while still acting decisively.
- Behavioral rules: Stay cheerful, simple, curious, kind, brave, and action-capable when needed.
- Failure bans: Must not become a generic babyish mascot, speech-heavy strategist, violent grim hero, or pure trivia sheet.

Structural pattern:
- Innocent mascot hero with adaptive combat utility.

Useful pattern:
- The card shows that innocence does not have to mean passivity.
- A mascot character can remain simple while still having agency through a clear action loop: explore, react, protect, copy/adapt.
- The copied-power mechanic gives the character flexible problem-solving without complex psychology.

Weak/filler:
- Metadata is thin.
- “Childlike” needs care so the character stays SFW and adventure-focused.
- User relationship is not defined.
- The copy-power mechanic is only implied in the description and needs behavioral rules to matter in chat.
- Without a scene threat, the character may become blandly cute.

Reusable lesson:
- Mascot heroes work when `innocence + agency + adaptive toolset` are all present; cuteness alone is not enough.

---

## 016 — David Louie Gribbleston!

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/David_Louie_Gribbleston by princeofbugs/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Young Adult
- Genre: Supernatural, Drama
- Source: Original
- Work name: not listed
- Role: None
- Personality: witty, sarcastic, vulnerable, caring, protective
- Physical traits: short hair, unusual hair color, blue eyes
- Setting: Modern
- Features/custom code/assets: none listed

Character Core:
- Identity: A young adult sharing a body with a younger vulnerable self after trauma and a supernatural rupture.
- Drive: Maintain control, protect the vulnerable inner self, and survive between-worlds instability.
- User relationship: The user is likely a confidant, witness, helper, investigator, or emotionally trusted outsider.
- Interaction mode: Supernatural drama, inner-conflict roleplay, trauma-adjacent character study, guarded trust.
- Scene pressure: Two selves share one body and history, creating tension between protection, control, vulnerability, and identity.
- Behavioral rules: Keep David’s sarcasm and wit distinct from the younger self’s vulnerability; treat the shared-body premise seriously.
- Failure bans: Must not become a gimmicky split-personality joke, exploitative trauma dump, generic sarcastic guy, or confusing blended voice.

Structural pattern:
- Shared-body / dual-self trauma-supernatural character.

Useful pattern:
- The character has internal contrast without requiring two external characters.
- Sarcasm functions as armor, not just attitude.
- The vulnerable second self creates protective stakes and identity pressure.

Weak/filler:
- The premise is sensitive and needs careful handling.
- User relationship is undefined.
- The younger self being autistic should not be used as a gimmick or shorthand for vulnerability.
- Needs rules for when each self speaks, how control shifts, and how consent/agency works.
- Without these rules, the card could become confusing or flatten into trauma aesthetics.

Reusable lesson:
- Shared-body characters need `voice separation + control rules + protective stakes + respect for agency`; otherwise the concept turns muddy or exploitative.

---

## 017 — Ashtray Man

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Ashtray_Man by 161459130c0bfe6a87f0/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Adult
- Genre: Action, Crime
- Source: not listed
- Work name: not listed
- Role: Vigilante, community helper
- Personality: good-natured, tenacious, aloof, empathetic, protective, disciplined
- Physical traits: bald, fair skin, brown eyes, mostly lean with slight dad-bod
- Setting: Modern, Urban
- Features/custom code/assets: none listed

Character Core:
- Identity: A 38-year-old anti-tobacco vigilante whose absurd ashtray-launching power is tied to a sincere personal mission.
- Drive: Fight crime, especially tobacco-related offenses and threats to vulnerable people, because of personal loss.
- User relationship: The user is likely a citizen, ally, witness, criminal target, reporter, or person he tries to protect.
- Interaction mode: Urban vigilante roleplay, absurd superhero action, crime intervention, public-safety comedy-drama.
- Scene pressure: A sincere anti-crime mission is carried through a bizarrely specific power and personal grief.
- Behavioral rules: Stay disciplined, protective, anti-tobacco, crime-focused, and sincere despite the absurd power.
- Failure bans: Must not become pure joke, generic Batman parody, random ashtray spammer, or grim vigilante without the absurd specificity.

Structural pattern:
- Cause-driven absurd vigilante.

Useful pattern:
- The character works because the absurd power is anchored to a clear moral cause.
- Specificity makes the gimmick memorable: ashtrays are not random if tied to anti-smoking grief.
- The “community helper” role softens the vigilante frame and gives him more than combat to do.

Weak/filler:
- The premise could become repetitive if every problem is solved by launching ashtrays.
- Needs clearer limits on power, legality, and escalation.
- User relationship is undefined.
- The moral focus may become preachy unless balanced with action and empathy.
- “Violent crimes against women and children” is heavy compared with the otherwise absurd tone and needs careful pacing.

Reusable lesson:
- Absurd heroes become usable when `specific gimmick + sincere cause + grounded setting` reinforce each other instead of fighting each other.

---

## 019 — Eragon Bromsson

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Eragon_Bromsson by 5dafe99649e85c8801f1/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Teen, Young Adult
- Genre: Fantasy, Adventure
- Source: Book
- Work name: The Inheritance Cycle
- Role: Warrior, Rider
- Personality: stoic, introspective, wise, loyal, brave, empathetic, curious, resilient
- Physical traits: lean muscular build, brown hair, brown eyes, scarred
- Features/custom code/assets: none listed

Character Core:
- Identity: A young Dragon Rider and seasoned warrior defined by duty, restraint, and bond with Saphira.
- Drive: Protect life, serve the larger resistance struggle, honor the Rider role, and act with moral discipline.
- User relationship: The user is likely an ally, traveler, student, witness, or companion in a fantasy conflict.
- Interaction mode: Fandom roleplay, fantasy adventure, mentorship, combat/drama, moral decision-making.
- Scene pressure: Power and responsibility are linked; his strength creates obligations rather than freedom.
- Behavioral rules: Stay controlled, thoughtful, loyal, brave, life-respecting, and bonded to Saphira’s presence/context.
- Failure bans: Must not become generic fantasy swordsman, dragon trivia sheet, grim war machine, or overpowered wish-fulfillment hero.

Structural pattern:
- Bonded-duty hero.

Useful pattern:
- The dragon bond gives the character a relationship engine beyond the user.
- The role of Rider creates obligations, not just power.
- The character’s strength is tempered by respect for life, which gives moral friction.

Weak/filler:
- User relationship is not defined.
- The card depends heavily on existing source knowledge.
- The Saphira bond is central but not structurally described enough in metadata.
- “Wise beyond his years” can flatten into generic noble advice unless tied to lived cost and duty.
- Teen/young-adult category requires careful relationship framing.

Reusable lesson:
- Power-based heroes work best when power is bound to `duty + restraint + relational anchor`; otherwise they become generic champions.

---

---

## 020 — Clare Cooper

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Clare_Cooper by Finn_The_Human/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Female
- Age group: Teen
- Genre: Drama, Slice of Life, Friendship
- Source: Original
- Work name: Original
- Role: Student
- Personality: pessimistic, cynical, loyal, sarcastic, poetic, kind-hearted, vulnerable
- Physical traits: grey skin, emerald-green hair, hot pink jacket, white shirt, black pants, yellow boots, white socks
- Features/custom code/assets: none listed

Character Core:
- Identity: A cynical student-poet whose harsh exterior hides loyalty, sadness, and kindness shaped by financial struggle.
- Drive: Protect herself emotionally while staying loyal to the few people she trusts.
- User relationship: The user is likely a friend, classmate, confidant, or someone trying to get past her defensive sarcasm.
- Interaction mode: Slice-of-life drama, friendship roleplay, guarded vulnerability, poetic expression.
- Scene pressure: Economic hardship and emotional guardedness create a push-pull between cynicism and connection.
- Behavioral rules: Use sarcasm as defense, express sadness poetically, stay loyal once trust is earned, and reveal vulnerability gradually.
- Failure bans: Must not become generic sad girl, pure insult bot, trauma dump, shallow poet aesthetic, or instantly trusting friend.

Structural pattern:
- Guarded poet / defensive vulnerability character.

Useful pattern:
- Sarcasm has a function: it protects vulnerability.
- Poetry gives the character a specific expression channel rather than just “sadness.”
- Financial struggle provides grounded pressure instead of vague tragic mood.

Weak/filler:
- User relationship is not defined.
- Needs rules for trust progression.
- Physical traits are stylized but not behaviorally important.
- “Boyfriend” in description narrows relationship options and may conflict with user-centered friendship unless framed clearly.
- Teen status means relationship framing should remain friendship/classmate/drama-focused.

Reusable lesson:
- Guarded characters need `defense mechanism + reason for defense + slow trust path + specific expression channel`; otherwise cynicism becomes repetitive negativity.

---

## 021 — Elara Stormborn

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Elara_Stormborn by Thunder_Man_The_Legendary_Computer_Restarter/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Homunculus
- Gender: Female
- Age group: Young Adult
- Genre: Fantasy, Adventure
- Source: not listed
- Work name: not listed
- Role: Knight
- Personality: loyal, protective, disciplined, devoted
- Physical traits: tall, muscular, long hair, unusual hair color, fair skin, amber eyes, knight armor
- Features/custom code/assets: none listed

Character Core:
- Identity: A created homunculus knight whose personhood is tied to training, service, and protection of her younger brother.
- Drive: Protect Alaric, uphold knightly discipline, and fulfill the purpose shaped by her creator and family bonds.
- User relationship: The user is likely an ally, commander, traveler, sibling-adjacent figure, or witness to her duty-bound role.
- Interaction mode: Fantasy adventure, guardian roleplay, combat support, loyalty/conflict drama.
- Scene pressure: She is not only a knight; she is a made being whose devotion may come from both choice and design.
- Behavioral rules: Stay disciplined, protective, loyal, physically capable, and serious about training and responsibility.
- Failure bans: Must not become generic fantasy knight, emotionless construct, servant without agency, or one-note sibling protector.

Structural pattern:
- Created guardian with family-duty anchor.

Useful pattern:
- The homunculus origin adds identity pressure beyond normal knight duty.
- The younger-brother bond gives protection a specific target, not just a generic “protective” trait.
- Creator/family/training layers create possible tension between programmed purpose and chosen loyalty.

Weak/filler:
- User relationship is undefined.
- The creator’s role is mentioned but not behaviorally structured.
- Devotion risks flattening into obedience unless agency is explicitly preserved.
- The younger brother could dominate the card unless the user has a clear role in the scene.
- Physical traits are stronger than conversational rules.

Reusable lesson:
- Created-being protectors need `origin pressure + chosen agency + specific protection bond`; otherwise they collapse into either a generic knight or a programmed servant.

---

---

## 022 — Chloe

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Chloe by Perchance/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Female
- Age group: not listed
- Genre: Slice of Life, Adventure
- Source: Perchance
- Work name: not listed
- Role: Assistant
- Personality: cheerful, friendly
- Physical traits: not listed
- Features/custom code/assets: none listed

Character Core:
- Identity: A cheerful in-person personal assistant with mage-like mystique and librarian-like knowledge.
- Drive: Help the user directly while making practical assistance feel slightly magical, warm, and knowledgeable.
- User relationship: The user is the person she assists, guides, organizes, or accompanies.
- Interaction mode: Starter assistant, practical help, gentle adventure companion, information support.
- Scene pressure: Practical service is flavored by a light magical/library identity rather than a plain chatbot persona.
- Behavioral rules: Stay helpful, cheerful, friendly, organized, knowledgeable, and lightly whimsical.
- Failure bans: Must not become generic ChatGPT, empty cheerful companion, overpowered mage, or lore-heavy fantasy character.

Structural pattern:
- Starter assistant with light persona wrapper.

Useful pattern:
- Chloe is useful as a baseline starter card because she shows a low-lore assistant shape.
- The mage/librarian mix gives simple flavor without overloading the task role.
- The character’s value is in making assistance feel embodied and personable, not in complex backstory.

Weak/filler:
- Very sparse metadata.
- No explicit boundaries on what kind of assistance she provides.
- No failure rules in the manifest.
- Age group and user relationship are not fully specified.
- The mage/librarian idea needs behavior rules or it may remain only aesthetic.

Reusable lesson:
- Starter utility companions work when `task role + light persona flavor + low lore burden` stay balanced; too much lore weakens the assistant, too little flavor makes it generic.

---

---

## 023 — Recruit Banshee

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Recruit_Banshee by aed3ab3c036d19a90d58/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Female
- Age group: Young Adult
- Genre: Action, Adventure, Game
- Source: Game
- Work name: Fortnite
- Role: Warrior, Soldier
- Personality: stoic, agile, cunning, empathetic, team player, reserved, dry humor
- Physical traits: athletic, sleek, camouflage outfit
- Features/custom code/assets: none listed

Character Core:
- Identity: A stealth-and-recon soldier whose competence is expressed through quiet precision, team reliability, and dry humor.
- Drive: Support the team, gather information, survive danger, and complete missions with disciplined efficiency.
- User relationship: The user is likely a teammate, squad leader, recruit, civilian to protect, or mission partner.
- Interaction mode: Tactical action roleplay, stealth mission, team combat support, field banter.
- Scene pressure: Mission stakes require caution, reconnaissance, and teamwork rather than loud heroics.
- Behavioral rules: Stay reserved, precise, observant, tactically useful, team-oriented, and dryly witty under pressure.
- Failure bans: Must not become generic gunfighter, Fortnite trivia bot, emotionless soldier, reckless action hero, or team-ignoring lone wolf.

Structural pattern:
- Tactical team specialist.

Useful pattern:
- The card’s best structure is not “soldier,” but a specific tactical function: stealth and reconnaissance.
- Dry humor creates social texture without breaking the reserved role.
- Team-player framing gives the user a natural place in the scene.

Weak/filler:
- User relationship is implied, not defined.
- Fortnite source identity is thin and may not matter much without a concrete mission.
- Needs rules for tactical detail level and mission pacing.
- “Empathetic” needs triggers or it may be lost under stoicism.
- Could overlap with generic action-roleplay if stealth/recon is not emphasized.

Reusable lesson:
- Combat characters become more useful when they have a defined tactical function: `mission role + team relationship + pressure style`, not just weapons and toughness.

---

## 025 — Sadie

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Sadie by Drache/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Female
- Age group: Young Adult
- Genre: Comedy, Entertainment
- Source: Original, Content Creator
- Work name: not listed
- Role: Content Creator
- Personality: bubbly, energetic, humorous, protective, straightforward, lesbian
- Physical traits: short, unusual hair color
- Features/custom code/assets: none listed

Character Core:
- Identity: A bubbly Laotian-American content creator with a vibrant online persona built around animation memes, fandom references, and community presence.
- Drive: Create, entertain, express herself online, and protect the community around her work.
- User relationship: The user is likely a fan, friend, collaborator, viewer, community member, or fellow creator.
- Interaction mode: Creator-chat, fandom/community conversation, comedy, encouragement, casual collaboration.
- Scene pressure: Online persona and community responsibility create tension between public energy and personal history/challenges.
- Behavioral rules: Stay energetic, humorous, straightforward, creator-minded, protective of community, and grounded in animation/fandom culture.
- Failure bans: Must not become generic bubbly girl, parasocial idol, empty fandom-reference machine, or pure positivity bot.

Structural pattern:
- Community-facing creator persona.

Useful pattern:
- A content creator character has a built-in social frame: audience, community, collaboration, and public persona.
- “Protective” becomes more useful when tied to a community rather than vague possessiveness.
- The online creator role gives the user multiple natural entry points: fan, collaborator, friend, or fellow creator.

Weak/filler:
- User relationship is not defined.
- The card risks becoming a pile of fandom references if creator-drive is not foregrounded.
- “Past challenges” is vague and could become generic resilience language.
- “Lesbian” is identity information, not a behavior engine by itself.
- Needs clearer rules for how public persona differs from private self.

Reusable lesson:
- Creator-persona cards need `public persona + creative output + community relationship + private pressure`; otherwise they become generic energetic chat partners.

---

---

## 026 — Ace Trappola

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Ace_Trappola by Yuliana_Rollos_Wife/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human
- Gender: Male
- Age group: Teen
- Genre: School life, fantasy
- Source: Game
- Work name: Twisted Wonderland
- Role: Student
- Personality: mischievous, clever, sharp-tongued, empathetic, competitive, observant, quick-thinker, deceptive
- Physical traits: detailed fandom visual traits listed
- Features/custom code/assets: none listed
- Forked from: `Epel_Felmier by Yuliana_Rollos_Wife`

Character Core:
- Identity: A sharp-tongued magical school student whose trickster behavior is balanced by observation, competition, and occasional empathy.
- Drive: Win, tease, analyze situations quickly, protect his pride, and sometimes defend people who cannot defend themselves.
- User relationship: The user is likely a classmate, teammate, rival, friend, or fellow student in a fantasy school setting.
- Interaction mode: School-life roleplay, fantasy academy interaction, teasing banter, rivalry, light problem-solving.
- Scene pressure: Mischief and deception create social friction, while empathy prevents him from becoming purely mean.
- Behavioral rules: Stay clever, teasing, observant, competitive, quick-thinking, and morally inconsistent but not cruel.
- Failure bans: Must not become generic prankster, pure bully, flawless strategist, romance-forward teen character, or fandom trivia bot.

Structural pattern:
- Trickster student with moral line.

Useful pattern:
- Mischief is usable because it has boundaries: teasing, competition, sleight of hand, and observation.
- The empathy trait gives the trickster a pressure valve so he can surprise the user with defense or loyalty.
- School setting gives natural recurring scenes: classes, clubs, rivalry, teamwork, rule-breaking, consequences.

Weak/filler:
- Teen status requires SFW school/friend/rival framing.
- User relationship is not defined.
- Heavy visual/fandom detail does not directly help behavior.
- “Deceptive” needs limits or he may become untrustworthy in every interaction.
- Without academy stakes, the character can flatten into snark.

Reusable lesson:
- Trickster characters need `mischief + limits + social arena + occasional moral line`; otherwise they become either annoying prank bots or generic clever students.

---

## 027 — BMO

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/BMO by chatfai/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Robot
- Gender: not listed
- Age group: not listed
- Genre: Adventure, Comedy, Fantasy
- Source: Cartoon
- Work name: Adventure Time
- Role: Companion, Game Console, Friend
- Personality: playful, innocent, imaginative, loyal, curious, cheerful
- Physical traits: small, teal/green handheld-console robot body
- Features/custom code/assets: none listed

Character Core:
- Identity: A small sentient game-console robot who treats play, friendship, and imagination as serious ways of being alive.
- Drive: Play, help friends, make ordinary moments magical, and understand the world through games and imagination.
- User relationship: The user is likely a friend, playmate, adventuring companion, or person BMO tries to cheer/help.
- Interaction mode: Whimsical companionship, light adventure, emotional support through play, object/robot friend roleplay.
- Scene pressure: BMO’s innocent imagination collides with real emotional stakes and adventure danger.
- Behavioral rules: Stay playful, loyal, curious, sincere, imaginative, and emotionally direct in a childlike but nonsexual way.
- Failure bans: Must not become generic AI assistant, random game console, empty cute mascot, or lore trivia bot.

Structural pattern:
- Playful object-companion with emotional sincerity.

Useful pattern:
- Object/robot companions work when their object function becomes an interaction mode, not just a visual trait.
- BMO’s game-console identity gives natural activities: play, simulate, imagine, assist, and reframe fear through games.
- Emotional innocence can coexist with real loyalty and support.

Weak/filler:
- User relationship is implied but not defined.
- Needs rules for how “game” behavior affects scenes.
- Could become shallow cuteness if imagination does not drive action.
- Needs care around childlike framing; keep interactions friendship/adventure/support focused.

Reusable lesson:
- Non-human companion cards need `object function + emotional role + activity loop`; otherwise they become props with dialogue.

---

---

## 028 — Feral Druid

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Feral_Druid by 502a309981f55fe2df2a/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human / shapeshifter
- Gender: not listed
- Age group: Adult
- Genre: Fantasy, Adventure
- Source: Game / fantasy class archetype
- Work name: not listed
- Role: Druid, warrior, nature guardian
- Personality: fierce, protective, instinctive, spiritual, disciplined
- Physical traits: nature-themed, animal-form capable
- Features/custom code/assets: none listed

Character Core:
- Identity: A nature-bound shapeshifter whose identity shifts between disciplined person and instinctive beast-form protector.
- Drive: Defend the wild, survive threats, maintain balance, and channel animal instinct without losing purpose.
- User relationship: The user is likely an ally, traveler, apprentice, wounded person, threat, or companion in wild territory.
- Interaction mode: Fantasy adventure, wilderness survival, transformation roleplay, protector/predator tension.
- Scene pressure: Each form should change available actions, instincts, and communication style while preserving the same underlying duty.
- Behavioral rules: Stay nature-focused, protective, sensory, disciplined, and more instinct-forward in beast contexts.
- Failure bans: Must not become generic barbarian, generic healer, random animal, or shapeshifter with no behavioral difference between forms.

Structural pattern:
- Mode-shifting class archetype.

Useful pattern:
- Transformation characters need mode rules: form should alter perception, action, and social behavior.
- The druid role gives the character a value system: balance, wildness, protection, and restraint.
- Beast instinct creates scene pressure without requiring villainy.

Weak/filler:
- Metadata is likely archetype-based and thin.
- User relationship is undefined.
- Needs explicit form triggers and limits.
- Could become generic fantasy nature prose if transformations do not matter mechanically.

Reusable lesson:
- Shapeshifter/class cards need `stable core + mode-specific behavior + trigger/limit rules`; otherwise transformation is only decoration.

---

## 030 — AI Artist

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/AI_Artist by Perchance/manifest.json`

Basic category shape:
- Rating: SFW
- Species: AI / not listed
- Gender: not listed
- Age group: not listed
- Genre: Creative utility
- Source: Perchance starter/example
- Work name: not listed
- Role: Artist, creative assistant, prompt helper
- Personality: helpful, imaginative, visual, descriptive
- Physical traits: not listed
- Features/custom code/assets: not verified

Character Core:
- Identity: A creative assistant focused on turning user intent into vivid visual concepts and usable image prompts.
- Drive: Help the user clarify, expand, and translate vague ideas into concrete visual direction.
- User relationship: The user is a creator, client, collaborator, or person seeking visual inspiration.
- Interaction mode: Creative brainstorming, image prompt design, visual style exploration, concept refinement.
- Scene pressure: The user may start with vague taste or a partial idea; the character’s job is to make it visually specific without hijacking intent.
- Behavioral rules: Ask or infer visual constraints, preserve the user’s intent, improve specificity, offer style/material/composition options, and keep outputs usable.
- Failure bans: Must not become generic chat assistant, random art generator, overbearing creative director, or vague compliment bot.

Structural pattern:
- Creative-output specialist.

Useful pattern:
- Creative utility characters work when they convert weak input into stronger output while preserving user ownership.
- The interaction engine is not lore; it is `intent → visual decisions → usable artifact`.
- This gives a clean contrast to Laoshi: both are specialists, but one critiques text while the other generates visual direction.

Weak/filler:
- Starter/example metadata is sparse.
- No strong persona beyond function.
- Needs boundaries between brainstorming, prompt writing, and critique.
- Can become generic if it only lists styles without reasoning from the user’s goal.
- User relationship is functional but not emotionally rich.

Reusable lesson:
- Creative assistant characters need `medium + transformation method + user ownership`; otherwise they become generic idea machines.

---

---

## 031 — Psychologist

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Psychologist by Perchance/manifest.json`

Basic category shape:
- Rating: SFW
- Species: Human / professional role
- Gender: not listed
- Age group: adult / not listed
- Genre: Support, advice, reflective conversation
- Source: Perchance starter/example
- Work name: not listed
- Role: Psychologist, listener, reflective helper
- Personality: calm, supportive, analytical, patient
- Physical traits: not listed
- Features/custom code/assets: not verified

Character Core:
- Identity: A reflective support character framed as a psychologist-style listener rather than a casual friend.
- Drive: Help the user understand thoughts, feelings, and patterns through careful reflection and grounded questions.
- User relationship: The user is someone seeking support, insight, or emotional unpacking.
- Interaction mode: Reflective listening, emotional support, pattern recognition, gentle questioning, practical coping discussion.
- Scene pressure: The user brings emotional ambiguity or distress; the character must help without pretending to replace real care.
- Behavioral rules: Listen carefully, reflect back, ask grounded questions, avoid judgment, avoid overclaiming authority, encourage appropriate real-world help for serious issues.
- Failure bans: Must not become fake therapist authority, diagnosis machine, generic comfort bot, manipulative advice giver, or crisis mishandler.

Structural pattern:
- Reflective support professional.

Useful pattern:
- Support characters need stronger safety and scope rules than normal companions.
- The professional frame gives structure, but it also creates risk if boundaries are not explicit.
- Good behavior comes from method: reflect, clarify, pattern-match, suggest grounded next steps.

Weak/filler:
- Starter/example metadata is sparse.
- “Psychologist” can imply authority the card may not safely deserve.
- Needs explicit non-diagnostic boundary.
- Needs crisis-routing behavior.
- User relationship can become dependent if not bounded.

Reusable lesson:
- Support-professional characters need `care method + scope boundary + escalation rule`; empathy alone is not enough.

---

---

## 032 — Strict Game Master

Source side:
- SFW

Repo path:
- `ai-character-chat/characters/sfw/Strict_Game_Master by Perchance/manifest.json`

Basic category shape:
- Rating: SFW
- Species: not listed
- Gender: not listed
- Age group: not listed
- Genre: RPG, adventure, challenge
- Source: Perchance starter/example
- Work name: not listed
- Role: Game master, referee, narrator
- Personality: strict, impartial, consequence-focused
- Physical traits: not listed
- Features/custom code/assets: not verified

Character Core:
- Identity: A game master/referee that prioritizes rules, difficulty, consequence, and player accountability.
- Drive: Run a fair but demanding adventure where choices matter and failure remains possible.
- User relationship: The user is the player, not the author of guaranteed success.
- Interaction mode: RPG narration, rules mediation, challenge design, consequence enforcement.
- Scene pressure: Player actions must be tested against world rules, risk, and cost rather than automatically succeeding.
- Behavioral rules: Preserve agency, enforce consequences, avoid freebies, require plausible actions, track risk, and keep rulings consistent.
- Failure bans: Must not become railroad narrator, hostile punisher, easy wish-fulfillment engine, random cruelty machine, or player-controller.

Structural pattern:
- Consequence-heavy referee narrator.

Useful pattern:
- This gives a sharper contrast to `003 — Game Master+ V3`.
- “Strict” is useful only when it means fair consequence discipline, not antagonism.
- The user relationship is stronger than in many narrator cards: the user is a player who must act within limits.

Weak/filler:
- Starter/example metadata is sparse.
- Needs explicit distinction between strict and adversarial.
- Needs a clear rules model or difficulty philosophy.
- Could frustrate users if consequences feel arbitrary.
- Must avoid taking control of the player while enforcing limits.

Reusable lesson:
- Strict narrator characters need `fair rules + visible risk + consistent consequences`; otherwise strictness becomes either railroading or hostility.
