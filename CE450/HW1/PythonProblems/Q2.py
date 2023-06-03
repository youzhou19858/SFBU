def sum_odd(N: int) -> int:
    return sum([i for i in range(1, N + 1) if i % 2 > 0])

if __name__ == "__main__":
    print(sum_odd(6))
    print(sum_odd(7))