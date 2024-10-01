from Player import Player
import json

from map import Rooms, Puzzle


class Game:
    def __init__(self):
        self.player = Player()

    def game_state(self):
        gamestate = {
            "Current_Location": self.player.Current_Location,
            "Inventory": self.player.Inventory,
            "Health":self.player.Health
        }
        room_state=self.Serialized_room(Rooms)
        json_object=json.dumps(gamestate)
        json_object2=json.dumps(room_state,indent=4)
        with open("game_state.json", "w") as write_file:
            write_file.write(json_object)
        with open("rooms.json","w") as write_file2:
            write_file2.write(json_object2)
        print("\n*** Game saved successfully! ***")

    def load_game(self):
        try:
            with open("game_state.json", 'r') as load_game:
                json_object = json.load(load_game)
                self.player.Inventory = json_object["Inventory"]
                self.player.Current_Location = json_object["Current_Location"]
                self.player.Health=json_object["Health"]

            print("\n*** Game loaded successfully! ***")
        except FileNotFoundError:
            print("\n*** No saved game found. Starting a new game. ***")
        try:
            #done with the help of gpt in loading game rooms as json
            with open("rooms.json", 'r') as load_game:
                room = json.load(load_game)
                return room

        except FileNotFoundError:
            print("\n*** No saved game found. Starting a new game. ***")
    def Serialized_room(self,rooms):
        rooms_state={}
        for room_name,room_detail in rooms.items():
            rooms_state[room_name]={
                "Items":[item.to_dict() if isinstance(item,Puzzle) else item for item in room_detail["Items"]],
                "Description":room_detail["Description"],
                "Directions":room_detail["Directions"]
            }
        return  rooms_state
    def play(self):
        print("_________________ Welcome to Mystery Castle Game _________________")
        print("Do you want to start a [new] game or [load] a saved game?")
        state = input().lower()

        if state == "load":
            Room = self.load_game()
            Rooms.update(Room)
            self.play_game()
        else:
            print("\nStarting a new game...")
            self.play_game()
    def play_game(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. Look around")
            print("2. Move to another room")
            print("3. Take an item")
            print("4. Look at your inventory")
            print("5. Save game and quit")
            print("6. Quit the game")

            action = input("\nEnter the number of your action: ")

            if action == "1":
                print("\nYou take a look around...")
                self.player.look()
            elif action == "2":
                self.player.move()
            elif action == "3":
                print("\nYou try to take an item...")
                self.player.pick()
            elif action == "4":
                print("\nChecking your inventory...")
                self.player.look_inventory()
            elif action == "5":
                self.game_state()
                exit(0)
            elif action == "6":
                print("\n*** Quitting the game. Goodbye! ***")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")
