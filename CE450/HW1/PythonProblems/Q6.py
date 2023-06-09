from math import sqrt, floor

def sumOfProperFactors(N: int) -> int:
    sumOfFactors = 0
    for fac in range(N - 1, floor(sqrt(N)), -1):
        if N % fac == 0:
            sumOfFactors += (fac + N // fac)
    return sumOfFactors + 1

def isPerfectNumber(N) -> int:
    while True:
        try:
            N = int(N)
            if (N < 0):
                print('Perfect Number can only be positive.')
                return False
            return sumOfProperFactors(N) == N
        except ValueError:
            N = input('Please enter a valid positive integer: ')

if __name__ == "__main__":
    print(isPerfectNumber(6))
    print(isPerfectNumber(28))
    print(isPerfectNumber(496))
    print(isPerfectNumber(8128))
    print(isPerfectNumber(33550336))
    print(isPerfectNumber(8))
    print(isPerfectNumber(22))
    print(isPerfectNumber('aaaaa'))