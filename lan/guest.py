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
            self.screen.blit(self.double_socket.recive(), (0, 0))

    def run(self):
        draw = Thread(target=self.draw)
        send_events = Thread(target=self.send_events)
        draw.start()
        send_events.start()
        while True:
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
