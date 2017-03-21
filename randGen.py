import random
from Constants import *

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
