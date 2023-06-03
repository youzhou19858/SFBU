from collections import deque

def df(a: int, b: int, c: int) -> bool:
    dq = deque([a, b, c])
    for _ in range(3):
        target = dq.popleft()
        if abs(dq[0] - dq[1]) == abs(target):
            return True
        dq.append(target)
    return False

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
