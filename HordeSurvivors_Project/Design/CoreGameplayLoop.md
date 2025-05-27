# Design Document: Core Gameplay Loop

This document outlines the primary gameplay loop for Horde Survivors, detailing the player's typical experience from starting a run to progressing through the game.

## I. Overall Game Structure (Macro Loop)

1.  **Class Selection (Start of Campaign):**
    * Player makes a long-term decision by choosing one of the four distinct classes: Lich, Prince, Beast Lord, or Void Spawn.
    * This choice dictates their unique units/abilities, minigame, and overall playstyle for the entire campaign/save.

2.  **Campaign Progression (Inter-Floor Loop):**
    * The campaign consists of a series of "Floors" or "Regions" (e.g., The Ruined Farmlands, The Cursed Catacombs).
    * To complete a Floor, the player must enter it, explore, achieve objectives, and defeat the Floor Boss.
    * Successfully clearing a Floor unlocks the next, more challenging Floor.
    * Between Floors, players may have opportunities for Meta-Progression (spending permanent currency) and deeper engagement with their class minigame.
    * Failure on a Floor might result in restarting that Floor (potentially with some minor resource retention) or returning to a hub with meta-progression opportunities.

## II. Per-Floor Gameplay (Micro Loop)

This describes the loop a player experiences within a single Floor:

1.  **Entry & Setup:**
    * Player enters the new Floor. The mini-open-world map is revealed (possibly with fog of war).
    * Player starts with their class leader and any initial units/abilities granted by their class and meta-progression.

2.  **Exploration & Objective Identification:**
    * Player navigates the procedurally generated mini-open-world map.
    * Map contains various Points of Interest (POIs): combat zones, resource nodes, events, shrines, class-specific locations (e.g., Graveyards for Lich), and the path to the Floor Boss (which may initially be locked).
    * Player identifies primary objectives (e.g., "Destroy 3 Spawners," "Collect 2 Key Fragments," "Survive the Gauntlet") necessary to unlock the Boss encounter.

3.  **Encounter & Combat (Vampire Survivors Style):**
    * Entering combat zones or triggering ambushes initiates horde combat.
    * Enemies spawn in waves or fill the screen, moving towards the player/army.
    * Player's character/army attacks automatically or with simple player-triggered abilities.
    * **Player Focus:** Strategic movement, positioning, dodging projectiles, and efficient collection of XP gems ("Essence" or "Souls").
    * **Leveling Up (In-Run):** Collecting enough XP gems triggers a level-up, presenting the player with a choice of 3-4 temporary upgrades for the current run (e.g., new ability, upgrade existing ability, stat boost, utility enhancement). These choices are critical for build-crafting.

4.  **Resource Gathering & Minigame Engagement:**
    * While exploring and fighting, player gathers:
        * **In-Run XP ("Essence"):** For leveling up abilities during the current run.
        * **In-Run Currency ("Gold/Shards"):** For temporary shops, events.
        * **Class-Specific Resources:** (Corpses, Survivors, Tameable Beasts, Genetic Markers) used for their unique class minigames.
    * Player interacts with class-specific POIs or interfaces to engage their minigame (Fuse Undead, Manage Kingdom, Breed Beasts/Carve Tattoos, Evolve Void Spawn). This grants new units, powers, or permanent (for the run) upgrades to their army/self.

5.  **Powering Up & Strategic Choices:**
    * Through combat upgrades, minigame progression, event rewards, and shrine boons, the player's overall power increases.
    * Player makes strategic decisions:
        * Which POIs to tackle first?
        * Risk vs. Reward: Engage optional, harder combat zones for better loot?
        * Which upgrades synergize best with their current class build?
        * How to best utilize their class-specific resources?

6.  **Achieving Objectives & Unlocking Boss:**
    * Player completes the necessary sub-objectives on the Floor map.
    * This opens the path to the Floor Boss arena.

7.  **Floor Boss Confrontation:**
    * A challenging, multi-stage encounter against a unique, powerful enemy with distinct mechanics.
    * May involve continued horde elements alongside direct boss mechanics.
    * Tests the player's build, execution, and understanding of their class.

8.  **Floor Completion & Rewards:**
    * Defeating the boss completes the Floor.
    * Player receives significant rewards:
        * Meta-Currency ("Realm-Shards") for permanent meta-progression.
        * Potential for unlocking new base abilities/units/minigame aspects for their class.
        * Sometimes a powerful "Relic" or unique item for the rest of the current campaign run.
    * Player exits the Floor and proceeds to the inter-floor progression stage.

## III. Failure Loop

* If the player's leader is defeated on a Floor:
    * The current run on that Floor ends.
    * Depending on design choice:
        * **Option A (Harsher):** Player loses all in-run progress for that Floor and must restart it from the beginning. Any collected Meta-Currency might be retained.
        * **Option B (Softer):** Player loses some progress/resources but might retain some class-specific resources or have an easier restart.
    * Player is typically returned to a meta-progression screen or hub before attempting the Floor again or choosing a different unlocked Floor (if applicable).

This loop structure aims to provide engaging moment-to-moment action, strategic depth through build choices and class mechanics, and long-term replayability via class diversity and meta-progression.
