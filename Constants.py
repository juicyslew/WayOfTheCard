"""
Python File to contain Constants for Card Game
"""
import operator

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000

DECK_INIT_SIZE = 30 #Initial Deck Size
MAX_NUMERIC = 3 #(Outdated?) Maximum Numerical Value On Effects
MAX_NEGATIVE_NUMERIC = 5
HAND_INIT_SIZE = 4 # Initial Hand Size
HAND_MAX_SIZE = 10 # Maximum Hand Size, Need To Actually Impliment

#NAME_LIST = ["Bird", "Robot Doctor", "Magic Stones", "Test Card", "JEREMEEEEE"]

#Integers to represent creature types, list of valid type choices, and dictionary for decoding them
TYPE_CREATURE = 0
TYPE_SPELL = 1
TYPE_LIST = (TYPE_CREATURE, TYPE_SPELL)
TYPE_DICT = {None:"None",TYPE_CREATURE:"Creature", TYPE_SPELL:"Spell"}


PLAYER_HEALTH = 30 #Player Health

COST = 0 #Cost index in stats
ATT = 1 #Attack index in stats
DEF = 2 #Defense index in stats

MAX_MANA = 10 #Maximum Mana in a Turn
MANA_PER_TURN = 1 #Mana gain per turn

#Mana curve for card cost generation: Pre-generated List of probabilities.
MANA_CURVE = [0.04973162330165214, 0.11935589592396513, 0.18898016854627814, 0.18898016854627814, 0.15914119456528683, 0.11559168664589639, 0.065624272622313, 0.037758460971486926, 0.023838973980991283, 0.015398532937511128, 0.010599021958340752]
tot = sum(MANA_CURVE)
MANA_CURVE = [i/tot for i in MANA_CURVE]
#SUMMON_CURVE = [0.1, 0.3, 0.4, 0.15, 0.05, 0, 0, 0, 0, 0, 0]

ATT_PREF_MULTIPLIER = 1 # Set Preference of Attack over Defense
DEF_PREF_MULTIPLIER = 1 # Set Preference of Defense over Attack
STATS_PREF = 1.1   #Should be about twice the Effect_Pref # Stats Preference over Other Stuff
EFFECT_PREF = .9   # Set Preference of Effects over Defense and Attack
TOT_PREF = STATS_PREF+EFFECT_PREF
PREF_MULTIPLIERS = (ATT_PREF_MULTIPLIER, DEF_PREF_MULTIPLIER) #Put multipliers in tuple together
EFFECT_THRESHOLD = .5 #(Outdated) Maximum wasted effect potential when generating effect for card
MIN_EFFECT = .5 #if an object is supposed to have an effect, this gives the initial value that it has to be at least.
CARD_STRENGTH = 1.8 #Overall strength of the generated cards
CARD_STRENGTH_DROPOFF = 0 #Amount of lost potential in higher cost cards (the larger this is, the less op high mana cards are relative to lower cost cards)
CARD_INITIAL_STRENGTH = 1.1 # Effective cost increase for every card
SPELL_EFFECT_MULTIPLIER = .46
LEFTOVER_MULTIPLIER = .75 #Percent of leftover spending from effect generation that is effective for stats
EFFECT_CHANCE = 0.7 #Chance that a given card that can have an effect has one.
DOUBLE_EFFECT_CHANCE = .33
SPELL_CHANCE = .25
SPELL_ADDER = 1
EFFECT_TRY_NUM = 25
NEGATIVE_ADDER = 1 #This adds to stats if the effect generated is negative, its like a little sweetener that helps dealing with negative effects on a card
#MANA_CURVE_CDF = [sum(MANA_CURVE[:i+1]) for i in range(len(MANA_CURVE))]
#psum = sum(MANA_SPLIT)
#MANA_SPLIT = [i / psum for i in MANA_SPLIT]


MAX_COST = 10 #Maximum possible Cost
MAX_ATT = 12 #Maximum Attack
MAX_DEF = 12 #Maximum Defense
MIN_DEF = 1
MAX_STATS = (MAX_COST, MAX_ATT, MAX_DEF) #List of Max Stats

#States, State Encoder List, and State Decoder Dictionary
STATE_SLEEP = 0
STATE_ACTIVE = 1
STATE_GRAVEYARD = 2
STATE_LIST = (STATE_SLEEP, STATE_ACTIVE)
STATE_DICT = {None:"None",STATE_SLEEP:"Sleep", STATE_ACTIVE:"Active",STATE_GRAVEYARD:"Dead"}

#Effects, Effect Encoder List, Effect Decoder Dictionary, and Effect Cost Dictionary
DRAW_EFFECT = 0
DEAL_EFFECT = 1
HEAL_EFFECT = 2
SUMMON_EFFECT = 3
BUFF_EFFECT = 4
SPLIT_DEAL_EFFECT = 5
SPLIT_HEAL_EFFECT = 6
TAUNT_EFFECT = 7
DIVINE_SHIELD_EFFECT = 8
CHARGE_EFFECT = 9
WINDFURY_EFFECT = 10

#-----------ORDER MATTERS WITH ALL OF THESE LISTS AND COST DICTIONARIES, THEY NEED TO HAVE THE SAME ORDER--------------#
EFFECT_LIST = (DRAW_EFFECT, DEAL_EFFECT, HEAL_EFFECT, SUMMON_EFFECT, BUFF_EFFECT, SPLIT_DEAL_EFFECT, SPLIT_HEAL_EFFECT, TAUNT_EFFECT, DIVINE_SHIELD_EFFECT, CHARGE_EFFECT, WINDFURY_EFFECT)
EFFECT_DICT = {None:"None",DRAW_EFFECT:"Draw Cards", DEAL_EFFECT:"Deal Damage", HEAL_EFFECT:"Heal", SUMMON_EFFECT:"Summon Creature", BUFF_EFFECT:"Buff Card", SPLIT_DEAL_EFFECT:"Split Damage", SPLIT_HEAL_EFFECT:"Split Heal", TAUNT_EFFECT:"Give Taunt", DIVINE_SHIELD_EFFECT:"Give Divine Shield", CHARGE_EFFECT:"Give Charge", WINDFURY_EFFECT:"Give Windfury"}
EFFECT_COST_DICT = {DRAW_EFFECT:-1.65, DEAL_EFFECT:1, HEAL_EFFECT:-.75, SUMMON_EFFECT:-1.1, BUFF_EFFECT:-.9, SPLIT_DEAL_EFFECT:1, SPLIT_HEAL_EFFECT:-.75, TAUNT_EFFECT:-2, DIVINE_SHIELD_EFFECT:-3, CHARGE_EFFECT:-2.5, WINDFURY_EFFECT:-4}#Split Damage and heal are so high because they only work with random targets which have low values, this offsets them a bit #This converts the identity of the effect to the cost of it when generating effects
STATIC_EFFECT_LIST = (TAUNT_EFFECT, DIVINE_SHIELD_EFFECT, CHARGE_EFFECT, WINDFURY_EFFECT)

TAUNT_INDEX = 0
DIVINE_SHIELD_INDEX = 1
CHARGE_INDEX = 2
WINDFURY_INDEX = 3
INIT_ACTIVE_EFFECT = [0,0,0,0]
ACTIVE_EFFECT_DICT = {0:"Taunt", 1:"Divine Shield", 2:"Charge", 3:"Windfury"}

#Creature Types, Creature Type Encoder List, and Creature Type Decoder Dictionary
CREATURE_HUMAN = 0
CREATURE_MECH = 1
CREATURE_BEAST = 2
CREATURE_DEMON = 3
CREATURE_DRAGON = 4
CREATURE_PIRATE = 5
CREATURE_ELEMENTAL = 6
CREATURE_LIST = (CREATURE_HUMAN, CREATURE_MECH, CREATURE_BEAST, CREATURE_DEMON,
CREATURE_DRAGON, CREATURE_PIRATE, CREATURE_ELEMENTAL)
CREATURE_DICT = {CREATURE_HUMAN:"Human", CREATURE_MECH:"Mech", CREATURE_BEAST:"Beast",
CREATURE_DEMON:"Demon", CREATURE_DRAGON:"Dragon", CREATURE_PIRATE:"Pirate", CREATURE_ELEMENTAL:"Elemental"}

#Triggers, Trigger Encoder List, Trigger Decoder Dictionary, and Trigger Cost Dictionary
TRIGGER_END = 0
TRIGGER_BEGIN = 1
TRIGGER_PLAY = 2
TRIGGER_DEATH = 3
TRIGGER_LIST = (TRIGGER_END, TRIGGER_BEGIN, TRIGGER_PLAY, TRIGGER_DEATH)
TRIGGER_DICT = {TRIGGER_END:"End Turn", TRIGGER_BEGIN:"Begin Turn", TRIGGER_PLAY:"Play", TRIGGER_DEATH:"Death"}
TRIGGER_COST_DICT = {TRIGGER_END:2.2, TRIGGER_BEGIN:1.5, TRIGGER_PLAY:1, TRIGGER_DEATH:1} # Converts identity of triggers to cost
PLAY_TRIGGER_LIST = (TRIGGER_PLAY,)

#Targets, Target Encoder List, and Target Decoder Dictionary
TARGET_ALL = 0
TARGET_OWN_PLAYER = 1
TARGET_CREATURE = 2
TARGET_OPPONENT = 3
TARGET_PLAYERS = 4
TARGET_BOTH = 5
TARGET_RANDOM = 6
TARGET_RANDOM_ENEMY = 7
TARGET_RANDOM_ALLY = 8
TARGET_RANDOM_CREATURE = 9
TARGET_RANDOM_ALLY_CREATURE = 10
TARGET_RANDOM_ENEMY_CREATURE = 11
TARGET_ALL_CREATURE = 12
TARGET_THIS_CREATURE = 13
TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE, TARGET_THIS_CREATURE)
PLAYER_TARGET_LIST = (TARGET_BOTH, TARGET_OWN_PLAYER, TARGET_OPPONENT, TARGET_PLAYERS)
CREATURE_TARGET_LIST = (TARGET_CREATURE, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_ALL_CREATURE, TARGET_THIS_CREATURE)
TARGET_DICT = {TARGET_BOTH:"Both Players", TARGET_ALL:"All Characters", TARGET_OWN_PLAYER:"Own Player", TARGET_CREATURE:"Creature of choice", TARGET_OPPONENT:"Opponent", TARGET_PLAYERS:"Player of choice", TARGET_RANDOM:"Random Character", TARGET_RANDOM_ENEMY:"Random Enemy", TARGET_RANDOM_ALLY:"Random Ally", TARGET_RANDOM_CREATURE:"Random Creature", TARGET_RANDOM_ENEMY_CREATURE:"Random Enemy Creature", TARGET_RANDOM_ALLY_CREATURE:"Random Ally Creature", TARGET_ALL_CREATURE:"All Creatures", TARGET_THIS_CREATURE:"This Card"}
TARGET_COST_DICT = {TARGET_BOTH:.6, TARGET_ALL:2, TARGET_OWN_PLAYER:-1, TARGET_CREATURE:1.3, TARGET_OPPONENT:1, TARGET_PLAYERS:1, TARGET_RANDOM:.6, TARGET_RANDOM_ENEMY:.8, TARGET_RANDOM_ALLY:-.8, TARGET_RANDOM_CREATURE:.6, TARGET_RANDOM_ENEMY_CREATURE:.8, TARGET_RANDOM_ALLY_CREATURE:-.8, TARGET_ALL_CREATURE:2, TARGET_THIS_CREATURE:-1}
TARGET_UNIVERSAL_POSITIVE = (TARGET_BOTH, TARGET_ALL, TARGET_CREATURE, TARGET_PLAYERS, TARGET_RANDOM, TARGET_RANDOM_CREATURE, TARGET_ALL_CREATURE)
RANDOM_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ALLY, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_CREATURE)
SELF_TARGET_LIST = (TARGET_THIS_CREATURE,)
SINGLE_CREATURE_TARGET_LIST = (TARGET_THIS_CREATURE, TARGET_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE)

SINGLE_CREATURE_DETERMINED_TARGET_LIST = (TARGET_THIS_CREATURE, TARGET_CREATURE)
SPELL_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE)

#Texts used in card rendering in Board
TRIGGER_TEXT_DICT = {TRIGGER_END:"at the end of your turn", TRIGGER_BEGIN:"at the start of your turn", TRIGGER_PLAY:"when you play this card", TRIGGER_DEATH:"when this creature dies"}
TARGET_TEXT_DICT = {TARGET_BOTH:"both Players", TARGET_ALL:"all creatures and players", TARGET_OWN_PLAYER:"you", TARGET_CREATURE:"target creature", TARGET_OPPONENT:"your opponent", TARGET_PLAYERS:"target player", TARGET_RANDOM:"a random creature or player", TARGET_RANDOM_ENEMY:"a random enemy", TARGET_RANDOM_ALLY:"a random ally", TARGET_RANDOM_CREATURE:"a random creature", TARGET_RANDOM_ENEMY_CREATURE:"a random enemy creature", TARGET_RANDOM_ALLY_CREATURE:"a random ally creature", TARGET_ALL_CREATURE:"all creatures", TARGET_THIS_CREATURE:"this creature"}
#NOT_THIS_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE)

#Classes, Class Decoder Dictionary
CLASS_PLAYER = 0
CLASS_CARDS = 1
CLASS_HANDS = 2
CLASS_DECK = 3
CLASS_CREATURE = 4
EFFECT_CLASS_DICT = {DRAW_EFFECT:CLASS_PLAYER, DEAL_EFFECT:CLASS_CARDS, HEAL_EFFECT:CLASS_CARDS, SUMMON_EFFECT:CLASS_PLAYER, BUFF_EFFECT:CLASS_CREATURE, SPLIT_DEAL_EFFECT:CLASS_CARDS, SPLIT_HEAL_EFFECT:CLASS_CARDS, TAUNT_EFFECT:CLASS_CARDS, DIVINE_SHIELD_EFFECT:CLASS_CARDS, CHARGE_EFFECT:CLASS_CARDS, WINDFURY_EFFECT:CLASS_CARDS}
EFFECT_TRIGGER_DICT = {DRAW_EFFECT:TRIGGER_LIST, DEAL_EFFECT:TRIGGER_LIST, HEAL_EFFECT:TRIGGER_LIST, SUMMON_EFFECT:TRIGGER_LIST, BUFF_EFFECT:TRIGGER_LIST, SPLIT_DEAL_EFFECT:TRIGGER_LIST, SPLIT_HEAL_EFFECT:TRIGGER_LIST, TAUNT_EFFECT:PLAY_TRIGGER_LIST, DIVINE_SHIELD_EFFECT:PLAY_TRIGGER_LIST, CHARGE_EFFECT:PLAY_TRIGGER_LIST, WINDFURY_EFFECT:PLAY_TRIGGER_LIST}
EFFECT_TARGET_DICT = {DRAW_EFFECT:PLAYER_TARGET_LIST, DEAL_EFFECT:TARGET_LIST, HEAL_EFFECT:TARGET_LIST, SUMMON_EFFECT:PLAYER_TARGET_LIST, BUFF_EFFECT:CREATURE_TARGET_LIST, SPLIT_DEAL_EFFECT:RANDOM_TARGET_LIST, SPLIT_HEAL_EFFECT:RANDOM_TARGET_LIST, TAUNT_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST, DIVINE_SHIELD_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST, CHARGE_EFFECT:SELF_TARGET_LIST, WINDFURY_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST}
TRIGGER_TARGET_DICT = {TRIGGER_END:TARGET_LIST, TRIGGER_BEGIN:TARGET_LIST, TRIGGER_PLAY:TARGET_LIST, TRIGGER_DEATH:SPELL_TARGET_LIST}

#Sorted Cost Dictionaries from Minimum cost to maximum cost.  Used to identify the least costly effect.
SORTED_EFFECT_COST = sorted(EFFECT_COST_DICT.items(), key=operator.itemgetter(1))
SORTED_TRIGGER_COST = sorted(TRIGGER_COST_DICT.items(), key=operator.itemgetter(1))
SORTED_TARGET_COST = sorted(TARGET_COST_DICT.items(), key=operator.itemgetter(1))

CREATURE_EFFECT_POSSIBILITIES = []
for i in EFFECT_LIST:
    Trigger_And_Targets = []
    for j in EFFECT_TRIGGER_DICT[i]:
        Targets = []
        for k in EFFECT_TARGET_DICT[i]:
            if not k in TRIGGER_TARGET_DICT[j]:
                continue
            #if i in STATIC_EFFECT_LIST:
            #    j = TRIGGER_PLAY
            #    k = TARGET_THIS_CREATURE
            eff_cost = EFFECT_COST_DICT[i] * TRIGGER_COST_DICT[j] * TARGET_COST_DICT[k]
            if k in TARGET_UNIVERSAL_POSITIVE:
                eff_cost = abs(eff_cost)
            Targets.append((k, eff_cost))
        Trigger_And_Targets.append((j, Targets))
    CREATURE_EFFECT_POSSIBILITIES.append((i, Trigger_And_Targets))

SPELL_EFFECT_POSSIBILITIES = []
for i in EFFECT_LIST:
    #if i in STATIC_EFFECT_LIST:
    #    continue
    Trigger_And_Targets = []
    for j in (TRIGGER_PLAY,):
        Targets = []
        for k in EFFECT_TARGET_DICT[i]:
            if not k in SPELL_TARGET_LIST:
                continue
            #if i in STATIC_EFFECT_LIST:
            #    j = TRIGGER_PLAY
            #    k = TARGET_THIS_CREATURE
            eff_cost = EFFECT_COST_DICT[i] * TRIGGER_COST_DICT[j] * TARGET_COST_DICT[k]
            if k in TARGET_UNIVERSAL_POSITIVE:
                eff_cost = abs(eff_cost)
            Targets.append((k, eff_cost))
        Trigger_And_Targets.append((j, Targets))
    SPELL_EFFECT_POSSIBILITIES.append((i, Trigger_And_Targets))
MIN_EFF_COST = EFFECT_COST_DICT[DEAL_EFFECT] * TRIGGER_COST_DICT[TRIGGER_PLAY] * TARGET_COST_DICT[TARGET_CREATURE]#SPELL_EFFECT_POSSIBILITIES[DEAL_EFFECT][1][TRIGGER_PLAY][1][TARGET_CREATURE][1]

#for j,ls in CREATURE_EFFECT_POSSIBILITIES[10][1]:
#    for k in ls:
#        print(TARGET_DICT[k[0]])
#V######################V#

#Constants for rendering the Field
PLAYER_CARD_FONT_SIZE = 35
PLAYER_HEALTH_FONT_SIZE = 100
CREATURE_CARD_FONT_SIZE = 20
CREATURE_STATS_FONT_SIZE = 30
MANA_COST_FONT_SIZE = 40

CARD_WIDTH = 150
CARD_HEIGHT = 210
