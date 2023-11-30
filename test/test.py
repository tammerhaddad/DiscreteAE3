from testHand import Hand
from testDeck import Deck
import itertools
import time
start = time.time()
fullTime = time.time()
output = True

def ptime(prefix):
    global start
    global output
    if(output):
        print(f"{prefix} Time: {time.time()-start:.2f}s")
        start = time.time()

allHands = open('sorted.txt').read().splitlines()
ptime("Read")
length = len(allHands)
numPlayers = 2

def calc(players, deck, table):
    known = table + players[0]
    unknown = deck.cards + [card for player in players[1:] for card in player]
    ptime("Initialize")
    ptime("Hand Possibilities")
    # print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}\nBest Hand: {best}, {best.strRank()}")
    return 0

deck = Deck()
players = [deck.draw(2) for _ in range(numPlayers)]
table = []

for i in range(4):
    # print(f"Prob = {calc(players, deck, table)/length}")
    print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}")
    input("enter for next")
    if i == 0:
        table += deck.draw(3)
    else:
        table += deck.draw()