from deck import Deck
from hand import Hand
import itertools
import time
import pickle


start = time.time()
def write(path, hands):
    sortedHands = sorted(hands)
    ptime("Sort")
    with open(f"{path}.txt", 'wb') as file:
        file.write('\n'.join(str(hand) for hand in sortedHands).encode())
        ptime("Write txt")
    with open(f"{path}set.pkl", 'wb') as file:
        pickle.dump(hands, file, pickle.HIGHEST_PROTOCOL)
        ptime("Write pkl")
    with open(f"{path}.pkl", 'wb') as file:
        pickle.dump(sortedHands, file, pickle.HIGHEST_PROTOCOL)
        ptime("Write sortedpkl")


def ptime(prefix):
    global start
    print(f"{prefix} Time: {time.time()-start:.2f}s")
    start = time.time()

deck = Deck()
mixes = itertools.combinations(deck.cards, 5)
ptime("Calculate")

hands = set(Hand(hand) for hand in mixes)
ptime("Convert")

write("sorted", hands)
ptime("Finish")
