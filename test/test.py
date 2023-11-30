from testHand import Hand
from testDeck import Deck
from testCard import Card
import itertools
import random
import time
start = time.time()
player1 = Hand([Card(10,"HEART"), Card(10,"SPADE"), Card(10,"CLUB"), Card(11,"HEART"), Card(11,"CLUB")])
player2 = Hand([Card(12,"HEART"), Card(12,"SPADE"), Card(12,"CLUB"), Card(7,"HEART"), Card(8,"CLUB")])

print(type(player1.hand))
print(player2.rank)
print(player1.rank)

print(player1 == player2)

# makeThemHands = [Hand(hand) for hand in possibleHands]
# makeThemHands.sort()
# for a in unknown:
#     print(a)
# print(f"{len(unknown)}, Time: {time.time()-start:.2f}")