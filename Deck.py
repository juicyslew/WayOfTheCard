from Constants import *
from Card import *
from random import shuffle

class Deck():
    """
    Deck class:  Contains list of cards in player's deck.
    """
    def __init__(self, rare_ls = None):
        self.cards = []
        if rare_ls == None:
            self.rarities = [None for a in range(DECK_INIT_SIZE)]
        else:
            self.rarities = rare_ls

    def __str__(self):
        return'\n' + '\n'.join(['%i)\n%s\n==============================================='%(i+1,str(self.cards[i])) for i in range(len(self.cards))]) + '\n'

    def init_deck(self):
        """ Generate Deck """
<<<<<<< HEAD
        for i in range(DECK_INIT_SIZE):
            self.cards.append(Card(state = STATE_SLEEP, effect = True)) #Using TestCards for now

=======
        if ARENA:
            for a in range(DECK_INIT_SIZE):
                chooseCards = []
                for k in range(randint(MINCHOICE,MAXCHOICE)):
                    chooseCards.append(Card(state = STATE_SLEEP, effect = True, rarity = self.rarities[a]))
                print('\n\n ~~~ CARD %i ~~~' % a)
                for j in range(len(chooseCards)):
                    print('\n%i)  %s'%(j, chooseCards[j]))
                while True:
                    i = input('Choose Your Card Index: ') # Get input of which creature to attack with.
                    try:
                        i = int(i) #check that input is a number
                        try:
                            self.cards.append(chooseCards[i])
                        except IndexError: # if index error
                            print("\nNot that many cards to choose from!")
                            continue #start over
                    except ValueError: # if value error (input isn't an integer)
                        print('\nInput a Number!')
                        continue #start over
                    break
        else:
            for i in range(DECK_INIT_SIZE):
                self.cards.append(Card(state = STATE_SLEEP, effect = True, rarity = self.rarities[i])) #Using TestCards for now
        self.shuffle_deck()
>>>>>>> a0db5a837f3ffcaa8a8a4e9b910fc07016d861fb
    def shuffle_deck(self):
        """ Shuffle Deck """
        shuffle(self.cards)

    def draw(self, hand, num):
        """ Draw "num" Cards into Hand """
        for n in range(num):
            if len(hand.cards) < HAND_MAX_SIZE:
                hand.cards.append(self.cards.pop(0))
            else:
                print("Genius. The following card was lost: \n" + str(self.cards[0]))
                self.cards.pop(0)
