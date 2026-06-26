import random
import os

def ClearS():
    os.system('cls' if os.name == 'nt' else 'clear')

def PrintSeparator(char="=", length=50):
    print(char * length)

def PrintTitle(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50 + "\n")

def GetSuitSymbol(suit):
    symbols = {
        "Heart": "♥",
        "Diamond": "♦",
        "Club": "♣",
        "Spade": "♠"
    }
    return symbols.get(suit, suit)

def FormatCard(card):
    suit, rank = card
    symbol = GetSuitSymbol(suit)
    return f"{rank:>5} {symbol}"

def GetInt(_str, _min=1, _max = 8):
    while True:
        try:
            nb = int(input(_str))
            if _min <= nb <= _max:
                return nb
            else:
                print(f"Please Enter an int between {_min} and {_max}")
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
        self.money = 0
        self.bet = 0
        self.loose = False
        self.isSplit = False
        self.AddCard(_hand)
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card)      
        
    def DisplayHand(self):
        print("\n" + "─" * 50)
        print("  🎮 PLAYER'S HAND")
        print("─" * 50)
        if not self.isSplit:
            for card in self.card:
                print(f"  {FormatCard(card)}")
        else :
            print("Split 1")
            for card in self.card[0]:
                print(f"  {FormatCard(card)}")
            print()
            print("Split 2")
            for card in self.card[1]:
                print(f"  {FormatCard(card)}")
        print("─" * 50)
            
    def GetFinishedTurn(self):
        # print(self.finishedTurn)
        return self.finishedTurn
    
    def SetFinishedTurn(self, _bool):
        self.finishedTurn = _bool
    
    def PlayerChoice(self):
        while True:
            choice = input("\n  Choose an action:\n    [H]it | [S]tand | [D]ouble Down | [SP]lit:").strip().lower()
            
            if choice == "h" or choice == "hit":
                return "hit"
            elif choice == "s" or choice == "stand":
                return "stand"
            elif choice == "d" or choice == "double down":
                return "double down"
            elif choice == "sp" or choice == "split":
                return "split"
            # elif choice == "i" or choice == "insurance":
            #     return "insurance"
            else:
                print("Please enter: 'H' (Hit) | 'S' (Stand) | 'D' (Double Down) | 'S' Split | 'I' Insurance")
    
    def SetSplit(self, _bool):
        self.isSplit = _bool
    
    def GetSplit(self):
        return self.isSplit
    
    def SplitHand(self):
        self.card = [self.card[0], self.card[1]]      
        
    
    def SetScore(self, _nb):
        self.score = _nb
        
    def GetHand(self):
        return self.card
    
    def SetLoose(self, _bool):
        self.loose = _bool
    
    def GetLoose(self):
        return self.loose
    
    def SetBet(self, _bet):
        self.bet = _bet
    
    def GetBet(self):
        return self.bet

    def WinBet(self):
        self.money += self.bet

    def LoseBet(self):
        self.money -= self.bet
        
    def PushBet(self):
        self.bet = 0

    def DoubleBet(self):
        self.bet *= 2
        
class Dealer:
    
    def __init__(self, _hand):
        self.card = []
        self.AddCard(_hand)
        
    def AddCard(self, _card):
        
        for card in _card:
            self.card.append(card)
            
        # print(self.card) 
        
    def AddCard(self, _card, _splitNb):
        for card in _card:
            self.card[_splitNb - 1].append(card)
        
    def GetHand(self):
        return self.card
    
    def GetFirstCard(self):
        return self.card[0]
    
    def DisplayHand(self, _hide = True):
        print("\n" + "─" * 50)
        print("  🎰 DEALER'S HAND")
        print("─" * 50)
        for i, card in enumerate(self.card):
            if _hide and i > 0:
                print(f"  {'[HIDDEN]':>5}")
            else:
                print(f"  {FormatCard(card)}")
        print("─" * 50)

def CalculateScore(_cards):
    
    score = 0
    
    for card in _cards:
        score += CARD_VALUES[card[1]]
    
    aceCount = 0
    
    for card in _cards:
        if card == "Ace":
            aceCount += 1
                
    while score > 21 and aceCount > 0:
        score -= 10
        ace_count -= 1
    
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

def SameCardHand(_hand):
    tempCard = None
    
    for card in _hand:
        tempCard = card
        if card != tempCard:
            return False
    
    return True   
    
# All player action is in this
def PlayerTurn(_player, _dealer, _deck):
    while not _player.GetFinishedTurn():
        print("\n" + "=" * 50)
        print("PLAYER'S TURN".center(50))
        print("=" * 50)
        
        _dealer.DisplayHand()
        _player.DisplayHand()
                
        if not _player.GetSplit():
            print(f"\n  💰 Your score: {CalculateScore(_player.GetHand())}")
            print()
        else :
            print(f"\n  💰 Split 1 score: {CalculateScore(_player.GetHand()[0])}")
            print(f"\n  💰 Split 2  score: {CalculateScore(_player.GetHand()[1])}")
            print()
        
        choice = _player.PlayerChoice()
      
        if choice == 'hit':
            
            if not _player.GetSplit():
                newCard = Distribute(_deck)
                _player.AddCard(newCard)
                print(f"\n  ✓ You drew: {FormatCard(newCard[0])}")
                _player.SetFinishedTurn(False)
            else:
                newCard = Distribute(_deck)
                print(f"\n  ✓ You drew: {FormatCard(newCard[0])}")
                
                while True:
                    handNb = GetInt("Choose hand '1' or '2' : ")
                    
                    if handNb == 1 or handNb == 2:
                        break
                    else:
                        print("Please choice between '1' or '2'")
                if CalculateScore(_player.GetHand()[handNb - 1]) > 21:
                    print(f"You can add an card to this split score over 21, split score = {CalculateScore(_player.GetHand()[handNb - 1])}")
                else:
                    print(f"\n  ✓ You add in your split {handNb} : {FormatCard(newCard[0])}")
                
                _player.SetFinishedTurn(False)
        
        elif choice == "double down":
            if not _player.GetSplit():
                newCard = Distribute(_deck)
                _player.AddCard(newCard)
                print(f"\n  ✓ You doubled down and drew: {FormatCard(newCard[0])}")
                _player.SetFinishedTurn(True)
            else:
                print('You can make a double down on a split')
                _player.SetFinishedTurn(False)
        elif choice == "split":
            hand = _player.GetHand()
            if SameCardHand(hand) and not _player.GetSplit():
                _player.SetSplit(True)
                _player.SplitHand()
                print(f"\n  ✓ You split you hand in two: {FormatCard(hand[0])} and {FormatCard(hand[1])}")
            else:
                if _player.GetSplit():
                    print("You have allready split your hand")
                else:
                    print("You didn't have the same card in your hand")
        # elif choice == "insurance":
        #     ...
        else:
            print("\n  ✓ You stand!")
            _player.SetFinishedTurn(True)
        
        
        if not _player.GetSplit():       
            if CalculateScore(_player.GetHand()) > 21:
                print("\n" + "!" * 50)
                print("  ❌ BUST! Your score exceeded 21".center(50))
                print("!" * 50)
                _player.DisplayHand() 
                print(f"\n  💥 Your final score: {CalculateScore(_player.GetHand())}")
                _player.SetLoose(True)
                break
        else :
            if CalculateScore(_player.GetHand()[0]) > 21 and CalculateScore(_player.GetHand()[1]) > 21:
                print("\n" + "!" * 50)
                print("  ❌ BUST! Your score exceeded 21".center(50))
                print("!" * 50)
                _player.DisplayHand() 
                print(f"\n  💥 Your final score: {CalculateScore(_player.GetHand())}")
                _player.SetLoose(True)
                break
            elif CalculateScore(_player.GetHand()[0]) > 21:
                print("\n" + "!" * 50)
                print("  ❌ Split 1 BUST! Your score exceeded 21".center(50))
                print("!" * 50)
                _player.DisplayHand() 
                print(f"\n  💥 Your final score: {CalculateScore(_player.GetHand())}")
            
            elif CalculateScore(_player.GetHand()[1]) > 21:
                print("\n" + "!" * 50)
                print("  ❌ Split 2 BUST! Your score exceeded 21".center(50))
                print("!" * 50)
                _player.DisplayHand() 
                print(f"\n  💥 Your final score: {CalculateScore(_player.GetHand())}")
            

def DealerTurn(_dealer, _deck):
    print("\n" + "=" * 50)
    print("DEALER'S TURN".center(50))
    print("=" * 50)
    
    while CalculateScore(_dealer.GetHand()) < 17:
        print("\n  🎰 Dealer's score: " + str(CalculateScore(_dealer.GetHand())))
        newCard = Distribute(_deck)
        _dealer.AddCard(newCard)
        print(f"  ✓ Dealer drew: {FormatCard(newCard[0])}")
        
    _dealer.DisplayHand(False)
    print(f"\n  💰 Dealer's final score: {CalculateScore(_dealer.GetHand())}")         

def BlackJack(_player, _dealer):
    
    blackJack = False
    dealerWin = False
    playerWin = False
    
    if IsBlackJack(_player.GetHand()):
            if IsBlackJack(_dealer.GetHand()):
                print("\n" + "🎉" * 25)
                print("  BLACKJACK! - Both have BlackJack!".center(50))
                print("  IT'S A PUSH!".center(50))
                print("🎉" * 25)
                blackJack = True
            else:
                print("\n" + "🎉" * 25)
                print("  BLACKJACK!".center(50))
                print("  YOU WIN WITH BLACKJACK!".center(50))
                print("🎉" * 25)
                blackJack = True
                playerWin = True
    elif IsBlackJack(_dealer.GetHand()):
                print("\n" + "😞" * 25)
                print("  DEALER'S BLACKJACK".center(50))
                print("😞" * 25)
                blackJack = True
                dealerWin = True
                
    return blackJack, dealerWin, playerWin

def PartiEnd(_player, _dealer):
    
    playerWin = False
    dealerWin = False
    
    print("\n" + "=" * 50)
    print("FINAL RESULT".center(50))
    print("=" * 50)
    
    _dealer.DisplayHand(False)
    print(f"  💰 Dealer's final score: {CalculateScore(_dealer.GetHand())}")   
    
    _player.DisplayHand() 
    print(f"  💰 Your final score: {CalculateScore(_player.GetHand())}")
    
    print("\n" + "─" * 50)
    
    if CalculateScore(_dealer.GetHand()) > 21:
        print("  🎉 PLAYER WINS! Dealer went BUST!".center(50))
        playerWin = True
    elif CalculateScore(_player.GetHand()) > 21:
        print("  😞 DEALER WINS! You went BUST!".center(50))
        dealerWin = True
    else:
        if CalculateScore(_dealer.GetHand()) > CalculateScore(_player.GetHand()):
            print("  😞 DEALER WINS!".center(50))
            dealerWin = True
        elif CalculateScore(_dealer.GetHand()) < CalculateScore(_player.GetHand()):
            print("  🎉 PLAYER WINS!".center(50))
            playerWin = True
        else:
            print("  🤝 IT'S A DRAW!".center(50))
    
    print("─" * 50 + "\n")
    
    return playerWin, dealerWin
        
def main():
    
    ClearS()
    PrintTitle("🎰 WELCOME TO BLACKJACK 🎰")
    
    inGame = True
    nbDeck = GetInt("How many decks do you want? (1-8): ", 1)
    deck = CreateDeck(nbDeck)
    random.shuffle(deck)
    
    game_count = 0
    
    while inGame:
        game_count += 1
        ClearS()
        PrintTitle(f"🎰 BLACKJACK - Game #{game_count} 🎰")
    
        if len(deck) < int((52*nbDeck) * float(0.2)):
            print("\n  🔄 Reshuffling deck...\n")
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
            choice = input("\n  Play another round? ('r' for restart | 'q' for quit): ").strip().lower()
                
            if choice == 'r' or choice == 'q':
                break
            else:
                print("  ⚠️  Please enter 'r' or 'q'")    
            
        # quit flag
        if choice == 'q':
            print("\n" + "=" * 50)
            print("Thanks for playing! Goodbye!".center(50))
            print("=" * 50 + "\n")
            break
        
        

if __name__ == "__main__":
    main()