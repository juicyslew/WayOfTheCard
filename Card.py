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
    def __init__(self, name=None, cardType=None, stats=None, state = None, creatureType = None, effect = False, effect_chance = EFFECT_CHANCE, cost = None, x = -100, y = -100, spell_chance = SPELL_CHANCE, active_effects = None): #Replace eventually with no init variables and just random generation.
        #Generate Randomly for Certain Items
        if cardType == None:
            if random() < spell_chance:
                cardType = TYPE_SPELL
            else:
                cardType = TYPE_CREATURE
        if state == None:
            state = choice(STATE_LIST)
        if creatureType == None and cardType == TYPE_CREATURE:
            creatureType = choice(CREATURE_LIST)
        if name == None:
            name = generate(cardType)
        if stats == None: # If stats not specified generate them
            if cost == None: #If cost not specified generate it
                cost = np.random.choice(range(0, MAX_COST+1), p = MANA_CURVE)
        if effect == True: #If effect equals True
            if random() < effect_chance or cardType == TYPE_SPELL: #Chance of having an effect
                effect = True
            else:
                effect = False
        if effect: #If effect is true then
            if cardType == TYPE_CREATURE:
                effect = Effect(self, cost, cardType) #Generate an effect with the effect spend
                if effect.effect == None: #If the effect generator didn't have enough effect spend, then set effect false
                    effect = False
            elif cardType == TYPE_SPELL:
                effect = Effect(self, cost, cardType)
        if stats == None:
            if effect:
                stats = generate_stats(cost, cardType, effect.leftover) #Generate Stats if None
            else:
                effect_spend = (CARD_INITIAL_STRENGTH+cost-cost*CARD_STRENGTH_DROPOFF) * CARD_STRENGTH
                stats = generate_stats(cost, cardType, effect_spend)
        if active_effects == None:
            active_effects = INIT_ACTIVE_EFFECT
        #if effect_spend == None: # if effect_spend == None
            #effect_spend = stats.pop(-1) # make effect_spend the final value of the stats
        starting_stats = stats #set original stats
        self.name = name
        self.cardType = cardType
        self.stats = stats
        self.starting_stats = starting_stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect
        self.manacost = cost
        self.active_effects = list(active_effects)

    def __str__(self): # Pret Pretty Strings
        if self.cardType == TYPE_CREATURE:
            active_strs = []
            for i in range(len(self.active_effects)):
                if self.active_effects[i]:
                    active_strs.append(ACTIVE_EFFECT_DICT[i])
            if self.effect == False:
                eff_s = ''
            else:
                eff_s = self.effect
            s = """@@@ %s || %s @@@\n---%s---%s
%s""" % (self.name, TYPE_DICT[self.cardType], self.stats, eff_s, 'Active Effects: ' + ', '.join(active_strs))
        if self.cardType == TYPE_SPELL:
            s = """@@@ %s || %s @@@\n---%s---%s""" % (self.name, TYPE_DICT[self.cardType], self.stats[0], self.effect)
        #s = """###Card###
#name: %s
#Card Type: %s
#Stats: %s
#State: %s
#Creature Type: %s
#Effect: %s
#""" % (self.name, TYPE_DICT[self.cardType], self.stats, STATE_DICT[self.state], CREATURE_DICT[self.creatureType], self.effect)
        return s

    def play(self, player_turn, all_players):
        """
        Put card from hand into field
        """
        if len(all_players) == 2:
            player = all_players[player_turn]
            enemy_player = all_players[not player_turn]
            if self.cardType == TYPE_CREATURE:
                player.cards.append(player.hand.cards.pop(player.hand.cards.index(self)))
                player.board.update_board(player.screen, all_players[0], all_players[1], self)
                try:
                    self.effect.activate(player, enemy_player, TRIGGER_PLAY)
                except AttributeError or TypeError:
                    pass
            if self.cardType == TYPE_SPELL:
                self.effect.activate(player, enemy_player, TRIGGER_PLAY)
                player.discard.cards.append(player.hand.cards.pop(player.hand.cards.index(self)))


        else:#3+ players
            if self.cardType == TYPE_CREATURE:
                all[0].cards.append(all[0].hand.cards.pop(all[0].hand.cards.index(self)))
                try:
                    self.effect.activate(all[0], all[1:], TRIGGER_PLAY)
                except AttributeError:
                    pass
            if self.cardType == TYPE_SPELL:
                self.effect.activate(all[0], all[1:], TRIGGER_PLAY)
                all[0].hand.cards.pop(all[0].hand.cards.index(self))

    def attack(self, opp_card):
        """
        Attack enemy card with your card
        """
        if self.active_effects[WINDFURY_INDEX] == 1:
            self.active_effects[WINDFURY_INDEX] = 2
        else:
            self.state = STATE_SLEEP
        self.active_effects[CHARGE_INDEX] = 2
        self.damage(opp_card.stats[ATT])
        opp_card.damage(self.stats[ATT])
        print('-----------------------------------')
        print('%s dealt %i damage to %s.  Result Health: %i' % (self.name, self.stats[ATT], opp_card.name, opp_card.stats[DEF]))
        print('%s dealt %i damage to %s.  Result Health: %i' % (opp_card.name, opp_card.stats[ATT], self.name, self.stats[DEF]))
        print('-----------------------------------')
    def damage(self, damage):
        """
        Code for taking damage
        """
        if self.active_effects[DIVINE_SHIELD_INDEX]:
            self.active_effects[DIVINE_SHIELD_INDEX] = 0
            print("Divine Shield Destroyed")
        else:
            self.stats[DEF] -= damage
