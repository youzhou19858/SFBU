def sum_odd(N) -> int:
    if isinstance(N, int):
        if N > 0:
            return sum([i for i in range(1, N + 1) if i % 2 > 0])
        else:
            print('Since you entered a negative number, the sum of all odd numbers less than or equal to it will be negative infinity.')
    else:
        while True:
            try:
                return sum_odd(int(N))
            except ValueError:
                N = input('Input should be a positive integer. Please re-enter: ')

if __name__ == "__main__":
    print(sum_odd(6))
    print(sum_odd(7))
    print(sum_odd('22'))
    print(sum_odd('gibberish'))
    print(sum_odd('-5'))