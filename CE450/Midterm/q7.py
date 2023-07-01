from math import log2, pow, ceil, floor


def nearestTwo(x: float) -> float:
    if (x < 0):
        print("Please only use positive number")
    else:
        logVal = log2(x)
        lb = pow(2, floor(logVal))
        ub = pow(2, ceil(logVal))
        return lb if x - lb < ub - x else ub


if __name__ == "__main__":
    print(nearestTwo(8))
    print(nearestTwo(11.5))
    print(nearestTwo(12))
    print(nearestTwo(14))
    print(nearestTwo(2019))
    print(nearestTwo(0.1))
    print(nearestTwo(0.75))
    print(nearestTwo(1.5))
