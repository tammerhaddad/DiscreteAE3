import random
from cards import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards):
        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards
