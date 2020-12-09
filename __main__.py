import framework
import pygame
pygame.init()

SCARRYMODE = False
if SCARRYMODE:
    import scarrycode
    screen = scarrycode.run()
else:
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

handler = framework.Framework()

handler.run(screen)
