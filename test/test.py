from testHand import Hand
from testDeck import Deck
from testCard import Card
import itertools
import time
start = time.time()
fullTime = time.time()
def stringToHand(str):
    return Hand([Card(int(a.split("-")[0]), a.split("-")[1]) for a in str.split(",")])

def ptime(prefix):
    global start
    print(f"{prefix} Time: {time.time()-start:.2f}s")
    start = time.time()

deck = Deck()
numPlayers = 2
players = [deck.draw(2) for _ in range(numPlayers)]
table = deck.draw(5)
comb = table + players[0]
ptime("Initialize")
allHands = open('test/sorted.txt').read().splitlines()
ptime("Read")
combs = [Hand(hand) for hand in itertools.combinations(comb, 5)]
ptime("Hand Possibilities")
best = max(combs)
print(f"{best}, {best.strRank()}")
best_index = allHands.index(str(best))
print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}\nBest Hand: {best}, {best.strRank()}\nProb = {best_index/len(allHands)}")
print(f"Total Time: {time.time()-fullTime} seconds.")