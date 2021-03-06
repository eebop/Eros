import socket
import pygame
from lan.download_protocol import get_local_address
import zlib
import pickle


class send:
    def __init__(self, port):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.bind((get_local_address(), port))
        self.sender.listen(1)
        self.clientsocket, (self.other_address, self.other_address_bytecode) = self.sender.accept()




    def send(self, obj):
        if type(obj) == pygame.Surface:
            data = zlib.compress(pygame.image.tostring(obj, 'RGB'))
        else:
            data = pickle.dumps(obj)
        size = bytes(chr(len(data)), 'utf-8')
        self.clientsocket.send(bytes(chr(len(size)), 'utf-8'))
        self.clientsocket.send(size)
        self.clientsocket.send(data)
