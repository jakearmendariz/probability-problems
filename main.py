from binomial import Binomial
from exponential import Exponential
from geometric import Geometric
from poisson import Poisson
from discrete import Discrete
from continuous import Continuous

user = ''
while(user != 'q' and user != 'quit'):
    problem = input("What type of random variable\n")
    prompt = "Preform what operation: expected, variance"
    if problem == 'q':
        break
    elif(problem == "binomial"):
        probability = float(input("What is the probability?\n"))
        problem = Binomial(probability)
        prompt += ", probablityofsuccess(n,k)"
        prompt += ", printTable"
    elif problem == "exponential":
        probability = float(input("What is the lambda?\n"))
        problem = Exponential(1/2)
    elif problem == "poisson":
        probability = float(input("What is the lambda?\n"))
        problem = Poisson(probability)
        prompt += ", probablityofsuccess(n,k)"
        prompt += ", printTable"
    elif problem == "discrete":
        probability = float(input("What is the probability?\n"))
        problem = Discrete(probability)
    elif problem == "geometric":
        probability = float(input("What is the probability?\n"))
        problem = Geometric(probability)
    elif problem == "continuous":
        probability = float(input("What is the probability?\n"))
        problem = Continuous(probability)
    else:
        print("Not an option")
        continue
    prompt += '\n'
    while(user != 'q'):
        user = input(prompt)
        if user == 'expected':
            print(problem.expected())
        elif user == 'variance':
            print(problem.variance())
        elif user == 'printTable':
            problem.printTable(10)
        else:
            print("did not recognize command")
