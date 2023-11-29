from testHand import Hand
from testDeck import Deck
import itertools
import random
import time
start = time.time()

deck = Deck()
numPlayers = 2
hands = [deck.draw(2) for _ in range(numPlayers)]
table = deck.draw(5)
player1hand = hands[0] + table
unknown = [card for card in deck.cards if card not in player1hand]

opposingHands = list(itertools.combinations(unknown, 5))
player1Hands = [Hand(hand) for hand in list(itertools.combinations(player1hand, 5))]

# makeThemHands = [Hand(hand) for hand in possibleHands]
# makeThemHands.sort()
# for a in unknown:
#     print(a)
# print(f"{len(unknown)}, Time: {time.time()-start:.2f}")