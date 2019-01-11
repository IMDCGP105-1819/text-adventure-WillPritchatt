class Room:

    def __init__(self, name, interactables, link, enter=False):
        self.room_name = name
        self.room_items = interactables
        self.linked_rooms = link
        self.enter = enter

