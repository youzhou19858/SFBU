def sameNumOfBits(a: int, b: int) -> bool:
    def cntBits(n: int, bitCnt: int = 0) -> int:
        while (n):
            bitCnt += n & 1
            n >>= 1
        return bitCnt
    return cntBits(a) == cntBits(b)

def sameNumOfDigits(a: int, b: int) -> bool:
    def cntDigits(n: int, digitCnt: int = 0) -> int:
        while (n):
            digitCnt += 1
            n //= 10
        return digitCnt
    return cntDigits(a) == cntDigits(b)

if __name__ == "__main__":
    print(sameNumOfBits(50, 70), bin(50), bin(70))
    print(sameNumOfBits(50, 100), bin(50), bin(100))
    print(sameNumOfBits(1000, 100000), bin(1000), bin(100000))
    print(sameNumOfDigits(50, 70))
    print(sameNumOfDigits(50, 100))
    print(sameNumOfDigits(1000, 100000))