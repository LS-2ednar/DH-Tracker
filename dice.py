import numpy as np

class Dice:
    def __init__(self):
        self.sides = 12

    def roll(self):
        return np.random.randint(1,self.sides+1)


class DualityDye:
    def __init__(self):
        self.hope = Dice()
        self.fear = Dice()
        self.last_hope = None
        self.last_fear = None

    def roll(self):

        hope_roll, fear_roll = self.hope.roll(), self.fear.roll()
        if hope_roll > fear_roll:
            return (hope_roll+fear_roll,"Hope")
        else:
            return (hope_roll+fear_roll,"Fear")

class nDice:
    def __init__(self, sides=0):
        if sides == 0:
            raise ValueError("Your Dice needs a number of sides")
        else:
            self.sides = sides