import random
def move_as_computer(self):
    lis = [True, False, False, False]
    random.shuffle(lis)
    self.w, self.a, self.d, self.f = lis
    self.run_with_data()
