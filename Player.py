from map import Rooms, Puzzle
class Player:
    def __init__(self, Current_Location="Cafeteria", Inventory=None, Health=100):
        self.Current_Location = Current_Location
        self.Health = Health
        self.Inventory = Inventory[:] if Inventory is not None else []

    def look(self):
        print(f"\nLocation: {Rooms[self.Current_Location]['Description']}\n")
        for item in Rooms[self.Current_Location]["Items"]:
            if isinstance(item, Puzzle):
                print(f"Puzzle Found: {item.Name}")
                if not self.use_inventory(item):
                    if item.Name == "Monster":
                        self.Health -= 50
                        print(f"\n*** ALERT: The monster hits you! Your health reduces to {self.Health} ***")
                        print(f"You don't have the required items in your inventory to solve {item.Name}.\n")
                        self.Current_Location="UpperEngine"
                        self.eat_food()
                        if self.Health == 0:
                            print("********** YOU LOSE **********")
                            exit(0)
                else:
                    action = input(f"\nYou can solve {item.Name} by using {' . '.join(item.SolveKey)} from your inventory.\nEnter 'Yes' to solve or 'No' to continue: ")
                    if action.lower() == 'yes':
                        item.solve(self.Current_Location)
                        self.drop_used_item(item)
                break
            else:
                print(f"Item Found:{item}\n")
    def drop_used_item(self,Puzzel):
        for i in Puzzel.SolveKey:
            self.Inventory.remove(i) if i in self.Inventory else None
        return
    def drop_item(self):
        print("Where would you like to drop?")
        drop_item=input()
        Rooms[self.Current_Location]['Items'].insert(0,drop_item)
        print(f"The {drop_item} is dropped at {self.Current_Location}")
        self.Inventory.remove(drop_item)



    def move(self):
        print("\nWhere would you like to move?\n")

        directions = Rooms[self.Current_Location]['Directions']
        available_direction = {direction: room for direction, room in directions.items() if room}
        if self.Current_Location == "ExitRoom" and not Rooms["ExitRoom"]["Items"]:
            self.exit_room()


        for direction, room in available_direction.items():
            print(f"Enter '{direction}' to move to {room}.")

        while True:
            next_room = input("\nEnter direction: ").capitalize()
            if next_room in available_direction.keys():
                self.Current_Location = Rooms[self.Current_Location]['Directions'][next_room]
                if self.Current_Location == "ExitRoom" and "ExitKey" not in self.Inventory:
                    print(f"To enter in Exit room you have to have Exit Key ")
                    self.Current_Location = "Basement"
                print(f"\n***You have moved to {self.Current_Location} ***\n")

                break
            else:
                print("Invalid direction. Please try again.")

    def look_inventory(self):
        if self.Inventory:
            print("\n*** Your Inventory ***")
            for item in self.Inventory:
                print(f" - {item}")
            print("Want to drop somthing? yes or no")
            action=input().lower()
            self.drop_item() if action=="yes" else None
        else:
            print("\nYour inventory is empty.")

    def pick(self):
        print("\nWhat would you like to pick up?")
        RoomItems =[]
        for item in Rooms[self.Current_Location]["Items"]:
            if isinstance(item, Puzzle):
                break
            else:
                RoomItems.insert(0,item)
        if RoomItems:
           for item in RoomItems:
             print(f"{item}")
           while True:
               pick_item = input(f"Enter the name of the item you want to pick: ")
               if pick_item in RoomItems:
                   self.Inventory.append(pick_item)
                   Rooms[self.Current_Location]["Items"].remove(pick_item)
                   print(f"\n*** {pick_item} added to your inventory. ***")
                   break
               else:
                   print("Invalid item. Please try again.")
        else:
            print("There is nothing to pick up ")


    def use_inventory(self, puzzle):
        for key in puzzle.SolveKey:
            if key not in self.Inventory:
                return False
        return True

    def eat_food(self):
        if 'food' in self.Inventory:
            print("\nYou have food in your inventory.")
            action = input("Do you want to eat the food to restore health? (yes/no): ")
            if action == "yes":
                self.Health += 50
                self.Inventory.remove("food")
                print(f"\n*** You ate the food. Your health is now {self.Health}% ***")
            else:
                print("\nYou chose not to eat the food.")
        else:
            print("\n*** No food in your inventory. Find food to restore health! ***")

    def exit_room(self):
        print("Solve this Riddle to Exit you have 5 chances")
        for i in range (5):
            print(f"Wo kon si cheez ha jis ko ham pani k ander khaty han ")
            answer=input("\nAnswer the Riddle ")
            if answer=="Gota":
                print("_________________ You have Won The Game _________________")
                exit(0)
        else:
            print("********** YOU LOSE **********")
            exit(0)
# Formating of code done by the greate Gpt