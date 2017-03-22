import random
import numpy as np
from Constants import *
from math import floor
import operator

class randGen():
    def __init__(self, type = "creature", word_num = random.choice([1, 2, 3])):
        pass

def generate(cardType = TYPE_CREATURE):
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
    return ["forgotten", "ancient", "frozen", "scornful", "vengeful",
    "resilient", "crafty", "colossal", "ice", "fire", "earth", "brutal",
    "fucking", "wandering", "black", "dark", "virtuous"]

def noun_list():
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
        name = name + random.choice(consonants)
    return name

def generate_stats(effect, cost):
    """
    Generates stats for a card (COST ATT DEF) and effect
    """
    stats = [0, 0, 0] #[ATT, DEF, EFFECT]
    #if cost == None:
    #    cost = np.random.choice(range(0, MAX_COST+1), p = MANA_CURVE)
    rands = [(random.random()*PREF_MULTIPLIERS[i] * .6)+.2 for i in range(3)]
    if not effect:
        rands[2] = 0
    tot = sum(rands)
    norm_rands = [r/tot for r in rands]
    #print(cost)
    #print(norm_rands)
    spend = (cost-cost*.075) * (3 + np.random.normal(0, 1/4))
    #print("cost = "+ str(cost))
    #print("spend = " + str(cost-cost*.15))
    if spend == 0:
        spend = max(0, np.random.normal(1.5, 1/2))
    stat_spend = [spend/3 * i for i in norm_rands]
    stat_spend[2] += MIN_EFFECT #constant added to effect spends
    #print(stat_spend)
    stats = [max(int(2*i),1) for i in stat_spend[:2]]
    diff_att = max(0, stats[0] - MAX_ATT) #find how much attack has passed the max
    diff_def = max(0, stats[1] - MAX_DEF) #find how much def has passed the max
    stats[0] = min(stats[0] + diff_def, MAX_ATT) #add the amount def passed to the att, if possible
    stats[1] = min(stats[1] + diff_att, MAX_DEF) #add how much att passed to the def, if possible
    stats.append(2*stat_spend[2])
    stats.insert(0, cost)
    return stats
#print(generate_stats(True, 10))

def generate_numerical_effect(effect_spend):
    """
    Generates Slightly More Balanced Numerical Effects
    """
    min_eff = SORTED_EFFECT_COST[0][1] * SORTED_TRIGGER_COST[0][1]
    #print('min_eff = ' + str(min_eff))
    if min_eff >= effect_spend:
        #find way to return none
        return [None, None, 0]
        #return [SORTED_EFFECT_COST[0][0], SORTED_TRIGGER_COST[0][0], 1]
    #print('eff_spnd = ' + str(effect_spend))
    trials = []
    for i in range(20):
        eff = random.choice(EFFECT_LIST)
        trig = random.choice(TRIGGER_LIST)
        trials.append((eff,trig))
    effect_costs = []
    minimums = []
    for eff, trig in trials:
        eff_trig = EFFECT_COST_DICT[eff] * TRIGGER_COST_DICT[trig]*(.2*random.random() + .9)
        effect_costs.append(eff_trig)
        if effect_spend < eff_trig:
            minimums.append(9999)
        else:
            minimums.append(effect_spend % eff_trig)
    #print(minimums)
    choices = [i for i in minimums if i < EFFECT_THRESHOLD]
    if len(choices) != 0:
        val = random.choice(choices)
    else:
        val = min(minimums)
    #val = min(minimums)
    #print('val = ' + str(val))
    if val == 9999:
        return [None, None, 0]
        #return [SORTED_EFFECT_COST[0][0], SORTED_TRIGGER_COST[0][0], 1]
    ind = minimums.index(val)
    #print('ind = ' + str(ind))
    #eff_trig = EFFECT_COST_DICT[trials[ind][0]] * TRIGGER_COST_DICT[trials[ind][1]]
    numeric = int(effect_spend/(effect_costs[ind]*(.4*random.random()+.8))) #int(effect_spend/(eff_trig*(.4*random.random()+.8)))
    #print('numeric = ' + str(numeric))
    if numeric >= 1:
        return [trials[ind][0], trials[ind][1], numeric]
    else:
        return [None, None, 0]
        #return [SORTED_EFFECT_COST[0][0], SORTED_TRIGGER_COST[0][0], 1]
    #return [sorted_eff[0][0], sorted_trig[0][0], 1]
