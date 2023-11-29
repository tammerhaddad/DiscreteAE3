from testHand import Hand
import itertools
import random
import time
start = time.time()

deck = range(52)
hand = random.sample(deck, 2)
unknown = set(deck) - set(hand)
allHands = list(itertools.combinations(unknown, 5))
hands = [Hand(hand) for hand in allHands]
hands.sort()

print(f"{len(unknown)}, Time: {time.time()-start:.2f}")