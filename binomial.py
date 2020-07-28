import math
import matplotlib.pyplot as plt
from probablity import Probablity
# Binomial probablity class
import random
import numpy as np

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

    def graph(self, n):
        plt.figure(num='Bernouli Distribution')
        plt.xlabel('Number of heads')
        plt.ylabel('probability of success')
        probs = []
        ks = []
        sum = 0
        for k in range(n+1):
            sum += self.probablityofsuccess(n, k)
            probs.append(self.probablityofsuccess(n, k))
            ks.append(k)
            print(k, ':', self.probablityofsuccess(n, k))

        plt.plot(ks, probs)
        plt.show()

    def runAndGraph(self, n):
        x_axis = np.arange(n+1)
        result = np.zeros(n+1)
        plt.figure(num='Flipping a coin 10 times, for 10,000 trials')
        plt.xlabel('Number of heads')
        plt.ylabel('Number of heads after ten flips')
        for i in range(10000):
            sum = 0
            for j in range(n):
                sum += random.randint(0,1)
            result[sum] += 1
        print(result)
        plt.plot(x_axis, result)
        plt.show()

flipCoin = Binomial(0.5)
flipCoin.runAndGraph(10)
flipCoin.graph(10)
# print(flipCoin.probablityofsuccess(5,2))
#size = 3
#print("Probablity of getting k heads after", size, "coin flips")
# flipCoin.graph(size)
