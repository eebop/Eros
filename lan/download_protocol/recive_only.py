import socket
import pickle
import zlib
import pygame

class recive:
    def __init__(self, address, port):
        self.address, self.port = address, port
        self.reciver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.reciver.connect((address, port))


    def recive(self, issurface=True):
        num_num_bytes = ord(self.reciver.recv(1))
        num_bytes = ord(self.reciver.recv(num_num_bytes).decode('utf-8'))
        data = []
        for _ in range(num_bytes):
            data.append(self.reciver.recv(1))
        value = b''.join(data)
        if issurface:
            return pygame.image.fromstring(zlib.decompress(value), (800, 800), 'RGB')
        else:
            return pickle.loads(value)
