class Room:
    def __init__(self, name, directions, interactables):
        self.room_name = name
        self.room_directions = directions
        self.room_items = interactables

    def check_direction(self, input_direction):
        for i in self.room_directions:
            if i in input_direction:
                return True
            else:
                return False
