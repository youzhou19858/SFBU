
def fancyPrint(n: int) -> None:
    def func(k: int) -> None:
        for i in range(k):
            if (i % n == 0):
                print('Buzz!')
            else:
                print(i)
    return func


if __name__ == '__main__':
    rangeDivisibleByN = fancyPrint(5)
    rangeDivisibleByN(10)
