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
    "aim", "nature", "vengeance", "damage", "damaged", "wrath", "sun",
    "shadow", "light", "dark", "destiny", "favor", "ruin", "fucking", "soul",
    "Broke", "frozen", "earth"]

def adjective():
    """
    List of Adjective Specific Name Artifacts
    """
    return ["forgotten", "ancient", "frozen", "scornful", "vengeful",
    "resilient", "crafty", "colossal", "ice", "fire", "earth", "brutal",
    "fucking", "wandering", "black", "dark", "virtuous"]

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
    "hellhound", "rogue", "knight", "tiger", "unicorn", "eater", "king", "gremlin"]

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

def generate_stats(effect, cost, card_type):
    """
    Generates stats ATT, DEF and effect for a card based on COST
    effect is a boolean dictating whether or not there is an effect
    """
    stats = [0, 0, 0] #[ATT, DEF, EFFECT]
    rands = [(random.random()*PREF_MULTIPLIERS[i] * .6)+.2 for i in range(3)] #Generate 3 Random Numbers to represent the relative amounts of ATT DEF and Effect  #Static Values were added to prevent ridiculously high and low values
    if not effect: # Check if Effect is True
        rands[2] = 0 # If Not then set its relative value to 0
    if card_type == TYPE_SPELL:
        rands[2] = cost+1
    tot = sum(rands) #Sum of randoms
    norm_rands = [r/tot for r in rands] #Normalized Randoms relative importance of ATT DEF and COST while also adding to 1
    spend = (cost-cost*CARD_STRENGTH_DROPOFF) * (CARD_STRENGTH + np.random.normal(0, 1/4)) #Determines amount of arbitrary spending money for each stat #Arbitrary values added to nerf higher cost enemies a bit and add some randomness
    if spend == 0:
        spend = max(0, np.random.normal(1, 1/2)) #This code and these arbitrary values give cost 0 cards a fighting chance, by giving a chance for them to have ok stats
    stat_spend = [spend * i for i in norm_rands] #Give each stat its proportion of the spending
    stat_spend[2] += MIN_EFFECT #constant added to increase spending for effect
    stats = [int(i) for i in stat_spend[:2]] # put ATT and DEF into ints and place them in stats
    diff_att = max(0, stats[0] - MAX_ATT) #find how much attack has passed the max
    diff_def = max(0, stats[1] - MAX_DEF) #find how much def has passed the max
    stats[0] = min(stats[0] + diff_def, MAX_ATT) #add the amount def passed to the att, if possible
    stats[1] = max(min(stats[1] + diff_att, MAX_DEF),MIN_DEF) #set Def min to be 1, add how much att passed to the def, if possible
    stats.append(stat_spend[2]) # Add Effect into Stats
    stats.insert(0, cost) #Insert Cost into the first slot of stats
    return stats

#print(generate_stats(True, 10))

def generate_numerical_effect(effect_spend):
    """
    Generates Slightly More Balanced Numerical Effects
    """
    min_eff = SORTED_EFFECT_COST[0][1] * SORTED_TRIGGER_COST[0][1] # Minimum Effect Cost
    if min_eff >= effect_spend: # If don't have enough for minimum
        return [None, None, 0] #Return none

    #trials = [] #Initialize List
    #for i in EFFECT_LIST: #Take 20 trial effects
    #    for j in TRIGGER_LIST:
    #        eff = random.choice(EFFECT_LIST) #Choose random effect
    #        trig = random.choice(TRIGGER_LIST) #Choose random Trigger
    #        trials.append((eff,trig)) #Add to List
    #effect_costs = [] # Initialize List
    #minimums = [] #Initialize List
    #i = 0

    valid_effs = [i for i in EFFECT_POSSIBILITIES if effect_spend > i[2]]
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
    val = random.choice(valid_effs) #Choose one at random
    #else: #Otherwise
    #    val = min(minimums) #Pick the value that most closely matches the cost, regardless of how far off that is

    #if val == 9999: #If somehow none of the values worked
    #    return [None, None, 0] #Return none

    #ind = minimums.index(val) # Find index of the value
    #print('ind = ' + str(ind))
    #eff_trig = EFFECT_COST_DICT[trials[ind][0]] * TRIGGER_COST_DICT[trials[ind][1]]
    numeric = int(effect_spend/(val[2]*(.15*random.random()+ .85))) #int(effect_spend/(eff_trig*(.4*random.random()+.8)))
    #print('numeric = ' + str(numeric))
    #if numeric >= 1:
    return [val[0], val[1], numeric]#[trials[ind][0], trials[ind][1], numeric]
    #else:
    #    return [None, None, 0]
        #return [SORTED_EFFECT_COST[0][0], SORTED_TRIGGER_COST[0][0], 1]
    #return [sorted_eff[0][0], sorted_trig[0][0], 1]
