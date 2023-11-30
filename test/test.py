from testHand import Hand
from testDeck import Deck
from testCard import Card
import itertools
import random
import time
start = time.time()

player1 = Hand([Card(3,"HEART"), Card(3,"SPADE"), Card(3,"CLUB"), Card(5,"HEART"), Card(5,"CLUB")])
player2 = Hand([Card(3,"HEART"), Card(3,"SPADE"), Card(3,"CLUB"), Card(5,"HEART"), Card(5,"CLUB")])

print(type(player1.hand))
print(player2.rank)



print(player1 == player2)

# makeThemHands = [Hand(hand) for hand in possibleHands]
# makeThemHands.sort()
# for a in unknown:
#     print(a)
# print(f"{len(unknown)}, Time: {time.time()-start:.2f}")