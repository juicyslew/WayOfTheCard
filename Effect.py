from Constants import *
import random

class Effect():
    def __init__(self, trigger, target, effect = None):
        self.trigger = trigger
        self.target = target
        self.effect = effect
        self.numeric = round(MAX_NUMERIC * random.random())
