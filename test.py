from hand import Hand
from deck import Deck
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
setHands = set(allHands)
ptime("toSet")
length = len(allHands)
numPlayers = 2
blankDeck = Deck()

#------------------------------------------------------------

def play():
    deck = Deck()
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = []
    for i in range(4):
        # input("enter for next")
        if i == 1:
            table += deck.draw(3)
            
            print(f"Prob: {postFlop(players, table)}")
        elif i > 1:
            table += deck.draw()
            print(f"Prob: {postFlop(players, table)}")
        print(f"Table: {list(map(str, table))}\nHands: {[f'{list(map(str, player))}' for player in players]}")
        ptime("Step")

def bestHand(player, table):
    return max([Hand(hand) for hand in itertools.combinations(player+table, 5)])

#------------------------------------------------------------------

def postFlop(players, table):
    bHand = bestHand(players[0], table)
    return bHand


#------------------------------------------------------------------

ptime("Before")
play()
ptime("After")