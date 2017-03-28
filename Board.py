from Constants import *
import pygame

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.card_name_font = pygame.font.SysFont("arial narrow", 15)
        self.card_text_font = pygame.font.SysFont("arial narrow", 12)
        self.mana_font = pygame.font.SysFont("arial narrow", 15)
        self.stats_font = pygame.font.SysFont("arial narrow", 15)
        self.cardwidth = 100
        self.cardheight = 140

    def render_card(self, card_obj, position):
        pygame.draw.rect(self.screen, [255, 255, 255], pygame.Rect(position[0], position[1], self.cardwidth, self.cardheight))

    def read_card(self, card):
        name = card.name
        stats = card.stats
        mana = card.manacost
        effect = card.effect
        effect_text = ""
        if not effect:
            effect_text = ""
        else:
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
        return (name, mana, stats, effect_text)

    def update_board(self, screen, player1, player2):
        screen.fill((0, 0, 255))
        pygame.draw.rect(screen, [255, 255, 255], (64, 100, 32, 32))
        xhalf = screen.get_size()[0]/2
        yhalf = screen.get_size()[1]/2

        self.render_card(player1.cards[0], (xhalf - 25, 50))
        self.render_card(player2.cards[0], (xhalf - 25, screen.get_size()[1] - 50 - self.cardheight))

        for card in player2.cards[1:] + player1.cards[1:]:
            try:
                x = player2.cards.index(card)*120 + 100
                y = yhalf - 50 - self.cardheight
                self.render_card(screen, (x, y))
                if self.read_card(card) != None:
                    (name, mana, stats, effect_text) = self.read_card(card)
                    name_render = self.card_name_font.render(name, 1, (0, 0, 0))
                    screen.blit(name_render, (x, y))
                    mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))
                    screen.blit(mana_render, (x + self.cardwidth - 20, y))
                    stats_render = self.stats_font.render(str(stats), 1, (0, 0, 0))
                    screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                    effect_render = self.card_text_font.render(effect_text, 1, (0, 0, 0))
                    screen.blit(effect_render, (x, y + 50))
            except ValueError:
                try:
                    x = player1.cards.index(card)*120 + 100
                    y = yhalf + 50
                    self.render_card(screen, (x, y))
                    if self.read_card(card) != None:
                        (name, mana, stats, effect_text) = self.read_card(card)
                        name_render = self.card_name_font.render(name, 1, (0, 0, 0))
                        screen.blit(name_render, (x, y))
                        mana_render = self.mana_font.render(str(mana), 1, (0, 0, 0))
                        screen.blit(mana_render, (x + self.cardwidth - 20, y))
                        stats_render = self.stats_font.render(str(stats), 1, (0, 0, 0))
                        screen.blit(stats_render, (x + 10, y + self.cardheight - 25))
                        effect_render = self.card_text_font.render(effect_text, 1, (0, 0, 0))
                        screen.blit(effect_render, (x, y + 50))
                except ValueError:
                    pass
