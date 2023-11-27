class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    valToWord = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def __str__(self):
        try:
            return self.valToWord[self.value] + " of " + self.suitToWord[self.suit]
        except:
            return str(self.value) + " of " + self.suit
    
    def compare(self, other):
        if self.value == other.value:
            return 2
        return self.value > other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value