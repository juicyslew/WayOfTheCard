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

    def init_game(self):
        self.running = True
        player1 = Player()
        player2 = Player()
        self.game_loop(player1, player2)

    def game_loop(self, player1, player2):
        while(self.running):
            print("### PLAYER 1 ###")
            print(player1)
            i = input('Index of Card to Play: ')
            try:
                i = int(i)
                try:
                    print(player1.hand.cards[i-1])
                    player1.hand.cards[i-1].play(player1)
                    player1.deck.draw(player1.hand)
                except IndexError:
                    print("\nYou don't have that many cards!")
            except ValueError:
                print('\nInput a Number!')

            print("### PLAYER 2 ###")
            print(player2)
            i = input('Index of Card to Play: ')
            try:
                i = int(i)
                try:
                    print(player2.hand.cards[i-1])
                    player2.hand.cards[i-1].play(player2)
                    player2.deck.draw(player2.hand)
                except IndexError:
                    print("\nYou don't have that many cards!")
            except ValueError:
                print('\nInput a Number!')


if __name__ == "__main__":
    game = Game()
