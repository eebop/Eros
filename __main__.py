import sys

try:
    import pygame
except ModuleNotFoundError:
    sys.exit('Needs module pygame to work properly. To install, run `pip install pygame`')
try:
    import numpy
except ModuleNotFoundError:
    sys.exit('Needs module numpy to work properly. To install, run `pip install pygame`')

print('here')

pygame.init()

print('here')

import framework

print('here')

import lan # must come after pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

if lan.run(screen):

    handler = framework.Framework()

    handler.run(screen)

else:
    lan.run_as_guest(screen)
