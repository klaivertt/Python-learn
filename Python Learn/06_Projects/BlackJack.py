import random
import os


def ClearS():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def GetInt(_str, _min=1, _max=8):
    while True:
        try:
            nb = int(input(_str))
            if _min <= nb <= _max:
                return nb
            print(f"Please enter an int between {_min} and {_max}")
        except ValueError:
            print("Please enter a valid int")


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


class Hand:

    def __init__(self):
        self.cards = []
        self.bet = 0
        self.finished = False
        self.double_down = False
        self.bust = False

    def AddCards(self, _cards):
        for card in _cards:
            self.cards.append(card)

    def SetBet(self, _bet):
        self.bet = _bet

    def GetBet(self):
        return self.bet

    def DoubleBet(self):
        self.bet *= 2


class Player:

    def __init__(self, _cards):
        self.hands = [Hand()]
        self.finishedTurn = False
        self.money = 0
        self.loose = False
        self.hands[0].AddCards(_cards)

    def AddCard(self, _card, _hand=0):
        self.hands[_hand].AddCards(_card)

    def DisplayHand(self):
        print("\n" + "─" * 50)
        print("  🎮 PLAYER'S HAND")
        print("─" * 50)
        for i, hand in enumerate(self.hands, start=1):
            status = []
            if hand.finished:
                status.append("stand")
            if hand.double_down:
                status.append("double")
            if hand.bust:
                status.append("bust")
            suffix = f" ({', '.join(status)})" if status else ""
            print(f"Hand {i}{suffix}")
            for card in hand.cards:
                print(f"  {FormatCard(card)}")
            print(f"  Score: {CalculateScore(hand.cards)}")
            print()
        print("─" * 50)

    def GetFinishedTurn(self):
        return self.finishedTurn

    def SetFinishedTurn(self, _bool):
        self.finishedTurn = _bool

    def PlayerChoice(self, can_double=True, can_split=False):
        actions = ["[H]it", "[S]tand"]
        if can_double:
            actions.append("[D]ouble Down")
        if can_split:
            actions.append("S[P]lit")

        prompt = " | ".join(actions)

        while True:
            choice = input(f"\n  Choose an action:\n    {prompt}: ").strip().lower()

            if choice in ("h", "hit"):
                return "hit"
            if choice in ("s", "stand"):
                return "stand"
            if can_double and choice in ("d", "double", "double down"):
                return "double down"
            if can_split and choice in ("sp", "p", "split"):
                return "split"
            print("Please choose a valid action from the list.")

    def GetHands(self):
        return self.hands

    def GetHand(self):
        return self.hands[0]

    def ClearHand(self):
        self.hands = [Hand()]
        self.finishedTurn = False
        self.loose = False

    def SetLoose(self, _bool):
        self.loose = _bool

    def GetLoose(self):
        return self.loose

    def CanSplitHand(self, hand_index=0):
        if len(self.hands) > 1:
            return False

        hand = self.hands[hand_index]
        if len(hand.cards) != 2:
            return False

        return hand.cards[0][1] == hand.cards[1][1]

    def SplitHand(self, hand_index=0):
        hand = self.hands[hand_index]
        card1 = hand.cards[0]
        card2 = hand.cards[1]

        hand.cards = [card1]

        second_hand = Hand()
        second_hand.cards = [card2]
        second_hand.bet = hand.bet

        self.hands.insert(hand_index + 1, second_hand)


class Dealer:

    def __init__(self, _cards):
        self.hand = Hand()
        self.hand.AddCards(_cards)

    def AddCard(self, _cards):
        self.hand.AddCards(_cards)

    def GetHand(self):
        return self.hand

    def ClearHand(self):
        self.hand = Hand()

    def DisplayHand(self, _hide=True):
        print("\n" + "─" * 50)
        print("  🎰 DEALER'S HAND")
        print("─" * 50)
        for i, card in enumerate(self.hand.cards):
            if _hide and i == 1:
                print(f"  {'[HIDDEN]':>5}")
            else:
                print(f"  {FormatCard(card)}")
        print("─" * 50)


def CalculateScore(_cards):
    score = 0
    ace_count = 0

    for card in _cards:
        rank = card[1]
        score += CARD_VALUES[rank]
        if rank == "Ace":
            ace_count += 1

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score


# here _nb corresponds to number of decks in your game
def CreateDeck(_nb=1):
    suits = ["Heart", "Diamond", "Club", "Spade"]
    ranks = [
        "Ace",
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King"
    ]

    deck = []
    for _ in range(_nb):
        for suit in suits:
            for rank in ranks:
                deck.append((suit, rank))

    return deck


def Distribute(_deck, _nb=1):
    hand = []

    for _ in range(_nb):
        card = random.choice(_deck)
        _deck.remove(card)
        hand.append(card)

    return hand


def IsBlackJack(_cards):
    return len(_cards) == 2 and CalculateScore(_cards) == 21


def PlayerTurn(_player, _dealer, _deck):
    handIndex = 0

    while handIndex < len(_player.GetHands()):
        hand = _player.GetHands()[handIndex]

        if hand.finished or hand.bust:
            handIndex += 1
            continue

        print("\n" + "=" * 50)
        print(f"PLAYER'S TURN - HAND {handIndex + 1}".center(50))
        print("=" * 50)

        _dealer.DisplayHand()
        _player.DisplayHand()

        can_split = _player.CanSplitHand(handIndex)
        can_double = len(hand.cards) == 2 and not hand.double_down
        choice = _player.PlayerChoice(can_double=can_double, can_split=can_split)

        if choice == "hit":
            new_card = Distribute(_deck)
            _player.AddCard(new_card, handIndex)
            print(f"\n  ✓ You drew: {FormatCard(new_card[0])}")

            if CalculateScore(hand.cards) > 21:
                hand.bust = True
                hand.finished = True
                print(f"  ❌ Hand {handIndex + 1} BUST! Score: {CalculateScore(hand.cards)}")
            continue

        if choice == "double down":
            hand.DoubleBet()
            hand.double_down = True
            new_card = Distribute(_deck)
            _player.AddCard(new_card, handIndex)
            hand.finished = True
            print(f"\n  ✓ Double down: {FormatCard(new_card[0])}")

            if CalculateScore(hand.cards) > 21:
                hand.bust = True
                print(f"  ❌ Hand {handIndex + 1} BUST! Score: {CalculateScore(hand.cards)}")

            handIndex += 1
            continue

        if choice == "split":
            _player.SplitHand(handIndex)

            # After split, each hand receives one additional card.
            first_new = Distribute(_deck)
            second_new = Distribute(_deck)
            _player.AddCard(first_new, handIndex)
            _player.AddCard(second_new, handIndex + 1)

            print(f"\n  ✓ Split done on hand {handIndex + 1}")
            print(f"    Hand {handIndex + 1} gets: {FormatCard(first_new[0])}")
            print(f"    Hand {handIndex + 2} gets: {FormatCard(second_new[0])}")
            continue

        hand.finished = True
        print("\n  ✓ You stand!")
        handIndex += 1

    _player.SetFinishedTurn(True)

    if all(h.bust for h in _player.GetHands()):
        _player.SetLoose(True)


def DealerTurn(_dealer, _deck):
    print("\n" + "=" * 50)
    print("DEALER'S TURN".center(50))
    print("=" * 50)

    while CalculateScore(_dealer.GetHand().cards) < 17:
        print("\n  🎰 Dealer's score: " + str(CalculateScore(_dealer.GetHand().cards)))
        new_card = Distribute(_deck)
        _dealer.AddCard(new_card)
        print(f"  ✓ Dealer drew: {FormatCard(new_card[0])}")

    _dealer.DisplayHand(False)
    print(f"\n  💰 Dealer's final score: {CalculateScore(_dealer.GetHand().cards)}")


def BlackJack(_player, _dealer):
    player_cards = _player.GetHand().cards
    dealer_cards = _dealer.GetHand().cards

    blackJack = False
    dealerWin = False
    playerWin = False

    if IsBlackJack(player_cards):
        if IsBlackJack(dealer_cards):
            print("\n" + "🎉" * 25)
            print("  BLACKJACK! - Both have Blackjack!".center(50))
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
    elif IsBlackJack(dealer_cards):
        print("\n" + "😞" * 25)
        print("  DEALER'S BLACKJACK".center(50))
        print("😞" * 25)
        blackJack = True
        dealerWin = True

    return blackJack, dealerWin, playerWin


def PartiEnd(_player, _dealer):
    playerWin = False
    dealerWin = False

    dealer_score = CalculateScore(_dealer.GetHand().cards)

    print("\n" + "=" * 50)
    print("FINAL RESULT".center(50))
    print("=" * 50)

    _dealer.DisplayHand(False)
    print(f"  💰 Dealer's final score: {dealer_score}")

    _player.DisplayHand()

    print("\n" + "─" * 50)

    for i, hand in enumerate(_player.GetHands(), start=1):
        score = CalculateScore(hand.cards)

        if hand.bust:
            print(f"  Hand {i}: 😞 DEALER WINS! You went BUST!")
            dealerWin = True
            continue

        if dealer_score > 21:
            print(f"  Hand {i}: 🎉 PLAYER WINS! Dealer went BUST!")
            playerWin = True
            continue

        if score > dealer_score:
            print(f"  Hand {i}: 🎉 PLAYER WINS!")
            playerWin = True
        elif score < dealer_score:
            print(f"  Hand {i}: 😞 DEALER WINS!")
            dealerWin = True
        else:
            print(f"  Hand {i}: 🤝 IT'S A DRAW!")

    print("─" * 50 + "\n")

    return playerWin, dealerWin


def main():
    ClearS()
    PrintTitle("🎰 WELCOME TO BLACKJACK 🎰")

    inGame = True
    nbDeck = GetInt("How many decks do you want? (1-8): ", 1)
    deck = CreateDeck(nbDeck)
    random.shuffle(deck)

    player = Player(Distribute(deck, 2))
    dealer = Dealer(Distribute(deck, 2))

    gameCount = 0

    while inGame:
        gameCount += 1
        ClearS()
        PrintTitle(f"🎰 BLACKJACK - Game #{gameCount} 🎰")

        if len(deck) < int((52 * nbDeck) * 0.2):
            print("\n  🔄 Reshuffling deck...\n")
            deck = CreateDeck(nbDeck)
            random.shuffle(deck)

        if gameCount > 1:
            player.ClearHand()
            dealer.ClearHand()
            player.AddCard(Distribute(deck, 2))
            dealer.AddCard(Distribute(deck, 2))

        blackJack, dealerWin, playerWin = BlackJack(player, dealer)

        if not blackJack:
            PlayerTurn(player, dealer, deck)

            if not player.GetLoose():
                DealerTurn(dealer, deck)

        playerWin, dealerWin = PartiEnd(player, dealer)

        while True:
            choice = input("\n  Play another round? ('r' for restart | 'q' for quit): ").strip().lower()

            if choice in ('r', 'q'):
                break
            print("  ⚠️  Please enter 'r' or 'q'")

        if choice == 'q':
            print("\n" + "=" * 50)
            print("Thanks for playing! Goodbye!".center(50))
            print("=" * 50 + "\n")
            inGame = False


if __name__ == "__main__":
    main()
