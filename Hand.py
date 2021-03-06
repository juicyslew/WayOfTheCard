from Constants import *
class Hand():
    """
    Hand class: Contains list of cards in player's hand. Uses Cards.
    """
    def __init__(self, deck, handstart):
        self.cards = []
        for i in range(handstart):
            self.cards.append(deck.cards.pop(0)) #Creates Initial Hand

    def __str__(self):
        return '\n' + '\n'.join(['%i)\n%s\n==============================================='%(i+1,str(self.cards[i])) for i in range(len(self.cards))]) + '\n'
