import socket
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 10998))
s.listen(1)

file = open('/tmp/ErosPickle', 'wb')


def send(clientsocket, obj):
    data = pickle.dumps(obj)
    clientsocket.send(bytes(chr(len(data)), "utf-8"))
    clientsocket.send(data)


clientsocket, address = s.accept()

send(clientsocket, (46, 93, (2.01, True), send))
file.close()
os.system('rm /tmp/ErosPickle')
