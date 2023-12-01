from poker import Poker
game = Poker(2)

def play():
    for i in range(4):
        game.renderGame()
        while game.gameUpdate():
            game.pause()
        game.dealTable(i)
        if i == 3:
            break
        game.updateProbs()

