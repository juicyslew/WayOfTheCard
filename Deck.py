from Constants import *
from Card import *
import random

class Deck():
    """
    Deck class:  Contains list of cards in player's deck.
    """
    def __init__(self):
        self.cards = []
        stats = [round(random.random()*MAX_STATS[i]) for i in range(len(MAX_STATS))]
        self.TestCard = Card("TestCard", CREATURE, stats)
    def init_deck(self):
        for i in range(DECK_INIT_SIZE):
            self.cards.append(self.TestCard) #Using TestCards for now
    def shuffle_deck(self):
        random.shuffle(cards)
