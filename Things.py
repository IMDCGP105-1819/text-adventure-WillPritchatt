class Item:

    # status determines how the object can be interacted with (Solid, Decor, Pickup, Used)
    # if an item is Solid, it does something when interacted with but cannot be added to the Adventurer inventory
    # if an item is a Pickup it can be added to the inventory
    # if an item is Used if it can no longer be interacted with

    def __init__(self, name, description, status, extra=False):
        self.item_name = name
        self.item_description = description
        self.item_status = status
        self.extra_status = extra
