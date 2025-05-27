Horde Survivors - Project Overview
Welcome to the Horde Survivors project! This document provides a high-level overview of the project structure and key directories.

Project Goal
Horde Survivors is a "horde/army based vampire survivors" style game where the player chooses one of four distinct classes (Lich, Prince, Beast Lord, Void Spawn) at the beginning of a campaign. Each class offers a unique gameplay experience, progression system, and associated minigame. The core gameplay loop involves navigating mini open-world "floors" (akin to Slay the Spire progression), battling hordes of enemies, gathering resources, upgrading the chosen class's army/abilities, and defeating floor bosses to advance.

Main Directory Structure
/Art_Source/: Contains all raw, editable art assets (e.g., .psd, .blend, .spp files). These are the source files used to generate game-ready assets.

/Audio_Source/: Contains all raw, editable audio assets (e.g., DAW project files, unmixed .wav files).

/Design/: Houses game design documents (GDDs), balance spreadsheets, narrative outlines, level design blueprints, UI mockups, and other planning materials.

/Game/: The root directory for the game engine project (e.g., Unity's Assets folder or Unreal Engine's Content folder). This contains all game-ready assets, scripts, scenes, and configurations.

/Tools/: Custom tools developed to aid in the creation, building, or management of the game (e.g., level editor extensions, build scripts).

/Documentation/: Technical documentation, coding standards, API references, and other developer-focused guides.

/ProjectManagement/: Files related to project management, such as build outputs, QA test plans, bug reports, and milestone tracking.

Getting Started
Familiarize yourself with the Design documents in /Design/ to understand the core mechanics, class specifics, and progression systems.

For Game Assets & Logic: The primary development work will occur within the /Game/ directory, using the chosen game engine.

Source Art/Audio: If you are contributing art or audio, work within the /Art_Source/ or /Audio_Source/ directories and export/import game-ready assets into the /Game/ directory.

Consult /Documentation/ for coding standards and technical guidelines.

Key Systems (Conceptual)
Class System: Lich, Prince, Beast Lord, Void Spawn with unique units, abilities, and minigames.

Combat: Vampire Survivors-inspired horde combat with automated/semi-automated attacks.

Progression: Slay the Spire-inspired floor-based advancement with mini open-world exploration on each floor.

Resources: In-run XP/currency, class-specific resources, and meta-progression currency.

Minigames:

Lich: Undead fusion.

Prince: Idle kingdom management.

Beast Lord: Monster breeding & shamanic tattoo carving.

Void Spawn: Evolutionary path fueled by consuming enemies.

Refer to the README.md file within each subdirectory for more specific information about its contents and purpose.