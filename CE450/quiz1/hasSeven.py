def hasSeven(n: int) -> bool:
    n = abs(n)
    return n != 0 and (n % 10 == 7 or hasSeven(n // 10))


if __name__ == '__main__':
    print(hasSeven(3))
    print(hasSeven(7))
    print(hasSeven(2734))
    print(hasSeven(2634))
    print(hasSeven(734))
    print(hasSeven(777))
    print(hasSeven(-777))
    while True:
        try:
            num = int(input('Please enter a number: '))
            print(f'hasSeven({num}): {hasSeven(num)}')
        except ValueError:
            print('Please enter a valid number!')
