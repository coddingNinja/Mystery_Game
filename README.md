sp23-bai-006 
sp23-bai-004


Mystery Castle Game
Project Overview
Mystery Castle is a text-based adventure game where players explore rooms, solve puzzles, and collect items while managing their inventory and health. The player must navigate through different rooms, find keys, and solve challenges to win the game. The game includes the ability to save and load progress using JSON files.

Features
Explore different rooms with unique descriptions and items.
Solve puzzles that either help you progress or hinder you by affecting your health.
Manage an inventory where you can pick up and use items.
Save and load the game state, allowing you to resume from where you left off.
Dynamic room states that update as you progress.
Win by solving a final puzzle.
Classes and Game Structure
Player Class
The Player class manages the player’s state in the game, such as:

Current Location: Tracks where the player is in the game world.
Inventory: Manages items that the player has collected and can use to solve puzzles or heal.
Health: Keeps track of the player’s health, which decreases if certain puzzles are not solved.
Key Methods:
look():
Displays the current room’s description and items, detects if a puzzle is present, and manages the puzzle-solving process.

move():
Allows the player to move between rooms.

pick():
Adds items to the player's inventory from the room.

look_inventory():
Displays the player’s inventory and allows them to drop items if needed.

use_inventory():
Verifies whether the player has the correct items in their inventory to solve a puzzle.

eat_food():
Restores the player’s health if they have food in their inventory.

Game Class
The Game class controls the overall game flow and manages saving/loading of the game state.

Key Methods:
game_state():
Saves the current player and room states to JSON files (game_state.json and rooms.json), allowing players to resume the game later.

load_game():
Loads the saved game state from JSON files and restores the player’s inventory, health, and current location, along with room data.

play():
Handles the initial game options, allowing players to either load a saved game or start a new one.

play_game():
The main game loop where players can look around, move between rooms, pick up items, check inventory, or quit the game.

Rooms and Puzzles
Rooms:
Each room in the game contains a description, items, and directions to other rooms. The player can explore rooms, pick up items, and interact with puzzles.

Puzzles:
Certain rooms contain puzzles that must be solved to progress. Some puzzles require specific items from the player’s inventory to be solved.





MysteryCastle/
│
├── game_state.json        # Saved player state file
├── rooms.json             # Saved room state file
├── map.py                 # Contains room and puzzle data
├── Player.py              # Player class definition
├── Game.py                # Game class definition
├── main.py                # Entry point to start the game
└── README.md              # Project documentation
