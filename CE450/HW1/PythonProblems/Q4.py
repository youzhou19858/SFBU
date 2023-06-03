from collections import deque

def df(a, b, c) -> bool:
    while True:
        try:
            dq = deque([int(a), int(b), int(c)])
            for _ in range(3):
                target = dq.popleft()
                if abs(dq[0] - dq[1]) == abs(target):
                    return True
                dq.append(target)
            return False
        except ValueError:
            [a, b, c, *rest] = input('Please enter only 3 integers. Please re-enter in a comma separated way(e.g. 3,-2,1): ').split(',')

if __name__ == "__main__":
    print(df(5, 3, 2))       # 5 - 3 is 2
    print(df(2, 3, 5))       # 5 - 3 is 2
    print(df(2, 5, 3))       # 5 - 3 is 2
    print(df(-2, 3, 5))      # 3 - 5 is -2
    print(df(-5, -3, -2))    # -5 - -2 is -3
    print(df(-2, 3, -5))     # -2 - 3 is -5
    print(df(2, 3, -5))
    print(df(10, 6, 4))
    print(df(10, 6, 3))
    print(df('bbbbb', '1231', 'aaaa'))
