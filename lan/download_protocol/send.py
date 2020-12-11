import socket
import pickle
import os


class send:
    def __init__(self, channel):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', channel))
        self.s.listen(1)
        self.clientsocket, self.other_address = self.s.accept()




    def send(self, obj):
        data = pickle.dumps(obj)
        self.clientsocket.send(bytes(chr(len(data)), "utf-8"))
        self.clientsocket.send(data)


if __name__ == '__main__':
    s = send(1025)
    s.send((46, 93, (2.01, True), print))
