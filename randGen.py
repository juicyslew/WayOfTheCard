import random
import numpy as np
from Constants import *
from math import floor
import operator

class randGen():
    """
    The class behind all random generation in the game except for the art on cards.
    """
    def __init__(self, type = "creature", word_num = random.choice([1, 2, 3])):
        pass

def generate(cardType = TYPE_CREATURE):
    """
    Generates Names for Creatures.
    (ADD COMMENTS)
    """
    if cardType == TYPE_CREATURE:     #Decides name length for creatures
        word_num = random.choice([1,2])
    else:
        word_num = random.choice([1,2,3]) #Decides name length for spells
    name = []
    i = 0
    while i < word_num: #Randomly pick words from the words
        i += 1
        name.append(random.choice(name_list()))
    if cardType == TYPE_CREATURE:   #Add a chance of creature names with "the" in it
        if random.random() < 0.35:
            name = []
            name.append(random_name())
            name.append("the")
            if random.random() < 0.4:   #Adds the possibility of an adjective as well.
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
    "red", "deadly", "minor", "major"]

def noun_list():
    """
    List of Noun Specific Name Artifacts
    """
    return ["cat", "mage", "horror", "bear", "warrior", "soldier",
    "shade", "angel", "demon", "elf", "elemental", "phoenix", "hero",
    "wizard", "dragon", "fairy", "hellkite", "horse", "leech", "troll",
    "giant", "griffen", "person", "golem", "shaman", "prophet", "siren",
    "succubis", "hydra", "basilisk", "satyr", "minotaur", "fish",
    "gargoyle", "wolf", "ooze", "protector", "goblin", "destroyer", "ape",
    "roc", "beast", "colossus", "titan", "dwarf", "sphinx", "ravager",
    "hellhound", "rogue", "knight", "tiger", "unicorn", "eater", "king", "gremlin",
    "orc", "god", "fungus", "leviathan", "priest", "cleric", "sprite", "vagabond",
    "reaper", "eagle", "sofa"]

def random_name():
    """
    Unique Character Name Generation
    Returns a string.
    """
    name = ""
    consonants = ["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p",
    "r", "s", "t", "v", "w", "y", "z"]
    sounds = ["br", "rd", "rn", "st", "tr", "lt", "pt", "mn", "ny", "gh", "sh",
    "xx", "kk", "ss", "tt", "mm", "rr", "ll"]   #Give pairs of consonants that make certain sounds.
    vowels = ["a", "e", "i", "o", "u"]
    if random.random() < 0.5:   #randomly selects vowels
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
    """
    Randomly generates a name for the specific game being played.
    """
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

def generate_effect_name(effect, reminder_text = True):
    if effect == None:
        return ""
    elif effect == WINDFURY_EFFECT:
        list1 = ["wind", "double", "duplicate", "duo", "back"] #Why "back"?
        list2 = ["fury", "rage", "strike", "slash", "power", "smash"]
        text = random.choice(list1).capitalize() + random.choice(list2).capitalize()
        if reminder_text:
            text = text + " (this creature can attack twice per turn)"
        return text
    elif effect == TAUNT_EFFECT:
        list1 = ["taunt", "protect", "defend"]
        list2 = ["er", "ish", ""]
        text = random.choice(list1).capitalize() + random.choice(list2)
        if reminder_text:
            text = text + " (enemy creatures can only attack creatures with %s)" % text
        return text
    elif effect == DIVINE_SHIELD_EFFECT:
        list1 = ["holy", "divine", "power", "golden", "light", "life"]
        list2 = ["shield", "barrier", "aegis", "aura", "defense"]
        text = random.choice(list1).capitalize() + " " + random.choice(list2).capitalize()
        if reminder_text:
            text = text + " (the next damage to this card is prevented)"
        return text
    elif effect == CHARGE_EFFECT:
        list1 = ["speed", "fast", "haste", "quick"]
        list2 = ["charge", "strike", ""]
        text = (random.choice(list1).capitalize() + " " + random.choice(list2).capitalize()).strip()
        if reminder_text:
            text = text + " (this creature can attack the turn it is played)"
        return text


    #print(generate_stats(True, 10))

def generate_numerical_effect(effect_spend, cardType, second = False):
    """
    Generates Slightly More Balanced Numerical Effects
    """
    #Return none
    if cardType == TYPE_SPELL:
        #varied_costs = [(i, TRIGGER_PLAY, i[2], EFFECT_COST_DICT[i[0]] * TRIGGER_PLAY * TARGET_COST_DICT[i[2]])
        #                for i in EFFECT_POSSIBILITIES if not i in STATIC_EFFECT_LIST for j in EFFECT_POSSIBILITIES[i] for k, eff_cost in EFFECT_POSSIBILITIES[i][j]] ##CHANGE THIS TO HAVE ITS OWN EFFECT_POSSIBILITIES LIST
        if second:
            valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1] and effect_spend % k[1] < EFFECT_THRESHOLD and k[1] > 0]) for j in i[1]]) for i in SPELL_EFFECT_POSSIBILITIES]
        else:
            valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1] and k[1] > 0]) for j in i[1]]) for i in SPELL_EFFECT_POSSIBILITIES] #if effect_spend > i[3] and i[3] > 0]
        ## Effect Choice
        if len(valid_combs) == 0:
            eff = DEAL_EFFECT
            targ = TARGET_CREATURE
            return(((eff, TRIGGER_PLAY, targ, 1),), effect_spend - MIN_EFF_COST)
    else:
        if second:
            valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1] and effect_spend % k[1] < EFFECT_THRESHOLD and k[1] > 0]) for j in i[1]]) for i in CREATURE_EFFECT_POSSIBILITIES]
        else:
            valid_combs = [(i[0],[(j[0],[k for k in j[1] if effect_spend > k[1]]) for j in i[1]]) for i in CREATURE_EFFECT_POSSIBILITIES]
    for i in range(EFFECT_TRY_NUM):
        success = False
        eff, val_trigs_targs = random.choice(valid_combs)
        if len(val_trigs_targs) == 0:
            #del eff, val_trigs_targs
            continue
        trig, val_targs = random.choice(val_trigs_targs)
        if len(val_targs) == 0:
            #del eff, val_trigs_targs, trig, val_targs
            continue
        targ, spend_cost = random.choice(val_targs)
        success = True
        break
    double = False
    if (DOUBLE_EFFECT_CHANCE > random.random()) and not second:
        double = True
    if not success:
        if cardType == TYPE_SPELL or second:
            print(effect_spend)
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
    elif not eff is None:
        if eff in STATIC_EFFECT_LIST or eff in ONE_DO_EFFECTS:
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
        if numeric == 0:
            numeric = 1
        eff_info = (eff, trig, targ, abs(numeric))
    if (double or cardType==TYPE_SPELL) and leftover > MIN_EFF_COST and not second :
        [eff2_info, leftover] = generate_numerical_effect(leftover, cardType, second = True)
        return ((eff_info, eff2_info[0]), leftover)
    return ((eff_info,), leftover)
