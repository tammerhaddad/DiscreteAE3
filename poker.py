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
        self.bounds = (1500, 750)
        self.window = pygame.display.set_mode(self.bounds, pygame.RESIZABLE)
        self.deck = Deck(self.renderBackground())
        for player in range(self.numPlayers): 
            self.deck.shuffle()
            self.players.append(self.deck.draw(2))

    def dealTable(self, step):
        if step == 0:
            self.table.extend(self.deck.draw(3))
        else:
            self.table.extend(self.deck.draw())

    def renderBackground(self):
        self.window.fill((40, 40, 43))
        screen_width, screen_height = self.window.get_size()
        if screen_width / screen_height  > 2:
            width = screen_height * 2 
            height = screen_height
            table = pygame.transform.scale(pygame.image.load('table.png'), (width, height)) 
            self.window.blit(table, ((screen_width - width) / 2, 0))
        else:
            width = screen_width 
            height = screen_width / 2
            table = pygame.transform.scale(pygame.image.load('table.png'), (width, height)) 
            self.window.blit(table, (0, (screen_height - height) / 2))
        return width

    def blindProb(self):
        blindDeck = [card for player in self.players[1:] for card in player] + self.deck.deck
        return len(blindDeck)
    
    def quitGame(self):
        pygame.quit()
    
    def pause(self):
        width = self.renderBackground()
        for cards in self.players:
            for card in cards:
                card.scale(width)
        for card in self.table:
            card.scale(width)
        self.renderGame()
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
        for i in range(len(self.table)):
            self.window.blit(self.table[i].image, (120 * i, 50))

        if (self.omnicient):
            for i in range(len(self.players)):
                self.window.blit(self.players[i][0].image, (250 * i, 300))
                self.window.blit(self.players[i][1].image, (250 * i + 110, 300))
        else:
            print()
        pygame.display.update()