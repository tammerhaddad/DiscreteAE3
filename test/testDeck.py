from testCard import Card
from testSuit import Suit

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in range(1, 13):
                self.cards.append(Card(value, suit))

    def draw(self, num):
        drawn = self.cards[:num]
        self.cards = self.cards[num:]
        return drawn
