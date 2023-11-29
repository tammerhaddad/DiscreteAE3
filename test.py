from testHand import Hand
import itertools
import random
import time
start = time.time()

deck = range(50)
num = 5
handsAsList = itertools.combinations(deck, num)
hands = [Hand(hand) for hand in handsAsList]
hands.sort()


# for hand in hands:
#     print(hand)
print(f"Time: {time.time()-start:.2f}")