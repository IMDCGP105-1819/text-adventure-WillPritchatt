import sqlite3
"""    candle = Item("Candle", "A candle to light your way. It appears to have a mechanism to self-light and extinguish "
                            "itself", "Pickup")
    electrified_ladder = Item("Electrified Ladder", "An iron ladder that appears to be letting off a lot of heat. You "
                                                    "conclude that it has been electrified", "Solid")
    iron_ladder = Item("Iron Ladder", "An Iron ladder. It should allow you to reach the next floor", "Solid")"""


def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("drop table if exists {0}".format(table_name))
        cursor.execute(sql)
        db.commit()
    print("a")


def add_player_stats(db_name, values):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "insert into Player (CurrentHealth, CurrentStrength, CurrentArmour, CurrentMaxHealth," \
              "Level, Experience, Mana, MaxMana) values (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, values)
        db.commit()
    print("b")


def add_monster_stats(db_name, values):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "insert into Monster (CurrentHealth, CurrentStrength, CurrentArmour, CurrentMaxHealth," \
              "Level, Status, StatusCounter) values (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, values)
        db.commit()
    print("c")


db_name = "ItemRoom.db"
# Creating the Room Table
sql = """create table Room
        (RoomID integer
        RoomName string
        RoomDirections string
        RoomItems string
        primary key(RoomID))"""
create_table(db_name, "Room", sql)
# Creating the Item Table
sql = """create table Item
        (ItemID integer
        ItemName string
        ItemDesc string
        ItemStatus string
        primary key(ItemID))"""
create_table(db_name, "Item", sql)

