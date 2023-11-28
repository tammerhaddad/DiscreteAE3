from cards import Card
from deck import Deck
import pygame
from math import comb
from enum import Enum
class Poker:
    def __init__(self, numPlayers=2, omniscient = True):
        pygame.init()
        pygame.display.set_caption("Poker")
        self.players = []
        self.table = []
        self.numPlayers = numPlayers
        self.omnicient = omniscient
        self.bounds = (1600, 1000)
        self.window = pygame.display.set_mode(self.bounds, pygame.RESIZABLE)
        self.deck = Deck(self.window)
        background_colour = (30, 92, 58)
        self.window.fill(background_colour)

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
    

    def blindProb(self):
        blindDeck = [card for player in self.players[1:] for card in player] + self.deck.deck
        return len(blindDeck)
    
    def quitGame(self):
        pygame.quit()
    
    def pause(self):
        pygame.time.wait(200)

    def gameUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                return False
        return True

    def renderGame(self):
        self.window.fill((30, 92, 58))
        font = pygame.font.SysFont('comicsans', 20, True)
        for i in range(len(self.table)):
            self.window.blit(self.table[i].image, (120 * i, 50))

        if (self.omnicient):
            for i in range(len(self.players)):
                text = font.render(f"Player {i + 1}", True, (255,255,255))
                self.window.blit(text, (i * 250 + 60, 250))
                self.window.blit(self.players[i][0].image, (250 * i, 300))
                self.window.blit(self.players[i][1].image, (250 * i + 110, 300))
        else:
            print()
        pygame.display.update()