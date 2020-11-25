import pygame

class screen_data:
    def __init__(self):
        self.text = pygame.font.Font(pygame.font.match_font('menlo'), 15)

    def enabled(self):
        return True

    def run(self, screen, events):
        words = self.get_words()
        self.print_words(screen, words)

    def print_words(self, screen, words):
        list_of_words = words.splitlines()
        for line, word in enumerate(list_of_words):
            self.print_line(screen, word, line)

    def print_line(self, screen, word, lines_down):
        screen.blit(self.text.render(word, (0, 0, 0), (109, 189, 255)), (0, lines_down*15))

    def get_words(self):
        return ''
