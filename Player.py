#from Constants import *
from Hand import *
from Deck import *
class Player():
    """
    Player class: Contains deck and hand of player
    """
    def __init__(self):
        self.cards = []
        self.deck = Deck()
        self.deck.init_deck()
        self.hand = Hand(self.deck)
        
    def __str__(self):
        return '\n\n'.join([str(card) for card in self.cards])
