from Player import Player

class Game:
    def __init__(self):
        self.player = Player()
    
    def LoadPlayer(self):
        self.player.SetName()
        self.player.StatisticalDistribution()
        
        
    def Load(self):    
        self.LoadPlayer()
    
    def Run(self):
        self.Load()