from Constants import *
import Card
from Card import *
from randGen import generate_numerical_effect
from random import choice, random, randint
import math
import numpy as np

class Effect():
    def __init__(self, effect_spend, card_type, trigger = None, target = None, effect = None, numeric = None):
        if trigger == None and effect == None and numeric == None: #If there is no information about the effect in general Then
            effect, trigger, numeric = generate_numerical_effect(effect_spend) #Use Effect Spend to Generate Effect
        else: #Otherwise Generate Effect Normally
            if trigger == None:
                trigger = choice(TRIGGER_LIST)
            if effect == None:
                effect = choice(EFFECT_LIST)
        #Set self values
        self.effect = effect
        if self.effect == None:
            self.class_type = CLASS_PLAYER
        else:
            self.class_type = EFFECT_CLASS_DICT[self.effect]
        self.trigger = trigger
        if target == None: #If no specified target, Generate Target
            if self.class_type == CLASS_PLAYER:
                target = choice(PLAYER_TARGET_LIST) #Add target based on stuff???
            elif self.class_type == CLASS_CREATURE:
                target = choice(CREATURE_TARGET_LIST)
            else:
                target = choice(TARGET_LIST)
        if numeric == None: #If no numeric value, Generate Numeric
            if self.effect == SUMMON_EFFECT:
                try:
                    numeric = np.random.choice(np.random.choice(range(0, MAX_COST+1), p = MANA_CURVE))
                except ValueError:
                    numeric = effect_spend
            elif self.effect == BUFF_EFFECT:
                r = math.ceil(MAX_NUMERIC * random())
                s = randint(0, r)
                numeric = [s, r-s]
            else:
                numeric = math.ceil(MAX_NUMERIC * random())
            #numeric = [math.ceil(MAX_NUMERIC * random()), math.ceil(MAX_NUMERIC * random())]
        #Set leftover self values
        if card_type == TYPE_SPELL and numeric == 0:
            numeric = 1
        self.numeric = numeric
        self.target = target

    def __str__(self): # Return Pretty Effect String
        s = """
$$$ %s Effect || Trigger on %s || Targets %s || Has Potency %s $$$"""% (EFFECT_DICT[self.effect], TRIGGER_DICT[self.trigger], TARGET_DICT[self.target], self.numeric)
        return s

    def determine_target(self, own_player, enemy_player):
        """
        Determine the target for an effect
        """
        if self.class_type == CLASS_PLAYER: #set a and b to the players if the effect is a player effect
            a = own_player
            b = enemy_player
        elif self.class_type == CLASS_CARDS: #set a and b to the player_cards if it is a card effect
            a = own_player.cards[0]
            b = enemy_player.cards[0]
        try:
            print("Effect: %s , Numeric: %i" % (EFFECT_DICT[self.effect], self.numeric))
        except TypeError:
            print("Effect: %s , Numeric: [%i,%i]" % (EFFECT_DICT[self.effect], self.numeric[0], self.numeric[1]))
        if self.target == TARGET_OWN_PLAYER: # If Target Is Own Player, Return
            return [a]
        elif self.target == TARGET_OPPONENT: # If Target is Enemy Player, Return
            return [b]
        elif self.target == TARGET_ALL: # If Target is All Cards, set and return
            print(own_player.cards + enemy_player.cards)
            return own_player.cards + enemy_player.cards
        elif self.target == TARGET_BOTH: # If Target is Both Players, set and return
            return [a, b]
        elif self.target == TARGET_RANDOM:
            return [choice(own_player.cards + enemy_player.cards)]
        elif self.target == TARGET_RANDOM_ENEMY:
            return [choice(enemy_player.cards)]
        elif self.target == TARGET_RANDOM_ALLY:
            return [choice(own_player.cards)]
        elif self.target == TARGET_RANDOM_CREATURE:
            return [choice(own_player.cards[1:] + enemy_player.cards[1:])]
        elif self.target == TARGET_RANDOM_ALLY_CREATURE:
            return [choice(own_player.cards[1:])]
        elif self.target == TARGET_RANDOM_ENEMY_CREATURE:
            return [choice(enemy_player.cards[1:])]
        elif self.target == TARGET_ALL_CREATURE:
            return own_player.cards[1:] + enemy_player.cards[1:]
        elif self.target == TARGET_PLAYERS: # If Target is Player of Choice
            while True:
                print("Your Health: %i\nEnemy Health: %i" % (own_player.cards[0].stats[DEF], enemy_player.cards[0].stats[DEF]))
                self.i = input('Target Which Player? (1 for self, 2 for enemy)') # Get Input for which enemy to attack
                try:
                    self.i = int(self.i) # Check that it is an int
                    #Return player based on player input
                    if self.i == 1:
                        return [a]
                    elif self.i == 2:
                        return [b]
                    else:
                        print('Input a Number Between 1 and 2!')
                except ValueError:
                    print('\nInput a Number!')
        elif self.target == TARGET_CREATURE: # If Target is Creature of Choice
            print(enemy_player) #Print Enemy Field
            while True:
                self.i = input('Target Which (Enemy) Creature? (0 to not attack)') # Get Input
                try:
                    self.i = int(self.i)
                    try:
                        #Return Card at Index or end effect
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
        """
        Function for Activating the Card Effect
        """
        if time == self.trigger: # If the current timing is the cards effect timing
            if self.effect == DRAW_EFFECT: # If draw
                self.t = self.determine_target(own_player, enemy_player) # Find Target List
                for c in self.t: # For Object in Target List
                    #Print Nice Strings and Draw Cards
                    print('-----------------------------------')
                    print("%s's hand increased from %i cards," %(c.name, len(c.hand.cards)))
                    c.deck.draw(c.hand, self.numeric)
                    print("to %i cards" % len(c.hand.cards))
                    print('-----------------------------------')
            if self.effect == DEAL_EFFECT: # If Deal Damage
                self.t = self.determine_target(own_player, enemy_player) #Find Target List
                print("target number: " + str(len(self.t))) # Print Number Of Targets
                for c in self.t: # Loop Through Targets
                    #Print Pretty String and Deal Damage
                    print('-----------------------------------')
                    c.stats[DEF] -= self.numeric
                    print('%i damage dealt to %s.  Result Health: %i' % (self.numeric, c.name, c.stats[DEF]))
                    print('-----------------------------------')
            if self.effect == HEAL_EFFECT: # If Heal
                self.t = self.determine_target(own_player, enemy_player) #Determine Target
                for c in self.t: # Loop Through Targets
                    #Print Pretty String and Heal
                    print('-----------------------------------')
                    c.stats[DEF] = min(c.starting_stats[DEF], c.stats[DEF]+self.numeric)
                    print("%s was healed %i health.  Result Health: %i" %(c.name, self.numeric, c.stats[DEF]))
                    print('-----------------------------------')
            if self.effect == SUMMON_EFFECT: # If Summon
                self.t = self.determine_target(own_player, enemy_player) # Determine Target
                for c in self.t: # Loop Through Targets
                    #Summon Card of Cost Numeric
                    c.cards.append(Card.Card(name = "SUMMONED DUDE", cardType = TYPE_CREATURE, state = STATE_SLEEP, effect = True, effect_chance = 0.2, cost = self.numeric))
                    print("Creature Summonned for %s" %c.name)
            if self.effect == BUFF_EFFECT: # If Buff
                self.t = self.determine_target(own_player, enemy_player) # Determine Target
                for c in self.t: # Loop Through Targets
                    c.stats[ATT] += self.numeric[0]
                    c.stats[DEF] += self.numeric[1]
                    print("%s was buffed +%i/+%i" %(c.name, self.numeric[0], self.numeric[1]))
