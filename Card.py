from Constants import *
from Effect import *
from random import choice, random, randint
from randGen import generate, generate_stats
import numpy as np

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
    def __init__(self, name=None, cardType=None, stats=None, state = None, creatureType = None, effect = False, effect_chance = EFFECT_CHANCE, effect_spend = None, cost = None): #Replace eventually with no init variables and just random generation.
        #Generate Randomly for Certain Items
        if cardType == None:
            cardType = choice(TYPE_LIST)
        if state == None:
            state = choice(STATE_LIST)
        if creatureType == None and cardType == TYPE_CREATURE:
            creatureType = choice(CREATURE_LIST)
        if name == None:
            name = generate(cardType)
        if effect == True: #If effect equals True
            if random() < effect_chance or cardType == TYPE_SPELL: #Chance of having an effect
                effect = True
            else:
                effect = False
        if stats == None: # If stats not specified generate them
            if cost == None: #If cost not specified generate it
                cost = np.random.choice(range(0, MAX_COST+1), p = MANA_CURVE)
            if cardType == TYPE_CREATURE:
                stats = generate_stats(effect, cost) #Generate Stats if None
            else:
                stats = [0, 0, 0]
        if effect_spend == None: # if effect_spend == None
            effect_spend = stats.pop(-1) # make effect_spend the final value of the stats
        else: #if not then
            stats.pop(-1) #still remove final value
        if effect: #If effect is true then
            effect = Effect(effect_spend) #Generate an effect with the effect spend
            if effect.effect == None: #If the effect generator didn't have enough effect spend, then set effect false
                effect = False
        starting_stats = stats #set original stats
        self.name = name
        self.cardType = cardType
        self.stats = stats
        self.starting_stats = starting_stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect
    def __str__(self): # Pret Pretty Strings
        if self.effect == False:
            eff_s = ''
        else:
            eff_s = self.effect
        s = """@@@ %s || %s @@@%s""" % (self.name, self.stats, eff_s)
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
        """
        Put card from hand into field
        """
        if self.cardType == TYPE_CREATURE:
            player.cards.append(player.hand.cards.pop(player.hand.cards.index(self)))
            try:
                self.effect.activate(player, enemy_player, TRIGGER_PLAY)
            except AttributeError:
                pass
        if self.cardType == TYPE_SPELL:
            self.effect.activate(player, enemy_player, TRIGGER_PLAY)

    def attack(self, opp_card):
        """
        Attack enemy card with your card
        """
        self.state = STATE_SLEEP
        self.stats[DEF] -= opp_card.stats[ATT]
        opp_card.stats[DEF] -= self.stats[ATT]
        print('-----------------------------------')
        print('%s dealt %i damage to %s.  Result Health: %i' % (self.name, self.stats[ATT], opp_card.name, opp_card.stats[DEF]))
        print('%s dealt %i damage to %s.  Result Health: %i' % (opp_card.name, opp_card.stats[ATT], self.name, self.stats[DEF]))
        print('-----------------------------------')
