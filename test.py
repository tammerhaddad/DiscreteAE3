from hand import Hand
from deck import Deck
from card import Card
import itertools
import time
start = time.time()
fullTime = time.time()
output = True

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
length = len(allHands)
numPlayers = 2

def calc():
    deck = Deck()
    players = [deck.draw(2) for _ in range(numPlayers)]
    table = deck.draw(5)
    comb = table + players[0]
    unknown = deck.cards + [card for player in players[1:] for card in player]
    ptime("Initialize")
    oppHands = [Hand(hand) for hand in itertools.combinations(unknown, 2)]
    combs = [Hand(hand) for hand in itertools.combinations(comb, 5)]
    ptime("Hand Possibilities")
    best = max(combs)
    print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}\nBest Hand: {best}, {best.strRank()}")
    return allHands.index(str(best))
# print(f"Total Time: {time.time()-fullTime} seconds.")

print(f"Prob = {calc()/length}")
