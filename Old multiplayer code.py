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
