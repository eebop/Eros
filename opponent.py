from player import player
from base import request
class opponent(player):
    def __init__(self):
        player.__init__(self, False, (200, 400), 180)

    def update(self, time, data):
        self.target = self.loc + np.array(self.image_now.get_size())/2
        self.move(request().double_socket.recive(False))
        return self.image_now, list(self.loc)
