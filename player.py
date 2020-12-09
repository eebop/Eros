from base import base, request
import pygame
import numpy as np
import math
from lan import move_as_computer

class player(base):
    def __init__(self, isplayer, location=None):
        self.image = pygame.image.load('/Users/kieran/Documents/python_projects/Eros/images/poco3.png')
        self.data = '''0x4b (standerd version)
crew: %s
excess heat: %s (%s%% of normal)'''
        self.image_now = self.image
        if not location:
            self.loc = np.array([400, 400], dtype=float)
        else:
            self.loc = np.array(location, dtype=float)
        self.degrees = 90
        self.isplayer = isplayer
        self.update_movement()
        self.w = False
        self.a = False
        self.d = False
        self.f = False

        self.missile_loc = False
        self.target = list(reversed(self.loc + np.array(self.image_now.get_size())/2))


    def update_movement(self):
        radians = math.pi/180 * self.degrees
        self.movement = [math.cos(radians), math.sin(radians)]
        self.movement *= np.array([1, -1]) * 2
        self.image_now = pygame.transform.rotate(self.image, self.degrees - 90)

    def update(self, time, data):
        self.target = self.loc + np.array(self.image_now.get_size())/2
        if self.isplayer:
            self.move(data)
        else:
            move_as_computer(self)
        return self.image_now, list(self.loc)

    def move(self, data):
        if data != None:
            self.w = False
            self.a = False
            self.d = False
            self.f = False
            for event in data:
                if event.type == pygame.TEXTINPUT:
                    if event.text == 'w':
                        self.w = True


                    if event.text == 'a':
                        self.a = True

                    if event.text == 'd':
                        self.d = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_f:
                        self.f = True

        self.run_with_data()

    def run_with_data(self):
        if self.w == True:
            self.loc += self.movement * 1

        if self.a == True:
            self.degrees += 2
            self.update_movement()

        if self.d == True:
            self.degrees -= 2
            self.update_movement()

        if self.f == True:
            self.f = False
            request()._items.append(request().get_item('missile', self.loc.copy() + (np.array([[0, self.image_now.get_size()[0]*2][self.missile_loc], self.image_now.get_size()[1]])/2), self.isplayer))
            self.missile_loc = not self.missile_loc

    def kill(self):
        request()._items.append(request().get_item('explosions', loc=self.loc, rot=self.degrees-90))
        request()._items.pop(request()._items.index(self))
        self.image=pygame.Surface((1,1))
