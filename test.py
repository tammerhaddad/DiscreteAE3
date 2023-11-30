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
        print(f"Prob: {prob(players, table)}")
        # input("enter for next")
        if i == 1:
            table += deck.draw(3)
        elif i > 1:
            table += deck.draw()
        ptime("Step")
    print(f"Table: {list(map(str, table))}\nHands: {[f'{list(map(str, player))}' for player in players]}")


def win(players, table):
    bestHands = []
    for player in players:
        combs = itertools.combinations(player + table, 5)
        bestHands.append(max(map(Hand, combs)))
    return not bool(bestHands.index(max(bestHands)))

def bestHand(hands):
    return max(hands)
#------------------------------------------------------------------

def prob(players, table):
    # p1Hands = set(hand for hand in setHands if any(card in hand.hand for card in players[0]+table))
    unknown = set(blankDeck.cards) - set(players[0]) - set(table)
    possibleTables = set(itertools.combinations(unknown, 5 - len(table)))
    return Hand(list(max(possibleTables)))

#------------------------------------------------------------------

ptime("Before")
play()
ptime("After")