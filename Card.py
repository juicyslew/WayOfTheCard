from Constants import *
from Effect import *
from random import choice, random, randint
from randGen import generate

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
    def __init__(self, name=None, cardType=None, stats=None, state = None, creatureType = None, effect = False, effect_chance = EFFECT_CHANCE): #Replace eventually with no init variables and just random generation.
        if cardType == None:
            cardType = choice(TYPE_LIST)
        if stats == None:
            stats = [round(random()*MAX_STATS[i]) for i in range(len(MAX_STATS))]
            stats[0] = int(min(MAX_COST, max(0, randint(0, 3)-2 + (stats[1] + stats[2])/2)))
        starting_stats = stats
        if state == None:
            state = choice(STATE_LIST)
        if creatureType == None:
            creatureType = choice(CREATURE_LIST)
        if name == None:
            name = generate(cardType)
        if effect == True:
            if random() < effect_chance:
                effect = Effect()
            else:
                effect = False
        self.name = name
        self.cardType = cardType
        self.stats = stats
        self.starting_stats = starting_stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect
    def __str__(self):
        s = """###Card###
Name: %s
Stats: %s
Effect: %s
""" % (self.name, self.stats, self.effect)
        #s = """###Card###
#name: %s
#Card Type: %s
#Stats: %s
#State: %s
#Creature Type: %s
#Effect: %s
#""" % (self.name, TYPE_DICT[self.cardType], self.stats, STATE_DICT[self.state], CREATURE_DICT[self.creatureType], self.effect)
        return s

    def play(self, player, enemy_player):
        player.cards.append(player.hand.cards.pop(player.hand.cards.index(self)))
        #try:
        self.effect.activate(player, enemy_player, TRIGGER_PLAY)
        #except AttributeError:
            #print(AttributeError)

    def attack(self, opp_card):
        self.state = STATE_SLEEP
        self.stats[DEF] -= opp_card.stats[ATT]
        opp_card.stats[DEF] -= self.stats[ATT]
        print('-----------------------------------')
        print('%s dealt %i damage to %s.  Result Health: %i' % (self.name, self.stats[ATT], opp_card.name, opp_card.stats[DEF]))
        print('%s dealt %i damage to %s.  Result Health: %i' % (opp_card.name, opp_card.stats[ATT], self.name, self.stats[DEF]))
        print('-----------------------------------')
