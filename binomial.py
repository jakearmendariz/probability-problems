import math
from probablity import Probablity
# Binomial probablity class


class Binomial(Probablity):
    def __init__(self, prob):
        self.probablity = prob
        pass

    def probablityofsuccess(self, n, k):
        a = self.nchoosek(n, k)
        b = self.probablity ** k
        c = (1-self.probablity) ** (n-k)

        return a*b*c

    def variance(self):
        return self.probablity*(1-self.probablity)

    def expected(self):
        return self.probablity

    def printTable(self, n):
        for k in range(n+1):
            print(k, ':', self.probablityofsuccess(n, k))


flipCoin = Binomial(0.5)
# print(flipCoin.probablityofsuccess(5,2))
size = 10
#print("Probablity of getting k heads after", size, "coin flips")
# flipCoin.printTable(size)