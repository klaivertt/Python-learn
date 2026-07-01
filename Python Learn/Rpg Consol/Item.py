from enum import Enum

class Item:
    class Type(Enum):
        ITEM = 0
        EQUIPEMENT = 1
        MATERIAL = 2
        MONEY = 3
            
    def __init__(self, _name = "", _description = "", _price = 0,  _itemType=Type.ITEM):
        self.name = _name
        self.description = _description
        self.price = _price
        self.type = _itemType
        
    # def __init__(self, _item):
    #     self.name = _item.name

