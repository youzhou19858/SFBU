from math import sqrt, ceil


def abndnt(n: int) -> None:
    cnt = 0
    for i in range(1, ceil(sqrt(n))):
        if (n % i == 0):
            print(f"{i} * {n // i}")
            cnt += (i + (n // i))
    print((cnt - n) > n)


if __name__ == '__main__':
    for i in range(12, 26, 2):
        print(f"abndnt({i})")
        abndnt(i)
