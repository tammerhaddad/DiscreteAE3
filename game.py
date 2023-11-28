from poker import Poker
game = Poker()

# RUN COMMAND
# cd '' && '/usr/local/bin/python3'  'game.py'  && echo Exit status: $? && exit 1

for i in range(4):
    game.renderGame()
    game.dealTable(i)
    while game.gameUpdate():
        game.pause()
game.quitGame()