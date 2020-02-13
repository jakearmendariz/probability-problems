# Continuous Random Variable
# Add in a string of the integrated version of pdf


class Continuous:
    def __init__(self, pdf_str):
        self.pdf_str = pdf_str
        pass

    def plugIn(self, value):
        val = str(value)
        val = self.pdf_str.replace('x', val)
        return eval(val)

    def pdf(self, lowerbound, upperbound):
        return self.plugIn(upperbound) - self.plugIn(lowerbound)

    def F(self, x):
        return self.pdf(-10000, x)


prob = Continuous("3*x*x+2*x")
#print(prob.pdf(10, 2))
