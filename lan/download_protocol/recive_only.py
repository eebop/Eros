import socket
#import pickle
import zlib
import pygame

class recive:
    def __init__(self, address, port):
        self.address, self.port = address, port
        self.reciver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.reciver.connect((address, port))


    def recive(self, issurface=True):
        num_bytes = ord(self.reciver.recv(4).decode('utf-8'))
        data = []
        for _ in range(num_bytes):
            data.append(self.reciver.recv(1))
        value = ''.join(data)
        return pygame.image.fromstring(zlib.decompress(value))


if __name__ == '__main__':
    r = recive('192.168.1.6', 1025)
    print(r.recive())
