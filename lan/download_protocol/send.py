import socket
import pickle
import os

adr = '192.168.1.10'#input('enter address')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 10999))
s.listen(1)

file = open('/tmp/ErosPickle', 'wb')

def send(clientsocket, obj):
    data = pickle.dumps(obj, 4)
    clientsocket.send(bytes(chr(len(data)), "utf-8"))
    clientsocket.send(data)

clientsocket, address = s.accept()

send(clientsocket, (46, 93, (2.01, True), send))
file.close()
os.system('rm /tmp/ErosPickle')
