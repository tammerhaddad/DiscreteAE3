from poker import Poker
game = Poker(6)

for i in range(4):
    game.renderGame()
    while game.gameUpdate():
        game.pause()
    game.dealTable(i)
    game.updateProbs()