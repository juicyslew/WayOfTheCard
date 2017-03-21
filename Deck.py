from Constants import *
from Card import *
from random import shuffle

class Deck():
    """
    Deck class:  Contains list of cards in player's deck.
    """
    def __init__(self):
        self.cards = []
    def __str__(self):
        return '\n\n'.join([str(card) for card in self.cards])
    def init_deck(self):
        for i in range(DECK_INIT_SIZE):
            self.cards.append(Card(state = STATE_SLEEP, cardType=TYPE_CREATURE, effect = True)) #Using TestCards for now
    def shuffle_deck(self):
        shuffle(cards)
    def draw(self, hand, num):
        for n in range(num):
            hand.cards.append(self.cards.pop(0))
