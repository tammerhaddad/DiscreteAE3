from hand import Hand
from deck import Deck
import itertools
import time
import pickle
from bisect import bisect

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
    setHands = pickle.load(file)
ptime("Read")
length = len(setHands)
numPlayers = 3
blankDeck = Deck()

#------------------------------------------------------------

def play():
    deck = Deck()
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = []
    probs = [1/numPlayers]*numPlayers
    for i in range(4):
        stepTime = time.time()
        # input("enter for next")
        if i == 1:
            table += deck.draw(3)
            probs = postFlop(players, table, deck)
        elif i > 1:
            table += deck.draw()
            probs = postFlop(players, table, deck)
        else:
            # probs = preFlop(players)
            # probs = postFlop(players, table, deck)
            pass
        print(f"Prob: {probs}")
        if output: print(f"STEPTIME: {time.time()-stepTime}")
    print(f"Table: {list(map(str, table))}\nHands: {[f'{list(map(str, player))}' for player in players]}")

# gets the best hand given player and a table (the table must have at least 3 cards in it)
def bestHand(player, table):
    return max([Hand(hand) for hand in itertools.combinations(player+table, 5)])

# returns the index in players of the player that won
def winner(players, table):
    bHands = [bestHand(player, table) for player in players]
    return bHands.index(max(bHands))


#------------------------------------------------------------------
# FAILED PREFLOP CALCULATOR

def preFlopProb(a, b):
    wins = 0
    for hand_a in a:
        wins += bisect(b, hand_a)
    return wins / (len(a) * len(b))

def preFlop(players):
    allPlayerCards = set(itertools.chain(*players))
    playerHands = [[hand for hand in allHands if any(card in hand for card in player) and not any(card in hand for card in allPlayerCards.difference(player))] for player in players]
    ptime("players")
    allHands = {tuple(hand) for player in playerHands for hand in player}
    oppHands = [sorted(allHands - set(tuple(hand) for hand in player)) for player in playerHands]
    ptime("opps")
    zipped = zip(playerHands, oppHands)
    ratings = [preFlopProb(player, opp) for player, opp in zipped]
    ptime("ratings")
    return ratings

#----------------------------------------------------------
# Prob Calculator (can be used for preflop but would take 1439 times longer than post flop, 20 minutes on my computer)

def postFlop(players, table, deck):
    unknown = set(deck.cards)
    ptables = [table+list(adds) for adds in itertools.combinations(unknown, 5-len(table))]
    # pHands = [[bestHand(player, ptable) for ptable in tables] for player in players]
    ptime("ptables")
    winners = [winner(players, ptable) for ptable in ptables]
    return [winners.count(i)/len(winners) for i in range(len(players))]

#------------------------------------------------------------------
for _ in range(1):
    t = time.time()
    play()
    print(f"{time.time()-t:.2f}s ----------------------------")