from card import Card

class Player:
    def __init__(self, id, hand):
        self.id = id
        self.name = f"Player {id}"
        self.hand = hand
        self.blind_odds = 0

    def __str__(self):
        output = f'{self.name}: '
        for card in self.hand.hand:
            output += f"{card}" 
        return output

    