Art_Source Directory
This directory contains all the raw, editable source files for the art assets used in Horde Survivors. These are the working files that artists will use in their respective software (e.g., Photoshop, Blender, Substance Painter) before exporting game-ready assets.

Purpose
Preservation of Quality: Stores original, high-resolution, and layered files, allowing for non-destructive editing and easier iteration.

Collaboration: Provides a central location for artists to access and modify source art.

Asset Pipeline: Serves as the starting point of the art pipeline. Assets created or modified here are then processed and exported to the main /Game/Art/ (or equivalent engine-specific) directory in a game-ready format (e.g., .png, .fbx with optimized topology/textures).

Subdirectory Structure
/Characters/: Source files for all character art.

/Prince/: Prince class specific character art (model, textures, concept).

/Lich/: Lich class specific character art.

/BeastLord/: Beast Lord class specific character art.

/VoidSpawn/: Void Spawn class specific character art.

/Enemies/: Source files for various enemy types (grunts, elites, bosses).

/NPCs/: Source files for any non-player characters (merchants, quest givers, etc.).

/Environments/: Source files for environment art.

/Floor_RuinedFarmlands/: Art for the "Ruined Farmlands" floor (props, textures, concept).

(Other floor-specific directories will follow the same pattern)

/UI/: Source files for User Interface elements.

/HUD_Source/: Source for Heads-Up Display elements.

/Menus_Source/: Source for main menu, pause menu, settings, etc.

/Icons_Source/: Source files for ability icons, item icons, status effect icons, etc.

/VFX_Source/: Source files for visual effects (e.g., texture sheets for particle systems, flipbooks).

/General/: VFX applicable across multiple classes or contexts.

/ClassSpecific/: VFX unique to each player class.

Guidelines
File Naming Conventions: Adhere to the project's established file naming conventions (see /Documentation/ArtStyleGuide.md - assuming this file will be created).

Version Control: Use Git LFS (Large File Storage) if necessary for large binary files. Commit frequently with clear messages.

Exporting: When exporting assets for the game, ensure they are optimized (correct formats, resolutions, compression) and placed in the appropriate subdirectories within /Game/.

Do Not Place Game-Ready Assets Here: This directory is strictly for source files. Game-ready, imported assets belong in the main /Game/ directory structure.

This organization helps maintain a clean and efficient workflow for all art-related tasks.