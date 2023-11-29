import pygame
from enum import Enum

class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3

class Card:
    def __init__(self, suit, value, back = False):
        self.suit = suit
        self.value = value
        self.back = back
        self.path = f'cards/{self.suit}-{self.value}.svg'
        self.image = pygame.image.load('cards/BACK.png') if self.back else pygame.image.load(self.path)

    valToWord = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
    suitToWord = {"S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

    def scale(self, table_width):
        relative_width = float(table_width) * 0.058
        relative_height = float(relative_width) * 1.4
        if self.back:
            self.image = pygame.image.load('cards/BACK.png')
        else:
            self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (relative_width, relative_height))

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