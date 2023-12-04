import itertools
import time
from bisect import bisect 

output = True
start = time.time()
def ptime(prefix):
    global start
    global output
    if(output):
        print(f"{prefix} Time: {time.time()-start:.2f}s")
        start = time.time()

cards = sorted(range(52))
setHands = {set(comb) for comb in itertools.combinations(cards, 5)}
hands = sorted(setHands)
ptime("hands")

def preFlopProb(a, b):
    wins = 0
    for hand_a in a:
        wins += bisect(b, hand_a)
    return wins / (len(a) * len(b))

def preFlop(players):
    allPlayerCards = set(itertools.chain(*players))
    playerHands = [[hand for hand in hands if any(card in hand for card in player) and not any(card in hand for card in allPlayerCards.difference(player))] for player in players]
    ptime("players")
    allHands = {tuple(hand) for player in playerHands for hand in player}
    oppHands = [sorted(allHands - set(tuple(hand) for hand in player)) for player in playerHands]
    ptime("opps")
    zipped = zip(playerHands, oppHands)
    ratings = [preFlopProb(player, opp) for player, opp in zipped]
    ptime("ratings")
    return ratings

a = [26, 42]
b = [17, 35]
c = [11, 49]
d = [21, 30]
e = [14, 38]
f = [23, 47]
plist = [a, b]
table = []
a = preFlop(plist)
print(len(a[0]))