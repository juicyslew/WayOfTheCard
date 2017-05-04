from Constants import *
from Card import *
from Deck import *
from Discard import *
from Effect import *
from Hand import *
from Player import *
from randGen import *
import random
import numpy as np
import pygame
from pygame.locals import *
from Board import *
from os import path

class Game():
    def __init__(self):
        #Rule Generation
        self.turn = 0 #Initialize Turns
        self.init_game() #Initialize Game
        self.player_turn = 0

    def init_game(self):
        folder = 'ImageStuff/finimages'
        if not path.isdir(folder):
            os.makedirs(folder)
        else:
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    #elif os.path.isdir(file_path): shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
        self.players = 2
        self.running = True #Set Running
        player_list = []
        totrarprobs = sum(RARITY_PROBS)
        rarities = [np.random.choice(RARITIES, p = RARITY_PROBS) for a in range(DECK_INIT_SIZE)]
        pygame.init()
        for j in range(1, self.players+1):
            print('Player %i:' % j)
            while True: #Create Loop for picking Name
                name = random_name().capitalize() #Create Name
                #print(name) #Display Name
                i = input('\n%s\nAre You Ok With This Name(y/n): ' %name) #Display Name and Check if Player Likes
                if i is 'y': #If player liked
                    if j == 1:
                        player_list.append(Player(name, HAND_INIT_SIZE, rarities)) #Save Player Name
                    else:
                        player_list.append(Player(name, HAND_INIT_SIZE + SECOND_PLAYER_CARD_BONUS, rarities)) #Save Player Name
                    break
                continue #If player doesn't like it, then generate new name
        # player_list.append(Player('Daniel', 4))
        self.game_loop(player_list) #Start Game Loop


    def play_card(self, player, all_players = None):
        """
        Function for putting cards into the field at the beginning of a player's turn
        """
        player = all_players[player]
        opp = all_players[not self.player_turn]
        while True: #Yes, it's bad. Will come back to to see necessity of this.
            not_played = True
            print("### %s's Hand ###" % player.name)
            print(player.hand) #Print the player hand
            print("mana: %i" % player.mana) #display mana
            while True:
                self.update_board()
                i = input('Index of Card to Play (End Placement, Start Attack = 0): ') #get input for card to play
                if i == '0': #if 0 then end function, showing that the player is done with their turn.
                    return True
                elif i == '-1':
                    return
                try:ar
                    i = int(i) #set input to integer
                    try:
                        card = player.hand.cards[i-1] #pull the card from hand
                        if card.stats[COST] > player.mana: #if player can't pay for card
                            print("That Card Costs Too Much!")
                            continue #return False #End Function and Return that it failed, and thus should be run again.
                        if player:
                            if len(player.cards) > MAX_BOARD_SIZE:
                                print("Too many monsters are on the board! You can't play this card.")
                                continue #return False #End Function and Return that it failed, and thus should be run again.
                        else:
                            if len(opp.cards) > MAX_BOARD_SIZE:
                                print("Too many monsters are on the board! You can't play this card.")
                                continue #return False #End Function and Return that it failed, and thus should be run again.
                        #print(card)
                        card.play(self.player_turn, all_players) #If it succeeded, Put the card in the field
                        player.mana -= card.stats[COST] #Subtract from the player's mana
                        player.check_dead(opp) #Check if anything died after the card play effect, which can happen in card.play()
                        opp.check_dead(player)
                        self.update_board()
                        break
                    except IndexError: # If index is out of range, return an error
                        print("\nYou don't have that many cards!")
                except ValueError: # if value converting to int is not possible, return error
                    print('\n`Input a Number!`')
                #return False # Return false showing that something went wrong, the player's play turn should only end once they decide they are done playing card (aka input 0, as shown above)


    def use_cards(self, player, all_players = None):
        """
        Function for using cards to perform actions (Do Work)
        """
        if all_players == None or len(all_players) == 2:
            player = all_players[self.player_turn]
            opp = all_players[not self.player_turn]
            a = player.check_active() # Create Variable that contains the active cards on the board
            active = [str(i+1)+')\n'+str(a[i]) for i in range(len(a))] # Create string to display the active cards on the board
            while len(active) > 0: #Allow attacks as long as there are active creatures on your field.S
                self.update_board()
                print("### %s's FIELD ### \n" % player.name) #Print name of player and their field
                print('\n'.join(active) + '\n') #Print active cards to choose from
                i = input('Index To Attack With (End Turn = 0): ') # Get input of which creature to attack with.
                print('')
                try:
                    i = int(i) #check that input is a number
                    try:
                        if i == 0: #if i == 0, end function
                            break
                        #print(player.cards[i-1])
                        attack_card = a[i-1] # set attack card
                    except IndexError: # if index error
                        print("\nYou don't have that many cards in field!")
                        continue #start over
                except ValueError: # if value error (input isn't an integer)
                    print('\nInput a Number!')
                    continue #start over

                taunt = False
                for card in opp.cards:
                    try:
                        if card.active_effects[TAUNT_INDEX]:
                            taunt = True
                            continue
                    except AttributeError:
                        pass

                print("### %s FIELD ### \n" % opp.name) # Print Opponent Field Header
                print(str(opp) + '\n') # Print Enemy Combatents
                i = input('Index to Attack (Cancel Attack = 0): ') # Get Input for Creature to Attack.
                try:
                    i = int(i) #check that input is an integer
                    try:
                        if i == 0: #if input is 0 go back to first step
                            continue
                        defend_card = opp.cards[i-1] #Set defense Card
                        if taunt and not defend_card.active_effects[TAUNT_INDEX]:
                            print("!!!!!---------------You Must Attack Taunt Cards First---------------!!!!!")
                            continue
                        attack_card.attack(defend_card) #Run the Attack Function
                        damage_dealt = attack_card.stats[ATT]
                        attacking_index = player.cards.index(attack_card)
                        self.board.card_dash((player, attacking_index), (opp, i - 1))
                        self.board.render_damage(damage_dealt, opp, i - 1)
                        if i - 1 != 0:
                            self.board.render_damage(damage_dealt, player, attacking_index)
                    except IndexError: # if index error
                        print("\nThe enemy doesn't have that many cards in field!")
                        continue # Start Over
                except ValueError: # if value error (input isn't an integer)
                    print('\nInput a Number!')
                    continue # Start Over
                player.check_dead(opp) # Check if anything died on your opponent's field
                opp.check_dead(player) # Check if anything died on your field.
                a = player.check_active() # Update a (active cards list)
                active = [str(i+1)+')\n'+str(a[i]) for i in range(len(a))] # update active cards string for display
                self.update_board()
            player.check_dead(opp) # Check if anything died on your opponent's field
            opp.check_dead(player) # Check if anything died on your field.
            self.update_board()
        else:
            pass
        for c in player.cards:
            if c.active_effects[WINDFURY_INDEX] == 2:
                c.active_effects[WINDFURY_INDEX] = 1
            if c.active_effects[FROZEN_INDEX] == 1:
                c.active_effects[FROZEN_INDEX] = 0


    def check_game_end(self, player, all_players = None):
        """
        Function for Checking if the game is over.

        return False means no player is dead and the game can continue
        return True means the game is done and the game_loop is broken

        Three cases in which game ends:
        -- P1 Wins
        -- P2 Wins
        -- Tie
        """
        player1 = all_players[0]
        player2 = all_players[1]
        if player1.dead and player2.dead: #If both players died then
            print("Well shoot.  A Tie.")
            return True
        elif player2.dead:
            print(player1.name + " Wins!!!")
            return True
        elif player1.dead:
            print(player2.name + " Wins!!!")
            return True
        return False

    def game_loop(self, all_players):
        player1 = all_players[0]
        player2 = all_players[1]
        self.player1 = player1
        self.player2 = player2
        """
        Game Loop!  This runs the code of the game in a large while loop that allows the game to continue and function.
        """
        pygame.display.set_caption(random_game_name())
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.screen.fill((150, 50, 150))
        self.board = Board(self.screen, (player1, player2))
        player1.board = self.board
        player2.board = self.board
        player1.screen = self.screen
        player2.screen = self.screen
        self.update_board()
        self.player_turn = False

        while(self.running):  #While the game is still running (Which is essentially While True)
            self.update_board()
            test = 0

            pause = input("\nPress Enter to Start %s's Turn: "% player1.name)
            if TEMP_MANA:
                player1.mana = min((self.turn+1) * MANA_PER_TURN, MAX_MANA) # update mana for player2
            else:
                player1.mana += min((self.turn+1) * MANA_PER_TURN, MAX_MANA)
                if player1.mana >= MANA_LIMIT:
                    player1.mana = MANA_LIMIT
            player1.activate_cards() #Activate cards in the field for usage
            print("\n\n\n\n### %s || %ls ###" % (player1.name, player1.cards[0].stats)) # Print player for turn and Stats
            #print() # Print Player Stats
            for card in player1.cards: #Run through the player cards on the field
                try:
                    card.effect.activate(player1, player2, TRIGGER_BEGIN) #If the cards have a "Begin Turn" Trigger, then activate their effect
                    if(self.check_game_end(self.player_turn, all_players)):
                        break
                except AttributeError or TypeError: #If there is some kind of attribute error then continue (This has to do with the "Player_Card", which is essentially a card but doesn't have some of the essential parts like an effect, Discussed more in Player.py)
                    continue

            self.play_card(0 ,all_players) #Need to unhardcode
            self.use_cards(self.player_turn, all_players) # Run Use Cards Script
            test = player1.deck.draw(player1.hand, CARDS_DRAWN_PER_TURN)    #basically, checking to see if there's damage
            if (test) > 0: # Draw Card From Deck as turn ends
                player1.cards[0].damage(test)
                player1.check_dead(player2)
                self.update_board()
            elif (test) < 0:
                player1.dead = True
            if self.check_game_end(self.player_turn, all_players): # if the game ends, end the game_loop
                break
            player1.check_hand()
            for card in player1.cards: #Run through cards on the field
                try:
                    card.effect.activate(player1, player2, TRIGGER_END) # If the cards have a "End Turn" Trigger, then activate effect
                    player1.check_dead(player2) # Check if anything died
                    player2.check_dead(player1)
                    self.update_board()
                except AttributeError or TypeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                    continue
            if self.check_game_end(self.player_turn, all_players): # if the game ends, end the game_loop
                break

            self.player_turn = not self.player_turn

            if MINION_RECOVER:
                for card in player1.cards[1:]: #Run through cards on the field
                    try:
                        card.heal()
                        self.update_board()
                    except AttributeError or TypeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                        continue
                for card in player2.cards[1:]: #Run through cards on the field
                    try:
                        card.heal()
                        self.update_board()
                    except AttributeError or TypeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                        continue
            self.update_board()

            #while True: # Removed because Outdated# Nested While Loop for the Second Player.  This way when we say "continue" the code starts here instead.  If you have better idea, please mention, this doesn't feel like the best way to do this.
            pause = input("\nPress Enter to Start %s's Turn: "% player2.name)
            if TEMP_MANA:
                player2.mana = min((self.turn+1) * MANA_PER_TURN, MAX_MANA) # update mana for player2
            else:
                player2.mana += min((self.turn+1) * MANA_PER_TURN, MAX_MANA)
                if player2.mana >= MANA_LIMIT:
                    player2.mana = MANA_LIMIT
            print(player2.mana) # display mana
            player2.activate_cards() # activate cards in field (wake them from sleep)
            print("\n\n\n\n### %s || %ls ###" % (player2.name, player2.cards[0].stats)) # Print Player
            #print(player2.cards[0].stats) #Display player stats
            for card in player2.cards: # For card in player2's field
                try:
                    card.effect.activate(player2, player1, TRIGGER_BEGIN) # If card has beginning trigger, activate effect
                except AttributeError or TypeError:
                    continue
            self.play_card(1, all_players)
            self.use_cards(self.player_turn, all_players)
            test = player2.deck.draw(player2.hand, CARDS_DRAWN_PER_TURN)    #basically, checking to see if there's damage
            if (test) > 0: # Draw Card From Deck as turn ends
                player2.cards[0].damage(test)
                player2.check_dead(player1)
                self.update_board()
            elif (test) < 0:
                player2.dead = True
            if self.check_game_end(self.player_turn, all_players): # if the game ends, end the game_loop
                break
            player2.check_hand()
            for card in player2.cards: # For Card in player2.cards:
                try:
                    card.effect.activate(player2, player1, TRIGGER_END) # if card has end trigger, activate effect.
                    self.update_board()
                    if(self.check_game_end(self.player_turn, all_players)):
                        break
                except AttributeError or TypeError:
                    continue
            if self.check_game_end(self.player_turn, all_players): # if the game ends, end the game_loop
                break


            if MINION_RECOVER:
                for card in player1.cards[1:]: #Run through cards on the field
                    try:
                        card.heal()
                        self.update_board()
                    except AttributeError or TypeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                        continue
                for card in player2.cards[1:]: #Run through cards on the field
                    try:
                        card.heal()
                        self.update_board()
                    except AttributeError or TypeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                        continue
            self.player_turn = not self.player_turn
            self.turn += 1 # Increment turn by 1.


    def update_board(self, card_to_animate = None):
        pygame.display.update()
        self.board.update_board(self.screen, self.player1, self.player2, card_to_animate)
        pygame.display.flip()

if __name__ == "__main__": # If this is the run code (Game.py)
    game = Game() # Create Game
