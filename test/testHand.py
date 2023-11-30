from collections import Counter

class Hand():
    def __init__(self, hand):
        self.hand = sorted(hand,reverse=True)
        self.rank = self.rank()

    def strRank(self):
        return {
            1: "High Card",
            2: "One Pair",
            3: "Two Pair",
            4: "Three of a Kind",
            5: "Straight",
            6: "Flush",
            7: "Full House",
            8: "Four of a Kind",
            9: "Straight Flush",
            10: "Royal Flush"
        }[self.rank]

    def __lt__(self, other):
        if self.rank == other.rank:
            if self.rank == 8:
                return self.of_kind_lt(other, 4)
            elif self.rank == 7:
                return self.full_house_lt(other)
            elif self.rank in [5,9]:
                self_values = [card.value for card in self.hand]
                other_values = [card.value for card in other.hand]
                if 14 in self_values:
                    self_values.remove(14)
                    self_values.append(1)
                if 14 in other_values:
                    other_values.remove(14)
                    other_values.append(1)
                self_values.sort(reverse=True)
                other_values.sort(reverse=True)
                for self_val, other_val in zip(self_values, other_values):
                    if self_val != other_val:
                        return self_val < other_val
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
        # Get the values of the three of a kind and the pair for both hands
        self_three_of_kind = [value for value, count in Counter(card.value for card in self.hand).items() if count == 3]
        other_three_of_kind = [value for value, count in Counter(card.value for card in other.hand).items() if count == 3]
        self_pair = [value for value, count in Counter(card.value for card in self.hand).items() if count == 2]
        other_pair = [value for value, count in Counter(card.value for card in other.hand).items() if count == 2]

        # Compare the three of a kind first
        if self_three_of_kind[0] < other_three_of_kind[0]:
            return True
        elif self_three_of_kind[0] > other_three_of_kind[0]:
            return False
        # If the three of a kind are equal, compare the pair
        else:
            if self_pair[0] < other_pair[0]:
                return True
            else:
                return False

    def full_house_equal(self, other):
        # Get the values of the three of a kind and the pair for both hands
        self_three_of_kind = [value for value, count in Counter(card.value for card in self.hand).items() if count == 3]
        other_three_of_kind = [value for value, count in Counter(card.value for card in other.hand).items() if count == 3]
        self_pair = [value for value, count in Counter(card.value for card in self.hand).items() if count == 2]
        other_pair = [value for value, count in Counter(card.value for card in other.hand).items() if count == 2]

        # Compare the three of a kind first
        if self_three_of_kind[0] != other_three_of_kind[0]:
            return False
        # If the three of a kind are equal, compare the pair
        else:
            if self_pair[0] != other_pair[0]:
                return False
            else:
                return True

    def of_kind_lt(self, other, occurance):
        self_counts = Counter(card.value for card in self.hand)
        other_counts = Counter(card.value for card in other.hand)

        self_of_kind = [value for value, count in self_counts.items() if count == occurance]
        other_of_kind = [value for value, count in other_counts.items() if count == occurance]

        self_extra = [value for value, count in self_counts.items() if count == 1]
        other_extra = [value for value, count in other_counts.items() if count == 1]

        # Check "of a kind" cards first
        for self_val, other_val in zip(self_of_kind, other_of_kind):
            if self_val != other_val:
                return self_val < other_val

        # Then check extra cards
        for self_val, other_val in zip(self_extra, other_extra):
            if self_val != other_val:
                return self_val < other_val

        return False
            
    def of_kind_equal(self, other, count):
        self_counts = Counter(card.value for card in self.hand)
        other_counts = Counter(card.value for card in other.hand)
        
        for value, self_count in self_counts.items():
            if self_count != other_counts[value]:
                return False
        
        return True
    
    def __str__(self):
        return ','.join(map(str, self.hand)) + " " + self.strRank()

    def flush(self):
        return all(card.suit == self.hand[0].suit for card in self.hand)
    
    def straight(self):
        values = [card.value for card in self.hand]
        values.sort()
        if values == list(range(min(values), max(values)+1)):
            return True
        # Check for straight with Ace as 1
        elif values[0] == 2 and values[-1] == 14:
            values[-1] = 1
            values.sort()
            return values == list(range(min(values), max(values)+1))
        return False
    
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
    
