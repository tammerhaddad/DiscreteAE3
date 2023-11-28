from poker import Poker
game = Poker()

game.printHand()
print(f"Prob: {game.blindProb()}")

for i in range(3):
    input("\nEnter to Continue.")
    game.renderGame()
    print(f"Prob: {game.blindProb()}")
    