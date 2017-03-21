from Constants import *
from random import choice, random
import math

class Effect():
    def __init__(self, trigger = None, target = None, effect = None, numeric = None):#, effect = None):
        if trigger == None:
            trigger = choice(TRIGGER_LIST)
        if effect == None:
            effect = choice(EFFECT_LIST)
        if target == None:
            if effect == DRAW_EFFECT:
                target = choice(DRAW_TARGET_LIST) #Add target based on stuff???
            else:
                target = choice(TARGET_LIST)
        if numeric == None:
            numeric = math.ceil(MAX_NUMERIC * random())
        self.trigger = trigger
        self.target = target
        self.effect = effect
        self.numeric = numeric
    def __str__(self):
        s = """True

###EFFECT###
trigger: %s
target: %s
effectType: %s
magnitude: %s
""" % (TRIGGER_DICT[self.trigger], TARGET_DICT[self.target], EFFECT_DICT[self.effect], self.numeric)
        return s

#print(Effect(0))
