from Constants import *
from random import choice, random
import math

class Effect():
    def __init__(self, trigger = None, target = None, effect = None, numeric = None):#, effect = None):
        if trigger == None:
            trigger = choice(TRIGGER_LIST)
        if effect == None:
            effect = choice(EFFECT_LIST)
        if target == None:
            if effect == DRAW_EFFECT:
                target = choice(DRAW_TARGET_LIST) #Add target based on stuff???
            else:
                target = choice(TARGET_LIST)
        if numeric == None:
            numeric = math.ceil(MAX_NUMERIC * random())
        self.trigger = trigger
        self.target = target
        self.effect = effect
        self.numeric = numeric
    def __str__(self):
        s = """True

###EFFECT###
trigger: %s
target: %s
effectType: %s
magnitude: %s
""" % (TRIGGER_DICT[self.trigger], TARGET_DICT[self.target], EFFECT_DICT[self.effect], self.numeric)
        return s

    def determine_target(self, own_player, enemy_player):
        if self.target == TARGET_SELF:
            return [own_player]
        elif self.target == TARGET_OPPONENT:
            return [enemy_player]
        elif self.target == TARGET_ALL:
            return own_player.cards + enemy_player.cards
        elif self.target == TARGET_BOTH:
            return own_player.cards[0] + enemy_player.cards[0]
        elif self.target == TARGET_PLAYERS:
            while True:
                self.i = input('Target Which Player? (1 for self, 2 for enemy)')
                try:
                    self.i = int(self.i)
                    if self.i == 1:
                        return [own_player]
                    elif self.i == 2:
                        return [enemy_player]
                    else:
                        print('Input a Number Between 1 and 2!')
                except ValueError:
                    print('\nInput a Number!')
        elif self.target == TARGET_CREATURE:
            while True:
                self.i = input('Target Which (Enemy) Creature?')
                try:
                    self.i = int(i)
                    try:
                        if self.i != 1:
                            return enemy_player.cards[self.i-1]
                        else:
                            print("\nMust target Creature")
                    except IndexError:
                        print("\nYou don't have that many cards!")
                        continue
                except ValueError:
                    print('\nInput a Number!')
                    continue

    def activate(self, own_player, enemy_player, time):
        if time == self.trigger:
            if self.effect == DRAW_EFFECT:
                self.t = self.determine_target(own_player, enemy_player)
                for c in self.t:
                    print('-----------------------------------')
                    print(len(c.hand))
                    c.deck.draw(c.hand, self.numeric)
                    print(len(c.hand))
                    print('-----------------------------------')
            if self.effect == DEAL_EFFECT:
                self.t = self.determine_target(own_player, enemy_player)
                for c in self.t:
                    c.stats[DEF] -= self.numeric
