import sys
from base import base, request
import pygame


class target:
    def __init__(self):
        self.number = 0

    def run(self, screen, data):
        if data:
            for event in data:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.number += 1
                    if event.key == pygame.K_b:
                        self.number -= 1

    def get_target(self, IsLaunchedByPlayer):
        try:
            answer = [x for x in request()._items if base in type(x).__bases__ and IsLaunchedByPlayer!=x.isplayer] + [request().get_item('empty')]
            if not answer:
                return request().get_item('empty')
            else:
                self.number = self.number % len(answer)
                return answer[self.number]
        except IndexError:
            return request().get_item('empty')

    def enabled(self):
        return True
