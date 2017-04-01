from Constants import *
import pygame
import os

class Board():
    def __init__(self, screen, players):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.card_name_font = pygame.font.SysFont("arial narrow", 25)   #   sets card fonts
        self.hero_name_font = pygame.font.SysFont("arial narrow", PLAYER_CARD_FONT_SIZE)
        self.card_text_font = pygame.font.SysFont("arial narrow", CREATURE_CARD_FONT_SIZE)
        self.mana_font = pygame.font.SysFont("arial narrow", MANA_COST_FONT_SIZE)
        self.stats_font = pygame.font.SysFont("arial narrow", CREATURE_STATS_FONT_SIZE)
        self.health_font = pygame.font.SysFont("arial narrow", PLAYER_HEALTH_FONT_SIZE)
        self.cardwidth = CARD_WIDTH         #  width in pixels of a card. Other scaling changes because of this
        self.cardheight = CARD_HEIGHT
        self.player1 = players[0]
        self.player2 = players[1]
        self.boom = pygame.image.load(os.path.join('redglow.png')).convert_alpha()

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

    def render_card(self, card_obj, position, is_animated = False):  #   display card on screen
        card = pygame.Surface((self.cardwidth, self.cardheight))
        if is_animated:
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
                    name_height += 20
                mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                card.blit(mana_render, (x + self.cardwidth - 20, y))
                stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                card.blit(stats_render, (x + 10, y + self.cardheight - 25))
                effect_height = 0
                for line in effect_text:    #   renders effect text in individual lines
                    effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                    card.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                    effect_height += 15
                #card.set_alpha(50)
                card.set_alpha(10 * alpha)
                self.screen.blit(card, (position[0], position[1]))
                pygame.display.flip()
                self.clock.tick(20)
        else:
            card.fill((255, 255, 255))
        self.screen.blit(card, (position[0], position[1]))

    def read_card(self, card):  #   turns card object into easily read tuple
        name = card.name
        name_length = 12
        while len(name) - name.rfind("\n") > name_length: # arranges name into lines of length <= name_length
            index = name.rfind("\n") + name_length
            while name[index] != " " and index > 0:
                index -= 1
            name = name[0:index + 1] + "\n" + name[index + 1:]
        name = name.split("\n")
        stats = card.stats
        mana = card.manacost
        effect = card.effect
        effect_text = ""
        if not effect:
            effect_text = ""
        else:                                       # generates card text
            if card.cardType == TYPE_CREATURE:
                effect_text = "%s," % (TRIGGER_TEXT_DICT[effect.trigger])
            if effect.effect == DEAL_EFFECT:
                effect_text += "deal %s damage to %s." % (effect.numeric, TARGET_TEXT_DICT[effect.target])
            elif effect.effect == DRAW_EFFECT:
                effect_text += "%s draws %s cards." % (TARGET_TEXT_DICT[effect.target], effect.numeric)
            elif effect.effect == HEAL_EFFECT:
                effect_text += "heal %s for %s damage." % (TARGET_TEXT_DICT[effect.target], effect.numeric)
            elif effect.effect == SUMMON_EFFECT:
                effect_text += "%s summons a random %s-mana creature." % (TARGET_TEXT_DICT[effect.target], effect.numeric)
            elif effect.effect == BUFF_EFFECT:
                effect_text += "%s gets +%s/+%s." % (TARGET_TEXT_DICT[effect.target], effect.numeric[0], effect.numeric[1])
            elif effect.effect == SPLIT_DEAL_EFFECT:
                effect_text += "deal %s damage split randomly between %s." % (effect.numeric, TARGET_TEXT_DICT[effect.target])
            elif effect.effect == SPLIT_HEAL_EFFECT:
                effect_text += "heal %s damage split randomly between %s." % (effect.numeric, TARGET_TEXT_DICT[effect.target])
            effect_text = effect_text.lower().capitalize()
            char_length = 20         # maximum characters on each line of text
            while len(effect_text) - effect_text.rfind("\n") > char_length: # arranges effect text into lines
                index = effect_text.rfind("\n") + char_length
                while effect_text[index] != " " and index > 0:
                    index -= 1
                effect_text = effect_text[0:index + 1] + "\n" + effect_text[index + 1:]
        effect_text = effect_text.split("\n")
        return (name, mana, stats, effect_text)

    def update_board(self, screen, player1, player2, card_to_animate = None, all_players = None):   #   updates board with current cards in play
        """
        Displaying an unknown number of players isn't my problem but I left an 'all' here anyway.
        """
        screen.fill((0, 0, 255))
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

        card_backlog = []

        for card in player2.cards[1:] + player1.cards[1:]:
            try:
                x = player2.cards.index(card)*(self.cardwidth + 20) + 80
                y = yhalf - 15 - self.cardheight
                if card is card_to_animate:
                    card_backlog.append([card, (x, y)])
                    #self.render_card(card, (x, y), True)
                else:
                    self.render_card(card, (x, y))
                if self.read_card(card) != None and card is not card_to_animate:
                    (name, mana, stats, effect_text) = self.read_card(card)
                    name_height = 0
                    for line in name:   #   renders name in individual lines
                        name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                        screen.blit(name_render, (x + 15, y + name_height + 15))
                        name_height += 20
                    mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                    screen.blit(mana_render, (x + self.cardwidth - 20, y))
                    stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                    screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                    effect_height = 0
                    for line in effect_text:    #   renders effect text in individual lines
                        effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                        screen.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                        effect_height += 15

            except ValueError:
                try:
                    x = player1.cards.index(card)*(self.cardwidth + 20) + 80
                    y = yhalf + 15
                    if card is card_to_animate:
                        self.render_card(card, (x, y), True)
                    else:
                        self.render_card(card, (x, y))
                    if self.read_card(card) != None:
                        (name, mana, stats, effect_text) = self.read_card(card)
                        name_height = 0
                        for line in name:   #   renders name in individual lines
                            name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                            screen.blit(name_render, (x + 15, y + name_height + 15))
                            name_height += 20
                        mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))    #   renders mana cost
                        screen.blit(mana_render, (x + self.cardwidth - 20, y))
                        stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0)) #   renders stats
                        screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                        height = 0
                        for line in effect_text:    #   renders effect text in individual lines
                            effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                            screen.blit(effect_render, (x + 15, y + self.cardheight/2 + height))
                            height += 15
                except ValueError:
                    pass
        for card in card_backlog:
            self.render_card(card_backlog[0][0], card_backlog[0][1], True)

    def render_damage(self, damage, player, index):
        x = index * (self.cardwidth + 20) + 60
        yhalf = self.screen.get_size()[1]/2
        if player is self.player1:
            y = yhalf + 15
        elif player is self.player2:
            y = yhalf - 15 - self.cardheight
        (x, y) = (x + 50, y + self.cardheight - 40)
        for i in range(50):
            self.update_board(self.screen, self.player1, self.player2)
            red_flare = pygame.transform.scale(self.boom, (50 + 2*i, 50 + 2*i))
            self.change_alpha(red_flare, max(255 - 8 * i, 0))
            flare_rect = red_flare.get_rect()
            flare_rect = flare_rect.move(x - i, y - i)
            self.screen.blit(red_flare, flare_rect)

            pygame.display.flip()
            self.clock.tick(50)


    def change_alpha(self, img, alpha=255):
        width,height=img.get_size()
        for x in range(0,width):
            for y in range(0,height):
                r,g,b,old_alpha=img.get_at((x,y))
                if old_alpha>0:
                    img.set_at((x,y),(r,g,b,alpha))
