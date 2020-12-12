import pygame
from base import request

class screen_data:
    def __init__(self):
        self.text = pygame.font.Font(pygame.font.match_font('menlo'), 15)
        self.default_color = (109, 189, 255)

    def enabled(self):
        return True

    def run(self, screen, events):
        words = self.get_words()
        for messege, color in words:

            self.color = color if color else self.default_color
            self.print_words(screen, messege)

    def print_words(self, screen, words):
        list_of_words = words.splitlines()
        for line, word in enumerate(list_of_words):
            self.print_line(screen, word, line)

    def print_line(self, screen, word, lines_down):
        screen.blit(self.text.render(word, (0, 0, 0), self.color), (0, lines_down*15))

    def get_words(self):
        return (self.get_target_words(),)

    def get_target_words(self):
        target = request().extentions['target'].get_target(True)
        return ('TARGET: ' + (target.data % target.respond_data)), (255, 0, 0)
