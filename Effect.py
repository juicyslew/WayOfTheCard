from Constants import *
from random import choice, random

class Effect():
    def __init__(self, trigger = None, target = None, effect = None, numeric = None):#, effect = None):
        if trigger == None:
            trigger = choice(TRIGGER_LIST)
        if target == None:
            target = "WIP" #Add target based on stuff???
        if effect == None:
            effect = choice(EFFECT_LIST)
        if numeric == None:
            numeric = round(MAX_NUMERIC * random())
        self.trigger = trigger
        self.target = target
        self.effect = effect
        self.numeric = numeric
    def __str__(self):
        s = """True

trigger: %s
target: %s
effectType: %s
magnitude: %s
""" % (TRIGGER_DICT[self.trigger], self.target, EFFECT_DICT[self.effect], self.numeric)
        return s

#print(Effect(0))
