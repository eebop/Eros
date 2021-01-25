import importlib
import pygame
import time
import sys
import lan

class Framework:
    def __init__(self):
        self.extentions = {'screen_data': self.get_item("screen_data"), 'target': self.get_item('target')}
        self.absolute_extentions = {}
        self._extention_data = {}
        self.move_extention = self.get_item('move')
        self.setup_rockets()

    def setup_rockets(self):
        self._items = [self.get_item("player", True), self.get_item("opponent", False, [100, 0])]

    def get_item(self, name, *data, **kwdata):
        if not name in sys.modules:
            importlib.import_module(name)
        return getattr(sys.modules[name], name)(*data, **kwdata)

    def run(self, screen, double_socket):
        self.double_socket = double_socket
        t = time.time()
        self.should_check = 0
        while True:
            t, e = self.run_normal(t)
            move = self.move_extention.run(screen, e)
            screen.blits([(image, move+location) for image, location in [x.update(t, e) for x in self._items]])
            [x.run(screen, e) for x in self.extentions.values() if x.enabled()]
            pygame.display.flip()
            self.double_socket.send(screen)
            screen.fill((32, 32, 32))

    def run_normal(self, t):
        while not time.time() - .05 >= t:
            pass
        t = time.time()
        self.should_check += 1
        if self.should_check == 4:
            e = pygame.event.get()
            sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in e]) else None
            self.should_check = 0
        else:
            e = None
        return t, e
