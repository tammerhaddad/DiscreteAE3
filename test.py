from hand import Hand
from deck import Deck
from bisect import bisect
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
    print(f"Players: {[list(map(str, player)) for player in players]}")
    print(f"Prob: {prob(players, table)}")
    # for i in range(4):
    #     # input("enter for next")
    #     if i == 1:
    #         table += deck.draw(3)
    #         print(f"Table: {list(map(str, table))}")
    #         print(f"Prob: {prob(players, table)}")
    #     elif i > 1:
    #         table += deck.draw()
    #         print(f"Table: {list(map(str, table))}")
    #         print(f"Prob: {prob(players, table)}")
    # print(f"Prob: {prob(players, table)}")
    # print(f"Table: {list(map(str, table))}\nHands: {[f'{list(map(str, player))}' for player in players]}")

def bestHand(player, table):
    return max(set(Hand(hand) for hand in itertools.combinations(player.union(table), 5)))

#------------------------------------------------------------------

def postFlop(players, table):
    unknown = set(blankDeck.cards) - set(players[0]) - set(table)
    tables = [table+list(hand) for hand in itertools.combinations(unknown, 5-len(table))]
    myHands = [bestHand(players[0], ptable) for ptable in tables]
    oppHands = [bestHand(players[1], ptable) for ptable in tables]
    return calculate_probability(myHands, oppHands)

def calculate_probability(list_a, list_b):
    total_pairs = len(list_a) * len(list_b)
    a_beats_b = sum(1 for item_a, item_b in itertools.product(list_a, list_b) if item_a > item_b)
    probability_a_beats_b = a_beats_b / total_pairs
    probability_b_beats_a = 1 - probability_a_beats_b

    return probability_a_beats_b, probability_b_beats_a

def prob(players, table):
    playerSets = [set(player) for player in players]
    tableCards = set(table)
    playerCards = set().union(*players)

    tableHands = [hand for hand in setHands if (not table or any(card in hand.hand for card in tableCards)) and not any(card in hand.hand for card in playerCards)]

    wins = [0] * len(players)
    numTableHands = len(tableHands)
    ptime("prep")
    for i in range(200000):
        bestHands = [bestHand(player, set(tableHands[i].hand)) for player in playerSets]
        wins[bestHands.index(max(bestHands))] += 1
    ptime("10k comps")
    probs = [win/200000 for win in wins]
    return probs

#------------------------------------------------------------------
# for _ in range(5):
ptime("Before")
play()
ptime("After")
print("--------------------------------------")



def preflop_prob(players):
    # remove cards from deck before
    allPlayersHands = [set(hand for hand in setHands if any(card in hand.hand for card in player)) for player in players]

    totalHands = set()
    for playerHands in allPlayersHands:
        totalHands = totalHands.union(playerHands)
    playerExcludedHands = [totalHands - player for player in allPlayersHands]

    listPlayerExcludedHands = [sorted(list(hands)) for hands in playerExcludedHands]
    probs = []
    for i in range(len(allPlayersHands)):
        playerSum = sum(bisect(listPlayerExcludedHands[i], hand) for hand in allPlayersHands[i])
        probs.append(playerSum/(len(allPlayersHands[i])*len(listPlayerExcludedHands[i])))

    return probs
