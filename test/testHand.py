from collections import Counter

class Hand():
    def __init__(self, hand):
        self.hand = sorted(hand)
        self.rank = self.rank()

    def __lt__(self, other):
        if self.rank == other.rank:
            if self.rank == 8:
                return self.of_kind_lt(other, 4)
            elif self.rank == 7:
                return self.full_house_lt(other)
            elif self.rank == 4:
                return self.of_kind_lt(other, 3)
            elif self.rank in [3,2]:
                return self.of_kind_lt(other, 2)
            for i in range(len(self.hand)):
                if self.hand[i] != other.hand[i]:
                    return self.hand[i] < other.hand[i]
            return self.hand[0] < other.hand[0]
        return self.rank < other.rank
    
    def __eq__(self, other):
        if self.rank == other.rank:
            if self.rank == 8:
                return self.of_kind_equal(other, 4)
            elif self.rank == 7:
                return self.full_house_equal(other)
            elif self.rank == 4:
                return self.of_kind_equal(other, 3)
            elif self.rank in [3,2]:
                return self.of_kind_equal(other, 2)
            for i in range(len(self.hand)):
                if self.hand[i] != other.hand[i]:
                    return  False
            return True
        return self.rank == other.rank
    
    
    def full_house_lt(self, other):
        self_three_of_a_kind = max([card.value for card in self.hand if self.hand.count(card) == 3])
        other_three_of_a_kind = max([card.value for card in other.hand if other.hand.count(card) == 3])
        
        self_pair = max([card.value for card in self.hand if self.hand.count(card) == 2])
        other_pair = max([card.value for card in other.hand if other.hand.count(card) == 2])

        if self_three_of_a_kind == other_three_of_a_kind:
            return self_pair < other_pair
        return self_three_of_a_kind < other_three_of_a_kind

    def full_house_equal(self, other):
        self_tok = max([card.value for card in self.hand if self.hand.count(card) == 3])
        other_tok = max([card.value for card in other.hand if other.hand.count(card) == 3])
        
        self_pair = max([card.value for card in self.hand if self.hand.count(card) == 2])
        other_pair = max([card.value for card in other.hand if other.hand.count(card) == 2])

        return self_tok == other_tok and self_pair == other_pair
    
    def of_kind_lt(self, other, count):
        self_of_kind= [card.value for card in self.hand if self.hand.count(card) == count]
        other_of_kind = [card.value for card in other.hand if other.hand.count(card) == count]

        self_extra= [card.value for card in self.hand if self.hand.count(card) == 1]
        other_extra = [card.value for card in other.hand if other.hand.count(card) == 1]
        
        for i in range(len(self_of_kind)):
            if self_of_kind[i] != other_of_kind[i]:
                return self_of_kind[i] < other_of_kind[i]
        for i in range(len(self_extra)):
        for i in range(len(self_extra)):
            if self_extra[i] != other_extra[i]:
                return  self_extra[i] < other_extra[i]
        return False

        
    def of_kind_equal(self, other, count):
        self_of_kind= [card.value for card in self.hand if self.hand.count(card) == count]
        other_of_kind = [card.value for card in other.hand if other.hand.count(card) == count]
        self_extra= [card.value for card in self.hand if self.hand.count(card) == 1]
        other_extra = [card.value for card in other.hand if other.hand.count(card) == 1]
        for i in range(len(self_of_kind)):
            if self_of_kind[i] != other_of_kind[i]:
                return False
        for i in range(len(self_extra)):
            if self_extra[i] != other_extra[i]:
                return  False
        return True
    
    def __str__(self):
        return ', '.join(map(str, self.hand))

    def flush(self):
        return all(card.suit == self.hand[0].suit for card in self.hand)
    
    def straight(self):
        values = [card.value for card in self.hand]
        return values == list(range(min(values), max(values)+1))
    
    def of_a_kind(self, num):
        value_counts = Counter(card.value for card in self.hand)
        return num in value_counts.values()
    
    def two_pair(self):
        value_counts = Counter(card.value for card in self.hand)
        return list(value_counts.values()).count(2) == 2
    
    def full_house(self):
        return self.of_a_kind(3) and self.of_a_kind(2)
    
    def rank(self):
        rank = 1
        if self.flush() and self.straight():
            rank = 9
        elif self.of_a_kind(4):
            rank = 8
        elif self.full_house():
            rank = 7
        elif self.flush():
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
