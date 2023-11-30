from enum import Enum
from testSuit import Suit

class Card:
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit
    
    valToWord = {14: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def __str__(self):
        return f"{self.value}-{self.suit.value}"
        
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value

    def sameSuit(self, other):
        return self.suit == other.suit
