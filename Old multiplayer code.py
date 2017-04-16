        else:
            while True:
                player = all_players[player]
                print("### %s's Hand ###" % all_players[player].name)
                print(all_players[player].hand) #Print to be out around 2020, which means he will have been writing the first 5 for 58 yethe player hand
                print("mana: %i" % all_players[player].mana) #display mana
                while True:
                    # self.update_board()
                    i = input('Index of Card to Play (End Placement, Start Attack = 0): ') #get input for card to play
                    if i == '0': #if 0 then end function, showing that the player is done with their turn.
                        return True
                    elif i == '-1':
                        return
                    try:
                        i = int(i) #set input to integer
                        try:
                            card = player.hand.cards[i-1] #pull the card from hand
                            if card.stats[COST] > player.mana: #if player can't pay for card
                                print("That Card Costs Too Much!")
                                continue #return False #End Function and Return that it failed, and thus should be run again.
                            #print(card)

                            card.play(self.player_turn, self.players) #If it succeeded, Put the card in the field
                            all_players[player].mana -= card.stats[COST] #Subtract from the player's mana
                            for peeps in all_players:
                                peeps.check_dead(peeps, all_players) #Check if anything died after the card play effect, which can happen in card.play()
                            # self.update_board()
                            break
                        except IndexError: # If index is out of range, return an error
                            print("\nYou don't have that many cards!")
                    except ValueError: # if value converting to int is not possible, return error
                        print('\nInput a Number!')
                    #return False # Return false showing that something went wrong, the player's play turn should only end once they decide they are done playing card (aka input 0, as shown above)

#Game.py
else: #Screw Pygame for now; I refuse to have it implemented.
    self.players = all_players
    self.player_turn = 0

    # pygame.init()
    # pygame.display.set_caption(random_game_name())
    # self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    # self.screen.fill((0, 0, 255))
    # self.board = Board(self.screen)
    # self.update_board()

    while(self.running):  #While the game is still running (Which is essentially While True)
        # self.update_board()

        pause = input("\nPress Enter to Start %s's Turn: " % self.players[self.player_turn].name)
        self.players[self.player_turn].mana = min((self.turn+1) * MANA_PER_TURN, MAX_MANA) #Update player mana for the turn based on which turn it is.
        self.players[self.player_turn].activate_cards() #Activate cards in the field for usage
        print("\n\n\n\n### %s || %ls ###" % (self.players[self.player_turn].name, self.players[self.player_turn].cards[0].stats)) # Print player for turn and Stats
        #print() # Print Player Stats
        for card in self.players[self.player_turn].cards: #Run through the player cards on the field
            try:
                card.effect.activate(player1, player2, TRIGGER_BEGIN, all_players = self.players) #If the cards have a "Begin Turn" Trigger, then activate their effect
            except AttributeError: #If there is some kind of attribute error then continue (This has to do with the "Player_Card", which is essentially a card but doesn't have some of the essential parts like an effect, Discussed more in Player.py)
                continue
        playable = True
        self.play_card(self.player_turn, self.players)
        self.use_cards(self.player_turn, self.players) # Run Use Cards Script
        self.players[self.player_turn].deck.draw(self.players[self.player_turn].hand, 1) # Draw Card From Deck as turn ends

        for card in self.players[self.player_turn].cards: #Run through cards on the field
            try:
                card.effect.activate(player1, player2, TRIGGER_END, all_players = self.players) # If the cards have a "End Turn" Trigger, then activate effect
                for i in range(0, len(all_players)):
                    player1.check_dead(player2, all_players = self.players) # Check if anything died
                    player2.check_dead(player1, all_players = self.players)
            # self.update_board()
            except AttributeError: # Attribute error check, in case activating the card didn't work due to not having the attributes necessary (player_card)
                continue
        if self.check_game_end(self.player_turn, self.players): # if the game ends, end the game_loop
            break
        # self.update_board()
        self.player_turn += 1
        if self.player_turn >= len(self.players):
            self.player_turn = 0
            self.turn += 1 # Increment turn by 1.

(Card.py)
        else:#3+ players
            if self.cardType == TYPE_CREATURE:
                all[0].cards.append(all[0].hand.cards.pop(all[0].hand.cards.index(self)))
                try:
                    self.effect.activate(all[0], all[1:], TRIGGER_PLAY)
                except AttributeError:
                    pass
            if self.cardType == TYPE_SPELL:
                self.effect.activate(all[0], all[1:], TRIGGER_PLAY)
                all[0].hand.cards.pop(all[0].hand.cards.index(self))
