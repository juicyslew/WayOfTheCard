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
        return'\n' + '\n'.join(['%i)\n%s\n==============================================='%(i+1,str(self.cards[i])) for i in range(len(self.cards))]) + '\n'

    def init_deck(self):
        """ Generate Deck """
        for i in range(DECK_INIT_SIZE):
            self.cards.append(Card(state = STATE_SLEEP, effect = True)) #Using TestCards for now

    def shuffle_deck(self):
        """ Shuffle Deck """
        shuffle(self.cards)

    def draw(self, hand, num):
        """ Draw "num" Cards into Hand """
        for n in range(num):
            if len(hand.cards) < HAND_MAX_SIZE:
                hand.cards.append(self.cards.pop(0))
            else:
                print("Genius. The following card was lost: \n" + str(self.cards[0]))
                self.cards.pop(0)
