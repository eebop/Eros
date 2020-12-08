import importlib
import pygame
import time
import sys

class Framework:
    def __init__(self):
        self.extentions = {'screen_data': self.get_item("screen_data"), 'target': self.get_item('target')}
        self._extention_data = {}
        self.setup_rockets()

    def _request(self, name):
        return getattr(sys.modules[self._main_name], name)

    def setup_rockets(self):
        self._items = [self.get_item("player", True), self.get_item("player", False, [0, 0]), self.get_item("player", False, [100, 300])]

    def get_item(self, name, *data, **kwdata):
        if not name in sys.modules:
            importlib.import_module(name)
        return getattr(sys.modules[name], name)(*data, **kwdata)

    def run(self, screen):
        t = time.time()
        should_check = 0
        while True:
            while not time.time() - .05 >= t:
                pass
            t = time.time()
            should_check += 1
            if should_check == 4:
                e = pygame.event.get()
                sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in e]) else None
                should_check = 0
            else:
                e = None
            screen.blits([x.update(t, e) for x in self._items])
            [x.run(screen, e) for x in self.extentions.values() if x.enabled()]
            pygame.display.flip()
            screen.fill((32, 32, 32))
