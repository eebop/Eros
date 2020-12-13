import pygame
from base import request
import numpy as np

class screen_data:
    def __init__(self, size=15):
        self.text = pygame.font.Font(pygame.font.match_font('menlo'), size)
        self.default_color = (109, 189, 255)
        self.size = size

    def enabled(self):
        return True

    def run(self, screen, events):
        words = self.get_words()
        for messege, color in words:

            self.print_words(screen, color, messege, (0, 0))

    def print_words(self, screen, color, words, location):
        if color:
            self.color = color
        else:
            self.color = self.default_color
        location = np.array(location, dtype=float)
        list_of_words = words.splitlines()
        for line, word in enumerate(list_of_words):
            self.print_line(screen, word, line, location)

    def print_line(self, screen, word, lines_down, location):
        screen.blit(self.text.render(word, 0, self.color), (location + (0, lines_down*self.size)))

    def get_words(self):
        return (self.get_target_words(),)

    def get_target_words(self):
        target = request().extentions['target'].get_target(True)
        return ('TARGET: ' + (target.data % target.respond_data)), (255, 0, 0)
