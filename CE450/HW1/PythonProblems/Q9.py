def cntDistinctDigits(n: int) -> int:
    distinct = set()
    while (n):
        distinct.add(n % 10)
        n //= 10
    return len(distinct)

if __name__ == "__main__":
    print(cntDistinctDigits(8675309))
    print(cntDistinctDigits(1313131))
    print(cntDistinctDigits(13173131))
    print(cntDistinctDigits(10000))
    print(cntDistinctDigits(101))
    print(cntDistinctDigits(10))