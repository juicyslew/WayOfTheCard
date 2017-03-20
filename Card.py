from Constants import *

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
