'''buit on top of download_protocol
can recive too
'''

from lan.download_protocol import recive_only, send_only
import time

class send(send_only, recive_only):
    def __init__(self, port=10998):
        send_only.__init__(self, port, True)
        done = False
        while not done:
            try:
                recive_only.__init__(self, self.other_address, port+1, False)
                done = True
            except ConnectionRefusedError:
                print('Connection refused... Trying again')
                time.sleep(.1)

def _test():
    s = send(1025)
    print(s.recive())
    s.send(421.05)

if __name__ == '__main__':
    _test()
