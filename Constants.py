"""
Python File to contain Constants for Card Game
"""
import operator
import random

WINDOW_WIDTH = 1850
WINDOW_HEIGHT = 1020

DECK_INIT_SIZE = 30 #Initial Deck Size
MAX_NUMERIC = 3 #(Outdated?) Maximum Numerical Value On Effects
MAX_NEGATIVE_NUMERIC = 5
HAND_INIT_SIZE = 3 # Initial Hand Size
HAND_MAX_SIZE = 10 # Maximum Hand Size, Need To Actually Impliment
CARDS_DRAWN_PER_TURN = 1
SECOND_PLAYER_CARD_BONUS = 1
MAX_BOARD_SIZE = 7
FATIGUE = True
MINION_RECOVER = False

#COLORS
PURPLE = (225, 50, 225)

#NAME_LIST = ["Bird", "Robot Doctor", "Magic Stones", "Test Card", "JEREMEEEEE"]

#Integers to represent creature types, list of valid type choices, and dictionary for decoding them
TYPE_CREATURE = 0
TYPE_SPELL = 1
TYPE_LIST = (TYPE_CREATURE, TYPE_SPELL)
TYPE_DICT = {None:"None",TYPE_CREATURE:"Creature", TYPE_SPELL:"Spell"}

COMMON = 0
UNCOMMON = 1
RARE = 2
EPIC = 3
LEGENDARY = 4
RARITIES = (COMMON, UNCOMMON, RARE, EPIC, LEGENDARY) #IN ORDER COMPARED TO RARITY
RARITY_DICT = {COMMON:'Common', UNCOMMON:'Uncommon', RARE:'Rare', EPIC:'Epic', LEGENDARY:'Legendary'}
POWER_DICT = {COMMON:(1.85, .35, 1.3), UNCOMMON:(1.85,.45, 1.5), RARE:(1.85,.5,1.7), EPIC:(1.85,.575,2.0), LEGENDARY:(1.85,.7, 2.5)}
#EFFECT_DICT = {COMMON:1.55, UNCOMMON:1.65, RARE:1.75, EPIC:1.85, LEGENDARY:2}
INPUT_RARITY = [.375, .325, .2, .1, .05]    #Card rarity
totrarprobs = sum(INPUT_RARITY)
RARITY_PROBS = [i/totrarprobs for i in INPUT_RARITY]
DEFAULT_RARITY = RARE

PLAYER_HEALTH = 30 #Player Health
PLAYER_ATTACK = 0

COST = 0 #Cost index in stats
ATT = 1 #Attack index in stats
DEF = 2 #Defense index in stats

MAX_MANA = 10 #Maximum Mana in a Turn
MANA_PER_TURN = 1 #Mana gain per turn
TEMP_MANA = True #Whether or not you have temporary mana
MANA_LIMIT = 2*MAX_MANA #The max mana for when you have permament mana

#Mana curve for card cost generation: Pre-generated List of probabilities.
MANA_CURVE = [0.04973162330165214, 0.11935589592396513, 0.18898016854627814, 0.18898016854627814, 0.15914119456528683, 0.11559168664589639, 0.065624272622313, 0.037758460971486926, 0.023838973980991283, 0.015398532937511128, 0.010599021958340752]
tot = sum(MANA_CURVE)
MANA_CURVE = [i/tot for i in MANA_CURVE]
#SUMMON_CURVE = [0.1, 0.3, 0.4, 0.15, 0.05, 0, 0, 0, 0, 0, 0]

ATT_PREF_MULTIPLIER = 1 # Set Preference of Attack over Defense
DEF_PREF_MULTIPLIER = 1 # Set Preference of Defense over Attack
#STATS_PREF = 1.1   #Should be about twice the Effect_Pref # Stats Preference over Other Stuff
#EFFECT_PREF = .9   # Set Preference of Effects over Defense and Attack
#TOT_PREF = STATS_PREF+EFFECT_PREF
PREF_MULTIPLIERS = (ATT_PREF_MULTIPLIER, DEF_PREF_MULTIPLIER) #Put multipliers in tuple together
EFFECT_THRESHOLD = 1.5 #Maximum wasted effect potential when generating effect for card (used to make spells spend all their effect juice)
MIN_EFFECT = .5 #if an object is supposed to have an effect, this gives the initial value that it has to be at least.
CARD_STRENGTH = 1.7 #Overall strength of the generated cards
CARD_STRENGTH_DROPOFF = 0 #Amount of lost potential in higher cost cards (the larger this is, the less op high mana cards are relative to lower cost cards)
CARD_INITIAL_STRENGTH = .8 # Effective cost increase for every card
SPELL_EFFECT_MULTIPLIER = .44
LEFTOVER_MULTIPLIER = .75 #Percent of leftover spending from effect generation that is effective for stats
EFFECT_CHANCE = 0.7 #Chance that a given card that can have an effect has one.
DOUBLE_EFFECT_CHANCE = .33
SPELL_CHANCE = .25
SPELL_ADDER = 1
EFFECT_TRY_NUM = 40
#NEGATIVE_ADDER = 1
#ZERO_STRENGTH = 1.5
MINCHOICE = 2
MAXCHOICE = 4
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
DEBUFF_EFFECT = 11
DESTROY_EFFECT = 12
FREEZE_EFFECT = 13
RETURN_EFFECT = 14
REANIMATE_EFFECT = 15
DEVOLVE_EFFECT = 16
REVOLVE_EFFECT = 17
EVOLVE_EFFECT = 18
AMANA_EFFECT = 19
RMANA_EFFECT = 20


#-----------ORDER MATTERS WITH ALL OF THESE LISTS AND COST DICTIONARIES, THEY NEED TO HAVE THE SAME ORDER--------------#
EFFECT_LIST = (DRAW_EFFECT, DEAL_EFFECT, HEAL_EFFECT, SUMMON_EFFECT, BUFF_EFFECT, SPLIT_DEAL_EFFECT, SPLIT_HEAL_EFFECT, TAUNT_EFFECT, DIVINE_SHIELD_EFFECT, CHARGE_EFFECT, WINDFURY_EFFECT, DEBUFF_EFFECT, DESTROY_EFFECT, FREEZE_EFFECT, RETURN_EFFECT, REANIMATE_EFFECT, DEVOLVE_EFFECT, REVOLVE_EFFECT, EVOLVE_EFFECT, AMANA_EFFECT, RMANA_EFFECT)
EFFECT_DICT = {None:"None",DRAW_EFFECT:"Draw Cards", DEAL_EFFECT:"Deal Damage", HEAL_EFFECT:"Heal", SUMMON_EFFECT:"Summon Creature", BUFF_EFFECT:"Buff Card", SPLIT_DEAL_EFFECT:"Split Damage", SPLIT_HEAL_EFFECT:"Split Heal", TAUNT_EFFECT:"Give Taunt", DIVINE_SHIELD_EFFECT:"Give Divine Shield", CHARGE_EFFECT:"Give Charge", WINDFURY_EFFECT:"Give Windfury", DEBUFF_EFFECT:"Give Debuff", DESTROY_EFFECT:"Destroy Creature", FREEZE_EFFECT:"Freeze Creature", RETURN_EFFECT: "Return Creature to Hand",  REANIMATE_EFFECT: "Revive Creature", DEVOLVE_EFFECT:"Devolve", REVOLVE_EFFECT:"Revolve", EVOLVE_EFFECT:"Evolve", AMANA_EFFECT:"Gain Mana Temporarily", RMANA_EFFECT:"Lose Mana Next Turn"}
EFFECT_COST_DICT = {DRAW_EFFECT:-1.7, DEAL_EFFECT:1, HEAL_EFFECT:-.75, SUMMON_EFFECT:-1.0, BUFF_EFFECT:-1, SPLIT_DEAL_EFFECT:1, SPLIT_HEAL_EFFECT:-.75, TAUNT_EFFECT:-1.5, DIVINE_SHIELD_EFFECT:-2.5, CHARGE_EFFECT:-2, WINDFURY_EFFECT:-3.5, DEBUFF_EFFECT:1.35, DESTROY_EFFECT:4.5, FREEZE_EFFECT:2.25, RETURN_EFFECT:2, REANIMATE_EFFECT:-2, DEVOLVE_EFFECT:2, REVOLVE_EFFECT:1, EVOLVE_EFFECT:-1.5, AMANA_EFFECT:-1.35, RMANA_EFFECT:1.35} #Split Damage and heal are so high because they only work with random targets which have low values, this offsets them a bit #This converts the identity of the effect to the cost of it when generating effects
STATIC_EFFECT_LIST = (TAUNT_EFFECT, DIVINE_SHIELD_EFFECT, CHARGE_EFFECT, WINDFURY_EFFECT, FREEZE_EFFECT, DEVOLVE_EFFECT, REVOLVE_EFFECT, EVOLVE_EFFECT)

TAUNT_INDEX = 0
DIVINE_SHIELD_INDEX = 1
CHARGE_INDEX = 2
WINDFURY_INDEX = 3
FROZEN_INDEX = 4
INIT_ACTIVE_EFFECT = [0,0,0,0,0]
ACTIVE_EFFECT_DICT = {0:"Taunt", 1:"Divine Shield", 2:"Charge", 3:"Windfury", 4:"Frozen"}

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
TRIGGER_COST_DICT = {TRIGGER_END:2.2, TRIGGER_BEGIN:1.5, TRIGGER_PLAY:1.15, TRIGGER_DEATH:1} # Converts identity of triggers to cost
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
TARGET_ALL_ENEMY_CREATURE = 14
TARGET_ALL_ALLY_CREATURE = 15
TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE, TARGET_THIS_CREATURE, TARGET_ALL_ENEMY_CREATURE, TARGET_ALL_ALLY_CREATURE)
PLAYER_TARGET_LIST = (TARGET_BOTH, TARGET_OWN_PLAYER, TARGET_OPPONENT, TARGET_PLAYERS)
CREATURE_TARGET_LIST = (TARGET_CREATURE, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_ALL_CREATURE, TARGET_THIS_CREATURE, TARGET_ALL_ENEMY_CREATURE, TARGET_ALL_ALLY_CREATURE)
NOT_ME_CREATURE_TARGET_LIST = (TARGET_CREATURE, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_ALL_CREATURE, TARGET_ALL_ENEMY_CREATURE, TARGET_ALL_ALLY_CREATURE)
TARGET_DICT = {TARGET_BOTH:"Both Players", TARGET_ALL:"All Characters", TARGET_OWN_PLAYER:"Own Player", TARGET_CREATURE:"Creature of choice", TARGET_OPPONENT:"Opponent", TARGET_PLAYERS:"Player of choice", TARGET_RANDOM:"Random Character", TARGET_RANDOM_ENEMY:"Random Enemy", TARGET_RANDOM_ALLY:"Random Ally", TARGET_RANDOM_CREATURE:"Random Creature", TARGET_RANDOM_ENEMY_CREATURE:"Random Enemy Creature", TARGET_RANDOM_ALLY_CREATURE:"Random Ally Creature", TARGET_ALL_CREATURE:"All Creatures", TARGET_THIS_CREATURE:"This Card", TARGET_ALL_ENEMY_CREATURE:'All Enemy Creatures', TARGET_ALL_ALLY_CREATURE:'All Ally Creatures'}
TARGET_COST_DICT = {TARGET_BOTH:.6, TARGET_ALL:2, TARGET_OWN_PLAYER:-1, TARGET_CREATURE:1.15, TARGET_OPPONENT:1, TARGET_PLAYERS:1, TARGET_RANDOM:.6, TARGET_RANDOM_ENEMY:.8, TARGET_RANDOM_ALLY:-.8, TARGET_RANDOM_CREATURE:.6, TARGET_RANDOM_ENEMY_CREATURE:.8, TARGET_RANDOM_ALLY_CREATURE:-.8, TARGET_ALL_CREATURE:2, TARGET_THIS_CREATURE:-1, TARGET_ALL_ENEMY_CREATURE:2, TARGET_ALL_ALLY_CREATURE:-2}
TARGET_UNIVERSAL_POSITIVE = (TARGET_BOTH, TARGET_ALL, TARGET_CREATURE, TARGET_PLAYERS, TARGET_RANDOM, TARGET_RANDOM_CREATURE, TARGET_ALL_CREATURE)
RANDOM_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ALLY, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_CREATURE)
SELF_TARGET_LIST = (TARGET_THIS_CREATURE,)
SINGLE_CREATURE_TARGET_LIST = (TARGET_THIS_CREATURE, TARGET_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_RANDOM_ENEMY_CREATURE)

SINGLE_CREATURE_DETERMINED_TARGET_LIST = (TARGET_THIS_CREATURE, TARGET_CREATURE)
SPELL_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE)

#Texts used in card rendering in Board
#TRIGGER_TEXT_DICT = {TRIGGER_END:"at the end of your turn", TRIGGER_BEGIN:"at the start of your turn", TRIGGER_PLAY:"when you play this card", TRIGGER_DEATH:"when this creature dies"}
TRIGGER_TEXT_DICT = {TRIGGER_END:"on turn end:", TRIGGER_BEGIN:"on turn begin:", TRIGGER_PLAY:"on play:", TRIGGER_DEATH:"on death:"}
#TARGET_TEXT_DICT = {TARGET_BOTH:"both Players", TARGET_ALL:"all creatures and players", TARGET_OWN_PLAYER:"you", TARGET_CREATURE:"target creature", TARGET_OPPONENT:"your opponent", TARGET_PLAYERS:"target player", TARGET_RANDOM:"a random creature or player", TARGET_RANDOM_ENEMY:"a random enemy", TARGET_RANDOM_ALLY:"a random ally", TARGET_RANDOM_CREATURE:"a random creature", TARGET_RANDOM_ENEMY_CREATURE:"a random enemy creature", TARGET_RANDOM_ALLY_CREATURE:"a random ally creature", TARGET_ALL_CREATURE:"all creatures", TARGET_THIS_CREATURE:"this creature", TARGET_ALL_ENEMY_CREATURE:'all enemy creatures', TARGET_ALL_ALLY_CREATURE:'all ally creatures'}
TARGET_TEXT_DICT = {TARGET_BOTH:"both Players", TARGET_ALL:"everyone", TARGET_OWN_PLAYER:"you", TARGET_CREATURE:"target creature", TARGET_OPPONENT:"opponent", TARGET_PLAYERS:"target player", TARGET_RANDOM:"a random target", TARGET_RANDOM_ENEMY:"a random enemy", TARGET_RANDOM_ALLY:"a random ally", TARGET_RANDOM_CREATURE:"a random creature", TARGET_RANDOM_ENEMY_CREATURE:"a random enemy creature", TARGET_RANDOM_ALLY_CREATURE:"a random ally creature", TARGET_ALL_CREATURE:"all creatures", TARGET_THIS_CREATURE:"this creature", TARGET_ALL_ENEMY_CREATURE:'all enemy creatures', TARGET_ALL_ALLY_CREATURE:'all ally creatures'}
#NOT_THIS_TARGET_LIST = (TARGET_RANDOM, TARGET_RANDOM_ENEMY, TARGET_RANDOM_ALLY, TARGET_ALL, TARGET_OWN_PLAYER, TARGET_CREATURE, TARGET_OPPONENT, TARGET_PLAYERS, TARGET_BOTH, TARGET_RANDOM_CREATURE, TARGET_RANDOM_ENEMY_CREATURE, TARGET_RANDOM_ALLY_CREATURE, TARGET_ALL_CREATURE)

ONE_DO_EFFECTS = (DESTROY_EFFECT,)


#Classes, Class Decoder Dictionary
CLASS_PLAYER = 0
CLASS_CARDS = 1
CLASS_HANDS = 2
CLASS_DECK = 3
CLASS_CREATURE = 4
EFFECT_CLASS_DICT = {DRAW_EFFECT:CLASS_PLAYER, DEAL_EFFECT:CLASS_CARDS, HEAL_EFFECT:CLASS_CARDS, SUMMON_EFFECT:CLASS_PLAYER, BUFF_EFFECT:CLASS_CREATURE, SPLIT_DEAL_EFFECT:CLASS_CARDS, SPLIT_HEAL_EFFECT:CLASS_CARDS, TAUNT_EFFECT:CLASS_CARDS, DIVINE_SHIELD_EFFECT:CLASS_CARDS, CHARGE_EFFECT:CLASS_CARDS, WINDFURY_EFFECT:CLASS_CARDS, DEBUFF_EFFECT:CLASS_CREATURE, DESTROY_EFFECT:CLASS_CREATURE, FREEZE_EFFECT:CLASS_CREATURE, RETURN_EFFECT:CLASS_CREATURE, REANIMATE_EFFECT:CLASS_PLAYER, DEVOLVE_EFFECT:CLASS_CREATURE, REVOLVE_EFFECT:CLASS_CREATURE, EVOLVE_EFFECT:CLASS_CREATURE, AMANA_EFFECT:CLASS_PLAYER, RMANA_EFFECT:CLASS_PLAYER}
EFFECT_TRIGGER_DICT = {DRAW_EFFECT:TRIGGER_LIST, DEAL_EFFECT:TRIGGER_LIST, HEAL_EFFECT:TRIGGER_LIST, SUMMON_EFFECT:TRIGGER_LIST, BUFF_EFFECT:TRIGGER_LIST, SPLIT_DEAL_EFFECT:TRIGGER_LIST, SPLIT_HEAL_EFFECT:TRIGGER_LIST, TAUNT_EFFECT:PLAY_TRIGGER_LIST, DIVINE_SHIELD_EFFECT:PLAY_TRIGGER_LIST, CHARGE_EFFECT:PLAY_TRIGGER_LIST, WINDFURY_EFFECT:PLAY_TRIGGER_LIST, DEBUFF_EFFECT:TRIGGER_LIST, DESTROY_EFFECT:TRIGGER_LIST, FREEZE_EFFECT:TRIGGER_LIST, RETURN_EFFECT:TRIGGER_LIST, REANIMATE_EFFECT:TRIGGER_LIST, DEVOLVE_EFFECT:TRIGGER_LIST, REVOLVE_EFFECT:TRIGGER_LIST, EVOLVE_EFFECT:TRIGGER_LIST, AMANA_EFFECT:TRIGGER_LIST, RMANA_EFFECT:TRIGGER_LIST}
EFFECT_TARGET_DICT = {DRAW_EFFECT:PLAYER_TARGET_LIST, DEAL_EFFECT:TARGET_LIST, HEAL_EFFECT:TARGET_LIST, SUMMON_EFFECT:PLAYER_TARGET_LIST, BUFF_EFFECT:CREATURE_TARGET_LIST, SPLIT_DEAL_EFFECT:RANDOM_TARGET_LIST, SPLIT_HEAL_EFFECT:RANDOM_TARGET_LIST, TAUNT_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST, DIVINE_SHIELD_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST, CHARGE_EFFECT:SELF_TARGET_LIST, WINDFURY_EFFECT:SINGLE_CREATURE_DETERMINED_TARGET_LIST, DEBUFF_EFFECT:CREATURE_TARGET_LIST, DESTROY_EFFECT:NOT_ME_CREATURE_TARGET_LIST, FREEZE_EFFECT:CREATURE_TARGET_LIST, RETURN_EFFECT:CREATURE_TARGET_LIST, REANIMATE_EFFECT:PLAYER_TARGET_LIST, DEVOLVE_EFFECT:CREATURE_TARGET_LIST, REVOLVE_EFFECT:CREATURE_TARGET_LIST, EVOLVE_EFFECT:CREATURE_TARGET_LIST, AMANA_EFFECT:PLAYER_TARGET_LIST, RMANA_EFFECT:PLAYER_TARGET_LIST}
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
            eff_cost = EFFECT_COST_DICT[i] * TRIGGER_COST_DICT[j] * TARGET_COST_DICT[k]
            if k in TARGET_UNIVERSAL_POSITIVE:
                eff_cost = abs(eff_cost)
            Targets.append((k, eff_cost))
        Trigger_And_Targets.append((j, Targets))
    CREATURE_EFFECT_POSSIBILITIES.append((i, Trigger_And_Targets))

SPELL_EFFECT_POSSIBILITIES = []
for i in EFFECT_LIST:
    Trigger_And_Targets = []
    for j in (TRIGGER_PLAY,):
        Targets = []
        for k in EFFECT_TARGET_DICT[i]:
            if not k in SPELL_TARGET_LIST:
                continue
            eff_cost = EFFECT_COST_DICT[i] * TRIGGER_COST_DICT[j] * TARGET_COST_DICT[k]
            if k in TARGET_UNIVERSAL_POSITIVE:
                eff_cost = abs(eff_cost)
            Targets.append((k, eff_cost))
        Trigger_And_Targets.append((j, Targets))
    SPELL_EFFECT_POSSIBILITIES.append((i, Trigger_And_Targets))
MIN_EFF_COST = EFFECT_COST_DICT[DEAL_EFFECT] * TRIGGER_COST_DICT[TRIGGER_PLAY] * TARGET_COST_DICT[TARGET_CREATURE]#SPELL_EFFECT_POSSIBILITIES[DEAL_EFFECT][1][TRIGGER_PLAY][1][TARGET_CREATURE][1]


#Constants for rendering the Field
PLAYER_CARD_FONT_SIZE = 35
PLAYER_HEALTH_FONT_SIZE = 100
CREATURE_CARD_FONT_SIZE = 15
CREATURE_STATS_FONT_SIZE = 30
MANA_COST_FONT_SIZE = 40
END_TURN_SHAPE = (100, 50)
END_TURN_POS = (WINDOW_WIDTH-END_TURN_SHAPE[0], (WINDOW_HEIGHT-END_TURN_SHAPE[1])/2)

#Define Card Size
CARD_SCALE = 30
CARD_WIDTH = CARD_SCALE * 5
CARD_HEIGHT = CARD_SCALE * 7

"""TODO CONSTANTS (if we want to expand a little); only one left </3
#Need to code in mana-giving
COIN = True #True = given to opponent, False = no coin given
COIN = random.choice([True, False])
"""

RANDOM = False
### RANDOMIZATION PART ###

info = input("Would you like to hear the rules? (y/n): ").lower()
if info == "y":
    print("There are only two players in the game, you and your opponent. The goal of the game is to outlast your opponent and deplete their life points to zero. In the game, there are two types of cards-- “Dudes” and “Dos.” “Dudes,” or creatures/minions/etc. are entities that exist on the board that have a mana cost, health, and attack. Minions can have a variety of effects that can happen on summon, upon death, or at the beginning/end of turns. Minions are able to attack during the attack phase. “Dos,” or spells, have only a cost and one or more effects and can be cast during the “Play” phase. Spells are only cast during this phase. You cast spells and summon minions by spending mana, which is a resource that you get every turn.")
    effs = input("Would you like to hear the explanation of different effects? (y/n): ").lower()
    if effs == "y":
        print("""
Taunt: Minions with Taunt must be attacked before other minions.
Mana Effects: Minions can change the amount of mana you or your opponent receive on their next turn. Mana can be given or taken away.
Divine Shield: Ignore the first amount of damage a minion takes. The shield can be re-applied to minions but each shield only absorbs one damage set.
Windfury: Minions with Windfury can attack twice.
Freeze: Minions cannot attack this turn. They unthaw at the end of the turn.
Deal Damage: Deal x damage to target.
Draw Cards: Target player draws x cards.
Heal: Heal x damage target has sustained.
Evolve: Change creature to a randomly generated creature of one mana cost more.
Revolve: Change creature to a randomly generated creature of the same mana cost.
Devolve: Change creature to a randomly generated creature of one mana cost less.
Return: Return a card that is on the field to a player's hand.
Reanimate: Take a creature out of the graveyard and return it to the field.
NOTE: Names can be randomized, and may be randomized.

              """)
    print("""The following rules will all hold true in a non-randomized game. If you wish to try the random rules, you will get a printed version of the new rules. The rules are as follows:

Player starting health: 30
Deck start size: 30
Hand start size: 3
Hand max size: 10
Max field size: 7
Cards drawn per turn: 1
Mana gained per turn: 1
The maximum mana is 10.
Second turn card bonus: 1
Fatigue is on.
Minion Recovery is off.

""")
    rulee = input("Would you like some more information on the rules? (y/n): ").lower()
    if rulee == "y":
        print("""Hand max size denotes the most cards that you can have in your hand. As you draw at the end of your turn, a good strategy is to have one less than the number of cards the maximum is.
Mana gained per turn means that one more mana is gained than the last turn when compared to the current turn. There is a maximum of 10 mana.
Fatigue occurs when a player runs out of cards. Whenever said player first tries to draw a card, they will take 1 damage. For every subsequent draw, they will take 1 more damage than the last draw.
Minion recovery means that at the conclusion of each player’s turn all minions will be healed to full health.""")


info1 = input("Do you want to hear about how to play? (y/n):").lower()
if info1 == "y":
    print("""

          A player hits the button to start their turn. The player then plays cards out of his or her hand during the “Play” phase of their turn by clicking and dragging their chosen card. Once they have spent all of their mana or wish to stop playing cards, they can choose to end their play phase by clicking on the button in the right again. If there are minions that the player has that can attack, the player then enters attack phase. During this phase, the player can make their minions attack valid targets by clicking on their minion and dragging to the enemy they want to attack. When the player wishes to end their turn or can make no more attacks, they end their turn by clicking on the button again. At this point, end of turn actions will automatically happen. When the next person is ready to begin their turn, they click on the button to reveal their cards.""")
ARENA = False
ans = input('\n \n \nArena mode is when you pick between a random number of cards to choose the best cards for your deck. \nDo you want Arena Mode? (y/n): ')
if ans == 'y':
    ARENA = True
else:
    ARENA = False

#WHERE RANDOMIZATION HAPPENS#
yup = input("Do you want a randomized game (recommended for advanced players) (y/n): ").lower()
if yup.lower() == "y":
    PLAYER_HEALTH = random.randint(20, 50)
    DECK_INIT_SIZE = random.randint(20, 50)
    HAND_MAX_SIZE = random.randint(7, 12)
    HAND_INIT_SIZE = random.randint(2, HAND_MAX_SIZE-4)
    CARDS_DRAWN_PER_TURN = random.randint(1, 2)
    MANA_PER_TURN = random.randint(1,2)
    SECOND_PLAYER_CARD_BONUS = random.randint(0,1)
    MAX_BOARD_SIZE = random.randint(5, 10)
    TEMP_MANA = random.randint(0, 1)
    MANA_LIMIT = random.randint(10, 20)
    MINION_RECOVER = random.randint(0,1)
    FATIGUE = random.randint(0,1)
    RANDOM = True

### PRINT RULES; UPDATE AS RANDOMIZATION IS UPDATED ###
print("""\n \n%sRULES: \n
Player starting health: %s
Deck start size: %s
Hand start size: %s
Hand max size: %s
Max field size: %s
Cards drawn per turn: %s
Mana gained per turn: %s
Second turn card bonus: %s
Fatigue is turned %s
Temporary Mana is turned %s%s
Minion Recovery is turned %s \n \n"""
% (("RANDOMIZED " if RANDOM else ""), PLAYER_HEALTH, DECK_INIT_SIZE, HAND_INIT_SIZE, HAND_MAX_SIZE, MAX_BOARD_SIZE, CARDS_DRAWN_PER_TURN, MANA_PER_TURN, ("Yes" if SECOND_PLAYER_CARD_BONUS else "No"), ("on" if TEMP_MANA else "off"), ("on" if FATIGUE else "off"), ("\nMax Temp Mana: %d" % MANA_LIMIT if not TEMP_MANA else ""), ("on" if MINION_RECOVER else "off")))
irrelevent = input("Press any button when you're ready to begin with the name randomization. Good luck!")
