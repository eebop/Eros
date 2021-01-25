import socket
#import pickle
import zlib
import pygame

class recive:
    def __init__(self, address, port, issurface):
        self.address, self.port = address, port
        self.reciver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.reciver.connect((address, port))
        self.issurface = issurface



    def recive(self):
        num_bytes = ord(self.reciver.recv(4).decode('utf-8'))
        data = []
        for _ in range(num_bytes):
            data.append(self.reciver.recv(1).decode('utf-8'))
        value = ''.join(data)
        if self.issurface:
            return pygame.image.fromstring(zlib.decompress(value), (800, 800), 'RGB')
        else:
            return pickle.loads(value.decode('utf-8'))
