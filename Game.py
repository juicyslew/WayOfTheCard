from Constants import *
from Card import *
from Deck import *
from Discard import *
from Effect import *
from Hand import *
from Player import *
from randGen import *
import random

class Game():
    def __init__(self):
        #Rule Generation
        self.turn = 0
        self.init_game()

    def init_game():
        self.running = True
        player1 = Player()
        self.game_loop()

    def game_loop():
        while(self.running):
            print(player1.hand)
            i = raw_input('Index of Card to Play: ')
            try int(i):


if __name__ == "__main__":
    game = Game()
    player1.hand.cards[1].play(player1)
