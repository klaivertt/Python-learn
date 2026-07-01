import Tools

from Stat import Stat
from Inventory import Inventory
from Item import Item 
from Equipment import Equipement
from Equipment import Weapon
from Equipment import Armor

#Max value for rpg stat
MAX_STAT = 20
    

class Entity :
    def __init__(self):
        self.name = ""
        
        self.level = 1
        self.xp = 0
        #Base stat for the player link to Level
        self.baseStat = Stat()
        
        #Stat added by level
        self.statByLevel = Stat()
        #this stat are used to update stat level stat + item stat
        self.currentStat = Stat()
        self.maxHealth = self.currentStat.health
        self.health = self.maxHealth
        
        #Rpg stat
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.vitality = 0
        self.luck = 0
        
        self.inventory = Inventory()
        
               
    def UpdateStat(self):
        #prendre les stat de l'entier lier a sont level
        #ajouter les stat des armure et des arme
        #retourner les stat flat
        self.currentStat = self.baseStat
        
        if not self.inventory.weapon == None and isinstance(self.inventory.weapon, Weapon):
            self.currentStat += self.inventory.weapon.stat
        for armor in self.inventory.armor:
            if not armor == None and isinstance(armor, Armor):
                self.currentStat += self.inventory.armor[armor.value].stat
                
        self.maxHealth = self.currentStat.health
                    
    def IsDead(self):
        ...
    
