import sys
from base import base, request


class target:
    def __init__(self):
        pass

    def run(self, screen, data):
        pass

    def get_target(self, IsLaunchedByPlayer):
        try:
            answer = [x for x in request()._items if base in x.__class__.__bases__]
            if len(answer) == 2:
                return answer[IsLaunchedByPlayer]
            elif len(answer) == 1:
                if answer[0].isplayer != IsLaunchedByPlayer:
                    return answer[0]
                else:
                    return request().get_item('empty')
            elif len(answer) == 0:
                return request().get_item('empty')
        except IndexError:
            return request().get_item('empty')

    def enabled(self):
        return True
