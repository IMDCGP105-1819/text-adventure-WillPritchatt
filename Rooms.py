class Room:

    def __init__(self, name, interactables, link):
        self.room_name = name
        self.room_items = interactables
        self.linked_rooms = link
        self.enter = False

    def check_direction(self, input_direction):
        for i in self.linked_rooms:
            if i in input_direction:
                link = self.linked_rooms[input_direction]
                return link
            else:
                return False

    def entered_room(self):
        pass
