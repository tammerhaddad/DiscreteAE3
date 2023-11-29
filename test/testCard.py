from enum import Enum
from testSuit import Suit
class Card:
    def __init__(self, val, suit):
        self.val = val 
        self.suit = suit
    
    valToWord = {14: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def __str__(self):
        try:
            return self.valToWord[self.val] + " of " + self.suitToWord[self.suit.value]
        except:
            return str(self.val) + " of " + self.suit.value + "-"
        
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

    def sameSuit(self, other):
        return self.suit == other.suit
