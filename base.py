import pygame
class base:
    '''all items should have inhertied from base'''
    def __init__(self, loc):
        pass
    def update(self, time, data):
        # must return an image to draw and a location to draw at
        s = pygame.Surface((10, 10))
        s.fill((10, 100, 37))
        return s, [100, 100]

def request():
    import sys
    return getattr(sys.modules['__main__'], 'handler')

class Wrapper:
    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return [x for x in self.__dict__ if not x in object().__dict__]
