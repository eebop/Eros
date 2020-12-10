import framework
import sys
try:
    import pygame
except ModuleNotFoundError:
    sys.exit('Needs module pygame to work properly. To install, run `pip install pygame`')
try:
    import numpy
except ModuleNotFoundError:
    sys.exit('Needs module numpy to work properly. To install, run `pip install pygame`')

pygame.init()

SCARRYMODE = False
if SCARRYMODE:
    import scarrycode
    screen = scarrycode.run()
else:
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

handler = framework.Framework()

handler.run(screen)
