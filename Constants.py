"""
Python File to contain Constants for Card Game
"""

DECK_INIT_SIZE = 30
MAX_NUMERIC = 3
HAND_INIT_SIZE = 4

NAME_LIST = ["Bird", "Robot Doctor", "Magic Stones", "Test Card", "JEREMEEEEE"]

TYPE_CREATURE = 0
TYPE_SPELL = 1
TYPE_LIST = (TYPE_CREATURE, TYPE_SPELL)
TYPE_DICT = {None:"None",TYPE_CREATURE:"Creature", TYPE_SPELL:"Spell"}


MAX_DEF = 10
MAX_ATT = 10
MAX_COST = 10
MAX_STATS = [MAX_COST, MAX_ATT, MAX_DEF]

STATE_SLEEP = 0
STATE_ACTIVE = 1
STATE_LIST = (STATE_SLEEP, STATE_ACTIVE)
STATE_DICT = {None:"None",0:"Sleep", 1:"Active"}

DRAW_EFFECT = 0
DEAL_EFFECT = 1
EFFECT_LIST = (DRAW_EFFECT, DEAL_EFFECT)
EFFECT_DICT = {None:"None",DRAW_EFFECT:"Draw", DEAL_EFFECT:"Deal"}
EFFECT_CHANCE = .5

CREATURE_MECH = 0
CREATURE_BEAST = 1
CREATURE_LIST = (None, CREATURE_MECH, CREATURE_BEAST) #CAREFUL, THIS LIST HAS NONE IN IT AS WELL.
CREATURE_DICT = {None:"None",CREATURE_MECH:"Mech", CREATURE_BEAST:"Beast"}

TRIGGER_PLAY = 0
TRIGGER_DEATH = 1
TRIGGER_LIST = (None, TRIGGER_PLAY, TRIGGER_DEATH)
TRIGGER_DICT = {None:"None",TRIGGER_PLAY:"Play", TRIGGER_DEATH:"Death"}
