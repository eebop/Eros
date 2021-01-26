import sys
import pygame
from select import select

class guest:
    def __init__(self, double_socket, screen):
        self.double_socket = double_socket
        self.screen = screen

    def run(self):
        while True:
            e = self._process_events()
            if e:
                print(e)
                self.double_socket.send(e)
            if select([self.double_socket.reciver], [], [], 0)[0]:
                self.screen.blit(self.double_socket.recive(), (0, 0))
            pygame.display.flip()
            self.events = pygame.event.get()


    def _process_events(self):
        print('in _process_events')
        events = pygame.event.get()
        print(events)
        sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in events]) else None
        events = [self.eventtoeventwrapper(e) for e in events if e.type in (pygame.KEYDOWN, pygame.KEYUP)]
        return events

    def eventtoeventwrapper(self, event):
        return EventWrapper(event.type, event.key)


class EventWrapper:
    def __init__(self, type, key):
        self.type = type
        self.key = key
