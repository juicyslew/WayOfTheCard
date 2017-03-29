from Constants import *
import pygame

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.card_name_font = pygame.font.SysFont("arial narrow", 25)   #   sets card fonts
        self.card_text_font = pygame.font.SysFont("arial narrow", 20)
        self.mana_font = pygame.font.SysFont("arial narrow", 40)
        self.stats_font = pygame.font.SysFont("arial narrow", 30)
        self.cardwidth = 150         #  width in pixels of a card. Other scaling changes because of this
        self.cardheight = 210

    def render_card(self, card_obj, position):  #   display card on screen
        pygame.draw.rect(self.screen, [255, 255, 255], pygame.Rect(position[0], position[1], self.cardwidth, self.cardheight))

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
                effect_text = "%s," % (EFFECT_TRIGGER_DICT[effect.trigger])
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

    def update_board(self, screen, player1, player2, all = None):   #   updates board with current cards in play
        """
        Displaying an unknown number of players isn't my problem but I left an 'all' here anyway.
        """
        screen.fill((0, 0, 255))
        pygame.draw.rect(screen, [255, 255, 255], (64, 100, 32, 32))
        xhalf = screen.get_size()[0]/2
        yhalf = screen.get_size()[1]/2

        self.render_card(player1.cards[0], (xhalf - self.cardwidth/2, 30))
        self.render_card(player2.cards[0], (xhalf - self.cardwidth/2, screen.get_size()[1] - 30 - self.cardheight))

        for card in player2.cards[1:] + player1.cards[1:]:
            try:
                x = player2.cards.index(card)*(self.cardwidth + 20) + 80
                y = yhalf - 50 - self.cardheight
                self.render_card(screen, (x, y))
                if self.read_card(card) != None:
                    (name, mana, stats, effect_text) = self.read_card(card)
                    name_height = 0
                    for line in name:
                        name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                        screen.blit(name_render, (x + 15, y + name_height + 15))
                        name_height += 20
                    mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))
                    screen.blit(mana_render, (x + self.cardwidth - 20, y))
                    stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0))
                    screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                    effect_height = 0
                    for line in effect_text:
                        effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                        screen.blit(effect_render, (x + 15, y + self.cardheight/2 + effect_height))
                        effect_height += 15

            except ValueError:
                try:
                    x = player1.cards.index(card)*(self.cardwidth + 20) + 80
                    y = yhalf + 50
                    self.render_card(screen, (x, y))
                    if self.read_card(card) != None:
                        (name, mana, stats, effect_text) = self.read_card(card)
                        name_height = 0
                        for line in name:
                            name_render = self.card_name_font.render(line, 1, (0, 0, 0))
                            screen.blit(name_render, (x + 15, y + name_height + 15))
                            name_height += 20
                        mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))
                        screen.blit(mana_render, (x + self.cardwidth - 20, y))
                        stats_render = self.stats_font.render(str(stats[1:]), 1, (0, 0, 0))
                        screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                        height = 0
                        for line in effect_text:
                            effect_render = self.card_text_font.render(line, 1, (0, 0, 0))
                            screen.blit(effect_render, (x + 15, y + self.cardheight/2 + height))
                            height += 15
                except ValueError:
                    pass
