"""
Initial test of simply setting up the game.  Ignore this.
If you want to see old code, feel free to browse. 
"""
import random
from Constants import *

class randGen():
    def __init__(self):
        #???
        pass
    def card_gen(self):
        #???
        pass

class Discard():
    def __init__(self):
        self.cards = []

class Player():
    """
    Player class: Contains deck and hand of player
    """
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand(deck)

class Hand():
    """
    Hand class: Contains list of cards in player's hand.
    """
    def __init__(self, deck):
        self.cards = []
        for i in range(HAND_INIT_SIZE):
            self.cards.append(deck.pop(0))

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

class Card():
    """
    This is the class for Cards.  This contains all the important information about the card and what it does.

    Name: string for name of card
    STRING

    Card Type: type of card: Creature vs Spell (Dudes vs Dos)
    INT

    Stats: Cost, Offense, Defense
    LIST OF INTS

    State: Asleep vs Active vs Dead vs In Hand
    INT

    Creature Type: Beast vs Robot vs Knight vs Whatever
    INT/STRING

    Effect: Effects Class, Handles the special effects of the card.
    EFFECT CLASS
    """
    def __init__(self, name, cardType, stats, state = STATE_SLEEP, creatureType = None, effect = None): #Replace eventually with no init variables and just random generation.
        self.name = name
        self.cardType = cardType
        self.stats = stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect

class Game():
    def __init__(self):
        #Rule Generation
        self.turn = 0
        self.init_game()

class Effect():
    def __init__(self, trigger, target, effect = None):
        self.trigger = trigger
        self.target = target
        self.effect = effect
        self.numeric = round(MAX_NUMERIC * random.random())

if __name__ == "__main__":
    deck = Deck()
    deck.init_deck()
