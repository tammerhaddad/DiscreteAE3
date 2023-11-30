from testHand import Hand
from testDeck import Deck
import itertools
import time
import pickle
import numpy as np

start = time.time()
fullTime = time.time()
output = True

def ptime(prefix):
    global start
    global output
    if(output):
        print(f"{prefix} Time: {time.time()-start:.2f}s")
        start = time.time()

with open('sorted.pkl', 'rb') as file:
    allHands = pickle.load(file)
ptime("Read")
setHands = set(allHands)
ptime("toSet")
length = len(allHands)
numPlayers = 2
blankDeck = Deck()
def play():
    deck = Deck()
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = []
    for i in range(3):
        print(f"Prob: {prob(players, table)}")
        # input("enter for next")
        if i == 0:
            table += deck.draw(3)
        else:
            table += deck.draw()
        ptime("Step")
    print(f"Table: {list(map(str, table))}\nHands: {[f'{list(map(str, player))}' for player in players]}")


def win(players, table):
    bestHands = []
    for player in players:
        combs = itertools.combinations(player + table, 5)
        bestHands.append(max(map(Hand, combs)))
    return not bool(bestHands.index(max(bestHands)))


#------------------------------------------------------------------

def prob(players, table):
    setHands
    return

#------------------------------------------------------------------

ptime("Before")
play()
ptime("After")