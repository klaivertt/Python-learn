from Player import Player
import Tools
class Game:
    def __init__(self):
        self.player = Player()
    
    def LoadPlayer(self):
        self.player.SetName()
        self.player.StatisticalDistribution(10)
        
        
    def Load(self):    
        self.LoadPlayer()
    
    def Run(self):
        Tools.ClearS()
        Tools.PrintTitle("Dungeon")
        self.Load()