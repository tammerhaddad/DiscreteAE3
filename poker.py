from card import Card
from deck import Deck
from player import Player
import pygame

# 6 player graphical max
class Poker:
    def __init__(self, numPlayers = 2 , blind = False):
        pygame.init()
        pygame.display.set_caption("Poker")
        self.players = []
        self.table = []
        self.blind = blind
        self.bounds = (1500, 750)
        self.window = pygame.display.set_mode(self.bounds, pygame.RESIZABLE)
        self.deck = Deck()
        for player in range(numPlayers): 
            self.deck.shuffle()
            self.players.append(Player(player, self.deck.draw(2)))

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
            offset = (screen_width - width) / 2
            wide = True
            self.window.blit(table, (offset, 0))
        else:
            width = screen_width 
            height = screen_width / 2
            table = pygame.transform.scale(pygame.image.load('table.png'), (width, height)) 
            offset = (screen_height - height) / 2
            self.window.blit(table, (0, offset))
            wide = False
        return (width, height, offset, wide)
    
    def pause(self):
        dimensions = self.renderBackground()
        for player in self.players:
            for card in player.hand:
                card.scale(dimensions[0])
        for card in self.table:
            card.scale(dimensions[0])
        self.renderGame()
        pygame.time.wait(500)

    def gameUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if self.blind:
                    self.players[0].blind_odds = self.blind_prob(0)
                return False
        return True
   
    def blind_prob(self, index):
        return 0
    
    def renderGame(self):
        cardSpacing = .0718
        tableOrigin = (.32786, .465573)
        playerOrigins = ((.19836, .760655), (.668852, .760655), (.19836, .06557), (.668852, .06557), (.434426, .760655), (.434426, .06557), (.137705, .36393), (.86393, .636065))

        width, height, offset, wide = self.renderBackground()
        blank = Card(1, 1, True)
        if wide:
            for i in range(len(self.table)):
                self.window.blit(self.table[i].image, (tableOrigin[0] * width + i * width * cardSpacing + offset, tableOrigin[1] * height))
            
            for i in range(len(self.players)):
                if i == 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(f"Probability: {self.players[i].blind_odds}", 1, (10, 10, 10))
                    text = pygame.transform.scale(text, (int(0.25 * height), int(0.05 * height)))  # Scale the text to 20% of the width and 5% of the height
                    self.window.blit(text, (playerOrigins[i][0] * width + offset, playerOrigins[i][1] * height - 0.05 * height))
                if i != 0 and self.blind:
                    self.window.blit(blank.image, (playerOrigins[i][0] * width + offset, playerOrigins[i][1] * height))
                    self.window.blit(blank.image, (playerOrigins[i][0] * width + cardSpacing * width + offset, playerOrigins[i][1] * height))
                else:
                    self.window.blit(self.players[i].hand[0].image, (playerOrigins[i][0] * width + offset, playerOrigins[i][1] * height))
                    self.window.blit(self.players[i].hand[1].image, (playerOrigins[i][0] * width + cardSpacing * width + offset, playerOrigins[i][1] * height))
        else:
            for i in range(len(self.table)):
                self.window.blit(self.table[i].image, (tableOrigin[0] * width + i * width * cardSpacing , tableOrigin[1] * height + offset))

            for i in range(len(self.players)):
                if i == 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(f"Probability: {self.players[i].blind_odds}", 1, (10, 10, 10))
                    text = pygame.transform.scale(text, (int(0.25 * height), int(0.05 * height)))  # Scale the text to 20% of the width and 5% of the height
                    self.window.blit(text, (playerOrigins[i][0] * width, playerOrigins[i][1] * height - 0.05 * height + offset))
                if i != 0 and self.blind:
                    self.window.blit(blank.image, (playerOrigins[i][0] * width, playerOrigins[i][1] * height + offset))
                    self.window.blit(blank.image, (playerOrigins[i][0] * width + cardSpacing * width, playerOrigins[i][1] * height + offset))
                else:
                    self.window.blit(self.players[i].hand[0].image, (playerOrigins[i][0] * width, playerOrigins[i][1] * height + offset))
                    self.window.blit(self.players[i].hand[1].image, (playerOrigins[i][0] * width + cardSpacing * width, playerOrigins[i][1] * height + offset))
        pygame.display.update()
