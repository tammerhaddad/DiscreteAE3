from cards import Card
from deck import Deck
import itertools
from math import comb
class Poker:
    def __init__(self, numPlayers=2):
        self.deck = Deck()
        self.players = []
        self.numPlayers = numPlayers
        for player in range(self.numPlayers): 
            self.deck.shuffle()
            self.players.append(self.deck.draw(2))

    def printHands(self):
        for i in range(len(self.players)):
            print(f"\nPlayer {i+1}")
            for card in self.players[i]:
                print(card)

    def printHand(self):
        print("Your Hand: ")
        for card in self.players[0]:
            print(card)

    def dealTable(self, step):
        if step == 0:
            self.table.extend(self.deck.draw(3))
        else:
            self.table.extend(self.deck.draw())
            
        print("Table:\n")
        for card in self.table:
            print(card)

    def blindProb(self):
        blindDeck = [card for player in self.players[1:] for card in player] + self.deck.deck
        return len(blindDeck)
