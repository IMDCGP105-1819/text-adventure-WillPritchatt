class Room:

    def __init__(self, name, directions, interactables, link):
        self.room_name = name
        self.room_directions = directions
        self.room_items = interactables
        self.linked_rooms = link

    def check_direction(self, input_direction):
        for i in self.room_directions:
            if i in input_direction:
                link = self.linked_rooms[input_direction]
                return link
            else:
                return False

    def entered_room(self):
        pass
