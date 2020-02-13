import math
from discrete import Discrete
# Poisson Random Variable probablity class


class Poisson(Discrete):

    def __init__(self, arrival_rate):
        # lmba bc lambda is a reserved word in python
        self.lmbda = arrival_rate
        # Creates the values array so this class can have a table displaying possion distribution
        super().__init__()
        pass

    # probablity of k occurences in t time
    def probablity_of_k_in_t(self, t, k):
        top = (self.lmbda*t)**k
        bottom = math.factorial(k)
        side = math.exp(-1*self.lmbda*t)

        return (top*side)/bottom

    # This is the pmf!
    # probablity that k things happen, when it there is an average of lambda occurences
    def probablity_of_k_arrivals(self, k):
        top = (self.lmbda)**k
        bottom = math.factorial(k)
        side = math.exp(-1*self.lmbda)

        return (top*side)/bottom

    def pmf(self, k):
        return self.probablity_of_k_arrivals(k)

    def expected(self):
        return self.lmbda

    def variance(self):
        return self.lmda

    def createTable(self):
        for i in range(15):
            prob = self.pmf(i)
            self.addOption(i, prob)
            if(prob < .001):
                break
        return


decay = Poisson(4.6)
decay.createTable()
# decay.printTable()
