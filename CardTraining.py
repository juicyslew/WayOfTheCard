import testCard
from Constants import *
import numpy as np
import theano
import theano.tensor as T
import pickle as pk

"""
Old code from when we thought we had time to set up a neural net to make better cards.
"""

x = 5
power = 1.5
initpow = .5
zerostrength = .5
spell_multi = 1.0
spell_add = 1.2
start = open('cardinfo.txt', 'rb')
try:
    cardinfotxt = pk.load(start)
    start.close()
    print(cardinfotxt)
except EOFError:
    cardinfo = [power, initpow, zerostrength, spell_multi, spell_add]
learnrate = .15
#x = T.matrix('x')
#y = T.vector('y')
#cost = T.vector('cost')
#w = theano.shared(0, name="w")
#b = theano.shared(1, name="b")

#powfunc = theano.function(inputs=[x,y],
#                          outputs=[cost]
#                          updates=(()))
def eff_spend_func(x, power, initpow, zerostrength, cardtype, spell_multi, spell_add):
    if x == 0:
        diff = [x, 0, 1, 0, 0]
        #res = power * x + zerostrength
    else:
        #res = power*x + initpow
        diff = [x, 1, 0, 0, 0]
    if cardtype == TYPE_SPELL:
        #res = res * spell_multi + spell_add
        diff[0] *= spell_multi
        diff[1] *= spell_multi
        diff[2] *= spell_multi
        diff[3] = power * x + zerostrength
        diff[4] = 1
    return diff

stop = False
cards = []
rarities = []
while True:
    rarity = np.random.choice(RARITIES, p = RARITY_PROBS)
    card = testCard.testCard(state = STATE_SLEEP, effect = True, rarity = rarity, cardinfo = cardinfo)
    if not card.cardinfo == cardinfo:
        print(cardinfo)
        print(card.cardinfo)
    #ratings = []
    rating = 0
    print(card)
    while True:
        s = input('rating from -10 to 10 for balance (s to end): ')
        if s == 's':
            print('stopping')
            stop = True
            break
        try:
            s = float(s)
        except ValueError:
            print('Not a Number!')
            continue
        if s > 10 or s < -10:
            print('Not valid rating!')
            continue
        else:
            rating = s
            break
    if stop:
        break
    x = card.manacost
    cardType = card.cardType
    cards.append(card)
    rarities.append(rarity)
    diffs = eff_spend_func(x, cardinfo[0], cardinfo[1], cardinfo[2], cardType, cardinfo[3], cardinfo[4])
    grad = -rating/10
    stepsize = learnrate*grad
    cardinfo = [cardinfo[i] + diffs[i]*stepsize for i in range(len(cardinfo))]
    print(grad)
    print('power: %f\ninitpow: %f\nzerostrength: %f\nspell_multi: %f\nspell_add: %f' %tuple(cardinfo))

output = open('cardinfo.txt', 'wb')
pk.dump(str(cardinfo), output)
