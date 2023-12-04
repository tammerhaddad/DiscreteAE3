from poker import Poker

def play():
    game = Poker(6)
    for i in range(4):
        game.render()
        while game.gameUpdate():
            game.pause()
        if i == 3:
            game.save()
            break
        game.dealTable(i)
        game.updateProbs()

for i in range(100):
    play()