from card import Card
from suit import Suit
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in range(13):
                self.cards.append(Card(value+2, suit))
        self.shuffle()

    def draw(self, num = 1):
        drawn = self.cards[:num]
        self.cards = self.cards[num:]
        return drawn
    
    def shuffle(self):
        random.shuffle(self.cards)
