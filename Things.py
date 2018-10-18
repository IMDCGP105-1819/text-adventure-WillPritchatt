class Item:

    # status determines how the object can be interacted with (Solid, Decor, Pickup)
    # if an item is Solid, it does something when interacted with but cannot be added to the Adventurer inventory
    # if an item is Decor it simply exists and does nothing but set the scene
    # if an item is a Pickup it can be added to the inventory

    def __init__(self, name, description, status):
        item_name = name
        item_description = description
        item_status = status
