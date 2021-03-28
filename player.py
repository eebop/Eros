from base import base, request
import pygame
import numpy as np
import math
from norm_keys_wrapper import norm_keys_wrapper
import os
import time

class player(base, norm_keys_wrapper):
    def __init__(self, isplayer=True, location=(600,400), degrees=180):
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'poco3.png'))
        if not location:
            self.loc = np.array([400, 400], dtype=float)
        else:
            self.loc = np.array(location, dtype=float)
        self.location = None # To placate move.move
        self.degrees = degrees
        self.isplayer = isplayer
        self.update_movement()
        self.w = False
        self.a = False
        self.d = False
        self.f = False
        self.data = 'Middleweight\nHeat: %s%% of max'
        self.respond_data = [10]
        norm_keys_wrapper.__init__(self)
        color = request().extentions['color'][isplayer]
        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                if self.image.get_at_mapped((x, y)) != 0x000000:
                    self.image.set_at((x, y), color)


        self.missile_loc = False
        self.target = list(reversed(self.loc + np.array(self.image_now.get_size())/2))
        self.last_shot = 2
        self.time = 0



    def update_movement(self):
        radians = math.pi/180 * self.degrees
        self.movement = [math.cos(radians), math.sin(radians)]
        self.movement *= np.array([2, -2])
        self.image_now = pygame.transform.rotate(self.image, self.degrees - 90)

    def update(self, time, data):
        self.target = self.loc + np.array(self.image_now.get_size())/2
        self.move(data)
        return self.image_now, list(self.loc)

    def move(self, data):
        if data != None:
            for event in data:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.f = True

        self.run(None, data)

    def _update(self):
        self.w, self.s, self.a, self.d = self.running_events
        if self.w == True:
            self.loc += self.movement * 1

        if self.a == True:
            self.degrees += 2
            self.update_movement()

        if self.d == True:
            self.degrees -= 2
            self.update_movement()

        if self.f == True and (time.time() - self.last_shot) > .5:
            request()._items.append(request().get_item('missile', self.loc.copy() + (np.array([[0, self.image_now.get_size()[0]*2][self.missile_loc], self.image_now.get_size()[1]])/2), self.isplayer))
            self.missile_loc = not self.missile_loc
            self.last_shot = time.time()
        self.f = False
        self.time = time.time()


    def kill(self):
        request()._items.append(request().get_item('explosions', loc=self.loc, rot=self.degrees-90))
        request()._items.pop(request()._items.index(self))
        self.image = pygame.Surface((1,1))
        request().player_killed(self.isplayer)
