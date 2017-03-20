from Constants import *
from Card import *
from Deck import *
from Discard import *
from Effect import *
from Hand import *
from Player import *
from randGen import *
import random

class Game():
    def __init__(self):
        #Rule Generation
        self.turn = 0
        self.init_game()

if __name__ == "__main__":
    deck = Deck()
    deck.init_deck()
    print(deck)
