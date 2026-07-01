from enum import Enum

class Item:
    class Type(Enum):
        ITEM = 0
        WEAPON = 1
        ARMOR = 2
        MATERIAL = 3
        MONEY = 4
            
    def __init__(self, _name = "", _description = "", _price = 0,  itemType=Type.ITEM):
        self.name = _name
        self.description = _description
        self.price = _price
        self.type = itemType
        