import pygame

class Card:
    valToWord = {14: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def __init__(self, val, suit):
        self.value = val 
        self.suit = suit
        self.path = f'cards/{str(self.suit)[5:]}-{1 if self.value == 14 else self.value}.svg'
        self.image = pygame.image.load(self.path)

    def __str__(self):
        return f"{self.value}-{self.suit.value}"
        
    def __lt__(self, other):
        if(self.value == other.value):
            return self.suit.value < other.suit.value
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.value, self.suit))

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["image"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Add baz back since it doesn't exist in the pickle
        self.image = pygame.image.load(self.path)

    def scale(self, table_width):
        relative_width = float(table_width) * 0.058
        relative_height = float(relative_width) * 1.4
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (relative_width, relative_height))
