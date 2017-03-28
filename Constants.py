"""
Python File to contain Constants for Card Game
"""
import operator

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

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
MANA_CURVE = [0.04973162330165214, 0.11935589592396513, 0.18898016854627814, 0.18898016854627814, 0.15914119456528683, 0.11559168664589639, 0.069624272622313, 0.044758460971486926, 0.029838973980991283, 0.020398532937511128, 0.013599021958340752]

#SUMMON_CURVE = [0.1, 0.3, 0.4, 0.15, 0.05, 0, 0, 0, 0, 0, 0]

ATT_PREF_MULTIPLIER = 1.05 # Set Preference of Attack over Defense and Effects
DEF_PREF_MULTIPLIER = 1.05 # Set Preference of Defense over Attack and Effects
EFFECT_PREF_MULTIPLIER = .9 # Set Preference of Effects over Defense and Attack
PREF_MULTIPLIERS = (ATT_PREF_MULTIPLIER, DEF_PREF_MULTIPLIER, EFFECT_PREF_MULTIPLIER) #Put multipliers in tuple together
EFFECT_THRESHOLD = .5 #(Outdated) Maximum wasted effect potential when generating effect for card
MIN_EFFECT = .5 #if an object is supposed to have an effect, this gives the initial value that it has to be at least.
CARD_STRENGTH = 1.8 #Overall strength of the generated cards
CARD_STRENGTH_DROPOFF = .075 #Amount of lost potential in higher cost cards (the larger this is, the less op high mana cards are relative to lower cost cards)
CARD_INITIAL_STRENGTH = 1 # Effective cost increase for every card
SPELL_EFFECT_MULTIPLIER = 3.5
LEFTOVER_MULTIPLIER = .75 #Percent of leftover spending from effect generation that is effective for stats
EFFECT_CHANCE = 0.5 #Chance that a given card that can have an effect has one.
SPELL_CHANCE = .25

#MANA_CURVE_CDF = [sum(MANA_CURVE[:i+1]) for i in range(len(MANA_CURVE))]
#psum = sum(MANA_SPLIT)
#MANA_SPLIT = [i / psum for i in MANA_SPLIT]


MAX_COST = 10 #Maximum possible Cost
MAX_ATT = 10 #Maximum Attack
MAX_DEF = 10 #Maximum Defense
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
EFFECT_LIST = (DRAW_EFFECT, DEAL_EFFECT, HEAL_EFFECT, SUMMON_EFFECT, BUFF_EFFECT, SPLIT_DEAL_EFFECT, SPLIT_HEAL_EFFECT)
EFFECT_DICT = {None:"None",DRAW_EFFECT:"Draw Cards", DEAL_EFFECT:"Deal Damage", HEAL_EFFECT:"Heal", SUMMON_EFFECT:"Summon Creature", BUFF_EFFECT:"Buff Card", SPLIT_DEAL_EFFECT:"Split Damage", SPLIT_HEAL_EFFECT:"Split Heal"}
EFFECT_COST_DICT = {DRAW_EFFECT:-1.5, DEAL_EFFECT:1, HEAL_EFFECT:-.6, SUMMON_EFFECT:-1.5, BUFF_EFFECT:-1.25, SPLIT_DEAL_EFFECT:1.2, SPLIT_HEAL_EFFECT:-1.2}#Split Damage and heal are so high because they only work with random targets which have low values, this offsets them a bit #This converts the identity of the effect to the cost of it when generating effects


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
TRIGGER_COST_DICT = {TRIGGER_END:2, TRIGGER_BEGIN:1.5, TRIGGER_PLAY:1, TRIGGER_DEATH:1} # Converts identity of triggers to cost

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
TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE) #TARGET_THIS_CREATURE)
PLAYER_TARGET_LIST = (TARGET_BOTH, TARGET_OWN_PLAYER, TARGET_OPPONENT, TARGET_PLAYERS)
CREATURE_TARGET_LIST = (TARGET_CREATURE, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_ALL_CREATURE, TARGET_THIS_CREATURE)
TARGET_DICT = {TARGET_BOTH:"Both Players", TARGET_ALL:"All Characters", TARGET_OWN_PLAYER:"Own Player", TARGET_CREATURE:"Creature of choice", TARGET_OPPONENT:"Opponent", TARGET_PLAYERS:"Player of choice", TARGET_RANDOM:"Random Character", TARGET_RANDOM_ENEMY:"Random Enemy", TARGET_RANDOM_ALLY:"Random Ally", TARGET_RANDOM_CREATURE:"Random Creature", TARGET_RANDOM_ENEMY_CREATURE:"Random Enemy Creature", TARGET_RANDOM_ALLY_CREATURE:"Random Ally Creature", TARGET_ALL_CREATURE:"All Creatures", TARGET_THIS_CREATURE:"This Card"}
TARGET_COST_DICT = {TARGET_BOTH:.5, TARGET_ALL:1.5, TARGET_OWN_PLAYER:-1, TARGET_CREATURE:1.2, TARGET_OPPONENT:1, TARGET_PLAYERS:1.1, TARGET_RANDOM:.5, TARGET_RANDOM_ENEMY:.8, TARGET_RANDOM_ALLY:-.8, TARGET_RANDOM_CREATURE:.6, TARGET_RANDOM_ENEMY_CREATURE:.8, TARGET_RANDOM_ALLY_CREATURE:-.8, TARGET_ALL_CREATURE:1.5, TARGET_THIS_CREATURE:-1}
TARGET_UNIVERSAL_POSITIVE = (TARGET_BOTH, TARGET_ALL, TARGET_CREATURE, TARGET_PLAYERS, TARGET_RANDOM, TARGET_RANDOM_CREATURE, TARGET_ALL_CREATURE)
RANDOM_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ALLY, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_CREATURE)

#Texts used in card rendering in Board
EFFECT_TRIGGER_DICT = {TRIGGER_END:"at the end of your turn", TRIGGER_BEGIN:"at the start of your turn", TRIGGER_PLAY:"when you play this card", TRIGGER_DEATH:"when this creature dies"}
TARGET_TEXT_DICT = {TARGET_BOTH:"both Players", TARGET_ALL:"all creatures and players", TARGET_OWN_PLAYER:"you", TARGET_CREATURE:"target creature", TARGET_OPPONENT:"your opponent", TARGET_PLAYERS:"target player", TARGET_RANDOM:"a random creature or player", TARGET_RANDOM_ENEMY:"a random enemy", TARGET_RANDOM_ALLY:"a random ally", TARGET_RANDOM_CREATURE:"a random creature", TARGET_RANDOM_ENEMY_CREATURE:"a random enemy creature", TARGET_RANDOM_ALLY_CREATURE:"a random ally creature", TARGET_ALL_CREATURE:"all creatures", TARGET_THIS_CREATURE:"this creature"}

#Classes, Class Decoder Dictionary
CLASS_PLAYER = 0
CLASS_CARDS = 1
CLASS_HANDS = 2
CLASS_DECK = 3
CLASS_CREATURE = 4
EFFECT_CLASS_DICT = {DRAW_EFFECT:CLASS_PLAYER, DEAL_EFFECT:CLASS_CARDS, HEAL_EFFECT:CLASS_CARDS, SUMMON_EFFECT:CLASS_PLAYER, BUFF_EFFECT:CLASS_CREATURE, SPLIT_DEAL_EFFECT:CLASS_CARDS, SPLIT_HEAL_EFFECT:CLASS_CARDS}
EFFECT_TARGET_DICT = {DRAW_EFFECT:PLAYER_TARGET_LIST, DEAL_EFFECT:TARGET_LIST, HEAL_EFFECT:TARGET_LIST, SUMMON_EFFECT:PLAYER_TARGET_LIST, BUFF_EFFECT:CREATURE_TARGET_LIST, SPLIT_DEAL_EFFECT:RANDOM_TARGET_LIST, SPLIT_HEAL_EFFECT:RANDOM_TARGET_LIST}

#Sorted Cost Dictionaries from Minimum cost to maximum cost.  Used to identify the least costly effect.
SORTED_EFFECT_COST = sorted(EFFECT_COST_DICT.items(), key=operator.itemgetter(1))
SORTED_TRIGGER_COST = sorted(TRIGGER_COST_DICT.items(), key=operator.itemgetter(1))
SORTED_TARGET_COST = sorted(TARGET_COST_DICT.items(), key=operator.itemgetter(1))

EFFECT_POSSIBILITIES = []
for i in EFFECT_LIST:
    for j in TRIGGER_LIST:
        for k in EFFECT_TARGET_DICT[i]:
            eff_cost = EFFECT_COST_DICT[i] * TRIGGER_COST_DICT[j] * TARGET_COST_DICT[k]
            if k in TARGET_UNIVERSAL_POSITIVE:
                eff_cost = abs(eff_cost)
            EFFECT_POSSIBILITIES.append((i, j, k, eff_cost))
