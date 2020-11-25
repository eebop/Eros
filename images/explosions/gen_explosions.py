import os
import sys
x = int(sys.argv[1])
for loc in range(x+1, 100):
    os.system(f'cp poco{x}.png poco{loc}.png')
