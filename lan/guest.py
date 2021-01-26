import framework
import norm_keys_wrapper
import sys
import time
import pygame
from threading import Thread

class guest:
    def __init__(self, double_socket, screen):
        self.double_socket = double_socket
        self.screen = screen

    def draw(self):
        while True:

    def run(self):
        send_events = Thread(target=self.send_events)
        send_events.start()
        while True:
            self.screen.blit(pygame.image.fromstring(self.double_socket.recive(), (800, 800), 'RGB'), (0, 0))
            pygame.display.flip()


    def send_events(self):
        while True:
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
