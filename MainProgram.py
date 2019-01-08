from Adventurer import *
from Rooms import *
from Things import *


def go(player, rooms, direction):
    if direction != "":
        current_room = player.Current_Room
        try:
            if rooms[current_room].linked_rooms[direction] is not False:
                link = rooms[current_room].linked_rooms[direction]
                if link is not False:
                    player.change_current_room(link)
        except KeyError:
            print("{0} does not have a {1} facing exit, remember to use your COMPASS!".format(current_room, direction))
    else:
        print("You must enter a direction")


def look(player, item, item_dict, rooms):
    current_room = player.Current_Room
    if look != "":
        if look == "COMPASS":
            connected_rooms = []
            if item_dict[item].held is True:
                connected_rooms.appened(rooms[current_room].linked_rooms)


def take(player, item, item_dict, rooms):
    current_room = player.Current_Room
    if item in rooms[current_room].room_items and item_dict[item].item_status == "Pickup":
        player.Inventory.append(item)
        rooms[current_room].room_items.remove(item)
        print(rooms[current_room].room_items)


def drop(player, item, item_dict, rooms):
    if item != "":
        current_room = player.Current_Room
        try:
            if item in player.Inventory:
                player.Inventory.remove(item)
                rooms[current_room].room_items.append(item)
            else:
                print("You are not holding {0}".format(item))
        except ValueError:
            print("{0} is not a valid item. Type 'Inventory' to check your held items".formtat(item))
    else:
        print("You must enter an item to drop")


def use(item):
    pass


def commands():
    print("""The command structure is: 'Command' 'Context' on the same line
    Sometimes the command will require extra context
    The list of commands are:
    'Go'   - This command followed by a direction will cause you to move to the room in that direction
    'Look' - If an item is specified you will look at the item, otherwise you will look around the room
    'Take' - Take an item from the room. If it cannot be picked up you will be notified
    'Drop' - Drop and item from your inventory on the ground in the room you are currently in
    'Use'  - Use the specified item. This command may require extra context, such as 'Use Wrench Throw'""")


def context():
    print(""""This contains all of the different context arguments
    Throw - Will throw an item in your inventory. Specifying an item in the room will throw the item at the specified item.
    """)


def list_of_items(item_dict):
    for i in item_dict:
        print(i)


def get_help_input(item_dict):
    user_input = " "
    while user_input != "":
        print("""The help menus are:
        'Commands' - Outputs the list of all commands
        'Context' - Outputs the list of all context actions
        'Items' - Outputs the list of all interactive items
        To return to the action menu, press enter with a clear entry""")
        user_input = input("> ").upper()
        if user_input == "COMMANDS":
            commands()
        elif user_input == "CONTEXT":
            context()
        elif user_input == "ITEMS":
            list_of_items(item_dict)


def get_user_input(player, item_dict, room_dict):
    user_input = 1
    while user_input != "QUIT":
        print("Enter next action")
        user_input = input("> ").upper()
        if user_input.startswith("GO"):
            user_input = user_input.replace("GO", "")
            user_input = user_input.strip()
            go(player, room_dict, user_input)
        elif user_input.startswith("LOOK"):
            user_input.replace("LOOK", "")
            user_input = user_input.strip()
            if len(user_input) > 1:
                look(player, user_input, item_dict, room_dict)
            else:
                look(user_input)
        elif user_input.startswith("TAKE"):
            user_input = user_input.replace("TAKE", "")
            user_input = user_input.strip()
            take(player, user_input, item_dict, room_dict)
        elif user_input.startswith("DROP"):
            user_input = user_input.replace("DROP", "")
            user_input = user_input.strip()
            drop(player, user_input, item_dict, room_dict)
        elif user_input == "INVENTORY":
            print(player.Inventory)
        elif user_input == "HELP":
            get_help_input(user_input)
        else:
            "Invalid input, type 'Help' to see a list of help menus"


# Code Start

item_dict = {}
room_dict = {}

player = Adventurer()
item_dict["SELF-LIGHTING CANDLE"] = Item("SELF-LIGHTING CANDLE", "While it may look like a regular candle, it actually "
                                                                 "has a self-lighting and self-extinguishing feature.",
                                         "Pickup")
item_dict["COMPASS"] = Item("COMPASS", "A COMPASS to help you find your way.", "Pickup")
item_dict["ELECTRIFIED LADDER"] = Item("ELECTRIFIED LADDER", "This LADDER glows and crackles, you probably shouldn't "
                                                             "touch it.", "Static")
item_dict["LADDER"] = Item("LADDER", "The LADDER is no longer glowing or crackling, it can climb it now", "Static")
item_dict["STORAGE WIRE"] = Item("STORAGE WIRE", "This wire is connected to the LADDER, it leads to the room to the "
                                                 "west.", "Static")

room_dict["Operating Theatre"] = Room("Operating Theatre", ["SELF-LIGHTING CANDLE", "COMPASS"],
                                      {"NORTH": "Generator Room", "EAST": "Workshop"})
room_dict["Storage Room"] = Room("Storage Room", ["ELECTRIFIED LADDER", "LADDER", "STORAGE WIRE"],
                                 {"SOUTH": "Workshop", "UP": "Lounge"})
room_dict["Generator Room"] = Room("Generator Room", [], {"SOUTH": "Operating Theatre"})
room_dict["Workshop"] = Room("Workshop", [], {"NORTH": "STORAGE Room", "WEST": "Operating Theatre"})
room_dict["Lounge"] = Room("Lounge", [], {"Down": "Storage Room"})
room_dict["Dining Room"] = Room(0, 0, 0)
room_dict["Kitchen"] = Room(0, 0, 0)
room_dict["Lobby"] = Room(0, 0, 0)
room_dict["Landing"] = Room(0, 0, 0)
room_dict["Boiler"] = Room(0, 0, 0)
room_dict["Bedroom"] = Room(0, 0, 0)
room_dict["Bathroom"] = Room(0, 0, 0)

print(room_dict["Generator Room"].room_name)

get_user_input(player, item_dict, room_dict)

