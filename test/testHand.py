from collections import Counter

class Hand():
    def __init__(self, hand):
        self.hand = hand
        self.rank = self.rank()
    
    def strRank(self):
        return {
            10: "Royal Flush",
            9: "Straight Flush",
            8: "Four of a Kind",
            7: "Full House",
            6: "Flush",
            5: "Straight",
            4: "Three of a Kind",
            3: "Two Pair",
            2: "One Pair",
            1: "High Card"
        }[self.rank]
    
    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank
    
    def __str__(self):
        return ', '.join(map(str, self.hand))

    def flush(self):
        return all(card.suit == self.hand[0].suit for card in self.hand)
    
    def straight(self):
        values = sorted([card.val for card in self.hand])
        return values == list(range(min(values), max(values)+1)) or values == [14, 2, 3, 4, 5]
    
    def of_a_kind(self, num):
        value_counts = Counter(card.val for card in self.hand)
        return num in value_counts.values()
    
    def two_pair(self):
        value_counts = Counter(card.val for card in self.hand)
        return list(value_counts.values()).count(2) == 2
    
    def full_house(self):
        return self.of_a_kind(3) and self.two_pair()
    
    def rank(self):
        rank = 1
        if self.flush() and self.straight():
            rank = 10
        elif self.flush():
            rank = 9
        elif self.of_a_kind(4):
            rank = 8
        elif self.full_house():
            rank = 7
        elif self.flush():
            print(self)
            rank = 6
        elif self.straight():
            rank = 5
        elif self.of_a_kind(3):
            rank = 4
        elif self.two_pair():
            rank = 3
        elif self.of_a_kind(2):
            rank = 2
        else:
            rank = 1
        return rank
