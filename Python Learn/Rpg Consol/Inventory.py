from Stat import Stat
from Item import Item 

#same inventory for player and monster 
class Inventory:
    ...
    def __init__(self):
        #l'inventaire peux contenir des item sans contraitre il est infinie
        # pour ce qui est des object un seul emplacement d'arme
        # et 4 morceau d'armur, tete, torse, jambe, pied
        #l'inventaire contiendra aussi un item "Gold" qui permetra de faire des echange avec le marchand
                
        self.items = {}
        self.weapon = None
        self.armor = {"helmet" : None, "chestplate" : None, "leggings" : None, "boots" : None}
        
    def GetWeapon(self):
        #get l'arme unique de l'entitée
        self.weapon
        
    def GetArmor(self):
        # renvoie exemple {"chestplate": chestplateTest, etc et renvoie none comme valeur ci vide }
        return self.armor
        
    def GetItemQuantity(self, _item):
        #revoie l'item dans le dictionaire d'item avec ça quantité
        if _item in self.items:
            return self.items[_item]
        
        return 0
    
    def RemoveItem(self , _item, _nb = 0):
        if _item in self.items :
            self.items[_item] -= _nb
        
        if self.items[_item] <= 0:
            del self.items[_item]
        
        
    
    def AddItem(self, _item, _quantity):
        # ici nous pouron ajouter un item déja existant ou non a l'inventaire de l'entitée et ça quantité
        if _item in self.items:
            self.items[_item] += _quantity
        else:
            self.items[_item] = _quantity
            