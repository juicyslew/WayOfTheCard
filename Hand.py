from Constants import *
class Hand():
    """
    Hand class: Contains list of cards in player's hand.
    """
    def __init__(self, deck):
        self.cards = []
        for i in range(HAND_INIT_SIZE):
            self.cards.append(deck.pop(0))
