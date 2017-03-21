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
        if random.random() < 0.25:
            name.append("the")
        name.append(random.choice(noun_list()))
    string = ""
    for item in name:
        string = string + item.capitalize() + " "
    return string

def name_list():
    return  ["fire", "slash", "ice", "sword", "smite", "destruction",
    "absolute", "death", "black", "edge", "abyssal", "growth", "charm",
    "cloud", "shield", "rain", "acid", "flame", "flare", "horror",
    "aegis", "honor", "mystic", "barrier", "burst", "charge", "aether",
    "meltdown", "rift", "shock", "shockwave", "lightning", "thunder",
    "hell", "storm", "tide", "ancient", "renegade", "agility", "warp",
    "aim", "shoot", "nature", "vengeance", "damage", "wrath", "sun",
    "shadow", "light", "dark", "destiny", "favor", "ruin", "fucking", "soul",
    "Broke", "frozen"]

def noun_list():
    return ["cat", "mage", "horror", "bears", "warrior", "soldier",
    "shade", "angel", "demon", "elf", "elemental", "phoenix", "hero",
    "wizard", "dragon", "fairy", "hellkite", "horse", "leech", "troll",
    "giant", "griffin", "person", "golem", "shaman", "prophet", "siren",
    "succubis", "hydra", "basilisk", "satyr", "minotaur", "jesus", "fish",
    "gargoyle", "wolf", "ooze", "protector", "goblin", "destroyer", "ape",
    "roc", "beast", "colossus", "titan", "dwarf", "sphinx", "ravager",
    "hellhound", "rogue", "knight", "tiger", "unicorn", "eater"]
