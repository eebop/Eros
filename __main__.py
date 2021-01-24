import sys

try:
    import pygame
except ModuleNotFoundError:
    sys.exit('Needs module pygame to work properly. To install, run `pip install pygame`')
try:
    import numpy
except ModuleNotFoundError:
    sys.exit('Needs module numpy to work properly. To install, run `pip install numpy`')


pygame.init()

import framework


import lan # must come after pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

double_socket = lan.run(screen)

if double_socket:

    handler = framework.Framework()

    handler.run(screen, double_socket)

else:
    lan.run_as_guest(screen)
