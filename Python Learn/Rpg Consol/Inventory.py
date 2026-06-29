import Stat

#same inventory for player and monster 
class Inventory:
    ...
    def __init__(self):
        #l'inventaire peux contenir des item sans contraitre il est infinie
        # pour ce qui est des object un seul emplacement d'arme
        # et 4 morceau d'armur, tete, torse, jambe, pied
        #l'inventaire contiendra aussi un item "Gold" qui permetra de faire des echange avec le marchand
        self.weapon = None
    
    def CheckItemExists(self, _itemName):
        ...
        
    def GetWeapon(self):
        ...
        #get l'arme unique de l'entitée
        
    def GetArmor(self):
        # revoie un dictionaire des 4 amur combiner,
        # renvoie exemple {"chestplate": chestplateTest, etc et renvoie none comme valeur ci vide }
        ...
        
    def GetItem(self, _itemName):
        #revoie l'item dans le dictionaire d'item avec ça quantité
        ...
    
    def AddItem(self, _itemName, _quantity):
        ...
        # ici nous pouron ajouter un item déja existant ou non a l'inventaire de l'entitée et ça quantité