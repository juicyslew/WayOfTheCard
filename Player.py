#from Constants import *
from Hand import *
from Deck import *
from Discard import *


class Player():
    """
    Player class: Contains deck and hand of player
    """
    def __init__(self):
        self.cards = []
        self.deck = Deck()
        self.deck.init_deck()
        self.hand = Hand(self.deck)
        self.discard = Discard()

    def __str__(self):
        return '\n\n'.join([str(card) for card in self.cards])
    #def str_hand(self):
        #return '\n\n'.join([card.name for card in self.hand.cards])
    def activate_cards(self):
        for card in self.cards:
            card.state = STATE_ACTIVE
    def check_active(self):
        ls = []
        for card in self.cards:
            if card.state == STATE_ACTIVE:
                ls.append(card)
        return ls
    def check_dead(self):
        ls = []
        for card in self.cards:
            if card.stats[DEF] <= 0:
                card.state = STATE_GRAVEYARD
                print(card.name + ' Has Died.')
                ls.append(card)
                self.discard.cards.append(self.cards.pop(self.cards.index(card)))
        return ls
