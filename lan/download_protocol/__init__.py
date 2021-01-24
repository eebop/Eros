import socket
def get_local_address():
    address = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
    s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
    socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    return address

from lan.download_protocol.recive_only import recive as recive_only
from lan.download_protocol.send_only import send as send_only
