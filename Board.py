from Constants import *
from randGen import *
import pygame
import os

class Board():
    def __init__(self, screen, players):
        self.clock = pygame.time.Clock()
        self.screen = screen
        typeface = "myriad pro cond"
        self.card_name_font = pygame.font.SysFont(typeface, 17)   #   sets card fonts
        self.hero_name_font = pygame.font.SysFont(typeface, PLAYER_CARD_FONT_SIZE)
        self.card_text_font = pygame.font.SysFont(typeface, CREATURE_CARD_FONT_SIZE)
        self.mana_font = pygame.font.SysFont(typeface, MANA_COST_FONT_SIZE)
        self.stats_font = pygame.font.SysFont(typeface, CREATURE_STATS_FONT_SIZE)
        self.health_font = pygame.font.SysFont(typeface, PLAYER_HEALTH_FONT_SIZE)
        self.cardwidth = CARD_WIDTH         #  width in pixels of a card. Other scaling changes because of this
        self.cardheight = CARD_HEIGHT
        self.player1 = players[0]
        self.player2 = players[1]
        backgrounds = ['BackgroundImage.jpg', 'bk2.jpg', 'bk3.jpg', 'bk4.jpg', 'bk5.jpg', 'bk6.jpg', 'bk7.jpg']
        self.backdrop = pygame.image.load(os.path.join(random.choice(backgrounds))).convert_alpha()
        self.backdrop = pygame.transform.scale(self.backdrop, (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2)))
        self.change_brightness(self.backdrop, 0.75)
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
        self.effect_spacing = 10
        self.name_spacing = 15
        self.char_length = 24
        self.effnames = {WINDFURY_EFFECT: generate_effect_name(WINDFURY_EFFECT),
        CHARGE_EFFECT: generate_effect_name(CHARGE_EFFECT),
        DIVINE_SHIELD_EFFECT: generate_effect_name(DIVINE_SHIELD_EFFECT),
        TAUNT_EFFECT: generate_effect_name(TAUNT_EFFECT)}
        self.anim_speed = 30

    # def render_text(self, card_obj, pos):
    #     surface = pygame.Surface((self.cardwidth, self.cardheight))
    #     surface.fill(255, 255, 255)
    #     x = 0
    #     y = 0
    #     (name, mana, stats, effect_text) = self.read_card(card_obj)
    #     name_height = 0
    #     for line in name:   #   renders name in individual lines
    #         name_render = self.card_name_font.render(line, 1, (0, 0, 0))
    #         surface.blit(name_render, (x + 15, y + name_height + 15))
    #         name_height += 20
    #     mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
    #     surface.blit(mana_render, (x + self.cardwidth - 20, y))
    #     stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
    #     surface.blit(stats_render, (x + 10, y + self.cardheight - 25))
    #     effect_height = 0
    #     for line in effect_text:    #   renders effect text in individual lines
    #         effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
    #         surface.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
    #         effect_height += 15
    #     return surface

    def render_card(self, card_obj, position, is_animated = False, is_dash = False):  #   display card on screen
        card = pygame.Surface((self.cardwidth, self.cardheight))
        try:
            art = pygame.image.load(card_obj.art_path).convert_alpha()

        except:
            art = self.bear
        art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))

        if is_animated or is_dash:
            for alpha in range(30):
                card.fill((255, 255, 255))
                # text_surface = self.render_text(card_obj, position)
                x = 0
                y = 0
                (name, mana, stats, effect_text) = self.read_card(card_obj)
                name_height = 0
                for line in name:   #   renders name in individual lines
                    name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                    card.blit(name_render, (x + 15, y + name_height + 15))
                    name_height += self.name_spacing
                card.blit(art, (x + int(CARD_WIDTH*0.045), y + 30))
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
                if card_obj.active_effects[WINDFURY_INDEX] == 1:
                    swords = pygame.transform.scale(self.double_sword, (int(self.cardwidth/6), int(self.cardwidth/6)))
                    swords_rect = swords.get_rect()
                    self.change_alpha(swords, 180)
                    swords_rect = swords_rect.move(x + self.cardwidth - int(self.cardwidth/6) - 12, y + self.cardheight - int(self.cardwidth/6) - 12)
                    card.blit(swords, swords_rect)
                card.set_alpha(10 * alpha)
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

    def update_board(self, screen, player1, player2, card_to_animate = None, card_not_to_render = None, all_players = None):   #   updates board with current cards in play
        """
        Displaying an unknown number of players isn't my problem but I left an 'all' here anyway.
        """
        screen.fill((200, 100, 200))
        bkgd = pygame.transform.scale(self.backdrop, (WINDOW_WIDTH, WINDOW_HEIGHT))
        bkgd_rect = bkgd.get_rect()
        self.screen.blit(bkgd, bkgd_rect)
        xhalf = screen.get_size()[0]/2
        yhalf = screen.get_size()[1]/2
        card_y_offset = 30
        name_y_offset = 15
        name_x_offset = 15
        health_x_offset = 35
        health_y_offset = 45

        self.render_card(player2.cards[0], (xhalf - self.cardwidth/2, card_y_offset))
        player2_name_render = self.hero_name_font.render(player2.player.name, 1, (0, 0, 0))          #   define name font object
        player2_health_render = self.health_font.render(str(player2.player.stats[2]), 1, (0, 0, 0))     #   define health font object
        screen.blit(player2_name_render, (xhalf - self.cardwidth/2 + name_x_offset, 30 + name_y_offset))                  #   blit player 2 name
        screen.blit(player2_health_render, (xhalf - self.cardwidth/2 + health_x_offset, card_y_offset + health_y_offset))

        self.render_card(player1.cards[0], (xhalf - self.cardwidth/2, screen.get_size()[1] - card_y_offset - self.cardheight))
        player1_name_render = self.hero_name_font.render(player1.player.name, 1, (0, 0, 0))
        player1_health_render = self.health_font.render(str(player1.player.stats[2]), 1, (0, 0, 0))     #   define health font object
        screen.blit(player1_name_render, (xhalf - self.cardwidth/2 + name_x_offset, screen.get_size()[1] - card_y_offset - self.cardheight + name_y_offset))
        screen.blit(player1_health_render, (xhalf - self.cardwidth/2 + health_x_offset, -card_y_offset + health_y_offset + 2*yhalf - self.cardheight))

        for cardindex in range(len(player1.hand.cards)):
            cardsurface = pygame.Surface((50, 50))
            cardsurface.fill((255, 255, 255))
            screen.blit(cardsurface, (100 * cardindex, 600))

        for cardindex in range(len(player2.hand.cards)):
            cardsurface = pygame.Surface((50, 50))
            cardsurface.fill((255, 255, 255))
            screen.blit(cardsurface, (100 * cardindex, 100))

        card_backlog = []   #   List of cards to render after all other cards are rendered

        for card in player2.cards[1:] + player1.cards[1:]:
            try:
                art = pygame.image.load(card.art_path).convert_alpha()

            except:
                art = self.bear
            art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
            try:
                x = player2.cards.index(card)*(self.cardwidth + 20) + 80
                y = yhalf - 15 - self.cardheight
                if card is card_not_to_render:
                    continue
                elif card is card_to_animate:
                    card_backlog.append([card, (x, y)])
                    #self.render_card(card, (x, y), True)
                else:
                    self.render_card(card, (x, y))
                if card is not card_to_animate and card is not card_not_to_render:
                    screen.blit(art, (x + int(CARD_WIDTH*0.045), y + 30))
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
                    effect_height = 0
                    for line in effect_text:    #   renders effect text in individual lines
                        effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                        screen.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                        effect_height += self.effect_spacing
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
                try:
                    art = pygame.image.load(card.art_path).convert_alpha()

                except:
                    art = self.bear
                art = pygame.transform.scale(art, (int(CARD_WIDTH*0.86), int(CARD_WIDTH*0.495)))
                try:
                    x = player1.cards.index(card)*(self.cardwidth + 20) + 80
                    y = yhalf + 15
                    if card is card_not_to_render:
                        continue
                    elif card is card_to_animate:
                        self.render_card(card, (x, y), True)
                    else:
                        self.render_card(card, (x, y))
                    if card is not card_to_animate and card is not card_not_to_render:
                        screen.blit(art, (x + int(CARD_WIDTH*0.045), y + 30))
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
        for card in card_backlog:
            self.render_card(card_backlog[0][0], card_backlog[0][1], True)

    def card_dash(self, atk_card_cat, def_card_cat):
        #   Give atk_card_cat and def_card_cat as lists, where the first item
        #   is the player and the second is the card index.
        atk_player = atk_card_cat[0]
        def_player = def_card_cat[0]
        atk_index = atk_card_cat[1]
        def_index = def_card_cat[1]
        atk_card = atk_player.cards[atk_index]
        apos = self.get_card_xy(atk_player, atk_index)
        dpos = self.get_card_xy(def_player, def_index)
        dx = (dpos[0] - apos[0])/1.8
        dy = (dpos[1] - apos[1])/1.8
        frames = int(0.3 * self.anim_speed)
        for i in range(0, frames):
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
        width, height = img.get_size()
        for x in range(0, width):
            for y in range(0, height):
                r, g, b, alpha = img.get_at((x, y))
                img.set_at((x, y), (r*f, g*f, b*f, alpha))

    def get_card_xy(self, player, index):
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
