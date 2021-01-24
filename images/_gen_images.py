import pygame
import time

pygame.init()

screen = pygame.display.set_mode()

spacecraft = pygame.Surface((50, 50))

pygame.draw.rect(spacecraft, (255, 255, 255), [20, 10, 11, 30])
pygame.draw.polygon(spacecraft, (255, 255, 255), [(25, 0), (20, 10), (30, 10)])

screen.blit(spacecraft, (0, 0))

pygame.display.flip()

pygame.image.save(spacecraft, pygame.image.load(os.path.join(os.path.dirname(__file__), 'player.png')

time.sleep(100)
