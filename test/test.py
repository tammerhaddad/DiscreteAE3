from testHand import Hand
from testDeck import Deck
from testCard import Card
import itertools
import time
start = time.time()
fullTime = time.time()
output = False

def stringToHand(str):
    return Hand([Card(int(a.split("-")[0]), a.split("-")[1]) for a in str.split(",")])

def ptime(prefix):
    global start
    global output
    if(output):
        print(f"{prefix} Time: {time.time()-start:.2f}s")
        start = time.time()

allHands = open('test/sorted.txt').read().splitlines()
ptime("Read")
numPlayers = 2

def calc():
    deck = Deck()
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = deck.draw(5)
    comb = table + players[0]
    ptime("Initialize")
    combs = [Hand(hand) for hand in itertools.combinations(comb, 5)]
    ptime("Hand Possibilities")
    best = max(combs)
    print(f"{best}, {best.strRank()}")
    return allHands.index(str(best))
# print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}\nBest Hand: {best}, {best.strRank()}\nProb = {best_index/len(allHands)}")
# print(f"Total Time: {time.time()-fullTime} seconds.")

for i in range(10):
    print(f"Prob = {calc()/len(allHands)}")