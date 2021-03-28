import pygame
import math
import sys
import os
import numpy as np
from base import base, request
import time

class missile:
    def __init__(self, loc, islaunchedbyplayer):
        self._loc = loc
        #self.s = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'missile.png'))
        s = pygame.Surface((10, 10))
        s.set_colorkey((0, 0, 0))
        color = request().extentions['color'][islaunchedbyplayer]
        pygame.draw.circle(s, color, (5, 5), 5)
        self.s = s
        self.goal = np.array([500, 500], dtype=float)
        self.frozen = False
        self.IsLaunchedByPlayer = islaunchedbyplayer
        self.time = time.time()

    def update(self, time, data):
        self.get_goal()
        # must return an image to draw and a location to draw at
        if (self._loc != self.goal).any():
            slope = np.array(self.goal - self._loc, dtype=int)

            if not slope[0] == 0:
                radians = math.atan2(*(slope[::-1]))
            else:
                radians = math.pi/2 if slope[1] > 0 else -math.pi/2
            print(radians)
            self._loc += np.array([math.cos(radians), math.sin(radians)])


            if ([-10, -10] < self.goal-self._loc).all() and (self.goal-self._loc < [10, 10]).all() and not self.frozen:
                request().extentions['target'].get_target(self.IsLaunchedByPlayer).kill()
                request()._items.pop(request()._items.index(self))
                self.loc = self.goal
                return pygame.Surface((1, 1)), (0, 0)
            return self.s, self._loc
        return self.s, self._loc

    def get_goal(self):
        self.goal = self.get()

    def get(self):
        answer = request().extentions['target'].get_target(self.IsLaunchedByPlayer)
        if hasattr(answer, 'IsNull'):
            return self.freeze()
        return answer.target - (np.array(self.s.get_size())/2)

    def freeze(self):
        self.frozen = True
        return self._loc
