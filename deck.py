import random
from cards import Card

class Deck:
    def __init__(self):
        self.deck = []
        for suit in ['HEART', 'DIAMOND', 'CLUB', 'SPADE']:
            for value in range(1, 14):
                self.deck.append(Card(suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)


    def draw(self, num = 1):
        drawn_cards = self.deck[:num]
        self.deck = self.deck[num:]
        return drawn_cards
    
    def __str__(self):
        deck = [f"{card}\n" for card in self.deck]
