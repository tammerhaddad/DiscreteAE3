from testHand import Hand
import itertools
import random
import time
start = time.time()

deck = range(50)
allHands = itertools.combinations(deck, 5)
hands = [Hand(hand) for hand in allHands]
hands.sort()


print(f"Time: {time.time()-start:.2f}")