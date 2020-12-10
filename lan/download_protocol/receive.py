import socket
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 10999))

os.system('mkfile 0 /tmp/ErosUnpickle')
file = open('/tmp/ErosUnpickle', 'rb')

def recive(socket):
    num_bytes = ord(socket.recv(1))
    data = []
    for _ in range(num_bytes):
        data.append(socket.recv(1))
    value = b''.join(data)
    return pickle.loads(value, 4)

def send():
    pass

print(recive(s))

file.close()

os.system('rm /tmp/ErosUnpickle')
