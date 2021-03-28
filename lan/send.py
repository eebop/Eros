'''buit on top of download_protocol
can recive too
'''

from lan.download_protocol import recive_only, send_only
import time
import sys
import os

class send(send_only, recive_only):
    def __init__(self, port=10998):
        send_only.__init__(self, port)
        done = False
        count = 1
        while (not done) and count != 20:
            try:
                recive_only.__init__(self, self.other_address, port+1)
                done = True
            except ConnectionRefusedError:
                if 'DEBUG' in os.environ.keys():
                    print('Connection refused... Trying again (try number %s/20)'%count)
                time.sleep(.1)
                count += 1
        if count == 20:
            sys.exit('Internal Error: secondary conection failed too many times')

def _test():
    s = send(1025)
    print(s.recive())
    s.send(421.05)

if __name__ == '__main__':
    _test()
