import pygame

class Card:
    valToWord = {14: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def __init__(self, val, suit, back = False):
        self.value = val 
        self.suit = suit
        self.back = back
        self.path = f'cards/{str(self.suit)[5:]}-{1 if self.value == 14 else self.value}.svg'
        self.image = None
        # self.image = pygame.image.load('cards/BACK.png') if self.back else pygame.image.load(self.path)

    def __str__(self):
        return f"{self.value}-{self.suit.value}"
        
    def __lt__(self, other):
        if(self.value == other.value):
            return self.suit.value < other.suit.value
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.value, self.suit, self.back))

    def scale(self, table_width):
        relative_width = float(table_width) * 0.058
        relative_height = float(relative_width) * 1.4
        if self.back:
            self.image = pygame.image.load('cards/BACK.png')
        else:
            self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (relative_width, relative_height))
