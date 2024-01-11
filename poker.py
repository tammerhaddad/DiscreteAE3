from card import Card
from deck import Deck
from hand import Hand
from player import Player
import pygame
import itertools
import pickle

# 6 player graphical max
class Poker:
    def __init__(self, numPlayers = 2):
        pygame.init()
        pygame.display.set_caption("Poker")
        self.players = []
        self.table = []
        self.bounds = (1500, 750)
        self.window = pygame.display.set_mode(self.bounds, pygame.RESIZABLE)
        self.deck = Deck()
        for player in range(min(numPlayers,6)):
            playerOrigins = ((.19836, .760655), (.668852, .760655), (.19836, .06557), (.668852, .06557), (.434426, .760655), (.434426, .06557), (.137705, .36393), (.86393, .636065))
            self.deck.shuffle()
            self.players.append(Player(player, self.deck.draw(2), playerOrigins[player]))
        self.history = []

    def save(self):
        self.history += [[str(card) for card in self.table]]
        self.history += [[[str(card) for card in player.hand] for player in self.players]]
        with open("history.txt", "w") as file:
            file.write(str(self.history + [[str(card) for card in self.table]]))
        with open("history.pkl", "wb") as file:
            pickle.dump(self.history, file, pickle.HIGHEST_PROTOCOL)
        for step in self.history:
            print([str(item) for item in step])
    
    def dealTable(self, step):
        if step == 0:
            self.table.extend(self.deck.draw(3))
        else:
            self.table.extend(self.deck.draw())

    def get_sorted_hands(self):
        with open("sorted.pkl", "rb") as file:
            hands = pickle.load(file)

    def pause(self):
        self.render()
        pygame.time.wait(500)

    def gameUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                return False
        return True
    
    def render(self):
        cardSpacing = .0718
        tableOrigin = (.32786, .465573)

        self.window.fill((40, 40, 43))
        screen_width, screen_height = self.window.get_size()
        wide = screen_width / screen_height > 2
        width = screen_height * 2 if wide else screen_width
        height = screen_height if wide else screen_width / 2
        table = pygame.transform.scale(pygame.image.load('table.png'), (width, height)) 
        offset = (screen_width - width) / 2 if wide else (screen_height - height) / 2

        self.window.blit(table, (offset, 0) if wide else (0, offset))

        for player in self.players:
            for card in player.hand:
                card.scale(width)
        for card in self.table:
            card.scale(width)

        for i in range(len(self.table)):
            self.window.blit(self.table[i].image, (tableOrigin[0] * width + i * width * cardSpacing + offset if wide else tableOrigin[0] * width + i * width * cardSpacing, tableOrigin[1] * height + 0 if wide else tableOrigin[1] * height + offset))
        
        for i, player in enumerate(self.players):
            font = pygame.font.Font(None, 36)
            text = font.render(f"Probability: {player.prob:.2f}", 1, (10, 10, 10))
            text = pygame.transform.scale(text, (int(0.25 * height), int(0.05 * height))) 
            self.window.blit(text, (player.origin[0] * width + (offset if wide else 0), player.origin[1] * height - 0.05 * height + (0 if wide else offset)))
            self.window.blit(player.hand[0].image, (player.origin[0] * width + offset if wide else player.origin[0] * width, player.origin[1] * height + 0 if wide else player.origin[1] * height + offset))
            self.window.blit(player.hand[1].image, (player.origin[0] * width + cardSpacing * width + offset if wide else player.origin[0] * width + cardSpacing * width, player.origin[1] * height + 0 if wide else player.origin[1] * height + offset))

        pygame.display.update()