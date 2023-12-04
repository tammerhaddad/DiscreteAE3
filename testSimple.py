import itertools
i = 0
# returns the best combination given a table and hands
def bestHand(player, table):
    global i
    i += 1
    best = max(hands.index(set(sorted(hand))) for hand in itertools.combinations(player+table, 3))
    return best
# returns the index in players of the player that won
def winner(players, table):
    bHands = [bestHand(player, table) for player in players]
    return bHands.index(max(bHands))

def postFlop(players):
    unknown = set(cards) - set(itertools.chain(*plist))
    ptables = [list(adds) for adds in itertools.combinations(unknown, 2)]
    # pHands = [[bestHand(player, ptable) for ptable in tables] for player in players]
    winners = [winner(players, ptable) for ptable in ptables]
    return [winners.count(i)/len(winners) for i in range(len(players))]
cards = sorted(range(15))
setHands = (set(comb) for comb in itertools.combinations(cards, 3))
hands = sorted(setHands)


def preFlop(players):
    playerHands = [[hand for hand in hands if any(card in hand for card in player)] for player in players]
    # print(playerHands)
    # sumHands = {itertools.chain(playerHands)}
    # oppHands = [sorted(sumHands - player) for player in playerHands]
    # pHands = [[bestHand(player, ptable) for ptable in tables] for player in players]
    # winners = [winner(players, ptable) for ptable in ptables]
    return [len(playerHands[0])]

a = [2, 7]
b = [1, 8]
c = [4, 6]
d = [4, 5]
plist = [a, b]
table = []
print(postFlop(plist))
print(i)
print(preFlop(plist))