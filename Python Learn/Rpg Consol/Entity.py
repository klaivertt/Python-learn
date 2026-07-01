from Stat import Stat
import Tools

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
        
    def AddBaseToStat(self):
        self.baseStat += self.statByLevel
               
    def UpdateStat(self):
        ...
        #prendre les stat de l'entier lier a sont level
        #ajouter les stat des armure et des arme
        #retourner les stat flat

    def GetStat(self):
        ...
        
    def IsDead(self):
        ...
    
