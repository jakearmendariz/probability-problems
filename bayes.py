# Very limited
# Finds the probably of Hypothesis, given evidence
# Requires P(Hypothesis), P(Evidence, assuming hypothesis is true), P(Evidence, assuming hypothesis is false)


class bayes:
    def __init__(self, pH, pE_H, pE_Hnot):
        self.pH = pH
        self.pE_H = pE_H
        self.pE_Hnot = pE_Hnot
        pass

    def calculate(self):
        top = self.pE_H * self.pH
        bottom = self.pE_H * self.pH + self.pE_Hnot * self.pE_Hnot
        return top/bottom
