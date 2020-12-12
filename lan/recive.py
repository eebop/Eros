'''buit on top of download_protocol
can send too
'''

from download_protocol import recive_only, send_only

class recive(recive_only, send_only):
    def __init__(self, address, channel=10998):
        recive_only.__init__(self, address, channel)
        send_only.__init__(self, channel+1)

def _test():
    r = recive('127.0.0.1', 1025)
    r.send('hi')
    print(r.recive())


if __name__ == '__main__':
    _test()
