from testHand import Hand
from testDeck import Deck
import itertools
import time
import pickle

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
length = len(allHands)
numPlayers = 2
deck = Deck()

def play():
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = []
    for i in range(4):
        # print(f"Prob = {prob(players, deck, table)/length}")
        print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}")
        input("enter for next")
        if i == 0:
            table += deck.draw(3)
        else:
            table += deck.draw()
    print(win(players, table))


def win(players, table):
    combs = [itertools.combinations(player + table, 5) for player in players]
    bestHand = max([Hand(list(comb)) for comb in combs])
    return bestHand
#------------------------------------------------------------------

play()




















