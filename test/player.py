from cards import Card

class Player:
    def __init__(self, id, hand):
        self.id = id
        self.name = f"Player {id}"
        self.hand = hand

    def __str__(self):
        output = f'{self.name}: '
        for card in self.hand:
            output += f"{card}" 
        return output
