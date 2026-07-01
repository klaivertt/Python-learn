from Player import Player
from Item import Item 
import Tools

class Game:
    def __init__(self):
        self.player = Player()
        self.items = {"Gold": Item("Gold", _itemType = Item.Type.MONEY)}
    def LoadPlayer(self):
        self.player.SetName()
        self.player.StatisticalDistribution(10)
        self.player.LoadGold(self.items["Gold"], 50)
        self.player.inventory.DispayItems()
        
    def Load(self):    
        self.LoadPlayer()
    
    def Run(self):
        Tools.ClearS()
        Tools.PrintTitle("Dungeon")
        self.Load()