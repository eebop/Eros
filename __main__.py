import sys
import os
import socket
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
try:
    import pygame
except ModuleNotFoundError:
    sys.exit('Needs module pygame to work properly. To install, run `python3 -m pip install pygame`')
try:
    import numpy
except ModuleNotFoundError:
    sys.exit('Needs module numpy to work properly. To install, run `python3 -m pip install numpy`')

socket.setdefaulttimeout(2)

pygame.init()

import framework


import lan # must come after pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

double_socket = lan.run(screen)

try:

        handler = framework.Framework()

        handler.run(screen, double_socket)

except (TypeError, BrokenPipeError, ConnectionResetError, KeyboardInterrupt):
    pass
