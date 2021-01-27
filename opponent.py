from player import player
from base import request
import numpy as np
from select import select

class opponent(player, base):
    def __init__(self):
        player.__init__(self, False, (200, 400), 0)

    def update(self, time, data):
        self.target = self.loc + np.array(self.image_now.get_size())/2
        double_socket = request().double_socket
        if select([double_socket.reciver], [], [], 0)[0]:
            move_data = double_socket.recive(False)
        else:
            move_data = None
        self.move(move_data)
        return self.image_now, list(self.loc)
