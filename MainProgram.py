from Adventurer import *
from Rooms import *
from Things import *


def go(direction):
    for i in range(4):
        if direction == "N" or direction == "NORTH":
            Room.check_direction(direction)


def look(item = None):
    pass


def take(item):
    pass


def drop(item):
    pass


def use(item):
    pass


def get_user_input():
    user_input = input(">").upper()
    if "GO" in user_input:
        user_input.replace("GO", "")
        go(user_input)


# Code Start

get_user_input()

