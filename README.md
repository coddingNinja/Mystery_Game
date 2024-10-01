Ahmed haseeb  006

Player Class
The Player class manages the player's current state, including their location, health, and inventory. It provides essential methods to allow the player to interact with the game world, move between rooms, pick up and use items, solve puzzles, and track health.

Attributes

Current_Location: The room the player is currently in (default is "Cafeteria").
Health: The player's health (starting at 100). Health can decrease or be restored by eating food.
Inventory: A list of items the player has collected, used for solving puzzles or restoring health.

Key Methods

look(): Describes the current location, displays available items or puzzles, and checks if a puzzle can be solved with the items in the inventory.
move(): Allows the player to move to a different room based on available directions. The player cannot enter certain rooms (e.g., ExitRoom) without required items.
pick(): Lets the player pick up items in the current room and add them to their inventory.
look_inventory(): Displays the player's inventory and offers the option to drop items.
use_inventory(): Checks if the player has the correct items to solve a puzzle.
drop_item(): Allows the player to drop an item from their inventory into the current room.
eat_food(): Restores health if the player has food in their inventory.
exit_room(): A final riddle challenge in the ExitRoom to win the game.
The player must strategize their moves, solve puzzles, and manage their inventory effectively to win the game!
