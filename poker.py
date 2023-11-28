from cards import Card
from deck import Deck
import pygame
from math import comb
from enum import Enum

class Poker:
    def __init__(self, numPlayers=2, omniscient = true):
        pygame.init()
        pygame.display.set_caption("Poker")
        self.deck = Deck()
        self.players = []
        self.table = []
        self.numPlayers = numPlayers
        self.omnicient = omniscient
        self.bounds = (1024, 768)
        self.window = pygame.display.set_mode(self.bounds)
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
        #print("Table:\n")
        #for card in self.table:
        #    print(card)
    

    def blindProb(self):
        blindDeck = [card for player in self.players[1:] for card in player] + self.deck.deck
        return len(blindDeck)
    
    def renderGame(self):
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                key = event.key
        
        self.window.fill((15,0,169))
        font = pygame.font.SysFont('comicsans', 60, True)

        for i in range(len(self.table)):
            self.window.blit(self.table[i].image, (10 + i * 10, 200))

        if (self.omnicient):
            for i in range(len(self.players)):
                text = font.render("Player " + i, True, (255,255,255))
                self.window.blit(text, (10 + i*10, 500))
                self.window.blit(self.players[i][0].image, (400, 200))
                self.window.blit(self.players[i][0].image, (400, 200))
        else:
            print()
