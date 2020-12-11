import socket
import pickle
import os

class recive:
    def __init__(self, address, channel):
        self.address, self.channel = address, channel
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((address, channel))


    def recive(self):
        num_bytes = ord(self.s.recv(1))
        data = []
        for _ in range(num_bytes):
            data.append(self.s.recv(1))
        value = b''.join(data)
        return pickle.loads(value)


if __name__ == '__main__':
    r = recive('192.168.1.10', 1025)
    print(r.recive())
