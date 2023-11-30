from testDeck import Deck
from testHand import Hand
import itertools
import time
start = time.time()
def write(path, hands):
    with open(f"{path}", 'w') as file:
        for hand in hands:
            file.write(f"{hand}\n")

def ptime(prefix):
    global start
    print(f"{prefix} Time: {time.time()-start:.2f}s")
    start = time.time()

deck = Deck()
mixes = itertools.combinations(deck.cards, 5)
ptime("Calculate")
hands = [Hand(hand) for hand in mixes]
ptime("Convert")
write("sorted.txt", sorted(hands))
ptime("Write and Finish")