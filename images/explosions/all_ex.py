import pygame
import time
import sys
import os

class all_im:
    def __init__(self, loc, rot):
        self.images = [pygame.image.load(os.path.join(os.path.dirname(__file__), 'poco%s.png')%x) for x in range(0, 24)]
        self.number = 9
        self.loc = loc
        self.rot = rot



    def update(self, t, d):
        self.number += 1
        if self.number == 239:
            self.kill()
        return pygame.transform.rotate(self.images[int(self.number/10)], self.rot), self.loc






def _test():
    pygame.init()
    screen = pygame.display.set_mode()
    a = all_im()
    while True:
        pygame.event.get()
        screen.blit(*a.update(None, None))
        pygame.display.flip()
        time.sleep(.1)
        screen.fill((0, 0, 0))

if __name__ == '__main__':
    _test()
