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
            answer = zlib.decompress(value)
            return pygame.image.fromstring(answer, (800, 800), 'RGB')
        else:
            return pickle.loads(value)

    def _close(self, s):
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except OSError:
            pass

    def close(self, force=False):
        self._close(self.reciver)
        if hasattr(self, 'sender'):
            self._close(self.sender)
        if force:
            self = None
