import sys
import pygame
from select import select
from norm_keys_wrapper import norm_keys_wrapper

class guest:
    def __init__(self, double_socket, screen):
        self.double_socket = double_socket
        self.screen = screen
        self.location = [0, 0]
        norm_keys_wrapper.__init__(self)

    def loop(self):
        while True:
            events = pygame.event.get()
            e = self._process_events(events)
            if e:
                self.double_socket.send(self.screen.get_size())
                self.double_socket.send(e)
            if select([self.double_socket.reciver], [], [], 0)[0]:
                self.screen.blit(self.double_socket.recive(), (0, 0))
            pygame.display.flip()


    def _process_events(self, events):
        sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in events]) else None
        return self.get_formatted(events)

    def get_formatted(self, events):
        events = [{'type': e.type, 'key': e.key} for e in events if e.type in (pygame.KEYDOWN, pygame.KEYUP)]
        return events
