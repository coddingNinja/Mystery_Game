class Puzzle:
    def __init__(self, Name, Description, SolveKey):
        self.Name = Name
        self.Description = Description
        self.SolveKey = SolveKey[:]

    def solve(self, Current_location):
        Rooms[Current_location]['Items'] = [i for i in Rooms[Current_location]['Items'] if not isinstance(i, Puzzle)]
        print(Rooms[Current_location]['Items'])
    def to_dict(self):
        return{
            "Name": self.Name,
            "Description": self.Description,
            "SolveKey": self.SolveKey
        }

Rooms = {
    "Cafeteria": {
        "Items": ["food"],
        "Description": "You are in the Cafeteria.",
        "Directions": {
            "North": None,
            "South": "Storage",
            "East": "Weapons",
            "West": "UpperEngine"
        }
    },
    "Weapons": {
        "Items": [
            Puzzle("Locked Box", "A box that requires two special keys to open.", ["a broken Key 1", "a broken Key 2"]),
            "Gun"
        ],
        "Description": "You are in the Weapons room.",
        "Directions": {
            "North": None,
            "South": "Navigation",
            "East": None,
            "West": "Cafeteria"
        }
    },
    "Navigation": {
        "Items": ["bullet", "8989"],
        "Description": "You are in the Navigation room.",
        "Directions": {
            "North": "Weapons",
            "South": None,
            "East": None,
            "West": None
        }
    },
    "Basement": {
        "Items": [
            Puzzle("Dark", "This room is dark; you need a light to see.", ["Torch"]),
            "ExitKey"
        ],
        "Description": "You are in the Basement.",
        "Directions": {
            "North": "Storage",
            "South": None,
            "East": None,
            "West": "ExitRoom"
        }
    },
    "Storage": {
        "Items": ["a broken Key 1"],
        "Description": "You are in the Storage room.",
        "Directions": {
            "North": "Cafeteria",
            "South": "Basement",
            "East": "Navigation",
            "West": "Reactor"
        }
    },
    "Reactor": {
        "Items": [
            "food",Puzzle("Locked Locker", "A locker that requires a passcode to open.", ["8989"]),
            "a broken Key 2"
        ],
        "Description": "You are in the Reactor room.",
        "Directions": {
            "North": None,
            "South": None,
            "East": "Storage",
            "West": None
        }
    },
    "UpperEngine": {
        "Items": ["bullet"],
        "Description": "You are in the Upper Engine room.",
        "Directions": {
            "North": None,
            "South": "Security",
            "East": "Cafeteria",
            "West": None
        }
    },
    "Security": {
        "Items": [
            Puzzle("Monster", "A monster is sleeping; requires a gun and two bullets to kill.", ["Gun", "bullet", "bullet"]),
            "Torch"
        ],
        "Description": "You are in the Security room.",
        "Directions": {
            "North": "UpperEngine",
            "South": "ExitRoom",
            "East": None,
            "West": None
        }
    },
    "ExitRoom":{
        "Items":{Puzzle("Locked Door","You require a ExitKey to open it",["ExitKey"])},
         "Description": "You are in the Exit room.",
        "Directions": {
            "North": None,
            "South":None,
            "East": None,
            "West": None
        }
    }
}