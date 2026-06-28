import Stat
import Tools
        

class Player :
    def __init__(self):
        self.name = ""
        
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.stat = Stat()
        
        self.SetName()
            
    def SetName(self):
        while True:
            try:
                name = str(input("Enter your name").strip().title())
                break
            except ValueError:
                print("Please enter an valid string for your name")
        
        self.name = name
    
    def StatisticalDistribution():
        ...
        
        