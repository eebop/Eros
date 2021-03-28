import numpy as np
class color:
    def __init__(self):
        self.colors = np.random.random_sample((2, 3)) * 255
        print(self.colors)

    def __getitem__(self, key):
        try:
            int(key)
        except:
            raise TypeError("%s cannot be cast to int" % key)
        else:
            return self.colors[int(key)]

    def enabled(self):
        return False
