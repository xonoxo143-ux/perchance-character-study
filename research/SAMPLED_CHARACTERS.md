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

The next batch starts at `012–014`.

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
