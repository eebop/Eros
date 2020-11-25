from base import base, request
from images.explosions import all_ex
import pygame

class explosions(all_ex.all_im):
    def kill(self):
        request()._items.pop(request()._items.index(self))
