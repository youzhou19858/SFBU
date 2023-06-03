def sameNumOfBits(a, b) -> bool:
    def cntBits(n: int, bitCnt: int = 0) -> int:
        while (n):
            bitCnt += n & 1
            n >>= 1
        return bitCnt
    while True:
        try:
            return cntBits(abs(int(a))) == cntBits(abs(int(b)))
        except ValueError:
            [a, b, *rest] = input('Please enter two integers in comma separated manner(e.g. 8,9): ').split(',')

def sameNumOfDigits(a, b) -> bool:
    def cntDigits(n: int, digitCnt: int = 0) -> int:
        while (n):
            digitCnt += 1
            n //= 10
        return digitCnt
    while True:
        try:
            return cntDigits(abs(int(a))) == cntDigits(abs(int(b)))
        except ValueError:
            [a, b, *rest] = input('Please enter two integers in comma separated manner(e.g. 8,9): ').split(',')


if __name__ == "__main__":
    print(sameNumOfBits(50, 70), bin(50), bin(70))
    print(sameNumOfBits(50, 100), bin(50), bin(100))
    print(sameNumOfBits(1000, 100000), bin(1000), bin(100000))
    print(sameNumOfBits('aaaa', 'bbb'))
    print(sameNumOfDigits(50, 70))
    print(sameNumOfDigits(50, 100))
    print(sameNumOfDigits(1000, 100000))
    print(sameNumOfDigits('aaaa', 'bbb'))
