def sumOfTwoSmallestSquared(a = 0, b = 0, c = 0, d = 0) -> int:
    while True:
        try:
            arr = [int(a), int(b), int(c), int(d)]
            arr.sort(reverse=True)
            return arr[-1] ** 2 + arr[-2] ** 2
        except ValueError:
            [a, b, c, d, *rest] = input('Please enter 4 valid integers in a comma separated manner(e.g. 4,2,-1,9): ').split(',')

if __name__ == "__main__":
    print(sumOfTwoSmallestSquared(1, 2, 3, 4))
    print(sumOfTwoSmallestSquared(-3, 1, 5, 6))
    print(sumOfTwoSmallestSquared('ddd'))