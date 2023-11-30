from testHand import Hand
from testDeck import Deck
from testCard import Card
import itertools
import time
start = time.time()

def stringToHand(str):
    return [Card(a.split("-")[0], a.split("-")[1]) for a in str.split(",")]

deck = Deck()
numPlayers = 2
players = [deck.draw(2) for _ in range(numPlayers)]
table = deck.draw(5)
comb = table + players[0]
unknown = deck.cards + [card for sublist in players[1:] for card in sublist] + table
unknown.sort()
possibleHands = itertools.combinations(Deck().cards, 5)
makeThemHands = [Hand(hand) for hand in possibleHands]
makeThemHands.sort()

print(f"Time: {time.time()-start:.2f}")
with open('allHands.txt', 'w') as file:
    for hand in makeThemHands:
        file.write(','.join(f"{card.val}-{card.suit.value}" for card in hand.hand) + '\n')

length = len(makeThemHands)
combs = [Hand(hand) for hand in itertools.combinations(comb, 5)]
# for a in combs:
#     print(a)
best = max(combs)
best_index = makeThemHands.index(best)
print(f"Table: {list(map(str, table))}\nHand: {list(map(str, players[0]))}\nBest Hand: {best}, {best.strRank()}\nProb = {best_index/len(makeThemHands)}\nTime: {time.time()-start:.2f}")
