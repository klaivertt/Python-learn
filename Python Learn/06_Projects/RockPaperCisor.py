import csv
import random
from pathlib import Path


DATA_FILE = Path(__file__).with_name("RPC_Robot.csv")

class Player:
    
    def __init__(self):
        self.choice = ""
        
    
    def Choice(self):
        while True:
            self.choice = input("Choose between, 'Rock' | 'Paper' | 'Cisor' : ").strip().lower()
            
            if self.choice in ['rock', 'paper', 'cisor']:                
                break 
            else :
                print("Please enter an valid value between, 'Rock' | 'Paper' | 'Cisor' ")
        
    def GetChoice(self):
        return self.choice
    
class Robot:
    
    def __init__(self):
        self.choice = ""
        self.playerChoice = {"rock" : 1, "paper" : 1, "cisor" : 1}
        
        try:
            with open(DATA_FILE, "r") as file:
                read = csv.reader(file)
            
                for row in read:
                    self.playerChoice[row[0]] = int(row[1])
        except FileNotFoundError:
            pass
        
        
    
    def Choice(self):
        total = self.playerChoice["rock"] + self.playerChoice["paper"] + self.playerChoice["cisor"] 

        if total <= 3:
            self.choice = random.choice(["rock", "paper", "cisor"])
        else:
            weight = [self.playerChoice["cisor"] / total, self.playerChoice["rock"] / total, self.playerChoice["paper"] / total ]
            self.choice= random.choices(["rock", "paper", "cisor"], weights= weight)[0]
    
    def Analyse(self, _choice):
        self.playerChoice[_choice] += 1
        
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for line in self.playerChoice:
                writer.writerow([line, self.playerChoice[line]])
        
    def GetChoice(self):
        return self.choice
        
def isVictory(_choice1, _choice2):
    victory = False
    
    if _choice1 == "paper" and _choice2 == "cisor":
        print("Robot win")
        victory = True
    elif  _choice1 == "cisor" and _choice2 == "paper":
        print("Player win")
        victory = True
        
    elif _choice1 == "rock" and _choice2 == "paper":
        print("Robot Win")
        victory = True
    elif _choice1 == "paper" and _choice2 == "rock":
        print("Player Win")
        victory = True
        
    elif  _choice1 == "cisor" and _choice2 == "rock":
        print("Robot Win")
        victory = True
    elif  _choice1 == "rock" and _choice2 == "cisor":
        print("Player Win")
        victory = True
        
    else :
        print('Draw')
    
    return victory
    

def main():
    gameWin = False 
    
    player = Player() 
    robot =  Robot()
    
    nbRound = 0
    
    while not gameWin:
        player.Choice()
        robot.Choice()
        print(f"Player choice : {player.GetChoice()} , Robot choice : {robot.GetChoice()}")
        robot.Analyse(player.GetChoice())
        
        nbRound +=1
        
        gameWin = isVictory(player.GetChoice(), robot.GetChoice())
    
    print(f"Game finished in {nbRound} rounds")
          
        
        

if __name__ == "__main__":
    main()