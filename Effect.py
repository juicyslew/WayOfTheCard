from Constants import *
import Card
from Card import *
from randGen import generate_numerical_effect
from random import choice, random, randint
import math
import numpy as np

class Effect():
    def __init__(self, ThisCard, cost, cardType, trigger = None, target = None, effect = None, numeric = None):
        if trigger == None and effect == None and numeric == None and target == None: #If there is no information about the effect in general Then
            #if cardType == TYPE_SPELL:
            effect_spend = (CARD_INITIAL_STRENGTH+cost-cost*CARD_STRENGTH_DROPOFF) * CARD_STRENGTH # Multiply Spell multiplier by the effective card cost, then by card strength and divide by 3 since the spending should be split between this and the attack and defense
            if cardType == TYPE_CREATURE:
                actual_spend = effect_spend*EFFECT_PREF/TOT_PREF
                effect_spend -= actual_spend
                #elif cardType == TYPE_CREATURE:
                #    effect_spend = EFFECT_PREF * (CARD_INITIAL_STRENGTH+cost-cost*CARD_STRENGTH_DROPOFF) * CARD_STRENGTH * 1/3 # Multiply Creature multiplier by the effective card cost, then by card strength and divide by 3 since the spending should be split between this and the attack and defense
                #print(cost)
                #effect, trigger, target, numeric,
                [effect_info, leftover] = generate_numerical_effect(actual_spend, cardType) #Use Effect Spend to Generate Effect
                #print(effect_spend, actual_spend, leftover)
                effect_spend += leftover
            elif cardType == TYPE_SPELL:
                actual_spend = effect_spend * SPELL_EFFECT_MULTIPLIER
                [effect_info, leftover] = generate_numerical_effect(actual_spend, cardType)
                effect_spend = 0
            #^#########################^#
            effect = [i[0] for i in effect_info]
            trigger = [i[1] for i in effect_info]
            target = [i[2] for i in effect_info]
            numeric = [i[3] for i in effect_info]
        else: #Otherwise Generate Effect Normally
            if trigger == None:
                trigger = (choice(TRIGGER_LIST),)
            if effect == None:
                effect = (choice(EFFECT_LIST),)
            if target == None:
                if self.class_type == CLASS_PLAYER:
                    target = (choice(PLAYER_TARGET_LIST),) #Add target based on stuff???
                elif self.class_type == CLASS_CREATURE:
                    target = (choice(CREATURE_TARGET_LIST),)
                else:
                    target = (choice(TARGET_LIST),)
        #Set self values
        eff_len = len(effect)
        self.effect = effect
        self.trigger = trigger
        for i in range(eff_len):
            if self.effect[i] == None:
                self.class_type = CLASS_PLAYER
                #effect_spend = 0
            else:
                self.class_type = EFFECT_CLASS_DICT[self.effect[i]]
            if numeric[i] == None: #If no numeric value, Generate Numeric
                if self.effect[i] == SUMMON_EFFECT:
                    #try:
                    numeric[i] = random()*MAX_NUMERIC #np.random.choice(np.random.choice(range(0, MAX_COST), p = MANA_CURVE))
                    #except ValueError:
                    #    numeric = effect_spend
                else:
                    numeric[i] = math.ceil(MAX_NUMERIC * random())
                #numeric = [math.ceil(MAX_NUMERIC * random()), math.ceil(MAX_NUMERIC * random())]
            #Set leftover self values
            if cardType == TYPE_SPELL and numeric[i] == 0:
                numeric[i] = 1
            if self.effect[i] == BUFF_EFFECT:
                r = randint(0, numeric[i])
                numeric[i] = [r, numeric[i]-r]
        self.numeric = numeric
        self.target = target
        self.leftover = effect_spend
        self.ThisCard = ThisCard
        self.eff_len = eff_len

    def __str__(self): # Return Pretty Effect String
        s = []
        for i in range(self.eff_len):
            print(self.effect[i])
            if type(self.effect) == int or self.effect[i] == None:
                s.append("")
            else:
                s.append("""
$$$ %s Effect || Trigger on %s || Targets %s || Has Potency %s $$$"""% (EFFECT_DICT[self.effect[i]], TRIGGER_DICT[self.trigger[i]], TARGET_DICT[self.target[i]], self.numeric[i]))
        return "".join(s)

    def determine_target(self, own_player, enemy_player):
        """
        Determine the target for an effect
        """
        if self.class_type == CLASS_PLAYER: #set a and b to the players if the effect is a player effect
            a = own_player
            b = enemy_player
        else:# self.class_type == CLASS_CARDS: #set a and b to the player_cards if it is a card effect
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
        elif self.target == TARGET_THIS_CREATURE:
            return [self.ThisCard]
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
            while True:
                self.i = input('Target Which Player? (1 for self, 2 for enemy)') # Get Input for which enemy to attack
                try:
                    self.i = int(self.i) # Check that it is an int
                    #Return player based on player input
                    if self.i == 1:
                        targ = own_player
                    elif self.i == 2:
                        targ = enemy_player
                    else:
                        print('Input a Number Between 1 and 2!')
                        continue
                except ValueError:
                    print('\nInput a Number!')
                    continue

                ## Now that player is picked, choose specific enemy
                print(targ)
                self.i = input("Which of %s's Creatures to target? (0 to not attack)" % targ.name) # Get Input
                try:
                    self.i = int(self.i)
                    try:
                        #Return Card at Index or end effect
                        if len(own_player.cards) + len(enemy_player.cards) <=2:
                            print("there are no creatures to attack")
                            return []
                        print(targ.cards)
                        if self.i == 0:
                            continue
                        elif self.i != 1:
                            return [targ.cards[self.i-1]]
                        else:
                            print("\nMust target Creature")
                            continue
                    except IndexError:
                        print("\nYou don't have that many cards!")
                        continue
                except ValueError:
                    print('\nInput a Number!')
                    continue

    def activate(self, own_player, enemy_player, time, all_players = None):     #May have to rewrite Activate based on all hands to make it make sense...
        """
        Function for Activating the Card Effect
        """
        for i in range(self.eff_len):
            eff_ls = self.effect
            trig_ls = self.trigger
            targ_ls = self.target
            num_ls = self.numeric
            self.effect = self.effect[i]
            self.trigger = self.trigger[i]
            self.target = self.target[i]
            self.numeric = self.numeric[i]
            if all_players == None:
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
                            if c in own_player.cards:
                                own_player.board.render_damage(self.numeric, own_player, own_player.cards.index(c))
                            elif c in enemy_player.cards:
                                own_player.board.render_damage(self.numeric, enemy_player, enemy_player.cards.index(c))
                    if self.effect == HEAL_EFFECT: # If Heal
                        self.t = self.determine_target(own_player, enemy_player) #Determine Target
                        for c in self.t: # Loop Through Targets
                            #Print Pretty String and Heal
                            print('-----------------------------------')
                            c.stats[DEF] = min(c.starting_stats[DEF], c.stats[DEF]+self.numeric)
                            print("%s was healed %i health.  Result Health: %i" %(c.name, self.numeric, c.stats[DEF]))
                            print('-----------------------------------')
                            if c in own_player.cards:
                                own_player.board.render_heal(self.numeric, own_player, own_player.cards.index(c))
                            elif c in enemy_player.cards:
                                own_player.board.render_heal(self.numeric, enemy_player, enemy_player.cards.index(c))
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
                            print("%s was buffed +%i/+%i to %i/%i" %(c.name, self.numeric[0], self.numeric[1], c.stats[0], c.stats[1]))
                    if self.effect == SPLIT_DEAL_EFFECT: # If Deal Damage
                        print('-----------------------------------')
                        i = 0
                        while i < self.numeric:
                            self.t = self.determine_target(own_player, enemy_player) #Find Target List
                            for c in self.t: # Loop Through Targets
                                #Print Pretty String and Deal Damage
                                c.stats[DEF] -= 1
                                print('%i damage dealt to %s.  Result Health: %i' % (1, c.name, c.stats[DEF]))
                            i+=1
                        print('-----------------------------------')
                    if self.effect == SPLIT_HEAL_EFFECT: # If Heal
                        print('-----------------------------------')
                        i = 0
                        while i < self.numeric:
                            self.t = self.determine_target(own_player, enemy_player) #Determine Target
                            for c in self.t: # Loop Through Targets
                                #Print Pretty String and Heal
                                c.stats[DEF] = min(c.starting_stats[DEF], c.stats[DEF]+1)
                                print("%s was healed %i health.  Result Health: %i" %(c.name, 1, c.stats[DEF]))
                            i+=1
                        print('-----------------------------------')
                    if self.effect == TAUNT_EFFECT:
                        self.t = self.determine_target(own_player, enemy_player) # Determine Target
                        for c in self.t: # Loop Through Targets
                            c.active_effects[TAUNT_INDEX] = 1
                    if self.effect == DIVINE_SHIELD_EFFECT:
                        self.t = self.determine_target(own_player, enemy_player)
                        for c in self.t:
                            c.active_effects[DIVINE_SHIELD_INDEX] = 1
                    if self.effect == CHARGE_EFFECT:
                        self.t = self.determine_target(own_player, enemy_player) # Determine Target
                        for c in self.t: # Loop Through Targets
                            c.active_effects[CHARGE_INDEX] = 1
                    if self.effect == WINDFURY_EFFECT:
                        self.t = self.determine_target(own_player, enemy_player) # Determine Target
                        for c in self.t: # Loop Through Targets
                            c.active_effects[WINDFURY_INDEX] = 1
            else:
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
                            print("%s was buffed +%i/+%i to %i/%i" %(c.name, self.numeric[0], self.numeric[1], c.stats[0], c.stats[1]))
                    if self.effect == SPLIT_DEAL_EFFECT: # If Deal Damage
                        print('-----------------------------------')
                        i = 0
                        while i < self.numeric:
                            self.t = self.determine_target(own_player, enemy_player) #Find Target List
                            for c in self.t: # Loop Through Targets
                                #Print Pretty String and Deal Damage
                                c.stats[DEF] -= 1
                                print('%i damage dealt to %s.  Result Health: %i' % (1, c.name, c.stats[DEF]))
                            i+=1
                        print('-----------------------------------')
                    if self.effect == SPLIT_HEAL_EFFECT: # If Heal
                        print('-----------------------------------')
                        i = 0
                        while i < self.numeric:
                            self.t = self.determine_target(own_player, enemy_player) #Determine Target
                            for c in self.t: # Loop Through Targets
                                #Print Pretty String and Heal
                                c.stats[DEF] = min(c.starting_stats[DEF], c.stats[DEF]+1)
                                print("%s was healed %i health.  Result Health: %i" %(c.name, 1, c.stats[DEF]))
                            i+=1
                        print('-----------------------------------')
            self.effect = eff_ls
            self.trigger = trig_ls
            self.target = targ_ls
            self.numeric = num_ls
            print(len(self.effect))
