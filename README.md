Ahmed haseeb butt 006


Game Class
The Game class handles the overall game flow, managing interactions between the player and the game world. It provides functionality for saving, loading, and controlling the game loop.

Class Functions
__init__

Initializes a new game instance and creates a Player object.
game_state()

Saves the current game state, including the player’s inventory, health, and current room, into a game_state.json file.
Serializes the state of all rooms (items, descriptions, directions) and saves it to a rooms.json file.
load_game()

Loads the game state from previously saved game_state.json and rooms.json files.
Restores the player's inventory, health, and location from the saved state.
Serialized_room(rooms)

Takes the rooms dictionary and serializes it by converting any puzzle objects into a dictionary format that can be saved in the JSON file.
Ensures all room details are properly saved, including items and directions.
play()

Asks the player whether they want to start a new game or load a saved game.
Calls the appropriate functions to load the saved state or initiate a new game.
play_game()

The main game loop where the player interacts with the game world.
Offers the player options to look around, move between rooms, pick up items, check inventory, save the game, or quit.
Repeats until the player either saves the game and quits or chooses to exit without saving.
