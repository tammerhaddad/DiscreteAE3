from cards import Card
from deck import Deck
import itertools
from math import comb

deck = Deck()
players = []
numPlayers = 2
#numPlayers = int(input("How many players? : "))
for player in range(numPlayers): 
    deck.shuffle()
    players.append(deck.draw(2))

def printHands():
    for i in range(len(players)):
        print(f"\nPlayer {i+1}")
        for card in players[i]:
            print(card)

def printHand():
    print("Your Hand: ")
    for card in players[0]:
        print(card)

table = []

def dealTable(step):
    if step == 0:
        table.extend(deck.draw(3))
    else:
        table.extend(deck.draw())
        
    print("Table:\n")
    for card in table:
        print(card)

printHand()
for i in range(3):
    input("\nEnter to Continue.")
    dealTable(i)