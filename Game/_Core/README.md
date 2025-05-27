/Game/_Core Directory
This directory is the heart of the shared gameplay systems for Horde Survivors. It contains all the fundamental scripts, prefabs, and assets that are not specific to any single player class but are essential for the overall game to function.

Purpose
Modularity and Reusability: To centralize common game logic, preventing code duplication and making systems easier to maintain and update.

Foundation for Classes: Provides the base systems upon which class-specific mechanics are built.

Global Managers: Houses manager scripts that oversee game-wide states and functionalities.

Subdirectory Structure
/Scripts/: Core C# (or other language) scripts.

/Managers/: Global manager singletons or services (e.g., GameManager, UIManager, AudioManager, InputManager, SaveLoadManager, SceneTransitionManager, PoolManager).

/CombatSystem/: Scripts related to fundamental combat mechanics like damage calculation, health systems, status effect application, targeting logic (if not purely auto-target), hit detection, projectile base classes.

/Progression/: Scripts for player leveling (in-run XP), handling the selection and application of temporary upgrades, and managing meta-progression currency and unlocks.

/EntitySystem/: Base classes or interfaces for all dynamic game objects (e.g., Entity, Character, Enemy, Projectile). Defines common properties like health, movement, and interaction with other systems.

/ResourceSystem/: Management of global in-run resources like "Essence/Souls" (XP) and "Gold/Shards" (currency). Does not handle class-specific resources.

/EventSystem/: Scripts for handling scripted map events, player choices, and their outcomes. May include a simple event bus or delegate system for inter-script communication.

/Utility/: General-purpose helper functions, common data structures (e.g., weighted random selectors), math utilities, and other miscellaneous tools used across multiple systems.

/AI/: Core Artificial Intelligence behaviors and systems.

Pathfinding: Scripts related to navigation meshes or A* pathfinding.

Flocking/Swarming: Behaviors for managing large groups of enemies.

SteeringBehaviors: Basic movement behaviors (seek, flee, wander, arrive).

StateMachineBase: A base class for creating finite state machines for AI agents.

/Prefabs/: Core prefabs used throughout the game.

XPGem.prefab: The visual and logical representation of experience pickups.

GoldPickup.prefab: Prefab for currency drops.

DamageNumberPopup.prefab: Prefab for displaying damage numbers.

GenericInteractable.prefab: A base prefab for objects players can interact with on the map.

/Shaders/: Commonly used shaders that are not specific to one asset type (e.g., a generic sprite shader, a highlight shader).

Guidelines
No Class-Specific Logic: Absolutely no code or assets that are unique to the Lich, Prince, Beast Lord, or Void Spawn should reside here. Such content belongs in the /Game/Classes/[ClassName]/ directories.

Interfaces and Base Classes: Favor the use of interfaces and abstract base classes here to define contracts that class-specific implementations can then fulfill.

Dependency Management: Core systems should be as self-contained as possible or rely on other core systems. Avoid direct dependencies from _Core systems into specific class directories. Class-specific systems will depend on _Core.

Testing: Core systems should be rigorously tested as they form the foundation of the entire game.

This directory is critical. Changes here can have wide-ranging effects, so careful planning and robust implementation are paramount.