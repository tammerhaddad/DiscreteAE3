class Player:
    def __init__(self, id, hand, origin = (0,0)):
        self.id = id
        self.origin = origin
        self.name = f"Player {id}"
        self.hand = hand
        self.prob = 0

    def __str__(self):
        output = f'{self.name}: '
        for card in self.hand.hand:
            output += f"{card}" 
        return output

    