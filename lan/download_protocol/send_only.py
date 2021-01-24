import socket
import pygame
from lan.download_protocol import get_local_address
import zlib


class send:
    def __init__(self, port):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.bind((get_local_address(), port))
        self.sender.listen(1)
        self.clientsocket, (self.other_address, self.other_address_bytecode) = self.sender.accept()




    def send(self, obj):
        #self.clientsocket.send(bytes(chr(len(data)), "utf-8"))
        #self.clientsocket.send(data)
        data = zlib.compress(pygame.image.tostring(obj, 'RGB'))
        print(len(data), chr(len(data)), len(chr(len(data))))
        self.clientsocket.send(bytes(chr(len(data)), 'utf-8'))
        self.clientsocket.send(data)


# if __name__ == '__main__':
#     print('here')
#     s = send(1025)
#     s.send((46, 93, (2.01, True), print))
