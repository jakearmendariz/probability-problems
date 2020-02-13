from continuous import Continuous
import math


class Exponential(Continuous):

    def __init__(self, arrival_rate):
        self.lmbda = arrival_rate
        pass

    def expected(self):
        return 1/self.lmbda

    def variance(self):
        return self.expected()**2

    def pdf(self, x):
        return self.lbmda * math.exp(-1*x*self.lmbda)

    def cdf(self, x):
        return 1 - math.exp(-1*x*self.lmbda)

    def probablity_less_than_x(self, x):
        return self.cdf(x)

    def probablity_greater_than_x(self, x):
        return math.exp(-1*self.lmbda * x)
