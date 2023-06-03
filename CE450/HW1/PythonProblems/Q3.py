def sumOfTwoSmallest(a: int, b: int, c: int, d: int) -> int:
    arr = [a, b, c, d]
    arr.sort(reverse=True)
    return arr[-1] ** 2 + arr[-2] ** 2

if __name__ == "__main__":
    print(sumOfTwoSmallest(1, 2, 3, 4))
    print(sumOfTwoSmallest(-3, 1, 5, 6))