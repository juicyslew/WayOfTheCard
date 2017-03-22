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

PLAYER_HEALTH = 30

COST = 0
ATT = 1
DEF = 2

MAX_MANA = 10
MANA_PER_TURN = 1


MAX_COST = 10
MAX_ATT = 7
MAX_DEF = 7
MAX_STATS = [MAX_COST, MAX_ATT, MAX_DEF]

STATE_SLEEP = 0
STATE_ACTIVE = 1
STATE_GRAVEYARD = 2
STATE_LIST = (STATE_SLEEP, STATE_ACTIVE)
STATE_DICT = {None:"None",STATE_SLEEP:"Sleep", STATE_ACTIVE:"Active",STATE_GRAVEYARD:"Dead"}

DRAW_EFFECT = 0
DEAL_EFFECT = 1
HEAL_EFFECT = 2
EFFECT_LIST = (DRAW_EFFECT, DEAL_EFFECT, HEAL_EFFECT)
EFFECT_DICT = {None:"None",DRAW_EFFECT:"Draw", DEAL_EFFECT:"Deal", HEAL_EFFECT:"Heal"}
EFFECT_CHANCE = 1

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

TRIGGER_END = 0
TRIGGER_BEGIN = 1
TRIGGER_PLAY = 2
TRIGGER_DEATH = 3
TRIGGER_LIST = (TRIGGER_END, TRIGGER_BEGIN, TRIGGER_PLAY, TRIGGER_DEATH)
TRIGGER_DICT = {TRIGGER_END:"End Turn", TRIGGER_BEGIN:"Begin Turn", TRIGGER_PLAY:"Play", TRIGGER_DEATH:"Death"}

TARGET_ALL = 0
TARGET_SELF = 1
TARGET_CREATURE = 2
TARGET_OPPONENT = 3
TARGET_PLAYERS = 4
TARGET_BOTH = 5
TARGET_LIST = (TARGET_ALL, TARGET_SELF, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH)
DRAW_TARGET_LIST = (TARGET_BOTH, TARGET_SELF, TARGET_OPPONENT, TARGET_PLAYERS)
TARGET_DICT = {TARGET_BOTH:"Both Players", TARGET_ALL:"All", TARGET_SELF:"Own Player", TARGET_CREATURE:"Creatures", TARGET_OPPONENT:"Opponent", TARGET_PLAYERS:"A Player"}

CLASS_PLAYER = 0
CLASS_CARDS = 1
CLASS_HANDS = 2
CLASS_DECK = 3
EFFECT_CLASS_DICT = {DRAW_EFFECT:CLASS_PLAYER, DEAL_EFFECT:CLASS_CARDS, HEAL_EFFECT:CLASS_CARDS }
