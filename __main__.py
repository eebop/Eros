import sys
import os
import socket
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
try:
    import pygame
except:
    sys.exit('Needs module pygame to work properly. To install, run `python%s -m pip install pygame`' % sys.version.split(' ')[0])
try:
    import numpy
except:
    sys.exit('Needs module numpy to work properly. To install, run `python%s -m pip install numpy`' % sys.version.split(' ')[0])


pygame.init()

import framework


import lan # must come after pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

double_socket = lan.run(screen)

handler = framework.Framework()

handler.run(screen, double_socket)
