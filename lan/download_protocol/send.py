import socket
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(input('enter channel: '))))
s.listen(1)



def send(clientsocket, obj):
    data = pickle.dumps(obj)
    clientsocket.send(bytes(chr(len(data)), "utf-8"))
    clientsocket.send(data)


clientsocket, address = s.accept()

send(clientsocket, (46, 93, (2.01, True), send))
