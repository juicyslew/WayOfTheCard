from Constants import *
from Effect import *
from random import choice, random, randint
from randGen import generate, generate_stats, name_list,adjective,noun_list
import numpy as np
import sys
from imagegen import *
import pygame
import os

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
    def __init__(self, name=None, cardType=None, stats=None, state = None, creatureType = None,
                 effect = False, effect_chance = EFFECT_CHANCE, cost = None, x = -100, y = -100,
                 spell_chance = SPELL_CHANCE, active_effects = None, rarity = None): #Replace eventually with no init variables and just random generation.
        #Generate Randomly for Certain Items
        self.blink = 0
        self.is_player = False
        if rarity == None:
            rarity = np.random.choice(RARITIES, p = RARITY_PROBS)
        if cardType == None:
            if random.random() < spell_chance:
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
            if random.random() < effect_chance or cardType == TYPE_SPELL: #Chance of having an effect
                effect = True
            else:
                effect = False
        if effect: #If effect is true then
            effect = Effect(self, cost, cardType, rarity)
            if cardType == TYPE_CREATURE:
                if effect.effect == None: #If the effect generator didn't have enough effect spend, then set effect false
                    effect = False
        if stats == None:
            if effect:
                stats = generate_stats(cost, cardType, effect.leftover) #Generate Stats if None
            else:
                powerinfo = POWER_DICT[rarity]
                power = powerinfo[0]
                eff_pref = powerinfo[1]
                init_pow = powerinfo[2]
                if cost == 0:
                    effect_spend = (init_pow + 1) * power
                else:
                    effect_spend = (init_pow + cost) * power
                stats = generate_stats(cost, cardType, effect_spend)
        if active_effects == None:
            active_effects = INIT_ACTIVE_EFFECT
        #if effect_spend == None: # if effect_spend == None
            #effect_spend = stats.pop(-1) # make effect_spend the final value of the stats
        self.name = name
        self.art = 1
        if cardType == TYPE_CREATURE:
            namelist = name.split()
            adj1 = 'NONE'
            adj2 = 'NONE'
            adj_s = 'NONE'
            noun = 'NONE'
            for i in namelist:
                if i.lower() in noun_list:
                    noun = i.lower()
                elif i.lower() in name_list:
                    if adj1 =='NONE':
                        adj1 = i.lower()
                    else:
                        adj2 = i.lower()
                elif i.lower() in special_adj:
                    adj_s = i.lower()
            #noun = name.split()[-1]
            #adj1 = name.split()[0]
            #if adj1.lower() not in name_list:
            #    adj1 = 'NONE'
            self.art = genimage_dudes(adj1, adj2=adj2, noun = noun, adj_s = adj_s)
            if adj2 == "NONE":
                adj2n = ""
            else:
                adj2n = adj2
            if adj_s == "NONE":
                adj_sn = ""
            else:
                adj_sn = adj_s
            self.arted = False
            self.art = 1
            self.art_path = "ImageStuff/finimages/%s%s%s%s.jpg" % (noun, adj1, adj2n,adj_sn)
        elif cardType == TYPE_SPELL:
            #chnge potato to spell to make work
            namelist = name.split()
            adj1 = 'NONE'
            adj2 = 'NONE'
            adj_s = 'NONE'
            for i in namelist:
                if i.lower() in name_list:
                    if adj1 =='NONE':
                        adj1 = i.lower()
                    else:
                        adj2 = i.lower()
                elif i.lower() in special_adj:
                    adj_s = i.lower()
            self.art = genimage_does(adj1, adj2=adj2, adj_s = adj_s)
            if adj2 == "NONE":
                adj2n = ""
            else:
                adj2n = adj2
            if adj_s == "NONE":
                adj_sn = ""
            else:
                adj_sn = adj_s
            self.arted = False
            self.art = 1
            self.art_path = "ImageStuff/finimages/%s%s%s%s.jpg" % ('spell', adj1, adj2n,adj_sn)
        self.cardType = cardType
        self.stats = stats
        self.state = state
        self.creatureType = creatureType
        self.effect = effect
        self.manacost = cost
        self.active_effects = list(active_effects)
        self.rarity = rarity
        self.starting_stats = self.stats.copy() #set original stats

    def __str__(self): # Pret Pretty Strings
        if self.cardType == TYPE_CREATURE:
            active_strs = []
            for i in range(len(self.active_effects)):
                if self.active_effects[i] == 1:
                    active_strs.append(ACTIVE_EFFECT_DICT[i])
            if self.effect == False:
                eff_s = ''
            else:
                eff_s = self.effect
            s = """@@@ %s || %s || %s @@@\n---%s---%s
%s""" % (self.name, TYPE_DICT[self.cardType], RARITY_DICT[self.rarity], self.stats, eff_s, 'Active Effects: ' + ', '.join(active_strs))
        if self.cardType == TYPE_SPELL:
            s = """@@@ %s || %s || %s @@@\n---%s---%s""" % (self.name, TYPE_DICT[self.cardType], RARITY_DICT[self.rarity], self.stats[0], self.effect)
        return s

    def play(self, player_turn, all_players):
        """
        Put card from hand into field
        """
        try:
            self.art = pygame.image.load(self.art_path).convert_alpha()
            self.art = pygame.transform.scaleNone(self.art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
        except:
            #self.art = pygame.image.load(os.path.join('bear.png')).convert_alpha()
            pass
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
        if self.active_effects[DIVINE_SHIELD_INDEX] and damage != 0:
            self.active_effects[DIVINE_SHIELD_INDEX] = 0
            print("Divine Shield Destroyed")
        elif damage != 0:
            self.stats[DEF] -= damage

    def heal(self):
        self.stats[DEF] = self.starting_stats[DEF]
