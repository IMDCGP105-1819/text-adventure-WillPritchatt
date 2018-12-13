from Adventurer import *
from Rooms import *
from Things import *


def go(player, rooms, direction=None):
    current_room = player.Current_Room
    if direction is not None:
        link = Room.check_direction(current_room, direction)
        if link is not False:
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
            user_input = user_input.replace("GO ", "")
            go(player, room_dict, user_input)
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

item_dict = {}
room_dict = {}

player = Adventurer()
item_dict["Self-Lighting Candle"] = Item("Self-Lighting Candle", "While it may look like a regular candle, it actually "
                                                                 "has a self-lighting and self-extinguishing feature.",
                                         "Pickup")
item_dict["Compass"] = Item("Compass", "A compass to help you find your way.", "Pickup")
item_dict["Electrified Ladder"] = Item("Electrified Ladder", "This ladder glows and crackles, you probably shouldn't "
                                                             "touch it.", "Static")
item_dict["Ladder"] = Item("Ladder", "The ladder is no longer glowing or crackling, it can climb it now", "Static")
item_dict["Storage Wire"] = Item("Storage Wire", "This wire is connected to the ladder, it leads to the room to the "
                                                 "west.", "Static")

room_dict["Operating Theatre"] = Room("Operating Theatre", ["Self-Lighting Candle", "Compass"],
                                      {"NORTH": "Generator Room", "EAST": "Workshop"})
room_dict["Storage Room"] = Room("Storage Room", ["Electrified Ladder", "Ladder", "Storage Wire"],
                                 {"SOUTH": "Workshop", "UP": "Lounge"})
room_dict["Generator Room"] = Room("Generator Room", [], {"SOUTH": "Operating Theatre"})
room_dict["Workshop"] = Room("Workshop", [], {"NORTH": "Storage Room", "WEST": "Operating Theatre"})
room_dict["Lounge"] = Room("Lounge", [], {"Down": "Storage Room"})

get_user_input(player, item_dict, room_dict)

