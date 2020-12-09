import numpy as np
import pygame

class move:
    def __init__(self):
        self.location = np.array([0, 0])
        self.running_events = [False, False, False, False]
        self.events = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        self.movements = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    def run(self, screen, events):
        if events:
            options = [x for x in events if x.type in [pygame.KEYDOWN, pygame.KEYUP] and x.key in self.events]
            self.add_options(options)
        self._update()
        #print('here, location is', self.location, 'events are', events)
        return self.location

    def add_options(self, options):
        for option in options:
            print(option, pygame.KEYDOWN)
            self.running_events[self.events.index(option.key)] = option.type==pygame.KEYDOWN
            print(self.running_events)

    def _update(self):
        for IsTrue, move in zip(self.running_events, self.movements):
            if IsTrue:
                self.location += move
