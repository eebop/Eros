from move import move
import pygame

class norm_keys_wrapper(move):
    def __init__(self):
        self.running_events = [False, False, False, False]
        self.events = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
        self.movements = [[0, -1], [0, 1], [-1, 0], [1, 0]]
