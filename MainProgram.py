from Adventurer import *
from Rooms import *
from Things import *

def go(direction=None):
    if direction is not None:
        for i in range(4):
            if direction == "N" or direction == "NORTH":
                Room.check_direction(direction)
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
    pass


def list_of_items(item_list):
    pass


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


def get_user_input():
    user_input = 1
    while user_input != "QUIT":
        print("Enter next action")
        user_input = input("> ").upper()
        if user_input.startswith("GO"):
            user_input.replace("GO", "")
            go(user_input)
        elif user_input.startswith("LOOK"):
            user_input.replace("LOOK", "")
            if user_input.len() > 1:
                look(user_input)
            else:
                look()
        elif user_input.startswith("TAKE"):
            user_input.replace("TAKE", "")
            take(user_input)
        elif user_input.startswith("DROP"):
            user_input.replace("DROP", "")
            drop(user_input)
        elif user_input == "HELP":
            get_help_input()
        else:
            "Invalid input, type 'Help' to see a list of help menus"


# Code Start

item_list = []
room_list = []

Candle = Item("Self-Lighting Candle", "While it may look like a regular candle, it actually has a self-lighting and"
                                      " self-extinguishing feature.", "Pickup")
item_list.append(Candle)
Compass = Item("Compass", "A compass to help you find your way.", "Pickup")
item_list.append(Compass)
Electrified_Ladder = Item("Electrified Ladder", "This ladder glows and crackles, you probably shouldn't touch it."
                          "Static")
item_list.append(Electrified_Ladder)
Ladder = Item("Ladder", "The ladder is no longer glowing or crackling, it can climb it now", "Static")
item_list.append(Ladder)
Storage_Wire = Item("Storage Wire", "This wire is connected to the ladder, it leads to the room to the west.", "Static")
item_list.append(Storage_Wire)

Operating_Theater = Room("Operating Theatre", "North, East", [Candle, Compass])
room_list.append(Operating_Theater)
Storage_Room = Room("Storage Room", "South, Up", [Electrified_Ladder, Ladder])
room_list.append(Storage_Room)
Generator_Room = Room("Generator Room", "West, North", [])
room_list.append(Generator_Room)
Workshop = Room("Workshop", "North, West", [])
Lounge = Room("Lounge", "South, West, Down", [])
room_list.append(Lounge)

get_user_input()




