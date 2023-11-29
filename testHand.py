class Hand():
    def __init__(self, hand):
        self.hand = hand
    
    def __lt__(self, other):
        if sum(self.hand) == sum(other.hand):
            return max(self.hand) < max(other.hand)
        return sum(self.hand) < sum(other.hand)

    def __eq__(self, other):
        return sum(self.hand) == sum(other.hand)
    
    def __str__(self):
        return ', '.join(map(str, self.hand))
