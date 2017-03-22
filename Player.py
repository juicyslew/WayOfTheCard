#from Constants import *
from Hand import *
from Deck import *
from Discard import *
from Card import *

class Player_Card(Card):
    def __init__(self, name):
        self.name = name
        self.stats = [0, 0, PLAYER_HEALTH]
        self.starting_stats = [0, 0, PLAYER_HEALTH]
        self.state = STATE_ACTIVE
        self.effect = False
    def __str__(self):
        s = """### Hero ###
name: %s
Stats: %s
""" % (self.name, self.stats)
        return s

class Player():
    """
    Player class: Contains deck and hand of player
    """
    def __init__(self, name):
        self.name = name
        self.player = Player_Card(name)
        self.cards = [self.player]
        self.deck = Deck()
        self.deck.init_deck()
        self.hand = Hand(self.deck)
        self.discard = Discard()
        self.dead = False
        self.mana = 0
        self.max_mana = MAX_MANA

    def __str__(self):
        return '\n\n'.join(['%i)\n%s'%(i+1,str(self.cards[i])) for i in range(len(self.cards))])
    #def str_hand(self):
        #return '\n\n'.join([card.name for card in self.hand.cards])
    def activate_cards(self):
        for card in self.cards:
            card.state = STATE_ACTIVE
    def check_active(self):
        ls = []
        for card in self.cards:
            if card.state == STATE_ACTIVE and not card is self.player:
                ls.append(card)
        return ls
    def check_dead(self, enemy_player):
        ls = []
        for card in self.cards:
            if card.stats[DEF] <= 0:
                if card is self.player:
                    self.dead = True
                card.state = STATE_GRAVEYARD
                try:
                    card.effect.activate(self, enemy_player, TRIGGER_DEATH)
                except AttributeError:
                    pass
                print('~~~~~~  '+card.name + ' Has Died.')
                ls.append(card)
                self.discard.cards.append(self.cards.pop(self.cards.index(card)))
        return ls
