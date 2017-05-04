from Constants import *
from randGen import *
import pygame
import os

class Board():
    def __init__(self, screen, players):
        self.clock = pygame.time.Clock()
        self.screen = screen

        # Create font objects
        typeface = "myriad pro cond"
        self.card_name_font = pygame.font.SysFont(typeface, 17)   #   sets card fonts
        self.hero_name_font = pygame.font.SysFont(typeface, PLAYER_CARD_FONT_SIZE)
        self.card_text_font = pygame.font.SysFont(typeface, CREATURE_CARD_FONT_SIZE)
        self.mana_font = pygame.font.SysFont(typeface, MANA_COST_FONT_SIZE)
        self.stats_font = pygame.font.SysFont(typeface, CREATURE_STATS_FONT_SIZE)
        self.health_font = pygame.font.SysFont(typeface, PLAYER_HEALTH_FONT_SIZE)
        self.card_name_font_small = pygame.font.SysFont(typeface, round(17*0.75)+2)   #   sets card fonts
        self.hero_name_font_small = pygame.font.SysFont(typeface, round(PLAYER_CARD_FONT_SIZE*0.75)+1)
        self.card_text_font_small = pygame.font.SysFont(typeface, round(CREATURE_CARD_FONT_SIZE*0.75)+1)
        self.mana_font_small = pygame.font.SysFont(typeface, round(MANA_COST_FONT_SIZE*0.75)+1)
        self.stats_font_small = pygame.font.SysFont(typeface, round(CREATURE_STATS_FONT_SIZE*0.75)+1)
        self.health_font_small = pygame.font.SysFont(typeface, round(PLAYER_HEALTH_FONT_SIZE*0.75)+1)

        #   Load card borders
        self.bord_c = pygame.image.load(os.path.join('CardBorder.png')).convert_alpha()
        self.bord_c = pygame.transform.scale(self.bord_c, (CARD_WIDTH, CARD_HEIGHT))
        self.bord_u = pygame.image.load(os.path.join('CardBorderU.png')).convert_alpha()
        self.bord_u = pygame.transform.scale(self.bord_u, (CARD_WIDTH, CARD_HEIGHT))
        self.bord_r = pygame.image.load(os.path.join('CardBorderR.png')).convert_alpha()
        self.bord_r = pygame.transform.scale(self.bord_r, (CARD_WIDTH, CARD_HEIGHT))
        self.bord_l = pygame.image.load(os.path.join('CardBorderL.png')).convert_alpha()
        self.bord_l = pygame.transform.scale(self.bord_l, (CARD_WIDTH, CARD_HEIGHT))

        self.bord_dict = {COMMON: self.bord_c, UNCOMMON: self.bord_u, RARE: self.bord_r, EPIC: self.bord_l, LEGENDARY: self.bord_l}
        self.bc_off = 0.9
        self.bc_move = (12, 14)

        self.cardwidth = CARD_WIDTH         #  width in pixels of a card. Other scaling changes because of this
        self.cardheight = CARD_HEIGHT
        self.player1 = players[0]           #  add players to class board for easy access
        self.player2 = players[1]

        #   Load background image and icons
        backgrounds = ['BackgroundImage.jpg', 'bk2.jpg', 'bk3.jpg', 'bk4.jpg', 'bk5.jpg', 'bk6.jpg', 'bk7.jpg']
        self.backdrop = pygame.image.load(os.path.join(random.choice(backgrounds))).convert_alpha()
        self.backdrop = pygame.transform.scale(self.backdrop, (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2)))
        self.change_brightness(self.backdrop, 0.75)     #   Darken image slightly
        self.boom = pygame.image.load(os.path.join('redglow2.png')).convert_alpha()
        self.axe = pygame.image.load(os.path.join('axe.png')).convert_alpha()
        self.bear = pygame.image.load(os.path.join('bear.png')).convert_alpha()
        self.damage = [self.boom, self.axe, self.bear]
        self.heal = pygame.image.load(os.path.join('heal_icon.png')).convert_alpha()
        self.buff = pygame.image.load(os.path.join('buff_icon.png')).convert_alpha()
        self.shield = pygame.image.load(os.path.join('div_shield_icon.png')).convert_alpha()
        self.ice = pygame.image.load(os.path.join('ice.jpg')).convert_alpha()
        self.glow = pygame.image.load(os.path.join('glow.jpg')).convert_alpha()
        self.double_sword = pygame.image.load(os.path.join('crossedswords.png')).convert_alpha()
        self.mana_crystal = pygame.image.load(os.path.join('crystal.png')).convert_alpha()
        self.mana_crystal = pygame.transform.scale(self.mana_crystal, (50, 50))

        #   Set board constants
        self.effect_spacing = 10        #   Spacing between lines of effect text
        self.name_spacing = 15          #   Spacing between lines of card name
        self.char_length = 24           #   Max number of characters in a line
        self.effnames = {WINDFURY_EFFECT: generate_effect_name(WINDFURY_EFFECT),
        CHARGE_EFFECT: generate_effect_name(CHARGE_EFFECT),
        DIVINE_SHIELD_EFFECT: generate_effect_name(DIVINE_SHIELD_EFFECT),
        TAUNT_EFFECT: generate_effect_name(TAUNT_EFFECT)}
        self.anim_speed = 24            #   FPS of all animations
        self.scale_img = 0.5
        self.end_turn = pygame.Surface(END_TURN_SHAPE) #End Turn is 100 by 50
        self.end_turn.fill(PURPLE)
        self.end_turn_rect = pygame.Rect(END_TURN_POS, END_TURN_SHAPE)


    def render_card(self, card_obj, position, is_animated = False, is_dash = False, scale_x = 1, scale_y = 1):  #   display card on screen
        card = pygame.Surface((self.cardwidth * scale_x, self.cardheight * scale_y))
        try:
            if card_obj.cardType == TYPE_CREATURE and not card_obj.arted:
                #   Load art using path in card
                card_obj.art = pygame.image.load(card_obj.art_path).convert_alpha()
                #   Compress then uncompress to minimize procecssing power
                card_obj.art = pygame.transform.scale(card_obj.art, (int(CARD_WIDTH*0.86*self.scale_img), int(CARD_WIDTH*0.495*self.scale_img)))
                card_obj.art = pygame.transform.scale(card_obj.art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
                art = card_obj.art
                card_obj.arted = True
            elif card_obj.arted:
                art = card_obj.art
        except:
            pass

        if is_animated or is_dash:
            for alpha in range(30):
                card.fill((255, 255, 255))
                # text_surface = self.render_text(card_obj, position)
                x = 0
                y = 0
                (name, mana, stats, effect_text) = self.read_card(card_obj)
                name_height = 0
                art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86*self.bc_off), int(CARD_WIDTH*0.495*self.bc_off)))    #   renders art
                card.blit(art, (x + int(CARD_WIDTH*0.045) + self.bc_move[0], y + 30 + self.bc_move[1]))
                card.blit(self.bord_dict[card_obj.rarity], (x, y))
                for line in name:   #   renders name in individual lines
                    name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                    card.blit(name_render, (x + 15, y + name_height + 15))
                    name_height += self.name_spacing
                mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                card.blit(mana_render, (x + self.cardwidth - 20, y))
                stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                card.blit(stats_render, (x + 10, y + self.cardheight - 25))
                effect_height = 0
                for line in effect_text:    #   renders effect text in individual lines
                    effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                    card.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                    effect_height += self.effect_spacing
                #card.set_alpha(50)
                if card_obj.active_effects[WINDFURY_INDEX] == 1:    #   Adds swords icon if card has windfury
                    swords = pygame.transform.scale(self.double_sword, (int(self.cardwidth/6), int(self.cardwidth/6)))
                    swords_rect = swords.get_rect()
                    self.change_alpha(swords, 180)
                    swords_rect = swords_rect.move(x + self.cardwidth - int(self.cardwidth/6) - 12, y + self.cardheight - int(self.cardwidth/6) - 12)
                    card.blit(swords, swords_rect)
                #if card_obj.cardType == TYPE_CREATURE:  #   only creatures have art
                #    card.blit(art, (int(CARD_WIDTH*0.045), 30))
                card.set_alpha(10 * alpha)     #    Makes card
                if not is_animated:
                    card.set_alpha(255)
                self.screen.blit(card, (position[0], position[1]))
                pygame.display.flip()
                if not is_animated:
                    break
                self.clock.tick(20)
        else:
                card.fill((255, 255, 255))
                self.screen.blit(card, (position[0], position[1]))


    def read_card(self, card):  #   turns card object into easily read tuple
        effect_text = ""
        name = card.name
        name_length = 20
        while len(name) - name.rfind("\n") > name_length: # arranges name into lines of length <= name_length
            index = name.rfind("\n") + name_length
            while name[index] != " " and index > 0:
                index -= 1
            name = name[0:index + 1] + "\n" + name[index + 1:]
        name = name.split("\n")
        stats = card.stats
        mana = card.manacost
        effect = card.effect
        tot_effect_text = ""
        if not effect:
            tot_effect_text = ""
        else: # generates card text
            #if type(effect.effect) == 0:
            #    a = 0
            #else:
            #    a = 1
            if not type(effect.effect) == int:
                for i in range(len(effect.effect)):
                    try:
                        additive = (trig == effect.trigger[i] and not keyword)  #   determines whether effect trigger is the same as last effect
                    except UnboundLocalError:
                        additive = 0
                    eff = effect.effect[i]
                    trig = effect.trigger[i]
                    targ = effect.target[i]
                    num = effect.numeric[i]
                    keyword = False
                    if eff == None:
                        continue
                    if additive:
                        tot_effect_text = tot_effect_text[0:-2]
                        effect_text = ", then "     #   if trigger is same as last effect, make text in one sentence

                    #   Generates effect text based on what the creature's effect is
                    elif card.cardType == TYPE_CREATURE:
                        effect_text = "%s," % (TRIGGER_TEXT_DICT[trig])
                    if eff == DEAL_EFFECT:
                        effect_text += "deal %s damage to %s." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == DRAW_EFFECT:
                        effect_text += "%s draws %s cards." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == HEAL_EFFECT:
                        effect_text += "heal %s for %s damage." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == SUMMON_EFFECT:
                        effect_text += "%s summons a random %s-mana creature." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == BUFF_EFFECT:
                        effect_text += "%s gets +%s/+%s." % (TARGET_TEXT_DICT[targ], num[0], num[1])
                    elif eff == SPLIT_DEAL_EFFECT:
                        effect_text += "deal %s damage split randomly between %s." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == SPLIT_HEAL_EFFECT:
                        effect_text += "heal %s damage split randomly between %s." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == TAUNT_EFFECT:
                        effect_text += "give %s to %s." % (self.effnames[TAUNT_EFFECT], TARGET_TEXT_DICT[targ])
                    elif eff == DIVINE_SHIELD_EFFECT:
                        effect_text += "give %s to %s." % (self.effnames[DIVINE_SHIELD_EFFECT], TARGET_TEXT_DICT[targ])
                    elif eff == CHARGE_EFFECT:
                        effect_text += "give %s to %s." % (self.effnames[CHARGE_EFFECT], TARGET_TEXT_DICT[targ])
                    elif eff == WINDFURY_EFFECT:
                        effect_text += "give %s to %s." % (self.effnames[WINDFURY_EFFECT], TARGET_TEXT_DICT[targ])
                    elif eff == DEBUFF_EFFECT:
                        effect_text += "%s gets -%s/-%s." % (TARGET_TEXT_DICT[targ], num[0], num[1])
                    elif eff == DEVOLVE_EFFECT:
                        effect_text += "devolve %s by %s." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == REVOLVE_EFFECT:
                        effect_text += "revolve %s." % (TARGET_TEXT_DICT[targ])
                    elif eff == EVOLVE_EFFECT:
                        effect_text += "evolve %s by %s." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == DESTROY_EFFECT:
                        effect_text += "destroy %s." % (TARGET_TEXT_DICT[targ])
                    elif eff == FREEZE_EFFECT:
                        effect_text += "freeze %s for %s turns." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == AMANA_EFFECT:
                        effect_text += "%s Gains %s Mana" % (TARGET_TEXT_DICT[targ], num)
                    elif eff == RMANA_EFFECT:
                        effect_text += "%s loses %s mana next turn." % (TARGET_TEXT_DICT[targ], num)
                    elif eff == RETURN_EFFECT:
                        effect_text += "Return creature to %s's hand" % (TARGET_TEXT_DICT[targ])
                    elif eff == REANIMATE_EFFECT:
                        effect_text += "Revives %s creatures for %s." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == ADD_CARD_EFFECT:
                        effect_text += "Adds %s Cards to %s's Hand." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == ADD_CREATURE_EFFECT:
                        effect_text += "Adds %s Creatures to %s's Hand." % (num, TARGET_TEXT_DICT[targ])
                    elif eff == ADD_SPELL_EFFECT:
                        effect_text += "Adds %s Spells to %s's Hand." % (num, TARGET_TEXT_DICT[targ])
                    if targ == TARGET_THIS_CREATURE and eff in [TAUNT_EFFECT, DIVINE_SHIELD_EFFECT, WINDFURY_EFFECT, CHARGE_EFFECT]:
                        effect_text = self.effnames[eff] + ". "
                        keyword = True
                    effect_text = effect_text.lower().capitalize()
                    if effect_text != tot_effect_text:
                        tot_effect_text = tot_effect_text + effect_text
            else:
                tot_effect_text = tot_effect_text + ''        # maximum characters on each line of text
        while len(tot_effect_text) - tot_effect_text.rfind("\n") > self.char_length: # arranges effect text into lines
            index = tot_effect_text.rfind("\n") + self.char_length
            while tot_effect_text[index] != " " and index > 0:
                index -= 1
            tot_effect_text = tot_effect_text[0:index + 1] + "\n" + tot_effect_text[index + 1:]
        tot_effect_text = tot_effect_text.split("\n")
        return (name, mana, stats, tot_effect_text)

    def update_board(self, screen, player1, player2, card_to_animate = None, card_not_to_render = None, all_players = None, turn_status = 3):   #   updates board with current cards in play
        """
        Displaying an unknown number of players isn't my problem but I left an 'all' here anyway.
        """

        if turn_status == 3:
            turn_status = player1.turn_status
        #   Render screen background
        screen.fill((200, 100, 200))
        bkgd = pygame.transform.scale(self.backdrop, (WINDOW_WIDTH, WINDOW_HEIGHT))
        bkgd_rect = bkgd.get_rect()
        self.screen.blit(bkgd, bkgd_rect)

        #   Initialize some useful constants
        xhalf = screen.get_size()[0]/2
        yhalf = screen.get_size()[1]/2
        card_y_offset = 30
        name_y_offset = 15
        name_x_offset = 15
        health_x_offset = 35
        health_y_offset = 45

        #   Create player 2 card
        self.screen.blit(self.end_turn, (WINDOW_WIDTH-END_TURN_SHAPE[0], (WINDOW_HEIGHT-END_TURN_SHAPE[1])/2))
        self.render_card(player2.cards[0], (xhalf - self.cardwidth/2, card_y_offset))
        screen.blit(self.bord_dict[COMMON], (xhalf - self.cardwidth/2, card_y_offset))
        player2_name_render = self.hero_name_font.render(player2.player.name, 1, (0, 0, 0))          #   define name font object
        player2_health_render = self.health_font.render(str(player2.player.stats[2]), 1, (0, 0, 0))     #   define health font object
        screen.blit(player2_name_render, (xhalf - self.cardwidth/2 + name_x_offset, 30 + name_y_offset))                  #   blit player 2 name
        screen.blit(player2_health_render, (xhalf - self.cardwidth/2 + health_x_offset, card_y_offset + health_y_offset))

        #   Create player 1 card
        self.render_card(player1.cards[0], (xhalf - self.cardwidth/2, screen.get_size()[1] - card_y_offset - self.cardheight))
        screen.blit(self.bord_dict[COMMON], (xhalf - self.cardwidth/2, screen.get_size()[1] - card_y_offset - self.cardheight))
        player1_name_render = self.hero_name_font.render(player1.player.name, 1, (0, 0, 0))
        player1_health_render = self.health_font.render(str(player1.player.stats[2]), 1, (0, 0, 0))     #   define health font object
        screen.blit(player1_name_render, (xhalf - self.cardwidth/2 + name_x_offset, screen.get_size()[1] - card_y_offset - self.cardheight + name_y_offset))
        screen.blit(player1_health_render, (xhalf - self.cardwidth/2 + health_x_offset, -card_y_offset + health_y_offset + 2*yhalf - self.cardheight))

        if turn_status == 2:
            self.render_mana(player2.mana, (25, 200))
        if turn_status == 1:
            self.render_mana(player1.mana, (25, WINDOW_HEIGHT - 200 - 50))
        card_backlog = []   #   List of cards to render after all other cards are rendered

        #   Render all cards in hands
        for card in player2.cards[1:] + player1.cards[1:]:
            art = card.art
            #art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
            try:
                x = player2.cards.index(card)*(self.cardwidth + 20) + 80
                y = yhalf - 15 - self.cardheight
                if card is card_not_to_render:
                    continue
                elif card is card_to_animate:
                    card_backlog.append([card, (x, y)]) #   animated cards are rendered last
                    #self.render_card(card, (x, y), True)
                else:
                    self.render_card(card, (x, y))
                if card is not card_to_animate and card is not card_not_to_render and card.arted:
                    try:
                        art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86*self.bc_off), int(CARD_WIDTH*0.495*self.bc_off)))
                        screen.blit(art, (x + int(CARD_WIDTH*0.045) + self.bc_move[0], y + 30 + self.bc_move[1]))
                    except:
                        pass
                    screen.blit(self.bord_dict[card.rarity], (x, y))
                    if card.active_effects[DIVINE_SHIELD_INDEX] == 1:   #   Render yellow glow if card has divine shield
                        glow = pygame.transform.scale(self.glow, (self.cardwidth, self.cardheight))
                        glow_rect = glow.get_rect()
                        self.change_alpha(glow, 100)
                        glow_rect = glow_rect.move(x, y)
                        self.screen.blit(glow, glow_rect)
                    (name, mana, stats, effect_text) = self.read_card(card)
                    name_height = 0
                    for line in name:   #   renders name in individual lines
                        name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                        screen.blit(name_render, (x + 15, y + name_height + 15))
                        name_height += self.name_spacing
                    mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                    screen.blit(mana_render, (x + self.cardwidth - 20, y))
                    stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                    screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                    effect_height = 0
                    for line in effect_text:    #   renders effect text in individual lines
                        effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                        screen.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                        effect_height += self.effect_spacing
                    if card.active_effects[WINDFURY_INDEX] == 1:    #   renders swords if card has windfury
                        swords = pygame.transform.scale(self.double_sword, (int(self.cardwidth/6), int(self.cardwidth/6)))
                        swords_rect = swords.get_rect()
                        self.change_alpha(swords, 180)
                        swords_rect = swords_rect.move(x + self.cardwidth - int(self.cardwidth/6) - 12, y + self.cardheight - int(self.cardwidth/6) - 12)
                        self.screen.blit(swords, swords_rect)
                    if card.active_effects[FROZEN_INDEX] == 1:  #   Render ice effect if card is frozen
                        ice = pygame.transform.scale(self.ice, (self.cardwidth, self.cardheight))
                        ice_rect = ice.get_rect()
                        self.change_alpha(ice, 180)
                        ice_rect = ice_rect.move(x, y)
                        self.screen.blit(ice, ice_rect)


            except ValueError:
                art = card.art
                #art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
                try:
                    x = player1.cards.index(card)*(self.cardwidth + 20) + 80
                    y = yhalf + 15
                    if card is card_not_to_render:
                        continue
                    elif card is card_to_animate:
                        card_backlog.append([card, (x, y)]) #   animated cards are rendered last
                    else:
                        self.render_card(card, (x, y))
                    if card is not card_to_animate and card is not card_not_to_render:
                        try:
                            art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86*self.bc_off), int(CARD_WIDTH*0.495*self.bc_off)))
                            screen.blit(art, (x + int(CARD_WIDTH*0.045) + self.bc_move[0], y + 30 + self.bc_move[1]))
                        except:
                            pass
                        screen.blit(self.bord_dict[card.rarity], (x, y))
                        if card.active_effects[DIVINE_SHIELD_INDEX] == 1:
                            glow = pygame.transform.scale(self.glow, (self.cardwidth, self.cardheight))
                            glow_rect = glow.get_rect()
                            self.change_alpha(glow, 100)
                            glow_rect = glow_rect.move(x, y)
                            self.screen.blit(glow, glow_rect)
                        (name, mana, stats, effect_text) = self.read_card(card)
                        name_height = 0
                        for line in name:   #   renders name in individual lines
                            name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                            screen.blit(name_render, (x + 15, y + name_height + 15))
                            name_height += self.name_spacing
                        mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                        screen.blit(mana_render, (x + self.cardwidth - 20, y))
                        stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                        screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                        height = 0
                        for line in effect_text:    #   renders effect text in individual lines
                            effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                            screen.blit(effect_render, (x + 15, y + self.cardheight/2 + height))
                            height += self.effect_spacing
                        if card.active_effects[WINDFURY_INDEX] == 1:
                            swords = pygame.transform.scale(self.double_sword, (int(self.cardwidth/6), int(self.cardwidth/6)))
                            swords_rect = swords.get_rect()
                            self.change_alpha(swords, 180)
                            swords_rect = swords_rect.move(x + self.cardwidth - int(self.cardwidth/6) - 12, y + self.cardheight - int(self.cardwidth/6) - 12)
                            self.screen.blit(swords, swords_rect)
                        if card.active_effects[FROZEN_INDEX] == 1:
                            ice = pygame.transform.scale(self.ice, (self.cardwidth, self.cardheight))
                            ice_rect = ice.get_rect()
                            self.change_alpha(ice, 180)
                            ice_rect = ice_rect.move(x, y)
                            self.screen.blit(ice, ice_rect)
                except ValueError:
                    pass

        for card in player2.hand.cards + player1.hand.cards:
            #art = pygame.transform.scale(art, (int(CARD_WIDTH*0.43), int(CARD_WIDTH*0.2475)))
            try:
                a = player1.hand.cards.index(card)
                if turn_status == 3 or turn_status == 1:
                    x = player1.hand.cards.index(card)*(self.cardwidth*0.75 + 10) + 10
                    if player1.hand.cards.index(card) > 5:
                        x += 370
                    y = WINDOW_HEIGHT - self.cardheight*0.75 - 30
                    if card is card_not_to_render:
                        continue
                    elif card is card_to_animate:
                        card_backlog.append([card, (x, y)])
                        #self.render_card(card, (x, y), True)
                    else:
                        self.render_card(card, (x, y), scale_x = 0.75, scale_y = 0.75)
                    if card is not card_to_animate and card is not card_not_to_render:
                        if not card.arted:
                            card.art = pygame.image.load(card.art_path).convert_alpha()
                            card.art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.86*self.scale_img), int(CARD_WIDTH*0.495*self.scale_img)))
                            art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.43*1.4), int(CARD_WIDTH * 0.2375 * 1.4)))
                            screen.blit(art, (x + int(CARD_WIDTH*0.045 + 20), y + 30))
                            card.arted = True
                        else:
                            art = card.art
                            art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.43*1.4), int(CARD_WIDTH * 0.2375 * 1.4)))
                            screen.blit(art, (x + int(CARD_WIDTH*0.045), y + 30))
                        small_border = pygame.transform.scale(self.bord_dict[card.rarity], (int(CARD_WIDTH*0.75), int(CARD_HEIGHT*0.75)))
                        screen.blit(small_border, (x, y))
                        (name, mana, stats, effect_text) = self.read_card(card)
                        name_height = -4
                        for line in name:   #   renders name in individual lines
                            name_render = self.card_name_font_small.render(line, 1, (0, 0, 0))
                            screen.blit(name_render, (x + 15, y + name_height + 15))
                            name_height += self.name_spacing - 4
                        mana_render = self.mana_font_small.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                        screen.blit(mana_render, (x + self.cardwidth*0.75 - 15, y))
                        if card.cardType == TYPE_CREATURE:
                            stats_render = self.stats_font_small.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                            screen.blit(stats_render, (x + 10, y + self.cardheight*0.75 - 25))
                        effect_height = 15
                        for line in effect_text:    #   renders effect text in individual lines
                            effect_render = self.card_text_font_small.render(line, 1, (0, 0, 0))
                            screen.blit(effect_render, (x + 7, y + self.cardheight/3 + effect_height))
                            effect_height += self.effect_spacing


            except ValueError:
                #art = pygame.transform.scale(art, (int(CARD_WIDTH*0.43), int(CARD_WIDTH*0.2375)))
                try:
                    if turn_status == 2 or turn_status == 3:
                        x = player2.hand.cards.index(card)*(self.cardwidth*0.75 + 10) + 10
                        if player2.hand.cards.index(card) > 5:
                            x += 370
                        y = 30
                        if card is card_not_to_render:
                            continue
                        elif card is card_to_animate:
                            self.render_card(card, (x, y), True, scale_x = 0.75, scale_y = 0.75)
                        else:
                            self.render_card(card, (x, y), scale_x = 0.75, scale_y = 0.75)
                        if card is not card_to_animate and card is not card_not_to_render:
                            if not card.arted:
                                card.art = pygame.image.load(card.art_path).convert_alpha()
                                card.art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.86*self.scale_img), int(CARD_WIDTH*0.495*self.scale_img)))
                                art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.43*1.4), int(CARD_WIDTH * 0.2375 * 1.4)))
                                screen.blit(art, (x + int(CARD_WIDTH*0.045 + 20), y + 30))
                                card.arted = True
                            else:
                                art = card.art
                                art = pygame.transform.scale(card.art, (int(CARD_WIDTH*0.43*1.4), int(CARD_WIDTH * 0.2375 * 1.4)))
                                screen.blit(art, (x + int(CARD_WIDTH*0.045), y + 30))
                            small_border = pygame.transform.scale(self.bord_dict[card.rarity], (int(CARD_WIDTH*0.75), int(CARD_HEIGHT*0.75)))
                            screen.blit(small_border, (x, y))
                            (name, mana, stats, effect_text) = self.read_card(card)
                            name_height = -4
                            for line in name:   #   renders name in individual lines
                                name_render = self.card_name_font_small.render(line, 1, (0, 0, 0))
                                screen.blit(name_render, (x + 15, y + name_height + 15))
                                name_height += self.name_spacing - 4
                            mana_render = self.mana_font_small.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                            screen.blit(mana_render, (x + self.cardwidth*0.75 - 15, y))
                            if card.cardType == TYPE_CREATURE:
                                stats_render = self.stats_font_small.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                                screen.blit(stats_render, (x + 10, y + self.cardheight*0.75 - 25))
                            height = 15
                            for line in effect_text:    #   renders effect text in individual lines
                                effect_render = self.card_text_font_small.render(line, 1, (0, 0, 0))
                                screen.blit(effect_render, (x + 7, y + self.cardheight/3 + height))
                                height += self.effect_spacing
                except ValueError:
                    pass

        for card in card_backlog:
            self.render_card(card_backlog[0][0], card_backlog[0][1], True)

    def card_dash(self, atk_card_cat, def_card_cat):
        #   Give atk_card_cat and def_card_cat as lists, where the first item
        #   is the player and the second is the card index.

        #   Renders animation of card dashing to another card for attack.
        atk_player = atk_card_cat[0]
        def_player = def_card_cat[0]
        atk_index = atk_card_cat[1]
        def_index = def_card_cat[1]
        atk_card = atk_player.cards[atk_index]

        #   Determine position of attacking and defending card
        apos = self.get_card_xy(atk_player, atk_index)
        dpos = self.get_card_xy(def_player, def_index)
        dx = (dpos[0] - apos[0])/1.8
        dy = (dpos[1] - apos[1])/1.8
        frames = int(0.3 * self.anim_speed)
        for i in range(0, frames):  #   On the way there
            prop_there = (i/frames)**3
            self.update_board(self.screen, self.player1, self.player2, None, atk_card)
            pos = (apos[0] + prop_there * dx, apos[1] + prop_there * dy)
            self.render_card(atk_card, pos, False, True)
            self.clock.tick(self.anim_speed)
            pygame.display.flip()
        for i in range(0, frames):
            prop_there = ((frames - i)/frames)**3
            self.update_board(self.screen, self.player1, self.player2, None, atk_card)
            pos = (apos[0] + prop_there * dx, apos[1] + prop_there * dy)
            self.render_card(atk_card, pos, False, True)
            self.clock.tick(self.anim_speed)
            pygame.display.flip()

    def render_damage(self, damage, player, index): #   fancy damage animation
        image = random.choice(self.damage)
        initial_size = 40   #   starting size px
        x = index * (self.cardwidth + 20) + 60
        yhalf = self.screen.get_size()[1]/2
        if player is self.player1:
            y = yhalf + 15
        elif player is self.player2:
            y = yhalf - 15 - self.cardheight
        (x, y) = (x + 50, y + self.cardheight - 40)
        if index == 0 and player is self.player1:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.screen.get_size()[1] - self.cardheight/2 - 30
        elif index == 0 and player is self.player2:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.cardheight/2 + 30
        frames = self.anim_speed
        for i in range(frames):
            self.update_board(self.screen, self.player1, self.player2)
            red_flare = pygame.transform.scale(image, (int(initial_size + i*100/self.anim_speed), int(initial_size + i*100/self.anim_speed)))
            self.change_alpha(red_flare, max(255 - i*400/self.anim_speed, 0))
            flare_rect = red_flare.get_rect()
            flare_rect = flare_rect.move(x - i * 50/self.anim_speed, y - i * 50/self.anim_speed)
            self.screen.blit(red_flare, flare_rect)
            pygame.display.flip()
            self.clock.tick(self.anim_speed)      #   run fade animation at 50 fps
        self.update_board(self.screen, self.player1, self.player2)

    def render_heal(self, amount, player, index):   #   fancy heal animations
        initial_size = 40
        x = index * (self.cardwidth + 20) + 60
        yhalf = self.screen.get_size()[1]/2
        if player is self.player1:
            y = yhalf + 15
        elif player is self.player2:
            y = yhalf - 15 - self.cardheight
        (x, y) = (x + 50, y + self.cardheight - 40)
        if index == 0 and player is self.player1:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.screen.get_size()[1] - self.cardheight/2 - 30
        elif index == 0 and player is self.player2:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.cardheight/2 + 30
        frames = self.anim_speed
        for i in range(frames):
            self.update_board(self.screen, self.player1, self.player2)
            heal_plus = pygame.transform.scale(self.heal, (int(initial_size + i*100/self.anim_speed), int(initial_size + i*100/self.anim_speed)))
            self.change_alpha(heal_plus, max(255 - i*400/self.anim_speed, 0))
            heal_rect = heal_plus.get_rect()
            heal_rect = heal_rect.move(x - i * 50/self.anim_speed, y - i * 50/self.anim_speed)
            self.screen.blit(heal_plus, heal_rect)
            pygame.display.flip()
            self.clock.tick(self.anim_speed)
        self.update_board(self.screen, self.player1, self.player2)

    def render_buff(self, amount, player, index):   #   fancy heal animations
        initial_size = 40
        x = index * (self.cardwidth + 20) + 60
        yhalf = self.screen.get_size()[1]/2
        if player is self.player1:
            y = yhalf + 15
        elif player is self.player2:
            y = yhalf - 15 - self.cardheight
        (x, y) = (x + 50, y + self.cardheight - 40)
        if index == 0 and player is self.player1:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.screen.get_size()[1] - self.cardheight/2 - 30
        elif index == 0 and player is self.player2:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.cardheight/2 + 30
        frames = self.anim_speed
        for i in range(frames):
            self.update_board(self.screen, self.player1, self.player2)
            buff_shield = pygame.transform.scale(self.buff, (int(initial_size + i*100/self.anim_speed), int(initial_size + i*100/self.anim_speed)))
            self.change_alpha(buff_shield, max(255 - i*400/self.anim_speed, 0))
            buff_rect = buff_shield.get_rect()
            buff_rect = buff_rect.move(x - i * 50/self.anim_speed, y - i * 50/self.anim_speed)
            self.screen.blit(buff_shield, buff_rect)
            pygame.display.flip()
            self.clock.tick(self.anim_speed)
        self.update_board(self.screen, self.player1, self.player2)

    def render_shield(self, amount, player, index):
        if 1:
            return True
        initial_size = 70
        x = index * (self.cardwidth + 20) + 60
        yhalf = self.screen.get_size()[1]/2
        if player is self.player1:
            y = yhalf + 15
        elif player is self.player2:
            y = yhalf - 15 - self.cardheight
        (x, y) = (x + 35, y + self.cardheight - 40)
        if index == 0 and player is self.player1:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.screen.get_size()[1] - self.cardheight/2 - 30
        elif index == 0 and player is self.player2:   #   change location of anim if target is player
            initial_size = 80
            x = self.screen.get_size()[0]/2 - initial_size/2
            y = self.cardheight/2 + 30
        frames = self.anim_speed
        for i in range(frames):
            self.update_board(self.screen, self.player1, self.player2)
            div_shield = pygame.transform.scale(self.shield, (int(initial_size + i*100/self.anim_speed), int(initial_size + i*100/self.anim_speed)))
            #div_shield = pygame.transform.rotate(div_shield, -2*i)
            self.change_alpha(div_shield, max(255 - i*400/self.anim_speed, 0))
            div_rect = div_shield.get_rect()
            div_rect = div_rect.move(x - i * 50/self.anim_speed, y - i * 50/self.anim_speed)
            self.screen.blit(div_shield, div_rect)
            pygame.display.flip()
            self.clock.tick(self.anim_speed)
        self.update_board(self.screen, self.player1, self.player2)

    def change_alpha(self, img, alpha=255): #   change opacity of img to alpha
        width,height=img.get_size()
        for x in range(0,width):
            for y in range(0,height):
                r,g,b,old_alpha=img.get_at((x,y))
                if old_alpha>0:
                    img.set_at((x,y),(r,g,b,alpha))

    def change_brightness(self, img, f = 0.75):
        #   Change brightness of an image. f is a ratio to original brightness.
        width, height = img.get_size()
        for x in range(0, width):
            for y in range(0, height):
                r, g, b, alpha = img.get_at((x, y))
                img.set_at((x, y), (r*f, g*f, b*f, alpha))

    def get_card_xy(self, player, index):
        #   Find the xy coordinates of a card on the field based on its
        #   list index and player
        x = index * (self.cardwidth + 20) + 80
        yhalf = self.screen.get_size()[1]/2
        if player is self.player2:
            y = yhalf - 15 - self.cardheight
        elif player is self.player1:
            y = yhalf + 15
        if index == 0 and player is self.player1:
            x = self.screen.get_size()[0]/2
            y = self.screen.get_size()[1] - self.cardheight/2
        elif index == 0 and player is self.player2:
            x = self.screen.get_size()[0]/2
            y = self.cardheight/2
        return (x, y)

    def render_mana(self, num, pos):
        if num > 0:
            self.screen.blit(self.mana_crystal, pos)
            self.render_mana(num - 1, (pos[0] + 70, pos[1]))
