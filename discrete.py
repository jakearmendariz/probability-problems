import math
from probablity import Probablity
# Discrete Random Variable probablity class


class Discrete(Probablity):
    def __init__(self):
        self.values = []
        pass

    def addOption(self, x, probablity):
        self.values.append((x, probablity))

    def valid(self):
        total = 0
        # All probablities should add up to exactly 1
        for var, prob in self.values:
            total += prob

        # Round to the nearest 100th, becuase python is weird
        total = round(total, 2)
        if total == 1:
            return True
        else:
            return False

    def probablityofsuccess(self, x):
        for value, prob in self.values:
            if(value == x):
                return prob
        # If it is not once of discrete variables then it is a probablity of 0
        return 0

    # Var(X) = E(X^2)-E^2(X)
    def variance(self):
        total = 0
        for value, prob in self.values:
            total += prob*(value**2)
        total -= self.expected()**2
        total = round(total, 2)
        return total

    # E(X) = Sum[all values](k*probalityof(k))
    def expected(self):
        total = 0
        for value, prob in self.values:
            total += prob*value
        return total

    def printTable(self):
        for value, prob in self.values:
            print(value, ':', prob)
        return


#bachelor = Discrete()
#bachelor.addOption(0, 0.1)
#bachelor.addOption(1, 0.2)
#bachelor.addOption(3, 0.4)
#bachelor.addOption(4, 0.2)
#bachelor.addOption(5, 0.1)
# bachelor.printTable()
# print(bachelor.expected())
