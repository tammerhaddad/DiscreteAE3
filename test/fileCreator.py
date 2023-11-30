from testDeck import Deck
from testHand import Hand
import itertools
import time
import pickle

start = time.time()
def write(path, hands):
    with open(f"{path}", 'wb') as file:
        pickle.dump(hands, file, pickle.HIGHEST_PROTOCOL)

def ptime(prefix):
    global start
    print(f"{prefix} Time: {time.time()-start:.2f}s")
    start = time.time()

deck = Deck()
mixes = itertools.combinations(deck.cards, 5)
ptime("Calculate")

hands = [Hand(hand) for hand in mixes]
ptime("Convert")

hands.sort()
ptime("Sort")

write("sorted.pkl", hands)
ptime("Write and Finish")