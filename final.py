import random as rand
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (self.rank_list[self.rank] + " of " + self.suits[self.suit])
    def __eq__(self, other):
        return (self.rank == other.rank and self.suit == other.suit)
    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit and self.rank > other.rank:
            return True
        return False
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(i) + " " + i * " " + str(self.cards[i]) + "\n"
        return s
    def shuffle(self):
        n_cards = len(self.cards)
        for i in range (self.cards):
            j = rand.randrange(0, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def pop_card(self):
        return self.cards.pop()
    def is_empty(self):
        return len(self.cards) == 0
    def deal(self, hands, n_cards = 52):
        n_players = len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)
class Hand:
    def __init__(self, name = ""):
        self.cards = []
        self.name = name
    def add_card(self, card):
        self.cards.append(card)
    def __str__(self):
        s = self.name + "'s Hand"
        if self.is_empty():
            return s + " is empty"
        s += " contains \n" + Deck.__str__(self)
        return s
        