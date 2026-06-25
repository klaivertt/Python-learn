import random

CARD_VALUES = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

class Player:
    
    def __init__(self):
        self.card = []
        self.finishedTurn = True
        self.score = 0
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card)      
        
    def DisplayHand(self):
        print("Player hands :")
        for card in self.card:
            print(card[1], card[0])
            
    def GetFinishedTurn(self):
        print(self.finishedTurn)
        return self.finishedTurn
    
    def SetFinishedTurn(self, _bool):
        self.finishedTurn = _bool
    
    def PlayerChoice(self):
        while True:
            choice = input("Choose an action between : 'Hit' | 'Stand' : ").strip().lower()
            
            if choice == "hit" or choice == "stand":
                return choice
            else:
                print("Please enter : 'Hit' or 'stand'")
    
    def SetScore(self, _nb):
        self.score = _nb
        
    def GetHand(self):
        return self.card
        
class Dealer:
    
    def __init__(self):
        self.card = []
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card) 
        
    def GetHand(self):
        return self.card
    
    def DisplayHand(self, _hide = True):
        print("Dealer hands :")
        for card in self.card:
            print(card[1], card[0])
            if _hide:
                print("[/?]")
                break

def CalculateScore(_cards):
    
    score = 0
    
    for card in _cards:
        score += CARD_VALUES[card[1]]
    
    if score > 21:
        if "Ace" in _cards:
            score -= 10
    
    return score
    
# here _nb correspond to number of deck you want in your game
def CreateDeck(_nb = 1):
    suits = ["Heart", "Diamond", "Club", "Spade"]

    ranks = [
        "Ace",
        "2", "3", "4", "5", "6", "7","8", "9", "10",
        "Jack", "Queen", "King"
    ]
    
    deck = []
    
    for _ in range(_nb):    
        for suit in suits:
            for rank in ranks:
                deck.append((suit,rank))
                # print(f"Card created : {rank} {suit}")
                
    return deck

def Distribute(_deck, _nb = 1):
    
    hand = []
    
    for _ in range(_nb):
        card = random.choice(_deck)
        _deck.remove(card)
                
        hand.append(card)
        
    # print(hand)
    return hand

def main():
    
    inGame = True
    while inGame:
        deck = CreateDeck(6)
        random.shuffle(deck)
    
        player = Player()
        player.AddCard(Distribute(deck , 2))
        
        dealer = Dealer()
        dealer.AddCard(Distribute(deck , 2))
        
        playerLoose = False
        while player.GetFinishedTurn():
            print("Player turn :")
            dealer.DisplayHand()
            player.DisplayHand()
            score = CalculateScore(player.GetHand())
            print(f"Player score = {score}")
            if player.PlayerChoice() == 'hit':
                player.AddCard(Distribute(deck))
                player.SetFinishedTurn(True)
            else:
                player.SetFinishedTurn(False)
                
            if CalculateScore(player.GetHand()) > 21:
                print("Player Loose")
                player.DisplayHand() 
                print(f"Player Score : {CalculateScore(player.GetHand())}")
                playerLoose = True
                break
        
        if not playerLoose :
        
            while CalculateScore(dealer.GetHand()) < 17:
                print("Dealer turn :")
                dealer.DisplayHand(False)
                dealer.AddCard(Distribute(deck))

            
        
            
            if CalculateScore(dealer.GetHand()) > 21:
                print("Player Win")
            elif CalculateScore(player.GetHand()) > 21:
                print("Dealer Win")
            else:
                if CalculateScore(dealer.GetHand()) > CalculateScore(player.GetHand()):
                    print("Dealer Win")
                elif CalculateScore(dealer.GetHand()) < CalculateScore(player.GetHand()):
                    print("Player Win")
                else:
                    print("Draw")
                
            dealer.DisplayHand(False)
            print(f"Dealer Score : {CalculateScore(dealer.GetHand())}")   
            player.DisplayHand() 
            print(f"Player Score : {CalculateScore(player.GetHand())}")
            
            break
            while True:
                choice = input("Do you want restart or quit ? 'r' for restart | 'q' for quit : ").strip().lower()
                
                if choice == 'r' or choice == 'q':
                    break
                else :
                    print("Please enter 'r' or 'q'")
            
            # quit flag
            if choice == 'q':
                ...
        
        

if __name__ == "__main__":
    main()