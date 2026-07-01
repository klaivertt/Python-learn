from enum import Enum

class Item:
    class Type(Enum):
        ITEM = 0
        WEAPON = 1
        ARMOR = 2
        MATERIAL = 3
            
    def __init__(self, item_type=Type.ITEM):
        self.name = ""
        self.description = ""
        self.price = ""
        self.type = item_type
        