SP23-BAI-004

# Puzzle Map Game

This is a simple Python-based text adventure game featuring a map where the player interacts with different rooms and solves puzzles by using specific items. The rooms are interconnected, and some rooms contain puzzles that need to be solved to progress.

## Features
- **Rooms:** The game consists of various rooms (Cafeteria, Weapons, Reactor, Security, etc.) each with its own description, items, and directions.
- **Puzzles:** Some rooms contain puzzles that must be solved to progress. These puzzles require certain items (like keys, torches, or bullets) and once solved, the puzzle object is removed from the room.
- **Items:** Players can collect and use various items to solve puzzles and progress through the map.
- **Navigation:** Each room is connected to other rooms, and players can move between them using directional commands (North, South, East, West).

## Room Details
Here is a brief overview of the rooms and their associated puzzles:

- **Cafeteria:** A starting room with food items.
- **Weapons:** Contains a locked box puzzle that requires two broken keys to open, and a gun.
- **Navigation:** Contains some bullets and a numeric code.
- **Basement:** A dark room requiring a torch to navigate, and an ExitKey to unlock the final door.
- **Storage:** Contains one of the broken keys.
- **Reactor:** Contains a locker puzzle that requires a passcode to unlock.
- **Upper Engine:** Contains bullets.
- **Security:** Contains a puzzle where a monster must be defeated using a gun and two bullets.
- **Exit Room:** Contains a locked door puzzle that requires an ExitKey to open.

## Classes

### `Puzzle`
This class represents a puzzle in the game. It has the following attributes:
- `Name`: The name of the puzzle.
- `Description`: A description of the puzzle and what it requires.
- `SolveKey`: A list of items required to solve the puzzle.

#### Methods:
- `solve(self, Current_location)`: Solves the puzzle by removing the puzzle from the room's item list.
- `to_dict(self)`: Returns the puzzle's details as a dictionary.

### Game Mechanics
Rooms are stored in a dictionary format where each room has:
- `Items`: A list of items present in the room.
- `Description`: A brief description of the room.
- `Directions`: Available directions for moving to other rooms.

## Example Usage

- **Navigating the map:** Move from room to room using directional commands.
- **Solving puzzles:** Collect items from the rooms and use them to solve puzzles in different rooms.
- **Inventory management:** Manage the items you've collected to ensure you can solve the puzzles and unlock new areas.
