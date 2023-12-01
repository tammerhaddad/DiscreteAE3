from poker import Poker
game = Poker(2)

def play():
    for i in range(4):
        game.render()
        while game.gameUpdate():
            game.pause()
        if i == 3:
            break
        game.dealTable(i)
        game.updateProbs()
    
play()