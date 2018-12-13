from Adventurer import *
from Rooms import *
from Things import *


def go(player, rooms, direction=None):
    current_room = player.Current_Room
    for i in rooms:
        if i.room_name == current_room:
            location = i
    if direction is not None:
        link = Room.check_direction(location, direction)
        if not link:
            player.change_current_room(link)
    else:
        print("You must enter a direction")


def look(item=None):
    pass


def take(item):
    pass


def drop(item):
    pass


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


def list_of_items(item_list):
    for i in item_list:
        print(i)


def get_help_input(item_list):
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
            list_of_items(item_list)


def get_user_input(player, item_list, room_list):
    user_input = 1
    while user_input != "QUIT":
        print("Enter next action")
        user_input = input("> ").upper()
        if user_input.startswith("GO"):
            user_input = user_input.replace("GO", "")
            go(player, room_list, user_input)
        elif user_input.startswith("LOOK"):
            user_input.replace("LOOK", "")
            if user_input.len() > 1:
                look(player, user_input)
            else:
                look()
        elif user_input.startswith("TAKE"):
            user_input.replace("TAKE", "")
            take(player, user_input)
        elif user_input.startswith("DROP"):
            user_input.replace("DROP", "")
        elif user_input == "HELP":
            get_help_input()
        else:
            "Invalid input, type 'Help' to see a list of help menus"


# Code Start

item_list = []
room_list = []

player = Adventurer()
item_list.append(Item("Self-Lighting Candle", "While it may look like a regular candle, it actually has a self-lighting"
                                              " and self-extinguishing feature.", "Pickup"))
item_list.append(Item("Compass", "A compass to help you find your way.", "Pickup"))
item_list.append(Item("Electrified Ladder", "This ladder glows and crackles, you probably shouldn't touch it.",
                      "Static"))
item_list.append(Item("Ladder", "The ladder is no longer glowing or crackling, it can climb it now", "Static"))
item_list.append(Item("Storage Wire", "This wire is connected to the ladder, it leads to the room to the west.",
                      "Static"))

room_list.append(Room("Operating Theatre", "NORTH, EAST", [item_list[0], item_list[1]], {"NORTH": "Generator Room",
                                                                                         "EAST": "Workshop"}))
room_list.append(Room("Storage Room", "SOUTH, UP", [item_list[2], item_list[3], item_list[4]], {"SOUTH": "Workshop",
                                                                                                "UP": "Lounge"}))
room_list.append(Room("Generator Room", "SOUTH", [], {"SOUTH": "Operating Theatre"}))
room_list.append(Room("Workshop", "NORTH, WEST", [], {"NORTH": "Storage Room", "WEST": "Operating Theatre"}))
room_list.append(Room("Lounge", "SOUTH, WEST, DOWN", [], {}))

get_user_input(player, item_list, room_list)




