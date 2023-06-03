from math import sqrt, floor

def maxFactor(N: int) -> int:
    for fac in range(N - 1, floor(sqrt(N)), -1):
        if N % fac == 0:
            return fac
    return 1

if __name__ == "__main__":
    print(maxFactor(15))
    print(maxFactor(80))
    print(maxFactor(27))
    print(maxFactor(220))
    print(maxFactor(124))
    print(maxFactor(79))
    print(maxFactor(51))
    print(maxFactor(22))