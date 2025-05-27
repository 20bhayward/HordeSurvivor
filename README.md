# Vampire Survivors Clone - Epochal Conquest

This project is a Vampire Survivors type game with a unique lore based on conquering different epochs of a sundered world. This initial version sets up the core game mechanics and the first epoch.

## Current Features

*   **Player:**
    *   WASD movement.
    *   Leveling system with stat increases (Health, Speed, Damage).
    *   XP collection from defeated enemies.
*   **Enemies:**
    *   Basic enemy AI (moves towards player).
    *   Spawn in waves with a configurable rate and maximum number.
*   **Combat:**
    *   Simple melee attack (Spacebar) with cooldown.
    *   Weapons are temporary sprites that damage enemies on contact.
*   **Game Systems:**
    *   XP orbs dropped by enemies.
    *   Pygame-based graphics for rendering.
    *   Thematic coloring for the "Sundered Epoch of Primordials."
*   **UI:**
    *   Displays Player Level.
    *   Displays Player Health (text and bar).
    *   Displays Player XP (text and bar).
    *   Displays current Wave Number.
    *   Displays current Epoch Name.

## Project Structure

*   `main.py`: Main game loop, Pygame initialization, event handling, and core game flow.
*   `player.py`: Defines the `Player` class, including movement, stats, leveling, and attacks.
*   `enemy.py`: Defines the `Enemy` class, including movement AI.
*   `weapon.py`: Defines the `Weapon` class used for player attacks.
*   `xp_orb.py`: Defines the `XPOrb` class for experience points dropped by enemies.
*   `game.py`: Manages game state, enemy spawning, combat resolution (weapon-enemy collision), XP collection, and leveling checks.
*   `graphics.py`: Currently unused, intended for more complex graphics rendering functions.
*   `config.py`: Contains game settings like screen dimensions, colors, speeds, spawn rates, UI parameters, etc.
*   `assets/`: Directory for game assets (currently empty, sprites are procedurally generated).

## Setup and Run

1.  Ensure you have Python installed.
2.  Install Pygame: `pip install pygame`
3.  Clone this repository.
4.  Run the game: `python main.py`

## Future Development Ideas (Beyond this initial phase)

*   Actual sprite assets for player, enemies, weapons.
*   Different enemy types per epoch.
*   More diverse weapons and attack patterns.
*   Passive abilities and class system.
*   Detailed lore implementation for each epoch.
*   Idle game mechanics.
*   Sound effects and music.
*   More sophisticated UI and menus.
