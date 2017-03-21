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
        player1 = Player("Lord Jaraxxus")
        player2 = Player("Medivh")
        self.game_loop(player1, player2)

    def play_card(self, player, opp):
        i = input('Index of Card to Play: ')
        try:
            i = int(i)
            try:
                print(player.hand.cards[i-1])
                player.hand.cards[i-1].play(player, opp)
                player.deck.draw(player.hand, 1)
            except IndexError:
                print("\nYou don't have that many cards!")
                return False
        except ValueError:
            print('\nInput a Number!')
            return False
        return True

    def use_cards(self, player, opp):
        a = player.check_active()
        active = [str(card) for card in a]
        while len(active) > 0:
            print("### YOUR FIELD ### \n")
            print('\n'.join(active) + '\n\n')
            i = input('Index To Attack With (End Turn = 0): ')
            print('')
            try:
                i = int(i)
                try:
                    if i == 0:
                        break
                    print(player.cards[i-1])
                    attack_card = a[i-1]
                except IndexError:
                    print("\nYou don't have that many cards!")
                    continue
            except ValueError:
                print('\nInput a Number!')
                continue
            print("### ENEMY FIELD ### \n")
            print(str(opp) + '\n')
            i = input('Index to Attack (Cancel Attack = 0): ')
            try:
                i = int(i)
                try:
                    if i == 0:
                        continue
                    defend_card = opp.cards[i-1]
                    attack_card.attack(defend_card)
                except IndexError:
                    print("\nYou don't have that many cards!")
                    continue
            except ValueError:
                print('\nInput a Number!')
                continue
            player.check_dead()
            opp.check_dead()
            a = player.check_active()
            active = [str(card) for card in a]
    def check_game_end(self, player1, player2):
        if player1.dead and player2.dead:
            print("Well Shoot.  A Tie.")
            return True
        elif player2.dead:
            print(player1.name + " Wins!!!")
            return True
        elif player1.dead:
            print(player2.name + " Wins!!!")
            return True
        return False
    def game_loop(self, player1, player2):
        while(self.running):
            player1.activate_cards()
            print("### PLAYER 1 ###")
            print(player1.hand)
            for card in player1.cards:
                try:
                    card.effect.activate(player1, player2, TRIGGER_BEGIN)
                except AttributeError:
                    pass
            while True:
                if not self.play_card(player1, player2):
                    continue
                break
            player1.check_dead()
            player2.check_dead()
            print(player1)
            self.use_cards(player1, player2)
            player1.check_dead()
            player2.check_dead()
            for card in player1.cards:
                try:
                    card.effect.activate(player1, player2, TRIGGER_END)
                except AttributeError:
                    pass
            if self.check_game_end(player1, player2):
                break

            while True:
                player2.activate_cards()
                print("\n### PLAYER 2 ###")
                print(player2.hand)
                for card in player2.cards:
                    try:
                        card.effect.activate(player2, player1, TRIGGER_BEGIN)
                    except AttributeError:
                        pass
                while True:
                    if not self.play_card(player2, player1):
                        continue
                    break
                player1.check_dead()
                player2.check_dead()
                print(player2)
                self.use_cards(player2, player1)
                player1.check_dead()
                player2.check_dead()
                for card in player2.cards:
                    try:
                        card.effect.activate(player2, player1, TRIGGER_END)
                    except AttributeError:
                        pass
                break
            if self.check_game_end(player1, player2):
                break
            self.turn += 1


if __name__ == "__main__":
    game = Game()
