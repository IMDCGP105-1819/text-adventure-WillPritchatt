from Adventurer import *
from Rooms import *
from Things import *


def go(player, item_dict, rooms, direction):
    if direction != "":
        current_room = player.Current_Room
        try:
            if rooms[current_room].linked_rooms[direction] is not False:
                link = rooms[current_room].linked_rooms[direction]
                if link is not False:
                    if item_dict["GENERATOR"].item_status == "Used":
                        if link == ("Operating Theatre" or link == "Generator Room" or link == "Workshop" or link ==
                                    "Storage Room") and item_dict["CANDLE"].extra_status == "Unlit":
                            print("You cannot see where to go, turn on your candle (Hint: Use Candle)")
                        elif link == "Lounge":
                            player.change_current_room(link)
                            first_time_entry(link, rooms)
                        elif link == "Bedroom":
                            if item_dict["CANDLE"].extra_status == "Unlit":
                                player.change_current_room(link)
                                first_time_entry(link, rooms)
                            else:
                                print("If you have your candle on, you'll wake your kidnapper!")
                        elif link == "Bathroom":
                            if item_dict["BOILER"].extra_status == "Unstable":
                                print("In the next room you can hear an explosion and the sounds of footsteps."
                                      " Your kidnapper is awake and you can now grab the key")
                                item_dict["BOILER"].extra_status = "Destroyed"
                                item_dict["KIDNAPPER"].extra_status = "Awake"
                                player.change_current_room(link)
                                first_time_entry(link, rooms)
                            else:
                                player.change_current_room(link)
                                first_time_entry(link, rooms)
                        else:
                            player.change_current_room(link)
                            first_time_entry(link, rooms)
                    elif link == "Lounge":
                        print("You think about climbing the ladder, but decide that using it while glowing is a bad idea")
                    else:
                        player.change_current_room(link)
                        first_time_entry(link, rooms)
        except KeyError:
            print("{0} does not have a {1} facing exit, remember to use your Compass!".format(current_room, direction))
    else:
        print("You must enter a direction")


def first_time_entry(current_room, rooms):
    if rooms[current_room].enter is False:
        rooms[current_room].enter = True
        if current_room == "Generator Room":
            print("This room contains a generator and many wires, perhaps turning off the generator could help you.")
        elif current_room == "Workshop":
            print("It would seem your kidnapper sees themselves as quite the engineer, and looking at the some of the "
                  "contraptions in here you have a sinking feeling you're not their first victim.")
        elif current_room == "Storage Room":
            print("In the centre of this room is a ladder, and in the corners are various robot-like contraptions "
                  "which you're almost certain are staring at you")
        elif current_room == "Lounge":
            print("The trapdoor opens to some kind of lounge. Looking out the windows you can see that it is night.")
        elif current_room == "Dining Room":
            print("A simple dining room, everyone needs somewhere to eat, even kidnappers")
        elif current_room == "Lobby":
            print("The entrance to the house and also your exit")
        elif current_room == "Kitchen":
            print("Food is prepared here, at least you think so")
        elif current_room == "Landing":
            print("The hallway of the upstairs")
        elif current_room == "Boiler Room":
            print("It contains a boiler, maybe this could help you out")
        elif current_room == "Bedroom":
            print("You kidnapper is asleep, or maybe they're not. You'll want to be quiet in here and hope they don't "
                  "find you")
        elif current_room == "Bathroom":
            print("Contains a shower, a toilet and a sink. There's really not much in here")


def look(player, item, item_dict, rooms):
    current_room = player.Current_Room
    if item != "":
        if item == "COMPASS" and "COMPASS" in player.Inventory:
            if len(rooms[current_room].linked_rooms) >= 2:
                print("The directions you can travel are:", end=" ")
                for i in rooms[current_room].linked_rooms:
                    print(i, end=", ")
                print("")
            else:
                print("The direction you can travel in is:", end=" ")
                for i in rooms[current_room].linked_rooms:
                    print(i)
        else:
            if item in rooms[current_room].linked_rooms:
                print("In the", item, "is the", rooms[current_room].linked_rooms[item])
            else:
                if item == "LADDER" and item_dict["GENERATOR"].item_status != "Used":
                    print("This Ladder glows and crackles, you probably shouldn't touch it.")
                elif item in rooms[current_room].room_items or item in player.Inventory:
                    print(item_dict[item].item_description)
                else:
                    print("That is not a valid item to look at")
    else:
        if len(rooms[current_room].room_items) > 0:
            print("You are in the", current_room, end=". Inside the room is a ")
            for i in rooms[current_room].room_items:
                if item_dict[i].item_status == "Used":
                    pass
                else:
                    print(i, end=", ")
            print("")
        else:
            print("You are in the", current_room, ". There is nothing of interest in here")


def take(player, item, item_dict, rooms):
    current_room = player.Current_Room
    if item != "":
        if item in rooms[current_room].room_items:
            if item_dict[item].item_status == "Pickup":
                if item == "KEY" and item_dict["KIDNAPPER"].extra_status == "Asleep":
                    print("You cannot take the key yet, your kidnapper could be woken")
                else:
                    player.Inventory.append(item)
                    rooms[current_room].room_items.remove(item)
                    print("You add a", player.Inventory[-1], "to your inventory")
            else:
                print("You cannot take this item")
        else:
            print("This item is not in this room")
    else:
        print("You must specify an item to take")


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
            print("{0} is not a valid item. Type 'Inventory' to check your held items".format(item))
    else:
        print("You must enter an item to drop")


def use(player, item, item_dict, rooms):
    clear = False
    current_room = player.Current_Room
    if item != "":
        if item in player.Inventory:
            if item == "COMPASS":
                if len(rooms[current_room].linked_rooms) >= 2:
                    print("The directions you can travel are:", end=" ")
                    for i in rooms[current_room].linked_rooms:
                        print(i, end=", ")
                    print("")
                else:
                    print("The direction you can travel in is:", end=" ")
                    for i in rooms[current_room].linked_rooms:
                        print(i)
            elif item == "WRENCH":
                print("Specify an item to use the wrench on")
                prompt = input("> ").upper()
                if prompt in rooms[current_room].room_items:
                    if prompt == "GENERATOR" and "CANDLE" in player.Inventory:
                        print("You throw the Wrench at the generator, turning it off. However this also turns off the "
                              "lights")
                        item_dict["GENERATOR"].item_status = "Used"
                    elif prompt == "GENERATOR" and "CANDLE" not in player.Inventory:
                        print("You think about throwing the wrench at the generator, but then realise you won't be "
                              "able to see, you need to find a candle")
                    elif prompt == "BOILER":
                        print("Using the wrench you turn the valve of the boiler, it now has nowhere to vent excess"
                              " steam to")
                        item_dict[prompt].extra_status = "Unstable"
                    else:
                        print("You hit it with the wrench, but nothing happens")
                else:
                    print("This item is not in this room")
            elif item == "KEY":
                print("Specify an item to use the key on")
                prompt = input("> ").upper()
                if prompt in rooms[current_room].room_items:
                    if prompt == "LOBBY DOOR":
                        print("You have escaped, Congratulations!")
                        clear = True
                    else:
                        print("You cannot use the key on this item")
                else:
                    print("Item is not in this room")
            elif item == "CANDLE":
                if item_dict[item].extra_status == "Unlit":
                    print("You light the candle")
                    item_dict[item].extra_status = "Lit"
                elif item_dict[item].extra_status == "Lit":
                    print("You extinguish the candle")
                    item_dict[item].extra_status = "Unlit"
            else:
                print("You cannot use this item")
        elif item in rooms[current_room].room_items:
            if item == "LADDER" and item_dict["GENERATOR"].item_status != "Used":
                print("You think about climbing the ladder, but decide that using it while glowing is a bad idea")
            elif item == "LADDER" and item_dict["GENERATOR"].item_status == "Used":
                print("You climb the ladder and open a trapdoor")
                go(player, item_dict, rooms, "UP")
            elif item == "STAIRS":
                print("You climb the stairs and reach the landing")
                go(player, item_dict, rooms, "UP")
            elif item == "LOBBY DOOR" and "KEY" in player.Inventory:
                print("You have escaped, Congratulations!")
                clear = True
            elif item == "LOBBY DOOR" and "Key" not in player.Inventory:
                print("The door is locked shut, there must be a key to open it")
            else:
                print("You cannot use this item")
        elif item == "DOOR":
            print("Did you mean Lobby Door?")
        else:
            print("This item is not in the room, or in your inventory")
    else:
        print("You must specify an item to use")

    if clear is not True:
        return False
    else:
        return True


def commands():
    print("""The command structure is: 'Command' 'Context' on the same line
    Sometimes the command will require extra context
    The list of commands are:
    'Go'   - This command followed by a direction will cause you to move to the room in that direction
    'Look' - If an item is specified you will look at the item, otherwise you will look around the room
    'Take' - Take an item from the room. If it cannot be picked up you will be notified
    'Drop' - Drop and item from your inventory on the ground in the room you are currently in
    'Use'  - Use the specified item. This command may prompt you for an item to use as context""")


def list_of_items(item_dict):
    print("All ingame items are: ")
    for i in item_dict:
        print(i)


def get_help_input(item_dict):
    user_input = " "
    while user_input != "":
        print("""The help menus are:
        'Commands' - Outputs the list of all commands
        'Items' - Outputs the list of all interactive items
        To return to the action menu, press enter with a clear entry""")
        user_input = input("> ").upper()
        if user_input == "COMMANDS":
            commands()
        elif user_input == "ITEMS":
            list_of_items(item_dict)


def get_user_input(player, item_dict, room_dict):
    user_input = 1
    game_clear = False
    while user_input != "QUIT" and not game_clear:
        print("Enter next action")
        user_input = input("> ").upper()
        if user_input.startswith("GO"):
            user_input = user_input.replace("GO", "")
            user_input = user_input.strip()
            go(player, item_dict, room_dict, user_input)
        elif user_input.startswith("LOOK"):
            user_input = user_input.replace("LOOK", "")
            user_input = user_input.strip()
            look(player, user_input, item_dict, room_dict)
        elif user_input.startswith("TAKE"):
            user_input = user_input.replace("TAKE", "")
            user_input = user_input.strip()
            take(player, user_input, item_dict, room_dict)
        elif user_input.startswith("DROP"):
            user_input = user_input.replace("DROP", "")
            user_input = user_input.strip()
            drop(player, user_input, item_dict, room_dict)
        elif user_input.startswith("USE"):
            user_input = user_input.replace("USE", "")
            user_input = user_input.strip()
            game_clear = use(player, user_input, item_dict, room_dict)
        elif user_input == "INVENTORY":
            print(player.Inventory)
        elif user_input == "HELP":
            get_help_input(item_dict)
        elif user_input == "QUIT":
            print()
        else:
            print("Invalid input, type 'Help' to see a list of help menus")
    print("Thanks for playing!")


# Code Start
player = Adventurer()

item_dict = {}
room_dict = {}

item_dict["CANDLE"] = Item("CANDLE", "While it may look like a regular candle, it actually has a self-lighting and "
                                     "self-extinguishing feature.", "Pickup", "Unlit")
item_dict["COMPASS"] = Item("COMPASS", "A Compass to help you find your way.", "Pickup")
item_dict["LADDER"] = Item("LADDER", "The Ladder is no longer glowing or crackling, it can be climbed it now", "Static")
item_dict["STORAGE WIRE"] = Item("STORAGE WIRE", "This wire is connected to the Ladder, it leads to the room to the "
                                                 "west.", "Static")
item_dict["GENERATOR WIRE"] = Item("GENERATOR WIRE", "This wire is comes out from under a wall to the east. It is "
                                                     "connected to the generator", "Static")
item_dict["WRENCH"] = Item("WRENCH", "This tool is often used to fix a lot of mechanical problems.", "Pickup")
item_dict["GENERATOR"] = Item("GENERATOR", "This Steam-powered generator is providing power to the whole house",
                              "Static")
item_dict["BOILER"] = Item("BOILER", "This contraption is used to heat the house, if you tried maybe you could cause it"
                                     " to overheat and explode", "Static", "Stable")
item_dict["KEY"] = Item("KEY", "This is literally the key to your escape, take it to the lobby and leave!", "Pickup")
item_dict["LOBBY DOOR"] = Item("LOBBY DOOR", "This is the only way out of the house, but its locked. If only you could"
                                             " find a key", "Static")
item_dict["STAIRS"] = Item("STAIRS", "These stairs will take you to the top floor, but be careful, your kidnapper is"
                                     " sleeping up there and you don't want to wake them", "Static")
item_dict["KIDNAPPER"] = Item("KIDNAPPER", "Some very quick close inspection reveals this is not a person, it's a "
                                           "creature. Even attempting to kill it could be too dangerous, you should try"
                                           " to distract it", "Static", "Asleep")

room_dict["Operating Theatre"] = Room("Operating Theatre", ["CANDLE", "COMPASS"],
                                      {"NORTH": "Generator Room", "EAST": "Workshop"}, True)
room_dict["Storage Room"] = Room("Storage Room", ["LADDER", "STORAGE WIRE"],
                                 {"SOUTH": "Workshop", "UP": "Lounge"})
room_dict["Generator Room"] = Room("Generator Room", ["GENERATOR", "GENERATOR WIRE"], {"SOUTH": "Operating Theatre"})
room_dict["Workshop"] = Room("Workshop", ["WRENCH"], {"NORTH": "Storage Room", "WEST": "Operating Theatre"})
room_dict["Lounge"] = Room("Lounge", [], {"DOWN": "Storage Room", "SOUTH": "Lobby", "WEST": "Dining Room"})
room_dict["Dining Room"] = Room("Dining Room", [], {"EAST": "Lounge", "SOUTH": "Kitchen"})
room_dict["Kitchen"] = Room("Kitchen", [], {"EAST": "Lobby", "NORTH": "Dining Room"})
room_dict["Lobby"] = Room("Lobby", ["STAIRS", "LOBBY DOOR"], {"UP": "Landing", "WEST": "Kitchen", "NORTH": "Lounge"})
room_dict["Landing"] = Room("Landing", [], {"DOWN": "Lobby", "NORTH": "Boiler", "WEST": "Bedroom"})
room_dict["Boiler"] = Room("Boiler", ["BOILER"], {"SOUTH": "Landing"})
room_dict["Bedroom"] = Room("Bedroom", ["KEY", "KIDNAPPER"], {"NORTH": "Bathroom", "EAST": "Landing"})
room_dict["Bathroom"] = Room("Bathroom", [], {"SOUTH": "Bedroom"})

print("You wake up laying on some kind of table. Above you is a dim light. On a table next to you is your Compass and "
      "your Candle. You've been kidnapped and now you must find your way out.")

get_user_input(player, item_dict, room_dict)

