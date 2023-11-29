from testHand import Hand
from testDeck import Deck
import itertools
import random
import time
start = time.time()

deck = Deck()
numPlayers = 2
hands = [deck.draw(2) for _ in range(numPlayers)]
unknown = [card for card in deck.cards if card not in hands[0]]

possibleHands = list(itertools.combinations(unknown, 5))

# makeThemHands = [Hand(hand) for hand in possibleHands]
# makeThemHands.sort()
for a in unknown:
    print(a)
print(f"{len(unknown)}, Time: {time.time()-start:.2f}")