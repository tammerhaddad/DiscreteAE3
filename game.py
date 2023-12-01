from poker import Poker
game = Poker(2)

for i in range(4):
    game.renderGame()
    while game.gameUpdate():
        game.pause()
    game.dealTable(i)
    game.updateProbs()