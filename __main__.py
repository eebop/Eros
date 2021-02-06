import sys
import os
import socket
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
try:
    import pygame
except ModuleNotFoundError:
    sys.exit('Needs module pygame to work properly. To install, run `python%s -m pip install pygame`', '.'.join(map(str, python.vernum[:3])))
try:
    import numpy
except ModuleNotFoundError:
    sys.exit('Needs module numpy to work properly. To install, run `python%s -m pip install numpy`', '.'.join(map(str, python.vernum[:3])))


pygame.init()

import framework


import lan # must come after pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

pygame.display.set_caption('Eros')

try:

    double_socket = lan.run(screen)

    handler = framework.Framework()

    handler.run(screen, double_socket)

except (TypeError, BrokenPipeError, ConnectionResetError, KeyboardInterrupt):
    raise
except OSError:
    sys.exit("Sorry, you don't have internet right now.")
