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
            self.double_socket.send(self._process_events(pygame.event.get()))

    def _process_events(self, events):
        events = [self.eventtoeventwrapper(e) for e in events if e.type in (pygame.KEYDOWN, pygame.KEYUP)]
        return events

    def eventtoeventwrapper(self, event):
        return EventWrapper(event.type, event.key)


class EventWrapper:
    def __init__(self, type, key):
        self.type = type
        self.key = key
