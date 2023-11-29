class Card:
    def __init__(self, val, suit):
        self.val = val 
        self.suit = suit

    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

    def sameSuit(self, other):
        return self.suit == other.suit
