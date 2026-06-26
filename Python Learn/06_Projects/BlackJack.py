import random

def GetInt(_str, _min=1):
    while True:
        try:
            nb = int(input(_str))
            if nb >= _min:
                return nb
            else:
                print(f"Please Enter an int greater or equal to {_min}")
        except ValueError:
            print("Please enter an valid int")

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
    
    def __init__(self, _hand):
        self.card = []
        self.finishedTurn = False
        self.score = 0
        self.loose = False
        self.AddCard(_hand)
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card)      
        
    def DisplayHand(self):
        print("Player hands :")
        for card in self.card:
            print(card[1], card[0])
            
    def GetFinishedTurn(self):
        # print(self.finishedTurn)
        return self.finishedTurn
    
    def SetFinishedTurn(self, _bool):
        self.finishedTurn = _bool
    
    def PlayerChoice(self):
        while True:
            choice = input("Choose an action between : 'Hit' | 'Stand' | 'Double Down': ").strip().lower()
            
            if choice == "hit" or choice == "stand" or choice == "double down":
                return choice
            else:
                print("Please enter : 'Hit' or 'stand'")
    
    def SetScore(self, _nb):
        self.score = _nb
        
    def GetHand(self):
        return self.card
    
    def SetLoose(self, _bool):
        self.loose = _bool
    
    def GetLoose(self):
        return self.loose
        
class Dealer:
    
    def __init__(self, _hand):
        self.card = []
        self.AddCard(_hand)
        
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

def IsBlackJack(_deck):
    if CalculateScore(_deck) == 21:
        return True
    else:
        return False
    
# All player action is in this
def PlayerTurn(_player, _dealer, _deck):
    while not _player.GetFinishedTurn():
        print("Player turn :")
        _dealer.DisplayHand()
        _player.DisplayHand()
            
        score = CalculateScore(_player.GetHand())
        print(f"Player score = {score}")
        
        choice = _player.PlayerChoice()
      
        if choice == 'hit':
            _player.AddCard(Distribute(_deck))
            _player.SetFinishedTurn(False)
        elif choice == "double down":
            _player.AddCard(Distribute(_deck))
            _player.SetFinishedTurn(True)
        else:
            _player.SetFinishedTurn(True)
                    
        if CalculateScore(_player.GetHand()) > 21:
            print("Player Loose")
            _player.DisplayHand() 
            print(f"Player Score : {CalculateScore(_player.GetHand())}")
            _player.SetLoose(True)
            break

def DealerTurn(_dealer, _deck):
    while CalculateScore(_dealer.GetHand()) < 17:
        print("Dealer turn :")
        _dealer.DisplayHand(False)
        _dealer.AddCard(Distribute(_deck))         

def BlackJack(_player, _dealer):
    
    blackJack = False
    dealerWin = False
    playerWin = False
    
    if IsBlackJack(_player.GetHand()):
            if IsBlackJack(_dealer.GetHand()):
                print("Push, Dealer and Player have an black jack")
                blackJack = True
            else:
                print("Player have a black jack")
                blackJack = True
                playerWin = True
    elif IsBlackJack(_dealer.GetHand()):
                print("Dealer have a black jack")
                blackJack = True
                dealerWin = True
                
    return blackJack, dealerWin, playerWin

def PartiEnd(_player, _dealer):
    
    playerWin = False
    dealerWin = False
    
    if CalculateScore(_dealer.GetHand()) > 21:
        print("Player Win")
        playerWin = True
    elif CalculateScore(_player.GetHand()) > 21:
        print("Dealer Win")
        dealerWin = True
    else:
        if CalculateScore(_dealer.GetHand()) > CalculateScore(_player.GetHand()):
            print("Dealer Win")
            dealerWin = True
        elif CalculateScore(_dealer.GetHand()) < CalculateScore(_player.GetHand()):
            print("Player Win")
            playerWin = True
        else:
            print("Draw")
                
    _dealer.DisplayHand(False)
    print(f"Dealer Score : {CalculateScore(_dealer.GetHand())}")   
    _player.DisplayHand() 
    print(f"Player Score : {CalculateScore(_player.GetHand())}") 
    
    return playerWin, dealerWin
        
def main():
    
    inGame = True
    nbDeck = GetInt("How many deck you want ? ")
    deck = CreateDeck(nbDeck)
    random.shuffle(deck)
    
    while inGame:
    
        if len(deck) < int((52*nbDeck) * float(0.2)):
            deck = CreateDeck(nbDeck)
            random.shuffle(deck)
    
        player = Player(Distribute(deck , 2))
        dealer = Dealer(Distribute(deck , 2))
        
        blackJack, dealerWin, playerWin = BlackJack(player, dealer)
             
        if not blackJack:       
            PlayerTurn(player, dealer, deck)
                                         
            if not player.GetLoose():
                DealerTurn(dealer, deck)
        
        playerWin, dealerWin = PartiEnd(player, dealer)
        
        while True:
            choice = input("Do you want restart or quit ? 'r' for restart | 'q' for quit : ").strip().lower()
                
            if choice == 'r' or choice == 'q':
                break
            else :
                print("Please enter 'r' or 'q'")    
            
        # quit flag
        if choice == 'q':
            break
        
        

if __name__ == "__main__":
    main()