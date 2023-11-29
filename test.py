from deck import Deck
hand = Deck(0).deck[:7]
def get_card_val(card):
    print(f"Sorting card with value: {card.value}")
    return card.value

def sort_hand(cards):
    return sorted(cards, reverse=True, key=get_card_val)

print([card.value for card in hand])
print(get_card_val(hand[0]))
def compare(card1, card2):
    if card1.value == card2.value:
        return 2
    return card1.value > card2.value

def get_card_val(card):
    return card.value

def sort_hand(self, cards):
    return cards.sort(reversed = True, key = self.get_card_val)

def trim_hand(hand):
    while len(hand) > 5:
        hand.pop()
    return hand

def get_flush(self, cards):
    suits = [card.suit for card in cards]
    hand = []
    if len(set(suits)) == 1 and len(cards) > 4:
        for card in cards:
            if card.suit == suits[0]:
                hand.append(card)
        return self.trim_hand(hand)
    return hand
