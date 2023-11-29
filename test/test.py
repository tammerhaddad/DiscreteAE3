from testHand import Hand
from testDeck import Deck
import itertools
import random
import time
start = time.time()

deck = Deck()
numPlayers = 2
players = [deck.draw(2) for _ in range(numPlayers)]
table = deck.draw(5)
comb = table + players[0]
unknown = deck.cards + [card for sublist in players[1:] for card in sublist] + table
unknown.sort()
possibleHands = itertools.combinations(unknown, 5)
makeThemHands = [Hand(hand) for hand in possibleHands]
makeThemHands.sort()
length = len(makeThemHands)
print(f"Time: {time.time()-start:.2f}")
combs = [Hand(hand) for hand in itertools.combinations(comb, 5)]
# for a in combs:
#     print(a)
best = max(combs)
best_index = makeThemHands.index(best)
print(f"Best Hand: {best}, {best.rank}\nProb = {best_index/len(makeThemHands)}\nTime: {time.time()-start:.2f}")