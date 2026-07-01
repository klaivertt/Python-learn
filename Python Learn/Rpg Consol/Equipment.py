from Stat import Stat
from Item import Item
from enum import Enum
from Stat import Stat
#equipment
#les equipement n'auront pour l'instant pas de fonctionalite passive mais uniquement des stat

class Equipement(Item):
    class Type(Enum):
        WEAPON = "Weapon"
        ARMOR = "Armor"
    
    def __init__(self, _name="", _description="", _price=0, _stat = None):
        super().__init__(_name, _description, _price, Item.Type.EQUIPEMENT)
        self.equipementType = None
        
        if _stat is None:
            self.stat = Stat()
        elif isinstance(_stat, Stat):
            self.stat = _stat
        else:
            raise TypeError("stat doit être une instance de Stat")

class Weapon(Equipement):
    def __init__(self, _name="", _description="", _price=0, _stat = None):
        super().__init__(_name, _description, _price, _stat)
        self.equipementType = self.Type.WEAPON

class Armor(Equipement):
    class Part(Enum):
        HELMET = "Helmet"
        CHESTPLATE = "Chestplate"
        LEGGINGS = "Meggings"
        BOOTS = "Boots"
    
    def __init__(self, _name="", _description="", _price=0, _stat = None, _part = None):
        super().__init__(_name, _description, _price, _stat)
        self.equipementType = self.Type.ARMOR
        self.part = _part