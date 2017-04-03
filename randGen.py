import random
import numpy as np
from Constants import *
from math import floor
import operator

class randGen():
    def __init__(self, type = "creature", word_num = random.choice([1, 2, 3])):
        pass

def generate(cardType = TYPE_CREATURE):
    """
    Generates Names for Creatures.
    (ADD COMMENTS)
    """
    word_num = random.choice([1,2,3])
    if cardType == TYPE_CREATURE:
        word_num = random.choice([1,2])
    name = []
    i = 0
    while i < word_num:
        i += 1
        name.append(random.choice(name_list()))
    if cardType == TYPE_CREATURE:
        if random.random() < 0.35:
            name = []
            name.append(random_name())
            name.append("the")
            if random.random() < 0.4:
                name.append(random.choice(adjective()))
        name.append(random.choice(noun_list()))
    string = ""
    for item in name:
        string = string + item.capitalize() + " "
    return string[:-1]

def name_list():
    """
    List Name Artifacts
    """
    return  ["fire", "slash", "ice", "sword", "smite", "destruction",
    "absolute", "death", "black", "edge", "abyssal", "growth", "charm",
    "cloud", "shield", "rain", "acid", "flame", "flare", "horror",
    "aegis", "honor", "mystic", "barrier", "burst", "charge", "aether",
    "meltdown", "rift", "shock", "shockwave", "lightning", "thunder",
    "hell", "storm", "tide", "ancient", "renegade", "agility", "warp",
    "aim", "nature", "vengeance", "damaged", "wrath", "sun",
    "shadow", "light", "dark", "destiny", "ruin", "soul",
    "broke", "frozen", "earth", "sudden"]

def adjective():
    """
    List of Adjective Specific Name Artifacts
    """
    return ["forgotten", "ancient", "frozen", "scornful", "vengeful",
    "resilient", "crafty", "colossal", "ice", "fire", "earth", "brutal",
    "wandering", "black", "dark", "virtuous", "unholy", "fungal", "white", "flushed",
    "red", "deadly"]

def noun_list():
    """
    List of Noun Specific Name Artifacts
    """
    return ["cat", "mage", "horror", "bear", "warrior", "soldier",
    "shade", "angel", "demon", "elf", "elemental", "phoenix", "hero",
    "wizard", "dragon", "fairy", "hellkite", "horse", "leech", "troll",
    "giant", "griffin", "person", "golem", "shaman", "prophet", "siren",
    "succubis", "hydra", "basilisk", "satyr", "minotaur", "fish",
    "gargoyle", "wolf", "ooze", "protector", "goblin", "destroyer", "ape",
    "roc", "beast", "colossus", "titan", "dwarf", "sphinx", "ravager",
    "hellhound", "rogue", "knight", "tiger", "unicorn", "eater", "king", "gremlin",
    "orc", "god", "fungus", "leviathan", "priest", "cleric", "sprite", "vagabond",
    "reaper", "eagle", "sofa"]

def random_name():
    """
    Unique Character Name Generation
    (ADD COMMENTS)
    """
    name = ""
    consonants = ["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p",
    "r", "s", "t", "v", "w", "y", "z"]
    sounds = ["br", "rd", "rn", "st", "tr", "lt", "pt", "mn", "ny", "gh", "sh",
    "xx", "kk", "ss", "tt", "mm", "rr", "ll"]
    vowels = ["a", "e", "i", "o", "u"]
    if random.random() < 0.5:
        name = random.choice(vowels)
    for i in range(0, round(2*random.random() + 1)):
        if i == 0 or random.random() < 0.5:
            name = name + random.choice(consonants)
        else:
            name = name + random.choice(sounds)
        name = name + random.choice(vowels)
    if random.random() < 0.5:
        name = name + random.choice(consonants)
    return name

def random_game_name():
    wordlist = ["hearth", "stone", "sweep", "magic", "monster", "iron", "fire",
    "emblem", "war", "craft", "spell", "fate", "shadow", "star", "lock", "mine"]
    rand1 = random.choice(wordlist)
    wordlist.remove(rand1)
    rand2 = random.choice(wordlist)
    return rand1.capitalize() + rand2.capitalize()

def generate_stats(cost, card_type, leftover):
    """
    Generates stats ATT, DEF and effect for a card based on COST
    effect is a boolean dictating whether or not there is an effect
    """
    stats = [0, 0] #[ATT, DEF, EFFECT]
    rands = [(random.random()*PREF_MULTIPLIERS[i] * .6)+.2 for i in range(2)] #Generate 3 Random Numbers to represent the relative amounts of ATT DEF and Effect  #Static Values were added to prevent ridiculously high and low values
    if card_type == TYPE_SPELL:
        return [cost, 0, 0]
    tot = sum(rands) #Sum of randoms
    norm_rands = [r/tot for r in rands] #Normalized Randoms relative importance of ATT DEF and COST while also adding to 1
    #spend = STATS_PREF*(CARD_INITIAL_STRENGTH+cost-cost*CARD_STRENGTH_DROPOFF) * (CARD_STRENGTH) #+ np.random.normal(0, 1/4)) #Determines amount of arbitrary spending money for each stat #Arbitrary values added to nerf higher cost enemies a bit and add some randomness
    spend = leftover
    #print(spend)
    if spend == 0:
        spend = max(0, np.random.normal(.5, 1/2)) #This code and these arbitrary values give cost 0 cards a fighting chance, by giving a chance for them to have ok stats
    stat_spend = [spend * i for i in norm_rands] #Give each stat its proportion of the spending
    #stat_spend[2] += MIN_EFFECT #constant added to increase spending for effect
    stats = [int(i) for i in stat_spend] # put ATT and DEF into ints and place them in stats
    diff_att = max(0, stats[0] - MAX_ATT) #find how much attack has passed the max
    diff_def = max(0, stats[1] - MAX_DEF) #find how much def has passed the max
    stats[0] = min(stats[0] + diff_def, MAX_ATT) #add the amount def passed to the att, if possible
    stats[1] = max(min(stats[1] + diff_att, MAX_DEF),MIN_DEF) #set Def min to be 1, add how much att passed to the def, if possible
    #stats.append(stat_spend[2]) # Add Effect into Stats
    stats.insert(0, cost) #Insert Cost into the first slot of stats
    #print(stats)
    return stats

#print(generate_stats(True, 10))

def generate_numerical_effect(effect_spend, cardType, second = False):
    """
    Generates Slightly More Balanced Numerical Effects
    """
    #Return none

    #trials = [] #Initialize List
    #for i in EFFECT_LIST: #Take 20 trial effects
    #    for j in TRIGGER_LIST:
    #        eff = random.choice(EFFECT_LIST) #Choose random effect
    #        trig = random.choice(TRIGGER_LIST) #Choose random Trigger
    #        trials.append((eff,trig)) #Add to List
    #effect_costs = [] # Initialize List
    #minimums = [] #Initialize List
    #i = 0
    if cardType == TYPE_SPELL:
        #varied_costs = [(i, TRIGGER_PLAY, i[2], EFFECT_COST_DICT[i[0]] * TRIGGER_PLAY * TARGET_COST_DICT[i[2]])
        #                for i in EFFECT_POSSIBILITIES if not i in STATIC_EFFECT_LIST for j in EFFECT_POSSIBILITIES[i] for k, eff_cost in EFFECT_POSSIBILITIES[i][j]] ##CHANGE THIS TO HAVE ITS OWN EFFECT_POSSIBILITIES LIST
        valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1] and k[1] > 0]) for j in i[1]]) for i in SPELL_EFFECT_POSSIBILITIES] #if effect_spend > i[3] and i[3] > 0]
        ## Effect Choice
        if len(valid_combs) == 0:
            #while True:
            #    eff = random.choice(EFFECT_LIST)
            #    if eff in STATIC_EFFECT_LIST:
            #        continue
            #    targ = random.choice(SPELL_TARGET_LIST)
            #    if eff*targ > 0:
            #        break
            eff = DEAL_EFFECT
            targ = TARGET_CREATURE
            return(((eff, TRIGGER_PLAY, targ, 1),), effect_spend - MIN_EFF_COST)
    else:
        valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1]]) for j in i[1]]) for i in CREATURE_EFFECT_POSSIBILITIES]
    for i in range(EFFECT_TRY_NUM):
        success = True
        eff, val_trigs_targs = random.choice(valid_combs)
        if len(val_trigs_targs) == 0:
            #del eff, val_trigs_targs
            success = False
            continue
        trig, val_targs = random.choice(val_trigs_targs)
        if len(val_targs) == 0:
            #del eff, val_trigs_targs, trig, val_targs
            success = False
            continue
        targ, spend_cost = random.choice(val_targs)
        #success = True
    double = False
    if (DOUBLE_EFFECT_CHANCE > random.random()) and not second:
        double = True
    if not success:
        if cardType == TYPE_SPELL or second:
            eff = DEAL_EFFECT
            targ = TARGET_CREATURE
            eff_info = (eff, TRIGGER_PLAY, targ, 1)
            leftover = effect_spend - MIN_EFF_COST
            if not second:
                double = True
        else:
            return (((None, None, None, 0),), effect_spend)
    #val = random.choice(valid_combs)
    #^###################^#
    else:
        if eff in STATIC_EFFECT_LIST:
            numeric = 1
        elif cardType == TYPE_SPELL:
            numeric = int(effect_spend/spend_cost)
            if double:
                numeric = max(1, random.randint(0, abs(numeric)))
        else:
            numeric_div = max(spend_cost/TARGET_COST_DICT[targ], spend_cost)
            numeric = int(abs(effect_spend/numeric_div)) #Make it so numeric is based on effect_spend and cost, but also allow - costs that get pretty negative
            if numeric < 0:
                numeric = int(random.random()*MAX_NEGATIVE_NUMERIC+1)
            elif double:
                numeric = max(1,random.randint(0, numeric))
        leftover = effect_spend - spend_cost * abs(numeric) #val[2] * numeric
        if leftover > effect_spend:
            leftover += NEGATIVE_ADDER
        #print(effect_spend, val[3], numeric, leftover)
        #print(val[0])
        if numeric == 0:
            numeric = 1
        eff_info = (eff, trig, targ, abs(numeric))
    if (double or cardType==TYPE_SPELL) and leftover > MIN_EFF_COST and not second :
        [eff2_info, leftover] = generate_numerical_effect(leftover, cardType, second = True)
        return ((eff_info, eff2_info[0]), leftover)
    return ((eff_info,), leftover)
    #for eff, trig, eff_cost in trial: #For values in the trials list
        #eff_cost = eff_cost_base #* (.4*random.random() + .8) # Cost of the effect #Arbitrary Values create variation in which values are lower and higher, this prevents more costly effects from being too rare
        #trial[2] = eff_cost #add cost of effect to respective list
    #    if effect_spend < eff_cost: #If can't afford effect
    #        trial.remove(i) #add obscenly large value
        #else: #Otherwise
        #    minimums.append(1) #Append the modulus of the spending available by the cost (since we can have any int numeric, we care about how close the spending is to a multiple of the value not to the cost itself)
    #    i+=1

    #choices = [i for i in minimums if i < EFFECT_THRESHOLD] #Only allow values over a certain threshold
    #if len(choices) != 0: #If there is at least one choice
     #Choose one at random
    #else: #Otherwise
    #    val = min(minimums) #Pick the value that most closely matches the cost, regardless of how far off that is

    #if val == 9999: #If somehow none of the values worked
    #    return [None, None, 0] #Return none

    #ind = minimums.index(val) # Find index of the value
    #print('ind = ' + str(ind))
    #eff_trig = EFFECT_COST_DICT[trials[ind][0]] * TRIGGER_COST_DICT[trials[ind][1]]
    #numeric = int(effect_spend/(val[2])) #int(effect_spend/(eff_trig*(.4*random.random()+.8)))
    #print('numeric = ' + str(numeric))
    #if numeric >= 1:
    #[trials[ind][0], trials[ind][1], numeric]
    #else:
    #    return [None, None, 0]
        #return [SORTED_EFFECT_COST[0][0], SORTED_TRIGGER_COST[0][0], 1]
    #return [sorted_eff[0][0], sorted_trig[0][0], 1]
