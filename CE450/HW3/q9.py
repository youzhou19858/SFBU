from typing import List
from operator import add, mul, sub


def fold(f, arr: List, v):
    if not arr:
        return v
    ret = f(v, arr[0])
    for i in range(1, len(arr)):
        ret = f(ret, arr[i])
    return ret


if __name__ == '__main__':
    print(fold(sub, [3, 2, 1], 0))
    print(fold(add, [3, 2, 1], 0))
    print(fold(mul, [3, 2, 1], 1))
    print(fold(sub, [], 100))
