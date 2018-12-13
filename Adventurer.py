from Things import *


class Adventurer:
    def __init__(self):
        self.Inventory = []
        self.Current_Room = "Operating Theatre"

    def change_current_room(self, link):
        self.Current_Room = link
        print(self.Current_Room)
