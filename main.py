import numpy as np

class Dice:
    def __init__(self):
        self.sides = 12

    def roll(self):
        return np.randint(1,self.sides)


TEST = Dice()
print(TEST.roll())