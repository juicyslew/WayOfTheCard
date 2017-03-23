from Constants import *
import Card
from Card import *
from randGen import generate_numerical_effect
from random import choice, random
import math

class Effect():
    def __init__(self, effect_spend, trigger = None, target = None, effect = None, numeric = None):#, effect = None):
        if trigger == None and effect == None and numeric == None:
            effect, trigger, numeric = generate_numerical_effect(effect_spend)
        else:
            if trigger == None:
                trigger = choice(TRIGGER_LIST)
            if effect == None:
                effect = choice(EFFECT_LIST)
        self.effect = effect
        if self.effect == None:
            self.class_type = CLASS_PLAYER #Random Class
        else:
            self.class_type = EFFECT_CLASS_DICT[self.effect]
        self.trigger = trigger
        if target == None:
            if self.class_type == CLASS_PLAYER:
                target = choice(PLAYER_TARGET_LIST) #Add target based on stuff???
            else:
                target = choice(TARGET_LIST)
        if numeric == None:
            if self.effect == SUMMON_EFFECT:
                numeric = np.random.choice(np.random.choice(range(0, MAX_COST+1), p = MANA_CURVE))
            else:
                numeric = math.ceil(MAX_NUMERIC * random())
            #numeric = [math.ceil(MAX_NUMERIC * random()), math.ceil(MAX_NUMERIC * random())]
        self.numeric = numeric
        self.target = target
    def __str__(self):
        s = """
$$$ %s Effect || Trigger on %s || Targets %s || Has Potency %s $$$"""% (EFFECT_DICT[self.effect], TRIGGER_DICT[self.trigger], TARGET_DICT[self.target], self.numeric)
        return s

    def determine_target(self, own_player, enemy_player):
        if self.class_type == CLASS_PLAYER:
            a = own_player
            b = enemy_player
        elif self.class_type == CLASS_CARDS:
            a = own_player.cards[0]
            b = enemy_player.cards[0]
        try:
            print("Effect: %s , Numeric: %i" % (EFFECT_DICT[self.effect], self.numeric))
        except TypeError:
            print("Effect: %s , Numeric: [%i,%i]" % (EFFECT_DICT[self.effect], self.numeric[0], self.numeric[1]))
        if self.target == TARGET_SELF:
            return [a]
        elif self.target == TARGET_OPPONENT:
            return [b]
        elif self.target == TARGET_ALL:
            print(own_player.cards + enemy_player.cards)
            return own_player.cards + enemy_player.cards
        elif self.target == TARGET_BOTH:
            return [a, b]
        elif self.target == TARGET_PLAYERS:
            while True:
                print("Your Health: %i\nEnemy Health: %i" % (own_player.cards[0].stats[DEF], enemy_player.cards[0].stats[DEF]))
                self.i = input('Target Which Player? (1 for self, 2 for enemy)')
                try:
                    self.i = int(self.i)
                    if self.i == 1:
                        return [a]
                    elif self.i == 2:
                        return [b]
                    else:
                        print('Input a Number Between 1 and 2!')
                except ValueError:
                    print('\nInput a Number!')
        elif self.target == TARGET_CREATURE:
            print(enemy_player)
            while True:
                self.i = input('Target Which (Enemy) Creature? (0 to not attack)')
                try:
                    self.i = int(self.i)
                    try:
                        if self.i == 0:
                            return []
                        if self.i != 1:
                            return [enemy_player.cards[self.i-1]]
                        else:
                            print("\nMust target Creature")
                            continue
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
                    print("%s's hand increased from %i cards," %(c.name, len(c.hand.cards)))
                    c.deck.draw(c.hand, self.numeric)
                    print("to %i cards" % len(c.hand.cards))
                    print('-----------------------------------')
            if self.effect == DEAL_EFFECT:
                self.t = self.determine_target(own_player, enemy_player)
                print("target number: " + str(len(self.t)))
                for c in self.t:
                    print('-----------------------------------')
                    c.stats[DEF] -= self.numeric
                    print('%i damage dealt to %s.  Result Health: %i' % (self.numeric, c.name, c.stats[DEF]))
                    print('-----------------------------------')
            if self.effect == HEAL_EFFECT:
                self.t = self.determine_target(own_player, enemy_player)
                for c in self.t:
                    print('-----------------------------------')
                    c.stats[DEF] = min(c.starting_stats[DEF], c.stats[DEF]+self.numeric)
                    print("%s was healed %i health.  Result Health: %i" %(c.name, self.numeric, c.stats[DEF]))
                    print('-----------------------------------')
            if self.effect == SUMMON_EFFECT:
                self.t = self.determine_target(own_player, enemy_player)
                for c in self.t:
                    c.cards.append(Card.Card(name = "SUMMONED DUDE", cardType = TYPE_CREATURE, state = STATE_SLEEP, effect = True, cost = self.numeric))
                    #c.cards.append(Card.Card(name = "SUMMONED DUDE", cardType = TYPE_CREATURE, stats = [0, self.numeric[0], self.numeric[1]], state = STATE_SLEEP, effect = True, effect_chance=0.1))
                    print("Creature Summonned for %s" %c.name)
            #print(self.t)
