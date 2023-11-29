import itertools
import time
start_time = time.time()

numPlayers = 1
cards = list(range(50))
tables = list(itertools.combinations(cards, 5))
a = 0
for table in tables:
    a += 1
print(f"{a}, Time: {time.time() - start_time:.2f} seconds")