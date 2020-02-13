import math
from probablity import Probablity
# Geometric Random Variable probablity class


class Geometric(Probablity):
    def __init__(self, p):
        self.probablity = p
        pass

    # p(1-p)^k-1
    def probabilityofsuccess(self, k):
        a = (1-self.probablity)**(k-1)
        return self.probablity*a

    def pmf(self, k):
        a = (1-self.probablity)**(k-1)
        return self.probablity*a

    def cdf(self, n):
        a = (1-self.probablity)**(n)
        return 1 - a

    # Var(X) = E(X^2)-E^2(X)
    def variance(self):
        return (1-self.probablity)/(self.probablity**2)

    # E(X) = Sum[all values](k*probalityof(k))
    def expected(self):
        return 1/self.probablity


#dice = Geometric(1/6)
# print(dice.probabilityofsuccess(6))
