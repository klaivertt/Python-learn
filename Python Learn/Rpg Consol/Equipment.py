from Stat import Stat
from Item import Item
from enum import Enum
from Stat import Stat
#equipment
#les equipement n'auront pour l'instant pas de fonctionalite passive mais uniquement des stat

class Equipement(Item):
    class Type(Enum):
        WEAPON = 0
        ARMOR = 1
    
    def __init__(self, _name="", _description="", _price=0, _stat = None):
        super().__init__(_name, _description, _price, Item.Type.EQUIPEMENT)
        self.type = None
        self.stat = _stat

class Weapon(Equipement):
    def __init__(self, _name="", _description="", _price=0):
        super().__init__(_name, _description, _price)
        self.Type = self.Type.WEAPON

class Armor(Equipement):
    class Part(Enum):
        HELMET = "helmet"
        CHESTPLATE = "chestplate"
        LEGGINGS = "leggings"
        BOOTS = "boots"
    
    def __init__(self, _name="", _description="", _price=0):
        super().__init__(_name, _description, _price)
        self.Type = self.Type.ARMOR