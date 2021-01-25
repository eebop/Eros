import framework
import norm_keys_wrapper
import sys
import time
import pygame

class guest:
    def __init__(self, double_socket, screen):
        self.double_socket = double_socket
        self.screen = screen

    def run(self):
        while True:
            self.screen.blit(self.double_socket.recive(), (0, 0))
            pygame.display.flip()
            self.double_socket.send(pygame.events.get())
