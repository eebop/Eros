'''buit on top of download_protocol
can recive too
'''

from lan.download_protocol import recive_only, send_only
import time

class send(send_only, recive_only):
    def __init__(self, port=10998):
        print('here, port is', port)
        send_only.__init__(self, port)
        time.sleep(1) # buffer time so recive() isn't called before send() (in send module)
        recive_only.__init__(self, self.other_address, port+1)

def _test():
    s = send(1025)
    print(s.recive())
    s.send(421.05)

if __name__ == '__main__':
    _test()
