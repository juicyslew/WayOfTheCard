#from Constants import *
from Hand import *
from Deck import *
from Discard import *
from Card import *

class Player_Card(Card):
    """
    Card for Representing the Player.  This is in the player's field and is the physical hero that the opponent can attack
    """
    def __init__(self, name):
        self.name = name #Player Name
        self.stats = [0, 0, PLAYER_HEALTH] #Player Stats
        self.starting_stats = [0, 0, PLAYER_HEALTH] # Player Base Stats
        self.state = STATE_SLEEP #Player State is Pretty Much Constantly Asleep
        self.effect = False #Player Has No Effects

    def __str__(self): #When printing the player
        s = """### %s || %s\n""" % (self.name, self.stats) # Return this string
        return s

class Player():
    """
    Player class: Acts as a Hub for most Player specific actions and code (Which is allot)
    """
    def __init__(self, name, handstart):
        self.name = name #Player Name
        self.player = Player_Card(name) #Player Card
        self.cards = [self.player] # Player Field
        self.deck = Deck() # Initialize Player Deck
        self.deck.init_deck()
        self.handstart = handstart
        self.hand = Hand(self.deck, self.handstart) # Initialize Player Hand
        self.discard = Discard() # Initialize Player Discard
        self.dead = False # Set Player to Alive
        self.mana = 0 #Set Initial Mana
        self.max_mana = MAX_MANA #Set Max Mana

    def __str__(self): # Return Formatted Cards from the Field
        return '\n' + '\n'.join(['%i)\n%s\n==============================================='%(i+1,str(self.cards[i])) for i in range(len(self.cards))]) + '\n'
    #def str_hand(self):
        #return '\n\n'.join([card.name for card in self.hand.cards])
    def activate_cards(self):
        """
        Awaken all the Cards from sleep state
        """
        for card in self.cards:
            if not card == self.player:
                card.state = STATE_ACTIVE
    def check_active(self):
        """
        return only active state cards
        """
        ls = []
        for card in self.cards:
            if card.state == STATE_ACTIVE:# and not card is self.player:
                ls.append(card)
        return ls

    def check_dead(self, enemy_player, all_players = None):
        """
        Function for Checking if anything has died
        """
        ls = [] #Initialize List
        for card in self.cards: #for each card
            if card.stats[DEF] <= 0: #If card has no defense/health
                if card is self.player: #If card is player
                    self.dead = True #This player is dead
                card.state = STATE_GRAVEYARD #Change Card State To Dead
                ls.append(card) # Add to list of cards that died
                self.discard.cards.append(self.cards.pop(self.cards.index(card))) #Remove from Player Field, Add to Discard Pile

        for card in ls: #Go back through list and check for any On Death effects
            try:
                card.effect.activate(self, enemy_player, TRIGGER_DEATH)
            except AttributeError:
                pass
            print('~~~~~~ '+card.name + ' Has Died. ~~~~~~')
        return ls # Return Death List
