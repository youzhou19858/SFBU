from sys import maxsize
from Q6 import sumOfProperFactors

def theImmediateAmicableNumGreaterThan(n: int) -> int:
    for i in range(n + 1, maxsize):
        sumOfProperFactorsOfI = sumOfProperFactors(i)
        if i != sumOfProperFactorsOfI and i == sumOfProperFactors(sumOfProperFactorsOfI):
            return i
    
if __name__ == "__main__":
    print(theImmediateAmicableNumGreaterThan(5))
    print(theImmediateAmicableNumGreaterThan(220))
    print(theImmediateAmicableNumGreaterThan(284))
    print(theImmediateAmicableNumGreaterThan(5000))