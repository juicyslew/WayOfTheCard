#from Constants import *
from Hand import *
from Deck import *
class Player():
    """
    Player class: Contains deck and hand of player
    """
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand(deck)
