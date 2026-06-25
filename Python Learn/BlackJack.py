

# Tant que le joueur joue :
#     Afficher les mains
#     Demander Hit ou Stand

#     Si Hit :
#         Ajouter une carte

#     Si score > 21 :
#         Défaite
#         Fin

# Tour du croupier

# Tant que score croupier < 17 :
#     Piocher

# Comparer les scores

# Afficher le résultat

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
        self.finishedTurn = False
        self.score = 0
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card)      
        
    def DisplayHand(self):
        for card in self.card:
            print(card[1], card[0])
            
    def GetFinishedTurn(self):
        return self.finishedTurn
    
    def SetFinishedTurn(self, _bool):
        self.finishedTurn = _bool
    
    def PlayerChoice(self):
        while True:
            choice = input("Choose an action between : 'Hit' | 'Stand' : ")
    
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
            
        print(self.card) 

def CalculateScore(_cards):
    
    score = 0
    
    for card in _cards:
        score += CARD_VALUES[card[1]]
    
    if score > 21:
        if "Ace" in _cards:
            score -= 10
    
    return score
    
        
def CreateDeck():
    suits = ["Heart", "Diamond", "Club", "Spade"]

    ranks = [
        "Ace",
        "2", "3", "4", "5", "6", "7","8", "9", "10",
        "Jack", "Queen", "King"
    ]
    
    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append((suit,rank))
            # print(f"Card created : {rank} {suit}")
            
    return deck

def Distribute(_deck, _nb):
    
    hand = []
    
    for _ in range(_nb):
        card = random.choice(_deck)
        _deck.remove(card)
                
        hand.append(card)
        
    print(hand)
    return hand

def main():
    
    inGame = True
    while inGame:
        deck = CreateDeck()
        random.shuffle(deck)
    
        player = Player()
        player.AddCard(Distribute(deck , 2))
        
        dealer = Dealer()
        dealer.AddCard(Distribute(deck , 2))
        
        while not player.GetFinishedTurn():
            player.DisplayHand()
            score = CalculateScore(player.GetHand())
            print(f"Player score = {score}")
            player.SetFinishedTurn(True)
    
        break
        
        
        
    
    
    
    

if __name__ in "__main__":
    main()