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
        self.turn = 0 #Initialize Turns
        self.init_game() #Initialize Game

    def init_game(self):
        self.running = True #Set Running
        print('Player 1:')
        while True: #Create Loop for picking Name
            name = random_name().capitalize() #Create Name
            print(name) #Display Name
            i = input('Are You Ok With This Name(y/n): ') #Check if Player Likes
            if i is 'y': #If player liked
                player1 = Player(name) #Save Player Name
                break
            continue #If player doesn't like it, then generate new name
        print('Player 2:')
        while True: #Create Loop for picking Name
            name = random_name().capitalize() #Create Name
            print(name) #Display Name
            i = input('Are You Ok With This Name(y/n): ') #Check if Player Likes
            if i is 'y': #If player liked
                player2 = Player(name) #Save Player Name
                break
            continue #If player doesn't like it, then generate new name
        self.game_loop(player1, player2) #Start Game Loop

    def play_card(self, player, opp): #Function for putting cards into the field
        print(player.mana) #display mana
        i = input('Index of Card to Play (End Placement, Start Attack = 0): ') #get input for card to play
        if i == '0': #if 0 then end function
            return True
        try:
            i = int(i) #set input to integer
            try:
                card = player.hand.cards[i-1] #pull the card from hand
                if card.stats[COST] > player.mana: #if player can't pay for card
                    print("That Card Cost's Too Much!")
                    return False #End Function
                #print(card)
                card.play(player, opp)
                player.mana -= card.stats[COST]
                player.check_dead(opp)
                opp.check_dead(player)
            except IndexError:
                print("\nYou don't have that many cards!")
        except ValueError:
            print('\nInput a Number!')
        return False

    def use_cards(self, player, opp):
        a = player.check_active()
        active = [str(i+1)+')\n'+str(a[i]) for i in range(len(a))]
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
                    print("\nYou don't have that many cards in field!")
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
                    print("\nThe enemy doesn't have that many cards in field!")
                    continue
            except ValueError:
                print('\nInput a Number!')
                continue
            player.check_dead(opp)
            opp.check_dead(player)
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
        """
        THIS NEEDS MORE COMMENTS, ADD THEM AS POSSIBLE.
        """
        while(self.running):
            player1.mana = min((self.turn+1) * MANA_PER_TURN, MAX_MANA)
            player1.activate_cards()
            print("### PLAYER 1 ###")
            for card in player1.cards:
                try:
                    card.effect.activate(player1, player2, TRIGGER_BEGIN)
                except AttributeError:
                    continue
            while True:
                print(player1.hand)
                if not self.play_card(player1, player2):
                    continue
                break
            self.use_cards(player1, player2)
            player1.deck.draw(player1.hand, 1)
            for card in player1.cards:
                try:
                    card.effect.activate(player1, player2, TRIGGER_END)
                    player1.check_dead(player2)
                    player2.check_dead(player1)
                except AttributeError:
                    continue
            if self.check_game_end(player1, player2):
                break

            while True:
                player2.mana = min((self.turn+1) * MANA_PER_TURN, MAX_MANA)
                print(player2.mana)
                player2.activate_cards()
                print("\n### PLAYER 2 ###")
                for card in player2.cards:
                    try:
                        card.effect.activate(player2, player1, TRIGGER_BEGIN)
                    except AttributeError:
                        continue
                while True:
                    print(player2.hand)
                    if not self.play_card(player2, player1):
                        continue
                    break
                print(player2)
                self.use_cards(player2, player1)
                player2.deck.draw(player2.hand, 1)
                for card in player2.cards:
                    try:
                        card.effect.activate(player2, player1, TRIGGER_END)
                        player1.check_dead(player2)
                        player2.check_dead(player1)
                    except AttributeError:
                        continue
                break
            if self.check_game_end(player1, player2):
                break
            self.turn += 1


if __name__ == "__main__":
    game = Game()
