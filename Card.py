from Constants import *
from Effect import *
from random import choice, random

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
    def __init__(self, name=None, cardType=None, stats=None, state = None, creatureType = None, effect = False): #Replace eventually with no init variables and just random generation.
        if name == None:
            name = choice(NAME_LIST)
        if cardType == None:
            cardType = choice(TYPE_LIST)
        if stats == None:
            stats =  [round(random()*MAX_STATS[i]) for i in range(len(MAX_STATS))]
        if state == None:
            state = choice(STATE_LIST)
        if creatureType == None:
            creatureType = choice(CREATURE_LIST)
        if effect == True:
            if random() < EFFECT_CHANCE:
                effect = Effect()
            else:
                effect = False
        self.name = name
        self.cardType = cardType
        self.stats = stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect
    def __str__(self):
        s = """###Card###
name: %s
Card Type: %s
Stats: %s
State: %s
Creature Type: %s
Effect: %s
""" % (self.name, TYPE_DICT[self.cardType], self.stats, STATE_DICT[self.state], CREATURE_DICT[self.creatureType], self.effect)
        return s


#print(Card('wow', TYPE_CREATURE, [1,2,3], STATE_ACTIVE, CREATURE_MECH, Effect(TRIGGER_PLAY)))
