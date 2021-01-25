'''buit on top of download_protocol
can send too
'''

from lan.download_protocol import recive_only, send_only

class recive(recive_only, send_only):
    def __init__(self, address, port=10998):
        recive_only.__init__(self, address, port, True)
        send_only.__init__(self, port+1, False)

def _test():
    r = recive('192.168.1.6', 1025)
    r.send('hi')
    print(r.recive())


if __name__ == '__main__':
    _test()
